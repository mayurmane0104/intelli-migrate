# APIkit for AsyncAPI Module Reference | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/apikit/latest/apikit-asyncapi-module-reference](https://docs.mulesoft.com/apikit/latest/apikit-asyncapi-module-reference)

---

<dependency> <groupId>org.mule.modules</groupId> <artifactId>mule-asynckit-module</artifactId> <version>LATEST_VERSION</version>(1)<classifier>mule-plugin</classifier> </dependency>

# APIkit for AsyncAPI Module Reference

Integrate AsyncAPI specifications into Mule with the APIkit for AsyncAPI module: add the Maven dependency, declare the module namespace, and apply the XML schema when you configure generated scaffolding. This reference documents coordinates, namespaces, schema locations, and configuration elements you use to implement event-driven APIs.

## Dependencies

| 1 | Check the [APIkit Release Notes](apikit-release-notes)to get theLATEST_VERSION. | 

## Namespace and Schema

xmlns:apikit-asyncapi="http://www.mulesoft.org/schema/mule/apikit-asyncapi" xsi:schemaLocation="http://www.mulesoft.org/schema/mule/apikit-asyncapi http://www.mulesoft.org/schema/mule/apikit-asyncapi/current/mule-apikit-asyncapi.xsd">

## Configurations

### Config

Default configuration

#### Parameters

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Name | String | Name for this configuration. Connectors reference the configuration with this name. | None | Yes | 
| Api Definition | String | API definition. | None | Yes | 
| Disable Content Validation | Boolean | Disable payload content validation. | 
 | No | 
| Kafka Configs | Array of  | List of Kafka server configurations. One for each Kafka server listed in the specification that is scaffolded to create the app. | None | No | 
| Anypoint MQ Configs | Array of  | List of AMQ configurations. | None | No | 
| Solace Configs | Array of  | List of Solace configurations. | None | No | 
| Salesforce Pub/Sub Configs | Array of  | List of SalesforcePubSub configurations. | None | No | 
| Name | String | Identifier of this element used to reference it in other components. | None | Yes | 

### Supported Message Brokers

| Message Broker | Description | Supported Protocols | Configuration Details | 
|---|---|---|---|
| Anypoint MQ | Supports asynchronous messaging with Anypoint MQ. | anypointmq | Anypoint MQ configurations are specified in the server object of the AsyncAPI specification. Supports  | 
| Kafka | Supports asynchronous messaging with Apache Kafka. | kafka, kafka-secure | Kafka configurations are specified in the server object of the AsyncAPI specification. Supports  | 
| Salesforce platform events | Allows implementing an Async API specification using Anypoint Connector for Salesforce Pub/Sub (Salesforce Pub/Sub Connector). | salesforcepubsub* | Connection details are available in the properties file. Supports  In the  In the  | 
| Solace Pub/Sub+ | Supports the implementation of an Async API specification using Solace PubSub+ Connector. | solace | Connection details are available in the properties file. Supports  | 

* You must use Anypoint Connector for Salesforce Pub/Sub Connector 1.0.15 or later.

#### Associated Operations

#### Associated Sources

## Validation of Messages

Unless explicitly restricted, the JSON schema validation allows omitting and adding fields. Check the message validation against the schema in the following table:

| Schema Definition | Message | Valid | 
|---|---|---|
| { A: integer, B: string } | {A, B} | Yes | 
| { A: integer, B: string } | {C, D} | Yes | 
| { A: integer, B: string } required [A, B] | {C, D} | No | 
| { A: integer, B: string } required [A, B] | {A, B, C} | Yes | 
| { A: integer, B: string } required [A, B]  | {A, B, C} | No | 
| { A: integer, B: string } required [A, B]  | {A, B} | No | 

- 
The `required`field specifies the list of fields that are mandatory in the JSON object.
- 
The `additionalProperties`field specifies if you can include additional properties to the JSON object.

The schemas must specify `required` and `additionalProperties` in the API specification.

| The field value is checked against the type specified in the schema as part of the validation. | 

If an operation has multiple message schemas associated in the specification, the validation adheres to these principles:

- 
Messages are validated against every schema. 
- 
If it’s compliant with at least one schema, the message is considered valid. 
- 
If the message doesn’t adhere to at least one schema, the message is considered invalid. 

### Example

| Schema Definition | Message | Valid | 
|---|---|---|
| { A: integer, B: string } required [A, B]  | {A, B} | Yes | 
| { A: integer, B: string } required [A, B]  | {B, C} | No | 
| { A: integer, B: string } required [A, B]  | {A, B, C} | No | 
| { A: integer, B: string } required [A, B]  | {C, D} | Yes | 

