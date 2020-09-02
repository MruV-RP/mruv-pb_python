# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: entrances/entrances.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from spots import spots_pb2 as spots_dot_spots__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='entrances/entrances.proto',
  package='mruv.entrances',
  syntax='proto3',
  serialized_options=_b('Z\'github.com/MruV-RP/mruv-pb-go/entrances'),
  serialized_pb=_b('\n\x19\x65ntrances/entrances.proto\x12\x0emruv.entrances\x1a\x1cgoogle/api/annotations.proto\x1a\x11spots/spots.proto\"U\n\x08\x45ntrance\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1d\n\x03out\x18\x02 \x01(\x0b\x32\x10.mruv.spots.Spot\x12\x1c\n\x02in\x18\x03 \x01(\x0b\x32\x10.mruv.spots.Spot\"b\n\x15\x43reateEntranceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1d\n\x03out\x18\x02 \x01(\x0b\x32\x10.mruv.spots.Spot\x12\x1c\n\x02in\x18\x03 \x01(\x0b\x32\x10.mruv.spots.Spot\"$\n\x16\x43reateEntranceResponse\x12\n\n\x02id\x18\x01 \x01(\r\" \n\x12GetEntranceRequest\x12\n\n\x02id\x18\x01 \x01(\r\"j\n\x13GetEntranceResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12!\n\x07in_spot\x18\x02 \x01(\x0b\x32\x10.mruv.spots.Spot\x12\"\n\x08out_spot\x18\x03 \x01(\x0b\x32\x10.mruv.spots.Spot\"L\n\x15UpdateEntranceRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x12\n\nin_spot_id\x18\x02 \x01(\r\x12\x13\n\x0bout_spot_id\x18\x03 \x01(\r\"\x18\n\x16UpdateEntranceResponse\"#\n\x15\x44\x65leteEntranceRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x18\n\x16\x44\x65leteEntranceResponse\"\x19\n\x0bLockRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x0e\n\x0cLockResponse\"\x1b\n\rUnlockRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x10\n\x0eUnlockResponse\"S\n\x1a\x46indNearestEntranceRequest\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\x12\x14\n\x0cmax_distance\x18\x04 \x01(\x02\"K\n\x1b\x46indNearestEntranceResponse\x12\n\n\x02id\x18\x01 \x01(\r\x12\x10\n\x08\x64istance\x18\x02 \x01(\x02\x12\x0e\n\x06inside\x18\x03 \x01(\x08\"\x1a\n\x0c\x45nterRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x0f\n\rEnterResponse\"\x19\n\x0b\x45xitRequest\x12\n\n\x02id\x18\x01 \x01(\r\"\x0e\n\x0c\x45xitResponse\".\n\x18\x46\x65tchAllEntrancesRequest\x12\x12\n\nchunk_size\x18\x01 \x01(\r\"\xb4\x01\n\x19\x46\x65tchAllEntrancesResponse\x12K\n\tentrances\x18\x01 \x03(\x0b\x32\x38.mruv.entrances.FetchAllEntrancesResponse.EntrancesEntry\x1aJ\n\x0e\x45ntrancesEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.mruv.entrances.Entrance:\x02\x38\x01\x32\x8d\t\n\x14MruVEntrancesService\x12v\n\x0e\x43reateEntrance\x12%.mruv.entrances.CreateEntranceRequest\x1a&.mruv.entrances.CreateEntranceResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\"\r/v1/entrances\x12r\n\x0bGetEntrance\x12\".mruv.entrances.GetEntranceRequest\x1a#.mruv.entrances.GetEntranceResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/v1/entrances/{id}\x12{\n\x0eUpdateEntrance\x12%.mruv.entrances.UpdateEntranceRequest\x1a&.mruv.entrances.UpdateEntranceResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\x32\x12/v1/entrances/{id}\x12{\n\x0e\x44\x65leteEntrance\x12%.mruv.entrances.DeleteEntranceRequest\x1a&.mruv.entrances.DeleteEntranceResponse\"\x1a\x82\xd3\xe4\x93\x02\x14*\x12/v1/entrances/{id}\x12\x62\n\x04Lock\x12\x1b.mruv.entrances.LockRequest\x1a\x1c.mruv.entrances.LockResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x17/v1/entrances/{id}/lock\x12j\n\x06Unlock\x12\x1d.mruv.entrances.UnlockRequest\x1a\x1e.mruv.entrances.UnlockResponse\"!\x82\xd3\xe4\x93\x02\x1b\"\x19/v1/entrances/{id}/unlock\x12\x8d\x01\n\x13\x46indNearestEntrance\x12*.mruv.entrances.FindNearestEntranceRequest\x1a+.mruv.entrances.FindNearestEntranceResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/v1/entrances/nearest\x12\x66\n\x05\x45nter\x12\x1c.mruv.entrances.EnterRequest\x1a\x1d.mruv.entrances.EnterResponse\" \x82\xd3\xe4\x93\x02\x1a\"\x18/v1/entrances/{id}/enter\x12\x62\n\x04\x45xit\x12\x1b.mruv.entrances.ExitRequest\x1a\x1c.mruv.entrances.ExitResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x17/v1/entrances/{id}/exit\x12\x63\n\x08\x46\x65tchAll\x12(.mruv.entrances.FetchAllEntrancesRequest\x1a).mruv.entrances.FetchAllEntrancesResponse\"\x00\x30\x01\x42)Z\'github.com/MruV-RP/mruv-pb-go/entrancesb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,spots_dot_spots__pb2.DESCRIPTOR,])




_ENTRANCE = _descriptor.Descriptor(
  name='Entrance',
  full_name='mruv.entrances.Entrance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.entrances.Entrance.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='out', full_name='mruv.entrances.Entrance.out', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='in', full_name='mruv.entrances.Entrance.in', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_end=179,
)


_CREATEENTRANCEREQUEST = _descriptor.Descriptor(
  name='CreateEntranceRequest',
  full_name='mruv.entrances.CreateEntranceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.entrances.CreateEntranceRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='out', full_name='mruv.entrances.CreateEntranceRequest.out', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='in', full_name='mruv.entrances.CreateEntranceRequest.in', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=181,
  serialized_end=279,
)


_CREATEENTRANCERESPONSE = _descriptor.Descriptor(
  name='CreateEntranceResponse',
  full_name='mruv.entrances.CreateEntranceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.entrances.CreateEntranceResponse.id', index=0,
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
  serialized_start=281,
  serialized_end=317,
)


_GETENTRANCEREQUEST = _descriptor.Descriptor(
  name='GetEntranceRequest',
  full_name='mruv.entrances.GetEntranceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.entrances.GetEntranceRequest.id', index=0,
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
  serialized_start=319,
  serialized_end=351,
)


_GETENTRANCERESPONSE = _descriptor.Descriptor(
  name='GetEntranceResponse',
  full_name='mruv.entrances.GetEntranceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.entrances.GetEntranceResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='in_spot', full_name='mruv.entrances.GetEntranceResponse.in_spot', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='out_spot', full_name='mruv.entrances.GetEntranceResponse.out_spot', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=353,
  serialized_end=459,
)


_UPDATEENTRANCEREQUEST = _descriptor.Descriptor(
  name='UpdateEntranceRequest',
  full_name='mruv.entrances.UpdateEntranceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.entrances.UpdateEntranceRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='in_spot_id', full_name='mruv.entrances.UpdateEntranceRequest.in_spot_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='out_spot_id', full_name='mruv.entrances.UpdateEntranceRequest.out_spot_id', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=461,
  serialized_end=537,
)


_UPDATEENTRANCERESPONSE = _descriptor.Descriptor(
  name='UpdateEntranceResponse',
  full_name='mruv.entrances.UpdateEntranceResponse',
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
  serialized_start=539,
  serialized_end=563,
)


_DELETEENTRANCEREQUEST = _descriptor.Descriptor(
  name='DeleteEntranceRequest',
  full_name='mruv.entrances.DeleteEntranceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.entrances.DeleteEntranceRequest.id', index=0,
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
  serialized_start=565,
  serialized_end=600,
)


_DELETEENTRANCERESPONSE = _descriptor.Descriptor(
  name='DeleteEntranceResponse',
  full_name='mruv.entrances.DeleteEntranceResponse',
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
  serialized_start=602,
  serialized_end=626,
)


_LOCKREQUEST = _descriptor.Descriptor(
  name='LockRequest',
  full_name='mruv.entrances.LockRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.entrances.LockRequest.id', index=0,
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
  serialized_start=628,
  serialized_end=653,
)


_LOCKRESPONSE = _descriptor.Descriptor(
  name='LockResponse',
  full_name='mruv.entrances.LockResponse',
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
  serialized_start=655,
  serialized_end=669,
)


_UNLOCKREQUEST = _descriptor.Descriptor(
  name='UnlockRequest',
  full_name='mruv.entrances.UnlockRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.entrances.UnlockRequest.id', index=0,
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
  serialized_start=671,
  serialized_end=698,
)


_UNLOCKRESPONSE = _descriptor.Descriptor(
  name='UnlockResponse',
  full_name='mruv.entrances.UnlockResponse',
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
  serialized_start=700,
  serialized_end=716,
)


_FINDNEARESTENTRANCEREQUEST = _descriptor.Descriptor(
  name='FindNearestEntranceRequest',
  full_name='mruv.entrances.FindNearestEntranceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='mruv.entrances.FindNearestEntranceRequest.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='mruv.entrances.FindNearestEntranceRequest.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='mruv.entrances.FindNearestEntranceRequest.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_distance', full_name='mruv.entrances.FindNearestEntranceRequest.max_distance', index=3,
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
  serialized_start=718,
  serialized_end=801,
)


_FINDNEARESTENTRANCERESPONSE = _descriptor.Descriptor(
  name='FindNearestEntranceResponse',
  full_name='mruv.entrances.FindNearestEntranceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.entrances.FindNearestEntranceResponse.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distance', full_name='mruv.entrances.FindNearestEntranceResponse.distance', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inside', full_name='mruv.entrances.FindNearestEntranceResponse.inside', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=803,
  serialized_end=878,
)


_ENTERREQUEST = _descriptor.Descriptor(
  name='EnterRequest',
  full_name='mruv.entrances.EnterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.entrances.EnterRequest.id', index=0,
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
  serialized_start=880,
  serialized_end=906,
)


_ENTERRESPONSE = _descriptor.Descriptor(
  name='EnterResponse',
  full_name='mruv.entrances.EnterResponse',
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
  serialized_start=908,
  serialized_end=923,
)


_EXITREQUEST = _descriptor.Descriptor(
  name='ExitRequest',
  full_name='mruv.entrances.ExitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.entrances.ExitRequest.id', index=0,
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
  serialized_start=925,
  serialized_end=950,
)


_EXITRESPONSE = _descriptor.Descriptor(
  name='ExitResponse',
  full_name='mruv.entrances.ExitResponse',
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
  serialized_start=952,
  serialized_end=966,
)


_FETCHALLENTRANCESREQUEST = _descriptor.Descriptor(
  name='FetchAllEntrancesRequest',
  full_name='mruv.entrances.FetchAllEntrancesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chunk_size', full_name='mruv.entrances.FetchAllEntrancesRequest.chunk_size', index=0,
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
  serialized_start=968,
  serialized_end=1014,
)


_FETCHALLENTRANCESRESPONSE_ENTRANCESENTRY = _descriptor.Descriptor(
  name='EntrancesEntry',
  full_name='mruv.entrances.FetchAllEntrancesResponse.EntrancesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='mruv.entrances.FetchAllEntrancesResponse.EntrancesEntry.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='mruv.entrances.FetchAllEntrancesResponse.EntrancesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1123,
  serialized_end=1197,
)

_FETCHALLENTRANCESRESPONSE = _descriptor.Descriptor(
  name='FetchAllEntrancesResponse',
  full_name='mruv.entrances.FetchAllEntrancesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entrances', full_name='mruv.entrances.FetchAllEntrancesResponse.entrances', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FETCHALLENTRANCESRESPONSE_ENTRANCESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1017,
  serialized_end=1197,
)

_ENTRANCE.fields_by_name['out'].message_type = spots_dot_spots__pb2._SPOT
_ENTRANCE.fields_by_name['in'].message_type = spots_dot_spots__pb2._SPOT
_CREATEENTRANCEREQUEST.fields_by_name['out'].message_type = spots_dot_spots__pb2._SPOT
_CREATEENTRANCEREQUEST.fields_by_name['in'].message_type = spots_dot_spots__pb2._SPOT
_GETENTRANCERESPONSE.fields_by_name['in_spot'].message_type = spots_dot_spots__pb2._SPOT
_GETENTRANCERESPONSE.fields_by_name['out_spot'].message_type = spots_dot_spots__pb2._SPOT
_FETCHALLENTRANCESRESPONSE_ENTRANCESENTRY.fields_by_name['value'].message_type = _ENTRANCE
_FETCHALLENTRANCESRESPONSE_ENTRANCESENTRY.containing_type = _FETCHALLENTRANCESRESPONSE
_FETCHALLENTRANCESRESPONSE.fields_by_name['entrances'].message_type = _FETCHALLENTRANCESRESPONSE_ENTRANCESENTRY
DESCRIPTOR.message_types_by_name['Entrance'] = _ENTRANCE
DESCRIPTOR.message_types_by_name['CreateEntranceRequest'] = _CREATEENTRANCEREQUEST
DESCRIPTOR.message_types_by_name['CreateEntranceResponse'] = _CREATEENTRANCERESPONSE
DESCRIPTOR.message_types_by_name['GetEntranceRequest'] = _GETENTRANCEREQUEST
DESCRIPTOR.message_types_by_name['GetEntranceResponse'] = _GETENTRANCERESPONSE
DESCRIPTOR.message_types_by_name['UpdateEntranceRequest'] = _UPDATEENTRANCEREQUEST
DESCRIPTOR.message_types_by_name['UpdateEntranceResponse'] = _UPDATEENTRANCERESPONSE
DESCRIPTOR.message_types_by_name['DeleteEntranceRequest'] = _DELETEENTRANCEREQUEST
DESCRIPTOR.message_types_by_name['DeleteEntranceResponse'] = _DELETEENTRANCERESPONSE
DESCRIPTOR.message_types_by_name['LockRequest'] = _LOCKREQUEST
DESCRIPTOR.message_types_by_name['LockResponse'] = _LOCKRESPONSE
DESCRIPTOR.message_types_by_name['UnlockRequest'] = _UNLOCKREQUEST
DESCRIPTOR.message_types_by_name['UnlockResponse'] = _UNLOCKRESPONSE
DESCRIPTOR.message_types_by_name['FindNearestEntranceRequest'] = _FINDNEARESTENTRANCEREQUEST
DESCRIPTOR.message_types_by_name['FindNearestEntranceResponse'] = _FINDNEARESTENTRANCERESPONSE
DESCRIPTOR.message_types_by_name['EnterRequest'] = _ENTERREQUEST
DESCRIPTOR.message_types_by_name['EnterResponse'] = _ENTERRESPONSE
DESCRIPTOR.message_types_by_name['ExitRequest'] = _EXITREQUEST
DESCRIPTOR.message_types_by_name['ExitResponse'] = _EXITRESPONSE
DESCRIPTOR.message_types_by_name['FetchAllEntrancesRequest'] = _FETCHALLENTRANCESREQUEST
DESCRIPTOR.message_types_by_name['FetchAllEntrancesResponse'] = _FETCHALLENTRANCESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Entrance = _reflection.GeneratedProtocolMessageType('Entrance', (_message.Message,), {
  'DESCRIPTOR' : _ENTRANCE,
  '__module__' : 'entrances.entrances_pb2'
  # @@protoc_insertion_point(class_scope:mruv.entrances.Entrance)
  })
_sym_db.RegisterMessage(Entrance)

CreateEntranceRequest = _reflection.GeneratedProtocolMessageType('CreateEntranceRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEENTRANCEREQUEST,
  '__module__' : 'entrances.entrances_pb2'
  # @@protoc_insertion_point(class_scope:mruv.entrances.CreateEntranceRequest)
  })
