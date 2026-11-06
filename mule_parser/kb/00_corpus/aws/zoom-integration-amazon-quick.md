# Zoom integration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/zoom-integration.html](https://docs.aws.amazon.com/quick/latest/userguide/zoom-integration.html)

---

With the Zoom action connector, you can access the Zoom platform directly in Amazon Quick through natural language. You can create and manage meetings, access recordings and meeting summaries, view webinar details, and search contacts without leaving Amazon Quick.

Amazon Quick supports multiple authentication methods for Zoom. Choose the method that best fits your organization's security requirements.

- 
            **Default OAuth app**– Uses an AWS-managed OAuth application. No additional credentials are needed. Users authenticate directly with their Zoom account.
- 
            **Custom OAuth app**– Uses a customer-managed OAuth application registered in the Zoom App Marketplace. This option gives your organization full control over the OAuth configuration.

For more information about the authentication methods that Amazon Quick
        supports, see [Authentication methods](./quick-action-auth.html).

## Before you begin

        Make sure that you have the following before you set up the integration.

- 
                An active Zoom account with access to the meetings, recordings, and webinars that you want to use. 
- 
                For **Custom OAuth app**: Access to the[Zoom App Marketplace](https://marketplace.zoom.us/)on the Zoom website to create an app.
- 
                For Amazon Quick subscription requirements, see [Set up integrations in the console](./integration-console-setup-process.html).

## Configuring Zoom

        If you are using **Default OAuth app**
            authentication, skip this section and proceed to [Setting up the connector in Amazon Quick](#zoom-quicksuite-setup).

For Custom OAuth app authentication, complete the following steps in the Zoom App Marketplace before configuring Amazon Quick.

### Create a Zoom app (Custom OAuth app)

Create an app in the Zoom App Marketplace to obtain the client
                credentials that you need for Amazon Quick. For more information, see
                [OAuth](https://developers.zoom.us/docs/integrations/oauth/)
                on the Zoom Developer website.

- 
                    Sign in to the [Zoom App Marketplace](https://marketplace.zoom.us/)on the Zoom website and go to the app creation portal.
- 
                    Create a new application. Choose **General**for user-based OAuth or**Server-to-Server OAuth**for service-to-service authentication.
- 
                    On the **Basic Information**tab, under**App Credentials**, record the following values. You need them when you configure Amazon Quick.- 
                            **Client ID**
- 
                            **Client secret**
 
- 
                            
- 
                    In the **OAuth Information**section, for**Authorized Redirect URI**, add the Amazon Quick callback URL:`https://``{region}`.quicksight.aws.amazon.com/sn/oauthcallback
- 
                    Choose the **Scopes**tab and choose**+ Add Scopes**to select the permissions that your integration requires. For the recommended scopes, see[Recommended scopes](#zoom-oauth-scopes).

### Recommended scopes

The following scopes are requested when you connect to Zoom.
                When you create a custom Zoom app, add these scopes on the
                **Scopes** tab.

| Scope | Description | 
|---|---|
| `meeting:read:list_meetings` | Lists meetings. | 
| `meeting:read:meeting` | Reads meeting details. | 
| `meeting:read:summary` | Reads meeting summaries. | 
| `meeting:read:list_past_participants` | Lists past meeting participants. | 
| `meeting:read:list_past_instances` | Lists past meeting instances. | 
| `meeting:write:meeting` | Creates meetings. | 
| `meeting:update:meeting` | Updates meetings. | 
| `meeting:delete:meeting` | Deletes meetings. | 
| `meeting:write:registrant` | Adds meeting registrants. | 
| `cloud_recording:read:list_user_recordings` | Lists user recordings. | 
| `cloud_recording:read:list_recording_files` | Lists recording files. | 
| `cloud_recording:delete:meeting_recording` | Deletes meeting recordings. | 
| `webinar:read:webinar` | Reads webinar details. | 
| `webinar:read:list_webinars` | Lists webinars. | 
| `webinar:read:list_past_participants` | Lists past webinar participants. | 
| `webinar:read:list_registrants` | Lists webinar registrants. | 
| `webinar:write:registrant` | Adds webinar registrants. | 
| `user:read:user` | Reads user information. | 
| `user:read:settings` | Reads user settings. | 
| `user:read:list_collaboration_devices` | Lists collaboration devices. | 
| `contact:read:list_contacts` | Lists contacts. | 

###### Note

Additional scopes for whiteboard and marketplace features are also requested. The scopes listed above cover the primary meeting, recording, webinar, user, and contact actions.

## Setting up the connector in Amazon Quick

         
            ### Connect from the Available tab

If you want to use Default OAuth app authentication, you can connect
                directly from the **Available** tab without additional
                configuration.

- 
                    In the Amazon Quick console, choose **Connectors**.
- 
                    On the **Available**tab, find**Zoom**and choose**Connect**.
- 
                    Complete the Zoom sign-in flow and grant the requested permissions. 

To configure a connector with Custom OAuth app instead,
                use the **Create for your team** tab as described
                below.

### Create from the Create for your team tab

After you complete any required Zoom configuration, create the connector in Amazon Quick.

- 
                    In the Amazon Quick console, choose **Connectors**.
- 
                    Choose the **Create for your team**tab.
- 
                    Find and choose **Zoom**.###### NoteIf a Zoom connector already exists, a dialog appears with your existing connectors. To use an existing connector, choose it. To create a new one, choose **No, create new**.
- 
                    Enter a **Name**for your connector. Optionally, choose**+ Add Description**to add a description.
- 
                    For **Connection type**, choose**Public network**.
- 
                    For **OAuth Configuration**, choose one of the following authentication methods and configure the required fields.- 
                            For **Default OAuth app**:No additional credentials are needed. Choose **Next**to continue.
- 
                            For **Custom OAuth app**, configure the following fields:- 
                                    **Base URL**(Optional) – The Zoom API base URL. Example:`https://api.zoom.us`
- 
                                    **Client ID**– The client ID from your Zoom app.
- 
                                    **Client secret**– The client secret from your Zoom app.
- 
                                    **Token URL**– The token endpoint. Example:`https://zoom.us/oauth/token`
- 
                                    **Authorization URL**– The authorization endpoint. Example:`https://zoom.us/oauth/authorize`
- 
                                    **Redirect URL**– Pre-filled with the Amazon Quick callback URL.
 
- 
                                    
 
- 
                            
- 
                    Choose **Next**.
- 
                    If you chose **Default OAuth app**or**Custom OAuth app**, a Zoom authorization window opens. Review the requested permissions and choose**Allow**.
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
| Meetings | List Meetings | Lists meetings for a user. | 
| Meetings | Get Meeting | Retrieves details for a specific meeting. | 
| Meetings | Create Meeting | Creates a new meeting. | 
| Meetings | Update Meeting | Updates an existing meeting. | 
| Meetings | Get Meeting Summary | Retrieves the AI-generated summary for a meeting. | 
| Meetings | List Meeting Summary Templates | Lists available meeting summary templates. | 
| Meetings | Get Past Meeting Participants | Retrieves participants from a past meeting. | 
| Meetings | List Past Meeting Instances | Lists instances of a recurring meeting. | 
| Meetings | Create Meeting Registrant | Adds a registrant to a meeting. | 
| Recordings | List Recordings | Lists all recordings for a user. | 
| Recordings | Get Meeting Recordings | Retrieves recordings for a specific meeting. | 
| Recordings | List Archived Files | Lists archived recording files. | 
| Webinars | List Webinars | Lists webinars for a user. | 
| Webinars | Get Webinar | Retrieves details for a specific webinar. | 
| Webinars | List Webinar Participants | Lists participants for a webinar. | 
| Contacts | Search Company Contacts | Searches for contacts in the company directory. | 
| Devices | List Devices | Lists Zoom devices. | 
| Reports | Get Daily Usage Report | Retrieves a daily usage report. | 
| Users | Get User | Retrieves information about the authenticated user. | 

###### Note

The actions that you can use depend on the permissions configured for your Zoom account and the data accessible to the authenticated user.

## Managing and troubleshooting

        To edit, share, or delete your connector, see [Managing existing integrations](./integration-workflows.html#managing-existing-integrations).

### Authentication issues

- 
                    **Sign-in fails (Default OAuth app or Custom OAuth app)**– Verify that your Zoom account is active and that you can sign in to[zoom.us](https://zoom.us)on the Zoom website directly. For Custom OAuth app, confirm that the redirect URI in your Zoom app matches the Amazon Quick callback URL.
- 
                    **Invalid client credentials (Custom OAuth app)**– Verify that the Client ID and Client secret match the values in your Zoom app. You can view your credentials from the app settings in the Zoom App Marketplace.
- 
                    **Insufficient permissions**– Verify that the scopes configured for your Zoom app include the permissions required for the actions that you want to use. See[Recommended scopes](#zoom-oauth-scopes).