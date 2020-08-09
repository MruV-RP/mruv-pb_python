# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gates/gates.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from objects import movable_pb2 as objects_dot_movable__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gates/gates.proto',
  package='mruv.gates',
  syntax='proto3',
  serialized_options=_b('Z#github.com/MruV-RP/mruv-pb-go/gates'),
  serialized_pb=_b('\n\x11gates/gates.proto\x12\nmruv.gates\x1a\x1cgoogle/api/annotations.proto\x1a\x15objects/movable.proto\"\x06\n\x04Gate\"T\n\x11\x43reateGateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x31\n\x0cgate_objects\x18\x02 \x03(\x0b\x32\x1b.mruv.objects.MovableObject\" \n\x12\x43reateGateResponse\x12\n\n\x02id\x18\x01 \x01(\r\"\x1c\n\x0eGetGateRequest\x12\n\n\x02id\x18\x01 \x01(\r\"r\n\x0fGetGateResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x31\n\x0cgate_objects\x18\x02 \x03(\x0b\x32\x1b.mruv.objects.MovableObject\x12\x0e\n\x06opened\x18\x03 \x01(\x08\x12\x0e\n\x06locked\x18\x04 \x01(\x08\"-\n\x11UpdateGateRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x14\n\x12UpdateGateResponse\"\x1f\n\x11\x44\x65leteGateRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x14\n\x12\x44\x65leteGateResponse\"\x19\n\x0bLockRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x0e\n\x0cLockResponse\"\x1b\n\rUnlockRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x10\n\x0eUnlockResponse\"\x19\n\x0bOpenRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x0e\n\x0cOpenResponse\"\x1a\n\x0c\x43loseRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x0f\n\rCloseResponse\"O\n\x16\x46indNearestGateRequest\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\x12\x14\n\x0cmax_distance\x18\x04 \x01(\x02\"7\n\x17\x46indNearestGateResponse\x12\n\n\x02id\x18\x01 \x01(\r\x12\x10\n\x08\x64istance\x18\x02 \x01(\x02\x32\xfb\x06\n\x10MruVGatesService\x12^\n\nCreateGate\x12\x1d.mruv.gates.CreateGateRequest\x1a\x1e.mruv.gates.CreateGateResponse\"\x11\x82\xd3\xe4\x93\x02\x0b\"\t/v1/gates\x12Z\n\x07GetGate\x12\x1a.mruv.gates.GetGateRequest\x1a\x1b.mruv.gates.GetGateResponse\"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/v1/gates/{id}\x12\x63\n\nUpdateGate\x12\x1d.mruv.gates.UpdateGateRequest\x1a\x1e.mruv.gates.UpdateGateResponse\"\x16\x82\xd3\xe4\x93\x02\x10\x32\x0e/v1/gates/{id}\x12\x63\n\nDeleteGate\x12\x1d.mruv.gates.DeleteGateRequest\x1a\x1e.mruv.gates.DeleteGateResponse\"\x16\x82\xd3\xe4\x93\x02\x10*\x0e/v1/gates/{id}\x12V\n\x04Lock\x12\x17.mruv.gates.LockRequest\x1a\x18.mruv.gates.LockResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x13/v1/gates/{id}/lock\x12^\n\x06Unlock\x12\x19.mruv.gates.UnlockRequest\x1a\x1a.mruv.gates.UnlockResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x15/v1/gates/{id}/unlock\x12V\n\x04Open\x12\x17.mruv.gates.OpenRequest\x1a\x18.mruv.gates.OpenResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x13/v1/gates/{id}/open\x12Z\n\x05\x43lose\x12\x18.mruv.gates.CloseRequest\x1a\x19.mruv.gates.CloseResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\"\x14/v1/gates/{id}/close\x12u\n\x0f\x46indNearestGate\x12\".mruv.gates.FindNearestGateRequest\x1a#.mruv.gates.FindNearestGateResponse\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/v1/gates/nearestB%Z#github.com/MruV-RP/mruv-pb-go/gatesb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,objects_dot_movable__pb2.DESCRIPTOR,])




_GATE = _descriptor.Descriptor(
  name='Gate',
  full_name='mruv.gates.Gate',
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
  serialized_start=86,
  serialized_end=92,
)


_CREATEGATEREQUEST = _descriptor.Descriptor(
  name='CreateGateRequest',
  full_name='mruv.gates.CreateGateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.gates.CreateGateRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gate_objects', full_name='mruv.gates.CreateGateRequest.gate_objects', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=94,
  serialized_end=178,
)


_CREATEGATERESPONSE = _descriptor.Descriptor(
  name='CreateGateResponse',
  full_name='mruv.gates.CreateGateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.gates.CreateGateResponse.id', index=0,
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
  serialized_start=180,
  serialized_end=212,
)


_GETGATEREQUEST = _descriptor.Descriptor(
  name='GetGateRequest',
  full_name='mruv.gates.GetGateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.gates.GetGateRequest.id', index=0,
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
  serialized_start=214,
  serialized_end=242,
)


_GETGATERESPONSE = _descriptor.Descriptor(
  name='GetGateResponse',
  full_name='mruv.gates.GetGateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.gates.GetGateResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gate_objects', full_name='mruv.gates.GetGateResponse.gate_objects', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='opened', full_name='mruv.gates.GetGateResponse.opened', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='locked', full_name='mruv.gates.GetGateResponse.locked', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=244,
  serialized_end=358,
)


_UPDATEGATEREQUEST = _descriptor.Descriptor(
  name='UpdateGateRequest',
  full_name='mruv.gates.UpdateGateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.gates.UpdateGateRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.gates.UpdateGateRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=360,
  serialized_end=405,
)


_UPDATEGATERESPONSE = _descriptor.Descriptor(
  name='UpdateGateResponse',
  full_name='mruv.gates.UpdateGateResponse',
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
  serialized_start=407,
  serialized_end=427,
)


_DELETEGATEREQUEST = _descriptor.Descriptor(
  name='DeleteGateRequest',
  full_name='mruv.gates.DeleteGateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.gates.DeleteGateRequest.id', index=0,
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
  serialized_start=429,
  serialized_end=460,
)


_DELETEGATERESPONSE = _descriptor.Descriptor(
  name='DeleteGateResponse',
  full_name='mruv.gates.DeleteGateResponse',
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
  serialized_start=462,
  serialized_end=482,
)


_LOCKREQUEST = _descriptor.Descriptor(
  name='LockRequest',
  full_name='mruv.gates.LockRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.gates.LockRequest.id', index=0,
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
  serialized_start=484,
  serialized_end=509,
)


_LOCKRESPONSE = _descriptor.Descriptor(
  name='LockResponse',
  full_name='mruv.gates.LockResponse',
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
  serialized_start=511,
  serialized_end=525,
)


_UNLOCKREQUEST = _descriptor.Descriptor(
  name='UnlockRequest',
  full_name='mruv.gates.UnlockRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.gates.UnlockRequest.id', index=0,
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
  serialized_start=527,
  serialized_end=554,
)


_UNLOCKRESPONSE = _descriptor.Descriptor(
  name='UnlockResponse',
  full_name='mruv.gates.UnlockResponse',
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
  serialized_start=556,
  serialized_end=572,
)


_OPENREQUEST = _descriptor.Descriptor(
  name='OpenRequest',
  full_name='mruv.gates.OpenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.gates.OpenRequest.id', index=0,
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
  serialized_start=574,
  serialized_end=599,
)


_OPENRESPONSE = _descriptor.Descriptor(
  name='OpenResponse',
  full_name='mruv.gates.OpenResponse',
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
  serialized_start=601,
  serialized_end=615,
)


_CLOSEREQUEST = _descriptor.Descriptor(
  name='CloseRequest',
  full_name='mruv.gates.CloseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.gates.CloseRequest.id', index=0,
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
  serialized_start=617,
  serialized_end=643,
)


_CLOSERESPONSE = _descriptor.Descriptor(
  name='CloseResponse',
  full_name='mruv.gates.CloseResponse',
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
  serialized_start=645,
  serialized_end=660,
)


_FINDNEARESTGATEREQUEST = _descriptor.Descriptor(
  name='FindNearestGateRequest',
  full_name='mruv.gates.FindNearestGateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='mruv.gates.FindNearestGateRequest.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='mruv.gates.FindNearestGateRequest.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='mruv.gates.FindNearestGateRequest.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_distance', full_name='mruv.gates.FindNearestGateRequest.max_distance', index=3,
      number=4, type=2, cpp_type=6, label=1,
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
  serialized_start=662,
  serialized_end=741,
)


_FINDNEARESTGATERESPONSE = _descriptor.Descriptor(
  name='FindNearestGateResponse',
  full_name='mruv.gates.FindNearestGateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.gates.FindNearestGateResponse.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distance', full_name='mruv.gates.FindNearestGateResponse.distance', index=1,
      number=2, type=2, cpp_type=6, label=1,
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
  serialized_start=743,
  serialized_end=798,
)

_CREATEGATEREQUEST.fields_by_name['gate_objects'].message_type = objects_dot_movable__pb2._MOVABLEOBJECT
_GETGATERESPONSE.fields_by_name['gate_objects'].message_type = objects_dot_movable__pb2._MOVABLEOBJECT
DESCRIPTOR.message_types_by_name['Gate'] = _GATE
DESCRIPTOR.message_types_by_name['CreateGateRequest'] = _CREATEGATEREQUEST
DESCRIPTOR.message_types_by_name['CreateGateResponse'] = _CREATEGATERESPONSE
DESCRIPTOR.message_types_by_name['GetGateRequest'] = _GETGATEREQUEST
DESCRIPTOR.message_types_by_name['GetGateResponse'] = _GETGATERESPONSE
DESCRIPTOR.message_types_by_name['UpdateGateRequest'] = _UPDATEGATEREQUEST
DESCRIPTOR.message_types_by_name['UpdateGateResponse'] = _UPDATEGATERESPONSE
DESCRIPTOR.message_types_by_name['DeleteGateRequest'] = _DELETEGATEREQUEST
DESCRIPTOR.message_types_by_name['DeleteGateResponse'] = _DELETEGATERESPONSE
DESCRIPTOR.message_types_by_name['LockRequest'] = _LOCKREQUEST
DESCRIPTOR.message_types_by_name['LockResponse'] = _LOCKRESPONSE
DESCRIPTOR.message_types_by_name['UnlockRequest'] = _UNLOCKREQUEST
DESCRIPTOR.message_types_by_name['UnlockResponse'] = _UNLOCKRESPONSE
DESCRIPTOR.message_types_by_name['OpenRequest'] = _OPENREQUEST
DESCRIPTOR.message_types_by_name['OpenResponse'] = _OPENRESPONSE
DESCRIPTOR.message_types_by_name['CloseRequest'] = _CLOSEREQUEST
DESCRIPTOR.message_types_by_name['CloseResponse'] = _CLOSERESPONSE
DESCRIPTOR.message_types_by_name['FindNearestGateRequest'] = _FINDNEARESTGATEREQUEST
DESCRIPTOR.message_types_by_name['FindNearestGateResponse'] = _FINDNEARESTGATERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Gate = _reflection.GeneratedProtocolMessageType('Gate', (_message.Message,), {
  'DESCRIPTOR' : _GATE,
  '__module__' : 'gates.gates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.gates.Gate)
  })
_sym_db.RegisterMessage(Gate)

CreateGateRequest = _reflection.GeneratedProtocolMessageType('CreateGateRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEGATEREQUEST,
  '__module__' : 'gates.gates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.gates.CreateGateRequest)
  })
