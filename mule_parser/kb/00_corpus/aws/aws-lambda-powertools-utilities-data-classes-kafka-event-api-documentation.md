# aws_lambda_powertools.utilities.data_classes.kafka_event API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/kafka_event.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/kafka_event.html)

---

# Module `aws_lambda_powertools.utilities.data_classes.kafka_event`

## Classes

- `class KafkaEvent (data: dict[str, Any])`
- 
## Expand source code`class KafkaEvent(DictWrapper): """Self-managed or MSK Apache Kafka event trigger Documentation: -------------- - https://docs.aws.amazon.com/lambda/latest/dg/with-kafka.html - https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html """ def __init__(self, data: dict[str, Any]): super().__init__(data) self._records: Iterator[KafkaEventRecord] | None = None @property def event_source(self) -> str: """The AWS service from which the Kafka event record originated.""" return self["eventSource"] @property def event_source_arn(self) -> str | None: """The AWS service ARN from which the Kafka event record originated, mandatory for AWS MSK.""" return self.get("eventSourceArn") @property def bootstrap_servers(self) -> str: """The Kafka bootstrap URL.""" return self["bootstrapServers"] @property def decoded_bootstrap_servers(self) -> list[str]: """The decoded Kafka bootstrap URL.""" return self.bootstrap_servers.split(",") @property def records(self) -> Iterator[KafkaEventRecord]: """The Kafka records.""" for chunk in self["records"].values(): for record in chunk: yield KafkaEventRecord(data=record, json_deserializer=self._json_deserializer) @property def record(self) -> KafkaEventRecord: """ Returns the next Kafka record using an iterator. Returns ------- KafkaEventRecord The next Kafka record. Raises ------ StopIteration If there are no more records available. """ if self._records is None: self._records = self.records return next(self._records)`Self-managed or MSK Apache Kafka event trigger Documentation: 
 - [https://docs.aws.amazon.com/lambda/latest/dg/with-kafka.html](https://docs.aws.amazon.com/lambda/latest/dg/with-kafka.html)
- [https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html](https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html)
 ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop bootstrap_servers : str`
- 
## Expand source code`@property def bootstrap_servers(self) -> str: """The Kafka bootstrap URL.""" return self["bootstrapServers"]`The Kafka bootstrap URL. 
- `prop decoded_bootstrap_servers : list[str]`
- 
## Expand source code`@property def decoded_bootstrap_servers(self) -> list[str]: """The decoded Kafka bootstrap URL.""" return self.bootstrap_servers.split(",")`The decoded Kafka bootstrap URL. 
- `prop event_source : str`
- 
## Expand source code`@property def event_source(self) -> str: """The AWS service from which the Kafka event record originated.""" return self["eventSource"]`The AWS service from which the Kafka event record originated. 
- `prop event_source_arn : str | None`
- 
## Expand source code`@property def event_source_arn(self) -> str | None: """The AWS service ARN from which the Kafka event record originated, mandatory for AWS MSK.""" return self.get("eventSourceArn")`The AWS service ARN from which the Kafka event record originated, mandatory for AWS MSK. 
- `prop record :`- [KafkaEventRecord](#aws_lambda_powertools.utilities.data_classes.kafka_event.KafkaEventRecord)
- 
## Expand source code`@property def record(self) -> KafkaEventRecord: """ Returns the next Kafka record using an iterator. Returns ------- KafkaEventRecord The next Kafka record. Raises ------ StopIteration If there are no more records available. """ if self._records is None: self._records = self.records return next(self._records)`Returns the next Kafka record using an iterator. ## Returns- [KafkaEventRecord](#aws_lambda_powertools.utilities.data_classes.kafka_event.KafkaEventRecord)
- The next Kafka record.
 ## Raises- `StopIteration`
- If there are no more records available.
 
- `prop records : Iterator[`- [KafkaEventRecord](#aws_lambda_powertools.utilities.data_classes.kafka_event.KafkaEventRecord)]
- 
## Expand source code`@property def records(self) -> Iterator[KafkaEventRecord]: """The Kafka records.""" for chunk in self["records"].values(): for record in chunk: yield KafkaEventRecord(data=record, json_deserializer=self._json_deserializer)`The Kafka records. 
 ### Inherited members
- `class KafkaEventRecord (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class KafkaEventRecord(DictWrapper): @property def topic(self) -> str: """The Kafka topic.""" return self["topic"] @property def partition(self) -> int: """The Kafka record parition.""" return self["partition"] @property def offset(self) -> int: """The Kafka record offset.""" return self["offset"] @property def timestamp(self) -> int: """The Kafka record timestamp.""" return self["timestamp"] @property def timestamp_type(self) -> str: """The Kafka record timestamp type.""" return self["timestampType"] @property def key(self) -> str: """The raw (base64 encoded) Kafka record key.""" return self["key"] @property def decoded_key(self) -> bytes: """Decode the base64 encoded key as bytes.""" return base64.b64decode(self.key) @property def value(self) -> str: """The raw (base64 encoded) Kafka record value.""" return self["value"] @property def decoded_value(self) -> bytes: """Decodes the base64 encoded value as bytes.""" return base64.b64decode(self.value) @cached_property def json_value(self) -> Any: """Decodes the text encoded data as JSON.""" return self._json_deserializer(self.decoded_value.decode("utf-8")) @property def headers(self) -> list[dict[str, list[int]]]: """The raw Kafka record headers.""" return self["headers"] @cached_property def decoded_headers(self) -> dict[str, bytes]: """Decodes the headers as a single dictionary.""" return CaseInsensitiveDict((k, bytes(v)) for chunk in self.headers for k, v in chunk.items())`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `var decoded_headers : dict[str, bytes]`
- 
## Expand source code`@cached_property def decoded_headers(self) -> dict[str, bytes]: """Decodes the headers as a single dictionary.""" return CaseInsensitiveDict((k, bytes(v)) for chunk in self.headers for k, v in chunk.items())`Decodes the headers as a single dictionary. 
- `prop decoded_key : bytes`
- 
## Expand source code`@property def decoded_key(self) -> bytes: """Decode the base64 encoded key as bytes.""" return base64.b64decode(self.key)`Decode the base64 encoded key as bytes. 
- `prop decoded_value : bytes`
- 
## Expand source code`@property def decoded_value(self) -> bytes: """Decodes the base64 encoded value as bytes.""" return base64.b64decode(self.value)`Decodes the base64 encoded value as bytes. 
- `prop headers : list[dict[str, list[int]]]`
- 
## Expand source code`@property def headers(self) -> list[dict[str, list[int]]]: """The raw Kafka record headers.""" return self["headers"]`The raw Kafka record headers. 
- `var json_value : Any`
- 
## Expand source code`@cached_property def json_value(self) -> Any: """Decodes the text encoded data as JSON.""" return self._json_deserializer(self.decoded_value.decode("utf-8"))`Decodes the text encoded data as JSON. 
- `prop key : str`
- 
## Expand source code`@property def key(self) -> str: """The raw (base64 encoded) Kafka record key.""" return self["key"]`The raw (base64 encoded) Kafka record key. 
- `prop offset : int`
- 
## Expand source code`@property def offset(self) -> int: """The Kafka record offset.""" return self["offset"]`The Kafka record offset. 
- `prop partition : int`
- 
## Expand source code`@property def partition(self) -> int: """The Kafka record parition.""" return self["partition"]`The Kafka record parition. 
- `prop timestamp : int`
- 
## Expand source code`@property def timestamp(self) -> int: """The Kafka record timestamp.""" return self["timestamp"]`The Kafka record timestamp. 
- `prop timestamp_type : str`
- 
## Expand source code`@property def timestamp_type(self) -> str: """The Kafka record timestamp type.""" return self["timestampType"]`The Kafka record timestamp type. 
- `prop topic : str`
- 
## Expand source code`@property def topic(self) -> str: """The Kafka topic.""" return self["topic"]`The Kafka topic. 
- `prop value : str`
- 
## Expand source code`@property def value(self) -> str: """The raw (base64 encoded) Kafka record value.""" return self["value"]`The raw (base64 encoded) Kafka record value. 
 ### Inherited members