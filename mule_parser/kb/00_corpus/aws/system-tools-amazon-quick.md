# System tools - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/system-tools-desktop.html](https://docs.aws.amazon.com/quick/latest/userguide/system-tools-desktop.html)

---

The Amazon Quick desktop application includes built-in system tools that provide core capabilities such as web search, file operations, browser automation, image generation, and more. You can individually enable or disable each system tool and configure granular permission controls that determine how much access Quick has for each operation.

You manage system tools in **Settings** >
        **Capabilities** > **System**.

## Managing system tool permissions

        Each system tool has a toggle to enable or disable it and a **Manage permissions** button that opens a detailed
            permission panel.

### Access levels

When you choose **Manage permissions** on a
                system tool, you can set one of the following three access levels.

| Access level | Description | 
|---|---|
| Full Access(Read & write) | Quick has full read and write access to this capability. Operations run without prompting you for confirmation. | 
| Read Only(View only) | Quick can perform read operations but cannot modify, write, or delete data through this tool. | 
| Ask Each Time(Confirm all) | Quick asks for your confirmation before performing any operation with this tool. | 

### Per-operation permissions

Below the access level, each tool lists its individual operations grouped
                into **Read Operations** and **Write Operations** (where applicable). Each
                operation has its own permission dropdown that you can set independently.
                For example, you might set the overall access level to **Full Access** but restrict a specific write operation to
                **Ask Each Time**.

### To manage permissions for a system tool

- 
                    Open **Settings**and choose**Capabilities**.
- 
                    Choose the **System**tab.
- 
                    Find the tool you want to configure. 
- 
                    Choose **Manage permissions**next to the tool.
- 
                    Set the **Access Level**to your preferred level.
- 
                    (Optional) Adjust individual operation permissions in the **Read Operations**and**Write Operations**sections.
- 
                    Close the panel. Changes take effect immediately. 

## Available system tools

        The following sections describe each of the built-in system tools.

### Web Search

Web Search enables Quick to find up-to-date information from the internet when responding to your messages. When web search is active in a conversation, Quick includes citations from the web sources it references.

| Operation | Type | Description | 
|---|---|---|
| Web search | Read | Search the web and return an AI-generated summary of results. | 
| Fetch URL | Read | Fetch and read the full content of a specific web page. | 

**When to use** – Enable this tool
                when you want Quick to supplement its responses with current
                information from the internet. You can also toggle web search on a
                per-conversation basis using the web search icon in the chat input
                area.

### File operations

File operations enables Quick to download files from URLs and open local files in their associated applications on your computer.

| Operation | Type | Description | 
|---|---|---|
| Download file | Write | Download a file from a URL to your local machine. | 
| Open file | Write | Open a local file in its default application (for example, open a PDF in Preview). | 

**When to use** – Enable this tool
                when you want Quick to download files from the web or open
                generated documents in their native applications for review.

### Browser Automation

Browser Automation gives Quick the ability to launch a Chrome browser, navigate to websites, interact with elements, fill in forms, take screenshots, and extract text. This tool is useful for tasks that require interacting with web applications or extracting information from websites.

Browser Automation supports the following two modes of operation.

- 
                    **Default mode**– Quick launches a separate Chrome instance with a copy of your Chrome profile. This preserves your saved logins and cookies while keeping the automation session isolated from your main browser.
- 
                    **Use my Chrome mode**– Quick connects directly to your running Chrome browser with your live logins, cookies, and extensions. To enable this mode, go to**Settings**>**Customization**>**Browser**, toggle**Use my Chrome**, and follow the setup steps to enable remote debugging.

| Operation | Type | Description | 
|---|---|---|
| Navigate | Read | Open a URL and return page content. | 
| Click | Write | Choose interactive elements on a web page. | 
| Type | Write | Enter text into input fields and editors. | 
| Screenshot | Read | Capture a screenshot of the current page. | 
| Extract text | Read | Extract text content from a page or element. | 
| Run JavaScript | Write | Run JavaScript in the page context. | 
| Download | Write | Download files through the browser. | 

**When to use** – Enable this tool
                when you want Quick to interact with web applications on your
                behalf, such as filling out forms, navigating internal tools, or extracting
                information from websites.

