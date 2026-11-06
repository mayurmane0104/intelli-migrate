# https://docs.mulesoft.com/monitoring/anypoint-insights-agentic.md

**Source:** [https://docs.mulesoft.com/monitoring/anypoint-insights-agentic.md](https://docs.mulesoft.com/monitoring/anypoint-insights-agentic.md)

---

```
# Monitoring Agentic Assets
> For the full documentation index, see: https://docs.mulesoft.com/llms.txt
In US and EU Cloud instances of Anypoint Platform, navigate from Agent Visualizer to view detailed
metrics on agentic assets (agent, broker, or MCP server instances).
- Agent: An autonomous software component that uses goals, context, and available tools (often via
  an LLM) to decide and execute actions on behalf of a user or system.
- Broker: An intelligent routing service that coordinates task delegation across specialized agents
  in your enterprise. Brokers originate from MuleSoft and are referenced in the agent network YAML.
- MCP server: A service that implements the Model Context Protocol to expose tools and data to AI
  clients, enabling LLMs to invoke external capabilities through a standard interface.
This example shows metrics for an instance of an agent.
![Metrics for an instance of an agent in Anypoint Monitoring](_images/metrics-agent.png)
<table><tbody><tr><td><i data-value="1"></i><b>1</b></td><td>Name of the instance</td></tr><tr><td><i data-value="2"></i><b>2</b></td><td><a href="#properties">Properties of the instance</a> that correspond to properties in API Manager</td></tr><tr><td><i data-value="3"></i><b>3</b></td><td><a href="#agent">Agent metrics</a></td></tr><tr><td><i data-value="4"></i><b>4</b></td><td>Lookback period selected for the agent</td></tr><tr><td><i data-value="5"></i><b>5</b></td><td><a href="#refresh">Auto-refresh</a> (subscription tier requirement)</td></tr><tr><td><i data-value="6"></i><b>6</b></td><td>Manual refresh option</td></tr></tbody></table>
For information about Agent Visualizer, see [Agent Visualizer Overview](../agent-visualizer/).
## Find Metrics for Agentic Assets
Agent Visualizer links to metrics for agentic assets (agent, broker, and MCP server instances) from
nodes in the visualizer graph.
1.  In Agent Visualizer, click a node to open its detail card.
2.  In **Performance and Health**, click **View Metrics** to view additional metrics in Anypoint
    Monitoring.
    1.  Optionally, set the lookback period ([see 4](#dashboard-overview)) to different range.
        Defaults to the last 24 hours. Select a period from the last 30 minutes to the last 30 days.
    2.  Review [properties](#properties) and metrics for the [agent](#agent), [broker](#broker), or
        [MCP server](#mcp-server) instance.
For more information about nodes in Agent Visualizer, see
[Agent Visualizer Overview](../agent-visualizer/).
## Instance Properties
Agent, broker, and MCP server pages display these properties:
- **Instance ID**: Unique identifier that API Manager generates for the instance
- **Instance Label**: Unique identifier configured in API Manager as an optional instance property
  that distinguishes one instance from another instance of the same API
- **Status**: **Active**, **Inactive**, or **Unregistered** status for the instance
  For more detail, see
  [Tracking Registration Status](../api-manager/latest/latest-overview-concept#tracking-registration-status)
  in the API Manager documentation.
  Applies to agents, brokers, and MCP servers
- **Asset Version**: Version of the asset (in [Anypoint Exchange](../exchange/asset-versions)) that
  the instance implements
  Examples: **1.0.0 (Latest)**, **1.0.2**
- **Implementation URI**: Upstream URI for the backend
- **Type**: An **Agent**, **Broker**, or **MCP Server** instance type
## Agent Metrics
Agents protected by a the
[A2A Agent Card Policy](../gateway/latest/policies-included-a2a-agent-card) policy produce metrics
in these charts:
- **Total Received**: All requests to the agent
- **Failed Requests**: Number of requests to the agent that failed
- **Failed Request Rate**: Percentage of requests to the agent that failed
The agentâ€™s Omni Gateway (formerly Flex Gateway) ingress supports request counts. The charts reflect
calls to the agent through that ingress.
## Broker Metrics
Metrics reported for brokers appear in these charts:
- **Requests Received**:
  - **Total Received**: Number of requests to the broker
  - **Failed Requests**: Number of requests to the broker that failed
  - **Failed Request Rate**: Percentage of requests to the broker that failed
## MCP Server Metrics
MCP servers protected by an Omni Gateway (formerly Flex Gateway) ingress policy
([MCP Support](../gateway-home/#policy-availability-by-gateway)) produce metrics in these charts:
- **Total Received**: All requests to the MCP server
- **Failed Requests**: Number of requests to the MCP server that failed
- **Failed Request Rate**: Percentage of requests to the MCP server that failed
The MCP serverâ€™s Omni Gateway (formerly Flex Gateway) ingress supports request counts. The charts
reflect calls to the MCP server through that ingress.
## Refresh Metrics
Refresh metrics in either of these ways:
- Manual refresh is available to all subscription levels.
- Auto refresh is available to Advanced and Titanium subscriptions.
  Refresh cycles range from every 5 minutes to one time per day.
```