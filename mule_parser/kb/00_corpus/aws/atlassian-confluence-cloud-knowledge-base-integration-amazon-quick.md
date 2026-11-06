# Atlassian Confluence Cloud knowledge base integration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/confluence-knowledge-base.html](https://docs.aws.amazon.com/quick/latest/userguide/confluence-knowledge-base.html)

---

Use the Atlassian Confluence Cloud knowledge base integration to index Confluence
        content so that Amazon Quick agents can search and answer questions about it.
        Amazon Quick supports optional document-level access controls (ACLs) for Confluence
        knowledge bases. When enabled, users only see answers from documents they are
        authorized to access in Confluence. For more information, see
        [Document-level access controls](./confluence-kb-acl.html).

## Before you begin

        Make sure you have the following before you set up the integration.

- 
                An Atlassian Confluence Cloud instance. 
- 
                For Quick subscription requirements, see [Set up integrations in the console](./integration-console-setup-process.html).

If you plan to enable document-level access controls, you must provide Atlassian admin credentials during setup. These credentials allow Amazon Quick to access all user and group information regardless of individual email visibility settings. Without admin credentials, the ACL option is not available during knowledge base creation. To provide admin credentials, you need the following from your Atlassian organization administrator:

- 
                **Atlassian admin API key**– An alphanumeric string generated in the Atlassian admin portal.
- 
                **Organization ID (UUID)**– The unique identifier for your Atlassian organization. You can find this in your browser URL when signed in to the admin portal:`admin.atlassian.com/o/`.`orgId`
- 
                **Directory ID (UUID)**– The unique identifier for your user directory. Retrieve this value using the Atlassian Admin Workspace API.

