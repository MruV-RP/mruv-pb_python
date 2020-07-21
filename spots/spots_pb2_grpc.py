# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from spots import spots_pb2 as spots_dot_spots__pb2


class MruVSpotsServiceStub(object):
  """The MruV spots service provides procedures for managing spots.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateSpot = channel.unary_unary(
        '/mruv.spots.MruVSpotsService/CreateSpot',
        request_serializer=spots_dot_spots__pb2.CreateSpotRequest.SerializeToString,
        response_deserializer=spots_dot_spots__pb2.CreateSpotResponse.FromString,
        )
    self.GetSpot = channel.unary_unary(
        '/mruv.spots.MruVSpotsService/GetSpot',
        request_serializer=spots_dot_spots__pb2.GetSpotRequest.SerializeToString,
        response_deserializer=spots_dot_spots__pb2.GetSpotResponse.FromString,
        )
    self.UpdateSpot = channel.unary_unary(
        '/mruv.spots.MruVSpotsService/UpdateSpot',
        request_serializer=spots_dot_spots__pb2.UpdateSpotRequest.SerializeToString,
        response_deserializer=spots_dot_spots__pb2.UpdateSpotResponse.FromString,
        )
    self.DeleteSpot = channel.unary_unary(
        '/mruv.spots.MruVSpotsService/DeleteSpot',
        request_serializer=spots_dot_spots__pb2.DeleteSpotRequest.SerializeToString,
        response_deserializer=spots_dot_spots__pb2.DeleteSpotResponse.FromString,
        )


class MruVSpotsServiceServicer(object):
  """The MruV spots service provides procedures for managing spots.
  """

  def CreateSpot(self, request, context):
    """Create a spot.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSpot(self, request, context):
    """Get a spot.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateSpot(self, request, context):
    """Update a spot.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteSpot(self, request, context):
    """Delete a spot.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MruVSpotsServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateSpot': grpc.unary_unary_rpc_method_handler(
          servicer.CreateSpot,
          request_deserializer=spots_dot_spots__pb2.CreateSpotRequest.FromString,
          response_serializer=spots_dot_spots__pb2.CreateSpotResponse.SerializeToString,
      ),
      'GetSpot': grpc.unary_unary_rpc_method_handler(
          servicer.GetSpot,
          request_deserializer=spots_dot_spots__pb2.GetSpotRequest.FromString,
          response_serializer=spots_dot_spots__pb2.GetSpotResponse.SerializeToString,
      ),
      'UpdateSpot': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateSpot,
          request_deserializer=spots_dot_spots__pb2.UpdateSpotRequest.FromString,
          response_serializer=spots_dot_spots__pb2.UpdateSpotResponse.SerializeToString,
      ),
      'DeleteSpot': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteSpot,
          request_deserializer=spots_dot_spots__pb2.DeleteSpotRequest.FromString,
          response_serializer=spots_dot_spots__pb2.DeleteSpotResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'mruv.spots.MruVSpotsService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))