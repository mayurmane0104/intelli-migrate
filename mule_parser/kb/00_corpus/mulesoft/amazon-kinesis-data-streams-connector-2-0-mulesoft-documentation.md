# Amazon Kinesis Data Streams Connector 2.0 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/amazon-kinesis-connector/latest](https://docs.mulesoft.com/amazon-kinesis-connector/latest)

---

# Amazon Kinesis Data Streams Connector 2.0

Anypoint Connector for Amazon Kinesis Data Streams (Amazon Kinesis Data Streams Connector) provides access to standard Amazon Kinesis Data Stream operations using Anypoint Platform.

Amazon Kinesis is a streaming solution built by Amazon AWS to collect and process large streams of data records in real time. To learn more, see the Amazon Kinesis official documentation.

For compatibility information and fixed issues, see the Amazon Kinesis Data Streams Release Notes.

| Amazon Kinesis Data Streams Connector doesn’t support Windows because it uses the Kinesis Producer Library (KPL), which deprecated Windows support starting in version 0.14.0. | 

## Before You Begin

To use this connector, you must be familiar with:

- 
The Amazon Kinesis Data Streams API 
- 
Anypoint Connectors 
- 
Mule runtime engine (Mule) 
- 
Elements and global elements in a Mule flow 
- 
Creating a Mule app using Anypoint Studio or Anypoint Code Builder 

Before creating an app, you must have:

- 
AWS Identity and Access Management (IAM) Access Key credentials with access rights to the Kinesis, DynamoDB, and CloudWatch services. You can find the required permissions [here](https://docs.aws.amazon.com/streams/latest/dev/tutorial-stock-data-kplkcl-iam.html).
- 
Access to the Amazon Kinesis target resource 
- 
Anypoint Studio or Anypoint Code Builder 

## Common Use Cases for the Connector

Common use cases for Kinesis Data Streams connector include the following:

- 
Troubleshooting Collect log and event data from sources such as servers, desktops, and mobile devices. Then continuously process the data, generate metrics, power live dashboards, and put the aggregated data into data stores such as Amazon S3. 
- 
Real-time analytics Run real-time analytics on high-frequency event data such as sensor data or social media data collected by Amazon Kinesis Data Streams. These analytics enable you to gain insights from your data at a frequency of minutes instead of a frequency of hours or days. 
- 
Mobile data capture Have your mobile applications push data to Amazon Kinesis data streams from hundreds of thousands of devices, making the data available to you as soon as it is produced on the mobile devices. 

For examples, see [Examples](amazon-kinesis-connector-examples).

## Audience

- 
New users, read: - 
[Using Anypoint Studio to Configure the Connector](amazon-kinesis-connector-studio)to create your Mule app
- 
[Examples](amazon-kinesis-connector-examples), which provide one or more use cases for the connector
 
- 
- 
Advanced users, read: 
- 
[Examples](amazon-kinesis-connector-examples), which provides one or more use cases for the connector
 

## Authentication Types

Amazon Kinesis Data Streams Connector supports Access Key authentication. With this type of authentication, the connector authenticates to AWS by using an access key, secret key, and optionally, a role.

For information about configuring authentication, see [Using Anypoint Studio to Configure Amazon Kinesis Data Streams](amazon-kinesis-connector-studio).

## Using Exchange Templates and Examples

[Anypoint Exchange](https://www.mulesoft.com/exchange/) provides templates
that you can use as starting points for your apps and examples that illustrate a complete solution.

## Next Step

After you complete the prerequisites and try the templates and examples, you are ready to create your own app and configure the connector using [Anypoint Studio](amazon-kinesis-connector-studio).

## See Also

- 
[Use Exchange to Discover Connectors, Templates, and Examples](../../connectors/introduction/intro-use-exchange)
- 
[Salesforce Help](https://help.salesforce.com)