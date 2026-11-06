# aws_lambda_powertools.utilities.data_classes API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/index.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/index.html)

---

# Module `aws_lambda_powertools.utilities.data_classes`

Event Source Data Classes utility provides classes self-describing Lambda event sources.

## Sub-modules

- [aws_lambda_powertools.utilities.data_classes.active_mq_event](active_mq_event.html)
- [aws_lambda_powertools.utilities.data_classes.alb_event](alb_event.html)
- [aws_lambda_powertools.utilities.data_classes.api_gateway_authorizer_event](api_gateway_authorizer_event.html)
- [aws_lambda_powertools.utilities.data_classes.api_gateway_proxy_event](api_gateway_proxy_event.html)
- [aws_lambda_powertools.utilities.data_classes.appsync](appsync/index.html)
- [aws_lambda_powertools.utilities.data_classes.appsync_authorizer_event](appsync_authorizer_event.html)
- [aws_lambda_powertools.utilities.data_classes.appsync_resolver_event](appsync_resolver_event.html)
- [aws_lambda_powertools.utilities.data_classes.aws_config_rule_event](aws_config_rule_event.html)
- [aws_lambda_powertools.utilities.data_classes.bedrock_agent_event](bedrock_agent_event.html)
- [aws_lambda_powertools.utilities.data_classes.cloud_watch_alarm_event](cloud_watch_alarm_event.html)
- [aws_lambda_powertools.utilities.data_classes.cloud_watch_custom_widget_event](cloud_watch_custom_widget_event.html)
- [aws_lambda_powertools.utilities.data_classes.cloud_watch_logs_event](cloud_watch_logs_event.html)
- [aws_lambda_powertools.utilities.data_classes.cloudformation_custom_resource_event](cloudformation_custom_resource_event.html)
- [aws_lambda_powertools.utilities.data_classes.code_deploy_lifecycle_hook_event](code_deploy_lifecycle_hook_event.html)
- [aws_lambda_powertools.utilities.data_classes.code_pipeline_job_event](code_pipeline_job_event.html)
- [aws_lambda_powertools.utilities.data_classes.cognito_user_pool_event](cognito_user_pool_event.html)
- [aws_lambda_powertools.utilities.data_classes.common](common.html)
- [aws_lambda_powertools.utilities.data_classes.connect_contact_flow_event](connect_contact_flow_event.html)
- [aws_lambda_powertools.utilities.data_classes.dynamo_db_stream_event](dynamo_db_stream_event.html)
- [aws_lambda_powertools.utilities.data_classes.event_bridge_event](event_bridge_event.html)
- [aws_lambda_powertools.utilities.data_classes.kafka_event](kafka_event.html)
- [aws_lambda_powertools.utilities.data_classes.kinesis_firehose_event](kinesis_firehose_event.html)
- [aws_lambda_powertools.utilities.data_classes.kinesis_stream_event](kinesis_stream_event.html)
- [aws_lambda_powertools.utilities.data_classes.lambda_function_url_event](lambda_function_url_event.html)
- [aws_lambda_powertools.utilities.data_classes.rabbit_mq_event](rabbit_mq_event.html)
- [aws_lambda_powertools.utilities.data_classes.s3_batch_operation_event](s3_batch_operation_event.html)
- [aws_lambda_powertools.utilities.data_classes.s3_event](s3_event.html)
- [aws_lambda_powertools.utilities.data_classes.s3_object_event](s3_object_event.html)
- [aws_lambda_powertools.utilities.data_classes.secrets_manager_event](secrets_manager_event.html)
- [aws_lambda_powertools.utilities.data_classes.ses_event](ses_event.html)
- [aws_lambda_powertools.utilities.data_classes.shared_functions](shared_functions.html)
- [aws_lambda_powertools.utilities.data_classes.sns_event](sns_event.html)
- [aws_lambda_powertools.utilities.data_classes.sqs_event](sqs_event.html)
- [aws_lambda_powertools.utilities.data_classes.transfer_family_event](transfer_family_event.html)
- [aws_lambda_powertools.utilities.data_classes.vpc_lattice](vpc_lattice.html)

## Functions

- `def event_source(handler: Callable[[Any, LambdaContext], Any],`
 event: dict[str, Any],
 context: LambdaContext,
 data_class: type[DictWrapper])
- 
## Expand source code`@lambda_handler_decorator def event_source( handler: Callable[[Any, LambdaContext], Any], event: dict[str, Any], context: LambdaContext, data_class: type[DictWrapper], ): """Middleware to create an instance of the passed in event source data class Parameters ---------- handler: Callable Lambda's handler event: dict[str, Any] Lambda's Event context: LambdaContext Lambda's Context data_class: type[DictWrapper] Data class type to instantiate Example -------- **Sample usage** from aws_lambda_powertools.utilities.data_classes import S3Event, event_source @event_source(data_class=S3Event) def handler(event: S3Event, context): return {"key": event.object_key} """ return handler(data_class(event), context)`Middleware to create an instance of the passed in event source data class ## Parameters- `handler`- `Callable`
- Lambda's handler
- `event`- `dict[str, Any]`
- Lambda's Event
- `context`- `LambdaContext`
- Lambda's Context
- `data_class`- `type[DictWrapper]`
- Data class type to instantiate
 ## Example**Sample usage**`from aws_lambda_powertools.utilities.data_classes import S3Event, event_source @event_source(data_class=S3Event) def handler(event: S3Event, context): return {"key": event.object_key}`

## Classes

