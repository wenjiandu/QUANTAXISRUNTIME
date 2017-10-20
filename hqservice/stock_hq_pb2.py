# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stock_hq.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import stock_min_pb2 as stock__min__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='stock_hq.proto',
  package='stock_hq',
  syntax='proto3',
  serialized_pb=_b('\n\x0estock_hq.proto\x12\x08stock_hq\x1a\x0fstock_min.proto\"#\n\x05Query\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t2Q\n\x0eStockHQService\x12?\n\x0cQA_fetch_get\x12\x0f.stock_hq.Query\x1a\x1e.QUANTAXIS_STOCK_MIN.stock_minb\x06proto3')
  ,
  dependencies=[stock__min__pb2.DESCRIPTOR,])




_QUERY = _descriptor.Descriptor(
  name='Query',
  full_name='stock_hq.Query',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='stock_hq.Query.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code', full_name='stock_hq.Query.code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=45,
  serialized_end=80,
)

DESCRIPTOR.message_types_by_name['Query'] = _QUERY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Query = _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), dict(
  DESCRIPTOR = _QUERY,
  __module__ = 'stock_hq_pb2'
  # @@protoc_insertion_point(class_scope:stock_hq.Query)
  ))
_sym_db.RegisterMessage(Query)



_STOCKHQSERVICE = _descriptor.ServiceDescriptor(
  name='StockHQService',
  full_name='stock_hq.StockHQService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=82,
  serialized_end=163,
  methods=[
  _descriptor.MethodDescriptor(
    name='QA_fetch_get',
    full_name='stock_hq.StockHQService.QA_fetch_get',
    index=0,
    containing_service=None,
    input_type=_QUERY,
    output_type=stock__min__pb2._STOCK_MIN,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STOCKHQSERVICE)

DESCRIPTOR.services_by_name['StockHQService'] = _STOCKHQSERVICE

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class StockHQServiceStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.QA_fetch_get = channel.unary_unary(
          '/stock_hq.StockHQService/QA_fetch_get',
          request_serializer=Query.SerializeToString,
          response_deserializer=stock__min__pb2.stock_min.FromString,
          )


  class StockHQServiceServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def QA_fetch_get(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_StockHQServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'QA_fetch_get': grpc.unary_unary_rpc_method_handler(
            servicer.QA_fetch_get,
            request_deserializer=Query.FromString,
            response_serializer=stock__min__pb2.stock_min.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'stock_hq.StockHQService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaStockHQServiceServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def QA_fetch_get(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaStockHQServiceStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def QA_fetch_get(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    QA_fetch_get.future = None


  def beta_create_StockHQService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('stock_hq.StockHQService', 'QA_fetch_get'): Query.FromString,
    }
    response_serializers = {
      ('stock_hq.StockHQService', 'QA_fetch_get'): stock__min__pb2.stock_min.SerializeToString,
    }
    method_implementations = {
      ('stock_hq.StockHQService', 'QA_fetch_get'): face_utilities.unary_unary_inline(servicer.QA_fetch_get),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_StockHQService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('stock_hq.StockHQService', 'QA_fetch_get'): Query.SerializeToString,
    }
    response_deserializers = {
      ('stock_hq.StockHQService', 'QA_fetch_get'): stock__min__pb2.stock_min.FromString,
    }
    cardinalities = {
      'QA_fetch_get': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'stock_hq.StockHQService', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
