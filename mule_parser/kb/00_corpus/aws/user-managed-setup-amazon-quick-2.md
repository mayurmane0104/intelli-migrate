# User-managed setup - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/sharepoint-kb-user-managed.html](https://docs.aws.amazon.com/quick/latest/userguide/sharepoint-kb-user-managed.html)

---

With user-managed setup, you sign in to SharePoint directly and Amazon Quick handles authentication. Most users can complete setup in a few minutes.

## Prerequisites

        Before you begin, make sure you have the following:

- 
                A Microsoft 365 account with access to the SharePoint sites you want to index. 
- 
                Access to Amazon Quick with permissions to create knowledge bases. 
- 
                A browser that allows popups from the Amazon Quick console domain. 

###### Important

User-managed setup does not support document-level access control
            (ACL). All indexed content is accessible to any user who has access to the
            knowledge base in Amazon Quick. Individual permissions in
            SharePoint are not enforced. Carefully review which content you include when creating a knowledge
            base. If you require document-level access control, use
            [Admin-managed setup (service credentials)](./sharepoint-kb-admin-managed.html) instead.

## Create the SharePoint knowledge base

         
            ### Navigate to Knowledge

- 
                    In Amazon Quick, choose **Knowledge**from the left navigation panel.
- 
                    Under **Set up new knowledge base**, locate**Microsoft SharePoint Online**and choose the**+**icon.

### Sign in to SharePoint

The **Create SharePoint knowledge base** wizard opens
                on the Authentication method step. **Quick setup** is
                selected by default.

- 
                    Under **Quick setup**, choose**Sign in to SharePoint**.
- 
                    A Microsoft sign-in window opens. Enter your Microsoft 365 credentials. 
- 
                    If a permissions consent dialog appears, review the permissions and choose **Accept**.If you see an error instead of the consent dialog, your organization might restrict third-party app access. See [Admin consent for Microsoft 365](#sharepoint-kb-user-admin-consent).
- 
                    After successful authentication, choose **Next**.

### Choose content

- 
                    Enter a **Name**and optional**Description**for your knowledge base.
- 
                    In the **Content**section, choose**Add content**.
- 
                    A dialog opens showing SharePoint sites and content accessible to your account. Select the pages, lists, files, or folders you want to index. 
- 
                    Choose **Add**to confirm your selections. You can add more content or remove items before continuing.
- 
                    Choose **Create**.

###### Tip

If the site you are looking for does not appear in the dialog,
                    choose the search link at the top of the Content section. Enter the
                    full URL of the SharePoint site (for example,
                    `https://contoso.sharepoint.com/sites/marketing`) and
                    choose **Browse**. The dialog then displays the
                    document libraries, lists, pages, folders, and files within that
                    site. Selecting a folder includes all files and subfolders within
                    it.

### Initial sync

After you choose **Create**, you are returned to the
                knowledge base list page. The knowledge base might take a few minutes to
                finish provisioning. Once creation is complete, an initial sync is
                automatically triggered.

## Admin consent for Microsoft 365

        Most users complete setup without any extra steps. However, if your Microsoft 365 tenant restricts third-party app access, you might see an error when you sign in. In this case, a Microsoft 365 administrator needs to grant one-time consent for the Amazon Quick application. After consent is granted, any user in your organization can connect.

If you are not a Microsoft 365 administrator, share the following information with your administrator:

- 
                **What to do:**Grant admin consent for the Amazon Quick SharePoint integration application.
- 
                **Why:**Amazon Quick needs delegated read access to SharePoint sites and files to index content for knowledge bases.

### Grant organization-wide admin consent

Some Amazon Quick features require delegated permissions from Microsoft Entra. By default, each user sees a Microsoft consent dialog the first time they use the feature. A Microsoft 365 administrator can pre-consent on behalf of the entire organization so that individual users aren't prompted. This is a one-time action per application.

###### Note

If your Microsoft 365 tenant is configured to restrict user consent for third-party applications, admin consent is required, not optional. Without it, users see an error when they attempt to use the feature.

The following table describes the user experience with and without admin consent.

| Scenario | User experience | 
|---|---|
| Admin consent not granted | Each user sees the Microsoft permissions consent dialog on first use. Users might be blocked if your tenant restricts user consent for third-party apps. | 
| Admin consent granted | Users aren't prompted for consent. The feature works immediately for all users in the organization. | 

#### Granting consent through the consent dialog

The simplest way to grant admin consent is through the Microsoft consent dialog that appears during the feature flow.

###### To grant consent through the consent dialog

- 
                Have a Global Administrator or Privileged Role Administrator initiate the feature flow that triggers the consent dialog. 
- 
                In the Microsoft sign-in dialog, select the **Consent on behalf of your organization**check box.
- 
                Choose **Accept**.

This grants consent for the requested delegated permissions for all users in your Microsoft 365 tenant.

#### Granting consent through the Microsoft Entra admin center

Administrators can also grant consent directly from the Microsoft Entra admin center.

###### To grant consent through the Microsoft Entra admin center

- 
                Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/).
