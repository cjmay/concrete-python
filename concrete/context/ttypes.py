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

from thrift.transport import TTransport
all_structs = []


class Context(object):
    """
    A structure intended to convey context about a particular
    Concrete communication.

    Contexts are intended to be used to convey meta-communication
    information to analytics via an RPC method. It is expected that
    services consuming or producing Contexts are coupled,
    delivering an agreed upon format that is capable of
    being interpreted and processed between two particular services.

    Currently, it is being used to transmit hypotheses alongside
    concrete communications for AIDA.

    Attributes:
     - contents: The contents of the Context. Services should agree
    upon what the expected format of the contents are
    (e.g. JSON, RDF) between themselves.
    """


    def __init__(self, contents=None,):
        self.contents = contents

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
                if ftype == TType.STRING:
                    self.contents = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('Context')
        if self.contents is not None:
            oprot.writeFieldBegin('contents', TType.STRING, 1)
            oprot.writeString(self.contents.encode('utf-8') if sys.version_info[0] == 2 else self.contents)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(Context)
Context.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'contents', 'UTF8', None, ),  # 1
)
fix_spec(all_structs)
del all_structs
