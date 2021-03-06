# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: elevators/elevators.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='elevators/elevators.proto',
  package='mruv.elevators',
  syntax='proto3',
  serialized_options=b'Z\'github.com/MruV-RP/mruv-pb-go/elevators',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19\x65levators/elevators.proto\x12\x0emruv.elevators\x1a\x1cgoogle/api/annotations.proto\"\x17\n\x15\x43reateElevatorRequest\"$\n\x16\x43reateElevatorResponse\x12\n\n\x02id\x18\x01 \x01(\r\" \n\x12GetElevatorRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x15\n\x13GetElevatorResponse\"#\n\x15UpdateElevatorRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x18\n\x16UpdateElevatorResponse\"#\n\x15\x44\x65leteElevatorRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x18\n\x16\x44\x65leteElevatorResponse\"&\n\x18GetElevatorFloorsRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x1b\n\x19GetElevatorFloorsResponse2\x90\x05\n\x14MruVElevatorsService\x12y\n\x0e\x43reateElevator\x12%.mruv.elevators.CreateElevatorRequest\x1a&.mruv.elevators.CreateElevatorResponse\"\x18\x82\xd3\xe4\x93\x02\x12\"\r/v1/elevators:\x01*\x12r\n\x0bGetElevator\x12\".mruv.elevators.GetElevatorRequest\x1a#.mruv.elevators.GetElevatorResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/v1/elevators/{id}\x12~\n\x0eUpdateElevator\x12%.mruv.elevators.UpdateElevatorRequest\x1a&.mruv.elevators.UpdateElevatorResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x32\x12/v1/elevators/{id}:\x01*\x12{\n\x0e\x44\x65leteElevator\x12%.mruv.elevators.DeleteElevatorRequest\x1a&.mruv.elevators.DeleteElevatorResponse\"\x1a\x82\xd3\xe4\x93\x02\x14*\x12/v1/elevators/{id}\x12\x8b\x01\n\x11GetElevatorFloors\x12(.mruv.elevators.GetElevatorFloorsRequest\x1a).mruv.elevators.GetElevatorFloorsResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/v1/elevators/{id}/floorsB)Z\'github.com/MruV-RP/mruv-pb-go/elevatorsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CREATEELEVATORREQUEST = _descriptor.Descriptor(
  name='CreateElevatorRequest',
  full_name='mruv.elevators.CreateElevatorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=75,
  serialized_end=98,
)


_CREATEELEVATORRESPONSE = _descriptor.Descriptor(
  name='CreateElevatorResponse',
  full_name='mruv.elevators.CreateElevatorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.elevators.CreateElevatorResponse.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=100,
  serialized_end=136,
)


_GETELEVATORREQUEST = _descriptor.Descriptor(
  name='GetElevatorRequest',
  full_name='mruv.elevators.GetElevatorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.elevators.GetElevatorRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=138,
  serialized_end=170,
)


_GETELEVATORRESPONSE = _descriptor.Descriptor(
  name='GetElevatorResponse',
  full_name='mruv.elevators.GetElevatorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=172,
  serialized_end=193,
)


_UPDATEELEVATORREQUEST = _descriptor.Descriptor(
  name='UpdateElevatorRequest',
  full_name='mruv.elevators.UpdateElevatorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.elevators.UpdateElevatorRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=195,
  serialized_end=230,
)


_UPDATEELEVATORRESPONSE = _descriptor.Descriptor(
  name='UpdateElevatorResponse',
  full_name='mruv.elevators.UpdateElevatorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=232,
  serialized_end=256,
)


_DELETEELEVATORREQUEST = _descriptor.Descriptor(
  name='DeleteElevatorRequest',
  full_name='mruv.elevators.DeleteElevatorRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.elevators.DeleteElevatorRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=258,
  serialized_end=293,
)


_DELETEELEVATORRESPONSE = _descriptor.Descriptor(
  name='DeleteElevatorResponse',
  full_name='mruv.elevators.DeleteElevatorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=295,
  serialized_end=319,
)


_GETELEVATORFLOORSREQUEST = _descriptor.Descriptor(
  name='GetElevatorFloorsRequest',
  full_name='mruv.elevators.GetElevatorFloorsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.elevators.GetElevatorFloorsRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=321,
  serialized_end=359,
)


_GETELEVATORFLOORSRESPONSE = _descriptor.Descriptor(
  name='GetElevatorFloorsResponse',
  full_name='mruv.elevators.GetElevatorFloorsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=361,
  serialized_end=388,
)

DESCRIPTOR.message_types_by_name['CreateElevatorRequest'] = _CREATEELEVATORREQUEST
DESCRIPTOR.message_types_by_name['CreateElevatorResponse'] = _CREATEELEVATORRESPONSE
DESCRIPTOR.message_types_by_name['GetElevatorRequest'] = _GETELEVATORREQUEST
DESCRIPTOR.message_types_by_name['GetElevatorResponse'] = _GETELEVATORRESPONSE
DESCRIPTOR.message_types_by_name['UpdateElevatorRequest'] = _UPDATEELEVATORREQUEST
DESCRIPTOR.message_types_by_name['UpdateElevatorResponse'] = _UPDATEELEVATORRESPONSE
DESCRIPTOR.message_types_by_name['DeleteElevatorRequest'] = _DELETEELEVATORREQUEST
DESCRIPTOR.message_types_by_name['DeleteElevatorResponse'] = _DELETEELEVATORRESPONSE
DESCRIPTOR.message_types_by_name['GetElevatorFloorsRequest'] = _GETELEVATORFLOORSREQUEST
DESCRIPTOR.message_types_by_name['GetElevatorFloorsResponse'] = _GETELEVATORFLOORSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateElevatorRequest = _reflection.GeneratedProtocolMessageType('CreateElevatorRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEELEVATORREQUEST,
  '__module__' : 'elevators.elevators_pb2'
  # @@protoc_insertion_point(class_scope:mruv.elevators.CreateElevatorRequest)
  })
