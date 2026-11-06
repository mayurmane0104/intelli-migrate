# aws_lambda_powertools.utilities.parser.envelopes.lambda_function_url API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/envelopes/lambda_function_url.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/envelopes/lambda_function_url.html)

---

# Module `aws_lambda_powertools.utilities.parser.envelopes.lambda_function_url`

## Classes

- `class LambdaFunctionUrlEnvelope`
- 
## Expand source code`class LambdaFunctionUrlEnvelope(BaseEnvelope): """Lambda function URL envelope to extract data within body key""" def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> Model | None: """Parses data found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- Any Parsed detail payload with model provided """ logger.debug(f"Parsing incoming data with Lambda function URL model {LambdaFunctionUrlModel}") parsed_envelope: LambdaFunctionUrlModel = LambdaFunctionUrlModel.model_validate(data) logger.debug(f"Parsing event payload in `detail` with {model}") return self._parse(data=parsed_envelope.body, model=model)`Lambda function URL envelope to extract data within body key ### Ancestors- [BaseEnvelope](base.html#aws_lambda_powertools.utilities.parser.envelopes.base.BaseEnvelope)
- abc.ABC
 ### Methods- `def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) ‑> Model | None`
- 
## Expand source code`def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> Model | None: """Parses data found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- Any Parsed detail payload with model provided """ logger.debug(f"Parsing incoming data with Lambda function URL model {LambdaFunctionUrlModel}") parsed_envelope: LambdaFunctionUrlModel = LambdaFunctionUrlModel.model_validate(data) logger.debug(f"Parsing event payload in `detail` with {model}") return self._parse(data=parsed_envelope.body, model=model)`Parses data found with model provided ## Parameters- `data`- `dict`
- Lambda event to be parsed
- `model`- `type[Model]`
- Data model provided to parse after extracting data using envelope
 ## Returns- `Any`
- Parsed detail payload with model provided