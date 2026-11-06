# aws_lambda_powertools.utilities.parser.envelopes.apigw_websocket API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/envelopes/apigw_websocket.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/envelopes/apigw_websocket.html)

---

# Module `aws_lambda_powertools.utilities.parser.envelopes.apigw_websocket`

## Classes

- `class ApiGatewayWebSocketEnvelope`
- 
## Expand source code`class ApiGatewayWebSocketEnvelope(BaseEnvelope): """API Gateway WebSockets envelope to extract data within body key of messages routes (not disconnect or connect)""" def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> Model | None: """Parses data found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- Any Parsed detail payload with model provided """ logger.debug( f"Parsing incoming data with Api Gateway WebSockets model {APIGatewayWebSocketMessageEventModel}", ) parsed_envelope: APIGatewayWebSocketMessageEventModel = APIGatewayWebSocketMessageEventModel.model_validate( data, ) logger.debug(f"Parsing event payload in `detail` with {model}") return self._parse(data=parsed_envelope.body, model=model)`API Gateway WebSockets envelope to extract data within body key of messages routes (not disconnect or connect) ### Ancestors- [BaseEnvelope](base.html#aws_lambda_powertools.utilities.parser.envelopes.base.BaseEnvelope)
- abc.ABC
 ### Methods- `def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) ‑> Model | None`
- 
## Expand source code`def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> Model | None: """Parses data found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- Any Parsed detail payload with model provided """ logger.debug( f"Parsing incoming data with Api Gateway WebSockets model {APIGatewayWebSocketMessageEventModel}", ) parsed_envelope: APIGatewayWebSocketMessageEventModel = APIGatewayWebSocketMessageEventModel.model_validate( data, ) logger.debug(f"Parsing event payload in `detail` with {model}") return self._parse(data=parsed_envelope.body, model=model)`Parses data found with model provided ## Parameters- `data`- `dict`
- Lambda event to be parsed
- `model`- `type[Model]`
- Data model provided to parse after extracting data using envelope
 ## Returns- `Any`
- Parsed detail payload with model provided