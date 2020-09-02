# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: plots/plots.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from common import spatial_pb2 as common_dot_spatial__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='plots/plots.proto',
  package='mruv.plots',
  syntax='proto3',
  serialized_options=_b('Z#github.com/MruV-RP/mruv-pb-go/plots'),
  serialized_pb=_b('\n\x11plots/plots.proto\x12\nmruv.plots\x1a\x1cgoogle/api/annotations.proto\x1a\x14\x63ommon/spatial.proto\"I\n\x04Plot\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x1e\n\x06points\x18\x03 \x03(\x0b\x32\x0e.mruv.Position\"V\n\x11\x43reatePlotRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x1e\n\x06points\x18\x03 \x03(\x0b\x32\x0e.mruv.Position\" \n\x12\x43reatePlotResponse\x12\n\n\x02id\x18\x01 \x01(\r\"\x1c\n\x0eGetPlotRequest\x12\n\n\x02id\x18\x01 \x01(\r\"b\n\x0fGetPlotResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x1e\n\x06points\x18\x03 \x03(\x0b\x32\x0e.mruv.Position\x12\x0c\n\x04\x61rea\x18\x04 \x01(\x01\"B\n\x11UpdatePlotRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"\x14\n\x12UpdatePlotResponse\"\x1f\n\x11\x44\x65letePlotRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x14\n\x12\x44\x65letePlotResponse2\x98\x03\n\x10MruVPlotsService\x12^\n\nCreatePlot\x12\x1d.mruv.plots.CreatePlotRequest\x1a\x1e.mruv.plots.CreatePlotResponse\"\x11\x82\xd3\xe4\x93\x02\x0b\"\t/v1/plots\x12Z\n\x07GetPlot\x12\x1a.mruv.plots.GetPlotRequest\x1a\x1b.mruv.plots.GetPlotResponse\"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/v1/plots/{id}\x12\x63\n\nUpdatePlot\x12\x1d.mruv.plots.UpdatePlotRequest\x1a\x1e.mruv.plots.UpdatePlotResponse\"\x16\x82\xd3\xe4\x93\x02\x10\x32\x0e/v1/plots/{id}\x12\x63\n\nDeletePlot\x12\x1d.mruv.plots.DeletePlotRequest\x1a\x1e.mruv.plots.DeletePlotResponse\"\x16\x82\xd3\xe4\x93\x02\x10*\x0e/v1/plots/{id}B%Z#github.com/MruV-RP/mruv-pb-go/plotsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,common_dot_spatial__pb2.DESCRIPTOR,])




_PLOT = _descriptor.Descriptor(
  name='Plot',
  full_name='mruv.plots.Plot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.plots.Plot.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='mruv.plots.Plot.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='points', full_name='mruv.plots.Plot.points', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=158,
)


_CREATEPLOTREQUEST = _descriptor.Descriptor(
  name='CreatePlotRequest',
  full_name='mruv.plots.CreatePlotRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.plots.CreatePlotRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='mruv.plots.CreatePlotRequest.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='points', full_name='mruv.plots.CreatePlotRequest.points', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=160,
  serialized_end=246,
)


_CREATEPLOTRESPONSE = _descriptor.Descriptor(
  name='CreatePlotResponse',
  full_name='mruv.plots.CreatePlotResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.plots.CreatePlotResponse.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=248,
  serialized_end=280,
)


_GETPLOTREQUEST = _descriptor.Descriptor(
  name='GetPlotRequest',
  full_name='mruv.plots.GetPlotRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.plots.GetPlotRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=282,
  serialized_end=310,
)


_GETPLOTRESPONSE = _descriptor.Descriptor(
  name='GetPlotResponse',
  full_name='mruv.plots.GetPlotResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.plots.GetPlotResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='mruv.plots.GetPlotResponse.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='points', full_name='mruv.plots.GetPlotResponse.points', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='area', full_name='mruv.plots.GetPlotResponse.area', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=312,
  serialized_end=410,
)


_UPDATEPLOTREQUEST = _descriptor.Descriptor(
  name='UpdatePlotRequest',
  full_name='mruv.plots.UpdatePlotRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.plots.UpdatePlotRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.plots.UpdatePlotRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='mruv.plots.UpdatePlotRequest.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=412,
  serialized_end=478,
)


_UPDATEPLOTRESPONSE = _descriptor.Descriptor(
  name='UpdatePlotResponse',
  full_name='mruv.plots.UpdatePlotResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=480,
  serialized_end=500,
)


_DELETEPLOTREQUEST = _descriptor.Descriptor(
  name='DeletePlotRequest',
  full_name='mruv.plots.DeletePlotRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.plots.DeletePlotRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=502,
  serialized_end=533,
)


_DELETEPLOTRESPONSE = _descriptor.Descriptor(
  name='DeletePlotResponse',
  full_name='mruv.plots.DeletePlotResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=535,
  serialized_end=555,
)

_PLOT.fields_by_name['points'].message_type = common_dot_spatial__pb2._POSITION
_CREATEPLOTREQUEST.fields_by_name['points'].message_type = common_dot_spatial__pb2._POSITION
_GETPLOTRESPONSE.fields_by_name['points'].message_type = common_dot_spatial__pb2._POSITION
DESCRIPTOR.message_types_by_name['Plot'] = _PLOT
DESCRIPTOR.message_types_by_name['CreatePlotRequest'] = _CREATEPLOTREQUEST
DESCRIPTOR.message_types_by_name['CreatePlotResponse'] = _CREATEPLOTRESPONSE
DESCRIPTOR.message_types_by_name['GetPlotRequest'] = _GETPLOTREQUEST
DESCRIPTOR.message_types_by_name['GetPlotResponse'] = _GETPLOTRESPONSE
DESCRIPTOR.message_types_by_name['UpdatePlotRequest'] = _UPDATEPLOTREQUEST
DESCRIPTOR.message_types_by_name['UpdatePlotResponse'] = _UPDATEPLOTRESPONSE
DESCRIPTOR.message_types_by_name['DeletePlotRequest'] = _DELETEPLOTREQUEST
DESCRIPTOR.message_types_by_name['DeletePlotResponse'] = _DELETEPLOTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Plot = _reflection.GeneratedProtocolMessageType('Plot', (_message.Message,), {
  'DESCRIPTOR' : _PLOT,
  '__module__' : 'plots.plots_pb2'
  # @@protoc_insertion_point(class_scope:mruv.plots.Plot)
  })
_sym_db.RegisterMessage(Plot)

CreatePlotRequest = _reflection.GeneratedProtocolMessageType('CreatePlotRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPLOTREQUEST,
  '__module__' : 'plots.plots_pb2'
  # @@protoc_insertion_point(class_scope:mruv.plots.CreatePlotRequest)
  })
