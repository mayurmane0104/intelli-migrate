# IAM roles for Amazon EC2 - Amazon Elastic Compute Cloud

**Source:** [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html)

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

Applications must sign their API requests with AWS credentials. Therefore, if you are an application developer, you need a strategy for managing credentials for your applications that run on EC2 instances. For example, you can securely distribute your AWS credentials to the instances, enabling the applications on those instances to use your credentials to sign requests, while protecting your credentials from other users. However, it's challenging to securely distribute credentials to each instance, especially those that AWS creates on your behalf, such as Spot Instances or instances in Auto Scaling groups. You must also be able to update the credentials on each instance when you rotate your AWS credentials.

We designed IAM roles so that your applications can securely make API requests from your instances, without requiring you to manage the security credentials that the applications use. Instead of creating and distributing your AWS credentials, you can delegate permission to make API requests using IAM roles as follows:

Create an IAM role.

Define which accounts or AWS services can assume the role.

Define which API actions and resources the application can use after assuming the role.

Specify the role when you launch your instance, or attach the role to an existing instance.

Have the application retrieve a set of temporary credentials and use them.

For example, you can use IAM roles to grant permissions to applications running on your instances that need to use a bucket in Amazon S3. You can specify permissions for IAM roles by creating a policy in JSON format. These are similar to the policies that you create for users. If you change a role, the change is propagated to all instances.

Amazon EC2 IAM role credentials are not subject to maximum session durations configured in the role. For more information, 
				see [Methods to assume a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage-assume.html) in the *IAM User Guide*.

When creating IAM roles, associate least privilege IAM policies that restrict access to the specific API calls the application requires. For Windows-to-Windows communication, use well-defined and well-documented Windows groups and roles to grant application-level access between Windows instances. Groups and roles allow customers to define least privilege application and NTFS folder-level permissions to limit access to application-specific requirements.

You can only attach one IAM role to an instance, but you can attach the same role to
			many instances. For more information about creating and using IAM roles, see [Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) in the
				*IAM User Guide*.

You can apply resource-level permissions to your IAM policies to control the users'
			ability to attach, replace, or detach IAM roles for an instance. For more information,
			see [Supported resource-level permissions for Amazon EC2 API actions](./iam-policies-for-amazon-ec2.html#ec2-supported-iam-actions-resources) and the following example:
				[Example: Work with IAM roles](./ExamplePolicies_EC2.html#iam-example-iam-roles).

Amazon EC2 uses an *instance profile* as a container for an IAM
				role. When you create an IAM role using the IAM console, the console creates an
				instance profile automatically and gives it the same name as the role to which it
				corresponds. If you use the Amazon EC2 console to launch an instance with an IAM role
				or to attach an IAM role to an instance, you choose the role based on a list of
				instance profile names. 

If you use the AWS CLI, API, or an AWS SDK to create a role, you create the role and instance profile as separate actions, with potentially different names. If you then use the AWS CLI, API, or an AWS SDK to launch an instance with an IAM role or to attach an IAM role to an instance, specify the instance profile name.

An instance profile can contain only one IAM role. You can include an IAM role in multiple instance profiles.

To update permissions for an instance, replace its instance profile. We do not recommend removing a role from an instance profile, because there is a delay of up to one hour before this change takes effect.

For more information, see [Use instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) in the *IAM User Guide*.

When you first create an IAM role for your applications, you might sometimes grant
				permissions beyond what is required. Before launching your application in your
				production environment, you can generate an IAM policy that is based on the
				access activity for an IAM role. IAM Access Analyzer reviews your AWS CloudTrail logs and
				generates a policy template that contains the permissions that have been used by
				the role in your specified date range. You can use the template to create a
				managed policy with fine-grained permissions and then attach it to the IAM
				role. That way, you grant only the permissions that the role needs to interact
				with AWS resources for your specific use case. This helps you adhere to the
				best practice of [granting least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege). For more information, see [IAM Access Analyzer
						policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html) in the *IAM User Guide*.

Each Amazon EC2 instance that you launch has an *instance identity
				role* that represents its identity. An instance identity role is a type of
				IAM role. AWS services and features that are integrated to use the instance identity
				role can use it to identify the instance to the service.

The instance identity role credentials are accessible from the Instance Metadata Service
				(IMDS) at
				`/identity-credentials/ec2/security-credentials/ec2-instance`. The
				credentials consist of an AWS temporary access key pair and a session token. They are
				used to sign AWS Sigv4 requests to the AWS services that use the instance identity
				role. The credentials are present in the instance metadata regardless of whether a
				service or feature that makes use of instance identity roles is enabled on the
				instance.

Instance identity roles are automatically created when an instance is launched, have no role-trust policy document, and are not subject to any identity or resource policy.

The following AWS services use the instance identity role:

Amazon EC2 – [EC2 Instance Connect](./connect-linux-inst-eic.html) uses the instance
							identity role to update the host keys for a Linux instance.

**Amazon GuardDuty** – [GuardDuty Runtime
							Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html) uses the instance identity role to allow the runtime
							agent to send security telemetry to the GuardDuty VPC endpoint.

AWS Lambda – [Lambda Managed
							Instances](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances.html) uses the instance identity role for lifecycle hooks,
							telemetry, and artifact distribution.

AWS Security Token Service (AWS STS) – Instance
							identity role credentials can be used with the AWS STS [ GetCallerIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetCallerIdentity.html) action.

AWS Systems Manager – When using [Default Host Management Configuration](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-default-host-management-configuration.html), AWS Systems Manager uses the
							identity provided by the instance identity role to register EC2 instances.
							After identifying your instance, Systems Manager can pass your
							`AWSSystemsManagerDefaultEC2InstanceManagementRole` IAM
							role to your instance.

Instance identity roles can’t be used with other AWS services or features because they do not have an integration with instance identity roles.

The instance identity role ARN takes the following format:

`arn:``aws-partition`:iam::`account-number`:assumed-role/aws:ec2-instance/`instance-id`

For example:

`arn:``aws`:iam::`0123456789012`:assumed-role/aws:ec2-instance/`i-1234567890abcdef0`

For more information about ARNs, see [Amazon Resource Names
					(ARNs)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) in the *IAM User Guide*.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

AWS CLI manages Cognito identity pools: create, delete, list, set roles, update unauthenticated access settings.

Browser SAML plugin enables SAML-based authentication, MFA support, SSO configuration, token caching, Lake Formation API integration.

AWS CLI examples managing Cognito identity pools: create, delete, list, update, set roles.

Scalable virtual servers on AWS reduce hardware costs, enabling faster application deployment and flexible capacity management.

EC2 spans Regions, Availability Zones, Local Zones, Wavelength Zones, Outposts delivering flexible, low-latency infrastructure.

EC2 key pairs secure instance connections via SSH private keys or Windows password decryption.