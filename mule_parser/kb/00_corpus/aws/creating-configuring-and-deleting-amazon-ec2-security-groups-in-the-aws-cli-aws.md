# Creating, configuring, and deleting Amazon EC2 security groups in the AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2-sg.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2-sg.html)

---

You can create a security group for your Amazon Elastic Compute Cloud (Amazon EC2) instances that essentially operates as a firewall, with rules that determine what network traffic can enter and leave.

Use the AWS Command Line Interface (AWS CLI) to create a security group, add rules to existing security groups, and delete security groups.

###### Note

For additional command examples, see the
                [AWS CLI reference
                guide](https://docs.aws.amazon.com/cli/latest/reference/index.html).

###### Topics

## Prerequisites

        To run the `ec2` commands, you need to:

- Install and configure the AWS CLI. For more information, see - [Installing or updating to the latest version of the AWS CLI](./getting-started-install.html)and- [Authentication and access credentials for the AWS CLI](./cli-chap-authentication.html).
- 
                Set your IAM permissions to allow for Amazon EC2 access. For more information about IAM permissions for Amazon EC2, see [IAM policies for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html)in the*Amazon EC2 User Guide*.

## Create a security group

    You can create security groups associated with virtual private clouds (VPCs) .

The following
                        [aws ec2 create-security-group](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-security-group.html)

`$``aws ec2 create-security-group --group-name``my-sg`--description "`My security group`" --vpc-id`vpc-1a2b3c4d``{ "GroupId": "sg-903004f8" }`

To view the initial information for a security group, run the
                        [aws ec2 describe-security-groups](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-security-groups.html)`vpc-id`, not its name.

`$``aws ec2 describe-security-groups --group-ids``sg-903004f8``{ "SecurityGroups": [ { "IpPermissionsEgress": [ { "IpProtocol": "-1", "IpRanges": [ { "CidrIp": "0.0.0.0/0" } ], "UserIdGroupPairs": [] } ], "Description": "My security group" "IpPermissions": [], "GroupName": "my-sg", "VpcId": "vpc-1a2b3c4d", "OwnerId": "123456789012", "GroupId": "sg-903004f8" } ] }`

## Add rules to your security group

    When you run an Amazon EC2 instance, you must enable rules in the security group to allow incoming network traffic for your means of connecting to the image.

For example, if you're launching a Windows instance, you typically add a rule to allow inbound traffic on TCP port 3389 to support Remote Desktop Protocol (RDP). If you're launching a Linux instance, you typically add a rule to allow inbound traffic on TCP port 22 to support SSH connections.

Use the
                    [aws ec2 authorize-security-group-ingress](https://docs.aws.amazon.com/cli/latest/reference/ec2/authorize-security-group-ingress.html)[CIDR](https://wikipedia.org/wiki/Classless_Inter-Domain_Routing)
            notation.

###### Note

We provide the following service, [https://checkip.global.api.aws/](https://checkip.global.api.aws/), to enable you to determine your public
                IP address. To find other services that can help you identify your IP address, use
                your browser to search for "

*what is my IP address*". If you connect through an ISP or from behind your firewall using a dynamic IP address (through a NAT gateway from a private network), your address can change periodically. In that case, you must find out the range of IP addresses used by client computers.

The following example shows how to add a rule for RDP (TCP port 3389) to an EC2-VPC
                security group with the ID `sg-903004f8` using your IP address.

To start, find your IP address.

`$``curl https://checkip.amazonaws.com``x.x.x.x`

You can then add the IP address to your security group by running the
                        [aws ec2
                    authorize-security-group-ingress](https://docs.aws.amazon.com/cli/latest/reference/ec2/authorize-security-group-ingress.html)

`$``aws ec2 authorize-security-group-ingress --group-id``sg-903004f8`--protocol tcp --port 3389 --cidr`x.x.x.x/x`

The following command adds another rule to enable SSH to instances in the same security group.

`$``aws ec2 authorize-security-group-ingress --group-id``sg-903004f8`--protocol tcp --port 22 --cidr`x.x.x.x/x`

To view the changes to the security group, run the
                        [aws ec2 describe-security-groups](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-security-groups.html)

`$``aws ec2 describe-security-groups --group-ids``sg-903004f8``{ "SecurityGroups": [ { "IpPermissionsEgress": [ { "IpProtocol": "-1", "IpRanges": [ { "CidrIp": "0.0.0.0/0" } ], "UserIdGroupPairs": [] } ], "Description": "My security group" "IpPermissions": [ { "ToPort": 22, "IpProtocol": "tcp", "IpRanges": [ { "CidrIp": "``x.x.x.x/x`" } ] "UserIdGroupPairs": [], "FromPort": 22 } ], "GroupName": "my-sg", "OwnerId": "123456789012", "GroupId": "sg-903004f8" } ] }

## Delete your security group

    To delete a security group, run the
                    [aws
                    ec2 delete-security-group](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-security-group.html)

###### Note

You can't delete a security group if it's currently attached to an environment.

The following command example deletes an EC2-VPC security group.

`$``aws ec2 delete-security-group --group-id``sg-903004f8`

## References

        **AWS CLI reference:**

**Other reference:**

- 
                To view and contribute to AWS SDK and AWS CLI code examples, see the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/)on*GitHub*.