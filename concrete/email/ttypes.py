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


class EmailAddress(object):
    """
    An email address, optionally accompanied by a display_name. These
    values are typically extracted from strings such as:
    <tt> "John Smith" &lt;john\@xyz.com&gt; </tt>.

    \see RFC2822 http://tools.ietf.org/html/rfc2822

    Attributes:
     - address
     - displayName
    """


    def __init__(self, address=None, displayName=None,):
        self.address = address
        self.displayName = displayName

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
                    self.address = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.displayName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('EmailAddress')
        if self.address is not None:
            oprot.writeFieldBegin('address', TType.STRING, 1)
            oprot.writeString(self.address.encode('utf-8') if sys.version_info[0] == 2 else self.address)
            oprot.writeFieldEnd()
        if self.displayName is not None:
            oprot.writeFieldBegin('displayName', TType.STRING, 2)
            oprot.writeString(self.displayName.encode('utf-8') if sys.version_info[0] == 2 else self.displayName)
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


class EmailCommunicationInfo(object):
    """
    Extra information about an email communication instance.

    Attributes:
     - messageId
     - contentType
     - userAgent
     - inReplyToList
     - referenceList
     - senderAddress
     - returnPathAddress
     - toAddressList
     - ccAddressList
     - bccAddressList
     - emailFolder
     - subject
     - quotedAddresses
     - attachmentPaths
     - salutation
     - signature
    """


    def __init__(self, messageId=None, contentType=None, userAgent=None, inReplyToList=None, referenceList=None, senderAddress=None, returnPathAddress=None, toAddressList=None, ccAddressList=None, bccAddressList=None, emailFolder=None, subject=None, quotedAddresses=None, attachmentPaths=None, salutation=None, signature=None,):
        self.messageId = messageId
        self.contentType = contentType
        self.userAgent = userAgent
        self.inReplyToList = inReplyToList
        self.referenceList = referenceList
        self.senderAddress = senderAddress
        self.returnPathAddress = returnPathAddress
        self.toAddressList = toAddressList
        self.ccAddressList = ccAddressList
        self.bccAddressList = bccAddressList
        self.emailFolder = emailFolder
        self.subject = subject
        self.quotedAddresses = quotedAddresses
        self.attachmentPaths = attachmentPaths
        self.salutation = salutation
        self.signature = signature

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
                    self.messageId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.contentType = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.userAgent = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.inReplyToList = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.inReplyToList.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.LIST:
                    self.referenceList = []
                    (_etype9, _size6) = iprot.readListBegin()
                    for _i10 in range(_size6):
                        _elem11 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.referenceList.append(_elem11)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRUCT:
                    self.senderAddress = EmailAddress()
                    self.senderAddress.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRUCT:
                    self.returnPathAddress = EmailAddress()
                    self.returnPathAddress.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.LIST:
                    self.toAddressList = []
                    (_etype15, _size12) = iprot.readListBegin()
                    for _i16 in range(_size12):
                        _elem17 = EmailAddress()
                        _elem17.read(iprot)
                        self.toAddressList.append(_elem17)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.LIST:
                    self.ccAddressList = []
                    (_etype21, _size18) = iprot.readListBegin()
                    for _i22 in range(_size18):
                        _elem23 = EmailAddress()
                        _elem23.read(iprot)
                        self.ccAddressList.append(_elem23)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.LIST:
                    self.bccAddressList = []
                    (_etype27, _size24) = iprot.readListBegin()
                    for _i28 in range(_size24):
                        _elem29 = EmailAddress()
                        _elem29.read(iprot)
                        self.bccAddressList.append(_elem29)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.emailFolder = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRING:
                    self.subject = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.LIST:
                    self.quotedAddresses = []
                    (_etype33, _size30) = iprot.readListBegin()
                    for _i34 in range(_size30):
                        _elem35 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.quotedAddresses.append(_elem35)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.LIST:
                    self.attachmentPaths = []
                    (_etype39, _size36) = iprot.readListBegin()
                    for _i40 in range(_size36):
                        _elem41 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.attachmentPaths.append(_elem41)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.STRING:
                    self.salutation = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 16:
                if ftype == TType.STRING:
                    self.signature = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('EmailCommunicationInfo')
        if self.messageId is not None:
            oprot.writeFieldBegin('messageId', TType.STRING, 1)
            oprot.writeString(self.messageId.encode('utf-8') if sys.version_info[0] == 2 else self.messageId)
            oprot.writeFieldEnd()
        if self.contentType is not None:
            oprot.writeFieldBegin('contentType', TType.STRING, 2)
            oprot.writeString(self.contentType.encode('utf-8') if sys.version_info[0] == 2 else self.contentType)
            oprot.writeFieldEnd()
        if self.userAgent is not None:
            oprot.writeFieldBegin('userAgent', TType.STRING, 3)
            oprot.writeString(self.userAgent.encode('utf-8') if sys.version_info[0] == 2 else self.userAgent)
            oprot.writeFieldEnd()
        if self.inReplyToList is not None:
            oprot.writeFieldBegin('inReplyToList', TType.LIST, 4)
            oprot.writeListBegin(TType.STRING, len(self.inReplyToList))
            for iter42 in self.inReplyToList:
                oprot.writeString(iter42.encode('utf-8') if sys.version_info[0] == 2 else iter42)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.referenceList is not None:
            oprot.writeFieldBegin('referenceList', TType.LIST, 5)
            oprot.writeListBegin(TType.STRING, len(self.referenceList))
            for iter43 in self.referenceList:
                oprot.writeString(iter43.encode('utf-8') if sys.version_info[0] == 2 else iter43)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.senderAddress is not None:
            oprot.writeFieldBegin('senderAddress', TType.STRUCT, 6)
            self.senderAddress.write(oprot)
            oprot.writeFieldEnd()
        if self.returnPathAddress is not None:
            oprot.writeFieldBegin('returnPathAddress', TType.STRUCT, 7)
            self.returnPathAddress.write(oprot)
            oprot.writeFieldEnd()
        if self.toAddressList is not None:
            oprot.writeFieldBegin('toAddressList', TType.LIST, 8)
            oprot.writeListBegin(TType.STRUCT, len(self.toAddressList))
            for iter44 in self.toAddressList:
                iter44.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.ccAddressList is not None:
            oprot.writeFieldBegin('ccAddressList', TType.LIST, 9)
            oprot.writeListBegin(TType.STRUCT, len(self.ccAddressList))
            for iter45 in self.ccAddressList:
                iter45.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.bccAddressList is not None:
            oprot.writeFieldBegin('bccAddressList', TType.LIST, 10)
            oprot.writeListBegin(TType.STRUCT, len(self.bccAddressList))
            for iter46 in self.bccAddressList:
                iter46.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.emailFolder is not None:
            oprot.writeFieldBegin('emailFolder', TType.STRING, 11)
            oprot.writeString(self.emailFolder.encode('utf-8') if sys.version_info[0] == 2 else self.emailFolder)
            oprot.writeFieldEnd()
        if self.subject is not None:
            oprot.writeFieldBegin('subject', TType.STRING, 12)
            oprot.writeString(self.subject.encode('utf-8') if sys.version_info[0] == 2 else self.subject)
            oprot.writeFieldEnd()
        if self.quotedAddresses is not None:
            oprot.writeFieldBegin('quotedAddresses', TType.LIST, 13)
            oprot.writeListBegin(TType.STRING, len(self.quotedAddresses))
            for iter47 in self.quotedAddresses:
                oprot.writeString(iter47.encode('utf-8') if sys.version_info[0] == 2 else iter47)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.attachmentPaths is not None:
            oprot.writeFieldBegin('attachmentPaths', TType.LIST, 14)
            oprot.writeListBegin(TType.STRING, len(self.attachmentPaths))
            for iter48 in self.attachmentPaths:
                oprot.writeString(iter48.encode('utf-8') if sys.version_info[0] == 2 else iter48)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.salutation is not None:
            oprot.writeFieldBegin('salutation', TType.STRING, 15)
            oprot.writeString(self.salutation.encode('utf-8') if sys.version_info[0] == 2 else self.salutation)
            oprot.writeFieldEnd()
        if self.signature is not None:
            oprot.writeFieldBegin('signature', TType.STRING, 16)
            oprot.writeString(self.signature.encode('utf-8') if sys.version_info[0] == 2 else self.signature)
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
all_structs.append(EmailAddress)
EmailAddress.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'address', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'displayName', 'UTF8', None, ),  # 2
)
all_structs.append(EmailCommunicationInfo)
EmailCommunicationInfo.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'messageId', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'contentType', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'userAgent', 'UTF8', None, ),  # 3
    (4, TType.LIST, 'inReplyToList', (TType.STRING, 'UTF8', False), None, ),  # 4
    (5, TType.LIST, 'referenceList', (TType.STRING, 'UTF8', False), None, ),  # 5
    (6, TType.STRUCT, 'senderAddress', [EmailAddress, None], None, ),  # 6
    (7, TType.STRUCT, 'returnPathAddress', [EmailAddress, None], None, ),  # 7
    (8, TType.LIST, 'toAddressList', (TType.STRUCT, [EmailAddress, None], False), None, ),  # 8
    (9, TType.LIST, 'ccAddressList', (TType.STRUCT, [EmailAddress, None], False), None, ),  # 9
    (10, TType.LIST, 'bccAddressList', (TType.STRUCT, [EmailAddress, None], False), None, ),  # 10
    (11, TType.STRING, 'emailFolder', 'UTF8', None, ),  # 11
    (12, TType.STRING, 'subject', 'UTF8', None, ),  # 12
    (13, TType.LIST, 'quotedAddresses', (TType.STRING, 'UTF8', False), None, ),  # 13
    (14, TType.LIST, 'attachmentPaths', (TType.STRING, 'UTF8', False), None, ),  # 14
    (15, TType.STRING, 'salutation', 'UTF8', None, ),  # 15
    (16, TType.STRING, 'signature', 'UTF8', None, ),  # 16
)
fix_spec(all_structs)
del all_structs
