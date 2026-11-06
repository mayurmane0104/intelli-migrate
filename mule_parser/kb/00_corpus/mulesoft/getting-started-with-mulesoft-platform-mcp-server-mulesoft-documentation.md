# Getting Started with MuleSoft Platform MCP Server | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mulesoft-mcp-server/getting-started-platform](https://docs.mulesoft.com/mulesoft-mcp-server/getting-started-platform)

---

# Getting Started with MuleSoft Platform MCP Server

Scan, discover, govern, and monitor APIs, agents, MCP servers, and LLMs across your entire IT landscape from a single AI-accessible interface. MuleSoft Platform MCP Server gives AI tools governed access to your infrastructure to accelerate production-ready AI deployment. Connect your IDE in minutes using any MCP-compatible client.

## Create a Connected App

Follow the steps in [Create a Connected App That Acts on the User’s Behalf](../access-management/creating-connected-apps-dev#create-connected-app) to create a connected app.

Additionally, when prompted, add the following permission scopes. These scopes enable you to use specific MuleSoft Platform MCP Server tools.

| When creating the connected app, be sure to select the Authorization Code and Refresh Token grant types. | 

Refer to the [MuleSoft Platform MCP Server Tool Reference](reference-mcp-tools-platform) for details on all MuleSoft Platform MCP Server tools. Only tools listed in these tables require specific permission scopes.

### Exchange

| To… | Required Permission | Associated Tools | 
|---|---|---|
| View and download assets within a business group. | Exchange Viewer | |
| View, create, and download assets within a business group, including editing asset portal content in an existing asset version. | Exchange Contributor | 

### API Manager

| To… | Required Permission | Associated Tools | 
|---|---|---|
| View API configurations and policies in the specified environment. | API Manager Environment Viewer | |
| View, create, modify, and delete APIs in the specified environment. | API Manager Environment Admin | 

### Anypoint Monitoring

| To… | Required Permission | Associated Tools | 
|---|---|---|
| View but not modify content in Anypoint Monitoring. | Monitoring Viewer | 

### Governance

| To… | Required Permission | Associated Tools | 
|---|---|---|
| View reports. | Governance Viewer | |
| Manage profiles and view reports. | Governance Administrator | 

### Runtime Manager

| To… | Required Permission | Associated Tools | 
|---|---|---|
| Create applications in a specific environment. | Manage Application Data | 

### General

| To… | Required Permission | Associated Tools | 
|---|---|---|
| View organization information. | organization_read (implicit) | 

## Configure Your IDE

Configure Claude Desktop, ChatGPT, Cursor, Windsurf, or VS Code to work with MuleSoft Platform MCP Server. After you add the configuration, verify it by checking that the server has started in the MCP section of your IDE.

| MuleSoft remote MCP servers currently only support manual client registration through app creation and do not support other client registration methods such as Dynamic Client Registration (DCR). | 

### Available Client Connections

When configuring your AI tool, use the endpoint for your region.

Use `/mcp`, and fall back to `/mcp/sse` if the client does not connect.

- 
[https://omni.mulesoft.com/mcp](https://omni.mulesoft.com/mcp)
- 
[https://omni.mulesoft.com/mcp/sse](https://omni.mulesoft.com/mcp/sse)

| Type | URL | 
| US Prod | 
 | 
| EU Prod | 
 | 
| CA Prod | 
 | 
| JP Prod | 
 | 
| IN Prod | 
 | 

For more information about Anypoint Platform regions, see [Control Plane Hosting Options](../hosting-home/#control-plane-hosting-options).

### Claude Desktop

In Claude Desktop:

- 
Click **Customize**>**Connectors**.
- 
Click the add (+) icon, and then click **Add Custom Connector**.
- 
Name the connection, and enter the **Remote Universal URL**, for example,[https://omni.mulesoft.com/mcp](https://omni.mulesoft.com/mcp).
- 
Enter the Client ID and Client Secret from your connected app. 

In your connected app:

- 
Log into Anypoint Platform, and open your connected app. 
- 
In the **Redirect URLs**field, enter[https://claude.ai/api/mcp/auth_callback](https://claude.ai/api/mcp/auth_callback)
- 
To apply changes, click **Continue**.

OR run this command in your terminal:

`MCP_CLIENT_SECRET=<YOUR_CLIENT_SECRET> claude mcp add --transport http mulesoft-platform YOUR_URL_HERE --client-id <YOUR_CLIENT_ID>`bash

Download [Claude Desktop](https://claude.com/download).

### ChatGPT

In ChatGPT:

- 
Click **Apps**>**Settings.**
- 
Click the settings icon, click **Create App**, and configure the following:- 
Name the connection, and enter the **Remote Universal URL**, for example,[https://omni.mulesoft.com/mcp](https://omni.mulesoft.com/mcp).
 
- 
- 
In **OAuth**>**Advanced settings**>**Client registration**, configure the following:- 
Enter the Client ID and Client Secret from your connected app. 
- 
Copy the Callback URL. 
 
- 

In your connected app:

- 
Log in to Anypoint Platform, and open your connected app. 
- 
In the redirect URLs field, enter the Callback URL value you copied. 
- 
To apply changes, click **Continue**.

Download [ChatGPT](https://chatgpt.com/download/).

### Cursor

In Cursor:

- 
Click **Settings**>**Tools and MCPs**>**Add a Custom MCP Server**.
- 
Add the following code snippet: `{ "mcpServers": { "mulesoft-platform": { "command": "npx", "args": [ "-y", "mcp-remote@latest", "https://omni.mulesoft.com/mcp", "--static-oauth-client-info", "{\"client_id\":\"YOUR_CLIENT_ID\",\"client_secret\":\"YOUR_CLIENT_SECRET HERE\"}" ] } } }`json

Download [Cursor](https://cursor.com/).

### Windsurf

In Windsurf:

- 
Click **Settings**>**Cascade**>**Open MCP Registry**.
- 
Click the settings icon and in `~/.codeium/windsurf/mcp_config.json`add the following code snippet:`{ "mcpServers": { "mulesoft-platform": { "command": "npx", "args": [ "-y", "mcp-remote@latest", "https://omni.mulesoft.com/mcp", "--static-oauth-client-info", "{\"client_id\":\"YOUR_CLIENT_ID\",\"client_secret\":\"YOUR_CLIENT_SECRET\"}" ] } } }`json

Download [Windsurf](https://windsurf.com/).

### VS Code

In VS Code:

- 
In your user profile, configure a custom MCP server in the `mcp.json`file. Alternatively, run`MCP: Add Server`in the Command Palette (Shift+Cmd+P) to add a server through a guided flow.`{ "servers": { "mulesoft-platform": { "type": "stdio", "command": "npx", "args": [ "-y", "mcp-remote@latest", "https://omni.mulesoft.com/mcp", "--static-oauth-client-info", "{\"client_id\":\"YOUR_CLIENT_ID\",\"client_secret\":\"YOUR_CLIENT_SECRET\"}" ] } } }`json
- 
To run the server, click **Start**.
- 
When prompted, enter the Client ID and Client Secret from your connected app. 

Download [VS Code](https://code.visualstudio.com/).

## Troubleshooting

Resolve authentication and connection issues with these troubleshooting steps.

### Authentication Failure

To resolve authentication issues, follow these troubleshooting steps.

- 
Try logging out of your Anypoint Platform account and logging back in. 
- 
If you encounter an authorization error: - 
Add the correct redirect URL to your connected app. 
- 
Add the necessary permissions scopes to your connected app. 
 
- 
- 
If you get an error when adding a non-traditional redirect URL to your connected app: - 
Determine the callback port automatically assigned for the client’s authentication request (for example, 12148). 
- 
Add the localhost URL to the redirect URLs in your connected app (for example, [http://localhost:12148/oauth/callback](http://localhost:12148/oauth/callback)
 
- 
- 
If you get a permissions-related error when attempting to authenticate, add these permissions to your connected app: - 
Background Access 
- 
Profile 
- 
Identity 
- 
Email 
 
- 

### Connection Issues

If your MCP client can’t reach the server or fails to establish a session, verify these settings.

- 
Ensure your MCP client supports Streamable HTTP transport. 
- 
Check that your client can handle OAuth authentication flows. 
- 
Verify the MCP server URL is [https://omni.mulesoft.com/mcp](https://omni.mulesoft.com/mcp).