# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import square_root_pb2 as square__root__pb2


class SquareRootServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SquareRoot = channel.unary_unary(
                '/SquareRootService/SquareRoot',
                request_serializer=square__root__pb2.Number.SerializeToString,
                response_deserializer=square__root__pb2.Result.FromString,
                )


class SquareRootServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SquareRoot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SquareRootServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SquareRoot': grpc.unary_unary_rpc_method_handler(
                    servicer.SquareRoot,
                    request_deserializer=square__root__pb2.Number.FromString,
                    response_serializer=square__root__pb2.Result.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SquareRootService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SquareRootService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SquareRoot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SquareRootService/SquareRoot',
            square__root__pb2.Number.SerializeToString,
            square__root__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)