# Monitoring Agentic Assets | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/monitoring/anypoint-insights-agentic](https://docs.mulesoft.com/monitoring/anypoint-insights-agentic)

---

![Metrics for an instance of an agent in Anypoint Monitoring](_images/metrics-agent.png) 

# Monitoring Agentic Assets

In US and EU Cloud instances of Anypoint Platform, navigate from Agent Visualizer to view detailed metrics on agentic assets (agent, broker, or MCP server instances).

- 
Agent: An autonomous software component that uses goals, context, and available tools (often via an LLM) to decide and execute actions on behalf of a user or system. 
- 
Broker: An intelligent routing service that coordinates task delegation across specialized agents in your enterprise. Brokers originate from MuleSoft and are referenced in the agent network YAML. 
- 
MCP server: A service that implements the Model Context Protocol to expose tools and data to AI clients, enabling LLMs to invoke external capabilities through a standard interface. 

This example shows metrics for an instance of an agent.

![Metrics for an instance of an agent in Anypoint Monitoring](_images/metrics-agent.png) 

| 1 | Name of the instance | 
| 2 | [Properties of the instance](#properties)that correspond to properties in API Manager | 
| 3 | [Agent metrics](#agent) | 
| 4 | Lookback period selected for the agent | 
| 5 | [Auto-refresh](#refresh)(subscription tier requirement) | 
| 6 | Manual refresh option | 

For information about Agent Visualizer, see [Agent Visualizer Overview](../agent-visualizer/).

## Find Metrics for Agentic Assets

Agent Visualizer links to metrics for agentic assets (agent, broker, and MCP server instances) from nodes in the visualizer graph.

- 
In Agent Visualizer, click a node to open its detail card. 
- 
In **Performance and Health**, click**View Metrics**to view additional metrics in Anypoint Monitoring.- 
Optionally, set the lookback period ( [see 4](#dashboard-overview)) to different range.Defaults to the last 24 hours. Select a period from the last 30 minutes to the last 30 days. 
- 
Review [properties](#properties)and metrics for the[agent](#agent),[broker](#broker), or[MCP server](#mcp-server)instance.
 
- 

For more information about nodes in Agent Visualizer, see [Agent Visualizer Overview](../agent-visualizer/).

## Instance Properties

Agent, broker, and MCP server pages display these properties:

- 
**Instance ID**: Unique identifier that API Manager generates for the instance

- 
**Instance Label**: Unique identifier configured in API Manager as an optional instance property that distinguishes one instance from another instance of the same API

- 
**Status**:**Active**,**Inactive**, or**Unregistered**status for the instanceFor more detail, see [Tracking Registration Status](../api-manager/latest/latest-overview-concept#tracking-registration-status)in the API Manager documentation.Applies to agents, brokers, and MCP servers 

- 
**Asset Version**: Version of the asset (in[Anypoint Exchange](../exchange/asset-versions)) that the instance implementsExamples: **1.0.0 (Latest)**,**1.0.2**

- 
**Implementation URI**: Upstream URI for the backend

- 
**Type**: An**Agent**,**Broker**, or**MCP Server**instance type

## Agent Metrics

Agents protected by a the [A2A Agent Card Policy](../gateway/latest/policies-included-a2a-agent-card) policy produce metrics in these charts:

- 
**Total Received**: All requests to the agent
- 
**Failed Requests**: Number of requests to the agent that failed
- 
**Failed Request Rate**: Percentage of requests to the agent that failed

The agent’s Omni Gateway (formerly Flex Gateway) ingress supports request counts. The charts reflect calls to the agent through that ingress.

## Broker Metrics

Metrics reported for brokers appear in these charts:

- 
**Requests Received**:- 
**Total Received**: Number of requests to the broker
- 
**Failed Requests**: Number of requests to the broker that failed
- 
**Failed Request Rate**: Percentage of requests to the broker that failed
 
- 

## MCP Server Metrics

MCP servers protected by an Omni Gateway (formerly Flex Gateway) ingress policy ([MCP Support](../gateway-home/#policy-availability-by-gateway)) produce metrics in these charts:

- 
**Total Received**: All requests to the MCP server
- 
**Failed Requests**: Number of requests to the MCP server that failed
- 
**Failed Request Rate**: Percentage of requests to the MCP server that failed

The MCP server’s Omni Gateway (formerly Flex Gateway) ingress supports request counts. The charts reflect calls to the MCP server through that ingress.

## Refresh Metrics

Refresh metrics in either of these ways:

- 
Manual refresh is available to all subscription levels. 
- 
Auto refresh is available to Advanced and Titanium subscriptions. Refresh cycles range from every 5 minutes to one time per day.