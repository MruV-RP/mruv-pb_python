# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from plots import plots_pb2 as plots_dot_plots__pb2


class MruVPlotsServiceStub(object):
  """The MruV plots service provides procedures for managing buildings plots and other areas.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreatePlot = channel.unary_unary(
        '/mruv.plots.MruVPlotsService/CreatePlot',
        request_serializer=plots_dot_plots__pb2.CreatePlotRequest.SerializeToString,
        response_deserializer=plots_dot_plots__pb2.CreatePlotResponse.FromString,
        )
    self.GetPlot = channel.unary_unary(
        '/mruv.plots.MruVPlotsService/GetPlot',
        request_serializer=plots_dot_plots__pb2.GetPlotRequest.SerializeToString,
        response_deserializer=plots_dot_plots__pb2.GetPlotResponse.FromString,
        )
    self.UpdatePlot = channel.unary_unary(
        '/mruv.plots.MruVPlotsService/UpdatePlot',
        request_serializer=plots_dot_plots__pb2.UpdatePlotRequest.SerializeToString,
        response_deserializer=plots_dot_plots__pb2.UpdatePlotResponse.FromString,
        )
    self.DeletePlot = channel.unary_unary(
        '/mruv.plots.MruVPlotsService/DeletePlot',
        request_serializer=plots_dot_plots__pb2.DeletePlotRequest.SerializeToString,
        response_deserializer=plots_dot_plots__pb2.DeletePlotResponse.FromString,
        )


class MruVPlotsServiceServicer(object):
  """The MruV plots service provides procedures for managing buildings plots and other areas.
  """

  def CreatePlot(self, request, context):
    """Create a plot.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPlot(self, request, context):
    """Get a plot.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdatePlot(self, request, context):
    """Update a plot.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeletePlot(self, request, context):
    """Delete a plot.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MruVPlotsServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreatePlot': grpc.unary_unary_rpc_method_handler(
          servicer.CreatePlot,
          request_deserializer=plots_dot_plots__pb2.CreatePlotRequest.FromString,
          response_serializer=plots_dot_plots__pb2.CreatePlotResponse.SerializeToString,
      ),
      'GetPlot': grpc.unary_unary_rpc_method_handler(
          servicer.GetPlot,
          request_deserializer=plots_dot_plots__pb2.GetPlotRequest.FromString,
          response_serializer=plots_dot_plots__pb2.GetPlotResponse.SerializeToString,
      ),
      'UpdatePlot': grpc.unary_unary_rpc_method_handler(
          servicer.UpdatePlot,
          request_deserializer=plots_dot_plots__pb2.UpdatePlotRequest.FromString,
          response_serializer=plots_dot_plots__pb2.UpdatePlotResponse.SerializeToString,
      ),
      'DeletePlot': grpc.unary_unary_rpc_method_handler(
          servicer.DeletePlot,
          request_deserializer=plots_dot_plots__pb2.DeletePlotRequest.FromString,
          response_serializer=plots_dot_plots__pb2.DeletePlotResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'mruv.plots.MruVPlotsService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
