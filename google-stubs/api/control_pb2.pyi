"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2015 Google LLC

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
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Control(google.protobuf.message.Message):
    """Selects and configures the service controller used by the service.  The
    service controller handles features like abuse, quota, billing, logging,
    monitoring, etc.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENVIRONMENT_FIELD_NUMBER: builtins.int
    environment: builtins.str
    """The service control environment to use. If empty, no control plane
    feature (like quota and billing) will be enabled.
    """
    def __init__(
        self,
        *,
        environment: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["environment", b"environment"]
    ) -> None: ...

global___Control = Control
