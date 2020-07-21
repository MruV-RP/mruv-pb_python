# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: economy/economy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='economy/economy.proto',
  package='mruv.economy',
  syntax='proto3',
  serialized_options=_b('Z%github.com/MruV-RP/mruv-pb-go/economy'),
  serialized_pb=_b('\n\x15\x65\x63onomy/economy.proto\x12\x0cmruv.economy\x1a\x1cgoogle/api/annotations.proto\"\x90\x01\n\x16RegisterProductRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tfull_name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x13\n\x0bprice_class\x18\x04 \x01(\r\x12\x13\n\x0bprice_ratio\x18\x05 \x01(\x02\x12\x16\n\x0estarting_price\x18\x06 \x01(\r\"%\n\x17RegisterProductResponse\x12\n\n\x02id\x18\x01 \x01(\r\"-\n\x11GetProductRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x9b\x01\n\x12GetProductResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tfull_name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x13\n\x0bprice_class\x18\x04 \x01(\r\x12\x13\n\x0bprice_ratio\x18\x05 \x01(\x02\x12\x16\n\x0estarting_price\x18\x06 \x01(\r\x12\r\n\x05price\x18\x07 \x01(\r\"\x82\x01\n\x14UpdateProductRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tfull_name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x13\n\x0bprice_class\x18\x05 \x01(\r\x12\x13\n\x0bprice_ratio\x18\x06 \x01(\x02\"\x17\n\x15UpdateProductResponse\"A\n\x12UpdatePriceRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tnew_price\x18\x03 \x01(\r\"\x15\n\x13UpdatePriceResponse\"0\n\x14\x44\x65leteProductRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x17\n\x15\x44\x65leteProductResponse\"+\n\x0fGetPriceRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\"!\n\x10GetPriceResponse\x12\r\n\x05price\x18\x01 \x01(\r\"-\n\x11\x42uyProductRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x14\n\x12\x42uyProductResponse\"/\n\x13WatchProductRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xc9\x01\n\x14WatchProductResponse\x12>\n\x05\x65vent\x18\x01 \x01(\x0e\x32/.mruv.economy.WatchProductResponse.ProductEvent\"q\n\x0cProductEvent\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x11\n\rPRICE_CHANGED\x10\x01\x12\x12\n\x0ePRODUCT_BOUGHT\x10\x02\x12\x18\n\x14PRODUCT_INFO_UPDATED\x10\x03\x12\x13\n\x0fPRODUCT_DELETED\x10\x04\"-\n\x11WatchPriceRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\"#\n\x12WatchPriceResponse\x12\r\n\x05price\x18\x01 \x01(\r2\xa3\x08\n\x12MruVEconomyService\x12|\n\x0fRegisterProduct\x12$.mruv.economy.RegisterProductRequest\x1a%.mruv.economy.RegisterProductResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\"\x14/v1/economy/products\x12t\n\nGetProduct\x12\x1f.mruv.economy.GetProductRequest\x1a .mruv.economy.GetProductResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/v1/economy/products/{name}\x12}\n\rUpdateProduct\x12\".mruv.economy.UpdateProductRequest\x1a#.mruv.economy.UpdateProductResponse\"#\x82\xd3\xe4\x93\x02\x1d\x32\x1b/v1/economy/products/{name}\x12}\n\rDeleteProduct\x12\".mruv.economy.DeleteProductRequest\x1a#.mruv.economy.DeleteProductResponse\"#\x82\xd3\xe4\x93\x02\x1d*\x1b/v1/economy/products/{name}\x12}\n\x0bUpdatePrice\x12 .mruv.economy.UpdatePriceRequest\x1a!.mruv.economy.UpdatePriceResponse\")\x82\xd3\xe4\x93\x02#2!/v1/economy/products/{name}/price\x12s\n\x08GetPrice\x12\x1d.mruv.economy.GetPriceRequest\x1a\x1e.mruv.economy.GetPriceResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /v1/economy/product/{name}/price\x12w\n\nBuyProduct\x12\x1f.mruv.economy.BuyProductRequest\x1a .mruv.economy.BuyProductResponse\"&\x82\xd3\xe4\x93\x02 \"\x1e/v1/economy/product/{name}/buy\x12Y\n\x0cWatchProduct\x12!.mruv.economy.WatchProductRequest\x1a\".mruv.economy.WatchProductResponse\"\x00\x30\x01\x12S\n\nWatchPrice\x12\x1f.mruv.economy.WatchPriceRequest\x1a .mruv.economy.WatchPriceResponse\"\x00\x30\x01\x42\'Z%github.com/MruV-RP/mruv-pb-go/economyb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_WATCHPRODUCTRESPONSE_PRODUCTEVENT = _descriptor.EnumDescriptor(
  name='ProductEvent',
  full_name='mruv.economy.WatchProductResponse.ProductEvent',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRICE_CHANGED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_BOUGHT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_INFO_UPDATED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_DELETED', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1070,
  serialized_end=1183,
)
_sym_db.RegisterEnumDescriptor(_WATCHPRODUCTRESPONSE_PRODUCTEVENT)


