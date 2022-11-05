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
import collections.abc
import google.api.label_pb2
import google.api.launch_stage_pb2
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class MetricDescriptor(google.protobuf.message.Message):
    """Defines a metric type and its schema. Once a metric descriptor is created,
    deleting or altering it stops data collection and makes the metric type's
    existing data unusable.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _MetricKind:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _MetricKindEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            MetricDescriptor._MetricKind.ValueType
        ],
        builtins.type,
    ):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        METRIC_KIND_UNSPECIFIED: MetricDescriptor._MetricKind.ValueType  # 0
        """Do not use this default value."""
        GAUGE: MetricDescriptor._MetricKind.ValueType  # 1
        """An instantaneous measurement of a value."""
        DELTA: MetricDescriptor._MetricKind.ValueType  # 2
        """The change in a value during a time interval."""
        CUMULATIVE: MetricDescriptor._MetricKind.ValueType  # 3
        """A value accumulated over a time interval.  Cumulative
        measurements in a time series should have the same start time
        and increasing end times, until an event resets the cumulative
        value to zero and sets a new start time for the following
        points.
        """

    class MetricKind(_MetricKind, metaclass=_MetricKindEnumTypeWrapper):
        """The kind of measurement. It describes how the data is reported.
        For information on setting the start time and end time based on
        the MetricKind, see [TimeInterval][google.monitoring.v3.TimeInterval].
        """

    METRIC_KIND_UNSPECIFIED: MetricDescriptor.MetricKind.ValueType  # 0
    """Do not use this default value."""
    GAUGE: MetricDescriptor.MetricKind.ValueType  # 1
    """An instantaneous measurement of a value."""
    DELTA: MetricDescriptor.MetricKind.ValueType  # 2
    """The change in a value during a time interval."""
    CUMULATIVE: MetricDescriptor.MetricKind.ValueType  # 3
    """A value accumulated over a time interval.  Cumulative
    measurements in a time series should have the same start time
    and increasing end times, until an event resets the cumulative
    value to zero and sets a new start time for the following
    points.
    """

    class _ValueType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ValueTypeEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            MetricDescriptor._ValueType.ValueType
        ],
        builtins.type,
    ):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        VALUE_TYPE_UNSPECIFIED: MetricDescriptor._ValueType.ValueType  # 0
        """Do not use this default value."""
        BOOL: MetricDescriptor._ValueType.ValueType  # 1
        """The value is a boolean.
        This value type can be used only if the metric kind is `GAUGE`.
        """
        INT64: MetricDescriptor._ValueType.ValueType  # 2
        """The value is a signed 64-bit integer."""
        DOUBLE: MetricDescriptor._ValueType.ValueType  # 3
        """The value is a double precision floating point number."""
        STRING: MetricDescriptor._ValueType.ValueType  # 4
        """The value is a text string.
        This value type can be used only if the metric kind is `GAUGE`.
        """
        DISTRIBUTION: MetricDescriptor._ValueType.ValueType  # 5
        """The value is a [`Distribution`][google.api.Distribution]."""
        MONEY: MetricDescriptor._ValueType.ValueType  # 6
        """The value is money."""

    class ValueType(_ValueType, metaclass=_ValueTypeEnumTypeWrapper):
        """The value type of a metric."""

    VALUE_TYPE_UNSPECIFIED: MetricDescriptor.ValueType.ValueType  # 0
    """Do not use this default value."""
    BOOL: MetricDescriptor.ValueType.ValueType  # 1
    """The value is a boolean.
    This value type can be used only if the metric kind is `GAUGE`.
    """
    INT64: MetricDescriptor.ValueType.ValueType  # 2
    """The value is a signed 64-bit integer."""
    DOUBLE: MetricDescriptor.ValueType.ValueType  # 3
    """The value is a double precision floating point number."""
    STRING: MetricDescriptor.ValueType.ValueType  # 4
    """The value is a text string.
    This value type can be used only if the metric kind is `GAUGE`.
    """
    DISTRIBUTION: MetricDescriptor.ValueType.ValueType  # 5
    """The value is a [`Distribution`][google.api.Distribution]."""
    MONEY: MetricDescriptor.ValueType.ValueType  # 6
    """The value is money."""
    @typing_extensions.final
    class MetricDescriptorMetadata(google.protobuf.message.Message):
        """Additional annotations that can be used to guide the usage of a metric."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        LAUNCH_STAGE_FIELD_NUMBER: builtins.int
        SAMPLE_PERIOD_FIELD_NUMBER: builtins.int
        INGEST_DELAY_FIELD_NUMBER: builtins.int
        launch_stage: google.api.launch_stage_pb2.LaunchStage.ValueType
        """Deprecated. Must use the [MetricDescriptor.launch_stage][google.api.MetricDescriptor.launch_stage] instead."""
        @property
        def sample_period(self) -> google.protobuf.duration_pb2.Duration:
            """The sampling period of metric data points. For metrics which are written
            periodically, consecutive data points are stored at this time interval,
            excluding data loss due to errors. Metrics with a higher granularity have
            a smaller sampling period.
            """
        @property
        def ingest_delay(self) -> google.protobuf.duration_pb2.Duration:
            """The delay of data points caused by ingestion. Data points older than this
            age are guaranteed to be ingested and available to be read, excluding
            data loss due to errors.
            """
        def __init__(
            self,
            *,
            launch_stage: google.api.launch_stage_pb2.LaunchStage.ValueType = ...,
            sample_period: google.protobuf.duration_pb2.Duration | None = ...,
            ingest_delay: google.protobuf.duration_pb2.Duration | None = ...,
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions.Literal[
                "ingest_delay", b"ingest_delay", "sample_period", b"sample_period"
            ],
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "ingest_delay",
                b"ingest_delay",
                "launch_stage",
                b"launch_stage",
                "sample_period",
                b"sample_period",
            ],
        ) -> None: ...
    NAME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    METRIC_KIND_FIELD_NUMBER: builtins.int
    VALUE_TYPE_FIELD_NUMBER: builtins.int
    UNIT_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    LAUNCH_STAGE_FIELD_NUMBER: builtins.int
    MONITORED_RESOURCE_TYPES_FIELD_NUMBER: builtins.int
    name: builtins.str
    """The resource name of the metric descriptor."""
    type: builtins.str
    """The metric type, including its DNS name prefix. The type is not
    URL-encoded. All user-defined metric types have the DNS name
    `custom.googleapis.com` or `external.googleapis.com`. Metric types should
    use a natural hierarchical grouping. For example:

        "custom.googleapis.com/invoice/paid/amount"
        "external.googleapis.com/prometheus/up"
        "appengine.googleapis.com/http/server/response_latencies"
    """
    @property
    def labels(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        google.api.label_pb2.LabelDescriptor
    ]:
        """The set of labels that can be used to describe a specific
        instance of this metric type. For example, the
        `appengine.googleapis.com/http/server/response_latencies` metric
        type has a label for the HTTP response code, `response_code`, so
        you can look at latencies for successful responses or just
        for responses that failed.
        """
    metric_kind: global___MetricDescriptor.MetricKind.ValueType
    """Whether the metric records instantaneous values, changes to a value, etc.
    Some combinations of `metric_kind` and `value_type` might not be supported.
    """
    value_type: global___MetricDescriptor.ValueType.ValueType
    """Whether the measurement is an integer, a floating-point number, etc.
    Some combinations of `metric_kind` and `value_type` might not be supported.
    """
    unit: builtins.str
    """The units in which the metric value is reported. It is only applicable
    if the `value_type` is `INT64`, `DOUBLE`, or `DISTRIBUTION`. The `unit`
    defines the representation of the stored metric values.

    Different systems might scale the values to be more easily displayed (so a
    value of `0.02kBy` _might_ be displayed as `20By`, and a value of
    `3523kBy` _might_ be displayed as `3.5MBy`). However, if the `unit` is
    `kBy`, then the value of the metric is always in thousands of bytes, no
    matter how it might be displayed.

    If you want a custom metric to record the exact number of CPU-seconds used
    by a job, you can create an `INT64 CUMULATIVE` metric whose `unit` is
    `s{CPU}` (or equivalently `1s{CPU}` or just `s`). If the job uses 12,005
    CPU-seconds, then the value is written as `12005`.

    Alternatively, if you want a custom metric to record data in a more
    granular way, you can create a `DOUBLE CUMULATIVE` metric whose `unit` is
    `ks{CPU}`, and then write the value `12.005` (which is `12005/1000`),
    or use `Kis{CPU}` and write `11.723` (which is `12005/1024`).

    The supported units are a subset of [The Unified Code for Units of
    Measure](https://unitsofmeasure.org/ucum.html) standard:

    **Basic units (UNIT)**

    * `bit`   bit
    * `By`    byte
    * `s`     second
    * `min`   minute
    * `h`     hour
    * `d`     day
    * `1`     dimensionless

    **Prefixes (PREFIX)**

    * `k`     kilo    (10^3)
    * `M`     mega    (10^6)
    * `G`     giga    (10^9)
    * `T`     tera    (10^12)
    * `P`     peta    (10^15)
    * `E`     exa     (10^18)
    * `Z`     zetta   (10^21)
    * `Y`     yotta   (10^24)

    * `m`     milli   (10^-3)
    * `u`     micro   (10^-6)
    * `n`     nano    (10^-9)
    * `p`     pico    (10^-12)
    * `f`     femto   (10^-15)
    * `a`     atto    (10^-18)
    * `z`     zepto   (10^-21)
    * `y`     yocto   (10^-24)

    * `Ki`    kibi    (2^10)
    * `Mi`    mebi    (2^20)
    * `Gi`    gibi    (2^30)
    * `Ti`    tebi    (2^40)
    * `Pi`    pebi    (2^50)

    **Grammar**

    The grammar also includes these connectors:

    * `/`    division or ratio (as an infix operator). For examples,
             `kBy/{email}` or `MiBy/10ms` (although you should almost never
             have `/s` in a metric `unit`; rates should always be computed at
             query time from the underlying cumulative or delta value).
    * `.`    multiplication or composition (as an infix operator). For
             examples, `GBy.d` or `k{watt}.h`.

    The grammar for a unit is as follows:

        Expression = Component { "." Component } { "/" Component } ;

        Component = ( [ PREFIX ] UNIT | "%" ) [ Annotation ]
                  | Annotation
                  | "1"
                  ;

        Annotation = "{" NAME "}" ;

    Notes:

    * `Annotation` is just a comment if it follows a `UNIT`. If the annotation
       is used alone, then the unit is equivalent to `1`. For examples,
       `{request}/s == 1/s`, `By{transmitted}/s == By/s`.
    * `NAME` is a sequence of non-blank printable ASCII characters not
       containing `{` or `}`.
    * `1` represents a unitary [dimensionless
       unit](https://en.wikipedia.org/wiki/Dimensionless_quantity) of 1, such
       as in `1/s`. It is typically used when none of the basic units are
       appropriate. For example, "new users per day" can be represented as
       `1/d` or `{new-users}/d` (and a metric value `5` would mean "5 new
       users). Alternatively, "thousands of page views per day" would be
       represented as `1000/d` or `k1/d` or `k{page_views}/d` (and a metric
       value of `5.3` would mean "5300 page views per day").
    * `%` represents dimensionless value of 1/100, and annotates values giving
       a percentage (so the metric values are typically in the range of 0..100,
       and a metric value `3` means "3 percent").
    * `10^2.%` indicates a metric contains a ratio, typically in the range
       0..1, that will be multiplied by 100 and displayed as a percentage
       (so a metric value `0.03` means "3 percent").
    """
    description: builtins.str
    """A detailed description of the metric, which can be used in documentation."""
    display_name: builtins.str
    """A concise name for the metric, which can be displayed in user interfaces.
    Use sentence case without an ending period, for example "Request count".
    This field is optional but it is recommended to be set for any metrics
    associated with user-visible concepts, such as Quota.
    """
    @property
    def metadata(self) -> global___MetricDescriptor.MetricDescriptorMetadata:
        """Optional. Metadata which can be used to guide usage of the metric."""
    launch_stage: google.api.launch_stage_pb2.LaunchStage.ValueType
    """Optional. The launch stage of the metric definition."""
    @property
    def monitored_resource_types(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Read-only. If present, then a [time
        series][google.monitoring.v3.TimeSeries], which is identified partially by
        a metric type and a [MonitoredResourceDescriptor][google.api.MonitoredResourceDescriptor], that is associated
        with this metric type can only be associated with one of the monitored
        resource types listed here.
        """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        type: builtins.str = ...,
        labels: collections.abc.Iterable[google.api.label_pb2.LabelDescriptor]
        | None = ...,
        metric_kind: global___MetricDescriptor.MetricKind.ValueType = ...,
        value_type: global___MetricDescriptor.ValueType.ValueType = ...,
        unit: builtins.str = ...,
        description: builtins.str = ...,
        display_name: builtins.str = ...,
        metadata: global___MetricDescriptor.MetricDescriptorMetadata | None = ...,
        launch_stage: google.api.launch_stage_pb2.LaunchStage.ValueType = ...,
        monitored_resource_types: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["metadata", b"metadata"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "description",
            b"description",
            "display_name",
            b"display_name",
            "labels",
            b"labels",
            "launch_stage",
            b"launch_stage",
            "metadata",
            b"metadata",
            "metric_kind",
            b"metric_kind",
            "monitored_resource_types",
            b"monitored_resource_types",
            "name",
            b"name",
            "type",
            b"type",
            "unit",
            b"unit",
            "value_type",
            b"value_type",
        ],
    ) -> None: ...

global___MetricDescriptor = MetricDescriptor

@typing_extensions.final
class Metric(google.protobuf.message.Message):
    """A specific metric, identified by specifying values for all of the
    labels of a [`MetricDescriptor`][google.api.MetricDescriptor].
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    @typing_extensions.final
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...
    TYPE_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    type: builtins.str
    """An existing metric type, see [google.api.MetricDescriptor][google.api.MetricDescriptor].
    For example, `custom.googleapis.com/invoice/paid/amount`.
    """
    @property
    def labels(
        self,
    ) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """The set of label values that uniquely identify this metric. All
        labels listed in the `MetricDescriptor` must be assigned values.
        """
    def __init__(
        self,
        *,
        type: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["labels", b"labels", "type", b"type"],
    ) -> None: ...

global___Metric = Metric
