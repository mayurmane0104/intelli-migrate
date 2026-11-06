# aws_lambda_powertools.utilities.parser.envelopes.bedrock_agent API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/envelopes/bedrock_agent.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/envelopes/bedrock_agent.html)

---

# Module `aws_lambda_powertools.utilities.parser.envelopes.bedrock_agent`

## Classes

- `class BedrockAgentEnvelope`
- 
## Expand source code`class BedrockAgentEnvelope(BaseEnvelope): """Bedrock Agent envelope to extract data within input_text key""" def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> Model | None: """Parses data found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- Model | None Parsed detail payload with model provided """ logger.debug(f"Parsing incoming data with Bedrock Agent model {BedrockAgentEventModel}") parsed_envelope: BedrockAgentEventModel = BedrockAgentEventModel.model_validate(data) logger.debug(f"Parsing event payload in `input_text` with {model}") return self._parse(data=parsed_envelope.input_text, model=model)`Bedrock Agent envelope to extract data within input_text key ### Ancestors- [BaseEnvelope](base.html#aws_lambda_powertools.utilities.parser.envelopes.base.BaseEnvelope)
- abc.ABC
 ### Methods- `def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) ‑> Model | None`
- 
## Expand source code`def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> Model | None: """Parses data found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- Model | None Parsed detail payload with model provided """ logger.debug(f"Parsing incoming data with Bedrock Agent model {BedrockAgentEventModel}") parsed_envelope: BedrockAgentEventModel = BedrockAgentEventModel.model_validate(data) logger.debug(f"Parsing event payload in `input_text` with {model}") return self._parse(data=parsed_envelope.input_text, model=model)`Parses data found with model provided ## Parameters- `data`- `dict`
- Lambda event to be parsed
- `model`- `type[Model]`
- Data model provided to parse after extracting data using envelope
 ## Returns- `Model | None`
- Parsed detail payload with model provided