For detailed steps to obtain these credentials, see
            [Obtain Atlassian admin credentials](./confluence-kb-acl.html#confluence-kb-atlassian-admin-credentials).

## Set up the knowledge base integration

        The setup wizard has three steps: authentication, knowledge base creation, and additional settings.

### Authenticate your account

- 
                    In the Amazon Quick console, choose **Knowledge**.
- 
                    Under **Knowledge**, choose**Atlassian Confluence Cloud**and choose the Add (plus "+") button.
- 
                    In the **Create Confluence knowledge base**dialog, under**Authentication method**, choose an existing connected account from the**Name**dropdown, or choose**Add account**to create a new connection.
- 
                    If you are adding a new account, complete the following fields: - 
                            **Name**– A descriptive name for your connection.
- 
                            **Description**(Optional) – Notes about the connection.
- 
                            **Confluence URL**– The URL of your Atlassian site (for example,`https://`).`your-site`.atlassian.net
 
- 
                            
- 
                    (Optional) Under **ACL Management**, select**Use Atlassian admin credentials**to provide Atlassian admin credentials. When selected, enter the following:- 
                            **API key**– The Atlassian admin API key.
- 
                            **OrganizationID (UUID)**– Your Atlassian organization ID.
- 
                            **Directory ID (UUID)**– Your Atlassian user directory ID.
 ###### ImportantAtlassian admin credentials are required to enable document-level access controls (ACLs) in **Additional settings**. Without admin credentials, the ACL option is disabled. Admin credentials cannot be added after the knowledge base is created. For steps to obtain these credentials, see[Obtain Atlassian admin credentials](./confluence-kb-acl.html#confluence-kb-atlassian-admin-credentials).
- 
                            
- 
                    Choose **Next**.
- 
                    Complete the Confluence Cloud authentication popup that appears. Review the requested permissions and choose **Accept**to authorize Amazon Quick to access your Confluence content.

### Create the knowledge base

- 
                    Under **Create knowledge base**, enter a**Name**for your knowledge base.
- 
                    (Optional) Enter a **Description**with notes about how the knowledge base will be used.
- 
                    Under **Confluence URLs**, paste the URLs of the Confluence spaces, blogs, or pages that you want to include. Choose**Add**after each URL.###### NoteURLs that follow the structure `https://`are treated as page URLs, not space URLs. To index an entire space, use the space URL without`company`.atlassian.net/wiki/spaces/`space-key`/overview`/overview`(for example,`https://`).`company`.atlassian.net/wiki/spaces/`space-key`
- 
                    Choose **Next: Additional settings**to configure access controls and indexing options, or choose**Create**to create the knowledge base with default settings.

### Configure additional settings

- 
                    To enable document-level access controls, select **Control document access with ACLs**. This option is only available if you provided Atlassian admin credentials in**Authentication method**. When enabled, Amazon Quick syncs access control lists from Confluence and verifies each user's permissions at query time. For more information about how access controls work, see[Document-level access controls](./confluence-kb-acl.html).If you do not enable ACLs, access is controlled at the knowledge base level. Anyone who has access to the knowledge base can get insights from all of the content within it. When ACLs are enabled, access is controlled at the document level. Users who have access to the knowledge base only see answers from documents that they are authorized to access in Confluence. ###### ImportantACL management cannot be changed after the knowledge base is created. If you need to change this setting, you must create a new knowledge base. ###### NoteIf you did not provide Atlassian admin credentials in **Authentication method**, this option is disabled. To enable ACLs, choose**Back**or cancel the wizard and start again with a connected account that includes admin credentials.
- 
                    Under **Multi-media content, file size, and file patterns**, configure the following indexing options as needed:- 
                            **Visual content in documents**– Index visual content such as images and charts embedded in documents.
- 
                            **Audio files**– Index audio file attachments.
- 
                            **Video files**– Index video file attachments.
- 
                            **Maximum single file size**– The maximum file size for individual attachments (default: 50 MB).
 
- 
                            
- 
                    Choose **Create**.

## Supported content types

        - Confluence pages and blog posts 
- Page and blog post attachments 

When you add a Confluence space URL, Amazon Quick crawls all pages and
            blog posts within that space. For supported attachment file types and size
            limits, see [File size and content limits](./knowledge-base-integrations.html#file-size-and-content-limits).

## Manage knowledge bases

         
            ### Edit existing knowledge bases

- 
                    In the Amazon Quick console, choose **Knowledge bases**.
- 
                    Select your Confluence Cloud knowledge base from the list. 
- 
                    Choose the three-dot icon under **Actions**, then choose**Edit knowledge base**.
- 
                    Update your configuration settings as needed and choose **Save**.

## Troubleshoot

        To edit, share, or delete your integration, see [Managing existing integrations](./integration-workflows.html#managing-existing-integrations).

For general knowledge base troubleshooting, including sync issues and missing
            documents, see [Troubleshooting knowledge bases](./troubleshooting-knowledge-bases.html).

### Blocked OAuth app authorization

**Symptoms:**

- Error message: "Your site admin must authorize this app for the site - `instance-name`.atlassian.net before the app can access your account."
- Choosing - **Accept**in the consent dialog has no effect.

**Cause:**

Your Atlassian site administrator has blocked user-installed OAuth apps. When this setting is enabled, only a site or organization administrator can authorize new third-party apps.

**Resolution steps:**

Use one of the following options to resolve this issue.

- 
                    **Option 1 (Recommended): Admin authorizes the app directly**- An Atlassian site administrator navigates to Amazon Quick and starts a new knowledge base setup with Confluence Cloud. 
- Because the administrator has site-level permissions, a clean consent screen appears without the error. 
- The administrator chooses - **Accept**to install the app.
 After the administrator authorizes the app, all other users on the site can connect without issues. 
- 
                    **Option 2: Temporarily allow user-installed apps**– An administrator goes to`admin.atlassian.com`, navigates to**Apps**,**Atlassian Apps**, then chooses the link for third-party and Marketplace apps. Under**Settings**, find**User Installed Apps**and toggle to allow user apps. After the user authorizes Amazon Quick, toggle the setting back to block user apps.

###### Important

Admin authorization applies per Atlassian site, not per organization.
                    If your company has multiple sites (for example,
                    `team-a.atlassian.net` and
                    `team-b.atlassian.net`), each site requires separate
                    authorization.

###### Note

While user-installed apps are unblocked (Option 2), any user on the site can authorize any OAuth app. Re-enable the block promptly after the user has connected.

### Authentication popup fails

**Symptoms:**

- Authentication popup does not appear or closes immediately. 
- Popup appears but fails to complete the OAuth flow. 

**Resolution steps:**

- Verify that your browser allows popups from the Amazon Quick console domain. 
- Verify that your Confluence Cloud instance is accessible from your network. 
- Try using a different browser or clearing your browser cache. 

### Missing content in knowledge base

**Symptoms:**

- Knowledge base sync completes but expected content is not indexed. 
- Search results do not include content from specific spaces or pages. 
- Only one document is indexed for an entire space. 

**Resolution steps:**

- Verify that the Confluence Cloud user who authenticated has access to the spaces and pages you selected during setup. 
- Check that the selected content types are supported (pages, blog posts, and attachments). 
- Review the content selection in your knowledge base configuration to confirm the correct spaces and pages are included. 
- 
                    Check your Confluence URLs for the `/overview`suffix. URLs that end with`/wiki/spaces/`are treated as a single page URL, not a full space. If you intended to index the entire space, use the space URL without`space-key`/overview`/overview`(for example,`https://`).`company`.atlassian.net/wiki/spaces/`space-key`

### ACL-related issues

**No results from ACL-enabled knowledge
                    base**

- Verify that the end user has signed in to Confluence when prompted during their first query. The sign-in is required for real-time permission verification. 
- Verify that the end user has access to the relevant Confluence content in their Confluence instance. 

**Documents skipped during sync**

- If sync reports show items with status SKIPPED, verify that the authenticating user has access to the Confluence spaces and pages included in the knowledge base. 
- For more information about verifying document access, see - [Check document access (ACL verification)](./sync-reports-observability.html#sync-reports-acl-verification).