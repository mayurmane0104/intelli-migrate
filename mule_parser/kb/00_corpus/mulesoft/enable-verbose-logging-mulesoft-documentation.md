# Enable Verbose Logging | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/enable-verbose-logging](https://docs.mulesoft.com/mule-runtime/latest/enable-verbose-logging)

---

```
<Loggers>
    ...
    <AsyncLogger name="org.mule.extensions.jms" level="DEBUG"/>
    ...
</Loggers>
```
xml# Enable Verbose Logging

You can enable verbose logging for different modules and connectors. Because of the high impact to application performance, limit verbose logging to testing and troubleshooting operations.

## Configure Verbose Logging

To configure verbose logging, add an entry to your `log4j2.xml` file, indicating the package names of the connectors or modules you want to log, and set the log level to `DEBUG`.

The following example shows how to find the package names for Anypoint Connector JMS (JMS Connector) and configure verbose logging:

- 
In the **Package Explorer**view, open the JMS Connector package library.
- 
Inside the `.jar`file, locate all Mule-related packages.![A package Explorer view listing various Java packages and libraries in a development environment](_images/mruntime-verbose-log-package.png) 
- 
Add an entry to your `log4j2.xml`file, indicating the package name and log level =`DEBUG`:

## Common Connector Package Names

The following table shows some common Anypoint Connectors and their package names so you don’t have to search for them:

| Connector Name | Package Names | 
|---|---|
| Anypoint Connector for HTTP | 
 | 
| Anypoint Connector for Salesforce | 
 | 
| Anypoint Connector for FTP | 
 | 
| Anypoint Connector for SFTP | 
 | 
| Anypoint Connector for FTPS | 
 | 
| Anypoint Connector for NetSuite | 
 | 
| Anypoint Connector for Amazon SQS | 
 | 
| Anypoint Connector for Microsoft Dynamics 365 | 
 | 
| Anypoint Connector for MuleSoft SAP | 
 | 
| Anypoint Connector for Anypoint MQ | 
 | 
| Anypoint Connector for Database | 
 | 
| Anypoint Connector for Microsoft SharePoint (version 3.x) | 
 |