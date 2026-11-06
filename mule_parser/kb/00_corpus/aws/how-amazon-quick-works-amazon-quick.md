# How Amazon Quick works - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/how-quicksuite-works.html](https://docs.aws.amazon.com/quick/latest/userguide/how-quicksuite-works.html)

---

When you use Quick, the following components work together to process your requests.

## You start in chat

        Chat is the primary interface for Quick. You type a question, give an
            instruction, or describe what you need. Quick interprets your request
            and determines how to respond: answering from connected data, generating content,
            running a workflow, conducting research, or taking action in an external application.
            For more information, see [Ask questions, explore data, and get insights with chat in Amazon Quick](./using-quick-chat.html).

## Agents process your requests

        Behind every interaction is an agent. Agents are configured with instructions that
            define their behavior, knowledge sources that ground their responses, and tools that
            let them take action. Quick provides a default agent, and you can create
            custom agents for specific domains. For more information, see [Create, customize, and deploy AI-powered chat agents in Amazon Quick](./working-with-agents.html).

## Spaces organize context

        Spaces bring together the resources an agent needs: documents, dashboards,
            datasets, knowledge bases, and action connectors. When you assign a space to an
            agent, it draws on everything in that space to answer questions and complete tasks.
            You share spaces with your team so everyone benefits from the same context. For more
            information, see [Organize, collaborate, and share resources with spaces in Amazon Quick](./working-with-spaces.html).

## Integrations connect Quick to your world

        Integrations give Quick access to external information and the ability to act on your behalf:

- **Knowledge bases**
- 
                    Bring external content into Quick for AI retrieval. Sources include Amazon S3, SharePoint, OneDrive, Confluence, Google Drive, and web crawlers. Quick keeps the index in sync as sources update. 
- **Action connectors**
- 
                    Let Quick read data, trigger workflows, and update records in external services. You create connectors from OpenAPI specifications or Model Context Protocol (MCP) servers. 
- **Extensions**
- 
                    Embed Quick inside Chrome, Slack, Microsoft Teams, and Microsoft 365 applications so you interact with agents without leaving the app you're working in. 
- **Structured data connections**
- 
                    Connect Quick Sight to databases, data warehouses, and data lakes for analytics and visualization. 

For more information, see [Work with integrations in Amazon Quick](./working-with-integrations.html).

## Features use those building blocks

        Each Quick feature combines the components above in different ways:

| Feature | What it does | What it uses | 
|---|---|---|
| Quick Sight | Interactive dashboards and analytics | Structured data connections, SPICE, datasets | 
| Quick Flows | Task automation | Action connectors, spaces, agent logic | 
| Quick Automate | End-to-end process automation | Action connectors, agents, human-in-the-loop | 
| Quick Research | In-depth cited reports | Spaces, knowledge bases, web | 
| Apps in Quick | Interactive web applications | Structured data, action connectors, Quick Sight visuals | 
| Desktop application | Personalized AI on your machine | Local files, email, calendar, MCP servers | 

## Where to go next

        | I want to... | Go to | 
|---|---|
| Set up Quick for my organization | [Setting up and signing into Amazon Quick](./setting-up.html) | 
| Start using Quick | [Getting started with Amazon Quick](./getting-started.html) | 
| Build dashboards and visualize data | [Visualize, analyze, and share data with analyses, dashboards, and reports in Amazon Quick Sight](./quick-bi.html) | 
| Automate tasks | [Using Amazon Quick automations](./using-amazon-quick-automations.html) | 
| Research a topic | [Using Amazon Quick Research](./using-amazon-quick-research.html) | 
| Build an app | [Build web applications with apps in Amazon Quick](./using-amazon-quick-apps.html) | 
| Connect Quick to my tools | [Work with integrations in Amazon Quick](./working-with-integrations.html) | 
| Use Quick on my desktop | [What is Amazon Quick on desktop?](./what-is-desktop.html) |