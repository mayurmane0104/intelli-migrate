# Host agent or tools with Amazon Bedrock AgentCore Runtime - Amazon Bedrock AgentCore

**Source:** [https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)

---

Amazon Bedrock AgentCore Runtime provides a secure, serverless and purpose-built hosting environment for deploying and running AI agents or tools. It offers the following benefits:

- Framework agnostic
- 
            AgentCore Runtime lets you transform any local agent code to cloud-native deployments with a few lines of code no matter the underlying framework. Works seamlessly with popular frameworks like LangGraph, Strands, and CrewAI. You can also leverage it with custom agents that don’t use a specific framework. 
- Model flexibility
- 
            AgentCore Runtime works with any Large Language Model, such as models offered by Amazon Bedrock, Anthropic Claude, Google Gemini, and OpenAI. 
- Protocol support
- 
            AgentCore Runtime lets agents communicate with other agents and tools via Model Context Protocol (MCP) or Agent to Agent (A2A). 
- Session isolation
- 
            In AgentCore Runtime, each user session runs in a dedicated microVM with isolated CPU, memory, and filesystem resources. This helps create complete separation between user sessions, safeguarding stateful agent reasoning processes and helps prevent cross-session data contamination. After session completion, the entire microVM is terminated and memory is sanitized, delivering deterministic security even when working with non-deterministic AI processes. 
- Extended execution time
- 
            AgentCore Runtime supports both real-time interactions and long-running workloads up to 8 hours, enabling complex agent reasoning and asynchronous workloads that may involve multi-agent collaboration or extended problem-solving sessions. 
- Persistent filesystems
- 
            Runtime supports persisting filesystem state across session stop/resume cycles. The agent’s files, installed packages, and build artifacts can survive session stops without external storage. 
- Consumption-based pricing model
- 
            Runtime implements consumption-based pricing that charges only for resources actually consumed. Unlike allocation-based models that require pre-selecting resources, Runtime dynamically provisions what’s needed without requiring right-sizing. The service aligns CPU billing with actual active processing - typically eliminating charges during I/O wait periods when agents are primarily waiting for LLM responses - while continuously maintaining your session state. 
- Built-in authentication
- 
            AgentCore Runtime, powered by AgentCore Identity, assigns distinct identities to AI agents and seamlessly integrates with your corporate identity provider such as Okta, Microsoft Entra ID, or Amazon Cognito, enabling your end users to authenticate into only the agents they have access to. In addition, Runtime lets outbound authentication flows to securely access third-party services like Slack, Zoom, and GitHub - whether operating on behalf of users or autonomously (using either OAuth or API keys). 
- Agent-specific observability
- 
            AgentCore Runtime provides specialized built-in tracing that captures agent reasoning steps, tool invocations, and model interactions, providing clear visibility into agent decision-making processes, a critical capability for debugging and auditing AI agent behaviors. 
- Enhanced payload handling
- 
            AgentCore Runtime can process 100MB payloads enabling seamless processing of multiple modalities (text, images, audio, video), with rich media content or large datasets. 
- Bidirectional streaming
- 
            AgentCore Runtime supports both HTTP API calls and persistent WebSocket connections for real-time bidirectional streaming, enabling interactive applications with immediate response feedback and maintained conversation context. 
- Unified set of agent-specific capabilities
- 
            AgentCore Runtime is delivered through a single, comprehensive SDK that provides streamlined access to the complete AgentCore capabilities including Memory, Tools, and Gateway. This integrated approach eliminates the integration work typically required when building equivalent agent infrastructure from disparate components.