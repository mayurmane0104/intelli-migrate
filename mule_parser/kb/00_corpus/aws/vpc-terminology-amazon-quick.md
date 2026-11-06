# VPC terminology - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/vpc-terminology.html](https://docs.aws.amazon.com/quick/latest/userguide/vpc-terminology.html)

---

The following terminology can be useful when you work with a VPC and Amazon Quick.

A *VPC* is a virtual private cloud, which works like a private network
        to isolate the resources within it. The solution described in these topics uses an AWS
        service called Amazon VPC.

A *route table* contains a set of rules, called *routes, *that are used to determine where network traffic is directed. You
        can view the route table in the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/). The VPC details display the route table that the VPC
        is using. You can also see 

**Route tables**listed in the Amazon VPC console.

A *subnet* is a defined set of network IP addresses that are used to
        increase the security and efficiency of network communications. You can think of them like
        postal codes, used for routing packages from one location to another. The
            **Subnets** list in the Amazon VPC console displays subnet IDs and also
        their associated VPC IDs, route tables, and network ACLs. You need to provide at least two
        subnets in different availability zones to create a VPC connection.

A *network interface* represents a virtual network card. The network
        interface automatically created by Amazon Quick is called a *Amazon Quick network
            interface.* Each network interface in a VPC connection is configured based on
        the subnet it's attached to. You can view your Amazon Quick network interfaces in the
        Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/). The network interface displays its network
        interface ID, subnet ID, VPC ID, security group, and the Availability Zone that it exists
        in. You can click on the security group name to see its group ID and its inbound and
        outbound rules. The term 

*network interface*in the following sections always means elastic network interface.

A *security group* is a set of rules that controls the
        network access to the resources it is associated with. Access is permitted only to and from
        the components defined in the security group's inbound and outbound rules. If no rules
        are defined, the security group prevents all access. You can view security groups from
        several different consoles, depending on which resource that a particular security group
        applies to. You can see all the security groups and their settings in one place in the VPC
        console. For the Amazon Quick VPC connection, create a new security group.

*Inbound and outbound rules* define the following:

- 
            The type of traffic to allow, for example `"All TCP"`or`"RDS"`.
- 
            The protocol to allow (TCP, UDP, or ICMP). 
- 
            The traffic source to allow for inbound rules, or the traffic destination to allow for outbound rules. When you work with a VPC and Amazon Quick, you specify the security group ID to use. 
- 
            An optional description. We recommend that you add the word `Amazon Quick`to the description for Amazon Quick VPC rules.

An *internet gateway* is a VPC component that allows communication
        between instances in your VPC and the internet. You don't need an internet gateway to use
        Amazon Quick VPC connections.

A *VPC endpoint* enables you to privately connect your VPC to supported
        AWS services without using public IP addresses. You don't need to set up a VPC endpoint to
        use Amazon Quick VPC connections.