_sym_db.RegisterMessage(CreateElevatorRequest)

CreateElevatorResponse = _reflection.GeneratedProtocolMessageType('CreateElevatorResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEELEVATORRESPONSE,
  '__module__' : 'elevators.elevators_pb2'
  # @@protoc_insertion_point(class_scope:mruv.elevators.CreateElevatorResponse)
  })
_sym_db.RegisterMessage(CreateElevatorResponse)

GetElevatorRequest = _reflection.GeneratedProtocolMessageType('GetElevatorRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETELEVATORREQUEST,
  '__module__' : 'elevators.elevators_pb2'
  # @@protoc_insertion_point(class_scope:mruv.elevators.GetElevatorRequest)
  })
_sym_db.RegisterMessage(GetElevatorRequest)

GetElevatorResponse = _reflection.GeneratedProtocolMessageType('GetElevatorResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETELEVATORRESPONSE,
  '__module__' : 'elevators.elevators_pb2'
  # @@protoc_insertion_point(class_scope:mruv.elevators.GetElevatorResponse)
  })
_sym_db.RegisterMessage(GetElevatorResponse)

UpdateElevatorRequest = _reflection.GeneratedProtocolMessageType('UpdateElevatorRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEELEVATORREQUEST,
  '__module__' : 'elevators.elevators_pb2'
  # @@protoc_insertion_point(class_scope:mruv.elevators.UpdateElevatorRequest)
  })
_sym_db.RegisterMessage(UpdateElevatorRequest)

UpdateElevatorResponse = _reflection.GeneratedProtocolMessageType('UpdateElevatorResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEELEVATORRESPONSE,
  '__module__' : 'elevators.elevators_pb2'
  # @@protoc_insertion_point(class_scope:mruv.elevators.UpdateElevatorResponse)
  })
_sym_db.RegisterMessage(UpdateElevatorResponse)

DeleteElevatorRequest = _reflection.GeneratedProtocolMessageType('DeleteElevatorRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEELEVATORREQUEST,
  '__module__' : 'elevators.elevators_pb2'
  # @@protoc_insertion_point(class_scope:mruv.elevators.DeleteElevatorRequest)
  })
_sym_db.RegisterMessage(DeleteElevatorRequest)

DeleteElevatorResponse = _reflection.GeneratedProtocolMessageType('DeleteElevatorResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEELEVATORRESPONSE,
  '__module__' : 'elevators.elevators_pb2'
  # @@protoc_insertion_point(class_scope:mruv.elevators.DeleteElevatorResponse)
  })
_sym_db.RegisterMessage(DeleteElevatorResponse)

GetElevatorFloorsRequest = _reflection.GeneratedProtocolMessageType('GetElevatorFloorsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETELEVATORFLOORSREQUEST,
  '__module__' : 'elevators.elevators_pb2'
  # @@protoc_insertion_point(class_scope:mruv.elevators.GetElevatorFloorsRequest)
  })
_sym_db.RegisterMessage(GetElevatorFloorsRequest)

GetElevatorFloorsResponse = _reflection.GeneratedProtocolMessageType('GetElevatorFloorsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETELEVATORFLOORSRESPONSE,
  '__module__' : 'elevators.elevators_pb2'
  # @@protoc_insertion_point(class_scope:mruv.elevators.GetElevatorFloorsResponse)
  })
_sym_db.RegisterMessage(GetElevatorFloorsResponse)


DESCRIPTOR._options = None

_MRUVELEVATORSSERVICE = _descriptor.ServiceDescriptor(
  name='MruVElevatorsService',
  full_name='mruv.elevators.MruVElevatorsService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=391,
  serialized_end=1047,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateElevator',
    full_name='mruv.elevators.MruVElevatorsService.CreateElevator',
    index=0,
    containing_service=None,
    input_type=_CREATEELEVATORREQUEST,
    output_type=_CREATEELEVATORRESPONSE,
    serialized_options=b'\202\323\344\223\002\022\"\r/v1/elevators:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetElevator',
    full_name='mruv.elevators.MruVElevatorsService.GetElevator',
    index=1,
    containing_service=None,
    input_type=_GETELEVATORREQUEST,
    output_type=_GETELEVATORRESPONSE,
    serialized_options=b'\202\323\344\223\002\024\022\022/v1/elevators/{id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateElevator',
    full_name='mruv.elevators.MruVElevatorsService.UpdateElevator',
    index=2,
    containing_service=None,
    input_type=_UPDATEELEVATORREQUEST,
    output_type=_UPDATEELEVATORRESPONSE,
    serialized_options=b'\202\323\344\223\002\0272\022/v1/elevators/{id}:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteElevator',
    full_name='mruv.elevators.MruVElevatorsService.DeleteElevator',
    index=3,
    containing_service=None,
    input_type=_DELETEELEVATORREQUEST,
    output_type=_DELETEELEVATORRESPONSE,
    serialized_options=b'\202\323\344\223\002\024*\022/v1/elevators/{id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetElevatorFloors',
    full_name='mruv.elevators.MruVElevatorsService.GetElevatorFloors',
    index=4,
    containing_service=None,
    input_type=_GETELEVATORFLOORSREQUEST,
    output_type=_GETELEVATORFLOORSRESPONSE,
    serialized_options=b'\202\323\344\223\002\033\022\031/v1/elevators/{id}/floors',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MRUVELEVATORSSERVICE)

DESCRIPTOR.services_by_name['MruVElevatorsService'] = _MRUVELEVATORSSERVICE

# @@protoc_insertion_point(module_scope)
