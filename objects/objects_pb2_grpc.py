# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from objects import objects_pb2 as objects_dot_objects__pb2


class MruVObjectsServiceStub(object):
  """The MruV objects service provides procedures for game objects.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateObjectModel = channel.unary_unary(
        '/mruv.gates.MruVObjectsService/CreateObjectModel',
        request_serializer=objects_dot_objects__pb2.CreateObjectModelRequest.SerializeToString,
        response_deserializer=objects_dot_objects__pb2.CreateObjectModelResponse.FromString,
        )
    self.GetObjectModel = channel.unary_unary(
        '/mruv.gates.MruVObjectsService/GetObjectModel',
        request_serializer=objects_dot_objects__pb2.GetObjectModelRequest.SerializeToString,
        response_deserializer=objects_dot_objects__pb2.GetObjectModelResponse.FromString,
        )
    self.UpdateObjectModel = channel.unary_unary(
        '/mruv.gates.MruVObjectsService/UpdateObjectModel',
        request_serializer=objects_dot_objects__pb2.UpdateObjectModelRequest.SerializeToString,
        response_deserializer=objects_dot_objects__pb2.UpdateObjectModelResponse.FromString,
        )
    self.DeleteObjectModel = channel.unary_unary(
        '/mruv.gates.MruVObjectsService/DeleteObjectModel',
        request_serializer=objects_dot_objects__pb2.DeleteObjectModelRequest.SerializeToString,
        response_deserializer=objects_dot_objects__pb2.DeleteObjectModelResponse.FromString,
        )
    self.CreateObject = channel.unary_unary(
        '/mruv.gates.MruVObjectsService/CreateObject',
        request_serializer=objects_dot_objects__pb2.CreateObjectRequest.SerializeToString,
        response_deserializer=objects_dot_objects__pb2.CreateObjectResponse.FromString,
        )
    self.GetObject = channel.unary_unary(
        '/mruv.gates.MruVObjectsService/GetObject',
        request_serializer=objects_dot_objects__pb2.GetObjectRequest.SerializeToString,
        response_deserializer=objects_dot_objects__pb2.GetObjectResponse.FromString,
        )
    self.UpdateObject = channel.unary_unary(
        '/mruv.gates.MruVObjectsService/UpdateObject',
        request_serializer=objects_dot_objects__pb2.UpdateObjectRequest.SerializeToString,
        response_deserializer=objects_dot_objects__pb2.UpdateObjectResponse.FromString,
        )
    self.DeleteObject = channel.unary_unary(
        '/mruv.gates.MruVObjectsService/DeleteObject',
        request_serializer=objects_dot_objects__pb2.DeleteObjectRequest.SerializeToString,
        response_deserializer=objects_dot_objects__pb2.DeleteObjectResponse.FromString,
        )


class MruVObjectsServiceServicer(object):
  """The MruV objects service provides procedures for game objects.
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

  def CreateObject(self, request, context):
    """Create an object.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetObject(self, request, context):
    """Get an object.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateObject(self, request, context):
    """Update an object.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteObject(self, request, context):
    """Delete an object.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MruVObjectsServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateObjectModel': grpc.unary_unary_rpc_method_handler(
          servicer.CreateObjectModel,
          request_deserializer=objects_dot_objects__pb2.CreateObjectModelRequest.FromString,
          response_serializer=objects_dot_objects__pb2.CreateObjectModelResponse.SerializeToString,
      ),
      'GetObjectModel': grpc.unary_unary_rpc_method_handler(
          servicer.GetObjectModel,
          request_deserializer=objects_dot_objects__pb2.GetObjectModelRequest.FromString,
          response_serializer=objects_dot_objects__pb2.GetObjectModelResponse.SerializeToString,
      ),
      'UpdateObjectModel': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateObjectModel,
          request_deserializer=objects_dot_objects__pb2.UpdateObjectModelRequest.FromString,
          response_serializer=objects_dot_objects__pb2.UpdateObjectModelResponse.SerializeToString,
      ),
      'DeleteObjectModel': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteObjectModel,
          request_deserializer=objects_dot_objects__pb2.DeleteObjectModelRequest.FromString,
          response_serializer=objects_dot_objects__pb2.DeleteObjectModelResponse.SerializeToString,
      ),
      'CreateObject': grpc.unary_unary_rpc_method_handler(
          servicer.CreateObject,
          request_deserializer=objects_dot_objects__pb2.CreateObjectRequest.FromString,
          response_serializer=objects_dot_objects__pb2.CreateObjectResponse.SerializeToString,
      ),
      'GetObject': grpc.unary_unary_rpc_method_handler(
          servicer.GetObject,
          request_deserializer=objects_dot_objects__pb2.GetObjectRequest.FromString,
          response_serializer=objects_dot_objects__pb2.GetObjectResponse.SerializeToString,
      ),
      'UpdateObject': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateObject,
          request_deserializer=objects_dot_objects__pb2.UpdateObjectRequest.FromString,
          response_serializer=objects_dot_objects__pb2.UpdateObjectResponse.SerializeToString,
      ),
      'DeleteObject': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteObject,
          request_deserializer=objects_dot_objects__pb2.DeleteObjectRequest.FromString,
          response_serializer=objects_dot_objects__pb2.DeleteObjectResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'mruv.gates.MruVObjectsService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))