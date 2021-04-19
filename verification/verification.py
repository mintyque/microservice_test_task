from concurrent import futures
import grpc

from verification_pb2 import UserCategory, VerificationResponse
import verification_pb2_grpc


"""
Implementation of a Verification microservice for a mock-up marketplace.

The user can have three roles depending on his id:
0 - RESERVED
1 - CLIENT
2 - ADMIN

If user's provided token is divisible by 3, then the user is ADMIN.
If user's provided token is divisible by 10, then the user is RESERVED.
Else, user is CLIENT.

It is accessed at port 50051 with RPC calls.
"""
class VerificationService(verification_pb2_grpc.VerificationsServicer):
    def Verify(self, request, context):
        int_token = request.user_token
        user_category = UserCategory.CLIENT		# CLIENT by default
        if (int_token % 3 == 0 ):			# check for ADMIN
            user_category = UserCategory.ADMIN
        if (int_token % 10 == 0 ):			# check for RESERVED
            user_category = UserCategory.RESERVED
        print("Received request with category ", user_category)
        return VerificationResponse(category = user_category)	# return 0, 1 or 2


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    verification_pb2_grpc.add_VerificationsServicer_to_server(VerificationService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("started successfully at port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
