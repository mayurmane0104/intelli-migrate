# Using Active Directory with Amazon Quick Enterprise edition - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/aws-directory-service.html](https://docs.aws.amazon.com/quick/latest/userguide/aws-directory-service.html)

---

| Applies
                    to:Enterprise Edition | 

| Intended audience: System administrators | 

###### Note

IAM identity federation doesn't support syncing identity provider groups with Amazon Quick.

Amazon Quick Enterprise edition supports both [AWS Directory Service for Microsoft Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html) and [Active Directory Connector](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_ad_connector.html). 

To create a new directory to be your identity manager for Quick, use
        AWS Directory Service for Microsoft Active Directory, also known as AWS Managed Microsoft AD. This is an Active Directory host in the
            AWS Cloud that offers most of the same functionality of Active Directory.
        Currently, you can connect to Active Directory in any AWS Region supported by
        Amazon Quick, except for Asia Pacific (Singapore). When you create a directory, you use it
        with a virtual private cloud (VPC). For more information, see [VPC](https://docs.aws.amazon.com/quicksight/latest/user/vpc-amazon-virtual-private-cloud.html).

If you have an existing directory that you want to use for Quick, you can use Active Directory Connector. This service redirects directory requests to your Active Directory—in another AWS Region or on-premises—without caching any information in the cloud.

For a walkthrough about creating and managing a directory with AWS Managed Microsoft AD, see [Use an AWS Managed Microsoft AD with Quick?](https://aws.amazon.com/premiumsupport/knowledge-center/quicksight-authenticate-active-directory/) in the
            AWS Knowledge Center. 

When you use AWS Directory Service to launch a directory, AWS creates an organizational unit (OU) with the same name as your domain. AWS
        also creates an administrative account with delegated administrative rights for the OU. You
        can create accounts, groups, and policies within the OU by using Active Directory users and
        groups. For more information, see [
            Best Practices for AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_best_practices.html) in the
            *Directory Service Administration Guide.*

After you establish your directory, you use it with Quick by creating groups for users. Amazon Quick has six specific user roles that can be assigned, including Pro versions that provide access to advanced capabilities:

- 
            Quick admins – Admins can change account settings, manage accounts. Admins can also purchase additional Amazon Quick user subscriptions or [SPICE](https://docs.aws.amazon.com/quicksight/latest/user/spice.html)capacity, or cancel the subscription to Amazon Quick for your AWS account. Admin Pro users have additional capabilities including creating content using natural language, building knowledge bases, configuring actions, and accessing advanced automation workflows.
- 
            Quick authors – Amazon Quick authors can create data sources, datasets, analyses, and dashboards. They can share analyses and dashboards with other Amazon Quick users. Author Pro users can additionally create content using natural language, build knowledge bases, configure actions, and access advanced automation capabilities. 
- 
            Quick readers – Readers can view and interact with dashboards that were created by someone else. Reader Pro users have access to advanced features including AI chat agents, collaborative spaces, flows, and extensions. 

You can add or refine access by applying IAM policies. For example, you can use IAM policies to allow users to subscribe themselves.

When you subscribe to Amazon Quick Enterprise edition and choose Active Directory as your identity provider, you can associate your AD groups with Amazon Quick. You can also add or change your AD groups later on.

## Directory integration with Quick Enterprise edition

        | Applies
                    to:Enterprise Edition | 

| Intended audience: System administrators | 

###### Note

IAM identity federation doesn't support syncing identity provider groups with Amazon Quick.

Quick Enterprise supports the following options:

- 
                AWS Directory Service 
- 
                AWS Directory Service with AD Connector 
- 
                On-premises Active Directory with IAM federation or AD Connector 
- 
                IAM federation using AWS IAM Identity Center or another third-party federation service 

If you want to use IAM federation with an on-premises Active Directory, you implement AWS Directory Service as a separate Active Directory with a trust relationship to the on-premises Active Directory.

If you want to avoid using a trust relationship, you can deploy a standalone domain for authentication within AWS. Then you can create users and groups in Active Directory. You'd then map them to users and groups in Quick. In this example, users authenticate using their Active Directory login credentials. To make access to Quick transparent to your users, use IAM federation in this scenario.