# Intercom integration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/intercom-integration.html](https://docs.aws.amazon.com/quick/latest/userguide/intercom-integration.html)

---

With Intercom integration in Amazon Quick, you can manage customer conversations, support tickets, and user engagement through MCP server connectivity. This integration provides action capabilities for customer support and communication operations.

## What you can do

        
        Intercom integration provides action connector capabilities through MCP server connectivity:

- 
                Manage customer conversations and messages 
- 
                Create and update support tickets 
- 
                Manage user profiles and contact information 
- 
                Send targeted messages and campaigns 
- 
                Track customer engagement and activity 
- 
                Manage team assignments and workflows 

## Available tools

        
        The Intercom MCP server typically provides these tools:

- 
                `create_conversation`- Start new conversations
- 
                `reply_to_conversation`- Reply to existing conversations
- 
                `list_conversations`- List customer conversations
- 
                `create_user`- Create new user profiles
- 
                `update_user`- Update user information
- 
                `send_message`- Send messages to users
- 
                `create_ticket`- Create support tickets
- 
                `search_users`- Search for users

###### Note

The specific tools and capabilities available through this MCP server may change over time. For the most current information about supported tools, features, and implementation details, check the official Intercom documentation and MCP server repository.

## Setting up Intercom integration

        
        Intercom integration uses MCP server connectivity to provide action capabilities. For detailed setup instructions, see [Model Context Protocol (MCP) integration](./mcp-integration.html).

You'll need:

- 
                Intercom account with appropriate permissions 
- 
                Intercom API access token 

## Compatibility

        
        Intercom integration supports:

- 
                **Chat Agents:**Yes
- 
                **Flows:**Yes
- 
                **Knowledge Base:**No