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

class Authentication(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RULES_FIELD_NUMBER: builtins.int
    PROVIDERS_FIELD_NUMBER: builtins.int
    @property
    def rules(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___AuthenticationRule
    ]: ...
    @property
    def providers(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___AuthProvider
    ]: ...
    def __init__(
        self,
        *,
        rules: typing.Optional[typing.Iterable[global___AuthenticationRule]] = ...,
        providers: typing.Optional[typing.Iterable[global___AuthProvider]] = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "providers", b"providers", "rules", b"rules"
        ],
    ) -> None: ...

global___Authentication = Authentication

class AuthenticationRule(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SELECTOR_FIELD_NUMBER: builtins.int
    OAUTH_FIELD_NUMBER: builtins.int
    ALLOW_WITHOUT_CREDENTIAL_FIELD_NUMBER: builtins.int
    REQUIREMENTS_FIELD_NUMBER: builtins.int
    selector: typing.Text = ...
    allow_without_credential: builtins.bool = ...
    @property
    def oauth(self) -> global___OAuthRequirements: ...
    @property
    def requirements(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___AuthRequirement
    ]: ...
    def __init__(
        self,
        *,
        selector: typing.Text = ...,
        oauth: typing.Optional[global___OAuthRequirements] = ...,
        allow_without_credential: builtins.bool = ...,
        requirements: typing.Optional[typing.Iterable[global___AuthRequirement]] = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["oauth", b"oauth"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "allow_without_credential",
            b"allow_without_credential",
            "oauth",
            b"oauth",
            "requirements",
            b"requirements",
            "selector",
            b"selector",
        ],
    ) -> None: ...

global___AuthenticationRule = AuthenticationRule

class AuthProvider(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    ISSUER_FIELD_NUMBER: builtins.int
    JWKS_URI_FIELD_NUMBER: builtins.int
    AUDIENCES_FIELD_NUMBER: builtins.int
    AUTHORIZATION_URL_FIELD_NUMBER: builtins.int
    id: typing.Text = ...
    issuer: typing.Text = ...
    jwks_uri: typing.Text = ...
    audiences: typing.Text = ...
    authorization_url: typing.Text = ...
    def __init__(
        self,
        *,
        id: typing.Text = ...,
        issuer: typing.Text = ...,
        jwks_uri: typing.Text = ...,
        audiences: typing.Text = ...,
        authorization_url: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "audiences",
            b"audiences",
            "authorization_url",
            b"authorization_url",
            "id",
            b"id",
            "issuer",
            b"issuer",
            "jwks_uri",
            b"jwks_uri",
        ],
    ) -> None: ...

global___AuthProvider = AuthProvider

class OAuthRequirements(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CANONICAL_SCOPES_FIELD_NUMBER: builtins.int
    canonical_scopes: typing.Text = ...
    def __init__(
        self,
        *,
        canonical_scopes: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["canonical_scopes", b"canonical_scopes"],
    ) -> None: ...

global___OAuthRequirements = OAuthRequirements

class AuthRequirement(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PROVIDER_ID_FIELD_NUMBER: builtins.int
    AUDIENCES_FIELD_NUMBER: builtins.int
    provider_id: typing.Text = ...
    audiences: typing.Text = ...
    def __init__(
        self,
        *,
        provider_id: typing.Text = ...,
        audiences: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "audiences", b"audiences", "provider_id", b"provider_id"
        ],
    ) -> None: ...

global___AuthRequirement = AuthRequirement