### Image Generation

Image Generation enables Quick to generate, edit, and manipulate images using Amazon Nova Canvas models. You can describe the image you want in natural language, and Quick generates it directly in your conversation.

Image Generation supports the following capabilities.

- 
                    **Generate image**– Create a new image from a text description.
- 
                    **Remove background**– Remove the background from an existing image.
- 
                    **Edit image**– Modify specific parts of an existing image based on instructions.
- 
                    **Image variation**– Create variations of an existing image.
- 
                    **Outpaint image**– Extend an image beyond its original borders.

| Operation | Type | Description | 
|---|---|---|
| Generate | Write | Generate a new image from a text prompt. | 
| Edit | Write | Edit or transform an existing image. | 

Generated images appear as artifacts in your conversation that you can
                save to your local machine or to your **My
                Stuff** library.

**When to use** – Enable this tool
                when you want Quick to create or edit images, generate
                illustrations, remove backgrounds, or produce image variations.

### Code Execution

Code Execution enables Quick to write and run Python code in a sandboxed environment on your machine. Quick uses this capability for data analysis, calculations, file processing, chart generation, and automation tasks.

Code Execution has the following key characteristics.

- 
                    Code runs in an **OS-level sandbox**(macOS Seatbelt or Windows AppContainer) for security.###### NoteThe sandbox also has access to the system temporary directories regardless of your folder permission settings. On Windows, these are `C:\TEMP`,`C:\TMP`,`\TEMP`, and`\TMP`. On macOS and Linux, these are`/tmp`,`/var/tmp`, and`/usr/tmp`.
- 
                    A **persistent namespace**is maintained across code runs within a conversation, so variables and functions carry over.
- 
                    Pre-installed Python packages are available. Package installation ( `pip install`) is not supported within the sandbox.
- 
                    File access within the sandbox follows the same folder permissions you configure in **Settings**>**My computer**. In addition, the sandbox always has access to system temporary directories. On Windows, these are`C:\TEMP`,`C:\TMP`,`\TEMP`, and`\TMP`. On macOS and Linux, these are`/tmp`,`/var/tmp`, and`/usr/tmp`.

| Operation | Type | Description | 
|---|---|---|
| Execute code | Write | Run Python code and return the output. | 

**When to use** – Enable this tool
                when you want Quick to perform calculations, analyze data,
                generate charts, process files, or automate tasks using Python.

### Engram Builder

The Engram Builder enables Quick to analyze your writing patterns across messages and conversations to create a personality profile (called an engram). Quick can then use this profile to write in your style, matching your tone, vocabulary, sentence structure, and communication patterns.

| Operation | Type | Description | 
|---|---|---|
| Get engram | Read | Retrieve a saved personality engram. | 
| List engrams | Read | List all available personality engrams. | 
| Save engram | Write | Save a new personality engram. | 
| Delete engram | Write | Delete a saved personality engram. | 

**When to use** – Enable this tool
                when you want Quick to learn your writing style and produce
                content that matches how you communicate. This is useful for drafting
                emails, messages, or documents in your voice.

### Knowledge & Memory

Knowledge & Memory enables Quick to access and build your personal knowledge graph, search for entities and relationships, and recall information it has learned from your conversations.

This tool provides the following key capabilities.

- 
                    **Knowledge graph queries**– Search for people, projects, customers, events, and other entities, and explore their relationships.
- 
                    **Graph building**– Add new entities and relationships to your knowledge graph from conversations.
- 
                    **Memory recall**– Retrieve learned facts, preferences, and patterns from previous conversations to provide more personalized responses.
- 
                    **Entity resolution**– Identify and connect references to the same person or entity across different sources.

| Operation | Type | Description | 
|---|---|---|
| Search | Read | Search the knowledge graph for entities and relationships. | 
| Add | Write | Add new entities or relationships to the knowledge graph. | 
| Edit | Write | Modify existing entities or relationships. | 
| Schema | Read | View the knowledge graph schema and entity types. | 
| Stats | Read | Get knowledge graph statistics (nodes, edges, entities, files). | 
| Build | Write | Build or rebuild knowledge graph structures. | 

