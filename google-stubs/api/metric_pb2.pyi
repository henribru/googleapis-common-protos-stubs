"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.api.label_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

# Defines a metric type and its schema. Once a metric descriptor is created,
# deleting or altering it stops data collection and makes the metric type's
# existing data unusable.
class MetricDescriptor(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    # The kind of measurement. It describes how the data is reported.
    class MetricKind(_MetricKind, metaclass=_MetricKindEnumTypeWrapper):
        pass
    class _MetricKind:
        V = typing.NewType("V", builtins.int)
    class _MetricKindEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_MetricKind.V],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        # Do not use this default value.
        METRIC_KIND_UNSPECIFIED = MetricDescriptor.MetricKind.V(0)
        # An instantaneous measurement of a value.
        GAUGE = MetricDescriptor.MetricKind.V(1)
        # The change in a value during a time interval.
        DELTA = MetricDescriptor.MetricKind.V(2)
        # A value accumulated over a time interval.  Cumulative
        # measurements in a time series should have the same start time
        # and increasing end times, until an event resets the cumulative
        # value to zero and sets a new start time for the following
        # points.
        CUMULATIVE = MetricDescriptor.MetricKind.V(3)
    # Do not use this default value.
    METRIC_KIND_UNSPECIFIED = MetricDescriptor.MetricKind.V(0)
    # An instantaneous measurement of a value.
    GAUGE = MetricDescriptor.MetricKind.V(1)
    # The change in a value during a time interval.
    DELTA = MetricDescriptor.MetricKind.V(2)
    # A value accumulated over a time interval.  Cumulative
    # measurements in a time series should have the same start time
    # and increasing end times, until an event resets the cumulative
    # value to zero and sets a new start time for the following
    # points.
    CUMULATIVE = MetricDescriptor.MetricKind.V(3)

    # The value type of a metric.
    class ValueType(_ValueType, metaclass=_ValueTypeEnumTypeWrapper):
        pass
    class _ValueType:
        V = typing.NewType("V", builtins.int)
    class _ValueTypeEnumTypeWrapper(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ValueType.V],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        # Do not use this default value.
        VALUE_TYPE_UNSPECIFIED = MetricDescriptor.ValueType.V(0)
        # The value is a boolean.
        # This value type can be used only if the metric kind is `GAUGE`.
        BOOL = MetricDescriptor.ValueType.V(1)
        # The value is a signed 64-bit integer.
        INT64 = MetricDescriptor.ValueType.V(2)
        # The value is a double precision floating point number.
        DOUBLE = MetricDescriptor.ValueType.V(3)
        # The value is a text string.
        # This value type can be used only if the metric kind is `GAUGE`.
        STRING = MetricDescriptor.ValueType.V(4)
        # The value is a [`Distribution`][google.api.Distribution].
        DISTRIBUTION = MetricDescriptor.ValueType.V(5)
        # The value is money.
        MONEY = MetricDescriptor.ValueType.V(6)
    # Do not use this default value.
    VALUE_TYPE_UNSPECIFIED = MetricDescriptor.ValueType.V(0)
    # The value is a boolean.
    # This value type can be used only if the metric kind is `GAUGE`.
    BOOL = MetricDescriptor.ValueType.V(1)
    # The value is a signed 64-bit integer.
    INT64 = MetricDescriptor.ValueType.V(2)
    # The value is a double precision floating point number.
    DOUBLE = MetricDescriptor.ValueType.V(3)
    # The value is a text string.
    # This value type can be used only if the metric kind is `GAUGE`.
    STRING = MetricDescriptor.ValueType.V(4)
    # The value is a [`Distribution`][google.api.Distribution].
    DISTRIBUTION = MetricDescriptor.ValueType.V(5)
    # The value is money.
    MONEY = MetricDescriptor.ValueType.V(6)

    NAME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    METRIC_KIND_FIELD_NUMBER: builtins.int
    VALUE_TYPE_FIELD_NUMBER: builtins.int
    UNIT_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    # The resource name of the metric descriptor.
    name: typing.Text = ...
    # The metric type, including its DNS name prefix. The type is not
    # URL-encoded.  All user-defined custom metric types have the DNS name
    # `custom.googleapis.com`.  Metric types should use a natural hierarchical
    # grouping. For example:
    #
    #     "custom.googleapis.com/invoice/paid/amount"
    #     "appengine.googleapis.com/http/server/response_latencies"
    type: typing.Text = ...
    # The set of labels that can be used to describe a specific
    # instance of this metric type. For example, the
    # `appengine.googleapis.com/http/server/response_latencies` metric
    # type has a label for the HTTP response code, `response_code`, so
    # you can look at latencies for successful responses or just
    # for responses that failed.
    @property
    def labels(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        google.api.label_pb2.LabelDescriptor
    ]: ...
    # Whether the metric records instantaneous values, changes to a value, etc.
    # Some combinations of `metric_kind` and `value_type` might not be supported.
    metric_kind: global___MetricDescriptor.MetricKind.V = ...
    # Whether the measurement is an integer, a floating-point number, etc.
    # Some combinations of `metric_kind` and `value_type` might not be supported.
    value_type: global___MetricDescriptor.ValueType.V = ...
    # The unit in which the metric value is reported. It is only applicable
    # if the `value_type` is `INT64`, `DOUBLE`, or `DISTRIBUTION`. The
    # supported units are a subset of [The Unified Code for Units of
    # Measure](http://unitsofmeasure.org/ucum.html) standard:
    #
    # **Basic units (UNIT)**
    #
    # * `bit`   bit
    # * `By`    byte
    # * `s`     second
    # * `min`   minute
    # * `h`     hour
    # * `d`     day
    #
    # **Prefixes (PREFIX)**
    #
    # * `k`     kilo    (10**3)
    # * `M`     mega    (10**6)
    # * `G`     giga    (10**9)
    # * `T`     tera    (10**12)
    # * `P`     peta    (10**15)
    # * `E`     exa     (10**18)
    # * `Z`     zetta   (10**21)
    # * `Y`     yotta   (10**24)
    # * `m`     milli   (10**-3)
    # * `u`     micro   (10**-6)
    # * `n`     nano    (10**-9)
    # * `p`     pico    (10**-12)
    # * `f`     femto   (10**-15)
    # * `a`     atto    (10**-18)
    # * `z`     zepto   (10**-21)
    # * `y`     yocto   (10**-24)
    # * `Ki`    kibi    (2**10)
    # * `Mi`    mebi    (2**20)
    # * `Gi`    gibi    (2**30)
    # * `Ti`    tebi    (2**40)
    #
    # **Grammar**
    #
    # The grammar also includes these connectors:
    #
    # * `/`    division (as an infix operator, e.g. `1/s`).
    # * `.`    multiplication (as an infix operator, e.g. `GBy.d`)
    #
    # The grammar for a unit is as follows:
    #
    #     Expression = Component { "." Component } { "/" Component } ;
    #
    #     Component = ( [ PREFIX ] UNIT | "%" ) [ Annotation ]
    #               | Annotation
    #               | "1"
    #               ;
    #
    #     Annotation = "{" NAME "}" ;
    #
    # Notes:
    #
    # * `Annotation` is just a comment if it follows a `UNIT` and is
    #    equivalent to `1` if it is used alone. For examples,
    #    `{requests}/s == 1/s`, `By{transmitted}/s == By/s`.
    # * `NAME` is a sequence of non-blank printable ASCII characters not
    #    containing '{' or '}'.
    # * `1` represents dimensionless value 1, such as in `1/s`.
    # * `%` represents dimensionless value 1/100, and annotates values giving
    #    a percentage.
    unit: typing.Text = ...
    # A detailed description of the metric, which can be used in documentation.
    description: typing.Text = ...
    # A concise name for the metric, which can be displayed in user interfaces.
    # Use sentence case without an ending period, for example "Request count".
    # This field is optional but it is recommended to be set for any metrics
    # associated with user-visible concepts, such as Quota.
    display_name: typing.Text = ...
    def __init__(
        self,
        *,
        name: typing.Text = ...,
        type: typing.Text = ...,
        labels: typing.Optional[
            typing.Iterable[google.api.label_pb2.LabelDescriptor]
        ] = ...,
        metric_kind: global___MetricDescriptor.MetricKind.V = ...,
        value_type: global___MetricDescriptor.ValueType.V = ...,
        unit: typing.Text = ...,
        description: typing.Text = ...,
        display_name: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "description",
            b"description",
            "display_name",
            b"display_name",
            "labels",
            b"labels",
            "metric_kind",
            b"metric_kind",
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

# A specific metric, identified by specifying values for all of the
# labels of a [`MetricDescriptor`][google.api.MetricDescriptor].
class Metric(google.protobuf.message.Message):
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
    TYPE_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    # An existing metric type, see [google.api.MetricDescriptor][google.api.MetricDescriptor].
    # For example, `custom.googleapis.com/invoice/paid/amount`.
    type: typing.Text = ...
    # The set of label values that uniquely identify this metric. All
    # labels listed in the `MetricDescriptor` must be assigned values.
    @property
    def labels(
        self,
    ) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...
    def __init__(
        self,
        *,
        type: typing.Text = ...,
        labels: typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["labels", b"labels", "type", b"type"],
    ) -> None: ...

global___Metric = Metric
