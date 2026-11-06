# aws_lambda_powertools.utilities.parser.envelopes.event_bridge API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/envelopes/event_bridge.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/envelopes/event_bridge.html)

---

# Module `aws_lambda_powertools.utilities.parser.envelopes.event_bridge`

## Classes

- `class EventBridgeEnvelope`
- 
## Expand source code`class EventBridgeEnvelope(BaseEnvelope): """EventBridge envelope to extract data within detail key""" def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> Model | None: """Parses data found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- Any Parsed detail payload with model provided """ logger.debug(f"Parsing incoming data with EventBridge model {EventBridgeModel}") parsed_envelope: EventBridgeModel = EventBridgeModel.model_validate(data) logger.debug(f"Parsing event payload in `detail` with {model}") return self._parse(data=parsed_envelope.detail, model=model)`EventBridge envelope to extract data within detail key ### Ancestors- [BaseEnvelope](base.html#aws_lambda_powertools.utilities.parser.envelopes.base.BaseEnvelope)
- abc.ABC
 ### Methods- `def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) ‑> Model | None`
- 
## Expand source code`def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> Model | None: """Parses data found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- Any Parsed detail payload with model provided """ logger.debug(f"Parsing incoming data with EventBridge model {EventBridgeModel}") parsed_envelope: EventBridgeModel = EventBridgeModel.model_validate(data) logger.debug(f"Parsing event payload in `detail` with {model}") return self._parse(data=parsed_envelope.detail, model=model)`Parses data found with model provided ## Parameters- `data`- `dict`
- Lambda event to be parsed
- `model`- `type[Model]`
- Data model provided to parse after extracting data using envelope
 ## Returns- `Any`
- Parsed detail payload with model provided