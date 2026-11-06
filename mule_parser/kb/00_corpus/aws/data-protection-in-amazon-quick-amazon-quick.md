# Data protection in Amazon Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/sec-data-protection.html](https://docs.aws.amazon.com/quick/latest/userguide/sec-data-protection.html)

---

The AWS 
[shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/)
    
   applies to data protection in Amazon Quick. 
   
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
        customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Amazon Quick or other AWS services 
        using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
        tags or free-form text fields used for names may be used for billing or diagnostic logs. If you 
        provide a URL to an external server, we strongly recommend that you do not include credentials 
        information in the URL to validate your request to that server.

Amazon Quick does not use customer data for training or improving underlying LLMs.