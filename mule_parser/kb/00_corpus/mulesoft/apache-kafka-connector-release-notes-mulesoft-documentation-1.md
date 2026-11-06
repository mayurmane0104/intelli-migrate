# Apache Kafka Connector Release Notes | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/release-notes/connector/kafka-connector-release-notes-mule-4](https://docs.mulesoft.com/release-notes/connector/kafka-connector-release-notes-mule-4)

---

# Apache Kafka Connector Release Notes

Support Category: [Select](https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/Agreements/versioning-back-support-policy.pdf)

Anypoint Connector for Apache Kafka (Kafka Connector) enables you to connect to the Apache Kafka messaging system, enabling seamless integration between your applications and an Apache Kafka cluster.

Guide: [Apache Kafka Connector](../../kafka-connector/latest/)

Reference: [Apache Kafka Connector Reference](../../kafka-connector/latest/kafka-connector-reference)

## 4.14.0

**June 12, 2026**

### What’s New

- 
Kafka Connector now supports DataWeave expressions in connection parameters. Expression support applies to the username, password, token ID, token HMAC, client ID, client secret, consumer group ID, and bootstrap servers parameters. 

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, 2.8.1, 3.2.0, 3.3.2, 3.4.0, 3.5.1, 3.6.1, 3.7.0, 3.8.0, 3.9.0, 3.9.2 | 
| OpenJDK | 8, 11, and 17 | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| The com.fasterxml.jackson.core:jackson-databind component is upgraded to 2.22.0. | W-3300013 | 
| The at.yawk.lz4:lz4-java component is upgraded to 1.11.0. | W-3300013 | 
| The commons-io:commons-io component is upgraded to 2.22.0. | W-3300013 | 

## 4.13.1

**April 25, 2026**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, 2.8.1, 3.2.0, 3.3.2, 3.4.0, 3.5.1, 3.6.1, 3.7.0, 3.8.0, 3.9.0, 3.9.2 | 
| OpenJDK | 8, 11, and 17 | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| Updated Apache Kafka client to version 3.9.2 for enhanced security and stability. | W-22161314 | 

## 4.13.0

**March 21, 2026**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, 2.8.1, 3.2.0, 3.3.2, 3.4.0, 3.5.1, 3.6.1, 3.7.0, 3.8.0, 3.9.0 | 
| OpenJDK | 8, 11, and 17 | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| This release includes general security fixes. | W-20953782 | 

## 4.12.2