_sym_db.RegisterMessage(CreatePlotRequest)

CreatePlotResponse = _reflection.GeneratedProtocolMessageType('CreatePlotResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPLOTRESPONSE,
  '__module__' : 'plots.plots_pb2'
  # @@protoc_insertion_point(class_scope:mruv.plots.CreatePlotResponse)
  })
_sym_db.RegisterMessage(CreatePlotResponse)

GetPlotRequest = _reflection.GeneratedProtocolMessageType('GetPlotRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPLOTREQUEST,
  '__module__' : 'plots.plots_pb2'
  # @@protoc_insertion_point(class_scope:mruv.plots.GetPlotRequest)
  })
_sym_db.RegisterMessage(GetPlotRequest)

GetPlotResponse = _reflection.GeneratedProtocolMessageType('GetPlotResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPLOTRESPONSE,
  '__module__' : 'plots.plots_pb2'
  # @@protoc_insertion_point(class_scope:mruv.plots.GetPlotResponse)
  })
_sym_db.RegisterMessage(GetPlotResponse)

UpdatePlotRequest = _reflection.GeneratedProtocolMessageType('UpdatePlotRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPLOTREQUEST,
  '__module__' : 'plots.plots_pb2'
  # @@protoc_insertion_point(class_scope:mruv.plots.UpdatePlotRequest)
  })
_sym_db.RegisterMessage(UpdatePlotRequest)

UpdatePlotResponse = _reflection.GeneratedProtocolMessageType('UpdatePlotResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPLOTRESPONSE,
  '__module__' : 'plots.plots_pb2'
  # @@protoc_insertion_point(class_scope:mruv.plots.UpdatePlotResponse)
  })
_sym_db.RegisterMessage(UpdatePlotResponse)

DeletePlotRequest = _reflection.GeneratedProtocolMessageType('DeletePlotRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPLOTREQUEST,
  '__module__' : 'plots.plots_pb2'
  # @@protoc_insertion_point(class_scope:mruv.plots.DeletePlotRequest)
  })
_sym_db.RegisterMessage(DeletePlotRequest)

DeletePlotResponse = _reflection.GeneratedProtocolMessageType('DeletePlotResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPLOTRESPONSE,
  '__module__' : 'plots.plots_pb2'
  # @@protoc_insertion_point(class_scope:mruv.plots.DeletePlotResponse)
  })
_sym_db.RegisterMessage(DeletePlotResponse)


DESCRIPTOR._options = None

_MRUVPLOTSSERVICE = _descriptor.ServiceDescriptor(
  name='MruVPlotsService',
  full_name='mruv.plots.MruVPlotsService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=558,
  serialized_end=966,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreatePlot',
    full_name='mruv.plots.MruVPlotsService.CreatePlot',
    index=0,
    containing_service=None,
    input_type=_CREATEPLOTREQUEST,
    output_type=_CREATEPLOTRESPONSE,
    serialized_options=_b('\202\323\344\223\002\013\"\t/v1/plots'),
  ),
  _descriptor.MethodDescriptor(
    name='GetPlot',
    full_name='mruv.plots.MruVPlotsService.GetPlot',
    index=1,
    containing_service=None,
    input_type=_GETPLOTREQUEST,
    output_type=_GETPLOTRESPONSE,
    serialized_options=_b('\202\323\344\223\002\020\022\016/v1/plots/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='UpdatePlot',
    full_name='mruv.plots.MruVPlotsService.UpdatePlot',
    index=2,
    containing_service=None,
    input_type=_UPDATEPLOTREQUEST,
    output_type=_UPDATEPLOTRESPONSE,
    serialized_options=_b('\202\323\344\223\002\0202\016/v1/plots/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='DeletePlot',
    full_name='mruv.plots.MruVPlotsService.DeletePlot',
    index=3,
    containing_service=None,
    input_type=_DELETEPLOTREQUEST,
    output_type=_DELETEPLOTRESPONSE,
    serialized_options=_b('\202\323\344\223\002\020*\016/v1/plots/{id}'),
  ),
])
_sym_db.RegisterServiceDescriptor(_MRUVPLOTSSERVICE)

DESCRIPTOR.services_by_name['MruVPlotsService'] = _MRUVPLOTSSERVICE

# @@protoc_insertion_point(module_scope)
