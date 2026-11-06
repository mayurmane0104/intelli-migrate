# Kafka Consumer - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka)

---

# Kafka Consumer

The Kafka Consumer utility transparently handles message deserialization, provides an intuitive developer experience, and integrates seamlessly with the rest of the Powertools for AWS Lambda ecosystem.

## Key features[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#key-features)

- Automatic deserialization of Kafka messages (JSON, Avro, and Protocol Buffers)
- Simplified event record handling with intuitive interface
- Support for key and value deserialization
- Support for custom output serializers (e.g., dataclasses, Pydantic models)
- Support for ESM with and without Schema Registry integration
- Proper error handling for deserialization issues

## Terminology[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#terminology)

**Event Source Mapping (ESM)**  A Lambda feature that reads from streaming sources (like Kafka) and invokes your Lambda function. It manages polling, batching, and error handling automatically, eliminating the need for consumer management code.

**Record Key and Value** A Kafka messages contain two important parts: an optional key that determines the partition and a value containing the actual message data. Both are base64-encoded in Lambda events and can be independently deserialized.

**Deserialization** Is the process of converting binary data (base64-encoded in Lambda events) into usable Python objects according to a specific format like JSON, Avro, or Protocol Buffers. Powertools handles this conversion automatically.

**SchemaConfig class** Contains parameters that tell Powertools how to interpret message data, including the format type (JSON, Avro, Protocol Buffers) and optional schema definitions needed for binary formats.

**Output Serializer** A Pydantic model, Python dataclass, or any custom function that helps structure data for your business logic.

**Schema Registry** Is a centralized service that stores and validates schemas, ensuring producers and consumers maintain compatibility when message formats evolve over time.

## Moving from traditional Kafka consumers[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#moving-from-traditional-kafka-consumers)

Lambda processes Kafka messages as discrete events rather than continuous streams, requiring a different approach to consumer development that Powertools for AWS helps standardize.

| Aspect | Traditional Kafka Consumers | Lambda Kafka Consumer | 
|---|---|---|
| Model | Pull-based (you poll for messages) | Push-based (Lambda invoked with messages) | 
| Scaling | Manual scaling configuration | Automatic scaling to partition count | 
| State | Long-running application with state | Stateless, ephemeral executions | 
| Offsets | Manual offset management | Automatic offset commitment | 
| Schema Validation | Client-side schema validation | Optional Schema Registry integration with Event Source Mapping | 
| Error Handling | Per-message retry control | Batch-level retry policies | 

## Getting started[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#getting-started)

### Installation[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#installation)

Install the Powertools for AWS Lambda package with the appropriate extras for your use case:

| `1` | 
 | 

| `1` | 
 | 

| `1` | 
 | 

### Required resources[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#required-resources)

To use the Kafka consumer utility, you need an AWS Lambda function configured with a Kafka event source. This can be Amazon MSK, MSK Serverless, or a self-hosted Kafka cluster.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 | 
 | 

### Using ESM with Schema Registry[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#using-esm-with-schema-registry)

The Event Source Mapping configuration determines which mode is used. With `JSON`, Lambda converts all messages to JSON before invoking your function. With `SOURCE` mode, Lambda preserves the original format, requiring you function to handle the appropriate deserialization.

Powertools for AWS supports both Schema Registry integration modes in your Event Source Mapping configuration.

For simplicity, we will use a simple schema containing `name` and `age` in all our examples. You can also copy the payload example with the expected Kafka event to test your code.

| 1 2 3 4 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 | 
 | 

| 1 2 3 4 5 6 7 8 9 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 | 
 | 

| 1 2 3 4 5 6 7 8 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 | 
 | 

### Processing Kafka events[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#processing-kafka-events)

The Kafka consumer utility transforms raw Lambda Kafka events into an intuitive format for processing. To handle messages effectively, you'll need to configure a schema that matches your data format.

## Using Avro is recommended

We recommend Avro for production Kafka implementations due to its schema evolution capabilities, compact binary format, and integration with Schema Registry. This offers better type safety and forward/backward compatibility compared to JSON.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 | 
 | 

### Deserializing key and value[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#deserializing-key-and-value)

The `@kafka_consumer` decorator can deserialize both key and value fields independently based on your schema configuration. This flexibility allows you to work with different data formats in the same message.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 | 
 | 

### Handling primitive types[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#handling-primitive-types)

When working with primitive data types (strings, integers, etc.) rather than structured objects, you can simplify your configuration by omitting the schema specification for that component. Powertools for AWS will deserialize the value always as a string.

## Common pattern: Keys with primitive values

Using primitive types (strings, integers) as Kafka message keys is a common pattern for partitioning and identifying messages. Powertools automatically handles these primitive keys without requiring special configuration, making it easy to implement this popular design pattern.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 | 
 | 

### Message format support and comparison[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#message-format-support-and-comparison)

The Kafka consumer utility supports multiple serialization formats to match your existing Kafka implementation. Choose the format that best suits your needs based on performance, schema evolution requirements, and ecosystem compatibility.

## Selecting the right format

