# What is Amazon Quick on desktop? - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/what-is-desktop.html](https://docs.aws.amazon.com/quick/latest/userguide/what-is-desktop.html)

---

The Amazon Quick desktop application is a native desktop application that extends Amazon Quick from the browser to your computer. It provides the same AI-powered capabilities you use in the web experience, plus deep integration with your local files, system notifications, background processing, and advanced tools like browser automation and knowledge graph.

The desktop application uses a **local-first architecture**.
        The AI backend runs locally on your machine, and your files stay on your computer. The
        only network calls are to AI models through API Gateway and to your connected services (such as
        Slack, Outlook, or Gmail). This approach keeps your data private while giving you full
        access to Amazon Quick capabilities.

###### Note

The Amazon Quick desktop application is currently available as a preview.

###### Note

The Amazon Quick desktop application is available to both Free and Plus accounts and Professional and Enterprise accounts.

## Comparing Quick on the web with Amazon Quick on desktop

        The following table compares the features available in the Quick web experience with the Amazon Quick desktop application.

| Feature | Quick on web | Amazon Quick on desktop | 
|---|---|---|
| Chat with AI | Yes | Yes | 
| Local file access | Upload only | Direct folder access | 
| Background agents | No | Yes | 
| Proactive notifications | No | Yes | 
| Activity feed | No | Yes | 
| System tray integration | No | Yes | 
| Offline draft access | No | Yes | 
| Voice input | No | Yes | 
| Third-party integrations | Yes | Yes | 
| MCP server support | No | Yes | 
| Browser automation | No | Yes | 
| Knowledge graph | No | Yes | 
| Create and manage chat agents | Yes | No | 
| Create and manage spaces | Yes | No | 
| Account administration | Yes | No | 
| Dashboards and analytics | Yes | No | 

## Benefits of Amazon Quick on desktop

        The Amazon Quick desktop application provides the following benefits.

###### Note

The desktop application connects to the same Amazon Quick account you use on the web. Features available on both platforms work the same way. The desktop app adds capabilities that require native presence on your machine.

### Work with your local files directly

The desktop application can read, write, search, and index files in folders you grant access to. You don't need to upload files — Quick can access them directly from your file system. You control which folders Quick can access, and you can revoke access at any time. Per-folder options include keyword search indexing, semantic search indexing, and knowledge graph extraction.

###### Note

Quick also has access to system temporary directories
                    regardless of your folder permission settings. On Windows, these are
                    `C:\TEMP`, `C:\TMP`,
                    `\TEMP`, and `\TMP`. On macOS and
                    Linux, these are `/tmp`,
                    `/var/tmp`, and
                    `/usr/tmp`.

### Stay informed with proactive notifications

Background agents run on a schedule to monitor your connected services and surface what matters. The Activity feed provides a unified, prioritized stream of items from Slack, email, calendar, and other connected sources. Each feed item includes an AI-generated summary and suggested actions you can take with one click.

### Automate recurring tasks with scheduled agents

Create scheduled agents that run on your behalf at set intervals. Agents can monitor channels, triage emails, summarize meetings, track incidents, and more. Agents run locally on your machine and deliver results through the Activity feed or desktop notifications.

### Extend Quick with MCP servers and coding agents

Connect custom MCP (Model Context Protocol) servers to extend what Quick can do. The desktop application supports local MCP servers (run a command on your machine), imported configurations (from Kiro, Claude Code, AIM, or other tools), and remote MCP servers over HTTP. You can also configure coding agents using the Agent Client Protocol (ACP) to delegate coding tasks to local agents.

### Browse the web with browser automation

Quick can launch and control Chrome to browse the web, fill forms, take screenshots, extract data, and interact with web applications on your behalf. Two modes are available: a default mode that launches a separate Chrome instance with a copy of your profile, and a "Use my Chrome" mode that connects directly to your running Chrome with your logins, cookies, and extensions.

### Build a personal knowledge graph

Quick automatically extracts entities and relationships from your connected sources — Slack messages, emails, calendar events, and local files — and builds a personal knowledge graph. The graph visualizes people, customers, projects, events, channels, and other entities relevant to your work, helping Quick provide more contextual and personalized responses.

### Use voice for hands-free interaction

Speak to Quick using dictation mode (speech-to-text) or talkback mode (Quick reads responses aloud for a hands-free conversation). Configure voice settings including voice selection, speed, and a live mode that keeps the microphone open for continuous conversation.

### Run tasks in the background

Quick can spawn parallel background tasks for complex, multi-step work. Track progress in the Tasks panel (Mission Control), and continue working in chat while background tasks complete. This is useful for batch processing, parallel research, and multi-source analysis.

## Next steps

        To get started with the Amazon Quick desktop application, see
            [Getting started](./getting-started-desktop.html). If your organization uses a Professional
            or Enterprise account and your Quick desktop has not yet been configured,
            see [Setting up Amazon Quick on desktop for enterprise deployments](./desktop-enterprise-setup.html) first.