# Setting up a VPC to use with Amazon Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/vpc-setup-for-quicksight.html](https://docs.aws.amazon.com/quick/latest/userguide/vpc-setup-for-quicksight.html)

---

| Applies
                    to:Enterprise Edition | 

| Intended audience: System administrators | 

To set up a VPC to use with Amazon Quick Enterprise edition, you need access to Amazon VPC and
        Amazon EC2. You also need access to each AWS database service that you plan to add to
        Quick. You can use the console, or you can use the AWS Command Line Interface (AWS CLI). For more
        information about the CLI, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/). To work
        with the CLI, go to [https://aws.amazon.com/cli/](https://aws.amazon.com/cli/).

Before you begin to set up your VPC connection in Amazon Quick, make sure that you understand the components of a VPC deployment. As part of that, familiarize yourself with the VPC's subnets and security groups in relation to the destinations (databases) that you want to reach from Amazon Quick. To set up a successful VPC connection, make sure that the following components work together to allow network traffic to pass between Amazon Quick and your data source:

- 
            The Amazon VPC service 
- 
            The subnets that your data source is using 
- 
            The Amazon Quick elastic network interfaces and the subnets they use 
- 
            The route table 
- 
            Inbound and outbound rules for these security groups: - 
                    Security group for your VPC. We recommend you create a new security group to isolate the rules on the VPC security group from the rules on the Amazon Quick network interface's security group). 
- 
                    Security group attached to the Amazon Quick network interface. 
- 
                    Security group attached to the database server (for each database server that you want to use). 
 
- 
                    
- 
            (Optional) Amazon Route 53 Resolver inbound endpoints for private DNS resolution. 

In the following topics, you can find the network components that are involved. You can
        also find descriptions of their roles in the network configuration of your VPC and your
        Amazon Quick VPC connection. The network interface for Amazon Quick that is automatically
        created during setup is called the *Amazon Quick network
            interface** (QNI).*

If your VPC is already completely configured, skip to the next section, [Finding information to connect to a VPC](https://docs.aws.amazon.com/quicksight/latest/user/vpc-finding-setup-information.html).