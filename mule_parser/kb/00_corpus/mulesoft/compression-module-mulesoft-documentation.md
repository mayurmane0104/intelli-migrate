# Compression Module | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/compression-module/latest](https://docs.mulesoft.com/compression-module/latest)

---

# Compression Module

Compression module v2.2

Compression module supports and provides access to the most-used file archiver and compression formats through a Mule app.

A file archiver is a computer program that combines a number of files together into one archive file for easier transportation or storage, and most archivers employ data compression in their archive formats to reduce the size of the final archive. However, not all compression algorithms can archive multiple files. Some are limited to single-file data compression.

This module compresses and decompresses files for each of the available formats without losing any of the features that the format associated algorithm provides.

To achieve this capability, the module provides the **Compress** and **Decompress** operations, which enable you to
compress and decompress a single file. Additionally, the module provides the **Archive** and **Extract** operations to archive and extract files. You can configure these operations with the compression or archiving strategies of your choice.

## Before You Begin

To use this connector, you must be familiar with:

- 
Anypoint Connectors 
- 
Mule runtime engine (Mule) 
- 
Elements and global elements in a Mule flow 
- 
How to create a Mule app using Anypoint Studio 

Before creating an app, you must have access to Anypoint Platform and Anypoint Studio.

## Common Use Cases For the Connector

Common use cases for Compression module include:

- 
Compress and decompress a file’s payload from a remote service. 
- 
Archive and extrat files from a file folder. 

For examples of these use cases, refer to [Compression Module Examples](compression-module-examples).

## Next Step

After you complete the prerequisites, you are ready to create an app and configure the connector using [Anypoint Studio](compression-module-studio-configuration).

## See Also

- 
[Salesforce Help](https://help.salesforce.com)