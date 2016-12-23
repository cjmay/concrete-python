# -*- coding: utf-8 -*-
#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style,utf8strings,coding=utf-8
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import concrete.services.Service
import logging
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface(concrete.services.Service.Iface):
  """
  Service to fetch particular communications.
  """
  def fetch(self, request):
    """
    Parameters:
     - request
    """
    pass

  def getCommunicationIDs(self, offset, count):
    """
    Get a list of 'count' Communication IDs starting at 'offset'.  Implementations
    that do not provide this should throw an exception.

    Parameters:
     - offset
     - count
    """
    pass

  def getCommunicationCount(self):
    """
    Get the number of Communications this service searches over.  Implementations
    that do not provide this should throw an exception.
    """
    pass


class Client(concrete.services.Service.Client, Iface):
  """
  Service to fetch particular communications.
  """
  def __init__(self, iprot, oprot=None):
    concrete.services.Service.Client.__init__(self, iprot, oprot)

  def fetch(self, request):
    """
    Parameters:
     - request
    """
    self.send_fetch(request)
    return self.recv_fetch()

  def send_fetch(self, request):
    self._oprot.writeMessageBegin('fetch', TMessageType.CALL, self._seqid)
    args = fetch_args()
    args.request = request
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_fetch(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = fetch_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ex is not None:
      raise result.ex
    raise TApplicationException(TApplicationException.MISSING_RESULT, "fetch failed: unknown result")

  def getCommunicationIDs(self, offset, count):
    """
    Get a list of 'count' Communication IDs starting at 'offset'.  Implementations
    that do not provide this should throw an exception.

    Parameters:
     - offset
     - count
    """
    self.send_getCommunicationIDs(offset, count)
    return self.recv_getCommunicationIDs()

  def send_getCommunicationIDs(self, offset, count):
    self._oprot.writeMessageBegin('getCommunicationIDs', TMessageType.CALL, self._seqid)
    args = getCommunicationIDs_args()
    args.offset = offset
    args.count = count
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_getCommunicationIDs(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = getCommunicationIDs_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ex is not None:
      raise result.ex
    raise TApplicationException(TApplicationException.MISSING_RESULT, "getCommunicationIDs failed: unknown result")

  def getCommunicationCount(self):
    """
    Get the number of Communications this service searches over.  Implementations
    that do not provide this should throw an exception.
    """
    self.send_getCommunicationCount()
    return self.recv_getCommunicationCount()

  def send_getCommunicationCount(self):
    self._oprot.writeMessageBegin('getCommunicationCount', TMessageType.CALL, self._seqid)
    args = getCommunicationCount_args()
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_getCommunicationCount(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = getCommunicationCount_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.ex is not None:
      raise result.ex
    raise TApplicationException(TApplicationException.MISSING_RESULT, "getCommunicationCount failed: unknown result")


class Processor(concrete.services.Service.Processor, Iface, TProcessor):
  def __init__(self, handler):
    concrete.services.Service.Processor.__init__(self, handler)
    self._processMap["fetch"] = Processor.process_fetch
    self._processMap["getCommunicationIDs"] = Processor.process_getCommunicationIDs
    self._processMap["getCommunicationCount"] = Processor.process_getCommunicationCount

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_fetch(self, seqid, iprot, oprot):
    args = fetch_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = fetch_result()
    try:
      result.success = self._handler.fetch(args.request)
      msg_type = TMessageType.REPLY
    except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
      raise
    except concrete.services.ttypes.ServicesException as ex:
      msg_type = TMessageType.REPLY
      result.ex = ex
    except Exception as ex:
      msg_type = TMessageType.EXCEPTION
      logging.exception(ex)
      result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
    oprot.writeMessageBegin("fetch", msg_type, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_getCommunicationIDs(self, seqid, iprot, oprot):
    args = getCommunicationIDs_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = getCommunicationIDs_result()
    try:
      result.success = self._handler.getCommunicationIDs(args.offset, args.count)
      msg_type = TMessageType.REPLY
    except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
      raise
    except concrete.services.ttypes.NotImplementedException as ex:
      msg_type = TMessageType.REPLY
      result.ex = ex
    except Exception as ex:
      msg_type = TMessageType.EXCEPTION
      logging.exception(ex)
      result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
    oprot.writeMessageBegin("getCommunicationIDs", msg_type, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_getCommunicationCount(self, seqid, iprot, oprot):
    args = getCommunicationCount_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = getCommunicationCount_result()
    try:
      result.success = self._handler.getCommunicationCount()
      msg_type = TMessageType.REPLY
    except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
      raise
    except concrete.services.ttypes.NotImplementedException as ex:
      msg_type = TMessageType.REPLY
      result.ex = ex
    except Exception as ex:
      msg_type = TMessageType.EXCEPTION
      logging.exception(ex)
      result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
    oprot.writeMessageBegin("getCommunicationCount", msg_type, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class fetch_args(object):
  """
  Attributes:
   - request
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'request', (FetchRequest, FetchRequest.thrift_spec), None, ), # 1
  )

  def __init__(self, request=None,):
    self.request = request

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.request = FetchRequest()
          self.request.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('fetch_args')
    if self.request is not None:
      oprot.writeFieldBegin('request', TType.STRUCT, 1)
      self.request.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.request)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class fetch_result(object):
  """
  Attributes:
   - success
   - ex
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (FetchResult, FetchResult.thrift_spec), None, ), # 0
    (1, TType.STRUCT, 'ex', (concrete.services.ttypes.ServicesException, concrete.services.ttypes.ServicesException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, ex=None,):
    self.success = success
    self.ex = ex

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = FetchResult()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.ex = concrete.services.ttypes.ServicesException()
          self.ex.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('fetch_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    if self.ex is not None:
      oprot.writeFieldBegin('ex', TType.STRUCT, 1)
      self.ex.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    value = (value * 31) ^ hash(self.ex)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getCommunicationIDs_args(object):
  """
  Attributes:
   - offset
   - count
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'offset', None, None, ), # 1
    (2, TType.I64, 'count', None, None, ), # 2
  )

  def __init__(self, offset=None, count=None,):
    self.offset = offset
    self.count = count

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.offset = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.count = iprot.readI64()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getCommunicationIDs_args')
    if self.offset is not None:
      oprot.writeFieldBegin('offset', TType.I64, 1)
      oprot.writeI64(self.offset)
      oprot.writeFieldEnd()
    if self.count is not None:
      oprot.writeFieldBegin('count', TType.I64, 2)
      oprot.writeI64(self.count)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.offset)
    value = (value * 31) ^ hash(self.count)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getCommunicationIDs_result(object):
  """
  Attributes:
   - success
   - ex
  """

  thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRING,None), None, ), # 0
    (1, TType.STRUCT, 'ex', (concrete.services.ttypes.NotImplementedException, concrete.services.ttypes.NotImplementedException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, ex=None,):
    self.success = success
    self.ex = ex

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.LIST:
          self.success = []
          (_etype17, _size14) = iprot.readListBegin()
          for _i18 in xrange(_size14):
            _elem19 = iprot.readString().decode('utf-8')
            self.success.append(_elem19)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.ex = concrete.services.ttypes.NotImplementedException()
          self.ex.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getCommunicationIDs_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRING, len(self.success))
      for iter20 in self.success:
        oprot.writeString(iter20.encode('utf-8'))
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.ex is not None:
      oprot.writeFieldBegin('ex', TType.STRUCT, 1)
      self.ex.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    value = (value * 31) ^ hash(self.ex)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getCommunicationCount_args(object):

  thrift_spec = (
  )

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getCommunicationCount_args')
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class getCommunicationCount_result(object):
  """
  Attributes:
   - success
   - ex
  """

  thrift_spec = (
    (0, TType.I64, 'success', None, None, ), # 0
    (1, TType.STRUCT, 'ex', (concrete.services.ttypes.NotImplementedException, concrete.services.ttypes.NotImplementedException.thrift_spec), None, ), # 1
  )

  def __init__(self, success=None, ex=None,):
    self.success = success
    self.ex = ex

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.I64:
          self.success = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.ex = concrete.services.ttypes.NotImplementedException()
          self.ex.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('getCommunicationCount_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.I64, 0)
      oprot.writeI64(self.success)
      oprot.writeFieldEnd()
    if self.ex is not None:
      oprot.writeFieldBegin('ex', TType.STRUCT, 1)
      self.ex.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    value = (value * 31) ^ hash(self.ex)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