_REGISTERPRODUCTREQUEST = _descriptor.Descriptor(
  name='RegisterProductRequest',
  full_name='mruv.economy.RegisterProductRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.economy.RegisterProductRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='full_name', full_name='mruv.economy.RegisterProductRequest.full_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='mruv.economy.RegisterProductRequest.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price_class', full_name='mruv.economy.RegisterProductRequest.price_class', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price_ratio', full_name='mruv.economy.RegisterProductRequest.price_ratio', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='starting_price', full_name='mruv.economy.RegisterProductRequest.starting_price', index=5,
      number=6, type=13, cpp_type=3, label=1,
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
  serialized_start=70,
  serialized_end=214,
)


_REGISTERPRODUCTRESPONSE = _descriptor.Descriptor(
  name='RegisterProductResponse',
  full_name='mruv.economy.RegisterProductResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.economy.RegisterProductResponse.id', index=0,
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
  serialized_start=216,
  serialized_end=253,
)


_GETPRODUCTREQUEST = _descriptor.Descriptor(
  name='GetProductRequest',
  full_name='mruv.economy.GetProductRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.economy.GetProductRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.economy.GetProductRequest.name', index=1,
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
  serialized_start=255,
  serialized_end=300,
)


_GETPRODUCTRESPONSE = _descriptor.Descriptor(
  name='GetProductResponse',
  full_name='mruv.economy.GetProductResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.economy.GetProductResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='full_name', full_name='mruv.economy.GetProductResponse.full_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='mruv.economy.GetProductResponse.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price_class', full_name='mruv.economy.GetProductResponse.price_class', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price_ratio', full_name='mruv.economy.GetProductResponse.price_ratio', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='starting_price', full_name='mruv.economy.GetProductResponse.starting_price', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='mruv.economy.GetProductResponse.price', index=6,
      number=7, type=13, cpp_type=3, label=1,
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
  serialized_start=303,
  serialized_end=458,
)


_UPDATEPRODUCTREQUEST = _descriptor.Descriptor(
  name='UpdateProductRequest',
  full_name='mruv.economy.UpdateProductRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.economy.UpdateProductRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.economy.UpdateProductRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='full_name', full_name='mruv.economy.UpdateProductRequest.full_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='mruv.economy.UpdateProductRequest.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price_class', full_name='mruv.economy.UpdateProductRequest.price_class', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price_ratio', full_name='mruv.economy.UpdateProductRequest.price_ratio', index=5,
      number=6, type=2, cpp_type=6, label=1,
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
  serialized_start=461,
  serialized_end=591,
)


_UPDATEPRODUCTRESPONSE = _descriptor.Descriptor(
  name='UpdateProductResponse',
  full_name='mruv.economy.UpdateProductResponse',
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
  serialized_start=593,
  serialized_end=616,
)


