# aws_lambda_powertools.event_handler.lambda_function_url API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/event_handler/lambda_function_url.html](https://docs.aws.amazon.com/powertools/python/latest/api/event_handler/lambda_function_url.html)

---

# Module `aws_lambda_powertools.event_handler.lambda_function_url`

## Classes

- `class LambdaFunctionUrlResolver (cors: CORSConfig | None = None,`
 debug: bool | None = None,
 serializer: Callable[[dict], str] | None = None,
 strip_prefixes: list[str | Pattern] | None = None,
 enable_validation: bool = False)
- 
## Expand source code`class LambdaFunctionUrlResolver(ApiGatewayResolver): """AWS Lambda Function URL resolver Notes: ----- Lambda Function URL follows the API Gateway HTTP APIs Payload Format Version 2.0. Documentation: - https://docs.aws.amazon.com/lambda/latest/dg/urls-configuration.html - https://docs.aws.amazon.com/lambda/latest/dg/urls-invocation.html#urls-payloads Examples -------- Simple example integrating with Tracer ```python from aws_lambda_powertools import Tracer from aws_lambda_powertools.event_handler import LambdaFunctionUrlResolver tracer = Tracer() app = LambdaFunctionUrlResolver() @app.get("/get-call") def simple_get(): return {"message": "Foo"} @app.post("/post-call") def simple_post(): post_data: dict = app.current_event.json_body return {"message": post_data} @tracer.capture_lambda_handler def lambda_handler(event, context): return app.resolve(event, context) """ current_event: LambdaFunctionUrlEvent def __init__( self, cors: CORSConfig | None = None, debug: bool | None = None, serializer: Callable[[dict], str] | None = None, strip_prefixes: list[str | Pattern] | None = None, enable_validation: bool = False, ): super().__init__( ProxyEventType.LambdaFunctionUrlEvent, cors, debug, serializer, strip_prefixes, enable_validation, ) def _get_base_path(self) -> str: stage = self.current_event.request_context.stage if stage and stage != "$default" and self.current_event.request_context.http.method.startswith(f"/{stage}"): return f"/{stage}" return ""`AWS Lambda Function URL resolver ## Notes:Lambda Function URL follows the API Gateway HTTP APIs Payload Format Version 2.0. Documentation: - [https://docs.aws.amazon.com/lambda/latest/dg/urls-configuration.html](https://docs.aws.amazon.com/lambda/latest/dg/urls-configuration.html)-[https://docs.aws.amazon.com/lambda/latest/dg/urls-invocation.html#urls-payloads](https://docs.aws.amazon.com/lambda/latest/dg/urls-invocation.html#urls-payloads)## ExamplesSimple example integrating with Tracer ```python from aws_lambda_powertools import Tracer from aws_lambda_powertools.event_handler import LambdaFunctionUrlResolver tracer = Tracer() app = LambdaFunctionUrlResolver() @app.get("/get-call") def simple_get(): return {"message": "Foo"} @app.post("/post-call") def simple_post(): post_data: dict = app.current_event.json_body return {"message": post_data} @tracer.capture_lambda_handler def lambda_handler(event, context): return app.resolve(event, context) ## Parameters- `proxy_type`- `ProxyEventType`
- Proxy request type, defaults to API Gateway V1
- `cors`- `CORSConfig`
- Optionally configure and enabled CORS. Not each route will need to have to cors=True
- `debug`- `bool | None`
- Enables debug mode, by default False. Can be also be enabled by "POWERTOOLS_DEV" environment variable
- `serializer`- `Callable`, optional
- function to serialize `obj`to a JSON formatted`str`, by default json.dumps
- `strip_prefixes`- `list[str | Pattern]`, optional
- optional list of prefixes to be removed from the request path before doing the routing. This is often used with api gateways with multiple custom mappings. Each prefix can be a static string or a compiled regex pattern
- `enable_validation`- `bool | None`
- Enables validation of the request body against the route schema, by default False.
 ### Ancestors- [ApiGatewayResolver](api_gateway.html#aws_lambda_powertools.event_handler.api_gateway.ApiGatewayResolver)
- [BaseRouter](api_gateway.html#aws_lambda_powertools.event_handler.api_gateway.BaseRouter)
- abc.ABC
 ### Class variables- `var current_event : LambdaFunctionUrlEvent`
 ### Inherited members