Implementation of a microservice test task
Made by Dmitriy Bochkaryov, 2021


Launch details:

The project was made on Ubuntu and is expected to work on Ubuntu.
python3 is needed. venv is provided.
To test the project three terminals are needed, one for each microservice. ./verification/verification.py launches the Verification microservice on port 50051. ./market/market.py launches the Market microservice on port 50050. ./client.py launches the Client on the port 5000.


Implementation details:

The system uses three microservices (Verification, Client and Market) to implement a mock-up of an online marketplace. Verification and Market microservices are implemented using grpc library and Protocol Buffers (protobufs). The Client microservice uses Flask and has a realized API, which will be explained further below.

The system has the following structure:
Verification -> Client <- Market

Verification microservice implements a function Verify() which accepts a request with a user token (int)user_token. It can then return three values depending on the token: if the token is divisible by 3, then the user is an ADMIN and 2 is returned. If the token is divisible by 10, then a grpc-specific case is handled and 0 is returned. In all other cases the user is a CLIENT and 1 is returned.

Market microservice implements a function AddItem() which accepts a request with a user token (int)cart_id and item ID (int)item_id, and a function RequestCart which accepts a request with a user token (int)cart_id. User tokens are used to differentiate between different carts, and users with different tokens can generate their own cart. They are stored in the microservice's runtime memory using a dictionary {(int):(list)}. 
AddItem() adds an item with item_id to a cart using cart_id as a key. It can return two codes: 0 if the item was added succesfully, or 1 if the item could not be added (e.g. it does not exist or user doesn't have a permission), however it is ouside of the test task scope and was not implemented.
RequestCart() returns a cart from the dictionary. The cart is returned as a packed encoding of a list, which can then be depacked using Google packages or represented in string as a list.

Client microservice accepts API calls from the web-client. It communicates with Verification and Market microservices via RPC protocol using grpc. Client microservice implements three function: internal verify() which accepts a user token (int)user_token, external add() which accepts a user token (int)user_token and an item ID (int)item_id, and external get_cart() which accepts a user token (int)user_token.
verify() is used to call the Verification microservice and get a response which determines the type of the user.
add() is used to call the Market microservice's function AddItem() which adds an item to user's cart. It is available at the route "/cart/add" and uses GET and POST methods. Arguments are fetched using request.form. The return message is in JSON format which contains the server response (item ID, cart ID and Market response code).
get_cart() is used to call the Verify() function of a Verification microservice and the RequestCart() function of a Market microservice. It is available at the route "/cart/get" and uses GET method. Arguments are fetched using request.args. The user_token is first passed to verify() function to determine further actions. If a user is a CLIENT, then the cart is passed back to the user wtih HTML code 200. Else, the user gets a message and HTML code 403. The return message is in JSON format which contains the server response (short message, cart ID, number of items and indexes of items).


Example calls and responses

curl -X POST -F 'item_id=1' -F 'user_token=2' localhost:5000/cart/add
{"item_id": 1, "cart_id": 2, "status": 0}

curl -X GET localhost:5000/cart/get?user_token=2
{"msg": "CLIENT", "cart_id": 2, "item_amt": 1, "cart_content": "[1]"}
