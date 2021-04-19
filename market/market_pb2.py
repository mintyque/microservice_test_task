# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: market.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='market.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cmarket.proto\".\n\nAddRequest\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\x0f\n\x07\x63\x61rt_id\x18\x02 \x01(\x05\"%\n\x0b\x41\x64\x64Response\x12\x16\n\x0eresponse_token\x18\x01 \x01(\x05\"\x1e\n\x0b\x43\x61rtRequest\x12\x0f\n\x07\x63\x61rt_id\x18\x01 \x01(\x05\"1\n\x0c\x43\x61rtResponse\x12\x10\n\x08item_amt\x18\x01 \x01(\x05\x12\x0f\n\x07item_id\x18\x02 \x03(\x05*\x1e\n\x0cResponseType\x12\x06\n\x02OK\x10\x00\x12\x06\n\x02NO\x10\x01\x32Z\n\x06Market\x12$\n\x07\x41\x64\x64Item\x12\x0b.AddRequest\x1a\x0c.AddResponse\x12*\n\x0bRequestCart\x12\x0c.CartRequest\x1a\r.CartResponseb\x06proto3'
)

_RESPONSETYPE = _descriptor.EnumDescriptor(
  name='ResponseType',
  full_name='ResponseType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NO', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=186,
  serialized_end=216,
)
_sym_db.RegisterEnumDescriptor(_RESPONSETYPE)

ResponseType = enum_type_wrapper.EnumTypeWrapper(_RESPONSETYPE)
OK = 0
NO = 1



_ADDREQUEST = _descriptor.Descriptor(
  name='AddRequest',
  full_name='AddRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='AddRequest.item_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cart_id', full_name='AddRequest.cart_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=16,
  serialized_end=62,
)


_ADDRESPONSE = _descriptor.Descriptor(
  name='AddResponse',
  full_name='AddResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='response_token', full_name='AddResponse.response_token', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=64,
  serialized_end=101,
)


_CARTREQUEST = _descriptor.Descriptor(
  name='CartRequest',
  full_name='CartRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cart_id', full_name='CartRequest.cart_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=103,
  serialized_end=133,
)


_CARTRESPONSE = _descriptor.Descriptor(
  name='CartResponse',
  full_name='CartResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_amt', full_name='CartResponse.item_amt', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='item_id', full_name='CartResponse.item_id', index=1,
      number=2, type=5, cpp_type=1, label=3,
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
  serialized_start=135,
  serialized_end=184,
)

DESCRIPTOR.message_types_by_name['AddRequest'] = _ADDREQUEST
DESCRIPTOR.message_types_by_name['AddResponse'] = _ADDRESPONSE
DESCRIPTOR.message_types_by_name['CartRequest'] = _CARTREQUEST
DESCRIPTOR.message_types_by_name['CartResponse'] = _CARTRESPONSE
DESCRIPTOR.enum_types_by_name['ResponseType'] = _RESPONSETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddRequest = _reflection.GeneratedProtocolMessageType('AddRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDREQUEST,
  '__module__' : 'market_pb2'
  # @@protoc_insertion_point(class_scope:AddRequest)
  })
_sym_db.RegisterMessage(AddRequest)

AddResponse = _reflection.GeneratedProtocolMessageType('AddResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESPONSE,
  '__module__' : 'market_pb2'
  # @@protoc_insertion_point(class_scope:AddResponse)
  })
_sym_db.RegisterMessage(AddResponse)

CartRequest = _reflection.GeneratedProtocolMessageType('CartRequest', (_message.Message,), {
  'DESCRIPTOR' : _CARTREQUEST,
  '__module__' : 'market_pb2'
  # @@protoc_insertion_point(class_scope:CartRequest)
  })
_sym_db.RegisterMessage(CartRequest)

CartResponse = _reflection.GeneratedProtocolMessageType('CartResponse', (_message.Message,), {
  'DESCRIPTOR' : _CARTRESPONSE,
  '__module__' : 'market_pb2'
  # @@protoc_insertion_point(class_scope:CartResponse)
  })
_sym_db.RegisterMessage(CartResponse)



_MARKET = _descriptor.ServiceDescriptor(
  name='Market',
  full_name='Market',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=218,
  serialized_end=308,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddItem',
    full_name='Market.AddItem',
    index=0,
    containing_service=None,
    input_type=_ADDREQUEST,
    output_type=_ADDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RequestCart',
    full_name='Market.RequestCart',
    index=1,
    containing_service=None,
    input_type=_CARTREQUEST,
    output_type=_CARTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MARKET)

DESCRIPTOR.services_by_name['Market'] = _MARKET

# @@protoc_insertion_point(module_scope)