# Introduction to IAM concepts - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/security_iam_concepts.html](https://docs.aws.amazon.com/quick/latest/userguide/security_iam_concepts.html)

---

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator to more securely
            control access to AWS resources. Administrators control who can be *authenticated* (signed in) and *authorized* (have permissions) to use Amazon Quick resources. IAM is an
            AWS service that you can use with no additional charge.

IAM is used with Amazon Quick in several ways, including the following:

- 
                If your company uses IAM for their identity management, people might have IAM user names and passwords that they use to sign in to Amazon Quick. 
- 
                If you want your Amazon Quick users to be automatically created at first sign-in, you can use IAM to create a policy for users who are preauthorized to use Amazon Quick. 
- 
                If you want to create specialized access for specific groups of Amazon Quick users or to specific resources, you can use IAM policies to accomplish this. 

## Audience

            Use the following to help understand the context of the information provided in this section, and how it applies to your role. How you use AWS Identity and Access Management (IAM) differs depending on the work that you do in Amazon Quick.

**Service user** – In some cases, you might
                use Amazon Quick as an Author or Reader to interact with data, analyses, and
                dashboards, spaces, and agents through the Amazon Quick by using the browser
                interface. In these cases, this section provides only background information for
                you. You don't directly interact with the IAM service, except if you use IAM to
                sign into Amazon Quick.

**Amazon Quick administrator** – If
                you're in charge of Amazon Quick resources at your company, you probably have
                full access to Amazon Quick. It's your job to determine which Amazon Quick
                features and resources your team members should access. If you have specialized
                requirements that you can't solve by using the Amazon Quick admin panel, then you
                can work with your administrator to create permissions policies for your
                Amazon Quick users. To learn more about IAM, read this page to understand the
                basic concepts of IAM. To learn more about how your company can use IAM with
                Amazon Quick, see [Using Amazon Quick with IAM](https://docs.aws.amazon.com/quicksight/latest/user/security_iam_service-with-iam.html).

**Administrator** – If you're a system
                administrator, you might want to learn details about how you can write policies to
                manage access to Amazon Quick. To view examples of Amazon Quick identity-based
                policies that you can use in IAM, see [IAM identity-based policies for
                Amazon Quick](https://docs.aws.amazon.com/quicksight/latest/user/iam-policy-examples.html#security_iam_id-based-policy-examples).

## Authenticating with identities

            
   
Authentication is how you sign in to AWS using your identity credentials. You must be authenticated as the AWS account root user, an IAM user, or by assuming an IAM role.

You can sign in as a federated identity using credentials from an identity source like AWS IAM Identity Center (IAM Identity Center), single sign-on authentication, or Google/Facebook credentials. For more information about signing in, see [How to sign in to your AWS account](https://docs.aws.amazon.com/signin/latest/userguide/how-to-sign-in.html) in the *AWS Sign-In User Guide*.

For programmatic access, AWS provides an SDK and CLI to cryptographically sign requests. For more information, see [AWS Signature Version 4 for API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) in the *IAM User Guide*.

### AWS account root user

 When you create an AWS account, you begin with one sign-in identity called the AWS account *root user* that has complete access to all AWS services and resources. We strongly recommend that you don't use the root user for everyday tasks. For tasks that require root user credentials, see [Tasks that require root user credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks) in the *IAM User Guide*.
 

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