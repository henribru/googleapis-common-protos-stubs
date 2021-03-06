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

class Logging(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class LoggingDestination(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        MONITORED_RESOURCE_FIELD_NUMBER: builtins.int
        LOGS_FIELD_NUMBER: builtins.int
        monitored_resource: typing.Text = ...
        logs: google.protobuf.internal.containers.RepeatedScalarFieldContainer[
            typing.Text
        ] = ...
        def __init__(
            self,
            *,
            monitored_resource: typing.Text = ...,
            logs: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "logs", b"logs", "monitored_resource", b"monitored_resource"
            ],
        ) -> None: ...
    PRODUCER_DESTINATIONS_FIELD_NUMBER: builtins.int
    CONSUMER_DESTINATIONS_FIELD_NUMBER: builtins.int
    @property
    def producer_destinations(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___Logging.LoggingDestination
    ]: ...
    @property
    def consumer_destinations(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___Logging.LoggingDestination
    ]: ...
    def __init__(
        self,
        *,
        producer_destinations: typing.Optional[
            typing.Iterable[global___Logging.LoggingDestination]
        ] = ...,
        consumer_destinations: typing.Optional[
            typing.Iterable[global___Logging.LoggingDestination]
        ] = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "consumer_destinations",
            b"consumer_destinations",
            "producer_destinations",
            b"producer_destinations",
        ],
    ) -> None: ...

global___Logging = Logging
