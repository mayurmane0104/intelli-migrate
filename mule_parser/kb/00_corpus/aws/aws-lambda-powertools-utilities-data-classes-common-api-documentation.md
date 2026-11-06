# aws_lambda_powertools.utilities.data_classes.common API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/common.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/common.html)

---

# Module `aws_lambda_powertools.utilities.data_classes.common`

## Classes

- `class APIGatewayEventIdentity (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class APIGatewayEventIdentity(DictWrapper): @property def access_key(self) -> str | None: return self["requestContext"]["identity"].get("accessKey") @property def account_id(self) -> str | None: """The AWS account ID associated with the request.""" return self["requestContext"]["identity"].get("accountId") @property def api_key(self) -> str | None: """For API methods that require an API key, this variable is the API key associated with the method request. For methods that don't require an API key, this variable is null.""" return self["requestContext"]["identity"].get("apiKey") @property def api_key_id(self) -> str | None: """The API key ID associated with an API request that requires an API key.""" return self["requestContext"]["identity"].get("apiKeyId") @property def caller(self) -> str | None: """The principal identifier of the caller making the request.""" return self["requestContext"]["identity"].get("caller") @property def cognito_authentication_provider(self) -> str | None: """A comma-separated list of the Amazon Cognito authentication providers used by the caller making the request. Available only if the request was signed with Amazon Cognito credentials.""" return self["requestContext"]["identity"].get("cognitoAuthenticationProvider") @property def cognito_authentication_type(self) -> str | None: """The Amazon Cognito authentication type of the caller making the request. Available only if the request was signed with Amazon Cognito credentials.""" return self["requestContext"]["identity"].get("cognitoAuthenticationType") @property def cognito_identity_id(self) -> str | None: """The Amazon Cognito identity ID of the caller making the request. Available only if the request was signed with Amazon Cognito credentials.""" return self["requestContext"]["identity"].get("cognitoIdentityId") @property def cognito_identity_pool_id(self) -> str | None: """The Amazon Cognito identity pool ID of the caller making the request. Available only if the request was signed with Amazon Cognito credentials.""" return self["requestContext"]["identity"].get("cognitoIdentityPoolId") @property def principal_org_id(self) -> str | None: """The AWS organization ID.""" return self["requestContext"]["identity"].get("principalOrgId") @property def source_ip(self) -> str: """The source IP address of the TCP connection making the request to API Gateway.""" return self["requestContext"]["identity"]["sourceIp"] @property def user(self) -> str | None: """The principal identifier of the user making the request.""" return self["requestContext"]["identity"].get("user") @property def user_agent(self) -> str | None: """The User Agent of the API caller.""" return self["requestContext"]["identity"].get("userAgent") @property def user_arn(self) -> str | None: """The Amazon Resource Name (ARN) of the effective user identified after authentication.""" return self["requestContext"]["identity"].get("userArn") @property def client_cert(self) -> RequestContextClientCert | None: client_cert = self["requestContext"]["identity"].get("clientCert") return None if client_cert is None else RequestContextClientCert(client_cert)`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [DictWrapper](#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- `prop access_key : str | None`
- 
## Expand source code`@property def access_key(self) -> str | None: return self["requestContext"]["identity"].get("accessKey")`
- `prop account_id : str | None`
- 
## Expand source code`@property def account_id(self) -> str | None: """The AWS account ID associated with the request.""" return self["requestContext"]["identity"].get("accountId")`The AWS account ID associated with the request. 
- `prop api_key : str | None`
- 
## Expand source code`@property def api_key(self) -> str | None: """For API methods that require an API key, this variable is the API key associated with the method request. For methods that don't require an API key, this variable is null.""" return self["requestContext"]["identity"].get("apiKey")`For API methods that require an API key, this variable is the API key associated with the method request. For methods that don't require an API key, this variable is null. 
- `prop api_key_id : str | None`
- 
## Expand source code`@property def api_key_id(self) -> str | None: """The API key ID associated with an API request that requires an API key.""" return self["requestContext"]["identity"].get("apiKeyId")`The API key ID associated with an API request that requires an API key. 
- `prop caller : str | None`
- 
## Expand source code`@property def caller(self) -> str | None: """The principal identifier of the caller making the request.""" return self["requestContext"]["identity"].get("caller")`The principal identifier of the caller making the request. 
- `prop client_cert :`- [RequestContextClientCert](#aws_lambda_powertools.utilities.data_classes.common.RequestContextClientCert)| None
- 
## Expand source code`@property def client_cert(self) -> RequestContextClientCert | None: client_cert = self["requestContext"]["identity"].get("clientCert") return None if client_cert is None else RequestContextClientCert(client_cert)`
- `prop cognito_authentication_provider : str | None`
- 
## Expand source code`@property def cognito_authentication_provider(self) -> str | None: """A comma-separated list of the Amazon Cognito authentication providers used by the caller making the request. Available only if the request was signed with Amazon Cognito credentials.""" return self["requestContext"]["identity"].get("cognitoAuthenticationProvider")`A comma-separated list of the Amazon Cognito authentication providers used by the caller making the request. Available only if the request was signed with Amazon Cognito credentials. 
- `prop cognito_authentication_type : str | None`
- 
## Expand source code`@property def cognito_authentication_type(self) -> str | None: """The Amazon Cognito authentication type of the caller making the request. Available only if the request was signed with Amazon Cognito credentials.""" return self["requestContext"]["identity"].get("cognitoAuthenticationType")`The Amazon Cognito authentication type of the caller making the request. Available only if the request was signed with Amazon Cognito credentials. 
- `prop cognito_identity_id : str | None`
- 
## Expand source code`@property def cognito_identity_id(self) -> str | None: """The Amazon Cognito identity ID of the caller making the request. Available only if the request was signed with Amazon Cognito credentials.""" return self["requestContext"]["identity"].get("cognitoIdentityId")`The Amazon Cognito identity ID of the caller making the request. Available only if the request was signed with Amazon Cognito credentials. 
- `prop cognito_identity_pool_id : str | None`
- 
## Expand source code`@property def cognito_identity_pool_id(self) -> str | None: """The Amazon Cognito identity pool ID of the caller making the request. Available only if the request was signed with Amazon Cognito credentials.""" return self["requestContext"]["identity"].get("cognitoIdentityPoolId")`The Amazon Cognito identity pool ID of the caller making the request. Available only if the request was signed with Amazon Cognito credentials. 
- `prop principal_org_id : str | None`
- 
## Expand source code`@property def principal_org_id(self) -> str | None: """The AWS organization ID.""" return self["requestContext"]["identity"].get("principalOrgId")`The AWS organization ID. 
- `prop source_ip : str`
- 
## Expand source code`@property def source_ip(self) -> str: """The source IP address of the TCP connection making the request to API Gateway.""" return self["requestContext"]["identity"]["sourceIp"]`The source IP address of the TCP connection making the request to API Gateway. 
- `prop user : str | None`
- 
## Expand source code`@property def user(self) -> str | None: """The principal identifier of the user making the request.""" return self["requestContext"]["identity"].get("user")`The principal identifier of the user making the request. 
- `prop user_agent : str | None`
- 
## Expand source code`@property def user_agent(self) -> str | None: """The User Agent of the API caller.""" return self["requestContext"]["identity"].get("userAgent")`The User Agent of the API caller. 
- `prop user_arn : str | None`
- 
## Expand source code`@property def user_arn(self) -> str | None: """The Amazon Resource Name (ARN) of the effective user identified after authentication.""" return self["requestContext"]["identity"].get("userArn")`The Amazon Resource Name (ARN) of the effective user identified after authentication. 
 ### Inherited members
- `class BaseProxyEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class BaseProxyEvent(DictWrapper): @property def headers(self) -> dict[str, str]: return CaseInsensitiveDict(self.get("headers")) @property def query_string_parameters(self) -> dict[str, str]: return self.get("queryStringParameters") or {} @property def multi_value_query_string_parameters(self) -> dict[str, list[str]]: return self.get("multiValueQueryStringParameters") or {} @cached_property def resolved_query_string_parameters(self) -> dict[str, list[str]]: """ This property determines the appropriate query string parameter to be used as a trusted source for validating OpenAPI. This is necessary because different resolvers use different formats to encode multi query string parameters. """ return {k: v.split(",") for k, v in self.query_string_parameters.items()} @property def resolved_headers_field(self) -> dict[str, str]: """ This property determines the appropriate header to be used as a trusted source for validating OpenAPI. This is necessary because different resolvers use different formats to encode headers parameters. Headers are case-insensitive according to RFC 7540 (HTTP/2), so we lower the header name This ensures that customers can access headers with any casing, as per the RFC guidelines. Reference: https://www.rfc-editor.org/rfc/rfc7540#section-8.1.2 """ return self.headers @property def is_base64_encoded(self) -> bool | None: return self.get("isBase64Encoded") @property def body(self) -> str | None: """Submitted body of the request as a string""" return self.get("body") @cached_property def json_body(self) -> Any: """Parses the submitted body as json""" if self.decoded_body: return self._json_deserializer(self.decoded_body) return None @cached_property def decoded_body(self) -> str | None: """Decode the body from base64 if encoded, otherwise return it as is.""" body: str | None = self.body if self.is_base64_encoded and body: return base64.b64decode(body.encode()).decode() return body @property def path(self) -> str: return self["path"] @property def http_method(self) -> str: """The HTTP method used. Valid values include: DELETE, GET, HEAD, OPTIONS, PATCH, POST, and PUT.""" return self["httpMethod"] @overload def get_query_string_value(self, name: str, default_value: str) -> str: ... @overload def get_query_string_value(self, name: str, default_value: str | None = None) -> str | None: ... def get_query_string_value(self, name: str, default_value: str | None = None) -> str | None: """Get query string value by name Parameters ---------- name: str Query string parameter name default_value: str, optional Default value if no value was found by name Returns ------- str, optional Query string parameter value """ return get_query_string_value( query_string_parameters=self.query_string_parameters, name=name, default_value=default_value, ) def get_multi_value_query_string_values( self, name: str, default_values: list[str] | None = None, ) -> list[str]: """Get multi-value query string parameter values by name Parameters ---------- name: str Multi-Value query string parameter name default_values: List[str], optional Default values is no values are found by name Returns ------- List[str], optional List of query string values """ return get_multi_value_query_string_values( multi_value_query_string_parameters=self.multi_value_query_string_parameters, name=name, default_values=default_values, ) @overload def get_header_value( self, name: str, default_value: str, case_sensitive: bool = False, ) -> str: ... @overload def get_header_value( self, name: str, default_value: str | None = None, case_sensitive: bool = False, ) -> str | None: ... @deprecated( "`get_header_value` function is deprecated; Access headers directly using event.headers.get('HeaderName')", category=None, ) def get_header_value( self, name: str, default_value: str | None = None, case_sensitive: bool = False, ) -> str | None: """Get header value by name Parameters ---------- name: str Header name default_value: str, optional Default value if no value was found by name case_sensitive: bool Whether to use a case-sensitive look up. By default we make a case-insensitive lookup. Returns ------- str, optional Header value """ warnings.warn( "The `get_header_value` function is deprecated in V3 and the `case_sensitive` parameter " "no longer has any effect. This function will be removed in the next major version. " "Instead, access headers directly using event.headers.get('HeaderName'), which is case insensitive.", category=PowertoolsDeprecationWarning, stacklevel=2, ) return get_header_value( headers=self.headers, name=name, default_value=default_value, case_sensitive=case_sensitive, ) def header_serializer(self) -> BaseHeadersSerializer: raise NotImplementedError()`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [DictWrapper](#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Subclasses### Instance variables- `prop body : str | None`
- 
## Expand source code`@property def body(self) -> str | None: """Submitted body of the request as a string""" return self.get("body")`Submitted body of the request as a string 
- `var decoded_body : str | None`
- 
## Expand source code`@cached_property def decoded_body(self) -> str | None: """Decode the body from base64 if encoded, otherwise return it as is.""" body: str | None = self.body if self.is_base64_encoded and body: return base64.b64decode(body.encode()).decode() return body`Decode the body from base64 if encoded, otherwise return it as is. 
- `prop headers : dict[str, str]`
- 
## Expand source code`@property def headers(self) -> dict[str, str]: return CaseInsensitiveDict(self.get("headers"))`
- `prop http_method : str`
- 
## Expand source code`@property def http_method(self) -> str: """The HTTP method used. Valid values include: DELETE, GET, HEAD, OPTIONS, PATCH, POST, and PUT.""" return self["httpMethod"]`The HTTP method used. Valid values include: DELETE, GET, HEAD, OPTIONS, PATCH, POST, and PUT. 
- `prop is_base64_encoded : bool | None`
- 
## Expand source code`@property def is_base64_encoded(self) -> bool | None: return self.get("isBase64Encoded")`
- `var json_body : Any`
- 
## Expand source code`@cached_property def json_body(self) -> Any: """Parses the submitted body as json""" if self.decoded_body: return self._json_deserializer(self.decoded_body) return None`Parses the submitted body as json 
- `prop multi_value_query_string_parameters : dict[str, list[str]]`
- 
## Expand source code`@property def multi_value_query_string_parameters(self) -> dict[str, list[str]]: return self.get("multiValueQueryStringParameters") or {}`
- `prop path : str`
- 
## Expand source code`@property def path(self) -> str: return self["path"]`
- `prop query_string_parameters : dict[str, str]`
- 
## Expand source code`@property def query_string_parameters(self) -> dict[str, str]: return self.get("queryStringParameters") or {}`
- `prop resolved_headers_field : dict[str, str]`
- 
## Expand source code`@property def resolved_headers_field(self) -> dict[str, str]: """ This property determines the appropriate header to be used as a trusted source for validating OpenAPI. This is necessary because different resolvers use different formats to encode headers parameters. Headers are case-insensitive according to RFC 7540 (HTTP/2), so we lower the header name This ensures that customers can access headers with any casing, as per the RFC guidelines. Reference: https://www.rfc-editor.org/rfc/rfc7540#section-8.1.2 """ return self.headers`This property determines the appropriate header to be used as a trusted source for validating OpenAPI. This is necessary because different resolvers use different formats to encode headers parameters. Headers are case-insensitive according to RFC 7540 (HTTP/2), so we lower the header name This ensures that customers can access headers with any casing, as per the RFC guidelines. Reference: [https://www.rfc-editor.org/rfc/rfc7540#section-8.1.2](https://www.rfc-editor.org/rfc/rfc7540#section-8.1.2)
- `var resolved_query_string_parameters : dict[str, list[str]]`
- 
## Expand source code`@cached_property def resolved_query_string_parameters(self) -> dict[str, list[str]]: """ This property determines the appropriate query string parameter to be used as a trusted source for validating OpenAPI. This is necessary because different resolvers use different formats to encode multi query string parameters. """ return {k: v.split(",") for k, v in self.query_string_parameters.items()}`This property determines the appropriate query string parameter to be used as a trusted source for validating OpenAPI. This is necessary because different resolvers use different formats to encode multi query string parameters. 
 ### Methods- `def get_header_value(self, name: str, default_value: str | None = None, case_sensitive: bool = False) ‑> str | None`
- 
## Expand source code`@deprecated( "`get_header_value` function is deprecated; Access headers directly using event.headers.get('HeaderName')", category=None, ) def get_header_value( self, name: str, default_value: str | None = None, case_sensitive: bool = False, ) -> str | None: """Get header value by name Parameters ---------- name: str Header name default_value: str, optional Default value if no value was found by name case_sensitive: bool Whether to use a case-sensitive look up. By default we make a case-insensitive lookup. Returns ------- str, optional Header value """ warnings.warn( "The `get_header_value` function is deprecated in V3 and the `case_sensitive` parameter " "no longer has any effect. This function will be removed in the next major version. " "Instead, access headers directly using event.headers.get('HeaderName'), which is case insensitive.", category=PowertoolsDeprecationWarning, stacklevel=2, ) return get_header_value( headers=self.headers, name=name, default_value=default_value, case_sensitive=case_sensitive, )`Get header value by name Parameters 
 - `name`- `str`
- Header name
- `default_value`- `str`, optional
- Default value if no value was found by name
- `case_sensitive`- `bool`
- Whether to use a case-sensitive look up. By default we make a case-insensitive lookup.
 ## Returns- `str`, optional
- Header value
 
- `def get_multi_value_query_string_values(self, name: str, default_values: list[str] | None = None) ‑> list[str]`
- 
## Expand source code`def get_multi_value_query_string_values( self, name: str, default_values: list[str] | None = None, ) -> list[str]: """Get multi-value query string parameter values by name Parameters ---------- name: str Multi-Value query string parameter name default_values: List[str], optional Default values is no values are found by name Returns ------- List[str], optional List of query string values """ return get_multi_value_query_string_values( multi_value_query_string_parameters=self.multi_value_query_string_parameters, name=name, default_values=default_values, )`Get multi-value query string parameter values by name Parameters 
 - `name`- `str`
- Multi-Value query string parameter name
- `default_values`- `List[str]`, optional
- Default values is no values are found by name
 ## Returns- `List[str]`, optional
- List of query string values
 
- `def get_query_string_value(self, name: str, default_value: str | None = None) ‑> str | None`
- 
## Expand source code`def get_query_string_value(self, name: str, default_value: str | None = None) -> str | None: """Get query string value by name Parameters ---------- name: str Query string parameter name default_value: str, optional Default value if no value was found by name Returns ------- str, optional Query string parameter value """ return get_query_string_value( query_string_parameters=self.query_string_parameters, name=name, default_value=default_value, )`Get query string value by name Parameters 
 - `name`- `str`
- Query string parameter name
- `default_value`- `str`, optional
- Default value if no value was found by name
 ## Returns- `str`, optional
- Query string parameter value
 
- `def header_serializer(self) ‑> BaseHeadersSerializer`
- 
## Expand source code`def header_serializer(self) -> BaseHeadersSerializer: raise NotImplementedError()`
 ### Inherited members
- `class BaseRequestContext (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class BaseRequestContext(DictWrapper): @property def account_id(self) -> str: """The AWS account ID associated with the request.""" return self["requestContext"]["accountId"] @property def api_id(self) -> str: """The identifier API Gateway assigns to your API.""" return self["requestContext"]["apiId"] @property def domain_name(self) -> str | None: """A domain name""" return self["requestContext"].get("domainName") @property def domain_prefix(self) -> str | None: return self["requestContext"].get("domainPrefix") @property def extended_request_id(self) -> str | None: """An automatically generated ID for the API call, which contains more useful information for debugging/troubleshooting.""" return self["requestContext"].get("extendedRequestId") @property def protocol(self) -> str: """The request protocol, for example, HTTP/1.1.""" return self["requestContext"]["protocol"] @property def http_method(self) -> str: """The HTTP method used. Valid values include: DELETE, GET, HEAD, OPTIONS, PATCH, POST, and PUT.""" return self["requestContext"]["httpMethod"] @property def identity(self) -> APIGatewayEventIdentity: return APIGatewayEventIdentity(self._data) @property def path(self) -> str: return self["requestContext"]["path"] @property def stage(self) -> str: """The deployment stage of the API request""" return self["requestContext"]["stage"] @property def request_id(self) -> str: """The ID that API Gateway assigns to the API request.""" return self["requestContext"]["requestId"] @property def request_time(self) -> str | None: """The CLF-formatted request time (dd/MMM/yyyy:HH:mm:ss +-hhmm)""" return self["requestContext"].get("requestTime") @property def request_time_epoch(self) -> int: """The Epoch-formatted request time.""" return self["requestContext"]["requestTimeEpoch"] @property def resource_id(self) -> str: return self["requestContext"]["resourceId"] @property def resource_path(self) -> str: return self["requestContext"]["resourcePath"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [DictWrapper](#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Subclasses### Instance variables- `prop account_id : str`
- 
## Expand source code`@property def account_id(self) -> str: """The AWS account ID associated with the request.""" return self["requestContext"]["accountId"]`The AWS account ID associated with the request. 
- `prop api_id : str`
- 
## Expand source code`@property def api_id(self) -> str: """The identifier API Gateway assigns to your API.""" return self["requestContext"]["apiId"]`The identifier API Gateway assigns to your API. 
- `prop domain_name : str | None`
- 
## Expand source code`@property def domain_name(self) -> str | None: """A domain name""" return self["requestContext"].get("domainName")`A domain name 
- `prop domain_prefix : str | None`
- 
## Expand source code`@property def domain_prefix(self) -> str | None: return self["requestContext"].get("domainPrefix")`
- `prop extended_request_id : str | None`
- 
## Expand source code`@property def extended_request_id(self) -> str | None: """An automatically generated ID for the API call, which contains more useful information for debugging/troubleshooting.""" return self["requestContext"].get("extendedRequestId")`An automatically generated ID for the API call, which contains more useful information for debugging/troubleshooting. 
- `prop http_method : str`
- 
## Expand source code`@property def http_method(self) -> str: """The HTTP method used. Valid values include: DELETE, GET, HEAD, OPTIONS, PATCH, POST, and PUT.""" return self["requestContext"]["httpMethod"]`The HTTP method used. Valid values include: DELETE, GET, HEAD, OPTIONS, PATCH, POST, and PUT. 
- `prop identity :`- [APIGatewayEventIdentity](#aws_lambda_powertools.utilities.data_classes.common.APIGatewayEventIdentity)
- 
## Expand source code`@property def identity(self) -> APIGatewayEventIdentity: return APIGatewayEventIdentity(self._data)`
- `prop path : str`
- 
## Expand source code`@property def path(self) -> str: return self["requestContext"]["path"]`
- `prop protocol : str`
- 
## Expand source code`@property def protocol(self) -> str: """The request protocol, for example, HTTP/1.1.""" return self["requestContext"]["protocol"]`The request protocol, for example, HTTP/1.1. 
- `prop request_id : str`
- 
## Expand source code`@property def request_id(self) -> str: """The ID that API Gateway assigns to the API request.""" return self["requestContext"]["requestId"]`The ID that API Gateway assigns to the API request. 
- `prop request_time : str | None`
- 
## Expand source code`@property def request_time(self) -> str | None: """The CLF-formatted request time (dd/MMM/yyyy:HH:mm:ss +-hhmm)""" return self["requestContext"].get("requestTime")`The CLF-formatted request time (dd/MMM/yyyy:HH:mm:ss +-hhmm) 
- `prop request_time_epoch : int`
- 
## Expand source code`@property def request_time_epoch(self) -> int: """The Epoch-formatted request time.""" return self["requestContext"]["requestTimeEpoch"]`The Epoch-formatted request time. 
- `prop resource_id : str`
- 
## Expand source code`@property def resource_id(self) -> str: return self["requestContext"]["resourceId"]`
- `prop resource_path : str`
- 
## Expand source code`@property def resource_path(self) -> str: return self["requestContext"]["resourcePath"]`
- `prop stage : str`
- 
## Expand source code`@property def stage(self) -> str: """The deployment stage of the API request""" return self["requestContext"]["stage"]`The deployment stage of the API request 
 ### Inherited members
- `class BaseRequestContextV2 (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class BaseRequestContextV2(DictWrapper): @property def account_id(self) -> str: """The AWS account ID associated with the request.""" return self["requestContext"]["accountId"] @property def api_id(self) -> str: """The identifier API Gateway assigns to your API.""" return self["requestContext"]["apiId"] @property def domain_name(self) -> str: """A domain name""" return self["requestContext"]["domainName"] @property def domain_prefix(self) -> str: return self["requestContext"]["domainPrefix"] @property def http(self) -> RequestContextV2Http: return RequestContextV2Http(self._data) @property def request_id(self) -> str: """The ID that API Gateway assigns to the API request.""" return self["requestContext"]["requestId"] @property def route_key(self) -> str: """The selected route key.""" return self["requestContext"]["routeKey"] @property def stage(self) -> str: """The deployment stage of the API request""" return self["requestContext"]["stage"] @property def time(self) -> str: """The CLF-formatted request time (dd/MMM/yyyy:HH:mm:ss +-hhmm).""" return self["requestContext"]["time"] @property def time_epoch(self) -> int: """The Epoch-formatted request time.""" return self["requestContext"]["timeEpoch"] @property def authentication(self) -> RequestContextClientCert | None: """Optional when using mutual TLS authentication""" # FunctionURL might have NONE as AuthZ authentication = self["requestContext"].get("authentication") or {} client_cert = authentication.get("clientCert") return None if client_cert is None else RequestContextClientCert(client_cert)`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [DictWrapper](#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Subclasses### Instance variables- `prop account_id : str`
- 
## Expand source code`@property def account_id(self) -> str: """The AWS account ID associated with the request.""" return self["requestContext"]["accountId"]`The AWS account ID associated with the request. 
- `prop api_id : str`
- 
## Expand source code`@property def api_id(self) -> str: """The identifier API Gateway assigns to your API.""" return self["requestContext"]["apiId"]`The identifier API Gateway assigns to your API. 
- `prop authentication :`- [RequestContextClientCert](#aws_lambda_powertools.utilities.data_classes.common.RequestContextClientCert)| None
- 
## Expand source code`@property def authentication(self) -> RequestContextClientCert | None: """Optional when using mutual TLS authentication""" # FunctionURL might have NONE as AuthZ authentication = self["requestContext"].get("authentication") or {} client_cert = authentication.get("clientCert") return None if client_cert is None else RequestContextClientCert(client_cert)`Optional when using mutual TLS authentication 
- `prop domain_name : str`
- 
## Expand source code`@property def domain_name(self) -> str: """A domain name""" return self["requestContext"]["domainName"]`A domain name 
- `prop domain_prefix : str`
- 
## Expand source code`@property def domain_prefix(self) -> str: return self["requestContext"]["domainPrefix"]`
- `prop http :`- [RequestContextV2Http](#aws_lambda_powertools.utilities.data_classes.common.RequestContextV2Http)
- 
## Expand source code`@property def http(self) -> RequestContextV2Http: return RequestContextV2Http(self._data)`
- `prop request_id : str`
- 
## Expand source code`@property def request_id(self) -> str: """The ID that API Gateway assigns to the API request.""" return self["requestContext"]["requestId"]`The ID that API Gateway assigns to the API request. 
- `prop route_key : str`
- 
## Expand source code`@property def route_key(self) -> str: """The selected route key.""" return self["requestContext"]["routeKey"]`The selected route key. 
- `prop stage : str`
- 
## Expand source code`@property def stage(self) -> str: """The deployment stage of the API request""" return self["requestContext"]["stage"]`The deployment stage of the API request 
- `prop time : str`
- 
## Expand source code`@property def time(self) -> str: """The CLF-formatted request time (dd/MMM/yyyy:HH:mm:ss +-hhmm).""" return self["requestContext"]["time"]`The CLF-formatted request time (dd/MMM/yyyy:HH:mm:ss +-hhmm). 
- `prop time_epoch : int`
- 
## Expand source code`@property def time_epoch(self) -> int: """The Epoch-formatted request time.""" return self["requestContext"]["timeEpoch"]`The Epoch-formatted request time. 
 ### Inherited members
- `class CaseInsensitiveDict (data=None, **kwargs)`
- 
## Expand source code`class CaseInsensitiveDict(dict): """Case insensitive dict implementation. Assumes string keys only.""" def __init__(self, data=None, **kwargs): super().__init__() self.update(data, **kwargs) def get(self, k, default=None): return super().get(k.lower(), default) def pop(self, k): return super().pop(k.lower()) def setdefault(self, k, default=None): return super().setdefault(k.lower(), default) def update(self, data=None, **kwargs): if data is not None: if isinstance(data, Mapping): data = data.items() super().update((k.lower(), v) for k, v in data) super().update((k.lower(), v) for k, v in kwargs) def __contains__(self, k): return super().__contains__(k.lower()) def __delitem__(self, k): super().__delitem__(k.lower()) def __eq__(self, other): if not isinstance(other, Mapping): return False if not isinstance(other, CaseInsensitiveDict): other = CaseInsensitiveDict(other) return super().__eq__(other) def __getitem__(self, k): return super().__getitem__(k.lower()) def __setitem__(self, k, v): super().__setitem__(k.lower(), v)`Case insensitive dict implementation. Assumes string keys only. ### Ancestors- builtins.dict
 ### Methods- `def get(self, k, default=None)`
- 
## Expand source code`def get(self, k, default=None): return super().get(k.lower(), default)`Return the value for key if key is in the dictionary, else default. 
- `def pop(self, k)`
- 
## Expand source code`def pop(self, k): return super().pop(k.lower())`D.pop(k[,d]) -> v, remove specified key and return the corresponding value. If the key is not found, return the default if given; otherwise, raise a KeyError. 
- `def setdefault(self, k, default=None)`
- 
## Expand source code`def setdefault(self, k, default=None): return super().setdefault(k.lower(), default)`Insert key with a value of default if key is not in the dictionary. Return the value for key if key is in the dictionary, else default. 
- `def update(self, data=None, **kwargs)`
- 
## Expand source code`def update(self, data=None, **kwargs): if data is not None: if isinstance(data, Mapping): data = data.items() super().update((k.lower(), v) for k, v in data) super().update((k.lower(), v) for k, v in kwargs)`D.update([E, ]**F) -> None. Update D from mapping/iterable E and F. If E is present and has a .keys() method, then does: for k in E.keys(): D[k] = E[k] If E is present and lacks a .keys() method, then does: for k, v in E: D[k] = v In either case, this is followed by: for k in F: D[k] = F[k] 
 
- `class DictWrapper (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class DictWrapper(Mapping): """Provides a single read only access to a wrapper dict""" def __init__(self, data: dict[str, Any], json_deserializer: Callable | None = None): """ Parameters ---------- data : dict[str, Any] Lambda Event Source Event payload json_deserializer : Callable, optional function to deserialize `str`, `bytes`, `bytearray` containing a JSON document to a Python `obj`, by default json.loads """ self._data = data self._json_deserializer = json_deserializer or json.loads def __getitem__(self, key: str) -> Any: return self._data[key] def __eq__(self, other: object) -> bool: if not isinstance(other, DictWrapper): return False return self._data == other._data def __iter__(self) -> Iterator: return iter(self._data) def __len__(self) -> int: return len(self._data) def __str__(self) -> str: return str(self._str_helper()) def _str_helper(self) -> dict[str, Any]: """ Recursively get a Dictionary of DictWrapper properties primarily for use by __str__ for debugging purposes. Will remove "raw_event" properties, and any defined by the Data Class `_sensitive_properties` list field. This should be used in case where secrets, such as access keys, are stored in the Data Class but should not be logged out. """ properties = self._properties() sensitive_properties = ["raw_event"] if hasattr(self, "_sensitive_properties"): sensitive_properties.extend(self._sensitive_properties) # pyright: ignore result: dict[str, Any] = {} for property_key in properties: if property_key in sensitive_properties: result[property_key] = "[SENSITIVE]" else: try: property_value = getattr(self, property_key) result[property_key] = property_value # Checks whether the class is a subclass of the parent class to perform a recursive operation. if issubclass(property_value.__class__, DictWrapper): result[property_key] = property_value._str_helper() # Checks if the key is a list and if it is a subclass of the parent class elif isinstance(property_value, list): for seq, item in enumerate(property_value): if issubclass(item.__class__, DictWrapper): result[property_key][seq] = item._str_helper() except Exception: result[property_key] = "[Cannot be deserialized]" return result def _properties(self) -> list[str]: return [p for p in dir(self.__class__) if isinstance(getattr(self.__class__, p), property)] def get(self, key: str, default: Any | None = None) -> Any | None: return self._data.get(key, default) @property def raw_event(self) -> dict[str, Any]: """The original raw event dict""" return self._data`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Subclasses- [ActiveMQEvent](active_mq_event.html#aws_lambda_powertools.utilities.data_classes.active_mq_event.ActiveMQEvent)
- [ActiveMQMessage](active_mq_event.html#aws_lambda_powertools.utilities.data_classes.active_mq_event.ActiveMQMessage)
- [ALBEventRequestContext](alb_event.html#aws_lambda_powertools.utilities.data_classes.alb_event.ALBEventRequestContext)
- [APIGatewayAuthorizerEventV2](api_gateway_authorizer_event.html#aws_lambda_powertools.utilities.data_classes.api_gateway_authorizer_event.APIGatewayAuthorizerEventV2)
- [APIGatewayAuthorizerRequestEvent](api_gateway_authorizer_event.html#aws_lambda_powertools.utilities.data_classes.api_gateway_authorizer_event.APIGatewayAuthorizerRequestEvent)
- [APIGatewayAuthorizerTokenEvent](api_gateway_authorizer_event.html#aws_lambda_powertools.utilities.data_classes.api_gateway_authorizer_event.APIGatewayAuthorizerTokenEvent)
- [APIGatewayEventAuthorizer](api_gateway_proxy_event.html#aws_lambda_powertools.utilities.data_classes.api_gateway_proxy_event.APIGatewayEventAuthorizer)
- [RequestContextV2Authorizer](api_gateway_proxy_event.html#aws_lambda_powertools.utilities.data_classes.api_gateway_proxy_event.RequestContextV2Authorizer)
- [RequestContextV2AuthorizerIam](api_gateway_proxy_event.html#aws_lambda_powertools.utilities.data_classes.api_gateway_proxy_event.RequestContextV2AuthorizerIam)
- [AppSyncAuthorizerEvent](appsync_authorizer_event.html#aws_lambda_powertools.utilities.data_classes.appsync_authorizer_event.AppSyncAuthorizerEvent)
- [AppSyncAuthorizerEventRequestContext](appsync_authorizer_event.html#aws_lambda_powertools.utilities.data_classes.appsync_authorizer_event.AppSyncAuthorizerEventRequestContext)
- [AppSyncIdentityCognito](appsync_resolver_event.html#aws_lambda_powertools.utilities.data_classes.appsync_resolver_event.AppSyncIdentityCognito)
- [AppSyncIdentityIAM](appsync_resolver_event.html#aws_lambda_powertools.utilities.data_classes.appsync_resolver_event.AppSyncIdentityIAM)
- [AppSyncResolverEvent](appsync_resolver_event.html#aws_lambda_powertools.utilities.data_classes.appsync_resolver_event.AppSyncResolverEvent)
- [AppSyncResolverEventInfo](appsync_resolver_event.html#aws_lambda_powertools.utilities.data_classes.appsync_resolver_event.AppSyncResolverEventInfo)
- [AWSConfigConfigurationChanged](aws_config_rule_event.html#aws_lambda_powertools.utilities.data_classes.aws_config_rule_event.AWSConfigConfigurationChanged)
- [AWSConfigConfigurationItemChanged](aws_config_rule_event.html#aws_lambda_powertools.utilities.data_classes.aws_config_rule_event.AWSConfigConfigurationItemChanged)
- [AWSConfigOversizedConfiguration](aws_config_rule_event.html#aws_lambda_powertools.utilities.data_classes.aws_config_rule_event.AWSConfigOversizedConfiguration)
- [AWSConfigOversizedConfigurationItemSummary](aws_config_rule_event.html#aws_lambda_powertools.utilities.data_classes.aws_config_rule_event.AWSConfigOversizedConfigurationItemSummary)
- [AWSConfigRuleEvent](aws_config_rule_event.html#aws_lambda_powertools.utilities.data_classes.aws_config_rule_event.AWSConfigRuleEvent)
- [AWSConfigScheduledNotification](aws_config_rule_event.html#aws_lambda_powertools.utilities.data_classes.aws_config_rule_event.AWSConfigScheduledNotification)
- [BedrockAgentInfo](bedrock_agent_event.html#aws_lambda_powertools.utilities.data_classes.bedrock_agent_event.BedrockAgentInfo)
- [BedrockAgentProperty](bedrock_agent_event.html#aws_lambda_powertools.utilities.data_classes.bedrock_agent_event.BedrockAgentProperty)
- [BedrockAgentRequestBody](bedrock_agent_event.html#aws_lambda_powertools.utilities.data_classes.bedrock_agent_event.BedrockAgentRequestBody)
- [BedrockAgentRequestMedia](bedrock_agent_event.html#aws_lambda_powertools.utilities.data_classes.bedrock_agent_event.BedrockAgentRequestMedia)
- [CloudWatchAlarmConfiguration](cloud_watch_alarm_event.html#aws_lambda_powertools.utilities.data_classes.cloud_watch_alarm_event.CloudWatchAlarmConfiguration)
- [CloudWatchAlarmData](cloud_watch_alarm_event.html#aws_lambda_powertools.utilities.data_classes.cloud_watch_alarm_event.CloudWatchAlarmData)
- [CloudWatchAlarmEvent](cloud_watch_alarm_event.html#aws_lambda_powertools.utilities.data_classes.cloud_watch_alarm_event.CloudWatchAlarmEvent)
- [CloudWatchAlarmMetric](cloud_watch_alarm_event.html#aws_lambda_powertools.utilities.data_classes.cloud_watch_alarm_event.CloudWatchAlarmMetric)
- [CloudWatchAlarmMetricStat](cloud_watch_alarm_event.html#aws_lambda_powertools.utilities.data_classes.cloud_watch_alarm_event.CloudWatchAlarmMetricStat)
- [CloudWatchAlarmState](cloud_watch_alarm_event.html#aws_lambda_powertools.utilities.data_classes.cloud_watch_alarm_event.CloudWatchAlarmState)
- [CloudWatchDashboardCustomWidgetEvent](cloud_watch_custom_widget_event.html#aws_lambda_powertools.utilities.data_classes.cloud_watch_custom_widget_event.CloudWatchDashboardCustomWidgetEvent)
- [CloudWatchWidgetContext](cloud_watch_custom_widget_event.html#aws_lambda_powertools.utilities.data_classes.cloud_watch_custom_widget_event.CloudWatchWidgetContext)
- [TimeRange](cloud_watch_custom_widget_event.html#aws_lambda_powertools.utilities.data_classes.cloud_watch_custom_widget_event.TimeRange)
- [TimeZone](cloud_watch_custom_widget_event.html#aws_lambda_powertools.utilities.data_classes.cloud_watch_custom_widget_event.TimeZone)
- [CloudWatchLogsDecodedData](cloud_watch_logs_event.html#aws_lambda_powertools.utilities.data_classes.cloud_watch_logs_event.CloudWatchLogsDecodedData)
- [CloudWatchLogsEvent](cloud_watch_logs_event.html#aws_lambda_powertools.utilities.data_classes.cloud_watch_logs_event.CloudWatchLogsEvent)
- [CloudWatchLogsLogEvent](cloud_watch_logs_event.html#aws_lambda_powertools.utilities.data_classes.cloud_watch_logs_event.CloudWatchLogsLogEvent)
- [CloudFormationCustomResourceEvent](cloudformation_custom_resource_event.html#aws_lambda_powertools.utilities.data_classes.cloudformation_custom_resource_event.CloudFormationCustomResourceEvent)
- [CodeDeployLifecycleHookEvent](code_deploy_lifecycle_hook_event.html#aws_lambda_powertools.utilities.data_classes.code_deploy_lifecycle_hook_event.CodeDeployLifecycleHookEvent)
- [CodePipelineActionConfiguration](code_pipeline_job_event.html#aws_lambda_powertools.utilities.data_classes.code_pipeline_job_event.CodePipelineActionConfiguration)
- [CodePipelineArtifact](code_pipeline_job_event.html#aws_lambda_powertools.utilities.data_classes.code_pipeline_job_event.CodePipelineArtifact)
- [CodePipelineArtifactCredentials](code_pipeline_job_event.html#aws_lambda_powertools.utilities.data_classes.code_pipeline_job_event.CodePipelineArtifactCredentials)
- [CodePipelineConfiguration](code_pipeline_job_event.html#aws_lambda_powertools.utilities.data_classes.code_pipeline_job_event.CodePipelineConfiguration)
- [CodePipelineData](code_pipeline_job_event.html#aws_lambda_powertools.utilities.data_classes.code_pipeline_job_event.CodePipelineData)
- [CodePipelineEncryptionKey](code_pipeline_job_event.html#aws_lambda_powertools.utilities.data_classes.code_pipeline_job_event.CodePipelineEncryptionKey)
- [CodePipelineJobEvent](code_pipeline_job_event.html#aws_lambda_powertools.utilities.data_classes.code_pipeline_job_event.CodePipelineJobEvent)
- [CodePipelineLocation](code_pipeline_job_event.html#aws_lambda_powertools.utilities.data_classes.code_pipeline_job_event.CodePipelineLocation)
- [CodePipelineS3Location](code_pipeline_job_event.html#aws_lambda_powertools.utilities.data_classes.code_pipeline_job_event.CodePipelineS3Location)
- [BaseTriggerEvent](cognito_user_pool_event.html#aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event.BaseTriggerEvent)
- [CallerContext](cognito_user_pool_event.html#aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event.CallerContext)
- [ChallengeResult](cognito_user_pool_event.html#aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event.ChallengeResult)
- [ClaimsAndScopeOverrideDetails](cognito_user_pool_event.html#aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event.ClaimsAndScopeOverrideDetails)
- [ClaimsOverrideDetails](cognito_user_pool_event.html#aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event.ClaimsOverrideDetails)
- [CreateAuthChallengeTriggerEventRequest](cognito_user_pool_event.html#aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event.CreateAuthChallengeTriggerEventRequest)
- [CreateAuthChallengeTriggerEventResponse](cognito_user_pool_event.html#aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event.CreateAuthChallengeTriggerEventResponse)
- [CustomEmailSenderTriggerEventRequest](cognito_user_pool_event.html#aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event.CustomEmailSenderTriggerEventRequest)
- [CustomMessageTriggerEventRequest](cognito_user_pool_event.html#aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event.CustomMessageTriggerEventRequest)
- [CustomMessageTriggerEventResponse](cognito_user_pool_event.html#aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event.CustomMessageTriggerEventResponse)
- [CustomSMSSenderTriggerEventRequest](cognito_user_pool_event.html#aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event.CustomSMSSenderTriggerEventRequest)
- [DefineAuthChallengeTriggerEventRequest](cognito_user_pool_event.html#aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event.DefineAuthChallengeTriggerEventRequest)
- [DefineAuthChallengeTriggerEventResponse](cognito_user_pool_event.html#aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event.DefineAuthChallengeTriggerEventResponse)
- [GroupOverrideDetails](cognito_user_pool_event.html#aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event.GroupOverrideDetails)
- [PostAuthenticationTriggerEventRequest](cognito_user_pool_event.html#aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event.PostAuthenticationTriggerEventRequest)
- [PostConfirmationTriggerEventRequest](cognito_user_pool_event.html#aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event.PostConfirmationTriggerEventRequest)
- [PreAuthenticationTriggerEventRequest](cognito_user_pool_event.html#aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event.PreAuthenticationTriggerEventRequest)
- [PreSignUpTriggerEventRequest](cognito_user_pool_event.html#aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event.PreSignUpTriggerEventRequest)
- [PreSignUpTriggerEventResponse](cognito_user_pool_event.html#aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event.PreSignUpTriggerEventResponse)
- [PreTokenGenerationTriggerEventRequest](cognito_user_pool_event.html#aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event.PreTokenGenerationTriggerEventRequest)
- [PreTokenGenerationTriggerEventResponse](cognito_user_pool_event.html#aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event.PreTokenGenerationTriggerEventResponse)
- [PreTokenGenerationTriggerV2EventResponse](cognito_user_pool_event.html#aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event.PreTokenGenerationTriggerV2EventResponse)
- [TokenClaimsAndScopeOverrideDetails](cognito_user_pool_event.html#aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event.TokenClaimsAndScopeOverrideDetails)
- [UserMigrationTriggerEventRequest](cognito_user_pool_event.html#aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event.UserMigrationTriggerEventRequest)
- [UserMigrationTriggerEventResponse](cognito_user_pool_event.html#aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event.UserMigrationTriggerEventResponse)
- [VerifyAuthChallengeResponseTriggerEventRequest](cognito_user_pool_event.html#aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event.VerifyAuthChallengeResponseTriggerEventRequest)
- [VerifyAuthChallengeResponseTriggerEventResponse](cognito_user_pool_event.html#aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event.VerifyAuthChallengeResponseTriggerEventResponse)
- [APIGatewayEventIdentity](#aws_lambda_powertools.utilities.data_classes.common.APIGatewayEventIdentity)
- [BaseProxyEvent](#aws_lambda_powertools.utilities.data_classes.common.BaseProxyEvent)
- [BaseRequestContext](#aws_lambda_powertools.utilities.data_classes.common.BaseRequestContext)
- [BaseRequestContextV2](#aws_lambda_powertools.utilities.data_classes.common.BaseRequestContextV2)
- [RequestContextClientCert](#aws_lambda_powertools.utilities.data_classes.common.RequestContextClientCert)
- [RequestContextV2Http](#aws_lambda_powertools.utilities.data_classes.common.RequestContextV2Http)
- [ConnectContactFlowData](connect_contact_flow_event.html#aws_lambda_powertools.utilities.data_classes.connect_contact_flow_event.ConnectContactFlowData)
- [ConnectContactFlowEndpoint](connect_contact_flow_event.html#aws_lambda_powertools.utilities.data_classes.connect_contact_flow_event.ConnectContactFlowEndpoint)
- [ConnectContactFlowEvent](connect_contact_flow_event.html#aws_lambda_powertools.utilities.data_classes.connect_contact_flow_event.ConnectContactFlowEvent)
- [ConnectContactFlowMediaStreamAudio](connect_contact_flow_event.html#aws_lambda_powertools.utilities.data_classes.connect_contact_flow_event.ConnectContactFlowMediaStreamAudio)
- [ConnectContactFlowMediaStreamCustomer](connect_contact_flow_event.html#aws_lambda_powertools.utilities.data_classes.connect_contact_flow_event.ConnectContactFlowMediaStreamCustomer)
- [ConnectContactFlowMediaStreams](connect_contact_flow_event.html#aws_lambda_powertools.utilities.data_classes.connect_contact_flow_event.ConnectContactFlowMediaStreams)
- [ConnectContactFlowQueue](connect_contact_flow_event.html#aws_lambda_powertools.utilities.data_classes.connect_contact_flow_event.ConnectContactFlowQueue)
- [DynamoDBRecord](dynamo_db_stream_event.html#aws_lambda_powertools.utilities.data_classes.dynamo_db_stream_event.DynamoDBRecord)
- [DynamoDBStreamEvent](dynamo_db_stream_event.html#aws_lambda_powertools.utilities.data_classes.dynamo_db_stream_event.DynamoDBStreamEvent)
- [StreamRecord](dynamo_db_stream_event.html#aws_lambda_powertools.utilities.data_classes.dynamo_db_stream_event.StreamRecord)
- [EventBridgeEvent](event_bridge_event.html#aws_lambda_powertools.utilities.data_classes.event_bridge_event.EventBridgeEvent)
- [KafkaEvent](kafka_event.html#aws_lambda_powertools.utilities.data_classes.kafka_event.KafkaEvent)
- [KafkaEventRecord](kafka_event.html#aws_lambda_powertools.utilities.data_classes.kafka_event.KafkaEventRecord)
- [KinesisFirehoseEvent](kinesis_firehose_event.html#aws_lambda_powertools.utilities.data_classes.kinesis_firehose_event.KinesisFirehoseEvent)
- [KinesisFirehoseRecord](kinesis_firehose_event.html#aws_lambda_powertools.utilities.data_classes.kinesis_firehose_event.KinesisFirehoseRecord)
- [KinesisFirehoseRecordMetadata](kinesis_firehose_event.html#aws_lambda_powertools.utilities.data_classes.kinesis_firehose_event.KinesisFirehoseRecordMetadata)
- [KinesisStreamEvent](kinesis_stream_event.html#aws_lambda_powertools.utilities.data_classes.kinesis_stream_event.KinesisStreamEvent)
- [KinesisStreamRecord](kinesis_stream_event.html#aws_lambda_powertools.utilities.data_classes.kinesis_stream_event.KinesisStreamRecord)
- [KinesisStreamRecordPayload](kinesis_stream_event.html#aws_lambda_powertools.utilities.data_classes.kinesis_stream_event.KinesisStreamRecordPayload)
- [BasicProperties](rabbit_mq_event.html#aws_lambda_powertools.utilities.data_classes.rabbit_mq_event.BasicProperties)
- [RabbitMQEvent](rabbit_mq_event.html#aws_lambda_powertools.utilities.data_classes.rabbit_mq_event.RabbitMQEvent)
- [RabbitMessage](rabbit_mq_event.html#aws_lambda_powertools.utilities.data_classes.rabbit_mq_event.RabbitMessage)
- [S3BatchOperationEvent](s3_batch_operation_event.html#aws_lambda_powertools.utilities.data_classes.s3_batch_operation_event.S3BatchOperationEvent)
- [S3BatchOperationJob](s3_batch_operation_event.html#aws_lambda_powertools.utilities.data_classes.s3_batch_operation_event.S3BatchOperationJob)
- [S3BatchOperationTask](s3_batch_operation_event.html#aws_lambda_powertools.utilities.data_classes.s3_batch_operation_event.S3BatchOperationTask)
- [S3Bucket](s3_event.html#aws_lambda_powertools.utilities.data_classes.s3_event.S3Bucket)
- [S3Event](s3_event.html#aws_lambda_powertools.utilities.data_classes.s3_event.S3Event)
- [S3EventBridgeNotificationDetail](s3_event.html#aws_lambda_powertools.utilities.data_classes.s3_event.S3EventBridgeNotificationDetail)
- [S3EventBridgeNotificationObject](s3_event.html#aws_lambda_powertools.utilities.data_classes.s3_event.S3EventBridgeNotificationObject)
- [S3EventNotificationEventBridgeBucket](s3_event.html#aws_lambda_powertools.utilities.data_classes.s3_event.S3EventNotificationEventBridgeBucket)
- [S3EventRecord](s3_event.html#aws_lambda_powertools.utilities.data_classes.s3_event.S3EventRecord)
- [S3EventRecordGlacierEventData](s3_event.html#aws_lambda_powertools.utilities.data_classes.s3_event.S3EventRecordGlacierEventData)
- [S3EventRecordGlacierRestoreEventData](s3_event.html#aws_lambda_powertools.utilities.data_classes.s3_event.S3EventRecordGlacierRestoreEventData)
- [S3Identity](s3_event.html#aws_lambda_powertools.utilities.data_classes.s3_event.S3Identity)
- [S3Message](s3_event.html#aws_lambda_powertools.utilities.data_classes.s3_event.S3Message)
- [S3Object](s3_event.html#aws_lambda_powertools.utilities.data_classes.s3_event.S3Object)
- [S3RequestParameters](s3_event.html#aws_lambda_powertools.utilities.data_classes.s3_event.S3RequestParameters)
- [S3ObjectConfiguration](s3_object_event.html#aws_lambda_powertools.utilities.data_classes.s3_object_event.S3ObjectConfiguration)
- [S3ObjectContext](s3_object_event.html#aws_lambda_powertools.utilities.data_classes.s3_object_event.S3ObjectContext)
- [S3ObjectLambdaEvent](s3_object_event.html#aws_lambda_powertools.utilities.data_classes.s3_object_event.S3ObjectLambdaEvent)
- [S3ObjectSessionAttributes](s3_object_event.html#aws_lambda_powertools.utilities.data_classes.s3_object_event.S3ObjectSessionAttributes)
- [S3ObjectSessionContext](s3_object_event.html#aws_lambda_powertools.utilities.data_classes.s3_object_event.S3ObjectSessionContext)
- [S3ObjectSessionIssuer](s3_object_event.html#aws_lambda_powertools.utilities.data_classes.s3_object_event.S3ObjectSessionIssuer)
- [S3ObjectUserIdentity](s3_object_event.html#aws_lambda_powertools.utilities.data_classes.s3_object_event.S3ObjectUserIdentity)
- [S3ObjectUserRequest](s3_object_event.html#aws_lambda_powertools.utilities.data_classes.s3_object_event.S3ObjectUserRequest)
- [SecretsManagerEvent](secrets_manager_event.html#aws_lambda_powertools.utilities.data_classes.secrets_manager_event.SecretsManagerEvent)
- [SESEvent](ses_event.html#aws_lambda_powertools.utilities.data_classes.ses_event.SESEvent)
- [SESEventRecord](ses_event.html#aws_lambda_powertools.utilities.data_classes.ses_event.SESEventRecord)
- [SESMail](ses_event.html#aws_lambda_powertools.utilities.data_classes.ses_event.SESMail)
- [SESMailCommonHeaders](ses_event.html#aws_lambda_powertools.utilities.data_classes.ses_event.SESMailCommonHeaders)
- [SESMailHeader](ses_event.html#aws_lambda_powertools.utilities.data_classes.ses_event.SESMailHeader)
- [SESMessage](ses_event.html#aws_lambda_powertools.utilities.data_classes.ses_event.SESMessage)
- [SESReceipt](ses_event.html#aws_lambda_powertools.utilities.data_classes.ses_event.SESReceipt)
- [SESReceiptAction](ses_event.html#aws_lambda_powertools.utilities.data_classes.ses_event.SESReceiptAction)
- [SESReceiptStatus](ses_event.html#aws_lambda_powertools.utilities.data_classes.ses_event.SESReceiptStatus)
- [SNSEvent](sns_event.html#aws_lambda_powertools.utilities.data_classes.sns_event.SNSEvent)
- [SNSEventRecord](sns_event.html#aws_lambda_powertools.utilities.data_classes.sns_event.SNSEventRecord)
- [SNSMessage](sns_event.html#aws_lambda_powertools.utilities.data_classes.sns_event.SNSMessage)
- [SNSMessageAttribute](sns_event.html#aws_lambda_powertools.utilities.data_classes.sns_event.SNSMessageAttribute)
- [SQSEvent](sqs_event.html#aws_lambda_powertools.utilities.data_classes.sqs_event.SQSEvent)
- [SQSMessageAttribute](sqs_event.html#aws_lambda_powertools.utilities.data_classes.sqs_event.SQSMessageAttribute)
- [SQSRecord](sqs_event.html#aws_lambda_powertools.utilities.data_classes.sqs_event.SQSRecord)
- [SQSRecordAttributes](sqs_event.html#aws_lambda_powertools.utilities.data_classes.sqs_event.SQSRecordAttributes)
- [TransferFamilyAuthorizer](transfer_family_event.html#aws_lambda_powertools.utilities.data_classes.transfer_family_event.TransferFamilyAuthorizer)
- [vpcLatticeEventV2Identity](vpc_lattice.html#aws_lambda_powertools.utilities.data_classes.vpc_lattice.vpcLatticeEventV2Identity)
- [vpcLatticeEventV2RequestContext](vpc_lattice.html#aws_lambda_powertools.utilities.data_classes.vpc_lattice.vpcLatticeEventV2RequestContext)
 ### Instance variables- `prop raw_event : dict[str, Any]`
- 
## Expand source code`@property def raw_event(self) -> dict[str, Any]: """The original raw event dict""" return self._data`The original raw event dict 
 ### Methods- `def get(self, key: str, default: Any | None = None) ‑> typing.Any | None`
- 
## Expand source code`def get(self, key: str, default: Any | None = None) -> Any | None: return self._data.get(key, default)`D.get(k[,d]) -> D[k] if k in D, else d. d defaults to None. 
 
- `class RequestContextClientCert (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class RequestContextClientCert(DictWrapper): @property def client_cert_pem(self) -> str: """Client certificate pem""" return self["clientCertPem"] @property def issuer_dn(self) -> str: """Issuer Distinguished Name""" return self["issuerDN"] @property def serial_number(self) -> str: """Unique serial number for client cert""" return self["serialNumber"] @property def subject_dn(self) -> str: """Subject Distinguished Name""" return self["subjectDN"] @property def validity_not_after(self) -> str: """Date when the cert is no longer valid eg: Aug 5 00:28:21 2120 GMT""" return self["validity"]["notAfter"] @property def validity_not_before(self) -> str: """Cert is not valid before this date eg: Aug 29 00:28:21 2020 GMT""" return self["validity"]["notBefore"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [DictWrapper](#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- `prop client_cert_pem : str`
- 
## Expand source code`@property def client_cert_pem(self) -> str: """Client certificate pem""" return self["clientCertPem"]`Client certificate pem 
- `prop issuer_dn : str`
- 
## Expand source code`@property def issuer_dn(self) -> str: """Issuer Distinguished Name""" return self["issuerDN"]`Issuer Distinguished Name 
- `prop serial_number : str`
- 
## Expand source code`@property def serial_number(self) -> str: """Unique serial number for client cert""" return self["serialNumber"]`Unique serial number for client cert 
- `prop subject_dn : str`
- 
## Expand source code`@property def subject_dn(self) -> str: """Subject Distinguished Name""" return self["subjectDN"]`Subject Distinguished Name 
- `prop validity_not_after : str`
- 
## Expand source code`@property def validity_not_after(self) -> str: """Date when the cert is no longer valid eg: Aug 5 00:28:21 2120 GMT""" return self["validity"]["notAfter"]`Date when the cert is no longer valid eg: Aug 5 00:28:21 2120 GMT 
- `prop validity_not_before : str`
- 
## Expand source code`@property def validity_not_before(self) -> str: """Cert is not valid before this date eg: Aug 29 00:28:21 2020 GMT""" return self["validity"]["notBefore"]`Cert is not valid before this date eg: Aug 29 00:28:21 2020 GMT 
 ### Inherited members
- `class RequestContextV2Http (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class RequestContextV2Http(DictWrapper): @property def method(self) -> str: return self["requestContext"]["http"]["method"] @property def path(self) -> str: return self["requestContext"]["http"]["path"] @property def protocol(self) -> str: """The request protocol, for example, HTTP/1.1.""" return self["requestContext"]["http"]["protocol"] @property def source_ip(self) -> str: """The source IP address of the TCP connection making the request to API Gateway.""" return self["requestContext"]["http"]["sourceIp"] @property def user_agent(self) -> str: """The User Agent of the API caller.""" return self["requestContext"]["http"]["userAgent"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [DictWrapper](#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- `prop method : str`
- 
## Expand source code`@property def method(self) -> str: return self["requestContext"]["http"]["method"]`
- `prop path : str`
- 
## Expand source code`@property def path(self) -> str: return self["requestContext"]["http"]["path"]`
- `prop protocol : str`
- 
## Expand source code`@property def protocol(self) -> str: """The request protocol, for example, HTTP/1.1.""" return self["requestContext"]["http"]["protocol"]`The request protocol, for example, HTTP/1.1. 
- `prop source_ip : str`
- 
## Expand source code`@property def source_ip(self) -> str: """The source IP address of the TCP connection making the request to API Gateway.""" return self["requestContext"]["http"]["sourceIp"]`The source IP address of the TCP connection making the request to API Gateway. 
- `prop user_agent : str`
- 
## Expand source code`@property def user_agent(self) -> str: """The User Agent of the API caller.""" return self["requestContext"]["http"]["userAgent"]`The User Agent of the API caller. 
 ### Inherited members