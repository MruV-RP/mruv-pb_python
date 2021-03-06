# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from objects import movable_pb2 as objects_dot_movable__pb2


class MruVMovableObjectsServiceStub(object):
    """The MruV objects service provides procedures for movable game objects.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateMovableObject = channel.unary_unary(
                '/mruv.objects.MruVMovableObjectsService/CreateMovableObject',
                request_serializer=objects_dot_movable__pb2.CreateMovableObjectRequest.SerializeToString,
                response_deserializer=objects_dot_movable__pb2.CreateMovableObjectResponse.FromString,
                )
        self.GetMovableObject = channel.unary_unary(
                '/mruv.objects.MruVMovableObjectsService/GetMovableObject',
                request_serializer=objects_dot_movable__pb2.GetMovableObjectRequest.SerializeToString,
                response_deserializer=objects_dot_movable__pb2.GetMovableObjectResponse.FromString,
                )
        self.UpdateMovableObject = channel.unary_unary(
                '/mruv.objects.MruVMovableObjectsService/UpdateMovableObject',
                request_serializer=objects_dot_movable__pb2.UpdateMovableObjectRequest.SerializeToString,
                response_deserializer=objects_dot_movable__pb2.UpdateMovableObjectResponse.FromString,
                )
        self.DeleteMovableObject = channel.unary_unary(
                '/mruv.objects.MruVMovableObjectsService/DeleteMovableObject',
                request_serializer=objects_dot_movable__pb2.DeleteMovableObjectRequest.SerializeToString,
                response_deserializer=objects_dot_movable__pb2.DeleteMovableObjectResponse.FromString,
                )
        self.MoveObject = channel.unary_unary(
                '/mruv.objects.MruVMovableObjectsService/MoveObject',
                request_serializer=objects_dot_movable__pb2.MoveObjectRequest.SerializeToString,
                response_deserializer=objects_dot_movable__pb2.MoveObjectResponse.FromString,
                )
        self.MoveObjectNext = channel.unary_unary(
                '/mruv.objects.MruVMovableObjectsService/MoveObjectNext',
                request_serializer=objects_dot_movable__pb2.MoveObjectNextRequest.SerializeToString,
                response_deserializer=objects_dot_movable__pb2.MoveObjectNextResponse.FromString,
                )
        self.MoveObjectPrevious = channel.unary_unary(
                '/mruv.objects.MruVMovableObjectsService/MoveObjectPrevious',
                request_serializer=objects_dot_movable__pb2.MoveObjectPreviousRequest.SerializeToString,
                response_deserializer=objects_dot_movable__pb2.MoveObjectPreviousResponse.FromString,
                )
        self.FetchAllMovableObjects = channel.unary_stream(
                '/mruv.objects.MruVMovableObjectsService/FetchAllMovableObjects',
                request_serializer=objects_dot_movable__pb2.FetchAllMovableObjectsRequest.SerializeToString,
                response_deserializer=objects_dot_movable__pb2.FetchAllMovableObjectsResponse.FromString,
                )


class MruVMovableObjectsServiceServicer(object):
    """The MruV objects service provides procedures for movable game objects.
    """

    def CreateMovableObject(self, request, context):
        """Create a movable object.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMovableObject(self, request, context):
        """Get a movable object.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateMovableObject(self, request, context):
        """Update a movable object.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteMovableObject(self, request, context):
        """Delete a movable object.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MoveObject(self, request, context):
        """Move an object to other state.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MoveObjectNext(self, request, context):
        """Move an object to next state.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MoveObjectPrevious(self, request, context):
        """Move an object to previous state.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchAllMovableObjects(self, request, context):
        """
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MruVMovableObjectsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateMovableObject': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateMovableObject,
                    request_deserializer=objects_dot_movable__pb2.CreateMovableObjectRequest.FromString,
                    response_serializer=objects_dot_movable__pb2.CreateMovableObjectResponse.SerializeToString,
            ),
            'GetMovableObject': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMovableObject,
                    request_deserializer=objects_dot_movable__pb2.GetMovableObjectRequest.FromString,
                    response_serializer=objects_dot_movable__pb2.GetMovableObjectResponse.SerializeToString,
            ),
            'UpdateMovableObject': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateMovableObject,
                    request_deserializer=objects_dot_movable__pb2.UpdateMovableObjectRequest.FromString,
                    response_serializer=objects_dot_movable__pb2.UpdateMovableObjectResponse.SerializeToString,
            ),
            'DeleteMovableObject': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteMovableObject,
                    request_deserializer=objects_dot_movable__pb2.DeleteMovableObjectRequest.FromString,
                    response_serializer=objects_dot_movable__pb2.DeleteMovableObjectResponse.SerializeToString,
            ),
            'MoveObject': grpc.unary_unary_rpc_method_handler(
                    servicer.MoveObject,
                    request_deserializer=objects_dot_movable__pb2.MoveObjectRequest.FromString,
                    response_serializer=objects_dot_movable__pb2.MoveObjectResponse.SerializeToString,
            ),
            'MoveObjectNext': grpc.unary_unary_rpc_method_handler(
                    servicer.MoveObjectNext,
                    request_deserializer=objects_dot_movable__pb2.MoveObjectNextRequest.FromString,
                    response_serializer=objects_dot_movable__pb2.MoveObjectNextResponse.SerializeToString,
            ),
            'MoveObjectPrevious': grpc.unary_unary_rpc_method_handler(
                    servicer.MoveObjectPrevious,
                    request_deserializer=objects_dot_movable__pb2.MoveObjectPreviousRequest.FromString,
                    response_serializer=objects_dot_movable__pb2.MoveObjectPreviousResponse.SerializeToString,
            ),
            'FetchAllMovableObjects': grpc.unary_stream_rpc_method_handler(
                    servicer.FetchAllMovableObjects,
                    request_deserializer=objects_dot_movable__pb2.FetchAllMovableObjectsRequest.FromString,
                    response_serializer=objects_dot_movable__pb2.FetchAllMovableObjectsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mruv.objects.MruVMovableObjectsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MruVMovableObjectsService(object):
    """The MruV objects service provides procedures for movable game objects.
    """

    @staticmethod
    def CreateMovableObject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.objects.MruVMovableObjectsService/CreateMovableObject',
            objects_dot_movable__pb2.CreateMovableObjectRequest.SerializeToString,
            objects_dot_movable__pb2.CreateMovableObjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMovableObject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.objects.MruVMovableObjectsService/GetMovableObject',
            objects_dot_movable__pb2.GetMovableObjectRequest.SerializeToString,
            objects_dot_movable__pb2.GetMovableObjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateMovableObject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.objects.MruVMovableObjectsService/UpdateMovableObject',
            objects_dot_movable__pb2.UpdateMovableObjectRequest.SerializeToString,
            objects_dot_movable__pb2.UpdateMovableObjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteMovableObject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.objects.MruVMovableObjectsService/DeleteMovableObject',
            objects_dot_movable__pb2.DeleteMovableObjectRequest.SerializeToString,
            objects_dot_movable__pb2.DeleteMovableObjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MoveObject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.objects.MruVMovableObjectsService/MoveObject',
            objects_dot_movable__pb2.MoveObjectRequest.SerializeToString,
            objects_dot_movable__pb2.MoveObjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MoveObjectNext(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.objects.MruVMovableObjectsService/MoveObjectNext',
            objects_dot_movable__pb2.MoveObjectNextRequest.SerializeToString,
            objects_dot_movable__pb2.MoveObjectNextResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MoveObjectPrevious(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.objects.MruVMovableObjectsService/MoveObjectPrevious',
            objects_dot_movable__pb2.MoveObjectPreviousRequest.SerializeToString,
            objects_dot_movable__pb2.MoveObjectPreviousResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FetchAllMovableObjects(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mruv.objects.MruVMovableObjectsService/FetchAllMovableObjects',
            objects_dot_movable__pb2.FetchAllMovableObjectsRequest.SerializeToString,
            objects_dot_movable__pb2.FetchAllMovableObjectsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
