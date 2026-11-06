# aws_lambda_powertools.utilities.parser.envelopes.apigw API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/envelopes/apigw.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/envelopes/apigw.html)

---

# Module `aws_lambda_powertools.utilities.parser.envelopes.apigw`

## Classes

- `class ApiGatewayEnvelope`
- 
## Expand source code`class ApiGatewayEnvelope(BaseEnvelope): """API Gateway envelope to extract data within body key""" def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> Model | None: """Parses data found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- Any Parsed detail payload with model provided """ logger.debug(f"Parsing incoming data with Api Gateway model {APIGatewayProxyEventModel}") parsed_envelope: APIGatewayProxyEventModel = APIGatewayProxyEventModel.model_validate(data) logger.debug(f"Parsing event payload in `detail` with {model}") return self._parse(data=parsed_envelope.body, model=model)`API Gateway envelope to extract data within body key ### Ancestors- [BaseEnvelope](base.html#aws_lambda_powertools.utilities.parser.envelopes.base.BaseEnvelope)
- abc.ABC
 ### Methods- `def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) ‑> Model | None`
- 
## Expand source code`def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> Model | None: """Parses data found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- Any Parsed detail payload with model provided """ logger.debug(f"Parsing incoming data with Api Gateway model {APIGatewayProxyEventModel}") parsed_envelope: APIGatewayProxyEventModel = APIGatewayProxyEventModel.model_validate(data) logger.debug(f"Parsing event payload in `detail` with {model}") return self._parse(data=parsed_envelope.body, model=model)`Parses data found with model provided ## Parameters- `data`- `dict`
- Lambda event to be parsed
- `model`- `type[Model]`
- Data model provided to parse after extracting data using envelope
 ## Returns- `Any`
- Parsed detail payload with model provided