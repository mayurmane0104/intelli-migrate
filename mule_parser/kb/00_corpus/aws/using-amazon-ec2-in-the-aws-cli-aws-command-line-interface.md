# Using Amazon EC2 in the AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2.html)

---

| An introduction to Amazon Elastic Compute Cloud | 
|---|
|  | 

Amazon Elastic Compute Cloud (Amazon EC2) provides highly scalable and flexible virtual computing environments. Amazon EC2 allows you to provision and manage virtual servers, known as Amazon EC2 instances, to meet a wide range of computing needs.

Amazon EC2 instances are virtual machines that can be customized with various configurations of CPU, memory, storage, and networking capabilities. You can choose from a diverse selection of instance types, ranging from lightweight, cost-effective options to powerful, high-performance instances, depending on your application requirements. This flexibility enables you to match your computing needs to optimize performance and cost-efficiency.

Additionally, Amazon EC2 offers a suite of features that empowers you to manage your compute resources effectively. These include the ability to quickly launch new instances, create custom machine images (AMIs) for rapid deployment, and scaling computing capacity up or down as needed.

You can access the features of Amazon EC2 using the AWS Command Line Interface (AWS CLI). To list the AWS CLI commands for Amazon EC2, use the following command.

`aws ec2 help`

Before you run any commands, set your default credentials. For more information, see [Configuring settings for the AWS CLI](./cli-chap-configure.html).

This topic shows short-form examples of AWS CLI commands that perform common tasks for Amazon EC2.

For long-form examples of AWS CLI commands, see [AWS CLI code examples
      repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/aws-cli) on 

*GitHub*.