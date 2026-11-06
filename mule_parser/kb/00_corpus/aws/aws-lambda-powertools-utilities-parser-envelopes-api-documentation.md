# aws_lambda_powertools.utilities.parser.envelopes API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/envelopes/index.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/envelopes/index.html)

---

# Module `aws_lambda_powertools.utilities.parser.envelopes`

## Sub-modules

- [aws_lambda_powertools.utilities.parser.envelopes.apigw](apigw.html)
- [aws_lambda_powertools.utilities.parser.envelopes.apigw_websocket](apigw_websocket.html)
- [aws_lambda_powertools.utilities.parser.envelopes.apigwv2](apigwv2.html)
- [aws_lambda_powertools.utilities.parser.envelopes.base](base.html)
- [aws_lambda_powertools.utilities.parser.envelopes.bedrock_agent](bedrock_agent.html)
- [aws_lambda_powertools.utilities.parser.envelopes.cloudwatch](cloudwatch.html)
- [aws_lambda_powertools.utilities.parser.envelopes.dynamodb](dynamodb.html)
- [aws_lambda_powertools.utilities.parser.envelopes.event_bridge](event_bridge.html)
- [aws_lambda_powertools.utilities.parser.envelopes.kafka](kafka.html)
- [aws_lambda_powertools.utilities.parser.envelopes.kinesis](kinesis.html)
- [aws_lambda_powertools.utilities.parser.envelopes.kinesis_firehose](kinesis_firehose.html)
- [aws_lambda_powertools.utilities.parser.envelopes.lambda_function_url](lambda_function_url.html)
- [aws_lambda_powertools.utilities.parser.envelopes.sns](sns.html)
- [aws_lambda_powertools.utilities.parser.envelopes.sqs](sqs.html)
- [aws_lambda_powertools.utilities.parser.envelopes.vpc_lattice](vpc_lattice.html)
- [aws_lambda_powertools.utilities.parser.envelopes.vpc_latticev2](vpc_latticev2.html)

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
 
 
- `class ApiGatewayV2Envelope`
- 
## Expand source code`class ApiGatewayV2Envelope(BaseEnvelope): """API Gateway V2 envelope to extract data within body key""" def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> Model | None: """Parses data found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- Any Parsed detail payload with model provided """ logger.debug(f"Parsing incoming data with Api Gateway model V2 {APIGatewayProxyEventV2Model}") parsed_envelope: APIGatewayProxyEventV2Model = APIGatewayProxyEventV2Model.model_validate(data) logger.debug(f"Parsing event payload in `detail` with {model}") return self._parse(data=parsed_envelope.body, model=model)`API Gateway V2 envelope to extract data within body key ### Ancestors- [BaseEnvelope](base.html#aws_lambda_powertools.utilities.parser.envelopes.base.BaseEnvelope)
- abc.ABC
 ### Methods- `def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) ‑> Model | None`
- 
## Expand source code`def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> Model | None: """Parses data found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- Any Parsed detail payload with model provided """ logger.debug(f"Parsing incoming data with Api Gateway model V2 {APIGatewayProxyEventV2Model}") parsed_envelope: APIGatewayProxyEventV2Model = APIGatewayProxyEventV2Model.model_validate(data) logger.debug(f"Parsing event payload in `detail` with {model}") return self._parse(data=parsed_envelope.body, model=model)`Parses data found with model provided ## Parameters- `data`- `dict`
- Lambda event to be parsed
- `model`- `type[Model]`
- Data model provided to parse after extracting data using envelope
 ## Returns- `Any`
- Parsed detail payload with model provided
 
 
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
 
 
- `class BaseEnvelope`
- 
## Expand source code`class BaseEnvelope(ABC): """ABC implementation for creating a supported Envelope""" @staticmethod def _parse(data: dict[str, Any] | Any | None, model: type[T]) -> T | None: """Parses envelope data against model provided Parameters ---------- data : dict Data to be parsed and validated model : type[T] Data model to parse and validate data against Returns ------- Any Parsed data """ if data is None: logger.debug("Skipping parsing as event is None") return data adapter = _retrieve_or_set_model_from_cache(model=model) logger.debug("parsing event against model") return _parse_and_validate_event(data=data, adapter=adapter) @abstractmethod def parse(self, data: dict[str, Any] | Any | None, model: type[T]): """Implementation to parse data against envelope model, then against the data model NOTE: Call `_parse` method to fully parse data with model provided. Example ------- **EventBridge envelope implementation example** def parse(...): # 1. parses data against envelope model parsed_envelope = EventBridgeModel(**data) # 2. parses portion of data within the envelope against model return self._parse(data=parsed_envelope.detail, model=data_model) """ return NotImplemented # pragma: no cover`ABC implementation for creating a supported Envelope ### Ancestors- abc.ABC
 ### Subclasses- [ApiGatewayEnvelope](apigw.html#aws_lambda_powertools.utilities.parser.envelopes.apigw.ApiGatewayEnvelope)
