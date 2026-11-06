# IAM federation - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/iam-federation.html](https://docs.aws.amazon.com/quick/latest/userguide/iam-federation.html)

---

| Applies
                    to:Enterprise Edition and Standard Edition | 

| Intended audience: System administrators | 

###### Important

Amazon Quick recommends that you integrate new Amazon Quick subscriptions with IAM Identity Center
            for identity management. This IAM identity federation user guide is provided as a
            reference for existing account configurations. For more information on integrating your
            Amazon Quick account with IAM Identity Center, see [Configure your Amazon Quick account with IAM Identity Center](https://docs.aws.amazon.com/quicksight/latest/user/sec-identity-management-identity-center.html).

###### Note

IAM identity federation doesn't support syncing identity provider groups with Amazon Quick.

Amazon Quick supports identity federation in both Standard and Enterprise editions. When you use federated users, you can manage users with your enterprise identity provider (IdP) and use AWS Identity and Access Management (IAM) to authenticate users when they sign in to Quick. You can use a third-party identity provider that supports Security Assertion Markup Language 2.0 (SAML 2.0) to provide an onboarding flow for your Amazon Quick users. Such identity providers include Microsoft Active Directory Federation Services, Okta, and Ping One Federation Server. With identity federation, your users get one-click access to their Amazon Quick applications using their existing identity credentials. You also have the security benefit of identity authentication by your identity provider. You can control which users have access to Amazon Quick using your existing identity provider.