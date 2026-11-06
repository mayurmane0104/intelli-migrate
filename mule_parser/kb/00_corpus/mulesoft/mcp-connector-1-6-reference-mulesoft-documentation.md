# MCP Connector 1.6 Reference | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mcp-connector/latest/mcp-connector-reference](https://docs.mulesoft.com/mcp-connector/latest/mcp-connector-reference)

---

One of:

- 
[Sse Client](#Client_SseClient)(Deprecated)

Anypoint Connector for MCP (MCP Connector) allows Mule applications to act as both MCP servers and clients. When acting as an MCP client, MuleSoft facilitates the creation of integrations and orchestrations where AI agents are integrated as just another system in the workflow.

Configuration element that acts as a client and connects to an MCP server.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Name | String | Name for this configuration. Connectors reference the configuration with this name. | Yes | |
| Connection | One of: 
 | The connection types to provide to this configuration. | Yes | |
| Client Name | String | Name the client uses to identify itself during the protocol initialization phase. This isn’t the same as the name given to this config element (which is later referenced through config-ref parameters). This name doesn’t need to be unique. | Yes | |
| Client Version | String | Version the client uses to identify itself during the protocol initialization phase. This doesn’t need to match the connector or Mule application version. | Yes | |
| Enable Elicitations | Boolean | Enable support for elicitation requests from the MCP server. When enabled without an elicitation-listener source, a default handler automatically declines all elicitation requests. When an elicitation-listener is configured, it overrides this default behavior. | Yes | |
| Name | String | ID used to reference this configuration. | Yes | |
| Expiration Policy | Configures the minimum amount of time that a dynamic configuration instance can remain idle before Mule considers it eligible for expiration. | 

Streamable HTTP transport is recommended.

The SSE (Server-Sent Events) Client connection type enables MCP Connector to establish a persistent, one-way (server-sent) connection to an MCP server using the SSE standard. This type of connection allows the MCP server to push real-time updates and messages to the client without the need for the client to constantly poll for new information.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Request Timeout | Number | Sets the duration to wait for server responses before timing out requests. | 30 | |
| Request Timeout Unit | Enumeration, one of: 
 | Time Unit for the requestTimeout parameter. | SECONDS | |
| Authentication | HttpRequestAuthentication | |||
| Default Request Headers | Object | Defines custom headers to send with every request to the MCP server. | ||
| Server Url | String | The base URL for the target MCP server. | 
 | |
| Sse Endpoint Path | String | /sse | ||
| Reconnection Delay | Number | Specifies how long to wait before reinitializing the SSE connection when it times out or closes. | 500 | |
| Reconnection Delay Unit | Enumeration, one of: 
 | Time Unit for the reconnectionDelay | MILLISECONDS | |
| Tls Context | ||||
| Reconnection | When the application is deployed, a connectivity test is performed on all connectors. If set to true, deployment fails if the test doesn’t pass after exhausting the associated reconnection strategy. | 

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Request Timeout | Number | Sets the duration to wait for server responses before timing out requests. | 30 | |
| Request Timeout Unit | Enumeration, one of: 
 | Time Unit for the requestTimeout parameter | SECONDS | |
| Authentication | HttpRequestAuthentication | |||
| Default Request Headers | Object | Defines custom headers to send with every request to the MCP server. | ||
| Server Url | String | The base URL for the target MCP server. | 
 | |
| Mcp Endpoint Path | String | /mcp | ||
| Tls Context | ||||
| Reconnection | When the application is deployed, a connectivity test is performed on all connectors. If set to true, deployment fails if the test doesn’t pass after exhausting the associated reconnection strategy. | 

Configuration element to act as an MCP server.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Name | String | Name for this configuration. Connectors reference the configuration with this name. | 
 | |
| Connection | 
 | The connection types to provide to this configuration. | 
 | |
| Server Name | String | Name this server uses to identify itself during the protocol initialization phase. This isn’t the same as the name given to this config element (which is later referenced through config-ref parameters). This name doesn’t need to be unique. | 
 | |
| Server Version | String | Version this server uses to identify itself during the protocol initialization phase. This doesn’t need to match the connector or Mule application version. | 
 | |
| Name | String | ID used to reference this configuration. | 
 | 

Streamable HTTP transport is recommended.

Exposes the MCP server using the SSE transport.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Request Timeout | Number | Request timeout. | 10 | |
| Request Timeout Unit | Enumeration, one of: 
 | Request Timeout unit | SECONDS | |
| Elicitation Timeout Seconds | Number | Timeout in seconds for elicitation requests. Elicitation requests sent to the client wait this long for a response before timing out. | 60 | |
| Listener Config | String | Reference to the HTTP Listener config used to expose the SSE and messaging endpoints. | 
 | |
| Sse Endpoint Path | String | The endpoint path clients use to initiate the SSE connection. | /sse | |
| Messages Path | String | The path to send the messaging endpoint request to. | /message | |
| Default Sse Response Headers | Object | |||
| Default Message Response Headers | Object | |||
| Elicitations Object Store | ObjectStore | ObjectStore that correlates elicitation requests and responses. For deployments with multiple replicas, configure a distributed object store (using Hazelcast or OSv2) to ensure responses are properly routed to the correct worker. If not specified, a default transient instance is used, which is recommended only for single-instance deployments. | ||
| Elicitation Polling Seconds | Number | Polling interval in seconds used to check for elicitation responses written by another replica. This setting controls how frequently the connector checks for responses that arrived on a different worker. | 5 | |
| Reconnection | When the application is deployed, a connectivity test is performed on all connectors. If set to true, deployment fails if the test doesn’t pass after exhausting the associated reconnection strategy. | 

Exposes the MCP server using the Streamable HTTP transport, as defined in [Streamable HTTP](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http).

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Request Timeout | Number | Request timeout. | 10 | |
| Request Timeout Unit | Enumeration, one of: 
 | Request Timeout unit | SECONDS | |
| Elicitation Timeout Seconds | Number | Timeout in seconds for elicitation requests. Elicitation requests sent to the client wait this long for a response before timing out. | 60 | |
| Listener Config | String | Reference to the http:listener-config used to expose the SSE and messaging endpoints. | 
 | |
| Mcp Endpoint Path | String | The endpoint path clients use to initiate the SSE connection. | 
 | |
| Response Content Type | Enumeration, one of: 
 | Whether responses should be sent by initiating a SSE stream or returning a single application/json body. | SSE | |
| Default Response Headers | Object | Custom headers to include on all valid responses (not including rejected invalid requests). | ||
| Session Idle Timeout | Number | Timeout for idle sessions. | 5 | |
| Session Idle Timeout Unit | Enumeration, one of: 
 | Time unit qualifying the sessionIdleTimeout | MINUTES | |
| Sessions Object Store | ObjectStore | An ObjectStore used to store session information. When deploying to multiple replicas, define a specific object store distributed across all replicas, either through Hazelcast or OSv2. If not specified, a default transient instance is created. Persistence must be enabled if running MCP Server listeners in a multi-worker deployment. For CloudHub 2.0, the Clustered option also must be enabled. | ||
| Elicitations Object Store | ObjectStore | ObjectStore that correlates elicitation requests and responses. For deployments with multiple replicas, configure a distributed object store (using Hazelcast or OSv2) to ensure responses are properly routed to the correct worker. If not specified, a default transient instance is used, which is recommended only for single-instance deployments. | ||
| Elicitation Polling Seconds | Number | Polling interval in seconds used to check for elicitation responses written by another replica. This setting controls how frequently the connector checks for responses that arrived on a different worker. | 5 | |
| Reconnection | When the application is deployed, a connectivity test is performed on all connectors. If set to true, deployment fails if the test doesn’t pass after exhausting the associated reconnection strategy. | 

`<mcp:call-tool>`

Invokes a tool on a remote MCP server.

Response validation is managed by the underlying SDK; the connector doesn’t perform its own validation.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Configuration | String | Name of the configuration to use. | Yes | |
| Tool Name | String | Name of the tool to invoke. | Yes | |
| Arguments | Object | The tool’s input arguments. | #[payload] | |
| Extract Structured Content | Boolean | Controls how the payload is exposed when a tool returns structured content. When  | true | |
| Config Ref | ConfigurationProvider | Name of the configuration to use to execute this component. | Yes | |
| Additional Properties | Object | #[null] | ||
| Target Variable | String | Name of the variable that stores the operation’s output. | ||
| Target Value | String | Expression that evaluates the operation’s output. The outcome of the expression is stored in the  | #[payload] | |
| Error Mappings | Array of  | Set of error mappings. | ||
| Reconnection Strategy | Retry strategy in case of connectivity errors. | 

| Type | |
| Attributes Type | 

MCP:CONNECTIVITY

MCP:INTERNAL_ERROR

MCP:INVALID_PARAMS

MCP:INVALID_REQUEST

MCP:JSON_RPC_ERROR

MCP:METHOD_NOT_FOUND

MCP:PARSE_ERROR

MCP:REQUEST_TIMEOUT

MCP:RETRY_EXHAUSTED

MCP:SCHEMA_VALIDATION_FAILED

MCP:SERVER_ERROR

MCP:UNAUTHORIZED

`<mcp:get-prompt>`

Resolves a prompt by name in the remote MCP server and returns the rendered prompt messages. Use this operation when your Mule application (acting as an MCP client) needs to fetch a prompt that a remote MCP server exposes, optionally passing arguments that the server uses to render the prompt content.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Configuration | String | Name of the configuration to use. | Yes | |
| Prompt Name | String | Name of the prompt to retrieve from the remote MCP server. | Yes | |
| Config Ref | ConfigurationProvider | Name of the configuration to use to execute this component. | Yes | |
| Arguments | Object | Arguments to pass to the prompt. The accepted keys and their types are defined by the remote prompt’s argument schema. | #[null] | |
| Additional Properties | Object | Additional properties to include with the request. Use this field to specify custom key-value pairs that are sent with the MCP connector request. This field is optional and null-safe. | #[null] | |
| Target Variable | String | Name of the variable that stores the operation’s output. | ||
| Target Value | String | Expression that evaluates the operation’s output. The outcome of the expression is stored in the  | #[payload] | |
| Error Mappings | Array of  | Set of error mappings. | ||
| Reconnection Strategy | Retry strategy in case of connectivity errors. | 

| Type | |
| Attributes Type | Any | 

MCP:CONNECTIVITY

MCP:INTERNAL_ERROR

MCP:INVALID_PARAMS

MCP:INVALID_REQUEST

MCP:JSON_RPC_ERROR

MCP:METHOD_NOT_FOUND

MCP:PARSE_ERROR

MCP:REQUEST_TIMEOUT

MCP:RETRY_EXHAUSTED

MCP:SCHEMA_VALIDATION_FAILED

MCP:SERVER_ERROR

MCP:UNAUTHORIZED

`<mcp:list-prompts>`

Lists all prompts available in the remote MCP server. Each entry in the returned array includes metadata such as the prompt name, optional title, description, and the argument definitions the prompt accepts.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Configuration | String | Name of the configuration to use. | Yes | |
| Config Ref | ConfigurationProvider | Name of the configuration to use to execute this component. | Yes | |
| Streaming Strategy | 
 | Configures how Mule processes streams. Repeatable streams are the default behavior. | ||
| Additional Properties | Object | Additional properties to include with the request. Use this field to specify custom key-value pairs that are sent with the MCP connector request. This field is optional and null-safe. | #[null] | |
| Target Variable | String | Name of the variable that stores the operation’s output. | ||
| Target Value | String | Expression that evaluates the operation’s output. The outcome of the expression is stored in the  | #[payload] | |
| Error Mappings | Array of  | Set of error mappings. | ||
| Reconnection Strategy | Retry strategy in case of connectivity errors. | 

| Type | Array of  | 

MCP:CONNECTIVITY

MCP:INTERNAL_ERROR

MCP:INVALID_PARAMS

MCP:INVALID_REQUEST

MCP:JSON_RPC_ERROR

MCP:METHOD_NOT_FOUND

MCP:PARSE_ERROR

MCP:REQUEST_TIMEOUT

MCP:RETRY_EXHAUSTED

MCP:SCHEMA_VALIDATION_FAILED

MCP:SERVER_ERROR

MCP:UNAUTHORIZED

`<mcp:list-resources>`

Lists all the available resources in the remote MCP server.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Configuration | String | Name of the configuration to use. | Yes | |
| Config Ref | ConfigurationProvider | Name of the configuration to use to execute this component. | Yes | |
| Streaming Strategy | 
 | Configures how Mule processes streams. Repeatable streams are the default behavior. | ||
| Additional Properties | Object | Additional properties to include with the request. Use this field to specify custom key-value pairs that are sent with the MCP connector request. This field is optional and null-safe. | #[null] | |
| Target Variable | String | Name of the variable that stores the operation’s output. | ||
| Target Value | String | Expression that evaluates the operation’s output. The outcome of the expression is stored in the  | #[payload] | |
| Error Mappings | Array of  | Set of error mappings. | ||
| Reconnection Strategy | Retry strategy in case of connectivity errors. | 

| Type | Array of  | 

MCP:CONNECTIVITY

MCP:INTERNAL_ERROR

MCP:INVALID_PARAMS

MCP:INVALID_REQUEST

MCP:INVALID_URI

MCP:JSON_RPC_ERROR

MCP:METHOD_NOT_FOUND

MCP:PARSE_ERROR

MCP:REQUEST_TIMEOUT

MCP:RETRY_EXHAUSTED

MCP:SCHEMA_VALIDATION_FAILED

MCP:SERVER_ERROR

MCP:UNAUTHORIZED

`<mcp:list-tools>`

Lists all the available tools in the remote MCP server.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Configuration | String | Name of the configuration to use. | Yes | |
| Config Ref | ConfigurationProvider | Name of the configuration to use to execute this component. | Yes | |
| Streaming Strategy | 
 | Configures how Mule processes streams. Repeatable streams are the default behavior. | ||
| Additional Properties | Object | Additional properties to include with the request. Use this field to specify custom key-value pairs that are sent with the MCP connector request. This field is optional and null-safe. | #[null] | |
| Target Variable | String | Name of the variable that stores the operation’s output. | ||
| Target Value | String | Expression that evaluates the operation’s output. The outcome of the expression is stored in the  | #[payload] | |
| Error Mappings | Array of  | Set of error mappings. | ||
| Reconnection Strategy | Retry strategy in case of connectivity errors. | 

| Type | Array of  | 

MCP:CONNECTIVITY

MCP:INTERNAL_ERROR

MCP:INVALID_PARAMS

MCP:INVALID_REQUEST

MCP:JSON_RPC_ERROR

MCP:METHOD_NOT_FOUND

MCP:PARSE_ERROR

MCP:REQUEST_TIMEOUT

MCP:RETRY_EXHAUSTED

MCP:SCHEMA_VALIDATION_FAILED

MCP:SERVER_ERROR

MCP:UNAUTHORIZED

`<mcp:ping>`

Pings the remote server.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Configuration | String | Name of the configuration to use. | Yes | |
| Config Ref | ConfigurationProvider | Name of the configuration to use to execute this component. | Yes | |
| Error Mappings | Array of  | Set of error mappings. | ||
| Reconnection Strategy | Retry strategy in case of connectivity errors. | 

| 
 | Any | 
| 
 | Any | 

MCP:CONNECTIVITY

MCP:RETRY_EXHAUSTED

`<mcp:read-resource>`

Reads a resource referenced by its URI.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Configuration | String | Name of the configuration to use. | Yes | |
| Uri | String | Yes | ||
| Config Ref | ConfigurationProvider | Name of the configuration to use to execute this component. | Yes | |
| Additional Properties | Object | #[null] | ||
| Target Variable | String | Name of the variable that stores the operation’s output. | ||
| Target Value | String | Expression that evaluates the operation’s output. The outcome of the expression is stored in the  | #[payload] | |
| Error Mappings | Array of  | Set of error mappings. | ||
| Reconnection Strategy | Retry strategy in case of connectivity errors. | 

| Type | |
| Attributes Type | Any | 

MCP:CONNECTIVITY

MCP:INTERNAL_ERROR

MCP:INVALID_PARAMS

MCP:INVALID_REQUEST

MCP:INVALID_URI

MCP:JSON_RPC_ERROR

MCP:METHOD_NOT_FOUND

MCP:PARSE_ERROR

MCP:REQUEST_TIMEOUT

MCP:RETRY_EXHAUSTED

MCP:SCHEMA_VALIDATION_FAILED

MCP:SERVER_ERROR

MCP:UNAUTHORIZED

`<mcp:create-elicitation>`

Requests an elicitation from the MCP Client. This operation sends an elicitation request via SSE and blocks until the response is received. In clustered environments, the elicitation response might arrive on a different worker, in which case it is stored in Object Store and polled.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Configuration | String | Name of the configuration to use. | Yes | |
| Session Id | String | Session identifier for the connected MCP client. | Yes | |
| Message | String | Prompt message shown to the client. | Yes | |
| Schema Properties | Input schema presented to the client for elicitation. | |||
| Config Ref | ConfigurationProvider | Name of the configuration to use to execute this component. | Yes | |
| Target Variable | String | Name of the variable that stores the operation’s output. | ||
| Target Value | String | Expression that evaluates the operation’s output. The outcome of the expression is stored in the  | #[payload] | |
| Error Mappings | Array of  | Set of error mappings. | 

| Type | 

MCP:INTERNAL_ERROR

MCP:INVALID_PARAMS

MCP:INVALID_REQUEST

MCP:JSON_RPC_ERROR

MCP:METHOD_NOT_FOUND

MCP:PARSE_ERROR

MCP:REQUEST_TIMEOUT

MCP:SCHEMA_VALIDATION_FAILED

MCP:SERVER_ERROR

MCP:UNAUTHORIZED

`<mcp:elicitation-listener>`

Listens for elicitation requests from MCP servers. When a server requires additional information during tool or resource execution, this source triggers a flow to collect that data and return it to the server. The triggered flow receives `ElicitationAttributes` containing the prompt and input schema, and must return an `ElicitationResponse` object specifying the action to take.

To accept with content:

```
<ee:transform>
  <ee:message>
    <ee:set-payload><![CDATA[
      %dw 2.0
      output application/java
      ---
      {
        action: "ACCEPT",
        content: {
          firstName: "John",
          lastName: "Doe"
        } as Object {class: "com.mulesoft.connectors.mcp.api.elicitation.ElicitationResponse"}
      }
    ]]></ee:set-payload>
  </ee:message>
</ee:transform>
```
To decline:

`<set-variable name="response" value="#[output application/java --- { action: 'DECLINE' as Object {class: 'com.mulesoft.connectors.mcp.api.elicitation.ElicitationResponse'} }]" />`To cancel:

`<set-variable name="response" value="#[output application/java --- { action: 'CANCEL' as Object {class: 'com.mulesoft.connectors.mcp.api.elicitation.ElicitationResponse'} }]" />`| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Configuration | String | Name of the configuration to use. | Yes | |
| Primary Node Only | Boolean | Determines whether to execute this source on only the primary node when running Mule instances in a cluster. | ||
| Config Ref | ConfigurationProvider | Name of the configuration to use to execute this component. | Yes | |
| Redelivery Policy | Defines a policy for processing the redelivery of the same message. | |||
| Reconnection Strategy | Retry strategy in case of connectivity errors. | |||
| Response | Elicitation response to send back to the server. | 

| Type | Object | 
| Attributes Type | 

`<mcp:on-new-session-listener>`

Triggers a flow when a new MCP client session is initiated. For each session connection request, the flow runs to let you review session details, validate client certificates, or apply custom authentication logic before choosing to accept or reject the session. When triggered, the flow receives a message with the session ID, relevant properties (including any custom headers), and client certificate information if present. To accept the session, let the flow complete successfully. To reject it, set the rejection parameters with your chosen error message, HTTP status code, and headers.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Configuration | String | Name of the configuration to use. | Yes | |
| Primary Node Only | Boolean | Determines whether to execute this source on only the primary node when running Mule instances in a cluster. | ||
| Config Ref | ConfigurationProvider | Name of the configuration to use to execute this component. | Yes | |
| Redelivery Policy | Defines a policy for processing the redelivery of the same message. | |||
| Reconnection Strategy | A retry strategy in case of connectivity errors | |||
| Reject With Status Code | Number | |||
| Reject With Message | String | |||
| Reject With Headers | Object | 

| Type | 

`<mcp:prompt-listener>`

Exposes a prompt whose messages are generated by the execution of the owning flow. The flow is executed for every received `prompts/get` request. When triggered, the flow runs with a message whose payload contains the prompt name and the arguments supplied by the client. The messages returned to the client are produced by the `<mcp:prompt-messages>` nested component.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Configuration | String | Name of the configuration to use. | Yes | |
| Name | String | The prompt name. This value is what clients use to request the prompt. | Yes | |
| Title | String | A short, human-friendly prompt title. | ||
| Description | String | A detailed enough description for an LLM to determine when this prompt should be used. | ||
| Prompt Arguments | Array of  | Prompt argument definitions exposed in  | ||
| Primary Node Only | Boolean | Determines whether to execute this source only on the primary node when running Mule instances in a cluster. | ||
| Config Ref | ConfigurationProvider | Name of the configuration to use to execute this component. | Yes | |
| Redelivery Policy | Defines a policy for processing the redelivery of the same message. | |||
| Reconnection Strategy | Retry strategy in case of connectivity errors. | |||
| Prompt Messages | Defines the prompt messages returned to the client. These parameters are evaluated when the flow finishes successfully (when the payload and variables are available). | Yes | 

| Type | |
| Attributes Type | 

`<mcp:resource-listener>`

Exposes a resource whose content is generated by the execution of the owning flow. The flow is executed for every received resources/read request. The user can choose to implement the flow so that the resource content is static or to make it dynamic. For instance, a dynamic resource could be a expenses.csv file, that is actually the result of executing a live DB query. Or a static resource could be a file obtained through Amazon S3 and locally cached using the `ee:cache` component.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Configuration | String | Name of the configuration to use. | Yes | |
| Name | String | Name of the resource. | Yes | |
| Description | String | Detailed enough description for an LLM to determine when to read this resource. | Yes | |
| Uri | String | Resource URI. | Yes | |
| Resource Mime Type | String | Resource MIME type. | Yes | |
| Primary Node Only | Boolean | Determines whether to execute this source on only the primary node when running Mule instances in a cluster. | ||
| Config Ref | ConfigurationProvider | Name of the configuration to use to execute this component. | Yes | |
| Redelivery Policy | Defines a policy for processing the redelivery of the same message. | |||
| Reconnection Strategy | Retry strategy in case of connectivity errors. | |||
| Resource Listener Content | One of: | Defines the resource content and type. These parameters are evaluated when the flow finishes successfully (when the payload and variables available). | Yes | 

| Type | |
| Attributes Type | 

`<mcp:tool-listener>`

Exposes a tool whose result is generated by the execution of the owning flow. The flow runs for every received tools/call request. When triggered, the flow runs with a message whose payload is a Java map holding the input arguments. The tool response is generated when the flow finishes either successfully or with error. In both cases, the response can include several content items of different types. If no error response is defined, then a text content item holding the error’s description is generated automatically.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Configuration | String | Name of the configuration to use. | Yes | |
| Name | String | The tool’s name. | Yes | |
| Description | String | A detailed enough description for an LLM to determine when this tool should be called. | Yes | |
| Parameters Schema | String | A JSON schema defining an object whose fields act as the tool’s input arguments. | Yes | |
| Output Schema Definition | Optional output schema definition. Choose between inline JSON schema or a file path reference. | |||
| Primary Node Only | Boolean | Determines whether to execute this source on only the primary node when running Mule instances in a cluster. | ||
| Config Ref | ConfigurationProvider | Name of the configuration to use to execute this component. | Yes | |
| Redelivery Policy | Defines a policy for processing the redelivery of the same message. | |||
| Reconnection Strategy | Retry strategy in case of connectivity errors. | |||
| Responses | Response items when the flow finishes successfully. | Yes | ||
| On Error Responses | Content items when the flow finishes in error. | 

| Type | Object | 
| Attributes Type | 

Configures TLS to provide secure communications for the Mule app.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Comma-separated list of protocols enabled for this context. | ||
| 
 | String | Comma-separated list of cipher suites enabled for this context. | ||
| 
 | Configures the TLS truststore. | |||
| 
 | Configures the TLS keystore. | |||
| 
 | Configures a revocation checking mechanism. | 

Configures the truststore for TLS.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Path to the truststore. Mule resolves the path relative to the current classpath and file system. | ||
| 
 | String | Password used to protect the truststore. | ||
| 
 | String | Type of store. | ||
| 
 | String | Encryption algorithm that the truststore uses. | ||
| 
 | Boolean | If  | 

Configures the keystore for the TLS protocol. The keystore you generate contains a private key and a public certificate.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Path to the keystore. Mule resolves the path relative to the current classpath and file system. | ||
| 
 | String | Type of store. | ||
| 
 | String | Alias of the key to use when the keystore contains multiple private keys. By default, Mule uses the first key in the file. | ||
| 
 | String | Password used to protect the private key. | ||
| 
 | String | Password used to protect the keystore. | ||
| 
 | String | Encryption algorithm that the keystore uses. | 

Configures standard revocation checks for TLS certificates.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Boolean | Which elements to verify in the certificate chain: 
 Verify only the last element in the certificate chain. 
 Verify all elements in the certificate chain. | ||
| 
 | Boolean | How to check certificate validity: 
 Check the Certification Revocation List (CRL) for certificate validity. 
 Use the Online Certificate Status Protocol (OCSP) to check certificate validity. | ||
| 
 | Boolean | Whether to use the secondary method to check certificate validity: 
 Use the method that wasn’t specified in the  
 Don’t use the secondary method to check certificate validity. | ||
| 
 | Boolean | What to do if the revocation server can’t be reached or is busy: 
 Avoid verification failure. 
 Allow the verification to fail. | 

Configures a custom OCSP responder for certification revocation checks.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | URL of the OCSP responder. | ||
| 
 | String | Alias of the signing certificate for the OCSP response. If specified, the alias must be in the truststore. | 

Specifies the location of the certification revocation list (CRL) file.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Path to the CRL file. | 

Configures a reconnection strategy for an operation.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Boolean | When the application is deployed, a connectivity test is performed on all connectors. If set to true, deployment fails if the test doesn’t pass after exhausting the associated reconnection strategy. | ||
| 
 | Reconnection strategy to use. | 

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Frequency | Number | How often in milliseconds to reconnect. | ||
| Count | Number | How many reconnection attempts to make. | ||
| blocking | Boolean | If false, the reconnection strategy runs in a separate, non-blocking thread. | true | 

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Frequency | Number | How often in milliseconds to reconnect. | ||
| blocking | Boolean | If false, the reconnection strategy runs in a separate, non-blocking thread. | true | 

Configures an expiration policy strategy.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Number | Configures the maximum amount of time that a dynamic configuration instance can remain idle before Mule considers it eligible for expiration. | ||
| 
 | Enumeration, one of: 
 | Time unit for the  | 

Attributes available in flows triggered by `Elicitation Listener`. Extends [Request Attributes](#RequestAttributes) to include elicitation-specific fields.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Session identifier for the connected MCP client. | Yes | |
| 
 | String | Unique identifier for the elicitation request. | Yes | |
| 
 | Object | Additional values attached to the request as HTTP headers. | Yes | |
| 
 | Client certificate used to authenticate the request. | No | 

Response structure for elicitation requests. This is returned by client flows handling elicitation requests from servers.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Enumeration, one of: 
 | Client response action. Valid values are: 
 | Yes | |
| 
 | Object | Response content when action is  | 

Result returned by the **Create Elicitation** operation to server flows. Contains the client’s response to an elicitation request.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Enumeration, one of: 
 | Client response action. Valid values are: 
 | Yes | |
| 
 | Object | Response content when action is  | 

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Boolean | Default value for the property. | false | |
| 
 | String | Property name. | Yes | |
| 
 | String | Property description. | ||
| 
 | Boolean | Whether the property is required. | false | 

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Object | Allowed values for the property. | Yes | |
| 
 | String | Property name. | Yes | |
| 
 | String | Property description. | ||
| 
 | Boolean | Whether the property is required. | false | 

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Number | Minimum accepted value. | ||
| 
 | Number | Maximum accepted value. | ||
| 
 | Number | Default value. | ||
| 
 | String | Property name. | Yes | |
| 
 | String | Property description. | ||
| 
 | Boolean | Whether the property is required. | false | 

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Number | Minimum accepted value. | ||
| 
 | Number | Maximum accepted value. | ||
| 
 | Number | Default value. | ||
| 
 | String | Property name. | Yes | |
| 
 | String | Property description. | ||
| 
 | Boolean | Whether the property is required. | false | 

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Number | Minimum string length. | ||
| 
 | Number | Maximum string length. | ||
| 
 | String | Validation regex pattern. | ||
| 
 | String | Default value. | ||
| 
 | String | Property name. | Yes | |
| 
 | String | Property description. | ||
| 
 | Boolean | Whether the property is required. | false | 

Response obtained from calling a tool as a client.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Array of  | The contents generated by the tool | Yes | |
| 
 | Boolean | Whether the tool execution was successful or errored out. Notice that even in case of error, contents might have been generated. | false | 

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Enumeration, one of: 
 | Content type. | Yes | |
| 
 | String | Content’s payload when type is  | ||
| 
 | String | Content’s MIME type. | ||
| 
 | Binary | Content’s payload when type is  | ||
| 
 | Content’s payload when type is  | |||
| 
 | Array of Enumeration, one of: 
 | Describes who the intended consumer of this data is. It can include multiple entries to indicate content useful for multiple audiences. | ||
| 
 | Number | Describes how important this data is for operating the server. A value of  | 

A flattened representation of a resource content. The resource can be either text or blob types. The text property is set for text resources, while the blob type is used for the latter.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Resource URI. | Yes | |
| 
 | String | Resource MIME type. | Yes | |
| 
 | String | Content of a text resource. Null for BLOB data types. | ||
| 
 | Binary | Content of a BLOB resource. Null for text data types. | 

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Enumeration, one of: 
 | |||
| 
 | String | Yes | 

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Resource URI. | Yes | |
| 
 | String | Name of the resource. | Yes | |
| 
 | String | Description of the resource. | Yes | |
| 
 | String | MIME type of the resource. | Yes | 

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Number | The amount of memory to allocate to consume the stream and provide random access to it. If the stream contains more data than can fit into this buffer, then the buffer expands according to the Buffer Size Increment value, with an upper limit of the Max In Memory Size value. instances. | 100 | |
| 
 | Number | Amount by which the buffer size expands if it exceeds its initial size. Setting a value of  | 100 | |
| 
 | Number | Maximum size of the buffer. If the buffer size exceeds this value, Mule raises a  | 

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Number | Maximum number of instances to keep in memory. If more than the maximum is required, content on the disk is buffered. | ||
| 
 | Enumeration, one of: 
 | Unit for the  | 

Describes a tool through its properties.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Name of the tool. | Yes | |
| 
 | String | A detailed enough description for an LLM to determine when to call this tool. | Yes | |
| 
 | String | JSON Schema describing the tool’s input parameters. | Yes | 

Contains the data associated to a client requiring the creation of a new server session.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Yes | ||
| 
 | Object | Yes | ||
| 
 | 

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Number | |||
| 
 | Array of String | |||
| 
 | Binary | |||
| 
 | Array of String | |||
| 
 | Array of  | |||
| 
 | Array of  | |||
| 
 | ||||
| 
 | Array of Boolean | |||
| 
 | ||||
| 
 | Array of Boolean | |||
| 
 | String | |||
| 
 | Array of String | |||
| 
 | Date | |||
| 
 | Date | |||
| 
 | ||||
| 
 | Number | |||
| 
 | ||||
| 
 | String | |||
| 
 | String | |||
| 
 | Binary | |||
| 
 | Binary | |||
| 
 | Array of  | |||
| 
 | ||||
| 
 | ||||
| 
 | String | |||
| 
 | Number | 

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Boolean | |||
| 
 | String | |||
| 
 | Binary | 

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | |||
| 
 | Number | 

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | |||
| 
 | String | 

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | 

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | |||
| 
 | Binary | |||
| 
 | Number | |||
| 
 | Number | |||
| 
 | String | 

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Number | 

Configures the redelivery policy for executing requests that generate errors. You can add a redelivery policy to any source in a flow.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Number | Maximum number of times that a redelivered request can be processed unsuccessfully before returning a REDELIVERY_EXHAUSTED error. | ||
| 
 | String | Secure hashing algorithm to use if the  | ||
| 
 | One or more expressions that determine if a message was redelivered. This property can be set only if the  | |||
| 
 | ObjectStore | Configures the object store that stores the redelivery counter for each message. | 

Configures how to identify a redelivered message and how to find out when the message was redelivered.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Boolean | If  | ||
| 
 | String | One or more expressions that determine when a message was redelivered. You can set this property only if the  | 

An inbound request for a resource, used when the connector is acting as an MCP server.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Yes | 

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Yes | ||
| 
 | String | Yes | ||
| 
 | Object | Additional values attached to the request as HTTP Headers. | Yes | |
| 
 | Client certificate used to authenticate the request. | 

Defines a text content that’s part of the response of a tool implemented through this connector.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Text content. | Yes | |
| 
 | Array of Enumeration, one of: 
 | Describes who the intended consumer of this data is. It can include multiple entries to indicate content that’s useful for multiple audiences. | ||
| 
 | Number | Describes how important this data is for operating the server. A value of  | 

Defines an image content that’s part of the response of a tool implemented through this connector.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Array of Enumeration, one of: 
 | Describes who the intended consumer of this data is. It can include multiple entries to indicate content useful for multiple audiences. | ||
| 
 | Number | Describes how important this data is for operating the server. A value of  | ||
| 
 | Binary | The raw image content, without Base64 encoding. | ||
| 
 | String | The image MIME type. | 

Defines an embedded text resource that’s part of the response of a tool implemented through this connector.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Array of Enumeration, one of: 
 | Describes who the intended consumer of this data is. It can include multiple entries to indicate content useful for multiple audiences. | ||
| 
 | Number | Describes how important this data is for operating the server. A value of  | ||
| 
 | String | Resource URI. | ||
| 
 | String | The resource MIME type. | ||
| 
 | String | Resource text. | 

Defines an embedded blob resource that’s part of the response of a tool implemented through this connector.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Array of Enumeration, one of: 
 | Describes who the intended consumer of this data is. It can include multiple entries to indicate content useful for multiple audiences. | ||
| 
 | Number | Describes how important this data is for operating the server. A value of  | ||
| 
 | Binary | The raw resource content, without Base64 encoding. | Yes | |
| 
 | String | Resource URI. | ||
| 
 | String | The resource MIME type. | 

Defines a text resource.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Text content. | Yes | 

Defines the contents of a Blob resource.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Binary | The raw blob content, without Base64 encoding. | Yes | 

Configures a custom header to be included in requests or responses.

| Name | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| Key | String | The header name. | Yes | |
| Value | String | The header value. Supports property placeholders and DataWeave expressions. | Yes | 

Attributes returned with the `CallTool` response. Use these attributes to inspect whether the remote tool returned structured content and to access the raw response.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Boolean | 
 | ||
| 
 | The full tool response returned by the server, including all content items. Useful when  | 

Response returned by `prompts/get`.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Optional description of the prompt returned by the server. | ||
| 
 | Array of  | The rendered prompt messages. | Yes | 

A single rendered prompt message.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Role associated with the message (typically  | Yes | |
| 
 | The content of the prompt message. | Yes | 

Prompt metadata returned by `prompts/list`.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Prompt name. | Yes | |
| 
 | String | Short, human-friendly title. | ||
| 
 | String | Description of the prompt. | ||
| 
 | Array of  | Argument definitions for the prompt. | 

Description of a single argument supported by a prompt on a remote MCP server.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Argument name. | Yes | |
| 
 | String | Short, human-friendly title. | ||
| 
 | String | Description of the argument. | ||
| 
 | Boolean | Whether the argument is required. | false | 

Input payload for `<mcp:prompt-listener>` flows.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | The prompt name that was requested. | Yes | |
| 
 | Object | Map of arguments provided by the client. | 

Prompt argument definition exposed in `prompts/list`.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Argument name. | Yes | |
| 
 | String | Description of the argument. | ||
| 
 | Boolean | Whether the argument is required. | false | 

Defines an inline JSON schema for the tool’s output structure. The schema content is provided directly as text.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | The JSON schema content. | Yes | 

Defines a file-based JSON schema for the tool’s output structure. The schema is loaded from a classpath resource (for example, a file under src/main/resources/ in the Mule project).

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | The path to the JSON schema file. | Yes | 

A text-based prompt message content.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | The message text. Supports DataWeave expressions. | Yes | |
| 
 | Enumeration, one of: 
 | Role associated with the message. | ||
| 
 | Array of Enumeration, one of: 
 | Describes who the intended consumer of this data is. It can include multiple entries to indicate content useful for multiple audiences. | ||
| 
 | Number | Describes how important this data is for operating the server. A value of  | 

An image-based prompt message content. Image data can be provided inline (via a DataWeave expression) or by selecting a file from the project’s classpath resources. The connector Base64-encodes the data internally.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | One of: | The image data provided either inline (base64-encoded) or as a file reference. | Yes | |
| 
 | String | The image MIME type. | Yes | |
| 
 | Enumeration, one of: 
 | Role associated with the message. | ||
| 
 | Array of Enumeration, one of: 
 | Describes who the intended consumer of this data is. It can include multiple entries to indicate content useful for multiple audiences. | ||
| 
 | Number | Describes how important this data is for operating the server. A value of  | 

An embedded resource prompt message content. The resource content (text or blob) is bundled directly inside the prompt message. Choose Text or Blob from the resource content dropdown, matching the same pattern used by the Resource Listener.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Resource URI. | Yes | |
| 
 | String | The resource MIME type. | Yes | |
| 
 | The resource content (text or blob). | Yes | ||
| 
 | Enumeration, one of: 
 | Role associated with the message. | ||
| 
 | Array of Enumeration, one of: 
 | Describes who the intended consumer of this data is. It can include multiple entries to indicate content useful for multiple audiences. | ||
| 
 | Number | Describes how important this data is for operating the server. A value of  | 

A resource link prompt message content that references an external resource by URI.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Resource URI. | Yes | |
| 
 | String | Name of the linked resource. | ||
| 
 | String | Human-friendly title. | ||
| 
 | String | Description. | ||
| 
 | String | MIME type of the linked resource. | ||
| 
 | Number | Size of the linked resource. | ||
| 
 | Enumeration, one of: 
 | Role associated with the message. | ||
| 
 | Array of Enumeration, one of: 
 | Describes who the intended consumer of this data is. It can include multiple entries to indicate content useful for multiple audiences. | ||
| 
 | Number | Describes how important this data is for operating the server. A value of  | 

Text-based embedded resource.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | The text content. | Yes | 

Binary embedded resource.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Binary | The raw blob content, without Base64 encoding. | Yes | 

Provides image data inline via a DataWeave expression that resolves to binary content. The connector Base64-encodes the data internally before sending it over MCP.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | Binary | The image data. | Yes | 

Provides image data by referencing a file in the project’s classpath resources. The connector reads and Base64-encodes the file content at runtime before sending it over MCP.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | The path to the image file. | Yes | 

Text content in a prompt response.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | The text content. | Yes | 

Image content in a prompt response. The data is the raw image bytes (already decoded from Base64).

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | The image MIME type. | Yes | |
| 
 | Binary | The image data. | Yes | 

Embedded resource content in a prompt response. The resource content (text or blob) is bundled directly inside the prompt message.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | The embedded resource payload. | Yes | 

Resource link content in a prompt response. References an external resource by URI.

| Field | Type | Description | Default Value | Required | 
|---|---|---|---|---|
| 
 | String | Resource URI. | Yes | |
| 
 | String | Name of the linked resource. | ||
| 
 | String | Human-friendly title. | ||
| 
 | String | Description. | ||
| 
 | String | MIME type of the linked resource. | ||
| 
 | Number | Size of the linked resource. | 

[MuleSoft Help Center](https://help.mulesoft.com)