# aws_lambda_powertools.utilities.data_classes.event_bridge_event API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/event_bridge_event.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/event_bridge_event.html)

---

# Module `aws_lambda_powertools.utilities.data_classes.event_bridge_event`

## Classes

- `class EventBridgeEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class EventBridgeEvent(DictWrapper): """Amazon EventBridge Event Documentation: -------------- - https://docs.aws.amazon.com/eventbridge/latest/userguide/aws-events.html """ @property def get_id(self) -> str: """A unique value is generated for every event. This can be helpful in tracing events as they move through rules to targets, and are processed.""" # Note: this name conflicts with existing python builtins return self["id"] @property def version(self) -> str: """By default, this is set to 0 (zero) in all events.""" return self["version"] @property def account(self) -> str: """The 12-digit number identifying an AWS account.""" return self["account"] @property def time(self) -> str: """The event timestamp, which can be specified by the service originating the event. If the event spans a time interval, the service might choose to report the start time, so this value can be noticeably before the time the event is actually received. """ return self["time"] @property def region(self) -> str: """Identifies the AWS region where the event originated.""" return self["region"] @property def resources(self) -> list[str]: """This JSON array contains ARNs that identify resources that are involved in the event. Inclusion of these ARNs is at the discretion of the service.""" return self["resources"] @property def source(self) -> str: """Identifies the service that sourced the event. All events sourced from within AWS begin with "aws." """ return self["source"] @property def detail_type(self) -> str: """Identifies, in combination with the source field, the fields and values that appear in the detail field.""" return self["detail-type"] @property def detail(self) -> dict[str, Any]: """A JSON object, whose content is at the discretion of the service originating the event.""" return self["detail"] @property def replay_name(self) -> str | None: """Identifies whether the event is being replayed and what is the name of the replay.""" return self["replay-name"]`Amazon EventBridge Event ## Documentation:## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Subclasses### Instance variables- `prop account : str`
- 
## Expand source code`@property def account(self) -> str: """The 12-digit number identifying an AWS account.""" return self["account"]`The 12-digit number identifying an AWS account. 
- `prop detail : dict[str, Any]`
- 
## Expand source code`@property def detail(self) -> dict[str, Any]: """A JSON object, whose content is at the discretion of the service originating the event.""" return self["detail"]`A JSON object, whose content is at the discretion of the service originating the event. 
- `prop detail_type : str`
- 
## Expand source code`@property def detail_type(self) -> str: """Identifies, in combination with the source field, the fields and values that appear in the detail field.""" return self["detail-type"]`Identifies, in combination with the source field, the fields and values that appear in the detail field. 
- `prop get_id : str`
- 
## Expand source code`@property def get_id(self) -> str: """A unique value is generated for every event. This can be helpful in tracing events as they move through rules to targets, and are processed.""" # Note: this name conflicts with existing python builtins return self["id"]`A unique value is generated for every event. This can be helpful in tracing events as they move through rules to targets, and are processed. 
- `prop region : str`
- 
## Expand source code`@property def region(self) -> str: """Identifies the AWS region where the event originated.""" return self["region"]`Identifies the AWS region where the event originated. 
- `prop replay_name : str | None`
- 
## Expand source code`@property def replay_name(self) -> str | None: """Identifies whether the event is being replayed and what is the name of the replay.""" return self["replay-name"]`Identifies whether the event is being replayed and what is the name of the replay. 
- `prop resources : list[str]`
- 
## Expand source code`@property def resources(self) -> list[str]: """This JSON array contains ARNs that identify resources that are involved in the event. Inclusion of these ARNs is at the discretion of the service.""" return self["resources"]`This JSON array contains ARNs that identify resources that are involved in the event. Inclusion of these ARNs is at the discretion of the service. 
- `prop source : str`
- 
## Expand source code`@property def source(self) -> str: """Identifies the service that sourced the event. All events sourced from within AWS begin with "aws." """ return self["source"]`Identifies the service that sourced the event. All events sourced from within AWS begin with "aws." 
- `prop time : str`
- 
## Expand source code`@property def time(self) -> str: """The event timestamp, which can be specified by the service originating the event. If the event spans a time interval, the service might choose to report the start time, so this value can be noticeably before the time the event is actually received. """ return self["time"]`The event timestamp, which can be specified by the service originating the event. If the event spans a time interval, the service might choose to report the start time, so this value can be noticeably before the time the event is actually received. 
- `prop version : str`
- 
## Expand source code`@property def version(self) -> str: """By default, this is set to 0 (zero) in all events.""" return self["version"]`By default, this is set to 0 (zero) in all events. 
 ### Inherited members