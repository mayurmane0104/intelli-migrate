# Verified Permissions examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_verifiedpermissions_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_verifiedpermissions_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Verified Permissions.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-identity-source`.

- **AWS CLI**
- 
            
                    **To create an identity source**The following `create-identity-source`example creates an identity source that lets you reference identities stored in the specified Amazon Cognito user pool. Those identities are available in Verified Permissions as entities of type`User`.`aws verifiedpermissions create-identity-source \ --configuration``file://config.txt`\ --principal-entity-type`"User"`\ --policy-store-id`PSEXAMPLEabcdefg111111`Contents of `config.txt`:`{ "cognitoUserPoolConfiguration": { "userPoolArn": "arn:aws:cognito-idp:us-west-2:123456789012:userpool/us-west-2_1a2b3c4d5", "clientIds":["a1b2c3d4e5f6g7h8i9j0kalbmc"] } }`Output: `{ "createdDate": "2023-05-19T20:30:28.214829+00:00", "identitySourceId": "ISEXAMPLEabcdefg111111", "lastUpdatedDate": "2023-05-19T20:30:28.214829+00:00", "policyStoreId": "PSEXAMPLEabcdefg111111" }`For more information about identity sources, see [Using Amazon Verified Permissions with identity providers](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/identity-providers.html)in the*Amazon Verified Permissions User Guide*.- 
                    For API details, see [CreateIdentitySource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/create-identity-source.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-policy-store`.

- **AWS CLI**
- 
            
                    **To create a policy store**The following `create-policy-store`example creates a policy store in the current AWS Region.`aws verifiedpermissions create-policy-store \ --validation-settings``"mode=STRICT"`Output: `{ "arn": "arn:aws:verifiedpermissions::123456789012:policy-store/PSEXAMPLEabcdefg111111", "createdDate": "2023-05-16T17:41:29.103459+00:00", "lastUpdatedDate": "2023-05-16T17:41:29.103459+00:00", "policyStoreId": "PSEXAMPLEabcdefg111111" }`For more information about policy stores, see [Amazon Verified Permissions policy stores](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-stores.html)in the*Amazon Verified Permissions User Guide*.- 
                    For API details, see [CreatePolicyStore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/create-policy-store.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-policy-template`.

- **AWS CLI**
- 
            
                    **To create a policy template**The following `create-policy-template`example creates a policy template with a statement that contains a placeholder for the principal.`aws verifiedpermissions create-policy-template \ --statement``file://template1.txt`\ --policy-store-id`PSEXAMPLEabcdefg111111`Contents of `template1.txt`:`permit( principal in ?principal, action == Action::"view", resource == Photo::"VacationPhoto94.jpg" );`Output: `{ "createdDate": "2023-06-12T20:47:42.804511+00:00", "lastUpdatedDate": "2023-06-12T20:47:42.804511+00:00", "policyStoreId": "PSEXAMPLEabcdefg111111", "policyTemplateId": "PTEXAMPLEabcdefg111111" }`For more information about policy templates, see [Amazon Verified Permissions policy templates](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-templates.html)in the*Amazon Verified Permissions User Guide*.- 
                    For API details, see [CreatePolicyTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/create-policy-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-policy`.

- **AWS CLI**
- 
            
                    **Example 1: To create a static policy**The following `create-policy`example creates a static policy with a policy scope that specifies both a principal and a resource.`aws verifiedpermissions create-policy \ --definition``file://definition1.txt`\ --policy-store-id`PSEXAMPLEabcdefg111111`Contents of file `definition1.txt`:`{ "static": { "description": "Grant everyone of janeFriends UserGroup access to the vacationFolder Album", "statement": "permit(principal in UserGroup::\"janeFriends\", action, resource in Album::\"vacationFolder\" );" } }`Output: `{ "createdDate": "2023-06-12T20:33:37.382907+00:00", "lastUpdatedDate": "2023-06-12T20:33:37.382907+00:00", "policyId": "SPEXAMPLEabcdefg111111", "policyStoreId": "PSEXAMPLEabcdefg111111", "policyType": "STATIC", "principal": { "entityId": "janeFriends", "entityType": "UserGroup" }, "resource": { "entityId": "vacationFolder", "entityType": "Album" } }`**Example 2: To create a static policy that grants access to a resource to everyone**The following `create-policy`example creates a static policy with a policy scope that specifies only a resource.`aws verifiedpermissions create-policy \ --definition``file://definition2.txt`\ --policy-store-id`PSEXAMPLEabcdefg111111`Contents of file `definition2.txt`:`{ "static": { "description": "Grant everyone access to the publicFolder Album", "statement": "permit(principal, action, resource in Album::\"publicFolder\");" } }`Output: `{ "createdDate": "2023-06-12T20:39:44.975897+00:00", "lastUpdatedDate": "2023-06-12T20:39:44.975897+00:00", "policyId": "PbfR73F8oh5MMfr9uRtFDB", "policyStoreId": "PSEXAMPLEabcdefg222222", "policyType": "STATIC", "resource": { "entityId": "publicFolder", "entityType": "Album" } }`**Example 3: To create a template-linked policy that is associated with the specified template**The following `create-policy`example creates a template-linked policy using the specified policy template and associates the specified principal to use with the new template-linked policy.`aws verifiedpermissions create-policy \ --definition``file://definition.txt`\ --policy-store-id`PSEXAMPLEabcdefg111111`Contents of `definition.txt`:`{ "templateLinked": { "policyTemplateId": "PTEXAMPLEabcdefg111111", "principal": { "entityType": "User", "entityId": "alice" } } }`Output: `{ "createdDate": "2023-06-12T20:49:51.490211+00:00", "lastUpdatedDate": "2023-06-12T20:49:51.490211+00:00", "policyId": "TPEXAMPLEabcdefg111111", "policyStoreId": "PSEXAMPLEabcdefg111111", "policyType": "TEMPLATE_LINKED", "principal": { "entityId": "alice", "entityType": "User" }, "resource": { "entityId": "VacationPhoto94.jpg", "entityType": "Photo" } }`For more information about policies, see [Amazon Verified Permissions policies](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policies.html)in the*Amazon Verified Permissions User Guide*.- 
                    For API details, see [CreatePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/create-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-identity-source`.

- **AWS CLI**
- 
            
                    **To delete an identity source**The following `delete-identity-source`example deletes the identity source that has the specified Id.`aws verifiedpermissions delete-identity-source \ --identity-source-id``ISEXAMPLEabcdefg111111`\ --policy-store-id`PSEXAMPLEabcdefg111111`This command produces no output. For more information about identity sources, see [Using Amazon Verified Permissions with identity providers](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/identity-providers.html)in the*Amazon Verified Permissions User Guide*.- 
                    For API details, see [DeleteIdentitySource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/delete-identity-source.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-policy-store`.

- **AWS CLI**
- 
            
                    **To delete a policy store**The following `delete-policy-store`example deletes the policy store that has the specified Id.`aws verifiedpermissions delete-policy-store \ --policy-store-id``PSEXAMPLEabcdefg111111`This command produces no output. For more information about policy stores, see [Amazon Verified Permissions policy stores](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-stores.html)in the*Amazon Verified Permissions User Guide*.- 
                    For API details, see [DeletePolicyStore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/delete-policy-store.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-policy-template`.

- **AWS CLI**
- 
            
                    **To delete a policy template**The following `delete-policy-template`example deletes the policy template that has the specified Id.`aws verifiedpermissions delete-policy-template \ --policy-template-id``PTEXAMPLEabcdefg111111`\ --policy-store-id`PSEXAMPLEabcdefg111111`This command produces no output. For more information about policy templates, see [Amazon Verified Permissions policy templates](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-templates.html)in the*Amazon Verified Permissions User Guide*.- 
                    For API details, see [DeletePolicyTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/delete-policy-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-policy`.

- **AWS CLI**
- 
            
                    **To delete a static or template-linked policy**The following `delete-policy`example deletes the policy that has the specified Id.`aws verifiedpermissions delete-policy \ --policy-id``SPEXAMPLEabcdefg111111`\ --policy-store-id`PSEXAMPLEabcdefg111111`This command produces no output. For more information about policies, see [Amazon Verified Permissions policies](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policies.html)in the*Amazon Verified Permissions User Guide*.- 
                    For API details, see [DeletePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/delete-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-identity-source`.

- **AWS CLI**
- 
            
                    **To retrieve details about an identity source**The following `get-identity-source`example displays the details for the identity source with the specified Id.`aws verifiedpermissions get-identity-source \ --identity-source``ISEXAMPLEabcdefg111111`\ --policy-store-id`PSEXAMPLEabcdefg111111`Output: `{ "createdDate": "2023-06-12T22:27:49.150035+00:00", "details": { "clientIds": [ "a1b2c3d4e5f6g7h8i9j0kalbmc" ], "discoveryUrl": "https://cognito-idp.us-west-2.amazonaws.com/us-west-2_1a2b3c4d5", "openIdIssuer": "COGNITO", "userPoolArn": "arn:aws:cognito-idp:us-west-2:123456789012:userpool/us-west-2_1a2b3c4d5" }, "identitySourceId": "ISEXAMPLEabcdefg111111", "lastUpdatedDate": "2023-06-12T22:27:49.150035+00:00", "policyStoreId": "PSEXAMPLEabcdefg111111", "principalEntityType": "User" }`For more information about identity sources, see [Using Amazon Verified Permissions with identity providers](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/identity-providers.html)in the*Amazon Verified Permissions User Guide*.- 
                    For API details, see [GetIdentitySource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/get-identity-source.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-policy-store`.

- **AWS CLI**
- 
            
                    **To retrieve details about a policy store**The following `get-policy-store`example displays the details for the policy store with the specified Id.`aws verifiedpermissions get-policy-store \ --policy-store-id``PSEXAMPLEabcdefg111111`Output: `{ "arn": "arn:aws:verifiedpermissions::123456789012:policy-store/PSEXAMPLEabcdefg111111", "createdDate": "2023-06-05T20:16:46.225598+00:00", "lastUpdatedDate": "2023-06-08T20:40:23.173691+00:00", "policyStoreId": "PSEXAMPLEabcdefg111111", "validationSettings": { "mode": "OFF" } }`For more information about policy stores, see [Amazon Verified Permissions policy stores](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-stores.html)in the*Amazon Verified Permissions User Guide*.- 
                    For API details, see [GetPolicyStore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/get-policy-store.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-policy-template`.

- **AWS CLI**
- 
            
                    **To retrieve details about a policy template**The following `get-policy-template`example displays the details for the policy template with the specified ID.`aws verifiedpermissions get-policy-template \ --policy-template-id``PTEXAMPLEabcdefg111111`\ --policy-store-id`PSEXAMPLEabcdefg111111`Output: `{ "createdDate": "2023-06-12T20:47:42.804511+00:00", "lastUpdatedDate": "2023-06-12T20:47:42.804511+00:00", "policyStoreId": "PSEXAMPLEabcdefg111111", "policyTemplateId": "PTEXAMPLEabcdefg111111", "statement": "permit(\n principal in ?principal,\n action == Action::\"view\",\n resource == Photo::\"VacationPhoto94.jpg\"\n);" }`For more information about policy templates, see [Amazon Verified Permissions policy templates](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-templates.html)in the*Amazon Verified Permissions User Guide*.- 
                    For API details, see [GetPolicyTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/get-policy-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-policy`.

- **AWS CLI**
- 
            
                    **To retrieve details about a policy**The following `get-policy`example displays the details for the policy with the specified ID.`aws verifiedpermissions get-policy \ --policy-id``PSEXAMPLEabcdefg111111`\ --policy-store-id`PSEXAMPLEabcdefg111111`Output: `{ "createdDate": "2023-06-12T20:33:37.382907+00:00", "definition": { "static": { "description": "Grant everyone of janeFriends UserGroup access to the vacationFolder Album", "statement": "permit(principal in UserGroup::\"janeFriends\", action, resource in Album::\"vacationFolder\" );" } }, "lastUpdatedDate": "2023-06-12T20:33:37.382907+00:00", "policyId": "SPEXAMPLEabcdefg111111", "policyStoreId": "PSEXAMPLEabcdefg111111", "policyType": "STATIC", "principal": { "entityId": "janeFriends", "entityType": "UserGroup" }, "resource": { "entityId": "vacationFolder", "entityType": "Album" } }`For more information about policies, see [Amazon Verified Permissions policies](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policies.html)in the*Amazon Verified Permissions User Guide*.- 
                    For API details, see [GetPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/get-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-schema`.

- **AWS CLI**
- 
            
                    **To retrieve the schema in a policy store**The following `get-schema`example displays the details of the schema in the specified policy store.`aws verifiedpermissions get-schema \ --policy-store-id``PSEXAMPLEabcdefg111111`Output: `{ "policyStoreId": "PSEXAMPLEabcdefg111111", "schema": "{\"MySampleNamespace\":{\"entityTypes\":{\"Employee\":{\"shape\":{\"attributes\":{\"jobLevel\":{\"type\":\"Long\"},\"name\":{\"type\":\"String\"}},\"type\":\"Record\"}}},\"actions\":{\"remoteAccess\":{\"appliesTo\":{\"principalTypes\":[\"Employee\"]}}}}}", "createdDate": "2023-06-14T17:47:13.999885+00:00", "lastUpdatedDate": "2023-06-14T17:47:13.999885+00:00" }`For more information about schema, see [Policy store schema](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/schema.html)in the*Amazon Verified Permissions User Guide*.- 
                    For API details, see [GetSchema](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/get-schema.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `is-authorized-with-token`.

- **AWS CLI**
- 
            
                    **Example 1: To request an authorization decision for a user request (allow)**The following `is-authorized-with-token`example requests an authorization decision for a user who was authenticated by Amazon Cognito. The request uses the identity token provided by Cognito rather than the access token. In this example, the specified information store is configured to return principals as entities of type`CognitoUser`.`aws verifiedpermissions is-authorized-with-token \ --action actionId="View",actionType="Action" \ --resource entityId="vacationPhoto94.jpg",entityType="Photo" \ --policy-store-id``PSEXAMPLEabcdefg111111`\ --identity-token`"AbCdE12345...long.string...54321EdCbA"`The policy store contains a policy with the following statement that accepts identities from the specified Cognito user pool and application Id. `permit( principal == CognitoUser::"us-east-1_1a2b3c4d5|a1b2c3d4e5f6g7h8i9j0kalbmc", action, resource == Photo::"VacationPhoto94.jpg" );`Output: `{ "decision":"Allow", "determiningPolicies":[ { "determiningPolicyId":"SPEXAMPLEabcdefg111111" } ], "errors":[] }`For more information about using identities from a Cognito user pool, see [Using Amazon Verified Permissions with identity providers](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/identity-providers.html)in the*Amazon Verified Permissions User Guide*.- 
                    For API details, see [IsAuthorizedWithToken](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/is-authorized-with-token.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `is-authorized`.

- **AWS CLI**
- 
            
                    **Example 1: To request an authorization decision for a user request (allow)**The following `is-authorized`example requests an authorization decision for a principal of type`User`named`Alice`, who wants to perform the`updatePhoto`operation, on a resource of type`Photo`named`VacationPhoto94.jpg`.The response shows that the request is allowed by one policy. `aws verifiedpermissions is-authorized \ --principal``entityType=User,entityId=alice`\ --action`actionType=Action,actionId=view`\ --resource`entityType=Photo,entityId=VactionPhoto94.jpg`\ --policy-store-id`PSEXAMPLEabcdefg111111`Output: `{ "decision": "ALLOW", "determiningPolicies": [ { "policyId": "SPEXAMPLEabcdefg111111" } ], "errors": [] }`**Example 2: To request an authorization decision for a user request (deny)**The following example is the same as the previous example, except that the principal is `User::"Bob"`. The policy store doesn't contain any policy that allows that user access to`Album::"alice_folder"`.The output indicates that the `Deny`was implicit because the list of`DeterminingPolicies`is empty.`aws verifiedpermissions create-policy \ --definition``file://definition2.txt`\ --policy-store-id`PSEXAMPLEabcdefg111111`Output: `{ "decision": "DENY", "determiningPolicies": [], "errors": [] }`For more information, see the [Amazon Verified Permissions User Guide](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/).- 
                    For API details, see [IsAuthorized](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/is-authorized.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-identity-sources`.

- **AWS CLI**
- 
            
                    **To list the available identity sources**The following `list-identity-sources`example lists all identity sources in the specified policy store.`aws verifiedpermissions list-identity-sources \ --policy-store-id``PSEXAMPLEabcdefg111111`Output: `{ "identitySources": [ { "createdDate": "2023-06-12T22:27:49.150035+00:00", "details": { "clientIds": [ "a1b2c3d4e5f6g7h8i9j0kalbmc" ], "discoveryUrl": "https://cognito-idp.us-west-2.amazonaws.com/us-west-2_1a2b3c4d5", "openIdIssuer": "COGNITO", "userPoolArn": "arn:aws:cognito-idp:us-west-2:123456789012:userpool/us-west-2_1a2b3c4d5" }, "identitySourceId": "ISEXAMPLEabcdefg111111", "lastUpdatedDate": "2023-06-12T22:27:49.150035+00:00", "policyStoreId": "PSEXAMPLEabcdefg111111", "principalEntityType": "User" } ] }`For more information about identity sources, see [Using Amazon Verified Permissions with identity providers](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/identity-providers.html)in the*Amazon Verified Permissions User Guide*.- 
                    For API details, see [ListIdentitySources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/list-identity-sources.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-policies`.

- **AWS CLI**
- 
            
                    **To list the available policies**The following `list-policies`example lists all policies in the specified policy store.`aws verifiedpermissions list-policies \ --policy-store-id``PSEXAMPLEabcdefg111111`Output: `{ "policies": [ { "createdDate": "2023-06-12T20:33:37.382907+00:00", "definition": { "static": { "description": "Grant everyone of janeFriends UserGroup access to the vacationFolder Album" } }, "lastUpdatedDate": "2023-06-12T20:33:37.382907+00:00", "policyId": "SPEXAMPLEabcdefg111111", "policyStoreId": "PSEXAMPLEabcdefg111111", "policyType": "STATIC", "principal": { "entityId": "janeFriends", "entityType": "UserGroup" }, "resource": { "entityId": "vacationFolder", "entityType": "Album" } }, { "createdDate": "2023-06-12T20:39:44.975897+00:00", "definition": { "static": { "description": "Grant everyone access to the publicFolder Album" } }, "lastUpdatedDate": "2023-06-12T20:39:44.975897+00:00", "policyId": "SPEXAMPLEabcdefg222222", "policyStoreId": "PSEXAMPLEabcdefg111111", "policyType": "STATIC", "resource": { "entityId": "publicFolder", "entityType": "Album" } }, { "createdDate": "2023-06-12T20:49:51.490211+00:00", "definition": { "templateLinked": { "policyTemplateId": "PTEXAMPLEabcdefg111111" } }, "lastUpdatedDate": "2023-06-12T20:49:51.490211+00:00", "policyId": "SPEXAMPLEabcdefg333333", "policyStoreId": "PSEXAMPLEabcdefg111111", "policyType": "TEMPLATE_LINKED", "principal": { "entityId": "alice", "entityType": "User" }, "resource": { "entityId": "VacationPhoto94.jpg", "entityType": "Photo" } } ] }`For more information about policies, see [Amazon Verified Permissions policies](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policies.html)in the*Amazon Verified Permissions User Guide*.- 
                    For API details, see [ListPolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/list-policies.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-policy-stores`.

- **AWS CLI**
- 
            
                    **To list the available policy stores**The following `list-policy-stores`example lists all policy stores in the AWS Region. All commands for Verified Permissions except`create-policy-store`and`list-policy-stores`require that you specify the Id of the policy store you want to work with.`aws verifiedpermissions list-policy-stores`Output: `{ "policyStores": [ { "arn": "arn:aws:verifiedpermissions::123456789012:policy-store/PSEXAMPLEabcdefg111111", "createdDate": "2023-06-05T20:16:46.225598+00:00", "policyStoreId": "PSEXAMPLEabcdefg111111" }, { "arn": "arn:aws:verifiedpermissions::123456789012:policy-store/PSEXAMPLEabcdefg222222", "createdDate": "2023-06-08T18:09:37.364356+00:00", "policyStoreId": "PSEXAMPLEabcdefg222222" }, { "arn": "arn:aws:verifiedpermissions::123456789012:policy-store/PSEXAMPLEabcdefg333333", "createdDate": "2023-06-08T18:09:46.920600+00:00", "policyStoreId": "PSEXAMPLEabcdefg333333" } ] }`For more information about policy stores, see [Amazon Verified Permissions policy stores](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-stores.html)in the*Amazon Verified Permissions User Guide*.- 
                    For API details, see [ListPolicyStores](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/list-policy-stores.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-policy-templates`.

- **AWS CLI**
- 
            
                    **To list the available policy templates**The following `list-policy-templates`example lists all policy templates in the specified policy store.`aws verifiedpermissions list-policy-templates \ --policy-store-id``PSEXAMPLEabcdefg111111`Output: `{ "policyTemplates": [ { "createdDate": "2023-06-12T20:47:42.804511+00:00", "lastUpdatedDate": "2023-06-12T20:47:42.804511+00:00", "policyStoreId": "PSEXAMPLEabcdefg111111", "policyTemplateId": "PTEXAMPLEabcdefg111111" } ] }`For more information about policy templates, see [Amazon Verified Permissions policy templates](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-templates.html)in the*Amazon Verified Permissions User Guide*.- 
                    For API details, see [ListPolicyTemplates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/list-policy-templates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-schema`.

- **AWS CLI**
- 
            
                    **To save a schema to a policy store**The following `put-schema`example creates or replaces the schema in the specified policy store.The `cedarJson`parameter in the input file takes a string representation of a JSON object. It contains embedded quotation marks (") within the outermost quotation mark pair. This requires you to convert the JSON to a string by preceding all embedded quotation marks with a backslash character ( " ) and combining all lines into a single text line with no line breaks.Example strings can be displayed wrapped across multiple lines here for readability, but the operation requires the parameters be submitted as single line strings. aws verifiedpermissions put-schema --definition file://schema.txt --policy-store-id PSEXAMPLEabcdefg111111 Contents of `schema.txt`:`{ "cedarJson": "{\"MySampleNamespace\": {\"actions\": {\"remoteAccess\": { \"appliesTo\": {\"principalTypes\": [\"Employee\"]}}},\"entityTypes\": { \"Employee\": {\"shape\": {\"attributes\": {\"jobLevel\": {\"type\": \"Long\"},\"name\": {\"type\": \"String\"}},\"type\": \"Record\"}}}}}" }`Output: `{ "policyStoreId": "PSEXAMPLEabcdefg111111", "namespaces": [ "MySampleNamespace" ], "createdDate": "2023-06-14T17:47:13.999885+00:00", "lastUpdatedDate": "2023-06-14T17:47:13.999885+00:00" }`For more information about schema, see [Policy store schema](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/schema.html)in the*Amazon Verified Permissions User Guide*.- 
                    For API details, see [PutSchema](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/put-schema.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-identity-source`.

- **AWS CLI**
- 
            
                    **To update an identity source**The following `update-identity-source`example modifies the specified identity source by providing a new Cognito user pool configuration and changing the entity type returned by the identity source.`aws verifiedpermissions update-identity-source --identity-source-id``ISEXAMPLEabcdefg111111`\ --update-configuration`file://config.txt`\ --principal-entity-type`"Employee"`\ --policy-store-id`PSEXAMPLEabcdefg111111`Contents of `config.txt`:`{ "cognitoUserPoolConfiguration": { "userPoolArn": "arn:aws:cognito-idp:us-west-2:123456789012:userpool/us-west-2_1a2b3c4d5", "clientIds":["a1b2c3d4e5f6g7h8i9j0kalbmc"] } }`Output: `{ "createdDate": "2023-05-19T20:30:28.214829+00:00", "identitySourceId": "ISEXAMPLEabcdefg111111", "lastUpdatedDate": "2023-05-19T20:30:28.214829+00:00", "policyStoreId": "PSEXAMPLEabcdefg111111" }`For more information about identity sources, see [Using Amazon Verified Permissions with identity providers](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/identity-providers.html)in the*Amazon Verified Permissions User Guide*.- 
                    For API details, see [UpdateIdentitySource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/update-identity-source.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-policy-store`.

- **AWS CLI**
- 
            
                    **To update a policy store**The following `update-policy-store`example modifies a policy store by changing its validation setting.`aws verifiedpermissions update-policy-store \ --validation-settings``"mode=STRICT"`\ --policy-store-id`PSEXAMPLEabcdefg111111`Output: `{ "arn": "arn:aws:verifiedpermissions::123456789012:policy-store/PSEXAMPLEabcdefg111111", "createdDate": "2023-05-16T17:41:29.103459+00:00", "lastUpdatedDate": "2023-05-16T17:41:29.103459+00:00", "policyStoreId": "PSEXAMPLEabcdefg111111" }`For more information about policy stores, see [Amazon Verified Permissions policy stores](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-stores.html)in the*Amazon Verified Permissions User Guide*.- 
                    For API details, see [UpdatePolicyStore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/update-policy-store.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-policy-template`.

- **AWS CLI**
- 
            
                    **Example 1: To update a policy template**The following `update-policy-template`example modifies the specified template-linked policy to replace its policy statement.`aws verifiedpermissions update-policy-template \ --policy-template-id``PTEXAMPLEabcdefg111111`\ --statement`file://template1.txt`\ --policy-store-id`PSEXAMPLEabcdefg111111`Contents of file `template1.txt`:`permit( principal in ?principal, action == Action::"view", resource == Photo::"VacationPhoto94.jpg" );`Output: `{ "createdDate": "2023-06-12T20:47:42.804511+00:00", "lastUpdatedDate": "2023-06-12T20:47:42.804511+00:00", "policyStoreId": "PSEXAMPLEabcdefg111111", "policyTemplateId": "PTEXAMPLEabcdefg111111" }`For more information about policy templates, see [Amazon Verified Permissions policy templates](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policy-templates.html)in the*Amazon Verified Permissions User Guide*.- 
                    For API details, see [UpdatePolicyTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/update-policy-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-policy`.

- **AWS CLI**
- 
            
                    **To update a static policy**The following `update-policy`example modifies an existing static policy by updating its description and statement.`aws verifiedpermissions update-policy \ --policy-id``SPEXAMPLEabcdefg111111`\ --definition`file://updated-definition.txt`\ --policy-store-id`PSEXAMPLEabcdefg111111`The `statement`parameter takes a string representation of a JSON object. It contains embedded quotation marks (") within the outermost quotation mark pair. This requires you to convert the JSON to a string by preceding all embedded quotation marks with a backslash character ( " ) and combining all lines into a single text line with no line breaks.You can display example strings wrapped across multiple lines for readability, but the operation requires the parameters to be submitted as single-line strings. Contents of file `updated-definition.txt`:`{ "static": { "description": "Updated policy to grant janeFriends UserGroup access to the vacationFolder Album with view action only", "statement": "permit(principal in UserGroup::\"janeFriends\", action == Action::\"view\", resource in Album::\"vacationFolder\" );" } }`Output: `{ "createdDate": "2023-06-12T20:33:37.382907+00:00", "lastUpdatedDate": "2023-06-12T20:33:37.382907+00:00", "policyId": "SPEXAMPLEabcdefg111111", "policyStoreId": "PSEXAMPLEabcdefg111111", "policyType": "STATIC", "principal": { "entityId": "janeFriends", "entityType": "UserGroup" }, "resource": { "entityId": "vacationFolder", "entityType": "Album" } }`For more information about policies, see [Amazon Verified Permissions policies](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/policies.html)in the*Amazon Verified Permissions User Guide*.- 
                    For API details, see [UpdatePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/update-policy.html)in*AWS CLI Command Reference*.
 
-