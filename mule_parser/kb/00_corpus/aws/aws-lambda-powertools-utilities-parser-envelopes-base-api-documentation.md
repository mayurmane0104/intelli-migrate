# aws_lambda_powertools.utilities.parser.envelopes.base API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/envelopes/base.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/envelopes/base.html)

---

# Module `aws_lambda_powertools.utilities.parser.envelopes.base`

## Classes

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