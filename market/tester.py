import grpc

from market_pb2 import AddRequest, CartRequest
from market_pb2_grpc import MarketStub

channel = grpc.insecure_channel("localhost:50050")
client = MarketStub(channel)
requestA = AddRequest(item_id = 1, cart_id = 3)
requestB = AddRequest(item_id = 2, cart_id = 3)
requestC = AddRequest(item_id = 1, cart_id = 2)
requestD = CartRequest(cart_id = 3)
requestE = CartRequest(cart_id = 2)
requestF = CartRequest(cart_id = 4)
respA = client.AddItem(requestA).response_token
respB = client.AddItem(requestB).response_token
respC = client.AddItem(requestC).response_token
respD = client.RequestCart(requestD)
respE = client.RequestCart(requestE)
respF = client.RequestCart(requestF)
print("Push 1 to 3: ", respA)
print("Push 2 to 3: ", respB)
print("Push 1 to 2: ", respC)
print("Get cart 3: ", respD)
print("Get cart 2: ", respE)
print("Get cart 4: ", respF)
