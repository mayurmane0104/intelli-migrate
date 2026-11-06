# aws_lambda_powertools.utilities.parser.envelopes.sqs API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/envelopes/sqs.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/envelopes/sqs.html)

---

# Module `aws_lambda_powertools.utilities.parser.envelopes.sqs`

## Classes

- `class SqsEnvelope`
- 
## Expand source code`class SqsEnvelope(BaseEnvelope): """SQS Envelope to extract array of Records The record's body parameter is a string, though it can also be a JSON encoded string. Regardless of its type it'll be parsed into a BaseModel object. Note: Records will be parsed the same way so if model is str, all items in the list will be parsed as str and npt as JSON (and vice versa) """ def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> list[Model | None]: """Parses records found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- list List of records parsed with model provided """ logger.debug(f"Parsing incoming data with SQS model {SqsModel}") parsed_envelope = SqsModel.model_validate(data) logger.debug(f"Parsing SQS records in `body` with {model}") return [self._parse(data=record.body, model=model) for record in parsed_envelope.Records]`SQS Envelope to extract array of Records The record's body parameter is a string, though it can also be a JSON encoded string. Regardless of its type it'll be parsed into a BaseModel object. Note: Records will be parsed the same way so if model is str, all items in the list will be parsed as str and npt as JSON (and vice versa) ### Ancestors- [BaseEnvelope](base.html#aws_lambda_powertools.utilities.parser.envelopes.base.BaseEnvelope)
- abc.ABC
 ### Methods- `def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) ‑> list[Model | None]`
- 
## Expand source code`def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> list[Model | None]: """Parses records found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- list List of records parsed with model provided """ logger.debug(f"Parsing incoming data with SQS model {SqsModel}") parsed_envelope = SqsModel.model_validate(data) logger.debug(f"Parsing SQS records in `body` with {model}") return [self._parse(data=record.body, model=model) for record in parsed_envelope.Records]`Parses records found with model provided ## Parameters- `data`- `dict`
- Lambda event to be parsed
- `model`- `type[Model]`
- Data model provided to parse after extracting data using envelope
 ## Returns- `list`
- List of records parsed with model provided