# What is Amazon VPC? - Amazon Virtual Private Cloud

**Source:** [https://docs.aws.amazon.com/vpc/latest/userguide/index.html](https://docs.aws.amazon.com/vpc/latest/userguide/index.html)

---

[Using service-linked roles for VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-slr.html)

*9 June 2026*

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies. 

 If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the [AWS Cookie Notice](https://aws.amazon.com/legal/cookies/).

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

With Amazon Virtual Private Cloud (Amazon VPC), you can launch AWS resources in a logically isolated virtual network that you've defined. This virtual network closely resembles a traditional network that you'd operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

The following diagram shows an example VPC. The VPC has one subnet in each of the Availability Zones in the Region, EC2 instances in each subnet, and an internet gateway to allow communication between the resources in your VPC and the internet.

For more information, see [Amazon Virtual Private Cloud (Amazon VPC)](https://aws.amazon.com/vpc/).

The following features help you configure a VPC to provide the connectivity that your applications need:

A [VPC](./configure-your-vpc.html) is a virtual 
					network that closely resembles a traditional network that you'd operate
					in your own data center. After you create a VPC, you can add subnets.

A [subnet](./configure-subnets.html) is a range of 
					IP addresses in your VPC. A subnet must reside in a single Availability Zone.
					After you add subnets, you can deploy AWS resources in your VPC.

You can assign [IP addresses](./vpc-ip-addressing.html), 
					both IPv4 and IPv6, to your VPCs and subnets. You can also bring your public 
					IPv4 addresses and IPv6 GUA addresses to AWS and allocate them to resources in your VPC, 
					such as EC2 instances, NAT gateways, and Network Load Balancers.

Use [route tables](./VPC_Route_Tables.html) to determine 
					where network traffic from your subnet or gateway is directed.

A [gateway](./extend-intro.html) connects your VPC to 
					another network. For example, use an [internet gateway](./VPC_Internet_Gateway.html)
					to connect your VPC to the internet. Use a [VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) to connect to AWS services privately, without 
					the use of an internet gateway or NAT device.

Use a [VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/) 
					to route traffic between the resources in two VPCs.

[Copy network traffic](https://docs.aws.amazon.com/vpc/latest/mirroring/) from 
					network interfaces and send it to security and monitoring appliances for 
					deep packet inspection.

Use a [transit gateway](./extend-tgw.html), which 
					acts as a central hub, to route traffic between your VPCs, VPN connections,
				    and Direct Connect connections.

A [flow log](./flow-logs.html) captures information 
					about the IP traffic going to and from network interfaces in your VPC.

Connect your VPCs to your on-premises networks using
					[AWS Virtual Private Network (Site-to-Site VPN)](./vpn-connections.html).

Your AWS account includes a [default VPC](./default-vpc.html) in each AWS Region. 
			Your default VPCs are configured such that you can immediately start launching and connecting 
			to EC2 instances. For more information, see [Plan your VPC](./vpc-getting-started.html).

You can choose to create additional VPCs with the subnets, IP addresses, gateways
			and routing that you need. For more information, see [Create a VPC](./create-vpc.html).

You can create and manage your VPCs using any of the following interfaces:

**AWS Management Console** — Provides a web interface that you can
                    use to access your VPCs.

**AWS Command Line Interface (AWS CLI)** —
					Provides commands for a broad set of AWS services, including Amazon VPC, and is
					supported on Windows, Mac, and Linux. For more information, see [AWS Command Line Interface](https://aws.amazon.com/cli/).

**AWS SDKs** — Provides language-specific
					APIs and takes care of many of the connection details, such as calculating
					signatures, handling request retries, and error handling. For more information,
					see [AWS SDKs](https://aws.amazon.com/developer/tools/).

**Query API** — Provides low-level API actions 
                    that you call using HTTPS requests. Using the Query API is the most direct way to
                    access Amazon VPC, but it requires that your application handle low-level details such as
                    generating the hash to sign the request, and error handling. For more information, 
                    see [Amazon VPC actions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/OperationList-query-vpc.html) in 
					the *Amazon EC2 API Reference*.

There's no additional charge for using a VPC. There are, however, charges for some VPC
			components, such as NAT gateways, IP Address Manager, traffic mirroring, Reachability Analyzer, and
			Network Access Analyzer. For more information, see [Amazon VPC Pricing](https://aws.amazon.com/vpc/pricing/).

Nearly all resources that you launch in your virtual private cloud (VPC) provide you with an IP address for connectivity. The vast majority of resources in your VPC use private IPv4 addresses. Resources that require direct access to the internet over IPv4, however, use public IPv4 addresses.

Amazon VPC enables you to launch managed services, such as Elastic Load Balancing, Amazon RDS, and Amazon EMR, without having a VPC set up beforehand. It does this by using the [default
				VPC](./default-vpc.html) in your account if you have
				one. Any public IPv4 addresses provisioned to your account by the managed
			service will be charged. These charges will be associated with Amazon VPC service in
			your AWS Cost and Usage Report.

**Pricing for public IPv4 addresses**

A *public IPv4 address* is an IPv4 address that is
			routable from the internet. A public IPv4 address is necessary for a resource to be
			directly reachable from the internet over IPv4.

If you are an existing or new [AWS Free Tier](https://aws.amazon.com/free/)
			customer, you get 750 hours of public IPv4 address usage with the EC2 service at no
			charge. If you are not using the EC2 service in the AWS Free Tier, Public IPv4
			addresses are charged. For specific pricing information, see the 

Private IPv4 addresses ([RFC
				1918](https://datatracker.ietf.org/doc/html/rfc1918)) are not charged. For more information about how public IPv4 addresses
			are charged for shared VPCs, see 

Public IPv4 addresses have the following types:

**Elastic IP addresses (EIPs)**: Static, public IPv4 addresses
                provided by Amazon that you can associate with an EC2 instance, elastic network
                interface, or AWS resource.

**EC2 public IPv4 addresses**: Public IPv4 addresses assigned to
                an EC2 instance by Amazon (if the EC2 instance is launched into a default subnet or
                if the instance is launched into a subnet that’s been configured to automatically
                assign a public IPv4 address).

**BYOIPv4 addresses**: Public IPv4 addresses in the IPv4 address
                range that you’ve brought to AWS using [Bring your own IP addresses (BYOIP)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html).

**Service-managed IPv4 addresses**: Public IPv4 addresses
                automatically provisioned on AWS resources and managed by an AWS service. For
                example, public IPv4 addresses on Amazon ECS, Amazon RDS, or Amazon WorkSpaces.

The following list shows the most common AWS services that can use public IPv4 addresses.

Amazon WorkSpaces Applications

AWS Database Migration Service

Amazon EC2

Amazon Elastic Container Service

Amazon EKS

Amazon EMR

Amazon GameLift Servers

AWS Global Accelerator

AWS Mainframe Modernization

Amazon Managed Streaming for Apache Kafka

Amazon MQ

Amazon RDS

Amazon Redshift

AWS Site-to-Site VPN

Amazon VPC NAT gateway

Amazon WorkSpaces

Elastic Load Balancing

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

AWS SDK, CLI, PowerShell cmdlets demonstrate DeleteVpc across Neptune, IPAM, peering connection scenarios.

AWS SDK CreateVpc examples cover IPv4, IPv6, dedicated tenancy, IPAM pool CIDR configurations.

Interface VPC endpoints enable private IP KMS communication, integrating AWS PrivateLink for secure, internal AWS network access.

Public/private NAT gateways enable private subnet outbound connectivity, using Elastic IPs or VPC routing.

VPC peering enables private IP routing across accounts and Regions, supporting file sharing and geographic redundancy.

NACLs control subnet inbound outbound traffic; stateless vs stateful security groups key distinction.