## Operations

## Publish

`<apikit-asyncapi:publish>`

### Parameters

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Configuration | String | Name of the configuration to use | None | Yes | 
| Content | Binary | The binary content to be processed | #[payload] | No | 
| Disable Content Validation | Boolean | Indicates if validation of the content is disabled | 
 | No | 
| Config Ref | ConfigurationProvider | Name of the configuration used to execute this component | None | Yes | 
| Channel Name | String | Channel name | None | Yes | 
| Server Name | String | Server name | None | Yes | 
| Target Variable | String | Name of a variable in which the operation output is placed | None | No | 
| Target Value | String | Expression that is evaluated against the operation output and the result of that expression is stored in the target variable | #[payload] | No | 
| Error Mappings | Array of  | Set of error mappings | None | No | 

### Output

| Field | Description | 
|---|---|
| Type | 

### For Configurations

### Throws

- 
APIKIT-ASYNCAPI:INTERNAL_SERVER_ERROR 
- 
APIKIT-ASYNCAPI:PUBLISHING_ERROR 
- 
APIKIT-ASYNCAPI:VALIDATION_ERROR 

## Sources

## Message Listener

`<apikit-asyncapi:message-listener>`

### Parameters

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Configuration | String | Name of the configuration to use | None | Yes | 
| Disable Content Validation | Boolean | Disable payload content validation | None | No | 
| Channel Name | String | Channel name | None | Yes | 
| Servers | Array of String | List of servers to listen to | None | No | 
| Output MIME Type | String | MIME type of the payload that this operation generates | None | No | 
| Output Encoding | String | Encoding of the payload that this operation generates | None | No | 
| Primary Node Only | Boolean | Specifies if this source must be executed on the primary node when running in a cluster | None | No | 
| Config Ref | ConfigurationProvider | Name of the configuration used to execute this component | None | Yes | 
| Streaming Strategy | 
 | Specify and configure repeatable streams | None | No | 
| Redelivery Policy | Policy for processing the redelivery of the same message | None | No | 

### Output

| Field | Description | 
|---|---|
| Type | Any type | 
| Attributes Type | 

### For Configurations

## Types

### Kafka Config

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Server Key | String | Identifier for the server configuration within the AsyncAPI configuration | None | Yes | 
| Producer Config Ref | String | Reference to the Kafka Producer configuration | None | No | 
| Consumer Config Ref | String | Reference to the Kafka Consumer configuration | None | No | 

| The Server Key is required to uniquely identify the server configuration. The references for Producer and Consumer configurations are optional and depend on the specific setup and requirements of the Kafka implementation. | 

### Anypoint MQ Config

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Server Key | String | Identifier for the server configuration in AsyncAPI | None | Yes | 
| Config Ref | String | Reference to the Anypoint MQ configuration details | None | No | 

| The Server Key is required to uniquely identify the server configuration. Config Ref is optional and used to specify additional configuration details. | 

### Solace Config

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Server Key | String | Server key set in the AsyncAPI spec | None | Yes | 
| Config Ref | String | Reference to the configuration name of the Solace connection | None | No | 

| The Server Key is required to uniquely identify the server configuration. Config Ref is optional and used to specify additional configuration details. | 

### Limitations of Solace PubSub+ Connector

Solace PubSub+ Connector in APIkit for AsyncAPI has these limitations:

- 
The Solace PubSub+ Connector supports `queue`and`topic`for`destinations`in the**message listener**and**publish**operations. But the APIkit for AsyncAPI implementation only supports using`queue`as the value of`destination`.
- 
Only one operator of the same type must be mapped to the same `queue`of`destination`.

### Salesforce Pub/Sub Connector Config

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Server Key | String | Server key set in the AsyncAPI spec | None | Yes | 
| Config Ref | String | Reference to the name of the Salesforce Pub/Sub Connector configuration | None | No | 

| The Server Key is required to uniquely identify the server configuration. Config Ref is optional and used to specify additional configuration details. | 

### Repeatable In Memory Stream

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Initial Buffer Size | Number | Amount of memory allocated to consume the stream and provide random access to it. If the stream data is larger than the buffer capacity, it expands according to the  | None | No | 
| Buffer Size Increment | Number | How much the buffer size expands if it exceeds its initial size. A value of zero or lower specifies that the buffer doesn’t expand. When the buffer is full, a  | None | No | 
| Max Buffer Size | Number | Maximum amount of memory used. If more is used, a  | None | No | 
| Buffer Unit | Enumeration, one of: 
 | These attributes are expressed in this unit. | None | No | 

