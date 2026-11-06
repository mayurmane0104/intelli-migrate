# Identity and Access Management - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/security-iam.html](https://docs.aws.amazon.com/cli/latest/userguide/security-iam.html)

---

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access
      to AWS resources. IAM administrators control who can be *authenticated* (signed in) and *authorized*
      (have permissions) to use AWS resources. IAM is an AWS service that you can
      use with no additional charge.

###### Topics

## Audience

    
    How you use AWS Identity and Access Management (IAM) differs, depending on the work that you do in AWS.

**Service user** – If you use AWS services to do
      your job, then your administrator provides you with the credentials and permissions that you
      need. As you use more AWS features to do your work, you might need additional permissions.
      Understanding how access is managed can help you request the right permissions from your
      administrator. If you cannot access a feature in AWS, see [Troubleshooting AWS identity and access](#security_iam_troubleshoot) or the user
      guide of the AWS service you are using.

**Service administrator** – If you're in charge
      of AWS resources at your company, you probably have full access to AWS. It's your job
      to determine which AWS features and resources your service users should access. You must
      then submit requests to your IAM administrator to change the permissions of your service
      users. Review the information on this page to understand the basic concepts of IAM. To learn
      more about how your company can use IAM with AWS, see the user guide of the AWS service
      you are using.

**IAM administrator** – If you're an IAM
      administrator, you might want to learn details about how you can write policies to manage
      access to AWS. To view example AWS identity-based policies that you can use in IAM, see
      the user guide of the AWS service you are using.

## Authenticating with identities

    
   
Authentication is how you sign in to AWS using your identity credentials. You must be authenticated as the AWS account root user, an IAM user, or by assuming an IAM role.

You can sign in as a federated identity using credentials from an identity source like AWS IAM Identity Center (IAM Identity Center), single sign-on authentication, or Google/Facebook credentials. For more information about signing in, see [How to sign in to your AWS account](https://docs.aws.amazon.com/signin/latest/userguide/how-to-sign-in.html) in the *AWS Sign-In User Guide*.

For programmatic access, AWS provides an SDK and CLI to cryptographically sign requests. For more information, see [AWS Signature Version 4 for API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) in the *IAM User Guide*.

### AWS account root user

 When you create an AWS account, you begin with one sign-in identity called the AWS account *root user* that has complete access to all AWS services and resources. We strongly recommend that you don't use the root user for everyday tasks. For tasks that require root user credentials, see [Tasks that require root user credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks) in the *IAM User Guide*.
 

### Federated identity

As a best practice, require human users to use federation with an identity provider to access AWS services using temporary credentials.

A *federated identity* is a user from your enterprise directory, web identity provider, or Directory Service that accesses AWS services using credentials from an identity source. Federated identities assume roles that provide temporary credentials.

For centralized access management, we recommend AWS IAM Identity Center. For more information, see [What is IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) in the *AWS IAM Identity Center User Guide*.

### IAM users and groups

An * IAM user* is an identity with specific permissions for a single person or application. We recommend using temporary credentials instead of IAM users with long-term credentials. For more information, see 

[Require human users to use federation with an identity provider to access AWS using temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-users-federation-idp)in the

*IAM User Guide*.

An [ IAM group](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html) specifies a collection of IAM users and makes permissions easier to manage for large sets of users. For more information, see 

[Use cases for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/gs-identities-iam-users.html)in the

*IAM User Guide*.

### IAM roles

An * IAM role* is an identity with specific permissions that provides temporary credentials. You can assume a role by 

[switching from a user to an IAM role (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-console.html)or by calling an AWS CLI or AWS API operation. For more information, see

[Methods to assume a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage-assume.html)in the

*IAM User Guide*.

IAM roles are useful for federated user access, temporary IAM user permissions, cross-account access, cross-service access, and applications running on Amazon EC2. For more information, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html) in the *IAM User Guide*.

## Managing access using policies

    
   
 You control access in AWS by creating policies and attaching them to AWS identities or resources. A policy defines permissions when associated with an identity or resource. AWS evaluates these policies when a principal makes a request. Most policies are stored in AWS as JSON documents. For more information about JSON policy documents, see [Overview of JSON policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json) in the *IAM User Guide*.

Using policies, administrators specify who has access to what by defining which **principal** can perform **actions** on what **resources**, and under what **conditions**.

By default, users and roles have no permissions. An IAM administrator creates IAM policies and adds them to roles, which users can then assume. IAM policies define permissions regardless of the method used to perform the operation.

### Identity-based policies

Identity-based policies are JSON permissions policy documents that you attach to an identity (user, group, or role). These policies control what actions identities can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

Identity-based policies can be *inline policies* (embedded directly into a single identity) or *managed policies* (standalone policies attached to multiple identities). To learn how to choose between managed and inline policies, see [Choose between managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.html) in the *IAM User Guide*.

### Resource-based policies

Resource-based policies are JSON policy documents that you attach to a resource. Examples include IAM *role trust policies* and Amazon S3 *bucket policies*. In services that support resource-based policies, service administrators can use them to control access to a specific resource. You must [specify a principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) in a resource-based policy.

Resource-based policies are inline policies that are located in that service. You can't use AWS managed policies from IAM in a resource-based policy.

### Access control lists (ACLs)

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

Amazon S3, AWS WAF, and Amazon VPC
            are examples of services that support ACLs. To learn more about ACLs, see [Access control list (ACL)
               overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html) in the *Amazon Simple Storage Service Developer Guide*.

### Other policy types

AWS supports additional policy types that can set the maximum permissions granted by more common policy types:

- 
               **Permissions boundaries**– Set the maximum permissions that an identity-based policy can grant to an IAM entity. For more information, see[Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)in the*IAM User Guide*.
- 
               **Service control policies (SCPs)**– Specify the maximum permissions for an organization or organizational unit in AWS Organizations. For more information, see[Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)in the*AWS Organizations User Guide*.
- 
            **Resource control policies (RCPs)**– Set the maximum available permissions for resources in your accounts. For more information, see[Resource control policies (RCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html)in the*AWS Organizations User Guide*.
- 
               **Session policies**– Advanced policies passed as a parameter when creating a temporary session for a role or federated user. For more information, see[Session policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session)in the*IAM User Guide*.

### Multiple policy types

When multiple types of policies apply to a request, the resulting permissions are more complicated to understand. To learn how AWS determines whether to allow a request when multiple policy types are involved, see [Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) in the *IAM User Guide*.

## How AWS services work with IAM

    To get a high-level view of how AWS services work with most IAM features, see [AWS services that work
        with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

To learn how to use a specific AWS service with IAM, see the security section of the relevant service's User Guide.

## Troubleshooting AWS identity and access

    
   
        Use the following information to help you diagnose and fix common issues that you might encounter when working with AWS and IAM.

###### Topics

### I am not authorized to perform an action in AWS

If you receive an error that you're not authorized to perform an action, your policies must be updated to allow you to perform the action.

The following example error occurs when the `mateojackson` IAM user
      tries to use the console to view details about a fictional
      `my-example-widget``awes:` permissions.`GetWidget`

User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: awes:`GetWidget`on resource:`my-example-widget`

In this case, the policy for the `mateojackson` user must be updated to allow access to the
      `my-example-widget``awes:` action.`GetWidget`

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

### I am not authorized to perform iam:PassRole

If you receive an error that you're not authorized to perform the `iam:PassRole` action, your policies must be updated to allow you to pass a role to AWS.

Some AWS services allow you to pass an existing role to that service instead of creating a new service role or service-linked role. To do this, you must have permissions to pass the role to the service.

The following example error occurs when an IAM user named `marymajor` tries to use the console to perform an action in
 AWS. However, the action requires the service to have permissions that are granted by a service role. Mary does not have permissions to pass the
 role to the service.

`User: arn:aws:iam::123456789012:user/``marymajor`is not authorized to perform: iam:PassRole

In this case, Mary's policies must be updated to allow her to perform the `iam:PassRole` action.

If you need help, contact your AWS administrator. Your administrator is the person who provided you with your sign-in credentials.

### I want to allow people outside of my AWS account to access my AWS resources

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant people access to your resources.

To learn more, consult the following:

- 
               To learn whether AWS supports these features, see [How AWS services work with IAM](#security_iam_service-with-iam).
- 
               To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you own](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html)in the*IAM User Guide*.
- 
               To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html)in the*IAM User Guide*.
- 
               To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html)in the*IAM User Guide*.
- 
               To learn the difference between using roles and resource-based policies for cross-account access, see [Cross account resource access in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-cross-account-resource-access.html)in the*IAM User Guide*.