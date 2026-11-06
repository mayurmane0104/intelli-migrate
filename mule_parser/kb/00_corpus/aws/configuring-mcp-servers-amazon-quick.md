# Configuring MCP servers - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/mcp-servers-desktop.html](https://docs.aws.amazon.com/quick/latest/userguide/mcp-servers-desktop.html)

---

The Amazon Quick desktop application supports the Model Context Protocol (MCP), an open standard that extends the capabilities of Quick with custom tools and integrations. You can connect MCP servers to give Quick access to databases, internal APIs, developer tools, and other systems that are not available through built-in connections.

## What is MCP?

        Model Context Protocol (MCP) is a protocol that allows AI assistants to interact with external tools and data sources. When you connect an MCP server to Quick, the tools provided by that server become available in your chat conversations and scheduled agents. For example, you can connect an MCP server that provides database query tools, and then ask Quick to query your database directly in chat.

## Accessing MCP settings

        To manage your MCP servers, open **Settings** in
            the sidebar, choose **Capabilities**, and then
            choose the **MCP** tab.

The MCP tab displays your connected servers with a search bar, filter
            dropdown, and grid or list view toggle. You can add new servers by choosing
            **+ Add MCP**.

## Adding an MCP server

        When you choose **+ Add MCP**, a dialog appears
            with three connection types: **Local**, **Import**, and **Remote**. Choose the connection type that matches how your MCP server
            runs.

### Local

Use the **Local** connection type to run an
                MCP server as a command on your machine. This is the most common option for
                development tools and locally installed servers.

The following table describes the fields for a Local MCP connection.

| Field | Required | Description | 
|---|---|---|
| Name | Yes | A friendly name to identify this MCP server (for example, "My Database MCP"). | 
| Command | Yes | The executable to run. Common values include `python`,`npx`,`node`, and`uvx`. | 
| Arguments | No | Command line arguments, separated by spaces (for
                                example, `-m mcp_server --port 8080`). | 
| Description | No | A description of what this MCP server does and what tools it provides. This helps Quick understand when to use the server's tools. | 
| Environment
                                variables | No | Environment variables required by the server. Choose + Add variableto add
                                key-value pairs. | 
| Timeout
                                (seconds) | No | Maximum time to wait for the server to start, from 5 to 300 seconds. The default is 30 seconds. | 

###### To add a local MCP server

Use the following procedure.

- 
                    Open **Settings**in the sidebar and choose**Capabilities**.
- 
                    Choose the **MCP**tab.
- 
                    Choose **+ Add MCP**.
- 
                    Choose **Local**as the connection type.
- 
                    Enter a **Name**and the**Command**to run (for example,`python`).
- 
                    Enter any **Arguments**the command requires (for example,`-m my_mcp_server`).
- 
                    Choose **+ Add MCP**to save.

### Import

Use the **Import** connection type to load
                MCP server configurations from an existing configuration file. This is
                useful when you already have MCP servers configured for other tools and
                want to reuse that configuration in Quick.

Quick supports configuration files from the following tools.

- Kiro 
- Claude Code 
- AIM 
- Antigravity 
- QuickWork exports 

The following table describes the fields for an Import MCP connection.

| Field | Required | Description | 
|---|---|---|
| Config file
                                path | Yes | The path to the configuration file on your machine
                                (for example, `~/.kiro/settings/mcp.json`). | 

When you enter a configuration file path, Quick automatically
                scans the file and detects the MCP servers defined in it.
                Quick also detects tools installed on your system and displays
                them as chips (for example, "Kiro", "AIM", "Claude Code") under
                **Detected on this system**.

###### To import MCP servers from a config file

Use the following procedure.

- 
                    Open **Settings**in the sidebar and choose**Capabilities**.
- 
                    Choose the **MCP**tab.
- 
                    Choose **+ Add MCP**.
- 
                    Choose **Import**as the connection type.
- 
                    Enter the **Config file path**to your existing MCP configuration file.
- 
                    Review the detected servers and system tools. 
- 
                    Choose **Load file**to import the servers.

### Remote

Use the **Remote** connection type to
                connect to an MCP server running on a remote machine or cloud service over
                HTTP. This is useful for shared team servers or hosted MCP
                services.

The following table describes the fields for a Remote MCP connection.

| Field | Required | Description | 
|---|---|---|
| Name | Yes | A friendly name to identify this MCP server. | 
| URL | Yes | The URL of the MCP endpoint (for example, `https://mcp.example.com/sse`). | 
| Token | No | A bearer token for authentication with the remote server. | 
| Description | No | A description of what this MCP server does and what tools it provides. | 
| Timeout
                                (seconds) | No | Maximum time to wait for the server to respond, from 5 to 300 seconds. The default is 30 seconds. | 

###### To add a remote MCP server

Use the following procedure.

- 
                    Open **Settings**in the sidebar and choose**Capabilities**.
- 
                    Choose the **MCP**tab.
- 
                    Choose **+ Add MCP**.
- 
                    Choose **Remote**as the connection type.
- 
                    Enter a **Name**and the**URL**of the MCP endpoint.
- 
                    (Optional) Enter a **Token**if the server requires authentication.
- 
                    Choose **+ Add MCP**to save.

## Managing MCP servers

        After you add MCP servers, they appear on the MCP tab. You can manage your servers using the following features.

- 
                **Search**– Use the search bar to find servers by name.
- 
                **Filter**– Use the dropdown filter to show all servers or filter by status.
- 
                **View toggle**– Switch between grid view and list view.
- 
                **Toggle**– Turn individual MCP servers on or off without removing them.
- 
                **Edit**– Modify server configuration.
- 
                **Remove**– Delete a server connection.

## Coding agents

        The MCP tab also includes a **Coding agents**
            section below the MCP servers. Coding agents use the Agent Client Protocol
            (ACP) to delegate coding tasks to local coding agents such as Kiro or Claude
            Code.

###### To add a coding agent

Use the following procedure.

- 
                Open **Settings**in the sidebar and choose**Capabilities**.
- 
                Choose the **MCP**tab.
- 
                In the **Coding agents**section, choose**+ Add Agent**.
- 
                Configure the agent connection settings. 
- 
                Save the configuration. 

After you configure a coding agent, you can delegate tasks to it from chat. For example, you can say "use Kiro to refactor this module" or "ask Claude Code to write tests for this function." Quick dispatches the work to the coding agent and reports the results back to you.

## Using MCP tools in scheduled agents

        You can attach MCP servers to scheduled agents as capabilities. When you create or edit a scheduled agent, you can select which MCP servers the agent has access to. This allows your automated agents to use custom tools when they run on their schedule.

To attach MCP capabilities to a scheduled agent, open the agent in
            **Settings** > **Capabilities** > **Scheduled
            tasks**, choose the **Capabilities** tab
            for that agent, and select the MCP servers you want to make available.

###### Note

MCP servers must be running and accessible when a scheduled agent attempts to use their tools. For local MCP servers, the server process starts automatically when needed. For remote servers, verify that the server is online and reachable.