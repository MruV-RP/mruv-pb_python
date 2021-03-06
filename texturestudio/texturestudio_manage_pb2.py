# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: texturestudio/texturestudio_manage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='texturestudio/texturestudio_manage.proto',
  package='texture_studio',
  syntax='proto3',
  serialized_options=b'Z+github.com/MruV-RP/mruv-pb-go/texturestudio',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(texturestudio/texturestudio_manage.proto\x12\x0etexture_studio\x1a\x1cgoogle/api/annotations.proto\"\'\n\x13\x43reateServerRequest\x12\x10\n\x08owner_id\x18\x01 \x01(\r\"0\n\x14\x43reateServerResponse\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04port\x18\x02 \x01(\r\"\x13\n\x11GetServersRequest\" \n\x12GetServersResponse\x12\n\n\x02id\x18\x01 \x03(\r\"\x11\n\x0fMyServerRequest\"\x1e\n\x10MyServerResponse\x12\n\n\x02id\x18\x01 \x01(\r\"?\n\x18TransferOwnershipRequest\x12\x11\n\tserver_id\x18\x01 \x01(\r\x12\x10\n\x08owner_id\x18\x02 \x01(\r\"\x1b\n\x19TransferOwnershipResponse\"!\n\x13\x44\x65leteServerRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x16\n\x14\x44\x65leteServerResponse2\xac\x05\n\x1bTextureStudioManagerService\x12\x7f\n\x0c\x43reateServer\x12#.texture_studio.CreateServerRequest\x1a$.texture_studio.CreateServerResponse\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/v1/texturestudio/servers:\x01*\x12v\n\nGetServers\x12!.texture_studio.GetServersRequest\x1a\".texture_studio.GetServersResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/v1/texturestudio/servers\x12s\n\x08MyServer\x12\x1f.texture_studio.MyServerRequest\x1a .texture_studio.MyServerResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/texturestudio/servers/my\x12\x9a\x01\n\x11TransferOwnership\x12(.texture_studio.TransferOwnershipRequest\x1a).texture_studio.TransferOwnershipResponse\"0\x82\xd3\xe4\x93\x02*2%/v1/texturestudio/servers/{server_id}:\x01*\x12\x81\x01\n\x0c\x44\x65leteServer\x12#.texture_studio.DeleteServerRequest\x1a$.texture_studio.DeleteServerResponse\"&\x82\xd3\xe4\x93\x02 *\x1e/v1/texturestudio/servers/{id}B-Z+github.com/MruV-RP/mruv-pb-go/texturestudiob\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CREATESERVERREQUEST = _descriptor.Descriptor(
  name='CreateServerRequest',
  full_name='texture_studio.CreateServerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner_id', full_name='texture_studio.CreateServerRequest.owner_id', index=0,
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
  serialized_start=90,
  serialized_end=129,
)


_CREATESERVERRESPONSE = _descriptor.Descriptor(
  name='CreateServerResponse',
  full_name='texture_studio.CreateServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='texture_studio.CreateServerResponse.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='texture_studio.CreateServerResponse.port', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=131,
  serialized_end=179,
)


_GETSERVERSREQUEST = _descriptor.Descriptor(
  name='GetServersRequest',
  full_name='texture_studio.GetServersRequest',
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
  serialized_start=181,
  serialized_end=200,
)


_GETSERVERSRESPONSE = _descriptor.Descriptor(
  name='GetServersResponse',
  full_name='texture_studio.GetServersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='texture_studio.GetServersResponse.id', index=0,
      number=1, type=13, cpp_type=3, label=3,
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
  serialized_start=202,
  serialized_end=234,
)


_MYSERVERREQUEST = _descriptor.Descriptor(
  name='MyServerRequest',
  full_name='texture_studio.MyServerRequest',
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
  serialized_start=236,
  serialized_end=253,
)


_MYSERVERRESPONSE = _descriptor.Descriptor(
  name='MyServerResponse',
  full_name='texture_studio.MyServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='texture_studio.MyServerResponse.id', index=0,
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
  serialized_start=255,
  serialized_end=285,
)


