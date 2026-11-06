# aws_lambda_powertools.utilities.data_classes.lambda_function_url_event API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/lambda_function_url_event.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/lambda_function_url_event.html)

---

# Module `aws_lambda_powertools.utilities.data_classes.lambda_function_url_event`

## Classes

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