# Deploy Agent Network Instances | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/af-deploy-agent-network-targets](https://docs.mulesoft.com/anypoint-code-builder/af-deploy-agent-network-targets)

---

- 
A2A Agent Card policy 
- 
Tracing policy 
- 
Agent Connection Telemetry policy 

# Deploy Agent Network Instances

Deploy your agent network instance to a deployment target. You can deploy to a CloudHub 2.0 private space or to a Runtime Fabric. When you deploy, Omni Gateway secures your agent network in the ingress gateway. Also, it secures your brokers, agents, and MCP servers in the egress gateway.

These Omni Gateway policies are applied automatically at deployment.

| Agent Type | Policy | 
|---|---|
| Broker | |
| Agent (ingress and egress) | 
 | 
| MCP Server (ingress and egress) | 
 | 

## Before You Begin

Make sure you review the [prerequisites](af-get-started#before-you-begin).

When you deploy your agent network, an instance is deployed for each connection defined in your agent network. If your agent network contains brokers, an instance is deployed per broker.

## Deploy Your Network Using MuleSoft Vibes

MuleSoft Vibes can help you deploy your agent network instances. For more information, see [Creating API Specs with MuleSoft Vibes](vibes-api-ai-create-spec).

- 
In the Anypoint Code Builder activity bar, click the agent icon ![](_images/af-acb-dev-agent-icon.png) . .
- 
Tell the agent that you want to deploy your agent network. MuleSoft Vibes does the rest. 

To get started, try one of these suggested messages.

- 
Deploy my agent network project to the production environment. 
- 
Deploy the hello-world-network project to staging. 
- 
Deploy agent network project at /path/to/project to dev environment with specific gateways. 
- 
Deploy my agent network to CloudHub 2.0. 

## Deploy Your Network Using Anypoint Code Builder

- 
If you’re not logged in already, log in to your Anypoint Platform account. 
- 
In Anypoint Code Builder, choose one of the following: 
- 
In Explorer, right-click a project file and select **Deploy Agent Network**.
- 
From the Command Palette, run this command: **MuleSoft: Deploy Agent Network**.
- 
In Deploy Agent Network, specify the environment, target space, gateways, and other deployment information. If you don’t see any deployment targets to select, then you need to set up your target deployment space and set up gateways. For instructions, see [Get Started with Agent Networks](af-get-started).
- 
Select **Deploy**.
- 
Your instances are deployed and ready to be tested. An instance is deployed for each connection defined in your agent network. If your agent network contains brokers, one instance is deployed per broker. 

Next, discover your agent network assets in **Agents & Tools** in Exchange, view your agent network in Agent Visualizer, apply a governance policy in API Manager, or monitor your agent network activity in Anypoint Monitoring.

## Deploy a Network Using the Anypoint CLI

If you run operations within a CI/CD environment, you can use Anypoint CLI’s plugin to set up, create, build, publish, and deploy agent networks. For more information, see [Build Agent Networks in a CI/CD Environment](af-build-agent-networks-in-a-ci-cd-environment).