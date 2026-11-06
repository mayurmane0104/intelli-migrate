# Finding information to connect to a VPC - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/vpc-finding-setup-information.html](https://docs.aws.amazon.com/quick/latest/userguide/vpc-finding-setup-information.html)

---

| Applies
                    to:Enterprise Edition | 

| Intended audience: System administrators | 

To gather the information to have ready when you create a VPC connection in Amazon Quick Enterprise edition, take the steps listed following.

###### Steps

## Identify the data sources to use

        Start by identifying all the data sources that you want to connect to using Quick. For each of these, note the database's private IP, security group, and subnets. Amazon Quick connects to your data using the private IP. However, you don't need to enter this or the security group or subnet information for the VPC connection. This information helps you identify the other components you need for the Amazon Quick VPC connection.

###### Note

For the connection to your data source to work, make sure that there's a
                traceable route from your data source to the VPC ID. For more details, see [Identify the data sources to use](https://docs.aws.amazon.com/quicksight/latest/user/vpc-finding-setup-information.html). 

## Identify the AWS Region to use

        For the connection to work, the data, the subnets, and the security group must be in the same VPC. Make sure also that you use Quick in the same AWS Region with the VPC.

You can't use Amazon Quick in one AWS Region and expect to connect to a VPC in a different AWS Region.

If your team is already using Amazon Quick, you can see your current AWS Region displayed at the upper right of the Amazon Quick home screen. You can change the AWS Region you're using in Amazon Quick by changing the Region at the upper right of the Amazon Quick home screen. All the people who plan to use the data in the VPC must be using the same AWS Region in Amazon Quick.

###### Note

The AWS Region that displays in the Amazon Quick console doesn't have to match your AWS CLI configuration. Take care not to mistake your current Amazon Quick console settings with the settings that apply in any AWS CLI commands that you run or the settings in other consoles. Changing the current AWS Region in any console doesn't change the Region anywhere except for that page.

For example, let's say you have three tabs open in one browser window. You can have the Amazon Quick console open in one AWS Region, the Amazon VPC console open in a second Region, the Amazon RDS console open in a third Region, and the AWS CLI running in a fourth Region.

## Identify the VPC ID to use

        The VPC ID is assigned when the VPC is created.

**Using the AWS CLI**

The following `describe-vpcs` example retrieves details for all of your
            VPCs.

```
aws ec2 describe-vpcs
```
The following `describe-vpcs` example retrieves details for the specified
            VPC.

```
aws ec2 describe-vpcs \
--vpc-ids vpc-06e4ab6c6cEXAMPLE
```
**Using the Amazon VPC console**

In the VPC console ([https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/)), choose 

**Your VPCs**at left. Choose the VPC-ID that you want to use. The correct one has Availability Zones in your AWS Region and also meets the requirements described in

[Finding information to connect to a VPC](https://docs.aws.amazon.com/quicksight/latest/user/vpc-finding-setup-information.html). Also note the ID of

**Main Route Table**, because you need this to identify related subnets.

###### Tip

In the Amazon VPC console, you can filter by VPC. This option is located at the top left of the console. If you filter by your VPC ID, all the other menus display only the network elements that are in your selected VPC.

## Identify the subnet IDs to use

        To locate the subnet IDs for the subnets used by the VPC, open the VPC console. Locate the VPC you are using, and at least two subnets in different availibility zones. Amazon Quick creates its Amazon Quick elastic network interface (Amazon Quick network interface) for the subnets that you choose. The Amazon Quick network interfaces get created after you save your VPC connection settings, described in the following section.

Your database instances can reside in different subnets. However, make sure you can trace the route from this subnet to any data destinations that you want to reach.

**Using the AWS CLI**

The following example describes all existing subnets.

```
aws ec2 describe-subnets
```
The following `describe-subnets` example uses a filter to retrieve details
            for the subnets of the specified VPC.

```
aws ec2 describe-subnets \
--filters "Name=vpc-id,Values=vpc-06e4ab6c6cEXAMPLE"
```
**Using the Amazon VPC console**

In the VPC console ([https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/)), choose 

**Subnets**at left, and find the correct

**Subnet ID**. Any subnet is correct if your database subnet has a route to the subnet that you choose at this point. In most cases, if you haven't configured the VPC network yourself, all subnets are connected.

## Identify the security group to use

        The security group contains rules that control the inbound and outbound network
            traffic on your data source instances. The security group you are using should have the
            description `"QuickSight-VPC"` to make it easier to identify. 

When you locate the correct security group, copy its **Group ID**
            value.

**Using the AWS CLI**

The following example displays the security groups in a specific AWS Region. It
            displays only the group ID, name, and description. It filters the result to display only
            groups for a specific VPC ID that also have a description of
                `"QuickSight-VPC"`. 

`aws ec2 describe-security-groups \ --region us-west-2 \ --query 'SecurityGroups[*].[GroupId, GroupName, Description]' \ --filters "Name=vpc-id,Values=vpc-06e4ab6c6cEXAMPLE" "Name=description,Values=QuickSight-VPC"`

The following example displays information about the security group with the ID
                `sg-903004f8`. Note that you can't reference a security group for EC2-VPC
            by name.

`aws ec2 describe-security-groups --group-ids sg-903004f8 --region us-west-2`

The following example queries the results to describe VPC the inbound and outbound
            rules of a security group with a specific ID (`sg-903004f8`), in a specific
            AWS Region (`us-west-2`).

```
aws ec2 describe-security-groups \
--region us-west-2 \
--group-ids sg-903004f8 \
--query 'SecurityGroups[*].[GroupId, GroupName, Description, IpPermissions,IpPermissionsEgress]'
```
The following example uses filters to describe VPC security groups that have a
            specific rule that allows SQL Server traffic (port `1433`). The example also
            has a rule that allows traffic from all addresses (`0.0.0.0/0`). The output
            is filtered to display only the group IDs, names, and descriptions of the security
            groups. Security groups must match all filters to be returned in the results. However, a
            single rule doesn't have to match all filters. (EC2-VPC only)

```
aws ec2 describe-security-groups \
--filters Name=ip-permission.from-port,Values=1433 \
Name=ip-permission.to-port,Values=1433 \
Name=ip-permission.cidr,Values='0.0.0.0/0' \
--query 'SecurityGroups[*].[GroupId, GroupName, Description]'
```
**Using the Amazon VPC console**

In the VPC console ([https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/)), choose 

**Security groups**at left, and find the correct group ID. The correct one has your VPC ID on it. It should also have a tag or description that includes the word

`"QuickSight"`.