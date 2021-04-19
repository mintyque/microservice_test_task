import grpc

from verification_pb2 import VerificationRequest
from verification_pb2_grpc import VerificationsStub

channel = grpc.insecure_channel("localhost:50051")
client = VerificationsStub(channel)
requestA = VerificationRequest(user_token = 1)
requestB = VerificationRequest(user_token = 3)
requestC = VerificationRequest(user_token = 9)
requestD = VerificationRequest(user_token = 100)
print("Expected 1, received: ", client.Verify(requestA))
print("Expected 2, received: ", client.Verify(requestB))
print("Expected 2, received: ", client.Verify(requestC))
print("Expected 0, received: ", client.Verify(requestD))

