# Integrations - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/actions-integrations.html](https://docs.aws.amazon.com/quick/latest/userguide/actions-integrations.html)

---

## AWS Services

        
         
            ### Amazon S3

Amazon S3 actions allow you to store and retrieve files and data.

**Available Actions**

- **Download File**- Downloads a file from Amazon S3 and returns a file object handle.
- **Upload File**- Uploads a file object handle to Amazon S3.
- **Copy Object**- Creates a copy of an object that is already stored in Amazon S3 from one source file to a destination location.
- **Delete Object**- Deletes a specified object from an S3 bucket.
- **List Objects**- Lists all of the objects in the given bucket. Can be filtered using a prefix.

### Amazon Bedrock

Amazon Bedrock actions allow you to connect to foundation models (FMs) from leading AI companies through a single API.

- **Basic model converse**- Sends a prompt to an AI model. Use natural language to generate text, analyze content, and get AI-powered responses.
- **Advanced model converse**- Prompts model with more options. Advanced options include custom message formats, tool integrations, and granular control over model behavior.

### Amazon Bedrock Agents

Amazon Bedrock Agent actions allows you to invoke AI assistants that can connect to your data sources, APIs, and backend systems.

- **Basic agent invoke**- Sends a request to an AI agent. Use for simple interactions that don't require file attachments, user input, or custom configurations.
- **Advanced agent invoke**- Calls an agent with more options. Used for advanced interactions that require file attachments, user input, or custom configurations.

### Amazon Bedrock Data Automation

Bedrock Data Automation (BDA) simplifies the process of extracting valuable insights from unstructured content using generative AI.

**Available Actions**

- **Invoke Data Automation Async**- Process data with a data automation project or blueprints. Starts asynchronous data processing and returns an invocation ID.
- **Get Data Automation Status**- Gets details about a data automation invocation status and output location.

### Amazon Textract

Amazon Textract helps you add document text detection and analysis to your automations.

- **Basic document query**- Extracts data based on questions. Each query contains the question you want to ask and the alias you want to associate. Textract provides the text answer to each question and a confidence score.
- **Basic document analysis**- Extracts data from documents. Automatically detects and extracts forms (key-value pairs), tables (structured data), and text while preserving document layout and data relationships.

### Amazon Comprehend

Amazon Comprehend is a natural language processing (NLP) service for gaining insight into document content. It helps analyze text to extract key phrases, identify sentiment, and classify documents.

**Available Actions**

- **Classify Document**- Creates a classification request to analyze a single document in real-time using a custom model endpoint. Supports text input or document files (PDF, Word, or image).
- **Detect Key Phrases**- Detects the key noun phrases found in the text, identifying important concepts and topics within the content.

## External Applications

        
         
            ### Microsoft Outlook

The Microsoft Outlook actions allow your automations to manage emails and calendars.

- **Email**- **Send User Email**- Send an email message on behalf of a specific user.
- **Reply to Email**- Reply to the sender of a message.
- **List Folder Messages**- Get the messages in a specific folder of the signed-in user's mailbox.
- **List User Mails**- Get the messages in the signed-in user's mailbox (including Deleted Items and Clutter folders).
- **View Email**- Retrieve the properties and relationships of a specific message object.
- **Update Email**- Update the properties of a message object.
- **Delete Email**- Delete a message in the specified user's mailbox.
- **List Email Attachments**- Retrieve a list of attachment objects attached to a message.
- **Get Attachment**- Read the properties, relationships, or raw contents of an attachment.
 
- **Folders**- **List Mail Folders**- Get the mail folder collection directly under the root folder of the signed-in user.
- **Move Email to Folder**- Move a message to another folder within the specified user's mailbox.
- **Get Mailbox Settings**- Get the user's mailbox settings, such as automatic replies, date format, and time zone.
 
