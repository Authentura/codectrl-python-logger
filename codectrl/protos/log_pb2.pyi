import backtrace_data_pb2 as _backtrace_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Log(_message.Message):
    __slots__ = ["address", "codeSnippet", "fileName", "language", "lineNumber", "message", "messageType", "stack", "uuid", "warnings"]
    class CodeSnippetEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CODESNIPPET_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    LINENUMBER_FIELD_NUMBER: _ClassVar[int]
    MESSAGETYPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STACK_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    address: str
    codeSnippet: _containers.ScalarMap[int, str]
    fileName: str
    language: str
    lineNumber: int
    message: str
    messageType: str
    stack: _containers.RepeatedCompositeFieldContainer[_backtrace_data_pb2.BacktraceData]
    uuid: str
    warnings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, uuid: _Optional[str] = ..., stack: _Optional[_Iterable[_Union[_backtrace_data_pb2.BacktraceData, _Mapping]]] = ..., lineNumber: _Optional[int] = ..., codeSnippet: _Optional[_Mapping[int, str]] = ..., message: _Optional[str] = ..., messageType: _Optional[str] = ..., fileName: _Optional[str] = ..., address: _Optional[str] = ..., language: _Optional[str] = ..., warnings: _Optional[_Iterable[str]] = ...) -> None: ...
