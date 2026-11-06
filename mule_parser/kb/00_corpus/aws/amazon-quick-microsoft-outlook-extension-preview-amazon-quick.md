# Amazon Quick Microsoft Outlook extension (Preview) - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/outlook-extension.html](https://docs.aws.amazon.com/quick/latest/userguide/outlook-extension.html)

---

###### Note

This extension is currently available as a preview. During the preview period, the extension is fully functional for end users and production workloads. Administrative features such as centralized deployment controls and usage monitoring are being developed and will be available when the extension becomes generally available. Functionality and features may change during the preview period. We recommend using this extension instead of the legacy Microsoft Outlook extension for new deployments.

The Quick extension for Microsoft Outlook integrates AI-powered assistance directly into your email workflows. Users can leverage Quick within Outlook to streamline their inbox and calendar management, draft contextual emails using their Quick data, and perform external actions without switching applications.

The Outlook extension enables users to:

- 
                Prioritize and organize their inbox. 
- 
                Search for relevant email content for a topic using natural language. 
- 
                Schedule meetings and manage their calendars. 
- 
                Summarize emails and draft contextual responses using Quick data. 
- 
                Access their enterprise data and perform actions in external applications. 

The Amazon Quick Outlook extension is available within Amazon Quick
            to all eligible users by default and requires no administrative setup for user access if
            users can access the Microsoft Outlook app store. Users can search for
            Amazon Quick in the Microsoft Outlook app store or visit the [Quick
                for Outlook Microsoft store page](https://marketplace.microsoft.com/en-us/product/WA200010695) to add the extension.

###### Important

- 
                    The Amazon Quick Outlook extension uses generative AI to create and execute code within your Outlook application sandbox to help you perform your Outlook tasks. AI can make mistakes and perform inaccurate actions within your Outlook mailbox. 
- 
                    Amazon Quick does not use your user data for service improvement or for training its underlying large language models (LLMs). 

The following procedures are for IT administrators who want to automatically deploy the Amazon Quick Outlook extension across their organization on behalf of their users.

###### Topics

## Prerequisites for deploying the Microsoft Outlook extension to your organization

            Before configuring access to the Amazon Quick extension to Microsoft Outlook, administrators must complete the following steps:

- 
                    Have a Microsoft 365 Business subscription and be a Global Admin or have administrative permissions (specifically `AppCatalog.ReadWrite.All`).
- 
                    Have an Amazon Quick instance. 
- 
                    Grant tenant-wide admin consent for Microsoft Graph permissions. This allows the extension to access inbox, calendar, and contact data for all users in your organization. Without these permissions, the extension can only respond to questions about the currently open email thread. For instructions, see [Grant tenant-wide admin consent](#outlook-grant-admin-consent).

## Microsoft Outlook extension permissions

            The Amazon Quick Outlook extension uses the
                `ReadWriteMailbox` Office JavaScript API permission level. This is an
                Office add-in manifest permission, not a Microsoft Graph API
                scope.

The default app capabilities for the Outlook add-in are:

- 
                    Can read and make changes to your document 
- 
                    Access your profile information such as your name, email address, company name, and preferred language 
- 
                    Can send data over the Internet 

### Graph API delegated permissions

The Outlook extension uses Microsoft Graph integration, which requires additional delegated permissions.

###### Important

These permissions are required for the Amazon Quick Outlook extension to provide its full range of capabilities. Without these permissions granted, the extension can only answer questions about the currently open email thread and draft a reply. It cannot summarize your inbox, manage your calendar, or perform inbox-wide operations such as searching, organizing, or triaging emails.

###### Note

The Amazon Quick Outlook extension does not send emails or create calendar appointments automatically. It uses Human-in-the-Loop (HITL) confirmation before any sending action, so users always review and approve outgoing messages and calendar changes.

Users are prompted
                    to sign in the first time they interact with the extension. Administrators can
                    pre-approve these permissions by granting tenant-wide admin consent (see
                    [Grant tenant-wide admin consent](#outlook-grant-admin-consent)).

The following table lists the delegated Graph API permissions used by the Outlook extension.

| Permission | Purpose | 
|---|---|
| `Calendars.Read.Shared` | Read events in user's and shared/delegate calendars for availability checks | 
| `Calendars.ReadWrite` | Create, update, and delete calendar events; accept/decline invites; check free/busy times | 
| `Contacts.ReadWrite` | Resolve recipients by name, look up contact details, and save new contacts | 
| `Files.Read` | Read user's OneDrive/SharePoint files to summarize or reference attachments | 
| `Mail.Read` | Read full email content, attachments, and threads for summarization and action items | 
| `Mail.ReadBasic` | Read email metadata (subject, sender, date) for efficient mailbox listing and search | 
| `Mail.ReadWrite` | Organize mail: move, delete, mark read/unread, create drafts, and manage attachments | 
| `MailboxSettings.ReadWrite` | Read and update timezone, working hours, out-of-office, inbox rules, and categories | 
| `offline_access` | Obtain refresh token for persistent sessions without repeated re-authentication | 
| `People.Read` | Suggest recipients and resolve names using collaboration and org signals | 
| `Tasks.ReadWrite` | Create, update, complete, and delete tasks and task lists across To Do/Planner | 
| `User.Read` | Identify the signed-in user's profile, email, job title, and timezone | 
| `User.ReadBasic.All` | Read basic profile info (name, email, photo) of other users in the org | 

### Grant tenant-wide admin consent

To enable the full capabilities of the Amazon Quick Outlook extension for all users in your organization, grant tenant-wide admin consent for the Microsoft Graph permissions listed above. This pre-approves the permissions so that individual users are not prompted to approve them when they first use the extension.

You can complete this process using either Microsoft Graph PowerShell or Microsoft Graph Explorer.

#### Prerequisites

Before granting admin consent, ensure you have a role that includes the following permissions:

- 
                            `Application.ReadWrite.All`
- 
                            `DelegatedPermissionGrant.ReadWrite.All`

#### Grant admin consent using PowerShell

Follow these steps to grant admin consent using Microsoft Graph PowerShell:

- 
                            Connect to Microsoft Graph with the required permissions: `Connect-MgGraph -Scopes "Application.ReadWrite.All","DelegatedPermissionGrant.ReadWrite.All"`
- 
                            Look up the Microsoft Graph service principal ID for your tenant and save the ID: `Get-MgServicePrincipal -Filter "displayName eq 'Microsoft Graph'"`
- 
                            Create a service principal for the Amazon Quick Outlook extension in your tenant and save the returned ID: `New-MgServicePrincipal -AppId "a5342f89-ebb1-4b1d-966c-34e8df972aaf"`
- 
                            Grant admin consent for all delegated permissions on behalf of all users in your tenant. Replace `ServicePrincipalId`with the ID from step 3 and`GraphServicePrincipalId`with the ID from step 2:`$params = @{ "ClientId" = "``ServicePrincipalId`" "ConsentType" = "AllPrincipals" "ResourceId" = "`GraphServicePrincipalId`" "Scope" = "Calendars.Read.Shared Calendars.ReadWrite Contacts.ReadWrite Files.Read Mail.Read Mail.ReadBasic Mail.ReadWrite MailboxSettings.ReadWrite offline_access People.Read Tasks.ReadWrite User.Read User.ReadBasic.All" } New-MgOauth2PermissionGrant -BodyParameter $params

#### Grant admin consent using Graph Explorer

Follow these steps to grant admin consent using Microsoft Graph Explorer:

- 
                            Sign in to Microsoft Graph Explorer with a role that has the `Application.ReadWrite.All`and`DelegatedPermissionGrant.ReadWrite.All`permissions.
- 
                            Look up the Microsoft Graph service principal ID for your tenant and save the ID from the response: `GET https://graph.microsoft.com/v1.0/servicePrincipals?$filter=displayName eq 'Microsoft Graph'&$select=id,displayName`
- 
                            Create a service principal for the Amazon Quick Outlook extension in your tenant and save the returned ID: `POST https://graph.microsoft.com/v1.0/servicePrincipals`Request body: `{ "appId": "a5342f89-ebb1-4b1d-966c-34e8df972aaf" }`
- 
                            Grant admin consent for all delegated permissions on behalf of all users in your tenant. Replace `ServicePrincipalId`with the ID from step 3 and`GraphServicePrincipalId`with the ID from step 2:`POST https://graph.microsoft.com/v1.0/oauth2PermissionGrants`Request body: `{ "clientId": "``ServicePrincipalId`", "consentType": "AllPrincipals", "resourceId": "`GraphServicePrincipalId`", "scope": "Calendars.Read.Shared Calendars.ReadWrite Contacts.ReadWrite Files.Read Mail.Read Mail.ReadBasic Mail.ReadWrite MailboxSettings.ReadWrite offline_access People.Read Tasks.ReadWrite User.Read User.ReadBasic.All" }

After granting admin consent, users in your organization will not be prompted to approve permissions individually when they first use the Amazon Quick Outlook extension. The extension will have immediate access to its full capabilities.

### Where to review permissions

To review permissions for the Outlook extension, go to
                    Microsoft Entra > **Enterprise Applications** >
                    find the app called "Amazon Quick Outlook Agent" >
                    **Permissions**.

## Deploying the Microsoft Outlook extension to your organization

            After completing the prerequisites and granting admin consent for Microsoft Graph permissions, follow these steps to deploy the extension to your users:

- 
                    Sign in to the M365 admin center. 
- 
                    Select **Settings**>**Integrated apps**in the left navigation menu.
- 
                    Choose **Get apps**.
- 
                    Search for "Amazon Quick". 
- 
                    Locate the tile for Amazon Quick in Outlook and choose **Get it now**.
- 
                    Confirm that you want to add the app. 
- 
                    Under **Assign users**, choose**Entire organization**or**Specific users/groups**depending on your needs.
- 
                    After selecting the users, review the app's requested permissions and capabilities and choose **Next**.
- 
                    Choose **Finish Deployment**.