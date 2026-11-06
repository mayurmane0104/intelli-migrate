# aws_lambda_powertools.utilities.data_classes.api_gateway_proxy_event API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/api_gateway_proxy_event.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/api_gateway_proxy_event.html)

---

# Module `aws_lambda_powertools.utilities.data_classes.api_gateway_proxy_event`

## Classes

- `class APIGatewayEventAuthorizer (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class APIGatewayEventAuthorizer(DictWrapper): @property def claims(self) -> dict[str, Any]: return self.get("claims") or {} # key might exist but can be `null` @property def scopes(self) -> list[str]: return self.get("scopes") or [] # key might exist but can be `null` @property def principal_id(self) -> str: """The principal user identification associated with the token sent by the client and returned from an API Gateway Lambda authorizer (formerly known as a custom authorizer)""" return self.get("principalId") or "" # key might exist but can be `null` @property def integration_latency(self) -> int | None: """The authorizer latency in ms.""" return self.get("integrationLatency") def get_context(self) -> dict[str, Any]: """Retrieve the authorization context details injected by a Lambda Authorizer. Example -------- ```python ctx: dict = request_context.authorizer.get_context() tenant_id = ctx.get("tenant_id") ``` Returns: -------- dict[str, Any] A dictionary containing Lambda authorization context details. """ return self._data`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop claims : dict[str, Any]`
- 
## Expand source code`@property def claims(self) -> dict[str, Any]: return self.get("claims") or {} # key might exist but can be `null``
- `prop integration_latency : int | None`
- 
## Expand source code`@property def integration_latency(self) -> int | None: """The authorizer latency in ms.""" return self.get("integrationLatency")`The authorizer latency in ms. 
- `prop principal_id : str`
- 
## Expand source code`@property def principal_id(self) -> str: """The principal user identification associated with the token sent by the client and returned from an API Gateway Lambda authorizer (formerly known as a custom authorizer)""" return self.get("principalId") or "" # key might exist but can be `null``The principal user identification associated with the token sent by the client and returned from an API Gateway Lambda authorizer (formerly known as a custom authorizer) 
- `prop scopes : list[str]`
- 
## Expand source code`@property def scopes(self) -> list[str]: return self.get("scopes") or [] # key might exist but can be `null``
 ### Methods- `def get_context(self) ‑> dict[str, typing.Any]`
- 
## Expand source code`def get_context(self) -> dict[str, Any]: """Retrieve the authorization context details injected by a Lambda Authorizer. Example -------- ```python ctx: dict = request_context.authorizer.get_context() tenant_id = ctx.get("tenant_id") ``` Returns: -------- dict[str, Any] A dictionary containing Lambda authorization context details. """ return self._data`Retrieve the authorization context details injected by a Lambda Authorizer. ## Example`ctx: dict = request_context.authorizer.get_context() tenant_id = ctx.get("tenant_id")`## Returns:dict[str, Any] A dictionary containing Lambda authorization context details. 
 ### Inherited members