_sym_db.RegisterMessage(CreateEntranceRequest)

CreateEntranceResponse = _reflection.GeneratedProtocolMessageType('CreateEntranceResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEENTRANCERESPONSE,
  '__module__' : 'entrances.entrances_pb2'
  # @@protoc_insertion_point(class_scope:mruv.entrances.CreateEntranceResponse)
  })
_sym_db.RegisterMessage(CreateEntranceResponse)

GetEntranceRequest = _reflection.GeneratedProtocolMessageType('GetEntranceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETENTRANCEREQUEST,
  '__module__' : 'entrances.entrances_pb2'
  # @@protoc_insertion_point(class_scope:mruv.entrances.GetEntranceRequest)
  })
_sym_db.RegisterMessage(GetEntranceRequest)

GetEntranceResponse = _reflection.GeneratedProtocolMessageType('GetEntranceResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETENTRANCERESPONSE,
  '__module__' : 'entrances.entrances_pb2'
  # @@protoc_insertion_point(class_scope:mruv.entrances.GetEntranceResponse)
  })
_sym_db.RegisterMessage(GetEntranceResponse)

UpdateEntranceRequest = _reflection.GeneratedProtocolMessageType('UpdateEntranceRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEENTRANCEREQUEST,
  '__module__' : 'entrances.entrances_pb2'
  # @@protoc_insertion_point(class_scope:mruv.entrances.UpdateEntranceRequest)
  })
