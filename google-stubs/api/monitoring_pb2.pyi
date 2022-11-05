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
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Monitoring(google.protobuf.message.Message):
    """Monitoring configuration of the service.

    The example below shows how to configure monitored resources and metrics
    for monitoring. In the example, a monitored resource and two metrics are
    defined. The `library.googleapis.com/book/returned_count` metric is sent
    to both producer and consumer projects, whereas the
    `library.googleapis.com/book/num_overdue` metric is only sent to the
    consumer project.

        monitored_resources:
        - type: library.googleapis.com/Branch
          display_name: "Library Branch"
          description: "A branch of a library."
          launch_stage: GA
          labels:
          - key: resource_container
            description: "The Cloud container (ie. project id) for the Branch."
          - key: location
            description: "The location of the library branch."
          - key: branch_id
            description: "The id of the branch."
        metrics:
        - name: library.googleapis.com/book/returned_count
          display_name: "Books Returned"
          description: "The count of books that have been returned."
          launch_stage: GA
          metric_kind: DELTA
          value_type: INT64
          unit: "1"
          labels:
          - key: customer_id
            description: "The id of the customer."
        - name: library.googleapis.com/book/num_overdue
          display_name: "Books Overdue"
          description: "The current number of overdue books."
          launch_stage: GA
          metric_kind: GAUGE
          value_type: INT64
          unit: "1"
          labels:
          - key: customer_id
            description: "The id of the customer."
        monitoring:
          producer_destinations:
          - monitored_resource: library.googleapis.com/Branch
            metrics:
            - library.googleapis.com/book/returned_count
          consumer_destinations:
          - monitored_resource: library.googleapis.com/Branch
            metrics:
            - library.googleapis.com/book/returned_count
            - library.googleapis.com/book/num_overdue
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    @typing_extensions.final
    class MonitoringDestination(google.protobuf.message.Message):
        """Configuration of a specific monitoring destination (the producer project
        or the consumer project).
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        MONITORED_RESOURCE_FIELD_NUMBER: builtins.int
        METRICS_FIELD_NUMBER: builtins.int
        monitored_resource: builtins.str
        """The monitored resource type. The type must be defined in
        [Service.monitored_resources][google.api.Service.monitored_resources] section.
        """
        @property
        def metrics(
            self,
        ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
            builtins.str
        ]:
            """Types of the metrics to report to this monitoring destination.
            Each type must be defined in [Service.metrics][google.api.Service.metrics] section.
            """
        def __init__(
            self,
            *,
            monitored_resource: builtins.str = ...,
            metrics: collections.abc.Iterable[builtins.str] | None = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "metrics", b"metrics", "monitored_resource", b"monitored_resource"
            ],
        ) -> None: ...
    PRODUCER_DESTINATIONS_FIELD_NUMBER: builtins.int
    CONSUMER_DESTINATIONS_FIELD_NUMBER: builtins.int
    @property
    def producer_destinations(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___Monitoring.MonitoringDestination
    ]:
        """Monitoring configurations for sending metrics to the producer project.
        There can be multiple producer destinations. A monitored resource type may
        appear in multiple monitoring destinations if different aggregations are
        needed for different sets of metrics associated with that monitored
        resource type. A monitored resource and metric pair may only be used once
        in the Monitoring configuration.
        """
    @property
    def consumer_destinations(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___Monitoring.MonitoringDestination
    ]:
        """Monitoring configurations for sending metrics to the consumer project.
        There can be multiple consumer destinations. A monitored resource type may
        appear in multiple monitoring destinations if different aggregations are
        needed for different sets of metrics associated with that monitored
        resource type. A monitored resource and metric pair may only be used once
        in the Monitoring configuration.
        """
    def __init__(
        self,
        *,
        producer_destinations: collections.abc.Iterable[
            global___Monitoring.MonitoringDestination
        ]
        | None = ...,
        consumer_destinations: collections.abc.Iterable[
            global___Monitoring.MonitoringDestination
        ]
        | None = ...,
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

global___Monitoring = Monitoring
