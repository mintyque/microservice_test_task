import os, sys

from flask import Flask, render_template, request, Response
import json
import grpc

# need to add child directories to path for imports
sys.path.append(os.path.join(sys.path[0],'verification'))
sys.path.append(os.path.join(sys.path[0],'market'))

from verification_pb2 import UserCategory, VerificationRequest
from verification_pb2_grpc import VerificationsStub

from market_pb2 import AddRequest, CartRequest
from market_pb2_grpc import MarketStub


"""
Implementation of a Client mircoservice for a mock-up marketplace.

The service is used for communication with other microservices. It can be used in browser
and can accept curl calls. It is accessible at localhost:5000 when running.
"""

app = Flask(__name__)

# establish connection with Verification
verification_host = os.getenv("VERIFICATIONS_HOST", "localhost")
verification_channel = grpc.insecure_channel(
    f"{verification_host}:50051"
)
verification_client = VerificationsStub(verification_channel)

# establish connection with Market
market_host = os.getenv("MARKET_HOST", "localhost")
market_channel = grpc.insecure_channel(
    f"{market_host}:50050"
)
market_client = MarketStub(market_channel)

@app.route("/")
def render_homepage():
    return("placeholder")

# internal function to verify user's status for fetching a cart
# if user's status is 1, then his cart can be fetched
def verify(cur_token):
    request = VerificationRequest(user_token = cur_token)
    response = verification_client.Verify(request)
    return response.category

# external function for adding item to user's cart
# it requests a form with int fields 'item_id' and 'user_token'
# which are then passed to Market microservice as
# 'item_id' and 'cart_id' respectfully
@app.route("/cart/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        cur_id = int(request.form['item_id'])
        cur_token = int(request.form['user_token'])
        market_request = AddRequest(item_id = cur_id, cart_id = cur_token)
        market_response = market_client.AddItem(market_request)
        response = {"item_id":cur_id, "cart_id":cur_token, "status":market_response.response_token}
        response = json.dumps(response)
        return Response(response = response, status=200, mimetype="application/json")
    return render_template("add_cart.html")

# external function for fetching a user's cart
# it requests int 'user_token' as an argument
# then, the token is verified via Verification microservice
# if return value is 1, cart can be fetched with status 200
# else, user gets message "FORBIDDEN" and server shows status 403
@app.route("/cart/get", methods=['GET'])
def get_cart():
    cur_token = request.args.get('user_token', default = 0, type = int)
    response_msg = "FORBIDDEN"
    cart_content = 0		# initialize return values as 0 for consistency
    item_amt = 0
    status = 403
    verification_response = verify(cur_token)
    if verification_response == 1:	# if user passed the check, prepare a positive response message
        market_request = CartRequest(cart_id = cur_token)
        market_response = market_client.RequestCart(market_request)
        response_msg = "CLIENT"
        item_amt = market_response.item_amt
        cart_content = market_response.item_id
        status = 200
    response = {"msg":response_msg, "cart_id":cur_token, "item_amt":item_amt, "cart_content":repr(cart_content)}
    response = json.dumps(response)
    return Response(response = response, status = status, mimetype="application/json")

