# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from objects import models_pb2 as objects_dot_models__pb2


class MruVObjectModelsServiceStub(object):
  """The MruV objects service provides procedures for game object models.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateObjectModel = channel.unary_unary(
        '/mruv.objects.MruVObjectModelsService/CreateObjectModel',
        request_serializer=objects_dot_models__pb2.CreateObjectModelRequest.SerializeToString,
        response_deserializer=objects_dot_models__pb2.CreateObjectModelResponse.FromString,
        )
    self.GetObjectModel = channel.unary_unary(
        '/mruv.objects.MruVObjectModelsService/GetObjectModel',
        request_serializer=objects_dot_models__pb2.GetObjectModelRequest.SerializeToString,
        response_deserializer=objects_dot_models__pb2.GetObjectModelResponse.FromString,
        )
    self.UpdateObjectModel = channel.unary_unary(
        '/mruv.objects.MruVObjectModelsService/UpdateObjectModel',
        request_serializer=objects_dot_models__pb2.UpdateObjectModelRequest.SerializeToString,
        response_deserializer=objects_dot_models__pb2.UpdateObjectModelResponse.FromString,
        )
    self.DeleteObjectModel = channel.unary_unary(
        '/mruv.objects.MruVObjectModelsService/DeleteObjectModel',
        request_serializer=objects_dot_models__pb2.DeleteObjectModelRequest.SerializeToString,
        response_deserializer=objects_dot_models__pb2.DeleteObjectModelResponse.FromString,
        )
    self.FetchAllModels = channel.unary_stream(
        '/mruv.objects.MruVObjectModelsService/FetchAllModels',
        request_serializer=objects_dot_models__pb2.FetchAllModelsRequest.SerializeToString,
        response_deserializer=objects_dot_models__pb2.FetchAllModelsResponse.FromString,
        )


class MruVObjectModelsServiceServicer(object):
  """The MruV objects service provides procedures for game object models.
  """

  def CreateObjectModel(self, request, context):
    """Create an object model.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetObjectModel(self, request, context):
    """Get an object model.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateObjectModel(self, request, context):
    """Update an object model.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteObjectModel(self, request, context):
    """Delete an object model.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FetchAllModels(self, request, context):
    """Get all models.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MruVObjectModelsServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateObjectModel': grpc.unary_unary_rpc_method_handler(
          servicer.CreateObjectModel,
          request_deserializer=objects_dot_models__pb2.CreateObjectModelRequest.FromString,
          response_serializer=objects_dot_models__pb2.CreateObjectModelResponse.SerializeToString,
      ),
      'GetObjectModel': grpc.unary_unary_rpc_method_handler(
          servicer.GetObjectModel,
          request_deserializer=objects_dot_models__pb2.GetObjectModelRequest.FromString,
          response_serializer=objects_dot_models__pb2.GetObjectModelResponse.SerializeToString,
      ),
      'UpdateObjectModel': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateObjectModel,
          request_deserializer=objects_dot_models__pb2.UpdateObjectModelRequest.FromString,
          response_serializer=objects_dot_models__pb2.UpdateObjectModelResponse.SerializeToString,
      ),
      'DeleteObjectModel': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteObjectModel,
          request_deserializer=objects_dot_models__pb2.DeleteObjectModelRequest.FromString,
          response_serializer=objects_dot_models__pb2.DeleteObjectModelResponse.SerializeToString,
      ),
      'FetchAllModels': grpc.unary_stream_rpc_method_handler(
          servicer.FetchAllModels,
          request_deserializer=objects_dot_models__pb2.FetchAllModelsRequest.FromString,
          response_serializer=objects_dot_models__pb2.FetchAllModelsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'mruv.objects.MruVObjectModelsService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
