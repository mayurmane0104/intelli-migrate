# Create Agent Networks | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/af-create-agent-network](https://docs.mulesoft.com/anypoint-code-builder/af-create-agent-network)

---

![Anypoint Code Builder canvas showing two different brokers with their respective agents and MCP servers](_images/af-acb-canvas.png) 

# Create Agent Networks

Whether you want to use MuleSoft Vibes or the UI, Anypoint Code Builder includes all the agent network functionality you need to get started.

## Before You Begin

Make sure you review the [prerequisites](af-get-started#before-you-begin).

## Create a Network Using MuleSoft Vibes

MuleSoft Vibes can help you create your project. For more information, see [Creating API Specs with MuleSoft Vibes](vibes-api-ai-create-spec).

- 
In the Anypoint Code Builder activity bar, click the agent icon ![](_images/af-acb-dev-agent-icon.png) . .
- 
Describe your agent network, including the brokers, agents, MCP servers, and LLMs you want to connect. MuleSoft Vibes does the rest. 

To get started, try one of these suggested messages.

- 
Create a new agent network project called "Employee Onboarding." Add HR agent and CRM agent. 
- 
Build a travel planner broker that plans multi-city trips and generate a new agent network. 
- 
Generate an agent network project for incident management. Include a broker that coordinates the resolution of incidents reported by customers. 

## Create a Network Using Anypoint Code Builder

- 
If you’re not logged in, log in to your Anypoint Platform account. 
- 
In Anypoint Code Builder, choose one of the following: - 
In Create, select **Create an Agent Network**.
- 
From the Command Palette, run this command: **MuleSoft: Create an Agent Network Project**.
 
- 
- 
Enter a name for the project and select the location to create the project. 
- 
Select the business group associated with the target space you created in [Get Started with Agent Networks](af-get-started). The business group you select must be the same business group you selected when you created the target space.
- 
Select **Create Project**.

Anypoint Code Builder creates these files as part of your agent network project. These files define your agent network specification to meet your business requirements. For more information, see [Agent Network Project File Reference](af-project-files).

- 
`agent-network.yaml`Specifies brokers, agents, MCP servers, LLMs, policies, and authentication in your agent network. 
- 
`exchange.json`Specifies Anypoint Exchange assets that are referenced in your agent network, as well as the variables to use in your agent network. Each asset has an asset ID that you use in the `agent-network.yaml`file.

The canvas shows a visual, read-only representation of your YAML file. Select any component to show the associated code in the code editor.

![Anypoint Code Builder canvas showing two different brokers with their respective agents and MCP servers](_images/af-acb-canvas.png) 

## Create a Network Using the Anypoint CLI

If you run operations within a CI/CD environment, you can use Anypoint CLI’s plugin to set up, create, build, publish, and deploy agent networks. For more information, see [Build Agent Networks in a CI/CD Environment](af-build-agent-networks-in-a-ci-cd-environment).