"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2020 Google LLC

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
class ListLocationsRequest(google.protobuf.message.Message):
    """The request message for [Locations.ListLocations][google.cloud.location.Locations.ListLocations]."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    name: builtins.str
    """The resource that owns the locations collection, if applicable."""
    filter: builtins.str
    """The standard list filter."""
    page_size: builtins.int
    """The standard list page size."""
    page_token: builtins.str
    """The standard list page token."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        filter: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "filter",
            b"filter",
            "name",
            b"name",
            "page_size",
            b"page_size",
            "page_token",
            b"page_token",
        ],
    ) -> None: ...

global___ListLocationsRequest = ListLocationsRequest

@typing_extensions.final
class ListLocationsResponse(google.protobuf.message.Message):
    """The response message for [Locations.ListLocations][google.cloud.location.Locations.ListLocations]."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOCATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    @property
    def locations(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___Location
    ]:
        """A list of locations that matches the specified filter in the request."""
    next_page_token: builtins.str
    """The standard List next-page token."""
    def __init__(
        self,
        *,
        locations: collections.abc.Iterable[global___Location] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "locations", b"locations", "next_page_token", b"next_page_token"
        ],
    ) -> None: ...

global___ListLocationsResponse = ListLocationsResponse

@typing_extensions.final
class GetLocationRequest(google.protobuf.message.Message):
    """The request message for [Locations.GetLocation][google.cloud.location.Locations.GetLocation]."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Resource name for the location."""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["name", b"name"]
    ) -> None: ...

global___GetLocationRequest = GetLocationRequest

@typing_extensions.final
class Location(google.protobuf.message.Message):
    """A resource that represents Google Cloud Platform location."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    @typing_extensions.final
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...
    NAME_FIELD_NUMBER: builtins.int
    LOCATION_ID_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Resource name for the location, which may vary between implementations.
    For example: `"projects/example-project/locations/us-east1"`
    """
    location_id: builtins.str
    """The canonical id for this location. For example: `"us-east1"`."""
    display_name: builtins.str
    """The friendly name for this location, typically a nearby city name.
    For example, "Tokyo".
    """
    @property
    def labels(
        self,
    ) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Cross-service attributes for the location. For example

        {"cloud.googleapis.com/region": "us-east1"}
        """
    @property
    def metadata(self) -> google.protobuf.any_pb2.Any:
        """Service-specific metadata. For example the available capacity at the given
        location.
        """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        location_id: builtins.str = ...,
        display_name: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        metadata: google.protobuf.any_pb2.Any | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["metadata", b"metadata"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "display_name",
            b"display_name",
            "labels",
            b"labels",
            "location_id",
            b"location_id",
            "metadata",
            b"metadata",
            "name",
            b"name",
        ],
    ) -> None: ...

global___Location = Location