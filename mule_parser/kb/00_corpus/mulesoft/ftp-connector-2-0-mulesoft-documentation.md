# FTP Connector 2.0 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/ftp-connector/latest](https://docs.mulesoft.com/ftp-connector/latest)

---

# FTP Connector 2.0

Support Category: [Select](https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/Agreements/versioning-back-support-policy.pdf)

Anypoint Connector for FTP (FTP Connector) provides access to files and folders on an FTP server. FTP connector operations manage file transfers by using File Transfer Protocol (FTP). The connector’s main features include:

- 
The ability to read files or fully list directory contents on demand. 
- 
Support for common FTP operations such as creating directories and copying, moving, renaming, and deleting files. 
- 
Support for locking files. 
- 
File matching functionality. 
- 
A design that is consistent with the File and FTP Connectors. The same set of operations is available using these two connectors, and they behave similarly. 

| FTP Connector doesn’t support z/OS MVS Datasets. | 

## Representation of File Attributes

Mule 4 provides a message structure of a payload and attributes in which the data moves around, making that payload a file content. The attributes provide an object that contains metadata on the payload and information such as the file’s name, path, size, and timestamps. For FTP Connector and SFTP Connector, these attributes are known as  *file attributes*.

Messages comprise *file content* (a payload) and *file attributes* (metadata about the payload, such the file’s name, path, size, and timestamps. The file attributes also describe the format in which a payload is represented by including a file’s encoding and MIME type.

## Before You Begin

To use this connector, you must be familiar with:

- 
Anypoint Connectors 
- 
Mule runtime engine (Mule) 
- 
Elements and global elements in a Mule flow 
- 
Creating a Mule app using Anypoint Studio or Anypoint Code Builder 

Before creating an app, you must have access to Anypoint Platform and Anypoint Studio.

## See Also

- 
[Use Exchange to Discover Connectors, Templates, and Examples](../../connectors/introduction/intro-use-exchange)
- 
[Salesforce Help](https://help.salesforce.com)