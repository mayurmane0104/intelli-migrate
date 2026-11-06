# Knowledge graph - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/knowledge-graph-desktop.html](https://docs.aws.amazon.com/quick/latest/userguide/knowledge-graph-desktop.html)

---

The Amazon Quick desktop application builds a personal knowledge graph that captures entities and relationships from your connected data sources. The knowledge graph gives Quick contextual understanding of the people, projects, organizations, and events in your work, so it can provide more relevant and personalized responses.

## What is the knowledge graph?

        The knowledge graph is a structured representation of your professional context. Quick automatically extracts entities (such as people, companies, projects, and events) and the relationships between them from your connected sources. This information is stored locally on your machine and used to enrich the understanding of Quick when you ask questions about your work.

For example, if you ask "What's the latest on Project Meridian?", Quick can use the knowledge graph to identify related people, recent meetings, associated documents, and relevant Slack channels — all without you needing to specify those connections explicitly.

## Entity categories

        Quick organizes knowledge graph entities into the following categories.

| Category | Description | Examples | 
|---|---|---|
| Person | People you interact with across your connected services. | Colleagues, managers, external contacts | 
| Customer | Organizations and companies referenced in your communications. | Client companies, partner organizations | 
| Channel | Communication channels from your messaging integrations. | Slack channels, Teams channels | 
| Event | Meetings, incidents, milestones, and other time-bound occurrences. | Board meetings, incidents, project launches | 
| Creative Work | Documents, presentations, reports, and other created content. | User guides, launch training decks, architecture docs | 
| Project | Projects and initiatives referenced across your sources. | Product launches, migration efforts, platform initiatives | 
| Action | Tasks, action items, and follow-ups extracted from conversations and meetings. | Review requests, sign-offs, deliverables | 
| Product | Products, services, and tools mentioned in your work context. | Internal tools, AWS services, third-party products | 
| Defined Term | Domain-specific terminology and acronyms from your workspace. | Company jargon, technical terms, abbreviations | 
| Place | Physical or virtual locations referenced in your work. | Offices, data centers, regional locations | 

Each entity has a count of edges (relationships) connecting it to other entities in the graph.

## Data sources

        The knowledge graph extracts entities from the following sources.

### Connected integrations

When you enable **Auto-ingest from
                integrations** in the knowledge graph configuration,
                Quick automatically extracts entities from your connected
                services. You can toggle ingestion independently for each source
                type.

- 
                    **Slack**– Extracts entities from messages, channels, threads, and direct messages.
- 
                    **Email**– Extracts entities from email messages, including senders, recipients, and referenced content.
- 
                    **Other**– Extracts entities from additional connected integrations.

### Local folders

When you enable **Knowledge graph
                extraction** for a local folder in **Settings** > **My
                computer**, Quick extracts entities from files in
                that folder. This works alongside keyword search and semantic search
                indexing, but is toggled independently.

## Viewing the knowledge graph

        To view your knowledge graph, open **Settings**
            in the sidebar and choose **My context**. The
            **Knowledge graph** tab displays an interactive
            visualization of your entities and relationships.

### Graph visualization

The knowledge graph visualization is an interactive force-directed graph where each node represents an entity and each edge represents a relationship between entities.

- 
                    **Node color**– Each entity category has a distinct color. Refer to the legend at the bottom-left of the graph for the color-to-category mapping.
- 
                    **Node size**– Node size is determined by the**Size**dropdown in the top-right corner. The default is**PageRank**, which makes nodes with more connections appear larger.
- 
                    **Edges**– Lines connecting nodes represent relationships between entities.

### Interacting with the graph

You can interact with the knowledge graph visualization using the following controls.

| Action | How to perform | 
|---|---|
| Select a
                                node | Choose a node to select it and view its details. | 
| Focus on a
                                node | Double-click a node to focus the view on that entity and its immediate connections. | 
| Zoom | Scroll to zoom in or out of the graph. | 
| Pan | Choose and drag on the background to move the view. | 
| Search | Use the Search
                                entitiesbar at the top to find specific
                                entities by name. | 

### Browsing entities

Choose **Browse all** at the bottom of the
                category legend to open a sidebar listing all entities organized by
                category. Each entity shows its name and edge count (the number of
                relationships it has). The categories are collapsible, and each shows a
                count of entities it contains.

You can choose any entity in the sidebar to highlight it in the graph visualization.

### Display limits

Choose the three-dot menu in the top-right corner of the graph to configure display limits. The display limits control how many nodes and edges are rendered in the visualization.

- 
                    **Total nodes**– The maximum number of nodes to display (for example, 300 out of 3,147 total nodes).
- 
                    **Total edges**– The maximum number of edges to display (for example, 2,000 out of the total edges).

Adjusting these limits can improve performance for large knowledge graphs or help you focus on the most connected entities.

### Refreshing the graph

Choose the refresh icon next to the **Size** dropdown to reload the knowledge graph visualization
                with the latest data.

## Configuring the knowledge graph

        Choose the **Configuration** button in the
            top-right corner of the My context page to open the configuration panel. The
            knowledge graph configuration includes the following settings.

### Knowledge graph statistics

The configuration panel displays current statistics for your knowledge graph.

| Statistic | Description | 
|---|---|
| Nodes | Total number of nodes in the graph, including entities and their attributes. | 
| Edges | Total number of relationships between entities. | 
| Entities | Total number of distinct entities (people, companies, projects, and so on). | 
| Files | Total number of files that have been processed for entity extraction. | 

### Auto-ingest from integrations

The **Auto-ingest from integrations**
                toggle controls whether Quick automatically extracts entities
                from your connected services into the knowledge graph. When enabled, you
                can toggle ingestion for individual source types.

- 
                    **Slack**– Toggle entity extraction from Slack messages and channels.
- 
                    **Email**– Toggle entity extraction from email messages.
- 
                    **Other**– Toggle entity extraction from other connected integrations.

### Per-folder knowledge graph ingestion

###### To enable knowledge graph extraction for a local folder

Use the following procedure.

- 
                    Open **Settings**in the sidebar and choose**My computer**.
- 
                    Expand the folder you want to configure. 
- 
                    Toggle **Knowledge graph extraction**to enable entity extraction for that folder.

###### Note

Enabling knowledge graph extraction for a folder is independent of keyword search and semantic search. You can enable any combination of these three indexing options for each folder.

## Using the knowledge graph

        Quick automatically uses the knowledge graph to provide contextual responses in your conversations. You don't need to explicitly reference the knowledge graph — Quick consults it when relevant to your questions.

The following are examples of how the knowledge graph enhances your interactions with Quick.

- 
                **People context**– Ask "What do I know about Rachel Byrne?" and Quick uses the knowledge graph to summarize her role, recent interactions, and related projects.
- 
                **Project context**– Ask "Give me an update on Project Meridian" and Quick identifies related people, meetings, documents, and action items from the graph.
- 
                **Relationship discovery**– Ask "Who is involved with the Atlas Risk Engine?" and Quick traverses relationships in the graph to identify connected people and teams.
- 
                **Meeting preparation**– Ask "Prepare me for my meeting with Sanjay Mehta" and Quick uses the knowledge graph to surface recent context, open action items, and relevant documents.

You can also interact with the knowledge graph directly in chat by asking Quick to add entities, explore relationships, or search for specific information.

###### Note

The knowledge graph is stored locally on your machine in the
                `~/.quickwork/` directory. Your knowledge graph data is backed
                up to your AWS account for cross-device continuity, but is never used
                for AI model training.