# Monday.com integration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/monday-integration.html](https://docs.aws.amazon.com/quick/latest/userguide/monday-integration.html)

---

With Monday.com integration in Amazon Quick, you can manage project boards, track items, and coordinate team workflows through MCP server connectivity. This integration provides action capabilities for project management and team collaboration operations.

## What you can do

        
        Monday.com integration provides action connector capabilities through MCP server connectivity:

- 
                Create and manage project boards 
- 
                Add and update board items and tasks 
- 
                Manage team assignments and workloads 
- 
                Track project timelines and deadlines 
- 
                Update item status and progress 
- 
                Generate reports and analytics 

## Available tools

        
        The Monday.com MCP server typically provides these tools:

- 
                `create_board`- Create new project boards
- 
                `get_board`- Get board information
- 
                `create_item`- Create new board items
- 
                `update_item`- Update item details
- 
                `list_items`- List board items
- 
                `create_column`- Create board columns
- 
                `update_column_value`- Update column values
- 
                `search_boards`- Search for boards

###### Note

The specific tools and capabilities available through this MCP server may change over time. For the most current information about supported tools, features, and implementation details, check the official Monday.com documentation and MCP server repository.

## Setting up Monday.com integration

        
        Monday.com integration uses MCP server connectivity to provide action capabilities. For detailed setup instructions, see [Model Context Protocol (MCP) integration](./mcp-integration.html).

You'll need:

- 
                Monday.com account with appropriate board permissions 
- 
                Monday.com API token for authentication 

## Compatibility

        
        Monday.com integration supports:

- 
                **Chat Agents:**Yes
- 
                **Flows:**Yes
- 
                **Knowledge Base:**No