_sym_db.RegisterMessage(UpdateEntranceRequest)

UpdateEntranceResponse = _reflection.GeneratedProtocolMessageType('UpdateEntranceResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEENTRANCERESPONSE,
  '__module__' : 'entrances.entrances_pb2'
  # @@protoc_insertion_point(class_scope:mruv.entrances.UpdateEntranceResponse)
  })
_sym_db.RegisterMessage(UpdateEntranceResponse)

DeleteEntranceRequest = _reflection.GeneratedProtocolMessageType('DeleteEntranceRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEENTRANCEREQUEST,
  '__module__' : 'entrances.entrances_pb2'
  # @@protoc_insertion_point(class_scope:mruv.entrances.DeleteEntranceRequest)
  })
_sym_db.RegisterMessage(DeleteEntranceRequest)

DeleteEntranceResponse = _reflection.GeneratedProtocolMessageType('DeleteEntranceResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEENTRANCERESPONSE,
  '__module__' : 'entrances.entrances_pb2'
  # @@protoc_insertion_point(class_scope:mruv.entrances.DeleteEntranceResponse)
  })
_sym_db.RegisterMessage(DeleteEntranceResponse)

LockRequest = _reflection.GeneratedProtocolMessageType('LockRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOCKREQUEST,
  '__module__' : 'entrances.entrances_pb2'
  # @@protoc_insertion_point(class_scope:mruv.entrances.LockRequest)
  })
