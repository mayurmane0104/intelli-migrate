# aws_lambda_powertools.utilities.data_classes.kinesis_stream_event API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/kinesis_stream_event.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/kinesis_stream_event.html)

---

# Module `aws_lambda_powertools.utilities.data_classes.kinesis_stream_event`

## Functions

- `def extract_cloudwatch_logs_from_event(event:`- [KinesisStreamEvent](#aws_lambda_powertools.utilities.data_classes.kinesis_stream_event.KinesisStreamEvent)) ‑> list[- [CloudWatchLogsDecodedData](cloud_watch_logs_event.html#aws_lambda_powertools.utilities.data_classes.cloud_watch_logs_event.CloudWatchLogsDecodedData)]
- 
## Expand source code`def extract_cloudwatch_logs_from_event(event: KinesisStreamEvent) -> list[CloudWatchLogsDecodedData]: return [CloudWatchLogsDecodedData(record.kinesis.data_zlib_compressed_as_json()) for record in event.records]`
- `def extract_cloudwatch_logs_from_record(record:`- [KinesisStreamRecord](#aws_lambda_powertools.utilities.data_classes.kinesis_stream_event.KinesisStreamRecord)) ‑>- [CloudWatchLogsDecodedData](cloud_watch_logs_event.html#aws_lambda_powertools.utilities.data_classes.cloud_watch_logs_event.CloudWatchLogsDecodedData)
- 
## Expand source code`def extract_cloudwatch_logs_from_record(record: KinesisStreamRecord) -> CloudWatchLogsDecodedData: return CloudWatchLogsDecodedData(data=record.kinesis.data_zlib_compressed_as_json())`

## Classes

- `class KinesisStreamEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class KinesisStreamEvent(DictWrapper): """Kinesis stream event Documentation: -------------- - https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html """ @property def records(self) -> Iterator[KinesisStreamRecord]: for record in self["Records"]: yield KinesisStreamRecord(record)`Kinesis stream event ## Documentation:## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop records : Iterator[`- [KinesisStreamRecord](#aws_lambda_powertools.utilities.data_classes.kinesis_stream_event.KinesisStreamRecord)]
- 
## Expand source code`@property def records(self) -> Iterator[KinesisStreamRecord]: for record in self["Records"]: yield KinesisStreamRecord(record)`
 ### Inherited members
- `class KinesisStreamRecord (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class KinesisStreamRecord(DictWrapper): @property def aws_region(self) -> str: """AWS region where the event originated eg: us-east-1""" return self["awsRegion"] @property def event_id(self) -> str: """A globally unique identifier for the event that was recorded in this stream record.""" return self["eventID"] @property def event_name(self) -> str: """Event type eg: aws:kinesis:record""" return self["eventName"] @property def event_source(self) -> str: """The AWS service from which the Kinesis event originated. For Kinesis, this is aws:kinesis""" return self["eventSource"] @property def event_source_arn(self) -> str: """The Amazon Resource Name (ARN) of the event source""" return self["eventSourceARN"] @property def event_version(self) -> str: """The eventVersion key value contains a major and minor version in the form <major>.<minor>.""" return self["eventVersion"] @property def invoke_identity_arn(self) -> str: """The ARN for the identity used to invoke the Lambda Function""" return self["invokeIdentityArn"] @property def kinesis(self) -> KinesisStreamRecordPayload: """Underlying Kinesis record associated with the event""" return KinesisStreamRecordPayload(self._data)`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop aws_region : str`
- 
## Expand source code`@property def aws_region(self) -> str: """AWS region where the event originated eg: us-east-1""" return self["awsRegion"]`AWS region where the event originated eg: us-east-1 
- `prop event_id : str`
- 
## Expand source code`@property def event_id(self) -> str: """A globally unique identifier for the event that was recorded in this stream record.""" return self["eventID"]`A globally unique identifier for the event that was recorded in this stream record. 
- `prop event_name : str`
- 
## Expand source code`@property def event_name(self) -> str: """Event type eg: aws:kinesis:record""" return self["eventName"]`Event type eg: aws:kinesis:record 
- `prop event_source : str`
- 
## Expand source code`@property def event_source(self) -> str: """The AWS service from which the Kinesis event originated. For Kinesis, this is aws:kinesis""" return self["eventSource"]`The AWS service from which the Kinesis event originated. For Kinesis, this is aws:kinesis 
- `prop event_source_arn : str`
- 
## Expand source code`@property def event_source_arn(self) -> str: """The Amazon Resource Name (ARN) of the event source""" return self["eventSourceARN"]`The Amazon Resource Name (ARN) of the event source 
- `prop event_version : str`
- 
## Expand source code`@property def event_version(self) -> str: """The eventVersion key value contains a major and minor version in the form <major>.<minor>.""" return self["eventVersion"]`The eventVersion key value contains a major and minor version in the form . . 
- `prop invoke_identity_arn : str`
- 
## Expand source code`@property def invoke_identity_arn(self) -> str: """The ARN for the identity used to invoke the Lambda Function""" return self["invokeIdentityArn"]`The ARN for the identity used to invoke the Lambda Function 
- `prop kinesis :`- [KinesisStreamRecordPayload](#aws_lambda_powertools.utilities.data_classes.kinesis_stream_event.KinesisStreamRecordPayload)
- 
## Expand source code`@property def kinesis(self) -> KinesisStreamRecordPayload: """Underlying Kinesis record associated with the event""" return KinesisStreamRecordPayload(self._data)`Underlying Kinesis record associated with the event 
 ### Inherited members
- `class KinesisStreamRecordPayload (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class KinesisStreamRecordPayload(DictWrapper): @property def approximate_arrival_timestamp(self) -> float: """The approximate time that the record was inserted into the stream""" return float(self["kinesis"]["approximateArrivalTimestamp"]) @property def data(self) -> str: """The data blob""" return self["kinesis"]["data"] @property def kinesis_schema_version(self) -> str: """Schema version for the record""" return self["kinesis"]["kinesisSchemaVersion"] @property def partition_key(self) -> str: """Identifies which shard in the stream the data record is assigned to""" return self["kinesis"]["partitionKey"] @property def sequence_number(self) -> str: """The unique identifier of the record within its shard""" return self["kinesis"]["sequenceNumber"] def data_as_bytes(self) -> bytes: """Decode binary encoded data as bytes""" return base64.b64decode(self.data) def data_as_text(self) -> str: """Decode binary encoded data as text""" return self.data_as_bytes().decode("utf-8") def data_as_json(self) -> dict: """Decode binary encoded data as json""" return json.loads(self.data_as_text()) def data_zlib_compressed_as_json(self) -> dict: """Decode binary encoded data as bytes""" decompressed = zlib.decompress(self.data_as_bytes(), zlib.MAX_WBITS | 32) return json.loads(decompressed)`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop approximate_arrival_timestamp : float`
- 
## Expand source code`@property def approximate_arrival_timestamp(self) -> float: """The approximate time that the record was inserted into the stream""" return float(self["kinesis"]["approximateArrivalTimestamp"])`The approximate time that the record was inserted into the stream 
- `prop data : str`
- 
## Expand source code`@property def data(self) -> str: """The data blob""" return self["kinesis"]["data"]`The data blob 
- `prop kinesis_schema_version : str`
- 
## Expand source code`@property def kinesis_schema_version(self) -> str: """Schema version for the record""" return self["kinesis"]["kinesisSchemaVersion"]`Schema version for the record 
- `prop partition_key : str`
- 
## Expand source code`@property def partition_key(self) -> str: """Identifies which shard in the stream the data record is assigned to""" return self["kinesis"]["partitionKey"]`Identifies which shard in the stream the data record is assigned to 
- `prop sequence_number : str`
- 
## Expand source code`@property def sequence_number(self) -> str: """The unique identifier of the record within its shard""" return self["kinesis"]["sequenceNumber"]`The unique identifier of the record within its shard 
 ### Methods- `def data_as_bytes(self) ‑> bytes`
- 
## Expand source code`def data_as_bytes(self) -> bytes: """Decode binary encoded data as bytes""" return base64.b64decode(self.data)`Decode binary encoded data as bytes 
- `def data_as_json(self) ‑> dict`
- 
## Expand source code`def data_as_json(self) -> dict: """Decode binary encoded data as json""" return json.loads(self.data_as_text())`Decode binary encoded data as json 
- `def data_as_text(self) ‑> str`
- 
## Expand source code`def data_as_text(self) -> str: """Decode binary encoded data as text""" return self.data_as_bytes().decode("utf-8")`Decode binary encoded data as text 
- `def data_zlib_compressed_as_json(self) ‑> dict`
- 
## Expand source code`def data_zlib_compressed_as_json(self) -> dict: """Decode binary encoded data as bytes""" decompressed = zlib.decompress(self.data_as_bytes(), zlib.MAX_WBITS | 32) return json.loads(decompressed)`Decode binary encoded data as bytes 
 ### Inherited members