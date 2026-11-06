# Get Started with Agent Networks | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/general/agent-networks-get-started](https://docs.mulesoft.com/general/agent-networks-get-started)

---

- 
Manage Servers 
- 
Create Applications 
- 
Read Servers 

# Get Started with Agent Networks

Creating agent networks is a multi-step process. Review these prerequisites and task overviews to make sure you can create agent networks efficiently.

## Before You Begin

Before you get started, review these prerequisites.

### Anypoint Platform Requirements and Permissions

| Anypoint Platform Component | Required Permissions | 
|---|---|
| Runtime Manager | |
| Anypoint Code Builder | 
 | 
| Anypoint Design Center | Design Center Developer | 
| API Manager | 
 | 
| Exchange | Exchange Contributor | 
| Usage | Usage Viewer | 
| CloudHub 2.0 or Runtime Fabric | 

See [Permissions by Product in Anypoint Platform](../access-management/permissions-by-product) for a list of all Anypoint Platform permissions.

### Additional Requirements

To complete these tasks, you also need:

- 
Your Anypoint Platform credentials 
- 
Allowlist Anypoint Code Builder URLs. For more information, see [Allow URLs for Anypoint Code Builder](../anypoint-code-builder/urls-to-allow).

### MuleSoft Vibes Requirements (Optional)

If you plan to use MuleSoft Vibes to create agent network projects, make sure you meet [the requirements](../anypoint-code-builder/mulesoft-vibes#before-you-begin).

### CLI Requirements (Optional)

If you’re using the Anypoint CLI to create agent network projects, ensure you meet these requirements.

- 
Node 20 (v20.19.4) or later. See [Nodejs.org](https://nodejs.org/en).
- 
Java 17 or later. Set the `JAVA_HOME`environment variable.

## Task Overview

### Step 1: Set Up Your Agent Network

- 
Use Anypoint Runtime Manager to set up a private space in CloudHub 2.0 or deployment target in Runtime Fabric. 
- 
Set up Ingress and egress Omni Gateways for the private space or deployment target. - 
If using Anypoint Code Builder, see [Set Up Agent Network Gateways for the Private Space or Deployment Target](../anypoint-code-builder/af-get-started#setup-gateways).
- 
If using the Anypoint CLI, see the [setup gateways command reference](../anypoint-code-builder/af-build-agent-networks-in-a-ci-cd-environment#agent-network-setup-gateways).
 
- 

### Step 2: Create a Project

Now you’re ready to create an agent network project. Choose one of these methods.

### Step 3: Define Your Agent Network Specification

After you create your agent network project, configure `agent-network.yaml` and `exchange.json` to reflect the structure of your network.

### Step 4: Publish Your Agent Network Assets

Build and publish your agent network project as Anypoint Exchange assets. When you publish the agent network, an asset is created in Exchange for each broker, agent, and MCP server that’s in your agent network.

### Step 5: Deploy Your Agent Network Instances

Deploy your agent network instance to a deployment target. You can deploy to a CloudHub 2.0 private space or to a Runtime Fabric.