_sym_db.RegisterMessage(LockRequest)

LockResponse = _reflection.GeneratedProtocolMessageType('LockResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOCKRESPONSE,
  '__module__' : 'entrances.entrances_pb2'
  # @@protoc_insertion_point(class_scope:mruv.entrances.LockResponse)
  })
_sym_db.RegisterMessage(LockResponse)

UnlockRequest = _reflection.GeneratedProtocolMessageType('UnlockRequest', (_message.Message,), {
  'DESCRIPTOR' : _UNLOCKREQUEST,
  '__module__' : 'entrances.entrances_pb2'
  # @@protoc_insertion_point(class_scope:mruv.entrances.UnlockRequest)
  })
_sym_db.RegisterMessage(UnlockRequest)

UnlockResponse = _reflection.GeneratedProtocolMessageType('UnlockResponse', (_message.Message,), {
  'DESCRIPTOR' : _UNLOCKRESPONSE,
  '__module__' : 'entrances.entrances_pb2'
  # @@protoc_insertion_point(class_scope:mruv.entrances.UnlockResponse)
  })
_sym_db.RegisterMessage(UnlockResponse)

FindNearestEntranceRequest = _reflection.GeneratedProtocolMessageType('FindNearestEntranceRequest', (_message.Message,), {
  'DESCRIPTOR' : _FINDNEARESTENTRANCEREQUEST,
  '__module__' : 'entrances.entrances_pb2'
  # @@protoc_insertion_point(class_scope:mruv.entrances.FindNearestEntranceRequest)
  })
