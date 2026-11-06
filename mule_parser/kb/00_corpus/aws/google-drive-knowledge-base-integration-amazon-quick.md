# Google Drive knowledge base integration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/google-drive-knowledge-base.html](https://docs.aws.amazon.com/quick/latest/userguide/google-drive-knowledge-base.html)

---

With the Google Drive knowledge base integration, you can index your Google Drive content. Your Amazon Quick agents can then search this content and answer questions about it.

Amazon Quick supports two authentication methods for connecting to Google Drive:

- 
            **User-managed setup**– You sign in to Google Drive directly to authorize the connection. This is the simplest way to get started. For more information, see[User-managed setup](./google-drive-kb-user-managed.html).
- 
            **Admin-managed setup (service credentials)**– A Google Workspace administrator creates a service account with domain-wide delegation to authorize the connection. A key benefit of admin-managed setup is built-in document-level access control (ACL). Amazon Quick automatically syncs access control lists from Google Drive. It verifies each user's permissions at query time, so users see answers only from documents that they are authorized to access. For more information, see[Admin-managed Google Drive knowledge base setup](./google-drive-kb-admin-managed.html).

After you connect, Amazon Quick indexes your Google Drive files and folders into a knowledge base. Your Amazon Quick agents can then search this content and generate answers that are grounded in your Google Drive data.

## Prerequisites

        Before you set up the Google Drive knowledge base integration, make sure that you have the following:

- 
                A Google account with Google Drive access. 
- 
                For subscription requirements, see [Set up integrations in the console](./integration-console-setup-process.html).

For admin-managed setup, additional prerequisites apply. For more
            information, see [Admin-managed Google Drive knowledge base setup](./google-drive-kb-admin-managed.html).

## Supported content types

        The Google Drive connector supports all of the common file types that Amazon Quick knowledge bases support. These include PDF, Word, Excel, PowerPoint, and text files. The connector also supports the following Google Workspace-specific formats:

- 
                Google Docs 
- 
                Google Sheets 
- 
                Google Slides 

For more information about supported file types, size limits, and content
            processing options, see [Common configuration settings](./knowledge-base-integrations.html#common-configuration-settings).