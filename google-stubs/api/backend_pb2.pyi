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

# `Backend` defines the backend configuration for a service.
class Backend(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RULES_FIELD_NUMBER: builtins.int
    # A list of API backend rules that apply to individual API methods.
    #
    # **NOTE:** All service configuration rules follow "last one wins" order.
    @property
    def rules(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___BackendRule
    ]: ...
    def __init__(
        self,
        *,
        rules: typing.Optional[typing.Iterable[global___BackendRule]] = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["rules", b"rules"]
    ) -> None: ...

global___Backend = Backend

# A backend rule provides configuration for an individual API element.
class BackendRule(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SELECTOR_FIELD_NUMBER: builtins.int
    ADDRESS_FIELD_NUMBER: builtins.int
    DEADLINE_FIELD_NUMBER: builtins.int
    MIN_DEADLINE_FIELD_NUMBER: builtins.int
    # Selects the methods to which this rule applies.
    #
    # Refer to [selector][google.api.DocumentationRule.selector] for syntax details.
    selector: typing.Text = ...
    # The address of the API backend.
    address: typing.Text = ...
    # The number of seconds to wait for a response from a request.  The default
    # deadline for gRPC is infinite (no deadline) and HTTP requests is 5 seconds.
    deadline: builtins.float = ...
    # Minimum deadline in seconds needed for this method. Calls having deadline
    # value lower than this will be rejected.
    min_deadline: builtins.float = ...
    def __init__(
        self,
        *,
        selector: typing.Text = ...,
        address: typing.Text = ...,
        deadline: builtins.float = ...,
        min_deadline: builtins.float = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "address",
            b"address",
            "deadline",
            b"deadline",
            "min_deadline",
            b"min_deadline",
            "selector",
            b"selector",
        ],
    ) -> None: ...

global___BackendRule = BackendRule
