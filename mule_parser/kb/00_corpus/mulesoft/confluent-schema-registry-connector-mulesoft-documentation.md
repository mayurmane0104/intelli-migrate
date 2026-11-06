# Confluent Schema Registry Connector | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/confluent-schema-registry-connector/latest](https://docs.mulesoft.com/confluent-schema-registry-connector/latest)

---

# Confluent Schema Registry Connector

Anypoint Connector for Confluent Schema Registry (Confluent Schema Registry Connector) enables interaction with Confluent’s Schema Registry to save and retrieve avro schemas to reduce the size of an avro message while it transports through the network.

For information about compatibility and fixed issues, see the Confluent Schema Registry Connector Release Notes.

## Before You Begin

To use this connector, you must be familiar with:

- 
The Confluent Schema Registry Connector’s API 
- 
Anypoint Connectors 
- 
Mule runtime engine (Mule) 
- 
Elements and global elements in a Mule flow 
- 
How to create a Mule app using Anypoint Studio 

Before creating an app, you must have:

- 
Credentials to access the Confluent Schema Registry target resource 
- 
Anypoint Platform 
- 
Anypoint Studio or Anypoint Code Builder 

## Common Use Cases For the Connector

Some possible uses for this connector include:

- 
Send an avro message to a Kafka broker. 
- 
Consume an avro message with a schema ID. 
- 
Send a schema to Confluent Schema Registry using authentication. 

## Connection Types

Confluent Schema Registry connections use the following authentication types:

- 
Basic auth 
 Basic HTTP authentication supported by the API.
- 
Unsecured 
 Unauthenticated.

For information about configuring authentication types, see [Using Anypoint Studio to Configure Confluent Schema Registry Connector](confluent-schema-registry-connector-studio).

## Next Step

After you complete the prerequisites, you are ready to create an app and configure the connector using [Anypoint Studio](confluent-schema-registry-connector-studio).

## See Also

- 
[Use Exchange to Discover Connectors, Templates, and Examples](../../connectors/introduction/intro-use-exchange)
- 
[Salesforce Help](https://help.salesforce.com)