For new applications, consider Avro or Protocol Buffers over JSON. Both provide schema validation, evolution support, and significantly better performance with smaller message sizes. Avro is particularly well-suited for Kafka due to its built-in schema evolution capabilities.

| Format | Schema Type | Description | Required Parameters | 
|---|---|---|---|
| JSON | `"JSON"` | Human-readable text format | None | 
| Avro | `"AVRO"` | Compact binary format with schema | `value_schema`(Avro schema string) | 
| Protocol Buffers | `"PROTOBUF"` | Efficient binary format | `value_schema`(Proto message class) | 

| Feature | JSON | Avro | Protocol Buffers | 
|---|---|---|---|
| Schema Definition | Optional | Required JSON schema | Required .proto file | 
| Schema Evolution | None | Strong support | Strong support | 
| Size Efficiency | Low | High | Highest | 
| Processing Speed | Slower | Fast | Fastest | 
| Human Readability | High | Low | Low | 
| Implementation Complexity | Low | Medium | Medium | 
| Additional Dependencies | None | `avro`package | `protobuf`package | 

Choose the serialization format that best fits your needs:

- **JSON**: Best for simplicity and when schema flexibility is important
- **Avro**: Best for systems with evolving schemas and when compatibility is critical
- **Protocol Buffers**: Best for performance-critical systems with structured data

## Advanced[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#advanced)

### Accessing record metadata[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#accessing-record-metadata)

Each Kafka record contains important metadata that you can access alongside the deserialized message content. This metadata helps with message processing, troubleshooting, and implementing advanced patterns like exactly-once processing.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 | 
 | 

#### Available metadata properties[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#available-metadata-properties)

| Property | Description | Example Use Case | 
|---|---|---|
| `topic` | Topic name the record was published to | Routing logic in multi-topic consumers | 
| `partition` | Kafka partition number | Tracking message distribution | 
| `offset` | Position in the partition | De-duplication, exactly-once processing | 
| `timestamp` | Unix timestamp when record was created | Event timing analysis | 
| `timestamp_type` | Timestamp type (CREATE_TIME or LOG_APPEND_TIME) | Data lineage verification | 
| `headers` | Key-value pairs attached to the message | Cross-cutting concerns like correlation IDs | 
| `key` | Deserialized message key | Customer ID or entity identifier | 
| `value` | Deserialized message content | The actual business data | 
| `original_value` | Base64-encoded original message value | Debugging or custom deserialization | 
| `original_key` | Base64-encoded original message key | Debugging or custom deserialization | 
| `value_schema_metadata` | Metadata about the value schema like `schemaId`and`dataFormat` | Data format and schemaId propagated when integrating with Schema Registry | 
| `key_schema_metadata` | Metadata about the key schema like `schemaId`and`dataFormat` | Data format and schemaId propagated when integrating with Schema Registry | 

### Custom output serializers[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#custom-output-serializers)

Transform deserialized data into your preferred object types using output serializers. This can help you integrate Kafka data with your domain models and application architecture, providing type hints, validation, and structured data access.

## Choosing the right output serializer

- **Pydantic models**offer robust data validation at runtime and excellent IDE support
- **Dataclasses**provide lightweight type hints with better performance than Pydantic
- **Custom functions**give complete flexibility for complex transformations and business logic

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 | 
 | 

### Error handling[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#error-handling)

Handle errors gracefully when processing Kafka messages to ensure your application maintains resilience and provides clear diagnostic information. The Kafka consumer utility provides specific exception types to help you identify and handle deserialization issues effectively.

Info

Fields like `value`, `key`, and `headers` are decoded lazily, meaning they are only deserialized when accessed. This allows you to handle deserialization errors at the point of access rather than when the record is first processed.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 | 
 | 

#### Exception types[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#exception-types)

| Exception | Description | Common Causes | 
|---|---|---|
| `KafkaConsumerDeserializationError` | Raised when message deserialization fails | Corrupted message data, schema mismatch, or wrong schema type configuration | 
| `KafkaConsumerAvroSchemaParserError` | Raised when parsing Avro schema definition fails | Syntax errors in schema JSON, invalid field types, or malformed schema | 
| `KafkaConsumerMissingSchemaError` | Raised when a required schema is not provided | Missing schema for AVRO or PROTOBUF formats (required parameter) | 
| `KafkaConsumerOutputSerializerError` | Raised when output serializer fails | Error in custom serializer function, incompatible data, or validation failures in Pydantic models | 
| `KafkaConsumerDeserializationFormatMismatch` | Raised when SchemaConfig format is wrong | When integrating with Schema Registry, the data format is propagated, so Powertools for AWS catches this error if the format is different from the configured one. | 

### Integrating with Idempotency[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#integrating-with-idempotency)

