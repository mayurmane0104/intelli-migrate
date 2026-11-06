# Amazon Cognito Identity examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_cognito-identity_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_cognito-identity_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon Cognito Identity.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-identity-pool`.

- **AWS CLI**
- 
            
                    **To create an identity pool with Cognito identity pool provider**This example creates an identity pool named MyIdentityPool. It has a Cognito identity pool provider. Unauthenticated identities are not allowed. Command: `aws cognito-identity create-identity-pool --identity-pool-name``MyIdentityPool`--no-allow-unauthenticated-identities --cognito-identity-providers ProviderName="cognito-idp.us-west-2.amazonaws.com/us-west-2_aaaaaaaaa",ClientId="3n4b5urk1ft4fl3mg5e62d9ado",ServerSideTokenCheck=falseOutput: `{ "IdentityPoolId": "us-west-2:11111111-1111-1111-1111-111111111111", "IdentityPoolName": "MyIdentityPool", "AllowUnauthenticatedIdentities": false, "CognitoIdentityProviders": [ { "ProviderName": "cognito-idp.us-west-2.amazonaws.com/us-west-2_111111111", "ClientId": "3n4b5urk1ft4fl3mg5e62d9ado", "ServerSideTokenCheck": false } ] }`- 
                    For API details, see [CreateIdentityPool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/create-identity-pool.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-identities`.

- **AWS CLI**
- 
            
                    **To delete an identity**This example deletes an identity from an identity pool. Command: `aws cognito-identity delete-identities --identity-ids-to-delete``"us-west-2:11111111-1111-1111-1111-111111111111"`Output: `{ "UnprocessedIdentityIds": [] }`- 
                    For API details, see [DeleteIdentities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/delete-identities.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-identity-pool`.

- **AWS CLI**
- 
            
                    **To delete identity pool**The following `delete-identity-pool`example deletes the specified identity pool.Command: `aws cognito-identity delete-identity-pool \ --identity-pool-id``"us-west-2:11111111-1111-1111-1111-111111111111"`This command produces no output. - 
                    For API details, see [DeleteIdentityPool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/delete-identity-pool.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-identity-pool`.

- **AWS CLI**
- 
            
                    **To describe an identity pool**This example describes an identity pool. Command: `aws cognito-identity describe-identity-pool --identity-pool-id``"us-west-2:11111111-1111-1111-1111-111111111111"`Output: `{ "IdentityPoolId": "us-west-2:11111111-1111-1111-1111-111111111111", "IdentityPoolName": "MyIdentityPool", "AllowUnauthenticatedIdentities": false, "CognitoIdentityProviders": [ { "ProviderName": "cognito-idp.us-west-2.amazonaws.com/us-west-2_111111111", "ClientId": "3n4b5urk1ft4fl3mg5e62d9ado", "ServerSideTokenCheck": false } ] }`- 
                    For API details, see [DescribeIdentityPool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/describe-identity-pool.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-identity-pool-roles`.

- **AWS CLI**
- 
            
                    **To get identity pool roles**This example gets identity pool roles. Command: `aws cognito-identity get-identity-pool-roles --identity-pool-id``"us-west-2:11111111-1111-1111-1111-111111111111"`Output: `{ "IdentityPoolId": "us-west-2:11111111-1111-1111-1111-111111111111", "Roles": { "authenticated": "arn:aws:iam::111111111111:role/Cognito_MyIdentityPoolAuth_Role", "unauthenticated": "arn:aws:iam::111111111111:role/Cognito_MyIdentityPoolUnauth_Role" } }`- 
                    For API details, see [GetIdentityPoolRoles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/get-identity-pool-roles.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-identity-pools`.

- **AWS CLI**
- 
            
                    **To list identity pools**This example lists identity pools. There s a maximum of 20 identities listed. Command: `aws cognito-identity list-identity-pools --max-results``20`Output: `{ "IdentityPools": [ { "IdentityPoolId": "us-west-2:11111111-1111-1111-1111-111111111111", "IdentityPoolName": "MyIdentityPool" }, { "IdentityPoolId": "us-west-2:11111111-1111-1111-1111-111111111111", "IdentityPoolName": "AnotherIdentityPool" }, { "IdentityPoolId": "us-west-2:11111111-1111-1111-1111-111111111111", "IdentityPoolName": "IdentityPoolRegionA" } ] }`- 
                    For API details, see [ListIdentityPools](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/list-identity-pools.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-identity-pool-roles`.

- **AWS CLI**
- 
            
                    **To set identity pool roles**The following `set-identity-pool-roles`example sets an identity pool role.`aws cognito-identity set-identity-pool-roles \ --identity-pool-id``"us-west-2:11111111-1111-1111-1111-111111111111"`\ --roles authenticated="arn:aws:iam::111111111111:role/Cognito_MyIdentityPoolAuth_Role"- 
                    For API details, see [SetIdentityPoolRoles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/set-identity-pool-roles.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-identity-pool`.

- **AWS CLI**
- 
            
                    **To update an identity pool**This example updates an identity pool. It sets the name to MyIdentityPool. It adds Cognito as an identity provider. It disallows unauthenticated identities. Command: `aws cognito-identity update-identity-pool --identity-pool-id``"us-west-2:11111111-1111-1111-1111-111111111111"`--identity-pool-name`"MyIdentityPool"`--no-allow-unauthenticated-identities --cognito-identity-providers ProviderName="cognito-idp.us-west-2.amazonaws.com/us-west-2_111111111",ClientId="3n4b5urk1ft4fl3mg5e62d9ado",ServerSideTokenCheck=falseOutput: `{ "IdentityPoolId": "us-west-2:11111111-1111-1111-1111-111111111111", "IdentityPoolName": "MyIdentityPool", "AllowUnauthenticatedIdentities": false, "CognitoIdentityProviders": [ { "ProviderName": "cognito-idp.us-west-2.amazonaws.com/us-west-2_111111111", "ClientId": "3n4b5urk1ft4fl3mg5e62d9ado", "ServerSideTokenCheck": false } ] }`- 
                    For API details, see [UpdateIdentityPool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-identity/update-identity-pool.html)in*AWS CLI Command Reference*.
 
-