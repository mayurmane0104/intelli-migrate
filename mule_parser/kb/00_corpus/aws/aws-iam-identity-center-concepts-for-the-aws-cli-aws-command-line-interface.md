# AWS IAM Identity Center concepts for the AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso-concepts.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso-concepts.html)

---

This topic describes the key concepts of AWS IAM Identity Center (IAM Identity Center). IAM Identity Center is a cloud-based IAM service that simplifies user access management across multiple AWS accounts, applications, SDKs, and tools by integrating with existing identity providers (IdP). It enables secure single sign-on, permission management, and auditing through a centralized user portal, streamlining identity and access governance for organizations.

## What is IAM Identity Center

        IAM Identity Center is a cloud-based identity and access management (IAM) service that enables you to centrally manage access to multiple AWS accounts and business applications.

It provides a user portal where authorized users can access the AWS accounts and applications they've been granted permission to, using their existing corporate credentials. This allows organizations to enforce consistent security policies and streamline user access management.

Regardless of which IdP you use, IAM Identity Center abstracts those distinctions away. For example,
            you can connect Microsoft Azure AD as described in the blog article [The Next
                Evolution in IAM Identity Center](https://aws.amazon.com/blogs/aws/the-next-evolution-in-aws-single-sign-on/).

###### Note

For information on using bearer auth, which uses no account ID and role, see
                    [Setting up to use the AWS CLI with CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/set-up-cli.html) in the *Amazon CodeCatalyst User Guide*.

## Terms

        Common terms when using IAM Identity Center are as follows:

- **Identity Provider (IdP)**
- 
                    An identity management system such as IAM Identity Center, Microsoft Azure AD, Okta, or your own corporate directory service. 
- **AWS IAM Identity Center**
- 
                    IAM Identity Center is the AWS owned IdP service. Formerly known as AWS Single Sign-On, SDKs and tools keep the `sso`API namespaces for backward compatibility. For more information, see[IAM Identity Center rename](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html#renamed)in the*AWS IAM Identity Center User Guide*.
- **AWS access portal URL, SSO start URL, Start URL**
- 
                    Your organization's unique IAM Identity Center URL to access your authorized AWS accounts, services, and resources. 
- **Issuer URL**
- 
                    Your organization's unique IAM Identity Center issuer URL for programmatic access for your authorized AWS accounts, services, and resources. Starting with version 2.22.0 of the AWS CLI, issuer URL can be used interchangeably with the start URL. 
- **Federation**
- 
                    The process of establishing trust between IAM Identity Center and an identity provider to enable single sign-on (SSO). 
- **AWS accounts**
- 
                    The AWS accounts that you provide users access to through AWS IAM Identity Center. 
- **Permission sets, AWS credentials, credentials, sigv4 credentials**
- 
                    Predefined collections of permissions that can be assigned to users or groups to grant access to AWS services. 
- **Registration scopes, access scopes, scopes**
- 
                    Scopes are a mechanism in OAuth 2.0 to limit an application's access to a user's account. An application can request one or more scopes, and the access token issued to the application is limited to the scopes granted. For information on scopes, see [Access scopes](https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps-saml2-oauth2.html#oidc-concept)in the*IAM Identity Center User Guide*.
- **Tokens, refresh token, access token**
- 
                    Tokens are temporary security credentials that are issued to you upon authentication. These tokens contain information about your identity and the permissions you've been granted. When you access an AWS resource or application through the IAM Identity Center portal, your token is presented to AWS for authentication and authorization. This allows AWS to verify your identity and ensure you have the necessary permissions to perform your requested actions. The authentication token is cached to disk under the `~/.aws/sso/cache`directory with a JSON filename based on the session name.
- **Session**
- 
                    An IAM Identity Center session refers to the period of time that a user is authenticated and authorized to access AWS resources or applications. When a user signs in to the IAM Identity Center portal, a session is established, and the user's token is valid for a specified duration. For more information on setting session durations, see [Set session duration](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtosessionduration.html)in the*AWS IAM Identity Center User Guide*.During the session, you can navigate between different AWS accounts and applications without having to re-authenticate, as long as their session remains active. When the session expires, sign in again to renew your access. IAM Identity Center sessions help to provide a seamless user experience while also enforcing security best practices by limiting the validity of user access credentials. 
- **Authorization code grant with PKCE, PKCE, Proof Key for Code Exchange**
- 
                    Starting with version 2.22.0, Proof Key for Code Exchange (PKCE) is an OAuth 2.0 authentication grant flow for devices with a browser. PKCE is a simple and safe way to authenticate and obtain consent to access your AWS resources from desktops and mobile devices with web browsers. This is the default authorization behavior. For more information on PKCE, see [Authorization Code Grant with PKCE](https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps-saml2-oauth2.html#auth-code-grant-pkce)in the*AWS IAM Identity Center User Guide*.
- **Device authorization grant**
- 
                    An OAuth 2.0 authentication grant flow for devices with or without a web browser. For more information on setting session durations, see [Device Authorization Grant](https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps-saml2-oauth2.html#device-auth-grant)in the*AWS IAM Identity Center User Guide*.

## How IAM Identity Center works

        IAM Identity Center integrates with your organization's identity provider, such as IAM Identity Center, Microsoft Azure AD, or Okta. Users authenticate against this identity provider, and IAM Identity Center then maps those identities to the appropriate permissions and access within your AWS environment.

The following IAM Identity Center workflow assumes you have already configured your AWS CLI to use IAM Identity Center:

- 
                In your preferred terminal, run the `aws sso login`command.
- 
                Sign in to your AWS access portal to start a new session. - 
                        When you start a new session, you receive a refresh token and access token that is cached. 
- 
                        If you already have an active session, the existing session is reused and expires when the existing session expires. 
 
- 
                        
- 
                Based on the profile you've set up in your `config`file, IAM Identity Center assumes the appropriate permission sets, granting access to the relevant AWS accounts and applications.
- 
                The AWS CLI, SDKs, and Tools use your assumed IAM role to make calls to AWS services such as creating Amazon S3 buckets until that session expires. 
- 
                The access token from IAM Identity Center is checked hourly and is automatically refreshed using the refresh token. - 
                        If the access token is expired, the SDK or tool uses the refresh token to get a new access token. These tokens' session durations are then compared, and if the refresh token is not expired IAM Identity Center provides a new access token. 
- 
                        If the refresh token has expired, then no new access tokens are provided and your session has ended. 
 
- 
                        
- 
                Sessions end after refresh tokens expire, or when you manually log out using the `aws sso logout`command. Cached credentials are removed. To continue accessing services using IAM Identity Center, you must start a new session using the the`aws sso login`command.

## Additional resources

        Additional resources are as follows.

- 
                [Configuring IAM Identity Center authentication with the AWS CLI](./cli-configure-sso.html)
- 
                [Tutorial: Using IAM Identity Center to run Amazon S3 commands in the AWS CLI](./cli-configure-sso-tutorial.html)
- 
                `aws configure sso`*AWS CLI version 2 Reference*
- 
                `aws configure sso-session`*AWS CLI version 2 Reference*
- 
                `aws sso login`*AWS CLI version 2 Reference*
- 
                `aws sso logout`*AWS CLI version 2 Reference*
- 
                [Setting up to use the AWS CLI with CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/set-up-cli.html)in the*Amazon CodeCatalyst User Guide*
- 
                [IAM Identity Center rename](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html#renamed)in the*AWS IAM Identity Center User Guide*
- 
                [OAuth 2.0 Access scopes](https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps-saml2-oauth2.html#oidc-concept)in the*IAM Identity Center User Guide*
- 
                [Set session duration](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtosessionduration.html)in the*AWS IAM Identity Center User Guide*
- 
                [Getting started tutorials](https://docs.aws.amazon.com/singlesignon/latest/userguide/tutorials.html)in the*IAM Identity Center User Guide*