_UPDATEPRICEREQUEST = _descriptor.Descriptor(
  name='UpdatePriceRequest',
  full_name='mruv.economy.UpdatePriceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.economy.UpdatePriceRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.economy.UpdatePriceRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_price', full_name='mruv.economy.UpdatePriceRequest.new_price', index=2,
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
  serialized_start=618,
  serialized_end=683,
)


_UPDATEPRICERESPONSE = _descriptor.Descriptor(
  name='UpdatePriceResponse',
  full_name='mruv.economy.UpdatePriceResponse',
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
  serialized_start=685,
  serialized_end=706,
)


_DELETEPRODUCTREQUEST = _descriptor.Descriptor(
  name='DeleteProductRequest',
  full_name='mruv.economy.DeleteProductRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.economy.DeleteProductRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.economy.DeleteProductRequest.name', index=1,
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
  serialized_start=708,
  serialized_end=756,
)


_DELETEPRODUCTRESPONSE = _descriptor.Descriptor(
  name='DeleteProductResponse',
  full_name='mruv.economy.DeleteProductResponse',
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
  serialized_start=758,
  serialized_end=781,
)


_GETPRICEREQUEST = _descriptor.Descriptor(
  name='GetPriceRequest',
  full_name='mruv.economy.GetPriceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.economy.GetPriceRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.economy.GetPriceRequest.name', index=1,
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
  serialized_start=783,
  serialized_end=826,
)


_GETPRICERESPONSE = _descriptor.Descriptor(
  name='GetPriceResponse',
  full_name='mruv.economy.GetPriceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='price', full_name='mruv.economy.GetPriceResponse.price', index=0,
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
  serialized_start=828,
  serialized_end=861,
)


_BUYPRODUCTREQUEST = _descriptor.Descriptor(
  name='BuyProductRequest',
  full_name='mruv.economy.BuyProductRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.economy.BuyProductRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.economy.BuyProductRequest.name', index=1,
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
  serialized_start=863,
  serialized_end=908,
)


_BUYPRODUCTRESPONSE = _descriptor.Descriptor(
  name='BuyProductResponse',
  full_name='mruv.economy.BuyProductResponse',
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
  serialized_start=910,
  serialized_end=930,
)


_WATCHPRODUCTREQUEST = _descriptor.Descriptor(
  name='WatchProductRequest',
  full_name='mruv.economy.WatchProductRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.economy.WatchProductRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.economy.WatchProductRequest.name', index=1,
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
  serialized_start=932,
  serialized_end=979,
)


_WATCHPRODUCTRESPONSE = _descriptor.Descriptor(
  name='WatchProductResponse',
  full_name='mruv.economy.WatchProductResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event', full_name='mruv.economy.WatchProductResponse.event', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _WATCHPRODUCTRESPONSE_PRODUCTEVENT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=982,
  serialized_end=1183,
)


_WATCHPRICEREQUEST = _descriptor.Descriptor(
  name='WatchPriceRequest',
  full_name='mruv.economy.WatchPriceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='mruv.economy.WatchPriceRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='mruv.economy.WatchPriceRequest.name', index=1,
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
  serialized_start=1185,
  serialized_end=1230,
)


_WATCHPRICERESPONSE = _descriptor.Descriptor(
  name='WatchPriceResponse',
  full_name='mruv.economy.WatchPriceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='price', full_name='mruv.economy.WatchPriceResponse.price', index=0,
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
  serialized_start=1232,
  serialized_end=1267,
)

