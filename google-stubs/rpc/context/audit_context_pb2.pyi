"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2022 Google LLC

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
import google.protobuf.struct_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class AuditContext(google.protobuf.message.Message):
    """`AuditContext` provides information that is needed for audit logging."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AUDIT_LOG_FIELD_NUMBER: builtins.int
    SCRUBBED_REQUEST_FIELD_NUMBER: builtins.int
    SCRUBBED_RESPONSE_FIELD_NUMBER: builtins.int
    SCRUBBED_RESPONSE_ITEM_COUNT_FIELD_NUMBER: builtins.int
    TARGET_RESOURCE_FIELD_NUMBER: builtins.int
    audit_log: builtins.bytes
    """Serialized audit log."""
    @property
    def scrubbed_request(self) -> google.protobuf.struct_pb2.Struct:
        """An API request message that is scrubbed based on the method annotation.
        This field should only be filled if audit_log field is present.
        Service Control will use this to assemble a complete log for Cloud Audit
        Logs and Google internal audit logs.
        """

    @property
    def scrubbed_response(self) -> google.protobuf.struct_pb2.Struct:
        """An API response message that is scrubbed based on the method annotation.
        This field should only be filled if audit_log field is present.
        Service Control will use this to assemble a complete log for Cloud Audit
        Logs and Google internal audit logs.
        """
    scrubbed_response_item_count: builtins.int
    """Number of scrubbed response items."""
    target_resource: builtins.str
    """Audit resource name which is scrubbed."""
    def __init__(
        self,
        *,
        audit_log: builtins.bytes = ...,
        scrubbed_request: google.protobuf.struct_pb2.Struct | None = ...,
        scrubbed_response: google.protobuf.struct_pb2.Struct | None = ...,
        scrubbed_response_item_count: builtins.int = ...,
        target_resource: builtins.str = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "scrubbed_request",
            b"scrubbed_request",
            "scrubbed_response",
            b"scrubbed_response",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "audit_log",
            b"audit_log",
            "scrubbed_request",
            b"scrubbed_request",
            "scrubbed_response",
            b"scrubbed_response",
            "scrubbed_response_item_count",
            b"scrubbed_response_item_count",
            "target_resource",
            b"target_resource",
        ],
    ) -> None: ...

global___AuditContext = AuditContext
