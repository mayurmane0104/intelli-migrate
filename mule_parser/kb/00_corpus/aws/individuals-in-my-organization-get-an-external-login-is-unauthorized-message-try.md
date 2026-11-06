# Individuals in my organization get an "External Login is Unauthorized" message when they try to access Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/troubleshoot-webidentity-federation.html](https://docs.aws.amazon.com/quick/latest/userguide/troubleshoot-webidentity-federation.html)

---

| Intended audience: Amazon Quick administrators | 

When an individual in your organization is federating into Quick Sight using
					**AssumeRoleWithWebIdentity**, Quick Sight maps a single
				role-based user to a single external login. In some cases, that individual might be
				authenticated through an external login (such as Amazon Cognito) that's different from
				the originally mapped user. If so, they can't access Quick Sight and get the
				following unexpected error message.

The external login used for federation is unauthorized for the Quick Sight user.

To learn how to troubleshoot this issue, see the following sections:

## Why is this happening?

				 
					### You are using a simplified Amazon Cognito flow

If you're using Amazon Cognito to federate into Quick Sight, the single
						sign-on (IAM Identity Center) setup might use the `CognitoIdentityCredentials`
						API operation to assume the Quick Sight role. This method maps all users in
						the Amazon Cognito identity pool to a single Quick Sight user and isn't
						supported by Quick Sight.

We recommend that you use the `AssumeRoleWithWebIdentity` API
						operation instead, which specifies the role session name.

### You're using unauthenticated Amazon Cognito users

Amazon Cognito IAM Identity Center is set up for unauthenticated users in the Amazon Cognito identity pool. The Quick Sight role trust policy is set up like the following example.

This setup allows a temporary Amazon Cognito user to assume a role session mapped to a unique Quick Sight user. Because unauthenticated identities are temporary, they aren't supported by Quick Sight.

We recommend that you don't use this setup, which setup isn't supported by Quick Sight. For Quick Sight, make sure that the Amazon Cognito IAM Identity Center uses authenticated users.

### You deleted and recreated an Amazon Cognito user with the same user name attributes

In this case, the associated Amazon Cognito user that's mapped to the Quick Sight user was deleted and recreated. The newly created Amazon Cognito user has a different underlying subject. Depending on how the role session name is mapped to the Quick Sight user, the session name might correspond to the same Quick Sight role-based user.