- 
                In the left navigation pane, expand **Entra ID**and choose**Enterprise applications**.
- 
                Locate the enterprise application for the Amazon Quick feature. ###### NoteThe application name appears in the consent dialog that users see when they first use the feature. 
- 
                In the left navigation pane, choose **Permissions**.
- 
                Choose **Grant admin consent for**.`Your Organization`
- 
                Confirm the consent. 

#### Verifying consent

After you grant consent, the Enterprise application's
            **Permissions** page shows all delegated permissions
            with a status indicator under the **Admin consent**
            column.

###### Note

When an administrator grants organizational consent, Microsoft Entra
                automatically creates an Enterprise Application (service principal) in
                your tenant. To revoke access, disable or delete this service principal
                from **Enterprise applications** in the Microsoft
                Entra admin center.

#### Checking tenant consent settings

To check whether your tenant restricts user consent, complete the following steps.

###### To check tenant consent settings

- 
                In the Microsoft Entra admin center, choose **Entra ID**,**Enterprise applications**,**Consent and permissions**,**User consent settings**.
- 
                If the setting is **Do not allow user consent**, an administrator must grant consent before users can use the feature.

### Permissions requested

The following delegated permissions are requested when a user signs in. Share this list with your administrator if they need to review the permissions before granting consent.

| Permission | API | Type | Description | 
|---|---|---|---|
| `Files.Read.All` | Microsoft Graph | Delegated | Read all files the signed-in user can access. | 
| `Notes.Read.All` | Microsoft Graph | Delegated | Read all OneNote notebooks the signed-in user can access. | 
| `User.Read` | Microsoft Graph | Delegated | Sign in and read the user's profile. | 
| `Sites.Read.All` | Microsoft Graph | Delegated | Read documents and list items in all site collections. | 
| `offline_access` | Microsoft Graph | Delegated | Maintain access using refresh tokens. | 
| `AllSites.Read` | Office 365 SharePoint Online | Delegated | Read items in all site collections. | 

## Manage and troubleshoot user-managed connections

        To edit, share, or delete your integration, see [Managing existing integrations](./integration-workflows.html#managing-existing-integrations).

- 
                **App blocked by administrator**– Your Microsoft 365 tenant restricts third-party app access. Ask your Microsoft 365 administrator to grant admin consent. For more information, see[Admin consent for Microsoft 365](#sharepoint-kb-user-admin-consent).
- 
                **Sign-in window closes without completing**– Verify that your browser allows popups from the Amazon Quick console domain and that third-party cookies are enabled.
- 
                **Token expired**– Delegated credentials last approximately 90 days. If syncs fail after this period, you need to re-authenticate. For more information, see[Token refresh with user-managed setup](./sharepoint-kb-troubleshooting.html#sharepoint-kb-troubleshooting-token-refresh).
- 
                **Missing content**– Verify that the account you used for authentication has access to the files and folders you selected. Content shared with you after the initial sync requires a resync to be indexed.

For additional troubleshooting, including sync monitoring and reports, see
            [Troubleshooting SharePoint knowledge bases](./sharepoint-kb-troubleshooting.html).

## Next steps

        After your knowledge base is created and the initial sync completes, you
            can use it in Amazon Quick to answer questions from your SharePoint content.
            To manage your knowledge base, see
            [Managing existing integrations](./integration-workflows.html#managing-existing-integrations).