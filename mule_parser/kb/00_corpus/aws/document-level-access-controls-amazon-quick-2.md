# Document-level access controls - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/onedrive-kb-acl.html](https://docs.aws.amazon.com/quick/latest/userguide/onedrive-kb-acl.html)

---

Admin-managed OneDrive knowledge bases include built-in document-level access control. Because admin-managed setup crawls the OneDrive content of every user in your organization, ACL is always enabled and cannot be turned off. Amazon Quick syncs access control lists (ACLs) from OneDrive during each crawl. The system verifies each user's permissions at query time, so users only see answers from documents they are authorized to access in OneDrive.

## How it works

        When a user queries an Amazon Quick agent that uses an admin-managed OneDrive knowledge base, the system enforces access controls in two stages:

- 
                **Pre-retrieval filtering**– Amazon Quick performs a semantic search against the vector index to find the most relevant document passages. The system applies access control lists that were synced from OneDrive during the last crawl. This produces a preliminary set of candidate documents.
- 
                **Real-time verification**– The system verifies the candidate documents in real time by checking the querying user's current access in OneDrive. Only documents the user is currently authorized to access are included in the response.

This two-stage approach provides document-level access control that stays current even when OneDrive permissions change between syncs.

## ACL management

        Document-level access control is automatically enabled for all admin-managed OneDrive knowledge bases. No additional configuration is required, and the setting cannot be turned off.

For ACL enforcement to work, your Entra app registration must have the following Microsoft Graph application permissions:

- 
                `User.Read.All`,`Group.Read.All`, and`GroupMember.Read.All`to resolve user and group membership.
- 
                `Sites.Read.All`to enumerate and read the OneDrive drives, which are hosted on SharePoint.

For more information about ACL best practices, see
            [Best practices for managing ACLs in knowledge bases](./acl-best-practices-kb.html).

## Real-time access verification

        The real-time verification stage uses a delegated OAuth flow managed automatically by Amazon Quick. Quick creates and manages a separate Microsoft Entra application specifically for this purpose. No customer configuration is required for this app. It is distinct from both the admin-managed app registration you created during setup and any user-managed OAuth app.

- 
                A user asks a question in the Quick chat assistant. 
- 
                If the answer involves OneDrive content from an admin-managed knowledge base, Quick prompts the user to **Sign in to OneDrive**.
- 
                The user signs in and accepts the Microsoft consent dialog (if admin consent has not been granted). 
- 
                Quick uses the user's delegated token to verify access to each candidate document in real time. 
- 
                Only documents the user currently has access to in OneDrive are included in the response. 

The sign-in is a one-time step. The delegated credentials use a refresh token and last approximately 90 days.

### Delegated permissions

The real-time ACL app requests the following delegated permissions:

| Permission | Scope | Purpose | 
|---|---|---|
| Read items in all site collections | `Sites.Read.All` | Verify user access to OneDrive content hosted on SharePoint. | 
| Have full access to your files | `Files.ReadWrite.All` | Verify user access to specific files. | 
| View your basic profile | `User.Read` | Identify the signed-in user. | 
| Maintain access to data you have given it access to | `offline_access` | Refresh tokens so users don't need to re-authenticate frequently. | 

### Admin consent

The real-time ACL check uses a separate Microsoft Entra application from the one used in user-managed setup or the admin-managed app registration. If your organization requires admin consent, an administrator must grant consent for each application independently.

When you create an admin-managed knowledge base, the Amazon Quick console provides a direct link to grant admin consent. This link is for the real-time ACL application. If you are a Microsoft 365 administrator, you can grant consent directly from the console. Otherwise, share the link with your administrator.

If admin consent is not granted, each user sees the consent dialog on their first query that involves OneDrive content. After accepting, they are not prompted again for approximately 90 days.

For detailed instructions on granting admin consent through the
                consent dialog or the Microsoft Entra admin center, see
                [Grant organization-wide admin consent](./sharepoint-kb-user-managed.html#entra-admin-consent).

## Next steps

        For more information about ACL best practices, see
            [Best practices for managing ACLs in knowledge bases](./acl-best-practices-kb.html). For information about
            creating admin-managed OneDrive knowledge bases, see
            [Admin-managed setup (service credentials)](./onedrive-kb-admin-managed.html).