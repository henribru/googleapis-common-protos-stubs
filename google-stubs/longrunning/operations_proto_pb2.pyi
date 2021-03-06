"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.rpc.status_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Operation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    DONE_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    RESPONSE_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    done: builtins.bool = ...
    @property
    def metadata(self) -> google.protobuf.any_pb2.Any: ...
    @property
    def error(self) -> google.rpc.status_pb2.Status: ...
    @property
    def response(self) -> google.protobuf.any_pb2.Any: ...
    def __init__(
        self,
        *,
        name: typing.Text = ...,
        metadata: typing.Optional[google.protobuf.any_pb2.Any] = ...,
        done: builtins.bool = ...,
        error: typing.Optional[google.rpc.status_pb2.Status] = ...,
        response: typing.Optional[google.protobuf.any_pb2.Any] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "error",
            b"error",
            "metadata",
            b"metadata",
            "response",
            b"response",
            "result",
            b"result",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "done",
            b"done",
            "error",
            b"error",
            "metadata",
            b"metadata",
            "name",
            b"name",
            "response",
            b"response",
            "result",
            b"result",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["result", b"result"]
    ) -> typing_extensions.Literal["error", "response"]: ...

global___Operation = Operation

class GetOperationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    def __init__(
        self,
        *,
        name: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["name", b"name"]
    ) -> None: ...

global___GetOperationRequest = GetOperationRequest

class ListOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    filter: typing.Text = ...
    page_size: builtins.int = ...
    page_token: typing.Text = ...
    def __init__(
        self,
        *,
        name: typing.Text = ...,
        filter: typing.Text = ...,
        page_size: builtins.int = ...,
        page_token: typing.Text = ...,
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

global___ListOperationsRequest = ListOperationsRequest

class ListOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: typing.Text = ...
    @property
    def operations(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___Operation
    ]: ...
    def __init__(
        self,
        *,
        operations: typing.Optional[typing.Iterable[global___Operation]] = ...,
        next_page_token: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "next_page_token", b"next_page_token", "operations", b"operations"
        ],
    ) -> None: ...

global___ListOperationsResponse = ListOperationsResponse

class CancelOperationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    def __init__(
        self,
        *,
        name: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["name", b"name"]
    ) -> None: ...

global___CancelOperationRequest = CancelOperationRequest

class DeleteOperationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    def __init__(
        self,
        *,
        name: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["name", b"name"]
    ) -> None: ...

global___DeleteOperationRequest = DeleteOperationRequest

class WaitOperationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    TIMEOUT_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    @property
    def timeout(self) -> google.protobuf.duration_pb2.Duration: ...
    def __init__(
        self,
        *,
        name: typing.Text = ...,
        timeout: typing.Optional[google.protobuf.duration_pb2.Duration] = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["timeout", b"timeout"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["name", b"name", "timeout", b"timeout"],
    ) -> None: ...

global___WaitOperationRequest = WaitOperationRequest

class OperationInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESPONSE_TYPE_FIELD_NUMBER: builtins.int
    METADATA_TYPE_FIELD_NUMBER: builtins.int
    response_type: typing.Text = ...
    metadata_type: typing.Text = ...
    def __init__(
        self,
        *,
        response_type: typing.Text = ...,
        metadata_type: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "metadata_type", b"metadata_type", "response_type", b"response_type"
        ],
    ) -> None: ...

global___OperationInfo = OperationInfo

operation_info: google.protobuf.descriptor.FieldDescriptor = ...