- **Calendar**- **List Calendar Events**- Fetch a list of calendar events for the specified user or resource from Microsoft Outlook.
- **Create Calendar Event**- Create an event in the user's default calendar or specified calendar.
- **Update Calendar Event**- Update the properties of an existing event object.
 
- **Other**- **List Places**- Get a collection of place objects (rooms or room lists) defined in the tenant.
- **List Users**- Retrieve a list of users in the organization from Microsoft Outlook with their basic information.
- **List Contacts**- Get a contact collection from the default contacts folder of the signed-in user.
 

### Microsoft Teams

The Microsoft Teams actions allow your automations to communicate with team members through channels and chat messages, as well as manage meetings.

- **Messages**- **List Chats**- View all chat conversations
- **Create Chat**- Start a new chat conversation
- **Get Individual Chat**- View details of a specific chat
- **List All Chat Messages**- View messages in a chat conversation
- **Send Chat Message**- Send a new message in a chat
 
- **Teams**- **List Teams**- View all teams accessible to the authenticated user
- **Get Team**- View detailed information about a specific team
- **List All Team Members**- View members of a team
- **Invite User To Team**- Add a new member to a team
 
- **Channels**- **List All Channels**- View all channels within a specific team
- **Create Channel**- Create a new channel within a team
- **Get Channel**- View detailed information about a specific channel
- **List All Channel Messages**- View messages posted in a channel
- **Send Channel Message**- Post a new message to a channel
- **Reply To Channel Message**- Add a reply to an existing channel message
- **Invite Channel Member**- Add a member to a specific channel
 
- **Meetings**- **Create Online Teams Meeting**- Schedule a new online meeting
- **Get Online Teams Meeting**- View details of a specific meeting
- **List All Recordings**- View recordings from a meeting
- **List All Transcripts**- View transcripts from a meeting
 
- **Users**- **List Users**- View list of users in the organization
 

### Microsoft SharePoint

The Microsoft SharePoint allows you to centrally store, manage, and share documents and information through your automations.

- **Lists and items**- **Get List**- Get a list of operations associated with a list
- **Create Item**- Create a new list Item in a list
- **Update Item**- Update the properties on a listItem
- **Delete Item**- Removes an item from a list
- **Get Item**- Returns the metadata for an item in a list
- **List Item**- Get the collection of items in a list
 
- **Sheets and files**- **Add Sheet**- Add a new worksheet to the workbook
- **Delete Sheet**- Remove worksheet from workbook
- **Update Sheet**- Edit worksheet properties (rename, visibility)
- **List Sheets**- Retrieve a list of worksheet objects
- **Read Sheet**- Retrieve properties of a worksheet
- **Upload File**- Creates or updates a workbook file
 
- **Ranges and cells**- **Read Range**- Retrieves values from a specified range
- **Delete Range**- Deletes cells in a specified range
- **Write Range**- Updates values in a specified range
- **Get Used Range**- Returns the used range of the given worksheet
- **Clear Range**- Clear range values including format, fill, and border
- **Read Cell**- Gets the value from a specific cell
- **Write Cell**- Sets the value of a specific cell
 

### Microsoft OneDrive

Microsoft OneDrive actions allow you to store, sync, and share files. You can interact directly with Microsoft Excel files saved to OneDrive for spreadsheet actions.

- **File management**- **Get Item**- View details of a specific file or folder
- **Get Drive**- View OneDrive account details and storage information
- **List Items**- View all files and folders in a drive
- **Create Item / Create Folder**- Create a new folder or item in OneDrive
- **List Children**- View items contained within a specific folder
- **Delete Item**- Remove a file or folder
- **Update Item / Move Item**- Update metadata or move files between folders
- **Copy Item**- Create a copy of a file or folder in a different location
- **Add Permissions**- Configure sharing and access permissions for files
- **Upload File**- Add new files to OneDrive
 
