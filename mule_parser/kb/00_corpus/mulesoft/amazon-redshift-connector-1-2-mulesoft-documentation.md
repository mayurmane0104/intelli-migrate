# Amazon Redshift Connector 1.2 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/amazon-redshift-connector/latest](https://docs.mulesoft.com/amazon-redshift-connector/latest)

---

# Amazon Redshift Connector 1.2

Anypoint Connector for Amazon Redshift (Amazon Redshift Connector) is a bulk-load connector that enables you to connect to Amazon Redshift database to perform inserts, deletes, updates, and to execute SQL queries.

For compatibility information and fixed issues, see the Amazon Redshift Connector Release Notes.

## Before You Begin

To use this connector, you must be familiar with:

- 
The Amazon Redshift API 
- 
Anypoint Connectors 
- 
Mule runtime (Mule) 
- 
Elements and global elements in a Mule flow 
- 
Creating a Mule app using Anypoint Studio or Anypoint Code Builder 

Before creating an app, you must have:

- 
Credentials to access the Amazon Redshift target resource 
- 
Anypoint Platform 
- 
Anypoint Studio or Anypoint Code Builder 

## Common Use Cases for the Connector

Some possible uses for this connector include:

- 
Analytics Amazon Redshift operates as an optimized data warehouse that can store large volumes of data, which can then be analyzed using a business intelligence (BI) tool such as Tableau. 
- 
Real-time processing of social media feeds Stream data from your social media feeds, such as a Twitter feed, into Amazon Kinesis Data Streams, and then store that data in a data warehouse, such as Amazon Redshift to perform real-time analytics. 

## Authentication Types

Amazon Redshift Connector uses the following connection methods:

- 
Basic authentication, which uses **user**and**password**field values to connect to the database
- 
IAM authentication, which uses **access key**and**secret key**field values to retrieve the temporary password for the specified user in order to connect to the database

## See Also

- 
[Use Exchange to Discover Connectors, Templates, and Examples](../../connectors/introduction/intro-use-exchange)
- 
[Salesforce Help](https://help.salesforce.com)