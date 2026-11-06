# aws_lambda_powertools.utilities.parser.models.lambda_function_url API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/models/lambda_function_url.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/models/lambda_function_url.html)

---

# Module `aws_lambda_powertools.utilities.parser.models.lambda_function_url`

## Classes

- `class LambdaFunctionUrlModel (**data: Any)`
- 
## Expand source code`class LambdaFunctionUrlModel(APIGatewayProxyEventV2Model): """AWS Lambda Function URL model Notes: ----- Lambda Function URL follows the API Gateway HTTP APIs Payload Format Version 2.0. Keys related to API Gateway features not available in Function URL use a sentinel value (e.g.`routeKey`, `stage`). Documentation: - https://docs.aws.amazon.com/lambda/latest/dg/urls-configuration.html - https://docs.aws.amazon.com/lambda/latest/dg/urls-invocation.html#urls-payloads """ pass`AWS Lambda Function URL model ## Notes:Lambda Function URL follows the API Gateway HTTP APIs Payload Format Version 2.0. Keys related to API Gateway features not available in Function URL use a sentinel value (e.g. `routeKey`,`stage`).Documentation: - [https://docs.aws.amazon.com/lambda/latest/dg/urls-configuration.html](https://docs.aws.amazon.com/lambda/latest/dg/urls-configuration.html)-[https://docs.aws.amazon.com/lambda/latest/dg/urls-invocation.html#urls-payloads](https://docs.aws.amazon.com/lambda/latest/dg/urls-invocation.html#urls-payloads)Create a new model by parsing and validating input data from keyword arguments. Raises [ `ValidationError`][pydantic_core.ValidationError] if the input data cannot be validated to form a valid model.`self`is explicitly positional-only to allow`self`as a field name.### Ancestors- [APIGatewayProxyEventV2Model](apigwv2.html#aws_lambda_powertools.utilities.parser.models.apigwv2.APIGatewayProxyEventV2Model)
- pydantic.main.BaseModel
 ### Class variables- `var model_config`