_TRANSFEROWNERSHIPREQUEST = _descriptor.Descriptor(
  name='TransferOwnershipRequest',
  full_name='texture_studio.TransferOwnershipRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_id', full_name='texture_studio.TransferOwnershipRequest.server_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner_id', full_name='texture_studio.TransferOwnershipRequest.owner_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=287,
  serialized_end=350,
)


_TRANSFEROWNERSHIPRESPONSE = _descriptor.Descriptor(
  name='TransferOwnershipResponse',
  full_name='texture_studio.TransferOwnershipResponse',
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
  serialized_start=352,
  serialized_end=379,
)


_DELETESERVERREQUEST = _descriptor.Descriptor(
  name='DeleteServerRequest',
  full_name='texture_studio.DeleteServerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='texture_studio.DeleteServerRequest.id', index=0,
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
  serialized_start=381,
  serialized_end=414,
)


_DELETESERVERRESPONSE = _descriptor.Descriptor(
  name='DeleteServerResponse',
  full_name='texture_studio.DeleteServerResponse',
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
  serialized_start=416,
  serialized_end=438,
)

DESCRIPTOR.message_types_by_name['CreateServerRequest'] = _CREATESERVERREQUEST
DESCRIPTOR.message_types_by_name['CreateServerResponse'] = _CREATESERVERRESPONSE
DESCRIPTOR.message_types_by_name['GetServersRequest'] = _GETSERVERSREQUEST
DESCRIPTOR.message_types_by_name['GetServersResponse'] = _GETSERVERSRESPONSE
DESCRIPTOR.message_types_by_name['MyServerRequest'] = _MYSERVERREQUEST
DESCRIPTOR.message_types_by_name['MyServerResponse'] = _MYSERVERRESPONSE
DESCRIPTOR.message_types_by_name['TransferOwnershipRequest'] = _TRANSFEROWNERSHIPREQUEST
DESCRIPTOR.message_types_by_name['TransferOwnershipResponse'] = _TRANSFEROWNERSHIPRESPONSE
DESCRIPTOR.message_types_by_name['DeleteServerRequest'] = _DELETESERVERREQUEST
DESCRIPTOR.message_types_by_name['DeleteServerResponse'] = _DELETESERVERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateServerRequest = _reflection.GeneratedProtocolMessageType('CreateServerRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESERVERREQUEST,
  '__module__' : 'texturestudio.texturestudio_manage_pb2'
  # @@protoc_insertion_point(class_scope:texture_studio.CreateServerRequest)
  })
_sym_db.RegisterMessage(CreateServerRequest)

CreateServerResponse = _reflection.GeneratedProtocolMessageType('CreateServerResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATESERVERRESPONSE,
  '__module__' : 'texturestudio.texturestudio_manage_pb2'
  # @@protoc_insertion_point(class_scope:texture_studio.CreateServerResponse)
  })
_sym_db.RegisterMessage(CreateServerResponse)

GetServersRequest = _reflection.GeneratedProtocolMessageType('GetServersRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSERVERSREQUEST,
  '__module__' : 'texturestudio.texturestudio_manage_pb2'
  # @@protoc_insertion_point(class_scope:texture_studio.GetServersRequest)
  })
_sym_db.RegisterMessage(GetServersRequest)

GetServersResponse = _reflection.GeneratedProtocolMessageType('GetServersResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSERVERSRESPONSE,
  '__module__' : 'texturestudio.texturestudio_manage_pb2'
  # @@protoc_insertion_point(class_scope:texture_studio.GetServersResponse)
  })
_sym_db.RegisterMessage(GetServersResponse)

MyServerRequest = _reflection.GeneratedProtocolMessageType('MyServerRequest', (_message.Message,), {
  'DESCRIPTOR' : _MYSERVERREQUEST,
  '__module__' : 'texturestudio.texturestudio_manage_pb2'
  # @@protoc_insertion_point(class_scope:texture_studio.MyServerRequest)
  })
_sym_db.RegisterMessage(MyServerRequest)

