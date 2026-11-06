# What is Amazon EC2? - Amazon Elastic Compute Cloud

**Source:** [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/index.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/index.html)

---

[Use AMI watermarks to track and identify AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-watermark.html)

*10 June 2026*

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies. 

 If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the [AWS Cookie Notice](https://aws.amazon.com/legal/cookies/).

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

Amazon Elastic Compute Cloud (Amazon EC2) provides on-demand, scalable computing capacity in the Amazon Web Services (AWS) Cloud. Using Amazon EC2 reduces hardware costs so you can develop and deploy applications faster. You can use Amazon EC2 to launch as many or as few virtual servers as you need, configure security and networking, and manage storage. You can add capacity (scale up) to handle compute-heavy tasks, such as monthly or yearly processes, or spikes in website traffic. When usage decreases, you can reduce capacity (scale down) again.

An EC2 instance is a virtual server in the AWS Cloud. When you launch an EC2 instance,
    	the instance type that you specify determines the hardware available to your instance. 
    	Each instance type offers a different balance of compute, memory, network, and storage 
    	resources. For more information, see the [Amazon EC2 Instance Types Guide](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-types.html).

Amazon EC2 provides the following high-level features:

Virtual servers.

Preconfigured templates for your instances that package the components you need for your server (including the operating system and additional software).

Various configurations of CPU, memory, storage, networking capacity, and graphics hardware for your instances.

Persistent storage volumes for your data using Amazon Elastic Block Store (Amazon EBS).

Storage volumes for temporary data that is deleted when you stop, hibernate, or terminate your instance.

Secure login information for your instances. AWS stores the public key and you store the private key in a secure place.

A virtual firewall that allows you to specify the protocols, ports, and source IP ranges that can reach your instances, and the destination IP ranges to which your instances can connect.

Amazon EC2 supports the processing, storage, and transmission 
of credit card data by a merchant or service provider, and has been 
validated as being compliant with Payment Card Industry (PCI) Data Security Standard (DSS). 
For more information about PCI DSS, including how to request a copy of the AWS PCI Compliance Package, 
see [PCI DSS Level 1](https://aws.amazon.com/compliance/pci-dss-level-1-faqs/).

You can use other AWS services with the instances that you deploy using Amazon EC2.

Helps ensure you have the correct number of Amazon EC2 instances available to handle the load for your application.

Automate backing up your Amazon EC2 instances and the Amazon EBS volumes attached to them.

Monitor your instances and Amazon EBS volumes.

Automatically distribute incoming application traffic across multiple instances.

Detect potentially unauthorized or malicious use of your EC2 instances.

Automate the creation, management, and deployment of customized, secure, and up-to-date server images.

Size, configure, and deploy AWS resources for third-party applications without having to manually identify and provision individual AWS resources.

Perform operations at scale on EC2 instances with this secure end-to-end management solution.

You can launch instances using another AWS compute service instead of using Amazon EC2.

Build websites or web applications using Amazon Lightsail, a cloud platform
						that provides the resources that you need to deploy your project quickly, for
						a low, predictable monthly price. To compare Amazon EC2 and Lightsail, see 
						[Amazon Lightsail or Amazon EC2](https://docs.aws.amazon.com/decision-guides/latest/lightsail-or-ec2/lightsail-or-ec2.html).

Deploy, manage, and scale containerized applications on a cluster of EC2
						instances. For more information, see [Choosing an AWS container service](https://docs.aws.amazon.com/decision-guides/latest/containers-on-aws-how-to-choose/choosing-aws-container-service.html).

Run your Kubernetes applications on AWS.  For more information, see 
						[Choosing an AWS container service](https://docs.aws.amazon.com/decision-guides/latest/containers-on-aws-how-to-choose/choosing-aws-container-service.html).

You can create and manage your Amazon EC2 instances using the following interfaces:

A simple web interface to create and manage Amazon EC2 instances and resources.
						If you've signed up for an AWS account, you can access the Amazon EC2 console
						by signing into the AWS Management Console and selecting **EC2** from
						the console home page.

Enables you to interact with AWS services using commands in your command-line shell. It
						is supported on Windows, Mac, and Linux. For more information about the
						AWS CLI , see [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/). You can find the Amazon EC2 commands in the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/ec2/index.html).

Amazon EC2 supports creating resources using CloudFormation. You create a template, in JSON or YAML
						format, that describes your AWS resources, and CloudFormation provisions and
						configures those resources for you. You can reuse your CloudFormation
						templates to provision the same resources multiple times, whether in the
						same Region and account or in multiple Regions and accounts. For more
						information about supported resource types and properties for Amazon EC2, see
							[EC2 resource type
							reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EC2.html) in the *AWS CloudFormation User Guide*.

If you prefer to build applications using language-specific APIs instead
						of submitting a request over HTTP or HTTPS, AWS provides libraries, sample
						code, tutorials, and other resources for software developers. These
						libraries provide basic functions that automate tasks such as
						cryptographically signing your requests, retrying requests, and handling
						error responses, making it easier for you to get started. For more
						information, see 
						[Tools to Build
								on AWS](https://aws.amazon.com/developer/tools/).

A set of PowerShell modules that are built on the functionality exposed by
						the SDK for .NET. The Tools for PowerShell enable you to script operations on your AWS
						resources from the PowerShell command line. To get started, see the
							[AWS Tools for PowerShell User Guide](https://docs.aws.amazon.com/powershell/latest/userguide/). You can find the cmdlets for Amazon EC2, in the [AWS Tools for PowerShell Cmdlet Reference](https://docs.aws.amazon.com/powershell/latest/reference/Index.html).

Amazon EC2 provides a Query API. These requests are HTTP or HTTPS requests that
						use the HTTP verbs GET or POST and a Query parameter named
						`Action`. For more information about the API actions for
						Amazon EC2, see [Actions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Operations.html) in the
						*Amazon EC2 API Reference*.

Amazon EC2 provides the following pricing options:

You can get started with Amazon EC2 for free. To explore the Free Tier options,
						see [AWS Free Tier](https://aws.amazon.com/free/).

Pay for the instances that you use by the second, with a minimum of 60 seconds, with no long-term commitments or upfront payments.

You can reduce your Amazon EC2 costs by making a commitment to a consistent amount of usage, in USD per hour, for a term of 1 or 3 years.

You can reduce your Amazon EC2 costs by making a commitment to a specific instance configuration, including instance type and Region, for a term of 1 or 3 years.

Request unused EC2 instances, which can reduce your Amazon EC2 costs significantly.

Reduce costs by using a physical EC2 server that is fully dedicated for your use, either On-Demand or as part of a Savings Plan. You can use your existing server-bound software licenses and get help meeting compliance requirements.

Reserve compute capacity for your EC2 instances in a specific Availability Zone for any duration of time.

Removes the cost of unused minutes and seconds from your bill.

For a complete list of charges and prices for Amazon EC2 and more information about the purchase
			models, see [Amazon EC2 pricing](https://aws.amazon.com/ec2/pricing/).

To create estimates for your AWS use cases, use the [AWS Pricing Calculator](https://calculator.aws/#/).

To estimate the cost of transforming **Microsoft
					workloads** to a modern architecture that uses open source and
				cloud-native services deployed on AWS, use the [AWS
					Modernization Calculator for Microsoft Workloads](https://modernization.calculator.aws/microsoft/workload).

To see your bill, go to the **Billing and Cost Management
					Dashboard** in the [AWS Billing and Cost Management
					console](https://console.aws.amazon.com/billing/). Your bill contains links to usage reports that provide details
				about your bill. To learn more about AWS account billing, see 

If you have questions concerning AWS billing, accounts, and events, [contact AWS Support](https://aws.amazon.com/contact-us/).

To calculate the cost of a sample provisioned
					environment, see [Cloud Economics
						Center](https://aws.amazon.com/economics/). When calculating the cost of a provisioned
				environment, remember to include incidental costs such as snapshot storage for EBS
				volumes. 

You can optimize the cost, security, and performance of your AWS environment
				using [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/).

You can use AWS Cost Explorer to analyze the cost and usage of your EC2 instances. You can view 
				data up to the last 13 months, and forecast how much you are likely to spend for the next 
				12 months. For more information, see
				[Analyzing your costs and usage with
					AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) in the *AWS Cost Management User Guide*.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

EC2 spans Regions, Availability Zones, Local Zones, Wavelength Zones, Outposts delivering flexible, low-latency infrastructure.

EC2 key pairs secure instance connections via SSH private keys or Windows password decryption.

Static IPv4 addresses allocated AWS accounts mask instance failure remapping address rapidly.