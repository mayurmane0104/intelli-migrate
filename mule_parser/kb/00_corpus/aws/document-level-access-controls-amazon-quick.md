# Document-level access controls - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/confluence-kb-acl.html](https://docs.aws.amazon.com/quick/latest/userguide/confluence-kb-acl.html)

---

Confluence Cloud knowledge bases optionally support document-level access control. When enabled, Amazon Quick syncs access control lists (ACLs) from Confluence during each crawl and verifies each user's permissions at query time. Users only see answers from documents they are authorized to access in Confluence.

## How it works

        When a user queries an Amazon Quick agent that uses a Confluence knowledge base with ACL management enabled, the system enforces access controls in two stages:

- 
                **Pre-retrieval filtering**– Amazon Quick performs a semantic search against the vector index to find the most relevant document passages. The system applies access control lists that were synced from Confluence during the last crawl. This produces a preliminary set of candidate documents.
- 
                **Real-time verification**– The system verifies the candidate documents in real time by checking the querying user's current access in Confluence. Only documents the user is currently authorized to access appear in the response.

This two-stage approach provides document-level access control that stays current even when Confluence permissions change between syncs.

Amazon Quick crawls the following Confluence ACL resources:

- 
                **Spaces**– Space permissions apply to all documents in the space by default.
- 
                **Pages**– Pages can be restricted to specific users and groups. Nested pages inherit restrictions from the parent page and can have their own restrictions.
- 
                **Blogs**– Blog posts can be restricted to specific users and groups in the space.
- 
                **Attachments**– Files attached to pages or blog posts inherit the access controls of their parent document.

## Enable ACL management

        You configure ACL management during knowledge base creation in the
            **Additional settings** step. Select the
            **Control document access with ACLs** checkbox to enable
            it. This option requires Atlassian admin credentials, which you provide
            during the **Authentication method** step. Without admin
            credentials, the ACL option is disabled.

###### Important

You cannot change ACL management after you create the knowledge base. If you need to change this setting, you must create a new knowledge base.

Atlassian admin credentials allow Amazon Quick to access all user and group
            information from your Confluence instance, regardless of individual email
            visibility settings. For steps to obtain admin credentials from your
            Atlassian organization, see
            [Obtain Atlassian admin credentials](#confluence-kb-atlassian-admin-credentials). For the
            knowledge base setup steps, see
            [Authenticate your account](./confluence-knowledge-base.html#confluence-kb-setup-auth).

For more information about ACL best practices, see
            [Best practices for managing ACLs in knowledge bases](./acl-best-practices-kb.html).

## Real-time access verification

        When a user submits a query that involves content from an ACL-enabled Confluence knowledge base, Amazon Quick verifies the user's access in real time:

- 
                The user asks a question in the Quick chat assistant. 
- 
                If the answer involves Confluence content from an ACL-enabled knowledge base, Quick prompts the user to sign in to Confluence. 
- 
                The user signs in with their Confluence email and password and accepts the authorization dialog. 
- 
                Quick uses the user's credentials to verify access to each candidate document in real time against the Confluence API. 
- 
                Only documents the user currently has access to in Confluence appear in the response. 

The sign-in is a one-time step. After signing in, users are not prompted again until their session expires.

###### Note

If real-time permission verification fails (for example, if the Confluence API is temporarily unavailable), users see an error message prompting them to retry. Amazon Quick does not fall back to cached permissions — real-time verification is mandatory to ensure access control accuracy.

## Obtain Atlassian admin credentials

        To provide Atlassian admin credentials during Confluence knowledge base setup, your Atlassian organization administrator must complete the following steps.

### Get your API key and Organization ID

- 
                    Sign in to the [Atlassian admin portal](https://admin.atlassian.com/)with administrator permissions.
- 
                    Open the Administration app for your organization. The URL should look like: `https://admin.atlassian.com/o/`.`ORGANIZATION-UUID`/overview
- 
                    Copy the **Organization ID**from the URL.
- 
                    Choose **Settings**, then choose**API Keys**.
- 
                    Choose **Create API key**.
- 
                    Select the following scopes for the API key: - `read:directories:admin`
- `read:workspaces:admin`
 
- 
                    Copy and save both the **Organization ID**and**API Key**.###### NoteAPI keys expire. Monitor the expiration date and update your data source credentials before the key expires. 

### Get your Directory ID

Use the Atlassian Admin Workspace API to retrieve your Directory ID.

- 
                    Run the following command, replacing `ORGANIZATION-ID`with your Organization ID and`API-KEY`with your API key:`curl --request POST \ --url 'https://api.atlassian.com/admin/v2/orgs/``ORGANIZATION-ID`/workspaces' \ --header 'Authorization: Bearer`API-KEY`' \ --header 'Accept: application/json' \ --header 'Content-Type: application/json' \ --data '{ "query": { "field": { "name": "attributes.type", "values": ["confluence"] } }, "limit": 20 }'This query filters results to Confluence workspaces only, so you don't need to page through all workspace types. 
- 
                    In the API response, find the workspace entry that matches your Confluence Cloud instance. Verify the workspace name matches your instance. 
- 
                    Copy the `directory`value from the`attributes`section. This is your**Directory ID**.

For more information about Atlassian admin API scopes, see
                [Atlassian
                    API scopes documentation](https://developer.atlassian.com/cloud/admin/scopes/). For API details, see
                

[Atlassian Admin Workspace API reference](https://developer.atlassian.com/cloud/admin/organization/rest/api-group-workspaces/#api-group-workspaces).

## Limitations

        - 
                **Atlassian admin credentials required**– Document-level access controls require Atlassian admin credentials, which must be provided during knowledge base setup. You cannot enable ACLs without admin credentials, and you cannot add admin credentials after the knowledge base is created.
- 
                **Real-time verification is mandatory**– Amazon Quick always performs real-time permission checks at query time for ACL-enabled knowledge bases. If the Confluence API is unavailable, queries that involve ACL-protected content return an error rather than falling back to cached permissions.

For general ACL limitations and best practices, including ACL
            permanence, research compatibility, and email address management, see
            [Best practices for managing ACLs in knowledge bases](./acl-best-practices-kb.html).

## Next steps

        To verify document-level access controls and troubleshoot permission
            issues, see [Check document access (ACL verification)](./sync-reports-observability.html#sync-reports-acl-verification). For
            information about setting up the Confluence knowledge base integration, see
            [Set up the knowledge base integration](./confluence-knowledge-base.html#confluence-kb-setup).