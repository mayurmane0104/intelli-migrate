# Settings - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/desktop-settings.html](https://docs.aws.amazon.com/quick/latest/userguide/desktop-settings.html)

---

You can configure the Amazon Quick desktop application through the **Settings** panel. To open Settings, choose the gear icon at the
        bottom of the sidebar. Settings are organized into four categories: **Capabilities**, **My computer**,
        **My context**, and **Customization**.

## Capabilities

        The Capabilities settings control the tools, integrations, and extensions
            available to Quick. The Capabilities page is organized into four
            tabs: **Connections**, **Skills**, **MCP**, and **System**.

To open Capabilities, choose **Settings** in the
            sidebar and then choose **Capabilities**.

### Connections tab

The Connections tab is where you connect messaging, email, cloud storage, and other external services to Quick. When you connect a service, Quick can access the information in that service to provide more relevant and personalized responses.

#### Authentication

At the top of the Connections tab, the **Authentication** section displays your sign-in status.
                    Quick uses Amazon Federate for Bedrock and
                    Quick Web access. You must be signed in to use AI models
                    and access Quick Web features.

To sign out, choose **Sign out** in the
                    Authentication section.

#### Built-in connections

Quick provides connections to popular services.
                    Each connection has a **Sign
                    in** button that opens a sign-in page for the service and
                    returns you to Quick automatically.

You can use the **Search connections**
                    bar and **filter dropdown** to find
                    specific connections.

#### Browse more connections

Below the built-in connections, the **Browse more
                    connections** section provides a link to Quick on
                    the web, where you can browse and add additional connections such as
                    project management tools, CRMs, and developer platforms. Connections
                    added on the web appear automatically in the desktop
                    application.

### Skills tab

The Skills tab lets you view, create, and manage skills. You can create
                custom skills with AI or by uploading a `SKILL.md` file, and
                you can toggle built-in skills on or off. For more information about
                skills, see [Skills and agents](./skills-and-agents-desktop.html).

### MCP tab

The MCP (Model Context Protocol) tab lets you connect custom MCP servers
                to extend Quick capabilities with additional tools. You can add
                local, imported, or remote MCP servers, and configure coding agents. For
                more information, see [Configuring MCP servers](./mcp-servers-desktop.html).

### System tab

The System tab displays the built-in system tools that provide core
                capabilities to Quick. Each tool has an enable/disable toggle
                and a **Manage permissions** button for
                granular access control. For more information, see
                [System tools](./system-tools-desktop.html).

## My Computer

        The My Computer settings control how Quick accesses and indexes files on your local machine.

To open My Computer, choose **Settings** in the
            sidebar and then choose **My computer**.

At the top of the page, the **My computer** card
            shows the connection status. Choose the three-dot menu next to the card to
            access **Manage permissions**.

### Manage permissions

The Manage Permissions panel provides granular control over file operations. It includes the following controls.

- 
                    **Access Level**– Choose Full Access (Read & write), Read Only (View only), or Ask Each Time (Confirm all).
- 
                    **Read Operations**(10 operations) – File Read, Fdfind, Folder List, File Read Image, File Read Pdf, File Read Docx, File Read Pptx, File Get Page Raster, File Rag Search, File Rag Status.
- 
                    **Write Operations**(6 operations) – File Write, File Edit, File Move, File Copy, File Delete, Folder Create.

Each operation has its own permission dropdown that you can set independently.

### Local folders

The **Local folders** section lists the
                folders you have granted Quick access to. For each folder, the
                following information and options are displayed.

- 
                    **Folder name and path**– The name and full path of the folder.
- 
                    **File count**– The number of files in the folder.
- 
                    **Last indexed**– When the folder was last indexed.

Each folder has three indexing options that you can toggle independently.

| Option | Description | 
|---|---|
| Keyword
                                search | Builds a keyword index of file contents for fast text search. When enabled, displays the index status (Ready or Indexing), file count, entry count, and index size. | 
| Semantic
                                search | Builds a semantic (vector) index of file contents for meaning-based search. | 
| Knowledge graph
                                extraction | Extracts entities and relationships from files and adds them to your personal knowledge graph. | 

To add a new folder, choose **+ Add
                folder** at the bottom of the Local folders section.

### Search indexing

The **Search indexing** section displays
                storage metrics and lets you configure indexing limits.

- 
                    **Disk space bar**– Shows your current free disk space. Indexing automatically stops when free space falls below 8.0 GiB.
- 
                    **Local folder and graph storage**– Shows how much storage is used by indexes and graph data.
- 
                    **Storage limit**– Slider that sets the maximum disk space for the knowledge database. Indexing pauses when this limit is reached.
- 
                    **Max file size for indexing**– Slider that sets the maximum size of individual files to index. Files larger than this are skipped during indexing but are still available to the agent through direct search.
- 
                    **Max folder size for indexing**– Slider that sets the maximum total indexable content for a folder. Folders exceeding this limit are not ingested. You can increase the limit and retry.

## My Context

        The My Context settings manage how Quick builds and uses knowledge
            about you and your work. The page has two tabs — **Knowledge graph** and **Memory** —
            and a **Configuration** button in the upper-right
            corner.

To open My Context, choose **Settings** in the
            sidebar and then choose **My context**.

### Knowledge graph tab

The Knowledge graph tab displays an interactive visualization of the
                entities and relationships that Quick has extracted from your
                connected data sources. You can search, browse, and explore entities and
                their connections. For more information, see
                [Knowledge graph](./knowledge-graph-desktop.html).

### Memory tab

The Memory tab displays the facts, procedures, and patterns that Quick has learned from your conversations.

The following table describes the filtering and search controls.

