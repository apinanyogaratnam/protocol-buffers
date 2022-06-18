import grpc
import square_root_pb2
import square_root_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = square_root_pb2_grpc.SquareRootServiceStub(channel)
        response = stub.SquareRoot(square_root_pb2.Number(input=7))
        print("Response: ", response.number)


if __name__ == '__main__':
    run()