_sym_db.RegisterMessage(FindNearestEntranceRequest)

FindNearestEntranceResponse = _reflection.GeneratedProtocolMessageType('FindNearestEntranceResponse', (_message.Message,), {
  'DESCRIPTOR' : _FINDNEARESTENTRANCERESPONSE,
  '__module__' : 'entrances.entrances_pb2'
  # @@protoc_insertion_point(class_scope:mruv.entrances.FindNearestEntranceResponse)
  })
_sym_db.RegisterMessage(FindNearestEntranceResponse)

EnterRequest = _reflection.GeneratedProtocolMessageType('EnterRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENTERREQUEST,
  '__module__' : 'entrances.entrances_pb2'
  # @@protoc_insertion_point(class_scope:mruv.entrances.EnterRequest)
  })
_sym_db.RegisterMessage(EnterRequest)

EnterResponse = _reflection.GeneratedProtocolMessageType('EnterResponse', (_message.Message,), {
  'DESCRIPTOR' : _ENTERRESPONSE,
  '__module__' : 'entrances.entrances_pb2'
  # @@protoc_insertion_point(class_scope:mruv.entrances.EnterResponse)
  })
_sym_db.RegisterMessage(EnterResponse)

ExitRequest = _reflection.GeneratedProtocolMessageType('ExitRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXITREQUEST,
  '__module__' : 'entrances.entrances_pb2'
  # @@protoc_insertion_point(class_scope:mruv.entrances.ExitRequest)
  })
