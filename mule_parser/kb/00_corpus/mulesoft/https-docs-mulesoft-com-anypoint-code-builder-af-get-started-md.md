# https://docs.mulesoft.com/anypoint-code-builder/af-get-started.md

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/af-get-started.md](https://docs.mulesoft.com/anypoint-code-builder/af-get-started.md)

---

```
# Get Started with Agent Networks
> For the full documentation index, see: https://docs.mulesoft.com/llms.txt
Creating agent networks is a multi-step process. Review these prerequisites and task overviews to
make sure you can create agent networks efficiently.
## Before You Begin
Before you get started, review these prerequisites.
### Anypoint Platform Requirements and Permissions
<table><colgroup><col> <col></colgroup><thead><tr><th>Anypoint Platform Component</th><th>Required Permissions</th></tr></thead><tbody><tr><td><p>Runtime Manager</p></td><td><div><div><ul><li><p>Manage Servers</p></li><li><p>Create Applications</p></li><li><p>Read Servers</p></li></ul></div></div></td></tr><tr><td><p>Anypoint Code Builder</p></td><td><div><div><ul><li><p>Anypoint Code Builder</p></li><li><p>Mule Developer Generative AI User</p></li></ul></div></div></td></tr><tr><td><p>Anypoint Design Center</p></td><td><p>Design Center Developer</p></td></tr><tr><td><p>API Manager</p></td><td><div><div><ul><li><p>Deploy API Proxies</p></li><li><p>Manage Policies</p></li></ul></div></div></td></tr><tr><td><p>Exchange</p></td><td><p>Exchange Contributor</p></td></tr><tr><td><p>Usage</p></td><td><p>Usage Viewer</p></td></tr><tr><td><p>CloudHub 2.0 or Runtime Fabric</p></td><td><p><a href="../runtime-fabric/latest/limitations-self">Runtime Fabric permissions</a> <a href="../cloudhub-2/ps-assign-permissions">CloudHub 2.0 permissions</a></p></td></tr></tbody></table>
See [Permissions by Product in Anypoint Platform](../access-management/permissions-by-product) for a
list of all Anypoint Platform permissions.
### Additional Requirements
To complete these tasks, you also need:
- Your Anypoint Platform credentials
- [Anypoint Code Builder desktop](start-acb)
  Allowlist Anypoint Code Builder URLs. For more information, see
  [Allow URLs for Anypoint Code Builder](urls-to-allow).
- [Omni Gateway Ingress and Egress gateways](../gateway/latest/flex-gateway-managed-ingress-egress)
### MuleSoft Vibes Requirements (Optional)
If you plan to use MuleSoft Vibes to create agent network projects, make sure you meet
[the requirements](mulesoft-vibes#before-you-begin).
### CLI Requirements (Optional)
If youâ€™re using the Anypoint CLI to create agent network projects, ensure you meet these
requirements.
- Node 20 (v20.19.4) or later. See [Nodejs.org](https://nodejs.org/en).
- Java 17 or later. Set the `JAVA_HOME` environment variable.
- [Anypoint CLI Fabric Plugin](af-build-agent-networks-in-a-ci-cd-environment)
## Task Overview
### Step 1: Set Up Your Agent Network
1.  Use Anypoint Runtime Manager to set up a private space in CloudHub 2.0 or deployment target in
    Runtime Fabric.
    See [Set Up the Private Space or Deployment Target for Your Environment](#setup-space).
2.  Set up Ingress and egress Omni Gateways for the private space or deployment target.
    - If using Anypoint Code Builder, see
      [Set Up Agent Network Gateways for the Private Space or Deployment Target](#setup-gateways).
    - If using the Anypoint CLI, see the
      [setup gateways command reference](af-build-agent-networks-in-a-ci-cd-environment#agent-network-setup-gateways).
### Step 2: Create a Project
Now youâ€™re ready to create an agent network project. Choose one of these methods.
- [Create a Network Using MuleSoft Vibes](af-create-agent-network#create-dev-agent)
- [Create a Network Using Anypoint Code Builder](af-create-agent-network#create-acb)
- [Create a Network Using the Anypoint CLI](af-create-agent-network#create-cli)
### Step 3: Define Your Agent Network Specification
After you create your agent network project, configure `agent-network.yaml` and `exchange.json` to
reflect the structure of your network.
- [Define a Network Using MuleSoft Vibes](af-define-your-agent-network-specification#define-dev-agent)
- [Define a Network Using Anypoint Code Builder or IDE](af-define-your-agent-network-specification#define-acb-ide)
### Step 4: Publish Your Agent Network Assets
Build and publish your agent network project as Anypoint Exchange assets. When you publish the agent
network, an asset is created in Exchange for each broker, agent, and MCP server thatâ€™s in your agent
network.
- [Publish Your Network Using MuleSoft Vibes](af-publish-agent-network-assets#publish-dev-agent)
- [Publish Your Network Using Anypoint Code Builder](af-publish-agent-network-assets#publish-acb)
- [Publish Your Network Using the Anypoint CLI](af-build-agent-networks-in-a-ci-cd-environment#agent-network-project-publish)
### Step 5: Deploy Your Agent Network Instances
Deploy your agent network instance to a deployment target. You can deploy to a CloudHub 2.0 private
space or to a Runtime Fabric.
- [Deploy Your Network Using MuleSoft Vibes](af-deploy-agent-network-targets#deploy-dev-agent)
- [Deploy Your Network Using Anypoint Code Builder](af-deploy-agent-network-targets#deploy-acb)
- [Deploy Your Network Using the Anypoint CLI](af-build-agent-networks-in-a-ci-cd-environment#agent-network-project-deploy)
## Set Up the Private Space or Deployment Target for Your Environment
To deploy an agent network, you need a private space on CloudHub 2.0 or a deployment target on
Anypoint Runtime Fabric.
If you already have a private space configured in CloudHub 2.0, you can associate it with the
business groups and environments where youâ€™ll deploy your agent network.
Depending on your deployment target:
- CloudHub 2.0:
  1.  Create a private space in CloudHub 2.0 or verify that you can access an existing private
      space.
      To create a private space, see [Creating Private Spaces](../cloudhub-2/ps-create-configure).
      We recommend naming the private space `agent-network-space`.
  2.  [Associate the new or existing private space with the business groups and environments](../cloudhub-2/ps-config-env)
      where you plan to deploy your agent network.
      You must complete this step so that the private space appears as a valid deployment target in
      Anypoint Code Builder and Anypoint CLI.
- Runtime Fabric:
  Create a target space for Runtime Fabric.
  For information about Runtime Fabric deployments, see
  [Managed Omni Gateway on Runtime Fabric](../gateway/latest/flex-gateway-managed-set-up#rtf).
## Set Up Agent Network Gateways for the Private Space or Deployment Target
After you have a target space, use the `MuleSoft: Set Up Agent Network Gateways` command to create
the ingress and egress gateways required for deployment in either CloudHub 2.0 or Runtime Fabric.
For agent networks, you must have at least one small Managed Omni Gateway and one large Managed Omni
Gateway in your environment. For more information about gateways, see
[Omni Gateway Deployment Models](../gateway/latest/flex-architecture-basic-deployments).
For more information about Runtime Fabric deployments, see
[Managed Omni Gateway on Runtime Fabric](../gateway/latest/flex-gateway-managed-set-up#rtf).
1.  In Anypoint Code Builder, from the Command Palette, run the command **MuleSoft: Set Up Agent
    Network Gateways**.
    If you didnâ€™t associate the private space with the business group and environment, you see an
    error.
2.  If youâ€™re not logged in, log in to your Anypoint Platform account.
3.  Select the business group, environment, and private or target space.
    The `MuleSoft: Set Up Agent Network Gateways` command creates these gateways in the private or
    target space you select:
    - agent-network-ingress-gw (with public and internal endpoint)
    - agent-network-egress-gw (with internal endpoint only)
If the gateways already exist in the selected private or target space, the command doesnâ€™t recreate
them.
## See Also
- [Create Agent Networks](af-create-agent-network)
```