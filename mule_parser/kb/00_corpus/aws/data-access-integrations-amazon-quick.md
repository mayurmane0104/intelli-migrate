# Data access integrations - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/data-access-integrations.html](https://docs.aws.amazon.com/quick/latest/userguide/data-access-integrations.html)

---

Data access integrations in Amazon Quick establish secure connections to external data sources. They serve as the foundation for creating knowledge bases. Unlike action connectors that perform actions, data access integrations focus on accessing and indexing content from third-party applications and services.

Data access integrations only configure authentication and point to the project or organization of the service. They cannot be used directly for analysis or by AI agents. You must create a connected knowledge base to make the data accessible.

## How data access integrations work

        
        Data access integrations configure authentication and establish connections to third-party service organizations or projects. You cannot use these integrations directly for analysis. You must create knowledge bases connected to the data access integration to make the data accessible for AI agents, chat interfaces, and spaces.

The relationship between data access integrations and knowledge bases is one-to-many:

- 
                One data access integration can support multiple knowledge bases. 
- 
                Each knowledge base selects specific content from the connected data source. 
- 
                Knowledge bases inherit authentication and access permissions from their parent data access integration. 

## Create a data access integration

        
        Use the following procedure to create a data access integration that establishes authentication and connection details for knowledge base creation. The following example demonstrates the process for setting up a Microsoft OneDrive data access integration, but the general steps are applicable to other data access integrations.

###### To create a data access integration

- 
                Scroll to the Set up a new integration area of the page. Find the application that you want to create an integration and knowledge base. Select "OneDrive". ###### NoteThe Integration page defaults Knowledge bases tab and there may be existing knowledge bases that have been set up by others and shared. If you have previously set up an integration, check the data tab and use the action menu to create a knowledge base from there. 
- 
                Select the plus (+) icon button on the application to create a new integration and knowledge base. 
- 
                Select Bring data from Microsoft OneDrive option and click Next button. ###### NoteSome application integrations support data ingestion and read/write actions. The set up varies for each one. To set up actions, you'll need more information from your admin. 
- 
                Complete the authentication process: - A Microsoft OneDrive sign in popup will appear automatically. If it doesn't, click Sign in to Microsoft OneDrive button. 
- Sign in using your Amazon credentials. 
- Wait until a success banner appears. 
- Click the "Next" button. 
 
- 
                Select the data that should be ingested into the knowledge base using the file picker for OneDrive and click Add button. 
- 
                Type in a knowledge base a Name and Description (optional), then click Create. 
- 
                There will be a success toast notification and the data ingestion and sync will begin. 
- 
                The data can take several minutes to sync, depending on the number files that are being ingested. The Status column will stay in the Syncing status until it is ready changing to Available. 
- 
                When the knowledge base is ready, use the chat to ask questions and interact with it. ###### NoteBy default, the chat uses 'all data and apps' that you have access to and that are set up on your behalf. If you want to chat with a single knowledge base, select the knowledge base in the chat data picker. ###### NoteYou can also attach a knowledge base to a Space by navigating to the Space and adding it. 

After successful creation, your data access integration appears in the integrations list. You can now create knowledge bases that use this integration to access and index content from the connected data source.

###### Note

For detailed configuration steps specific to each data source, see [Supported integrations](./supported-integrations.html).

## Supported data sources

        
        Amazon Quick supports data access integrations with the following applications and services. These integrations allow you to create knowledge bases from external data sources:

- 
                **Amazon S3**- Access documents and files stored in S3 buckets using AWS credentials.
- 
                **Atlassian Confluence**- Index pages, spaces, and attachments using user authentication or service authentication.
- 
                **Google Drive**- Connect to personal and shared drives using OAuth 2.0 authentication.
- 
                **Microsoft OneDrive**- Access OneDrive for Business content using user authentication or service authentication.
- 
                **Microsoft SharePoint**- Index SharePoint Online and Server content using OAuth 2.0 authentication.
- 
                **Web Crawler**- Index content from internal and external websites using basic authentication or form/SAML authentication.

Each data source supports different authentication methods and content access capabilities. The relationship between data access integrations and knowledge bases is one-to-many - one integration can support multiple knowledge bases, each selecting specific content from the connected data source.

## Data source categories

        
        Data access integrations are organized into the following categories based on the type of content and access patterns:

- **Cloud storage and file systems**
- 
                    - AWS S3 - Access documents and files stored in S3 buckets. 
- Google Drive - Index content from personal and shared drives. 
- Microsoft OneDrive - Connect to OneDrive for Business content. 
 
- **Content management systems**
- 
                    - Atlassian Confluence - Access pages, spaces, and attachments. 
- Microsoft SharePoint - Index SharePoint Online and Server content. 
 
- **Web content**
- 
                    - Web Crawler - Index content from internal and external websites. 
 

### Authentication and security

Data access integrations use secure authentication methods to protect your data and maintain access controls. The authentication method depends on the specific data source and your organization's security requirements.

- **OAuth authentication**
- 
                    Most cloud-based integrations (Google Drive, OneDrive, Confluence Cloud) use OAuth 2.0 for secure, token-based authentication. This method allows Amazon Quick to access your data without storing your credentials. 
- **Service account authentication**
- 
                    Enterprise integrations may use service accounts for programmatic access. This method is common for AWS S3 and other infrastructure-based data sources. 
- **No authentication**
- 
                    Some integrations, such as web crawlers accessing public websites, may not require authentication. However, access controls are still enforced based on your Amazon Quick permissions. 

###### Note

Authentication requirements and available methods vary by user tier. Readers may have limited authentication options compared to Authors.

### Access control and permissions

Data access integrations maintain security by enforcing access controls at multiple levels. When users query content through knowledge bases, Amazon Quick ensures they can only access content they have permission to view.

- 
                **Source-level permissions**- Users must have appropriate permissions in the source system (Google Drive, SharePoint, etc.).
- 
                **Integration-level permissions**- Access to the integration itself is controlled by Amazon Quick permissions.
- 
                **Knowledge base permissions**- Individual knowledge bases can have their own access controls.
- 
                **Entity-level access controls**- When users query content, Amazon Quick verifies permissions for each document or item.

### Key features and capabilities

Data access integrations provide several features to enhance your data integration experience:

- 
                **Real-time synchronization**- Content is automatically updated when changes occur in the source system.
- 
                **Selective indexing**- Choose specific folders, sites, or content types to include in your knowledge bases.
- 
                **Content type support**- Index various file formats including documents, spreadsheets, presentations, and web pages.
- 
                **Metadata preservation**- Maintain important metadata such as creation dates, authors, and tags.
- 
                **Natural language querying**- Enable AI-powered search and question-answering across your indexed content.

### Before you begin

Before creating data access integrations, ensure you have the following requirements in place:

- 
                **Amazon Quick permissions**- Author or Admin role to create and manage integrations.
- 
                **Source system access**- Appropriate permissions in the target system (administrative access may be required for some integrations).
- 
                **Authentication credentials**- Valid credentials or service accounts for the target system.
- 
                **Network connectivity**- Ensure Amazon Quick can access your data sources. Network requirements differ by integration type:- 
                        **Knowledge bases**- Do not support VPC connectivity. Data sources must be accessible over the public internet.
- 
                        **Action connectors**- Support VPC connectivity for resource servers within your VPC. However, authentication servers must remain publicly accessible.
 
-