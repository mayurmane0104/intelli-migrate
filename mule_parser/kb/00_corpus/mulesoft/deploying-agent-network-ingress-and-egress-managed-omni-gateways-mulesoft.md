# Deploying Agent Network Ingress and Egress Managed Omni Gateways | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/gateway/latest/flex-gateway-managed-ingress-egress](https://docs.mulesoft.com/gateway/latest/flex-gateway-managed-ingress-egress)

---

![Agent Network showing agents and MCP servers defined in YAML and published to Exchange, with traffic through Omni Gateway, governed by API Manager, and observed in Monitoring and Visualizer](_images/agent-fabric-architecture.png) 

# Deploying Agent Network Ingress and Egress Managed Omni Gateways

Agent Network deployments require both an ingress and egress Omni Gateway. The ingress Omni Gateway sits in front of broker and API endpoints to manage and enforce policies on traffic entering the network. The egress Omni Gateway sits on outbound paths from brokers and agents to external agents and enforces policies, manages connections, and emits telemetry data.

The only functional difference between ingress and egress Omni Gateways, is that the egress Gateway doesn’t have a public endpoint. Only clients inside the same private space as the egress gateway can make requests to it. Traffic leaving the private space to external services passes through the egress gateway.

![Agent Network showing agents and MCP servers defined in YAML and published to Exchange, with traffic through Omni Gateway, governed by API Manager, and observed in Monitoring and Visualizer](_images/agent-fabric-architecture.png) 

| For a more detailed description of this architecture diagram, see [Agent Network Architecture](../../anypoint-code-builder/af-agent-networks#agent-network-architecture). | 

## Deploy Ingress and Egress Managed Omni Gateways

The easiest way to deploy your Agent Network ingress and egress Omni Gateways is by using Anypoint Code Builder or Anypoint Command Line Interface (CLI):

To manually deploy both ingress and egress managed Omni Gateways using the Runtime Manager UI, see [Deploy a Managed Omni Gateway](flex-gateway-managed-set-up).

For ingress gateways, configure a **Public endpoint** in the advanced options **Ingress** tab. For egress gateways, verify that there’s no **Public endpoint** configured. To prevent confusion, give a descriptive name defining the gateway as either ingress or egress.

## Apply Inbound and Outbound Policies

Inbound policies are policies that are enforced on all traffic accessing an instance’s endpoint. Outbound policies are policies that are enforced on all traffic accessing a specific URL and are only applied to that URL. For example, for an agent instance that has multiple upstreams, an inbound client ID enforcement policy enforces client ID verification for all traffic accessing the agent instance. However, an outbound policy might be applied to only one of the instance’s upstream.