- `class ALBEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class ALBEvent(BaseProxyEvent): """Application load balancer event Documentation: -------------- - https://docs.aws.amazon.com/lambda/latest/dg/services-alb.html - https://docs.aws.amazon.com/elasticloadbalancing/latest/application/lambda-functions.html """ @property def request_context(self) -> ALBEventRequestContext: return ALBEventRequestContext(self._data) @property def multi_value_query_string_parameters(self) -> dict[str, list[str]]: return self.get("multiValueQueryStringParameters") or {} @property def resolved_query_string_parameters(self) -> dict[str, list[str]]: return self.multi_value_query_string_parameters or super().resolved_query_string_parameters @property def multi_value_headers(self) -> dict[str, list[str]]: return CaseInsensitiveDict(self.get("multiValueHeaders")) @property def resolved_headers_field(self) -> dict[str, Any]: return self.multi_value_headers or self.headers def header_serializer(self) -> BaseHeadersSerializer: # When using the ALB integration, the `multiValueHeaders` feature can be disabled (default) or enabled. # We can determine if the feature is enabled by looking if the event has a `multiValueHeaders` key. if self.multi_value_headers: return MultiValueHeadersSerializer() return SingleValueHeadersSerializer()`Application load balancer event ## Documentation:- [https://docs.aws.amazon.com/lambda/latest/dg/services-alb.html](https://docs.aws.amazon.com/lambda/latest/dg/services-alb.html)
- [https://docs.aws.amazon.com/elasticloadbalancing/latest/application/lambda-functions.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/lambda-functions.html)
 ## Parameters- `data`- `dict[str, Any]`
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
## Expand source code`@property def multi_value_query_string_parameters(self) -> dict[str, list[str]]: return self.get("multiValueQueryStringParameters") or {}`
- `prop request_context : ALBEventRequestContext`
- 
## Expand source code`@property def request_context(self) -> ALBEventRequestContext: return ALBEventRequestContext(self._data)`
 ### Methods- `def header_serializer(self) ‑>`- [BaseHeadersSerializer](../../shared/headers_serializer.html#aws_lambda_powertools.shared.headers_serializer.BaseHeadersSerializer)
- 
## Expand source code`def header_serializer(self) -> BaseHeadersSerializer: # When using the ALB integration, the `multiValueHeaders` feature can be disabled (default) or enabled. # We can determine if the feature is enabled by looking if the event has a `multiValueHeaders` key. if self.multi_value_headers: return MultiValueHeadersSerializer() return SingleValueHeadersSerializer()`
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
- `prop request_context : APIGatewayEventRequestContext`
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
- `prop request_context : RequestContextV2`
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
- `class AWSConfigRuleEvent (data: dict[str, Any])`
- 
## Expand source code`class AWSConfigRuleEvent(DictWrapper): """Events for AWS Config Rules Documentation: -------------- - https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_lambda-functions.html """ def __init__(self, data: dict[str, Any]): super().__init__(data) self._invoking_event: Any | None = None self._rule_parameters: Any | None = None @property def version(self) -> str: """The version of the event.""" return self["version"] @property def invoking_event( self, ) -> AWSConfigConfigurationChanged | AWSConfigScheduledNotification | AWSConfigOversizedConfiguration: """The invoking payload of the event.""" if self._invoking_event is None: self._invoking_event = self._json_deserializer(self["invokingEvent"]) return get_invoke_event(self._invoking_event) @property def raw_invoking_event(self) -> str: """The raw invoking payload of the event.""" return self["invokingEvent"] @property def rule_parameters(self) -> dict: """The parameters of the event.""" if self._rule_parameters is None: self._rule_parameters = self._json_deserializer(self["ruleParameters"]) return self._rule_parameters @property def result_token(self) -> str: """The result token of the event.""" return self["resultToken"] @property def event_left_scope(self) -> bool: """The left scope of the event.""" return self["eventLeftScope"] @property def execution_role_arn(self) -> str: """The execution role arn of the event.""" return self["executionRoleArn"] @property def config_rule_arn(self) -> str: """The arn of the rule of the event.""" return self["configRuleArn"] @property def config_rule_name(self) -> str: """The name of the rule of the event.""" return self["configRuleName"] @property def config_rule_id(self) -> str: """The id of the rule of the event.""" return self["configRuleId"] @property def accountid(self) -> str: """The accountid of the event.""" return self["accountId"] @property def evalution_mode(self) -> str | None: """The evalution mode of the event.""" return self.get("evaluationMode")`Events for AWS Config Rules Documentation: 
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
 ### Instance variables- `prop accountid : str`
- 
## Expand source code`@property def accountid(self) -> str: """The accountid of the event.""" return self["accountId"]`The accountid of the event. 
- `prop config_rule_arn : str`
- 
## Expand source code`@property def config_rule_arn(self) -> str: """The arn of the rule of the event.""" return self["configRuleArn"]`The arn of the rule of the event. 
- `prop config_rule_id : str`
- 
## Expand source code`@property def config_rule_id(self) -> str: """The id of the rule of the event.""" return self["configRuleId"]`The id of the rule of the event. 
- `prop config_rule_name : str`
- 
## Expand source code`@property def config_rule_name(self) -> str: """The name of the rule of the event.""" return self["configRuleName"]`The name of the rule of the event. 
- `prop evalution_mode : str | None`
- 
## Expand source code`@property def evalution_mode(self) -> str | None: """The evalution mode of the event.""" return self.get("evaluationMode")`The evalution mode of the event. 
- `prop event_left_scope : bool`
- 
## Expand source code`@property def event_left_scope(self) -> bool: """The left scope of the event.""" return self["eventLeftScope"]`The left scope of the event. 
- `prop execution_role_arn : str`
- 
## Expand source code`@property def execution_role_arn(self) -> str: """The execution role arn of the event.""" return self["executionRoleArn"]`The execution role arn of the event. 
- `prop invoking_event : AWSConfigConfigurationChanged | AWSConfigScheduledNotification | AWSConfigOversizedConfiguration`
- 
## Expand source code`@property def invoking_event( self, ) -> AWSConfigConfigurationChanged | AWSConfigScheduledNotification | AWSConfigOversizedConfiguration: """The invoking payload of the event.""" if self._invoking_event is None: self._invoking_event = self._json_deserializer(self["invokingEvent"]) return get_invoke_event(self._invoking_event)`The invoking payload of the event. 
- `prop raw_invoking_event : str`
- 
## Expand source code`@property def raw_invoking_event(self) -> str: """The raw invoking payload of the event.""" return self["invokingEvent"]`The raw invoking payload of the event. 
- `prop result_token : str`
- 
## Expand source code`@property def result_token(self) -> str: """The result token of the event.""" return self["resultToken"]`The result token of the event. 
- `prop rule_parameters : dict`
- 
## Expand source code`@property def rule_parameters(self) -> dict: """The parameters of the event.""" if self._rule_parameters is None: self._rule_parameters = self._json_deserializer(self["ruleParameters"]) return self._rule_parameters`The parameters of the event. 
- `prop version : str`
- 
## Expand source code`@property def version(self) -> str: """The version of the event.""" return self["version"]`The version of the event. 
 ### Inherited members
- `class AppSyncResolverEvent (data: dict)`
- 
## Expand source code`class AppSyncResolverEvent(DictWrapper): """AppSync resolver event **NOTE:** AppSync Resolver Events can come in various shapes this data class supports both Amplify GraphQL directive @function and Direct Lambda Resolver Documentation: ------------- - https://docs.aws.amazon.com/appsync/latest/devguide/resolver-context-reference.html - https://docs.amplify.aws/cli/graphql-transformer/function#structure-of-the-function-event """ def __init__(self, data: dict): super().__init__(data) info: dict | None = data.get("info") if not info: parent_type_name = self.get("parentTypeName") or self.get("typeName") info = {"fieldName": self.get("fieldName"), "parentTypeName": parent_type_name} self._info = AppSyncResolverEventInfo(info) @property def type_name(self) -> str: """The name of the parent type for the field that is currently being resolved.""" return self.info.parent_type_name @property def field_name(self) -> str: """The name of the field that is currently being resolved.""" return self.info.field_name @property def arguments(self) -> dict[str, Any]: """A map that contains all GraphQL arguments for this field.""" return self["arguments"] @property def identity(self) -> AppSyncIdentityIAM | AppSyncIdentityCognito | None: """An object that contains information about the caller. Depending on the type of identify found: - API_KEY authorization - returns None - AWS_IAM authorization - returns AppSyncIdentityIAM - AMAZON_COGNITO_USER_POOLS authorization - returns AppSyncIdentityCognito """ return get_identity_object(self.get("identity")) @property def source(self) -> dict[str, Any]: """A map that contains the resolution of the parent field.""" return self.get("source") or {} @property def request_headers(self) -> dict[str, str]: """Request headers""" return CaseInsensitiveDict(self["request"]["headers"]) @property def prev_result(self) -> dict[str, Any] | None: """It represents the result of whatever previous operation was executed in a pipeline resolver.""" prev = self.get("prev") if not prev: return None return prev.get("result") @property def info(self) -> AppSyncResolverEventInfo: """The info section contains information about the GraphQL request.""" return self._info @property def stash(self) -> dict: """The stash is a map that is made available inside each resolver and function mapping template. The same stash instance lives through a single resolver execution. This means that you can use the stash to pass arbitrary data across request and response mapping templates, and across functions in a pipeline resolver.""" return self.get("stash") or {} @overload def get_header_value( self, name: str, default_value: str, case_sensitive: bool = False, ) -> str: ... @overload def get_header_value( self, name: str, default_value: str | None = None, case_sensitive: bool = False, ) -> str | None: ... @deprecated( "`get_header_value` function is deprecated; Access headers directly using event.headers.get('HeaderName')", category=None, ) def get_header_value( self, name: str, default_value: str | None = None, case_sensitive: bool = False, ) -> str | None: """Get header value by name Parameters ---------- name: str Header name default_value: str, optional Default value if no value was found by name case_sensitive: bool Whether to use a case-sensitive look up Returns ------- str, optional Header value """ warnings.warn( "The `get_header_value` function is deprecated in V3 and the `case_sensitive` parameter " "no longer has any effect. This function will be removed in the next major version. " "Instead, access headers directly using event.headers.get('HeaderName'), which is case insensitive.", category=PowertoolsDeprecationWarning, stacklevel=2, ) return get_header_value(self.request_headers, name, default_value, case_sensitive)`AppSync resolver event **NOTE:**AppSync Resolver Events can come in various shapes this data class supports both Amplify GraphQL directive @function and Direct Lambda Resolver## Documentation:- [https://docs.aws.amazon.com/appsync/latest/devguide/resolver-context-reference.html](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-context-reference.html)
- [https://docs.amplify.aws/cli/graphql-transformer/function#structure-of-the-function-event](https://docs.amplify.aws/cli/graphql-transformer/function#structure-of-the-function-event)
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
 ### Instance variables- `prop arguments : dict[str, Any]`
- 
## Expand source code`@property def arguments(self) -> dict[str, Any]: """A map that contains all GraphQL arguments for this field.""" return self["arguments"]`A map that contains all GraphQL arguments for this field. 
- `prop field_name : str`
- 
## Expand source code`@property def field_name(self) -> str: """The name of the field that is currently being resolved.""" return self.info.field_name`The name of the field that is currently being resolved. 
- `prop identity : AppSyncIdentityIAM | AppSyncIdentityCognito | None`
- 
## Expand source code`@property def identity(self) -> AppSyncIdentityIAM | AppSyncIdentityCognito | None: """An object that contains information about the caller. Depending on the type of identify found: - API_KEY authorization - returns None - AWS_IAM authorization - returns AppSyncIdentityIAM - AMAZON_COGNITO_USER_POOLS authorization - returns AppSyncIdentityCognito """ return get_identity_object(self.get("identity"))`An object that contains information about the caller. Depending on the type of identify found: - API_KEY authorization - returns None
- AWS_IAM authorization - returns AppSyncIdentityIAM
- AMAZON_COGNITO_USER_POOLS authorization - returns AppSyncIdentityCognito
 
- `prop info : AppSyncResolverEventInfo`
- 
## Expand source code`@property def info(self) -> AppSyncResolverEventInfo: """The info section contains information about the GraphQL request.""" return self._info`The info section contains information about the GraphQL request. 
- `prop prev_result : dict[str, Any] | None`
- 
## Expand source code`@property def prev_result(self) -> dict[str, Any] | None: """It represents the result of whatever previous operation was executed in a pipeline resolver.""" prev = self.get("prev") if not prev: return None return prev.get("result")`It represents the result of whatever previous operation was executed in a pipeline resolver. 
- `prop request_headers : dict[str, str]`
- 
## Expand source code`@property def request_headers(self) -> dict[str, str]: """Request headers""" return CaseInsensitiveDict(self["request"]["headers"])`Request headers 
- `prop source : dict[str, Any]`
- 
## Expand source code`@property def source(self) -> dict[str, Any]: """A map that contains the resolution of the parent field.""" return self.get("source") or {}`A map that contains the resolution of the parent field. 
- `prop stash : dict`
- 
## Expand source code`@property def stash(self) -> dict: """The stash is a map that is made available inside each resolver and function mapping template. The same stash instance lives through a single resolver execution. This means that you can use the stash to pass arbitrary data across request and response mapping templates, and across functions in a pipeline resolver.""" return self.get("stash") or {}`The stash is a map that is made available inside each resolver and function mapping template. The same stash instance lives through a single resolver execution. This means that you can use the stash to pass arbitrary data across request and response mapping templates, and across functions in a pipeline resolver. 
- `prop type_name : str`
- 
## Expand source code`@property def type_name(self) -> str: """The name of the parent type for the field that is currently being resolved.""" return self.info.parent_type_name`The name of the parent type for the field that is currently being resolved. 
 ### Methods- `def get_header_value(self, name: str, default_value: str | None = None, case_sensitive: bool = False) ‑> str | None`
- 
## Expand source code`@deprecated( "`get_header_value` function is deprecated; Access headers directly using event.headers.get('HeaderName')", category=None, ) def get_header_value( self, name: str, default_value: str | None = None, case_sensitive: bool = False, ) -> str | None: """Get header value by name Parameters ---------- name: str Header name default_value: str, optional Default value if no value was found by name case_sensitive: bool Whether to use a case-sensitive look up Returns ------- str, optional Header value """ warnings.warn( "The `get_header_value` function is deprecated in V3 and the `case_sensitive` parameter " "no longer has any effect. This function will be removed in the next major version. " "Instead, access headers directly using event.headers.get('HeaderName'), which is case insensitive.", category=PowertoolsDeprecationWarning, stacklevel=2, ) return get_header_value(self.request_headers, name, default_value, case_sensitive)`Get header value by name Parameters 
 - `name`- `str`
- Header name
- `default_value`- `str`, optional
- Default value if no value was found by name
- `case_sensitive`- `bool`
- Whether to use a case-sensitive look up
 ## Returns- `str`, optional
- Header value
 
 ### Inherited members
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
- `prop agent : BedrockAgentInfo`
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
- `prop parameters : list[BedrockAgentProperty]`
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
- `prop request_body : BedrockAgentRequestBody | None`
- 
## Expand source code`@property def request_body(self) -> BedrockAgentRequestBody | None: return BedrockAgentRequestBody(self["requestBody"]) if self.get("requestBody") else None`
- `prop session_attributes : dict[str, str]`
- 
## Expand source code`@property def session_attributes(self) -> dict[str, str]: return self["sessionAttributes"]`
- `prop session_id : str`
- 
## Expand source code`@property def session_id(self) -> str: return self["sessionId"]`
 ### Inherited members
- `class CloudFormationCustomResourceEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class CloudFormationCustomResourceEvent(DictWrapper): @property def request_type(self) -> Literal["Create", "Update", "Delete"]: return self["RequestType"] @property def service_token(self) -> str: return self["ServiceToken"] @property def response_url(self) -> str: return self["ResponseURL"] @property def stack_id(self) -> str: return self["StackId"] @property def request_id(self) -> str: return self["RequestId"] @property def logical_resource_id(self) -> str: return self["LogicalResourceId"] @property def physical_resource_id(self) -> str: return self.get("PhysicalResourceId") or "" @property def resource_type(self) -> str: return self["ResourceType"] @property def resource_properties(self) -> dict[str, Any]: return self.get("ResourceProperties") or {} @property def old_resource_properties(self) -> dict[str, Any]: return self.get("OldResourceProperties") or {}`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop logical_resource_id : str`
- 
## Expand source code`@property def logical_resource_id(self) -> str: return self["LogicalResourceId"]`
- `prop old_resource_properties : dict[str, Any]`
- 
## Expand source code`@property def old_resource_properties(self) -> dict[str, Any]: return self.get("OldResourceProperties") or {}`
- `prop physical_resource_id : str`
- 
## Expand source code`@property def physical_resource_id(self) -> str: return self.get("PhysicalResourceId") or ""`
- `prop request_id : str`
- 
## Expand source code`@property def request_id(self) -> str: return self["RequestId"]`
- `prop request_type : Literal['Create', 'Update', 'Delete']`
- 
## Expand source code`@property def request_type(self) -> Literal["Create", "Update", "Delete"]: return self["RequestType"]`
- `prop resource_properties : dict[str, Any]`
- 
## Expand source code`@property def resource_properties(self) -> dict[str, Any]: return self.get("ResourceProperties") or {}`
- `prop resource_type : str`
- 
## Expand source code`@property def resource_type(self) -> str: return self["ResourceType"]`
- `prop response_url : str`
- 
## Expand source code`@property def response_url(self) -> str: return self["ResponseURL"]`
- `prop service_token : str`
- 
## Expand source code`@property def service_token(self) -> str: return self["ServiceToken"]`
- `prop stack_id : str`
- 
## Expand source code`@property def stack_id(self) -> str: return self["StackId"]`
 ### Inherited members
- `class CloudWatchAlarmConfiguration (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class CloudWatchAlarmConfiguration(DictWrapper): @property def description(self) -> str | None: """ Optional description for the Alarm. """ return self.get("description", None) @property def alarm_rule(self) -> str | None: """ Optional description for the Alarm rule in case of composite alarm. """ return self.get("alarmRule", None) @property def alarm_actions_suppressor(self) -> str | None: """ Optional action suppression for the Alarm rule in case of composite alarm. """ return self.get("actionsSuppressor", None) @property def alarm_actions_suppressor_wait_period(self) -> str | None: """ Optional action suppression wait period for the Alarm rule in case of composite alarm. """ return self.get("actionsSuppressorWaitPeriod", None) @property def alarm_actions_suppressor_extension_period(self) -> str | None: """ Optional action suppression extension period for the Alarm rule in case of composite alarm. """ return self.get("actionsSuppressorExtensionPeriod", None) @property def metrics(self) -> list[CloudWatchAlarmMetric]: """ The metrics evaluated for the Alarm. """ metrics = self.get("metrics") or [] return [CloudWatchAlarmMetric(i) for i in metrics]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop alarm_actions_suppressor : str | None`
- 
## Expand source code`@property def alarm_actions_suppressor(self) -> str | None: """ Optional action suppression for the Alarm rule in case of composite alarm. """ return self.get("actionsSuppressor", None)`Optional action suppression for the Alarm rule in case of composite alarm. 
- `prop alarm_actions_suppressor_extension_period : str | None`
- 
## Expand source code`@property def alarm_actions_suppressor_extension_period(self) -> str | None: """ Optional action suppression extension period for the Alarm rule in case of composite alarm. """ return self.get("actionsSuppressorExtensionPeriod", None)`Optional action suppression extension period for the Alarm rule in case of composite alarm. 
- `prop alarm_actions_suppressor_wait_period : str | None`
- 
## Expand source code`@property def alarm_actions_suppressor_wait_period(self) -> str | None: """ Optional action suppression wait period for the Alarm rule in case of composite alarm. """ return self.get("actionsSuppressorWaitPeriod", None)`Optional action suppression wait period for the Alarm rule in case of composite alarm. 
- `prop alarm_rule : str | None`
- 
## Expand source code`@property def alarm_rule(self) -> str | None: """ Optional description for the Alarm rule in case of composite alarm. """ return self.get("alarmRule", None)`Optional description for the Alarm rule in case of composite alarm. 
- `prop description : str | None`
- 
## Expand source code`@property def description(self) -> str | None: """ Optional description for the Alarm. """ return self.get("description", None)`Optional description for the Alarm. 
- `prop metrics : list[`- [CloudWatchAlarmMetric](#aws_lambda_powertools.utilities.data_classes.CloudWatchAlarmMetric)]
- 
## Expand source code`@property def metrics(self) -> list[CloudWatchAlarmMetric]: """ The metrics evaluated for the Alarm. """ metrics = self.get("metrics") or [] return [CloudWatchAlarmMetric(i) for i in metrics]`The metrics evaluated for the Alarm. 
 ### Inherited members
- `class CloudWatchAlarmData (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class CloudWatchAlarmData(DictWrapper): @property def alarm_name(self) -> str: """ Alarm name. """ return self["alarmName"] @property def state(self) -> CloudWatchAlarmState: """ The current state of the Alarm. """ return CloudWatchAlarmState(self["state"]) @property def previous_state(self) -> CloudWatchAlarmState: """ The previous state of the Alarm. """ return CloudWatchAlarmState(self["previousState"]) @property def configuration(self) -> CloudWatchAlarmConfiguration: """ The configuration of the Alarm. """ return CloudWatchAlarmConfiguration(self["configuration"])`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop alarm_name : str`
- 
## Expand source code`@property def alarm_name(self) -> str: """ Alarm name. """ return self["alarmName"]`Alarm name. 
- `prop configuration :`- [CloudWatchAlarmConfiguration](#aws_lambda_powertools.utilities.data_classes.CloudWatchAlarmConfiguration)
- 
## Expand source code`@property def configuration(self) -> CloudWatchAlarmConfiguration: """ The configuration of the Alarm. """ return CloudWatchAlarmConfiguration(self["configuration"])`The configuration of the Alarm. 
- `prop previous_state :`- [CloudWatchAlarmState](#aws_lambda_powertools.utilities.data_classes.CloudWatchAlarmState)
- 
## Expand source code`@property def previous_state(self) -> CloudWatchAlarmState: """ The previous state of the Alarm. """ return CloudWatchAlarmState(self["previousState"])`The previous state of the Alarm. 
- `prop state :`- [CloudWatchAlarmState](#aws_lambda_powertools.utilities.data_classes.CloudWatchAlarmState)
- 
## Expand source code`@property def state(self) -> CloudWatchAlarmState: """ The current state of the Alarm. """ return CloudWatchAlarmState(self["state"])`The current state of the Alarm. 
 ### Inherited members
- `class CloudWatchAlarmEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class CloudWatchAlarmEvent(DictWrapper): @property def source(self) -> Literal["aws.cloudwatch"]: """ Source of the triggered event. """ return self["source"] @property def alarm_arn(self) -> str: """ The ARN of the CloudWatch Alarm. """ return self["alarmArn"] @property def region(self) -> str: """ The AWS region in which the Alarm is active. """ return self["region"] @property def source_account_id(self) -> str: """ The AWS Account ID that the Alarm is deployed to. """ return self["accountId"] @property def timestamp(self) -> str: """ Alarm state change event timestamp in ISO-8601 format. """ return self["time"] @property def alarm_data(self) -> CloudWatchAlarmData: """ Contains basic data about the Alarm and its current and previous states. """ return CloudWatchAlarmData(self["alarmData"])`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop alarm_arn : str`
- 
## Expand source code`@property def alarm_arn(self) -> str: """ The ARN of the CloudWatch Alarm. """ return self["alarmArn"]`The ARN of the CloudWatch Alarm. 
- `prop alarm_data :`- [CloudWatchAlarmData](#aws_lambda_powertools.utilities.data_classes.CloudWatchAlarmData)
- 
## Expand source code`@property def alarm_data(self) -> CloudWatchAlarmData: """ Contains basic data about the Alarm and its current and previous states. """ return CloudWatchAlarmData(self["alarmData"])`Contains basic data about the Alarm and its current and previous states. 
- `prop region : str`
- 
## Expand source code`@property def region(self) -> str: """ The AWS region in which the Alarm is active. """ return self["region"]`The AWS region in which the Alarm is active. 
- `prop source : Literal['aws.cloudwatch']`
- 
## Expand source code`@property def source(self) -> Literal["aws.cloudwatch"]: """ Source of the triggered event. """ return self["source"]`Source of the triggered event. 
- `prop source_account_id : str`
- 
## Expand source code`@property def source_account_id(self) -> str: """ The AWS Account ID that the Alarm is deployed to. """ return self["accountId"]`The AWS Account ID that the Alarm is deployed to. 
- `prop timestamp : str`
- 
## Expand source code`@property def timestamp(self) -> str: """ Alarm state change event timestamp in ISO-8601 format. """ return self["time"]`Alarm state change event timestamp in ISO-8601 format. 
 ### Inherited members
- `class CloudWatchAlarmMetric (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class CloudWatchAlarmMetric(DictWrapper): @property def metric_id(self) -> str: """ Unique ID of the alarm metric. """ return self["id"] @property def expression(self) -> str | None: """ Optional expression of the alarm metric. """ return self.get("expression", None) @property def label(self) -> str | None: """ Optional label of the alarm metric. """ return self.get("label", None) @property def return_data(self) -> bool: """ Whether this metric data is used to determine the state of the alarm or not. """ return self["returnData"] @property def metric_stat(self) -> CloudWatchAlarmMetricStat: return CloudWatchAlarmMetricStat(self["metricStat"])`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop expression : str | None`
- 
## Expand source code`@property def expression(self) -> str | None: """ Optional expression of the alarm metric. """ return self.get("expression", None)`Optional expression of the alarm metric. 
- `prop label : str | None`
- 
## Expand source code`@property def label(self) -> str | None: """ Optional label of the alarm metric. """ return self.get("label", None)`Optional label of the alarm metric. 
- `prop metric_id : str`
- 
## Expand source code`@property def metric_id(self) -> str: """ Unique ID of the alarm metric. """ return self["id"]`Unique ID of the alarm metric. 
- `prop metric_stat :`- [CloudWatchAlarmMetricStat](#aws_lambda_powertools.utilities.data_classes.CloudWatchAlarmMetricStat)
- 
## Expand source code`@property def metric_stat(self) -> CloudWatchAlarmMetricStat: return CloudWatchAlarmMetricStat(self["metricStat"])`
- `prop return_data : bool`
- 
## Expand source code`@property def return_data(self) -> bool: """ Whether this metric data is used to determine the state of the alarm or not. """ return self["returnData"]`Whether this metric data is used to determine the state of the alarm or not. 
 ### Inherited members
- `class CloudWatchAlarmMetricStat (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class CloudWatchAlarmMetricStat(DictWrapper): @property def period(self) -> int | None: """ Metric evaluation period, in seconds. """ return self.get("period", None) @property def stat(self) -> str | None: """ Statistical aggregation of metric points, e.g. Average, SampleCount, etc. """ return self.get("stat", None) @property def unit(self) -> str | None: """ Unit for metric. """ return self.get("unit", None) @property def metric(self) -> dict: """ Metric details """ return self.get("metric") or {}`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop metric : dict`
- 
## Expand source code`@property def metric(self) -> dict: """ Metric details """ return self.get("metric") or {}`Metric details 
- `prop period : int | None`
- 
## Expand source code`@property def period(self) -> int | None: """ Metric evaluation period, in seconds. """ return self.get("period", None)`Metric evaluation period, in seconds. 
- `prop stat : str | None`
- 
## Expand source code`@property def stat(self) -> str | None: """ Statistical aggregation of metric points, e.g. Average, SampleCount, etc. """ return self.get("stat", None)`Statistical aggregation of metric points, e.g. Average, SampleCount, etc. 
- `prop unit : str | None`
- 
## Expand source code`@property def unit(self) -> str | None: """ Unit for metric. """ return self.get("unit", None)`Unit for metric. 
 ### Inherited members
- `class CloudWatchAlarmState (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class CloudWatchAlarmState(DictWrapper): @property def value(self) -> Literal["OK", "ALARM", "INSUFFICIENT_DATA"]: """ Overall state of the alarm. """ return self["value"] @property def reason(self) -> str: """ Reason why alarm was changed to this state. """ return self["reason"] @property def reason_data(self) -> str: """ Additional data to back up the reason, usually contains the evaluated data points, the calculated threshold and timestamps. """ return self["reasonData"] @cached_property def reason_data_decoded(self) -> Any | None: """ Deserialized version of reason_data. """ return self._json_deserializer(self.reason_data) if self.reason_data else None @property def actions_suppressed_by(self) -> Literal["Alarm", "ExtensionPeriod", "WaitPeriod"] | None: """ Describes why the actions when the value is `ALARM` are suppressed in a composite alarm. """ return self.get("actionsSuppressedBy", None) @property def actions_suppressed_reason(self) -> str | None: """ Captures the reason for action suppression. """ return self.get("actionsSuppressedReason", None) @property def timestamp(self) -> str: """ Timestamp of this state change in ISO-8601 format. """ return self["timestamp"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop actions_suppressed_by : Literal['Alarm', 'ExtensionPeriod', 'WaitPeriod'] | None`
- 
## Expand source code`@property def actions_suppressed_by(self) -> Literal["Alarm", "ExtensionPeriod", "WaitPeriod"] | None: """ Describes why the actions when the value is `ALARM` are suppressed in a composite alarm. """ return self.get("actionsSuppressedBy", None)`Describes why the actions when the value is `ALARM`are suppressed in a composite alarm.
- `prop actions_suppressed_reason : str | None`
- 
## Expand source code`@property def actions_suppressed_reason(self) -> str | None: """ Captures the reason for action suppression. """ return self.get("actionsSuppressedReason", None)`Captures the reason for action suppression. 
- `prop reason : str`
- 
## Expand source code`@property def reason(self) -> str: """ Reason why alarm was changed to this state. """ return self["reason"]`Reason why alarm was changed to this state. 
- `prop reason_data : str`
- 
## Expand source code`@property def reason_data(self) -> str: """ Additional data to back up the reason, usually contains the evaluated data points, the calculated threshold and timestamps. """ return self["reasonData"]`Additional data to back up the reason, usually contains the evaluated data points, the calculated threshold and timestamps. 
- `var reason_data_decoded : Any | None`
- 
## Expand source code`@cached_property def reason_data_decoded(self) -> Any | None: """ Deserialized version of reason_data. """ return self._json_deserializer(self.reason_data) if self.reason_data else None`Deserialized version of reason_data. 
- `prop timestamp : str`
- 
## Expand source code`@property def timestamp(self) -> str: """ Timestamp of this state change in ISO-8601 format. """ return self["timestamp"]`Timestamp of this state change in ISO-8601 format. 
- `prop value : Literal['OK', 'ALARM', 'INSUFFICIENT_DATA']`
- 
## Expand source code`@property def value(self) -> Literal["OK", "ALARM", "INSUFFICIENT_DATA"]: """ Overall state of the alarm. """ return self["value"]`Overall state of the alarm. 
 ### Inherited members
- `class CloudWatchDashboardCustomWidgetEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class CloudWatchDashboardCustomWidgetEvent(DictWrapper): """CloudWatch dashboard custom widget event You can use a Lambda function to create a custom widget on a CloudWatch dashboard. Documentation: ------------- - https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add_custom_widget_dashboard_about.html """ @property def describe(self) -> bool: """Display widget documentation""" return bool(self.get("describe", False)) @property def widget_context(self) -> CloudWatchWidgetContext | None: """The widget context""" if self.get("widgetContext"): return CloudWatchWidgetContext(self["widgetContext"]) return None`CloudWatch dashboard custom widget event You can use a Lambda function to create a custom widget on a CloudWatch dashboard. ## Documentation:## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop describe : bool`
- 
## Expand source code`@property def describe(self) -> bool: """Display widget documentation""" return bool(self.get("describe", False))`Display widget documentation 
- `prop widget_context : CloudWatchWidgetContext | None`
- 
## Expand source code`@property def widget_context(self) -> CloudWatchWidgetContext | None: """The widget context""" if self.get("widgetContext"): return CloudWatchWidgetContext(self["widgetContext"]) return None`The widget context 
 ### Inherited members
- `class CloudWatchLogsEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class CloudWatchLogsEvent(DictWrapper): """CloudWatch Logs log stream event You can use a Lambda function to monitor and analyze logs from an Amazon CloudWatch Logs log stream. Documentation: -------------- - https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchlogs.html """ _decompressed_logs_data = None _json_logs_data = None @property def raw_logs_data(self) -> str: """The value of the `data` field is a Base64 encoded ZIP archive.""" return self["awslogs"]["data"] @property def decompress_logs_data(self) -> bytes: """Decode and decompress log data""" if self._decompressed_logs_data is None: payload = base64.b64decode(self.raw_logs_data) self._decompressed_logs_data = zlib.decompress(payload, zlib.MAX_WBITS | 32) return self._decompressed_logs_data def parse_logs_data(self) -> CloudWatchLogsDecodedData: """Decode, decompress and parse json data as CloudWatchLogsDecodedData""" if self._json_logs_data is None: self._json_logs_data = self._json_deserializer(self.decompress_logs_data.decode("UTF-8")) return CloudWatchLogsDecodedData(self._json_logs_data)`CloudWatch Logs log stream event You can use a Lambda function to monitor and analyze logs from an Amazon CloudWatch Logs log stream. ## Documentation:## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop decompress_logs_data : bytes`
- 
## Expand source code`@property def decompress_logs_data(self) -> bytes: """Decode and decompress log data""" if self._decompressed_logs_data is None: payload = base64.b64decode(self.raw_logs_data) self._decompressed_logs_data = zlib.decompress(payload, zlib.MAX_WBITS | 32) return self._decompressed_logs_data`Decode and decompress log data 
- `prop raw_logs_data : str`
- 
## Expand source code`@property def raw_logs_data(self) -> str: """The value of the `data` field is a Base64 encoded ZIP archive.""" return self["awslogs"]["data"]`The value of the `data`field is a Base64 encoded ZIP archive.
 ### Methods- `def parse_logs_data(self) ‑>`- [CloudWatchLogsDecodedData](cloud_watch_logs_event.html#aws_lambda_powertools.utilities.data_classes.cloud_watch_logs_event.CloudWatchLogsDecodedData)
- 
## Expand source code`def parse_logs_data(self) -> CloudWatchLogsDecodedData: """Decode, decompress and parse json data as CloudWatchLogsDecodedData""" if self._json_logs_data is None: self._json_logs_data = self._json_deserializer(self.decompress_logs_data.decode("UTF-8")) return CloudWatchLogsDecodedData(self._json_logs_data)`Decode, decompress and parse json data as CloudWatchLogsDecodedData 
 ### Inherited members
- `class CodeDeployLifecycleHookEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class CodeDeployLifecycleHookEvent(DictWrapper): @property def deployment_id(self) -> str: """The unique ID of the calling CodeDeploy Deployment.""" return self["DeploymentId"] @property def lifecycle_event_hook_execution_id(self) -> str: """The unique ID of a deployments lifecycle hook.""" return self["LifecycleEventHookExecutionId"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop deployment_id : str`
- 
## Expand source code`@property def deployment_id(self) -> str: """The unique ID of the calling CodeDeploy Deployment.""" return self["DeploymentId"]`The unique ID of the calling CodeDeploy Deployment. 
- `prop lifecycle_event_hook_execution_id : str`
- 
## Expand source code`@property def lifecycle_event_hook_execution_id(self) -> str: """The unique ID of a deployments lifecycle hook.""" return self["LifecycleEventHookExecutionId"]`The unique ID of a deployments lifecycle hook. 
 ### Inherited members
- `class CodePipelineJobEvent (data: dict[str, Any])`
- 
## Expand source code`class CodePipelineJobEvent(DictWrapper): """AWS CodePipeline Job Event Documentation: ------------- - https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-invoke-lambda-function.html - https://docs.aws.amazon.com/lambda/latest/dg/services-codepipeline.html """ def __init__(self, data: dict[str, Any]): super().__init__(data) self._job = self["CodePipeline.job"] @property def get_id(self) -> str: """Job id""" return self._job["id"] @property def account_id(self) -> str: """Account id""" return self._job["accountId"] @property def data(self) -> CodePipelineData: """Code pipeline jab data""" return CodePipelineData(self._job["data"]) @property def user_parameters(self) -> str | None: """Action configuration user parameters""" return self.data.action_configuration.configuration.user_parameters @property def decoded_user_parameters(self) -> dict[str, Any]: """Json Decoded action configuration user parameters""" return self.data.action_configuration.configuration.decoded_user_parameters @property def input_bucket_name(self) -> str: """Get the first input artifact bucket name""" return self.data.input_artifacts[0].location.s3_location.bucket_name @property def input_object_key(self) -> str: """Get the first input artifact order key unquote plus""" return self.data.input_artifacts[0].location.s3_location.object_key def setup_s3_client(self): """Creates an S3 client Uses the credentials passed in the event by CodePipeline. These credentials can be used to access the artifact bucket. Returns ------- BaseClient An S3 client with the appropriate credentials """ # IMPORTING boto3 within the FUNCTION and not at the top level to get # it only when we explicitly want it for better performance. import boto3 from aws_lambda_powertools.shared import user_agent s3 = boto3.client( "s3", aws_access_key_id=self.data.artifact_credentials.access_key_id, aws_secret_access_key=self.data.artifact_credentials.secret_access_key, aws_session_token=self.data.artifact_credentials.session_token, ) user_agent.register_feature_to_client(client=s3, feature="data_classes") return s3 def find_input_artifact(self, artifact_name: str) -> CodePipelineArtifact | None: """Find an input artifact by artifact name Parameters ---------- artifact_name : str The name of the input artifact to look for Returns ------- CodePipelineArtifact, None Matching CodePipelineArtifact if found """ for artifact in self.data.input_artifacts: if artifact.name == artifact_name: return artifact return None def find_output_artifact(self, artifact_name: str) -> CodePipelineArtifact | None: """Find an output artifact by artifact name Parameters ---------- artifact_name : str The name of the output artifact to look for Returns ------- CodePipelineArtifact, None Matching CodePipelineArtifact if found """ for artifact in self.data.output_artifacts: if artifact.name == artifact_name: return artifact return None def get_artifact(self, artifact_name: str, filename: str | None = None) -> str | None: """Get a file within an artifact zip on s3 Parameters ---------- artifact_name : str Name of the S3 artifact to download filename : str The file name within the artifact zip to extract as a string If None, this will return the raw object body. Returns ------- str, None Returns the contents file contents as a string """ artifact = self.find_input_artifact(artifact_name) if artifact is None: return None s3 = self.setup_s3_client() bucket = artifact.location.s3_location.bucket_name key = artifact.location.s3_location.key if filename: with tempfile.NamedTemporaryFile() as tmp_file: s3.download_file(bucket, key, tmp_file.name) with zipfile.ZipFile(tmp_file.name, "r") as zip_file: return zip_file.read(filename).decode("UTF-8") return s3.get_object(Bucket=bucket, Key=key)["Body"].read() def put_artifact(self, artifact_name: str, body: Any, content_type: str) -> None: """Writes an object to an s3 output artifact. Parameters ---------- artifact_name : str Name of the S3 artifact to upload body: Any The data to be written. Binary files should use io.BytesIO. content_type: str The content type of the data. Returns ------- None """ artifact = self.find_output_artifact(artifact_name) if artifact is None: raise ValueError(f"Artifact not found: {artifact_name}.") s3 = self.setup_s3_client() bucket = artifact.location.s3_location.bucket_name key = artifact.location.s3_location.key # boto3 doesn't support None to omit the parameter when using ServerSideEncryption and SSEKMSKeyId # So we are using if/else instead. if self.data.encryption_key: encryption_key_id = self.data.encryption_key.get_id encryption_key_type = self.data.encryption_key.get_type if encryption_key_type == "KMS": encryption_key_type = "aws:kms" s3.put_object( Bucket=bucket, Key=key, ContentType=content_type, Body=body, ServerSideEncryption=encryption_key_type, SSEKMSKeyId=encryption_key_id, BucketKeyEnabled=True, ) else: s3.put_object( Bucket=bucket, Key=key, ContentType=content_type, Body=body, BucketKeyEnabled=True, )`AWS CodePipeline Job Event ## Documentation:- [https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-invoke-lambda-function.html](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-invoke-lambda-function.html)
- [https://docs.aws.amazon.com/lambda/latest/dg/services-codepipeline.html](https://docs.aws.amazon.com/lambda/latest/dg/services-codepipeline.html)
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
 ### Instance variables- `prop account_id : str`
- 
## Expand source code`@property def account_id(self) -> str: """Account id""" return self._job["accountId"]`Account id 
- `prop data : CodePipelineData`
- 
## Expand source code`@property def data(self) -> CodePipelineData: """Code pipeline jab data""" return CodePipelineData(self._job["data"])`Code pipeline jab data 
- `prop decoded_user_parameters : dict[str, Any]`
- 
## Expand source code`@property def decoded_user_parameters(self) -> dict[str, Any]: """Json Decoded action configuration user parameters""" return self.data.action_configuration.configuration.decoded_user_parameters`Json Decoded action configuration user parameters 
- `prop get_id : str`
- 
## Expand source code`@property def get_id(self) -> str: """Job id""" return self._job["id"]`Job id 
- `prop input_bucket_name : str`
- 
## Expand source code`@property def input_bucket_name(self) -> str: """Get the first input artifact bucket name""" return self.data.input_artifacts[0].location.s3_location.bucket_name`Get the first input artifact bucket name 
- `prop input_object_key : str`
- 
## Expand source code`@property def input_object_key(self) -> str: """Get the first input artifact order key unquote plus""" return self.data.input_artifacts[0].location.s3_location.object_key`Get the first input artifact order key unquote plus 
- `prop user_parameters : str | None`
- 
## Expand source code`@property def user_parameters(self) -> str | None: """Action configuration user parameters""" return self.data.action_configuration.configuration.user_parameters`Action configuration user parameters 
 ### Methods- `def find_input_artifact(self, artifact_name: str) ‑>`- [CodePipelineArtifact](code_pipeline_job_event.html#aws_lambda_powertools.utilities.data_classes.code_pipeline_job_event.CodePipelineArtifact)| None
- 
## Expand source code`def find_input_artifact(self, artifact_name: str) -> CodePipelineArtifact | None: """Find an input artifact by artifact name Parameters ---------- artifact_name : str The name of the input artifact to look for Returns ------- CodePipelineArtifact, None Matching CodePipelineArtifact if found """ for artifact in self.data.input_artifacts: if artifact.name == artifact_name: return artifact return None`Find an input artifact by artifact name ## Parameters- `artifact_name`- `str`
- The name of the input artifact to look for
 ## Returns- `CodePipelineArtifact, None`
- Matching CodePipelineArtifact if found
 
- `def find_output_artifact(self, artifact_name: str) ‑>`- [CodePipelineArtifact](code_pipeline_job_event.html#aws_lambda_powertools.utilities.data_classes.code_pipeline_job_event.CodePipelineArtifact)| None
- 
## Expand source code`def find_output_artifact(self, artifact_name: str) -> CodePipelineArtifact | None: """Find an output artifact by artifact name Parameters ---------- artifact_name : str The name of the output artifact to look for Returns ------- CodePipelineArtifact, None Matching CodePipelineArtifact if found """ for artifact in self.data.output_artifacts: if artifact.name == artifact_name: return artifact return None`Find an output artifact by artifact name ## Parameters- `artifact_name`- `str`
- The name of the output artifact to look for
 ## Returns- `CodePipelineArtifact, None`
- Matching CodePipelineArtifact if found
 
- `def get_artifact(self, artifact_name: str, filename: str | None = None) ‑> str | None`
- 
## Expand source code`def get_artifact(self, artifact_name: str, filename: str | None = None) -> str | None: """Get a file within an artifact zip on s3 Parameters ---------- artifact_name : str Name of the S3 artifact to download filename : str The file name within the artifact zip to extract as a string If None, this will return the raw object body. Returns ------- str, None Returns the contents file contents as a string """ artifact = self.find_input_artifact(artifact_name) if artifact is None: return None s3 = self.setup_s3_client() bucket = artifact.location.s3_location.bucket_name key = artifact.location.s3_location.key if filename: with tempfile.NamedTemporaryFile() as tmp_file: s3.download_file(bucket, key, tmp_file.name) with zipfile.ZipFile(tmp_file.name, "r") as zip_file: return zip_file.read(filename).decode("UTF-8") return s3.get_object(Bucket=bucket, Key=key)["Body"].read()`Get a file within an artifact zip on s3 ## Parameters- `artifact_name`- `str`
- Name of the S3 artifact to download
- `filename`- `str`
- The file name within the artifact zip to extract as a string If None, this will return the raw object body.
 ## Returns- `str, None`
- Returns the contents file contents as a string
 
- `def put_artifact(self, artifact_name: str, body: Any, content_type: str) ‑> None`
- 
## Expand source code`def put_artifact(self, artifact_name: str, body: Any, content_type: str) -> None: """Writes an object to an s3 output artifact. Parameters ---------- artifact_name : str Name of the S3 artifact to upload body: Any The data to be written. Binary files should use io.BytesIO. content_type: str The content type of the data. Returns ------- None """ artifact = self.find_output_artifact(artifact_name) if artifact is None: raise ValueError(f"Artifact not found: {artifact_name}.") s3 = self.setup_s3_client() bucket = artifact.location.s3_location.bucket_name key = artifact.location.s3_location.key # boto3 doesn't support None to omit the parameter when using ServerSideEncryption and SSEKMSKeyId # So we are using if/else instead. if self.data.encryption_key: encryption_key_id = self.data.encryption_key.get_id encryption_key_type = self.data.encryption_key.get_type if encryption_key_type == "KMS": encryption_key_type = "aws:kms" s3.put_object( Bucket=bucket, Key=key, ContentType=content_type, Body=body, ServerSideEncryption=encryption_key_type, SSEKMSKeyId=encryption_key_id, BucketKeyEnabled=True, ) else: s3.put_object( Bucket=bucket, Key=key, ContentType=content_type, Body=body, BucketKeyEnabled=True, )`Writes an object to an s3 output artifact. ## Parameters- `artifact_name`- `str`
- Name of the S3 artifact to upload
- `body`- `Any`
- The data to be written. Binary files should use io.BytesIO.
- `content_type`- `str`
- The content type of the data.
 ## Returns- `None`
 
- `def setup_s3_client(self)`
- 
## Expand source code`def setup_s3_client(self): """Creates an S3 client Uses the credentials passed in the event by CodePipeline. These credentials can be used to access the artifact bucket. Returns ------- BaseClient An S3 client with the appropriate credentials """ # IMPORTING boto3 within the FUNCTION and not at the top level to get # it only when we explicitly want it for better performance. import boto3 from aws_lambda_powertools.shared import user_agent s3 = boto3.client( "s3", aws_access_key_id=self.data.artifact_credentials.access_key_id, aws_secret_access_key=self.data.artifact_credentials.secret_access_key, aws_session_token=self.data.artifact_credentials.session_token, ) user_agent.register_feature_to_client(client=s3, feature="data_classes") return s3`Creates an S3 client Uses the credentials passed in the event by CodePipeline. These credentials can be used to access the artifact bucket. ## Returns- `BaseClient`
- An S3 client with the appropriate credentials
 
 ### Inherited members
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
 ### Instance variables- `prop contact_data : ConnectContactFlowData`
- 
## Expand source code`@property def contact_data(self) -> ConnectContactFlowData: """This is always passed by Amazon Connect for every contact. Some parameters are optional.""" return ConnectContactFlowData(self["Details"]["ContactData"])`This is always passed by Amazon Connect for every contact. Some parameters are optional. 
- `prop parameters : dict[str, str]`
- 
## Expand source code`@property def parameters(self) -> dict[str, str]: """These are parameters specific to this call that were defined when you created the Lambda function.""" return self["Details"]["Parameters"]`These are parameters specific to this call that were defined when you created the Lambda function. 
 ### Inherited members
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
 ### Instance variables- `prop records : Iterator[DynamoDBRecord]`
- 
## Expand source code`@property def records(self) -> Iterator[DynamoDBRecord]: for record in self["Records"]: yield DynamoDBRecord(record)`
 ### Inherited members
- `class EventBridgeEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class EventBridgeEvent(DictWrapper): """Amazon EventBridge Event Documentation: -------------- - https://docs.aws.amazon.com/eventbridge/latest/userguide/aws-events.html """ @property def get_id(self) -> str: """A unique value is generated for every event. This can be helpful in tracing events as they move through rules to targets, and are processed.""" # Note: this name conflicts with existing python builtins return self["id"] @property def version(self) -> str: """By default, this is set to 0 (zero) in all events.""" return self["version"] @property def account(self) -> str: """The 12-digit number identifying an AWS account.""" return self["account"] @property def time(self) -> str: """The event timestamp, which can be specified by the service originating the event. If the event spans a time interval, the service might choose to report the start time, so this value can be noticeably before the time the event is actually received. """ return self["time"] @property def region(self) -> str: """Identifies the AWS region where the event originated.""" return self["region"] @property def resources(self) -> list[str]: """This JSON array contains ARNs that identify resources that are involved in the event. Inclusion of these ARNs is at the discretion of the service.""" return self["resources"] @property def source(self) -> str: """Identifies the service that sourced the event. All events sourced from within AWS begin with "aws." """ return self["source"] @property def detail_type(self) -> str: """Identifies, in combination with the source field, the fields and values that appear in the detail field.""" return self["detail-type"] @property def detail(self) -> dict[str, Any]: """A JSON object, whose content is at the discretion of the service originating the event.""" return self["detail"] @property def replay_name(self) -> str | None: """Identifies whether the event is being replayed and what is the name of the replay.""" return self["replay-name"]`Amazon EventBridge Event ## Documentation:## Parameters- `data`- `dict[str, Any]`
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
 ### Subclasses### Instance variables- `prop account : str`
- 
## Expand source code`@property def account(self) -> str: """The 12-digit number identifying an AWS account.""" return self["account"]`The 12-digit number identifying an AWS account. 
- `prop detail : dict[str, Any]`
- 
## Expand source code`@property def detail(self) -> dict[str, Any]: """A JSON object, whose content is at the discretion of the service originating the event.""" return self["detail"]`A JSON object, whose content is at the discretion of the service originating the event. 
- `prop detail_type : str`
- 
## Expand source code`@property def detail_type(self) -> str: """Identifies, in combination with the source field, the fields and values that appear in the detail field.""" return self["detail-type"]`Identifies, in combination with the source field, the fields and values that appear in the detail field. 
- `prop get_id : str`
- 
## Expand source code`@property def get_id(self) -> str: """A unique value is generated for every event. This can be helpful in tracing events as they move through rules to targets, and are processed.""" # Note: this name conflicts with existing python builtins return self["id"]`A unique value is generated for every event. This can be helpful in tracing events as they move through rules to targets, and are processed. 
- `prop region : str`
- 
## Expand source code`@property def region(self) -> str: """Identifies the AWS region where the event originated.""" return self["region"]`Identifies the AWS region where the event originated. 
- `prop replay_name : str | None`
- 
## Expand source code`@property def replay_name(self) -> str | None: """Identifies whether the event is being replayed and what is the name of the replay.""" return self["replay-name"]`Identifies whether the event is being replayed and what is the name of the replay. 
- `prop resources : list[str]`
- 
## Expand source code`@property def resources(self) -> list[str]: """This JSON array contains ARNs that identify resources that are involved in the event. Inclusion of these ARNs is at the discretion of the service.""" return self["resources"]`This JSON array contains ARNs that identify resources that are involved in the event. Inclusion of these ARNs is at the discretion of the service. 
- `prop source : str`
- 
## Expand source code`@property def source(self) -> str: """Identifies the service that sourced the event. All events sourced from within AWS begin with "aws." """ return self["source"]`Identifies the service that sourced the event. All events sourced from within AWS begin with "aws." 
- `prop time : str`
- 
## Expand source code`@property def time(self) -> str: """The event timestamp, which can be specified by the service originating the event. If the event spans a time interval, the service might choose to report the start time, so this value can be noticeably before the time the event is actually received. """ return self["time"]`The event timestamp, which can be specified by the service originating the event. If the event spans a time interval, the service might choose to report the start time, so this value can be noticeably before the time the event is actually received. 
- `prop version : str`
- 
## Expand source code`@property def version(self) -> str: """By default, this is set to 0 (zero) in all events.""" return self["version"]`By default, this is set to 0 (zero) in all events. 
 ### Inherited members
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
- `prop record : KafkaEventRecord`
- 
## Expand source code`@property def record(self) -> KafkaEventRecord: """ Returns the next Kafka record using an iterator. Returns ------- KafkaEventRecord The next Kafka record. Raises ------ StopIteration If there are no more records available. """ if self._records is None: self._records = self.records return next(self._records)`Returns the next Kafka record using an iterator. ## Returns- `KafkaEventRecord`
- The next Kafka record.
 ## Raises- `StopIteration`
- If there are no more records available.
 
- `prop records : Iterator[KafkaEventRecord]`
- 
## Expand source code`@property def records(self) -> Iterator[KafkaEventRecord]: """The Kafka records.""" for chunk in self["records"].values(): for record in chunk: yield KafkaEventRecord(data=record, json_deserializer=self._json_deserializer)`The Kafka records. 
 ### Inherited members
- `class KinesisFirehoseDataTransformationRecord (record_id: str,`
 result: "Literal['Ok', 'Dropped', 'ProcessingFailed']" = 'Ok',
 data: str = '',
 metadata:- [KinesisFirehoseDataTransformationRecordMetadata](#aws_lambda_powertools.utilities.data_classes.KinesisFirehoseDataTransformationRecordMetadata)| None = None,
 json_serializer: Callable = <function dumps>,
 json_deserializer: Callable = <function loads>)
- 
## Expand source code`@dataclass(repr=False, order=False) class KinesisFirehoseDataTransformationRecord: """Record in Kinesis Data Firehose response object. Parameters ---------- record_id: str uniquely identifies this record within the current batch result: Literal["Ok", "Dropped", "ProcessingFailed"] record data transformation status, whether it succeeded, should be dropped, or failed. data: str base64-encoded payload, by default empty string. Use `data_from_text` or `data_from_json` methods to convert data if needed. metadata: KinesisFirehoseDataTransformationRecordMetadata | None Metadata associated with this record; can contain partition keys. See: https://docs.aws.amazon.com/firehose/latest/dev/dynamic-partitioning.html json_serializer: Callable function to serialize `obj` to a JSON formatted `str`, by default json.dumps json_deserializer: Callable function to deserialize `str`, `bytes`, bytearray` containing a JSON document to a Python `obj`, by default json.loads Documentation: -------------- - https://docs.aws.amazon.com/firehose/latest/dev/data-transformation.html """ _valid_result_types: ClassVar[tuple[str, str, str]] = ("Ok", "Dropped", "ProcessingFailed") record_id: str result: Literal["Ok", "Dropped", "ProcessingFailed"] = "Ok" data: str = "" metadata: KinesisFirehoseDataTransformationRecordMetadata | None = None json_serializer: Callable = json.dumps json_deserializer: Callable = json.loads def asdict(self) -> dict: if self.result not in self._valid_result_types: warnings.warn( stacklevel=1, message=f'The result "{self.result}" is not valid, Choose from "Ok", "Dropped", "ProcessingFailed"', ) record: dict[str, Any] = { "recordId": self.record_id, "result": self.result, "data": self.data, } if self.metadata: record["metadata"] = self.metadata.asdict() return record @property def data_as_bytes(self) -> bytes: """Decoded base64-encoded data as bytes""" if not self.data: return b"" return base64.b64decode(self.data) @property def data_as_text(self) -> str: """Decoded base64-encoded data as text""" if not self.data: return "" return self.data_as_bytes.decode("utf-8") @cached_property def data_as_json(self) -> dict: """Decoded base64-encoded data loaded to json""" if not self.data: return {} return self.json_deserializer(self.data_as_text)`Record in Kinesis Data Firehose response object. ## Parameters- `record_id`- `str`
- uniquely identifies this record within the current batch
- `result`- `Literal["Ok", "Dropped", "ProcessingFailed"]`
- record data transformation status, whether it succeeded, should be dropped, or failed.
- `data`- `str`
- 
base64-encoded payload, by default empty string. Use `data_from_text`or`data_from_json`methods to convert data if needed.
- `metadata`- `KinesisFirehoseDataTransformationRecordMetadata | None`
- 
Metadata associated with this record; can contain partition keys. See: [https://docs.aws.amazon.com/firehose/latest/dev/dynamic-partitioning.html](https://docs.aws.amazon.com/firehose/latest/dev/dynamic-partitioning.html)
- `json_serializer`- `Callable`
- function to serialize `obj`to a JSON formatted`str`, by default json.dumps
- `json_deserializer`- `Callable`
- function to deserialize `str`,`bytes`, bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ## Documentation:### Class variables- `var data : str`
- `var metadata :`- [KinesisFirehoseDataTransformationRecordMetadata](#aws_lambda_powertools.utilities.data_classes.KinesisFirehoseDataTransformationRecordMetadata)| None
- `var record_id : str`
- `var result : Literal['Ok', 'Dropped', 'ProcessingFailed']`
 ### Instance variables- `prop data_as_bytes : bytes`
- 
## Expand source code`@property def data_as_bytes(self) -> bytes: """Decoded base64-encoded data as bytes""" if not self.data: return b"" return base64.b64decode(self.data)`Decoded base64-encoded data as bytes 
- `var data_as_json : dict`
- 
## Expand source code`@cached_property def data_as_json(self) -> dict: """Decoded base64-encoded data loaded to json""" if not self.data: return {} return self.json_deserializer(self.data_as_text)`Decoded base64-encoded data loaded to json 
- `prop data_as_text : str`
- 
## Expand source code`@property def data_as_text(self) -> str: """Decoded base64-encoded data as text""" if not self.data: return "" return self.data_as_bytes.decode("utf-8")`Decoded base64-encoded data as text 
 ### Methods- `def asdict(self) ‑> dict`
- 
## Expand source code`def asdict(self) -> dict: if self.result not in self._valid_result_types: warnings.warn( stacklevel=1, message=f'The result "{self.result}" is not valid, Choose from "Ok", "Dropped", "ProcessingFailed"', ) record: dict[str, Any] = { "recordId": self.record_id, "result": self.result, "data": self.data, } if self.metadata: record["metadata"] = self.metadata.asdict() return record`
- `def json_deserializer(s,`
 *,
 cls=None,
 object_hook=None,
 parse_float=None,
 parse_int=None,
 parse_constant=None,
 object_pairs_hook=None,
 **kw)
- 
## Expand source code`def loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw): """Deserialize ``s`` (a ``str``, ``bytes`` or ``bytearray`` instance containing a JSON document) to a Python object. ``object_hook`` is an optional function that will be called with the result of any object literal decode (a ``dict``). The return value of ``object_hook`` will be used instead of the ``dict``. This feature can be used to implement custom decoders (e.g. JSON-RPC class hinting). ``object_pairs_hook`` is an optional function that will be called with the result of any object literal decoded with an ordered list of pairs. The return value of ``object_pairs_hook`` will be used instead of the ``dict``. This feature can be used to implement custom decoders. If ``object_hook`` is also defined, the ``object_pairs_hook`` takes priority. ``parse_float``, if specified, will be called with the string of every JSON float to be decoded. By default this is equivalent to float(num_str). This can be used to use another datatype or parser for JSON floats (e.g. decimal.Decimal). ``parse_int``, if specified, will be called with the string of every JSON int to be decoded. By default this is equivalent to int(num_str). This can be used to use another datatype or parser for JSON integers (e.g. float). ``parse_constant``, if specified, will be called with one of the following strings: -Infinity, Infinity, NaN. This can be used to raise an exception if invalid JSON numbers are encountered. To use a custom ``JSONDecoder`` subclass, specify it with the ``cls`` kwarg; otherwise ``JSONDecoder`` is used. """ if isinstance(s, str): if s.startswith('\ufeff'): raise JSONDecodeError("Unexpected UTF-8 BOM (decode using utf-8-sig)", s, 0) else: if not isinstance(s, (bytes, bytearray)): raise TypeError(f'the JSON object must be str, bytes or bytearray, ' f'not {s.__class__.__name__}') s = s.decode(detect_encoding(s), 'surrogatepass') if (cls is None and object_hook is None and parse_int is None and parse_float is None and parse_constant is None and object_pairs_hook is None and not kw): return _default_decoder.decode(s) if cls is None: cls = JSONDecoder if object_hook is not None: kw['object_hook'] = object_hook if object_pairs_hook is not None: kw['object_pairs_hook'] = object_pairs_hook if parse_float is not None: kw['parse_float'] = parse_float if parse_int is not None: kw['parse_int'] = parse_int if parse_constant is not None: kw['parse_constant'] = parse_constant return cls(**kw).decode(s)`Deserialize `s`(a`str`,`bytes`or`bytearray`instance containing a JSON document) to a Python object.`object_hook`is an optional function that will be called with the result of any object literal decode (a`dict`). The return value of`object_hook`will be used instead of the`dict`. This feature can be used to implement custom decoders (e.g. JSON-RPC class hinting).`object_pairs_hook`is an optional function that will be called with the result of any object literal decoded with an ordered list of pairs. The return value of`object_pairs_hook`will be used instead of the`dict`. This feature can be used to implement custom decoders. If`object_hook`is also defined, the`object_pairs_hook`takes priority.`parse_float`, if specified, will be called with the string of every JSON float to be decoded. By default this is equivalent to float(num_str). This can be used to use another datatype or parser for JSON floats (e.g. decimal.Decimal).`parse_int`, if specified, will be called with the string of every JSON int to be decoded. By default this is equivalent to int(num_str). This can be used to use another datatype or parser for JSON integers (e.g. float).`parse_constant`, if specified, will be called with one of the following strings: -Infinity, Infinity, NaN. This can be used to raise an exception if invalid JSON numbers are encountered.To use a custom `JSONDecoder`subclass, specify it with the`cls`kwarg; otherwise`JSONDecoder`is used.
- `def json_serializer(obj,`
 *,
 skipkeys=False,
 ensure_ascii=True,
 check_circular=True,
 allow_nan=True,
 cls=None,
 indent=None,
 separators=None,
 default=None,
 sort_keys=False,
 **kw)
- 
## Expand source code`def dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw): """Serialize ``obj`` to a JSON formatted ``str``. If ``skipkeys`` is true then ``dict`` keys that are not basic types (``str``, ``int``, ``float``, ``bool``, ``None``) will be skipped instead of raising a ``TypeError``. If ``ensure_ascii`` is false, then the return value can contain non-ASCII characters if they appear in strings contained in ``obj``. Otherwise, all such characters are escaped in JSON strings. If ``check_circular`` is false, then the circular reference check for container types will be skipped and a circular reference will result in an ``RecursionError`` (or worse). If ``allow_nan`` is false, then it will be a ``ValueError`` to serialize out of range ``float`` values (``nan``, ``inf``, ``-inf``) in strict compliance of the JSON specification, instead of using the JavaScript equivalents (``NaN``, ``Infinity``, ``-Infinity``). If ``indent`` is a non-negative integer, then JSON array elements and object members will be pretty-printed with that indent level. An indent level of 0 will only insert newlines. ``None`` is the most compact representation. If specified, ``separators`` should be an ``(item_separator, key_separator)`` tuple. The default is ``(', ', ': ')`` if *indent* is ``None`` and ``(',', ': ')`` otherwise. To get the most compact JSON representation, you should specify ``(',', ':')`` to eliminate whitespace. ``default(obj)`` is a function that should return a serializable version of obj or raise TypeError. The default simply raises TypeError. If *sort_keys* is true (default: ``False``), then the output of dictionaries will be sorted by key. To use a custom ``JSONEncoder`` subclass (e.g. one that overrides the ``.default()`` method to serialize additional types), specify it with the ``cls`` kwarg; otherwise ``JSONEncoder`` is used. """ # cached encoder if (not skipkeys and ensure_ascii and check_circular and allow_nan and cls is None and indent is None and separators is None and default is None and not sort_keys and not kw): return _default_encoder.encode(obj) if cls is None: cls = JSONEncoder return cls( skipkeys=skipkeys, ensure_ascii=ensure_ascii, check_circular=check_circular, allow_nan=allow_nan, indent=indent, separators=separators, default=default, sort_keys=sort_keys, **kw).encode(obj)`Serialize `obj`to a JSON formatted`str`.If `skipkeys`is true then`dict`keys that are not basic types (`str`,`int`,`float`,`bool`,`None`) will be skipped instead of raising a`TypeError`.If `ensure_ascii`is false, then the return value can contain non-ASCII characters if they appear in strings contained in`obj`. Otherwise, all such characters are escaped in JSON strings.If `check_circular`is false, then the circular reference check for container types will be skipped and a circular reference will result in an`RecursionError`(or worse).If `allow_nan`is false, then it will be a`ValueError`to serialize out of range`float`values (`nan`,`inf`,`-inf`) in strict compliance of the JSON specification, instead of using the JavaScript equivalents (`NaN`,`Infinity`,`-Infinity`).If `indent`is a non-negative integer, then JSON array elements and object members will be pretty-printed with that indent level. An indent level of 0 will only insert newlines.`None`is the most compact representation.If specified, `separators`should be an`(item_separator, key_separator)`tuple. The default is`(', ', ': ')`if*indent*is`None`and`(',', ': ')`otherwise. To get the most compact JSON representation, you should specify`(',', ':')`to eliminate whitespace.`default(obj)`is a function that should return a serializable version of obj or raise TypeError. The default simply raises TypeError.If *sort_keys*is true (default:`False`), then the output of dictionaries will be sorted by key.To use a custom `JSONEncoder`subclass (e.g. one that overrides the`.default()`method to serialize additional types), specify it with the`cls`kwarg; otherwise`JSONEncoder`is used.
 
- `class KinesisFirehoseDataTransformationRecordMetadata (partition_keys: dict[str, str] = <factory>)`
- 
## Expand source code`@dataclass(repr=False, order=False, frozen=True) class KinesisFirehoseDataTransformationRecordMetadata: """ Metadata in Firehose Data Transform Record. Parameters ---------- partition_keys: dict[str, str] A dict of partition keys/value in string format, e.g. `{"year":"2023","month":"09"}` Documentation: -------------- - https://docs.aws.amazon.com/firehose/latest/dev/dynamic-partitioning.html """ partition_keys: dict[str, str] = field(default_factory=lambda: {}) def asdict(self) -> dict: if self.partition_keys is not None: return {"partitionKeys": self.partition_keys} return {}`Metadata in Firehose Data Transform Record. ## Parameters- `partition_keys`- `dict[str, str]`
- A dict of partition keys/value in string format, e.g. `{"year":"2023","month":"09"}`
 ## Documentation:### Class variables- `var partition_keys : dict[str, str]`
 ### Methods- `def asdict(self) ‑> dict`
- 
## Expand source code`def asdict(self) -> dict: if self.partition_keys is not None: return {"partitionKeys": self.partition_keys} return {}`
 
- `class KinesisFirehoseDataTransformationResponse (records: list[`- [KinesisFirehoseDataTransformationRecord](#aws_lambda_powertools.utilities.data_classes.KinesisFirehoseDataTransformationRecord)] = <factory>)
- 
## Expand source code`@dataclass(repr=False, order=False) class KinesisFirehoseDataTransformationResponse: """Kinesis Data Firehose response object Documentation: -------------- - https://docs.aws.amazon.com/firehose/latest/dev/data-transformation.html Parameters ---------- records : list[KinesisFirehoseResponseRecord] records of Kinesis Data Firehose response object, optional parameter at start. can be added later using `add_record` function. Examples -------- **Transforming data records** ```python from aws_lambda_powertools.utilities.data_classes import ( KinesisFirehoseDataTransformationRecord, KinesisFirehoseDataTransformationResponse, KinesisFirehoseEvent, ) from aws_lambda_powertools.utilities.serialization import base64_from_json from aws_lambda_powertools.utilities.typing import LambdaContext def lambda_handler(event: dict, context: LambdaContext): firehose_event = KinesisFirehoseEvent(event) result = KinesisFirehoseDataTransformationResponse() for record in firehose_event.records: payload = record.data_as_text # base64 decoded data as str ## generate data to return transformed_data = {"tool_used": "powertools_dataclass", "original_payload": payload} processed_record = KinesisFirehoseDataTransformationRecord( record_id=record.record_id, data=base64_from_json(transformed_data), ) result.add_record(processed_record) # return transformed records return result.asdict() ``` """ records: list[KinesisFirehoseDataTransformationRecord] = field(default_factory=list) def add_record(self, record: KinesisFirehoseDataTransformationRecord): self.records.append(record) def asdict(self) -> dict: if not self.records: raise ValueError("Amazon Kinesis Data Firehose doesn't accept empty response") return {"records": [record.asdict() for record in self.records]}`Kinesis Data Firehose response object ## Documentation:## Parameters- `records`- `list[KinesisFirehoseResponseRecord]`
- records of Kinesis Data Firehose response object,
optional parameter at start. can be added later using `add_record`function.
 ## Examples**Transforming data records**`from aws_lambda_powertools.utilities.data_classes import ( KinesisFirehoseDataTransformationRecord, KinesisFirehoseDataTransformationResponse, KinesisFirehoseEvent, ) from aws_lambda_powertools.utilities.serialization import base64_from_json from aws_lambda_powertools.utilities.typing import LambdaContext def lambda_handler(event: dict, context: LambdaContext): firehose_event = KinesisFirehoseEvent(event) result = KinesisFirehoseDataTransformationResponse() for record in firehose_event.records: payload = record.data_as_text # base64 decoded data as str ## generate data to return transformed_data = {"tool_used": "powertools_dataclass", "original_payload": payload} processed_record = KinesisFirehoseDataTransformationRecord( record_id=record.record_id, data=base64_from_json(transformed_data), ) result.add_record(processed_record) # return transformed records return result.asdict()`### Class variables- `var records : list[`- [KinesisFirehoseDataTransformationRecord](kinesis_firehose_event.html#aws_lambda_powertools.utilities.data_classes.kinesis_firehose_event.KinesisFirehoseDataTransformationRecord)]
 ### Methods- `def add_record(self,`
 record:- [KinesisFirehoseDataTransformationRecord](#aws_lambda_powertools.utilities.data_classes.KinesisFirehoseDataTransformationRecord))
- 
## Expand source code`def add_record(self, record: KinesisFirehoseDataTransformationRecord): self.records.append(record)`
- `def asdict(self) ‑> dict`
- 
## Expand source code`def asdict(self) -> dict: if not self.records: raise ValueError("Amazon Kinesis Data Firehose doesn't accept empty response") return {"records": [record.asdict() for record in self.records]}`
 
- `class KinesisFirehoseEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class KinesisFirehoseEvent(DictWrapper): """Kinesis Data Firehose event Documentation: -------------- - https://docs.aws.amazon.com/lambda/latest/dg/services-kinesisfirehose.html """ @property def invocation_id(self) -> str: """Unique ID for for Lambda invocation""" return self["invocationId"] @property def delivery_stream_arn(self) -> str: """ARN of the Firehose Data Firehose Delivery Stream""" return self["deliveryStreamArn"] @property def source_kinesis_stream_arn(self) -> str | None: """ARN of the Kinesis Stream; present only when Kinesis Stream is source""" return self.get("sourceKinesisStreamArn") @property def region(self) -> str: """AWS region where the event originated eg: us-east-1""" return self["region"] @property def records(self) -> Iterator[KinesisFirehoseRecord]: for record in self["records"]: yield KinesisFirehoseRecord(data=record, json_deserializer=self._json_deserializer)`Kinesis Data Firehose event ## Documentation:## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop delivery_stream_arn : str`
- 
## Expand source code`@property def delivery_stream_arn(self) -> str: """ARN of the Firehose Data Firehose Delivery Stream""" return self["deliveryStreamArn"]`ARN of the Firehose Data Firehose Delivery Stream 
- `prop invocation_id : str`
- 
## Expand source code`@property def invocation_id(self) -> str: """Unique ID for for Lambda invocation""" return self["invocationId"]`Unique ID for for Lambda invocation 
- `prop records : Iterator[KinesisFirehoseRecord]`
- 
## Expand source code`@property def records(self) -> Iterator[KinesisFirehoseRecord]: for record in self["records"]: yield KinesisFirehoseRecord(data=record, json_deserializer=self._json_deserializer)`
- `prop region : str`
- 
## Expand source code`@property def region(self) -> str: """AWS region where the event originated eg: us-east-1""" return self["region"]`AWS region where the event originated eg: us-east-1 
- `prop source_kinesis_stream_arn : str | None`
- 
## Expand source code`@property def source_kinesis_stream_arn(self) -> str | None: """ARN of the Kinesis Stream; present only when Kinesis Stream is source""" return self.get("sourceKinesisStreamArn")`ARN of the Kinesis Stream; present only when Kinesis Stream is source 
 ### Inherited members
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
 ### Instance variables- `prop records : Iterator[KinesisStreamRecord]`
- 
## Expand source code`@property def records(self) -> Iterator[KinesisStreamRecord]: for record in self["Records"]: yield KinesisStreamRecord(record)`
 ### Inherited members
- `class LambdaFunctionUrlEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class LambdaFunctionUrlEvent(APIGatewayProxyEventV2): """AWS Lambda Function URL event Notes: ----- Lambda Function URL follows the API Gateway HTTP APIs Payload Format Version 2.0. Keys related to API Gateway features not available in Function URL use a sentinel value (e.g.`routeKey`, `stage`). Documentation: - https://docs.aws.amazon.com/lambda/latest/dg/urls-configuration.html - https://docs.aws.amazon.com/lambda/latest/dg/urls-invocation.html#urls-payloads """ pass`AWS Lambda Function URL event ## Notes:Lambda Function URL follows the API Gateway HTTP APIs Payload Format Version 2.0. Keys related to API Gateway features not available in Function URL use a sentinel value (e.g. `routeKey`,`stage`).Documentation: - [https://docs.aws.amazon.com/lambda/latest/dg/urls-configuration.html](https://docs.aws.amazon.com/lambda/latest/dg/urls-configuration.html)-[https://docs.aws.amazon.com/lambda/latest/dg/urls-invocation.html#urls-payloads](https://docs.aws.amazon.com/lambda/latest/dg/urls-invocation.html#urls-payloads)## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [APIGatewayProxyEventV2](api_gateway_proxy_event.html#aws_lambda_powertools.utilities.data_classes.api_gateway_proxy_event.APIGatewayProxyEventV2)
- [BaseProxyEvent](common.html#aws_lambda_powertools.utilities.data_classes.common.BaseProxyEvent)
- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Inherited members
- `class S3BatchOperationEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class S3BatchOperationEvent(DictWrapper): """Amazon S3BatchOperation Event Documentation: -------------- - https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-invoke-lambda.html """ @property def invocation_id(self) -> str: """Get the identifier of the invocation request""" return self["invocationId"] @property def invocation_schema_version(self) -> Literal["1.0", "2.0"]: """ Get the schema version for the payload that Batch Operations sends when invoking an AWS Lambda function. Either '1.0' or '2.0'. """ return self["invocationSchemaVersion"] @property def tasks(self) -> Iterator[S3BatchOperationTask]: """Get s3 batch operation tasks""" for task in self["tasks"]: yield S3BatchOperationTask(task) @property def task(self) -> S3BatchOperationTask: """Get the first s3 batch operation task""" return next(self.tasks) @property def job(self) -> S3BatchOperationJob: """Get the s3 batch operation job""" return S3BatchOperationJob(self["job"])`Amazon S3BatchOperation Event ## Documentation:## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop invocation_id : str`
- 
## Expand source code`@property def invocation_id(self) -> str: """Get the identifier of the invocation request""" return self["invocationId"]`Get the identifier of the invocation request 
- `prop invocation_schema_version : Literal['1.0', '2.0']`
- 
## Expand source code`@property def invocation_schema_version(self) -> Literal["1.0", "2.0"]: """ Get the schema version for the payload that Batch Operations sends when invoking an AWS Lambda function. Either '1.0' or '2.0'. """ return self["invocationSchemaVersion"]`Get the schema version for the payload that Batch Operations sends when invoking an AWS Lambda function. Either '1.0' or '2.0'. 
- `prop job : S3BatchOperationJob`
- 
## Expand source code`@property def job(self) -> S3BatchOperationJob: """Get the s3 batch operation job""" return S3BatchOperationJob(self["job"])`Get the s3 batch operation job 
- `prop task : S3BatchOperationTask`
- 
## Expand source code`@property def task(self) -> S3BatchOperationTask: """Get the first s3 batch operation task""" return next(self.tasks)`Get the first s3 batch operation task 
- `prop tasks : Iterator[S3BatchOperationTask]`
- 
## Expand source code`@property def tasks(self) -> Iterator[S3BatchOperationTask]: """Get s3 batch operation tasks""" for task in self["tasks"]: yield S3BatchOperationTask(task)`Get s3 batch operation tasks 
 ### Inherited members
- `class S3BatchOperationResponse (invocation_schema_version: str,`
 invocation_id: str,
 treat_missing_keys_as: RESULT_CODE_TYPE = 'Succeeded',
 results: list[- [S3BatchOperationResponseRecord](#aws_lambda_powertools.utilities.data_classes.S3BatchOperationResponseRecord)] = <factory>)
- 
## Expand source code`@dataclass(repr=False, order=False) class S3BatchOperationResponse: """S3 Batch Operations response object Documentation: -------------- - https://docs.aws.amazon.com/lambda/latest/dg/services-s3-batch.html - https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-invoke-lambda.html#batch-ops-invoke-lambda-custom-functions - https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_LambdaInvokeOperation.html#AmazonS3-Type-control_LambdaInvokeOperation-InvocationSchemaVersion Parameters ---------- invocation_schema_version : str Specifies the schema version for the payload that Batch Operations sends when invoking an AWS Lambda function., either '1.0' or '2.0'. This must be copied from the event. invocation_id : str The identifier of the invocation request. This must be copied from the event. treat_missing_keys_as : Literal["Succeeded", "TemporaryFailure", "PermanentFailure"] Undocumented parameter, defaults to "Succeeded" results : list[S3BatchOperationResult] Results of each S3 Batch Operations task, optional parameter at start. Can be added later using `add_result` function. Examples -------- **S3 Batch Operations** ```python import boto3 from botocore.exceptions import ClientError from aws_lambda_powertools.utilities.data_classes import ( S3BatchOperationEvent, S3BatchOperationResponse, event_source ) from aws_lambda_powertools.utilities.typing import LambdaContext @event_source(data_class=S3BatchOperationEvent) def lambda_handler(event: S3BatchOperationEvent, context: LambdaContext): response = S3BatchOperationResponse( event.invocation_schema_version, event.invocation_id, "PermanentFailure" ) result = None task = event.task src_key: str = task.s3_key src_bucket: str = task.s3_bucket s3 = boto3.client("s3", region_name='us-east-1') try: dest_bucket, dest_key = do_some_work(s3, src_bucket, src_key) result = task.build_task_batch_response("Succeeded", f"s3://{dest_bucket}/{dest_key}") except ClientError as e: error_code = e.response['Error']['Code'] error_message = e.response['Error']['Message'] if error_code == 'RequestTimeout': result = task.build_task_batch_response("TemporaryFailure", "Timeout - trying again") else: result = task.build_task_batch_response("PermanentFailure", f"{error_code}: {error_message}") except Exception as e: result = task.build_task_batch_response("PermanentFailure", str(e)) finally: response.add_result(result) return response.asdict() ``` """ invocation_schema_version: str invocation_id: str treat_missing_keys_as: RESULT_CODE_TYPE = "Succeeded" results: list[S3BatchOperationResponseRecord] = field(default_factory=list) def __post_init__(self): if self.treat_missing_keys_as not in VALID_RESULT_CODES: warnings.warn( stacklevel=2, message=f"The value {self.treat_missing_keys_as} is not valid for treat_missing_keys_as, " f"Choose from {', '.join(map(repr, VALID_RESULT_CODES))}.", ) def add_result(self, result: S3BatchOperationResponseRecord): self.results.append(result) def asdict(self) -> dict: result_count = len(self.results) if result_count != 1: raise ValueError(f"Response must have exactly one result, but got {result_count}") return { "invocationSchemaVersion": self.invocation_schema_version, "treatMissingKeysAs": self.treat_missing_keys_as, "invocationId": self.invocation_id, "results": [result.asdict() for result in self.results], }`S3 Batch Operations response object ## Documentation:- [https://docs.aws.amazon.com/lambda/latest/dg/services-s3-batch.html](https://docs.aws.amazon.com/lambda/latest/dg/services-s3-batch.html)
- [https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-invoke-lambda.html#batch-ops-invoke-lambda-custom-functions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops-invoke-lambda.html#batch-ops-invoke-lambda-custom-functions)
- [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_LambdaInvokeOperation.html#AmazonS3-Type-control_LambdaInvokeOperation-InvocationSchemaVersion](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_LambdaInvokeOperation.html#AmazonS3-Type-control_LambdaInvokeOperation-InvocationSchemaVersion)
 ## Parameters- `invocation_schema_version`- `str`
- Specifies the schema version for the payload that Batch Operations sends when invoking an AWS Lambda function., either '1.0' or '2.0'. This must be copied from the event.
- `invocation_id`- `str`
- The identifier of the invocation request. This must be copied from the event.
- `treat_missing_keys_as`- `Literal["Succeeded", "TemporaryFailure", "PermanentFailure"]`
- Undocumented parameter, defaults to "Succeeded"
- `results`- `list[S3BatchOperationResult]`
- Results of each S3 Batch Operations task,
optional parameter at start. Can be added later using `add_result`function.
 ## Examples**S3 Batch Operations**`import boto3 from botocore.exceptions import ClientError from aws_lambda_powertools.utilities.data_classes import ( S3BatchOperationEvent, S3BatchOperationResponse, event_source ) from aws_lambda_powertools.utilities.typing import LambdaContext @event_source(data_class=S3BatchOperationEvent) def lambda_handler(event: S3BatchOperationEvent, context: LambdaContext): response = S3BatchOperationResponse( event.invocation_schema_version, event.invocation_id, "PermanentFailure" ) result = None task = event.task src_key: str = task.s3_key src_bucket: str = task.s3_bucket s3 = boto3.client("s3", region_name='us-east-1') try: dest_bucket, dest_key = do_some_work(s3, src_bucket, src_key) result = task.build_task_batch_response("Succeeded", f"s3://{dest_bucket}/{dest_key}") except ClientError as e: error_code = e.response['Error']['Code'] error_message = e.response['Error']['Message'] if error_code == 'RequestTimeout': result = task.build_task_batch_response("TemporaryFailure", "Timeout - trying again") else: result = task.build_task_batch_response("PermanentFailure", f"{error_code}: {error_message}") except Exception as e: result = task.build_task_batch_response("PermanentFailure", str(e)) finally: response.add_result(result) return response.asdict()`### Class variables- `var invocation_id : str`
- `var invocation_schema_version : str`
- `var results : list[`- [S3BatchOperationResponseRecord](s3_batch_operation_event.html#aws_lambda_powertools.utilities.data_classes.s3_batch_operation_event.S3BatchOperationResponseRecord)]
- `var treat_missing_keys_as : Literal['Succeeded', 'TemporaryFailure', 'PermanentFailure']`
 ### Methods- `def add_result(self,`
 result:- [S3BatchOperationResponseRecord](#aws_lambda_powertools.utilities.data_classes.S3BatchOperationResponseRecord))
- 
## Expand source code`def add_result(self, result: S3BatchOperationResponseRecord): self.results.append(result)`
- `def asdict(self) ‑> dict`
- 
## Expand source code`def asdict(self) -> dict: result_count = len(self.results) if result_count != 1: raise ValueError(f"Response must have exactly one result, but got {result_count}") return { "invocationSchemaVersion": self.invocation_schema_version, "treatMissingKeysAs": self.treat_missing_keys_as, "invocationId": self.invocation_id, "results": [result.asdict() for result in self.results], }`
 
- `class S3BatchOperationResponseRecord (task_id: str, result_code: RESULT_CODE_TYPE, result_string: str | None = None)`
- 
## Expand source code`@dataclass(repr=False, order=False) class S3BatchOperationResponseRecord: task_id: str result_code: RESULT_CODE_TYPE result_string: str | None = None def asdict(self) -> dict[str, Any]: if self.result_code not in VALID_RESULT_CODES: warnings.warn( stacklevel=2, message=f"The resultCode {self.result_code} is not valid. " f"Choose from {', '.join(map(repr, VALID_RESULT_CODES))}.", ) return { "taskId": self.task_id, "resultCode": self.result_code, "resultString": self.result_string, }`S3BatchOperationResponseRecord(task_id: 'str', result_code: 'RESULT_CODE_TYPE', result_string: 'str | None' = None) ### Class variables- `var result_code : Literal['Succeeded', 'TemporaryFailure', 'PermanentFailure']`
- `var result_string : str | None`
- `var task_id : str`
 ### Methods- `def asdict(self) ‑> dict[str, typing.Any]`
- 
## Expand source code`def asdict(self) -> dict[str, Any]: if self.result_code not in VALID_RESULT_CODES: warnings.warn( stacklevel=2, message=f"The resultCode {self.result_code} is not valid. " f"Choose from {', '.join(map(repr, VALID_RESULT_CODES))}.", ) return { "taskId": self.task_id, "resultCode": self.result_code, "resultString": self.result_string, }`
 
- `class S3Event (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class S3Event(DictWrapper): """S3 event notification Documentation: ------------- - https://docs.aws.amazon.com/lambda/latest/dg/with-s3.html - https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html - https://docs.aws.amazon.com/AmazonS3/latest/dev/notification-content-structure.html """ @property def records(self) -> Iterator[S3EventRecord]: for record in self["Records"]: yield S3EventRecord(record) @property def record(self) -> S3EventRecord: """Get the first s3 event record""" return next(self.records) @property def bucket_name(self) -> str: """Get the bucket name for the first s3 event record""" return self["Records"][0]["s3"]["bucket"]["name"] @property def object_key(self) -> str: """Get the object key for the first s3 event record and unquote plus""" return unquote_plus(self["Records"][0]["s3"]["object"]["key"])`S3 event notification ## Documentation:- [https://docs.aws.amazon.com/lambda/latest/dg/with-s3.html](https://docs.aws.amazon.com/lambda/latest/dg/with-s3.html)
- [https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html)
- [https://docs.aws.amazon.com/AmazonS3/latest/dev/notification-content-structure.html](https://docs.aws.amazon.com/AmazonS3/latest/dev/notification-content-structure.html)
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
 ### Instance variables- `prop bucket_name : str`
- 
## Expand source code`@property def bucket_name(self) -> str: """Get the bucket name for the first s3 event record""" return self["Records"][0]["s3"]["bucket"]["name"]`Get the bucket name for the first s3 event record 
- `prop object_key : str`
- 
## Expand source code`@property def object_key(self) -> str: """Get the object key for the first s3 event record and unquote plus""" return unquote_plus(self["Records"][0]["s3"]["object"]["key"])`Get the object key for the first s3 event record and unquote plus 
- `prop record : S3EventRecord`
- 
## Expand source code`@property def record(self) -> S3EventRecord: """Get the first s3 event record""" return next(self.records)`Get the first s3 event record 
- `prop records : Iterator[S3EventRecord]`
- 
## Expand source code`@property def records(self) -> Iterator[S3EventRecord]: for record in self["Records"]: yield S3EventRecord(record)`
 ### Inherited members
- `class S3EventBridgeNotificationEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class S3EventBridgeNotificationEvent(EventBridgeEvent): """Amazon S3EventBridge Event Documentation: -------------- - https://docs.aws.amazon.com/AmazonS3/latest/userguide/ev-events.html """ @property def detail(self) -> S3EventBridgeNotificationDetail: # type: ignore[override] """S3 notification details""" return S3EventBridgeNotificationDetail(self["detail"])`Amazon S3EventBridge Event ## Documentation:## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [EventBridgeEvent](event_bridge_event.html#aws_lambda_powertools.utilities.data_classes.event_bridge_event.EventBridgeEvent)
- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- `prop detail : S3EventBridgeNotificationDetail`
- 
## Expand source code`@property def detail(self) -> S3EventBridgeNotificationDetail: # type: ignore[override] """S3 notification details""" return S3EventBridgeNotificationDetail(self["detail"])`S3 notification details 
 ### Inherited members
- `class SESEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class SESEvent(DictWrapper): """Amazon SES to receive message event trigger NOTE: There is a 30-second timeout on RequestResponse invocations. Documentation: -------------- - https://docs.aws.amazon.com/lambda/latest/dg/services-ses.html - https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-action-lambda.html """ @property def records(self) -> Iterator[SESEventRecord]: for record in self["Records"]: yield SESEventRecord(record) @property def record(self) -> SESEventRecord: return next(self.records) @property def mail(self) -> SESMail: return self.record.ses.mail @property def receipt(self) -> SESReceipt: return self.record.ses.receipt`Amazon SES to receive message event trigger NOTE: There is a 30-second timeout on RequestResponse invocations. ## Documentation:- [https://docs.aws.amazon.com/lambda/latest/dg/services-ses.html](https://docs.aws.amazon.com/lambda/latest/dg/services-ses.html)
- [https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-action-lambda.html](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-action-lambda.html)
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
 ### Instance variables- `prop mail : SESMail`
- 
## Expand source code`@property def mail(self) -> SESMail: return self.record.ses.mail`
- `prop receipt : SESReceipt`
- 
## Expand source code`@property def receipt(self) -> SESReceipt: return self.record.ses.receipt`
- `prop record : SESEventRecord`
- 
## Expand source code`@property def record(self) -> SESEventRecord: return next(self.records)`
- `prop records : Iterator[SESEventRecord]`
- 
## Expand source code`@property def records(self) -> Iterator[SESEventRecord]: for record in self["Records"]: yield SESEventRecord(record)`
 ### Inherited members
- `class SNSEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class SNSEvent(DictWrapper): """SNS Event Documentation: ------------- - https://docs.aws.amazon.com/lambda/latest/dg/with-sns.html """ @property def records(self) -> Iterator[SNSEventRecord]: for record in self["Records"]: yield SNSEventRecord(record) @property def record(self) -> SNSEventRecord: """Return the first SNS event record""" return next(self.records) @property def sns_message(self) -> str: """Return the message for the first sns event record""" return self.record.sns.message`SNS Event ## Documentation:## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop record : SNSEventRecord`
- 
## Expand source code`@property def record(self) -> SNSEventRecord: """Return the first SNS event record""" return next(self.records)`Return the first SNS event record 
- `prop records : Iterator[SNSEventRecord]`
- 
## Expand source code`@property def records(self) -> Iterator[SNSEventRecord]: for record in self["Records"]: yield SNSEventRecord(record)`
- `prop sns_message : str`
- 
## Expand source code`@property def sns_message(self) -> str: """Return the message for the first sns event record""" return self.record.sns.message`Return the message for the first sns event record 
 ### Inherited members
- `class SQSEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class SQSEvent(DictWrapper): """SQS Event Documentation: -------------- - https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html """ @property def records(self) -> Iterator[SQSRecord]: for record in self["Records"]: yield SQSRecord(data=record, json_deserializer=self._json_deserializer)`SQS Event ## Documentation:## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop records : Iterator[SQSRecord]`
- 
## Expand source code`@property def records(self) -> Iterator[SQSRecord]: for record in self["Records"]: yield SQSRecord(data=record, json_deserializer=self._json_deserializer)`
 ### Inherited members
- `class SecretsManagerEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class SecretsManagerEvent(DictWrapper): @property def secret_id(self) -> str: """SecretId: The secret ARN or identifier""" return self["SecretId"] @property def client_request_token(self) -> str: """ClientRequestToken: The ClientRequestToken associated with the secret version""" return self["ClientRequestToken"] @property def version_id(self) -> str: """Alias to ClientRequestToken to get token associated to version""" return self["ClientRequestToken"] @property def step(self) -> Literal["createSecret", "setSecret", "testSecret", "finishSecret"]: """Step: The rotation step (one of createSecret, setSecret, testSecret, or finishSecret)""" return self["Step"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop client_request_token : str`
- 
## Expand source code`@property def client_request_token(self) -> str: """ClientRequestToken: The ClientRequestToken associated with the secret version""" return self["ClientRequestToken"]`ClientRequestToken: The ClientRequestToken associated with the secret version 
- `prop secret_id : str`
- 
## Expand source code`@property def secret_id(self) -> str: """SecretId: The secret ARN or identifier""" return self["SecretId"]`SecretId: The secret ARN or identifier 
- `prop step : Literal['createSecret', 'setSecret', 'testSecret', 'finishSecret']`
- 
## Expand source code`@property def step(self) -> Literal["createSecret", "setSecret", "testSecret", "finishSecret"]: """Step: The rotation step (one of createSecret, setSecret, testSecret, or finishSecret)""" return self["Step"]`Step: The rotation step (one of createSecret, setSecret, testSecret, or finishSecret) 
- `prop version_id : str`
- 
## Expand source code`@property def version_id(self) -> str: """Alias to ClientRequestToken to get token associated to version""" return self["ClientRequestToken"]`Alias to ClientRequestToken to get token associated to version 
 ### Inherited members
- `class TransferFamilyAuthorizer (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class TransferFamilyAuthorizer(DictWrapper): @property def username(self) -> str: """The username used for authentication""" return self["username"] @property def password(self) -> str | None: """ The password used for authentication. None in case customer authenticating with certificates """ return self["password"] @property def protocol(self) -> str: """The protocol can be SFTP, FTP or FTPS""" return self["protocol"] @property def server_id(self) -> str: """The AWS Transfer Family ServerID""" return self["serverId"] @property def source_ip(self) -> str: """The customer IP used for connection""" return self["sourceIp"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop password : str | None`
- 
## Expand source code`@property def password(self) -> str | None: """ The password used for authentication. None in case customer authenticating with certificates """ return self["password"]`The password used for authentication. None in case customer authenticating with certificates 
- `prop protocol : str`
- 
## Expand source code`@property def protocol(self) -> str: """The protocol can be SFTP, FTP or FTPS""" return self["protocol"]`The protocol can be SFTP, FTP or FTPS 
- `prop server_id : str`
- 
## Expand source code`@property def server_id(self) -> str: """The AWS Transfer Family ServerID""" return self["serverId"]`The AWS Transfer Family ServerID 
- `prop source_ip : str`
- 
## Expand source code`@property def source_ip(self) -> str: """The customer IP used for connection""" return self["sourceIp"]`The customer IP used for connection 
- `prop username : str`
- 
## Expand source code`@property def username(self) -> str: """The username used for authentication""" return self["username"]`The username used for authentication 
 ### Inherited members
- `class TransferFamilyAuthorizerResponse`
- 
## Expand source code`class TransferFamilyAuthorizerResponse: def _build_authentication_response( self, role_arn: str, policy: str | None = None, home_directory: str | None = None, home_directory_details: dict | None = None, home_directory_type: Literal["LOGICAL", "PATH"] = "PATH", user_gid: int | None = None, user_uid: int | None = None, public_keys: str | None = None, ) -> dict[str, Any]: response: dict[str, Any] = {} if home_directory_type == "PATH": if not home_directory: raise ValueError("home_directory must be set when home_directory_type is PATH") response["HomeDirectory"] = home_directory elif home_directory_type == "LOGICAL": if not home_directory_details: raise ValueError("home_directory_details must be set when home_directory_type is LOGICAL") response["HomeDirectoryDetails"] = [home_directory_details] else: raise ValueError(f"Invalid home_directory_type: {home_directory_type}") if user_uid is not None: response["PosixProfile"] = {"Gid": user_gid, "Uid": user_gid} if policy: response["Policy"] = policy if public_keys: response["PublicKeys"] = public_keys response["Role"] = role_arn response["HomeDirectoryType"] = home_directory_type return response def build_authentication_response_efs( self, role_arn: str, user_gid: int, user_uid: int, policy: str | None = None, home_directory: str | None = None, home_directory_details: dict | None = None, home_directory_type: Literal["LOGICAL", "PATH"] = "PATH", public_keys: str | None = None, ) -> dict[str, Any]: """ Build an authentication response for AWS Transfer Family using EFS (Elastic File System). Parameters: ----------- role_arn : str The Amazon Resource Name (ARN) of the IAM role. user_gid : int The group ID of the user. user_uid : int The user ID. policy : str | None, optional The IAM policy document. Defaults to None. home_directory : str | None, optional The home directory path. Required if home_directory_type is "PATH". Defaults to None. home_directory_details : dict | None, optional Details of the home directory. Required if home_directory_type is "LOGICAL". Defaults to None. home_directory_type : Literal["LOGICAL", "PATH"], optional The type of home directory. Must be either "LOGICAL" or "PATH". Defaults to "PATH". public_keys : str | None, optional The public keys associated with the user. Defaults to None. Returns: -------- dict[str, Any] A dictionary containing the authentication response with various details such as role ARN, policy, home directory information, and user details. Raises: ------- ValueError If an invalid home_directory_type is provided or if required parameters are missing for the specified home_directory_type. """ return self._build_authentication_response( role_arn=role_arn, policy=policy, home_directory=home_directory, home_directory_details=home_directory_details, home_directory_type=home_directory_type, public_keys=public_keys, user_gid=user_gid, user_uid=user_uid, ) def build_authentication_response_s3( self, role_arn: str, policy: str | None = None, home_directory: str | None = None, home_directory_details: dict | None = None, home_directory_type: Literal["LOGICAL", "PATH"] = "PATH", public_keys: str | None = None, ) -> dict[str, Any]: """ Build an authentication response for Amazon S3. This method constructs an authentication response tailored for S3 access, likely by calling an internal method with the provided parameters. Parameters: ----------- role_arn : str The Amazon Resource Name (ARN) of the IAM role for S3 access. policy : str | None, optional The IAM policy document for S3 access. Defaults to None. home_directory : str | None, optional The home directory path in S3. Required if home_directory_type is "PATH". Defaults to None. home_directory_details : dict | None, optional Details of the home directory in S3. Required if home_directory_type is "LOGICAL". Defaults to None. home_directory_type : Literal["LOGICAL", "PATH"], optional The type of home directory in S3. Must be either "LOGICAL" or "PATH". Defaults to "PATH". public_keys : str | None, optional The public keys associated with the user for S3 access. Defaults to None. Returns: -------- dict[str, Any] A dictionary containing the authentication response with various details such as role ARN, policy, home directory information, and potentially other S3-specific attributes. Raises: ------- ValueError If an invalid home_directory_type is provided or if required parameters are missing for the specified home_directory_type. """ return self._build_authentication_response( role_arn=role_arn, policy=policy, home_directory=home_directory, home_directory_details=home_directory_details, home_directory_type=home_directory_type, public_keys=public_keys, )`### Methods- `def build_authentication_response_efs(self,`
 role_arn: str,
 user_gid: int,
 user_uid: int,
 policy: str | None = None,
 home_directory: str | None = None,
 home_directory_details: dict | None = None,
 home_directory_type: "Literal['LOGICAL', 'PATH']" = 'PATH',
 public_keys: str | None = None) ‑> dict[str, typing.Any]
- 
## Expand source code`def build_authentication_response_efs( self, role_arn: str, user_gid: int, user_uid: int, policy: str | None = None, home_directory: str | None = None, home_directory_details: dict | None = None, home_directory_type: Literal["LOGICAL", "PATH"] = "PATH", public_keys: str | None = None, ) -> dict[str, Any]: """ Build an authentication response for AWS Transfer Family using EFS (Elastic File System). Parameters: ----------- role_arn : str The Amazon Resource Name (ARN) of the IAM role. user_gid : int The group ID of the user. user_uid : int The user ID. policy : str | None, optional The IAM policy document. Defaults to None. home_directory : str | None, optional The home directory path. Required if home_directory_type is "PATH". Defaults to None. home_directory_details : dict | None, optional Details of the home directory. Required if home_directory_type is "LOGICAL". Defaults to None. home_directory_type : Literal["LOGICAL", "PATH"], optional The type of home directory. Must be either "LOGICAL" or "PATH". Defaults to "PATH". public_keys : str | None, optional The public keys associated with the user. Defaults to None. Returns: -------- dict[str, Any] A dictionary containing the authentication response with various details such as role ARN, policy, home directory information, and user details. Raises: ------- ValueError If an invalid home_directory_type is provided or if required parameters are missing for the specified home_directory_type. """ return self._build_authentication_response( role_arn=role_arn, policy=policy, home_directory=home_directory, home_directory_details=home_directory_details, home_directory_type=home_directory_type, public_keys=public_keys, user_gid=user_gid, user_uid=user_uid, )`Build an authentication response for AWS Transfer Family using EFS (Elastic File System). ## Parameters:role_arn : str The Amazon Resource Name (ARN) of the IAM role. user_gid : int The group ID of the user. user_uid : int The user ID. policy : str | None, optional The IAM policy document. Defaults to None. home_directory : str | None, optional The home directory path. Required if home_directory_type is "PATH". Defaults to None. home_directory_details : dict | None, optional Details of the home directory. Required if home_directory_type is "LOGICAL". Defaults to None. home_directory_type : Literal["LOGICAL", "PATH"], optional The type of home directory. Must be either "LOGICAL" or "PATH". Defaults to "PATH". public_keys : str | None, optional The public keys associated with the user. Defaults to None. ## Returns:dict[str, Any] A dictionary containing the authentication response with various details such as role ARN, policy, home directory information, and user details. ## Raises:ValueError If an invalid home_directory_type is provided or if required parameters are missing for the specified home_directory_type. 
- `def build_authentication_response_s3(self,`
 role_arn: str,
 policy: str | None = None,
 home_directory: str | None = None,
 home_directory_details: dict | None = None,
 home_directory_type: "Literal['LOGICAL', 'PATH']" = 'PATH',
 public_keys: str | None = None) ‑> dict[str, typing.Any]
- 
## Expand source code`def build_authentication_response_s3( self, role_arn: str, policy: str | None = None, home_directory: str | None = None, home_directory_details: dict | None = None, home_directory_type: Literal["LOGICAL", "PATH"] = "PATH", public_keys: str | None = None, ) -> dict[str, Any]: """ Build an authentication response for Amazon S3. This method constructs an authentication response tailored for S3 access, likely by calling an internal method with the provided parameters. Parameters: ----------- role_arn : str The Amazon Resource Name (ARN) of the IAM role for S3 access. policy : str | None, optional The IAM policy document for S3 access. Defaults to None. home_directory : str | None, optional The home directory path in S3. Required if home_directory_type is "PATH". Defaults to None. home_directory_details : dict | None, optional Details of the home directory in S3. Required if home_directory_type is "LOGICAL". Defaults to None. home_directory_type : Literal["LOGICAL", "PATH"], optional The type of home directory in S3. Must be either "LOGICAL" or "PATH". Defaults to "PATH". public_keys : str | None, optional The public keys associated with the user for S3 access. Defaults to None. Returns: -------- dict[str, Any] A dictionary containing the authentication response with various details such as role ARN, policy, home directory information, and potentially other S3-specific attributes. Raises: ------- ValueError If an invalid home_directory_type is provided or if required parameters are missing for the specified home_directory_type. """ return self._build_authentication_response( role_arn=role_arn, policy=policy, home_directory=home_directory, home_directory_details=home_directory_details, home_directory_type=home_directory_type, public_keys=public_keys, )`Build an authentication response for Amazon S3. This method constructs an authentication response tailored for S3 access, likely by calling an internal method with the provided parameters. ## Parameters:role_arn : str The Amazon Resource Name (ARN) of the IAM role for S3 access. policy : str | None, optional The IAM policy document for S3 access. Defaults to None. home_directory : str | None, optional The home directory path in S3. Required if home_directory_type is "PATH". Defaults to None. home_directory_details : dict | None, optional Details of the home directory in S3. Required if home_directory_type is "LOGICAL". Defaults to None. home_directory_type : Literal["LOGICAL", "PATH"], optional The type of home directory in S3. Must be either "LOGICAL" or "PATH". Defaults to "PATH". public_keys : str | None, optional The public keys associated with the user for S3 access. Defaults to None. ## Returns:dict[str, Any] A dictionary containing the authentication response with various details such as role ARN, policy, home directory information, and potentially other S3-specific attributes. ## Raises:ValueError If an invalid home_directory_type is provided or if required parameters are missing for the specified home_directory_type. 
 
- `class VPCLatticeEvent (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class VPCLatticeEvent(VPCLatticeEventBase): @property def raw_path(self) -> str: """The raw VPC Lattice request path.""" return self["raw_path"] @property def is_base64_encoded(self) -> bool: """A boolean flag to indicate if the applicable request payload is Base64-encode""" return self["is_base64_encoded"] # VPCLattice event has no path field # Added here for consistency with the BaseProxyEvent class @property def path(self) -> str: return self["raw_path"] @property def query_string_parameters(self) -> dict[str, str]: """The request query string parameters.""" return self["query_string_parameters"] @cached_property def resolved_headers_field(self) -> dict[str, Any]: return CaseInsensitiveDict((k, v.split(",") if "," in v else v) for k, v in self.headers.items())`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [VPCLatticeEventBase](vpc_lattice.html#aws_lambda_powertools.utilities.data_classes.vpc_lattice.VPCLatticeEventBase)
- [BaseProxyEvent](common.html#aws_lambda_powertools.utilities.data_classes.common.BaseProxyEvent)
- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- `prop is_base64_encoded : bool`
- 
## Expand source code`@property def is_base64_encoded(self) -> bool: """A boolean flag to indicate if the applicable request payload is Base64-encode""" return self["is_base64_encoded"]`A boolean flag to indicate if the applicable request payload is Base64-encode 
- `prop path : str`
- 
## Expand source code`@property def path(self) -> str: return self["raw_path"]`
- `prop query_string_parameters : dict[str, str]`
- 
## Expand source code`@property def query_string_parameters(self) -> dict[str, str]: """The request query string parameters.""" return self["query_string_parameters"]`The request query string parameters. 
- `prop raw_path : str`
- 
## Expand source code`@property def raw_path(self) -> str: """The raw VPC Lattice request path.""" return self["raw_path"]`The raw VPC Lattice request path. 
 ### Inherited members
- `class VPCLatticeEventV2 (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class VPCLatticeEventV2(VPCLatticeEventBase): @property def version(self) -> str: """The VPC Lattice v2 Event version""" return self["version"] @property def is_base64_encoded(self) -> bool | None: """A boolean flag to indicate if the applicable request payload is Base64-encode""" return self.get("isBase64Encoded") @property def path(self) -> str: """The VPC Lattice v2 Event path""" return self["path"] @property def request_context(self) -> vpcLatticeEventV2RequestContext: """The VPC Lattice v2 Event request context.""" return vpcLatticeEventV2RequestContext(self["requestContext"]) @cached_property def query_string_parameters(self) -> dict[str, str]: """The request query string parameters. For VPC Lattice V2, the queryStringParameters will contain a dict[str, list[str]] so to keep compatibility with existing utilities, we merge all the values with a comma. """ params = self.get("queryStringParameters") or {} return {k: ",".join(v) for k, v in params.items()} @property def resolved_headers_field(self) -> dict[str, str]: if self.headers is not None: return {key.lower(): value for key, value in self.headers.items()} return {}`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
- Lambda Event Source Event payload
- `json_deserializer`- `Callable`, optional
- function to deserialize `str`,`bytes`,`bytearray`containing a JSON document to a Python`obj`, by default json.loads
 ### Ancestors- [VPCLatticeEventBase](vpc_lattice.html#aws_lambda_powertools.utilities.data_classes.vpc_lattice.VPCLatticeEventBase)
- [BaseProxyEvent](common.html#aws_lambda_powertools.utilities.data_classes.common.BaseProxyEvent)
- [DictWrapper](common.html#aws_lambda_powertools.utilities.data_classes.common.DictWrapper)
- collections.abc.Mapping
- collections.abc.Collection
- collections.abc.Sized
- collections.abc.Iterable
- collections.abc.Container
- typing.Generic
 ### Instance variables- `prop is_base64_encoded : bool | None`
- 
## Expand source code`@property def is_base64_encoded(self) -> bool | None: """A boolean flag to indicate if the applicable request payload is Base64-encode""" return self.get("isBase64Encoded")`A boolean flag to indicate if the applicable request payload is Base64-encode 
- `prop path : str`
- 
## Expand source code`@property def path(self) -> str: """The VPC Lattice v2 Event path""" return self["path"]`The VPC Lattice v2 Event path 
- `var query_string_parameters : dict[str, str]`
- 
## Expand source code`@cached_property def query_string_parameters(self) -> dict[str, str]: """The request query string parameters. For VPC Lattice V2, the queryStringParameters will contain a dict[str, list[str]] so to keep compatibility with existing utilities, we merge all the values with a comma. """ params = self.get("queryStringParameters") or {} return {k: ",".join(v) for k, v in params.items()}`The request query string parameters. For VPC Lattice V2, the queryStringParameters will contain a dict[str, list[str]] so to keep compatibility with existing utilities, we merge all the values with a comma. 
- `prop request_context : vpcLatticeEventV2RequestContext`
- 
## Expand source code`@property def request_context(self) -> vpcLatticeEventV2RequestContext: """The VPC Lattice v2 Event request context.""" return vpcLatticeEventV2RequestContext(self["requestContext"])`The VPC Lattice v2 Event request context. 
- `prop version : str`
- 
## Expand source code`@property def version(self) -> str: """The VPC Lattice v2 Event version""" return self["version"]`The VPC Lattice v2 Event version 
 ### Inherited members