# Security groups: inbound and outbound rules - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/vpc-security-groups.html](https://docs.aws.amazon.com/quick/latest/userguide/vpc-security-groups.html)

---

A *security group* acts as a virtual firewall for
            your instance to control inbound and outbound traffic. For each security group, you add
            rules that control the inbound traffic to instances, and a separate set of rules that
            control the outbound traffic.

For your VPC connection, create a new security group with the description
                `QuickSight-VPC`. This security group must allow all inbound TCP traffic
            from the security groups of the data destinations that you want to reach. The following
            example creates a new security group in the VPC and returns the ID of the new security
            group.

```
aws ec2 create-security-group \
--group-name quicksight-vpc \
--description "QuickSight-VPC" \
--vpc-id 
```
`vpc-0daeb67adda59e0cd`
###### Important

Network configuration is sufficiently complex that we strongly recommend that you create a new security group for use with Amazon Quick. It also makes it easier for AWS Support to help you if you need to contact them. Creating a new group isn't absolutely required. However, the following topics are based on the assumption that you follow this recommendation.

To enable Quick to successfully connect to an instance in your VPC, configure your security group rules to allow traffic between the Amazon Quick network interface and the instance that contains your data. To do this, configure the security group attached to your database's instance inbound rules to allow the following traffic:

- 
                From the port that Amazon Quick is connecting to 
- 
                From one of the following options: - 
                        The security group ID that's associated with Amazon Quick network interface (recommended) or 
- 
                        The private IP address of the Amazon Quick network interface 
 
- 
                        

For more information, see [Security
                groups for your VPC](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_SecurityGroups.html) and [VPCs and
                subnets](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html) in the *Amazon VPC User Guide.*
        

Use the topics listed below to learn more about inbound and outbound rules.

## Inbound rules

            ###### Important

The following section applies to your VPC connection if the connection was created before April 27, 2023.

When you create a security group, it has no inbound rules. No inbound traffic originating from another host to your instance is allowed until you add inbound rules to the security group.

The security group attached to the Amazon Quick network interface behaves
                differently than most security groups, because it isn't stateful. Other security
                groups are usually *stateful*. This means that, after they
                establish an outbound connection to a resource's security group, they automatically
                allow return traffic. In contrast, the Amazon Quick network interface security group
                doesn't automatically allow return traffic. Because of this, adding an egress rule
                to the Amazon Quick network interface security group doesn't work. To make it work
                for the Amazon Quick network interface security group, make sure to add an inbound
                rule that explicitly authorizes the return traffic from the database host.

The inbound rule in your security group must allow traffic on all ports. It needs to do this because the destination port number of any inbound return packets is set to a randomly allocated port number.

To restrict Amazon Quick to connect only to certain instances, you can specify the security group ID (recommended) or private IP address of the instances that you want to allow. In either case, your security group inbound rule still needs to allow traffic on all ports (0–65535).

To allow Amazon Quick to connect to any instance in the VPC, you can configure the Amazon Quick network interface security group. In this case, give it an inbound rule to allow traffic on 0.0.0.0/0 on all ports (0–65535). The security group used by the Amazon Quick network interface should be different than the security groups used for your databases. We recommend that you use separate security groups for VPC connection.

###### Important

If you are using a long-standing Amazon RDS DB instance, check your configuration to see if you're using a DB security group. DB security groups are used with DB instances that are not in a VPC and are on the EC2-Classic platform.

If this is your configuration, and you aren't moving your DB instance into the
                    VPC for use with Amazon Quick, make sure to update your DB security group's
                    inbound rules. Update them to allow inbound traffic from the VPC security group
                    that you're using for Amazon Quick. For more information, see [Controlling Access with Security Groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html) in the
                        *Amazon RDS User Guide.*
                

## Outbound rules

            ###### Important

The following section applies to your VPC connection if the connection was created before April 27, 2023.

By default, a security group includes an outbound rule that allows all outbound traffic. We recommend that you remove this default rule and add outbound rules that allow specific outbound traffic only.

###### Warning

Do not configure the security group on the Amazon Quick network interface with
                    an outbound rule to allow traffic on all ports. For information on key
                    considerations and recommendations for managing network egress traffic from
                    VPCs, see [Security best practices for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html) in the
                        *Amazon VPC User Guide.*
                    

The security group attached to Amazon Quick network interface should have outbound rules that allow traffic to each of the database instances in your VPC that you want Amazon Quick to connect to. To restrict Amazon Quick to connect only to certain instances, specify the security group ID (recommended) or the private IP address of the instances to allow. You set this up, along with the appropriate port numbers for your instances (the port that the instances are listening on), in the outbound rule.

The VPC security group must also allow outbound traffic to the security groups of the data destinations, specifically on the port or ports that the database is listening on.