_sym_db.RegisterMessage(CreateGateRequest)

CreateGateResponse = _reflection.GeneratedProtocolMessageType('CreateGateResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEGATERESPONSE,
  '__module__' : 'gates.gates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.gates.CreateGateResponse)
  })
_sym_db.RegisterMessage(CreateGateResponse)

GetGateRequest = _reflection.GeneratedProtocolMessageType('GetGateRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETGATEREQUEST,
  '__module__' : 'gates.gates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.gates.GetGateRequest)
  })
_sym_db.RegisterMessage(GetGateRequest)

GetGateResponse = _reflection.GeneratedProtocolMessageType('GetGateResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETGATERESPONSE,
  '__module__' : 'gates.gates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.gates.GetGateResponse)
  })
_sym_db.RegisterMessage(GetGateResponse)

UpdateGateRequest = _reflection.GeneratedProtocolMessageType('UpdateGateRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEGATEREQUEST,
  '__module__' : 'gates.gates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.gates.UpdateGateRequest)
  })
_sym_db.RegisterMessage(UpdateGateRequest)

UpdateGateResponse = _reflection.GeneratedProtocolMessageType('UpdateGateResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEGATERESPONSE,
  '__module__' : 'gates.gates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.gates.UpdateGateResponse)
  })
