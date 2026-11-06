# Data protection in the AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/data-protection.html](https://docs.aws.amazon.com/cli/latest/userguide/data-protection.html)

---

The AWS 
[shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/)
    
   applies to data protection in AWS Command Line Interface. 
   
   As described in this model, AWS is
   responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are
   responsible for maintaining control over your content that is hosted on this infrastructure.
   You are also responsible for the security configuration and management tasks for the AWS services
   that you use. 
   
   For more information about data privacy, see 
   

[Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/). For information about data protection in Europe, see the

[General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/).

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:

- 
        Use multi-factor authentication (MFA) with each account. 
- 
        Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3. 
- 
        Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html)in the*AWS CloudTrail User Guide*.
- 
        Use AWS encryption solutions, along with all default security controls within AWS services. 
- 
        Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3. 
- 
        If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/).

We strongly recommend that you never put confidential or sensitive information, such as your
        customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with AWS CLI or other AWS services 
        using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
        tags or free-form text fields used for names may be used for billing or diagnostic logs. If you 
        provide a URL to an external server, we strongly recommend that you do not include credentials 
        information in the URL to validate your request to that server.

## Data encryption

        A key feature of any secure service is that information is encrypted when it is not being actively used.

### Encryption at rest

By default, the AWS CLI does not itself store any customer data other than the credentials it needs to interact with the AWS services on the user's behalf.

When the user enables the optional 
                [cli_history](./cli-configure-files.html#cli-config-cli_history) feature, the 
                AWS CLI stores complete command execution history, including command parameters and 
                API request/response data in `~/.aws/cli/history/history.db`. You can 
                disable this feature at any time by setting `cli_history = disabled` in 
                the AWS CLI configuration. To store history in a different location, set the 
                `AWS_CLI_HISTORY_FILE` environment variable.

If you use the AWS CLI to invoke an AWS service that transmits customer data to your local computer for storage, then refer to the Security & Compliance chapter in that service's User Guide for information on how that data is stored, protected, and encrypted.

### Encryption in transit

By default, all data transmitted from the client computer running the AWS CLI and AWS service endpoints is encrypted by sending everything through a HTTPS/TLS connection.

You don't need to do anything to enable the use of HTTPS/TLS. It is always enabled
                unless you explicitly disable it for an individual command by using the
                    `--no-verify-ssl` command line option.