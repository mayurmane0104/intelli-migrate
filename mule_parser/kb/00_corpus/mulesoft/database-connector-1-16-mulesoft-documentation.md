# Database Connector 1.16 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/db-connector/latest](https://docs.mulesoft.com/db-connector/latest)

---

# Database Connector 1.16

Anypoint Connector for Database (Database Connector) establishes communication between your Mule app and a relational database. Database Connector can connect to almost any Java Database Connectivity (JDBC) relational database and run SQL operations. An application can support multi-tenant scenarios using the same configuration element, changing the connection attributes based on, for example, information coming from each request.

Database Connector has connection providers that automatically set the driver class name and create JDBC URLs with given parameters for the following databases:

- 
Derby 
- 
Microsoft SQL Server 
- 
MySQL 
- 
Oracle 

You can set up other JDBC databases using a generic JDBC configuration. Database Connector is JDBC compliant. Ensure that for the connection configuration, you use a driver that is compliant with JDBC to avoid compatibility issues. Additionally, you can reference a JDBC `DataSource` object or an `XADataSource` object, which is required for XA transactions, by creating the object in Anypoint Studio using Spring.

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

Before creating an app, you must have access to the database target resource, Anypoint Platform, and have downloaded the proper database driver for your database.

## Common Use Cases for the Connector

Database Connector enables you to:

- 
Perform predefined queries, dynamically constructed queries, and template queries that are self-sufficient and customizable. 
- 
Specify DataWeave expressions in connector fields and configure attributes dynamically, depending on the database configuration you use. 
- 
Use a source listener operation to read from a database in the data source section of a flow. 
- 
Execute other operations to read and write to a database anywhere in the process section. 
- 
Perform multiple SQL requests in a single bulk update. 
- 
Make Data Definition Language (DDL) requests that alter the data structure rather than the data itself. 
- 
Execute stored procedures and SQL scripts. 

For examples, see [Examples](database-connector-examples).

## Audience

- 
New users, read: - 
[Using Anypoint Studio to Configure the Connector](database-connector-studio)to create your Mule app
- 
[Examples](database-connector-examples), which provide one or more use cases for the connector
 
- 
- 
Advanced users, read: 
- 
[Examples](database-connector-examples), which provide one or more use cases for the connector
 

## Using Exchange Templates and Examples

[Anypoint Exchange](https://www.mulesoft.com/exchange/) provides templates
that you can use as starting points for your apps and examples that illustrate a complete solution.

- 
[Database Connector Examples](https://www.mulesoft.com/exchange/?search=database&type=example)
- 
[Database Connector Templates](https://www.mulesoft.com/exchange/?search=database&type=template)

## Next Step

After you complete the prerequisites and try the templates and examples, you are ready to create your own app and configure the connector using [Anypoint Studio](database-connector-studio).

## See Also

- 
[Use Exchange to Discover Connectors, Templates, and Examples](../../connectors/introduction/intro-use-exchange)
- 
[Salesforce Help](https://help.salesforce.com)