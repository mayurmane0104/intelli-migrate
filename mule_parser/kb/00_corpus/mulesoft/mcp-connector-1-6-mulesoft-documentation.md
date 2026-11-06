# MCP Connector 1.6 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mcp-connector/latest](https://docs.mulesoft.com/mcp-connector/latest)

---

# MCP Connector 1.6

Anypoint Connector for MCP (MCP Connector) uses the Model Context Protocol (MCP) to enable AI clients that support MCP to invoke and interact with APIs, connectors, and apps.

Use MCP Connector to connect LLM applications with your APIs. Expose APIs with complex endpoints as simpler, more atomic tools or resources that are better suited for agentic clients. Decide on what is straightforward, repeatable, and optimal for agent actions, and start there.

MCP is an open protocol that enables integration between LLM applications and external data, services, and tools.

The MCP protocol:

- 
Enhances AI precision by supplying AI with relevant information, leading to more accurate responses. 
- 
Empowers AI to manage intricate tasks that require access to external data or services. 
- 
Promotes interoperability between AI models and external systems, simplifying integration into workflows. 

MCP Connector:

- 
Enables you to expose your Mule apps, connectors, and custom APIs using the MCP protocol to further enable agentic experiences from agents in Claude, Cursor, Windsurf, and your own agents. 
- 
Enables you to write Mule apps that can act as both an MCP server and a client. The resulting MCP server or client runs inside of Mule, which means you don’t need to configure your own hosting environment. - 
When acting as an MCP server, Mule allows AI clients to use existing API-led investments, legacy systems, and SaaS applications that don’t natively support MCP. 
- 
When acting as an MCP client, Mule helps you create connections and orchestrations where AI agents are added as just another system in the workflow. 
 
- 
- 
Allows you to incorporate AI agents into your existing Enterprise ecosystem, using Mule as the orchestration layer. 
- 
Supports Streamable HTTP (recommended) and SSE (deprecated) for both server and client [transport methods](#connection-types).
- 
Supports custom response headers on every exposed endpoint, including `/sse`,`/message`, and`/mcp`. Use custom response headers for security, operational, integration, and governance benefits.
- 
Provides distributed tracing support, enabling comprehensive monitoring and observability of MCP interactions across distributed systems. 

This makes the capabilities of your Mule APIs and applications available to a growing ecosystem of AI agents.

For information about compatibility and fixed issues, see the MCP Connector Release Notes.

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

These are some common use cases for the connector:

- 
Customer Service Use AI agents to help human agents be more efficient by handling time-intensive tasks like reviewing case histories, analyzing reported issues, and retrieving relevant information. 
- 
Sales Improve sales teams' success by accelerating prospect research, generating customized collateral, and preparing contracts. 
- 
Marketing Empower marketing teams with AI-driven support for drafting social media content, conducting market research, and analyzing campaign performance. 

## Connection Types

- 
Streamable HTTP Allows you to deploy multiple instances of your MCP server to run behind a load balancer without clients knowing about the individual server URLs. Clients connect to a single endpoint (like `/mcp`) and the load balancer distributes requests across all your MCP server instances. This is particularly useful for scalability in cloud environments, where you might have multiple replicas of your Mule app running.When acting as an MCP client, use Streamable HTTP to connect your Mule application to remote MCP servers using the same scalable, load-balanced approach. 
- 
SSE Client (Deprecated) Enables MCP Connector to establish a persistent, one-way (server-sent) connection to an MCP server using the Server-Sent Events (SSE) standard. This type of connection allows the MCP server to push real-time updates and messages to the client without the need for the client to constantly poll for new information. 
- 
SSE Server (Deprecated) Exposes the MCP server using the Server-Sent Events (SSE) transport. This allows MCP clients to establish persistent, one-way connections to this server to receive real-time updates and messages. 

### Streamable HTTP Limitations

The Streamable HTTP connection type has no support for:

- 
Calling the GET `/mcp`endpoint for getting notifications
- 
Resumability and Redelivery 

### SSE Limitations

| The SSE server transport ( | 

This applies to the SSE *server* transport.
The SSE *client* connection (`<mcp:sse-client-connection>`) is unaffected because it makes an outbound connection to a remote MCP server.

## Next Step

After you complete the prerequisites, you’re ready to create an app and configure the connector using [Anypoint Studio](mcp-connector-studio) or [Anypoint Code Builder](mcp-connector-acb).

## See Also

- 
[MuleSoft MCP Support: Get Started With Model Context Protocol](https://blogs.mulesoft.com/news/model-context-protocol/)
- 
[Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro)
- 
[MuleSoft Help Center](https://help.mulesoft.com)