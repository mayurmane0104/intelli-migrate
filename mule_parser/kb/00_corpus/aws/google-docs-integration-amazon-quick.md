# Google Docs integration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/google-docs-integration.html](https://docs.aws.amazon.com/quick/latest/userguide/google-docs-integration.html)

---

With the Google Docs action connector, you can access Google Docs directly in Amazon Quick through natural language. You can create and edit documents, read content, insert text and images, and manage document structure without leaving Amazon Quick.

Amazon Quick supports multiple authentication methods for Google Docs. Choose the method that best fits your organization's security requirements.

- 
            **Default OAuth app**– Uses an AWS-managed OAuth application. No additional credentials are needed. You authenticate directly with your Google account.
- 
            **Custom OAuth app**– Uses a customer-managed OAuth client created in the Google Cloud Console. This option gives your organization full control over the OAuth configuration.

For more information about the authentication methods that Amazon Quick
        supports, see [Authentication methods](./quick-action-auth.html).

## Before you begin

        Make sure that you have the following before you set up the integration.

- 
                A Google account with access to Google Docs. 
- 
                For **Custom OAuth app**: Access to the[Google Cloud Console](https://console.cloud.google.com/)on the Google website with permissions to create OAuth clients.
- 
                For Amazon Quick subscription requirements, see [Set up integrations in the console](./integration-console-setup-process.html).

## Configuring Google Cloud

        If you use **Default OAuth app**
            authentication, skip this section and see [Setting up the connector in Amazon Quick](#google-docs-quicksuite-setup).

For Custom OAuth app authentication,
            complete the following steps in the Google Cloud Console before you
            configure Amazon Quick. When you enable the API in step 3, search for
            and enable the **Google Docs API**.

### Create an OAuth client in Google Cloud Console

Create an OAuth client in the Google Cloud Console to get the client
        credentials that you need for Amazon Quick. For more information, see [Using OAuth
            2.0 to Access Google APIs](https://developers.google.com/identity/protocols/oauth2) on the Google website.

- 
            Sign in to the [Google Cloud Console](https://console.cloud.google.com/)on the Google website.
- 
            Create a new project or select an existing project. 
- 
            In the left navigation pane, choose **APIs & Services**, then choose**Library**. Search for the API that your integration requires and choose**Enable**.
- 
            Choose **OAuth consent screen**and choose**Get Started**.
- 
            Configure the consent screen: - 
                    Enter an **App Name**and select a**User support email**.
- 
                    For **Audience**, choose**Internal**(your organization only) or**External**(any Google user).
- 
                    Add developer contact details and choose **Create**.
 
- 
                    
- 
            Choose **Create OAuth client**.
- 
            Configure the client: - 
                    For **Application type**, choose**Web application**.
- 
                    Enter a **Name**for your client.
- 
                    Under **Authorized redirect URIs**, add the Amazon Quick callback URL:`https://``{region}`.quicksight.aws.amazon.com/sn/oauthcallback
 
- 
                    
- 
            Choose **Create**.
- 
            Record the following values. You need them when you configure Amazon Quick. - 
                    **Client ID**
- 
                    **Client secret**
 
- 
                    

### Recommended scopes

The following scopes are requested when you connect to Google Docs.

| Scope | Description | 
|---|---|
| `https://www.googleapis.com/auth/documents` | Reads and writes Google Docs documents. | 
| `https://www.googleapis.com/auth/drive` | Reads and writes files in Google Drive. | 
| `https://www.googleapis.com/auth/drive.readonly` | Reads files in Google Drive. | 
| `openid` | Authenticates the user's identity. | 
| `email` | Reads the user's email address. | 

###### Note

The `openid` and `email` scopes are
                    automatically included in the OAuth consent flow for user
                    authentication. They are not required for Service-to-Service
                    OAuth.

## Setting up the connector in Amazon Quick

         
            ### Connect from the Available tab

If you want to use Default OAuth app authentication, you can connect
                directly from the **Available** tab without additional
                configuration.

- 
                    In the Amazon Quick console, choose **Connectors**.
- 
                    On the **Available**tab, find**Google Docs**and choose**Connect**.
- 
                    Complete the Google sign-in flow and grant the requested permissions. 

To configure a connector with Custom OAuth app instead, use the
                **Create for your team** tab as described
                below.

### Create from the Create for your team tab

After you complete any required Google Cloud configuration, create the connector in Amazon Quick.

- 
                    In the Amazon Quick console, choose **Connectors**.
- 
                    Choose the **Create for your team**tab.
- 
                    Find and choose **Google Docs**.###### NoteIf a Google Docs connector already exists, a dialog appears with your existing connectors. To use an existing connector, choose it. To create a new one, choose **No, create new**.
- 
                    Enter a **Name**for your connector. Optionally, choose**+ Add Description**to add a description.
- 
                    For **Connection type**, choose**Public network**.
- 
                    For **OAuth Configuration**, choose one of the following authentication methods and configure the required fields.- 
                            For **Default OAuth app**:No additional credentials are needed. Choose **Next**to continue.
- 
                            For **Custom OAuth app**, configure the following fields:- 
                                    **Base URL**(Optional) – The Google Docs API base URL. For example:`https://docs.googleapis.com`
- 
                                    **Client ID**– The client ID from your Google Cloud OAuth client.
- 
                                    **Client secret**– The client secret from your Google Cloud OAuth client.
- 
                                    **Token URL**– The token endpoint. For example:`https://oauth2.googleapis.com/token`
- 
                                    **Authorization URL**– The authorization endpoint. For example:`https://accounts.google.com/o/oauth2/v2/auth`
- 
                                    **Redirect URL**– Pre-filled with the Amazon Quick callback URL.
 
- 
                                    
 
- 
                            
- 
                    Choose **Next**.
- 
                    If you chose **Default OAuth app**or**Custom OAuth app**, a Google authorization window opens. Review the requested permissions and choose**Allow**.
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
| Documents | Get Document | Retrieves a document by ID. | 
| Documents | Get Document Plaintext | Retrieves the plain text content of a document. | 
| Documents | Search Documents | Searches for documents. | 
| Documents | Create Document | Creates a new document. | 
| Documents | Create Document Markdown | Creates a new document from Markdown content. | 
| Documents | Copy Document | Creates a copy of an existing document. | 
| Documents | Update Document | Updates an existing document. | 
| Documents | Update Document Markdown | Updates a document with Markdown content. | 
| Documents | Update Document Section | Updates a specific section of a document with Markdown. | 
| Documents | Update Document Style | Updates the style of a document. | 
| Documents | Export Pdf | Exports a document as a PDF file. | 
| Content | Insert Text | Inserts text at a specified location. | 
| Content | Update Text | Replaces all occurrences of specified text. | 
| Content | Delete Content Range | Deletes content within a specified range. | 
| Content | Insert Inline Image | Inserts an inline image into a document. | 
| Content | Create Table | Inserts a table into a document. | 
| Content | Create Paragraph Bullets | Adds bullet formatting to paragraphs. | 
| Content | Create Named Range | Creates a named range in a document. | 
| Content | Create Page Break | Inserts a page break. | 
| Structure | Create Header | Creates a header in a document. | 
| Structure | Create Footer | Creates a footer in a document. | 

###### Note

The actions that you can use depend on the documents accessible to the authenticated user.

## Managing and troubleshooting

        To edit, share, or delete your connector, see [Managing existing integrations](./integration-workflows.html#managing-existing-integrations).

### Common Google authentication issues

- 
            **Sign-in fails (Default OAuth app or Custom OAuth app)**– Verify that your Google account is active and that you can sign in to[the Google website](https://accounts.google.com)directly. For Custom OAuth app, confirm that the redirect URI in your Google Cloud OAuth client matches the Amazon Quick callback URL.
- 
            **App blocked by administrator**– If your Google Workspace administrator restricts third-party app access, you might see an error when you attempt to sign in. Contact your Google Workspace administrator to allow the Amazon Quick app.
- 
            **Invalid client credentials (Custom OAuth app)**– Verify that the Client ID and Client secret match the values in your Google Cloud OAuth client.
- 
            **Authentication popup fails**– Verify that your browser allows popups from the Amazon Quick console domain. Try using a different browser or clearing your browser cache.
- 
            **Permissions revoked**– If you previously revoked Amazon Quick access from your Google Account permissions settings, you need to re-authenticate by editing the connector and signing in again.
- 
            **Google API rate limiting**– Google might limit requests during high usage periods. If actions fail, retry after a few minutes.

### Google Docs-specific issues

- 
                    **Google Docs API not enabled**– Verify that the Google Docs API is enabled in your Google Cloud project under**APIs & Services**,**Library**.