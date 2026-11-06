# Notion integration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/notion-integration.html](https://docs.aws.amazon.com/quick/latest/userguide/notion-integration.html)

---

With Notion integration in Amazon Quick, you can manage pages, databases, and collaborative workspaces through MCP server connectivity. This integration provides action capabilities for knowledge management and content organization operations.

## What you can do

        
        Notion integration provides action connector capabilities through MCP server connectivity:

- 
                Create and edit pages and documents 
- 
                Manage databases and structured content 
- 
                Organize content with tags and properties 
- 
                Share pages and collaborate with team members 
- 
                Search across workspaces and content 
- 
                Manage workspace permissions and access 

## Available tools

        
        The Notion MCP server typically provides these tools:

- 
                `create_page`- Create new pages
- 
                `update_page`- Update page content
- 
                `get_page`- Retrieve page information
- 
                `search_pages`- Search for pages
- 
                `create_database`- Create new databases
- 
                `query_database`- Query database entries
- 
                `create_database_entry`- Add database entries
- 
                `update_database_entry`- Update database entries

###### Note

The specific tools and capabilities available through this MCP server may change over time. For the most current information about supported tools, features, and implementation details, check the official Notion documentation and MCP server repository.

## Setting up Notion integration

        
        Notion integration uses MCP server connectivity to provide action capabilities. For detailed setup instructions, see [Model Context Protocol (MCP) integration](./mcp-integration.html).

You'll need:

- 
                Notion account with appropriate workspace permissions 
- 
                Notion integration token for API access 

## Compatibility

        
        Notion integration supports:

- 
                **Chat Agents:**Yes
- 
                **Flows:**Yes
- 
                **Knowledge Base:**No