# aws_lambda_powertools.event_handler.router API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/event_handler/router.html](https://docs.aws.amazon.com/powertools/python/latest/api/event_handler/router.html)

---

# Module `aws_lambda_powertools.event_handler.router`

## Classes

- `class ALBRouter`
- 
## Expand source code`class ALBRouter(Router): """Specialized Router class that exposes current_event as an ALBEvent""" current_event: ALBEvent`Specialized Router class that exposes current_event as an ALBEvent ### Ancestors- [Router](api_gateway.html#aws_lambda_powertools.event_handler.api_gateway.Router)
- [BaseRouter](api_gateway.html#aws_lambda_powertools.event_handler.api_gateway.BaseRouter)
- abc.ABC
 ### Class variables- `var current_event : ALBEvent`
 ### Inherited members
- `class APIGatewayHttpRouter`
- 
## Expand source code`class APIGatewayHttpRouter(Router): """Specialized Router class that exposes current_event as an APIGatewayProxyEventV2""" current_event: APIGatewayProxyEventV2`Specialized Router class that exposes current_event as an APIGatewayProxyEventV2 ### Ancestors- [Router](api_gateway.html#aws_lambda_powertools.event_handler.api_gateway.Router)
- [BaseRouter](api_gateway.html#aws_lambda_powertools.event_handler.api_gateway.BaseRouter)
- abc.ABC
 ### Class variables- `var current_event : APIGatewayProxyEventV2`
 ### Inherited members
- `class APIGatewayRouter`
- 
## Expand source code`class APIGatewayRouter(Router): """Specialized Router class that exposes current_event as an APIGatewayProxyEvent""" current_event: APIGatewayProxyEvent`Specialized Router class that exposes current_event as an APIGatewayProxyEvent ### Ancestors- [Router](api_gateway.html#aws_lambda_powertools.event_handler.api_gateway.Router)
- [BaseRouter](api_gateway.html#aws_lambda_powertools.event_handler.api_gateway.BaseRouter)
- abc.ABC
 ### Class variables- `var current_event : APIGatewayProxyEvent`
 ### Inherited members
- `class LambdaFunctionUrlRouter`
- 
## Expand source code`class LambdaFunctionUrlRouter(Router): """Specialized Router class that exposes current_event as a LambdaFunctionUrlEvent""" current_event: LambdaFunctionUrlEvent`Specialized Router class that exposes current_event as a LambdaFunctionUrlEvent ### Ancestors- [Router](api_gateway.html#aws_lambda_powertools.event_handler.api_gateway.Router)
- [BaseRouter](api_gateway.html#aws_lambda_powertools.event_handler.api_gateway.BaseRouter)
- abc.ABC
 ### Class variables- `var current_event : LambdaFunctionUrlEvent`
 ### Inherited members