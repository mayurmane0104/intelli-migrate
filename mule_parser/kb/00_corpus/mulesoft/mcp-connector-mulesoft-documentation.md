# MCP Connector | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/release-notes/connector/mcp-connector-release-notes-mule-4](https://docs.mulesoft.com/release-notes/connector/mcp-connector-release-notes-mule-4)

---

# MCP Connector

Anypoint Connector for MCP (MCP Connector) uses the Model Context Protocol (MCP) to enable AI clients that support MCP to invoke and interact with APIs, connectors, and apps.

Guide: [MCP Connector User Guide](../../mcp-connector/latest/)

## 1.6.0

**June 8, 2026**

### What’s New

- 
MCP Connector now includes the **MCP Server - Create Elicitation**operation and the**MCP Client - Elicitation Listener**source.These capabilities implement the MCP elicitation protocol so servers can request additional structured input from clients during tool and resource execution. 
- 
Elicitation is opt-in through the new **Enable Elicitations**field on the client configuration.For multi-worker deployments, use Streamable HTTP server transport and configure an Object Store on the server connection so elicitation correlation is preserved across workers. SSE server transport is single-worker only. 
- 
Server connection configuration now includes the new **Elicitation Timeout Seconds**,**Elicitations Object Store**, and**Elicitation Polling Seconds**fields to route elicitation responses across replicas.
- 
The **MCP Client - List Tools**,**MCP Client - List Resources**, and**MCP Client - List Prompts**operations now include the new**Additional Properties**field.Pass custom headers, correlation IDs, tenant identifiers, or other metadata on list calls. The values are propagated to the corresponding server-side listeners and are accessible from `attributes.additionalProperties`.

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.9.6 and later | 
| OpenJDK | 17 | 
| MCP Java SDK | 1.0.1 | 
| MCP Protocol | 2025-06-18 | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| The MCP client now refreshes the OAuth bearer token automatically when an outbound request receives an HTTP 401 response, and the resulting error is reclassified as a connectivity error so it is eligible for reconnection. | W-22677666 | 
| Events emitted by the  | W-21663653 | 

## 1.5.0

**May 1, 2026**

### What’s New

- 
MCP Connector now includes the **MCP Client - Get Prompt**and**MCP Client - List Prompts**operations, and the**MCP Server - Prompt Listener**source.Expose server-side prompt templates with typed arguments and consume them from clients, with responses supporting text, image, embedded resource, and resource link content. 
- 
The **MCP Client - Call Tool**operation now includes the new**Extract Structured Content**field.Define tool parameter and output schemas using either inline JSON or external files, fully supported by robust design-time schema validation. With this, the connector now also includes the new `MCP:SCHEMA_VALIDATION_FAILED`error.
- 
The connector now includes response attributes to support structured client-side error handling with HTTP response details. With this, the connector now also includes the new `MCP:UNAUTHORIZED`error.

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.9.6 and later | 
| OpenJDK | 17 | 
| MCP Java SDK | 1.0.1 | 
| MCP Protocol | 2025-06-18 | 

## 1.4.0

**March 22, 2026**

### What’s New

- 
The MCP Java SDK is upgraded to the latest release version (1.0.0). 
- 
Both the server and client transports now default to 2025-06-18 as the preferred version of the protocol. 
- 
Both the server and client transports now set the `Mcp-Protocol-Version`header to the version negotiated upon connection initialization.

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.9.6 and later | 
| OpenJDK | 17 | 
| MCP Java SDK | 1.0.0 | 
| MCP Protocol | 2025-06-18 | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| When no audience is defined in the Mule flow, TextContent responses for tool calls no longer serialize an empty audience array in annotations. An empty array could cause some MCP clients to interpret the content as being visible to nobody and filter it out. | W-21425262 | 

## 1.3.1

**January 16, 2026**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.9.6 and later | 
| OpenJDK | 17 | 
| MCP Java SDK | 0.11.2 | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| Nested objects are now properly serialized for downstream consumption. | W-20405721 | 
| In the  | W-20437648 | 
| Tool parameters are now validated according to the JSON schema before execution. | W-20037056 | 

## 1.3.0

**November 13, 2025**

### What’s New

- 
The **MCP Server - On New Session Listener**source now supports custom rejection headers with the new**Reject With Headers**field.

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.9.6 and later | 
| OpenJDK | 17 | 
| MCP Java SDK | 0.11.2 | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| In the  | W-19387519 | 
| The connector now properly cleans up tracked inbound requests even when exceptions occur during message processing, preventing memory leaks that could accumulate over time. | W-20037035 | 

## 1.2.1

**September 11, 2025**

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.9.6 and later | 
| OpenJDK | 17 | 
| MCP Java SDK | 0.11.2 | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| The MCP server now responds with HTTP 404 for expired sessions, and the MCP client now properly handles session expiration by creating a new session when receiving HTTP 404 responses. | W-19178802 | 
| Connection and disconnection handling is now improved because disconnect methods are now properly subscribed and executed. | W-19264682 | 

## 1.2.0

**August 6, 2025**

### What’s New

- 
MCP Connector now supports distributed tracing. 

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.9.6 and later | 
| OpenJDK | 17 | 
| MCP Java SDK | 0.10.0 | 

## 1.1.0

**July 18, 2025**

### What’s New

- 
A **Default Request Headers**parameter is added to both the SSE Client and Streamable HTTP Client connection types within the MCP Connector’s Client configuration. This parameter lets you specify custom headers to send with every request to the MCP server.

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.9.6 and later | 
| OpenJDK | 17 | 
| MCP Java SDK | 0.10.0 | 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| Serialization errors with ObjectStore v2 no longer occur. | W-19045311 | 

## 1.0.0

**June 26, 2025**

### What’s New

- 
MCP Connector 1.0.0 is not backward-compatible with the 0.1.0-BETA version of this connector. For more information, see [Upgrading MCP Connector to Version 1.0.0](../../mcp-connector/latest/mcp-connector-upgrade-migrate).
- 
Support for the Streamable HTTP transport method is added. 
- 
You can now add custom response headers on every exposed endpoint (including `/sse`,`/messages`, and the new`/mcp`).
- 
You no longer need to add the `mule.http.service.implementation=NETTY`system property.

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.9.6 and later | 
| OpenJDK | 17 | 
| MCP Java SDK | 0.10.0 | 

## 0.1.0-BETA (Deprecated)

**April 15, 2025**

### What’s New

This is a new connector.

| MCP Connector is a beta connector that is subject to the Beta Services Terms at  | 

For more information, see the [MCP Connector User Guide](../../mcp-connector/latest/).

### Compatibility

| Software | Version | 
|---|---|
| Mule | 4.9.3 and later | 
| OpenJDK | 17 | 

## See Also

- 
[Salesforce Help](https://help.salesforce.com)
- 
[MuleSoft Services](https://www.mulesoft.com/support-and-services)
- 
[Known Issues](https://help.salesforce.com/s/issues)