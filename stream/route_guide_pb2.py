# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: route_guide.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11route_guide.proto\",\n\x05Point\x12\x10\n\x08latitude\x18\x01 \x01(\x05\x12\x11\n\tlongitude\x18\x02 \x01(\x05\"3\n\tRectangle\x12\x12\n\x02lo\x18\x01 \x01(\x0b\x32\x06.Point\x12\x12\n\x02hi\x18\x02 \x01(\x0b\x32\x06.Point\"1\n\x07\x46\x65\x61ture\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x08location\x18\x02 \x01(\x0b\x32\x06.Point\"6\n\tRouteNote\x12\x18\n\x08location\x18\x01 \x01(\x0b\x32\x06.Point\x12\x0f\n\x07message\x18\x02 \x01(\t\"b\n\x0cRouteSummary\x12\x13\n\x0bpoint_count\x18\x01 \x01(\x05\x12\x15\n\rfeature_count\x18\x02 \x01(\x05\x12\x10\n\x08\x64istance\x18\x03 \x01(\x05\x12\x14\n\x0c\x65lapsed_time\x18\x04 \x01(\x05\x32\xad\x01\n\nRouteGuide\x12 \n\nGetFeature\x12\x06.Point\x1a\x08.Feature\"\x00\x12(\n\x0cListFeatures\x12\n.Rectangle\x1a\x08.Feature\"\x00\x30\x01\x12(\n\x0bRecordRoute\x12\x06.Point\x1a\r.RouteSummary\"\x00(\x01\x12)\n\tRouteChat\x12\n.RouteNote\x1a\n.RouteNote\"\x00(\x01\x30\x01\x62\x06proto3')



_POINT = DESCRIPTOR.message_types_by_name['Point']
_RECTANGLE = DESCRIPTOR.message_types_by_name['Rectangle']
_FEATURE = DESCRIPTOR.message_types_by_name['Feature']
_ROUTENOTE = DESCRIPTOR.message_types_by_name['RouteNote']
_ROUTESUMMARY = DESCRIPTOR.message_types_by_name['RouteSummary']
Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), {
  'DESCRIPTOR' : _POINT,
  '__module__' : 'route_guide_pb2'
  # @@protoc_insertion_point(class_scope:Point)
  })
_sym_db.RegisterMessage(Point)

Rectangle = _reflection.GeneratedProtocolMessageType('Rectangle', (_message.Message,), {
  'DESCRIPTOR' : _RECTANGLE,
  '__module__' : 'route_guide_pb2'
  # @@protoc_insertion_point(class_scope:Rectangle)
  })
_sym_db.RegisterMessage(Rectangle)

Feature = _reflection.GeneratedProtocolMessageType('Feature', (_message.Message,), {
  'DESCRIPTOR' : _FEATURE,
  '__module__' : 'route_guide_pb2'
  # @@protoc_insertion_point(class_scope:Feature)
  })
_sym_db.RegisterMessage(Feature)

RouteNote = _reflection.GeneratedProtocolMessageType('RouteNote', (_message.Message,), {
  'DESCRIPTOR' : _ROUTENOTE,
  '__module__' : 'route_guide_pb2'
  # @@protoc_insertion_point(class_scope:RouteNote)
  })
_sym_db.RegisterMessage(RouteNote)

RouteSummary = _reflection.GeneratedProtocolMessageType('RouteSummary', (_message.Message,), {
  'DESCRIPTOR' : _ROUTESUMMARY,
  '__module__' : 'route_guide_pb2'
  # @@protoc_insertion_point(class_scope:RouteSummary)
  })
_sym_db.RegisterMessage(RouteSummary)

_ROUTEGUIDE = DESCRIPTOR.services_by_name['RouteGuide']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _POINT._serialized_start=21
  _POINT._serialized_end=65
  _RECTANGLE._serialized_start=67
  _RECTANGLE._serialized_end=118
  _FEATURE._serialized_start=120
  _FEATURE._serialized_end=169
  _ROUTENOTE._serialized_start=171
  _ROUTENOTE._serialized_end=225
  _ROUTESUMMARY._serialized_start=227
  _ROUTESUMMARY._serialized_end=325
  _ROUTEGUIDE._serialized_start=328
  _ROUTEGUIDE._serialized_end=501
# @@protoc_insertion_point(module_scope)
