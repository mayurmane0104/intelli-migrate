# aws_lambda_powertools.utilities.parser.envelopes.dynamodb API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/envelopes/dynamodb.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/envelopes/dynamodb.html)

---

# Module `aws_lambda_powertools.utilities.parser.envelopes.dynamodb`

## Classes

- `class DynamoDBStreamEnvelope`
- 
## Expand source code`class DynamoDBStreamEnvelope(BaseEnvelope): """DynamoDB Stream Envelope to extract data within NewImage/OldImage Note: Values are the parsed models. Images' values can also be None, and length of the list is the record's amount in the original event. """ def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> list[dict[str, Model | None]]: """Parses DynamoDB Stream records found in either NewImage and OldImage with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- list List of dictionaries with NewImage and OldImage records parsed with model provided """ logger.debug(f"Parsing incoming data with DynamoDB Stream model {DynamoDBStreamModel}") parsed_envelope = DynamoDBStreamModel.model_validate(data) logger.debug(f"Parsing DynamoDB Stream new and old records with {model}") return [ { "NewImage": self._parse(data=record.dynamodb.NewImage, model=model), "OldImage": self._parse(data=record.dynamodb.OldImage, model=model), } for record in parsed_envelope.Records ]`DynamoDB Stream Envelope to extract data within NewImage/OldImage Note: Values are the parsed models. Images' values can also be None, and length of the list is the record's amount in the original event. ### Ancestors- [BaseEnvelope](base.html#aws_lambda_powertools.utilities.parser.envelopes.base.BaseEnvelope)
- abc.ABC
 ### Methods- `def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) ‑> list[dict[str, Model | None]]`
- 
## Expand source code`def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> list[dict[str, Model | None]]: """Parses DynamoDB Stream records found in either NewImage and OldImage with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- list List of dictionaries with NewImage and OldImage records parsed with model provided """ logger.debug(f"Parsing incoming data with DynamoDB Stream model {DynamoDBStreamModel}") parsed_envelope = DynamoDBStreamModel.model_validate(data) logger.debug(f"Parsing DynamoDB Stream new and old records with {model}") return [ { "NewImage": self._parse(data=record.dynamodb.NewImage, model=model), "OldImage": self._parse(data=record.dynamodb.OldImage, model=model), } for record in parsed_envelope.Records ]`Parses DynamoDB Stream records found in either NewImage and OldImage with model provided ## Parameters- `data`- `dict`
- Lambda event to be parsed
- `model`- `type[Model]`
- Data model provided to parse after extracting data using envelope
 ## Returns- `list`
- List of dictionaries with NewImage and OldImage records parsed with model provided