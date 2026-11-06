# Amazon EC2 Connector 3.0 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/amazon-ec2-connector/latest](https://docs.mulesoft.com/amazon-ec2-connector/latest)

---

# Amazon EC2 Connector 3.0

Anypoint Connector for Amazon EC2 (Amazon EC2 Connector) provides connectivity to the Amazon Elastic Compute Cloud (Amazon EC2) API, enabling you to interface with Amazon EC2 to launch as many or as few virtual servers as you need, configure security and networking, and manage storage.

## Before You Begin

To use Amazon EC2 Connector, you must be familiar with:

- 
The Amazon EC2 API 
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
AWS Identity and Access Management (IAM) user account credentials 
- 
A secret access key to IAM 
- 
Access to EC2 via the AWS cloud 

## Common Use Cases for the Connector

Common use cases for the connector include:

- 
Creating an EBS volume to attach to an instance in the same availability zone 
- 
Attaching an EBS volume to a running or stopped Amazon EC2 instance 
- 
Restarting an Amazon EBS-backed AMI that you’ve previously stopped 
- 
Stopping an Amazon EC2 instance 

## Audience

- 
New users, read: - 
[Using Anypoint Studio to Configure the Connector](amazon-ec2-connector-studio)to create your Mule app
- 
[Examples](amazon-ec2-connector-examples), which provide one or more use cases for the connector
 
- 
- 
Advanced users, read: 
- 
[Examples](amazon-ec2-connector-examples), which provides one or more use cases for the connector
 

## Authentication Types

Amazon EC2 Connector connections use the following authentication types:

- 
Basic Uses a session token provided by Amazon STS to connect to Amazon EC2 
- 
Role Uses the Amazon role ARN that uniquely identifies the role to allow cross-account access 

For information about configuring these authentication types, see [Using Anypoint Studio to Configure Amazon EC2](amazon-ec2-connector-studio).

## Next Step

After you complete the prerequisites and try the examples, you are ready to create your own app and configure the connector using [Using Anypoint Studio to Configure Amazon EC2 Connector](amazon-ec2-connector-studio).

## See Also

- 
[Use Exchange to Discover Connectors, Templates, and Examples](../../connectors/introduction/intro-use-exchange)
- 
[Salesforce Help](https://help.salesforce.com)