- `class APIGatewayEventRequestContext (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class APIGatewayEventRequestContext(BaseRequestContext): @property def connected_at(self) -> int | None: """The Epoch-formatted connection time. (WebSocket API)""" return self["requestContext"].get("connectedAt") @property def connection_id(self) -> str | None: """A unique ID for the connection that can be used to make a callback to the client. (WebSocket API)""" return self["requestContext"].get("connectionId") @property def event_type(self) -> str | None: """The event type: `CONNECT`, `MESSAGE`, or `DISCONNECT`. (WebSocket API)""" return self["requestContext"].get("eventType") @property def message_direction(self) -> str | None: """Message direction (WebSocket API)""" return self["requestContext"].get("messageDirection") @property def message_id(self) -> str | None: """A unique server-side ID for a message. Available only when the `eventType` is `MESSAGE`.""" return self["requestContext"].get("messageId") @property def operation_name(self) -> str | None: """The name of the operation being performed""" return self["requestContext"].get("operationName") @property def route_key(self) -> str | None: """The selected route key.""" return self["requestContext"].get("routeKey") @property def authorizer(self) -> APIGatewayEventAuthorizer: authz_data = self._data.get("requestContext", {}).get("authorizer", {}) return APIGatewayEventAuthorizer(authz_data)`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [BaseRequestContext](common.html#aws_lambda_powertools.utilities.data_classes.common.BaseRequestContext)
- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- 
## Expand source code`@property def authorizer(self) -> APIGatewayEventAuthorizer: authz_data = self._data.get("requestContext", {}).get("authorizer", {}) return APIGatewayEventAuthorizer(authz_data)`
- `prop connected_at : int | None`
- 
## Expand source code`@property def connected_at(self) -> int | None: """The Epoch-formatted connection time. (WebSocket API)""" return self["requestContext"].get("connectedAt")`The Epoch-formatted connection time. (WebSocket API) 
- `prop connection_id : str | None`
- 
## Expand source code`@property def connection_id(self) -> str | None: """A unique ID for the connection that can be used to make a callback to the client. (WebSocket API)""" return self["requestContext"].get("connectionId")`A unique ID for the connection that can be used to make a callback to the client. (WebSocket API) 
- `prop event_type : str | None`
- 
## Expand source code`@property def event_type(self) -> str | None: """The event type: `CONNECT`, `MESSAGE`, or `DISCONNECT`. (WebSocket API)""" return self["requestContext"].get("eventType")`The event type: `CONNECT`,`MESSAGE`, or`DISCONNECT`. (WebSocket API)
- `prop message_direction : str | None`
- 
## Expand source code`@property def message_direction(self) -> str | None: """Message direction (WebSocket API)""" return self["requestContext"].get("messageDirection")`Message direction (WebSocket API) 
- `prop message_id : str | None`
- 
## Expand source code`@property def message_id(self) -> str | None: """A unique server-side ID for a message. Available only when the `eventType` is `MESSAGE`.""" return self["requestContext"].get("messageId")`A unique server-side ID for a message. Available only when the `eventType`is`MESSAGE`.
- `prop operation_name : str | None`
- 
## Expand source code`@property def operation_name(self) -> str | None: """The name of the operation being performed""" return self["requestContext"].get("operationName")`The name of the operation being performed 
- `prop route_key : str | None`
- 
## Expand source code`@property def route_key(self) -> str | None: """The selected route key.""" return self["requestContext"].get("routeKey")`The selected route key. 
 ### Inherited members
- `class APIGatewayProxyEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class APIGatewayProxyEvent(BaseProxyEvent): """AWS Lambda proxy V1 Documentation: -------------- - https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html """ @property def version(self) -> str: return self["version"] @property def resource(self) -> str: return self["resource"] @property def multi_value_headers(self) -> dict[str, list[str]]: return CaseInsensitiveDict(self.get("multiValueHeaders")) @property def multi_value_query_string_parameters(self) -> dict[str, list[str]]: return self.get("multiValueQueryStringParameters") or {} # key might exist but can be `null` @property def resolved_query_string_parameters(self) -> dict[str, list[str]]: if self.multi_value_query_string_parameters: return self.multi_value_query_string_parameters return super().resolved_query_string_parameters @property def resolved_headers_field(self) -> dict[str, Any]: return self.multi_value_headers or self.headers @property def request_context(self) -> APIGatewayEventRequestContext: return APIGatewayEventRequestContext(self._data) @property def path_parameters(self) -> dict[str, str]: return self.get("pathParameters") or {} @property def stage_variables(self) -> dict[str, str]: return self.get("stageVariables") or {} def header_serializer(self) -> BaseHeadersSerializer: return MultiValueHeadersSerializer()`AWS Lambda proxy V1 ## Documentation:## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop multi_value_headers : dict[str, list[str]]`
- 
## Expand source code`@property def multi_value_headers(self) -> dict[str, list[str]]: return CaseInsensitiveDict(self.get("multiValueHeaders"))`
- `prop multi_value_query_string_parameters : dict[str, list[str]]`
- 
## Expand source code`@property def multi_value_query_string_parameters(self) -> dict[str, list[str]]: return self.get("multiValueQueryStringParameters") or {} # key might exist but can be `null``
- `prop path_parameters : dict[str, str]`
- 
## Expand source code`@property def path_parameters(self) -> dict[str, str]: return self.get("pathParameters") or {}`
- `prop request_context :`- [APIGatewayEventRequestContext](#aws_lambda_powertools.utilities.data_classes.api_gateway_proxy_event.APIGatewayEventRequestContext)
- 
## Expand source code`@property def request_context(self) -> APIGatewayEventRequestContext: return APIGatewayEventRequestContext(self._data)`
- `prop resource : str`
- 
## Expand source code`@property def resource(self) -> str: return self["resource"]`
- `prop stage_variables : dict[str, str]`
- 
## Expand source code`@property def stage_variables(self) -> dict[str, str]: return self.get("stageVariables") or {}`
- `prop version : str`
- 
## Expand source code`@property def version(self) -> str: return self["version"]`
 ### Methods- `def header_serializer(self) ‑>`- [BaseHeadersSerializer](../../shared/headers_serializer.html#aws_lambda_powertools.shared.headers_serializer.BaseHeadersSerializer)
- 
## Expand source code`def header_serializer(self) -> BaseHeadersSerializer: return MultiValueHeadersSerializer()`
 ### Inherited members
- `class APIGatewayProxyEventV2 (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class APIGatewayProxyEventV2(BaseProxyEvent): """AWS Lambda proxy V2 event Notes: ----- Format 2.0 doesn't have multiValueHeaders or multiValueQueryStringParameters fields. Duplicate headers are combined with commas and included in the headers field. Duplicate query strings are combined with commas and included in the queryStringParameters field. Format 2.0 includes a new cookies field. All cookie headers in the request are combined with commas and added to the cookies field. In the response to the client, each cookie becomes a set-cookie header. Documentation: -------------- - https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html """ @property def version(self) -> str: return self["version"] @property def route_key(self) -> str: return self["routeKey"] @property def raw_path(self) -> str: return self["rawPath"] @property def raw_query_string(self) -> str: return self["rawQueryString"] @property def cookies(self) -> list[str]: return self.get("cookies") or [] @property def request_context(self) -> RequestContextV2: return RequestContextV2(self._data) @property def path_parameters(self) -> dict[str, str]: return self.get("pathParameters") or {} @property def stage_variables(self) -> dict[str, str]: return self.get("stageVariables") or {} @property def path(self) -> str: stage = self.request_context.stage if stage != "$default": return self.raw_path[len("/" + stage) :] return self.raw_path @property def http_method(self) -> str: """The HTTP method used. Valid values include: DELETE, GET, HEAD, OPTIONS, PATCH, POST, and PUT.""" return self.request_context.http.method def header_serializer(self): return HttpApiHeadersSerializer() @cached_property def resolved_headers_field(self) -> dict[str, Any]: return CaseInsensitiveDict((k, v.split(",") if "," in v else v) for k, v in self.headers.items())`AWS Lambda proxy V2 event ## Notes:Format 2.0 doesn't have multiValueHeaders or multiValueQueryStringParameters fields. Duplicate headers are combined with commas and included in the headers field. Duplicate query strings are combined with commas and included in the queryStringParameters field. Format 2.0 includes a new cookies field. All cookie headers in the request are combined with commas and added to the cookies field. In the response to the client, each cookie becomes a set-cookie header. ## Documentation:## Parameters- `data`- `dict[str, Any]`
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
 ### Subclasses### Instance variables- 
## Expand source code`@property def cookies(self) -> list[str]: return self.get("cookies") or []`
- `prop path : str`
- 
## Expand source code`@property def path(self) -> str: stage = self.request_context.stage if stage != "$default": return self.raw_path[len("/" + stage) :] return self.raw_path`
- `prop path_parameters : dict[str, str]`
- 
## Expand source code`@property def path_parameters(self) -> dict[str, str]: return self.get("pathParameters") or {}`
- `prop raw_path : str`
- 
## Expand source code`@property def raw_path(self) -> str: return self["rawPath"]`
- `prop raw_query_string : str`
- 
## Expand source code`@property def raw_query_string(self) -> str: return self["rawQueryString"]`
- `prop request_context :`- [RequestContextV2](#aws_lambda_powertools.utilities.data_classes.api_gateway_proxy_event.RequestContextV2)
- 
## Expand source code`@property def request_context(self) -> RequestContextV2: return RequestContextV2(self._data)`
- `prop route_key : str`
- 
## Expand source code`@property def route_key(self) -> str: return self["routeKey"]`
- `prop stage_variables : dict[str, str]`
- 
## Expand source code`@property def stage_variables(self) -> dict[str, str]: return self.get("stageVariables") or {}`
- `prop version : str`
- 
## Expand source code`@property def version(self) -> str: return self["version"]`
 ### Methods- `def header_serializer(self)`
- 
## Expand source code`def header_serializer(self): return HttpApiHeadersSerializer()`
 ### Inherited members
- `class RequestContextV2 (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class RequestContextV2(BaseRequestContextV2): @property def authorizer(self) -> RequestContextV2Authorizer: ctx = self.get("requestContext") or {} # key might exist but can be `null` return RequestContextV2Authorizer(ctx.get("authorizer", {}))`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [BaseRequestContextV2](common.html#aws_lambda_powertools.utilities.data_classes.common.BaseRequestContextV2)
- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- 
## Expand source code`@property def authorizer(self) -> RequestContextV2Authorizer: ctx = self.get("requestContext") or {} # key might exist but can be `null` return RequestContextV2Authorizer(ctx.get("authorizer", {}))`
 ### Inherited members
- `class RequestContextV2Authorizer (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class RequestContextV2Authorizer(DictWrapper): @property def jwt_claim(self) -> dict[str, Any]: jwt = self.get("jwt") or {} # not available in FunctionURL; key might exist but can be `null` return jwt.get("claims") or {} # key might exist but can be `null` @property def jwt_scopes(self) -> list[str]: jwt = self.get("jwt") or {} # not available in FunctionURL; key might exist but can be `null` return jwt.get("scopes", []) @property def get_lambda(self) -> dict[str, Any]: """Lambda authorization context details""" return self.get("lambda") or {} # key might exist but can be `null` def get_context(self) -> dict[str, Any]: """Retrieve the authorization context details injected by a Lambda Authorizer. Example -------- ```python ctx: dict = request_context.authorizer.get_context() tenant_id = ctx.get("tenant_id") ``` Returns: -------- dict[str, Any] A dictionary containing Lambda authorization context details. """ return self.get_lambda @property def iam(self) -> RequestContextV2AuthorizerIam: """IAM authorization details used for making the request.""" iam = self.get("iam") or {} # key might exist but can be `null` return RequestContextV2AuthorizerIam(iam)`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop get_lambda : dict[str, Any]`
- 
## Expand source code`@property def get_lambda(self) -> dict[str, Any]: """Lambda authorization context details""" return self.get("lambda") or {} # key might exist but can be `null``Lambda authorization context details 
- `prop iam :`- [RequestContextV2AuthorizerIam](#aws_lambda_powertools.utilities.data_classes.api_gateway_proxy_event.RequestContextV2AuthorizerIam)
- 
## Expand source code`@property def iam(self) -> RequestContextV2AuthorizerIam: """IAM authorization details used for making the request.""" iam = self.get("iam") or {} # key might exist but can be `null` return RequestContextV2AuthorizerIam(iam)`IAM authorization details used for making the request. 
- `prop jwt_claim : dict[str, Any]`
- 
## Expand source code`@property def jwt_claim(self) -> dict[str, Any]: jwt = self.get("jwt") or {} # not available in FunctionURL; key might exist but can be `null` return jwt.get("claims") or {} # key might exist but can be `null``
- `prop jwt_scopes : list[str]`
- 
## Expand source code`@property def jwt_scopes(self) -> list[str]: jwt = self.get("jwt") or {} # not available in FunctionURL; key might exist but can be `null` return jwt.get("scopes", [])`
 ### Methods- `def get_context(self) ‑> dict[str, typing.Any]`
- 
## Expand source code`def get_context(self) -> dict[str, Any]: """Retrieve the authorization context details injected by a Lambda Authorizer. Example -------- ```python ctx: dict = request_context.authorizer.get_context() tenant_id = ctx.get("tenant_id") ``` Returns: -------- dict[str, Any] A dictionary containing Lambda authorization context details. """ return self.get_lambda`Retrieve the authorization context details injected by a Lambda Authorizer. ## Example`ctx: dict = request_context.authorizer.get_context() tenant_id = ctx.get("tenant_id")`## Returns:dict[str, Any] A dictionary containing Lambda authorization context details. 
 ### Inherited members
- `class RequestContextV2AuthorizerIam (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class RequestContextV2AuthorizerIam(DictWrapper): @property def access_key(self) -> str: """The IAM user access key associated with the request.""" return self.get("accessKey") or "" # key might exist but can be `null` @property def account_id(self) -> str: """The AWS account ID associated with the request.""" return self.get("accountId") or "" # key might exist but can be `null` @property def caller_id(self) -> str: """The principal identifier of the caller making the request.""" return self.get("callerId") or "" # key might exist but can be `null` def _cognito_identity(self) -> dict: return self.get("cognitoIdentity") or {} # not available in FunctionURL; key might exist but can be `null` @property def cognito_amr(self) -> list[str]: """This represents how the user was authenticated. AMR stands for Authentication Methods References as per the openid spec""" return self._cognito_identity().get("amr", []) @property def cognito_identity_id(self) -> str: """The Amazon Cognito identity ID of the caller making the request. Available only if the request was signed with Amazon Cognito credentials.""" return self._cognito_identity().get("identityId", "") @property def cognito_identity_pool_id(self) -> str: """The Amazon Cognito identity pool ID of the caller making the request. Available only if the request was signed with Amazon Cognito credentials.""" return self._cognito_identity().get("identityPoolId") or "" # key might exist but can be `null` @property def principal_org_id(self) -> str: """The AWS organization ID.""" return self.get("principalOrgId") or "" # key might exist but can be `null` @property def user_arn(self) -> str: """The Amazon Resource Name (ARN) of the effective user identified after authentication.""" return self.get("userArn") or "" # key might exist but can be `null` @property def user_id(self) -> str: """The IAM user ID of the effective user identified after authentication.""" return self.get("userId") or "" # key might exist but can be `null``Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop access_key : str`
- 
## Expand source code`@property def access_key(self) -> str: """The IAM user access key associated with the request.""" return self.get("accessKey") or "" # key might exist but can be `null``The IAM user access key associated with the request. 
- `prop account_id : str`
- 
## Expand source code`@property def account_id(self) -> str: """The AWS account ID associated with the request.""" return self.get("accountId") or "" # key might exist but can be `null``The AWS account ID associated with the request. 
- `prop caller_id : str`
- 
## Expand source code`@property def caller_id(self) -> str: """The principal identifier of the caller making the request.""" return self.get("callerId") or "" # key might exist but can be `null``The principal identifier of the caller making the request. 
- `prop cognito_amr : list[str]`
- 
## Expand source code`@property def cognito_amr(self) -> list[str]: """This represents how the user was authenticated. AMR stands for Authentication Methods References as per the openid spec""" return self._cognito_identity().get("amr", [])`This represents how the user was authenticated. AMR stands for Authentication Methods References as per the openid spec 
- `prop cognito_identity_id : str`
- 
## Expand source code`@property def cognito_identity_id(self) -> str: """The Amazon Cognito identity ID of the caller making the request. Available only if the request was signed with Amazon Cognito credentials.""" return self._cognito_identity().get("identityId", "")`The Amazon Cognito identity ID of the caller making the request. Available only if the request was signed with Amazon Cognito credentials. 
- `prop cognito_identity_pool_id : str`
- 
## Expand source code`@property def cognito_identity_pool_id(self) -> str: """The Amazon Cognito identity pool ID of the caller making the request. Available only if the request was signed with Amazon Cognito credentials.""" return self._cognito_identity().get("identityPoolId") or "" # key might exist but can be `null``The Amazon Cognito identity pool ID of the caller making the request. Available only if the request was signed with Amazon Cognito credentials. 
- `prop principal_org_id : str`
- 
## Expand source code`@property def principal_org_id(self) -> str: """The AWS organization ID.""" return self.get("principalOrgId") or "" # key might exist but can be `null``The AWS organization ID. 
- `prop user_arn : str`
- 
## Expand source code`@property def user_arn(self) -> str: """The Amazon Resource Name (ARN) of the effective user identified after authentication.""" return self.get("userArn") or "" # key might exist but can be `null``The Amazon Resource Name (ARN) of the effective user identified after authentication. 
- `prop user_id : str`
- 
## Expand source code`@property def user_id(self) -> str: """The IAM user ID of the effective user identified after authentication.""" return self.get("userId") or "" # key might exist but can be `null``The IAM user ID of the effective user identified after authentication. 
 ### Inherited members