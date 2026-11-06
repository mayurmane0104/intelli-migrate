# Box Agent integration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/box-integration.html](https://docs.aws.amazon.com/quick/latest/userguide/box-integration.html)

---

With the Box Agent connector, you can access Box AI features, manage files and folders, and organize content in hubs directly in Amazon Quick through natural language.

Amazon Quick supports the following authentication methods for Box Agent.

- 
            **Default OAuth app**– Uses an AWS-managed OAuth application. No additional credentials are needed. You authenticate directly with your Box account.
- 
            **Custom OAuth app**– Uses a customer-managed OAuth 2.0 application registered in the Box Developer Console. This option gives your organization full control over the OAuth configuration.

For more information about the authentication methods that Amazon Quick
        supports, see [Authentication methods](./quick-action-auth.html).

## Before you begin

        Make sure that you have the following before you set up the integration.

- 
                A Box account with access to files and folders. 
- 
                For **Custom OAuth app**: Access to the Box Developer Console to create a custom app. For more information, see[OAuth 2.0 setup](https://developer.box.com/guides/authentication/oauth2/oauth2-setup)in the Box documentation.
- 
                For Amazon Quick subscription requirements, see [Set up integrations in the console](./integration-console-setup-process.html).

## Setting up the connector in Amazon Quick

         
            ### Connect from the Available tab

If you want to use Default OAuth app authentication, you can connect
                directly from the **Available** tab without additional
                configuration.

- 
                    In the Amazon Quick console, choose **Connectors**.
- 
                    On the **Available**tab, find**Box Agent**and choose**Connect**.
- 
                    Complete the Box sign-in flow and grant the requested permissions. 

To configure a connector with Custom OAuth app instead, use the
                **Create for your team** tab as described
                below.

### Create from the Create for your team tab

If you use Custom OAuth app authentication, create a custom app in
                the Box Developer Console before configuring Amazon Quick. For setup
                instructions, see [OAuth 2.0 setup](https://developer.box.com/guides/authentication/oauth2/oauth2-setup) in the Box documentation.

- 
                    In the Amazon Quick console, choose **Connectors**.
- 
                    Choose the **Create for your team**tab.
- 
                    Find and choose **Box Agent**.###### NoteIf a Box Agent connector already exists, a dialog appears with your existing connectors. To use an existing connector, choose it. To create a new one, choose **No, create new**.
- 
                    Enter a **Name**for your connector. Optionally, choose**+ Add Description**to add a description.
- 
                    For **Connection type**, choose**Public network**.
- 
                    For **OAuth Configuration**, choose one of the following:- 
                            For **Default OAuth app**:No additional credentials are needed. Choose **Next**to continue.
- 
                            For **Custom OAuth app**, configure the following fields:- 
                                    **Base URL**(Optional) – The Box API base URL. Example:`https://mcp.box.com`
- 
                                    **Client ID**– The client ID from your Box app.
- 
                                    **Client secret**– The client secret from your Box app.
 
- 
                                    
 
- 
                            
- 
                    Choose **Next**.
- 
                    A Box authorization window opens. Review the requested permissions and choose **Grant access to Box**.
- 
                    On the **Review**page, review the available actions for the connector. Choose**Next**.
- 
                    On the **Publish**page, choose who can access the connector. You can enable access for everyone in your organization or search for specific teams or groups.
- 
                    Choose **Publish**.

## Available actions

        After you set up the connector, the following actions are available.

| Category | Action | Description | 
|---|---|---|
| AI | AI Q&A (Hub) | Ask a question to a Box Hub using Box AI. | 
| AI | AI Q&A (Single File) | Ask a question to a single file using Box AI. | 
| AI | AI Q&A (Multiple Files) | Ask a question to multiple files using Box AI. | 
| AI | AI Extract (Freeform) | Extract metadata from files using Box AI in freeform format. | 
| AI | AI Extract (Structured) | Extract structured metadata from files using Box AI based on custom fields or a metadata template. | 
| Files | Get File Content | Extract and return file content in text format for files under 50 MB. | 
| Files | Get File Details | Get comprehensive file information including metadata, permissions, and version details. | 
| Files | Update File Properties | Update file metadata including name, description, tags, and collections. | 
| Files | Upload File | Upload a new file to Box. | 
| Files | Upload File Version | Upload a new version of an existing file. | 
| Files | Search Files | Search for files using keywords with support for metadata filters and file extension filtering. | 
| Folders | Create Folder | Create a new folder in Box. | 
| Folders | Get Folder Details | Retrieve comprehensive folder information including metadata and collaboration settings. | 
| Folders | List Folder Content | List files, folders, and web links in a folder. | 
| Folders | Update Folder Properties | Update folder metadata including name, description, tags, and collections. | 
| Folders | Search Folders | Search for folders by name using keyword matching. | 
| Hubs | Create Hub | Create a new hub for organizing content. | 
| Hubs | Get Hub Details | Retrieve information about a specific hub. | 
| Hubs | Get Hub Items | Retrieve items within a hub including files, folders, and web links. | 
| Hubs | List Hubs | List all hubs accessible to the current user. | 
| Hubs | Update Hub | Update the title or description of a hub. | 
| Hubs | Add Items to Hub | Add files, folders, or web links to a hub. | 
| Comments and tasks | Create File Comment | Create a new comment on a file. | 
| Comments and tasks | List File Comments | List all comments on a file. | 
| Comments and tasks | List Tasks | List all tasks associated with a file. | 
| Users | Who Am I | Return information about the currently authenticated user. | 

## Managing and troubleshooting

        For instructions on editing, sharing, or deleting your connector, see
            [Managing existing integrations](./integration-workflows.html#managing-existing-integrations).

- 
                **Authentication popup fails**– Verify that your browser allows popups from the Amazon Quick console domain.
- 
                **Invalid client credentials (Custom OAuth app)**– Verify that the Client ID and Client secret match the values in your Box Developer Console app.
- 
                **Insufficient permissions**– Verify that your Box account has access to the files, folders, or hubs you are trying to access.