# aws_lambda_powertools.utilities.data_classes.alb_event API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/alb_event.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/alb_event.html)

---

# Module `aws_lambda_powertools.utilities.data_classes.alb_event`

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
- `prop request_context :`- [ALBEventRequestContext](#aws_lambda_powertools.utilities.data_classes.alb_event.ALBEventRequestContext)
- 
## Expand source code`@property def request_context(self) -> ALBEventRequestContext: return ALBEventRequestContext(self._data)`
 ### Methods- `def header_serializer(self) ‑>`- [BaseHeadersSerializer](../../shared/headers_serializer.html#aws_lambda_powertools.shared.headers_serializer.BaseHeadersSerializer)
- 
## Expand source code`def header_serializer(self) -> BaseHeadersSerializer: # When using the ALB integration, the `multiValueHeaders` feature can be disabled (default) or enabled. # We can determine if the feature is enabled by looking if the event has a `multiValueHeaders` key. if self.multi_value_headers: return MultiValueHeadersSerializer() return SingleValueHeadersSerializer()`
 ### Inherited members
- `class ALBEventRequestContext (data: dict[str, Any], json_deserializer: Callable | None = None)`
- 
## Expand source code`class ALBEventRequestContext(DictWrapper): @property def elb_target_group_arn(self) -> str: """Target group arn for your Lambda function""" return self["requestContext"]["elb"]["targetGroupArn"]`Provides a single read only access to a wrapper dict ## Parameters- `data`- `dict[str, Any]`
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
 ### Instance variables- `prop elb_target_group_arn : str`
- 
## Expand source code`@property def elb_target_group_arn(self) -> str: """Target group arn for your Lambda function""" return self["requestContext"]["elb"]["targetGroupArn"]`Target group arn for your Lambda function 
 ### Inherited members