_sym_db.RegisterMessage(ExitRequest)

ExitResponse = _reflection.GeneratedProtocolMessageType('ExitResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXITRESPONSE,
  '__module__' : 'entrances.entrances_pb2'
  # @@protoc_insertion_point(class_scope:mruv.entrances.ExitResponse)
  })
_sym_db.RegisterMessage(ExitResponse)

FetchAllEntrancesRequest = _reflection.GeneratedProtocolMessageType('FetchAllEntrancesRequest', (_message.Message,), {
  'DESCRIPTOR' : _FETCHALLENTRANCESREQUEST,
  '__module__' : 'entrances.entrances_pb2'
  # @@protoc_insertion_point(class_scope:mruv.entrances.FetchAllEntrancesRequest)
  })
_sym_db.RegisterMessage(FetchAllEntrancesRequest)

FetchAllEntrancesResponse = _reflection.GeneratedProtocolMessageType('FetchAllEntrancesResponse', (_message.Message,), {

  'EntrancesEntry' : _reflection.GeneratedProtocolMessageType('EntrancesEntry', (_message.Message,), {
    'DESCRIPTOR' : _FETCHALLENTRANCESRESPONSE_ENTRANCESENTRY,
    '__module__' : 'entrances.entrances_pb2'
    # @@protoc_insertion_point(class_scope:mruv.entrances.FetchAllEntrancesResponse.EntrancesEntry)
    })
  ,
  'DESCRIPTOR' : _FETCHALLENTRANCESRESPONSE,
  '__module__' : 'entrances.entrances_pb2'
  # @@protoc_insertion_point(class_scope:mruv.entrances.FetchAllEntrancesResponse)
  })
_sym_db.RegisterMessage(FetchAllEntrancesResponse)
_sym_db.RegisterMessage(FetchAllEntrancesResponse.EntrancesEntry)


DESCRIPTOR._options = None
_FETCHALLENTRANCESRESPONSE_ENTRANCESENTRY._options = None