MyServerResponse = _reflection.GeneratedProtocolMessageType('MyServerResponse', (_message.Message,), {
  'DESCRIPTOR' : _MYSERVERRESPONSE,
  '__module__' : 'texturestudio.texturestudio_manage_pb2'
  # @@protoc_insertion_point(class_scope:texture_studio.MyServerResponse)
  })
_sym_db.RegisterMessage(MyServerResponse)

TransferOwnershipRequest = _reflection.GeneratedProtocolMessageType('TransferOwnershipRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFEROWNERSHIPREQUEST,
  '__module__' : 'texturestudio.texturestudio_manage_pb2'
  # @@protoc_insertion_point(class_scope:texture_studio.TransferOwnershipRequest)
  })
_sym_db.RegisterMessage(TransferOwnershipRequest)

TransferOwnershipResponse = _reflection.GeneratedProtocolMessageType('TransferOwnershipResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFEROWNERSHIPRESPONSE,
  '__module__' : 'texturestudio.texturestudio_manage_pb2'
  # @@protoc_insertion_point(class_scope:texture_studio.TransferOwnershipResponse)
  })
_sym_db.RegisterMessage(TransferOwnershipResponse)

DeleteServerRequest = _reflection.GeneratedProtocolMessageType('DeleteServerRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETESERVERREQUEST,
  '__module__' : 'texturestudio.texturestudio_manage_pb2'
  # @@protoc_insertion_point(class_scope:texture_studio.DeleteServerRequest)
  })
_sym_db.RegisterMessage(DeleteServerRequest)

DeleteServerResponse = _reflection.GeneratedProtocolMessageType('DeleteServerResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETESERVERRESPONSE,
  '__module__' : 'texturestudio.texturestudio_manage_pb2'
  # @@protoc_insertion_point(class_scope:texture_studio.DeleteServerResponse)
  })
_sym_db.RegisterMessage(DeleteServerResponse)


DESCRIPTOR._options = None

_TEXTURESTUDIOMANAGERSERVICE = _descriptor.ServiceDescriptor(
  name='TextureStudioManagerService',
  full_name='texture_studio.TextureStudioManagerService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=441,
  serialized_end=1125,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateServer',
    full_name='texture_studio.TextureStudioManagerService.CreateServer',
    index=0,
    containing_service=None,
    input_type=_CREATESERVERREQUEST,
    output_type=_CREATESERVERRESPONSE,
    serialized_options=b'\202\323\344\223\002\036\"\031/v1/texturestudio/servers:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetServers',
    full_name='texture_studio.TextureStudioManagerService.GetServers',
    index=1,
    containing_service=None,
    input_type=_GETSERVERSREQUEST,
    output_type=_GETSERVERSRESPONSE,
    serialized_options=b'\202\323\344\223\002\033\022\031/v1/texturestudio/servers',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MyServer',
    full_name='texture_studio.TextureStudioManagerService.MyServer',
    index=2,
    containing_service=None,
    input_type=_MYSERVERREQUEST,
    output_type=_MYSERVERRESPONSE,
    serialized_options=b'\202\323\344\223\002\036\022\034/v1/texturestudio/servers/my',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TransferOwnership',
    full_name='texture_studio.TextureStudioManagerService.TransferOwnership',
    index=3,
    containing_service=None,
    input_type=_TRANSFEROWNERSHIPREQUEST,
    output_type=_TRANSFEROWNERSHIPRESPONSE,
    serialized_options=b'\202\323\344\223\002*2%/v1/texturestudio/servers/{server_id}:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteServer',
    full_name='texture_studio.TextureStudioManagerService.DeleteServer',
    index=4,
    containing_service=None,
    input_type=_DELETESERVERREQUEST,
    output_type=_DELETESERVERRESPONSE,
    serialized_options=b'\202\323\344\223\002 *\036/v1/texturestudio/servers/{id}',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TEXTURESTUDIOMANAGERSERVICE)

DESCRIPTOR.services_by_name['TextureStudioManagerService'] = _TEXTURESTUDIOMANAGERSERVICE

# @@protoc_insertion_point(module_scope)
