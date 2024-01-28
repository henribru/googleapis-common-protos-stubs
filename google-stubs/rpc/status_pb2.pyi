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
import collections.abc
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Status(google.protobuf.message.Message):
    """The `Status` type defines a logical error model that is suitable for
    different programming environments, including REST APIs and RPC APIs. It is
    used by [gRPC](https://github.com/grpc). Each `Status` message contains
    three pieces of data: error code, error message, and error details.

    You can find out more about this error model and how to work with it in the
    [API Design Guide](https://cloud.google.com/apis/design/errors).
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CODE_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    DETAILS_FIELD_NUMBER: builtins.int
    code: builtins.int
    """The status code, which should be an enum value of
    [google.rpc.Code][google.rpc.Code].
    """
    message: builtins.str
    """A developer-facing error message, which should be in English. Any
    user-facing error message should be localized and sent in the
    [google.rpc.Status.details][google.rpc.Status.details] field, or localized
    by the client.
    """
    @property
    def details(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        google.protobuf.any_pb2.Any
    ]:
        """A list of messages that carry the error details.  There is a common set of
        message types for APIs to use.
        """

    def __init__(
        self,
        *,
        code: builtins.int = ...,
        message: builtins.str = ...,
        details: collections.abc.Iterable[google.protobuf.any_pb2.Any] | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "code", b"code", "details", b"details", "message", b"message"
        ],
    ) -> None: ...

global___Status = Status
