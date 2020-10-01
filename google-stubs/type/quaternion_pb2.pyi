# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class Quaternion(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    x = ... # type: float
    y = ... # type: float
    z = ... # type: float
    w = ... # type: float

    def __init__(self,
        *,
        x : typing___Optional[float] = None,
        y : typing___Optional[float] = None,
        z : typing___Optional[float] = None,
        w : typing___Optional[float] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Quaternion: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"w",u"x",u"y",u"z"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"w",b"w",u"x",b"x",u"y",b"y",u"z",b"z"]) -> None: ...