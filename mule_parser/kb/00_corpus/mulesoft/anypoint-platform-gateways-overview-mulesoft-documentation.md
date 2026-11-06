# Anypoint Platform Gateways Overview | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/gateway-home](https://docs.mulesoft.com/gateway-home)

---

**Summary**

# Anypoint Platform Gateways Overview

An API gateway is an intermediary between a client application and a set of microservices or backend APIs. Responsibilities include request routing, rate limiting, caching, authentication, authorization, security, monitoring, and logging.

A gateway enables you to add a dedicated orchestration layer on top of your backend APIs and services to help you separate orchestration from implementation.

Anypoint Platform offers two gateway products for managing and securing your APIs:

## Omni Gateway

Omni Gateway (formally Flex Gateway) is an Envoy-based, ultrafast lightweight API gateway designed to manage and secure APIs running anywhere. Built to seamlessly integrate with DevOps and CI/CD workflows, Omni Gateway delivers the performance required for the most demanding applications and microservices while providing enterprise security and manageability across any environment.

For more information, see [Omni Gateway Overview](../gateway/latest/).

## Anypoint Mule Gateway

Mule runtime engine includes an embedded Mule Gateway. You can leverage the governance capabilities of API Manager to apply, among other capabilities, throttling, security, caching, and logging to your APIs.

Using Mule Gateway, you can, for example:

- 
Apply a basic authentication policy on top of a Mule application. 
- 
Enrich an incoming or outgoing message. 
- 
Add any other complex capability to an API without having to write any code. 

For more information, see [Mule Gateway Overview](../mule-gateway/mule-gateway-capabilities-mule4).

## Omni Gateway vs. Mule Gateway

Omni Gateway can manage and secure APIs, both Mule and non-Mule, running anywhere.

In contrast, Mule Gateway protects a single Mule API. The key advantage is that it’s easy for Mule app developers to provide basic endpoint protection. You can configure Mule in Anypoint Runtime Manager as a CloudHub proxy application, protecting multiple backends.

Building custom policies on Mule Gateway is similar to building an application with Java using the Mule DSL. Building a custom policy in Omni Gateway is based on Envoy-provided Rust WASM SDKs. A Mule Gateway policy cannot be reused in Omni Gateway and vice versa, because the underlying architectures are fundamentally different.

MuleSoft recommends you choose Omni Gateway for high-availability and high-performance Mule and non-Mule applications.

To protect Mule applications that do not require the management and maintenance of underlying infrastructure, choose Mule Gateway for CloudHub.

| Omni Gateway | Mule Gateway | |
|---|---|---|
| Envoy-based API gateway to secure all APIs, Mule and non-Mule, running anywhere | Java-based API gateway embedded into Mule, to secure only Mule APIs | |
| 
 | 
 | Java Spring Application embedded into Mule | 
| 
 | 
 | 
 | 
| 
 | 
 | 
 | 
| 
 | Rust WASM SDKs | Java and Mule DSL | 

## Policy Availability by Gateway

