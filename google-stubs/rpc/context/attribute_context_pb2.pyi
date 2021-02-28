"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class AttributeContext(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Peer(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class LabelsEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text = ...
            value: typing.Text = ...
            def __init__(
                self,
                *,
                key: typing.Text = ...,
                value: typing.Text = ...,
            ) -> None: ...
            def ClearField(
                self,
                field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
            ) -> None: ...
        IP_FIELD_NUMBER: builtins.int
        PORT_FIELD_NUMBER: builtins.int
        LABELS_FIELD_NUMBER: builtins.int
        PRINCIPAL_FIELD_NUMBER: builtins.int
        REGION_CODE_FIELD_NUMBER: builtins.int
        ip: typing.Text = ...
        port: builtins.int = ...
        principal: typing.Text = ...
        region_code: typing.Text = ...
        @property
        def labels(
            self,
        ) -> google.protobuf.internal.containers.ScalarMap[
            typing.Text, typing.Text
        ]: ...
        def __init__(
            self,
            *,
            ip: typing.Text = ...,
            port: builtins.int = ...,
            labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
            principal: typing.Text = ...,
            region_code: typing.Text = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "ip",
                b"ip",
                "labels",
                b"labels",
                "port",
                b"port",
                "principal",
                b"principal",
                "region_code",
                b"region_code",
            ],
        ) -> None: ...
    class Api(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        SERVICE_FIELD_NUMBER: builtins.int
        OPERATION_FIELD_NUMBER: builtins.int
        PROTOCOL_FIELD_NUMBER: builtins.int
        VERSION_FIELD_NUMBER: builtins.int
        service: typing.Text = ...
        operation: typing.Text = ...
        protocol: typing.Text = ...
        version: typing.Text = ...
        def __init__(
            self,
            *,
            service: typing.Text = ...,
            operation: typing.Text = ...,
            protocol: typing.Text = ...,
            version: typing.Text = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "operation",
                b"operation",
                "protocol",
                b"protocol",
                "service",
                b"service",
                "version",
                b"version",
            ],
        ) -> None: ...
    class Auth(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        PRINCIPAL_FIELD_NUMBER: builtins.int
        AUDIENCES_FIELD_NUMBER: builtins.int
        PRESENTER_FIELD_NUMBER: builtins.int
        CLAIMS_FIELD_NUMBER: builtins.int
        ACCESS_LEVELS_FIELD_NUMBER: builtins.int
        principal: typing.Text = ...
        audiences: google.protobuf.internal.containers.RepeatedScalarFieldContainer[
            typing.Text
        ] = ...
        presenter: typing.Text = ...
        access_levels: google.protobuf.internal.containers.RepeatedScalarFieldContainer[
            typing.Text
        ] = ...
        @property
        def claims(self) -> google.protobuf.struct_pb2.Struct: ...
        def __init__(
            self,
            *,
            principal: typing.Text = ...,
            audiences: typing.Optional[typing.Iterable[typing.Text]] = ...,
            presenter: typing.Text = ...,
            claims: typing.Optional[google.protobuf.struct_pb2.Struct] = ...,
            access_levels: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["claims", b"claims"]
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "access_levels",
                b"access_levels",
                "audiences",
                b"audiences",
                "claims",
                b"claims",
                "presenter",
                b"presenter",
                "principal",
                b"principal",
            ],
        ) -> None: ...
    class Request(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class HeadersEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text = ...
            value: typing.Text = ...
            def __init__(
                self,
                *,
                key: typing.Text = ...,
                value: typing.Text = ...,
            ) -> None: ...
            def ClearField(
                self,
                field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
            ) -> None: ...
        ID_FIELD_NUMBER: builtins.int
        METHOD_FIELD_NUMBER: builtins.int
        HEADERS_FIELD_NUMBER: builtins.int
        PATH_FIELD_NUMBER: builtins.int
        HOST_FIELD_NUMBER: builtins.int
        SCHEME_FIELD_NUMBER: builtins.int
        QUERY_FIELD_NUMBER: builtins.int
        TIME_FIELD_NUMBER: builtins.int
        SIZE_FIELD_NUMBER: builtins.int
        PROTOCOL_FIELD_NUMBER: builtins.int
        REASON_FIELD_NUMBER: builtins.int
        AUTH_FIELD_NUMBER: builtins.int
        id: typing.Text = ...
        method: typing.Text = ...
        path: typing.Text = ...
        host: typing.Text = ...
        scheme: typing.Text = ...
        query: typing.Text = ...
        size: builtins.int = ...
        protocol: typing.Text = ...
        reason: typing.Text = ...
        @property
        def headers(
            self,
        ) -> google.protobuf.internal.containers.ScalarMap[
            typing.Text, typing.Text
        ]: ...
        @property
        def time(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
        @property
        def auth(self) -> global___AttributeContext.Auth: ...
        def __init__(
            self,
            *,
            id: typing.Text = ...,
            method: typing.Text = ...,
            headers: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
            path: typing.Text = ...,
            host: typing.Text = ...,
            scheme: typing.Text = ...,
            query: typing.Text = ...,
            time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
            size: builtins.int = ...,
            protocol: typing.Text = ...,
            reason: typing.Text = ...,
            auth: typing.Optional[global___AttributeContext.Auth] = ...,
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions.Literal["auth", b"auth", "time", b"time"],
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "auth",
                b"auth",
                "headers",
                b"headers",
                "host",
                b"host",
                "id",
                b"id",
                "method",
                b"method",
                "path",
                b"path",
                "protocol",
                b"protocol",
                "query",
                b"query",
                "reason",
                b"reason",
                "scheme",
                b"scheme",
                "size",
                b"size",
                "time",
                b"time",
            ],
        ) -> None: ...
    class Response(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class HeadersEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text = ...
            value: typing.Text = ...
            def __init__(
                self,
                *,
                key: typing.Text = ...,
                value: typing.Text = ...,
            ) -> None: ...
            def ClearField(
                self,
                field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
            ) -> None: ...
        CODE_FIELD_NUMBER: builtins.int
        SIZE_FIELD_NUMBER: builtins.int
        HEADERS_FIELD_NUMBER: builtins.int
        TIME_FIELD_NUMBER: builtins.int
        code: builtins.int = ...
        size: builtins.int = ...
        @property
        def headers(
            self,
        ) -> google.protobuf.internal.containers.ScalarMap[
            typing.Text, typing.Text
        ]: ...
        @property
        def time(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
        def __init__(
            self,
            *,
            code: builtins.int = ...,
            size: builtins.int = ...,
            headers: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
            time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["time", b"time"]
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "code", b"code", "headers", b"headers", "size", b"size", "time", b"time"
            ],
        ) -> None: ...
    class Resource(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class LabelsEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text = ...
            value: typing.Text = ...
            def __init__(
                self,
                *,
                key: typing.Text = ...,
                value: typing.Text = ...,
            ) -> None: ...
            def ClearField(
                self,
                field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
            ) -> None: ...
        SERVICE_FIELD_NUMBER: builtins.int
        NAME_FIELD_NUMBER: builtins.int
        TYPE_FIELD_NUMBER: builtins.int
        LABELS_FIELD_NUMBER: builtins.int
        service: typing.Text = ...
        name: typing.Text = ...
        type: typing.Text = ...
        @property
        def labels(
            self,
        ) -> google.protobuf.internal.containers.ScalarMap[
            typing.Text, typing.Text
        ]: ...
        def __init__(
            self,
            *,
            service: typing.Text = ...,
            name: typing.Text = ...,
            type: typing.Text = ...,
            labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "labels",
                b"labels",
                "name",
                b"name",
                "service",
                b"service",
                "type",
                b"type",
            ],
        ) -> None: ...
    ORIGIN_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    DESTINATION_FIELD_NUMBER: builtins.int
    REQUEST_FIELD_NUMBER: builtins.int
    RESPONSE_FIELD_NUMBER: builtins.int
    RESOURCE_FIELD_NUMBER: builtins.int
    API_FIELD_NUMBER: builtins.int
    @property
    def origin(self) -> global___AttributeContext.Peer: ...
    @property
    def source(self) -> global___AttributeContext.Peer: ...
    @property
    def destination(self) -> global___AttributeContext.Peer: ...
    @property
    def request(self) -> global___AttributeContext.Request: ...
    @property
    def response(self) -> global___AttributeContext.Response: ...
    @property
    def resource(self) -> global___AttributeContext.Resource: ...
    @property
    def api(self) -> global___AttributeContext.Api: ...
    def __init__(
        self,
        *,
        origin: typing.Optional[global___AttributeContext.Peer] = ...,
        source: typing.Optional[global___AttributeContext.Peer] = ...,
        destination: typing.Optional[global___AttributeContext.Peer] = ...,
        request: typing.Optional[global___AttributeContext.Request] = ...,
        response: typing.Optional[global___AttributeContext.Response] = ...,
        resource: typing.Optional[global___AttributeContext.Resource] = ...,
        api: typing.Optional[global___AttributeContext.Api] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "api",
            b"api",
            "destination",
            b"destination",
            "origin",
            b"origin",
            "request",
            b"request",
            "resource",
            b"resource",
            "response",
            b"response",
            "source",
            b"source",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "api",
            b"api",
            "destination",
            b"destination",
            "origin",
            b"origin",
            "request",
            b"request",
            "resource",
            b"resource",
            "response",
            b"response",
            "source",
            b"source",
        ],
    ) -> None: ...

global___AttributeContext = AttributeContext
