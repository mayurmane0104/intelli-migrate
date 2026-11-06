# MuleSoft Vibes Overview | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/mulesoft-vibes](https://docs.mulesoft.com/anypoint-code-builder/mulesoft-vibes)

---

# MuleSoft Vibes Overview

MuleSoft Vibes is a purpose-built assistant for the development lifecycle, available directly in Anypoint Code Builder.

MuleSoft Vibes enables you to build, deploy, and manage your projects using natural language messages.

MuleSoft Vibes integrates with the [MuleSoft MCP Server](../mulesoft-mcp-server/), which provides a set of agentic tools that connect MuleSoft Vibes directly to your MuleSoft environment. Through this integration, MuleSoft Vibes can perform actions and retrieve data on your behalf, enabling capabilities such as:

- 
Developing API specifications 
- 
Creating and configuring applications 
- 
Creating agent networks 
- 
Searching for assets 
- 
Deploying and managing instances 
- 
Securing your applications 
- 
Managing custom metadata 

You can also use [skills](vibes-skills), reusable instruction sets that MuleSoft Vibes activates when your task matches a skill’s description. MuleSoft Vibes uses the `use_skill` tool to load and run a skill’s full instructions when your task matches that skill.
**Workspace skills** are available only in the workspace or project where they are defined.
**Global skills** are available in every project and workspace.

Large language models (LLMs) power these features and operate within the Salesforce Shared Trust Boundary.

MuleSoft Vibes is part of the broader MuleSoft AI ecosystem, which also includes capabilities such as Map with AI and Map and Transform with AI. For an overview of all MuleSoft AI features, see the [Learning Map: MuleSoft AI](../general/learning-map-mulesoft-ai). For a high-level overview that guides you through a curated set of MuleSoft Vibes topics in Anypoint Code Builder, see [Learning Map: MuleSoft Vibes for Anypoint Code Builder](../general/learning-map-mulesoft-vibes).

| MuleSoft Vibes is available on US, EU, Canada, and Japan cloud hosts. | 

## Capabilities in Your Workspace

MuleSoft Vibes helps you describe outcomes in plain language so the assistant can plan changes, generate artifacts, and run permitted actions against your connected MuleSoft environment. Generated work stays in your project and is subject to the same governance as code you write manually.

Models run within the Salesforce Shared Trust Boundary, and the assistant inherits the permissions of the user signed in to Anypoint Code Builder. For supported regions, prerequisites, and a full capability list, see [Before You Begin](#before-you-begin-vibes).

## MCP Servers and Agentic Tools

The MuleSoft MCP Server supplies tools that connect MuleSoft Vibes to Exchange, Runtime Manager, and other services so prompts can search assets, inspect deployments, and perform other allowed operations. You enable or restrict that behavior by which servers and tools you install.

For product-level MCP documentation, see [MuleSoft MCP Servers Overview](../mulesoft-mcp-server/). When you are ready to add or tune servers inside the IDE, continue with [Configuring an MCP Server](vibes-mcp-server).

## Related MuleSoft AI Resources

MuleSoft Vibes is part of the broader MuleSoft AI story alongside experiences such as Map with AI and Map and Transform with AI. For a platform-wide learning path across those capabilities, see [MuleSoft AI](../general/learning-map-mulesoft-ai).

## Before You Begin

To use MuleSoft Vibes, make sure that you meet these prerequisites:

- 
Make sure you have the [required Anypoint Code Builder permissions](start-configure-permissions#permissions).
- 
Install Node.js 20 LTS or later. 
- 
Install the latest version of `jq`.
- 
On Windows, install **Git Bash**to use skills that run prepackaged shell-based steps.
- 
Ensure you have the following permissions: - 
**Anypoint Code Builder Developer**(to use MuleSoft Vibes in the Cloud IDE)
- 
**Mule Developer Generative AI User**
 
- 
- 
Make sure Einstein is enabled in Access Management. For more information, see [Enabling or Disabling Agentforce for Anypoint Platform](../access-management/enabling-agentforce).

| Authentication happens through the user logged in to Anypoint Code Builder. MuleSoft Vibes inherits the same permissions as that user and can only execute actions that the user is authorized to perform in Anypoint Platform. | 

## See Also

- 
Learning Map: MuleSoft Vibes for Anypoint Code Builder (MuleSoft documentation portal)