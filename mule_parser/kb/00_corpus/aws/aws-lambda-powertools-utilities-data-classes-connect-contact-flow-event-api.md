# aws_lambda_powertools.utilities.data_classes.connect_contact_flow_event API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/connect_contact_flow_event.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/connect_contact_flow_event.html)

---

# Module `aws_lambda_powertools.utilities.data_classes.connect_contact_flow_event`

## Classes

- `class ConnectContactFlowChannel (*args, **kwds)`
- 
## Expand source code`class ConnectContactFlowChannel(Enum): VOICE = auto() CHAT = auto()`Create a collection of name/value pairs. Example enumeration: `>>> class Color(Enum): ... RED = 1 ... BLUE = 2 ... GREEN = 3`Access them by: - attribute access:
 Color.RED - value lookup:
 Color(1) - name lookup:
 Color['RED'] Enumerations can be iterated over, and know how many members they have: `>>> len(Color) 3``>>> list(Color) [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]`Methods can be added to enumerations, and members can have their own attributes – see the documentation for details. ### Ancestors- enum.Enum
 ### Class variables- `var CHAT`
- `var VOICE`
 
- `class ConnectContactFlowData (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class ConnectContactFlowData(DictWrapper): @property def attributes(self) -> dict[str, str]: """These are attributes that have been previously associated with a contact, such as when using a Set contact attributes block in a contact flow. This map may be empty if there aren't any saved attributes. """ return self["Attributes"] @property def channel(self) -> ConnectContactFlowChannel: """The method used to contact your contact center.""" return ConnectContactFlowChannel[self["Channel"]] @property def contact_id(self) -> str: """The unique identifier of the contact.""" return self["ContactId"] @property def customer_endpoint(self) -> ConnectContactFlowEndpoint | None: """Contains the customer’s address (number) and type of address.""" if self["CustomerEndpoint"] is not None: return ConnectContactFlowEndpoint(self["CustomerEndpoint"]) return None @property def initial_contact_id(self) -> str: """The unique identifier for the contact associated with the first interaction between the customer and your contact center. Use the initial contact ID to track contacts between contact flows. """ return self["InitialContactId"] @property def initiation_method(self) -> ConnectContactFlowInitiationMethod: """How the contact was initiated.""" return ConnectContactFlowInitiationMethod[self["InitiationMethod"]] @property def instance_arn(self) -> str: """The ARN for your Amazon Connect instance.""" return self["InstanceARN"] @property def previous_contact_id(self) -> str: """The unique identifier for the contact before it was transferred. Use the previous contact ID to trace contacts between contact flows. """ return self["PreviousContactId"] @property def queue(self) -> ConnectContactFlowQueue | None: """The current queue.""" if self["Queue"] is not None: return ConnectContactFlowQueue(self["Queue"]) return None @property def system_endpoint(self) -> ConnectContactFlowEndpoint | None: """Contains the address (number) the customer dialed to call your contact center and type of address.""" if self["SystemEndpoint"] is not None: return ConnectContactFlowEndpoint(self["SystemEndpoint"]) return None @property def media_streams(self) -> ConnectContactFlowMediaStreams: return ConnectContactFlowMediaStreams(self["MediaStreams"])`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop attributes : dict[str, str]`
- 
## Expand source code`@property def attributes(self) -> dict[str, str]: """These are attributes that have been previously associated with a contact, such as when using a Set contact attributes block in a contact flow. This map may be empty if there aren't any saved attributes. """ return self["Attributes"]`These are attributes that have been previously associated with a contact, such as when using a Set contact attributes block in a contact flow. This map may be empty if there aren't any saved attributes. 
- `prop channel :`- [ConnectContactFlowChannel](#aws_lambda_powertools.utilities.data_classes.connect_contact_flow_event.ConnectContactFlowChannel)
- 
## Expand source code`@property def channel(self) -> ConnectContactFlowChannel: """The method used to contact your contact center.""" return ConnectContactFlowChannel[self["Channel"]]`The method used to contact your contact center. 
- `prop contact_id : str`
- 
## Expand source code`@property def contact_id(self) -> str: """The unique identifier of the contact.""" return self["ContactId"]`The unique identifier of the contact. 
- `prop customer_endpoint :`- [ConnectContactFlowEndpoint](#aws_lambda_powertools.utilities.data_classes.connect_contact_flow_event.ConnectContactFlowEndpoint)| None
- 
## Expand source code`@property def customer_endpoint(self) -> ConnectContactFlowEndpoint | None: """Contains the customer’s address (number) and type of address.""" if self["CustomerEndpoint"] is not None: return ConnectContactFlowEndpoint(self["CustomerEndpoint"]) return None`Contains the customer’s address (number) and type of address. 
- `prop initial_contact_id : str`
- 
## Expand source code`@property def initial_contact_id(self) -> str: """The unique identifier for the contact associated with the first interaction between the customer and your contact center. Use the initial contact ID to track contacts between contact flows. """ return self["InitialContactId"]`The unique identifier for the contact associated with the first interaction between the customer and your contact center. Use the initial contact ID to track contacts between contact flows. 
- `prop initiation_method :`- [ConnectContactFlowInitiationMethod](#aws_lambda_powertools.utilities.data_classes.connect_contact_flow_event.ConnectContactFlowInitiationMethod)
- 
## Expand source code`@property def initiation_method(self) -> ConnectContactFlowInitiationMethod: """How the contact was initiated.""" return ConnectContactFlowInitiationMethod[self["InitiationMethod"]]`How the contact was initiated. 
- `prop instance_arn : str`
- 
## Expand source code`@property def instance_arn(self) -> str: """The ARN for your Amazon Connect instance.""" return self["InstanceARN"]`The ARN for your Amazon Connect instance. 
- `prop media_streams :`- [ConnectContactFlowMediaStreams](#aws_lambda_powertools.utilities.data_classes.connect_contact_flow_event.ConnectContactFlowMediaStreams)
- 
## Expand source code`@property def media_streams(self) -> ConnectContactFlowMediaStreams: return ConnectContactFlowMediaStreams(self["MediaStreams"])`
- `prop previous_contact_id : str`
- 
## Expand source code`@property def previous_contact_id(self) -> str: """The unique identifier for the contact before it was transferred. Use the previous contact ID to trace contacts between contact flows. """ return self["PreviousContactId"]`The unique identifier for the contact before it was transferred. Use the previous contact ID to trace contacts between contact flows. 
- `prop queue :`- [ConnectContactFlowQueue](#aws_lambda_powertools.utilities.data_classes.connect_contact_flow_event.ConnectContactFlowQueue)| None
- 
## Expand source code`@property def queue(self) -> ConnectContactFlowQueue | None: """The current queue.""" if self["Queue"] is not None: return ConnectContactFlowQueue(self["Queue"]) return None`The current queue. 
- `prop system_endpoint :`- [ConnectContactFlowEndpoint](#aws_lambda_powertools.utilities.data_classes.connect_contact_flow_event.ConnectContactFlowEndpoint)| None
- 
## Expand source code`@property def system_endpoint(self) -> ConnectContactFlowEndpoint | None: """Contains the address (number) the customer dialed to call your contact center and type of address.""" if self["SystemEndpoint"] is not None: return ConnectContactFlowEndpoint(self["SystemEndpoint"]) return None`Contains the address (number) the customer dialed to call your contact center and type of address. 
 ### Inherited members
- `class ConnectContactFlowEndpoint (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class ConnectContactFlowEndpoint(DictWrapper): @property def address(self) -> str: """The phone number.""" return self["Address"] @property def endpoint_type(self) -> ConnectContactFlowEndpointType: """The endpoint type.""" return ConnectContactFlowEndpointType[self["Type"]]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop address : str`
- 
## Expand source code`@property def address(self) -> str: """The phone number.""" return self["Address"]`The phone number. 
- `prop endpoint_type :`- [ConnectContactFlowEndpointType](#aws_lambda_powertools.utilities.data_classes.connect_contact_flow_event.ConnectContactFlowEndpointType)
- 
## Expand source code`@property def endpoint_type(self) -> ConnectContactFlowEndpointType: """The endpoint type.""" return ConnectContactFlowEndpointType[self["Type"]]`The endpoint type. 
 ### Inherited members
- `class ConnectContactFlowEndpointType (*args, **kwds)`
- 
## Expand source code`class ConnectContactFlowEndpointType(Enum): TELEPHONE_NUMBER = auto()`Create a collection of name/value pairs. Example enumeration: `>>> class Color(Enum): ... RED = 1 ... BLUE = 2 ... GREEN = 3`Access them by: - attribute access:
 Color.RED - value lookup:
 Color(1) - name lookup:
 Color['RED'] Enumerations can be iterated over, and know how many members they have: `>>> len(Color) 3``>>> list(Color) [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]`Methods can be added to enumerations, and members can have their own attributes – see the documentation for details. ### Ancestors- enum.Enum
 ### Class variables- `var TELEPHONE_NUMBER`
 
- `class ConnectContactFlowEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class ConnectContactFlowEvent(DictWrapper): """Amazon Connect contact flow event Documentation: ------------- - https://docs.aws.amazon.com/connect/latest/adminguide/connect-lambda-functions.html """ @property def contact_data(self) -> ConnectContactFlowData: """This is always passed by Amazon Connect for every contact. Some parameters are optional.""" return ConnectContactFlowData(self["Details"]["ContactData"]) @property def parameters(self) -> dict[str, str]: """These are parameters specific to this call that were defined when you created the Lambda function.""" return self["Details"]["Parameters"]`Amazon Connect contact flow event ## Documentation:## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop contact_data :`- [ConnectContactFlowData](#aws_lambda_powertools.utilities.data_classes.connect_contact_flow_event.ConnectContactFlowData)
- 
## Expand source code`@property def contact_data(self) -> ConnectContactFlowData: """This is always passed by Amazon Connect for every contact. Some parameters are optional.""" return ConnectContactFlowData(self["Details"]["ContactData"])`This is always passed by Amazon Connect for every contact. Some parameters are optional. 
- `prop parameters : dict[str, str]`
- 
## Expand source code`@property def parameters(self) -> dict[str, str]: """These are parameters specific to this call that were defined when you created the Lambda function.""" return self["Details"]["Parameters"]`These are parameters specific to this call that were defined when you created the Lambda function. 
 ### Inherited members
- `class ConnectContactFlowInitiationMethod (*args, **kwds)`
- 
## Expand source code`class ConnectContactFlowInitiationMethod(Enum): INBOUND = auto() OUTBOUND = auto() TRANSFER = auto() CALLBACK = auto() API = auto()`Create a collection of name/value pairs. Example enumeration: `>>> class Color(Enum): ... RED = 1 ... BLUE = 2 ... GREEN = 3`Access them by: - attribute access:
 Color.RED - value lookup:
 Color(1) - name lookup:
 Color['RED'] Enumerations can be iterated over, and know how many members they have: `>>> len(Color) 3``>>> list(Color) [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]`Methods can be added to enumerations, and members can have their own attributes – see the documentation for details. ### Ancestors- enum.Enum
 ### Class variables- `var API`
- `var CALLBACK`
- `var INBOUND`
- `var OUTBOUND`
- `var TRANSFER`
 
- `class ConnectContactFlowMediaStreamAudio (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class ConnectContactFlowMediaStreamAudio(DictWrapper): @property def start_fragment_number(self) -> str | None: """The number that identifies the Kinesis Video Streams fragment, in the stream used for Live media streaming, in which the customer audio stream started. """ return self["StartFragmentNumber"] @property def start_timestamp(self) -> str | None: """When the customer audio stream started.""" return self["StartTimestamp"] @property def stream_arn(self) -> str | None: """The ARN of the Kinesis Video stream used for Live media streaming that includes the customer data to reference. """ return self["StreamARN"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop start_fragment_number : str | None`
- 
## Expand source code`@property def start_fragment_number(self) -> str | None: """The number that identifies the Kinesis Video Streams fragment, in the stream used for Live media streaming, in which the customer audio stream started. """ return self["StartFragmentNumber"]`The number that identifies the Kinesis Video Streams fragment, in the stream used for Live media streaming, in which the customer audio stream started. 
- `prop start_timestamp : str | None`
- 
## Expand source code`@property def start_timestamp(self) -> str | None: """When the customer audio stream started.""" return self["StartTimestamp"]`When the customer audio stream started. 
- `prop stream_arn : str | None`
- 
## Expand source code`@property def stream_arn(self) -> str | None: """The ARN of the Kinesis Video stream used for Live media streaming that includes the customer data to reference. """ return self["StreamARN"]`The ARN of the Kinesis Video stream used for Live media streaming that includes the customer data to reference. 
 ### Inherited members
- `class ConnectContactFlowMediaStreamCustomer (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class ConnectContactFlowMediaStreamCustomer(DictWrapper): @property def audio(self) -> ConnectContactFlowMediaStreamAudio: return ConnectContactFlowMediaStreamAudio(self["Audio"])`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop audio :`- [ConnectContactFlowMediaStreamAudio](#aws_lambda_powertools.utilities.data_classes.connect_contact_flow_event.ConnectContactFlowMediaStreamAudio)
- 
## Expand source code`@property def audio(self) -> ConnectContactFlowMediaStreamAudio: return ConnectContactFlowMediaStreamAudio(self["Audio"])`
 ### Inherited members
- `class ConnectContactFlowMediaStreams (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class ConnectContactFlowMediaStreams(DictWrapper): @property def customer(self) -> ConnectContactFlowMediaStreamCustomer: return ConnectContactFlowMediaStreamCustomer(self["Customer"])`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop customer :`- [ConnectContactFlowMediaStreamCustomer](#aws_lambda_powertools.utilities.data_classes.connect_contact_flow_event.ConnectContactFlowMediaStreamCustomer)
- 
## Expand source code`@property def customer(self) -> ConnectContactFlowMediaStreamCustomer: return ConnectContactFlowMediaStreamCustomer(self["Customer"])`
 ### Inherited members
- `class ConnectContactFlowQueue (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class ConnectContactFlowQueue(DictWrapper): @property def arn(self) -> str: """The unique queue ARN.""" return self["ARN"] @property def name(self) -> str: """The queue name.""" return self["Name"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop arn : str`
- 
## Expand source code`@property def arn(self) -> str: """The unique queue ARN.""" return self["ARN"]`The unique queue ARN. 
- `prop name : str`
- 
## Expand source code`@property def name(self) -> str: """The queue name.""" return self["Name"]`The queue name. 
 ### Inherited members