# Allowing autodiscovery of AWS resources - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/autodiscover-aws-data-sources.html](https://docs.aws.amazon.com/quick/latest/userguide/autodiscover-aws-data-sources.html)

---

| Applies
                    to:Enterprise Edition and Standard Edition | 

| Intended audience: System administrators | 

Each AWS service that you access from Amazon Quick needs to allow traffic from Quick. Instead of opening each service console separately to add permissions, a Quick administrator can do this in the administration screen. Before you begin, make sure that you have addressed the following prerequisites.

If you choose to enable autodiscovery of AWS resources for your Quick account, Quick creates an AWS Identity and Access Management (IAM) role in your AWS account. This IAM role grants your account permission to identify and retrieve data from your AWS data sources.

Because AWS limits the number of IAM roles that you can create, make sure that you have at least one free role. You need this role for Amazon Quick to use if you want Amazon Quick to autodiscover your AWS resources.

You can have Amazon Quick autodiscover Amazon RDS DB instances or Amazon Redshift clusters that are associated with your AWS account. These resources must be located in the same AWS Region as your Amazon Quick account.

If you choose to enable autodiscovery, choose one of the following options to make the AWS resource accessible:

- 
            For Amazon RDS DB instances that you created in a default VPC and didn't make private, or that aren't in a VPC (EC2-Classic instances), see [Authorizing connections from Amazon Quick to Amazon RDS instances](https://docs.aws.amazon.com/quicksight/latest/user/enabling-access-rds.html). In this topic, you can find information on creating a security group to allow connections from Amazon Quick servers.
- 
            For Amazon Redshift clusters that you created in a default VPC and didn't choose to make private, or that aren't in a VPC (that is, EC2-Classic instances), see [Authorizing connections from Amazon Quick to Amazon Redshift clusters](https://docs.aws.amazon.com/quicksight/latest/user/enabling-access-redshift.html). In this topic, you can find information on creating a security group to allow connections from Amazon Quick servers.
- 
            For an Amazon RDS DB instance or Amazon Redshift cluster that is in a nondefault VPC, see [Authorizing connections from Amazon Quick to Amazon RDS instances](https://docs.aws.amazon.com/quicksight/latest/user/enabling-access-rds.html)or[Authorizing connections from Amazon Quick to Amazon Redshift clusters](https://docs.aws.amazon.com/quicksight/latest/user/enabling-access-redshift.html). In these topics, you can find information on first creating a security group to allow connections from Amazon Quick servers. In addition, you can find information on then verifying that the VPC meets the requirements described in[Network configuration for an AWS instance in a nondefault VPC](https://docs.aws.amazon.com/quicksight/latest/user/configure-access.html#network-configuration-aws-nondefault-vpc).
- 
            If you don't use a private VPC, set up the Amazon RDS instance to allow connections from the Amazon Quick Region's public IP address. 

Enabling autodiscovery is the easiest way to make this data available in Amazon Quick. You can still manually create data connections whether or not you enable autodiscovery.