### Repeatable File Store Stream

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| In Memory Size | Number | Defines the maximum memory that the stream uses to keep data in memory. If it consumes more, the stream buffers the content on the disk. | None | No | 
| Buffer Unit | Enumeration, one of: 
 | The unit for expressing  | None | No | 

### Redelivery Policy

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Max Redelivery Count | Number | Maximum number of times a message can be redelivered and processed unsuccessfully before triggering process-failed-message | None | No | 
| Message Digest Algorithm | String | Secure hashing algorithm | SHA-256 | No | 
| Message Identifier | Strategy used to identify the messages | None | No | |
| Object Store | ObjectStore | Object store where the redelivery counter for each message is stored | None | No | 

### Redelivery Policy Message Identifier

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Use Secure Hash | Boolean | Whether to use a secure hash algorithm to identify a redelivered message. | None | No | 
| Id Expression | String | Expression used to determine if a message has been redelivered. You can set this property if  | None | No | 

### Publish Response

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Response Data | Object | Data the server returns in response to a request | None | No | 

### Error Mapping

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Source | Enumeration, one of: 
 | Type of error encountered during the operation | None | Yes | 
| Target | String | The specific component or module where the error needs to be addressed | None | Yes | 

### Kafka Message Attributes

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Channel Name | String | Name of the Kafka channel (topic) where the message is published or consumed | None | Yes | 
| Channel Parameters | Object | Additional parameters or settings specific to the channel | None | No | 
| Creation Timestamp | DateTime | Timestamp when the message was created | None | No | 
| Headers | Object | Metadata associated with the message, typically key-value pairs | None | No | 
| Key | String | This key determines the partition within the Kafka topic where the message is sent | None | No | 
| Leader Epoch | Number | Epoch of the leader broker at the time the message is sent | None | No | 
| Log Append Timestamp | DateTime | Timestamp when the message is appended to the log | None | No | 
| Offset | Number | Message offset in the Kafka topic partition | None | No | 
| Partition | Number | Partition within the Kafka topic where the message is stored | None | No | 
| Protocol | String | Protocol the Kafka server uses | None | No | 
| Server Name | String | Name of the Kafka server that processes the message | None | Yes | 

### Anypoint MQ Message Attributes

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Ack Token | String | Token used for acknowledging the receipt of a message | None | No | 
| Channel Name | String | Name of the Anypoint MQ channel where the message is published or consumed | None | Yes | 
| Channel Parameters | Object | Additional parameters or settings specific to the channel | None | No | 
| Content Type | String | MIME type of the message content | None | No | 
| Delivery Count | Number | Number of times the message is delivered | None | No | 
| Headers | Object | Metadata associated with the message, typically key-value pairs | None | No | 
| Message Id | String | Unique identifier for the message | None | Yes | 
| Properties | Object | Custom properties associated with the message | None | No | 
| Protocol | String | Protocol the Anypoint MQ server uses | None | No | 
| Server Name | String | Name of the Anypoint MQ server that processes the message | None | Yes | 

### Solace Message Attributes

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| DMQ Eligible | Boolean | Indicates if the message is eligible for Dead Message Queue | 
 | No | 
| Channel Name | String | Name of the Solace channel where the message is published or consumed | None | No | 
| Channel Parameters | Object | Additional parameters or settings specific to the Solace channel | None | No | 
| Content Type | String | MIME type of the message content | None | No | 
| Delivery Mode | String | Delivery mode of the message | None | No | 
| Discard Indication | Boolean | Indicates if the message is discarded | 
 | No | 
| Eliding Eligible | Boolean | Indicates if the message is eligible for eliding | 
 | No | 
| Endpoint Type | String | Type of endpoint used | None | No | 
| Message Reference Id | String | Reference identifier for the message | None | No | 
| Priority | Number | Priority level of the message | 0 | No | 
| Protocol | String | Protocol the Solace server uses | None | No | 
| Receive Timestamp | DateTime | Timestamp when the message was received | None | No | 
| Redelivered | Boolean | Indicates if the message is redelivered | 
 | No | 
| Reply | Boolean | Indicates if the message expects a reply | 
 | No | 
| Server Name | String | Name of the Solace server that processes the message | None | Yes | 
| Time To Live | Number | Time in milliseconds that the message remains valid | 0 | No | 

### Salesforce Pub/Sub Attributes

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Channel Name | String | Name of the Salesforce Pub/Sub channel where the message is published or consumed | None | No | 
| Channel Parameters | Object | Additional parameters or settings specific to the Salesforce Pub/Sub channel | None | No | 
| Protocol | String | Protocol the Salesforce Pub/Sub server uses | None | No | 
| Server Name | String | Name of the Salesforce Pub/Sub server that processes the message | None | No |