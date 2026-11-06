# Understanding the desktop interface - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/desktop-interface.html](https://docs.aws.amazon.com/quick/latest/userguide/desktop-interface.html)

---

The Amazon Quick desktop application interface is organized into a sidebar for navigation, a top bar with panel toggles, and a main content area. You use the sidebar to access core features and manage your settings, and the top bar to open overlay panels for your activity feed, agents, tasks, and connected data sources.

## Sidebar navigation

        The sidebar on the left side of the application provides quick access to all main areas. The sidebar is divided into three sections: primary navigation at the top, chat history in the middle, and settings at the bottom.

### Primary navigation

The following table describes each item in the primary navigation section of the sidebar.

| Sidebar item | Icon | Description | 
|---|---|---|
| New chat | Pencil | Starts a new chat conversation with a clean context. | 
| Activity feed | Lightning bolt | Opens the activity feed, which displays a unified, prioritized stream of items from your connected services. | 
| My stuff | Bar chart | Opens your artifact library, where you can browse, search, and reuse documents, images, code snippets, and other outputs that Amazon Quick generates during your conversations. | 
| More | People/group | Expands a menu with additional features. For more information, see the following section. | 

### More menu

When you choose **More** in the sidebar, a popup
                menu appears with the following items. The items open Amazon Quick in the web 
                browser for features available in the web experience.

| Menu item | Description | 
|---|---|
| Automations | Opens the automations interface for creating and managing automated workflows. | 
| Chat agents | Opens the list of available chat agents for specialized conversational tasks. | 
| Research | Opens the Research interface for deep analysis and structured investigation across multiple research tracks. | 
| Flows | Opens the Flows interface for creating multi-step automated workflows. | 
| Spaces | Opens your Quick Web Spaces for accessing shared team knowledge and curated content collections. | 
| Dashboards | Opens the Dashboards interface for viewing data visualizations and summary views. | 

### Recents

Below the primary navigation, the **Recents**
                section displays your previous conversations organized by date. The Recents
                section includes the following controls.

| Control | Icon | Description | 
|---|---|---|
| Export | Folder with arrow | Export or manage conversation archives. | 
| Search | Magnifying glass | Search across your conversations, artifacts, and connected data sources. | 

You can organize your conversations into folders, pin important conversations, and delete conversations you no longer need.

### Settings

The **Settings** section is an expandable area at
                the bottom of the sidebar. When expanded, it displays the following
                sub-pages.

| Settings sub-page | Description | 
|---|---|
| Capabilities | Manage connections, skills, scheduled tasks, MCP servers, and system tools. | 
| My computer | Configure local file access, folder permissions, and search indexing. | 
| My context | View and manage your knowledge graph and memory settings. | 
| Customization | Adjust appearance, notifications, browser, voice, performance, and other preferences. | 

For more information about settings, see
                [Settings](./desktop-settings.html).

## Top bar panels

        The top bar on the right side of the application contains panel toggles that open overlay panels. These panels provide quick access to key features without leaving your current view.

The following table describes each panel toggle.

