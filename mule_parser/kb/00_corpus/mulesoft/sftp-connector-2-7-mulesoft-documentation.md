# SFTP Connector 2.7 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/sftp-connector/latest](https://docs.mulesoft.com/sftp-connector/latest)

---

# SFTP Connector 2.7

Anypoint Connector for SFTP (SFTP Connector) manages secure file transfers over the Secure File Transfer Protocol (SFTP). You can read files, list directories, create folders, copy, move, rename, and delete files on SFTP servers with built-in file locking and matching capabilities. The connector provides the same operations and behavior as File Connector and FTP Connector for consistent integration patterns.

## Representation of File Attributes

Mule 4 provides a message structure of a payload and attributes in which the data moves around, making that payload a file content. The attributes provide an object that contains metadata on the payload and information such as the file’s name, path, size, and timestamps. For FTP Connector and SFTP Connector, these attributes are known as  *file attributes*.

The Mule message contains the concepts of encoding and MIME type. These describe the format in which a payload is represented. The file attributes describe a file’s encoding and MIME type.

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

## Next Step

After you complete the prerequisites, you are ready to create your own app and configure the connector using [Anypoint Studio](sftp-studio).

## See Also

- 
[Use Exchange to Discover Connectors, Templates, and Examples](../../connectors/introduction/intro-use-exchange)
- 
[Salesforce Help](https://help.salesforce.com)