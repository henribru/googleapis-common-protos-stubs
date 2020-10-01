# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class Context(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def rules(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ContextRule]: ...

    def __init__(self,
        *,
        rules : typing___Optional[typing___Iterable[ContextRule]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Context: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"rules"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"rules",b"rules"]) -> None: ...

class ContextRule(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    selector = ... # type: typing___Text
    requested = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    provided = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    allowed_request_extensions = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    allowed_response_extensions = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    def __init__(self,
        *,
        selector : typing___Optional[typing___Text] = None,
        requested : typing___Optional[typing___Iterable[typing___Text]] = None,
        provided : typing___Optional[typing___Iterable[typing___Text]] = None,
        allowed_request_extensions : typing___Optional[typing___Iterable[typing___Text]] = None,
        allowed_response_extensions : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ContextRule: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"allowed_request_extensions",u"allowed_response_extensions",u"provided",u"requested",u"selector"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"allowed_request_extensions",b"allowed_request_extensions",u"allowed_response_extensions",b"allowed_response_extensions",u"provided",b"provided",u"requested",b"requested",u"selector",b"selector"]) -> None: ...