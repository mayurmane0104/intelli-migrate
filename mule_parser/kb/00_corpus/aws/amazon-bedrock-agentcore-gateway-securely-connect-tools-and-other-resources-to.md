# Amazon Bedrock AgentCore Gateway: Securely connect tools and other resources to your Gateway - Amazon Bedrock AgentCore

**Source:** [https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)

---

Amazon Bedrock AgentCore Gateway provides an easy and secure way for developers to build, deploy, discover, and connect to tools at scale. AI agents need tools to perform real-world tasks—from querying databases to sending messages to analyzing documents. With Gateway, developers can convert APIs, Lambda functions, and existing services into Model Context Protocol (MCP)-compatible tools and make them available to agents through Gateway endpoints with just a few lines of code. Gateway supports OpenAPI, Smithy, and Lambda as input types, and is the only solution that provides both comprehensive ingress authentication and egress authentication in a fully-managed service. Gateway also provides 1-click integration with several popular tools such as Salesforce, Slack, Jira, Asana, and Zendesk. Gateway eliminates weeks of custom code development, infrastructure provisioning, and security implementation so developers can focus on building innovative agent applications.

###### Topics

## Key benefits

      - 
               **Simplify tool development and integration**
- 
               Transform existing enterprise resources into agent-ready tools in just a few lines of code. Instead of spending months writing custom integration code and managing infrastructure, developers can focus on building differentiated agent capabilities while Gateway handles the undifferentiated heavy lifting of tool management and security at enterprise scale. Gateway also provides 1-click integration with several popular tools such as Salesforce, Slack, Jira, Asana, and Zendesk. 
- 
               **Accelerate agent development through unified access**
- 
               Enable your agents to discover and use tools through a single, secure endpoint. By combining multiple tool sources—from APIs to Lambda functions—into one unified interface, developers can build and scale agent workflows faster without managing multiple tool connections or reimplementing integrations. 
- 
               **Scale with confidence through intelligent tool discovery**
- 
               As your tool collection grows, help your agents find and use the right tools through contextual search. Built-in semantic search capabilities help agents effectively utilize available tools based on their task context, improving agent performance and reducing development complexity at scale. 
- 
               **Comprehensive authentication**
- 
               Manage both inbound authentication (verifying agent identity) and outbound authentication (connecting to tools) in a single service. Handle OAuth flows, token refresh, and secure credential storage for third-party services. 
- 
               **Framework compatibility**
- 
               Work with popular open-source frameworks including CrewAI, LangGraph, LlamaIndex, and Strands Agents. Integrate with any model while maintaining enterprise-grade security and reliability. 
- 
               **Serverless infrastructure**
- 
               Eliminate infrastructure management with a fully managed service that automatically scales based on demand. Built-in observability and auditing capabilities simplify monitoring and troubleshooting. 

## Key capabilities

      Gateway provides the following key capabilities:

- 
            **Security Guard**- Manages OAuth authorization to ensure only valid users and agents can access tools and resources.
- 
            **Translation**- Converts agent requests using protocols like Model Context Protocol (MCP) into API requests and Lambda invocations, eliminating the need to manage protocol integration or version support.
- 
            **Composition**- Combines multiple APIs, functions, and tools into a single MCP endpoint for streamlined agent access.
- 
            **Secure Credential Exchange**- Handles credential injection for each tool, enabling agents to use tools with different authentication requirements seamlessly.
- 
            **Semantic Tool Selection**- Enables agents to search across available tools to find the most appropriate ones for specific contexts, allowing agents to leverage thousands of tools while minimizing prompt size and reducing latency.
- 
            **Infrastructure Manager**- Provides a serverless solution with built-in observability and auditing, eliminating infrastructure management overhead.