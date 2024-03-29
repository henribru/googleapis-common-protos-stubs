"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2023 Google LLC

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
import google.api.label_pb2
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
class LogDescriptor(google.protobuf.message.Message):
    """A description of a log type. Example in YAML format:

    - name: library.googleapis.com/activity_history
      description: The history of borrowing and returning library items.
      display_name: Activity
      labels:
      - key: /customer_id
        description: Identifier of a library customer
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """The name of the log. It must be less than 512 characters long and can
    include the following characters: upper- and lower-case alphanumeric
    characters [A-Za-z0-9], and punctuation characters including
    slash, underscore, hyphen, period [/_-.].
    """
    @property
    def labels(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        google.api.label_pb2.LabelDescriptor
    ]:
        """The set of labels that are available to describe a specific log entry.
        Runtime requests that contain labels not specified here are
        considered invalid.
        """
    description: builtins.str
    """A human-readable description of this log. This information appears in
    the documentation and can contain details.
    """
    display_name: builtins.str
    """The human-readable name for this log. This information appears on
    the user interface and should be concise.
    """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        labels: (
            collections.abc.Iterable[google.api.label_pb2.LabelDescriptor] | None
        ) = ...,
        description: builtins.str = ...,
        display_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "description",
            b"description",
            "display_name",
            b"display_name",
            "labels",
            b"labels",
            "name",
            b"name",
        ],
    ) -> None: ...

global___LogDescriptor = LogDescriptor
