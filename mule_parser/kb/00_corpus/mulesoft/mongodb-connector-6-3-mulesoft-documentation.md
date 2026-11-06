# MongoDB Connector 6.3 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mongodb-connector/latest](https://docs.mulesoft.com/mongodb-connector/latest)

---

```
{
  "timeStamp": "2024-06-17T16:44:17.000+01:00"
}
```
json# MongoDB Connector 6.3

Anypoint Connector for MongoDB (MongoDB Connector) is a closed-source connector that provides a connection between the Mule runtime engine (Mule) and third-party software on a MongoDB server.

Release Notes: [MongoDB Connector Release Notes](../../release-notes/connector/mongodb-connector-release-notes-mule-4)

Exchange: [MongoDB Connector](https://www.mulesoft.com/exchange/com.mulesoft.connectors/mule-mongodb-connector/)

## Before You Begin

To use this connector, you must be familiar with MongoDB, Mule runtime engine (Mule), Anypoint Connectors, Anypoint Studio, elements in a Mule flow, and global elements.

Before creating an app, you must have access to the MongoDB target resource and Anypoint Platform. You must also understand how to create a Mule app using Anypoint Studio.

To use the this connector, you need:

- 
A MongoDB instance 
- 
A set of valid credentials, including the required MongoDB endpoints that point to your instance 

## Common Use Cases for the Connector

Common use cases for MongoDB Connector include:

- 
**Single View of Data**Create a single view of your most important data and aggregate your siloed data from multiple enterprise systems, transform the data, and write the data to MongoDB. For example, you can import data into a CSV format from a local directory into MongoDB. 
- 
**Mainframe Offloading**Mirror or synchronize your operational data from mainframes into MongoDB to offload workloads from your mainframes while enabling the ability to meet your customer where they are. 
- 
**Real-time Analytics**Leverage MongoDB’s rich query language to make real-time decisions on shipping, inventory, and pricing, and analyze any data using documents in MongoDB. 
- 
**Personalization**Create personalized omnichannel retail experiences by collecting and synchronizing data across your retail channels and your backend systems into MongoDB. 

For examples of these use cases, refer to [MongoDB Connector Examples](mongodb-connector-examples).

## Authentication

This connector does not validate all possible authentication types.

## Exchange Example

[Anypoint Exchange](https://www.mulesoft.com/exchange/org.mule.examples/importing-a-CSV-file-into-Mongo-DB/) has an example that shows how to import data in a CSV format from a local directory into MongoDB.

## Important Date Handling Considerations

When using MongoDB Connector, consider the following date-handling behavior:

- 
**Automatic conversion to UTC**MongoDB Connector converts dates (whether sent to or retrieved from MongoDB) to UTC before storage for consistent date handling in distributed environments. 
- 
**ISO 8601 format**Dates (whether they are sent to or retrieved from MongoDB) in JSON documents are transformed to the ISO 8601 format. Additionally, any String values in JSON documents that match the ISO 8601 format are automatically transformed and stored as Date types in MongoDB. This change ensures more consistent and standardized date handling in a distributed environment. 
- 
**Millisecond truncation**Dates (whether sent to or retrieved from MongoDB) that include milliseconds with a value of `.000`are not shown in connector output.

Here is an example of date handling in a Mule app:

Input:

Mule 4:

```
{
  "timeStamp": "2024-06-17T15:44:17+00:00"
}
```
jsonBecause of these changes in date handling, it is important to:

- 
**Review flows involving dates**If your Mule apps rely on specific timezones of dates stored in MongoDB, you must review and possibly adjust flows to correctly handle the UTC conversion. 
- 
**Test thoroughly**Conduct thorough testing in a controlled environment to ensure that the changes in date handling do not negatively impact the expected behavior of the Mule app. 
- 
**Document the behavioral differences**Review these date-handling details to ensure correct behavior in your application. 

## Next Steps

After you complete the prerequisites and experiment with the example, you are ready to create an app with [Studio](mongodb-connector-studio).

## See Also

- 
[Salesforce Help](https://help.salesforce.com)