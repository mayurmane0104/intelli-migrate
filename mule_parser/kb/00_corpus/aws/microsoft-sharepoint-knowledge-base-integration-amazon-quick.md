# Microsoft SharePoint knowledge base integration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/sharepoint-knowledge-base.html](https://docs.aws.amazon.com/quick/latest/userguide/sharepoint-knowledge-base.html)

---

Microsoft SharePoint Online is a collaborative platform for building websites, managing document libraries, and organizing content across your organization. With the Amazon Quick SharePoint connector, you can create knowledge bases from your SharePoint content to power AI-driven search and Q&A.

Amazon Quick supports two authentication methods for connecting to SharePoint Online:

- 
            **User-managed setup**– You sign in to SharePoint directly to authorize the connection. This is the simplest way to get started. For more information, see[User-managed setup](./sharepoint-kb-user-managed.html).
- 
            **Admin-managed setup (service credentials)**– An Entra ID app registration authenticates on behalf of the application using certificate-based credentials. A key benefit of admin-managed setup is built-in document-level access control (ACL). Amazon Quick automatically syncs access control lists from SharePoint and verifies each user's permissions at query time. Users see answers only from documents that they are authorized to access. For more information, see[Admin-managed setup (service credentials)](./sharepoint-kb-admin-managed.html).

After connecting, Amazon Quick indexes your SharePoint document libraries, sites, lists, and pages into a knowledge base. Your Amazon Quick agents can then search this content and generate answers grounded in your SharePoint data.

## Prerequisites

        Before you set up the SharePoint knowledge base integration, make sure that you have the following:

- 
                An AWS account with an active Amazon Quick instance. 
- 
                A Microsoft 365 account with SharePoint Online access. 
- 
                For subscription requirements, see [Set up integrations in the console](./integration-console-setup-process.html).

For admin-managed setup, additional prerequisites apply. For more
            information, see [Admin-managed setup (service credentials)](./sharepoint-kb-admin-managed.html).

###### Tip

Custom SharePoint domains are supported. If your organization uses
                a custom domain instead of the default
                `https://`
                format, you can use your custom SharePoint URL when configuring the
                knowledge base.`tenant`.sharepoint.com