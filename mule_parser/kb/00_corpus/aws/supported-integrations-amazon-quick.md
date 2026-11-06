# Supported integrations - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/supported-integrations.html](https://docs.aws.amazon.com/quick/latest/userguide/supported-integrations.html)

---

Amazon Quick supports integrations with various third-party applications and services. Each integration supports different combinations of actions and knowledge base creation capabilities. The following table shows the supported integrations and their capabilities.

| Integration | Actions | Knowledge Base | 
|---|---|---|
| Airtable | ✓ | — | 
| Amazon S3 | ✓ | ✓ | 
| Asana | ✓ | — | 
| Atlassian Confluence Cloud | ✓ | ✓ | 
| Atlassian Jira Cloud | ✓ | — | 
| BambooHR | ✓ | — | 
| Box | ✓ | — | 
| Canva | ✓ | — | 
| Dropbox | ✓ | — | 
| GitHub | ✓ | — | 
| Gmail | ✓ | — | 
| Google Analytics | ✓ | — | 
| Google Calendar | ✓ | — | 
| Google Docs | ✓ | — | 
| Google Drive | ✓ | ✓ | 
| Google Meet | ✓ | — | 
| Google Sheets | ✓ | — | 
| Google Slides | ✓ | — | 
| HubSpot | ✓ | — | 
| HuggingFace | ✓ | — | 
| Intercom | ✓ | — | 
| Linear | ✓ | — | 
| Microsoft OneDrive | ✓ | ✓ | 
| Microsoft Outlook | ✓ | — | 
| Microsoft SharePoint Online | ✓ | ✓ | 
| Microsoft Teams | ✓ | — | 
| Model Context Protocol (MCP) | ✓ | — | 
| Monday.com | ✓ | — | 
| New Relic | ✓ | — | 
| Notion | ✓ | — | 
| OpenAPI Specification | ✓ | — | 
| PagerDuty | ✓ | — | 
| QuickBooks | ✓ | — | 
| REST API | ✓ | — | 
| Salesforce | ✓ | — | 
| SAP Bill of Materials | ✓ | — | 
| SAP Business Partner | ✓ | — | 
| SAP Material Stock | ✓ | — | 
| SAP Physical Inventory Docs | ✓ | — | 
| SAP Product Master | ✓ | — | 
| ServiceNow | ✓ | — | 
| Slack | ✓ | — | 
| Smartsheet | ✓ | — | 
| Visier | ✓ | — | 
| Web Crawler | — | ✓ | 
| Zendesk Suite | ✓ | — | 
| Zoom | ✓ | — | 

###### Note

Not all applications support all integration types. The available options depend on the capabilities of each specific application and your user role.

## Integration capability definitions

        
        - **Actions**
- 
                    Call APIs and perform actions in external applications directly from Amazon Quick. You can share action connectors with other users and use them in automated workflows. 
- **Knowledge base**
- 
                    Create searchable repositories of information from external sources. Knowledge bases are children of data access integrations. Add them to spaces or use them directly in chat agents. 

## Authentication method definitions

        
        - **User auth**
- 
                    Custom user-based OAuth authentication requiring base URL, client ID, client secret, token URL, auth URL, and redirect URL. 
- **Service auth**
- 
                    Service-to-service authentication using either API key (with base URL and email) or service-to-service OAuth (with base URL, client ID, client secret, and token URL). 
- **Managed OAuth 2.0**
- 
                    Managed OAuth 2.0 authentication flow with provider-specific sign-in interface. 
- **AWS credentials**
- 
                    AWS-specific authentication using AWS access keys and permissions. 
- **Basic auth**
- 
                    Username and password authentication. 
- **Form/SAML auth**
- 
                    Form-based or SAML authentication with configurable field selectors. 
- **JSON schema**
- 
                    Schema-based authentication for OpenAPI specifications.