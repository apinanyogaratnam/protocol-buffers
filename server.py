import grpc
import square_root_pb2
import square_root_pb2_grpc
from concurrent import futures


class SquareRootServiceServicer(square_root_pb2_grpc.SquareRootServiceServicer):
    def SquareRoot(self, request, context):
        result = request.input ** 0.5
        return square_root_pb2.Result(result=result)


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    print("Starting server. Listening on port 50051.")
    square_root_pb2_grpc.add_SquareRootServiceServicer_to_server(
        SquareRootServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


main()
