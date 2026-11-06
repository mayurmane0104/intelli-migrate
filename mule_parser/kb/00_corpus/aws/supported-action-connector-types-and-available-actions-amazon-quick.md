# Supported action connector types and available actions - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/action-connector-apis-supported-types.html](https://docs.aws.amazon.com/quick/latest/userguide/action-connector-apis-supported-types.html)

---

Amazon Quick supports multiple connector types, each with specific actions available:

## External service connectors

        - 
                **Airtable**- Create and update records, manage bases and tables, filter views, and perform relational data operations.
- 
                **Asana**- Manage tasks, workspace operations, and project handling.
- 
                **Atlassian Confluence Cloud**- Create, update, and manage pages, spaces, and other Confluence objects.
- 
                **Atlassian Jira Cloud**- Create issues, update tickets, search projects, manage workflows.
- 
                **BambooHR**- Access employee data, manage time-off requests.
- 
                **Box**- Manage files, folders, and collaborate on documents.
- 
                **Canva**- Create and edit designs, manage templates and assets.
- 
                **Dropbox**- Upload files, manage folder structures, generate sharing links, and control access permissions.
- 
                **GitHub**- Manage repositories, issues, pull requests, and code collaboration.
- 
                **Gmail**- Read emails, search inbox, draft messages, manage labels, and organize threads.
- 
                **Google Analytics**- Query traffic reports, retrieve audience data, monitor conversion events, and access performance metrics.
- 
                **Google Calendar**- Create and update events, check availability, manage invites, and retrieve schedules.
- 
                **Google Docs**- Create and edit documents, read content, and collaborate on text-based files.
- 
                **Google Drive**- Upload files, manage folders, search content, and perform file operations.
- 
                **Google Meet**- Schedule video meetings, list hosted meetings, retrieve transcripts, and update access settings.
- 
                **Google Sheets**- Create and edit spreadsheets, read and write cell ranges, and perform data operations.
- 
                **Google Slides**- Create presentations, edit slides, manage layouts, and add speaker notes.
- 
                **HubSpot**- Manage contacts, deals, marketing campaigns, and CRM data.
- 
                **HuggingFace**- Access AI models, datasets, and machine learning workflows.
- 
                **Intercom**- Manage customer conversations, support tickets, and messaging.
- 
                **Linear**- Create and manage issues, projects, and development workflows.
- 
                **Microsoft OneDrive**- Create, update, delete, and manage OneDrive files and folders.
- 
                **Microsoft Outlook**- Send emails, manage calendar events, access contacts.
- 
                **Microsoft SharePoint**- Perform actions on SharePoint lists, items, files, and Excel workbooks.
- 
                **Microsoft Teams**- Send messages, manage channels, schedule meetings, and manage team collaboration.
- 
                **Monday.com**- Manage projects, tasks, and team collaboration workflows.
- 
                **New Relic**- Access observability data, query metrics, and manage monitoring workflows.
- 
                **Notion**- Create and manage pages, databases, and collaborative workspaces.
- 
                **PagerDuty**- Create incidents, manage escalations, update on-call schedules.
- 
                **QuickBooks**- Manage invoices, track expenses, generate financial reports, and handle vendor records.
- 
                **Salesforce**- Create records, update opportunities, search accounts, manage leads.
- 
                **SAP**- Access SAP S/4HANA systems to perform read operations on enterprise data.
- 
                **ServiceNow**- Create incidents, update requests, manage workflows.
- 
                **Slack**- Send messages, create channels, manage notifications.
- 
                **Smartsheet**- Update sheets, manage project data.
- 
                **Visier**- Access workforce analytics, query people data, and generate HR insights.
- 
                **Zendesk**- Create tickets, update cases, search knowledge base.
- 
                **Zoom**- Schedule meetings, add webinar registrants, summarize recorded meetings, and list participants.

## AWS service connectors

        - 
                **Amazon S3**- Upload files, manage buckets, retrieve objects.
- 
                **Amazon Bedrock**- Generate content, analyze data, process requests.
- 
                **Amazon Textract**- Extract text and data from documents.
- 
                **Amazon Comprehend**- Natural language processing and sentiment analysis.