**When to use** – Enable this tool
                when you want Quick to use its knowledge of your work
                context — people, projects, meetings, and relationships — to
                provide more relevant and personalized responses.

### Agent Management

Agent Management enables Quick to create, update, delete, and trigger scheduled agents programmatically during conversations. This is the tool that powers the ability to set up automated monitoring and recurring tasks when you ask for them in chat.

| Operation | Type | Description | 
|---|---|---|
| List agents | Read | List all scheduled agents and their configurations. | 
| Create agent | Write | Create a new scheduled agent with instructions and schedule. | 
| Update agent | Write | Modify an existing agent's instructions, schedule, or capabilities. | 
| Delete agent | Write | Remove a scheduled agent. | 
| Trigger agent | Write | Manually run a scheduled agent immediately. | 

**When to use** – Enable this tool
                when you want Quick to create and manage scheduled agents on
                your behalf through natural language requests in chat (for example,
                "Monitor my Slack channels every morning and summarize important
                messages").

### Task Management

Task Management enables Quick to break complex requests into multiple parallel sub-tasks, each running as an independent background agent. This is the capability behind the ability to handle multi-step, parallel workloads efficiently.

This tool provides the following key capabilities.

- 
                    **Sub-task spawning**– Break a complex request into independent tasks that run in parallel.
- 
                    **Task groups**– Organize related tasks into groups for coordinated execution.
- 
                    **Progress tracking**– Monitor the status and progress of running tasks through the**Tasks**panel in the top bar.
- 
                    **Workflow orchestration**– Chain tasks together where the output of one task feeds into the next.

| Operation | Type | Description | 
|---|---|---|
| Create task | Write | Spawn a new background sub-task. | 
| List tasks | Read | List active and completed tasks. | 
| Cancel task | Write | Cancel a running task. | 
| Get task result | Read | Retrieve the result of a completed task. | 

**When to use** – Enable this tool
                when you want Quick to handle complex, multi-part requests
                efficiently by breaking them into parallel workstreams. This is especially
                useful for batch processing, multi-source research, and large-scale
                document operations.

### Chat & Notifications

Chat & Notifications enables Quick to enhance the chat experience with interactive elements and proactive communication features.

This tool provides the following key capabilities.

- 
                    **Suggestion pills**– Quick surfaces contextual action suggestions as clickable pills below messages, making it easy to take next steps.
- 
                    **Message reactions**– Interactive response elements within the chat interface.
- 
                    **Notifications**– System notifications for agent completions, connection updates, and other events. Configure notification preferences in**Settings**>**Customization**>**Notifications**.
- 
                    **Briefings**– Proactive summaries and morning briefs that appear on the Home screen, highlighting your priorities for the day.

| Operation | Type | Description | 
|---|---|---|
| Send notification | Write | Send a desktop notification to the user. | 
| Create suggestion | Write | Generate suggestion pills for contextual next actions. | 

**When to use** – Enable this tool
                when you want Quick to proactively surface suggestions, send
                notifications about completed tasks, and provide briefing
                summaries.

## Summary of system tools

        The following table lists all built-in system tools and their default state.

| Tool | Description | Default state | 
|---|---|---|
| Web Search | Search the internet for current information | Enabled | 
| File operations | Download files and open in default application | Enabled | 
| Browser Automation | Browse and interact with web pages using Chrome | Enabled | 
| Image Generation | Create and edit images with Amazon Nova Canvas | Enabled | 
| Code Execution | Run Python code for calculations and automation | Enabled | 
| Engram Builder | Build personality engrams for writing style cloning | Enabled | 
| Knowledge & Memory | Query knowledge, build graphs, recall patterns | Enabled | 
| Agent Management | Create and manage scheduled agents | Enabled | 
| Task Management | Spawn sub-tasks and orchestrate parallel work | Enabled | 
| Chat & Notifications | Reactions, suggestions, notifications, briefings | Enabled | 

###### Note

All system tools are enabled by default with **Full
                Access** permissions. You can restrict or disable any tool at any
                time. Changes take effect immediately for new conversations and agent
                runs.