**January 23, 2026**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, 2.8.1, 3.2.0, 3.3.2, 3.4.0, 3.5.1, 3.6.1, 3.7.0, 3.8.0, 3.9.0 | 
| OpenJDK | 8, 11, and 17 | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| The connector now includes the secure LZ4 compression library ( | W-20880709 | 

## 4.12.1 (Deprecated)

This version is deprecated. The fixed issues for this version are in version [4.12.2](#4-12-2).

**December 21, 2025**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, 2.8.1, 3.2.0, 3.3.2, 3.4.0, 3.5.1, 3.6.1, 3.7.0, 3.8.0, 3.9.0 | 
| OpenJDK | 8, 11, and 17 | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| The connector now properly skips certificate validation when the TLS context is configured with  | W-18214347 | 

## 4.12.0

**November 5, 2025**

### What’s New

- 
Kafka Connector now supports deserializing records serialized with Avro schemas. This new functionality enables you to easily integrate your Mule applications with Avro Schema Deserializer. For details, refer to [Configure the Confluent Schema Registry](../../kafka-connector/latest/kafka-connector-configure-confluent-example#configure-the-confluent-schema-registry).

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, 2.8.1, 3.2.0, 3.3.2, 3.4.0, 3.5.1, 3.6.1, 3.7.0, 3.8.0, 3.9.0 | 
| OpenJDK | 8, 11, and 17 | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| The connector no longer throws a  | W-19153642 | 

## 4.11.1

**September 24, 2025**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, 2.8.1, 3.2.0, 3.3.2, 3.4.0, 3.5.1, 3.6.1, 3.7.0, 3.8.0, 3.9.0 | 
| OpenJDK | 8, 11, and 17 | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| Upgraded jackson-databind library version from 2.18.3 to 2.20.0. | W-19688916 | 

## 4.11.0

**August 28, 2025**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, 2.8.1, 3.2.0, 3.3.2, 3.4.0, 3.5.1, 3.6.1, 3.7.0, 3.8.0, 3.9.0, 3.9.1 | 
| OpenJDK | 8, 11, and 17 | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| All operations now throw the new  | W-19132680 | 

## 4.10.2

**July 23, 2025**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, 2.8.1, 3.2.0, 3.3.2, 3.4.0, 3.5.1, 3.6.1, 3.7.0, 3.8.0, 3.9.0 | 
| OpenJDK | 8, 11, and 17 | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| The Kafka client dependency is upgraded to version 3.9.1 to fix the  | W-19063366 | 

## 4.10.1

**April 17, 2025**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, 2.8.1, 3.2.0, 3.3.2, 3.4.0, 3.5.1, 3.6.1, 3.7.0, 3.8.0, 3.9.0 | 
| OpenJDK | 8, 11, and 17 | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| The connector no longer overrides serializers configuration when it is configured in the  | W-17105037 | 

## 4.10.0

**December 19, 2024**

### What’s New

- 
The **Partitioner**field for all connection types in the producer configuration now includes a`NONE`option, which enables the Kafka client to manage the partition strategy.

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, 2.8.1, 3.2.0, 3.3.2, 3.4.0, 3.5.1, 3.6.1, and 3.7.0 | 
| OpenJDK | 8, 11, and 17 | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| The connector no longer overrides the transaction ID if it is configured in the  | W-17105037 | 
| The connector now handles Kafka headers with null values properly by converting them to empty byte arrays instead of throwing a  | W-16167262 | 

## 4.9.0

**August 23, 2024**

### What’s New

- 
The **Bulk publish**operation is added to publish multiple messages at the same time.
- 
The custom `MuleKafkaAvroSerializer`property is added to publish messages in Avro format.

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, 2.8.1, 3.2.0, 3.3.2, 3.4.0, 3.5.1, 3.6.1, and 3.7.0 | 
| OpenJDK | 8, 11, and 17 | 

## 4.8.0

**June 18, 2024**

### What’s New

- 
Apache Kafka Connector now supports OAuth2 Client Credentials grant type authentication to integrate seamlessly with OAuth2-compliant authorization servers. Use the **Consumer SASL/OAUTHBEARER - Client Credentials Connection**or**Producer SASL/OAUTHBEARER - Client Credentials Connection**options in the connector configuration.
- 
The consumer and producer connection configurations have a new **Additional properties**field to customize the Kafka connection as you desire.

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, 2.8.1, 3.2.0, 3.3.2, 3.4.0, 3.5.1, 3.6.1, and 3.7.0 | 
| OpenJDK | 8, 11, and 17 | 

## 4.7.6

**May 31, 2024**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, 2.8.1, 3.2.0, 3.3.2, 3.4.0, 3.5.1, and 3.6.1 | 
| OpenJDK | 8, 11, and 17 | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| The connector performance is now improved when redeploying. | W-15637208 | 

## 4.7.5

**February 2, 2024**

### What’s New

- 
This connector is now compatible with Java 17. 

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, 2.8.1, 3.2.0, 3.3.2, 3.4.0, 3.5.1, and 3.6.1 | 
| OpenJDK | 8, 11, and 17 | 

## 4.7.4

**January 9, 2024**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, 2.8.1, 3.2.0, 3.3.2, 3.4.0, and 3.6.1 | 
| OpenJDK | 8 and 11 | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| The Mule application deployment no longer fails when the connector connection test fails. | W-13197433 | 
| The Kafka clients library is upgraded to version 3.6.1 to address reported security vulnerabilities. | W-14486778 | 

## 4.7.3

**November 29, 2023**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, 2.8.1, 3.2.0, 3.3.2, and 3.4.0 | 
| OpenJDK | 8 and 11 | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| Upgraded snappy-java library version from 1.1.8.1 to 1.1.10.4. | W-14486778 | 

## 4.7.2

**May 4, 2023**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, 2.8.1, 3.2.0, 3.3.2, and 3.4.0 | 
| OpenJDK | 8 and 11 | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| Upgraded the Kafka Clients library from org.apache.kafka:kafka-clients:3.3.2 to org.apache.kafka:kafka-clients:3.4.0. | W-12665458 | 

## 4.7.1

**March 17, 2023**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, 2.8.1, 3.2.0 and 3.3.2 | 
| OpenJDK | 8 and 11 | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| Updated the  | W-12660459 | 
| Updated internal dependencies. | W-12710406 | 

## 4.7.0

**February 13, 2023**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, 2.8.1, 3.2.0 and 3.3.2 | 
| OpenJDK | 8 and 11 | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| Kafka Connector now uses kafka-clients 3.3.2. | W-11554436 | 
| The  | W-12042969 | 
| Kafka connector now supports the boolean system property  | W-12150770 | 

## 4.6.8

**November 25, 2022**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, and 2.8.1 | 
| OpenJDK | 8 and 11 | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| The Kafka record is no longer empty when using the  | W-11768903 | 
| Kafka Connector now throws the expected error when the message body exceeds the maximum topic size. | W-12042969 | 

## 4.6.7

**May 30, 2022**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, and 2.8.1 | 
| OpenJDK | 8 and 11 | 

### Fixed Issues

| Issue | ID | 
|---|---|
| The connector now displays the correct field names for  | W-11137428 | 

## 4.6.6

**May 5, 2022**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, and 2.8.1 | 
| OpenJDK | 8 and 11 | 

### Fixed Issues

| Issue | ID | 
|---|---|
| The Kafka message key is no longer empty when reprocessing messages when the topic contains more than one partition. | W-11048498 | 
| The connector no longer throws null pointer exceptions when the message key is null. | W-11090869 | 

## 4.6.5

**April 7, 2022**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, and 2.8.1 | 
| OpenJDK | 8 and 11 | 

### Fixed Issues

| Issue | ID | 
|---|---|
| The Kafka message key is no longer empty when reprocessing messages. | W-10795597, W-10889605 | 

## 4.6.4

**February 4, 2022**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, and 2.8.1 | 
| OpenJDK | 8 and 11 | 

### Fixed Issues

| Issue | ID | 
|---|---|
| Reconnection issues caused the Kafka  | SE-22821, SE-24437 | 

## 4.6.3

**February 2, 2022**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, and 2.8.1 | 
| OpenJDK | 8 and 11 | 

### Fixed Issues

| Issue | ID | 
|---|---|
| The  | CONN-9887 | 

## 4.6.2

**January 4, 2022**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, and 2.8.1 | 
| OpenJDK | 8 and 11 | 

### Fixed Issues

| Issue | ID | 
|---|---|
| Kafka  | SE-23630 | 
| Kafka  | SE-22821 | 

## 4.6.1

**October 27, 2021**

### What’s New

- 
Upgraded the Kafka client library to version 2.8.1. 

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, 2.7.0, and 2.8.1 | 
| OpenJDK | 8 and 11 | 

## 4.6.0

**October 19, 2021**

### What’s New

- 
Added the **Consumer SASL/TOKEN Connection**and**Producer SASL/TOKEN Connection**authentication types, which use token delegation to connect to the Kafka cluster.

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, and 2.7.0 | 
| OpenJDK | 8 and 11 | 

## 4.5.7

**September 28, 2021**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, and 2.7.0 | 
| OpenJDK | 8 and 11 | 

### Fixed Issues

| Issue | ID | 
|---|---|
| Kafka Connector reconnection did not work when there was an ACL access issue. | SE-22595 | 
| Kafka  | SE-22520 | 

## 4.5.6

**September 15, 2021**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, and 2.7.0 | 
| OpenJDK | 8 and 11 | 

### Fixed Issues

| Issue | ID | 
|---|---|
| The reconnection strategy did not work. | SE-22340 | 

## 4.5.5

**July 12, 2021**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, and 2.7.0 | 
| OpenJDK | 8 and 11 | 

### Fixed Issues

- 
Kafka **Consumer**and**Message Listener**failed after picking one message. (SE-21705)

## 4.5.4

**June 11, 2021**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, and 2.7.0 | 
| OpenJDK | 8 and 11 | 

### Fixed Issues

- 
Kafka **Message Listener**failed to process messages while using IMMEDIATE ACK. (SE-21070)

## 4.5.3

**June 8, 2021**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, and 2.7.0 | 
| OpenJDK | 8 and 11 | 

### Fixed Issues

- 
Kafka Connector was continuously rebalancing the loop when using multiple consumers per partition. (SE-20824) 

## 4.5.2

**April 8, 2021**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, and 2.7.0 | 
| OpenJDK | 8 and 11 | 

### Fixed Issues

- 
Payload was null in the Batch component when using the Batch message listener source. (SE-20119) 

## 4.5.1

**March 19, 2021**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, and 2.7.0 | 
| OpenJDK | 8 and 11 | 

### Fixed Issues

- 
Performance degraded when using the Publish operation. (SE-20124) 
- 
Kafka connector created a new connection every time a producer published a new message. (SE-20003) 

## 4.5.0

**February 25, 2021**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, 2.6.0, and 2.7.0 | 
| OpenJDK | 8 and 11 | 

### Features

Added a new configuration property to Producer connections to enable the selection of a message partition strategy from those provided by the `kafka-clients` library. The message partition strategy is used for routing messages to partitions when a key or a partition is not provided.

### Fixed Issues

Fixed the performance degradation issue that occurred when an incorrect key was used to remove closed sessions. (SE-19638)

## 4.4.3

**January 29, 2021**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, and 2.7.0 | 
| OpenJDK | 8 and 11 | 

### Fixed Issues

Fixed the Anypoint Studio test connection functionality for producer and consumer connections.

## 4.4.2

**January 15, 2021**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0, and 2.7.0 | 
| OpenJDK | 8 and 11 | 

### Features

Upgraded the Kafka client library to version 2.7.0.

## 4.4.1

**January 12, 2021**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0 | 
| OpenJDK | 8 and 11 | 

### Fixed Issues

On Windows, using backslashes as path separators when providing a full path for a keytab file did not work. (SE-15416)

## 4.4.0

**November 26, 2020**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0 | 
| OpenJDK | 8 and 11 | 

### New Features

Added the ability to leverage the manual offset commit option for the **Consume** operation.

### Fixed Issues

The manual connector commit inside Mule error handling had no effect. (SE-18605)

## 4.3.5

**November 2, 2020**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0 | 
| OpenJDK | 8 and 11 | 

### Fixed Issues

Apache Kafka Connector ignored the values of the **Heartbeat interval** and **Session timeout** fields in the consumer configuration. (SE-18343)

## 4.3.4

**October 15, 2020**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0 | 
| OpenJDK | 8 and 11 | 

### Fixed Issues

The issue that caused the Kafka Connector source to fail to reconnect after multiple queue stop events is fixed. (SE-17727)

## 4.3.3

**September 18, 2020**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0 | 
| OpenJDK | 8 and 11 | 

### Fixed Issues

The issue that caused Kafka Connector to throw a `KAFKA:COMMIT_FAILED` error when messages took a longer time to process than what was specified in the **Maximum poll interval** parameter is fixed. (SE-17447)

## 4.3.2

**July 30, 2020**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0 | 

### Fixed Issues

The issue that caused Kafka Connector to throw a `No ConnectionProvider defined` error when the connection expires while the client consumer is polling is fixed. (SE-16727)

## 4.3.1

**July 14, 2020**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0 | 

### Fixed Issues

Fixed an issue where the value for the password key of the JAAS configuration was not set. (SE-16670)

## 4.3.0

**June 30, 2020**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0 | 

### New Features

Added support for a SASL/PLAIN connection.

## 4.2.0

**June 19, 2020**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0, 2.5.0 | 

### New Features

Added support for a Kerberos connection.

### Fixed Issues

- 
Kafka Connector 4.1.0 did not allow you to pass `ssl.endpoint.identification.algorithm`with a blank value. (SE-16215)
- 
Kafka Connector 4.0.0 had missing connection options. (SE-15175) 

## 4.1.0

**May 28, 2020**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0 | 

### New Features

- 
Added the SASL SCRAM connection type for connecting to a Kafka broker. This connection type works with the SCRAM-SHA-256 and SCARM-SHA-512 authentication mechanisms. 
- 
Added the Endpoint Identification Algorithm field to all connection types. Clients use this field to validate the server hostname. 

### Fixed Issues

- 
Inability to set additional properties in Kafka Connector 4.0.0 (SE-15197) 

## 4.0.0

**February 25, 2020**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0 | 

### New Features

Kafka Connector 4.0.0 contains a lot of changes to improve efficiency, including new operations to enable you to better understand how to use the connector.

All of the changes included in this version break backward compatibility.

See [Kafka Connector Upgrade](../../kafka-connector/latest/kafka-connector-upgrade-migrate) for detailed information about all of the changes in this release.

The new features and changes in this release include:

- 
Four new operations, including: - 
Commit 
- 
Consume 
- 
Publish 
- 
Seek 
 
- 
- 
A new Batch Message Listener source 
- 
The addition of different acknowledgment modes in the Consumer configuration, including: - 
AUTO 
- 
MANUAL 
- 
DUPS_OK 
- 
IMMEDIATE 
 
- 
- 
One plaintext connection type that supports transactions 

## 3.0.12

**September 9, 2020**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.4.0 | 

### Fixed Issues

- 
Fixed a vulnerability related to the Guava library. 
- 
Kafka Connector versions 3.0.8 through 3.0.11 do not work with Mule 4.1.x, as previously stated by the documentation. (SE-17493) 

## 3.0.11 (Deprecated)

**June 12, 2020**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.2.1 and later | 
| Apache Kafka | 2.4.0 | 

### Fixed Issues

Changed the Scheduler type from cpuLight to IO. (SE-16328)

## 3.0.10 (Deprecated)

**December 17, 2019**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.2.1 and later | 
| Apache Kafka | 2.4.0 | 

### Fixed Issues

- 
Updated Kafka Client version to the latest to prevent internal exceptions. (SE-14104) 
- 
Fixed Kafka consumer disconnection that occurred after a period of inactivity. (SE-14221) 

## 3.0.9 (Deprecated)

**December 16, 2019**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.2.1 and later | 
| Apache Kafka | 2.3.0 | 

### Fixed Issues

Fixed relative path issue for Kafka connector settings with Windows. (SE-14140)

## 3.0.8 (Deprecated)

**November 25, 2019**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.2.1 and later | 
| Apache Kafka | 2.3.0 | 

### Fixed Issues

When `KafkaConsumer` was stopped by the Mule runtime engine, Kafka threw a concurrency error. (SE-13970)

## 3.0.7

**August 21, 2019**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.1.1 and later | 
| Apache Kafka | 2.3.0 | 

### Features

- 
Upgraded the Kafka Clients library to version 2.3.0. (CONN-2857) 
- 
Implemented validation method for producer and consumer connection. (CONN-2698) 
- 
Added Scheduler Service for spawning new threads for consumers. (CONN-2849) 

### Fixed Issues

- 
Refactoring to improve compliance with the Mule development best practices. (CONN-2699, CONN-2700, CONN-2701, CONN-2702, CONN-2848, CONN-2703, CONN-2847, CONN-2747, CONN-2696, CONN-2697) 
- 
Deprecated the UNKNOWN error type that will be removed in the next major upcoming release. (CONN-2703) 
- 
In Kafka versions 3.0.2 to 3.0.6, in the **Publish Message**operation, the**Key**field appeared in Anypoint Studio as required. In version 3.0.7, the**Key**field was no longer required.
- 
In Kafka versions 3.0.2 to 3.0.6, in the **Message Consumer**source operation, the**Partition Offsets**field was described as "a list of offsets representing the partitions offsets configuration. For each element in the list you have to specify partition index and offset". In version 3.0.7, the**Partition Offsets**field is now described as "a list of objects that contain the index of the partition and the offset".
- 
In Kafka versions 3.0.2 to 3.0.6, in the **Message Consumer**source operation, the**Partition Offsets**field is typed as an array of offsets. In 3.0.2 to 3.0.6 in the Offset array, the**Partition Number**and**Partition Offset**fields did not require values. In 3.0.7, the**Partition Number**and**Partition Offset**fields now require values.
- 
In Kafka versions 3.0.2 to 3.0.6, in the **Repeatable File Store Stream**object, the**Max in Memory Size**field name was changed to be**In Memory Size**in 3.0.7.

## 3.0.6

**July 2, 2019**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.0.0 and later | 
| Apache Kafka | 2.2.0 | 

### Fixed Issues

Kafka connector overrode the user-defined `security.protocol=SASL_SSL` to use the `security.protocol=SSL` value. (SE-11947)

## 3.0.5

**June 19, 2019**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.0.0 and later | 
| Apache Kafka | 2.2.0 | 

### Fixed Issues

- 
Updated the Kafka Clients library to version 2.2.0. 
- 
Updated code to use the `poll(java.time.Duration)`method provided in the new library that replaces the deprecated`poll(long)`method. The deprecated method did not block beyond the timeout for waiting on a partition assignment. (KIP-266)

## 3.0.4

**May 16, 2019**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.0.0 and later | 
| Apache Kafka | 0.10.2.0 | 

### Fixed Issues

Fixed a performance connection validation issue relating to the same issue as in v3.0.3. (SE-11817)

## 3.0.3

**May 16, 2019**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.0.0 and later | 
| Apache Kafka | 0.10.2.0 | 

### Fixed Issues

- 
The **Test Connection**button in Anypoint Studio for the Kafka connector did not work in Mule 4. (SE-11817)
- 
Fixed a performance connection validation issue relating to the same issue as in v3.0.3. (SE-11817) 

## 3.0.2

**April 30, 2019**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.0.0 and later | 
| Apache Kafka | 0.10.2.0 | 

### Fixed Issues

- 
Can’t stop Kafka consumer flow. See [How To Stop Or Start Flows In Mule 4.x Programmatically](https://help.salesforce.com/s/articleView?id=001114843&type=1). (SE-11337)
- 
The **Test Connection**button in Anypoint Studio for the Kafka connector did not work in Mule 4. (SE-11817)

## 3.0.1

**June 26, 2018**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.0.0 and later | 
| Apache Kafka | 0.10.2.0 | 

### Features

None

### Fixed Issues

Kafka connector was not serializing and deserializing properly the messages that were not plain text. Now the content of the messages can be sent as any type (plain, XML, JSON) as the value is serialized and deserialized properly.

## See Also

- 
[Salesforce Help](https://help.salesforce.com)
- 
[MuleSoft Services](https://www.mulesoft.com/support-and-services)
- 
[Known Issues](https://help.salesforce.com/s/issues)