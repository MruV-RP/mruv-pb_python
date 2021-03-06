# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from jobs import jobs_pb2 as jobs_dot_jobs__pb2


class MruVJobsServiceStub(object):
    """The MruV jobs service provides procedures for managing jobs.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateJob = channel.unary_unary(
                '/mruv.jobs.MruVJobsService/CreateJob',
                request_serializer=jobs_dot_jobs__pb2.CreateJobRequest.SerializeToString,
                response_deserializer=jobs_dot_jobs__pb2.CreateJobResponse.FromString,
                )
        self.GetJob = channel.unary_unary(
                '/mruv.jobs.MruVJobsService/GetJob',
                request_serializer=jobs_dot_jobs__pb2.GetJobRequest.SerializeToString,
                response_deserializer=jobs_dot_jobs__pb2.GetJobResponse.FromString,
                )
        self.UpdateJob = channel.unary_unary(
                '/mruv.jobs.MruVJobsService/UpdateJob',
                request_serializer=jobs_dot_jobs__pb2.UpdateJobRequest.SerializeToString,
                response_deserializer=jobs_dot_jobs__pb2.UpdateJobResponse.FromString,
                )
        self.DeleteJob = channel.unary_unary(
                '/mruv.jobs.MruVJobsService/DeleteJob',
                request_serializer=jobs_dot_jobs__pb2.DeleteJobRequest.SerializeToString,
                response_deserializer=jobs_dot_jobs__pb2.DeleteJobResponse.FromString,
                )


class MruVJobsServiceServicer(object):
    """The MruV jobs service provides procedures for managing jobs.
    """

    def CreateJob(self, request, context):
        """Create a job.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetJob(self, request, context):
        """Get a job.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateJob(self, request, context):
        """Update a job.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteJob(self, request, context):
        """Delete a job.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MruVJobsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateJob': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateJob,
                    request_deserializer=jobs_dot_jobs__pb2.CreateJobRequest.FromString,
                    response_serializer=jobs_dot_jobs__pb2.CreateJobResponse.SerializeToString,
            ),
            'GetJob': grpc.unary_unary_rpc_method_handler(
                    servicer.GetJob,
                    request_deserializer=jobs_dot_jobs__pb2.GetJobRequest.FromString,
                    response_serializer=jobs_dot_jobs__pb2.GetJobResponse.SerializeToString,
            ),
            'UpdateJob': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateJob,
                    request_deserializer=jobs_dot_jobs__pb2.UpdateJobRequest.FromString,
                    response_serializer=jobs_dot_jobs__pb2.UpdateJobResponse.SerializeToString,
            ),
            'DeleteJob': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteJob,
                    request_deserializer=jobs_dot_jobs__pb2.DeleteJobRequest.FromString,
                    response_serializer=jobs_dot_jobs__pb2.DeleteJobResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mruv.jobs.MruVJobsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MruVJobsService(object):
    """The MruV jobs service provides procedures for managing jobs.
    """

    @staticmethod
    def CreateJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.jobs.MruVJobsService/CreateJob',
            jobs_dot_jobs__pb2.CreateJobRequest.SerializeToString,
            jobs_dot_jobs__pb2.CreateJobResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.jobs.MruVJobsService/GetJob',
            jobs_dot_jobs__pb2.GetJobRequest.SerializeToString,
            jobs_dot_jobs__pb2.GetJobResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.jobs.MruVJobsService/UpdateJob',
            jobs_dot_jobs__pb2.UpdateJobRequest.SerializeToString,
            jobs_dot_jobs__pb2.UpdateJobResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mruv.jobs.MruVJobsService/DeleteJob',
            jobs_dot_jobs__pb2.DeleteJobRequest.SerializeToString,
            jobs_dot_jobs__pb2.DeleteJobResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
