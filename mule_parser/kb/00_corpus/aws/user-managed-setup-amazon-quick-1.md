# User-managed setup - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/onedrive-kb-user-managed.html](https://docs.aws.amazon.com/quick/latest/userguide/onedrive-kb-user-managed.html)

---

With user-managed setup, you sign in to OneDrive directly and Amazon Quick handles authentication through a managed OAuth flow. Amazon Quick uses a pre-registered multi-tenant application, so you don't need to create an app registration. Most users can complete setup in a few minutes.

## Prerequisites

        Before you begin, make sure you have the following:

- 
                A Microsoft 365 account with access to the OneDrive content you want to index. 
- 
                Access to Amazon Quick with permissions to create knowledge bases. 
- 
                A browser that allows popups from the Amazon Quick console domain. 

Your Microsoft administrator might need to grant organizational consent
            before users can create a OneDrive knowledge base. Administrators can grant
            organization-wide consent by signing in and choosing **Consent on
                behalf of your organization** during the integration creation
            flow. For more information, see
            [Admin consent for Microsoft 365](#onedrive-kb-user-admin-consent).

###### Important

User-managed setup does not support document-level access control
            (ACL). All indexed content is accessible to any user who has access to the
            knowledge base in Amazon Quick. Individual permissions in OneDrive are not
            enforced. Carefully review which content you include when creating a knowledge
            base. If you require document-level access control, use
            [Admin-managed setup (service credentials)](./onedrive-kb-admin-managed.html) instead.

## Create the OneDrive knowledge base

         
            ### Navigate to Knowledge

- 
                    In Amazon Quick, choose **Knowledge**from the left navigation panel.
- 
                    Under **Set up new knowledge base**, locate**Microsoft OneDrive**and choose the**+**icon.

### Sign in to OneDrive

The **Create OneDrive knowledge base** wizard opens
                on the Authentication method step. **Quick setup** is
                selected by default.

- 
                    Under **Quick setup**, choose**Sign in to OneDrive**.
- 
                    A Microsoft sign-in window opens. Enter your Microsoft 365 credentials. 
- 
                    If a permissions consent dialog appears, review the permissions and choose **Accept**.If you see an error instead of the consent dialog, your organization might restrict third-party app access. See [Admin consent for Microsoft 365](#onedrive-kb-user-admin-consent).
- 
                    After successful authentication, choose **Next**.

### Choose content

- 
                    Enter a **Name**and optional**Description**for your knowledge base.
- 
                    In the **Content**section, choose**Add content**.
- 
                    A dialog opens showing OneDrive files and folders accessible to your account. Select the files or folders you want to index. 
- 
                    Choose **Add**to confirm your selections. You can add more content or remove items before continuing.
- 
                    Choose **Create**.

### Initial sync

After you choose **Create**, you are returned to the
                knowledge base list page. The knowledge base might take a few minutes to
                finish provisioning. Once creation is complete, an initial sync is
                automatically triggered.

## Admin consent for Microsoft 365

        Most users complete setup without any extra steps. However, if your Microsoft 365 tenant restricts third-party app access, you might see an error when you sign in. In this case, a Microsoft 365 administrator needs to grant one-time consent for the Amazon Quick application. After consent is granted, any user in your organization can connect.

If you are not a Microsoft 365 administrator, share the following information with your administrator:

- 
                **What to do:**Grant admin consent for the Amazon Quick OneDrive integration application.
- 
                **Why:**Amazon Quick needs delegated read access to OneDrive files to index content for knowledge bases.

For detailed instructions on granting admin consent through the consent
            dialog or the Microsoft Entra admin center, see
            [Grant organization-wide admin consent](./sharepoint-kb-user-managed.html#entra-admin-consent).

### Permissions requested

The following delegated permissions are requested when a user signs in. Share this list with your administrator if they need to review the permissions before granting consent.

| Permission | API | Type | Description | 
|---|---|---|---|
| `Files.Read.All` | Microsoft Graph | Delegated | Read all files the signed-in user can access. | 
| `Notes.Read.All` | Microsoft Graph | Delegated | Read all OneNote notebooks the signed-in user can access. | 
| `User.Read` | Microsoft Graph | Delegated | Sign in and read the user's profile. | 
| `offline_access` | Microsoft Graph | Delegated | Maintain access using refresh tokens. | 

## Manage and troubleshoot user-managed connections

        To edit, share, or delete your integration, see [Managing existing integrations](./integration-workflows.html#managing-existing-integrations).

- 
                **App blocked by administrator**– Your Microsoft 365 tenant restricts third-party app access. Ask your Microsoft 365 administrator to grant admin consent. For more information, see[Admin consent for Microsoft 365](#onedrive-kb-user-admin-consent).
- 
                **Sign-in window closes without completing**– Verify that your browser allows popups from the Amazon Quick console domain and that third-party cookies are enabled.
- 
                **Token expired**– Delegated credentials last approximately 90 days. If syncs fail after this period, you need to re-authenticate. For more information, see[Token refresh with user-managed setup](./onedrive-kb-troubleshooting.html#onedrive-kb-troubleshooting-token-refresh).
- 
                **Missing content**– Verify that the account you used for authentication has access to the files and folders you selected. Content shared with you after the initial sync requires a resync to be indexed.

For additional troubleshooting, including sync monitoring and reports, see
            [Troubleshooting OneDrive knowledge bases](./onedrive-kb-troubleshooting.html).

## Known limitations

        - 
                Document-level access control (ACL) is not supported with user-managed setup. If you require document-level access control, use [Admin-managed setup (service credentials)](./onedrive-kb-admin-managed.html).
- 
                File comments synchronization is not supported. 

## Next steps

        After your knowledge base is created and the initial sync completes, you
            can use it in Amazon Quick to answer questions from your OneDrive content.
            To manage your knowledge base, see
            [Managing existing integrations](./integration-workflows.html#managing-existing-integrations).