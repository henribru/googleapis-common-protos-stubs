"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class LatLng(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    LATITUDE_FIELD_NUMBER: builtins.int
    LONGITUDE_FIELD_NUMBER: builtins.int
    latitude: builtins.float = ...
    longitude: builtins.float = ...
    def __init__(
        self,
        *,
        latitude: builtins.float = ...,
        longitude: builtins.float = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "latitude", b"latitude", "longitude", b"longitude"
        ],
    ) -> None: ...

global___LatLng = LatLng
