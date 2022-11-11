import log_pb2 as _log_pb2
import auth_pb2 as _auth_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

CONFIRMED: RequestStatus
DESCRIPTOR: _descriptor.FileDescriptor
ERROR: RequestStatus

class Connection(_message.Message):
    __slots__ = ["token", "uuid"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    token: _auth_pb2.Token
    uuid: str
    def __init__(self, uuid: _Optional[str] = ..., token: _Optional[_Union[_auth_pb2.Token, _Mapping]] = ...) -> None: ...

class RequestResult(_message.Message):
    __slots__ = ["authStatus", "message", "status"]
    AUTHSTATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    authStatus: _auth_pb2.GenerateTokenRequestResult
    message: str
    status: RequestStatus
    def __init__(self, message: _Optional[str] = ..., status: _Optional[_Union[RequestStatus, str]] = ..., authStatus: _Optional[_Union[_auth_pb2.GenerateTokenRequestResult, _Mapping]] = ...) -> None: ...

class ServerDetails(_message.Message):
    __slots__ = ["host", "port", "requiresAuthentication", "uptime"]
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    REQUIRESAUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    UPTIME_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    requiresAuthentication: bool
    uptime: int
    def __init__(self, host: _Optional[str] = ..., port: _Optional[int] = ..., uptime: _Optional[int] = ..., requiresAuthentication: bool = ...) -> None: ...

class RequestStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