_sym_db.RegisterMessage(UpdateGateResponse)

DeleteGateRequest = _reflection.GeneratedProtocolMessageType('DeleteGateRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEGATEREQUEST,
  '__module__' : 'gates.gates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.gates.DeleteGateRequest)
  })
_sym_db.RegisterMessage(DeleteGateRequest)

DeleteGateResponse = _reflection.GeneratedProtocolMessageType('DeleteGateResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEGATERESPONSE,
  '__module__' : 'gates.gates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.gates.DeleteGateResponse)
  })
_sym_db.RegisterMessage(DeleteGateResponse)

LockRequest = _reflection.GeneratedProtocolMessageType('LockRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOCKREQUEST,
  '__module__' : 'gates.gates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.gates.LockRequest)
  })
_sym_db.RegisterMessage(LockRequest)

LockResponse = _reflection.GeneratedProtocolMessageType('LockResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOCKRESPONSE,
  '__module__' : 'gates.gates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.gates.LockResponse)
  })
_sym_db.RegisterMessage(LockResponse)

UnlockRequest = _reflection.GeneratedProtocolMessageType('UnlockRequest', (_message.Message,), {
  'DESCRIPTOR' : _UNLOCKREQUEST,
  '__module__' : 'gates.gates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.gates.UnlockRequest)
  })
