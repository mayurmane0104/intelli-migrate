# Create an MCP Server | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/general/exp-services-create-mcp-server](https://docs.mulesoft.com/general/exp-services-create-mcp-server)

---

- 
Exchange: Exchange Contributor 
- 
Exchange: Exchange Administrator 
- 
Exchange: Exchange Creator 

# Create an MCP Server

Create MCP servers to define identity, runtime connectivity, and the tools and resources exposed to MCP clients.

Creating an MCP server defines a new MCP implementation—for example, by transcoding an existing REST API or creating a runtime deployment—and establishes the server identity, runtime connectivity, and the MCP capabilities (tools and resources) exposed to clients.

When you create an MCP server in Enhanced Experience, the server is added to **Portfolio** automatically.

During creation, you define:

- 
**Service definition**Name, description, and ownership metadata so teams can identify the server in catalogs and governance views. 
- 
**Connection and runtime details**Endpoint and access settings Enhanced Experience uses at runtime to connect to underlying SaaS systems. 
- 
**Capability surface**The MCP tools and resources clients can discover and invoke. 
- 
**Validation and readiness**Checks that confirm the server is reachable and that the declared MCP capabilities are usable. 

## Before You Begin

Before getting started, make sure you have:

- 
An Anypoint Platform account. 
- 
One of these permissions: For more information, see [Enhanced Experience Permissions](exp-home-start#permissions).

## Steps to Create an MCP Server

- 
Open **MCP Servers**and select**Add MCP Server**>**Create MCP Server**.
- 
In **Select Source, Instance & Tools**, select the APIs or SaaS systems you want to expose. Select the source instance or version, then select the tools to publish, including optional read-only filtering. Click**Next**.
- 
In **SaaS Credentials**, provide the credentials required for the selected sources so the MCP server can call them securely. Click**Next**.
- 
In **Review**, validate the selected sources, tools, and credential mappings, then complete creation.

## After You Create an MCP Server

After you click **Save**, the MCP server is automatically added to the **MCP Servers** catalog in **Portfolio**. No additional action is required.