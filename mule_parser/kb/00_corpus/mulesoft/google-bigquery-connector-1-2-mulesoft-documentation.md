# Google BigQuery Connector 1.2 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/google-bigquery-connector/latest](https://docs.mulesoft.com/google-bigquery-connector/latest)

---

# Google BigQuery Connector 1.2

Anypoint Connector for Google BigQuery (Google BigQuery Connector) syncs data and automates business processes between Google BigQuery and third-party applications, either on-premises or in the cloud.

For information about compatibility and fixed issues, refer to the Google BigQuery Connector Release Notes.

## Before You Begin

To use this connector, you must be familiar with:

- 
The Google BigQuery API 
- 
Anypoint Connectors 
- 
Mule runtime engine (Mule) 
- 
Elements and global elements in a Mule flow 
- 
How to create a Mule app using Anypoint Studio 

Before creating an app, you must have:

- 
Credentials to access the Google BigQuery target resource 
- 
Anypoint Platform 
- 
Anypoint Studio or Anypoint Code Builder 

## Common Use Cases For the Connector

These are some common use cases for Google BigQuery Connector:

- 
Use log and event data collection to analyze problems 
- 
Insert, update, and delete data in Google BigQuery You can insert multiple rows by using multi-row `INSERT`statements in your query or job (for example,`INSERT INTO table VALUES (1, 'val1'), (2, 'val2')`). The connector passes the SQL to BigQuery. There’s no dedicated bulk insert operation, batching, or optimization for large datasets.`MERGE`isn’t supported. For merge-like behavior, use a`SELECT`followed by conditional`INSERT`or`UPDATE`operations in your flow, which is less efficient and not atomic.
- 
Execute a query in Google BigQuery 

For examples of these use cases, refer to [Google BigQuery Connector Examples](google-bigquery-connector-examples).

## Connection Types

Google BigQuery connections use the following authentication types:

- 
JWT Connection 
 Uses a token for authentication
- 
OAuth2 Connection 
 Uses service account authentication

For information about configuring authentication types, refer to [Configure a Global Element for the Connector](google-bigquery-connector-studio#configure-global-element).

## Next Step

After you complete the prerequisites, you are ready to create an app and configure the connector using [Anypoint Studio](google-bigquery-connector-studio).

## See Also

- 
[Use Exchange to Discover Connectors, Templates, and Examples](../../connectors/introduction/intro-use-exchange)
- 
[Salesforce Help](https://help.salesforce.com)