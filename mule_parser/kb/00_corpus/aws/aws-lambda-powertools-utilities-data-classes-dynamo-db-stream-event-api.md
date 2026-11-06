# aws_lambda_powertools.utilities.data_classes.dynamo_db_stream_event API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/dynamo_db_stream_event.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/dynamo_db_stream_event.html)

---

# Module `aws_lambda_powertools.utilities.data_classes.dynamo_db_stream_event`

## Classes

- `class DynamoDBRecord (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class DynamoDBRecord(DictWrapper): """A description of a unique event within a stream""" @property def aws_region(self) -> str | None: """The region in which the GetRecords request was received""" return self.get("awsRegion") @property def dynamodb(self) -> StreamRecord | None: """The main body of the stream record, containing all the DynamoDB-specific dicts.""" stream_record = self.get("dynamodb") return None if stream_record is None else StreamRecord(stream_record) @property def event_id(self) -> str | None: """A globally unique identifier for the event that was recorded in this stream record.""" return self.get("eventID") @property def event_name(self) -> DynamoDBRecordEventName | None: """The type of data modification that was performed on the DynamoDB table""" item = self.get("eventName") return None if item is None else DynamoDBRecordEventName[item] @property def event_source(self) -> str | None: """The AWS service from which the stream record originated. For DynamoDB Streams, this is aws:dynamodb.""" return self.get("eventSource") @property def event_source_arn(self) -> str | None: """The Amazon Resource Name (ARN) of the event source""" return self.get("eventSourceARN") @property def event_version(self) -> str | None: """The version number of the stream record format.""" return self.get("eventVersion") @property def user_identity(self) -> dict: """Contains details about the type of identity that made the request""" return self.get("userIdentity") or {}`A description of a unique event within a stream ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop aws_region : str | None`
- 
## Expand source code`@property def aws_region(self) -> str | None: """The region in which the GetRecords request was received""" return self.get("awsRegion")`The region in which the GetRecords request was received 
- `prop dynamodb :`- [StreamRecord](#aws_lambda_powertools.utilities.data_classes.dynamo_db_stream_event.StreamRecord)| None
- 
## Expand source code`@property def dynamodb(self) -> StreamRecord | None: """The main body of the stream record, containing all the DynamoDB-specific dicts.""" stream_record = self.get("dynamodb") return None if stream_record is None else StreamRecord(stream_record)`The main body of the stream record, containing all the DynamoDB-specific dicts. 
- `prop event_id : str | None`
- 
## Expand source code`@property def event_id(self) -> str | None: """A globally unique identifier for the event that was recorded in this stream record.""" return self.get("eventID")`A globally unique identifier for the event that was recorded in this stream record. 
- `prop event_name :`- [DynamoDBRecordEventName](#aws_lambda_powertools.utilities.data_classes.dynamo_db_stream_event.DynamoDBRecordEventName)| None
- 
## Expand source code`@property def event_name(self) -> DynamoDBRecordEventName | None: """The type of data modification that was performed on the DynamoDB table""" item = self.get("eventName") return None if item is None else DynamoDBRecordEventName[item]`The type of data modification that was performed on the DynamoDB table 
- `prop event_source : str | None`
- 
## Expand source code`@property def event_source(self) -> str | None: """The AWS service from which the stream record originated. For DynamoDB Streams, this is aws:dynamodb.""" return self.get("eventSource")`The AWS service from which the stream record originated. For DynamoDB Streams, this is aws:dynamodb. 
- `prop event_source_arn : str | None`
- 
## Expand source code`@property def event_source_arn(self) -> str | None: """The Amazon Resource Name (ARN) of the event source""" return self.get("eventSourceARN")`The Amazon Resource Name (ARN) of the event source 
- `prop event_version : str | None`
- 
## Expand source code`@property def event_version(self) -> str | None: """The version number of the stream record format.""" return self.get("eventVersion")`The version number of the stream record format. 
- `prop user_identity : dict`
- 
## Expand source code`@property def user_identity(self) -> dict: """Contains details about the type of identity that made the request""" return self.get("userIdentity") or {}`Contains details about the type of identity that made the request 
 ### Inherited members
- `class DynamoDBRecordEventName (*args, **kwds)`
- 
## Expand source code`class DynamoDBRecordEventName(Enum): INSERT = 0 # a new item was added to the table MODIFY = 1 # one or more of an existing item's attributes were modified REMOVE = 2 # the item was deleted from the table`Create a collection of name/value pairs. Example enumeration: `>>> class Color(Enum): ... RED = 1 ... BLUE = 2 ... GREEN = 3`Access them by: - attribute access:
 Color.RED - value lookup:
 Color(1) - name lookup:
 Color['RED'] Enumerations can be iterated over, and know how many members they have: `>>> len(Color) 3``>>> list(Color) [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]`Methods can be added to enumerations, and members can have their own attributes – see the documentation for details. ### Ancestors- enum.Enum
 ### Class variables- `var INSERT`
