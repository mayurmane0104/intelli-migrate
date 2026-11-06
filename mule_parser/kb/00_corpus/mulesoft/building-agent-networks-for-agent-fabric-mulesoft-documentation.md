# Building Agent Networks for Agent Fabric | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/af-agent-networks](https://docs.mulesoft.com/anypoint-code-builder/af-agent-networks)

---

![Anypoint Code Builder canvas showing brokers, agents, and MCP servers](_images/af-agent-network-canvas.png) 

# Building Agent Networks for Agent Fabric

An agent network is a coordinated group of agents, brokers, LLMs, and MCP servers that acts as a central hub for defining, validating, and executing agentic processes across your enterprise.

An agent network provides the building blocks of your agentic deployment while MuleSoft Agent Fabric helps you maximize the potential of every AI agent with centralized discovery, orchestration across agents and tools, cross-ecosystem governance, and full transparency into agentic interactions.

You define your agent network in a simple, human-readable YAML file in Anypoint Code Builder. This approach abstracts away the underlying technical complexities, allowing you to focus on the business constraints and context of your process without needing to understand the inner workings of the orchestration engine.

At the start of a new agent network project, we provide a YAML template to give you a head start. You can use MuleSoft Vibes to configure your network, publish the assets to Anypoint Exchange, and deploy your agent network instance.

## Key Benefits of Agent Networks

Create robust, automated agent networks with these key benefits.

- 
Simplified Development Define your agent processes in an intentional way using a simple YAML file, which is easier and faster than writing complex code. 
- 
Safety and Governance Ensure control and compliance across every agent and tool interaction with enterprise-grade governance. 
- 
Observability Gain insight into agent actions with a visual trace of their decision-making. 
- 
Flexibility Coordinate any type of agent and tool, regardless of where it’s built and deployed so you can build a diverse network of agents. 
- 
Tool and Agent Invocation Manage the invocation of both deterministic (tool-based) and probabilistic (LLM-based) actions. 

## Example Use Case: Employee Onboarding

In this example, the goal is to seamlessly activate a new hire across HR, IT, Security, and Facilities with a single, policy‑governed experience.

Here’s how it works:

- 
Discover Publish existing agents and tools (HRIS, Identity, ITSM, Payroll, Facilities, LMS) in Anypoint Exchange for reuse. 
- 
Orchestrate An agent broker decomposes the task of onboarding the new hire (create HR record, provision identity, assign hardware, grant app access, enroll in benefits and training), calling MCP and A2A agents as needed, with human‑in‑the‑loop approvals where required. 
- 
Govern Omni Gateway enforces authentication, least‑privilege access, and guardrails. API Manager policies ensure consistent controls across all calls and data exchanges. 
- 
Observe Monitoring and traces (beta) give end‑to‑end visibility into progress, failures, and latency. Visualization shows which agents interacted and where bottlenecks occurred. 
- 
Reuse The onboarding definition (YAML) is versioned and shareable, enabling rapid adaptation for roles, regions, or subsidiaries without rebuilding flows. 
- 
Trust and Compliance Centralized credentials, audit trails, and policy inheritance support security, privacy, and regulatory requirements (PII handling, approvals, and separation of duties). 

With this experience, you get faster time‑to‑productivity, fewer handoffs, lower error rates, and a consistent new‑hire experience across the enterprise.

## Agent Network Components

An agent network is a collection of agents, brokers, LLMs, and MCP servers that are connected to each other. Agent networks use LLMs for reasoning and planning capabilities and integrate with Anypoint Connector for MCP (Model Context Protocol) and Anypoint Connector for Agent2Agent (A2A) communication.

- Broker
- 
An intelligent routing service that coordinates task delegation across specialized A2A-compliant agents in your enterprise. A broker is defined by the agents and MCP servers it can leverage to accomplish tasks. Brokers originate from MuleSoft and are referenced in the agent network YAML. After you publish your agent network, brokers appear as specialized agents in Anypoint Exchange and can be reused by other brokers. 
- Agent
- 
An autonomous software component that uses goals, context, and available tools, often via a large language model (LLM), to decide and execute actions on behalf of a user or system. Agents can be defined either locally in the agent network or externally in a different agent network or elsewhere in your company. Your agent network can use both locally defined and externally defined agents to complete tasks. Agent assets must be A2A-compliant. 
- MCP server
- 
A service that implements the Model Context Protocol (MCP) to expose tools and data to AI clients, enabling LLMs to invoke external capabilities through a standard interface. MCP servers can be defined either locally in the agent network or externally in a different agent network or elsewhere in your company. Your agent network can use both locally defined and externally defined MCP servers to complete tasks. 

### Agent Networks in Anypoint Code Builder

When you create agent networks, the Anypoint Code Builder canvas shows the brokers, agents, and MCP servers you’ve configured.

![Anypoint Code Builder canvas showing brokers, agents, and MCP servers](_images/af-agent-network-canvas.png) 

