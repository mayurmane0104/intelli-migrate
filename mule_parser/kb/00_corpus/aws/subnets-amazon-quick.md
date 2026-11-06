# Subnets - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/vpc-subnets.html](https://docs.aws.amazon.com/quick/latest/userguide/vpc-subnets.html)

---

A *subnet* is a range of IP addresses in your VPC.
            You need to provide at least two subnets to create a VPC connection. Each subnet must
            belong a different availability zone. You can attach AWS resources, such as Amazon EC2
            instances and Amazon RDS DB instances, to subnets. You can create subnets to group instances
            together according to your security and operational needs.

For Amazon Quick to connect to your database, the network needs to route traffic to
            the data sources that you want to reach from one of the subnets used by the Amazon Quick
            network interface. Amazon Quick determines which subnet to route traffic through on the
            backend. If the availability zone that the subnet is attached to experiences an outage,
            Amazon Quick reroutes the traffic to one of the other subnets that are configured in the
            VPC connection. If the data sources are on different subnets, make sure that there is a
            route from the Amazon Quick network interface to your database instance. By default,
            each subnet in a VPC is associated with one main route table and can reach the other
            subnets. For more information, see [VPC and Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html)
            and [Network ACLs](https://docs.aws.amazon.com/vpc//latest/userguide/vpc-connection-network-acls.html) in the *Amazon VPC User Guide.*

If you use Amazon RDS, DB instances are associated with a subnet group that you can view
            either in the Amazon RDS console ([https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/)) or in the VPC console. For troubleshooting
            connectivity to Amazon RDS, see the AWS Support article 

[How can I troubleshoot connectivity to an Amazon RDS instance that uses a public or private subnet of a VPC?](https://aws.amazon.com/premiumsupport/knowledge-center/rds-connectivity-instance-subnet-vpc/)