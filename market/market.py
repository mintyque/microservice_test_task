from concurrent import futures
import grpc

from market_pb2 import ResponseType, AddResponse, CartResponse
import market_pb2_grpc


"""
Implementation of a Market microservice for a mock-up marketplace.

The service is used to store users' carts. A user can add an item to a cart or
request a cart. User's ID is used as a cart ID.

It is accessed at port 50050 with RPC calls.
"""

carts_dict = {}		# carts are stored in a dict

class MarketService(market_pb2_grpc.MarketServicer):
    def AddItem(self, request, context):
        response_type = ResponseType.OK
        ind = request.cart_id
        iid = request.item_id
        if(ind not in carts_dict):	# if the cart does not exist, create it
            carts_dict[ind] = []
        carts_dict[ind].append(iid)
        print("Added item ", iid, " to cart ", ind)
        return AddResponse(response_token = response_type)

    def RequestCart(self, request, context):
        item_ids = []	# empty array by default for consistency
        if(request.cart_id in carts_dict):	
            item_ids = carts_dict[request.cart_id]
        print("Cart ", request.cart_id, " has ", len(item_ids), " items: ", item_ids)
        return CartResponse(item_amt = len(item_ids), item_id = item_ids)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    market_pb2_grpc.add_MarketServicer_to_server(MarketService(), server)
    server.add_insecure_port("[::]:50050")
    server.start()
    print("started successfully at port 50050")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