- `var MODIFY`
- `var REMOVE`
 
- `class DynamoDBStreamEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class DynamoDBStreamEvent(DictWrapper): """Dynamo DB Stream Event Documentation: ------------- - https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html Example ------- **Process dynamodb stream events. DynamoDB types are automatically converted to their equivalent Python values.** from aws_lambda_powertools.utilities.data_classes import event_source, DynamoDBStreamEvent from aws_lambda_powertools.utilities.typing import LambdaContext @event_source(data_class=DynamoDBStreamEvent) def lambda_handler(event: DynamoDBStreamEvent, context: LambdaContext): for record in event.records: # {"N": "123.45"} => Decimal("123.45") key: str = record.dynamodb.keys["id"] print(key) """ @property def records(self) -> Iterator[DynamoDBRecord]: for record in self["Records"]: yield DynamoDBRecord(record)`Dynamo DB Stream Event ## Documentation:## Example**Process dynamodb stream events. DynamoDB types are automatically converted to their equivalent Python values.**`from aws_lambda_powertools.utilities.data_classes import event_source, DynamoDBStreamEvent from aws_lambda_powertools.utilities.typing import LambdaContext @event_source(data_class=DynamoDBStreamEvent) def lambda_handler(event: DynamoDBStreamEvent, context: LambdaContext): for record in event.records: # {"N": "123.45"} => Decimal("123.45") key: str = record.dynamodb.keys["id"] print(key)`## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop records : Iterator[`- [DynamoDBRecord](#aws_lambda_powertools.utilities.data_classes.dynamo_db_stream_event.DynamoDBRecord)]
- 
## Expand source code`@property def records(self) -> Iterator[DynamoDBRecord]: for record in self["Records"]: yield DynamoDBRecord(record)`
 ### Inherited members
- `class StreamRecord (data: dict[str, Any])`
- 
## Expand source code`class StreamRecord(DictWrapper): _deserializer = TypeDeserializer() def __init__(self, data: dict[str, Any]): """StreamRecord constructor Parameters ---------- data: dict[str, Any] Represents the dynamodb dict inside DynamoDBStreamEvent's records """ super().__init__(data) self._deserializer = TypeDeserializer() def _deserialize_dynamodb_dict(self, key: str) -> dict[str, Any]: """Deserialize DynamoDB records available in `Keys`, `NewImage`, and `OldImage` Parameters ---------- key : str DynamoDB key (e.g., Keys, NewImage, or OldImage) Returns ------- dict[str, Any] Deserialized records in Python native types """ dynamodb_dict = self._data.get(key) or {} return {k: self._deserializer.deserialize(v) for k, v in dynamodb_dict.items()} @property def approximate_creation_date_time(self) -> int | None: """The approximate date and time when the stream record was created, in UNIX epoch time format.""" item = self.get("ApproximateCreationDateTime") return None if item is None else int(item) @cached_property def keys(self) -> dict[str, Any]: # type: ignore[override] """The primary key attribute(s) for the DynamoDB item that was modified.""" return self._deserialize_dynamodb_dict("Keys") @cached_property def new_image(self) -> dict[str, Any]: """The item in the DynamoDB table as it appeared after it was modified.""" return self._deserialize_dynamodb_dict("NewImage") @cached_property def old_image(self) -> dict[str, Any]: """The item in the DynamoDB table as it appeared before it was modified.""" return self._deserialize_dynamodb_dict("OldImage") @property def sequence_number(self) -> str | None: """The sequence number of the stream record.""" return self.get("SequenceNumber") @property def size_bytes(self) -> int | None: """The size of the stream record, in bytes.""" item = self.get("SizeBytes") return None if item is None else int(item) @property def stream_view_type(self) -> StreamViewType | None: """The type of data from the modified DynamoDB item that was captured in this stream record""" item = self.get("StreamViewType") return None if item is None else StreamViewType[str(item)]`Provides a single read only access to a wrapper dict StreamRecord constructor Parameters 
 - `data`- `dict[str, Any]`
