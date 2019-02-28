# -*- coding: utf-8 -*-
#
# Autogenerated by Thrift Compiler (0.11.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:coding=utf-8
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
import concrete.services.ttypes
import concrete.uuid.ttypes
import concrete.communication.ttypes

from thrift.transport import TTransport
all_structs = []


class AnnotationTask(object):
    """
    Annotation task including information for pulling data.

    Attributes:
     - type: Type of annotation task
     - language: Language of the data for the task
     - unitType: Entire communication or individual sentences
     - units: Identifiers for each annotation unit
    """


    def __init__(self, type=None, language=None, unitType=None, units=None,):
        self.type = type
        self.language = language
        self.unitType = unitType
        self.units = units

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.language = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.unitType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.units = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = concrete.services.ttypes.AnnotationUnitIdentifier()
                        _elem5.read(iprot)
                        self.units.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('AnnotationTask')
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 1)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.language is not None:
            oprot.writeFieldBegin('language', TType.STRING, 2)
            oprot.writeString(self.language.encode('utf-8') if sys.version_info[0] == 2 else self.language)
            oprot.writeFieldEnd()
        if self.unitType is not None:
            oprot.writeFieldBegin('unitType', TType.I32, 3)
            oprot.writeI32(self.unitType)
            oprot.writeFieldEnd()
        if self.units is not None:
            oprot.writeFieldBegin('units', TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.units))
            for iter6 in self.units:
                iter6.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.type is None:
            raise TProtocolException(message='Required field type is unset!')
        if self.unitType is None:
            raise TProtocolException(message='Required field unitType is unset!')
        if self.units is None:
            raise TProtocolException(message='Required field units is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Annotation(object):
    """
    Annotation on a communication.

    Attributes:
     - id: Identifier of the part of the communication being annotated.
     - communication: Communication with the annotation stored in it.
    The location of the annotation depends on the annotation unit identifier
    """


    def __init__(self, id=None, communication=None,):
        self.id = id
        self.communication = communication

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.id = concrete.services.ttypes.AnnotationUnitIdentifier()
                    self.id.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.communication = concrete.communication.ttypes.Communication()
                    self.communication.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Annotation')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRUCT, 1)
            self.id.write(oprot)
            oprot.writeFieldEnd()
        if self.communication is not None:
            oprot.writeFieldBegin('communication', TType.STRUCT, 2)
            self.communication.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.id is None:
            raise TProtocolException(message='Required field id is unset!')
        if self.communication is None:
            raise TProtocolException(message='Required field communication is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(AnnotationTask)
AnnotationTask.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'type', None, None, ),  # 1
    (2, TType.STRING, 'language', 'UTF8', None, ),  # 2
    (3, TType.I32, 'unitType', None, None, ),  # 3
    (4, TType.LIST, 'units', (TType.STRUCT, [concrete.services.ttypes.AnnotationUnitIdentifier, None], False), None, ),  # 4
)
all_structs.append(Annotation)
Annotation.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'id', [concrete.services.ttypes.AnnotationUnitIdentifier, None], None, ),  # 1
    (2, TType.STRUCT, 'communication', [concrete.communication.ttypes.Communication, None], None, ),  # 2
)
fix_spec(all_structs)
del all_structs
