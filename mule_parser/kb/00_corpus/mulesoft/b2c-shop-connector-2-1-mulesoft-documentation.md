# B2C Shop Connector 2.1 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/commerce-cloud-shop-api-connector/latest](https://docs.mulesoft.com/commerce-cloud-shop-api-connector/latest)

---

# B2C Shop Connector 2.1

| No further updates or new versions are planned for this connector. Use [Anypoint Connector for HTTP (HTTP Connector)](../../http-connector/latest/)instead. Refer to the[migration guide](https://developer.salesforce.com/docs/commerce/commerce-api/guide/migrate-mulesoft-http-connector.html). | 

Anypoint Connector for Salesforce Commerce Cloud B2C Shop APIs (B2C Shop Connector) enables a client to interact with the Commerce Cloud B2C API system as either a shop customer or as an agent shopping on behalf of a customer.

For information about compatibility and fixed issues, see Commerce Cloud B2C Shop Connector Release Notes.

| Salesforce Commerce Cloud B2C Data Connector and Salesforce Commerce Cloud B2C Shop Connector cannot be run in the same application. | 

## Before You Begin

To use this connector, you must be familiar with:

- 
The Salesforce Commerce Cloud Shop API 
- 
Anypoint Connectors 
- 
Mule runtime engine (Mule) 
- 
Elements and global elements in a Mule flow 
- 
How to create a Mule app using Anypoint Studio 

Before creating an app, you must have access to:

- 
The Commerce Cloud B2C Shop Connector target resource 
- 
Anypoint Platform 
- 
Anypoint Studio version 7.1 or later 
- 
Salesforce-provided Commerce Cloud credentials (such as Client Id, Client Secret, and Scopes) necessary to access Shop API. 

## Common Uses for the Connector

These are some common use cases for B2C Shop Connector:

- 
Create a basket 
- 
Add items to a basket 
- 
Add shipping details 
- 
Place an order 

Check the [Examples](shop-api-connector-examples) for a simple use case.

## Audience

- 
New user To create your Mule app, see: 
- 
[Using Anypoint Studio to Configure Commerce Cloud B2C Connector](shop-api-connector-studio)
- 
Advanced user 
- 
Read the following: 

## Connection Types

B2C Shop Connector connections use the following authentication types:

- 
Customers Auth 
 Uses a Bearer Token, which is generated using the**Authorize Customer**operation
- 
OAuth 2.0 
 Delegates user authentication to the service hosting the user account

For information about configuring authentication types, see [Using Anypoint Studio to Configure Commerce Cloud B2C Shop Connector](shop-api-connector-studio).

## Next Step

After you complete the prerequisites and try the templates and examples, you are ready to create an app and configure the connector using [Anypoint Studio](shop-api-connector-studio).

## See Also

- 
[Use Exchange to Discover Connectors, Templates, and Examples](../../connectors/introduction/intro-use-exchange)
- 
[Salesforce Help](https://help.salesforce.com)