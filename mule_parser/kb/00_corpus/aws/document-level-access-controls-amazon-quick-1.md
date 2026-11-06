# Document-level access controls - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/google-drive-kb-acl.html](https://docs.aws.amazon.com/quick/latest/userguide/google-drive-kb-acl.html)

---

Admin-managed Google Drive knowledge bases include built-in document-level access control. Amazon Quick syncs access control lists (ACLs) from Google Drive during each crawl and verifies each user's permissions at query time, so users only see answers from documents that they are authorized to access.

## How it works

        When a user submits a query to an Amazon Quick agent that uses an admin-managed Google Drive knowledge base, the system enforces access controls in two stages:

- 
                **Pre-retrieval filtering**– Amazon Quick performs a semantic search against the vector index to find the most relevant document passages. The system applies access control lists that are already stored in the index. This produces a preliminary set of candidate documents. This stage is necessary because real-time API calls for every document in the index would be too costly at scale.
- 
                **Real-time verification**– The system verifies the candidate documents in real time by calling the Google Drive APIs. It uses the service account credential that the administrator provided to generate user-specific access tokens through impersonation. Google Drive maintains the source of truth for access control lists that are associated with each document. The system removes any documents that the user is not authorized to access from the result set.

The system passes only the verified and authorized document passages to the model as context. The model uses this knowledge to generate a response. This two-stage approach provides document-level access control guarantees and maintains performance at scale.

## Enable ACL management

        Document-level access control is automatically enabled for all admin-managed knowledge bases. No additional configuration is required.

For more information about ACL best practices, see
            [Best practices for managing ACLs in knowledge bases](./acl-best-practices-kb.html).