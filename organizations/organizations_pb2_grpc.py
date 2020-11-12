# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from organizations import organizations_pb2 as organizations_dot_organizations__pb2


class MruVOrganizationsServiceStub(object):
    """The MruV jobs service provides procedures for managing organizations and fractions.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateOrganization = channel.unary_unary(
                '/mruv.organizations.MruVOrganizationsService/CreateOrganization',
                request_serializer=organizations_dot_organizations__pb2.CreateOrganizationRequest.SerializeToString,
                response_deserializer=organizations_dot_organizations__pb2.CreateOrganizationResponse.FromString,
                )
        self.GetOrganization = channel.unary_unary(
                '/mruv.organizations.MruVOrganizationsService/GetOrganization',
                request_serializer=organizations_dot_organizations__pb2.GetOrganizationRequest.SerializeToString,
                response_deserializer=organizations_dot_organizations__pb2.GetOrganizationResponse.FromString,
                )
        self.UpdateOrganization = channel.unary_unary(
                '/mruv.organizations.MruVOrganizationsService/UpdateOrganization',
                request_serializer=organizations_dot_organizations__pb2.UpdateOrganizationRequest.SerializeToString,
                response_deserializer=organizations_dot_organizations__pb2.UpdateOrganizationResponse.FromString,
                )
        self.DeleteOrganization = channel.unary_unary(
                '/mruv.organizations.MruVOrganizationsService/DeleteOrganization',
                request_serializer=organizations_dot_organizations__pb2.DeleteOrganizationRequest.SerializeToString,
                response_deserializer=organizations_dot_organizations__pb2.DeleteOrganizationResponse.FromString,
                )
        self.AssignLeader = channel.unary_unary(
                '/mruv.organizations.MruVOrganizationsService/AssignLeader',
                request_serializer=organizations_dot_organizations__pb2.AssignLeaderRequest.SerializeToString,
                response_deserializer=organizations_dot_organizations__pb2.AssignLeaderResponse.FromString,
                )
        self.UnassignLeader = channel.unary_unary(
                '/mruv.organizations.MruVOrganizationsService/UnassignLeader',
                request_serializer=organizations_dot_organizations__pb2.UnassignLeaderRequest.SerializeToString,
                response_deserializer=organizations_dot_organizations__pb2.UnassignLeaderResponse.FromString,
                )


class MruVOrganizationsServiceServicer(object):
    """The MruV jobs service provides procedures for managing organizations and fractions.
    """

    def CreateOrganization(self, request, context):
        """Create a organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrganization(self, request, context):
        """Get organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateOrganization(self, request, context):
        """Update organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteOrganization(self, request, context):
        """Delete organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AssignLeader(self, request, context):
        """Assign an organization leader. Leader is a main administrator of a organization, have all rights to manage organization.
        If the organization leader already exists, the leader will be overwritten.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnassignLeader(self, request, context):
        """
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MruVOrganizationsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateOrganization': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateOrganization,
                    request_deserializer=organizations_dot_organizations__pb2.CreateOrganizationRequest.FromString,
                    response_serializer=organizations_dot_organizations__pb2.CreateOrganizationResponse.SerializeToString,
            ),
            'GetOrganization': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrganization,
                    request_deserializer=organizations_dot_organizations__pb2.GetOrganizationRequest.FromString,
                    response_serializer=organizations_dot_organizations__pb2.GetOrganizationResponse.SerializeToString,
            ),
            'UpdateOrganization': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateOrganization,
                    request_deserializer=organizations_dot_organizations__pb2.UpdateOrganizationRequest.FromString,
                    response_serializer=organizations_dot_organizations__pb2.UpdateOrganizationResponse.SerializeToString,
            ),
            'DeleteOrganization': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteOrganization,
                    request_deserializer=organizations_dot_organizations__pb2.DeleteOrganizationRequest.FromString,
                    response_serializer=organizations_dot_organizations__pb2.DeleteOrganizationResponse.SerializeToString,
            ),
            'AssignLeader': grpc.unary_unary_rpc_method_handler(
                    servicer.AssignLeader,
                    request_deserializer=organizations_dot_organizations__pb2.AssignLeaderRequest.FromString,
                    response_serializer=organizations_dot_organizations__pb2.AssignLeaderResponse.SerializeToString,
            ),
            'UnassignLeader': grpc.unary_unary_rpc_method_handler(
                    servicer.UnassignLeader,
                    request_deserializer=organizations_dot_organizations__pb2.UnassignLeaderRequest.FromString,
                    response_serializer=organizations_dot_organizations__pb2.UnassignLeaderResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mruv.organizations.MruVOrganizationsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MruVOrganizationsService(object):
    """The MruV jobs service provides procedures for managing organizations and fractions.
    """

    @staticmethod
    def CreateOrganization(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.organizations.MruVOrganizationsService/CreateOrganization',
            organizations_dot_organizations__pb2.CreateOrganizationRequest.SerializeToString,
            organizations_dot_organizations__pb2.CreateOrganizationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrganization(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.organizations.MruVOrganizationsService/GetOrganization',
            organizations_dot_organizations__pb2.GetOrganizationRequest.SerializeToString,
            organizations_dot_organizations__pb2.GetOrganizationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateOrganization(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.organizations.MruVOrganizationsService/UpdateOrganization',
            organizations_dot_organizations__pb2.UpdateOrganizationRequest.SerializeToString,
            organizations_dot_organizations__pb2.UpdateOrganizationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteOrganization(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.organizations.MruVOrganizationsService/DeleteOrganization',
            organizations_dot_organizations__pb2.DeleteOrganizationRequest.SerializeToString,
            organizations_dot_organizations__pb2.DeleteOrganizationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AssignLeader(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.organizations.MruVOrganizationsService/AssignLeader',
            organizations_dot_organizations__pb2.AssignLeaderRequest.SerializeToString,
            organizations_dot_organizations__pb2.AssignLeaderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnassignLeader(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.organizations.MruVOrganizationsService/UnassignLeader',
            organizations_dot_organizations__pb2.UnassignLeaderRequest.SerializeToString,
            organizations_dot_organizations__pb2.UnassignLeaderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
