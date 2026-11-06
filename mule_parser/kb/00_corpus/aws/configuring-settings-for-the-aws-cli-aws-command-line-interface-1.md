# Configuring settings for the AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-configure.html](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-configure.html)

---

**This documentation is for Version 1 of the AWS CLI only.**

We announced the upcoming end-of-support for the AWS CLI version 1. We recommend that you migrate to the AWS CLI version 2. For dates, additional details, and information on how to migrate, see the [announcement](https://aws.amazon.com/blogs/developer/cli-v1-maintenance-mode-announcement/). For documentation related to Version 2 of the AWS CLI, see the 

[Version 2 User Guide](https://docs.aws.amazon.com/cli/latest/userguide/).

This section explains how to configure the settings that the AWS Command Line Interface (AWS CLI) uses to interact with AWS. These include the following:

- 
            **Credentials**identify who is calling the API. Access credentials are used to encrypt the request to the AWS servers to confirm your identity and retrieve associated permissions policies. These permissions determine the actions you can perform. For information on setting up your credentials, see[Authentication and access credentials for the AWS CLI](./cli-chap-authentication.html).
- 
            **Other configuration details**to tell the AWS CLI how to process requests, such as the default output format and the default AWS Region.

###### Note

AWS requires that all incoming requests are cryptographically signed. The AWS CLI does this for you. The "signature" includes a date/time stamp. Therefore, you must ensure that your computer's date and time are set correctly. If you don't, and the date/time in the signature is too far off of the date/time recognized by the AWS service, AWS rejects the request.

## Configuration and credentials precedence

        Credentials and configuration settings are located in multiple places, such as the system or user environment variables, local AWS configuration files, or explicitly declared on the command line as a parameter. Certain locations take precedence over others. The AWS CLI credentials and configuration settings take precedence in the following order:

- 
    [Command line options](./cli-configure-options.html)`--region`,`--output`, and`--profile`parameters.
- 
    [Environment variables](./cli-configure-envvars.html)
- 
    [Assume role](./cli-configure-role.html)`assume-role`
- 
    [Assume role with web identity](./cli-configure-role.html)`assume-role-with-web-identity`
- 
    [Credentials file](./cli-configure-files.html)`credentials`and`config`file are updated when you run the command`aws configure`. The`credentials`file is located at`~/.aws/credentials`on Linux or macOS, or at`C:\Users\`on Windows.`USERNAME`\.aws\credentials
- 
    [Custom process](./cli-configure-sourcing-external.html)
- 
    [Configuration file](./cli-configure-files.html)`credentials`and`config`file are updated when you run the command`aws configure`. The`config`file is located at`~/.aws/config`on Linux or macOS, or at`C:\Users\`on Windows.`USERNAME`\.aws\config
- 
    [Container credentials](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html)[IAM Roles for Tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html)in the*Amazon Elastic Container Service Developer Guide*.
- 
    [Amazon EC2 instance profile credentials](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html)[IAM Roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html)in the*Amazon EC2 User Guide*and[Using Instance Profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html)in the*IAM User Guide*.