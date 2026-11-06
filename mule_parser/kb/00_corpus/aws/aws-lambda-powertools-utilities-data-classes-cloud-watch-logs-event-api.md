# aws_lambda_powertools.utilities.data_classes.cloud_watch_logs_event API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/cloud_watch_logs_event.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/cloud_watch_logs_event.html)

---

# Module `aws_lambda_powertools.utilities.data_classes.cloud_watch_logs_event`

## Classes

- `class CloudWatchLogsDecodedData (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class CloudWatchLogsDecodedData(DictWrapper): @property def owner(self) -> str: """The AWS Account ID of the originating log data.""" return self["owner"] @property def log_group(self) -> str: """The log group name of the originating log data.""" return self["logGroup"] @property def log_stream(self) -> str: """The log stream name of the originating log data.""" return self["logStream"] @property def subscription_filters(self) -> list[str]: """The list of subscription filter names that matched with the originating log data.""" return self["subscriptionFilters"] @property def message_type(self) -> str: """Data messages will use the "DATA_MESSAGE" type. Sometimes CloudWatch Logs may emit Kinesis records with a "CONTROL_MESSAGE" type, mainly for checking if the destination is reachable. """ return self["messageType"] @property def policy_level(self) -> str | None: """The level at which the policy was enforced.""" return self.get("policyLevel") @property def log_events(self) -> list[CloudWatchLogsLogEvent]: """The actual log data, represented as an array of log event records. The ID property is a unique identifier for every log event. """ return [CloudWatchLogsLogEvent(i) for i in self["logEvents"]]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop log_events : list[`- [CloudWatchLogsLogEvent](#aws_lambda_powertools.utilities.data_classes.cloud_watch_logs_event.CloudWatchLogsLogEvent)]
- 
## Expand source code`@property def log_events(self) -> list[CloudWatchLogsLogEvent]: """The actual log data, represented as an array of log event records. The ID property is a unique identifier for every log event. """ return [CloudWatchLogsLogEvent(i) for i in self["logEvents"]]`The actual log data, represented as an array of log event records. The ID property is a unique identifier for every log event. 
- `prop log_group : str`
- 
## Expand source code`@property def log_group(self) -> str: """The log group name of the originating log data.""" return self["logGroup"]`The log group name of the originating log data. 
- `prop log_stream : str`
- 
## Expand source code`@property def log_stream(self) -> str: """The log stream name of the originating log data.""" return self["logStream"]`The log stream name of the originating log data. 
- `prop message_type : str`
- 
## Expand source code`@property def message_type(self) -> str: """Data messages will use the "DATA_MESSAGE" type. Sometimes CloudWatch Logs may emit Kinesis records with a "CONTROL_MESSAGE" type, mainly for checking if the destination is reachable. """ return self["messageType"]`Data messages will use the "DATA_MESSAGE" type. Sometimes CloudWatch Logs may emit Kinesis records with a "CONTROL_MESSAGE" type, mainly for checking if the destination is reachable. 
- `prop owner : str`
- 
## Expand source code`@property def owner(self) -> str: """The AWS Account ID of the originating log data.""" return self["owner"]`The AWS Account ID of the originating log data. 
- `prop policy_level : str | None`
- 
## Expand source code`@property def policy_level(self) -> str | None: """The level at which the policy was enforced.""" return self.get("policyLevel")`The level at which the policy was enforced. 
- `prop subscription_filters : list[str]`
- 
## Expand source code`@property def subscription_filters(self) -> list[str]: """The list of subscription filter names that matched with the originating log data.""" return self["subscriptionFilters"]`The list of subscription filter names that matched with the originating log data. 
 ### Inherited members
- `class CloudWatchLogsEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class CloudWatchLogsEvent(DictWrapper): """CloudWatch Logs log stream event You can use a Lambda function to monitor and analyze logs from an Amazon CloudWatch Logs log stream. Documentation: -------------- - https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchlogs.html """ _decompressed_logs_data = None _json_logs_data = None @property def raw_logs_data(self) -> str: """The value of the `data` field is a Base64 encoded ZIP archive.""" return self["awslogs"]["data"] @property def decompress_logs_data(self) -> bytes: """Decode and decompress log data""" if self._decompressed_logs_data is None: payload = base64.b64decode(self.raw_logs_data) self._decompressed_logs_data = zlib.decompress(payload, zlib.MAX_WBITS | 32) return self._decompressed_logs_data def parse_logs_data(self) -> CloudWatchLogsDecodedData: """Decode, decompress and parse json data as CloudWatchLogsDecodedData""" if self._json_logs_data is None: self._json_logs_data = self._json_deserializer(self.decompress_logs_data.decode("UTF-8")) return CloudWatchLogsDecodedData(self._json_logs_data)`CloudWatch Logs log stream event You can use a Lambda function to monitor and analyze logs from an Amazon CloudWatch Logs log stream. ## Documentation:## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop decompress_logs_data : bytes`
- 
## Expand source code`@property def decompress_logs_data(self) -> bytes: """Decode and decompress log data""" if self._decompressed_logs_data is None: payload = base64.b64decode(self.raw_logs_data) self._decompressed_logs_data = zlib.decompress(payload, zlib.MAX_WBITS | 32) return self._decompressed_logs_data`Decode and decompress log data 
- `prop raw_logs_data : str`
- 
## Expand source code`@property def raw_logs_data(self) -> str: """The value of the `data` field is a Base64 encoded ZIP archive.""" return self["awslogs"]["data"]`The value of the `data`field is a Base64 encoded ZIP archive.
 ### Methods- `def parse_logs_data(self) ‑>`- [CloudWatchLogsDecodedData](#aws_lambda_powertools.utilities.data_classes.cloud_watch_logs_event.CloudWatchLogsDecodedData)
- 
## Expand source code`def parse_logs_data(self) -> CloudWatchLogsDecodedData: """Decode, decompress and parse json data as CloudWatchLogsDecodedData""" if self._json_logs_data is None: self._json_logs_data = self._json_deserializer(self.decompress_logs_data.decode("UTF-8")) return CloudWatchLogsDecodedData(self._json_logs_data)`Decode, decompress and parse json data as CloudWatchLogsDecodedData 
 ### Inherited members
- `class CloudWatchLogsLogEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class CloudWatchLogsLogEvent(DictWrapper): @property def get_id(self) -> str: """The ID property is a unique identifier for every log event.""" # Note: this name conflicts with existing python builtins return self["id"] @property def timestamp(self) -> int: """Get the `timestamp` property""" return self["timestamp"] @property def message(self) -> str: """Get the `message` property""" return self["message"] @property def extracted_fields(self) -> dict[str, str]: """Get the `extractedFields` property""" return self.get("extractedFields") or {}`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop extracted_fields : dict[str, str]`
- 
## Expand source code`@property def extracted_fields(self) -> dict[str, str]: """Get the `extractedFields` property""" return self.get("extractedFields") or {}`Get the `extractedFields`property
- `prop get_id : str`
- 
## Expand source code`@property def get_id(self) -> str: """The ID property is a unique identifier for every log event.""" # Note: this name conflicts with existing python builtins return self["id"]`The ID property is a unique identifier for every log event. 
- `prop message : str`
- 
## Expand source code`@property def message(self) -> str: """Get the `message` property""" return self["message"]`Get the `message`property
- `prop timestamp : int`
- 
## Expand source code`@property def timestamp(self) -> int: """Get the `timestamp` property""" return self["timestamp"]`Get the `timestamp`property
 ### Inherited members