_WATCHPRODUCTRESPONSE.fields_by_name['event'].enum_type = _WATCHPRODUCTRESPONSE_PRODUCTEVENT
_WATCHPRODUCTRESPONSE_PRODUCTEVENT.containing_type = _WATCHPRODUCTRESPONSE
DESCRIPTOR.message_types_by_name['RegisterProductRequest'] = _REGISTERPRODUCTREQUEST
DESCRIPTOR.message_types_by_name['RegisterProductResponse'] = _REGISTERPRODUCTRESPONSE
DESCRIPTOR.message_types_by_name['GetProductRequest'] = _GETPRODUCTREQUEST
DESCRIPTOR.message_types_by_name['GetProductResponse'] = _GETPRODUCTRESPONSE
DESCRIPTOR.message_types_by_name['UpdateProductRequest'] = _UPDATEPRODUCTREQUEST
DESCRIPTOR.message_types_by_name['UpdateProductResponse'] = _UPDATEPRODUCTRESPONSE
DESCRIPTOR.message_types_by_name['UpdatePriceRequest'] = _UPDATEPRICEREQUEST
DESCRIPTOR.message_types_by_name['UpdatePriceResponse'] = _UPDATEPRICERESPONSE
DESCRIPTOR.message_types_by_name['DeleteProductRequest'] = _DELETEPRODUCTREQUEST
DESCRIPTOR.message_types_by_name['DeleteProductResponse'] = _DELETEPRODUCTRESPONSE
DESCRIPTOR.message_types_by_name['GetPriceRequest'] = _GETPRICEREQUEST
DESCRIPTOR.message_types_by_name['GetPriceResponse'] = _GETPRICERESPONSE
DESCRIPTOR.message_types_by_name['BuyProductRequest'] = _BUYPRODUCTREQUEST
DESCRIPTOR.message_types_by_name['BuyProductResponse'] = _BUYPRODUCTRESPONSE
DESCRIPTOR.message_types_by_name['WatchProductRequest'] = _WATCHPRODUCTREQUEST
DESCRIPTOR.message_types_by_name['WatchProductResponse'] = _WATCHPRODUCTRESPONSE
DESCRIPTOR.message_types_by_name['WatchPriceRequest'] = _WATCHPRICEREQUEST
DESCRIPTOR.message_types_by_name['WatchPriceResponse'] = _WATCHPRICERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegisterProductRequest = _reflection.GeneratedProtocolMessageType('RegisterProductRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERPRODUCTREQUEST,
  '__module__' : 'economy.economy_pb2'
  # @@protoc_insertion_point(class_scope:mruv.economy.RegisterProductRequest)
  })
_sym_db.RegisterMessage(RegisterProductRequest)

RegisterProductResponse = _reflection.GeneratedProtocolMessageType('RegisterProductResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERPRODUCTRESPONSE,
  '__module__' : 'economy.economy_pb2'
  # @@protoc_insertion_point(class_scope:mruv.economy.RegisterProductResponse)
  })
_sym_db.RegisterMessage(RegisterProductResponse)

GetProductRequest = _reflection.GeneratedProtocolMessageType('GetProductRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPRODUCTREQUEST,
  '__module__' : 'economy.economy_pb2'
  # @@protoc_insertion_point(class_scope:mruv.economy.GetProductRequest)
  })
_sym_db.RegisterMessage(GetProductRequest)

GetProductResponse = _reflection.GeneratedProtocolMessageType('GetProductResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPRODUCTRESPONSE,
  '__module__' : 'economy.economy_pb2'
  # @@protoc_insertion_point(class_scope:mruv.economy.GetProductResponse)
  })
_sym_db.RegisterMessage(GetProductResponse)

UpdateProductRequest = _reflection.GeneratedProtocolMessageType('UpdateProductRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPRODUCTREQUEST,
  '__module__' : 'economy.economy_pb2'
  # @@protoc_insertion_point(class_scope:mruv.economy.UpdateProductRequest)
  })
_sym_db.RegisterMessage(UpdateProductRequest)

UpdateProductResponse = _reflection.GeneratedProtocolMessageType('UpdateProductResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPRODUCTRESPONSE,
  '__module__' : 'economy.economy_pb2'
  # @@protoc_insertion_point(class_scope:mruv.economy.UpdateProductResponse)
  })
_sym_db.RegisterMessage(UpdateProductResponse)

UpdatePriceRequest = _reflection.GeneratedProtocolMessageType('UpdatePriceRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPRICEREQUEST,
  '__module__' : 'economy.economy_pb2'
  # @@protoc_insertion_point(class_scope:mruv.economy.UpdatePriceRequest)
  })