- [ApiGatewayWebSocketEnvelope](apigw_websocket.html#aws_lambda_powertools.utilities.parser.envelopes.apigw_websocket.ApiGatewayWebSocketEnvelope)
- [ApiGatewayV2Envelope](apigwv2.html#aws_lambda_powertools.utilities.parser.envelopes.apigwv2.ApiGatewayV2Envelope)
- [BedrockAgentEnvelope](bedrock_agent.html#aws_lambda_powertools.utilities.parser.envelopes.bedrock_agent.BedrockAgentEnvelope)
- [CloudWatchLogsEnvelope](cloudwatch.html#aws_lambda_powertools.utilities.parser.envelopes.cloudwatch.CloudWatchLogsEnvelope)
- [DynamoDBStreamEnvelope](dynamodb.html#aws_lambda_powertools.utilities.parser.envelopes.dynamodb.DynamoDBStreamEnvelope)
- [EventBridgeEnvelope](event_bridge.html#aws_lambda_powertools.utilities.parser.envelopes.event_bridge.EventBridgeEnvelope)
- [KafkaEnvelope](kafka.html#aws_lambda_powertools.utilities.parser.envelopes.kafka.KafkaEnvelope)
- [KinesisDataStreamEnvelope](kinesis.html#aws_lambda_powertools.utilities.parser.envelopes.kinesis.KinesisDataStreamEnvelope)
- [KinesisFirehoseEnvelope](kinesis_firehose.html#aws_lambda_powertools.utilities.parser.envelopes.kinesis_firehose.KinesisFirehoseEnvelope)
- [LambdaFunctionUrlEnvelope](lambda_function_url.html#aws_lambda_powertools.utilities.parser.envelopes.lambda_function_url.LambdaFunctionUrlEnvelope)
- [SnsEnvelope](sns.html#aws_lambda_powertools.utilities.parser.envelopes.sns.SnsEnvelope)
- [SnsSqsEnvelope](sns.html#aws_lambda_powertools.utilities.parser.envelopes.sns.SnsSqsEnvelope)
- [SqsEnvelope](sqs.html#aws_lambda_powertools.utilities.parser.envelopes.sqs.SqsEnvelope)
- [VpcLatticeEnvelope](vpc_lattice.html#aws_lambda_powertools.utilities.parser.envelopes.vpc_lattice.VpcLatticeEnvelope)
- [VpcLatticeV2Envelope](vpc_latticev2.html#aws_lambda_powertools.utilities.parser.envelopes.vpc_latticev2.VpcLatticeV2Envelope)
 ### Methods- `def parse(self, data: dict[str, Any] | Any | None, model: type[T])`
- 
## Expand source code`@abstractmethod def parse(self, data: dict[str, Any] | Any | None, model: type[T]): """Implementation to parse data against envelope model, then against the data model NOTE: Call `_parse` method to fully parse data with model provided. Example ------- **EventBridge envelope implementation example** def parse(...): # 1. parses data against envelope model parsed_envelope = EventBridgeModel(**data) # 2. parses portion of data within the envelope against model return self._parse(data=parsed_envelope.detail, model=data_model) """ return NotImplemented # pragma: no cover`Implementation to parse data against envelope model, then against the data model NOTE: Call `_parse`method to fully parse data with model provided.## Example**EventBridge envelope implementation example**def parse(…): # 1. parses data against envelope model parsed_envelope = EventBridgeModel(**data) `# 2. parses portion of data within the envelope against model return self._parse(data=parsed_envelope.detail, model=data_model)`
 
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
 
 
- `class CloudWatchLogsEnvelope`
- 
## Expand source code`class CloudWatchLogsEnvelope(BaseEnvelope): """CloudWatch Envelope to extract a list of log records. The record's body parameter is a string (after being base64 decoded and gzipped), though it can also be a JSON encoded string. Regardless of its type it'll be parsed into a BaseModel object. Note: The record will be parsed the same way so if model is str """ def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> list[Model | None]: """Parses records found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- list List of records parsed with model provided """ logger.debug(f"Parsing incoming data with SNS model {CloudWatchLogsModel}") parsed_envelope = CloudWatchLogsModel.model_validate(data) logger.debug(f"Parsing CloudWatch records in `body` with {model}") return [ self._parse(data=record.message, model=model) for record in parsed_envelope.awslogs.decoded_data.logEvents ]`CloudWatch Envelope to extract a list of log records. The record's body parameter is a string (after being base64 decoded and gzipped), though it can also be a JSON encoded string. Regardless of its type it'll be parsed into a BaseModel object. Note: The record will be parsed the same way so if model is str ### Ancestors- [BaseEnvelope](base.html#aws_lambda_powertools.utilities.parser.envelopes.base.BaseEnvelope)
- abc.ABC
 ### Methods- `def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) ‑> list[Model | None]`
- 
## Expand source code`def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> list[Model | None]: """Parses records found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- list List of records parsed with model provided """ logger.debug(f"Parsing incoming data with SNS model {CloudWatchLogsModel}") parsed_envelope = CloudWatchLogsModel.model_validate(data) logger.debug(f"Parsing CloudWatch records in `body` with {model}") return [ self._parse(data=record.message, model=model) for record in parsed_envelope.awslogs.decoded_data.logEvents ]`Parses records found with model provided ## Parameters- `data`- `dict`
- Lambda event to be parsed
- `model`- `type[Model]`
- Data model provided to parse after extracting data using envelope
 ## Returns- `list`
- List of records parsed with model provided
 
 
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
 
 
- `class KafkaEnvelope`
- 
## Expand source code`class KafkaEnvelope(BaseEnvelope): """Kafka event envelope to extract data within body key The record's body parameter is a string, though it can also be a JSON encoded string. Regardless of its type it'll be parsed into a BaseModel object. Note: Records will be parsed the same way so if model is str, all items in the list will be parsed as str and npt as JSON (and vice versa) """ def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> list[Model | None]: """Parses data found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- list List of records parsed with model provided """ event_source = cast(dict, data).get("eventSource") model_parse_event: type[KafkaMskEventModel | KafkaSelfManagedEventModel] = ( KafkaMskEventModel if event_source == "aws:kafka" else KafkaSelfManagedEventModel ) logger.debug(f"Parsing incoming data with Kafka event model {model_parse_event}") parsed_envelope = model_parse_event.model_validate(data) logger.debug(f"Parsing Kafka event records in `value` with {model}") ret_list = [] for records in parsed_envelope.records.values(): ret_list += [self._parse(data=record.value, model=model) for record in records] return ret_list`Kafka event envelope to extract data within body key The record's body parameter is a string, though it can also be a JSON encoded string. Regardless of its type it'll be parsed into a BaseModel object. Note: Records will be parsed the same way so if model is str, all items in the list will be parsed as str and npt as JSON (and vice versa) ### Ancestors- [BaseEnvelope](base.html#aws_lambda_powertools.utilities.parser.envelopes.base.BaseEnvelope)
- abc.ABC
 ### Methods- `def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) ‑> list[Model | None]`
- 
## Expand source code`def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> list[Model | None]: """Parses data found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- list List of records parsed with model provided """ event_source = cast(dict, data).get("eventSource") model_parse_event: type[KafkaMskEventModel | KafkaSelfManagedEventModel] = ( KafkaMskEventModel if event_source == "aws:kafka" else KafkaSelfManagedEventModel ) logger.debug(f"Parsing incoming data with Kafka event model {model_parse_event}") parsed_envelope = model_parse_event.model_validate(data) logger.debug(f"Parsing Kafka event records in `value` with {model}") ret_list = [] for records in parsed_envelope.records.values(): ret_list += [self._parse(data=record.value, model=model) for record in records] return ret_list`Parses data found with model provided ## Parameters- `data`- `dict`
- Lambda event to be parsed
- `model`- `type[Model]`
- Data model provided to parse after extracting data using envelope
 ## Returns- `list`
- List of records parsed with model provided
 
 
- `class KinesisDataStreamEnvelope`
- 
## Expand source code`class KinesisDataStreamEnvelope(BaseEnvelope): """Kinesis Data Stream Envelope to extract array of Records The record's data parameter is a base64 encoded string which is parsed into a bytes array, though it can also be a JSON encoded string. Regardless of its type it'll be parsed into a BaseModel object. Note: Records will be parsed the same way so if model is str, all items in the list will be parsed as str and not as JSON (and vice versa) """ def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> list[Model | None]: """Parses records found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- list List of records parsed with model provided """ logger.debug(f"Parsing incoming data with Kinesis model {KinesisDataStreamModel}") parsed_envelope: KinesisDataStreamModel = KinesisDataStreamModel.model_validate(data) logger.debug(f"Parsing Kinesis records in `body` with {model}") models = [] for record in parsed_envelope.Records: # We allow either AWS expected contract (bytes) or a custom Model, see #943 data = cast(bytes, record.kinesis.data) models.append(self._parse(data=data.decode("utf-8"), model=model)) return models`Kinesis Data Stream Envelope to extract array of Records The record's data parameter is a base64 encoded string which is parsed into a bytes array, though it can also be a JSON encoded string. Regardless of its type it'll be parsed into a BaseModel object. Note: Records will be parsed the same way so if model is str, all items in the list will be parsed as str and not as JSON (and vice versa) ### Ancestors- [BaseEnvelope](base.html#aws_lambda_powertools.utilities.parser.envelopes.base.BaseEnvelope)
- abc.ABC
 ### Methods- `def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) ‑> list[Model | None]`
- 
## Expand source code`def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> list[Model | None]: """Parses records found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- list List of records parsed with model provided """ logger.debug(f"Parsing incoming data with Kinesis model {KinesisDataStreamModel}") parsed_envelope: KinesisDataStreamModel = KinesisDataStreamModel.model_validate(data) logger.debug(f"Parsing Kinesis records in `body` with {model}") models = [] for record in parsed_envelope.Records: # We allow either AWS expected contract (bytes) or a custom Model, see #943 data = cast(bytes, record.kinesis.data) models.append(self._parse(data=data.decode("utf-8"), model=model)) return models`Parses records found with model provided ## Parameters- `data`- `dict`
- Lambda event to be parsed
- `model`- `type[Model]`
- Data model provided to parse after extracting data using envelope
 ## Returns- `list`
- List of records parsed with model provided
 
 
- `class KinesisFirehoseEnvelope`
- 
## Expand source code`class KinesisFirehoseEnvelope(BaseEnvelope): """Kinesis Firehose Envelope to extract array of Records The record's data parameter is a base64 encoded string which is parsed into a bytes array, though it can also be a JSON encoded string. Regardless of its type it'll be parsed into a BaseModel object. Note: Records will be parsed the same way so if model is str, all items in the list will be parsed as str and not as JSON (and vice versa) https://docs.aws.amazon.com/lambda/latest/dg/services-kinesisfirehose.html """ def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> list[Model | None]: """Parses records found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- list List of records parsed with model provided """ logger.debug(f"Parsing incoming data with Kinesis Firehose model {KinesisFirehoseModel}") parsed_envelope: KinesisFirehoseModel = KinesisFirehoseModel.model_validate(data) logger.debug(f"Parsing Kinesis Firehose records in `body` with {model}") models = [] for record in parsed_envelope.records: # We allow either AWS expected contract (bytes) or a custom Model, see #943 data = cast(bytes, record.data) models.append(self._parse(data=data.decode("utf-8"), model=model)) return models`Kinesis Firehose Envelope to extract array of Records The record's data parameter is a base64 encoded string which is parsed into a bytes array, though it can also be a JSON encoded string. Regardless of its type it'll be parsed into a BaseModel object. Note: Records will be parsed the same way so if model is str, all items in the list will be parsed as str and not as JSON (and vice versa) [https://docs.aws.amazon.com/lambda/latest/dg/services-kinesisfirehose.html](https://docs.aws.amazon.com/lambda/latest/dg/services-kinesisfirehose.html)### Ancestors- [BaseEnvelope](base.html#aws_lambda_powertools.utilities.parser.envelopes.base.BaseEnvelope)
- abc.ABC
 ### Methods- `def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) ‑> list[Model | None]`
- 
## Expand source code`def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> list[Model | None]: """Parses records found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- list List of records parsed with model provided """ logger.debug(f"Parsing incoming data with Kinesis Firehose model {KinesisFirehoseModel}") parsed_envelope: KinesisFirehoseModel = KinesisFirehoseModel.model_validate(data) logger.debug(f"Parsing Kinesis Firehose records in `body` with {model}") models = [] for record in parsed_envelope.records: # We allow either AWS expected contract (bytes) or a custom Model, see #943 data = cast(bytes, record.data) models.append(self._parse(data=data.decode("utf-8"), model=model)) return models`Parses records found with model provided ## Parameters- `data`- `dict`
- Lambda event to be parsed
- `model`- `type[Model]`
- Data model provided to parse after extracting data using envelope
 ## Returns- `list`
- List of records parsed with model provided
 
 
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
 
 
- `class SnsEnvelope`
- 
## Expand source code`class SnsEnvelope(BaseEnvelope): """SNS Envelope to extract array of Records The record's body parameter is a string, though it can also be a JSON encoded string. Regardless of its type it'll be parsed into a BaseModel object. Note: Records will be parsed the same way so if model is str, all items in the list will be parsed as str and npt as JSON (and vice versa) """ def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> list[Model | None]: """Parses records found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- list List of records parsed with model provided """ logger.debug(f"Parsing incoming data with SNS model {SnsModel}") parsed_envelope = SnsModel.model_validate(data) logger.debug(f"Parsing SNS records in `body` with {model}") return [self._parse(data=record.Sns.Message, model=model) for record in parsed_envelope.Records]`SNS Envelope to extract array of Records The record's body parameter is a string, though it can also be a JSON encoded string. Regardless of its type it'll be parsed into a BaseModel object. Note: Records will be parsed the same way so if model is str, all items in the list will be parsed as str and npt as JSON (and vice versa) ### Ancestors- [BaseEnvelope](base.html#aws_lambda_powertools.utilities.parser.envelopes.base.BaseEnvelope)
- abc.ABC
 ### Methods- `def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) ‑> list[Model | None]`
- 
## Expand source code`def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> list[Model | None]: """Parses records found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- list List of records parsed with model provided """ logger.debug(f"Parsing incoming data with SNS model {SnsModel}") parsed_envelope = SnsModel.model_validate(data) logger.debug(f"Parsing SNS records in `body` with {model}") return [self._parse(data=record.Sns.Message, model=model) for record in parsed_envelope.Records]`Parses records found with model provided ## Parameters- `data`- `dict`
- Lambda event to be parsed
- `model`- `type[Model]`
- Data model provided to parse after extracting data using envelope
 ## Returns- `list`
- List of records parsed with model provided
 
 
- `class SnsSqsEnvelope`
- 
## Expand source code`class SnsSqsEnvelope(BaseEnvelope): """SNS plus SQS Envelope to extract array of Records Published messages from SNS to SQS has a slightly different payload. Since SNS payload is marshalled into `Record` key in SQS, we have to: 1. Parse SQS schema with incoming data 2. Unmarshall SNS payload and parse against SNS Notification model not SNS/SNS Record 3. Finally, parse provided model against payload extracted """ def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> list[Model | None]: """Parses records found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- list List of records parsed with model provided """ logger.debug(f"Parsing incoming data with SQS model {SqsModel}") parsed_envelope = SqsModel.model_validate(data) output = [] for record in parsed_envelope.Records: # We allow either AWS expected contract (str) or a custom Model, see #943 body = cast(str, record.body) sns_notification = SnsNotificationModel.model_validate_json(body) output.append(self._parse(data=sns_notification.Message, model=model)) return output`SNS plus SQS Envelope to extract array of Records Published messages from SNS to SQS has a slightly different payload. Since SNS payload is marshalled into `Record`key in SQS, we have to:- Parse SQS schema with incoming data
- Unmarshall SNS payload and parse against SNS Notification model not SNS/SNS Record
- Finally, parse provided model against payload extracted
 ### Ancestors- [BaseEnvelope](base.html#aws_lambda_powertools.utilities.parser.envelopes.base.BaseEnvelope)
- abc.ABC
 ### Methods- `def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) ‑> list[Model | None]`
- 
## Expand source code`def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> list[Model | None]: """Parses records found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- list List of records parsed with model provided """ logger.debug(f"Parsing incoming data with SQS model {SqsModel}") parsed_envelope = SqsModel.model_validate(data) output = [] for record in parsed_envelope.Records: # We allow either AWS expected contract (str) or a custom Model, see #943 body = cast(str, record.body) sns_notification = SnsNotificationModel.model_validate_json(body) output.append(self._parse(data=sns_notification.Message, model=model)) return output`Parses records found with model provided ## Parameters- `data`- `dict`
- Lambda event to be parsed
- `model`- `type[Model]`
- Data model provided to parse after extracting data using envelope
 ## Returns- `list`
- List of records parsed with model provided
 
 
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
 
 
- `class VpcLatticeEnvelope`
- 
## Expand source code`class VpcLatticeEnvelope(BaseEnvelope): """Amazon VPC Lattice envelope to extract data within body key""" def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> Model | None: """Parses data found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- Model | None Parsed detail payload with model provided """ logger.debug(f"Parsing incoming data with VPC Lattice model {VpcLatticeModel}") parsed_envelope: VpcLatticeModel = VpcLatticeModel.model_validate(data) logger.debug(f"Parsing event payload in `detail` with {model}") return self._parse(data=parsed_envelope.body, model=model)`Amazon VPC Lattice envelope to extract data within body key ### Ancestors- [BaseEnvelope](base.html#aws_lambda_powertools.utilities.parser.envelopes.base.BaseEnvelope)
- abc.ABC
 ### Methods- `def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) ‑> Model | None`
- 
## Expand source code`def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> Model | None: """Parses data found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- Model | None Parsed detail payload with model provided """ logger.debug(f"Parsing incoming data with VPC Lattice model {VpcLatticeModel}") parsed_envelope: VpcLatticeModel = VpcLatticeModel.model_validate(data) logger.debug(f"Parsing event payload in `detail` with {model}") return self._parse(data=parsed_envelope.body, model=model)`Parses data found with model provided ## Parameters- `data`- `dict`
- Lambda event to be parsed
- `model`- `type[Model]`
- Data model provided to parse after extracting data using envelope
 ## Returns- `Model | None`
- Parsed detail payload with model provided
 
 
- `class VpcLatticeV2Envelope`
- 
## Expand source code`class VpcLatticeV2Envelope(BaseEnvelope): """Amazon VPC Lattice envelope to extract data within body key""" def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> Model | None: """Parses data found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- Model | None Parsed detail payload with model provided """ logger.debug(f"Parsing incoming data with VPC Lattice V2 model {VpcLatticeV2Model}") parsed_envelope: VpcLatticeV2Model = VpcLatticeV2Model.model_validate(data) logger.debug(f"Parsing event payload in `detail` with {model}") return self._parse(data=parsed_envelope.body, model=model)`Amazon VPC Lattice envelope to extract data within body key ### Ancestors- [BaseEnvelope](base.html#aws_lambda_powertools.utilities.parser.envelopes.base.BaseEnvelope)
- abc.ABC
 ### Methods- `def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) ‑> Model | None`
- 
## Expand source code`def parse(self, data: dict[str, Any] | Any | None, model: type[Model]) -> Model | None: """Parses data found with model provided Parameters ---------- data : dict Lambda event to be parsed model : type[Model] Data model provided to parse after extracting data using envelope Returns ------- Model | None Parsed detail payload with model provided """ logger.debug(f"Parsing incoming data with VPC Lattice V2 model {VpcLatticeV2Model}") parsed_envelope: VpcLatticeV2Model = VpcLatticeV2Model.model_validate(data) logger.debug(f"Parsing event payload in `detail` with {model}") return self._parse(data=parsed_envelope.body, model=model)`Parses data found with model provided ## Parameters- `data`- `dict`
- Lambda event to be parsed
- `model`- `type[Model]`
- Data model provided to parse after extracting data using envelope
 ## Returns- `Model | None`
- Parsed detail payload with model provided