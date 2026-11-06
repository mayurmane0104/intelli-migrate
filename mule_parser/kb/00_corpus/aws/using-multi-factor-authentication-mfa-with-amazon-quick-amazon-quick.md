# Using multi-factor authentication (MFA) with Amazon Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/using-multi-factor-authentication-mfa.html](https://docs.aws.amazon.com/quick/latest/userguide/using-multi-factor-authentication-mfa.html)

---

| Applies
                    to:Enterprise Edition and Standard Edition | 

| Intended audience: System administrators | 

###### Important

Amazon Quick recommends that you integrate new Quick subscriptions with
            IAM Identity Center for identity management. This IAM identity federation user guide is provided as
            a reference for existing account configurations. For more information on integrating
            your Quick account with IAM Identity Center, see [Configure your Quick account with
            IAM Identity Center](https://docs.aws.amazon.com/quicksight/latest/user/sec-identity-management-identity-center.html).

###### Note

IAM identity federation doesn't support syncing identity provider groups with Amazon Quick.

There are several ways that you can use multi-factor authentication (MFA) with
        Quick. You can use it with AWS Identity and Access Management (IAM). You can use it with AD Connector
        or your [AWS Directory
            Service](https://aws.amazon.com/directoryservice/) for Microsoft Active Directory, also known as AWS
        Microsoft Active Directory or AWS Managed Microsoft Active Directory. And if
        you use an external identity provider (IdP), AWS doesn't need to have any
        information about MFA because that is part of the authentication handled by the IdP. 

For more information, see the following:

- 
            [Using multi-factor authentication (MFA) in AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html)in the IAM User Guide
- 
            [Enable Multi-Factor Authentication for AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/mfa_ad.html)in the AWS Directory Service Administration Guide
- 
            [Enable Multi-Factor Authentication for AD Connector](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_connector_mfa.html)in the AWS Directory Service Administration Guide

If you're a developer, see the following: