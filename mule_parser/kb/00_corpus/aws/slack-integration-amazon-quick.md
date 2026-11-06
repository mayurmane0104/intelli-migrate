# Slack integration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/slack-integration.html](https://docs.aws.amazon.com/quick/latest/userguide/slack-integration.html)

---

With the Slack action connector, you can access the Slack platform directly in Amazon Quick through natural language. You can send messages, manage channels, search content, and interact with users and user groups without leaving Amazon Quick.

Amazon Quick supports multiple authentication methods for Slack. Choose the method that best fits your organization's security requirements.

- 
            **Default OAuth app**– Uses an AWS-managed OAuth application. No additional credentials are needed. You authenticate directly with your Slack workspace.
- 
            **Custom OAuth app**– Uses a customer-managed Slack app. This option gives your organization full control over the OAuth configuration.
- 
            **Bearer Token**– Uses a Slack bot token for authentication. This method is suitable for bot-level access to a workspace.

For more information about the authentication methods that Amazon Quick
        supports, see [Authentication methods](./quick-action-auth.html).

## Before you begin

        Make sure that you have the following before you set up the integration.

- 
                A Slack workspace with access to the channels and data that you want to use. 
- 
                For **Custom OAuth app**: Access to the[Slack API dashboard](https://api.slack.com/apps)on the Slack website to create an app.
- 
                For **Bearer Token**: A bot token (starts with`xoxb-`) from a Slack app. For more information, see[Quickstart app settings](https://docs.slack.dev/app-management/quickstart-app-settings)on the Slack website.
- 
                For Amazon Quick subscription requirements, see [Set up integrations in the console](./integration-console-setup-process.html).

## Configuring Slack

        If you are using **Default OAuth app**
            authentication, skip this section and go to [Setting up the connector in Amazon Quick](#slack-quicksuite-setup).

For Custom OAuth app or Bearer Token authentication, complete the applicable steps in Slack before you configure Amazon Quick.

### Create a Slack app for Custom OAuth app or Bearer Token

Create a Slack app to get the client credentials or bot token that you need for Amazon Quick.

- 
                    Go to the [Slack API dashboard](https://api.slack.com/apps)on the Slack website and choose**Create New App**.
- 
                    Choose **From scratch**.
- 
                    Enter an **App Name**and select your Slack workspace. Choose**Create App**.
- 
                    In the left sidebar, choose **OAuth & Permissions**.
- 
                    Under **Redirect URLs**, choose**Add New Redirect URL**and enter the Amazon Quick callback URL:`https://``{region}`.quicksight.aws.amazon.com/sn/oauthcallbackChoose **Add**, then choose**Save URLs**.
- 
                    Under **Scopes**, add the Bot Token Scopes that your integration requires. For the recommended scopes, see[Recommended scopes](#slack-oauth-scopes).
- 
                    In the left sidebar, choose **Basic Information**. Under**App Credentials**, record the following values:- 
                            **Client ID**
- 
                            **Client secret**
 
- 
                            
- 
                    For **Bearer Token**: Install the app to your workspace from the**OAuth & Permissions**page. After installation, copy the**Bot User OAuth Token**(starts with`xoxb-`).

### Recommended scopes

The following scopes are requested when you connect to Slack.
                When you create a custom Slack app, add these scopes on the
                **OAuth & Permissions** page. For Custom OAuth
                app, add them as **User Token Scopes**. For Bearer
                Token, add them as **Bot Token Scopes**.

| Scope | Description | 
|---|---|
| `calls:read` | Reads call information. | 
| `calls:write` | Creates and manages calls. | 
| `channels:history` | Reads message history in public channels. | 
| `channels:read` | Reads information about public channels. | 
| `channels:write` | Manages public channels. | 
| `chat:write` | Sends messages to channels and conversations. | 
| `dnd:read` | Reads Do Not Disturb settings. | 
| `dnd:write` | Updates Do Not Disturb settings. | 
| `emoji:read` | Reads custom emoji. | 
| `files:read` | Reads files shared in channels. | 
| `files:write` | Uploads and manages files. | 
| `groups:history` | Reads message history in private channels. | 
| `groups:read` | Reads information about private channels. | 
| `groups:write` | Manages private channels. | 
| `im:history` | Reads message history in direct messages. | 
| `im:read` | Reads information about direct messages. | 
| `im:write` | Starts direct messages. | 
| `links:read` | Reads link previews. | 
| `links:write` | Manages link previews. | 
| `mpim:history` | Reads message history in group direct messages. | 
| `mpim:read` | Reads information about group direct messages. | 
| `mpim:write` | Starts group direct messages. | 
| `pins:read` | Reads pinned messages. | 
| `pins:write` | Pins and unpins messages. | 
| `reactions:read` | Reads emoji reactions on messages. | 
| `reactions:write` | Adds and removes emoji reactions. | 
| `reminders:read` | Reads reminders. | 
| `reminders:write` | Creates reminders. | 
| `remote_files:read` | Reads remote files. | 
| `remote_files:share` | Shares remote files. | 
| `search:read` | Searches messages and files. | 
| `stars:read` | Reads starred items. | 
| `stars:write` | Stars and unstars items. | 
| `team:read` | Reads workspace information. | 
| `usergroups:read` | Reads user group information. | 
| `usergroups:write` | Manages user groups. | 
| `users:read` | Reads user information. | 
| `users:read.email` | Reads user email addresses. | 
| `users:write` | Updates user information. | 
| `users.profile:read` | Reads user profile information. | 
| `users.profile:write` | Updates user profile information. | 

###### Note

Not all scopes are available for both User Token Scopes and
                    Bot Token Scopes. Some scopes, such as `search:read`
                    and `stars:read`, are available only as User Token
                    Scopes. When you configure scopes for Bearer Token
                    authentication, verify scope availability in the
                    [Slack API scopes
                        reference](https://api.slack.com/scopes) on the Slack website.

## Setting up the connector in Amazon Quick

         
            ### Connect from the Available tab

If you want to use Default OAuth app authentication, you can connect
                directly from the **Available** tab without additional
                configuration.

- 
                    In the Amazon Quick console, choose **Connectors**.
- 
                    On the **Available**tab, find**Slack**and choose**Connect**.
- 
                    Complete the Slack sign-in flow and grant the requested permissions. 

To configure a connector with Custom OAuth app or Bearer Token
                instead, use the **Create for your team** tab as
                described below.

### Create from the Create for your team tab

After you complete any required Slack configuration, create the connector in Amazon Quick.

- 
                    In the Amazon Quick console, choose **Connectors**.
- 
                    Choose the **Create for your team**tab.
- 
                    Find and choose **Slack**.###### NoteIf a Slack connector already exists, a dialog appears with your existing connectors. To use an existing connector, choose it. To create a new one, choose **No, create new**.
- 
                    Enter a **Name**for your connector. Optionally, choose**+ Add Description**to add a description.
- 
                    For **Connection type**, choose**Public network**.
- 
                    For **OAuth Configuration**, choose one of the following authentication methods and configure the required fields.- 
                            For **Default OAuth app**:No additional credentials are needed. Choose **Next**to continue.
- 
                            For **Custom OAuth app**, configure the following fields:- 
                                    **Base URL**(Optional) – The Slack API base URL. Example:`https://slack.com/api`
- 
                                    **Client ID**– The client ID from your Slack app.
- 
                                    **Client secret**– The client secret from your Slack app.
- 
                                    **Token URL**– The token endpoint. Example:`https://slack.com/api/oauth.v2.access`
- 
                                    **Authorization URL**– The authorization endpoint. Example:`https://slack.com/oauth/v2/authorize`
- 
                                    **Redirect URL**– Pre-filled with the Amazon Quick callback URL.
 
- 
                                    
- 
                            For **Bearer Token**, configure the following fields:- 
                                    **Base URL**(Optional) – The Slack API base URL. Example:`https://slack.com/api`
- 
                                    **Bot token**– Your Slack bot token (starts with`xoxb-`).
 
- 
                                    
 
- 
                            
- 
                    Choose **Next**.
- 
                    If you chose **Default OAuth app**or**Custom OAuth app**, a Slack authorization window opens. Review the requested permissions, select your workspace, and choose**Allow**.
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
| Messages | Chat Post Message | Posts a message to a channel, direct message, or private group. | 
| Messages | Send Me Message | Sends a third-person action message to a channel. | 
| Messages | Get Message Permalink | Retrieves a permalink URL for a specific message. | 
| Channels | Conversations Create | Creates a public or private channel. | 
| Channels | Conversations History | Retrieves message history from a channel. Returns main timeline messages only, not threaded replies. | 
| Channels | Conversations Replies | Retrieves threaded replies to a specific parent message. | 
| Channels | Conversations Invite | Invites users to an existing channel. | 
| Channels | Conversations Join | Joins an existing channel. | 
| Channels | Conversations Kick | Removes a user from a channel. | 
| Channels | Conversations Leave | Leaves a channel. | 
| Channels | Conversations Members | Lists member IDs for a channel. | 
| Channels | Conversations Open | Opens or resumes a direct message or multi-person direct message. | 
| Channels | Conversations Set Topic | Sets or updates the topic for a channel. | 
| Channels | Get Conversation | Retrieves metadata for a channel by ID. | 
| Channels | List Channels | Lists channels available to the user. | 
| Channels | List Conversations For User | Lists channels and direct messages accessible to a user. | 
| Reactions | Create Reaction | Adds an emoji reaction to a message. | 
| Reactions | Delete Reaction | Removes an emoji reaction from a message. | 
| Reactions | List Reactions | Lists reactions on a message, file, or file comment. | 
| Files | Upload Or Create File | Uploads files or media to channels or threads. | 
| Files | Upload To URL External | Adds a reference to an external file for sharing in Slack. | 
| Files | Download File | Downloads a file shared in Slack. | 
| Files | Files Info | Retrieves metadata and comments for a file. | 
| Files | Files List | Lists files in a workspace with optional filters. | 
| Search | Search All | Searches messages and files across the workspace. | 
| Search | Search Messages | Searches messages with date ranges and filters. | 
| Search | Search Channels | Searches channels by name, topic, or purpose. | 
| Search | Search Users | Searches users by email, name, or display name. | 
| Search | Search Context | Searches across messages, files, channels, and users. Supports semantic search on workspaces with Slack AI. | 
| Search | Get Search Configuration | Checks whether semantic search is available on the workspace. | 
| Users | Get User Details | Retrieves information for a user by ID. | 
| Users | Get User Profile | Retrieves profile information for a user. | 
| Users | Users Profile Set | Updates a user's profile fields. | 
| Users | Users List | Lists all users in the workspace. | 
| User groups | User Groups Create | Creates a new user group. | 
| User groups | User Groups List | Lists user groups in the workspace. | 
| User groups | User Groups Users Update | Replaces all members of a user group. | 
| Reminders | Reminders Add | Creates a reminder with specified text and time. | 
| Workspace | Get Team | Retrieves metadata about the Slack workspace. | 

###### Note

The actions that you can use depend on the scopes configured for your Slack app and the channels accessible to the authenticated user.

## Managing and troubleshooting

        To edit, share, or delete your connector, see [Managing existing integrations](./integration-workflows.html#managing-existing-integrations).

### Authentication issues

- 
                    **Sign-in fails (Default OAuth app or Custom OAuth app)**– Verify that your Slack workspace is active and that you can sign in to[the Slack website](https://slack.com)directly. For Custom OAuth app, confirm that the redirect URL in your Slack app matches the Amazon Quick callback URL.
- 
                    **Invalid client credentials (Custom OAuth app)**– Verify that the Client ID and Client secret match the values in your Slack app's Basic Information section.
- 
                    **Bearer Token rejected**– Verify that your bot token is active and starts with`xoxb-`. Tokens can be revoked from the Slack API dashboard.
- 
                    **Insufficient permissions**– Verify that the scopes configured for your Slack app include the permissions required for the actions that you want to use. See[Recommended scopes](#slack-oauth-scopes).
- 
                    **Channel not found or not in channel**– Verify that the bot has been added to the channel. Invite the bot to the channel before attempting to post messages or read history.