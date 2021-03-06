"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GapicMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class ServicesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___GapicMetadata.ServiceForTransport: ...
        def __init__(
            self,
            *,
            key: typing.Text = ...,
            value: typing.Optional[global___GapicMetadata.ServiceForTransport] = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["value", b"value"]
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...
    class ServiceForTransport(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class ClientsEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text = ...
            @property
            def value(self) -> global___GapicMetadata.ServiceAsClient: ...
            def __init__(
                self,
                *,
                key: typing.Text = ...,
                value: typing.Optional[global___GapicMetadata.ServiceAsClient] = ...,
            ) -> None: ...
            def HasField(
                self, field_name: typing_extensions.Literal["value", b"value"]
            ) -> builtins.bool: ...
            def ClearField(
                self,
                field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
            ) -> None: ...
        CLIENTS_FIELD_NUMBER: builtins.int
        @property
        def clients(
            self,
        ) -> google.protobuf.internal.containers.MessageMap[
            typing.Text, global___GapicMetadata.ServiceAsClient
        ]: ...
        def __init__(
            self,
            *,
            clients: typing.Optional[
                typing.Mapping[typing.Text, global___GapicMetadata.ServiceAsClient]
            ] = ...,
        ) -> None: ...
        def ClearField(
            self, field_name: typing_extensions.Literal["clients", b"clients"]
        ) -> None: ...
    class ServiceAsClient(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class RpcsEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text = ...
            @property
            def value(self) -> global___GapicMetadata.MethodList: ...
            def __init__(
                self,
                *,
                key: typing.Text = ...,
                value: typing.Optional[global___GapicMetadata.MethodList] = ...,
            ) -> None: ...
            def HasField(
                self, field_name: typing_extensions.Literal["value", b"value"]
            ) -> builtins.bool: ...
            def ClearField(
                self,
                field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
            ) -> None: ...
        LIBRARY_CLIENT_FIELD_NUMBER: builtins.int
        RPCS_FIELD_NUMBER: builtins.int
        library_client: typing.Text = ...
        @property
        def rpcs(
            self,
        ) -> google.protobuf.internal.containers.MessageMap[
            typing.Text, global___GapicMetadata.MethodList
        ]: ...
        def __init__(
            self,
            *,
            library_client: typing.Text = ...,
            rpcs: typing.Optional[
                typing.Mapping[typing.Text, global___GapicMetadata.MethodList]
            ] = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "library_client", b"library_client", "rpcs", b"rpcs"
            ],
        ) -> None: ...
    class MethodList(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        METHODS_FIELD_NUMBER: builtins.int
        methods: google.protobuf.internal.containers.RepeatedScalarFieldContainer[
            typing.Text
        ] = ...
        def __init__(
            self,
            *,
            methods: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
        def ClearField(
            self, field_name: typing_extensions.Literal["methods", b"methods"]
        ) -> None: ...
    SCHEMA_FIELD_NUMBER: builtins.int
    COMMENT_FIELD_NUMBER: builtins.int
    LANGUAGE_FIELD_NUMBER: builtins.int
    PROTO_PACKAGE_FIELD_NUMBER: builtins.int
    LIBRARY_PACKAGE_FIELD_NUMBER: builtins.int
    SERVICES_FIELD_NUMBER: builtins.int
    schema: typing.Text = ...
    comment: typing.Text = ...
    language: typing.Text = ...
    proto_package: typing.Text = ...
    library_package: typing.Text = ...
    @property
    def services(
        self,
    ) -> google.protobuf.internal.containers.MessageMap[
        typing.Text, global___GapicMetadata.ServiceForTransport
    ]: ...
    def __init__(
        self,
        *,
        schema: typing.Text = ...,
        comment: typing.Text = ...,
        language: typing.Text = ...,
        proto_package: typing.Text = ...,
        library_package: typing.Text = ...,
        services: typing.Optional[
            typing.Mapping[typing.Text, global___GapicMetadata.ServiceForTransport]
        ] = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "comment",
            b"comment",
            "language",
            b"language",
            "library_package",
            b"library_package",
            "proto_package",
            b"proto_package",
            "schema",
            b"schema",
            "services",
            b"services",
        ],
    ) -> None: ...

global___GapicMetadata = GapicMetadata
