# Using IAM Identity Center - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/setting-up-sso.html](https://docs.aws.amazon.com/quick/latest/userguide/setting-up-sso.html)

---

| Applies
                    to:Enterprise Edition and Standard Edition | 

| Intended audience: System administrators and Amazon Quick administrators | 

Amazon Quick Enterprise edition integrates with your existing directories, using either Microsoft Active Directory or single sign-on (IAM Identity Center) using Security Assertion Markup Language (SAML). You can use AWS Identity and Access Management (IAM) to further enhance your security, or for custom options such as embedding dashboards.

In Quick Standard edition, you can manage users entirely within Quick. If you prefer, you can integrate with your existing users, groups, and roles in IAM.

You can use the following tools for identity and access to Amazon Quick:

- 
            [IAM Identity Center](https://docs.aws.amazon.com/quicksight/latest/user/sec-identity-management-identity-center.html)(Enterprise edition only)
- 
            [IAM federation](https://docs.aws.amazon.com/quicksuite/latest/userguide/iam-federation.html)(Standard and Enterprise editions)
- 
            [AWS Directory Service for Microsoft Active Directory](https://docs.aws.amazon.com/quicksight/latest/user/aws-directory-service.html)(Enterprise edition only)
- 
            [SAML-based single sign-on](https://docs.aws.amazon.com/quicksight/latest/user/external-identity-providers.html)(Standard and Enterprise edition)
- 
            [Multifactor authentication (MFA)](https://docs.aws.amazon.com/quicksight/latest/user/using-multi-factor-authentication-mfa.html)(Standard and Enterprise edition)

###### Note

In the regions listed below, Amazon Quick accounts can only use [IAM Identity Center](https://docs.aws.amazon.com/quicksight/latest/user/sec-identity-management-identity-center.html) for identity and access management.

- 
                `af-south-1`Africa (Cape Town)
- 
                `ap-southeast-3`Asia Pacific (Jakarta)
- 
                `ap-southeast-5`Asia Pacific (Malaysia)
- 
                `eu-south-1`Europe (Milan)
- 
                `eu-central-2`Europe (Zurich)

IAM Identity Center helps you securely create or connect your workforce identities and manage their access across AWS accounts and applications.

Before you integrate your Amazon Quick account with IAM Identity Center, set up IAM Identity Center in your AWS
        account. If you haven't set up IAM Identity Center in your AWS organization, see [Getting
            started](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html) in the *AWS IAM Identity Center User Guide*.

If you want to configure an external identity provider with IAM Identity Center, see [Supported
            identity providers](https://docs.aws.amazon.com/singlesignon/latest/userguide/supported-idps.html) to view a list of supported identity providers'
        configuration steps.

## Configure your Amazon Quick account with IAM Identity Center

        | Applies
                    to:Enterprise Edition | 

| Intended audience: System administrators | 

IAM Identity Center helps you securely create or configure your existing workforce identities and
            manage their access across AWS accounts and applications. IAM Identity Center is the recommended
            approach for workforce authentication and authorization on AWS for organizations of
            any size and type. To learn more about IAM Identity Center, see [AWS IAM Identity Center](https://aws.amazon.com//iam/identity-center/).

Configure Amazon Quick and IAM Identity Center so that you can sign up for a new Amazon Quick account with an IAM Identity Center configured identity source. With IAM Identity Center, you can configure your external identity provider as an identity source. You can also use IAM Identity Center as an identity store if you don't want to use a third-party identity provider with Amazon Quick. Identity methods can't be changed after your account is created.

When you integrate your Amazon Quick account with IAM Identity Center, Amazon Quick account administrators can create a new Amazon Quick account that automatically has the identity provider's groups available. This simplifies asset sharing at scale in Amazon Quick.

Access to some sections of the Amazon Quick administration console is restricted by IAM permissions. The following table summarizes the admin actions that you can perform in Amazon Quick based on the access type that you choose.

To learn more how to sign up for an Amazon Quick account with IAM Identity Center, see [Signing up for an
                Amazon Quick subscription](https://docs.aws.amazon.com/quicksight/latest/user/signing-up.html).

| Admin action | IAM permissions | Amazon Quick admin role permissions | 
|---|---|---|
| 
 |  |  | 
| 
 |  |  | 
| 
 |  |  | 
| 
 |  |  | 
| 
 |  |  | 
| 
 |  |  | 
| 
 |  |  | 
| 
 |  |  | 
| 
 |  |  | 
| 
 |  |  | 
| 
 |  |  | 

The Amazon Quick mobile app is not supported with Amazon Quick accounts that are integrated with IAM Identity Center.

### Considerations

The following actions permanently remove the ability for Amazon Quick users to sign into Amazon Quick. Amazon Quick does not recommend that Amazon Quick users perform these actions.

- 
                    Disabling or deleting the Amazon Quick application in the IAM Identity Center console. If you want to delete your Amazon Quick account, see [Closing your Amazon Quick account](https://docs.aws.amazon.com/quicksight/latest/user/closing-account.html).
- 
                    Migrating the Amazon Quick account that contains your IAM Identity Center configuration to an AWS Organization that does not contain the IAM Identity Center instance that your Amazon Quick account is configured to. 
- 
                    Deleting the IAM Identity Center instance that is configured to your Amazon Quick account. 
- 
                    Editing IAM Identity Center application attributes, for example the **requires assignment**attribute.