| Control | Description | 
|---|---|
| All typesdropdown | Filter by memory type (facts, procedures). | 
| All categoriesdropdown | Filter by category (source, tool-strategy, profile). | 
| Sortdropdown | Sort by Recent or other criteria. | 
| Semantic
                                search | Search memories by meaning, not just keywords. | 
| +Inferredcheckbox | Include or exclude inferred memories. | 
| Reset | Clear all filters. | 

Each memory card displays the following information.

- 
                    **Type tag**–`fact`or`procedure`.
- 
                    **Category tag**– Such as`source`,`tool-strategy`, or`profile`.
- 
                    **Description**– The content of the memory.
- 
                    **Certainty percentage**– How confident Quick is in this memory.
- 
                    **Usage counts**– Views, confirmations, and rejections.
- 
                    **Actions**– Edit (pencil icon), upvote (arrow up), downvote (arrow down), and delete (x).

### Configuration

Choose **Configuration** in the upper-right
                corner to open the Configuration panel. This panel contains settings that
                apply to both the Knowledge graph and Memory tabs.

###### Memory

**Enable memory** – Toggle to
                    allow Quick to learn from conversations and personalize
                    future interactions.

###### Privacy

**Allow Quick to search and
                    reference past conversations** – Toggle to control
                    whether Quick can search your conversation history to
                    provide more relevant answers.

###### Knowledge graph

The knowledge graph section displays the following settings.

- 
                    **Stats**– Displays the current counts for Nodes, Edges, Entities, and Files in your knowledge graph.
- 
                    **Auto-ingest from integrations**– Toggle to automatically extract entities from your connected integrations into the knowledge graph. When enabled, you can control ingestion per source (Slack, Email, Other).

###### Search indexing

The Configuration panel also includes the same search indexing settings found in My Computer: disk space monitoring, storage limit, max file size for indexing, and max folder size for indexing.

## Customization

        The Customization settings let you personalize the appearance and behavior of the Amazon Quick desktop application.

To open Customization, choose **Settings** in the
            sidebar and then choose **Customization**.

### Appearance

Choose your preferred color theme for the application interface.

| Theme | Description | 
|---|---|
| System | Follow OS setting. Automatically matches your operating system's light or dark mode. | 
| Light | Always light. | 
| Dark | Always dark. | 
| Kiro Light | Purple and warm light theme. | 
| Kiro Dark | Purple and deep dark theme. | 

### Notifications

Control how you receive notifications from Quick.

- 
                    **Desktop notifications**– Toggle to show OS-level notifications when the app is in the background. Notifications include agent completions, connection updates, and other events.

### Activity Feed

Choose which integrations surface items to your activity feed.

| Category | Sources | 
|---|---|
| Messaging | Slack — DMs & Mentions, Teams —
                                Messages & Mentions. Choose Connect Slack or Teamsto
                                connect. | 
| Mail | Outlook Email, Gmail. Choose Connect Outlook or Gmailto
                                connect. | 
| Calendar | Outlook Calendar, Google Calendar. Choose Connect Outlook or Google
                                Calendarto connect. | 

**Check frequency** – How often the
                feed agent checks for new activity (for example, Every 15
                minutes).

### Browser

Configure how the agent browses the web. Quick can use a browser to navigate web pages, interact with content, fill forms, and take screenshots on your behalf.

**Use my Chrome** – Toggle to connect
                the agent to your running Chrome browser. When enabled, the agent uses your
                existing logins, cookies, and extensions.

When you enable **Use my Chrome**, follow
                these setup steps.

- 
                    Open Chrome and paste the following URL in the address bar: `chrome://inspect/#remote-debugging`
- 
                    Choose **Enable remote debugging**.
- 
                    Return to Quick and choose **Test Connection**to verify the connection.

###### Important

Enabling remote debugging allows any application running on your computer to connect to Chrome and access open pages, cookies, and authenticated sessions. Disable remote debugging when you are not actively using this feature.

When **Use my Chrome** is disabled, the
                agent launches a separate Chrome instance with a copy of your Chrome
                profile.

### Message submit keybinding

Choose which keyboard shortcut submits messages in chat.

**Submit key** – Choose the key that
                sends a message. Default is **Enter** (Enter
                submits the message, Shift+Enter creates a new line).

### Performance

Configure task parallelism and resource usage.

**Max parallel tasks** – Slider from
                1 to 50 (default: 50). Sets the maximum number of concurrent extraction
                tasks for batch operations.

### Voice

Manage voice input and output settings for hands-free interaction with Quick.

**Enable toggle** – Master toggle to
                enable or disable voice features.

###### Dictation

How you speak to the assistant.

- 
                    **Microphone**– Choose the microphone to use for voice input. Default is**System default**.
- 
                    **Advanced**– Expand for additional dictation settings.

###### Talkback

Read responses aloud and keep the microphone open for a hands-free conversation.

- 
                    **Voice**– Choose the voice for spoken responses. Use the play button to preview the selected voice.
- 
                    **Speed**– Slider to adjust speech speed. Speed effect might vary by voice.
- 
                    **Live mode**– Toggle to keep the microphone on while the assistant speaks. Say 3 or more words to interrupt.

### Troubleshooting

Export diagnostic logs for troubleshooting issues.

**Export diagnostics** – Save
                diagnostic logs to your desktop for troubleshooting. Choose a time range
                from the dropdown (for example, **Last 2
                hours**) and then choose **Export
                Diagnostics**.

### Danger zone

Irreversible actions that affect all your data.

**Clear all data** – Removes all
                Quick data including conversations, cached messages, knowledge
                graph, saved credentials, and user preferences. The application quits after
                cleanup.

###### Warning

Clearing all data is irreversible. All your conversations, memories, knowledge graph data, and saved credentials are permanently deleted.

To fully uninstall Quick, clear all data first, then drag
                `Amazon Quick.app` to Trash.