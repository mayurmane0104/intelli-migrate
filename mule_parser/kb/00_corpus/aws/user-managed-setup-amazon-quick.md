# User-managed setup - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/google-drive-kb-user-managed.html](https://docs.aws.amazon.com/quick/latest/userguide/google-drive-kb-user-managed.html)

---

With user-managed setup, you sign in to Google Drive directly to authorize the connection. Amazon Quick handles authentication through a managed OAuth flow. No Google Cloud project, service account, or domain-wide delegation is required.

## Prerequisites

        Before you set up a user-managed Google Drive knowledge base, verify the following:

- 
                You have a Google account with access to Google Drive. 
- 
                Your Google Workspace administrator allows third-party app access, or can allow the Amazon Quick app on your behalf. 
- 
                Your browser allows popups from the Amazon Quick console domain. 

###### Note

If your organization restricts third-party app access in Google Workspace, your Google Workspace administrator might need to allow the Amazon Quick app before users can sign in. Contact your Google Workspace administrator if you encounter an error during sign-in.

###### Note

User-managed setup does not support document-level access control (ACL). ACL is a mechanism that controls which users can access specific documents. If
                you need document-level access control, use
                [Admin-managed Google Drive knowledge base setup](./google-drive-kb-admin-managed.html) instead.

## Permissions granted during consent

        When you authorize the connection, Amazon Quick requests the following permissions from your Google account:

- See and download all your Google Drive files
- 
                    - 
                            Allows Amazon Quick to see your Google Drive files 
- 
                            Allows Amazon Quick to download your files 
- 
                            Allows Amazon Quick to see the names and email addresses of people you share files with 
 
- 
                            
- See information about your Google Drive files
- 
                    - 
                            Allows Amazon Quick to see the titles and descriptions of your files 
- 
                            Allows Amazon Quick to see the names and email addresses of people you share files with 
- 
                            Allows Amazon Quick to see your folders and how files are organized 
 
- 
                            

###### Note

You can review and remove this access at any time from your Google Account permissions settings.

## Set up a Google Drive knowledge base

        To create a user-managed Google Drive knowledge base, complete the following steps in the Amazon Quick console.

- 
                In the Amazon Quick console, choose **Knowledge**.
- 
                Find **Google Drive**and choose the**Add**(+) icon.
- 
                In the **Create Google Drive knowledge base**dialog, under**Authentication method**, choose**Sign in to Google Drive**and complete the Google sign-in and consent flow.
- 
                Under **Create knowledge base**, enter a name and an optional description for your knowledge base.
- 
                In the **Content**section, choose**Add content**and select the Google Drive files and folders that you want to index. You can browse content from your personal drive, files shared with you, and shared drives in your organization.
- 
                Choose **Create**.

After you choose **Create**, the data sync starts
            automatically.

## Access controls

        ###### Important

When Amazon Quick indexes Google Drive content through user-managed setup, it does not sync access control lists (ACLs) from Google Drive. All indexed content is accessible to any user who has access to the knowledge base in Amazon Quick, regardless of their permissions in Google Drive. Carefully review which content you include when you create a knowledge base.

If you require document-level access control, use the
            [Admin-managed Google Drive knowledge base setup](./google-drive-kb-admin-managed.html) instead.

## Manage and troubleshoot your integration

        For instructions on editing, sharing, or deleting your integration, see [Managing existing integrations](./integration-workflows.html#managing-existing-integrations).

For more information about knowledge base troubleshooting, including sync issues and
            missing documents, see [Troubleshooting knowledge bases](./troubleshooting-knowledge-bases.html).

### Google Drive-specific issues

- 
                    **App blocked by administrator**– If your Google Workspace administrator restricts third-party app access, you might see an error when you attempt to sign in. Contact your Google Workspace administrator to allow the Amazon Quick app.
- 
                    **Authentication popup fails**– Verify that your browser allows popups from the Amazon Quick console domain. Try using a different browser or clearing your browser cache.
- 
                    **Permissions revoked**– If you previously revoked Amazon Quick access from your Google Account permissions settings, you need to re-authenticate by editing the integration and signing in again.
- 
                    **Missing content**– Verify that the Google account that you used for authentication has access to the files and folders that you selected. Content that was shared with you after the initial sync requires a resync to be indexed.
- 
                    **Google API rate limiting**– Google Drive might limit requests during high usage periods. If syncs fail or are incomplete, retry during off-peak hours.

## Known limitations

        - 
                Document-level access control (ACL) is not supported with user-managed setup. If you require document-level access control, use [Admin-managed Google Drive knowledge base setup](./google-drive-kb-admin-managed.html).
- 
                Synchronization of file comments is not supported.