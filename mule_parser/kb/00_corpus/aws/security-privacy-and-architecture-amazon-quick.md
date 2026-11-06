# Security, privacy, and architecture - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/desktop-security.html](https://docs.aws.amazon.com/quick/latest/userguide/desktop-security.html)

---

The Amazon Quick desktop application uses a local-first architecture designed to keep your data private while providing full access to AI capabilities. Your conversations, files, and personal context stay on your computer. The following sections describe how Amazon Quick on desktop handles security, privacy, and data storage.

###### Important

Your data is never used for AI model training. AWS does not use your conversations, files, or personal context to train or improve AI models.

## Local-first architecture

        The Amazon Quick desktop application runs most of its functionality locally on your computer. The following components run entirely on your machine.

- 
                **AI agent backend**– The agent runtime, including tool execution, skill loading, and task orchestration, runs as a local process on your machine.
- 
                **Conversation history**– All chat messages, threads, and conversation metadata are stored and persisted locally.
- 
                **Knowledge graph**– The entity graph that captures people, projects, customers, channels, events, and their relationships is built and queried locally.
- 
                **Memory**– Learned facts, procedures, and preferences that personalize your experience are stored locally.
- 
                **File indexing**– Keyword indexes, semantic search indexes, and knowledge graph extraction for your local folders are built and maintained on your machine.
- 
                **Scheduled agents**– Background agents that run on recurring schedules execute locally. Your computer must be on and Quick must be running for agents to operate.
- 
                **Artifacts and outputs**– Documents, images, visualizations, and other outputs that Quick generates are saved locally.

All Amazon Quick desktop application data is stored locally in the
            `~/.quickwork/` directory on macOS or
            `%USERPROFILE%\.quickwork\` on Windows. The following
            table describes the data stored in this directory.
        

## Data storage

        All Amazon Quick desktop application data is stored locally in the
            `~/.quickwork/` directory on your computer. The following
            table describes the data stored in this directory.

| Data type | Description | 
|---|---|
| Conversations | Chat messages, threads, and conversation metadata. | 
| Knowledge graph | Entity graph database containing people, projects, customers, channels, events, and relationships. | 
| Memory | Learned facts, procedures, tool strategies, and user preferences with confidence scores. | 
| File indexes | Keyword search indexes and semantic search embeddings for granted folders. | 
| Agent configurations | Scheduled agent definitions, schedules, prompts, and execution history. | 
| Credentials | Saved authentication tokens for connected third-party services. | 
| Artifacts | Downloaded files, generated documents, images, and other outputs. | 
| Application settings | User preferences, theme selection, and configuration state. | 

## Folder permissions

        Amazon Quick on desktop uses OS-level sandboxing to control file access. Quick can only access folders that you explicitly grant permission to, and you can revoke access at any time. Each folder supports independent controls for keyword search indexing, semantic search indexing, and knowledge graph extraction. You can also set granular per-operation permissions for read and write operations.

To manage folder access and permissions, see
            [My Computer](./desktop-settings.html#desktop-settings-my-computer).

## System tool permissions

        Amazon Quick on desktop includes system tools that provide core capabilities.
            Each tool can be individually toggled on or off and supports a three-tier
            permission model (Full Access, Read Only, or Ask Each Time) with granular
            per-operation controls. For a complete list of system tools and their
            permissions, see [System tools](./system-tools-desktop.html).

## Connection security

        Amazon Quick on desktop uses industry-standard security practices for third-party service connections.

- 
                **OAuth 2.0**– Services such as Slack, Google, and Microsoft use OAuth 2.0 for authentication. Quick redirects you to the service's sign-in page, and the service returns an authorization token. Quick never sees or stores your third-party passwords.
- 
                **Independent connections**– Each connected service is managed independently. You can disconnect and reconnect any service at any time from**Settings**>**Capabilities**>**Connections**without affecting other connections.
- 
                **Minimal permissions**– Quick requests only the permissions needed to provide its features for each connected service.

## Privacy controls

        Amazon Quick on desktop provides privacy controls that let you manage whether
            Quick learns from your conversations, searches your conversation
            history, and extracts entities from connected services. You can also view, edit,
            and delete individual memories. To configure privacy settings, see
            [My Context](./desktop-settings.html#desktop-settings-my-context).

## Clearing all data

        If you need to completely reset Amazon Quick on desktop, you can use the
            **Clear all data** option in **Settings** > **Customization** >
            **Danger zone**. This action is irreversible and
            removes all conversations, knowledge graph data, saved credentials, and user
            preferences. For more information, see
            [Danger zone](./desktop-settings.html#desktop-settings-danger-zone).