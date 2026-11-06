# Document-level ACLs - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/s3-acl.html](https://docs.aws.amazon.com/quick/latest/userguide/s3-acl.html)

---

You can enable access control lists (ACLs) at the Amazon S3 knowledge base level using one of two configuration methods, each optimized for different use cases.

###### Important

Document-level ACL configuration is permanent. You cannot enable ACLs on knowledge bases created without ACL support, and you cannot disable ACLs once enabled. To change ACL configuration, create a new knowledge base with your desired setting from the start.

###### Note

For ACL-enabled knowledge bases, documents without an associated ACL entry are not ingested. Make sure every document has an ACL defined either through the global ACL file or in its metadata file.

- **Global ACL configuration file**
- 
                Create a single centralized file that defines access permissions at the folder level. This provides a streamlined way to manage permissions across large document hierarchies. This method is ideal for organizations with stable permission structures. Any changes to the global file require reindexing the entire affected prefix, which can take hours for knowledge bases with tens of millions of documents. For the file format, see [Global ACL file structure](#s3-global-acl).
- **Document-level metadata files**
- 
                Each document has its own metadata file containing specific access control information. This approach requires you to create and maintain individual metadata files for each document. It enables significantly faster index updates when permissions change because only the affected documents need to be reindexed rather than entire folder structures. For more information about configuring ACLs in metadata files, see [Document metadata](./s3-metadata.html).

Choose the method that best fits your operational needs: centralized management with the global ACL file for simpler administration, or document-level metadata files for faster permission updates and more granular control.

Keep your document-level ACLs current by regularly updating the Amazon S3 ACL configuration
        to match your organization's access requirements. For more information about common best
        practices, see [Best practices for managing ACLs in knowledge bases](./acl-best-practices-kb.html).

## Global ACL file structure

        The global file provides centralized access control management at the folder level. Each entry in the file maps an Amazon S3 key prefix to a set of ACL entries that apply to all documents under that prefix.

The global ACL json file uses the following structure:

```
[
    {
        "keyPrefix": "s3://BUCKETNAME/prefix1/",
        "aclEntries": [
            {
                "Name": "user1@example.com",
                "Type": "USER",
                "Access": "ALLOW"
            },
            {
                "Name": "group1",
                "Type": "GROUP",
                "Access": "DENY"
            }
        ]
    },
    {
        "keyPrefix": "s3://BUCKETNAME/prefix1/document_1.txt",
        "aclEntries": [
            {
                "Name": "user1@example.com",
                "Type": "USER",
                "Access": "ALLOW"
            },
            {
                "Name": "group1",
                "Type": "GROUP",
                "Access": "DENY"
            }
        ]
    },
    {
        "keyPrefix": "s3://BUCKETNAME/prefix2/",
        "aclEntries": [
            {
                "Name": "user2@example.com",
                "Type": "USER",
                "Access": "ALLOW"
            },
            {
                "Name": "user1@example.com",
                "Type": "USER",
                "Access": "DENY"
            },
            {
                "Name": "group1",
                "Type": "GROUP",
                "Access": "DENY"
            }
        ]
    }
]
        
```
Each entry in the array contains the following fields:

- `keyPrefix`
- 
                    The Amazon S3 path prefix that the ACL entries apply to. All documents under this prefix inherit the specified permissions. 
- `aclEntries`
- 
                    An array of access control entries, each containing the following fields: - 
                            `Name`– For`USER`type, the email address of the user in Quick. For`GROUP`type, the group name in Quick.
- 
                            `Type`– Either`USER`or`GROUP`.
- 
                            `Access`– Either`ALLOW`or`DENY`.
 
-