# Tableau Connector 1.1 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/tableau-specialist-connector/latest](https://docs.mulesoft.com/tableau-specialist-connector/latest)

---

# Tableau Connector 1.1

Anypoint Connector for Tableau (Tableau Connector) enables you to integrate and transform data from applications to build visualizations. This connector exposes operations provided by the Tableau API.

For information about compatibility and fixed issues, refer to the Tableau Connector Release Notes.

## Before You Begin

To use this connector, you must be familiar with:

- 
The Tableau Connector’s API 
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
Credentials to access the Tableau target resource 
- 
Anypoint Platform 
- 
Anypoint Studio or Anypoint Code Builder 

## Common Use Cases for the Connector

Some common use cases for Tableau Connector include:

- 
Visualizing data from a Zendesk or Salesforce endpoint. 
- 
Cleaning, preparing, and curating data to power flows. 
- 
Analyzing product sales trends based on a region using a Tableau mapping. 
- 
Importing data as a Tableau Data Extract (TDE) file to create interactive dashboards that work in real time. 

## Connection Types

Tableau connections use the following authentication types:

- 
Hyper Configuration - 
Hyper Connection 
 
- 
- 
Rest Configuration - 
Basic Authentication 
- 
PAT Authentication 
 
- 

| Hyper Configuration requires you to provide a path to the hyperd executable file. It is not possible to use Hyper Configuration and its operations in CloudHub because CloudHub does not allow executing external code due to security reasons. | 

## See Also

- 
[Use Exchange to Discover Connectors, Templates, and Examples](../../connectors/introduction/intro-use-exchange)
- 
[Salesforce Help](https://help.salesforce.com)