_sym_db.RegisterMessage(UnlockRequest)

UnlockResponse = _reflection.GeneratedProtocolMessageType('UnlockResponse', (_message.Message,), {
  'DESCRIPTOR' : _UNLOCKRESPONSE,
  '__module__' : 'gates.gates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.gates.UnlockResponse)
  })
_sym_db.RegisterMessage(UnlockResponse)

OpenRequest = _reflection.GeneratedProtocolMessageType('OpenRequest', (_message.Message,), {
  'DESCRIPTOR' : _OPENREQUEST,
  '__module__' : 'gates.gates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.gates.OpenRequest)
  })
_sym_db.RegisterMessage(OpenRequest)

OpenResponse = _reflection.GeneratedProtocolMessageType('OpenResponse', (_message.Message,), {
  'DESCRIPTOR' : _OPENRESPONSE,
  '__module__' : 'gates.gates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.gates.OpenResponse)
  })
_sym_db.RegisterMessage(OpenResponse)

CloseRequest = _reflection.GeneratedProtocolMessageType('CloseRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLOSEREQUEST,
  '__module__' : 'gates.gates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.gates.CloseRequest)
  })
_sym_db.RegisterMessage(CloseRequest)

CloseResponse = _reflection.GeneratedProtocolMessageType('CloseResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLOSERESPONSE,
  '__module__' : 'gates.gates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.gates.CloseResponse)
  })
_sym_db.RegisterMessage(CloseResponse)

FindNearestGateRequest = _reflection.GeneratedProtocolMessageType('FindNearestGateRequest', (_message.Message,), {
  'DESCRIPTOR' : _FINDNEARESTGATEREQUEST,
  '__module__' : 'gates.gates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.gates.FindNearestGateRequest)
  })
_sym_db.RegisterMessage(FindNearestGateRequest)

