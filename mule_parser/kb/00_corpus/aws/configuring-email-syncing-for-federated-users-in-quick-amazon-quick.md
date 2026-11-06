# Configuring email syncing for federated users in Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/jit-email-syncing.html](https://docs.aws.amazon.com/quick/latest/userguide/jit-email-syncing.html)

---

| Applies
                    to:Enterprise Edition | 

| Intended audience: System administrators and Amazon Quick administrators | 

###### Note

IAM identity federation doesn't support syncing identity provider groups with Amazon Quick.

In Amazon Quick Enterprise edition, as an administrator you can restrict new users from using personal email addresses when provisioning through their identity provider (IdP) directly to Quick. Quick then uses the preconfigured email addresses passed through the IdP when provisioning new users to your account. For example, you can make it so that only corporate-assigned email addresses are used when users are provisioned to your Amazon Quick account through your IdP.

###### Note

Make sure that your users are federating directly to Amazon Quick through their IdP. Federating to the AWS Management Console through their IdP and then clicking into Amazon Quick results in an error and they won't be able to access Amazon Quick.

When you configure email syncing for federated users in Amazon Quick, users who log in to your Amazon Quick account for the first time have preassigned email addresses. These are used to register their accounts. With this approach, users can manually bypass by entering an email address. Also, users can't use an email address that might differ from the email address prescribed by you, the administrator.

Amazon Quick supports provisioning through an IdP that supports SAML or OpenID Connect
            (OIDC) authentication. To configure email addresses for new users when provisioning
            through an IdP, you update the trust relationship for the IAM role that they use with
                `AssumeRoleWithSAML` or `AssumeRoleWithWebIdentity`. Then you
            add a SAML attribute or OIDC token in their IdP. Last, you turn on email syncing for
            federated users in Amazon Quick.

The following procedures describe these steps in detail.

## Step 1: Update the trust relationship for the IAM role with AssumeRoleWithSAML or AssumeRoleWithWebIdentity

            You can configure email addresses for your users to use when provisioning through
                your IdP to Amazon Quick. To do this, add the `sts:TagSession` action to
                the trust relationship for the IAM role that you use with
                    `AssumeRoleWithSAML` or `AssumeRoleWithWebIdentity`. By
                doing this, you can pass in `principal` tags when users assume the
                role.

The following example illustrates an updated IAM role where the IdP is Okta. To
                use this example, update the `Federated` Amazon Resource Name (ARN) with
                the ARN for your service provider. You can replace items in red with your AWS and
                IdP service-specific information.

`{ "Version": "2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "Federated": "arn:aws:iam::``account-id`:`saml-provider`/`Okta`" }, "Action": "sts:AssumeRoleWithSAML", "Condition": { "StringEquals": { "SAML:aud": "https://signin.aws.amazon.com/saml" } } }, { "Effect": "Allow", "Principal": { "Federated": "arn:aws:iam::`account-id`:`saml-provider`/`Okta`" }, "Action": "sts:TagSession", "Condition": { "StringLike": { "aws:RequestTag/Email": "*" } } } ] }

## Step 2: Add a SAML attribute or OIDC token for the IAM principal tag in your IdP

            After you update the trust relationship for the IAM role as described in the
                preceding section, add a SAML attribute or OIDC token for the IAM
                    `Principal` tag in your IdP.

The following examples illustrate a SAML attribute and an OIDC token. To use these examples, replace the email address with a variable in your IdP that points to a user's email address. You can replace items highlighted in red with your information.

- 
                    **SAML attribute**: The following example illustrates a SAML attribute.`<Attribute Name="https://aws.amazon.com/SAML/Attributes/PrincipalTag:Email"><AttributeValue>``john.doe@example.com`</AttributeValue></Attribute>###### NoteIf you're using Okta as your IdP, make sure to turn on a feature flag in your Okta user account to use SAML. For more information, see [Okta and AWS Partner to Simplify Access Via Session Tags](https://www.okta.com/blog/2019/11/okta-and-aws-partner-to-simplify-access-via-session-tags/)on the Okta blog.
- 
                    **OIDC token**: The following example illustrates an OIDC token example.`"https://aws.amazon.com/tags": {"principal_tags": {"Email": ["``john.doe@example.com`"]

## Step 3: Turn on email syncing for federated users in Amazon Quick

            As described preceding, update the trust relationship for the IAM role and add a
                SAML attribute or OIDC token for the IAM `Principal` tag in your IdP.
                Then turn on email syncing for federated users in Amazon Quick as described in the
                following procedure.

###### To turn on email syncing for federated users

- 
                    From any page in Amazon Quick, choose your username at top right, and then choose **Manage Amazon Quick**.
- 
                    Choose **Single sign-on (IAM federation)**in the menu at left.
- 
                    On the **Service Provider Initiated IAM federation**page, for**Email Syncing for Federated Users**, choose**ON**.When email syncing for federated users is on, Amazon Quick uses the email addresses that you configured in steps 1 and 2 when provisioning new users to your account. Users can't enter their own email addresses. When email syncing for federated users is off, Amazon Quick asks users to input their email address manually when provisioning new users to your account. They can use any email addresses that they want.