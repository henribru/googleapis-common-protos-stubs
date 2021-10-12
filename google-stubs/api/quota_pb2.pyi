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

# Quota configuration helps to achieve fairness and budgeting in service
# usage.
#
# The quota configuration works this way:
# - The service configuration defines a set of metrics.
# - For API calls, the quota.metric_rules maps methods to metrics with
#   corresponding costs.
# - The quota.limits defines limits on the metrics, which will be used for
#   quota checks at runtime.
#
# An example quota configuration in yaml format:
#
#    quota:
#      limits:
#
#      - name: apiWriteQpsPerProject
#        metric: library.googleapis.com/write_calls
#        unit: "1/min/{project}"  # rate limit for consumer projects
#        values:
#          STANDARD: 10000
#
#      # The metric rules bind all methods to the read_calls metric,
#      # except for the UpdateBook and DeleteBook methods. These two methods
#      # are mapped to the write_calls metric, with the UpdateBook method
#      # consuming at twice rate as the DeleteBook method.
#      metric_rules:
#      - selector: "*"
#        metric_costs:
#          library.googleapis.com/read_calls: 1
#      - selector: google.example.library.v1.LibraryService.UpdateBook
#        metric_costs:
#          library.googleapis.com/write_calls: 2
#      - selector: google.example.library.v1.LibraryService.DeleteBook
#        metric_costs:
#          library.googleapis.com/write_calls: 1
#
#  Corresponding Metric definition:
#
#      metrics:
#      - name: library.googleapis.com/read_calls
#        display_name: Read requests
#        metric_kind: DELTA
#        value_type: INT64
#
#      - name: library.googleapis.com/write_calls
#        display_name: Write requests
#        metric_kind: DELTA
#        value_type: INT64
class Quota(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    LIMITS_FIELD_NUMBER: builtins.int
    METRIC_RULES_FIELD_NUMBER: builtins.int
    # List of `QuotaLimit` definitions for the service.
    #
    # Used by metric-based quotas only.
    @property
    def limits(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___QuotaLimit
    ]: ...
    # List of `MetricRule` definitions, each one mapping a selected method to one
    # or more metrics.
    #
    # Used by metric-based quotas only.
    @property
    def metric_rules(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___MetricRule
    ]: ...
    def __init__(
        self,
        *,
        limits: typing.Optional[typing.Iterable[global___QuotaLimit]] = ...,
        metric_rules: typing.Optional[typing.Iterable[global___MetricRule]] = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "limits", b"limits", "metric_rules", b"metric_rules"
        ],
    ) -> None: ...

global___Quota = Quota

