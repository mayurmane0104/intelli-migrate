# ServiceNow Connector 6.18 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/servicenow-connector/latest](https://docs.mulesoft.com/servicenow-connector/latest)

---

# ServiceNow Connector 6.18

Anypoint Connector for ServiceNow (ServiceNow Connector) provides connections between Mule runtime engine (Mule) and ServiceNow apps. Use the ServiceNow operations with the custom ServiceNow tables, along with any operations available through the installed plugins.

For compatibility information and fixed issues, see the ServiceNow Connector Release Notes.

## Before You Begin

To use this connector, you must be familiar with:

- 
Anypoint Connectors 
- 
Mule runtime engine (Mule) 
- 
Elements in a Mule flow and global elements 
- 
How to create a Mule app using Anypoint Studio 

Before creating an app, you must have access to the ServiceNow target resource and Anypoint Platform.

## Common Use Cases for the Connector

Common use cases for ServiceNow Connector include:

- 
**IT Service Management (ITSM)**Sync ServiceNow data and extend IT service management (ITSM) capabilities to SaaS and on-premises applications, such as Salesforce, SAP, Workday, and Microsoft Dynamics 365, to help with data migration and replication, application integration, and consolidation. For example, you can bidirectionally sync workers data between Workday and ServiceNow or aggregate employees from Workday and users from ServiceNow into a CSV file. 
- 
**Integrated Business Processes**Fully integrate business processes across HR, legal, procurement, operations, marketing, and facilities departments. 
- 
**Record Creation and Retrieval**Transform enterprise IT by automating and managing IT service relationships to create a single system of records that you can retrieve. 

For examples of these use cases, refer to [ServiceNow Connector Examples](servicenow-connector-examples).

## Audience

- 
New users, read: - 
[Using Anypoint Studio to Configure the Connector](servicenow-connector-studio)to create your Mule app
 
- 
- 
Advanced users, read: 
- 
[Examples](servicenow-connector-examples), which provides one or more use cases for the connector
 

## Connection Types

The following authentication types are supported:

- 
Basic 
- 
OAuth 2.0 Authorization Code 

### Limitations

- 
OAuth 2.0 Authorization Code authentication works only with the following versions of Mule: - 
4.1.5 
- 
4.2.1 and later 
 
- 
- 
Metadata does not work with OAuth 2.0 Authorization Code authentication. 

## Use Exchange Templates and Examples

[Anypoint Exchange](https://www.mulesoft.com/exchange/) provides templates
you can use as a starting point for your app, as well as examples that illustrate a complete solution.

- 
[Workday and ServiceNow Worker Bidirectional Sync](https://anypoint.mulesoft.com/exchange/org.mule.templates/template-wday2snow-worker-bidirectional-sync)
- 
[Workday Worker to ServiceNow Service Request Migration](https://anypoint.mulesoft.com/exchange/org.mule.templates/template-wday2snow-workerservicerequest-migration/)
- 
[Workday and ServiceNow Employee Aggregation](https://anypoint.mulesoft.com/exchange/org.mule.templates/template-wday2snow-employee-aggregation/)
- 
[Workday to ServiceNow Service Worker Migration](https://anypoint.mulesoft.com/exchange/org.mule.templates/template-wday2snow-worker-migration/)
- 
[Workday Worker to ServiceNow Service Request Broadcast](https://anypoint.mulesoft.com/exchange/org.mule.templates/template-wday2snow-worker2servicerequest-broadcast/)

## Next Step

After you complete the prerequisites and experiment with templates and examples, you are ready to create an app with [Anypoint Studio](servicenow-connector-studio).

## See Also

- 
[Use Anypoint Exchange to Discover Connectors, Templates, and Examples](../../connectors/introduction/intro-use-exchange)
- 
[ServiceNow Connector on Exchange](https://www.mulesoft.com/exchange/com.mulesoft.connectors/mule-servicenow-connector/)
- 
[Salesforce Help](https://help.salesforce.com)