# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    List as typing___List,
    Tuple as typing___Tuple,
    cast as typing___cast,
)


class DayOfWeek(int):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: int) -> str: ...
    @classmethod
    def Value(cls, name: str) -> DayOfWeek: ...
    @classmethod
    def keys(cls) -> typing___List[str]: ...
    @classmethod
    def values(cls) -> typing___List[DayOfWeek]: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[str, DayOfWeek]]: ...
    DAY_OF_WEEK_UNSPECIFIED = typing___cast(DayOfWeek, 0)
    MONDAY = typing___cast(DayOfWeek, 1)
    TUESDAY = typing___cast(DayOfWeek, 2)
    WEDNESDAY = typing___cast(DayOfWeek, 3)
    THURSDAY = typing___cast(DayOfWeek, 4)
    FRIDAY = typing___cast(DayOfWeek, 5)
    SATURDAY = typing___cast(DayOfWeek, 6)
    SUNDAY = typing___cast(DayOfWeek, 7)
DAY_OF_WEEK_UNSPECIFIED = typing___cast(DayOfWeek, 0)
MONDAY = typing___cast(DayOfWeek, 1)
TUESDAY = typing___cast(DayOfWeek, 2)
WEDNESDAY = typing___cast(DayOfWeek, 3)
THURSDAY = typing___cast(DayOfWeek, 4)
FRIDAY = typing___cast(DayOfWeek, 5)
SATURDAY = typing___cast(DayOfWeek, 6)
SUNDAY = typing___cast(DayOfWeek, 7)
