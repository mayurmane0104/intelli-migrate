# aws_lambda_powertools.utilities.data_classes.bedrock_agent_event API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/bedrock_agent_event.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/bedrock_agent_event.html)

---

# Module `aws_lambda_powertools.utilities.data_classes.bedrock_agent_event`

## Classes

- `class BedrockAgentEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class BedrockAgentEvent(BaseProxyEvent): """ Bedrock Agent input event See https://docs.aws.amazon.com/bedrock/latest/userguide/agents-create.html """ @property def message_version(self) -> str: return self["messageVersion"] @property def input_text(self) -> str: return self["inputText"] @property def session_id(self) -> str: return self["sessionId"] @property def action_group(self) -> str: return self["actionGroup"] @property def api_path(self) -> str: return self["apiPath"] @property def http_method(self) -> str: return self["httpMethod"] @property def parameters(self) -> list[BedrockAgentProperty]: parameters = self.get("parameters") or [] return [BedrockAgentProperty(x) for x in parameters] @property def request_body(self) -> BedrockAgentRequestBody | None: return BedrockAgentRequestBody(self["requestBody"]) if self.get("requestBody") else None @property def agent(self) -> BedrockAgentInfo: return BedrockAgentInfo(self["agent"]) @property def session_attributes(self) -> dict[str, str]: return self["sessionAttributes"] @property def prompt_session_attributes(self) -> dict[str, str]: return self["promptSessionAttributes"] # The following methods add compatibility with BaseProxyEvent @property def path(self) -> str: return self["apiPath"] @cached_property def query_string_parameters(self) -> dict[str, str]: # In Bedrock Agent events, query string parameters are passed as undifferentiated parameters, # together with the other parameters. So we just return all parameters here. parameters = self.get("parameters") or [] return {x["name"]: x["value"] for x in parameters} @property def resolved_headers_field(self) -> dict[str, Any]: return {} @cached_property def json_body(self) -> Any: # In Bedrock Agent events, body parameters are encoded differently # @see https://docs.aws.amazon.com/bedrock/latest/userguide/agents-lambda.html#agents-lambda-input if not self.request_body: return None json_body = self.request_body.content.get("application/json") if not json_body: return None return {x.name: x.value for x in json_body.properties}`Bedrock Agent input event See [https://docs.aws.amazon.com/bedrock/latest/userguide/agents-create.html](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-create.html)## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [BaseProxyEvent](common.html#aws_lambda_powertools.utilities.data_classes.common.BaseProxyEvent)
- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- `prop action_group : str`
- 
## Expand source code`@property def action_group(self) -> str: return self["actionGroup"]`
- `prop agent :`- [BedrockAgentInfo](#aws_lambda_powertools.utilities.data_classes.bedrock_agent_event.BedrockAgentInfo)
- 
## Expand source code`@property def agent(self) -> BedrockAgentInfo: return BedrockAgentInfo(self["agent"])`
- `prop api_path : str`
- 
## Expand source code`@property def api_path(self) -> str: return self["apiPath"]`
- `prop input_text : str`
- 
## Expand source code`@property def input_text(self) -> str: return self["inputText"]`
- `prop message_version : str`
- 
## Expand source code`@property def message_version(self) -> str: return self["messageVersion"]`
- `prop parameters : list[`- [BedrockAgentProperty](#aws_lambda_powertools.utilities.data_classes.bedrock_agent_event.BedrockAgentProperty)]
- 
## Expand source code`@property def parameters(self) -> list[BedrockAgentProperty]: parameters = self.get("parameters") or [] return [BedrockAgentProperty(x) for x in parameters]`
- `prop path : str`
- 
## Expand source code`@property def path(self) -> str: return self["apiPath"]`
- `prop prompt_session_attributes : dict[str, str]`
- 
## Expand source code`@property def prompt_session_attributes(self) -> dict[str, str]: return self["promptSessionAttributes"]`
- `var query_string_parameters : dict[str, str]`
- 
## Expand source code`@cached_property def query_string_parameters(self) -> dict[str, str]: # In Bedrock Agent events, query string parameters are passed as undifferentiated parameters, # together with the other parameters. So we just return all parameters here. parameters = self.get("parameters") or [] return {x["name"]: x["value"] for x in parameters}`
- `prop request_body :`- [BedrockAgentRequestBody](#aws_lambda_powertools.utilities.data_classes.bedrock_agent_event.BedrockAgentRequestBody)| None
- 
## Expand source code`@property def request_body(self) -> BedrockAgentRequestBody | None: return BedrockAgentRequestBody(self["requestBody"]) if self.get("requestBody") else None`
- `prop session_attributes : dict[str, str]`
- 
## Expand source code`@property def session_attributes(self) -> dict[str, str]: return self["sessionAttributes"]`
- `prop session_id : str`
- 
## Expand source code`@property def session_id(self) -> str: return self["sessionId"]`
 ### Inherited members
- `class BedrockAgentInfo (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class BedrockAgentInfo(DictWrapper): @property def name(self) -> str: return self["name"] @property def id(self) -> str: # noqa: A003 return self["id"] @property def alias(self) -> str: return self["alias"] @property def version(self) -> str: return self["version"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop alias : str`
- 
## Expand source code`@property def alias(self) -> str: return self["alias"]`
- `prop id : str`
- 
## Expand source code`@property def id(self) -> str: # noqa: A003 return self["id"]`
- `prop name : str`
- 
## Expand source code`@property def name(self) -> str: return self["name"]`
- `prop version : str`
- 
## Expand source code`@property def version(self) -> str: return self["version"]`
 ### Inherited members
- `class BedrockAgentProperty (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class BedrockAgentProperty(DictWrapper): @property def name(self) -> str: return self["name"] @property def type(self) -> str: # noqa: A003 return self["type"] @property def value(self) -> str: return self["value"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop name : str`
- 
## Expand source code`@property def name(self) -> str: return self["name"]`
- `prop type : str`
- 
## Expand source code`@property def type(self) -> str: # noqa: A003 return self["type"]`
- `prop value : str`
- 
## Expand source code`@property def value(self) -> str: return self["value"]`
 ### Inherited members
- `class BedrockAgentRequestBody (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class BedrockAgentRequestBody(DictWrapper): @property def content(self) -> dict[str, BedrockAgentRequestMedia]: return {k: BedrockAgentRequestMedia(v) for k, v in self["content"].items()}`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop content : dict[str,`- [BedrockAgentRequestMedia](#aws_lambda_powertools.utilities.data_classes.bedrock_agent_event.BedrockAgentRequestMedia)]
- 
## Expand source code`@property def content(self) -> dict[str, BedrockAgentRequestMedia]: return {k: BedrockAgentRequestMedia(v) for k, v in self["content"].items()}`
 ### Inherited members
- `class BedrockAgentRequestMedia (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class BedrockAgentRequestMedia(DictWrapper): @property def properties(self) -> list[BedrockAgentProperty]: return [BedrockAgentProperty(x) for x in self["properties"]]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop properties : list[`- [BedrockAgentProperty](#aws_lambda_powertools.utilities.data_classes.bedrock_agent_event.BedrockAgentProperty)]
- 
## Expand source code`@property def properties(self) -> list[BedrockAgentProperty]: return [BedrockAgentProperty(x) for x in self["properties"]]`
 ### Inherited members