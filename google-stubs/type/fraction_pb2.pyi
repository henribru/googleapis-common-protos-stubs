"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Fraction(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NUMERATOR_FIELD_NUMBER: builtins.int
    DENOMINATOR_FIELD_NUMBER: builtins.int
    numerator: builtins.int = ...
    denominator: builtins.int = ...
    def __init__(
        self,
        *,
        numerator: builtins.int = ...,
        denominator: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "denominator", b"denominator", "numerator", b"numerator"
        ],
    ) -> None: ...

global___Fraction = Fraction
