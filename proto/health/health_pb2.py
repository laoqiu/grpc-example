# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/health/health.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/health/health.proto',
  package='grpc.health.v1',
  syntax='proto3',
  serialized_pb=_b('\n\x19proto/health/health.proto\x12\x0egrpc.health.v1\x1a\x1cgoogle/api/annotations.proto\"%\n\x12HealthCheckRequest\x12\x0f\n\x07service\x18\x01 \x01(\t\"\x94\x01\n\x13HealthCheckResponse\x12\x41\n\x06status\x18\x01 \x01(\x0e\x32\x31.grpc.health.v1.HealthCheckResponse.ServingStatus\":\n\rServingStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SERVING\x10\x01\x12\x0f\n\x0bNOT_SERVING\x10\x02\x32\\\n\x06Health\x12R\n\x05\x43heck\x12\".grpc.health.v1.HealthCheckRequest\x1a#.grpc.health.v1.HealthCheckResponse\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_HEALTHCHECKRESPONSE_SERVINGSTATUS = _descriptor.EnumDescriptor(
  name='ServingStatus',
  full_name='grpc.health.v1.HealthCheckResponse.ServingStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERVING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_SERVING', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=205,
  serialized_end=263,
)
_sym_db.RegisterEnumDescriptor(_HEALTHCHECKRESPONSE_SERVINGSTATUS)


_HEALTHCHECKREQUEST = _descriptor.Descriptor(
  name='HealthCheckRequest',
  full_name='grpc.health.v1.HealthCheckRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='grpc.health.v1.HealthCheckRequest.service', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=112,
)


_HEALTHCHECKRESPONSE = _descriptor.Descriptor(
  name='HealthCheckResponse',
  full_name='grpc.health.v1.HealthCheckResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='grpc.health.v1.HealthCheckResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HEALTHCHECKRESPONSE_SERVINGSTATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=263,
)

_HEALTHCHECKRESPONSE.fields_by_name['status'].enum_type = _HEALTHCHECKRESPONSE_SERVINGSTATUS
_HEALTHCHECKRESPONSE_SERVINGSTATUS.containing_type = _HEALTHCHECKRESPONSE
DESCRIPTOR.message_types_by_name['HealthCheckRequest'] = _HEALTHCHECKREQUEST
DESCRIPTOR.message_types_by_name['HealthCheckResponse'] = _HEALTHCHECKRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HealthCheckRequest = _reflection.GeneratedProtocolMessageType('HealthCheckRequest', (_message.Message,), dict(
  DESCRIPTOR = _HEALTHCHECKREQUEST,
  __module__ = 'proto.health.health_pb2'
  # @@protoc_insertion_point(class_scope:grpc.health.v1.HealthCheckRequest)
  ))
_sym_db.RegisterMessage(HealthCheckRequest)

HealthCheckResponse = _reflection.GeneratedProtocolMessageType('HealthCheckResponse', (_message.Message,), dict(
  DESCRIPTOR = _HEALTHCHECKRESPONSE,
  __module__ = 'proto.health.health_pb2'
  # @@protoc_insertion_point(class_scope:grpc.health.v1.HealthCheckResponse)
  ))
_sym_db.RegisterMessage(HealthCheckResponse)



_HEALTH = _descriptor.ServiceDescriptor(
  name='Health',
  full_name='grpc.health.v1.Health',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=265,
  serialized_end=357,
  methods=[
  _descriptor.MethodDescriptor(
    name='Check',
    full_name='grpc.health.v1.Health.Check',
    index=0,
    containing_service=None,
    input_type=_HEALTHCHECKREQUEST,
    output_type=_HEALTHCHECKRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_HEALTH)

DESCRIPTOR.services_by_name['Health'] = _HEALTH

# @@protoc_insertion_point(module_scope)
