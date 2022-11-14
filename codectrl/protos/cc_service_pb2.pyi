"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from . import auth_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _RequestStatus:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _RequestStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_RequestStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    CONFIRMED: _RequestStatus.ValueType  # 0
    ERROR: _RequestStatus.ValueType  # 1

class RequestStatus(_RequestStatus, metaclass=_RequestStatusEnumTypeWrapper):
    """Status codes for whether or not a particular request has succeeded."""

CONFIRMED: RequestStatus.ValueType  # 0
ERROR: RequestStatus.ValueType  # 1
global___RequestStatus = RequestStatus

@typing_extensions.final
class Connection(google.protobuf.message.Message):
    """Describes the connection between the interface and a given server. Each
    client is supplied with a uuid that is saved to disk or to localStorage. The
    server uses this information to determine which logs should be sent to each
    client and to skip duplicate identified by the `uuid` of the log.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UUID_FIELD_NUMBER: builtins.int
    TOKEN_FIELD_NUMBER: builtins.int
    uuid: builtins.str
    @property
    def token(self) -> auth_pb2.Token: ...
    def __init__(
        self,
        *,
        uuid: builtins.str = ...,
        token: auth_pb2.Token | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_token", b"_token", "token", b"token"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_token", b"_token", "token", b"token", "uuid", b"uuid"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_token", b"_token"]) -> typing_extensions.Literal["token"] | None: ...

global___Connection = Connection

@typing_extensions.final
class RequestResult(google.protobuf.message.Message):
    """Returned by the procedures to describe the result of a request."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MESSAGE_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    AUTHSTATUS_FIELD_NUMBER: builtins.int
    message: builtins.str
    status: global___RequestStatus.ValueType
    @property
    def authStatus(self) -> auth_pb2.GenerateTokenRequestResult: ...
    def __init__(
        self,
        *,
        message: builtins.str = ...,
        status: global___RequestStatus.ValueType = ...,
        authStatus: auth_pb2.GenerateTokenRequestResult | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_authStatus", b"_authStatus", "authStatus", b"authStatus"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_authStatus", b"_authStatus", "authStatus", b"authStatus", "message", b"message", "status", b"status"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_authStatus", b"_authStatus"]) -> typing_extensions.Literal["authStatus"] | None: ...

global___RequestResult = RequestResult

@typing_extensions.final
class ServerDetails(google.protobuf.message.Message):
    """Server details about the current gRPC server."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_FIELD_NUMBER: builtins.int
    PORT_FIELD_NUMBER: builtins.int
    UPTIME_FIELD_NUMBER: builtins.int
    REQUIRESAUTHENTICATION_FIELD_NUMBER: builtins.int
    host: builtins.str
    port: builtins.int
    uptime: builtins.int
    requiresAuthentication: builtins.bool
    def __init__(
        self,
        *,
        host: builtins.str = ...,
        port: builtins.int = ...,
        uptime: builtins.int = ...,
        requiresAuthentication: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["host", b"host", "port", b"port", "requiresAuthentication", b"requiresAuthentication", "uptime", b"uptime"]) -> None: ...

global___ServerDetails = ServerDetails