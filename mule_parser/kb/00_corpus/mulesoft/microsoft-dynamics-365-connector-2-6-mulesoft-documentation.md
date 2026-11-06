# Microsoft Dynamics 365 Connector 2.6 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/microsoft-dynamics-365-connector/latest](https://docs.mulesoft.com/microsoft-dynamics-365-connector/latest)

---

# Microsoft Dynamics 365 Connector 2.6

Anypoint Connector for Microsoft Dynamics 365 (Microsoft Dynamics 365 Connector) enables integration with the Microsoft Dynamics 365 Cloud API.

This connector enables you to perform operations to:

- 
Authorize or unauthorize server access 
- 
Create, update, and delete entities 
- 
Retrieve a single entity or query multiple entities 
- 
Associate and disassociate entities 
- 
Execute actions 

Release Notes: [Microsoft Dynamics 365 Connector Release Notes](../../release-notes/connector/microsoft-dynamics-365-connector-release-notes-mule-4)

Exchange: [Microsoft Dynamics 365 Connector](https://www.mulesoft.com/exchange/com.mulesoft.connectors/mule-microsoft-dynamics365-connector/)

## Before You Begin

Before creating an app, you must have access to the Microsoft Dynamics 365 target resource and Anypoint Platform. You also must understand how to create a Mule app using Anypoint Studio.

Obtain a client ID and secret for your app by logging in to the Microsoft Azure Active Directory portal at portal.azure.com.

Before starting:

You need access to a Microsoft Dynamics 365 instance for which Azure Active Directory is the Identity Provider that provides access to an application.

## Common Use Cases for the Connector

Common use cases for Microsoft Dynamics 365 Connector include:

- 
**Entity Management**Create, retrieve, update, or delete entities: - 
Create an account with attributes that associate an account with a contact 
- 
Create an empty contact entity 
- 
Create an empty opportunity entity 
- 
Create multiple entities of the same type in a single batch request 
- 
Delete an entity by type 
- 
Disassociate keys based on an identity ID 
- 
Retrieve an entity by type 
- 
Retrieve multiple entities using a URL request 
- 
Retrieve multiple entities using DataSense query language 
- 
Update an account with attributes 
- 
Update multiple entities of the same type in a single batch request 
 
- 
- 
**Automated Business Processes**Automate businesses processes across sales, marketing, social media, and customer service departments with seamless communication to keep your enterprise connected. 
- 
**Data Synchronization**Perform data migration, social data synchronization, and lead and contact data sharing. 

For examples of these use cases, refer to [Microsoft Dynamics 365 Connector Examples](microsoft-dynamics-365-connector-examples).

## Audience

- 
New users, read: - 
[Using Anypoint Studio to Configure the Connector](microsoft-dynamics-365-connector-studio)to create your Mule app
- 
[Examples](microsoft-dynamics-365-connector-examples), which provides an example use case for the connector
 
- 
- 
Advanced users, read: 
- 
[Examples](microsoft-dynamics-365-connector-examples), which provides an example use case for the connector
 

## Authentication Types

Microsoft Dynamics 365 Connector uses the following authentication types:

- 
**Connection**(OAuth 2.0)Connects to servers that manage authorization and token access 
- 
**OAuth 2.0 client credentials**Uses a client ID and client secret to authenticate the connection to the server 
- 
**OAuth 2.0 username and password**Uses a username and password to authenticate the connection to the server 

## Terminology

- Actions
- 
Operations that allow side effects, such as data modification, cannot be further composed to avoid non-deterministic behavior. 
- Complex types
- 
Keyless structured types consisting of a set of properties. Complex types are commonly used as property values in model entities, or as parameters or return values for operations. 
- Entities
- 
Instances of entity types, for example, an account or an opportunity. 
- Entity set
- 
Collections of entities, for example, an account is an entity set containing account entities. An entity’s key uniquely identifies the entity within an entity set. 
- Entity types
- 
Structured types with a key. Entity types define the properties and relationships of an entity, and may derive by single inheritance from other entity types. 
- Enumeration types or enum types
- 
Primitive types whose values are constants with underlying integer values. 
- Functions
- 
Operations that do not have side effects and may support further composition, for example, with additional filter operations, functions, or an action. 

## Using Exchange Templates and Examples

[Anypoint Exchange](https://www.mulesoft.com/exchange/) provides templates
that you can use as starting points for your apps and examples that illustrate a complete solution.

## Next Step

After you have met the prerequisites and experimented with templates and examples, you are ready to create an app with [Anypoint Studio](microsoft-dynamics-365-connector-studio).

## See Also

- 
[Salesforce Help](https://help.salesforce.com)