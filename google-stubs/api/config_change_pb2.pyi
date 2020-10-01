# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    List as typing___List,
    Optional as typing___Optional,
    Text as typing___Text,
    Tuple as typing___Tuple,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class ChangeType(int):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: int) -> str: ...
    @classmethod
    def Value(cls, name: str) -> ChangeType: ...
    @classmethod
    def keys(cls) -> typing___List[str]: ...
    @classmethod
    def values(cls) -> typing___List[ChangeType]: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[str, ChangeType]]: ...
    CHANGE_TYPE_UNSPECIFIED = typing___cast(ChangeType, 0)
    ADDED = typing___cast(ChangeType, 1)
    REMOVED = typing___cast(ChangeType, 2)
    MODIFIED = typing___cast(ChangeType, 3)
CHANGE_TYPE_UNSPECIFIED = typing___cast(ChangeType, 0)
ADDED = typing___cast(ChangeType, 1)
REMOVED = typing___cast(ChangeType, 2)
MODIFIED = typing___cast(ChangeType, 3)

class ConfigChange(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    element = ... # type: typing___Text
    old_value = ... # type: typing___Text
    new_value = ... # type: typing___Text
    change_type = ... # type: ChangeType

    @property
    def advices(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Advice]: ...

    def __init__(self,
        *,
        element : typing___Optional[typing___Text] = None,
        old_value : typing___Optional[typing___Text] = None,
        new_value : typing___Optional[typing___Text] = None,
        change_type : typing___Optional[ChangeType] = None,
        advices : typing___Optional[typing___Iterable[Advice]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ConfigChange: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"advices",u"change_type",u"element",u"new_value",u"old_value"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"advices",b"advices",u"change_type",b"change_type",u"element",b"element",u"new_value",b"new_value",u"old_value",b"old_value"]) -> None: ...

class Advice(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    description = ... # type: typing___Text

    def __init__(self,
        *,
        description : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Advice: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"description"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"description",b"description"]) -> None: ...