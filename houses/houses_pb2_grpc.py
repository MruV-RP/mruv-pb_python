# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from houses import houses_pb2 as houses_dot_houses__pb2


class MruVHousesServiceStub(object):
    """The MruV houses service provides procedures for managing houses.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateHouse = channel.unary_unary(
                '/mruv.houses.MruVHousesService/CreateHouse',
                request_serializer=houses_dot_houses__pb2.CreateHouseRequest.SerializeToString,
                response_deserializer=houses_dot_houses__pb2.CreateHouseResponse.FromString,
                )
        self.GetHouse = channel.unary_unary(
                '/mruv.houses.MruVHousesService/GetHouse',
                request_serializer=houses_dot_houses__pb2.GetHouseRequest.SerializeToString,
                response_deserializer=houses_dot_houses__pb2.GetHouseResponse.FromString,
                )
        self.UpdateHouse = channel.unary_unary(
                '/mruv.houses.MruVHousesService/UpdateHouse',
                request_serializer=houses_dot_houses__pb2.UpdateHouseRequest.SerializeToString,
                response_deserializer=houses_dot_houses__pb2.UpdateHouseResponse.FromString,
                )
        self.DeleteHouse = channel.unary_unary(
                '/mruv.houses.MruVHousesService/DeleteHouse',
                request_serializer=houses_dot_houses__pb2.DeleteHouseRequest.SerializeToString,
                response_deserializer=houses_dot_houses__pb2.DeleteHouseResponse.FromString,
                )


class MruVHousesServiceServicer(object):
    """The MruV houses service provides procedures for managing houses.
    """

    def CreateHouse(self, request, context):
        """Create a house.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetHouse(self, request, context):
        """Get a house.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateHouse(self, request, context):
        """Update a house.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteHouse(self, request, context):
        """Delete a house.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MruVHousesServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateHouse': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateHouse,
                    request_deserializer=houses_dot_houses__pb2.CreateHouseRequest.FromString,
                    response_serializer=houses_dot_houses__pb2.CreateHouseResponse.SerializeToString,
            ),
            'GetHouse': grpc.unary_unary_rpc_method_handler(
                    servicer.GetHouse,
                    request_deserializer=houses_dot_houses__pb2.GetHouseRequest.FromString,
                    response_serializer=houses_dot_houses__pb2.GetHouseResponse.SerializeToString,
            ),
            'UpdateHouse': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateHouse,
                    request_deserializer=houses_dot_houses__pb2.UpdateHouseRequest.FromString,
                    response_serializer=houses_dot_houses__pb2.UpdateHouseResponse.SerializeToString,
            ),
            'DeleteHouse': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteHouse,
                    request_deserializer=houses_dot_houses__pb2.DeleteHouseRequest.FromString,
                    response_serializer=houses_dot_houses__pb2.DeleteHouseResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mruv.houses.MruVHousesService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MruVHousesService(object):
    """The MruV houses service provides procedures for managing houses.
    """

    @staticmethod
    def CreateHouse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.houses.MruVHousesService/CreateHouse',
            houses_dot_houses__pb2.CreateHouseRequest.SerializeToString,
            houses_dot_houses__pb2.CreateHouseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetHouse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.houses.MruVHousesService/GetHouse',
            houses_dot_houses__pb2.GetHouseRequest.SerializeToString,
            houses_dot_houses__pb2.GetHouseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateHouse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.houses.MruVHousesService/UpdateHouse',
            houses_dot_houses__pb2.UpdateHouseRequest.SerializeToString,
            houses_dot_houses__pb2.UpdateHouseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteHouse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.houses.MruVHousesService/DeleteHouse',
            houses_dot_houses__pb2.DeleteHouseRequest.SerializeToString,
            houses_dot_houses__pb2.DeleteHouseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
