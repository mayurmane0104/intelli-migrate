# Upgrade guide - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/upgrade](https://docs.aws.amazon.com/powertools/python/latest/upgrade)

---

# Upgrade guide

## End of support v2[¶](https://docs.aws.amazon.com/powertools/python/latest/upgrade/#end-of-support-v2)

On March 25st, 2025, Powertools for AWS Lambda (Python) v2 reached end of support and will no longer receive updates or releases. If you are still using v2, we strongly recommend you to read our upgrade guide and update to the latest version.

Given our commitment to all of our customers using Powertools for AWS Lambda (Python), we will keep [Pypi](https://pypi.org/project/aws-lambda-powertools/) v2 releases and documentation 2.x versions to prevent any disruption.

## Migrate to v3 from v2[¶](https://docs.aws.amazon.com/powertools/python/latest/upgrade/#migrate-to-v3-from-v2)

We strongly encourage you to migrate to v3. However, if you still need to upgrade from v1 to v2, you can find the [upgrade guide](https://docs.aws.amazon.com/powertools/python/2.43.1/).

We've made minimal breaking changes to make your transition to v3 as smooth as possible.

### Quick summary[¶](https://docs.aws.amazon.com/powertools/python/latest/upgrade/#quick-summary)

| Area | Change | Code change required | 
|---|---|---|
| Pydantic | We have removed support for [Pydantic v1](https://docs.aws.amazon.com/powertools/python/latest/upgrade/#drop-support-for-pydantic-v1) | No | 
| Parser | We have replaced [DynamoDBStreamModel](https://docs.aws.amazon.com/powertools/python/latest/upgrade/#dynamodbstreammodel-in-parser)`AttributeValue`with native Python types | Yes | 
| Parser | We no longer export [Pydantic objects](https://docs.aws.amazon.com/powertools/python/latest/upgrade/#importing-pydantic-objects)from`parser.pydantic`. | Yes | 
| Lambda layer | [Lambda layers](https://docs.aws.amazon.com/powertools/python/latest/upgrade/#new-aws-lambda-layer-arns)are now compiled according to the specific Python version and architecture | No | 
| Event Handler | We [have deprecated](https://docs.aws.amazon.com/powertools/python/latest/upgrade/#event-handler-headers-are-case-insensitive)the`get_header_value`function. | Yes | 
| Batch Processor | `@batch_processor`and`@async_batch_processor`decorators[are now deprecated](https://docs.aws.amazon.com/powertools/python/latest/upgrade/#deprecated-batch-processing-decorators) | Yes | 
| Event Source Data Classes | We have updated [default values](https://docs.aws.amazon.com/powertools/python/latest/upgrade/#event-source-default-values)for optional fields. | Yes | 
| Parameters | The [default cache TTL](https://docs.aws.amazon.com/powertools/python/latest/upgrade/#parameters-default-cache-ttl-updated-to-5-minutes)is now set to5 minutes | No | 
| Parameters | The `config`parameter[is deprecated](https://docs.aws.amazon.com/powertools/python/latest/upgrade/#parameters-using-the-new-boto_config-parameter)in favor of`boto_config` | Yes | 
| JMESPath Functions | The `extract_data_from_envelope`function is[deprecated in favor](https://docs.aws.amazon.com/powertools/python/latest/upgrade/#utilizing-the-new-query-function-in-jmespath-functions)of`query` | Yes | 
| Types file | We have removed the [type imports](https://docs.aws.amazon.com/powertools/python/latest/upgrade/#importing-types-from-typing-and-typing_annotations)from the`shared/types.py`file | Yes | 

### First Steps[¶](https://docs.aws.amazon.com/powertools/python/latest/upgrade/#first-steps)

Before you start, we suggest making a copy of your current working project or create a new branch with git.

- **Upgrade**Python to at least v3.10.
- **Ensure**you have the latest version via- [Lambda Layer or PyPi](https://docs.aws.amazon.com/powertools/python/latest/#install).
- **Review**the following sections to confirm if you need to make changes to your code.

## Drop support for Pydantic v1[¶](https://docs.aws.amazon.com/powertools/python/latest/upgrade/#drop-support-for-pydantic-v1)

No code changes required

As of June 30, 2024, Pydantic v1 has reached its end-of-life, and we have discontinued support for this version. We now exclusively support Pydantic v2.

Use [Pydantic v2 Migration Guide](https://docs.pydantic.dev/latest/migration/) to migrate your custom Pydantic models to v2.

## DynamoDBStreamModel in parser[¶](https://docs.aws.amazon.com/powertools/python/latest/upgrade/#dynamodbstreammodel-in-parser)

This also applies if you're using [ DynamoDB BatchProcessor](https://docs.aws.amazon.com/powertools/python/latest/utilities/batch/#processing-messages-from-dynamodb).

`DynamoDBStreamModel` now returns native Python types when you access DynamoDB records through `Keys`, `NewImage`, and `OldImage` attributes.

Previously, you'd receive a raw JSON and need to deserialize each item to the type you'd want for convenience, or to the type DynamoDB stored via `get` method.

With this change, you can access data deserialized as stored in DynamoDB, and no longer need to recursively deserialize nested objects (Maps) if you had them.

## Note

For a lossless conversion of DynamoDB `Number` type, we follow AWS Python SDK (boto3) approach and convert to `Decimal`.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 | 
 | 

## Importing Pydantic objects[¶](https://docs.aws.amazon.com/powertools/python/latest/upgrade/#importing-pydantic-objects)

We have stopped exporting Pydantic objects directly from `aws_lambda_powertools.utilities.parser.pydantic`. This change prevents customers from accidentally importing all of Pydantic, which could significantly slow down function startup times.

| 1 2 3 4 5 | 
 | 

## New AWS Lambda Layer ARNs[¶](https://docs.aws.amazon.com/powertools/python/latest/upgrade/#new-aws-lambda-layer-arns)

No code changes required

To give you better a better experience, we're now building Powertools for AWS Lambda (Python)'s Lambda layers for specific Python versions (`3.10-3.14`) and architectures (`x86_64` & `arm64`).

This also allows us to include architecture-specific versions of both Pydantic v2 and AWS Encryption SDK and give you a more streamlined setup.

To take advantage of the new layers, you need to update your functions or deployment setup to include one of the new Lambda layer ARN from the table below:

| Architecture | Python version | Layer ARN | 
|---|---|---|
| x86_64 | 3.10 | arn:aws:lambda:{region}:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-x86_64:{version} | 
| x86_64 | 3.11 | arn:aws:lambda:{region}:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-x86_64:{version} | 
| x86_64 | 3.12 | arn:aws:lambda:{region}:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:{version} | 
| x86_64 | 3.13 | arn:aws:lambda:{region}:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:{version} | 
| x86_64 | 3.14 | arn:aws:lambda:{region}:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-x86_64:{version} | 
| arm64 | 3.10 | arn:aws:lambda:{region}:017000801446:layer:AWSLambdaPowertoolsPythonV3-python310-arm64:{version} | 
| arm64 | 3.11 | arn:aws:lambda:{region}:017000801446:layer:AWSLambdaPowertoolsPythonV3-python311-arm64:{version} | 
| arm64 | 3.12 | arn:aws:lambda:{region}:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-arm64:{version} | 
| arm64 | 3.13 | arn:aws:lambda:{region}:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-arm64:{version} | 
| arm64 | 3.14 | arn:aws:lambda:{region}:017000801446:layer:AWSLambdaPowertoolsPythonV3-python314-arm64:{version} | 

## Event Handler: headers are case-insensitive[¶](https://docs.aws.amazon.com/powertools/python/latest/upgrade/#event-handler-headers-are-case-insensitive)

According to the [HTTP RFC](https://datatracker.ietf.org/doc/html/rfc9110#section-5.1), HTTP headers are case-insensitive. As a result, we have deprecated the `get_header_value` function to align with this standard. Instead, we recommend using `app.current_event.headers.get` to access header values directly

Consequently, the `case_sensitive` parameter in this function no longer has any effect, as we now ensure consistent casing by normalizing headers for you. This function will be removed in a future release, and we encourage users to adopt the new method to access header values.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 | 
 | 

## Deprecated Batch Processing decorators[¶](https://docs.aws.amazon.com/powertools/python/latest/upgrade/#deprecated-batch-processing-decorators)

In v2, we designated `@batch_processor` and `@async_batch_processor` as legacy modes for using the Batch Processing utility.

In v3, these have been marked as deprecated. Continuing to use them will result in warnings in your IDE and during Lambda execution.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 | 
 | 

## Event source default values[¶](https://docs.aws.amazon.com/powertools/python/latest/upgrade/#event-source-default-values)

We've modified the **Event Source Data classes** so that optional dictionaries and lists now return empty strings, dictionaries or lists instead of `None`. This improvement simplifies your code by eliminating the need for conditional checks when accessing these fields, while maintaining backward compatibility with previous implementations.

We've applied this change broadly across various event source data classes, ensuring a more consistent and streamlined coding experience for you.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 | 
 | 

## Parameters: default cache TTL updated to 5 minutes[¶](https://docs.aws.amazon.com/powertools/python/latest/upgrade/#parameters-default-cache-ttl-updated-to-5-minutes)

No code changes required

We have updated the cache TTL from 5 seconds to 5 minutes to reduce the number of API calls to AWS, leading to improved performance and lower costs.

No code changes are necessary for this update; however, if you prefer the previous behavior, you can set the `max_age` parameter back to 5 seconds.

## Parameters: using the new boto_config parameter[¶](https://docs.aws.amazon.com/powertools/python/latest/upgrade/#parameters-using-the-new-boto_config-parameter)

In v2, you could use the `config` parameter to modify the **botocore Config** session settings.

In v3, we renamed this parameter to `boto_config` to standardize the name with other features, such as Idempotency, and introduced deprecation warnings for users still using `config`.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 | 
 | 

## Utilizing the new query function in JMESPath Functions[¶](https://docs.aws.amazon.com/powertools/python/latest/upgrade/#utilizing-the-new-query-function-in-jmespath-functions)

In v2, you could use the `extract_data_from_envelope` function to search and extract data from dictionaries with JMESPath. This name was too generic and customers told us it was confusing.

In v3, we renamed this function to `query` to align with similar frameworks in the ecosystem, and introduced deprecation warnings for users still using `extract_data_from_envelope`.

| 1 2 3 4 5 6 7 8 9 10 11 12 | 
 | 

## Importing types from typing and typing_annotations[¶](https://docs.aws.amazon.com/powertools/python/latest/upgrade/#importing-types-from-typing-and-typing_annotations)

We refactored our codebase to align with Python guidelines and eliminated the use of `aws_lambda_powertools.shared.types` imports.

Instead, we now utilize types from the standard `typing` library, which are compatible with Python versions 3.10 and above, or from `typing_extensions` (included as a required dependency) for additional type support.

| 1 2 3 4 5 6 7 8 9 10 11 | 
 |