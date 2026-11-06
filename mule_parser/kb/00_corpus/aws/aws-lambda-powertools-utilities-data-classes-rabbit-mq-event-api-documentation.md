# aws_lambda_powertools.utilities.data_classes.rabbit_mq_event API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/rabbit_mq_event.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/rabbit_mq_event.html)

---

# Module `aws_lambda_powertools.utilities.data_classes.rabbit_mq_event`

## Classes

- `class BasicProperties (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class BasicProperties(DictWrapper): @property def content_type(self) -> str: return self["contentType"] @property def content_encoding(self) -> str: return self["contentEncoding"] @property def headers(self) -> dict[str, Any]: return self["headers"] @property def delivery_mode(self) -> int: return self["deliveryMode"] @property def priority(self) -> int: return self["priority"] @property def correlation_id(self) -> str: return self["correlationId"] @property def reply_to(self) -> str: return self["replyTo"] @property def expiration(self) -> str: return self["expiration"] @property def message_id(self) -> str: return self["messageId"] @property def timestamp(self) -> str: return self["timestamp"] @property def get_type(self) -> str: return self["type"] @property def user_id(self) -> str: return self["userId"] @property def app_id(self) -> str: return self["appId"] @property def cluster_id(self) -> str: return self["clusterId"] @property def body_size(self) -> int: return self["bodySize"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop app_id : str`
- 
## Expand source code`@property def app_id(self) -> str: return self["appId"]`
- `prop body_size : int`
- 
## Expand source code`@property def body_size(self) -> int: return self["bodySize"]`
- `prop cluster_id : str`
- 
## Expand source code`@property def cluster_id(self) -> str: return self["clusterId"]`
- `prop content_encoding : str`
- 
## Expand source code`@property def content_encoding(self) -> str: return self["contentEncoding"]`
- `prop content_type : str`
- 
## Expand source code`@property def content_type(self) -> str: return self["contentType"]`
- `prop correlation_id : str`
- 
## Expand source code`@property def correlation_id(self) -> str: return self["correlationId"]`
- `prop delivery_mode : int`
- 
## Expand source code`@property def delivery_mode(self) -> int: return self["deliveryMode"]`
- `prop expiration : str`
- 
## Expand source code`@property def expiration(self) -> str: return self["expiration"]`
- `prop get_type : str`
- 
## Expand source code`@property def get_type(self) -> str: return self["type"]`
- `prop headers : dict[str, Any]`
- 
## Expand source code`@property def headers(self) -> dict[str, Any]: return self["headers"]`
- `prop message_id : str`
- 
## Expand source code`@property def message_id(self) -> str: return self["messageId"]`
- `prop priority : int`
- 
## Expand source code`@property def priority(self) -> int: return self["priority"]`
- `prop reply_to : str`
- 
## Expand source code`@property def reply_to(self) -> str: return self["replyTo"]`
- `prop timestamp : str`
- 
## Expand source code`@property def timestamp(self) -> str: return self["timestamp"]`
- `prop user_id : str`
- 
## Expand source code`@property def user_id(self) -> str: return self["userId"]`
 ### Inherited members
- `class RabbitMQEvent (data: dict[str, Any])`
- 
## Expand source code`class RabbitMQEvent(DictWrapper): """Represents a Rabbit MQ event sent to Lambda Documentation: -------------- - https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html - https://aws.amazon.com/blogs/compute/using-amazon-mq-for-rabbitmq-as-an-event-source-for-lambda/ """ def __init__(self, data: dict[str, Any]): super().__init__(data) self._rmq_messages_by_queue = { key: [RabbitMessage(message) for message in messages] for key, messages in self["rmqMessagesByQueue"].items() } @property def event_source(self) -> str: return self["eventSource"] @property def event_source_arn(self) -> str: """The Amazon Resource Name (ARN) of the event source""" return self["eventSourceArn"] @property def rmq_messages_by_queue(self) -> dict[str, list[RabbitMessage]]: return self._rmq_messages_by_queue`Represents a Rabbit MQ event sent to Lambda ## Documentation:- [https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html](https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html)
- [https://aws.amazon.com/blogs/compute/using-amazon-mq-for-rabbitmq-as-an-event-source-for-lambda/](https://aws.amazon.com/blogs/compute/using-amazon-mq-for-rabbitmq-as-an-event-source-for-lambda/)
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
 ### Instance variables- `prop event_source : str`
- 
## Expand source code`@property def event_source(self) -> str: return self["eventSource"]`
- `prop event_source_arn : str`
- 
## Expand source code`@property def event_source_arn(self) -> str: """The Amazon Resource Name (ARN) of the event source""" return self["eventSourceArn"]`The Amazon Resource Name (ARN) of the event source 
- `prop rmq_messages_by_queue : dict[str, list[`- [RabbitMessage](#aws_lambda_powertools.utilities.data_classes.rabbit_mq_event.RabbitMessage)]]
- 
## Expand source code`@property def rmq_messages_by_queue(self) -> dict[str, list[RabbitMessage]]: return self._rmq_messages_by_queue`
 ### Inherited members
- `class RabbitMessage (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class RabbitMessage(DictWrapper): @property def basic_properties(self) -> BasicProperties: return BasicProperties(self["basicProperties"]) @property def redelivered(self) -> bool: return self["redelivered"] @property def data(self) -> str: return self["data"] @property def decoded_data(self) -> str: """Decodes the data as a str""" return base64_decode(self.data) @cached_property def json_data(self) -> Any: """Parses the data as json""" return self._json_deserializer(self.decoded_data)`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop basic_properties :`- [BasicProperties](#aws_lambda_powertools.utilities.data_classes.rabbit_mq_event.BasicProperties)
- 
## Expand source code`@property def basic_properties(self) -> BasicProperties: return BasicProperties(self["basicProperties"])`
- `prop data : str`
- 
## Expand source code`@property def data(self) -> str: return self["data"]`
- `prop decoded_data : str`
- 
## Expand source code`@property def decoded_data(self) -> str: """Decodes the data as a str""" return base64_decode(self.data)`Decodes the data as a str 
- `var json_data : Any`
- 
## Expand source code`@cached_property def json_data(self) -> Any: """Parses the data as json""" return self._json_deserializer(self.decoded_data)`Parses the data as json 
- `prop redelivered : bool`
- 
## Expand source code`@property def redelivered(self) -> bool: return self["redelivered"]`
 ### Inherited members