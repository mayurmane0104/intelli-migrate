# Document-level access controls - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/sharepoint-kb-acl.html](https://docs.aws.amazon.com/quick/latest/userguide/sharepoint-kb-acl.html)

---

Admin-managed SharePoint knowledge bases optionally support document-level access control. When enabled, Amazon Quick syncs access control lists (ACLs) from SharePoint during each crawl. The system verifies each user's permissions at query time, so users only see answers from documents they are authorized to access in SharePoint.

## How it works

        When a user queries an Amazon Quick agent that uses an admin-managed SharePoint knowledge base with ACL management enabled, the system enforces access controls in two stages:

- 
                **Pre-retrieval filtering**– Amazon Quick performs a semantic search against the vector index to find the most relevant document passages. The system applies access control lists that were synced from SharePoint during the last crawl. This produces a preliminary set of candidate documents.
- 
                **Real-time verification**– The system verifies the candidate documents in real time by checking the querying user's current access in SharePoint. Only documents the user is currently authorized to access are included in the response.

This two-stage approach provides document-level access control that stays current even when SharePoint permissions change between syncs.

## Enable ACL management

        ACL management is configured during knowledge base creation in the
            **Additional settings** step. Select the
            **Control document access with ACLs** checkbox to
            enable it.

###### Important

ACL management cannot be changed after the knowledge base is created. If you need to change this setting, you must create a new knowledge base.

To enable ACL management, your Entra app registration must have the following permissions:

- 
                `User.Read.All`and`GroupMember.Read.All`on Microsoft Graph.
- 
                `Sites.FullControl.All`on the SharePoint resource, or`Sites.Selected`with per-site permissions granted.

For more information about ACL best practices, see
            [Best practices for managing ACLs in knowledge bases](./acl-best-practices-kb.html).

## Real-time access verification

        The real-time verification stage uses a delegated OAuth flow managed automatically by Amazon Quick. Quick creates and manages a separate Microsoft Entra application specifically for this purpose. No customer configuration is required for this app. It is distinct from both the admin-managed app registration you created during setup and any user-managed OAuth app.

- 
                A user asks a question in the Quick chat assistant. 
- 
                If the answer involves SharePoint content from an ACL-enabled knowledge base, Quick prompts the user to **Sign in to SharePoint**.
- 
                The user signs in and accepts the Microsoft consent dialog (if admin consent has not been granted). 
- 
                Quick uses the user's delegated token to verify access to each candidate document in real time. 
- 
                Only documents the user currently has access to in SharePoint are included in the response. 

The sign-in is a one-time step. The delegated credentials use a refresh token and last approximately 90 days.

### Delegated permissions

The real-time ACL app requests the following delegated permissions:

| Permission | Scope | Purpose | 
|---|---|---|
| Read items in all site collections | `Sites.Read.All` | Verify user access to SharePoint site content. | 
| Read your files | `Files.Read.All` | Verify user access to specific files. | 
| View your basic profile | `User.Read` | Identify the signed-in user. | 
| Maintain access to data you have given it access to | `offline_access` | Refresh tokens so users don't need to re-authenticate frequently. | 

### Admin consent

The real-time ACL check uses a separate Microsoft Entra application from the one used in user-managed setup or the admin-managed app registration. If your organization requires admin consent, an administrator must grant consent for each application independently.

When you enable ACL management during knowledge base creation, the Amazon Quick console provides a direct link to grant admin consent. This link is for the real-time ACL application. If you are a Microsoft 365 administrator, you can grant consent directly from the console. Otherwise, share the link with your administrator.

If admin consent is not granted, each user sees the consent dialog on their first query that involves SharePoint content. After accepting, they are not prompted again for approximately 90 days.

For detailed instructions on granting admin consent through the
                consent dialog or the Microsoft Entra admin center, see
                [Grant organization-wide admin consent](./sharepoint-kb-user-managed.html#entra-admin-consent).

## Next steps

        For more information about ACL best practices, see
            [Best practices for managing ACLs in knowledge bases](./acl-best-practices-kb.html). For information about
            creating admin-managed SharePoint knowledge bases, see
            [Admin-managed setup (service credentials)](./sharepoint-kb-admin-managed.html).