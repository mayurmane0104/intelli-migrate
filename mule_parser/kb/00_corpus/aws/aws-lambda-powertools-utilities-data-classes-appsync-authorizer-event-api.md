# aws_lambda_powertools.utilities.data_classes.appsync_authorizer_event API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/appsync_authorizer_event.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/appsync_authorizer_event.html)

---

# Module `aws_lambda_powertools.utilities.data_classes.appsync_authorizer_event`

## Classes

- 
## Expand source code`class AppSyncAuthorizerEvent(DictWrapper): """AppSync lambda authorizer event Documentation: ------------- - https://aws.amazon.com/blogs/mobile/appsync-lambda-auth/ - https://docs.aws.amazon.com/appsync/latest/devguide/security-authz.html#aws-lambda-authorization - https://docs.amplify.aws/lib/graphqlapi/authz/q/platform/js#aws-lambda """ @property def authorization_token(self) -> str: """Authorization token""" return self["authorizationToken"] @property def request_context(self) -> AppSyncAuthorizerEventRequestContext: """Request context""" return AppSyncAuthorizerEventRequestContext(self._data)`AppSync lambda authorizer event ## Documentation:- [https://aws.amazon.com/blogs/mobile/appsync-lambda-auth/](https://aws.amazon.com/blogs/mobile/appsync-lambda-auth/)
- [https://docs.aws.amazon.com/appsync/latest/devguide/security-authz.html#aws-lambda-authorization](https://docs.aws.amazon.com/appsync/latest/devguide/security-authz.html#aws-lambda-authorization)
- [https://docs.amplify.aws/lib/graphqlapi/authz/q/platform/js#aws-lambda](https://docs.amplify.aws/lib/graphqlapi/authz/q/platform/js#aws-lambda)
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
 ### Instance variables- 
## Expand source code`@property def authorization_token(self) -> str: """Authorization token""" return self["authorizationToken"]`Authorization token 
- 
## Expand source code`@property def request_context(self) -> AppSyncAuthorizerEventRequestContext: """Request context""" return AppSyncAuthorizerEventRequestContext(self._data)`Request context 
 ### Inherited members
- 
## Expand source code`class AppSyncAuthorizerEventRequestContext(DictWrapper): """Request context""" @property def api_id(self) -> str: """AppSync API ID""" return self["requestContext"]["apiId"] @property def account_id(self) -> str: """AWS Account ID""" return self["requestContext"]["accountId"] @property def request_id(self) -> str: """Requestt ID""" return self["requestContext"]["requestId"] @property def query_string(self) -> str: """GraphQL query string""" return self["requestContext"]["queryString"] @property def operation_name(self) -> str | None: """GraphQL operation name, optional""" return self["requestContext"].get("operationName") @property def variables(self) -> dict: """GraphQL variables""" return self["requestContext"]["variables"]`Request context ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- 
## Expand source code`@property def account_id(self) -> str: """AWS Account ID""" return self["requestContext"]["accountId"]`AWS Account ID 
- 
## Expand source code`@property def api_id(self) -> str: """AppSync API ID""" return self["requestContext"]["apiId"]`AppSync API ID 
- 
## Expand source code`@property def operation_name(self) -> str | None: """GraphQL operation name, optional""" return self["requestContext"].get("operationName")`GraphQL operation name, optional 
- 
## Expand source code`@property def query_string(self) -> str: """GraphQL query string""" return self["requestContext"]["queryString"]`GraphQL query string 
- 
## Expand source code`@property def request_id(self) -> str: """Requestt ID""" return self["requestContext"]["requestId"]`Requestt ID 
- 
## Expand source code`@property def variables(self) -> dict: """GraphQL variables""" return self["requestContext"]["variables"]`GraphQL variables 
 ### Inherited members
- 
## Expand source code`class AppSyncAuthorizerResponse: """AppSync Lambda authorizer response helper Parameters ---------- authorize: bool authorize is a boolean value indicating if the value in authorizationToken is authorized to make calls to the GraphQL API. If this value is true, execution of the GraphQL API continues. If this value is false, an UnauthorizedException is raised max_age: int, optional Set the ttlOverride. The number of seconds that the response should be cached for. If no value is returned, the value from the API (if configured) or the default of 300 seconds (five minutes) is used. If this is 0, the response is not cached. resolver_context: dict[str, Any], optional A JSON object visible as `$ctx.identity.resolverContext` in resolver templates The resolverContext object only supports key-value pairs. Nested keys are not supported. Warning: The total size of this JSON object must not exceed 5MB. deny_fields: list[str], optional A list of fields that will be set to `null` regardless of the resolver's return. A field is either `TypeName.FieldName`, or an ARN such as `arn:aws:appsync:us-east-1:111122223333:apis/GraphQLApiId/types/TypeName/fields/FieldName` Use the full ARN for correctness when sharing a Lambda function authorizer between APIs. """ def __init__( self, authorize: bool = False, max_age: int | None = None, resolver_context: dict[str, Any] | None = None, deny_fields: list[str] | None = None, ): self.authorize = authorize self.max_age = max_age self.deny_fields = deny_fields self.resolver_context = resolver_context def asdict(self) -> dict: """Return the response as a dict""" response: dict = {"isAuthorized": self.authorize} if self.max_age is not None: response["ttlOverride"] = self.max_age if self.deny_fields: response["deniedFields"] = self.deny_fields if self.resolver_context: response["resolverContext"] = self.resolver_context return response`AppSync Lambda authorizer response helper ## Parameters- `authorize`- `bool`
- authorize is a boolean value indicating if the value in authorizationToken is authorized to make calls to the GraphQL API. If this value is true, execution of the GraphQL API continues. If this value is false, an UnauthorizedException is raised
- `max_age`- `int`, optional
- Set the ttlOverride. The number of seconds that the response should be cached for. If no value is returned, the value from the API (if configured) or the default of 300 seconds (five minutes) is used. If this is 0, the response is not cached.
- `resolver_context`- `dict[str, Any]`, optional
- 
A JSON object visible as `$ctx.identity.resolverContext`in resolver templatesThe resolverContext object only supports key-value pairs. Nested keys are not supported. Warning: The total size of this JSON object must not exceed 5MB. 
- `deny_fields`- `list[str]`, optional
- 
A list of fields that will be set to `null`regardless of the resolver's return.A field is either `TypeName.FieldName`, or an ARN such as`arn:aws:appsync:us-east-1:111122223333:apis/GraphQLApiId/types/TypeName/fields/FieldName`Use the full ARN for correctness when sharing a Lambda function authorizer between APIs. 
 ### Methods- 
## Expand source code`def asdict(self) -> dict: """Return the response as a dict""" response: dict = {"isAuthorized": self.authorize} if self.max_age is not None: response["ttlOverride"] = self.max_age if self.deny_fields: response["deniedFields"] = self.deny_fields if self.resolver_context: response["resolverContext"] = self.resolver_context return response`Return the response as a dict