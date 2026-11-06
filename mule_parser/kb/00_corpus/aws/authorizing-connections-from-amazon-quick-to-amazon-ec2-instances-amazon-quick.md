# Authorizing connections from Amazon Quick to Amazon EC2 instances - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/enabling-access-ec2.html](https://docs.aws.amazon.com/quick/latest/userguide/enabling-access-ec2.html)

---

| Applies
                    to:Enterprise Edition and Standard Edition | 

| Intended audience: System administrators | 

For Amazon Quick Sight to connect to an Amazon EC2 instance, you must create a new security group for that instance. This security group contains an inbound rule authorizing access from the appropriate IP address range for the Quick servers in that AWS Region.

To modify the security groups for these Amazon EC2 instances, you must have AWS credentials that permit you to access to the instances.

Enabling connection from Quick servers to your instance is just one of
            several prerequisites for creating a data set based on an AWS database data source.
            For more information about what is required, see [Creating a dataset from a database](https://docs.aws.amazon.com/quicksight/latest/user/create-a-database-data-set.html).

###### To enable Amazon Quick access to an Amazon EC2 instance

-  Sign in to the AWS Management Console and open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).
- 
                If your EC2 instance is in a VPC, choose the instance to view the instance details pane. Find its VPC ID and note that ID for later use. 
- 
                Choose **Security Groups**in the**NETWORK & SECURITY**section of the navigation pane. Then choose**Create Security Group**, as shown following.
- 
                Enter the security group information as follows: - 
                        For **Security group name**, enter`Amazon-QuickSight-access`.
- 
                        For **Description**, enter`Amazon-QuickSight-access`.
- 
                        For **VPC**, choose the VPC ID that you noted in step 2 if your Amazon EC2 instance is in a VPC. Otherwise, choose**No VPC**.
 
- 
                        
- 
                Choose **Add Rule**on the**Inbound**tab.
- 
                Create a new rule with the following values: - 
                        For **Type**, choose**Custom TCP Rule**.
- 
                        For **Protocol**, choose**TCP**.
- 
                        (Optional) For **Port Range**, enter the port number used by the instance on this Amazon EC2 instance to which you are providing access.
- 
                        For **Source**, enter the CIDR address block for the AWS Region where you plan to use Amazon Quick. For example, here is the CIDR address block for Europe (Ireland):`52.210.255.224/27`. For more information on the IP address ranges for Amazon Quick in supported AWS Regions, see[AWS Regions, websites, IP address ranges, and endpoints](https://docs.aws.amazon.com/quicksight/latest/user/regions.html).###### NoteIf you have activated Amazon Quick in multiple AWS Regions, you can create inbound rules for each Amazon Quick endpoint CIDR. Doing this allows Amazon Quick to have access to the Amazon RDS DB instance from any AWS Region defined in the inbound rules. An Amazon Quick user or administrator who uses Amazon Quick in multiple AWS Regions is treated as a single user. In other words, even if you are using Amazon Quick in every AWS Region, both your Amazon Quick account and your users are global. 
 
- 
                        
- 
                Choose **Create**.
- 
                Choose **Instances**in the**INSTANCES**section of the navigation pane, and then choose the instance that you want to enable access to.
- 
                Choose **Actions**, then**Networking**, and then**Change Security Groups**.
- 
                In **Change Security Groups**, choose the**Amazon-QuickSight-access**security group.Then choose **Assign Security Groups**, as shown following.