# Connecting your data sources - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/connecting-data-sources-desktop.html](https://docs.aws.amazon.com/quick/latest/userguide/connecting-data-sources-desktop.html)

---

You can connect multiple data sources to the Amazon Quick desktop application. When you connect a data source, Quick can access the information in that source to provide more relevant and personalized responses. Amazon Quick on desktop supports local file access, messaging platforms, email and calendar services, cloud storage, and business tools.

## Local files

        You can grant Quick access to specific folders on your machine. Quick can then read, search, write, and reference files in those folders during your conversations.

###### To grant folder access

- 
                In the sidebar, choose **Settings**.
- 
                Choose **My computer**.
- 
                In the **Local folders**section, choose**+ Add folder**.
- 
                Select the folder you want to grant access to. 

### Per-folder indexing options

After you add a folder, you can configure the following indexing options for each folder individually. Choose the expand arrow next to a folder name to view these options.

| Option | Description | 
|---|---|
| Keyword search | Builds a local keyword index of your file contents for fast text search. The status indicator shows the number of files indexed, entry count, index size, and last indexed time. | 
| Semantic search | Creates semantic embeddings of your file contents for meaning-based search. Returns results based on conceptual similarity, not just keyword matches. | 
| Knowledge graph extraction | Extracts entities, relationships, and structured information from your files and adds them to your personal knowledge graph. | 

### Search indexing settings

You can configure global search indexing limits in the
                **Search indexing** section of the My computer
                page.

| Setting | Description | 
|---|---|
| Storage limit | Maximum disk space for the knowledge database. Indexing pauses when this limit is reached. | 
| Max file size for indexing | Files larger than this size are skipped during indexing. Skipped files are still available to the agent through direct search. | 
| Max folder size for indexing | Folders whose total indexable content exceeds this limit are not ingested. You can increase the limit and retry. | 

###### Note

Indexing stops automatically when your free disk space falls below 8.0 GiB. All indexes are stored locally on your machine.

### What Quick can do with your local files

After you grant folder access, Quick can perform the following actions with your local files.

- 
                    Read and analyze files in supported formats (PDF, DOCX, PPTX, XLSX, images, code, text, and more) 
- 
                    Search across file contents using keyword or semantic search 
- 
                    Create new files and save them to your granted folders 
- 
                    Edit existing files 
- 
                    Move, copy, and organize files 
- 
                    Reference file contents when answering your questions 

## Online services

        Amazon Quick on desktop provides built-in connections for services such as Slack, Microsoft Outlook, Microsoft Teams, Gmail, Google Calendar, Google Meet, Microsoft OneDrive, Microsoft SharePoint, Google Drive, Google Docs, Google Sheets, Google Slides, Dropbox, Google Analytics, Airtable, QuickBooks, Zoom, and Zapier. Additional connections are available through Quick on the web.

###### To connect a service

- 
                In the sidebar, choose **Settings**.
- 
                Choose **Capabilities**.
- 
                On the **Connections**tab, find the service you want to connect and choose**Sign in**.
- 
                Complete the authentication flow for that service. 

To browse and add connections beyond the built-in services, choose
            **Browse connections** at the bottom of the Connections
            tab. This opens Quick on the web, where you can discover additional
            integrations. Connections added on the web appear automatically in the desktop
            application.

###### Tip

You can also extend the capabilities of Quick by adding custom MCP
                (Model Context Protocol) servers. For more information, see
                [Configuring MCP servers](./mcp-servers-desktop.html).

## Additional data sources

        The Amazon Quick desktop application supports additional connections beyond the built-in services. You can browse and add more connections through Quick on the web, including project management tools, CRMs, developer platforms, and more. Connections added on the web appear automatically in the desktop application.

To browse additional connections, open **Settings**,
            choose **Capabilities**, and choose
            **Browse connections** at the bottom of the
            **Connections** tab.

## Connection management

         
            ### Viewing your connections

All connections are managed from **Settings** >
                **Capabilities** >
                **Connections**. The Connections tab provides the
                following tools.

- 
                    **Search bar**– Search for a specific connection by name.
- 
                    **Filter dropdown**– Filter connections by status (All, Connected, Available).
- 
                    **Pagination**– Browse through pages of available connections.

### Disconnecting a service

To disconnect a service, navigate to **Settings**
                > **Capabilities** >
                **Connections**, find the connected service, and
                choose the disconnect option. Quick immediately stops accessing data
                from that service.

### Connection status

Each connection displays its current status.

| Status | Description | 
|---|---|
| Sign in | The service is available but not connected. Choose Sign into connect. | 
| Connected | The service is connected and syncing data. | 
| Not synced | The connection exists but data is not syncing. Try disconnecting and reconnecting. | 

### Activity feed integration

After you connect messaging, email, or calendar services, you can configure which services surface items in your activity feed.

###### To configure feed sources

- 
                    In the sidebar, choose **Settings**.
- 
                    Choose **Customization**.
- 
                    In the **Activity feed**section, select the integrations you want to include:- 
                            **Messaging**– Slack DMs & Mentions, Teams Messages & Mentions
- 
                            **Mail**– Outlook Email, Gmail
- 
                            **Calendar**– Outlook Calendar, Google Calendar
 
- 
                            
- 
                    Set the **Check frequency**to control how often the feed agent checks for new activity (for example, every 15 minutes).