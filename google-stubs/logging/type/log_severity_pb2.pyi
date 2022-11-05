"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2022 Google LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _LogSeverity:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _LogSeverityEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_LogSeverity.ValueType],
    builtins.type,
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    DEFAULT: _LogSeverity.ValueType  # 0
    """(0) The log entry has no assigned severity level."""
    DEBUG: _LogSeverity.ValueType  # 100
    """(100) Debug or trace information."""
    INFO: _LogSeverity.ValueType  # 200
    """(200) Routine information, such as ongoing status or performance."""
    NOTICE: _LogSeverity.ValueType  # 300
    """(300) Normal but significant events, such as start up, shut down, or
    a configuration change.
    """
    WARNING: _LogSeverity.ValueType  # 400
    """(400) Warning events might cause problems."""
    ERROR: _LogSeverity.ValueType  # 500
    """(500) Error events are likely to cause problems."""
    CRITICAL: _LogSeverity.ValueType  # 600
    """(600) Critical events cause more severe problems or outages."""
    ALERT: _LogSeverity.ValueType  # 700
    """(700) A person must take an action immediately."""
    EMERGENCY: _LogSeverity.ValueType  # 800
    """(800) One or more systems are unusable."""

class LogSeverity(_LogSeverity, metaclass=_LogSeverityEnumTypeWrapper):
    """The severity of the event described in a log entry, expressed as one of the
    standard severity levels listed below.  For your reference, the levels are
    assigned the listed numeric values. The effect of using numeric values other
    than those listed is undefined.

    You can filter for log entries by severity.  For example, the following
    filter expression will match log entries with severities `INFO`, `NOTICE`,
    and `WARNING`:

        severity > DEBUG AND severity <= WARNING

    If you are writing log entries, you should map other severity encodings to
    one of these standard levels. For example, you might map all of Java's FINE,
    FINER, and FINEST levels to `LogSeverity.DEBUG`. You can preserve the
    original severity level in the log entry payload if you wish.
    """

DEFAULT: LogSeverity.ValueType  # 0
"""(0) The log entry has no assigned severity level."""
DEBUG: LogSeverity.ValueType  # 100
"""(100) Debug or trace information."""
INFO: LogSeverity.ValueType  # 200
"""(200) Routine information, such as ongoing status or performance."""
NOTICE: LogSeverity.ValueType  # 300
"""(300) Normal but significant events, such as start up, shut down, or
a configuration change.
"""
WARNING: LogSeverity.ValueType  # 400
"""(400) Warning events might cause problems."""
ERROR: LogSeverity.ValueType  # 500
"""(500) Error events are likely to cause problems."""
CRITICAL: LogSeverity.ValueType  # 600
"""(600) Critical events cause more severe problems or outages."""
ALERT: LogSeverity.ValueType  # 700
"""(700) A person must take an action immediately."""
EMERGENCY: LogSeverity.ValueType  # 800
"""(800) One or more systems are unusable."""
global___LogSeverity = LogSeverity