_sym_db.RegisterMessage(UpdatePriceRequest)

UpdatePriceResponse = _reflection.GeneratedProtocolMessageType('UpdatePriceResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPRICERESPONSE,
  '__module__' : 'economy.economy_pb2'
  # @@protoc_insertion_point(class_scope:mruv.economy.UpdatePriceResponse)
  })
_sym_db.RegisterMessage(UpdatePriceResponse)

DeleteProductRequest = _reflection.GeneratedProtocolMessageType('DeleteProductRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPRODUCTREQUEST,
  '__module__' : 'economy.economy_pb2'
  # @@protoc_insertion_point(class_scope:mruv.economy.DeleteProductRequest)
  })
_sym_db.RegisterMessage(DeleteProductRequest)

DeleteProductResponse = _reflection.GeneratedProtocolMessageType('DeleteProductResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPRODUCTRESPONSE,
  '__module__' : 'economy.economy_pb2'
  # @@protoc_insertion_point(class_scope:mruv.economy.DeleteProductResponse)
  })
_sym_db.RegisterMessage(DeleteProductResponse)

GetPriceRequest = _reflection.GeneratedProtocolMessageType('GetPriceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPRICEREQUEST,
  '__module__' : 'economy.economy_pb2'
  # @@protoc_insertion_point(class_scope:mruv.economy.GetPriceRequest)
  })
_sym_db.RegisterMessage(GetPriceRequest)

GetPriceResponse = _reflection.GeneratedProtocolMessageType('GetPriceResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPRICERESPONSE,
  '__module__' : 'economy.economy_pb2'
  # @@protoc_insertion_point(class_scope:mruv.economy.GetPriceResponse)
  })
_sym_db.RegisterMessage(GetPriceResponse)

BuyProductRequest = _reflection.GeneratedProtocolMessageType('BuyProductRequest', (_message.Message,), {
  'DESCRIPTOR' : _BUYPRODUCTREQUEST,
  '__module__' : 'economy.economy_pb2'
  # @@protoc_insertion_point(class_scope:mruv.economy.BuyProductRequest)
  })
_sym_db.RegisterMessage(BuyProductRequest)

BuyProductResponse = _reflection.GeneratedProtocolMessageType('BuyProductResponse', (_message.Message,), {
  'DESCRIPTOR' : _BUYPRODUCTRESPONSE,
  '__module__' : 'economy.economy_pb2'
  # @@protoc_insertion_point(class_scope:mruv.economy.BuyProductResponse)
  })
_sym_db.RegisterMessage(BuyProductResponse)

WatchProductRequest = _reflection.GeneratedProtocolMessageType('WatchProductRequest', (_message.Message,), {
  'DESCRIPTOR' : _WATCHPRODUCTREQUEST,
  '__module__' : 'economy.economy_pb2'
  # @@protoc_insertion_point(class_scope:mruv.economy.WatchProductRequest)
  })
_sym_db.RegisterMessage(WatchProductRequest)

WatchProductResponse = _reflection.GeneratedProtocolMessageType('WatchProductResponse', (_message.Message,), {
  'DESCRIPTOR' : _WATCHPRODUCTRESPONSE,
  '__module__' : 'economy.economy_pb2'
  # @@protoc_insertion_point(class_scope:mruv.economy.WatchProductResponse)
  })
_sym_db.RegisterMessage(WatchProductResponse)

WatchPriceRequest = _reflection.GeneratedProtocolMessageType('WatchPriceRequest', (_message.Message,), {
  'DESCRIPTOR' : _WATCHPRICEREQUEST,
  '__module__' : 'economy.economy_pb2'
  # @@protoc_insertion_point(class_scope:mruv.economy.WatchPriceRequest)
  })
_sym_db.RegisterMessage(WatchPriceRequest)

