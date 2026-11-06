# Admin-managed setup (service credentials) - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/sharepoint-kb-admin-managed.html](https://docs.aws.amazon.com/quick/latest/userguide/sharepoint-kb-admin-managed.html)

---

With admin-managed setup, an administrator configures an AWS KMS signing key and a Microsoft Entra ID app registration with certificate-based credentials. Individual users don't need to authorize through sign-in.

Admin-managed setup optionally includes document-level access control list (ACL)
        support. When enabled, Amazon Quick syncs ACLs from SharePoint and verifies each
        user's permissions at query time. For more information, see
        [Document-level access controls](./sharepoint-kb-acl.html).

## Prerequisites

        Before you begin, make sure that you have the following:

- 
                Administrator access to the Amazon Quick admin console. 
- 
                Administrator access to Microsoft Entra ID to register an application and grant API permissions. 
- 
                A SharePoint Online site with content to index. 

## Setup overview

        The setup involves the following phases:

- 
                **Set up service credentials**– Create a KMS signing key, generate a certificate, register an application in Entra, and grant Amazon Quick permission to use the key. For more information, see[Set up service credentials](./sharepoint-kb-admin-config.html).
- 
                **Create the knowledge base in Amazon Quick**– Create a SharePoint knowledge base using the service credentials from Phase 1. For more information, see[Create the knowledge base in Amazon Quick](./sharepoint-kb-admin-connection.html).

Document-level access control is optionally available for all admin-managed
            knowledge bases. For more information about how access controls work, see
            [Document-level access controls](./sharepoint-kb-acl.html).

## Manage and troubleshoot admin-managed connections

        To edit, share, or delete your integration, see [Managing existing integrations](./integration-workflows.html#managing-existing-integrations).

- 
                **Unable to access KMS key**– Verify the KMS key ARN and Region. Confirm the KMS key has been added in the Amazon Quick admin console under**Manage account**,**AWS resources**,**AWS Key Management Service**. Confirm the key is enabled and has not been scheduled for deletion. Multi-Region keys are not currently supported.
- 
                **Certificate validation failed**– Verify the thumbprint using the base64url-encoded SHA-1 value from the certificate generation step. Ensure the certificate uploaded to Entra has not expired.
- 
                **ACL not enforced**– Confirm the Entra app has`User.Read.All`and`GroupMember.Read.All`on Microsoft Graph. For the SharePoint resource, confirm the app has`Sites.FullControl.All`. If using`Sites.Selected`, confirm that per-site permissions have been granted for each site in the knowledge base. Re-run a full sync after fixing permissions. For more information about verifying document access, see[Check document access (ACL verification)](./sync-reports-observability.html#sync-reports-acl-verification).
- 
                **Zero items crawled**– The sync completed but no documents were indexed. This typically indicates a permissions issue. Verify the Entra app has the correct API permissions for your permission scope. If using`Sites.Selected`, confirm that per-site permissions have been granted for each site included in the knowledge base (see[Step 3b: Grant site-level permissions (Sites.Selected only)](./sharepoint-kb-admin-config.html#sharepoint-kb-admin-sites-selected)). Also verify that the SharePoint sites contain content and are accessible.
- 
                **New site not crawled (Sites.Selected)**– If you added a new site URL to the knowledge base but no content from that site is indexed, the Microsoft Graph API permission grant might be missing. Verify that you ran the grant for the new site. Each site requires a separate grant when using`Sites.Selected`. For more information, see[Grant site-level permissions](./sharepoint-kb-admin-config.html#sharepoint-kb-admin-sites-selected-grant).
- 
                **Specific paths returning no results**– Verify that you used the SharePoint path, not the browser URL. To get the correct path, navigate to the item in SharePoint, choose the**More options**menu (⋮), select**Details**, then scroll to**Path**and choose**Copy**. Also verify the path still exists and has not been renamed or moved in SharePoint.
- 
                **Syncs failing after certificate expiry**– If syncs fail across multiple knowledge bases that share the same data source connection, the certificate uploaded to Entra might have expired. Generate a new certificate (see[Step 2: Generate a self-signed certificate](./sharepoint-kb-admin-config.html#sharepoint-kb-admin-step2-certificate)), upload it to the Entra app registration, and update the connection details. A Amazon Quick administrator can reassign data source ownership through**Manage assets**if the original creator is unavailable. For more information, see[Sharing data source connections](./sharing-kb-datasources.html#sharing-datasources).
- 
                **No results from ACL-enabled knowledge base**– If users receive no results from a knowledge base with ACL management enabled, admin consent for the real-time ACL application might not have been granted. Your tenant might also block user consent. Grant admin consent using the link provided in the Amazon Quick console when ACL management is enabled, or see[Admin consent](./sharepoint-kb-acl.html#sharepoint-kb-acl-admin-consent).
- 
                **Documents skipped with "File has no ACL" error**– If sync reports show items with status SKIPPED and error type VALIDATION_ERROR with the message "File has no ACL while crawlACL is true, skipping ingestion," the Entra app registration is missing the required ACL permissions. Verify the app has the correct permissions for your setup. For the required permissions, see[Permissions](./sharepoint-kb-admin-config.html#sharepoint-kb-admin-config-permissions).

For additional troubleshooting, including sync monitoring, reports, and ACL
            verification, see
            [Troubleshooting SharePoint knowledge bases](./sharepoint-kb-troubleshooting.html).