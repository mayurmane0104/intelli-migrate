# Airtable integration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/airtable-integration.html](https://docs.aws.amazon.com/quick/latest/userguide/airtable-integration.html)

---

With the Airtable action connector, you can access the Airtable platform directly in Amazon Quick through natural language. You can create and update records, manage bases and tables, filter views, and perform relational data operations without leaving Amazon Quick.

Amazon Quick supports multiple authentication methods for Airtable. Choose the method that best fits your organization's security requirements.

- 
            **Default OAuth app**– Uses an AWS-managed OAuth application. No additional credentials are needed. Users authenticate directly with their Airtable account.
- 
            **Custom OAuth app**– Uses a customer-managed OAuth application registered in Airtable. This option gives your organization full control over the OAuth configuration.
- 
            **API Key**– Uses an Airtable personal access token for authentication. Suitable for individual use or testing.

For more information about the authentication methods that Amazon Quick supports, see
        [Authentication methods](./quick-action-auth.html).

## Before you begin

        Make sure that you have the following before you set up the integration.

- 
                An active Airtable account with access to the bases and data that you want to use. 
- 
                For **Custom OAuth app**: Access to the[Airtable Builder Hub](https://airtable.com/create/oauth)on the Airtable website to register an OAuth integration.
- 
                For **API Key**: A personal access token from the[Airtable Builder Hub](https://airtable.com/create/tokens)on the Airtable website.
- 
                For Amazon Quick subscription requirements, see [Set up integrations in the console](./integration-console-setup-process.html).

## Configuring Airtable

        If you are using **Default OAuth app**
            authentication, skip this section and proceed to [Setting up the connector in Amazon Quick](#airtable-quicksuite-setup).

For Custom OAuth app or API Key authentication, complete the applicable steps in Airtable before configuring Amazon Quick.

### Register an OAuth integration (Custom OAuth app)

Create an OAuth integration in the Airtable Builder Hub to obtain the client credentials that you need for Amazon Quick.

- 
                    Sign in to the [Airtable Builder Hub](https://airtable.com/create/oauth)on the Airtable website and choose**OAuth integrations**.
- 
                    Choose **Register new OAuth integration**.
- 
                    Enter a **Name**for your integration.
- 
                    For **OAuth redirect URLs**, enter the redirect URL from Amazon Quick:`https://``{region}`.quicksight.aws.amazon.com/sn/oauthcallback
- 
                    Choose **Register integration**.
- 
                    After registration, generate a client secret by choosing **Regenerate client secret**.
- 
                    Record the following values. You need them when you configure Amazon Quick. - 
                            **Client ID**
- 
                            **Client secret**
 
- 
                            
- 
                    Under **Scopes**, select the permissions that your integration requires. For the full list of recommended scopes, see[Recommended scopes](#airtable-oauth-scopes).

### Create a personal access token (API Key)

Create a personal access token in the Airtable Builder Hub for API Key authentication.

- 
                    Sign in to the [Airtable Builder Hub](https://airtable.com/create/tokens)on the Airtable website and choose**Personal access tokens**.
- 
                    Choose **Create token**.
- 
                    Configure the token name, scopes, and base access as needed for your use case. 
- 
                    Copy and securely store the generated token. You need it when you configure Amazon Quick. 

### Recommended scopes

When you register an OAuth integration or create a personal access token, configure the following scopes based on the actions that you want to use.

| Scope | Description | 
|---|---|
| `data.records:read` | Read data in records. | 
| `data.records:write` | Create, edit, and delete records. | 
| `data.recordComments:read` | Read comments in records. | 
| `data.recordComments:write` | Create, edit, and delete record comments. | 
| `schema.bases:read` | Read the structure of bases, including table names and field types. | 
| `schema.bases:write` | Edit the structure of bases, including table names and field types. | 
| `user.email:read` | Read the email address of the authenticated user. | 

## Setting up the connector in Amazon Quick

         
            ### Connect from the Available tab

If you want to use Default OAuth app authentication, you can connect
                directly from the **Available** tab without additional
                configuration.

- 
                    In the Amazon Quick console, choose **Connectors**.
- 
                    On the **Available**tab, find**Airtable**and choose**Connect**.
- 
                    Complete the Airtable sign-in flow and grant the requested permissions. 

To configure a connector with Custom OAuth app or API Key instead,
                use the **Create for your team** tab as described
                below.

### Create from the Create for your team tab

After you complete any required Airtable configuration, create the connector in Amazon Quick.

- 
                    In the Amazon Quick console, choose **Connectors**.
- 
                    Choose the **Create for your team**tab.
- 
                    Find and choose **Airtable**.###### NoteIf an Airtable connector already exists, a dialog appears with your existing connectors. To use an existing connector, choose it. To create a new one, choose **No, create new**.
- 
                    Enter a **Name**for your connector. Optionally, choose**+ Add Description**to add a description.
- 
                    For **Connection type**, choose**Public network**.
- 
                    For **OAuth Configuration**, choose one of the following authentication methods and configure the required fields.- 
                            For **Default OAuth app**:No additional credentials are needed. Choose **Next**to continue.
- 
                            For **Custom OAuth app**, configure the following fields:- 
                                    **Base URL**(Optional) – The Airtable API base URL. Example:`https://api.airtable.com`
- 
                                    **Client ID**– The client ID from your Airtable OAuth integration.
- 
                                    **Client secret**– The client secret from your Airtable OAuth integration.
- 
                                    **Token URL**– The token endpoint. Example:`https://airtable.com/oauth2/v1/token`
- 
                                    **Authorization URL**– The authorization endpoint. Example:`https://airtable.com/oauth2/v1/authorize`
- 
                                    **Redirect URL**– Pre-filled with the Amazon Quick callback URL.
 
- 
                                    
- 
                            For **API Key**, configure the following fields:- 
                                    **Base URL**(Optional) – The Airtable API base URL. Example:`https://api.airtable.com`
- 
                                    **API Key**– Your Airtable personal access token.
- 
                                    **Email**(Optional) – The email address associated with your Airtable account.
 
- 
                                    
 
- 
                            
- 
                    Choose **Next**.
- 
                    If you chose **Default OAuth app**or**Custom OAuth app**, an Airtable authorization window opens. Review the requested permissions, choose the bases and workspaces to grant access to, and choose**Grant access**.
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
| Records | List Records | Lists records in a table with optional filtering and sorting. | 
| Records | Get Record | Retrieves a specific record by ID. | 
| Records | Batch Create Record | Creates one or more new records in a table. | 
| Records | Update Record | Updates fields on an existing record. | 
| Records | Batch Update Record | Updates multiple records in a single operation using PATCH. | 
| Records | Batch Put Record | Upserts multiple records in a single operation using PUT. | 
| Comments | List Comments | Lists comments on a record. | 
| Comments | Create Comment | Adds a comment to a record. | 
| Comments | Update Comment | Edits an existing comment on a record. | 
| Schema | List Bases | Lists all bases accessible to the authenticated user. | 
| Schema | Get Base Schema | Retrieves the schema of a base, including tables and field definitions. | 
| Schema | Create Table | Creates a new table in a base. | 
| Schema | Update Table | Updates table properties such as name or description. | 
| Schema | Create Field | Adds a new field to a table. | 
| Schema | Update Field | Updates field properties such as name or type. | 
| Attachments | Create Attachment | Uploads an attachment to a record. | 
| Users | Get User Info | Retrieves information about the authenticated user. | 

###### Note

The actions that you can use depend on the bases and workspaces accessible to the authenticated user.

## Managing and troubleshooting

        To edit, share, or delete your connector, see [Managing existing integrations](./integration-workflows.html#managing-existing-integrations).

### Authentication issues

- 
                    **Sign-in fails (Default OAuth app or Custom OAuth app)**– Verify that your Airtable account is active and that you can sign in to[airtable.com](https://airtable.com)on the Airtable website directly. For Custom OAuth app, confirm that the redirect URL in your Airtable OAuth integration matches the Amazon Quick callback URL.
- 
                    **Invalid client credentials (Custom OAuth app)**– Verify that the Client ID and Client secret match the values in your Airtable OAuth integration. If you regenerated the client secret, update the value in Amazon Quick.
- 
                    **API Key rejected**– Verify that your personal access token is active and has the required scopes. Tokens can be revoked or expired in the Airtable Builder Hub.
- 
                    **Insufficient permissions**– Verify that the scopes configured for your authentication method include the permissions required for the actions that you want to use. See[Recommended scopes](#airtable-oauth-scopes).