| 1 | The Brokerscomponent groups brokers defined locally in your agent network YAML.
It can include assets defined locally within the project and assets previously published to Anypoint Exchange, either by your organization or third parties.Brokers can reference other brokers defined within the project. Agent network projects don’t require brokers. They can contain only agents and MCP servers defined within the agent network project. | 
| 2 | The Agentscomponent groups agents defined locally in your agent network YAML.These agents will be published to Exchange. | 
| 3 | The MCP Serverscomponent groups MCP servers defined locally in your agent network YAML.These servers will be published to Exchange. | 
| 4 | An asset that has been defined within this agent network project. The asset might also be published to Exchange. | 
| 5 | An asset that has been added to this agent network project from Exchange. | 

## Agent Network Architecture

This diagram shows an agent network with agents and MCP servers, traffic through Omni Gateway, governed by API Manager, and observed in Anypoint Monitoring and Agent Visualizer.

![Agent Fabric showing agents and MCP servers defined in YAML and published to Exchange](_images/agent-fabric-architecture.png) 

| 1 | Publish the agentic assets to Anypoint Exchange for discovery and reuse after you define the agent network (brokers, agents, MCP servers) in the agent network YAML in Anypoint Code Builder. | 
| 2 | Deploy the agentic assets to CloudHub 2.0 (managed in Runtime Manager). | 
| 3 | Enforce policies on incoming traffic to the network with an ingress Omni Gateway, which sits in front of brokers and API endpoints. | 
| 4 | Enforce policies, manage connections, and emit telemetry data with an egress Omni Gateway, which sits on outbound paths from brokers and agents to external agents and services. | 
| 5 | Collect logs, metrics, and traces from Omni Gateway and runtimes in Anypoint Monitoring. | 

## Large Language Models

Agent network brokers support the latest Gemini and OpenAI models and LLM Proxies.

- 
Azure OpenAI and OpenAI API: - 
GPT-5.2 
- 
GPT-5.2 Pro 
- 
GPT-5-mini 
- 
GPT-5 nano 
- 
GPT-5 For more information about these models, see the [OpenAI](https://developers.openai.com/api/docs/models)documentation.
 
- 
- 
Gemini API: - 
Gemini 2.5 Pro 
- 
Gemini 2.5 Flash-Lite 
- 
Gemini 2.5 Flash 
- 
Gemini 3 Flash 
- 
Gemini 3 Pro For more information about these models, see the [Gemini](https://ai.google.dev/gemini-api/docs/models)documentation.
 
- 
- 
LLM Proxy: LLM Proxy provides a unified endpoint for multiple LLM providers including Gemini, OpenAI, Bedrock (Anthropic Claude models), and NVIDIA Nemotron. To find the supported models, see [LLM Proxy Supported LLM Providers](../gateway/latest/flex-gateway-llm-proxy#supported-llm-providers).

This table details the requirements and recommended models.

| Model Provider | Required Endpoint | Required Capabilities | Suggested Models | 
|---|---|---|---|
| OpenAI | 
 | 
 | 
 | 
| Gemini | 
 | 
 | 
 | 

Agent networks support text-based messages and responses. Image and binary message types aren’t supported.

## A2A Protocol

The Agent2Agent (A2A) Protocol governs agent-to-agent communication. This protocol powers orchestration, observability, and governance features in agent networks. MuleSoft supports v0.3.0 of the A2A Protocol Specification.

### Context and Task ID Scoping in Agent Networks

In MuleSoft agent networks, the brokers receiving a request always generate a `contextId` and `taskId`. These IDs define the state and scope of a specific conversation between two agents. A `taskId` is always matched to a `contextId`, but a `contextId` can exist without a `taskId`.

In a multi-agent network, a client sends a request to Broker_1 and Broker_1 generates the necessary IDs for that request. When Broker_1 sends a new request to the next broker or non-broker agent in line, that broker or non-broker agent establishes a unique `contextId` and `taskId` for the new request.

| It is not mandatory for non-broker agents to generate a `contextId`and`taskId`when receiving requests from a client. | 

Consider a network with a client and two brokers (1 and 2).

- 
The IDs used between the client and Broker_1 are independent of the IDs used between Broker_1 and Broker_2. 
- 
When Broker_1 delegates a task to Broker_2, Broker_2 (acting as a server) generates its own `contextId`and`taskId`.
- 
Broker_1 is responsible for maintaining a mapping between its own upstream `taskId`(used to respond to its client) and the downstream`taskId`it’s tracking with Broker_2.
- 
If Broker_2 requires more information (if it returns `status: input-required`), it provides a`contextId`and`taskId`to Broker_1. Broker_1 uses these IDs to provide the requested input to Broker_2. The client never sees Broker_2’s internal IDs.

| Relationship | Role | Logic | 
|---|---|---|
| Client → Broker_1 | Broker_1 is server | Generates  | 
| Agent A → Broker_2 | Broker_2 is server | Generates  | 
| Network broker | Broker_1 | Broker_1 maps  | 

For more information, see [Life of a Task - Group Related Interactions](https://a2a-protocol.org/v0.3.0/topics/life-of-a-task/#group-related-interactions).

| Agent networks don’t support streaming with Server-Sent Events (SSE). |