WatchPriceResponse = _reflection.GeneratedProtocolMessageType('WatchPriceResponse', (_message.Message,), {
  'DESCRIPTOR' : _WATCHPRICERESPONSE,
  '__module__' : 'economy.economy_pb2'
  # @@protoc_insertion_point(class_scope:mruv.economy.WatchPriceResponse)
  })
_sym_db.RegisterMessage(WatchPriceResponse)


DESCRIPTOR._options = None

_MRUVECONOMYSERVICE = _descriptor.ServiceDescriptor(
  name='MruVEconomyService',
  full_name='mruv.economy.MruVEconomyService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1270,
  serialized_end=2329,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterProduct',
    full_name='mruv.economy.MruVEconomyService.RegisterProduct',
    index=0,
    containing_service=None,
    input_type=_REGISTERPRODUCTREQUEST,
    output_type=_REGISTERPRODUCTRESPONSE,
    serialized_options=_b('\202\323\344\223\002\026\"\024/v1/economy/products'),
  ),
  _descriptor.MethodDescriptor(
    name='GetProduct',
    full_name='mruv.economy.MruVEconomyService.GetProduct',
    index=1,
    containing_service=None,
    input_type=_GETPRODUCTREQUEST,
    output_type=_GETPRODUCTRESPONSE,
    serialized_options=_b('\202\323\344\223\002\035\022\033/v1/economy/products/{name}'),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateProduct',
    full_name='mruv.economy.MruVEconomyService.UpdateProduct',
    index=2,
    containing_service=None,
    input_type=_UPDATEPRODUCTREQUEST,
    output_type=_UPDATEPRODUCTRESPONSE,
    serialized_options=_b('\202\323\344\223\002\0352\033/v1/economy/products/{name}'),
  ),
  _descriptor.MethodDescriptor(
    name='DeleteProduct',
    full_name='mruv.economy.MruVEconomyService.DeleteProduct',
    index=3,
    containing_service=None,
    input_type=_DELETEPRODUCTREQUEST,
    output_type=_DELETEPRODUCTRESPONSE,
    serialized_options=_b('\202\323\344\223\002\035*\033/v1/economy/products/{name}'),
  ),
  _descriptor.MethodDescriptor(
    name='UpdatePrice',
    full_name='mruv.economy.MruVEconomyService.UpdatePrice',
    index=4,
    containing_service=None,
    input_type=_UPDATEPRICEREQUEST,
    output_type=_UPDATEPRICERESPONSE,
    serialized_options=_b('\202\323\344\223\002#2!/v1/economy/products/{name}/price'),
  ),
  _descriptor.MethodDescriptor(
    name='GetPrice',
    full_name='mruv.economy.MruVEconomyService.GetPrice',
    index=5,
    containing_service=None,
    input_type=_GETPRICEREQUEST,
    output_type=_GETPRICERESPONSE,
    serialized_options=_b('\202\323\344\223\002\"\022 /v1/economy/product/{name}/price'),
  ),
  _descriptor.MethodDescriptor(
    name='BuyProduct',
    full_name='mruv.economy.MruVEconomyService.BuyProduct',
    index=6,
    containing_service=None,
    input_type=_BUYPRODUCTREQUEST,
    output_type=_BUYPRODUCTRESPONSE,
    serialized_options=_b('\202\323\344\223\002 \"\036/v1/economy/product/{name}/buy'),
  ),
  _descriptor.MethodDescriptor(
    name='WatchProduct',
    full_name='mruv.economy.MruVEconomyService.WatchProduct',
    index=7,
    containing_service=None,
    input_type=_WATCHPRODUCTREQUEST,
    output_type=_WATCHPRODUCTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='WatchPrice',
    full_name='mruv.economy.MruVEconomyService.WatchPrice',
    index=8,
    containing_service=None,
    input_type=_WATCHPRICEREQUEST,
    output_type=_WATCHPRICERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MRUVECONOMYSERVICE)

DESCRIPTOR.services_by_name['MruVEconomyService'] = _MRUVECONOMYSERVICE

# @@protoc_insertion_point(module_scope)