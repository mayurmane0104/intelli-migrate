# Authentication and access credentials for the AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-authentication.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-authentication.html)

---

You must establish how the AWS CLI authenticates with AWS when you develop with AWS services. To configure credentials for programmatic access for the AWS CLI, choose one of the following options. The options are in order of recommendation.

| Authentication type | Purpose | Instructions | 
|---|---|---|
| AWS Management Console credentials | 
 | [Login for AWS local development using console credentials](./cli-configure-sign-in.html) | 
| IAM Identity Center workforce users short-term credentials | Use short-term credentials for an
          IAM Identity Center workforce user. Security best practice is to use AWS Organizations with IAM Identity Center. It combines short-term credentials with a user directory, such as the built-in IAM Identity Center directory or Active Directory. | [Configuring IAM Identity Center authentication with the AWS CLI](./cli-configure-sso.html) | 
| IAM user short-term credentials | Use IAM user short-term credentials, which are more secure than long-term credentials. If your credentials are compromised, there is a limited time they can be used before they expire. | [Authenticating with short-term credentials for the AWS CLI](./cli-authentication-short-term.html) | 
| IAM or IAM Identity Center users on an Amazon EC2 instance. | Use Amazon EC2 instance metadata to query for temporary credentials using the role assigned to the Amazon EC2 instance. | [Using Amazon EC2 instance metadata as credentials in the AWS CLI](./cli-configure-metadata.html) | 
| Assume roles for permissions | Pair another credential method and assume a role for temporary access to AWS services your user might not have access to. | [Using an IAM role in the AWS CLI](./cli-configure-role.html) | 
| IAM user long-term credentials | (Not recommended)Use long-term credentials, which
          have no expiration. | [Authenticating using IAM user credentials for the AWS CLI](./cli-authentication-user.html) | 
| External storage of IAM or IAM Identity Center workforce users | (Not recommended)Pair another credential method but
          store credential values in a location outside of the AWS CLI. This method is only as secure
          as the external location the credentials are stored. | [Sourcing credentials with an external process in the AWS CLI](./cli-configure-sourcing-external.html) | 

## Configuration and credential precedence

    Credentials and configuration settings are located in multiple places, such as the system or user environment variables, local AWS configuration files, or explicitly declared on the command line as a parameter. Certain authentication take precedence over others. The AWS CLI authentication settings take precedence in the following order:

- 
    [Command line options](./cli-configure-options.html)`--region`,`--output`, and`--profile`parameters.
- 
    [Environment variables](./cli-configure-envvars.html)
- 
    [Assume role](./cli-configure-role.html)`assume-role`
- 
    [Assume role with web identity](./cli-configure-role.html)`assume-role-with-web-identity`
- 
    [AWS IAM Identity Center](./cli-configure-files.html)`config`file are updated when you run the`aws configure sso`command. Credentials are then authenticated when you run the`aws sso login`command. The`config`file is located at`~/.aws/config`on Linux or macOS, or at`C:\Users\`on Windows.`USERNAME`\.aws\config
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