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


class Backend(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def rules(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[BackendRule]: ...

    def __init__(self,
        *,
        rules : typing___Optional[typing___Iterable[BackendRule]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Backend: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"rules"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"rules",b"rules"]) -> None: ...

class BackendRule(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class PathTranslation(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> BackendRule.PathTranslation: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[BackendRule.PathTranslation]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, BackendRule.PathTranslation]]: ...
        PATH_TRANSLATION_UNSPECIFIED = typing___cast(BackendRule.PathTranslation, 0)
        CONSTANT_ADDRESS = typing___cast(BackendRule.PathTranslation, 1)
        APPEND_PATH_TO_ADDRESS = typing___cast(BackendRule.PathTranslation, 2)
    PATH_TRANSLATION_UNSPECIFIED = typing___cast(BackendRule.PathTranslation, 0)
    CONSTANT_ADDRESS = typing___cast(BackendRule.PathTranslation, 1)
    APPEND_PATH_TO_ADDRESS = typing___cast(BackendRule.PathTranslation, 2)

    selector = ... # type: typing___Text
    address = ... # type: typing___Text
    deadline = ... # type: float
    min_deadline = ... # type: float
    operation_deadline = ... # type: float
    path_translation = ... # type: BackendRule.PathTranslation
    jwt_audience = ... # type: typing___Text

    def __init__(self,
        *,
        selector : typing___Optional[typing___Text] = None,
        address : typing___Optional[typing___Text] = None,
        deadline : typing___Optional[float] = None,
        min_deadline : typing___Optional[float] = None,
        operation_deadline : typing___Optional[float] = None,
        path_translation : typing___Optional[BackendRule.PathTranslation] = None,
        jwt_audience : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BackendRule: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"authentication",u"jwt_audience"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"address",u"authentication",u"deadline",u"jwt_audience",u"min_deadline",u"operation_deadline",u"path_translation",u"selector"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"authentication",b"authentication",u"jwt_audience",b"jwt_audience"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"address",b"address",u"authentication",b"authentication",u"deadline",b"deadline",u"jwt_audience",b"jwt_audience",u"min_deadline",b"min_deadline",u"operation_deadline",b"operation_deadline",u"path_translation",b"path_translation",u"selector",b"selector"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"authentication",b"authentication"]) -> typing_extensions___Literal["jwt_audience"]: ...
