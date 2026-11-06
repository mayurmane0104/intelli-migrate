# Using Amazon EC2 instance metadata as credentials in the AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-metadata.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-metadata.html)

---

When you run the AWS CLI from within an Amazon Elastic Compute Cloud (Amazon EC2) instance, you can simplify providing credentials to your commands. Each Amazon EC2 instance contains metadata that the AWS CLI can directly query for temporary credentials. When an IAM role is attached to the instance, the AWS CLI automatically and securely retrieves the credentials from the instance metadata.

To disable this service, use the [AWS_EC2_METADATA_DISABLED](./cli-configure-envvars.html#envvars-list-AWS_EC2_METADATA_DISABLED)
        environment variable.

## Prerequisites

        To use Amazon EC2 credentials with the AWS CLI, you need to complete the following:

- 
                Install and configure the AWS CLI. For more information, see [Installing or updating to the latest version of the AWS CLI](./getting-started-install.html)and[Authentication and access credentials for the AWS CLI](./cli-chap-authentication.html).
- 
                You understand configuration files and named profiles. For more information, see [Configuration and credential file settings in the AWS CLI](./cli-configure-files.html).
- 
                You've created an AWS Identity and Access Management (IAM) role that has access to the resources needed, and attached that role to the Amazon EC2 instance when you launch it. For more information, see [IAM policies for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html)in the*Amazon EC2 User Guide*and[Granting Applications That Run on Amazon EC2 Instances Access to AWS Resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/role-usecase-ec2app.html)in the*IAM User Guide*.

## Configuring a profile for Amazon EC2 metadata

        To specify that you want to use the credentials available in the hosting Amazon EC2 instance profile, use the following syntax in the named profile in your configuration file. See the following steps for more instructions.

`[profile``profilename`] role_arn =`arn:aws:iam::123456789012:role/rolename`credential_source = Ec2InstanceMetadata region =`region`

- 
                Create a profile in your configuration file. `[profile``profilename`]
- 
                Add your IAM arn role that has access to the resources needed. `role_arn =``arn:aws:iam::123456789012:role/rolename`
- 
                Specify `Ec2InstanceMetadata`as your credential source.`credential_source = Ec2InstanceMetadata`
- 
                Set your Region. `region =``region`

**Example**

The following example assumes the
                `marketingadminrole``us-west-2``marketingadmin`

`[profile``marketingadmin`] role_arn =`arn:aws:iam::123456789012:role/marketingadminrole`credential_source = Ec2InstanceMetadata region =`us-west-2`