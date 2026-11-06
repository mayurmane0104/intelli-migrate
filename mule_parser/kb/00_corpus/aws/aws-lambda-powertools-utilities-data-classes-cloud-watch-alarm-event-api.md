# aws_lambda_powertools.utilities.data_classes.cloud_watch_alarm_event API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/cloud_watch_alarm_event.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/cloud_watch_alarm_event.html)

---

# Module `aws_lambda_powertools.utilities.data_classes.cloud_watch_alarm_event`

## Classes

- `class CloudWatchAlarmConfiguration (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class CloudWatchAlarmConfiguration(DictWrapper): @property def description(self) -> str | None: """ Optional description for the Alarm. """ return self.get("description", None) @property def alarm_rule(self) -> str | None: """ Optional description for the Alarm rule in case of composite alarm. """ return self.get("alarmRule", None) @property def alarm_actions_suppressor(self) -> str | None: """ Optional action suppression for the Alarm rule in case of composite alarm. """ return self.get("actionsSuppressor", None) @property def alarm_actions_suppressor_wait_period(self) -> str | None: """ Optional action suppression wait period for the Alarm rule in case of composite alarm. """ return self.get("actionsSuppressorWaitPeriod", None) @property def alarm_actions_suppressor_extension_period(self) -> str | None: """ Optional action suppression extension period for the Alarm rule in case of composite alarm. """ return self.get("actionsSuppressorExtensionPeriod", None) @property def metrics(self) -> list[CloudWatchAlarmMetric]: """ The metrics evaluated for the Alarm. """ metrics = self.get("metrics") or [] return [CloudWatchAlarmMetric(i) for i in metrics]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop alarm_actions_suppressor : str | None`
- 
## Expand source code`@property def alarm_actions_suppressor(self) -> str | None: """ Optional action suppression for the Alarm rule in case of composite alarm. """ return self.get("actionsSuppressor", None)`Optional action suppression for the Alarm rule in case of composite alarm. 
- `prop alarm_actions_suppressor_extension_period : str | None`
- 
## Expand source code`@property def alarm_actions_suppressor_extension_period(self) -> str | None: """ Optional action suppression extension period for the Alarm rule in case of composite alarm. """ return self.get("actionsSuppressorExtensionPeriod", None)`Optional action suppression extension period for the Alarm rule in case of composite alarm. 
- `prop alarm_actions_suppressor_wait_period : str | None`
- 
## Expand source code`@property def alarm_actions_suppressor_wait_period(self) -> str | None: """ Optional action suppression wait period for the Alarm rule in case of composite alarm. """ return self.get("actionsSuppressorWaitPeriod", None)`Optional action suppression wait period for the Alarm rule in case of composite alarm. 
- `prop alarm_rule : str | None`
- 
## Expand source code`@property def alarm_rule(self) -> str | None: """ Optional description for the Alarm rule in case of composite alarm. """ return self.get("alarmRule", None)`Optional description for the Alarm rule in case of composite alarm. 
- `prop description : str | None`
- 
## Expand source code`@property def description(self) -> str | None: """ Optional description for the Alarm. """ return self.get("description", None)`Optional description for the Alarm. 
- `prop metrics : list[`- [CloudWatchAlarmMetric](#aws_lambda_powertools.utilities.data_classes.cloud_watch_alarm_event.CloudWatchAlarmMetric)]
- 
## Expand source code`@property def metrics(self) -> list[CloudWatchAlarmMetric]: """ The metrics evaluated for the Alarm. """ metrics = self.get("metrics") or [] return [CloudWatchAlarmMetric(i) for i in metrics]`The metrics evaluated for the Alarm. 
 ### Inherited members
- `class CloudWatchAlarmData (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class CloudWatchAlarmData(DictWrapper): @property def alarm_name(self) -> str: """ Alarm name. """ return self["alarmName"] @property def state(self) -> CloudWatchAlarmState: """ The current state of the Alarm. """ return CloudWatchAlarmState(self["state"]) @property def previous_state(self) -> CloudWatchAlarmState: """ The previous state of the Alarm. """ return CloudWatchAlarmState(self["previousState"]) @property def configuration(self) -> CloudWatchAlarmConfiguration: """ The configuration of the Alarm. """ return CloudWatchAlarmConfiguration(self["configuration"])`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop alarm_name : str`
- 
## Expand source code`@property def alarm_name(self) -> str: """ Alarm name. """ return self["alarmName"]`Alarm name. 
- `prop configuration :`- [CloudWatchAlarmConfiguration](#aws_lambda_powertools.utilities.data_classes.cloud_watch_alarm_event.CloudWatchAlarmConfiguration)
- 
## Expand source code`@property def configuration(self) -> CloudWatchAlarmConfiguration: """ The configuration of the Alarm. """ return CloudWatchAlarmConfiguration(self["configuration"])`The configuration of the Alarm. 
- `prop previous_state :`- [CloudWatchAlarmState](#aws_lambda_powertools.utilities.data_classes.cloud_watch_alarm_event.CloudWatchAlarmState)
- 
## Expand source code`@property def previous_state(self) -> CloudWatchAlarmState: """ The previous state of the Alarm. """ return CloudWatchAlarmState(self["previousState"])`The previous state of the Alarm. 
- `prop state :`- [CloudWatchAlarmState](#aws_lambda_powertools.utilities.data_classes.cloud_watch_alarm_event.CloudWatchAlarmState)
- 
## Expand source code`@property def state(self) -> CloudWatchAlarmState: """ The current state of the Alarm. """ return CloudWatchAlarmState(self["state"])`The current state of the Alarm. 
 ### Inherited members
- `class CloudWatchAlarmEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class CloudWatchAlarmEvent(DictWrapper): @property def source(self) -> Literal["aws.cloudwatch"]: """ Source of the triggered event. """ return self["source"] @property def alarm_arn(self) -> str: """ The ARN of the CloudWatch Alarm. """ return self["alarmArn"] @property def region(self) -> str: """ The AWS region in which the Alarm is active. """ return self["region"] @property def source_account_id(self) -> str: """ The AWS Account ID that the Alarm is deployed to. """ return self["accountId"] @property def timestamp(self) -> str: """ Alarm state change event timestamp in ISO-8601 format. """ return self["time"] @property def alarm_data(self) -> CloudWatchAlarmData: """ Contains basic data about the Alarm and its current and previous states. """ return CloudWatchAlarmData(self["alarmData"])`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop alarm_arn : str`
- 
## Expand source code`@property def alarm_arn(self) -> str: """ The ARN of the CloudWatch Alarm. """ return self["alarmArn"]`The ARN of the CloudWatch Alarm. 
- `prop alarm_data :`- [CloudWatchAlarmData](#aws_lambda_powertools.utilities.data_classes.cloud_watch_alarm_event.CloudWatchAlarmData)
- 
## Expand source code`@property def alarm_data(self) -> CloudWatchAlarmData: """ Contains basic data about the Alarm and its current and previous states. """ return CloudWatchAlarmData(self["alarmData"])`Contains basic data about the Alarm and its current and previous states. 
- `prop region : str`
- 
## Expand source code`@property def region(self) -> str: """ The AWS region in which the Alarm is active. """ return self["region"]`The AWS region in which the Alarm is active. 
- `prop source : Literal['aws.cloudwatch']`
- 
## Expand source code`@property def source(self) -> Literal["aws.cloudwatch"]: """ Source of the triggered event. """ return self["source"]`Source of the triggered event. 
- `prop source_account_id : str`
- 
## Expand source code`@property def source_account_id(self) -> str: """ The AWS Account ID that the Alarm is deployed to. """ return self["accountId"]`The AWS Account ID that the Alarm is deployed to. 
- `prop timestamp : str`
- 
## Expand source code`@property def timestamp(self) -> str: """ Alarm state change event timestamp in ISO-8601 format. """ return self["time"]`Alarm state change event timestamp in ISO-8601 format. 
 ### Inherited members
- `class CloudWatchAlarmMetric (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class CloudWatchAlarmMetric(DictWrapper): @property def metric_id(self) -> str: """ Unique ID of the alarm metric. """ return self["id"] @property def expression(self) -> str | None: """ Optional expression of the alarm metric. """ return self.get("expression", None) @property def label(self) -> str | None: """ Optional label of the alarm metric. """ return self.get("label", None) @property def return_data(self) -> bool: """ Whether this metric data is used to determine the state of the alarm or not. """ return self["returnData"] @property def metric_stat(self) -> CloudWatchAlarmMetricStat: return CloudWatchAlarmMetricStat(self["metricStat"])`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop expression : str | None`
- 
## Expand source code`@property def expression(self) -> str | None: """ Optional expression of the alarm metric. """ return self.get("expression", None)`Optional expression of the alarm metric. 
- `prop label : str | None`
- 
## Expand source code`@property def label(self) -> str | None: """ Optional label of the alarm metric. """ return self.get("label", None)`Optional label of the alarm metric. 
- `prop metric_id : str`
- 
## Expand source code`@property def metric_id(self) -> str: """ Unique ID of the alarm metric. """ return self["id"]`Unique ID of the alarm metric. 
- `prop metric_stat :`- [CloudWatchAlarmMetricStat](#aws_lambda_powertools.utilities.data_classes.cloud_watch_alarm_event.CloudWatchAlarmMetricStat)
- 
## Expand source code`@property def metric_stat(self) -> CloudWatchAlarmMetricStat: return CloudWatchAlarmMetricStat(self["metricStat"])`
- `prop return_data : bool`
- 
## Expand source code`@property def return_data(self) -> bool: """ Whether this metric data is used to determine the state of the alarm or not. """ return self["returnData"]`Whether this metric data is used to determine the state of the alarm or not. 
 ### Inherited members
- `class CloudWatchAlarmMetricStat (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class CloudWatchAlarmMetricStat(DictWrapper): @property def period(self) -> int | None: """ Metric evaluation period, in seconds. """ return self.get("period", None) @property def stat(self) -> str | None: """ Statistical aggregation of metric points, e.g. Average, SampleCount, etc. """ return self.get("stat", None) @property def unit(self) -> str | None: """ Unit for metric. """ return self.get("unit", None) @property def metric(self) -> dict: """ Metric details """ return self.get("metric") or {}`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop metric : dict`
- 
## Expand source code`@property def metric(self) -> dict: """ Metric details """ return self.get("metric") or {}`Metric details 
- `prop period : int | None`
- 
## Expand source code`@property def period(self) -> int | None: """ Metric evaluation period, in seconds. """ return self.get("period", None)`Metric evaluation period, in seconds. 
- `prop stat : str | None`
- 
## Expand source code`@property def stat(self) -> str | None: """ Statistical aggregation of metric points, e.g. Average, SampleCount, etc. """ return self.get("stat", None)`Statistical aggregation of metric points, e.g. Average, SampleCount, etc. 
- `prop unit : str | None`
- 
## Expand source code`@property def unit(self) -> str | None: """ Unit for metric. """ return self.get("unit", None)`Unit for metric. 
 ### Inherited members
- `class CloudWatchAlarmState (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class CloudWatchAlarmState(DictWrapper): @property def value(self) -> Literal["OK", "ALARM", "INSUFFICIENT_DATA"]: """ Overall state of the alarm. """ return self["value"] @property def reason(self) -> str: """ Reason why alarm was changed to this state. """ return self["reason"] @property def reason_data(self) -> str: """ Additional data to back up the reason, usually contains the evaluated data points, the calculated threshold and timestamps. """ return self["reasonData"] @cached_property def reason_data_decoded(self) -> Any | None: """ Deserialized version of reason_data. """ return self._json_deserializer(self.reason_data) if self.reason_data else None @property def actions_suppressed_by(self) -> Literal["Alarm", "ExtensionPeriod", "WaitPeriod"] | None: """ Describes why the actions when the value is `ALARM` are suppressed in a composite alarm. """ return self.get("actionsSuppressedBy", None) @property def actions_suppressed_reason(self) -> str | None: """ Captures the reason for action suppression. """ return self.get("actionsSuppressedReason", None) @property def timestamp(self) -> str: """ Timestamp of this state change in ISO-8601 format. """ return self["timestamp"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop actions_suppressed_by : Literal['Alarm', 'ExtensionPeriod', 'WaitPeriod'] | None`
- 
## Expand source code`@property def actions_suppressed_by(self) -> Literal["Alarm", "ExtensionPeriod", "WaitPeriod"] | None: """ Describes why the actions when the value is `ALARM` are suppressed in a composite alarm. """ return self.get("actionsSuppressedBy", None)`Describes why the actions when the value is `ALARM`are suppressed in a composite alarm.
- `prop actions_suppressed_reason : str | None`
- 
## Expand source code`@property def actions_suppressed_reason(self) -> str | None: """ Captures the reason for action suppression. """ return self.get("actionsSuppressedReason", None)`Captures the reason for action suppression. 
- `prop reason : str`
- 
## Expand source code`@property def reason(self) -> str: """ Reason why alarm was changed to this state. """ return self["reason"]`Reason why alarm was changed to this state. 
- `prop reason_data : str`
- 
## Expand source code`@property def reason_data(self) -> str: """ Additional data to back up the reason, usually contains the evaluated data points, the calculated threshold and timestamps. """ return self["reasonData"]`Additional data to back up the reason, usually contains the evaluated data points, the calculated threshold and timestamps. 
- `var reason_data_decoded : Any | None`
- 
## Expand source code`@cached_property def reason_data_decoded(self) -> Any | None: """ Deserialized version of reason_data. """ return self._json_deserializer(self.reason_data) if self.reason_data else None`Deserialized version of reason_data. 
- `prop timestamp : str`
- 
## Expand source code`@property def timestamp(self) -> str: """ Timestamp of this state change in ISO-8601 format. """ return self["timestamp"]`Timestamp of this state change in ISO-8601 format. 
- `prop value : Literal['OK', 'ALARM', 'INSUFFICIENT_DATA']`
- 
## Expand source code`@property def value(self) -> Literal["OK", "ALARM", "INSUFFICIENT_DATA"]: """ Overall state of the alarm. """ return self["value"]`Overall state of the alarm. 
 ### Inherited members