| Panel toggle | Description | 
|---|---|
| Feed | Opens the activity feed panel on the right side of the application.
                            The feed panel displays prioritized items from your connected services
                            with AI-generated summaries and suggested action buttons. For more
                            information, see [Activity feed](#desktop-activity-feed). | 
| Agents | Opens the scheduled agents panel, where you can view your scheduled agents and quickly toggle them on or off without navigating to Settings. | 
| Tasks | Opens Mission Control, where you can view and manage background tasks, track progress on multi-step operations, and monitor parallel work. | 
| All data and apps | Opens a view of your connected data sources and applications, showing the status of each connection. | 

### Developer menu

The connection status indicator is a colored dot in the top-right corner of the application, to the right of the panel toggles. The color of the dot indicates the current connection status (green indicates connected).

When you choose the connection status dot, a developer menu appears with the following options.

| Option | Description | 
|---|---|
| Mission control | Opens the full Mission Control page for detailed task management and system monitoring. | 
| Metrics | Toggles a performance metrics overlay that displays real-time statistics about the application. | 
| Debug panel | Toggles a debug panel for viewing detailed diagnostic information during conversations. | 
| Memory | Toggles a memory panel that displays the agent's active memory and learned context for the current session. | 

## Home

        The Home screen is the first view you see when you open Amazon Quick on desktop. It provides a personalized starting point for your work.

### Personalized greeting

The Home screen displays a time-aware greeting that adapts to the time of day. For example, the greeting might say "Good morning" in the morning or "Burning the midnight oil?" late at night.

### Chat input

Below the greeting, the chat input area is where you start conversations with Amazon Quick. The chat input includes the following elements.

| Element | Description | 
|---|---|
| Persona selector | A dropdown at the top-left of the input area that displays the active persona (default: "Quick"). Choose to switch between different assistant personas. | 
| Text input field | The main text area where you type your messages. Placeholder text reads "Ask a question..." | 
| Attachment button (+) | Opens options to attach files, folders, or other content to your message. | 
| Model selector | Displays the current AI model mode (Fast, Balanced, Smart, or Auto). Choose to switch modes or adjust thinking effort. | 
| Equalizer | Opens audio and voice-related controls. | 
| Voice input | A microphone button for dictation. When Talkback mode is enabled, the icon changes to a waveform. | 

For more information about model modes and thinking effort, see
                [Working with chat](./working-with-chat-desktop.html).

### Connection setup cards

If you haven't connected your messaging or email accounts, the Home screen
                displays connection setup cards. Each card includes a brief description of the
                benefits of connecting and a **Connect** button with
                a dropdown for choosing your provider. You can choose
                **Dismiss** to hide a card.

The following connection cards might appear.

| Card | Description | 
|---|---|
| Email | "Calendar and email for meeting prep and action items." Connect your Outlook or Gmail account. | 
| Messaging | "Threads, DMs, and channels — triage what matters." Connect your Slack or Teams workspace. | 

### Priority feed widget

Below the connection cards, the Home screen displays a priority feed widget that shows the most important items from your connected services. The widget includes the following elements.

- 
                    A count of priority items (for example, "1 priority for now") 
- 
                    A **View feed**link to open the full activity feed
- 
                    Feed item cards with the item title and source, an **Importance tag**(for example, "Important") with color coding, an AI-generated summary,**Suggested action buttons**that you can choose to have Amazon Quick perform an action immediately, and a more options menu (three dots) for additional actions

## Activity feed

        The Activity feed provides a unified, prioritized stream of items from all your connected services. A built-in feed agent processes items from your connected messaging, email, and calendar sources and assigns importance levels to help you focus on what matters most.

### Accessing the activity feed

You can access the activity feed in the following ways.

- 
                    Choose **Activity feed**in the sidebar for the full-page view.
- 
                    Choose **Feed**in the top bar to open the feed as an overlay panel.
- 
                    View priority items in the Home screen feed widget. 

### Importance levels

Amazon Quick assigns one of the following importance levels to each feed item.

| Level | Description | 
|---|---|
| Important | Items that require your immediate attention, such as direct mentions, urgent requests, or time-sensitive updates. | 
| Informational | Items that are relevant to your work but don't require immediate action, such as project updates or team announcements. | 
| Low priority | Items that are nice to know but can be reviewed later, such as general channel activity or FYI messages. | 

### Feed item details

Each feed item includes the following information.

- 
                    **Source service**– The connected service the item came from (Slack, Outlook, Gmail, and so on)
- 
                    **AI-generated summary**– A concise summary of the item content
- 
                    **Importance tag**– A colored label indicating the importance level
- 
                    **Suggested actions**– Action buttons that Amazon Quick can perform on your behalf
- 
                    **Draft response**– When a reply is appropriate, Amazon Quick suggests a draft response

### Catch-up mode

When you return after being away, the activity feed provides a catch-up mode. Catch-up mode presents a consolidated summary of everything that happened while you were gone, organized by importance level, so you can quickly get up to speed.

### Configuring the activity feed

You can configure which integrations surface items to your activity feed and how
                often the feed agent checks for new activity. To configure the activity feed, go
                to **Settings**, choose
                **Customization**, and then choose
                **Activity feed**. For more information, see
                [Settings](./desktop-settings.html).

## Chat

        The Chat interface is where you interact with Amazon Quick using natural language. You can ask questions, request tasks, analyze files, create documents, generate visualizations, and work with your connected services through conversation.

### Chat input area

The chat input area at the bottom of the chat view includes the following controls.

| Control | Description | 
|---|---|
| Persona selector | Switch between different assistant personas. | 
| Spaces | Attach Quick Web Spaces to the conversation to give Amazon Quick access to shared team knowledge. | 
| Attachment (+) | Attach files, choose folders, or upload content to the conversation. | 
| Web search toggle | Turn on or turn off web search for the next query. When active, Amazon Quick searches the internet and includes citations. | 
| Model selector | Switch between Fast, Balanced, Smart, and Auto modes. Adjust thinking effort (Off, Low, Med, High, Max). | 
| Voice input | Use your microphone for dictation or hands-free Talkback mode. | 
| Cost display | Shows the token spend for the current conversation, helping you monitor usage. | 
| Send | Send your message. | 

### Conversation management

Amazon Quick on desktop persists your conversation history locally on your machine. You can organize, search, and manage your conversations using the following features.

- 
                    **Folders**– Organize conversations into custom folders for easy retrieval.
- 
                    **Pinning**– Pin important conversations so they appear at the top of your chat history.
- 
                    **Search**– Search across all conversations using the search icon in the Recents section.
- 
                    **Delete**– Remove conversations you no longer need.

## My Stuff

        My Stuff is your artifact library. It stores documents, images, code snippets, data visualizations, and other outputs that Amazon Quick generates during your conversations.

### Accessing My Stuff

To access My Stuff, choose **My stuff** in the
                sidebar.

### Working with artifacts

Artifacts are organized by type and date. You can perform the following actions with your artifacts.

- 
                    **Browse**– View all artifacts, filtered by type.
- 
                    **Search**– Search across all saved artifacts by name or content.
- 
                    **Reuse**– Reference artifacts from previous conversations in new chats.
- 
                    **Download**– Save artifacts to your local machine.
- 
                    **Delete**– Remove artifacts you no longer need.