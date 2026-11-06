# Hadoop (HDFS) Connector | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/hdfs-connector/latest](https://docs.mulesoft.com/hdfs-connector/latest)

---

# Hadoop (HDFS) Connector

Hadoop (HDFS) Connector Version 6.0

Anypoint Connector for Hadoop (HDFS) works as a bidirectional gateway between Mule applications and Apache Hadoop Distributed File System (HDFS). You can use the Hadoop (HDFS) Connector to poll the content of a file at a configurable rate or interval, or to manipulate data in an HDFS server.

For information about compatibility and fixed issues, see [Hadoop (HDFS) Connector Release Notes](../../release-notes/connector/hdfs-connector-release-notes-mule-4)

## Before You Begin

To use this connector, you must be familiar with:

- 
Anypoint Connectors 
- 
Mule runtime engine (Mule) 
- 
Elements in a Mule flow 
- 
Global elements 
- 
How to create a Mule app using Anypoint Studio 

Before creating an app, you must have:

- 
Access to the Hadoop (HDFS) target resource and Anypoint Platform 
- 
Anypoint Studio version 7.0 or later 
- 
A running instance of Hadoop Distributed File System (HDFS) 

## Connection Authentication Types

Hadoop (HDFS) Connector supports the following connection authentication types:

- 
Kerberos 
 This connection type uses the Kerberos principal as the username. The keytab path you specify obtains a ticket-granting ticket (TGT) from the authorization server.
- 
Simple 
 This connection type passes the name of the node that contains the file system you want to connect to as the default name key.

## Next Step

After you complete the prerequisites and experiment with templates and examples, you are ready to create an app with [Anypoint Studio](hdfs-connector-studio).

## See Also

- 
[Hadoop (HDFS) Connector on Exchange](https://www.mulesoft.com/exchange/?search=hdfs&type=connector)
- 
[Salesforce Help](https://help.salesforce.com)