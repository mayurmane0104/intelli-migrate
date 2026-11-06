# Document metadata - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/s3-metadata.html](https://docs.aws.amazon.com/quick/latest/userguide/s3-metadata.html)

---

You can add metadata to documents in your Amazon S3 bucket to customize chat results and control document-level access. Metadata is additional information about a document, such as its title, creation date, and access permissions.

Amazon Quick supports source attribution with citations. If you specify the
        `_source_uri` metadata field, the source attribution links in chat results
        direct users to the configured URL. If you don't specify a `_source_uri`,
        users can still access source documents through clickable citation links that download
        the file at query time.

## Document metadata location

        
        In Amazon S3, each metadata file can be associated with an indexed document. Your metadata files must be stored in the same Amazon S3 bucket as your indexed files. You can specify a location within the Amazon S3 bucket for your metadata files when configuring your Amazon S3 integration in Amazon Quick.

If you don't specify an Amazon S3 prefix, your metadata files must be stored in the same location as your indexed documents. If you specify an Amazon S3 prefix for your metadata files, they must be in a directory structure parallel to your indexed documents. Amazon Quick looks only in the specified directory for your metadata. If the metadata isn't read, check that the directory location matches the location of your metadata.

The following examples show how the indexed document location maps to the metadata file location. The document's Amazon S3 key is appended to the metadata's Amazon S3 prefix and then suffixed with `.metadata.json` to form the metadata file's Amazon S3 path.

###### Note

The combined Amazon S3 key, the metadata's Amazon S3 prefix, and the `.metadata.json` suffix must be no more than a total of 1,024 characters. We recommend that your Amazon S3 key is less than 1,000 characters to account for additional characters when combining your key with the prefix and suffix.

###### Example 1: No metadata path specified

```
Bucket name:
     s3://bucketName
Document path:
     documents
Metadata path:
     none
File mapping
     s3://bucketName/documents/file.txt -> 
        s3://bucketName/documents/file.txt.metadata.json
            
```
###### Example 2: Metadata path specified

```
Bucket name:
     s3://bucketName
Document path:
     documents/legal
Metadata path:
     metadata
File mapping
     s3://bucketName/documents/legal/file.txt -> 
        s3://bucketName/metadata/documents/legal/file.txt.metadata.json
            
```
## Document metadata structure

        
        You define your document metadata itself in a JSON file. The file must be a UTF-8 text file without a BOM marker. The file name of the JSON file must be `<document>.<extension>.metadata.json`. In this example, `document` is the name of the document that the metadata applies to and `extension` is the file extension for the document. The document ID must be unique in `<document>.<extension>.metadata.json`.

The content of the JSON file uses the following template:

```
{
    "DocumentId": "document ID",
    "Attributes": {
        "_authors": ["author of the document"],
        "_category": "document category",
        "_created_at": "ISO 8601 encoded string",
        "_last_updated_at": "ISO 8601 encoded string",
        "_source_uri": "document URI",
        "_version": "file version",
        "_view_count": number of times document has been viewed
    },
    "AccessControlList": [
        {
            "Name": "user1@example.com",
            "Type": "GROUP | USER",
            "Access": "ALLOW | DENY"
        }
    ],
    "Title": "document title",
    "ContentType": "PDF | HTML | MS_WORD | PLAIN_TEXT | PPT | RTF | XML | XSLT | MS_EXCEL | CSV | JSON | MD"
}
        
```
If you provide a metadata path, make sure that directory structure inside the metadata directory exactly matches the directory structure of data file.

For example, if the data file location is at `s3://bucketName/documents/legal/file.txt`, the metadata file location should be at `s3://bucketName/metadata/documents/legal/file.txt.metadata.json`.

All of the attributes and fields are optional, so it's not necessary to include all attributes. However, you must provide a value for each attribute that you want to include; the value can't be empty.

The `_created_at` and `_last_updated_at` metadata fields are ISO 8601 encoded dates. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25, 2012, at 12:30PM (plus 10 seconds) in the Central European Time time zone.

The `AccessControlList` field is an optional array that defines
            document-level access control. Each entry in the array contains the following
            fields:

- 
                `Name`– For`USER`type, the email address of the user in Quick. For`GROUP`type, the group name in Quick.
- 
                `Type`– Either`USER`or`GROUP`.
- 
                `Access`– Either`ALLOW`or`DENY`.

###### Note

To use the `AccessControlList` field, you must enable document-level
                ACLs when creating the knowledge base. For more information, see
                [Document-level ACLs](./s3-acl.html).