FindNearestGateResponse = _reflection.GeneratedProtocolMessageType('FindNearestGateResponse', (_message.Message,), {
  'DESCRIPTOR' : _FINDNEARESTGATERESPONSE,
  '__module__' : 'gates.gates_pb2'
  # @@protoc_insertion_point(class_scope:mruv.gates.FindNearestGateResponse)
  })
_sym_db.RegisterMessage(FindNearestGateResponse)


DESCRIPTOR._options = None

_MRUVGATESSERVICE = _descriptor.ServiceDescriptor(
  name='MruVGatesService',
  full_name='mruv.gates.MruVGatesService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=801,
  serialized_end=1692,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateGate',
    full_name='mruv.gates.MruVGatesService.CreateGate',
    index=0,
    containing_service=None,
    input_type=_CREATEGATEREQUEST,
    output_type=_CREATEGATERESPONSE,
    serialized_options=_b('\202\323\344\223\002\013\"\t/v1/gates'),
  ),
  _descriptor.MethodDescriptor(
    name='GetGate',
    full_name='mruv.gates.MruVGatesService.GetGate',
    index=1,
    containing_service=None,
    input_type=_GETGATEREQUEST,
    output_type=_GETGATERESPONSE,
    serialized_options=_b('\202\323\344\223\002\020\022\016/v1/gates/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateGate',
    full_name='mruv.gates.MruVGatesService.UpdateGate',
    index=2,
    containing_service=None,
    input_type=_UPDATEGATEREQUEST,
    output_type=_UPDATEGATERESPONSE,
    serialized_options=_b('\202\323\344\223\002\0202\016/v1/gates/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='DeleteGate',
    full_name='mruv.gates.MruVGatesService.DeleteGate',
    index=3,
    containing_service=None,
    input_type=_DELETEGATEREQUEST,
    output_type=_DELETEGATERESPONSE,
    serialized_options=_b('\202\323\344\223\002\020*\016/v1/gates/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='Lock',
    full_name='mruv.gates.MruVGatesService.Lock',
    index=4,
    containing_service=None,
    input_type=_LOCKREQUEST,
    output_type=_LOCKRESPONSE,
    serialized_options=_b('\202\323\344\223\002\025\"\023/v1/gates/{id}/lock'),
  ),
  _descriptor.MethodDescriptor(
    name='Unlock',
    full_name='mruv.gates.MruVGatesService.Unlock',
    index=5,
    containing_service=None,
    input_type=_UNLOCKREQUEST,
    output_type=_UNLOCKRESPONSE,
    serialized_options=_b('\202\323\344\223\002\027\"\025/v1/gates/{id}/unlock'),
  ),
  _descriptor.MethodDescriptor(
    name='Open',
    full_name='mruv.gates.MruVGatesService.Open',
    index=6,
    containing_service=None,
    input_type=_OPENREQUEST,
    output_type=_OPENRESPONSE,
    serialized_options=_b('\202\323\344\223\002\025\"\023/v1/gates/{id}/open'),
  ),
  _descriptor.MethodDescriptor(
    name='Close',
    full_name='mruv.gates.MruVGatesService.Close',
    index=7,
    containing_service=None,
    input_type=_CLOSEREQUEST,
    output_type=_CLOSERESPONSE,
    serialized_options=_b('\202\323\344\223\002\026\"\024/v1/gates/{id}/close'),
  ),
  _descriptor.MethodDescriptor(
    name='FindNearestGate',
    full_name='mruv.gates.MruVGatesService.FindNearestGate',
    index=8,
    containing_service=None,
    input_type=_FINDNEARESTGATEREQUEST,
    output_type=_FINDNEARESTGATERESPONSE,
    serialized_options=_b('\202\323\344\223\002\023\022\021/v1/gates/nearest'),
  ),
])
_sym_db.RegisterServiceDescriptor(_MRUVGATESSERVICE)

DESCRIPTOR.services_by_name['MruVGatesService'] = _MRUVGATESSERVICE

# @@protoc_insertion_point(module_scope)
