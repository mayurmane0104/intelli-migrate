# Configuring the VPC connection with the Amazon Quick CLI - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/vpc-creating-a-connection-in-quicksight-cli.html](https://docs.aws.amazon.com/quick/latest/userguide/vpc-creating-a-connection-in-quicksight-cli.html)

---

To create a secure private connection to the Amazon VPC service from Quick with the Amazon Quick CLI, use the following procedure:

###### Prerequisites

- 
                Before you begin, make sure that you have the following information available to copy and paste into the **VPC Connection**page. For more information, see[Finding information to connect to a VPC](https://docs.aws.amazon.com/quicksight/latest/user/vpc-finding-setup-information.html).- 
                        AWS Region – The AWS Region where you plan to create a connection to your data source. 
- 
                        VPC ID – The ID of the VPC that contains the data, the subnets, and the security groups that you plan to use. 
- 
                        Execution role– An IAM role that contains a trust policy that allows Amazon Quick to create, update, and delete network infrastructure in your account. This policy is required for all VPC connections. At minimum, the IAM policy needs the following Amazon EC2 permissions: - 
                                `DescribeSecurityGroups`
- 
                                `DescribeSubnets`
- 
                                `CreateNetworkInterface`
- 
                                `DeleteNetworkInterface`
- 
                                `ModifyNetworkInterfaceAttribute`
 The following example shows an IAM policy that you can add to an existing IAM role to create, delete, or modify a VPC connection: - 
            
                
                `{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "ec2:CreateNetworkInterface", "ec2:ModifyNetworkInterfaceAttribute", "ec2:DeleteNetworkInterface", "ec2:DescribeSubnets", "ec2:DescribeSecurityGroups" ], "Resource": "*" } ] }`
 After you add the necessary permissions to an IAM role, attach a trust policy to allow Amazon Quick to configure the VPC connection to your account. The following shows an example trust policy that you can add to an existing IAM role to allow Amazon Quick access to the role: - 
            
                
                `{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "Service": "quicksight.amazonaws.com" }, "Action": "sts:AssumeRole" } ] }`
 
- 
                                
- 
                        Subnet IDs – The IDs of the subnets that the Amazon Quick network interface is using. Each VPC connection needs at least two subnets. 
- 
                        Security group IDs – The IDs of the security groups. Each VPC connection needs at least one security group. 
 
- 
                        

## Using the AWS CLI

            The following example creates a VPC connection.

`aws quicksight create-vpc-connection \ --aws-account-id``123456789012`\ --vpc-connection-id`test`\ --name`test`\ --subnet-ids '["`subnet-12345678`", "`subnet-12345678`"]' \ --security-group-ids '["`sg-12345678`"]' \ --role-arn arn:aws:iam::`123456789012`:role/`test-role`\ --region`us-west-2`

After you create a VPC connection, you can update, delete, or request a summary of the VPC connection.

The following example updates a VPC connection.

`aws quicksight update-vpc-connection \ --aws-account-id``123456789012`\ --vpc-connection-id`test`\ --name`test`\ --subnet-ids '["`subnet-12345678`", "`subnet-12345678`"]' \ --security-group-ids '["`sg-12345678`"]' \ --role-arn arn:aws:iam::`123456789012`:role/`test-role`\ --region`us-west-2`

The following example deletes a VPC connection.

`aws quicksight delete-vpc-connection \ --aws-account-id``123456789012`\ --vpc-connection-id`test`\ --region`us-west-2`

The following example describes a VPC connection.

`aws quicksight describe-vpc-connection \ --aws-account-id``123456789012`\ --vpc-connection-id`test`\ --region`us-west-2`

The following table describes the different **Status** values for
                a network interface that `describe-vpc-connection` returns.

| Status | Description | 
|---|---|
| 
 | The network interface creation is in progress. | 
| 
 | The network interface is available for use. | 
| 
 | The network interface couldn't be created. | 
| 
 | The security group associated with the network inferface is updating. | 
| 
 | The security group associated with the network interface did not update successfully. | 
| 
 | The network interface is in the process of being deleted. | 
| 
 | The network interface is deleted and can no longer be used. | 
| 
 | The network interface deletion failed and can still be used. | 
| 
 | This network interface is scheduled for deletion. | 
| 
 | The elastic interface failed to attach and Amazon Quick was unable to delete the elastic network interface that was created within your account. | 

You can also use the AWS CLI to generate a list of all VPC connections in your Amazon Quick account.

`aws quicksight list-vpc-connections \ --aws-account-id``123456789012`\ --`region us-west-2`