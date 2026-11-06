# aws_lambda_powertools.utilities.data_classes.active_mq_event API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/active_mq_event.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/active_mq_event.html)

---

# Module `aws_lambda_powertools.utilities.data_classes.active_mq_event`

## Classes

- `class ActiveMQEvent (data: dict[str, Any])`
- 
## Expand source code`class ActiveMQEvent(DictWrapper): """Represents an Active MQ event sent to Lambda Documentation: -------------- - https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html - https://aws.amazon.com/blogs/compute/using-amazon-mq-as-an-event-source-for-aws-lambda/ """ def __init__(self, data: dict[str, Any]): super().__init__(data) self._messages: Iterator[ActiveMQMessage] | None = None @property def event_source(self) -> str: return self["eventSource"] @property def event_source_arn(self) -> str: """The Amazon Resource Name (ARN) of the event source""" return self["eventSourceArn"] @property def messages(self) -> Iterator[ActiveMQMessage]: for record in self["messages"]: yield ActiveMQMessage(record, json_deserializer=self._json_deserializer) @property def message(self) -> ActiveMQMessage: """ Returns the next ActiveMQ message using an iterator Returns ------- ActiveMQMessage The next activemq message. Raises ------ StopIteration If there are no more records available. """ if self._messages is None: self._messages = self.messages return next(self._messages)`Represents an Active MQ event sent to Lambda ## Documentation:- [https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html](https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html)
- [https://aws.amazon.com/blogs/compute/using-amazon-mq-as-an-event-source-for-aws-lambda/](https://aws.amazon.com/blogs/compute/using-amazon-mq-as-an-event-source-for-aws-lambda/)
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
- `prop message :`- [ActiveMQMessage](#aws_lambda_powertools.utilities.data_classes.active_mq_event.ActiveMQMessage)
- 
## Expand source code`@property def message(self) -> ActiveMQMessage: """ Returns the next ActiveMQ message using an iterator Returns ------- ActiveMQMessage The next activemq message. Raises ------ StopIteration If there are no more records available. """ if self._messages is None: self._messages = self.messages return next(self._messages)`Returns the next ActiveMQ message using an iterator ## Returns- [ActiveMQMessage](#aws_lambda_powertools.utilities.data_classes.active_mq_event.ActiveMQMessage)
- The next activemq message.
 ## Raises- `StopIteration`
- If there are no more records available.
 
- `prop messages : Iterator[`- [ActiveMQMessage](#aws_lambda_powertools.utilities.data_classes.active_mq_event.ActiveMQMessage)]
- 
## Expand source code`@property def messages(self) -> Iterator[ActiveMQMessage]: for record in self["messages"]: yield ActiveMQMessage(record, json_deserializer=self._json_deserializer)`
 ### Inherited members
- `class ActiveMQMessage (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class ActiveMQMessage(DictWrapper): @property def message_id(self) -> str: """Unique identifier for the message""" return self["messageID"] @property def message_type(self) -> str: return self["messageType"] @property def data(self) -> str: return self["data"] @property def decoded_data(self) -> str: """Decodes the data as a str""" return base64_decode(self.data) @cached_property def json_data(self) -> Any: return self._json_deserializer(self.decoded_data) @property def connection_id(self) -> str: return self["connectionId"] @property def redelivered(self) -> bool: """true if the message is being resent to the consumer""" return self["redelivered"] @property def timestamp(self) -> int: """Time in milliseconds.""" return self["timestamp"] @property def broker_in_time(self) -> int: """Time stamp (in milliseconds) for when the message arrived at the broker.""" return self["brokerInTime"] @property def broker_out_time(self) -> int: """Time stamp (in milliseconds) for when the message left the broker.""" return self["brokerOutTime"] @property def properties(self) -> dict: """Custom properties""" return self["properties"] @property def destination_physicalname(self) -> str: return self["destination"]["physicalName"] @property def delivery_mode(self) -> int | None: """persistent or non-persistent delivery""" return self.get("deliveryMode") @property def correlation_id(self) -> str | None: """User defined correlation id""" return self.get("correlationID") @property def reply_to(self) -> str | None: """User defined reply to""" return self.get("replyTo") @property def get_type(self) -> str | None: """User defined message type""" return self.get("type") @property def expiration(self) -> int | None: """Expiration attribute whose value is given in milliseconds""" return self.get("expiration") @property def priority(self) -> int | None: """ JMS defines a ten-level priority value, with 0 as the lowest priority and 9 as the highest. In addition, clients should consider priorities 0-4 as gradations of normal priority and priorities 5-9 as gradations of expedited priority. JMS does not require that a provider strictly implement priority ordering of messages; however, it should do its best to deliver expedited messages ahead of normal messages. """ return self.get("priority")`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop broker_in_time : int`
- 
## Expand source code`@property def broker_in_time(self) -> int: """Time stamp (in milliseconds) for when the message arrived at the broker.""" return self["brokerInTime"]`Time stamp (in milliseconds) for when the message arrived at the broker. 
- `prop broker_out_time : int`
- 
## Expand source code`@property def broker_out_time(self) -> int: """Time stamp (in milliseconds) for when the message left the broker.""" return self["brokerOutTime"]`Time stamp (in milliseconds) for when the message left the broker. 
- `prop connection_id : str`
- 
## Expand source code`@property def connection_id(self) -> str: return self["connectionId"]`
- `prop correlation_id : str | None`
- 
## Expand source code`@property def correlation_id(self) -> str | None: """User defined correlation id""" return self.get("correlationID")`User defined correlation id 
- `prop data : str`
- 
## Expand source code`@property def data(self) -> str: return self["data"]`
- `prop decoded_data : str`
- 
## Expand source code`@property def decoded_data(self) -> str: """Decodes the data as a str""" return base64_decode(self.data)`Decodes the data as a str 
- `prop delivery_mode : int | None`
- 
## Expand source code`@property def delivery_mode(self) -> int | None: """persistent or non-persistent delivery""" return self.get("deliveryMode")`persistent or non-persistent delivery 
- `prop destination_physicalname : str`
- 
## Expand source code`@property def destination_physicalname(self) -> str: return self["destination"]["physicalName"]`
- `prop expiration : int | None`
- 
## Expand source code`@property def expiration(self) -> int | None: """Expiration attribute whose value is given in milliseconds""" return self.get("expiration")`Expiration attribute whose value is given in milliseconds 
- `prop get_type : str | None`
- 
## Expand source code`@property def get_type(self) -> str | None: """User defined message type""" return self.get("type")`User defined message type 
- `var json_data : Any`
- 
## Expand source code`@cached_property def json_data(self) -> Any: return self._json_deserializer(self.decoded_data)`
- `prop message_id : str`
- 
## Expand source code`@property def message_id(self) -> str: """Unique identifier for the message""" return self["messageID"]`Unique identifier for the message 
- `prop message_type : str`
- 
## Expand source code`@property def message_type(self) -> str: return self["messageType"]`
- `prop priority : int | None`
- 
## Expand source code`@property def priority(self) -> int | None: """ JMS defines a ten-level priority value, with 0 as the lowest priority and 9 as the highest. In addition, clients should consider priorities 0-4 as gradations of normal priority and priorities 5-9 as gradations of expedited priority. JMS does not require that a provider strictly implement priority ordering of messages; however, it should do its best to deliver expedited messages ahead of normal messages. """ return self.get("priority")`JMS defines a ten-level priority value, with 0 as the lowest priority and 9 as the highest. In addition, clients should consider priorities 0-4 as gradations of normal priority and priorities 5-9 as gradations of expedited priority. JMS does not require that a provider strictly implement priority ordering of messages; however, it should do its best to deliver expedited messages ahead of normal messages. 
- `prop properties : dict`
- 
## Expand source code`@property def properties(self) -> dict: """Custom properties""" return self["properties"]`Custom properties 
- `prop redelivered : bool`
- 
## Expand source code`@property def redelivered(self) -> bool: """true if the message is being resent to the consumer""" return self["redelivered"]`true if the message is being resent to the consumer 
- `prop reply_to : str | None`
- 
## Expand source code`@property def reply_to(self) -> str | None: """User defined reply to""" return self.get("replyTo")`User defined reply to 
- `prop timestamp : int`
- 
## Expand source code`@property def timestamp(self) -> int: """Time in milliseconds.""" return self["timestamp"]`Time in milliseconds. 
 ### Inherited members