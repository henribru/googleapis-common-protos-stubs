"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

# Represents a month in the Gregorian calendar.
class Month(_Month, metaclass=_MonthEnumTypeWrapper):
    pass

class _Month:
    V = typing.NewType("V", builtins.int)

class _MonthEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Month.V], builtins.type
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    # The unspecifed month.
    MONTH_UNSPECIFIED = Month.V(0)
    # The month of January.
    JANUARY = Month.V(1)
    # The month of February.
    FEBRUARY = Month.V(2)
    # The month of March.
    MARCH = Month.V(3)
    # The month of April.
    APRIL = Month.V(4)
    # The month of May.
    MAY = Month.V(5)
    # The month of June.
    JUNE = Month.V(6)
    # The month of July.
    JULY = Month.V(7)
    # The month of August.
    AUGUST = Month.V(8)
    # The month of September.
    SEPTEMBER = Month.V(9)
    # The month of October.
    OCTOBER = Month.V(10)
    # The month of November.
    NOVEMBER = Month.V(11)
    # The month of December.
    DECEMBER = Month.V(12)

# The unspecifed month.
MONTH_UNSPECIFIED = Month.V(0)
# The month of January.
JANUARY = Month.V(1)
# The month of February.
FEBRUARY = Month.V(2)
# The month of March.
MARCH = Month.V(3)
# The month of April.
APRIL = Month.V(4)
# The month of May.
MAY = Month.V(5)
# The month of June.
JUNE = Month.V(6)
# The month of July.
JULY = Month.V(7)
# The month of August.
AUGUST = Month.V(8)
# The month of September.
SEPTEMBER = Month.V(9)
# The month of October.
OCTOBER = Month.V(10)
# The month of November.
NOVEMBER = Month.V(11)
# The month of December.
DECEMBER = Month.V(12)
global___Month = Month
