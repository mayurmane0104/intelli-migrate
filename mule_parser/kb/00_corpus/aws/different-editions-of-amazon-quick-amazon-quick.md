# Different editions of Amazon Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/editions.html](https://docs.aws.amazon.com/quick/latest/userguide/editions.html)

---

Amazon Quick offers Standard and Enterprise editions. Both editions offer a full set of features for creating and sharing data visualizations. Enterprise edition additionally offers encryption at rest and Microsoft Active Directory integration. In Enterprise edition, you select a Microsoft Active Directory directory in Directory Service. You use that active directory to identify and manage your Quick users and administrators.

For more information about the different features offered by the Quick
        editions and about pricing, see [Amazon Quick pricing](https://aws.amazon.com/quicksuite/pricing/).

###### Note

New Amazon Quick features are only available under the Enterprise edition.

###### Topics

## Availability of editions

        All editions are available in any AWS Region that is currently supported by Amazon Quick.

The capacity region in which you start your Amazon Quick subscription is where your
            account's default [SPICE](https://docs.aws.amazon.com/quicksight/latest/user/spice.html) capacity is allocated. However, you can purchase additional
                SPICE capacity and access your AWS resources in any other supported
            AWS Region.

New Amazon Quick features are not available in the Standard edition. If you are an existing customer on the Standard edition, you can upgrade to Enterprise edition and provision appropriate roles to access Amazon Quick features.

To manage Enterprise account settings, you must temporarily change your region for your session to US East (N. Virginia) Region. You can change it back when you have finished editing your account settings. These settings include changing your subscription's notification email, enabling IAM access requests, editing access to AWS resources, and unsubscribing from Amazon Quick.

## User management between editions

        User management is different between the Amazon Quick Standard and Enterprise editions. However, both editions support identity federation, or Federated Single Sign-On (IAM Identity Center), through Security Assertion Markup Language 2.0 (SAML 2.0).

### User management for standard edition

In the Standard edition, as a system administrator, you can invite an AWS Identity and Access Management user and allow that user to use their credentials to access Amazon Quick. Alternatively, you can invite any person with an email address to create an Amazon Quick–only account. When you create a Amazon Quick user account, Amazon Quick sends an email to that user inviting them to activate their account.

When you create a Amazon Quick user account, you also choose to assign it either an administrative or a user role. This role assignment determines the user's permissions in Amazon Quick. You perform all management of users by adding, changing, and deleting accounts in Amazon Quick.

### User management for enterprise edition

In the Enterprise edition, as a system administrator, you can select one or more IAM Identity Center or Microsoft Active Directory groups for administrative access. All users in these groups are authorized to sign in to Amazon Quick as Amazon Quick administrators. You can also select one or more IAM Identity Center or Microsoft Active Directory groups in Directory Service for user access. All users in these groups are authorized to sign in to Amazon Quick as users.

###### Important

With IAM Identity Center, share the AWS sign in portal with end users to access
                    Amazon Quick. For more information, see [Sign in to the AWS access portal](https://docs.aws.amazon.com/signin/latest/userguide/iam-id-center-sign-in-tutorial.html).

With Active Directory, Amazon Quick Administrators and users aren't automatically notified of their access to Amazon Quick. You must email users with the sign-in URL, the account name, and their credentials.

You can only add or remove Enterprise edition accounts by adding or removing a person from the IAM Identity Center or Microsoft Active Directory group that you associated with Amazon Quick. When you add a Amazon Quick user account, its permissions depend on whether the IAM Identity Center or Microsoft Active Directory group is an administrative group or a user group in Amazon Quick.

To remove a user's access to Amazon Quick, remove the user from an IAM Identity Center or Microsoft Active Directory group or remove their IAM Identity Center or Microsoft Active Directory group from an associated role in Amazon Quick.

## Permissions for the different editions

        In the Standard edition, all Amazon Quick administrators can manage subscriptions and SPICE capacity. They can also add, modify, and delete accounts.

Additional IAM permissions are required to manage Amazon Quick permissions to AWS resources and to unsubscribe from Amazon Quick. These tasks can only be performed by an IAM user who also has administrative permissions in Amazon Quick, or by the IAM user or AWS account (system administrator) that created the Amazon Quick account.

To manage access to AWS resources from Amazon Quick, you must be logged in as one of the following:

- 
                Any IAM user who is an Amazon Quick administrator 
- 
                The IAM user or AWS root account that created the Amazon Quick account (system administrator) 

All IAM Identity Center or Microsoft Active Directory users that are Amazon Quick administrators can manage subscriptions and SPICE capacity.

Additional IAM permissions are required to manage access to AWS resources or to unsubscribe from Amazon Quick. Administrators need to sign in with IAM permissions to perform these tasks.

For more information on admin user permissions, see [Amazon Quick
                user types](https://docs.aws.amazon.com/quicksuite/latest/userguide/user-types.html).