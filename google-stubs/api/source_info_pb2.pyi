"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class SourceInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SOURCE_FILES_FIELD_NUMBER: builtins.int
    @property
    def source_files(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        google.protobuf.any_pb2.Any
    ]: ...
    def __init__(
        self,
        *,
        source_files: typing.Optional[
            typing.Iterable[google.protobuf.any_pb2.Any]
        ] = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["source_files", b"source_files"]
    ) -> None: ...

global___SourceInfo = SourceInfo
