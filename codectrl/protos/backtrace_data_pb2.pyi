from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BacktraceData(_message.Message):
    __slots__ = ["code", "columnNumber", "filePath", "lineNumber", "name"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    COLUMNNUMBER_FIELD_NUMBER: _ClassVar[int]
    FILEPATH_FIELD_NUMBER: _ClassVar[int]
    LINENUMBER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    code: str
    columnNumber: int
    filePath: str
    lineNumber: int
    name: str
    def __init__(self, name: _Optional[str] = ..., filePath: _Optional[str] = ..., lineNumber: _Optional[int] = ..., columnNumber: _Optional[int] = ..., code: _Optional[str] = ...) -> None: ...
