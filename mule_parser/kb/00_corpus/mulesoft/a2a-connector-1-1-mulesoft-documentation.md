# A2A Connector 1.1 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/a2a-connector/latest](https://docs.mulesoft.com/a2a-connector/latest)

---

# A2A Connector 1.1

Anypoint Connector for Agent2Agent (A2A) (A2A Connector) facilitates inter-agent communication for Large Language Model (LLM) agents and other applications by implementing the A2A protocol. This enables agents to interact and delegate specialized tasks to other agents.

The A2A protocol is an open standard that supports:

- 
Capability discovery Identifies the functions and services offered by agents. 
- 
Interaction negotiation Establishes communication methods between agents. 
- 
Secure information exchange Transmits data between agent systems without requiring direct internal access. 

A2A Connector provides Mule app integration that functions as both A2A servers and A2A clients.

For information about compatibility and fixed issues, see the A2A Connector Release Notes.

## Before You Begin

To use this connector, you must be familiar with:

- 
Anypoint Connectors 
- 
Mule runtime engine (Mule) 
- 
Elements and global elements in a Mule flow 
- 
How to create a Mule app using Anypoint Code Builder or Anypoint Studio 

Before creating an app, you must have:

- 
Java 17 
- 
Apache Maven 
- 
Anypoint Platform 
- 
Credentials to connect with the target resource 
- 
The latest versions of Anypoint Code Builder or Anypoint Studio 

## Common Use Cases for the Connector

Build specialized domain specific agents each for Customer Service, Sales, or Marketing and have other agents interact with these agents using the A2A protocol.

A2A Connector also provides distributed tracing support, enabling comprehensive monitoring and observability of A2A interactions across distributed systems.

## Connection Types

A2A Connector supports these connection types:

- 
A2A server 
- 
A2A client 

## Next Step

After you complete the prerequisites, you’re ready to create an app and configure the connector using [Anypoint Studio](a2a-connector-studio) or [Anypoint Code Builder](a2a-connector-acb).

## See Also

- 
[Salesforce Help](https://help.salesforce.com)