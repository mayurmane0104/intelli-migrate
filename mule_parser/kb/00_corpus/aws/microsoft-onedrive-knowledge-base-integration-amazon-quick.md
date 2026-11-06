# Microsoft OneDrive knowledge base integration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/onedrive-knowledge-base.html](https://docs.aws.amazon.com/quick/latest/userguide/onedrive-knowledge-base.html)

---

Microsoft OneDrive is a cloud storage service for storing, sharing, and collaborating on files across your organization. With the Amazon Quick OneDrive connector, you can create knowledge bases from your OneDrive content to power AI-driven search and Q&A.

Amazon Quick supports two authentication methods for connecting to OneDrive:

- 
            **User-managed setup**– You sign in to OneDrive directly to authorize the connection. This is the simplest way to get started. For more information, see[User-managed setup](./onedrive-kb-user-managed.html).
- 
            **Admin-managed setup (service credentials)**– An Entra ID app registration authenticates on behalf of the application using certificate-based credentials, and Amazon Quick crawls the OneDrive content of every user in your organization. Admin-managed setup includes built-in document-level access control (ACL). Amazon Quick automatically syncs access control lists from OneDrive and verifies each user's permissions at query time. Users see answers only from documents that they are authorized to access. For more information, see[Admin-managed setup (service credentials)](./onedrive-kb-admin-managed.html).

After connecting, Amazon Quick indexes your OneDrive files and folders into a knowledge base. Your Amazon Quick agents can then search this content and generate answers grounded in your OneDrive data.

## Prerequisites

        Before you set up the OneDrive knowledge base integration, make sure that you have the following:

- 
                An AWS account with an active Amazon Quick instance. 
- 
                A Microsoft 365 account with OneDrive access. 
- 
                For subscription requirements, see [Set up integrations in the console](./integration-console-setup-process.html).

For admin-managed setup, additional prerequisites apply. For more
            information, see [Admin-managed setup (service credentials)](./onedrive-kb-admin-managed.html).

## Supported content types

        The OneDrive connector supports the common file types that Amazon Quick knowledge bases support, including the following:

- 
                **Microsoft Office documents:**Word, Excel, PowerPoint
- 
                **PDF files**
- 
                **Text files and rich text documents**
- 
                **Text documents with embedded images**
- 
                **Audio and video files**

For more information about supported file types, size limits, and content
            processing options, see [Common configuration settings](./knowledge-base-integrations.html#common-configuration-settings).