# Bind API methods to metrics. Binding a method to a metric causes that
# metric's configured quota, billing, and monitoring behaviors to apply to the
# method call.
#
# Used by metric-based quotas only.
class MetricRule(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class MetricCostsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: builtins.int = ...
        def __init__(
            self,
            *,
            key: typing.Text = ...,
            value: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...
    SELECTOR_FIELD_NUMBER: builtins.int
    METRIC_COSTS_FIELD_NUMBER: builtins.int
    # Selects the methods to which this rule applies.
    #
    # Refer to [selector][google.api.DocumentationRule.selector] for syntax details.
    selector: typing.Text = ...
    # Metrics to update when the selected methods are called, and the associated
    # cost applied to each metric.
    #
    # The key of the map is the metric name, and the values are the amount
    # increased for the metric against which the quota limits are defined.
    # The value must not be negative.
    @property
    def metric_costs(
        self,
    ) -> google.protobuf.internal.containers.ScalarMap[typing.Text, builtins.int]: ...
    def __init__(
        self,
        *,
        selector: typing.Text = ...,
        metric_costs: typing.Optional[typing.Mapping[typing.Text, builtins.int]] = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "metric_costs", b"metric_costs", "selector", b"selector"
        ],
    ) -> None: ...

global___MetricRule = MetricRule

# `QuotaLimit` defines a specific limit that applies over a specified duration
# for a limit type. There can be at most one limit for a duration and limit
# type combination defined within a `QuotaGroup`.
class QuotaLimit(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class ValuesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: builtins.int = ...
        def __init__(
            self,
            *,
            key: typing.Text = ...,
            value: builtins.int = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    DEFAULT_LIMIT_FIELD_NUMBER: builtins.int
    MAX_LIMIT_FIELD_NUMBER: builtins.int
    FREE_TIER_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    METRIC_FIELD_NUMBER: builtins.int
    UNIT_FIELD_NUMBER: builtins.int
    VALUES_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    # Name of the quota limit. The name is used to refer to the limit when
    # overriding the default limit on per-consumer basis.
    #
    # For group-based quota limits, the name must be unique within the quota
    # group. If a name is not provided, it will be generated from the limit_by
    # and duration fields.
    #
    # For metric-based quota limits, the name must be provided, and it must be
    # unique within the service. The name can only include alphanumeric
    # characters as well as '-'.
    #
    # The maximum length of the limit name is 64 characters.
    #
    # The name of a limit is used as a unique identifier for this limit.
    # Therefore, once a limit has been put into use, its name should be
    # immutable. You can use the display_name field to provide a user-friendly
    # name for the limit. The display name can be evolved over time without
    # affecting the identity of the limit.
    name: typing.Text = ...
    # Optional. User-visible, extended description for this quota limit.
    # Should be used only when more context is needed to understand this limit
    # than provided by the limit's display name (see: `display_name`).
    description: typing.Text = ...
    # Default number of tokens that can be consumed during the specified
    # duration. This is the number of tokens assigned when a client
    # application developer activates the service for his/her project.
    #
    # Specifying a value of 0 will block all requests. This can be used if you
    # are provisioning quota to selected consumers and blocking others.
    # Similarly, a value of -1 will indicate an unlimited quota. No other
    # negative values are allowed.
    #
    # Used by group-based quotas only.
    default_limit: builtins.int = ...
    # Maximum number of tokens that can be consumed during the specified
    # duration. Client application developers can override the default limit up
    # to this maximum. If specified, this value cannot be set to a value less
    # than the default limit. If not specified, it is set to the default limit.
    #
    # To allow clients to apply overrides with no upper bound, set this to -1,
    # indicating unlimited maximum quota.
    #
    # Used by group-based quotas only.
    max_limit: builtins.int = ...
    # Free tier value displayed in the Developers Console for this limit.
    # The free tier is the number of tokens that will be subtracted from the
    # billed amount when billing is enabled.
    # This field can only be set on a limit with duration "1d", in a billable
    # group; it is invalid on any other limit. If this field is not set, it
    # defaults to 0, indicating that there is no free tier for this service.
    #
    # Used by group-based quotas only.
    free_tier: builtins.int = ...
    # Duration of this limit in textual notation. Example: "100s", "24h", "1d".
    # For duration longer than a day, only multiple of days is supported. We
    # support only "100s" and "1d" for now. Additional support will be added in
    # the future. "0" indicates indefinite duration.
    #
    # Used by group-based quotas only.
    duration: typing.Text = ...
    # The name of the metric this quota limit applies to. The quota limits with
    # the same metric will be checked together during runtime. The metric must be
    # defined within the service config.
    #
    # Used by metric-based quotas only.
    metric: typing.Text = ...
    # Specify the unit of the quota limit. It uses the same syntax as
    # [Metric.unit][]. The supported unit kinds are determined by the quota
    # backend system.
    #
    # The [Google Service Control](https://cloud.google.com/service-control)
    # supports the following unit components:
    # * One of the time intevals:
    #   * "/min"  for quota every minute.
    #   * "/d"  for quota every 24 hours, starting 00:00 US Pacific Time.
    #   * Otherwise the quota won't be reset by time, such as storage limit.
    # * One and only one of the granted containers:
    #   * "/{organization}" quota for an organization.
    #   * "/{project}" quota for a project.
    #   * "/{folder}" quota for a folder.
    #   * "/{resource}" quota for a universal resource.
    # * Zero or more quota segmentation dimension. Not all combos are valid.
    #   * "/{region}" quota for every region. Not to be used with time intervals.
    #   * Otherwise the resources granted on the target is not segmented.
    #   * "/{zone}" quota for every zone. Not to be used with time intervals.
    #   * Otherwise the resources granted on the target is not segmented.
    #   * "/{resource}" quota for a resource associated with a project or org.
    #
    # Here are some examples:
    # * "1/min/{project}" for quota per minute per project.
    # * "1/min/{user}" for quota per minute per user.
    # * "1/min/{organization}" for quota per minute per organization.
    #
    # Note: the order of unit components is insignificant.
    # The "1" at the beginning is required to follow the metric unit syntax.
    #
    # Used by metric-based quotas only.
    unit: typing.Text = ...
    # Tiered limit values. Also allows for regional or zone overrides for these
    # values if "/{region}" or "/{zone}" is specified in the unit field.
    #
    # Currently supported tiers from low to high:
    # VERY_LOW, LOW, STANDARD, HIGH, VERY_HIGH
    #
    # To apply different limit values for users according to their tiers, specify
    # the values for the tiers you want to differentiate. For example:
    # {LOW:100, STANDARD:500, HIGH:1000, VERY_HIGH:5000}
    #
    # The limit value for each tier is optional except for the tier STANDARD.
    # The limit value for an unspecified tier falls to the value of its next
    # tier towards tier STANDARD. For the above example, the limit value for tier
    # STANDARD is 500.
    #
    # To apply the same limit value for all users, just specify limit value for
    # tier STANDARD. For example: {STANDARD:500}.
    #
    # To apply a regional overide for a tier, add a map entry with key
    # "<TIER>/<region>", where <region> is a region name. Similarly, for a zone
    # override, add a map entry with key "<TIER>/{zone}".
    # Further, a wildcard can be used at the end of a zone name in order to
    # specify zone level overrides. For example:
    # LOW: 10, STANDARD: 50, HIGH: 100,
    # LOW/us-central1: 20, STANDARD/us-central1: 60, HIGH/us-central1: 200,
    # LOW/us-central1-*: 10, STANDARD/us-central1-*: 20, HIGH/us-central1-*: 80
    #
    # The regional overrides tier set for each region must be the same as
    # the tier set for default limit values. Same rule applies for zone overrides
    # tier as well.
    #
    # Used by metric-based quotas only.
    @property
    def values(
        self,
    ) -> google.protobuf.internal.containers.ScalarMap[typing.Text, builtins.int]: ...
    # User-visible display name for this limit.
    # Optional. If not set, the UI will provide a default display name based on
    # the quota configuration. This field can be used to override the default
    # display name generated from the configuration.
    display_name: typing.Text = ...
    def __init__(
        self,
        *,
        name: typing.Text = ...,
        description: typing.Text = ...,
        default_limit: builtins.int = ...,
        max_limit: builtins.int = ...,
        free_tier: builtins.int = ...,
        duration: typing.Text = ...,
        metric: typing.Text = ...,
        unit: typing.Text = ...,
        values: typing.Optional[typing.Mapping[typing.Text, builtins.int]] = ...,
        display_name: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "default_limit",
            b"default_limit",
            "description",
            b"description",
            "display_name",
            b"display_name",
            "duration",
            b"duration",
            "free_tier",
            b"free_tier",
            "max_limit",
            b"max_limit",
            "metric",
            b"metric",
            "name",
            b"name",
            "unit",
            b"unit",
            "values",
            b"values",
        ],
    ) -> None: ...

global___QuotaLimit = QuotaLimit
