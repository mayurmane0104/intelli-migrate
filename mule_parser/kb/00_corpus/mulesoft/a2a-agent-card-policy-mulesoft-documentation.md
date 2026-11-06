# A2A Agent Card Policy | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/gateway/latest/policies-included-a2a-agent-card](https://docs.mulesoft.com/gateway/latest/policies-included-a2a-agent-card)

---

Consumer URL

# A2A Agent Card Policy

| 
 | A2A Agent Card | 
| 
 | Rewrites the Agent Card URL to match the public URL of the gateway | 
| 
 | A2A | 
| 
 | v1.9.3 | 
| 
 | 

| This policy supports Agent2Agent Protocol (A2A) version v0.3.0. To learn more about A2A versions, see [A2A Releases](https://github.com/a2aproject/A2A/releases). | 

## Summary

The A2A Agent Card Policy rewrites the URL in the A2A Agent Card responses so that the exposed URL points to the public endpoint of the Omni Gateway A2A server instance rather than directly to backend services. This ensures that all client requests are routed through Omni Gateway, enabling it to enforce security and access controls, while preventing direct access to backend resources.

The A2A Agent Card policy also enables the **Total Agent Calls** metric that tracks the total successful and unsuccessful calls made to the agent. To view **Total Agent Calls**, see [Viewing Key Metrics in API Manager for Managed Omni Gateway](flex-managed-view-api-metrics).

## Configuring Policy Parameters

### Omni Gateway Local Mode

The A2A Agent Card policy isn’t supported in Local Mode.

### Managed Omni Gateway and Omni Gateway Connected Mode

When you apply the policy from the UI, the following parameters are displayed:

| Element | Description | 
|---|---|
| The consumer URL of the agent’s A2A service where JSON-RPC requests are sent. | |
| Card Path | The path where the agent presents the card. |