- 
                **Amazon Comprehend Medical**- Medical text analysis and entity extraction.

## Action connector compatibility matrix

        
        The following table shows which Amazon Quick features each action connector type supports:

| Action Connector | Chat Agents | Flows | Dashboard Visuals | Dashboard Alerts | Automations | Companions | 
|---|---|---|---|---|---|---|
| AWS Built-in Services | ||||||
| AWS Bedrock Agent Runtime | — | — | — | — | ✓ | — | 
| AWS Bedrock Data Automation Runtime | — | — | — | — | ✓ | — | 
| AWS Bedrock Runtime | — | — | — | — | ✓ | — | 
| Amazon Comprehend | — | — | — | — | ✓ | — | 
| Amazon Comprehend Medical | — | — | — | — | — | — | 
| Amazon S3 | — | — | — | — | ✓ | — | 
| Amazon Textract | — | — | — | — | ✓ | — | 
| External Service Connectors | ||||||
| Airtable | ✓ | ✓ | ✓ | — | — | — | 
| Asana | ✓ | ✓ | — | — | — | ✓ | 
| Atlassian Confluence Cloud | ✓ | ✓ | — | — | ✓ | ✓ | 
| Atlassian Jira Cloud | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| BambooHR | ✓ | ✓ | — | — | — | ✓ | 
| Box | ✓ | ✓ | — | — | — | — | 
| Canva | ✓ | ✓ | — | — | — | — | 
| Dropbox | ✓ | ✓ | ✓ | — | — | — | 
| GitHub | ✓ | ✓ | — | — | — | — | 
| Gmail | ✓ | ✓ | ✓ | — | — | — | 
| Google Analytics | ✓ | ✓ | ✓ | — | — | — | 
| Google Calendar | ✓ | ✓ | ✓ | — | — | — | 
| Google Docs | ✓ | ✓ | ✓ | — | — | — | 
| Google Drive | ✓ | ✓ | ✓ | — | — | — | 
| Google Meet | ✓ | ✓ | ✓ | — | — | — | 
| Google Sheets | ✓ | ✓ | ✓ | — | — | — | 
| Google Slides | ✓ | ✓ | ✓ | — | — | — | 
| HubSpot | ✓ | ✓ | — | — | — | — | 
| HuggingFace | ✓ | ✓ | — | — | — | — | 
| Intercom | ✓ | ✓ | — | — | — | — | 
| Linear | ✓ | ✓ | — | — | — | — | 
| Microsoft OneDrive | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| Microsoft Outlook | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| Microsoft SharePoint | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| Microsoft Teams | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| Monday.com | ✓ | ✓ | — | — | — | — | 
| New Relic | ✓ | ✓ | — | — | — | — | 
| Notion | ✓ | ✓ | — | — | — | — | 
| PagerDuty | ✓ | ✓ | — | — | ✓ | ✓ | 
| QuickBooks | ✓ | ✓ | ✓ | — | — | — | 
| Salesforce | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| SAP | ✓ | — | — | — | ✓ | ✓ | 
| ServiceNow | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 
| Slack | ✓ | ✓ | ✓ | — | — | ✓ | 
| Smartsheet | ✓ | ✓ | — | — | — | ✓ | 
| Visier | ✓ | ✓ | — | — | — | — | 
| Zendesk | ✓ | ✓ | — | — | — | ✓ | 
| Zoom | ✓ | ✓ | ✓ | — | — | — | 
| Custom Connector Types | ||||||
| Model Context Protocol (MCP) | ✓ | ✓ | — | — | ✓ | — | 
| OpenAPI | ✓ | ✓ | — | — | — | — | 
| REST API | — | — | — | — | ✓ | — | 

**Authentication Support:**

- 
                **Chat Agents and Companions**- Support user authentication (Default OAuth app, Custom OAuth app, Basic)
- 
                **Dashboard Visuals**- Support user authentication (Default OAuth app, Custom OAuth app)
- 
                **Dashboard Alerts**- Support system authentication (Service-to-Service OAuth or API Key)
- 
                **Automations**- Support system authentication (Service-to-Service OAuth)