When processing Kafka messages in Lambda, failed batches can result in message reprocessing. The [idempotency utility](https://docs.aws.amazon.com/powertools/python/latest/utilities/idempotency/) prevents duplicate processing by tracking which messages have already been handled, ensuring each message is processed exactly once.

The [idempotency utility](https://docs.aws.amazon.com/powertools/python/latest/utilities/idempotency/) automatically stores the result of each successful operation, returning the cached result if the same message is processed again, which prevents potentially harmful duplicate operations like double-charging customers or double-counting metrics.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 | 
 | 

TIP: By using the Kafka record's unique coordinates (topic, partition, offset) as the idempotency key, you ensure that even if a batch fails and Lambda retries the messages, each message will be processed exactly once.

### Handling partial batch failures[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#handling-partial-batch-failures)

When processing Kafka messages, individual records may fail while others succeed. By default, Lambda retries the entire batch when any record fails. To retry only the failed records, use the [Batch Processing utility](https://docs.aws.amazon.com/powertools/python/latest/utilities/batch/#processing-messages-from-kafka) with `EventType.Kafka`.

This feature allows Lambda to checkpoint successful records and only retry the failed ones, significantly improving processing efficiency and reducing duplicate processing.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 | 
 | 

Using with deserialization

The Batch Processing utility uses the basic `KafkaEventRecord` data class. For advanced deserialization (Avro, Protobuf), you can use the Kafka Consumer's deserialization utilities inside your record handler function.

### Best practices[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#best-practices)

#### Handling large messages[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#handling-large-messages)

When processing large Kafka messages in Lambda, be mindful of memory limitations. Although the Kafka consumer utility optimizes memory usage, large deserialized messages can still exhaust Lambda's resources.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 | 
 | 

For large messages, consider these proven approaches:

- **Store the data**: use Amazon S3 and include only the S3 reference in your Kafka message
- **Split large payloads**: use multiple smaller messages with sequence identifiers
- **Increase memory**Increase your Lambda function's memory allocation, which also increases CPU capacity

#### Batch size configuration[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#batch-size-configuration)

The number of Kafka records processed per Lambda invocation is controlled by your Event Source Mapping configuration. Properly sized batches optimize cost and performance.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 | 
 | 

Different workloads benefit from different batch configurations:

- **High-volume, simple processing**: Use larger batches (100-500 records) with short timeout
- **Complex processing with database operations**: Use smaller batches (10-50 records)
- **Mixed message sizes**: Set appropriate batching window (1-5 seconds) to handle variability

#### Cross-language compatibility[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#cross-language-compatibility)

When using binary serialization formats across multiple programming languages, ensure consistent schema handling to prevent deserialization failures.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 | 
 | 

Common cross-language challenges to address:

- **Field naming conventions**: camelCase in Java vs snake_case in Python
- **Date/time**: representation differences
- **Numeric precision handling**: especially decimals

### Troubleshooting common errors[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#troubleshooting-common-errors)

### Troubleshooting[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#troubleshooting)

#### Deserialization failures[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#deserialization-failures)

When encountering deserialization errors with your Kafka messages, follow this systematic troubleshooting approach to identify and resolve the root cause.

First, check that your schema definition exactly matches the message format. Even minor discrepancies can cause deserialization failures, especially with binary formats like Avro and Protocol Buffers.

For binary messages that fail to deserialize, examine the raw encoded data:

| 1 2 3 4 5 6 7 | 
 | 

#### Schema compatibility issues[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#schema-compatibility-issues)

Schema compatibility issues often manifest as successful connections but failed deserialization. Common causes include:

- **Schema evolution without backward compatibility**: New producer schema is incompatible with consumer schema
- **Field type mismatches**: For example, a field changed from string to integer across systems
- **Missing required fields**: Fields required by the consumer schema but absent in the message
- **Default value discrepancies**: Different handling of default values between languages

When using Schema Registry, verify schema compatibility rules are properly configured for your topics and that all applications use the same registry.

#### Memory and timeout optimization[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#memory-and-timeout-optimization)

Lambda functions processing Kafka messages may encounter resource constraints, particularly with large batches or complex processing logic.

For memory errors:

- Increase Lambda memory allocation, which also provides more CPU resources
- Process fewer records per batch by adjusting the `BatchSize`parameter in your event source mapping
- Consider optimizing your message format to reduce memory footprint

For timeout issues:

- Extend your Lambda function timeout setting to accommodate processing time
- Implement chunked or asynchronous processing patterns for time-consuming operations
- Monitor and optimize database operations, external API calls, or other I/O operations in your handler

## Monitoring memory usage

Use CloudWatch metrics to track your function's memory utilization. If it consistently exceeds 80% of allocated memory, consider increasing the memory allocation or optimizing your code.

## Kafka consumer workflow[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#kafka-consumer-workflow)

### Using ESM with Schema Registry validation (SOURCE)[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#using-esm-with-schema-registry-validation-source)

### Using ESM with Schema Registry deserialization (JSON)[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#using-esm-with-schema-registry-deserialization-json)

### Using ESM without Schema Registry integration[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#using-esm-without-schema-registry-integration)

## Testing your code[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/kafka/#testing-your-code)

Testing Kafka consumer functions is straightforward with pytest. You can create simple test fixtures that simulate Kafka events without needing a real Kafka cluster.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 | 
 | 

| 1 2 3 4 5 6 7 8 9 | 
 |