| Policy | Summary | Managed Omni Gateway | Omni Gateway Connected Mode | Omni Gateway Local Mode | Mule Gateway | 
|---|---|---|---|---|---|
| A2A Agent Card | Rewrites the Agent card URL to match the server instance public URL | No | No | ||
| A2A PII Detector | Detects personally identifiable information (PII) in requests sent to the agent | No | No | ||
| A2A Prompt Decorator | Decorates prompts with context information | No | No | ||
| A2A Schema Validation | Validates Agent requests to ensure they conform to the A2A specification | No | No | ||
| A2A Token Based Rate Limit | Limits API usage based on the number of GPT-4o-mini tokens consumed by the agents | No | No | ||
| LLM Token Based Rate Limit | Rate limits LLM Proxy usage based on token consumption | No | No | ||
| Agent Connection Telemetry | Tracks the number of requests made to agent or MCP server instances | No | No | ||
| Amazon Bedrock Guardrails | Evaluates LLM prompts and responses against Amazon Bedrock guardrails for content safety, PII detection, and contextual grounding | No | No | ||
| Azure Content Safety | Evaluates LLM prompts and responses against Azure AI Content Safety for harmful content, jailbreak attempts, hallucinations, and copyrighted material | No | No | ||
| AWS Lambda | Allows access based on the basic authorization mechanism, with user-password defined on LDAP | No | |||
| AWS Request Signature | Signs outgoing requests with AWS Signature Version 4 (SigV4) or Signature Version 4A (SigV4A) | No | |||
| Basic Authentication: LDAP | Allows access based on the basic authorization mechanism, with user-password defined on LDAP | ||||
| Basic Authentication: Simple | Allows access based on the basic authorization mechanism, with a single user-password | ||||
| Client ID Enforcement | Allows access only to authorized client applications | No | |||
| Circuit Breaker | Prevents an upstream from receiving too many requests or connections | No | |||
| Credential Injection Basic Authentication | Injects a basic authorization header into outgoing requests | No | |||
| Credential Injection API Key | Injects an API key or client credentials headers into outgoing requests | No | |||
| Credential Injection OAuth 2.0 | Injects an OAuth 2.0 authorization header into outgoing requests | No | |||
| Credential Injection JWT Generation | Generates and injects a JWT token into outgoing requests | No | |||
| OAuth 2.0 OBO Credential Injection | Exchanges incoming bearer tokens using OAuth 2.0 Token Exchange (RFC 8693), Microsoft Entra ID On-Behalf-Of, or OAuth 2.0 Token Exchange with CIBA | No | No | ||
| Cross-Origin Resource Sharing (CORS) | Enables access to resources residing in external domains | ||||
| DataWeave Body Transformation | Transforms request or response body content with a DataWeave script | No | |||
| DataWeave Headers Transformation | Transforms request or response headers with a DataWeave script | No | |||
| DataWeave Request Filter | Filters requests by using a DataWeave script | No | |||
| Detokenization | Returns a tokenized value to its original value | No | No | No | |
| External Authorization | Authenticates requests by using an external gRPC or HTTP authorization service | No | |||
| External Processing | Sends the incoming HTTP requests or outgoing HTTP responses to an external gRPC service for additional processing | No | |||
| GraphQL Introspection Control | Blocks or allows requests that  access the  `type`, and`__typename`GraphQL meta fields | No | |||
| GraphQL Operation Limits | Limits GraphQL operation depth, aliases, root fields, and directives | No | |||
| GraphQL Schema Validation | Validates incoming GraphQL operations against a GraphQL schema definition | No | |||
| GraphQL Static Query Complexity | Calculates query complexity and blocks requests that exceed the defined budget | No | |||
| Header Injection | Adds headers to a request or a response | ||||
| Header Removal | Removes headers from a request or a response | ||||
| Health Check | Monitors API upstream health at specific intervals | No | No | ||
| HTTP Caching | Caches HTTP responses from an API implementation | ||||
| Injection Protection | Scans request headers, path, query, and body to protect against SQL, XSS, and custom injection attacks in incoming requests | No | |||
| IP Allowlist | Allows a list or range of specified IP addresses to request access | ||||
| IP Blocklist | Blocks a single IP address or a range of IP addresses from accessing an API endpoint | ||||
| A2A In-Task Authorization Code | Ensures secondary credentials are present for in-task authentication using OAuth 2.0 Authorization Code flow | No | No | ||
| JSON Threat Protection | Protects against malicious JSON in API requests | ||||
| JWT Validation | Validates a JWT | ||||
| MCP Attribute-Based Access Control | Controls access to tools, resources, and prompts based on user information such as Tiers, IP, Headers, or Claims | No | No | ||
| MCP Global Access | Restricts which MCP tools are exposed by defining Allow and Block rules | No | No | ||
| MCP PII Detector | Blocks elicitation responses containing personally identifiable information (PII) from reaching MCP servers | No | No | ||
| MCP Payload Optimization | Optimizes MCP tool responses for token consumption by transforming HTML to Markdown and removing unnecessary data | No | No | ||
| MCP Schema Validation | Validates MCP requests to ensure they conform to the MCP specification | No | No | ||
| MCP Support | Adds MCP support to an Omni Gateway MCP server instance. This policy is required for your MCP server instance to function properly. | No | No | ||
| MCP Tool Mapping | Redefines tool names and descriptions to reduce prompt complexity and improve LLM comprehension | No | No | ||
| Message Logging | Logs custom messages using information from incoming requests, responses from the backend, or information from other policies applied to the same API endpoint | ||||
| Outbound Message Logging | Logs custom messages from outbound requests sent to upstream services, responses from upstream services, or information from other outbound policies applied to the same upstream service | No | |||
| OAuth 2.0 Access Token Enforcement Using Mule OAuth Provider | Allows access only to authorized client applications | No | No | No | |
| OAuth 2.0 Token Introspection | Allows access only to authorized client applications | No | |||
| OpenAM OAuth 2.0 Token Enforcement | Allows access only to authorized client applications | No | No | No | |
| OpenID Connect OAuth 2.0 Access Token Enforcement | Allows access only to authorized client applications | No | |||
| PingFederate OAuth 2.0 Token Enforcement | Allows access only to authorized client applications | No | No | No | |
| Rate Limiting | Monitors access to an API by defining the maximum number of requests processed within a period of time | ||||
| Rate Limiting: SLA-based | Monitors access to an API by defining the maximum number of requests processed within a timespan, based on SLAs | No | |||
| Regex Prompt Guard | Blocks LLM requests that match deny-list regex patterns | No | No | ||
| Response Timeout | Sets the maximum duration Omni Gateway waits for a response from an upstream service | No | |||
| Schema Validation | Validates incoming traffic against a supplied OAS3 schema | No | |||
| SOAP Schema Validation | Validates incoming traffic against a specified WSDL schema | No | |||
| SSE Logging | Logs every SSE event while streaming | No | No | ||
| Stream Idle Timeout | Sets the maximum duration a stream can remain idle without receiving a request or response | No | |||
| Spike Control | Regulates API traffic | ||||
| Traffic Management for Multiple Upstream Services | Manages API instance traffic to multiple upstream services from a single consumer endpoint | No | |||
| Traffic Management for Multiple Upstream Services (Weighted) | Manages API instance traffic to multiple upstream services from a single consumer endpoint, using weighted percentages | No | |||
| Transport Layer Security (TLS) - Inbound | Enables authentication between a client and the API proxy | No | |||
| Transport Layer Security (TLS) - Outbound | Enables two-way authentication between the API proxy and an upstream service | No | |||
| Tokenization | Transforms sensitive data into a nonsensitive equivalent, named token | No | No | No | |
| Upstream Idle Timeout | Sets the maximum duration a stream between Omni Gateway and an upstream service can remain idle | No | |||
| WebSocket Connection Limit | Limits the number of simultaneous WebSocket connections that each API instance allows | No | |||
| XML Threat Protection | Protects against malicious XML in API requests |