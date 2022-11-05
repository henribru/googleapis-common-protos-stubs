"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2021 Google LLC

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
import google.protobuf.descriptor
import google.protobuf.descriptor_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.extension_dict
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Visibility(google.protobuf.message.Message):
    """`Visibility` defines restrictions for the visibility of service
    elements.  Restrictions are specified using visibility labels
    (e.g., PREVIEW) that are elsewhere linked to users and projects.

    Users and projects can have access to more than one visibility label. The
    effective visibility for multiple labels is the union of each label's
    elements, plus any unrestricted elements.

    If an element and its parents have no restrictions, visibility is
    unconditionally granted.

    Example:

        visibility:
          rules:
          - selector: google.calendar.Calendar.EnhancedSearch
            restriction: PREVIEW
          - selector: google.calendar.Calendar.Delegate
            restriction: INTERNAL

    Here, all methods are publicly visible except for the restricted methods
    EnhancedSearch and Delegate.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RULES_FIELD_NUMBER: builtins.int
    @property
    def rules(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___VisibilityRule
    ]:
        """A list of visibility rules that apply to individual API elements.

        **NOTE:** All service configuration rules follow "last one wins" order.
        """
    def __init__(
        self,
        *,
        rules: collections.abc.Iterable[global___VisibilityRule] | None = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["rules", b"rules"]
    ) -> None: ...

global___Visibility = Visibility

@typing_extensions.final
class VisibilityRule(google.protobuf.message.Message):
    """A visibility rule provides visibility configuration for an individual API
    element.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SELECTOR_FIELD_NUMBER: builtins.int
    RESTRICTION_FIELD_NUMBER: builtins.int
    selector: builtins.str
    """Selects methods, messages, fields, enums, etc. to which this rule applies.

    Refer to [selector][google.api.DocumentationRule.selector] for syntax details.
    """
    restriction: builtins.str
    """A comma-separated list of visibility labels that apply to the `selector`.
    Any of the listed labels can be used to grant the visibility.

    If a rule has multiple labels, removing one of the labels but not all of
    them can break clients.

    Example:

        visibility:
          rules:
          - selector: google.calendar.Calendar.EnhancedSearch
            restriction: INTERNAL, PREVIEW

    Removing INTERNAL from this restriction will break clients that rely on
    this method and only had access to it through INTERNAL.
    """
    def __init__(
        self,
        *,
        selector: builtins.str = ...,
        restriction: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "restriction", b"restriction", "selector", b"selector"
        ],
    ) -> None: ...

global___VisibilityRule = VisibilityRule

ENUM_VISIBILITY_FIELD_NUMBER: builtins.int
VALUE_VISIBILITY_FIELD_NUMBER: builtins.int
FIELD_VISIBILITY_FIELD_NUMBER: builtins.int
MESSAGE_VISIBILITY_FIELD_NUMBER: builtins.int
METHOD_VISIBILITY_FIELD_NUMBER: builtins.int
API_VISIBILITY_FIELD_NUMBER: builtins.int
enum_visibility: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[
    google.protobuf.descriptor_pb2.EnumOptions, global___VisibilityRule
]
"""See `VisibilityRule`."""
value_visibility: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[
    google.protobuf.descriptor_pb2.EnumValueOptions, global___VisibilityRule
]
"""See `VisibilityRule`."""
field_visibility: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[
    google.protobuf.descriptor_pb2.FieldOptions, global___VisibilityRule
]
"""See `VisibilityRule`."""
message_visibility: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[
    google.protobuf.descriptor_pb2.MessageOptions, global___VisibilityRule
]
"""See `VisibilityRule`."""
method_visibility: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[
    google.protobuf.descriptor_pb2.MethodOptions, global___VisibilityRule
]
"""See `VisibilityRule`."""
api_visibility: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[
    google.protobuf.descriptor_pb2.ServiceOptions, global___VisibilityRule
]
"""See `VisibilityRule`."""
