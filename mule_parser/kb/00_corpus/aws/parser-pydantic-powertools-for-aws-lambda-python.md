# Parser (Pydantic) - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/utilities/parser](https://docs.aws.amazon.com/powertools/python/latest/utilities/parser)

---

# Parser (Pydantic)

The Parser utility simplifies data parsing and validation using [Pydantic](https://pydantic-docs.helpmanual.io/). It allows you to define data models in pure Python classes, parse and validate incoming events, and extract only the data you need.

## Key features[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/parser/#key-features)

- Define data models using Python classes
- Parse and validate Lambda event payloads
- Built-in support for common AWS event sources
- Runtime type checking with user-friendly error messages
- Compatible with Pydantic v2.x

## Getting started[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/parser/#getting-started)

### Install[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/parser/#install)

Powertools only supports Pydantic v2, so make sure to install the required dependencies for Pydantic v2 before using the Parser.

| `1` | 
 | 

This is not necessary if you're installing Powertools for AWS Lambda (Python) via [Lambda Layer/SAR](https://docs.aws.amazon.com/powertools/python/latest/#lambda-layer)

You can also add as a dependency in your preferred tool: `e.g., requirements.txt, pyproject.toml`, etc.

### Data Model with Parser[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/parser/#data-model-with-parser)

You can define models by inheriting from `BaseModel` or any other supported type through `TypeAdapter` to parse incoming events. Pydantic then validates the data, ensuring that all fields conform to the specified types and maintaining data integrity.

## Info

The new TypeAdapter feature provide a flexible way to perform validation and serialization based on a Python type. Read more in the [Pydantic documentation](https://docs.pydantic.dev/latest/api/type_adapter/).

#### Event parser[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/parser/#event-parser)

The `@event_parser` decorator automatically parses the incoming event into the specified Pydantic model `MyEvent`. If the input doesn't match the model's structure or type requirements, it raises a `ValidationError` directly from Pydantic.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 | 
 | 

| 1 2 3 4 | 
 | 

#### Parse function[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/parser/#parse-function)

You can use the `parse()` function when you need to have flexibility with different event formats, custom pre-parsing logic, and better exception handling.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 | 
 | 

| 1 2 3 4 | 
 | 

#### Keys differences between parse and event_parser[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/parser/#keys-differences-between-parse-and-event_parser)

The `parse()` function offers more flexibility and control:

- It allows parsing different parts of an event using multiple models.
- You can conditionally handle events before parsing them.
- It's useful for integrating with complex workflows where a decorator might not be sufficient.
- It provides more control over the validation process and handling exceptions.

The `@event_parser` decorator is ideal for:

- Fail-fast scenarios where you want to immediately stop execution if the event payload is invalid.
- Simplifying your code by automatically parsing and validating the event at the function entry point.

### Built-in models[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/parser/#built-in-models)

You can use pre-built models to work events from AWS services, so you don’t need to create them yourself. We’ve already done that for you!

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 | 
 | 

The example above uses `SqsModel`. Other built-in models can be found below.

| Model name | Description | 
|---|---|
| AlbModel | Lambda Event Source payload for Amazon Application Load Balancer | 
| APIGatewayProxyEventModel | Lambda Event Source payload for Amazon API Gateway | 
| ApiGatewayAuthorizerToken | Lambda Event Source payload for Amazon API Gateway Lambda Authorizer with Token | 
| ApiGatewayAuthorizerRequest | Lambda Event Source payload for Amazon API Gateway Lambda Authorizer with Request | 
| APIGatewayProxyEventV2Model | Lambda Event Source payload for Amazon API Gateway v2 payload | 
| ApiGatewayAuthorizerRequestV2 | Lambda Event Source payload for Amazon API Gateway v2 Lambda Authorizer | 
| APIGatewayWebSocketMessageEventModel | Lambda Event Source payload for Amazon API Gateway WebSocket API message body | 
| APIGatewayWebSocketConnectEventModel | Lambda Event Source payload for Amazon API Gateway WebSocket API $connect message | 
| APIGatewayWebSocketDisconnectEventModel | Lambda Event Source payload for Amazon API Gateway WebSocket API $disconnect message | 
| AppSyncResolverEventModel | Lambda Event Source payload for AWS AppSync Resolver | 
| AppSyncEventsModel | Lambda Event Source payload for AWS AppSync Events | 
| BedrockAgentEventModel | Lambda Event Source payload for Bedrock Agents - OpenAPI-based | 
| BedrockAgentFunctionEventModel | Lambda Event Source payload for Bedrock Agents - Function-based | 
| CloudFormationCustomResourceCreateModel | Lambda Event Source payload for AWS CloudFormation `CREATE`operation | 
| CloudFormationCustomResourceUpdateModel | Lambda Event Source payload for AWS CloudFormation `UPDATE`operation | 
| CloudFormationCustomResourceDeleteModel | Lambda Event Source payload for AWS CloudFormation `DELETE`operation | 
| CloudwatchLogsModel | Lambda Event Source payload for Amazon CloudWatch Logs | 
| CognitoPreSignupTriggerModel | Lambda User Pool Pre-Sign-Up trigger event | 
| CognitoPostConfirmationTriggerModel | Lambda User Pool Post Confirmation trigger event | 
| CognitoPreAuthenticationTriggerModel | Lambda User Pool Pre Authentication trigger event | 
| CognitoPostAuthenticationTriggerModel | Lambda User Pool Post Authentication trigger event | 
| CognitoPreTokenGenerationTriggerModelV1 | Lambda User Pool Pre Token Generation V1 trigger event | 
| CognitoPreTokenGenerationTriggerModelV2AndV3 | Lambda User Pool Pre Token Generation V2 and V3 trigger event | 
| CognitoMigrateUserTriggerModel | Lambda User Pool Migrate User trigger event | 
| CognitoCustomMessageTriggerModel | Lambda User Pool Custom Message trigger event | 
| CognitoCustomEmailSenderTriggerModel | Lambda User Pool Custom Email Sender trigger event | 
| CognitoCustomSMSSenderTriggerModel | Lambda User Pool Custom SMS Sender trigger event | 
| CognitoDefineAuthChallengeTriggerModel | Lambda User Pool Define Auth Challenge trigger event | 
| CognitoCreateAuthChallengeTriggerModel | Lambda User Pool Create Auth Challenge trigger event | 
| CognitoVerifyAuthChallengeTriggerModel | Lambda User Pool Verify Auth Challenge trigger event | 
| DynamoDBStreamModel | Lambda Event Source payload for Amazon DynamoDB Streams | 
| DynamoDBStreamLambdaOnFailureDestinationModel | Lambda on-failure destination payload for Amazon DynamoDB Streams | 
| EventBridgeModel | Lambda Event Source payload for Amazon EventBridge | 
| IoTCoreThingEvent | Lambda Event Source payload for IoT Core Thing created, updated, or deleted. | 
| IoTCoreThingTypeEvent | Lambda Event Source payload for IoT Core Thing Type events. | 
| IoTCoreThingTypeAssociationEvent | Lambda Event Source payload for IoT Core Thing Type associated or disassociated with a Thing. | 
| IoTCoreThingGroupEvent | Lambda Event Source payload for IoT Core Thing Group created, updated, or deleted. | 
| IoTCoreAddOrRemoveFromThingGroupEvent | Lambda Event Source payload for IoT Core Thing added to or removed from a Thing Group. | 
| IoTCoreAddOrDeleteFromThingGroupEvent | Lambda Event Source payload for IoT Core Thing Group added to or deleted from a Thing Group. | 
| KafkaMskEventModel | Lambda Event Source payload for AWS MSK payload | 
| KafkaSelfManagedEventModel | Lambda Event Source payload for self managed Kafka payload | 
| KinesisDataStreamModel | Lambda Event Source payload for Amazon Kinesis Data Streams | 
| KinesisFirehoseModel | Lambda Event Source payload for Amazon Kinesis Firehose | 
| KinesisFirehoseSqsModel | Lambda Event Source payload for SQS messages wrapped in Kinesis Firehose records | 
| LambdaFunctionUrlModel | Lambda Event Source payload for Lambda Function URL payload | 
| S3BatchOperationModel | Lambda Event Source payload for Amazon S3 Batch Operation | 
| S3EventNotificationEventBridgeModel | Lambda Event Source payload for Amazon S3 Event Notification to EventBridge. | 
| S3Model | Lambda Event Source payload for Amazon S3 | 
| S3ObjectLambdaEvent | Lambda Event Source payload for Amazon S3 Object Lambda | 
| S3SqsEventNotificationModel | Lambda Event Source payload for S3 event notifications wrapped in SQS event (S3->SQS) | 
| SesModel | Lambda Event Source payload for Amazon Simple Email Service | 
| SnsModel | Lambda Event Source payload for Amazon Simple Notification Service | 
| SqsModel | Lambda Event Source payload for Amazon SQS | 
| TransferFamilyAuthorizer | Lambda Event Source payload for AWS Transfer Family Lambda authorizer | 
| VpcLatticeModel | Lambda Event Source payload for Amazon VPC Lattice | 
| VpcLatticeV2Model | Lambda Event Source payload for Amazon VPC Lattice v2 payload | 

#### Extending built-in models[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/parser/#extending-built-in-models)

You can extend them to include your own models, and yet have all other known fields parsed along the way.

## Tip

For Mypy users, we only allow type override for fields where payload is injected e.g. `detail`, `body`, etc.

**Example: custom data model with Amazon EventBridge**
Use the model to validate and extract relevant information from the incoming event. This can be useful when you need to handle events with a specific structure or when you want to ensure that the event data conforms to certain rules.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 | 
 | 

## Advanced[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/parser/#advanced)

### Envelopes[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/parser/#envelopes)

You can use **Envelopes** to extract specific portions of complex, nested JSON structures. This is useful when your actual payload is wrapped around a known structure, for example Lambda Event Sources like **EventBridge**.

Envelopes can be used via `envelope` parameter available in both `parse` function and `event_parser` decorator.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 | 
 | 

#### Built-in envelopes[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/parser/#built-in-envelopes)

You can use pre-built envelopes provided by the Parser to extract and parse specific parts of complex event structures.

| Envelope name | Behaviour | Return | 
|---|---|---|
| DynamoDBStreamEnvelope | 1. Parses data using `DynamoDBStreamModel`.`2. Parses records in `NewImage` and `OldImage` keys using your model.`3. Returns a list with a dictionary containing`NewImage`and`OldImage`keys | `List[Dict[str, Optional[Model]]]` | 
| EventBridgeEnvelope | 1. Parses data using `EventBridgeModel`.`2. Parses `detail` key using your model`and returns it. | `Model` | 
| SqsEnvelope | 1. Parses data using `SqsModel`.`2. Parses records in `body` key using your model`and return them in a list. | `List[Model]` | 
| CloudWatchLogsEnvelope | 1. Parses data using `CloudwatchLogsModel`which will base64 decode and decompress it.`2. Parses records in `message` key using your model`and return them in a list. | `List[Model]` | 
| KinesisDataStreamEnvelope | 1. Parses data using `KinesisDataStreamModel`which will base64 decode it.`2. Parses records in the `Records` key using your model`and returns them in a list. | `List[Model]` | 
| KinesisFirehoseEnvelope | 1. Parses data using `KinesisFirehoseModel`which will base64 decode it.`2. Parses records in the `Records` key using your model`and returns them in a list. | `List[Model]` | 
| SnsEnvelope | 1. Parses data using `SnsModel`.`2. Parses records in `body` key using your model`and return them in a list. | `List[Model]` | 
| SnsSqsEnvelope | 1. Parses data using `SqsModel`.`2. Parses SNS records in `body` key using `SnsNotificationModel`.`3. Parses data in`Message`key using your model and return them in a list. | `List[Model]` | 
| ApiGatewayV2Envelope | 1. Parses data using `APIGatewayProxyEventV2Model`.`2. Parses `body` key using your model`and returns it. | `Model` | 
| ApiGatewayEnvelope | 1. Parses data using `APIGatewayProxyEventModel`.`2. Parses `body` key using your model`and returns it. | `Model` | 
| ApiGatewayWebSocketEnvelope | 1. Parses data using `APIGatewayWebSocketMessageEventModel`.`2. Parses `body` key using your model`and returns it. | `Model` | 
| LambdaFunctionUrlEnvelope | 1. Parses data using `LambdaFunctionUrlModel`.`2. Parses `body` key using your model`and returns it. | `Model` | 
| KafkaEnvelope | 1. Parses data using `KafkaRecordModel`.`2. Parses `value` key using your model`and returns it. | `Model` | 
| VpcLatticeEnvelope | 1. Parses data using `VpcLatticeModel`.`2. Parses `value` key using your model`and returns it. | `Model` | 
| BedrockAgentEnvelope | 1. Parses data using `BedrockAgentEventModel`.`2. Parses `inputText` key using your model`and returns it. | `Model` | 

#### Bringing your own envelope[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/parser/#bringing-your-own-envelope)

You can create your own Envelope model and logic by inheriting from `BaseEnvelope`, and implementing the `parse` method.

Here's a snippet of how the EventBridge envelope we demonstrated previously is implemented.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 | 
 | 

**What's going on here, you might ask**:

- **EventBridgeEnvelope**: extracts the detail field from EventBridge events.
- **OrderDetail Model**: defines and validates the structure of order data.
- **@event_parser**: decorator automates parsing and validation of incoming events using the specified model and envelope.

### Data model validation[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/parser/#data-model-validation)

## Warning

This is radically different from the **Validator utility** which validates events against JSON Schema.

You can use Pydantic's validator for deep inspection of object values and complex relationships.

There are two types of class method decorators you can use:

- `field_validator`
- `model_validator`

Keep the following in mind regardless of which decorator you end up using it:

- You must raise either `ValueError`,`TypeError`, or`AssertionError`when value is not compliant
- You must return the value(s) itself if compliant

#### Field Validator[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/parser/#field-validator)

Quick validation using decorator `field_validator` to verify whether the field `message` has the value of `hello world`.

| field_validator.py | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 | 
 | 

If you run using a test event `{"message": "hello universe"}` you should expect the following error with the message we provided in our exception:

| `1` | 
 | 

#### Model validator[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/parser/#model-validator)

`model_validator` can help when you have a complex validation mechanism. For example finding whether data has been omitted or comparing field values.

If you are still using the deprecated `root_validator` function, switch to `model_validator` for the latest Pydantic functionality.

| model_validator.py | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 | 
 | 

## Info

You can read more about validating list items, reusing validators, validating raw inputs, and a lot more in [Pydantic's documentation](https://pydantic-docs.helpmanual.io/usage/validators/).

#### String fields that contain JSON data[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/parser/#string-fields-that-contain-json-data)

Wrap these fields with [Pydantic's Json Type](https://pydantic-docs.helpmanual.io/usage/types/#json-type). This approach allows Pydantic to properly parse and validate the JSON content, ensuring type safety and data integrity.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 | 
 | 

| 1 2 3 | 
 | 

### Serialization[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/parser/#serialization)

Models in Pydantic offer more than direct attribute access. They can be transformed, serialized, and exported in various formats.

Pydantic's definition of *serialization* is broader than usual. It includes converting structured objects to simpler Python types, not just data to strings or bytes. This reflects the close relationship between these processes in Pydantic.

Read more at [Serialization for Pydantic documentation](https://docs.pydantic.dev/latest/concepts/serialization/#model_copy).

| serialization_parser.py | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 | 
 | 

## Info

There are number of advanced use cases well documented in Pydantic's doc such as creating [immutable models](https://pydantic-docs.helpmanual.io/usage/models/#faux-immutability), [declaring fields with dynamic values](https://pydantic-docs.helpmanual.io/usage/models/#field-with-dynamic-default-value).

## FAQ[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/parser/#faq)

**When should I use parser vs data_classes utility?**

Use data classes utility when you're after autocomplete, self-documented attributes and helpers to extract data from common event sources.

Parser is best suited for those looking for a trade-off between defining their models for deep validation, parsing and autocomplete for an additional dependency to be brought in.

**How do I import X from Pydantic?**

We recommend importing directly from Pydantic to access all features and stay up-to-date with the latest Pydantic updates. For example:

| `1` | 
 | 

While we export some common Pydantic classes and utilities through the parser for convenience (e.g., `from aws_lambda_powertools.utilities.parser import BaseModel`), importing directly from Pydantic ensures you have access to all features and the most recent updates.