_MRUVENTRANCESSERVICE = _descriptor.ServiceDescriptor(
  name='MruVEntrancesService',
  full_name='mruv.entrances.MruVEntrancesService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1200,
  serialized_end=2365,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateEntrance',
    full_name='mruv.entrances.MruVEntrancesService.CreateEntrance',
    index=0,
    containing_service=None,
    input_type=_CREATEENTRANCEREQUEST,
    output_type=_CREATEENTRANCERESPONSE,
    serialized_options=_b('\202\323\344\223\002\017\"\r/v1/entrances'),
  ),
  _descriptor.MethodDescriptor(
    name='GetEntrance',
    full_name='mruv.entrances.MruVEntrancesService.GetEntrance',
    index=1,
    containing_service=None,
    input_type=_GETENTRANCEREQUEST,
    output_type=_GETENTRANCERESPONSE,
    serialized_options=_b('\202\323\344\223\002\024\022\022/v1/entrances/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateEntrance',
    full_name='mruv.entrances.MruVEntrancesService.UpdateEntrance',
    index=2,
    containing_service=None,
    input_type=_UPDATEENTRANCEREQUEST,
    output_type=_UPDATEENTRANCERESPONSE,
    serialized_options=_b('\202\323\344\223\002\0242\022/v1/entrances/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='DeleteEntrance',
    full_name='mruv.entrances.MruVEntrancesService.DeleteEntrance',
    index=3,
    containing_service=None,
    input_type=_DELETEENTRANCEREQUEST,
    output_type=_DELETEENTRANCERESPONSE,
    serialized_options=_b('\202\323\344\223\002\024*\022/v1/entrances/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='Lock',
    full_name='mruv.entrances.MruVEntrancesService.Lock',
    index=4,
    containing_service=None,
    input_type=_LOCKREQUEST,
    output_type=_LOCKRESPONSE,
    serialized_options=_b('\202\323\344\223\002\031\"\027/v1/entrances/{id}/lock'),
  ),
  _descriptor.MethodDescriptor(
    name='Unlock',
    full_name='mruv.entrances.MruVEntrancesService.Unlock',
    index=5,
    containing_service=None,
    input_type=_UNLOCKREQUEST,
    output_type=_UNLOCKRESPONSE,
    serialized_options=_b('\202\323\344\223\002\033\"\031/v1/entrances/{id}/unlock'),
  ),
  _descriptor.MethodDescriptor(
    name='FindNearestEntrance',
    full_name='mruv.entrances.MruVEntrancesService.FindNearestEntrance',
    index=6,
    containing_service=None,
    input_type=_FINDNEARESTENTRANCEREQUEST,
    output_type=_FINDNEARESTENTRANCERESPONSE,
    serialized_options=_b('\202\323\344\223\002\027\022\025/v1/entrances/nearest'),
  ),
  _descriptor.MethodDescriptor(
    name='Enter',
    full_name='mruv.entrances.MruVEntrancesService.Enter',
    index=7,
    containing_service=None,
    input_type=_ENTERREQUEST,
    output_type=_ENTERRESPONSE,
    serialized_options=_b('\202\323\344\223\002\032\"\030/v1/entrances/{id}/enter'),
  ),
  _descriptor.MethodDescriptor(
    name='Exit',
    full_name='mruv.entrances.MruVEntrancesService.Exit',
    index=8,
    containing_service=None,
    input_type=_EXITREQUEST,
    output_type=_EXITRESPONSE,
    serialized_options=_b('\202\323\344\223\002\031\"\027/v1/entrances/{id}/exit'),
  ),
  _descriptor.MethodDescriptor(
    name='FetchAll',
    full_name='mruv.entrances.MruVEntrancesService.FetchAll',
    index=9,
    containing_service=None,
    input_type=_FETCHALLENTRANCESREQUEST,
    output_type=_FETCHALLENTRANCESRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MRUVENTRANCESSERVICE)

DESCRIPTOR.services_by_name['MruVEntrancesService'] = _MRUVENTRANCESSERVICE

# @@protoc_insertion_point(module_scope)
