"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

global___Code = Code

class _Code(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Code.V], builtins.type
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    OK = Code.V(0)
    CANCELLED = Code.V(1)
    UNKNOWN = Code.V(2)
    INVALID_ARGUMENT = Code.V(3)
    DEADLINE_EXCEEDED = Code.V(4)
    NOT_FOUND = Code.V(5)
    ALREADY_EXISTS = Code.V(6)
    PERMISSION_DENIED = Code.V(7)
    UNAUTHENTICATED = Code.V(16)
    RESOURCE_EXHAUSTED = Code.V(8)
    FAILED_PRECONDITION = Code.V(9)
    ABORTED = Code.V(10)
    OUT_OF_RANGE = Code.V(11)
    UNIMPLEMENTED = Code.V(12)
    INTERNAL = Code.V(13)
    UNAVAILABLE = Code.V(14)
    DATA_LOSS = Code.V(15)

class Code(metaclass=_Code):
    V = typing.NewType("V", builtins.int)

OK = Code.V(0)
CANCELLED = Code.V(1)
UNKNOWN = Code.V(2)
INVALID_ARGUMENT = Code.V(3)
DEADLINE_EXCEEDED = Code.V(4)
NOT_FOUND = Code.V(5)
ALREADY_EXISTS = Code.V(6)
PERMISSION_DENIED = Code.V(7)
UNAUTHENTICATED = Code.V(16)
RESOURCE_EXHAUSTED = Code.V(8)
FAILED_PRECONDITION = Code.V(9)
ABORTED = Code.V(10)
OUT_OF_RANGE = Code.V(11)
UNIMPLEMENTED = Code.V(12)
INTERNAL = Code.V(13)
UNAVAILABLE = Code.V(14)
DATA_LOSS = Code.V(15)