- **Excel**- **Add Sheet**- Create a new worksheet in an Excel workbook
- **Clear Range**- Remove content and formatting from a range of cells
- **Delete Range**- Remove cells, rows, or columns from a worksheet
- **Delete Sheet**- Remove a worksheet from a workbook
- **List Sheets**- View all worksheets in a workbook
- **Read Cell**- Get the value of a specific cell
- **Read Range**- Get values from a range of cells
- **Read Sheet**- View contents of an entire worksheet
- **Read Used Range**- Get the range of cells that contain data
- **Update Sheet**- Modify worksheet properties
- **Write Cell**- Set the value of a specific cell
- **Write Range**- Set values for a range of cells
 

### Salesforce

Salesforce actions allow you to automate the process of managing customer relationships across cases, opportunities, leads, campaigns, contacts and more.

- **Cases**- **Get Case List**- Gets a list of customer support cases from Salesforce, including their metadata and recent items.
- **Get Case**- View details of a specific case
- **Create Case**- Create a new support case
- **Delete Case**- Remove an existing case
- **Update Case**- Edit case details and information
 
- **Opportunities**- **Get Opportunities**- View list of sales opportunities
- **Get Specific Opportunity**- View details of a specific opportunity
- **Create Opportunity**- Create a new sales opportunity
- **Update Opportunity**- Edit opportunity details
- **Delete Opportunity**- Remove an existing opportunity
 
- **Leads**- **Update Lead**- Edit lead details and information
 
- **Campaigns**- **Update Campaign**- Edit campaign details and information
 
- **Feed Items**- **Update Feed Item**- Edit feed item content and properties
 
- **Contacts**- **Get Contact List**- View all contacts in the system
- **Get Contact**- Fetch details of a specific contact
- **Update Contact**- Edit contact information
 
- **Users**- **Get User List**- Retrieve list of Salesforce users
 
- **System**- **Describe SObject**- Get object metadata and field details for any Salesforce object type
 

### Jira

Jira actions allow you to automate managing issues, projects, sprints and more.

- **Issues**- **Create Issue**- Create an issue in a project.
- **Edit Issue**- Modify an existing issue in a project.
- **Update Issue Status (Do Transition)**- Change task status of an issue.
- **Delete Issue**- Delete an issue in a project.
- **Get Issue**- View details of an issue in a project.
- **Search Issues**- Searches for issues using JQL
- **Search Statuses**- Search issue statuses.
- **Download Issue Attachment**- View the contents of an attachment.
- **Add Attachment**- Add an attachment to an issue.
- **Get All Labels**- View all labels.
 
- **Comments**- **Add Comment**- Add new comment to an issue.
- **Delete Comment**- Remove comment from an issue.
- **Update Comment**- Edit an existing comment on an issue.
- **Get Comments**- View issue comments.
 
- **Projects**- **Create Project**- Create new project in Jira.
- **Update Project**- Modify project details.
- **Delete Project**- Remove project from Jira.
- **Get Project**- View project details.
- **Get Issue Types For Project**- View project issue types.
- **Search Projects**- Find visible projects.
 
- **Sprints**- **Create Sprint**- Create a sprint in a project.
- **Update Sprint**- Update sprint details.
- **Delete Sprint**- Delete a sprint in a project.
- **Get Sprint**- View details of a sprint in a project.
- **Move Issues to Sprint and Rank**- Assign an issue to a sprint.
- **Move Issues to Backlog**- Move issues to backlog.
 
- **Users**- **Find Users**- Search for a Jira user.
- **Find Assignable Users**- Returns a list of users that can be assigned to an issue.
- **Get All Users**- List all Jira users.
 

### ServiceNow

ServiceNow actions allow you to automate IT service management of incidents, change requests, and more.

- **Incidents**- **Create Incident**- Creates a new incident record.
- **Read Incident**- Retrieves details of a specific incident.
- **Update Incident**- Modifies an existing incident record.
- **Delete Incident**- Removes a specific incident record.
 
