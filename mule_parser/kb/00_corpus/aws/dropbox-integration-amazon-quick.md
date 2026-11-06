# Dropbox integration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/dropbox-integration.html](https://docs.aws.amazon.com/quick/latest/userguide/dropbox-integration.html)

---

With the Dropbox action connector, you can access the Dropbox platform directly in Amazon Quick through natural language. You can upload files, manage folder structures, generate sharing links, and search for content without leaving Amazon Quick.

Amazon Quick supports multiple authentication methods for Dropbox. Choose the method that best fits your organization's security requirements.

- 
            **Default OAuth app**– Uses an AWS-managed OAuth application. No additional credentials are needed. You authenticate directly with your Dropbox account.
- 
            **Custom OAuth app**– Uses a customer-managed OAuth application that is registered in Dropbox. This option gives your organization full control over the OAuth configuration.
- 
            **API Key**– Uses a Dropbox access token for authentication. This method is suitable for individual use or testing.

For more information about the authentication methods that Amazon Quick supports, see
        [Authentication methods](./quick-action-auth.html).

## Before you begin

        Make sure that you have the following before you set up the integration.

- 
                An active Dropbox account with access to the files and folders that you want to use. 
- 
                For **Custom OAuth app**: Access to the[Dropbox App Console](https://www.dropbox.com/developers/apps)on the Dropbox website to create an app.
- 
                For **API Key**: An access token that is generated from the[Dropbox App Console](https://www.dropbox.com/developers/apps)on the Dropbox website.
- 
                For Amazon Quick subscription requirements, see [Set up integrations in the console](./integration-console-setup-process.html).

## Configuring Dropbox

        If you are using **Default OAuth app**
            authentication, skip this section and go to [Setting up the connector in Amazon Quick](#dropbox-quicksuite-setup).

For Custom OAuth app or API Key authentication, complete the applicable steps in Dropbox before you configure Amazon Quick.

### Create a Dropbox app for Custom OAuth app

Create an app in the Dropbox App Console to get the client credentials that you need for Amazon Quick.

- 
                    Sign in to your Dropbox account and go to the [Dropbox App Console](https://www.dropbox.com/developers/apps)on the Dropbox website.
- 
                    Choose **Create app**.
- 
                    For **Choose an API**, select**Scoped access**.
- 
                    Choose the type of access that you need: - 
                            **App folder**– Provides access only to a specific folder.
- 
                            **Full Dropbox**– Provides access to all files and folders.
 
- 
                            
- 
                    Enter an app name and choose **Create app**.
- 
                    On the app settings page, record the following values. You need them when you configure Amazon Quick. - 
                            **App key**– This is your Client ID.
- 
                            **App secret**– This is your Client secret.
 
- 
                            
- 
                    Under **OAuth 2**, in the**Redirect URIs**section, add the Amazon Quick callback URL:`https://``{region}`.quicksight.aws.amazon.com/sn/oauthcallback
- 
                    Choose the **Permissions**tab and select the scopes that your integration requires. For the recommended scopes, see[Recommended scopes](#dropbox-oauth-scopes).

### Generate an access token for API Key

Generate an access token from the Dropbox App Console for API Key authentication.

- 
                    Sign in to your Dropbox account and go to the [Dropbox App Console](https://www.dropbox.com/developers/apps)on the Dropbox website.
- 
                    Choose your app, or create a new one if needed. 
- 
                    Under **OAuth 2**, choose**Generate**to create an access token.
- 
                    Copy and securely store the generated token. You need it when you configure Amazon Quick. 

### Recommended scopes

When you create a Dropbox app, configure the following scopes on the
                **Permissions** tab based on the actions that you want
                to use.

| Scope | Description | 
|---|---|
| `account_info.read` | Reads account information. | 
| `account_info.write` | Updates account information. | 
| `contacts.read` | Reads contact information. | 
| `contacts.write` | Updates contact information. | 
| `events.read` | Reads event log entries. | 
| `events.write` | Creates event log entries. | 
| `file_requests.read` | Reads file requests. | 
| `file_requests.write` | Creates and manages file requests. | 
| `files.content.read` | Reads file content. | 
| `files.content.write` | Creates, modifies, and deletes files. | 
| `files.metadata.read` | Reads file and folder metadata. | 
| `files.metadata.write` | Edits file and folder metadata. | 
| `files.permanent_delete` | Permanently deletes files. | 
| `files.team_metadata.read` | Reads team file metadata. | 
| `files.team_metadata.write` | Edits team file metadata. | 
| `groups.read` | Reads group information. | 
| `groups.write` | Manages groups. | 
| `members.delete` | Removes team members. | 
| `members.read` | Reads team member information. | 
| `members.write` | Manages team members. | 
| `sessions.list` | Lists active sessions. | 
| `sessions.modify` | Modifies active sessions. | 
| `sharing.read` | Reads sharing settings and shared links. | 
| `sharing.write` | Creates and manages shared links and folder sharing. | 
| `team_data.content.read` | Reads team content. | 
| `team_data.content.write` | Manages team content. | 
| `team_data.governance.read` | Reads team data governance settings. | 
| `team_data.governance.write` | Manages team data governance settings. | 
| `team_data.team_space` | Accesses team space data. | 
| `team_info.read` | Reads team information. | 
| `team_info.write` | Updates team information. | 

## Setting up the connector in Amazon Quick

         
            ### Connect from the Available tab

If you want to use Default OAuth app authentication, you can connect
                directly from the **Available** tab without additional
                configuration.

- 
                    In the Amazon Quick console, choose **Connectors**.
- 
                    On the **Available**tab, find**Dropbox**and choose**Connect**.
- 
                    Complete the Dropbox sign-in flow and grant the requested permissions. 

To configure a connector with Custom OAuth app or API Key instead,
                use the **Create for your team** tab as described
                below.

### Create from the Create for your team tab

After you complete any required Dropbox configuration, create the connector in Amazon Quick.

- 
                    In the Amazon Quick console, choose **Connectors**.
- 
                    Choose the **Create for your team**tab.
- 
                    Find and choose **Dropbox**.###### NoteIf a Dropbox connector already exists, a dialog appears with your existing connectors. To use an existing connector, choose it. To create a new one, choose **No, create new**.
- 
                    Enter a **Name**for your connector. Optionally, choose**+ Add Description**to add a description.
- 
                    For **Connection type**, choose**Public network**.
- 
                    For **OAuth Configuration**, choose one of the following authentication methods and configure the required fields.- 
                            For **Default OAuth app**:No additional credentials are needed. Choose **Next**to continue.
- 
                            For **Custom OAuth app**, configure the following fields:- 
                                    **Base URL**(Optional) – The Dropbox API base URL. Example:`https://api.dropboxapi.com`
- 
                                    **Client ID**– The app key from your Dropbox app.
- 
                                    **Client secret**– The app secret from your Dropbox app.
- 
                                    **Token URL**– The token endpoint. Example:`https://api.dropboxapi.com/oauth2/token`
- 
                                    **Authorization URL**– The authorization endpoint. Example:`https://www.dropbox.com/oauth2/authorize`
- 
                                    **Redirect URL**– Pre-filled with the Amazon Quick callback URL.
 
- 
                                    
- 
                            For **API Key**, configure the following fields:- 
                                    **Base URL**(Optional) – The Dropbox API base URL. Example:`https://api.dropboxapi.com`
- 
                                    **API Key**– Your Dropbox access token.
- 
                                    **Email**(Optional) – The email address that is associated with your Dropbox account.
 
- 
                                    
 
- 
                            
- 
                    Choose **Next**.
- 
                    If you chose **Default OAuth app**or**Custom OAuth app**, a Dropbox authorization window opens. Review the requested permissions and choose**Allow**.
- 
                    On the **Review**page, review the available actions for the connector. Choose**Next**.
- 
                    On the **Publish**page, choose who can access the connector. You can turn on access for everyone in your organization or search for specific teams or groups.
- 
                    Choose **Publish**.

## Available actions

        After you set up the connector, the following actions are available.

| Category | Action | Description | 
|---|---|---|
| Files | List Files | Lists files in a folder. | 
| Files | Get File | Reads the content of a file. | 
| Files | Import File | Uploads a file to Dropbox. | 
| Files | Search Files | Searches for files or folders by name or content. | 
| Files | Update File Location | Moves a file or folder to a different location. | 
| Files | Get Temporary Link | Generates a temporary download link for a file. | 
| Files | Get Metadata | Retrieves metadata for a file or folder. | 
| Files | Save File From URL | Saves a file to Dropbox from a URL. | 
| Folders | Create Folder | Creates a new folder. | 
| Folders | List Folders | List of folders user has access to. | 
| Batch operations | Get Batch Move Status | Checks the status of a batch move operation. | 
| Sharing | Create Shared Link | Creates a shared link for a file or folder. | 
| Sharing | List Shared Links | Lists shared links for a file or folder. | 
| Sharing | Update Folder Sharing | Shares a folder with other users. | 
| Sharing | List Received Files | Lists files that other users have shared with you. | 
| File requests | Create File Request | Creates a file request for others to upload files to. | 
| Account | Get User | Retrieves information about the authenticated user. | 
| Account | Get Space Usage | Retrieves storage space usage for the account. | 

###### Note

The actions that you can use depend on the files and folders that are accessible to the authenticated user.

## Managing and troubleshooting

        To edit, share, or delete your connector, see [Managing existing integrations](./integration-workflows.html#managing-existing-integrations).

### Authentication issues

- 
                    **Sign-in fails (Default OAuth app or Custom OAuth app)**– Verify that your Dropbox account is active and that you can sign in to[the Dropbox website](https://www.dropbox.com)directly. For Custom OAuth app, confirm that the redirect URL in your Dropbox app matches the Amazon Quick callback URL.
- 
                    **Invalid client credentials (Custom OAuth app)**– Verify that the Client ID and Client secret match the app key and app secret values in your Dropbox app. If you regenerated the app secret, update the value in Amazon Quick.
- 
                    **API Key rejected**– Verify that your access token is active. Tokens can expire or be revoked in the Dropbox App Console.
- 
                    **Insufficient permissions**– Verify that your Dropbox app has the required permission scopes for the actions that you want to use.