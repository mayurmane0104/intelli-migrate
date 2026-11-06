# Amazon S3 Connector 8.0 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/amazon-s3-connector/latest](https://docs.mulesoft.com/amazon-s3-connector/latest)

---

# Amazon S3 Connector 8.0

Anypoint Connector for Amazon S3 (Amazon S3 Connector) provides connectivity to the Amazon S3 API, enabling you to interface with Amazon S3 to store objects, download and use data with other AWS services, and build applications that require internet storage.

Instant access to the Amazon S3 API enables seamless integrations between Amazon S3 and other databases, CMS applications such as Drupal, and CRM applications such as Salesforce. Use Amazon S3 to store and retrieve any amount of data at any time, from anywhere on the web. You can accomplish these tasks by using the simple and intuitive web interface of the AWS Management Console.

AWS SDK for Java provides a Java API for AWS infrastructure services. The Amazon S3 connector is built using the SDK for Java.

For compatibility information and fixed issues, see the [Amazon S3 Connector Release Notes](../../release-notes/connector/amazon-s3-connector-release-notes-mule-4).

For a major release, see [Upgrading and Migrating](amazon-s3-connector-upgrade-migrate).

## About Connectors

Anypoint connectors are Mule runtime engine extensions that enable you to connect to APIs and resources on external systems, such as Salesforce, Amazon S3, ServiceNow, and Twitter.

## Before You Begin

To use this connector, you must be familiar with:

- 
The Amazon S3 API 
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
Credentials to access the Amazon S3 target resource 
- 
Anypoint Platform 
- 
Anypoint Studio or Anypoint Code Builder 
- 
Amazon Web Services 
- 
AWS Identity and Access Management (IAM) credentials 

| For the Amazon S3 operations to work, you need to enable or update the subset of the overall list of actions in the Amazon S3 bucket to specify that the AWS account has access these actions. | 

## Common Use Cases for the Connector

Common use cases for Amazon S3 Connector include:

- 
**Storage Service**Store, access, download, retrieve, or display data. For example, you can store an image from a URL in Amazon S3 and then retrieve and display the image, or create an image link in Amazon S3 and then update the status and image link on Twitter. 
- 
**App-Building with Native Cloud-Based Storage**Connect your applications to scalable Amazon S3 buckets and build applications that require internet storage. 
- 
**Data Backup and Archive**Create seamless integrations between Amazon S3 and other databases, CMS applications such as Drupal, CRM applications such as Salesforce, ERP systems, EDI systems, or fulfillment systems, and archive necessary data. 
- 
**Business Intelligence**Drive business intelligence and optimize operational outcomes by leveraging Amazon S3 as a data lake and extract valuable insights using query-in-place, analytics, and machine learning tools. 

For examples of these use cases, refer to [Amazon S3 Connector Examples](amazon-s3-connector-examples).

## Authentication Types

Amazon S3 connections use the following authentication type:

- 
Connection (S3) Uses the S3 connection type, which covers both the Basic and Role connections. 

For information about configuring this authentication type, see [Using Anypoint Studio to Configure Amazon S3](amazon-s3-connector-studio).

## Next Step

After you complete the prerequisites, you are ready to create your own app and configure the connector using [Anypoint Studio](amazon-s3-connector-studio).

## See Also

- 
[Use Exchange to Discover Connectors, Templates, and Examples](../../connectors/introduction/intro-use-exchange)
- 
[Salesforce Help](https://help.salesforce.com)