We recommend that you remap the Quick Sight user to the updated Amazon Cognito
						user subject by using the `UpdateUser` API operation. For more
						information, see the following [UpdateUser API example](#troubleshoot-webidentity-federation-solutions-updateuser).

### You're mapping multiple Amazon Cognito user pools in different AWS accounts to one identity pool and with Quick Sight

Mapping multiple Amazon Cognito user pools in different AWS accounts to one identity pool and Quick Sight isn't supported by Quick Sight.

## How can I fix it?

				You can use Quick Sight public API operations to update the external login information for your users. Use the following options to learn how.

### Use RegisterUser to create users with external login information

If the external login provider is Amazon Cognito, use the following CLI code to create users.

`aws quicksight register-user --aws-account-id``account-id`--namespace`namespace`--email`user-email`--user-role`user-role`--identity-type IAM --iam-arn arn:aws:iam::`account-id`:role/`cognito-associated-iam-role`--session-name`cognito-username`--external-login-federation-provider-type COGNITO --external-login-id`cognito-identity-id`--region`identity-region`

The `external-login-id` should be the identity ID for the
						Amazon Cognito user. The format is
							`<identity-region>:<cognito-user-sub>`, as shown
						in the following example.

`aws quicksight register-user --aws-account-id 111222333 --namespace default --email cognito-user@amazon.com --user-role ADMIN --identity-type IAM --iam-arn arn:aws:iam::111222333:role/CognitoQuickSightRole --session-name cognito-user --external-login-federation-provider-type COGNITO --external-login-id us-east-1:12345678-1234-1234-abc1-a1b1234567 --region us-east-1`

If the external login provider is a custom OpenID Connect (OIDC) provider, use the following CLI code to create users.

`aws quicksight register-user --aws-account-id``account-id`--namespace`namespace`--email`user-email`--user-role`user-role`--identity-type IAM --iam-arn arn:aws:iam::`account-id`:role/`identity-provider-associated-iam-role`--session-name`identity-username`--external-login-federation-provider-type CUSTOM_OIDC --custom-federation-provider-url`custom-identity-provider-url`--external-login-id`custom-provider-identity-id`--region`identity-region`

The following is an example.

`aws quicksight register-user --aws-account-id 111222333 --namespace default --email identity-user@amazon.com --user-role ADMIN --identity-type IAM --iam-arn arn:aws:iam::111222333:role/CustomIdentityQuickSightRole --session-name identity-user --external-login-federation-provider-type CUSTOM_OIDC --custom-federation-provider-url idp.us-east-1.amazonaws.com/us-east-1_ABCDE --external-login-id 12345678-1234-1234-abc1-a1b1234567 --region us-east-1`

To learn more about using `RegisterUser` in the CLI, see [RegisterUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RegisterUser.html) in the *Amazon Quick API Reference*.

### Use DescribeUser to check external login information for users

If a user is a role-based federated user from an external login provider,
						use the `DescribeUser` API operation to check the external login
						information for it, as shown in the following code.

`aws quicksight describe-user --aws-account-id``account-id`--namespace`namespace`--user-name`identity-provider-associated-iam-role`/`identity-username`--region`identity-region`

The following is an example.

`aws quicksight describe-user --aws-account-id 111222333 --namespace default --user-name IdentityQuickSightRole/user --region us-west-2`

The result contains the external login information fields if there are any. Following is an example.

```
{
    "Status": 200,
    "User": {
        "Arn": "arn:aws:quicksight:us-east-1:111222333:user-default-IdentityQuickSightRole-user",
        "UserName": "IdentityQuickSightRole-user",
        "Email": "user@amazon.com",
        "Role": "ADMIN",
        "IdentityType": "IAM",
        "Active": true,
        "PrincipalId": "federated-iam-AROAAAAAAAAAAAAAA:user",
        "ExternalLoginFederationProviderType": "COGNITO",
        "ExternalLoginFederationProviderUrl": "cognito-identity.amazonaws.com",
        "ExternalLoginId": "us-east-1:123abc-1234-123a-b123-12345678a"
    },
    "RequestId": "12345678-1234-1234-abc1-a1b1234567"
}
```
To learn more about using `DescribeUser` in the CLI, see [DescribeUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeUser.html) in the *Amazon Quick API Reference*.

### Use UpdateUser to update external login information for users

In some cases, you might find that the external login information saved
						for the user from the `DescribeUser` result isn't correct or the
						external login information is missing. If so, you can use the
							`UpdateUser` API operation to update it. Use the following
						examples.

For Amazon Cognito users, use the following.

`aws quicksight update-user --aws-account-id``account-id`--namespace`namespace`--user-name`cognito-associated-iam-role`/`cognito-username`--email`user-email`--role`user-role`--external-login-federation-provider-type COGNITO --external-login-id`cognito-identity-id`--region`identity-region`

The following is an example.

`aws quicksight update-user --aws-account-id 111222333 --namespace default --user-name CognitoQuickSightRole/cognito-user --email cognito-user@amazon.com --role ADMIN --external-login-federation-provider-type COGNITO --external-login-id us-east-1:12345678-1234-1234-abc1-a1b1234567 --region us-west-2`

For custom OIDC provider users, use the following.

`aws quicksight update-user --aws-account-id``account-id`--namespace`namespace`--user-name`identity-provider-associated-iam-role`/`identity-username`--email`user-email`--role`user-role`--external-login-federation-provider-type CUSTOM_OIDC --custom-federation-provider-url`custom-identity-provider-url`--external-login-id`custom-provider-identity-id`--region`identity-region`

The following is an example.

`aws quicksight update-user --aws-account-id 111222333 --namespace default --user-name IdentityQuickSightRole/user --email user@amazon.com --role ADMIN --external-login-federation-provider-type CUSTOM_OIDC --custom-federation-provider-url idp.us-east-1.amazonaws.com/us-east-1_ABCDE --external-login-id 123abc-1234-123a-b123-12345678a --region us-west-2`

If you want to delete the external login information for the user, use
							`NONE`
						`external login federation provider type`. Use the following CLI
						command to delete external login information.

`aws quicksight update-user --aws-account-id``account-id`--namespace`namespace`--user-name`identity-provider-associated-iam-role`/`identity-username`--email`user-email`--role`user-role`--external-login-federation-provider-type NONE --region`identity-region`

The following is an example.

`aws quicksight update-user --aws-account-id 111222333 --namespace default --user-name CognitoQuickSightRole/cognito-user --email cognito-user@amazon.com --role ADMIN --external-login-federation-provider-type NONE --region us-west-2`

To learn more about using `UpdateUser` in the CLI, see the
							[UpdateUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateUser.html) in the *Amazon Quick API Reference*.