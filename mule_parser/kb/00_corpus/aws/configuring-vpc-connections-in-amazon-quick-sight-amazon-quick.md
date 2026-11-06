# Configuring VPC connections in Amazon Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/working-with-aws-vpc.html](https://docs.aws.amazon.com/quick/latest/userguide/working-with-aws-vpc.html)

---

| Applies
                    to:Enterprise Edition | 

| Intended audience: System administrators and Amazon Quick administrators | 

###### Note

**If you're a Amazon Quick system administrator**
                configuring a VPC connection to Amazon Quick Sight, this section is for you. Amazon Quick
                knowledge bases currently don't support VPC integrations.

Quick Enterprise edition is fully integrated with the Amazon VPC service. A
                *VPC* based on this service closely resembles a
            traditional network that you operate in your own data center. It enables you to secure
            and isolate traffic between resources. You define and control the network elements to
            suit your requirements, while still getting the benefit of cloud networking and the
            scalable infrastructure of AWS. 

By creating a VPC connection in Amazon Quick, you're adding elastic network interfaces in your VPC. These network interfaces allow Amazon Quick to exchange network traffic with a network instance within your VPC. You can provide all of the standard security controls for this network traffic, as you do with other traffic in your VPC. Route tables, network access control lists (ACLs), subnets, and security groups settings all apply to network traffic to and from Amazon Quick in the same way that they apply to traffic between other instances in your VPC.

When you register a VPC connection with Amazon Quick, you can securely connect to data that's available only in your VPC, for example:

- 
                Data you can reach by IP address 
- 
                Data that isn't available on the public internet 
- 
                Private databases 
- 
                On-premises data This works if you set up connectivity between the VPC and your on-premises network. For example, you might set up connectivity with AWS Direct Connect, a virtual private network (VPN), or a proxy. 

After you connect to the data, you can use it to create data analyses and publish secure data dashboards.

To further increase security, consider logging data access operations with AWS CloudTrail,
            as described in [Logging Amazon Quick information with CloudTrail](https://docs.aws.amazon.com/quicksight/latest/user/logging-using-cloudtrail.html). You can even create
            a dashboard to help you analyze your CloudTrail logs. By combining Amazon Quick logs with logs
            from your other AWS services, you can get a fuller view of how your data is being
            used.

You don't need to be a networking expert to connect and use a VPC with Amazon Quick, because Amazon Quick provides a user interface for adding your network information. However, the person who gathers the information that you need for setup should have some understanding of networking concepts and using VPCs. This person also needs read-only access to the services. If network changes are required, we recommend that you don't make changes to your networking configuration without expert assistance.

To use a command line interface to access your VPC, you can use the AWS Command Line Interface (AWS CLI).
            For more information on using the AWS CLI, see the [AWS CLI User Guide](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).