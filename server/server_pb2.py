# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server/server.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from server import server_model_pb2 as server_dot_server__model__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='server/server.proto',
  package='mruv.server',
  syntax='proto3',
  serialized_options=b'Z$github.com/MruV-RP/mruv-pb-go/server',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13server/server.proto\x12\x0bmruv.server\x1a\x1cgoogle/api/annotations.proto\x1a\x19server/server_model.proto\"\x1d\n\x1bGetRegisteredServersRequest\"H\n\x1cGetRegisteredServersResponse\x12(\n\x07servers\x18\x01 \x03(\x0b\x32\x17.mruv.server.ServerInfo\"c\n\x19UpdateServerStatusRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12)\n\x06status\x18\x02 \x01(\x0e\x32\x19.mruv.server.ServerStatus\x12\x0f\n\x07players\x18\x03 \x01(\r\"\x1c\n\x1aUpdateServerStatusResponse\"\'\n\x19ServerEventsStreamRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\xaa\x01\n\x0bServerEvent\x12\x36\n\x04type\x18\x01 \x01(\x0e\x32(.mruv.server.ServerEvent.ServerEventType\"c\n\x0fServerEventType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nREGISTERED\x10\x01\x12\x0f\n\x0bSERVER_DOWN\x10\x02\x12\r\n\tSERVER_UP\x10\x03\x12\x13\n\x0fPLAYERS_CHANGED\x10\x04\x32\xad\x04\n\x11MruVServerService\x12U\n\x0eRegisterServer\x12\x17.mruv.server.ServerInfo\x1a\x15.mruv.server.ServerID\"\x13\x82\xd3\xe4\x93\x02\r\"\x0b/v1/servers\x12\x80\x01\n\x14GetRegisteredServers\x12(.mruv.server.GetRegisteredServersRequest\x1a).mruv.server.GetRegisteredServersResponse\"\x13\x82\xd3\xe4\x93\x02\r\x12\x0b/v1/servers\x12Y\n\rGetServerInfo\x12\x15.mruv.server.ServerID\x1a\x17.mruv.server.ServerInfo\"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/v1/servers/{id}\x12\x86\x01\n\x12UpdateServerStatus\x12&.mruv.server.UpdateServerStatusRequest\x1a\'.mruv.server.UpdateServerStatusResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x32\x17/v1/servers/{id}/status\x12Z\n\x12ServerEventsStream\x12&.mruv.server.ServerEventsStreamRequest\x1a\x18.mruv.server.ServerEvent\"\x00\x30\x01\x42&Z$github.com/MruV-RP/mruv-pb-go/serverb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,server_dot_server__model__pb2.DESCRIPTOR,])



_SERVEREVENT_SERVEREVENTTYPE = _descriptor.EnumDescriptor(
  name='ServerEventType',
  full_name='mruv.server.ServerEvent.ServerEventType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REGISTERED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SERVER_DOWN', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SERVER_UP', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PLAYERS_CHANGED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=442,
  serialized_end=541,
)
_sym_db.RegisterEnumDescriptor(_SERVEREVENT_SERVEREVENTTYPE)


_GETREGISTEREDSERVERSREQUEST = _descriptor.Descriptor(
  name='GetRegisteredServersRequest',
  full_name='mruv.server.GetRegisteredServersRequest',
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
  serialized_start=93,
  serialized_end=122,
)


_GETREGISTEREDSERVERSRESPONSE = _descriptor.Descriptor(
  name='GetRegisteredServersResponse',
  full_name='mruv.server.GetRegisteredServersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='servers', full_name='mruv.server.GetRegisteredServersResponse.servers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=124,
  serialized_end=196,
)


_UPDATESERVERSTATUSREQUEST = _descriptor.Descriptor(
  name='UpdateServerStatusRequest',
  full_name='mruv.server.UpdateServerStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.server.UpdateServerStatusRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='mruv.server.UpdateServerStatusRequest.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='players', full_name='mruv.server.UpdateServerStatusRequest.players', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=198,
  serialized_end=297,
)


_UPDATESERVERSTATUSRESPONSE = _descriptor.Descriptor(
  name='UpdateServerStatusResponse',
  full_name='mruv.server.UpdateServerStatusResponse',
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
  serialized_start=299,
  serialized_end=327,
)


_SERVEREVENTSSTREAMREQUEST = _descriptor.Descriptor(
  name='ServerEventsStreamRequest',
  full_name='mruv.server.ServerEventsStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.server.ServerEventsStreamRequest.id', index=0,
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
  serialized_start=329,
  serialized_end=368,
)


_SERVEREVENT = _descriptor.Descriptor(
  name='ServerEvent',
  full_name='mruv.server.ServerEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='mruv.server.ServerEvent.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SERVEREVENT_SERVEREVENTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=371,
  serialized_end=541,
)

