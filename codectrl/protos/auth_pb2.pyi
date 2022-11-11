from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

AUTHORISED: VerifyTokenRequestResultEnum
DESCRIPTOR: _descriptor.FileDescriptor
FRONTEND: TokenIntent
LOGGER: TokenIntent
NAME_ALREADY_EXISTS: GenerateTokenRequestResultEnum
NOTFOUND: VerifyTokenRequestResultEnum
TOKEN_ALREADY_EXISTS: GenerateTokenRequestResultEnum
TOKEN_GENERATION_SUCCEEDED: GenerateTokenRequestResultEnum
TOKEN_NOT_FOUND: RevokeTokenRequestResultEnum
TOKEN_REVOKATION_SUCCEEDED: RevokeTokenRequestResultEnum
UNAUTHORISED: VerifyTokenRequestResultEnum

class GenerateTokenRequest(_message.Message):
    __slots__ = ["intent", "name"]
    INTENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    intent: TokenIntent
    name: Name
    def __init__(self, name: _Optional[_Union[Name, _Mapping]] = ..., intent: _Optional[_Union[TokenIntent, str]] = ...) -> None: ...

class GenerateTokenRequestResult(_message.Message):
    __slots__ = ["status", "token"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    status: GenerateTokenRequestResultEnum
    token: Token
    def __init__(self, status: _Optional[_Union[GenerateTokenRequestResultEnum, str]] = ..., token: _Optional[_Union[Token, _Mapping]] = ...) -> None: ...

class LoginUrl(_message.Message):
    __slots__ = ["url"]
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class Name(_message.Message):
    __slots__ = ["inner"]
    INNER_FIELD_NUMBER: _ClassVar[int]
    inner: str
    def __init__(self, inner: _Optional[str] = ...) -> None: ...

class RevokeTokenRequestResult(_message.Message):
    __slots__ = ["message", "status"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    message: str
    status: RevokeTokenRequestResultEnum
    def __init__(self, message: _Optional[str] = ..., status: _Optional[_Union[RevokeTokenRequestResultEnum, str]] = ...) -> None: ...

class Token(_message.Message):
    __slots__ = ["intent", "name", "permissions"]
    INTENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    intent: TokenIntent
    name: Name
    permissions: TokenPermissions
    def __init__(self, name: _Optional[_Union[Name, _Mapping]] = ..., permissions: _Optional[_Union[TokenPermissions, _Mapping]] = ..., intent: _Optional[_Union[TokenIntent, str]] = ...) -> None: ...

class TokenPermissions(_message.Message):
    __slots__ = ["read", "write"]
    READ_FIELD_NUMBER: _ClassVar[int]
    WRITE_FIELD_NUMBER: _ClassVar[int]
    read: bool
    write: bool
    def __init__(self, read: bool = ..., write: bool = ...) -> None: ...

class VerifyTokenRequest(_message.Message):
    __slots__ = ["intent", "token"]
    INTENT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    intent: TokenIntent
    token: Token
    def __init__(self, token: _Optional[_Union[Token, _Mapping]] = ..., intent: _Optional[_Union[TokenIntent, str]] = ...) -> None: ...

class VerifyTokenRequestResult(_message.Message):
    __slots__ = ["message", "status"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    message: str
    status: VerifyTokenRequestResultEnum
    def __init__(self, message: _Optional[str] = ..., status: _Optional[_Union[VerifyTokenRequestResultEnum, str]] = ...) -> None: ...

class TokenIntent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class VerifyTokenRequestResultEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class GenerateTokenRequestResultEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class RevokeTokenRequestResultEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