- **Change Requests**- **Create Change Request**- Creates a new change request record.
- **Read Change Request**- Retrieves details of a specific change request.
- **Update Change Request**- Modifies an existing change request record.
- **Delete Change Request**- Removes a specific change request record.
 
- **Knowledge Base Articles**- **Update Knowledge Base Article**- Modifies an existing knowledge base article.
 
- **Problem Records**- **Update Problem Record**- Modifies an existing problem record.
 
- **Attachments**- **Upload Binary Attachment**- Uploads a file as an attachment to a specified record.
- **Upload Multipart Form Attachment**- Uploads a form attachment to a record.
- **Retrieve Attachment Content**- Gets the binary content of a specific attachment.
- **Retrieve Attachment Metadata**- Gets metadata for a specific attachment.
- **Delete Attachment**- Removes an attachment from the system.
- **Retrieve Metadata for Attachments**- Gets metadata for multiple attachments.
 
- **System**- **List Users**- Retrieves all existing records from system user table.
- **List Choices**- Retrieves choice list values from the system.
 

### SAP

SAP actions allow you to automate processes involving business partner data, material stocks, bills of material, product masters, and physical inventory.

- **SAP Business Partners**- **Get Business Partner**- Retrieves general data for business partners, providing a comprehensive view of partner information.
- **Get Business Partner By ID**- Retrieves detailed business partner data using a specific business partner number as identifier.
- **Get Business Partner Address**- Retrieves address details associated with business partners, including postal addresses and contact information.
- **Get Business Partner Role**- Retrieves role information for business partners, showing their relationships and functions within the system.
- **Get Business Partner Role By ID**- Retrieves specific role data for a business partner using key identifier fields.
 
- **SAP Material Stock**- **Get Material Stock In Account Model Collection**- Gets material stock levels with details like batch, storage location, and special stock indicators.
 
- **SAP Bill Of Material**- **Get Material BOM Item**- Retrieves details of materials used in bills of materials including quantities, categories, and relationships.
 
- **SAP Product Master**- **Get Product Master Records**- View product master general details. Returns complete product master records with options to filter, sort and select specific data.
- **Get Plant Data Of Product Master Record**- View plant details of the product. Access detailed plant-specific information for a given product including manufacturing, storage, and logistics data.
- **Get Supply Planning Data By Product Number And Plant**- View supply planning details by product number and plant. Retrieves detailed planning parameters including lot sizes, safety stock levels, and procurement data.
 
- **SAP Physical Inventory**- **Get Phys Inventory Doc Item**- Retrieves physical inventory document items including counting results and inventory differences.
 

## REST API Integration

        The REST API Connection integration enables Quick Automate to interact with custom REST APIs and web services, allowing you to extend automation capabilities to external systems. This integration supports action execution for GET, POST, DELETE, PATCH and PUT HTTP methods.

**Common Use Cases:**

- Sending notifications to external systems 
- Retrieving data from third-party services 
- Updating records in external databases 
- Triggering workflows in connected applications 

**Prerequisites**

Before creating automations with REST API integration, ensure you have:

- **Configured REST API Integration**- Access Quick Suite console 
- Navigate to Integrations > REST API Connection 
- Configure your REST API endpoint with base URL 
- Complete authentication setup (see Authentication section below) 
- Full details: - [REST API Connection integration](./rest-api-integration.html)
 
- **Connected Integration to Automation Group**- Link your configured REST API integration to your automation group 
- Verify integration appears in available actions 
- Step-by-step guide: - [AWS service action connectors](./builtin-services-integration.html)
 
- **Authentication Configured**- OAuth 2.0 credentials obtained from your API provider 
 

### Authentication

For Quick Automate, this integration supports **OAuth 2.0** authentication. You must configure OAuth credentials before creating automations.

**OAuth 2.0 Setup Steps:**

