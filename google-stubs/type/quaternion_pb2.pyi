"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Quaternion(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    Z_FIELD_NUMBER: builtins.int
    W_FIELD_NUMBER: builtins.int
    x: builtins.float = ...
    y: builtins.float = ...
    z: builtins.float = ...
    w: builtins.float = ...
    def __init__(
        self,
        *,
        x: builtins.float = ...,
        y: builtins.float = ...,
        z: builtins.float = ...,
        w: builtins.float = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "w", b"w", "x", b"x", "y", b"y", "z", b"z"
        ],
    ) -> None: ...

global___Quaternion = Quaternion
