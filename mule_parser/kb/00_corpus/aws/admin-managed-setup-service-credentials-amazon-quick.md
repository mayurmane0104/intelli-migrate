# Admin-managed setup (service credentials) - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/onedrive-kb-admin-managed.html](https://docs.aws.amazon.com/quick/latest/userguide/onedrive-kb-admin-managed.html)

---

With admin-managed setup, an administrator configures an AWS KMS signing key and a Microsoft Entra ID app registration with certificate-based credentials. Individual users don't need to authorize through sign-in. Amazon Quick crawls the OneDrive content of every user in your organization.

Admin-managed setup includes built-in document-level access control list (ACL)
        support. Because admin-managed setup crawls the OneDrive content of all users, ACL
        is always enabled and cannot be turned off. Amazon Quick syncs ACLs from OneDrive
        during each crawl and verifies each user's permissions at query time, so users see
        answers only from documents that they are authorized to access. For more
        information, see [Document-level access controls](./onedrive-kb-acl.html).

## Prerequisites

        Before you begin, make sure that you have the following:

- 
                Administrator access to the Amazon Quick admin console. 
- 
                Administrator access to Microsoft Entra ID to register an application and grant API permissions. 
- 
                A Microsoft 365 tenant with OneDrive content to index. 

## Setup overview

        The setup involves the following phases:

- 
                **Set up service credentials**– Create a KMS signing key, generate a certificate, register an application in Entra, and grant Amazon Quick permission to use the key. For more information, see[Set up service credentials](./onedrive-kb-admin-config.html).
- 
                **Create the knowledge base in Amazon Quick**– Create a OneDrive knowledge base using the service credentials from Phase 1. For more information, see[Create the knowledge base in Amazon Quick](./onedrive-kb-admin-connection.html).

Document-level access control is automatically enabled for all admin-managed
            knowledge bases. For more information about how access controls work, see
            [Document-level access controls](./onedrive-kb-acl.html).

## Known limitations

        - 
                OneNote files are not crawled in admin-managed setup. Microsoft retired app-only tokens for the OneNote APIs on March 31, 2025. To index OneNote content, use [User-managed setup](./onedrive-kb-user-managed.html).
- 
                Shared folders are not crawled. Folders shared with a user are stored in SharePoint and cannot be accessed with the application credentials used for admin-managed setup. To sync shared content, we recommend creating a [Microsoft SharePoint knowledge base integration](./sharepoint-knowledge-base.html).

## Manage and troubleshoot admin-managed connections

        To edit, share, or delete your integration, see [Managing existing integrations](./integration-workflows.html#managing-existing-integrations).

- 
                **Unable to access KMS key**– Verify the KMS key ARN and Region. Confirm the KMS key has been added in the Amazon Quick admin console under**Manage account**,**AWS resources**,**AWS Key Management Service**. Confirm the key is enabled and has not been scheduled for deletion. Multi-Region keys are not currently supported.
- 
                **Certificate validation failed**– Verify the thumbprint using the base64url-encoded SHA-1 value from the certificate generation step. Ensure the certificate uploaded to Entra has not expired.
- 
                **ACL not enforced**– Confirm the Entra app has`Files.Read.All`,`Sites.Read.All`,`User.Read.All`,`Group.Read.All`, and`GroupMember.Read.All`on Microsoft Graph. Re-run a full sync after fixing permissions. For more information about verifying document access, see[Check document access (ACL verification)](./sync-reports-observability.html#sync-reports-acl-verification).
- 
                **Zero items crawled**– The sync completed but no documents were indexed. This typically indicates a permissions issue. Verify the Entra app has the correct API permissions, including`Sites.Read.All`so that Amazon Quick can enumerate the OneDrive drives hosted on SharePoint. Also verify that users have OneDrive content and that admin consent has been granted.
- 
                **Syncs failing after certificate expiry**– If syncs fail across multiple knowledge bases that share the same data source connection, the certificate uploaded to Entra might have expired. Generate a new certificate (see[Step 2: Generate a self-signed certificate](./onedrive-kb-admin-config.html#onedrive-kb-admin-step2-certificate)), upload it to the Entra app registration, and update the connection details. An Amazon Quick administrator can reassign data source ownership through**Manage assets**if the original creator is unavailable. For more information, see[Sharing data source connections](./sharing-kb-datasources.html#sharing-datasources).
- 
                **No results from ACL-enabled knowledge base**– If users receive no results from an admin-managed knowledge base, admin consent for the real-time ACL application might not have been granted. Your tenant might also block user consent. Grant admin consent using the link provided in the Amazon Quick console, or see[Admin consent](./onedrive-kb-acl.html#onedrive-kb-acl-admin-consent).

For additional troubleshooting, including sync monitoring, reports, and ACL
            verification, see
            [Troubleshooting OneDrive knowledge bases](./onedrive-kb-troubleshooting.html).