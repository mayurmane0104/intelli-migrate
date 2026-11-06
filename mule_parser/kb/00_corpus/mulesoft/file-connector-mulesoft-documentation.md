# File Connector | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/file-connector/latest](https://docs.mulesoft.com/file-connector/latest)

---

# File Connector

Anypoint Connector for File (File Connector) manages files and folders on a locally mounted file system. The connector’s main features include:

- 
The ability to read files or fully list directory contents on demand 
- 
Support for common file operations such as creating directories, reading, writing, copying, moving, renaming, deleting and listing files 
- 
Support for locking files 
- 
File matching functionality 
- 
A design that is consistent with FTP Connector and SFTP Connector 

## Representation of File Attributes

Mule 4 provides a message structure of a payload and attributes in which the data moves around, making that payload file content. The attributes provide an object that contains metadata on the payload and information such as the file’s name, path, size, and timestamps. For FTP Connector and SFTP Connector, these attributes are named *file attributes*.

The Mule message specifies the encoding and MIME type, which describe the format in which a payload is represented. The file attributes describe a file’s encoding and MIME type.

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