_GETREGISTEREDSERVERSRESPONSE.fields_by_name['servers'].message_type = server_dot_server__model__pb2._SERVERINFO
_UPDATESERVERSTATUSREQUEST.fields_by_name['status'].enum_type = server_dot_server__model__pb2._SERVERSTATUS
_SERVEREVENT.fields_by_name['type'].enum_type = _SERVEREVENT_SERVEREVENTTYPE
_SERVEREVENT_SERVEREVENTTYPE.containing_type = _SERVEREVENT
DESCRIPTOR.message_types_by_name['GetRegisteredServersRequest'] = _GETREGISTEREDSERVERSREQUEST
DESCRIPTOR.message_types_by_name['GetRegisteredServersResponse'] = _GETREGISTEREDSERVERSRESPONSE
DESCRIPTOR.message_types_by_name['UpdateServerStatusRequest'] = _UPDATESERVERSTATUSREQUEST
DESCRIPTOR.message_types_by_name['UpdateServerStatusResponse'] = _UPDATESERVERSTATUSRESPONSE
DESCRIPTOR.message_types_by_name['ServerEventsStreamRequest'] = _SERVEREVENTSSTREAMREQUEST
DESCRIPTOR.message_types_by_name['ServerEvent'] = _SERVEREVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetRegisteredServersRequest = _reflection.GeneratedProtocolMessageType('GetRegisteredServersRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETREGISTEREDSERVERSREQUEST,
  '__module__' : 'server.server_pb2'
  # @@protoc_insertion_point(class_scope:mruv.server.GetRegisteredServersRequest)
  })
_sym_db.RegisterMessage(GetRegisteredServersRequest)

GetRegisteredServersResponse = _reflection.GeneratedProtocolMessageType('GetRegisteredServersResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETREGISTEREDSERVERSRESPONSE,
  '__module__' : 'server.server_pb2'
  # @@protoc_insertion_point(class_scope:mruv.server.GetRegisteredServersResponse)
  })
_sym_db.RegisterMessage(GetRegisteredServersResponse)

UpdateServerStatusRequest = _reflection.GeneratedProtocolMessageType('UpdateServerStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESERVERSTATUSREQUEST,
  '__module__' : 'server.server_pb2'
  # @@protoc_insertion_point(class_scope:mruv.server.UpdateServerStatusRequest)
  })
_sym_db.RegisterMessage(UpdateServerStatusRequest)

UpdateServerStatusResponse = _reflection.GeneratedProtocolMessageType('UpdateServerStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESERVERSTATUSRESPONSE,
  '__module__' : 'server.server_pb2'
  # @@protoc_insertion_point(class_scope:mruv.server.UpdateServerStatusResponse)
  })
_sym_db.RegisterMessage(UpdateServerStatusResponse)

ServerEventsStreamRequest = _reflection.GeneratedProtocolMessageType('ServerEventsStreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVEREVENTSSTREAMREQUEST,
  '__module__' : 'server.server_pb2'
  # @@protoc_insertion_point(class_scope:mruv.server.ServerEventsStreamRequest)
  })
_sym_db.RegisterMessage(ServerEventsStreamRequest)

ServerEvent = _reflection.GeneratedProtocolMessageType('ServerEvent', (_message.Message,), {
  'DESCRIPTOR' : _SERVEREVENT,
  '__module__' : 'server.server_pb2'
  # @@protoc_insertion_point(class_scope:mruv.server.ServerEvent)
  })
_sym_db.RegisterMessage(ServerEvent)


DESCRIPTOR._options = None

_MRUVSERVERSERVICE = _descriptor.ServiceDescriptor(
  name='MruVServerService',
  full_name='mruv.server.MruVServerService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=544,
  serialized_end=1101,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterServer',
    full_name='mruv.server.MruVServerService.RegisterServer',
    index=0,
    containing_service=None,
    input_type=server_dot_server__model__pb2._SERVERINFO,
    output_type=server_dot_server__model__pb2._SERVERID,
    serialized_options=b'\202\323\344\223\002\r\"\013/v1/servers',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetRegisteredServers',
    full_name='mruv.server.MruVServerService.GetRegisteredServers',
    index=1,
    containing_service=None,
    input_type=_GETREGISTEREDSERVERSREQUEST,
    output_type=_GETREGISTEREDSERVERSRESPONSE,
    serialized_options=b'\202\323\344\223\002\r\022\013/v1/servers',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetServerInfo',
    full_name='mruv.server.MruVServerService.GetServerInfo',
    index=2,
    containing_service=None,
    input_type=server_dot_server__model__pb2._SERVERID,
    output_type=server_dot_server__model__pb2._SERVERINFO,
    serialized_options=b'\202\323\344\223\002\022\022\020/v1/servers/{id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateServerStatus',
    full_name='mruv.server.MruVServerService.UpdateServerStatus',
    index=3,
    containing_service=None,
    input_type=_UPDATESERVERSTATUSREQUEST,
    output_type=_UPDATESERVERSTATUSRESPONSE,
    serialized_options=b'\202\323\344\223\002\0312\027/v1/servers/{id}/status',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ServerEventsStream',
    full_name='mruv.server.MruVServerService.ServerEventsStream',
    index=4,
    containing_service=None,
    input_type=_SERVEREVENTSSTREAMREQUEST,
    output_type=_SERVEREVENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MRUVSERVERSERVICE)

DESCRIPTOR.services_by_name['MruVServerService'] = _MRUVSERVERSERVICE

# @@protoc_insertion_point(module_scope)
