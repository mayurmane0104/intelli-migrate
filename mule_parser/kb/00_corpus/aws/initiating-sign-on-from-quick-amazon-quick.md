# Initiating sign-on from Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/federated-identities-sp-to-idp.html](https://docs.aws.amazon.com/quick/latest/userguide/federated-identities-sp-to-idp.html)

---

| Applies
                    to:Enterprise Edition | 

| Intended audience: System administrators | 

###### Note

IAM identity federation doesn't support syncing identity provider groups with Amazon Quick.

In this scenario, your user initiates the sign-on process from an Amazon Quick application portal without being signed on to the identity provider. In this case, the user has a federated account managed by a third-party IdP. The user might have a user account on Quick. Quick sends an authentication request to the IdP. After the user is authenticated, Quick opens.

Beginning with the user signing into Quick, authentication flows through these steps:

- 
                The user opens Quick. At this point, the user isn't signed in to the IdP. 
- 
                The user attempts to sign in to Amazon Quick. 
- 
                Amazon Quick redirects the user's input to the federation service and requests authentication. 
- 
                The federation service and the IdP authenticate the user: - 
                        The federation service requests authentication from the organization's identity store. 
- 
                        The identity store authenticates the user and returns the authentication response to the federation service. 
- 
                        When authentication is successful, the federation service posts the SAML assertion to the user's browser. 
- 
                        The user's browser posts the SAML assertion to the AWS Sign-In SAML endpoint ( `https://signin.aws.amazon.com/saml`).
- 
                        AWS Sign-In receives the SAML request, processes the request, authenticates the user, and forwards the authentication token to the Amazon Quick service. 
 
- 
                        
- 
                Amazon Quick accepts the authentication token from AWS and presents Amazon Quick to the user. 

From the user's perspective, the process happens transparently. The user starts at an Amazon Quick application portal. Amazon Quick negotiates authentication with your organization's federation service and AWS. Amazon Quick opens, without the user needing to supply any additional credentials.