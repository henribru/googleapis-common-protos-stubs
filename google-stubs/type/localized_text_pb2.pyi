"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright 2021 Google LLC

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
class LocalizedText(google.protobuf.message.Message):
    """Localized variant of a text in a particular language."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEXT_FIELD_NUMBER: builtins.int
    LANGUAGE_CODE_FIELD_NUMBER: builtins.int
    text: builtins.str
    """Localized string in the language corresponding to `language_code' below."""
    language_code: builtins.str
    """The text's BCP-47 language code, such as "en-US" or "sr-Latn".

    For more information, see
    http://www.unicode.org/reports/tr35/#Unicode_locale_identifier.
    """
    def __init__(
        self,
        *,
        text: builtins.str = ...,
        language_code: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "language_code", b"language_code", "text", b"text"
        ],
    ) -> None: ...

global___LocalizedText = LocalizedText