- Represents the dynamodb dict inside DynamoDBStreamEvent's records
 ### Ancestors- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- `prop approximate_creation_date_time : int | None`
- 
## Expand source code`@property def approximate_creation_date_time(self) -> int | None: """The approximate date and time when the stream record was created, in UNIX epoch time format.""" item = self.get("ApproximateCreationDateTime") return None if item is None else int(item)`The approximate date and time when the stream record was created, in UNIX epoch time format. 
- `var keys : dict[str, Any]`
- 
## Expand source code`@cached_property def keys(self) -> dict[str, Any]: # type: ignore[override] """The primary key attribute(s) for the DynamoDB item that was modified.""" return self._deserialize_dynamodb_dict("Keys")`The primary key attribute(s) for the DynamoDB item that was modified. 
- `var new_image : dict[str, Any]`
- 
## Expand source code`@cached_property def new_image(self) -> dict[str, Any]: """The item in the DynamoDB table as it appeared after it was modified.""" return self._deserialize_dynamodb_dict("NewImage")`The item in the DynamoDB table as it appeared after it was modified. 
- `var old_image : dict[str, Any]`
- 
## Expand source code`@cached_property def old_image(self) -> dict[str, Any]: """The item in the DynamoDB table as it appeared before it was modified.""" return self._deserialize_dynamodb_dict("OldImage")`The item in the DynamoDB table as it appeared before it was modified. 
- `prop sequence_number : str | None`
- 
## Expand source code`@property def sequence_number(self) -> str | None: """The sequence number of the stream record.""" return self.get("SequenceNumber")`The sequence number of the stream record. 
- `prop size_bytes : int | None`
- 
## Expand source code`@property def size_bytes(self) -> int | None: """The size of the stream record, in bytes.""" item = self.get("SizeBytes") return None if item is None else int(item)`The size of the stream record, in bytes. 
- `prop stream_view_type :`- [StreamViewType](#aws_lambda_powertools.utilities.data_classes.dynamo_db_stream_event.StreamViewType)| None
- 
## Expand source code`@property def stream_view_type(self) -> StreamViewType | None: """The type of data from the modified DynamoDB item that was captured in this stream record""" item = self.get("StreamViewType") return None if item is None else StreamViewType[str(item)]`The type of data from the modified DynamoDB item that was captured in this stream record 
 ### Inherited members
- `class StreamViewType (*args, **kwds)`
- 
## Expand source code`class StreamViewType(Enum): """The type of data from the modified DynamoDB item that was captured in this stream record""" KEYS_ONLY = 0 # only the key attributes of the modified item NEW_IMAGE = 1 # the entire item, as it appeared after it was modified. OLD_IMAGE = 2 # the entire item, as it appeared before it was modified. NEW_AND_OLD_IMAGES = 3 # both the new and the old item images of the item.`The type of data from the modified DynamoDB item that was captured in this stream record ### Ancestors- enum.Enum
 ### Class variables- `var KEYS_ONLY`
- `var NEW_AND_OLD_IMAGES`
- `var NEW_IMAGE`
- `var OLD_IMAGE`