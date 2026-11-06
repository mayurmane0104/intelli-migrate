# Create a Scanner for Provider Services | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/general/exp-services-connect-providers-to-add](https://docs.mulesoft.com/general/exp-services-connect-providers-to-add)

---

- 
Exchange: Exchange Administrator 
- 
Exchange: Exchange Contributor 
- 
API Manager: API Creator 
- 
API Manager: Manage Policies 

# Create a Scanner for Provider Services

To create a scanner, connect to a provider. The system runs scanners against supported cloud platforms, discovers services (such as agents, APIs, and MCP servers), and registers them in the matching catalog in **Portfolio**. You supply credentials and scanner metadata so the integration is repeatable and auditable.

Start the flow from **Home** or from a specific catalog in **Portfolio**. To see how this flow relates to manual registration, see [Adding Services to Your Portfolio](exp-services-add-to-portfolio). To create and tune scanners, see [Adding Scanners from Providers](exp-scanners-add-from-providers).

## Before You Begin

Before getting started, make sure you have:

- 
An Anypoint Platform account. 
- 
One of these permissions: For more information, see [Enhanced Experience Permissions](exp-home-start#permissions).

## When to Use a Scanner

Use a scanner when your team maintains services in an external platform and wants those services to appear automatically in portfolio catalogs after authentication and discovery, instead of registering each service manually.

## Entry Points for Creating a Scanner

- 
**Home**Use **Add Services**, select**Connect to Provider**, then work through the flow to pick a provider, validate access, and save scanner settings. Use this path when you’re not starting from a single catalog view.
- 
**Portfolio**Open a supported service catalog in **Portfolio**. Use the add control for that service type (for example**Add API**or**Add MCP Server**), select**Connect to Provider**, and complete the same style of flow scoped to that catalog.

Labels differ by catalog and release. Match what you see in the UI.

## Create a Scanner

Across **Home** and **Portfolio** entry points, scanner creation includes the same decisions:

- 
Which provider or platform to target for discovery and import. 
- 
Credentials and authentication so the system can reach the provider securely. 
- 
Connection validation so you know discovery can run against live data. 
- 
Scanner identity and settings: name, description, and options your administrator expects before you save the scanner. 

When the scanner runs successfully, the system registers discovered services in the catalog you started from (for example, APIs land in the **APIs** catalog).

## What Changes by Catalog

Scanner setup decisions stay the same across catalogs. However, after successful runs, discovered results get registered in specific service catalogs.

For example, when you start from **APIs**, discovered APIs are registered in the **APIs** catalog.