- Obtain OAuth credentials (Client ID and Client Secret) from your identity provider 
- In the Quick Suite console, navigate to your REST API integration settings 
- Select OAuth 2.0 as the authentication method 
- Enter your Client ID and Client Secret 
- Configure the authorization URL and token URL provided by your API provider 
- Complete the OAuth flow to authorize Quick Suite 
- Test the connection to verify authentication 

**Important Notes:**

- Quick Automate does not support bearer token authentication in request headers. Use OAuth configuration instead. 
- Configure authentication at the integration level, not per automation action 

### Configuration

**Setting Up Your REST API Integration**

Step 1: Create Base URL Configuration

Step 2: Connect to Automation Group

Step 3: Access REST API Actions

- Open the Actions Panel in your automation 
- Locate REST API action 
- Drag and drop actions into your automation workflow 
- ###### Note- REST API actions must be added through the Actions Panel; they are not available in the Build with Assistant interface 

### Properties Reference

- 
                    **Q Action Connector ID (Required)**- **Description:**Unique identifier that links the REST API action to your configured integration, including base URL and authentication settings.
- **Format:**Auto-populated from your connected integration
- **Example:**- `rest-api-connector-abc123`
 
- 
                    **URI (Optional)**- **Description:**Additional path appended to the base URL to specify the exact API endpoint.
- **Format:**Path string with or without leading slash (depends on the base url format)
- **How It Works:**- Base URL: - `https://api.example.com`
- URI: - `/users/123`
- Final URL: - `https://api.example.com/users/123`
 
- **Examples:**- `/users/123 prod/send-email /v2/orders customers/search`
 
- 
                    **Additional Headers (Optional)**- **Description:**Custom HTTP headers to include in the API request as key-value pairs.
- **Format:**- `Key: Value`
- **Common Examples:**- `Content-Type: application/json Accept: application/json X-Custom-Header: custom-value X-API-Version: 2.0`
- **Important Limitations:**- Do not include Authorization headers; authentication is handled via OAuth configuration 
- Each header must be on a separate line 
- Headers are case-sensitive 
 
 
- 
                    **Request (Required)**- **Description:**JSON-formatted data to send with POST or PUT requests.
- **Format:**Valid JSON object. {} for blank requests
- **POST Request Example (Creating a resource):**- `{ "title": "My New Post", "body": "This is the content of my new post.", "userId": 1, "tags": ["automation", "api"], "published": true }`
- **PUT Request Example (Updating a resource):**- `{ "status": "completed", "completedDate": "2026-01-27", "notes": "Task finished successfully" }`
 
- 
                    **Output Variable (Optional)**- **Description:**Variable name to store the JSON response from the API call for use in subsequent automation actions.
- **Format:**Alphanumeric variable name (no spaces)
- **Example:**- `apiResponse`,- `userData`,- `orderDetails`
 

### Example of API usage

#### Example 1: GET Request - Retrieve Ticket Details

**Scenario:** Retrieve details of an existing support ticket from an external ticketing system

**Configuration:**

- **Q Action Connector ID:**rest-api-connector-tickets
- **HTTP Method:**GET
- **URI:**/tickets/- `ticketId`
- **Additional Headers:**- `Accept: application/json`
- **Request Body:**{} (empty for GET requests)
- **Output Variable:**ticketDetails

#### Example 2: POST Request - Create New Record

**Scenario:** Submit a new support ticket to an external ticketing system

**Configuration:**

- **Q Action Connector ID:**rest-api-connector-tickets
- **HTTP Method:**POST
- **URI:**- `/tickets`
- **Additional Headers:**- `Content-Type: application/json Accept: application/json`
- **Request Body:**- `{ "title": "{{ticketTitle}}", "description": "{{ticketDescription}}", "priority": "{{ticketPriority}}", "requestedBy": "{{userEmail}}", "category": "technical_support" }`
- **Output Variable:**- `ticketResponse`