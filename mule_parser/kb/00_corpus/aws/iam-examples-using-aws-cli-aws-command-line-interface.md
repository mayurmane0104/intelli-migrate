# IAM examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_iam_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_iam_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with IAM.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `add-client-id-to-open-id-connect-provider`.

- **AWS CLI**
- 
            
                    **To add a client ID (audience) to an Open-ID Connect (OIDC) provider**The following `add-client-id-to-open-id-connect-provider`command adds the client ID`my-application-ID`to the OIDC provider named`server.example.com`.`aws iam add-client-id-to-open-id-connect-provider \ --client-id``my-application-ID`\ --open-id-connect-provider-arn`arn:aws:iam::123456789012:oidc-provider/server.example.com`This command produces no output. To create an OIDC provider, use the `create-open-id-connect-provider`command.For more information, see [Creating OpenID Connect (OIDC) identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html)in the*AWS IAM User Guide*.- 
                    For API details, see [AddClientIdToOpenIdConnectProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/add-client-id-to-open-id-connect-provider.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `add-role-to-instance-profile`.

- **AWS CLI**
- 
            
                    **To add a role to an instance profile**The following `add-role-to-instance-profile`command adds the role named`S3Access`to the instance profile named`Webserver`.`aws iam add-role-to-instance-profile \ --role-name``S3Access`\ --instance-profile-name`Webserver`This command produces no output. To create an instance profile, use the `create-instance-profile`command.For more information, see [Using an IAM role to grant permissions to applications running on Amazon EC2 instances](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html)in the*AWS IAM User Guide*.- 
                    For API details, see [AddRoleToInstanceProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/add-role-to-instance-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `add-user-to-group`.

- **AWS CLI**
- 
            
                    **To add a user to an IAM group**The following `add-user-to-group`command adds an IAM user named`Bob`to the IAM group named`Admins`.`aws iam add-user-to-group \ --user-name``Bob`\ --group-name`Admins`This command produces no output. For more information, see [Adding and removing users in an IAM user group](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_add-remove-users.html)in the*AWS IAM User Guide*.- 
                    For API details, see [AddUserToGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/add-user-to-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `attach-group-policy`.

- **AWS CLI**
- 
            
                    **To attach a managed policy to an IAM group**The following `attach-group-policy`command attaches the AWS managed policy named`ReadOnlyAccess`to the IAM group named`Finance`.`aws iam attach-group-policy \ --policy-arn``arn:aws:iam::aws:policy/ReadOnlyAccess`\ --group-name`Finance`This command produces no output. For more information, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html)in the*AWS IAM User Guide*.- 
                    For API details, see [AttachGroupPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-group-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `attach-role-policy`.

- **AWS CLI**
- 
            
                    **To attach a managed policy to an IAM role**The following `attach-role-policy`command attaches the AWS managed policy named`ReadOnlyAccess`to the IAM role named`ReadOnlyRole`.`aws iam attach-role-policy \ --policy-arn``arn:aws:iam::aws:policy/ReadOnlyAccess`\ --role-name`ReadOnlyRole`This command produces no output. For more information, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html)in the*AWS IAM User Guide*.- 
                    For API details, see [AttachRolePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-role-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `attach-user-policy`.

- **AWS CLI**
- 
            
                    **To attach a managed policy to an IAM user**The following `attach-user-policy`command attaches the AWS managed policy named`AdministratorAccess`to the IAM user named`Alice`.`aws iam attach-user-policy \ --policy-arn``arn:aws:iam::aws:policy/AdministratorAccess`\ --user-name`Alice`This command produces no output. For more information, see [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html)in the*AWS IAM User Guide*.- 
                    For API details, see [AttachUserPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-user-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `change-password`.

- **AWS CLI**
- 
            
                    **To change the password for your IAM user**To change the password for your IAM user, we recommend using the `--cli-input-json`parameter to pass a JSON file that contains your old and new passwords. Using this method, you can use strong passwords with non-alphanumeric characters. It can be difficult to use passwords with non-alphanumeric characters when you pass them as command line parameters. To use the`--cli-input-json`parameter, start by using the`change-password`command with the`--generate-cli-skeleton`parameter, as in the following example.`aws iam change-password \ --generate-cli-skeleton``>``change-password.json`The previous command creates a JSON file called change-password.json that you can use to fill in your old and new passwords. For example, the file might look like the following. `{ "OldPassword": "3s0K_;xh4~8XXI", "NewPassword": "]35d/{pB9Fo9wJ" }`Next, to change your password, use the `change-password`command again, this time passing the`--cli-input-json`parameter to specify your JSON file. The following`change-password`command uses the`--cli-input-json`parameter with a JSON file called change-password.json.`aws iam change-password \ --cli-input-json``file://change-password.json`This command produces no output. This command can be called by IAM users only. If this command is called using AWS account (root) credentials, the command returns an `InvalidUserType`error.For more information, see [How an IAM user changes their own password](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_user-change-own.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ChangePassword](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/change-password.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-access-key`.

- **AWS CLI**
- 
            
                    **To create an access key for an IAM user**The following `create-access-key`command creates an access key (access key ID and secret access key) for the IAM user named`Bob`.`aws iam create-access-key \ --user-name``Bob`Output: `{ "AccessKey": { "UserName": "Bob", "Status": "Active", "CreateDate": "2015-03-09T18:39:23.411Z", "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY", "AccessKeyId": "AKIAIOSFODNN7EXAMPLE" } }`Store the secret access key in a secure location. If it is lost, it cannot be recovered, and you must create a new access key. For more information, see [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)in the*AWS IAM User Guide*.- 
                    For API details, see [CreateAccessKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-access-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-account-alias`.

- **AWS CLI**
- 
            
                    **To create an account alias**The following `create-account-alias`command creates the alias`examplecorp`for your AWS account.`aws iam create-account-alias \ --account-alias``examplecorp`This command produces no output. For more information, see [Your AWS account ID and its alias](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html)in the*AWS IAM User Guide*.- 
                    For API details, see [CreateAccountAlias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-account-alias.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-group`.

- **AWS CLI**
- 
            
                    **To create an IAM group**The following `create-group`command creates an IAM group named`Admins`.`aws iam create-group \ --group-name``Admins`Output: `{ "Group": { "Path": "/", "CreateDate": "2015-03-09T20:30:24.940Z", "GroupId": "AIDGPMS9RO4H3FEXAMPLE", "Arn": "arn:aws:iam::123456789012:group/Admins", "GroupName": "Admins" } }`For more information, see [Creating IAM user groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_create.html)in the*AWS IAM User Guide*.- 
                    For API details, see [CreateGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-instance-profile`.

- **AWS CLI**
- 
            
                    **To create an instance profile**The following `create-instance-profile`command creates an instance profile named`Webserver`.`aws iam create-instance-profile \ --instance-profile-name``Webserver`Output: `{ "InstanceProfile": { "InstanceProfileId": "AIPAJMBYC7DLSPEXAMPLE", "Roles": [], "CreateDate": "2015-03-09T20:33:19.626Z", "InstanceProfileName": "Webserver", "Path": "/", "Arn": "arn:aws:iam::123456789012:instance-profile/Webserver" } }`To add a role to an instance profile, use the `add-role-to-instance-profile`command.For more information, see [Using an IAM role to grant permissions to applications running on Amazon EC2 instances](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html)in the*AWS IAM User Guide*.- 
                    For API details, see [CreateInstanceProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-instance-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-login-profile`.

- **AWS CLI**
- 
            
                    **To create a password for an IAM user**To create a password for an IAM user, we recommend using the `--cli-input-json`parameter to pass a JSON file that contains the password. Using this method, you can create a strong password with non-alphanumeric characters. It can be difficult to create a password with non-alphanumeric characters when you pass it as a command line parameter.To use the `--cli-input-json`parameter, start by using the`create-login-profile`command with the`--generate-cli-skeleton`parameter, as in the following example.`aws iam create-login-profile \ --generate-cli-skeleton``>``create-login-profile.json`The previous command creates a JSON file called create-login-profile.json that you can use to fill in the information for a subsequent `create-login-profile`command. For example:`{ "UserName": "Bob", "Password": "&1-3a6u:RA0djs", "PasswordResetRequired": true }`Next, to create a password for an IAM user, use the `create-login-profile`command again, this time passing the`--cli-input-json`parameter to specify your JSON file. The following`create-login-profile`command uses the`--cli-input-json`parameter with a JSON file called create-login-profile.json.`aws iam create-login-profile \ --cli-input-json``file://create-login-profile.json`Output: `{ "LoginProfile": { "UserName": "Bob", "CreateDate": "2015-03-10T20:55:40.274Z", "PasswordResetRequired": true } }`If the new password violates the account password policy, the command returns a `PasswordPolicyViolation`error.To change the password for a user that already has one, use `update-login-profile`. To set a password policy for the account, use the`update-account-password-policy`command.If the account password policy allows them to, IAM users can change their own passwords using the `change-password`command.For more information, see [Managing passwords for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_admin-change-user.html)in the*AWS IAM User Guide*.- 
                    For API details, see [CreateLoginProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-login-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-open-id-connect-provider`.

- **AWS CLI**
- 
            
                    **To create an OpenID Connect (OIDC) provider**To create an OpenID Connect (OIDC) provider, we recommend using the `--cli-input-json`parameter to pass a JSON file that contains the required parameters. When you create an OIDC provider, you must pass the URL of the provider, and the URL must begin with`https://`. It can be difficult to pass the URL as a command line parameter, because the colon (:) and forward slash (/) characters have special meaning in some command line environments. Using the`--cli-input-json`parameter gets around this limitation.To use the `--cli-input-json`parameter, start by using the`create-open-id-connect-provider`command with the`--generate-cli-skeleton`parameter, as in the following example.`aws iam create-open-id-connect-provider \ --generate-cli-skeleton``>``create-open-id-connect-provider.json`The previous command creates a JSON file called create-open-id-connect-provider.json that you can use to fill in the information for a subsequent `create-open-id-connect-provider`command. For example:`{ "Url": "https://server.example.com", "ClientIDList": [ "example-application-ID" ], "ThumbprintList": [ "c3768084dfb3d2b68b7897bf5f565da8eEXAMPLE" ] }`If your OIDC provider's discovery and JWKS endpoints use different certificates, include thumbprints for both endpoints in the `ThumbprintList`.Next, to create the OpenID Connect (OIDC) provider, use the `create-open-id-connect-provider`command again, this time passing the`--cli-input-json`parameter to specify your JSON file. The following`create-open-id-connect-provider`command uses the`--cli-input-json`parameter with a JSON file called create-open-id-connect-provider.json.`aws iam create-open-id-connect-provider \ --cli-input-json``file://create-open-id-connect-provider.json`Output: `{ "OpenIDConnectProviderArn": "arn:aws:iam::123456789012:oidc-provider/server.example.com" }`For more information about OIDC providers, see [Creating OpenID Connect (OIDC) identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html)in the*AWS IAM User Guide*.For more information about obtaining thumbprints for an OIDC provider, see [Obtaining the thumbprint for an OpenID Connect Identity Provider](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc_verify-thumbprint.html)in the*AWS IAM User Guide*.- 
                    For API details, see [CreateOpenIdConnectProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-open-id-connect-provider.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-policy-version`.

- **AWS CLI**
- 
            
                    **To create a new version of a managed policy**This example creates a new `v2`version of the IAM policy whose ARN is`arn:aws:iam::123456789012:policy/MyPolicy`and makes it the default version.`aws iam create-policy-version \ --policy-arn``arn:aws:iam::123456789012:policy/MyPolicy`\ --policy-document`file://NewPolicyVersion.json`\ --set-as-defaultOutput: `{ "PolicyVersion": { "CreateDate": "2015-06-16T18:56:03.721Z", "VersionId": "v2", "IsDefaultVersion": true } }`For more information, see [Versioning IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)in the*AWS IAM User Guide*.- 
                    For API details, see [CreatePolicyVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-policy-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-policy`.

- **AWS CLI**
- 
            
                    **Example 1: To create a customer managed policy**The following command creates a customer managed policy named `my-policy`. The file`policy.json`is a JSON document in the current folder that grants read only access to the`shared`folder in an Amazon S3 bucket named`amzn-s3-demo-bucket`.`aws iam create-policy \ --policy-name``my-policy`\ --policy-document`file://policy.json`Contents of policy.json: `{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "s3:Get*", "s3:List*" ], "Resource": [ "arn:aws:s3:::amzn-s3-demo-bucket/shared/*" ] } ] }`Output: `{ "Policy": { "PolicyName": "my-policy", "CreateDate": "2015-06-01T19:31:18.620Z", "AttachmentCount": 0, "IsAttachable": true, "PolicyId": "ZXR6A36LTYANPAI7NJ5UV", "DefaultVersionId": "v1", "Path": "/", "Arn": "arn:aws:iam::0123456789012:policy/my-policy", "UpdateDate": "2015-06-01T19:31:18.620Z" } }`For more information on using files as input for string parameters, see [Specify parameter values for the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters.html)in the*AWS CLI User Guide*.**Example 2: To create a customer managed policy with a description**The following command creates a customer managed policy named `my-policy`with an immutable description.The file `policy.json`is a JSON document in the current folder that grants access to all Put, List, and Get actions for an Amazon S3 bucket named`amzn-s3-demo-bucket`.`aws iam create-policy \ --policy-name``my-policy`\ --policy-document`file://policy.json`\ --description`"This policy grants access to all Put, Get, and List actions for amzn-s3-demo-bucket"`Contents of policy.json: `{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "s3:ListBucket*", "s3:PutBucket*", "s3:GetBucket*" ], "Resource": [ "arn:aws:s3:::amzn-s3-demo-bucket" ] } ] }`Output: `{ "Policy": { "PolicyName": "my-policy", "PolicyId": "ANPAWGSUGIDPEXAMPLE", "Arn": "arn:aws:iam::123456789012:policy/my-policy", "Path": "/", "DefaultVersionId": "v1", "AttachmentCount": 0, "PermissionsBoundaryUsageCount": 0, "IsAttachable": true, "CreateDate": "2023-05-24T22:38:47+00:00", "UpdateDate": "2023-05-24T22:38:47+00:00" } }`For more information on Idenity-based Policies, see [Identity-based policies and resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html)in the*AWS IAM User Guide*.**Example 3: To create a customer managed policy with tags**The following command creates a customer managed policy named `my-policy`with tags. This example uses the`--tags`parameter with the following JSON-formatted tags:`'{"Key": "Department", "Value": "Accounting"}' '{"Key": "Location", "Value": "Seattle"}'`. Alternatively, the`--tags`parameter can be used with tags in the shorthand format:`'Key=Department,Value=Accounting Key=Location,Value=Seattle'`.The file `policy.json`is a JSON document in the current folder that grants access to all Put, List, and Get actions for an Amazon S3 bucket named`amzn-s3-demo-bucket`.`aws iam create-policy \ --policy-name``my-policy`\ --policy-document`file://policy.json`\ --tags '`{"Key": "Department", "Value": "Accounting"}`' '`{"Key": "Location", "Value": "Seattle"}`'Contents of policy.json: `{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "s3:ListBucket*", "s3:PutBucket*", "s3:GetBucket*" ], "Resource": [ "arn:aws:s3:::amzn-s3-demo-bucket" ] } ] }`Output: `{ "Policy": { "PolicyName": "my-policy", "PolicyId": "ANPAWGSUGIDPEXAMPLE", "Arn": "arn:aws:iam::12345678012:policy/my-policy", "Path": "/", "DefaultVersionId": "v1", "AttachmentCount": 0, "PermissionsBoundaryUsageCount": 0, "IsAttachable": true, "CreateDate": "2023-05-24T23:16:39+00:00", "UpdateDate": "2023-05-24T23:16:39+00:00", "Tags": [ { "Key": "Department", "Value": "Accounting" }, "Key": "Location", "Value": "Seattle" { ] } }`For more information on Tagging policies, see [Tagging customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags_customer-managed-policies.html)in the*AWS IAM User Guide*.- 
                    For API details, see [CreatePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-role`.

- **AWS CLI**
- 
            
                    **Example 1: To create an IAM role**The following `create-role`command creates a role named`Test-Role`and attaches a trust policy to it.`aws iam create-role \ --role-name``Test-Role`\ --assume-role-policy-document`file://Test-Role-Trust-Policy.json`Output: `{ "Role": { "AssumeRolePolicyDocument": "<URL-encoded-JSON>", "RoleId": "AKIAIOSFODNN7EXAMPLE", "CreateDate": "2013-06-07T20:43:32.821Z", "RoleName": "Test-Role", "Path": "/", "Arn": "arn:aws:iam::123456789012:role/Test-Role" } }`The trust policy is defined as a JSON document in the *Test-Role-Trust-Policy.json*file. (The file name and extension do not have significance.) The trust policy must specify a principal.To attach a permissions policy to a role, use the `put-role-policy`command.For more information, see [Creating IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html)in the*AWS IAM User Guide*.**Example 2: To create an IAM role with specified maximum session duration**The following `create-role`command creates a role named`Test-Role`and sets a maximum session duration of 7200 seconds (2 hours).`aws iam create-role \ --role-name``Test-Role`\ --assume-role-policy-document`file://Test-Role-Trust-Policy.json`\ --max-session-duration`7200`Output: `{ "Role": { "Path": "/", "RoleName": "Test-Role", "RoleId": "AKIAIOSFODNN7EXAMPLE", "Arn": "arn:aws:iam::12345678012:role/Test-Role", "CreateDate": "2023-05-24T23:50:25+00:00", "AssumeRolePolicyDocument": { "Version":"2012-10-17", "Statement": [ { "Sid": "Statement1", "Effect": "Allow", "Principal": { "AWS": "arn:aws:iam::12345678012:root" }, "Action": "sts:AssumeRole" } ] } } }`For more information, see [Modifying a role maximum session duration (AWS API)](https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-managingrole-editing-api.html#roles-modify_max-session-duration-api)in the*AWS IAM User Guide*.**Example 3: To create an IAM Role with tags**The following command creates an IAM Role `Test-Role`with tags. This example uses the`--tags`parameter flag with the following JSON-formatted tags:`'{"Key": "Department", "Value": "Accounting"}' '{"Key": "Location", "Value": "Seattle"}'`. Alternatively, the`--tags`flag can be used with tags in the shorthand format:`'Key=Department,Value=Accounting Key=Location,Value=Seattle'`.`aws iam create-role \ --role-name``Test-Role`\ --assume-role-policy-document`file://Test-Role-Trust-Policy.json`\ --tags '`{"Key": "Department", "Value": "Accounting"}`' '`{"Key": "Location", "Value": "Seattle"}`'Output: `{ "Role": { "Path": "/", "RoleName": "Test-Role", "RoleId": "AKIAIOSFODNN7EXAMPLE", "Arn": "arn:aws:iam::123456789012:role/Test-Role", "CreateDate": "2023-05-25T23:29:41+00:00", "AssumeRolePolicyDocument": { "Version":"2012-10-17", "Statement": [ { "Sid": "Statement1", "Effect": "Allow", "Principal": { "AWS": "arn:aws:iam::123456789012:root" }, "Action": "sts:AssumeRole" } ] }, "Tags": [ { "Key": "Department", "Value": "Accounting" }, { "Key": "Location", "Value": "Seattle" } ] } }`For more information, see [Tagging IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags_roles.html)in the*AWS IAM User Guide*.- 
                    For API details, see [CreateRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-role.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-saml-provider`.

- **AWS CLI**
- 
            
                    **To create a SAML provider**This example creates a new SAML provider in IAM named `MySAMLProvider`. It is described by the SAML metadata document found in the file`SAMLMetaData.xml`.`aws iam create-saml-provider \ --saml-metadata-document``file://SAMLMetaData.xml`\ --name`MySAMLProvider`Output: `{ "SAMLProviderArn": "arn:aws:iam::123456789012:saml-provider/MySAMLProvider" }`For more information, see [Creating IAM SAML identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml.html)in the*AWS IAM User Guide*.- 
                    For API details, see [CreateSAMLProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-saml-provider.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-service-linked-role`.

- **AWS CLI**
- 
            
                    **To create a service-linked role**The following `create-service-linked-role`example creates a service-linked role for the specified AWS service and attaches the specified description.`aws iam create-service-linked-role \ --aws-service-name``lex.amazonaws.com`\ --description`"My service-linked role to support Lex"`Output: `{ "Role": { "Path": "/aws-service-role/lex.amazonaws.com/", "RoleName": "AWSServiceRoleForLexBots", "RoleId": "AROA1234567890EXAMPLE", "Arn": "arn:aws:iam::1234567890:role/aws-service-role/lex.amazonaws.com/AWSServiceRoleForLexBots", "CreateDate": "2019-04-17T20:34:14+00:00", "AssumeRolePolicyDocument": { "Version":"2012-10-17", "Statement": [ { "Action": [ "sts:AssumeRole" ], "Effect": "Allow", "Principal": { "Service": [ "lex.amazonaws.com" ] } } ] } } }`For more information, see [Using service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html)in the*AWS IAM User Guide*.- 
                    For API details, see [CreateServiceLinkedRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-service-linked-role.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-service-specific-credential`.

- **AWS CLI**
- 
            
                    **Create a set of service-specific credentials for a user**The following `create-service-specific-credential`example creates a username and password that can be used to access only the configured service.`aws iam create-service-specific-credential \ --user-name``sofia`\ --service-name`codecommit.amazonaws.com`Output: `{ "ServiceSpecificCredential": { "CreateDate": "2019-04-18T20:45:36+00:00", "ServiceName": "codecommit.amazonaws.com", "ServiceUserName": "sofia-at-123456789012", "ServicePassword": "k1zPZM6uVxMQ3oxqgoYlNuJPyRTZ1vREs76zTQE3eJk=", "ServiceSpecificCredentialId": "ACCAEXAMPLE123EXAMPLE", "UserName": "sofia", "Status": "Active" } }`For more information, see [Create Git credentials for HTTPS connections to CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-gc.html#setting-up-gc-iam)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [CreateServiceSpecificCredential](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-service-specific-credential.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-user`.

- **AWS CLI**
- 
            
                    **Example 1: To create an IAM user**The following `create-user`command creates an IAM user named`Bob`in the current account.`aws iam create-user \ --user-name``Bob`Output: `{ "User": { "UserName": "Bob", "Path": "/", "CreateDate": "2023-06-08T03:20:41.270Z", "UserId": "AIDAIOSFODNN7EXAMPLE", "Arn": "arn:aws:iam::123456789012:user/Bob" } }`For more information, see [Creating an IAM user in your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)in the*AWS IAM User Guide*.**Example 2: To create an IAM user at a specified path**The following `create-user`command creates an IAM user named`Bob`at the specified path.`aws iam create-user \ --user-name``Bob`\ --path`/division_abc/subdivision_xyz/`Output: `{ "User": { "Path": "/division_abc/subdivision_xyz/", "UserName": "Bob", "UserId": "AIDAIOSFODNN7EXAMPLE", "Arn": "arn:aws:iam::12345678012:user/division_abc/subdivision_xyz/Bob", "CreateDate": "2023-05-24T18:20:17+00:00" } }`For more information, see [IAM identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html)in the*AWS IAM User Guide*.**Example 3: To Create an IAM User with tags**The following `create-user`command creates an IAM user named`Bob`with tags. This example uses the`--tags`parameter flag with the following JSON-formatted tags:`'{"Key": "Department", "Value": "Accounting"}' '{"Key": "Location", "Value": "Seattle"}'`. Alternatively, the`--tags`flag can be used with tags in the shorthand format:`'Key=Department,Value=Accounting Key=Location,Value=Seattle'`.`aws iam create-user \ --user-name``Bob`\ --tags '`{"Key": "Department", "Value": "Accounting"}`' '`{"Key": "Location", "Value": "Seattle"}`'Output: `{ "User": { "Path": "/", "UserName": "Bob", "UserId": "AIDAIOSFODNN7EXAMPLE", "Arn": "arn:aws:iam::12345678012:user/Bob", "CreateDate": "2023-05-25T17:14:21+00:00", "Tags": [ { "Key": "Department", "Value": "Accounting" }, { "Key": "Location", "Value": "Seattle" } ] } }`For more information, see [Tagging IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags_users.html)in the*AWS IAM User Guide*.**Example 3: To create an IAM user with a set permissions boundary**The following `create-user`command creates an IAM user named`Bob`with the permissions boundary of AmazonS3FullAccess.`aws iam create-user \ --user-name``Bob`\ --permissions-boundary`arn:aws:iam::aws:policy/AmazonS3FullAccess`Output: `{ "User": { "Path": "/", "UserName": "Bob", "UserId": "AIDAIOSFODNN7EXAMPLE", "Arn": "arn:aws:iam::12345678012:user/Bob", "CreateDate": "2023-05-24T17:50:53+00:00", "PermissionsBoundary": { "PermissionsBoundaryType": "Policy", "PermissionsBoundaryArn": "arn:aws:iam::aws:policy/AmazonS3FullAccess" } } }`For more information, see [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html)in the*AWS IAM User Guide*.- 
                    For API details, see [CreateUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-virtual-mfa-device`.

- **AWS CLI**
- 
            
                    **To create a virtual MFA device**This example creates a new virtual MFA device called `BobsMFADevice`. It creates a file that contains bootstrap information called`QRCode.png`and places it in the`C:/`directory. The bootstrap method used in this example is`QRCodePNG`.`aws iam create-virtual-mfa-device \ --virtual-mfa-device-name``BobsMFADevice`\ --outfile`C:/QRCode.png`\ --bootstrap-method`QRCodePNG`Output: `{ "VirtualMFADevice": { "SerialNumber": "arn:aws:iam::210987654321:mfa/BobsMFADevice" }`For more information, see [Using multi-factor authentication (MFA) in AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html)in the*AWS IAM User Guide*.- 
                    For API details, see [CreateVirtualMfaDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-virtual-mfa-device.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deactivate-mfa-device`.

- **AWS CLI**
- 
            
                    **To deactivate an MFA device**This command deactivates the virtual MFA device with the ARN `arn:aws:iam::210987654321:mfa/BobsMFADevice`that is associated with the user`Bob`.`aws iam deactivate-mfa-device \ --user-name``Bob`\ --serial-number`arn:aws:iam::210987654321:mfa/BobsMFADevice`This command produces no output. For more information, see [Using multi-factor authentication (MFA) in AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html)in the*AWS IAM User Guide*.- 
                    For API details, see [DeactivateMfaDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/deactivate-mfa-device.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `decode-authorization-message`.

- **AWS CLI**
- 
            
                    **To decode a authorization failure message**The following `decode-authorization-message`example decodes the message returned by the EC2 console when attempting to launch an instance without the required permissions.`aws sts decode-authorization-message \ --encoded-message``lxzA8VEjEvu-s0TTt3PgYCXik9YakOqsrFJGRZR98xNcyWAxwRq14xIvd-npzbgTevuufCTbjeBAaDARg9cbTK1rJbg3awM33o-Vy3ebPErE2-mWR9hVYdvX-0zKgVOWF9pWjZaJSMqxB-aLXo-I_8TTvBq88x8IFPbMArNdpu0IjxDjzf22PF3SOE3XvIQ-_PEO0aUqHCCcsSrFtvxm6yQD1nbm6VTIVrfa0Bzy8lsoMo7SjIaJ2r5vph6SY5vCCwg6o2JKe3hIHTa8zRrDbZSFMkcXOT6EOPkQXmaBsAC6ciG7Pz1JnEOvuj5NSTlSMljrAXczWuRKAs5GsMYiU8KZXZhokVzdQCUZkS5aVHumZbadu0io53jpgZqhMqvS4fyfK4auK0yKRMtS6JCXPlhkolEs7ZMFA0RVkutqhQqpSDPB5SX5l00lYipWyFK0_AyAx60vumPuVh8P0AzXwdFsT0l4D0m42NFIKxbWXsoJdqaOqVFyFEd0-Xx9AYAAIr6bhcis7C__bZh4dlAAWooHFGKgfoJcWGwgdzgbu9hWyVvKTpeot5hsb8qANYjJRCPXTKpi6PZfdijIkwb6gDMEsJ9qMtr62qP_989mwmtNgnVvBa_ir6oxJxVe_kL9SH1j5nsGDxQFajvPQhxWOHvEQIg_H0bnKWk`The output is formatted as a single-line string of JSON text that you can parse with any JSON text processor. `{ "DecodedMessage": "{\"allowed\":false,\"explicitDeny\":false,\"matchedStatements\":{\"items\":[]},\"failures\":{\"items\":[]},\"context\":{\"principal\":{\"id\":\"AIDAV3ZUEFP6J7GY7O6LO\",\"name\":\"chain-user\",\"arn\":\"arn:aws:iam::403299380220:user/chain-user\"},\"action\":\"ec2:RunInstances\",\"resource\":\"arn:aws:ec2:us-east-2:403299380220:instance/*\",\"conditions\":{\"items\":[{\"key\":\"ec2:InstanceMarketType\",\"values\":{\"items\":[{\"value\":\"on-demand\"}]}},{\"key\":\"aws:Resource\",\"values\":{\"items\":[{\"value\":\"instance/*\"}]}},{\"key\":\"aws:Account\",\"values\":{\"items\":[{\"value\":\"403299380220\"}]}},{\"key\":\"ec2:AvailabilityZone\",\"values\":{\"items\":[{\"value\":\"us-east-2b\"}]}},{\"key\":\"ec2:ebsOptimized\",\"values\":{\"items\":[{\"value\":\"false\"}]}},{\"key\":\"ec2:IsLaunchTemplateResource\",\"values\":{\"items\":[{\"value\":\"false\"}]}},{\"key\":\"ec2:InstanceType\",\"values\":{\"items\":[{\"value\":\"t2.micro\"}]}},{\"key\":\"ec2:RootDeviceType\",\"values\":{\"items\":[{\"value\":\"ebs\"}]}},{\"key\":\"aws:Region\",\"values\":{\"items\":[{\"value\":\"us-east-2\"}]}},{\"key\":\"aws:Service\",\"values\":{\"items\":[{\"value\":\"ec2\"}]}},{\"key\":\"ec2:InstanceID\",\"values\":{\"items\":[{\"value\":\"*\"}]}},{\"key\":\"aws:Type\",\"values\":{\"items\":[{\"value\":\"instance\"}]}},{\"key\":\"ec2:Tenancy\",\"values\":{\"items\":[{\"value\":\"default\"}]}},{\"key\":\"ec2:Region\",\"values\":{\"items\":[{\"value\":\"us-east-2\"}]}},{\"key\":\"aws:ARN\",\"values\":{\"items\":[{\"value\":\"arn:aws:ec2:us-east-2:403299380220:instance/*\"}]}}]}}}" }`For more information, see [How can I decode an authorization failure message after receiving an "UnauthorizedOperation" error during an EC2 instance launch?](https://repost.aws/knowledge-center/ec2-not-auth-launch)in*AWS re:Post*.- 
                    For API details, see [DecodeAuthorizationMessage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/decode-authorization-message.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-access-key`.

- **AWS CLI**
- 
            
                    **To delete an access key for an IAM user**The following `delete-access-key`command deletes the specified access key (access key ID and secret access key) for the IAM user named`Bob`.`aws iam delete-access-key \ --access-key-id``AKIDPMS9RO4H3FEXAMPLE`\ --user-name`Bob`This command produces no output. To list the access keys defined for an IAM user, use the `list-access-keys`command.For more information, see [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)in the*AWS IAM User Guide*.- 
                    For API details, see [DeleteAccessKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-access-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-account-alias`.

- **AWS CLI**
- 
            
                    **To delete an account alias**The following `delete-account-alias`command removes the alias`mycompany`for the current account.`aws iam delete-account-alias \ --account-alias``mycompany`This command produces no output. For more information, see [Your AWS account ID and its alias](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html)in the*AWS IAM User Guide*.- 
                    For API details, see [DeleteAccountAlias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-account-alias.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-account-password-policy`.

- **AWS CLI**
- 
            
                    **To delete the current account password policy**The following `delete-account-password-policy`command removes the password policy for the current account.`aws iam delete-account-password-policy`This command produces no output. For more information, see [Setting an account password policy for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html)in the*AWS IAM User Guide*.- 
                    For API details, see [DeleteAccountPasswordPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-account-password-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-group-policy`.

- **AWS CLI**
- 
            
                    **To delete a policy from an IAM group**The following `delete-group-policy`command deletes the policy named`ExamplePolicy`from the group named`Admins`.`aws iam delete-group-policy \ --group-name``Admins`\ --policy-name`ExamplePolicy`This command produces no output. To see the policies attached to a group, use the `list-group-policies`command.For more information, see [Managing IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage.html)in the*AWS IAM User Guide*.- 
                    For API details, see [DeleteGroupPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-group-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-group`.

- **AWS CLI**
- 
            
                    **To delete an IAM group**The following `delete-group`command deletes an IAM group named`MyTestGroup`.`aws iam delete-group \ --group-name``MyTestGroup`This command produces no output. For more information, see [Deleting an IAM user group](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_delete.html)in the*AWS IAM User Guide*.- 
                    For API details, see [DeleteGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-instance-profile`.

- **AWS CLI**
- 
            
                    **To delete an instance profile**The following `delete-instance-profile`command deletes the instance profile named`ExampleInstanceProfile`.`aws iam delete-instance-profile \ --instance-profile-name``ExampleInstanceProfile`This command produces no output. For more information, see [Using instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html)in the*AWS IAM User Guide*.- 
                    For API details, see [DeleteInstanceProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-instance-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-login-profile`.

- **AWS CLI**
- 
            
                    **To delete a password for an IAM user**The following `delete-login-profile`command deletes the password for the IAM user named`Bob`.`aws iam delete-login-profile \ --user-name``Bob`This command produces no output. For more information, see [Managing passwords for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_admin-change-user.html)in the*AWS IAM User Guide*.- 
                    For API details, see [DeleteLoginProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-login-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-open-id-connect-provider`.

- **AWS CLI**
- 
            
                    **To delete an IAM OpenID Connect identity provider**This example deletes the IAM OIDC provider that connects to the provider `example.oidcprovider.com`.`aws iam delete-open-id-connect-provider \ --open-id-connect-provider-arn``arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com`This command produces no output. For more information, see [Creating OpenID Connect (OIDC) identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html)in the*AWS IAM User Guide*.- 
                    For API details, see [DeleteOpenIdConnectProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-open-id-connect-provider.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-policy-version`.

- **AWS CLI**
- 
            
                    **To delete a version of a managed policy**This example deletes the version identified as `v2`from the policy whose ARN is`arn:aws:iam::123456789012:policy/MySamplePolicy`.`aws iam delete-policy-version \ --policy-arn``arn:aws:iam::123456789012:policy/MyPolicy`\ --version-id`v2`This command produces no output. For more information, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)in the*AWS IAM User Guide*.- 
                    For API details, see [DeletePolicyVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-policy-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-policy`.

- **AWS CLI**
- 
            
                    **To delete an IAM policy**This example deletes the policy whose ARN is `arn:aws:iam::123456789012:policy/MySamplePolicy`.`aws iam delete-policy \ --policy-arn``arn:aws:iam::123456789012:policy/MySamplePolicy`This command produces no output. For more information, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)in the*AWS IAM User Guide*.- 
                    For API details, see [DeletePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-role-permissions-boundary`.

- **AWS CLI**
- 
            
                    **To delete a permissions boundary from an IAM role**The following `delete-role-permissions-boundary`example deletes the permissions boundary for the specified IAM role. To apply a permissions boundary to a role, use the`put-role-permissions-boundary`command.`aws iam delete-role-permissions-boundary \ --role-name``lambda-application-role`This command produces no output. For more information, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)in the*AWS IAM User Guide*.- 
                    For API details, see [DeleteRolePermissionsBoundary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-role-permissions-boundary.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-role-policy`.

- **AWS CLI**
- 
            
                    **To remove a policy from an IAM role**The following `delete-role-policy`command removes the policy named`ExamplePolicy`from the role named`Test-Role`.`aws iam delete-role-policy \ --role-name``Test-Role`\ --policy-name`ExamplePolicy`This command produces no output. For more information, see [Modifying a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_modify.html)in the*AWS IAM User Guide*.- 
                    For API details, see [DeleteRolePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-role-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-role`.

- **AWS CLI**
- 
            
                    **To delete an IAM role**The following `delete-role`command removes the role named`Test-Role`.`aws iam delete-role \ --role-name``Test-Role`This command produces no output. Before you can delete a role, you must remove the role from any instance profile ( `remove-role-from-instance-profile`), detach any managed policies (`detach-role-policy`) and delete any inline policies that are attached to the role (`delete-role-policy`).For more information, see [Creating IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html)and[Using instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html)in the*AWS IAM User Guide*.- 
                    For API details, see [DeleteRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-role.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-saml-provider`.

- **AWS CLI**
- 
            
                    **To delete a SAML provider**This example deletes the IAM SAML 2.0 provider whose ARN is `arn:aws:iam::123456789012:saml-provider/SAMLADFSProvider`.`aws iam delete-saml-provider \ --saml-provider-arn``arn:aws:iam::123456789012:saml-provider/SAMLADFSProvider`This command produces no output. For more information, see [Creating IAM SAML identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml.html)in the*AWS IAM User Guide*.- 
                    For API details, see [DeleteSAMLProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-saml-provider.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-server-certificate`.

- **AWS CLI**
- 
            
                    **To delete a server certificate from your AWS account**The following `delete-server-certificate`command removes the specified server certificate from your AWS account.`aws iam delete-server-certificate \ --server-certificate-name``myUpdatedServerCertificate`This command produces no output. To list the server certificates available in your AWS account, use the `list-server-certificates`command.For more information, see [Managing server certificates in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html)in the*AWS IAM User Guide*.- 
                    For API details, see [DeleteServerCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-server-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-service-linked-role`.

- **AWS CLI**
- 
            
                    **To delete a service-linked role**The following `delete-service-linked-role`example deletes the specified service-linked role that you no longer need. The deletion happens asynchronously. You can check the status of the deletion and confirm when it is done by using the`get-service-linked-role-deletion-status`command.`aws iam delete-service-linked-role \ --role-name``AWSServiceRoleForLexBots`Output: `{ "DeletionTaskId": "task/aws-service-role/lex.amazonaws.com/AWSServiceRoleForLexBots/1a2b3c4d-1234-abcd-7890-abcdeEXAMPLE" }`For more information, see [Using service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html)in the*AWS IAM User Guide*.- 
                    For API details, see [DeleteServiceLinkedRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-service-linked-role.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-service-specific-credential`.

- **AWS CLI**
- 
            
                    **Example 1: Delete a service-specific credential for the requesting user**The following `delete-service-specific-credential`example deletes the specified service-specific credential for the user making the request. The`service-specific-credential-id`is provided when you create the credential and you can retrieve it by using the`list-service-specific-credentials`command.`aws iam delete-service-specific-credential \ --service-specific-credential-id``ACCAEXAMPLE123EXAMPLE`This command produces no output. **Example 2: Delete a service-specific credential for a specified user**The following `delete-service-specific-credential`example deletes the specified service-specific credential for the specified user. The`service-specific-credential-id`is provided when you create the credential and you can retrieve it by using the`list-service-specific-credentials`command.`aws iam delete-service-specific-credential \ --user-name``sofia`\ --service-specific-credential-id`ACCAEXAMPLE123EXAMPLE`This command produces no output. For more information, see [Create Git credentials for HTTPS connections to CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-gc.html#setting-up-gc-iam)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [DeleteServiceSpecificCredential](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-service-specific-credential.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-signing-certificate`.

- **AWS CLI**
- 
            
                    **To delete a signing certificate for an IAM user**The following `delete-signing-certificate`command deletes the specified signing certificate for the IAM user named`Bob`.`aws iam delete-signing-certificate \ --user-name``Bob`\ --certificate-id`TA7SMP42TDN5Z26OBPJE7EXAMPLE`This command produces no output. To get the ID for a signing certificate, use the `list-signing-certificates`command.For more information, see [Manage signing certificates](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-up-ami-tools.html#ami-tools-managing-certs)in the*Amazon EC2 User Guide*.- 
                    For API details, see [DeleteSigningCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-signing-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-ssh-public-key`.

- **AWS CLI**
- 
            
                    **To delete an SSH public keys attached to an IAM user**The following `delete-ssh-public-key`command deletes the specified SSH public key attached to the IAM user`sofia`.`aws iam delete-ssh-public-key \ --user-name``sofia`\ --ssh-public-key-id`APKA123456789EXAMPLE`This command produces no output. For more information, see [Use SSH keys and SSH with CodeCommit](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_ssh-keys.html#ssh-keys-code-commit)in the*AWS IAM User Guide*.- 
                    For API details, see [DeleteSshPublicKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-ssh-public-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-user-permissions-boundary`.

- **AWS CLI**
- 
            
                    **To delete a permissions boundary from an IAM user**The following `delete-user-permissions-boundary`example deletes the permissions boundary attached to the IAM user named`intern`. To apply a permissions boundary to a user, use the`put-user-permissions-boundary`command.`aws iam delete-user-permissions-boundary \ --user-name``intern`This command produces no output. For more information, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)in the*AWS IAM User Guide*.- 
                    For API details, see [DeleteUserPermissionsBoundary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-user-permissions-boundary.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-user-policy`.

- **AWS CLI**
- 
            
                    **To remove a policy from an IAM user**The following `delete-user-policy`command removes the specified policy from the IAM user named`Bob`.`aws iam delete-user-policy \ --user-name``Bob`\ --policy-name`ExamplePolicy`This command produces no output. To get a list of policies for an IAM user, use the `list-user-policies`command.For more information, see [Creating an IAM user in your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)in the*AWS IAM User Guide*.- 
                    For API details, see [DeleteUserPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-user-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-user`.

- **AWS CLI**
- 
            
                    **To delete an IAM user**The following `delete-user`command removes the IAM user named`Bob`from the current account.`aws iam delete-user \ --user-name``Bob`This command produces no output. For more information, see [Deleting an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_manage.html#id_users_deleting)in the*AWS IAM User Guide*.- 
                    For API details, see [DeleteUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-virtual-mfa-device`.

- **AWS CLI**
- 
            
                    **To remove a virtual MFA device**The following `delete-virtual-mfa-device`command removes the specified MFA device from the current account.`aws iam delete-virtual-mfa-device \ --serial-number``arn:aws:iam::123456789012:mfa/MFATest`This command produces no output. For more information, see [Deactivating MFA devices](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_disable.html)in the*AWS IAM User Guide*.- 
                    For API details, see [DeleteVirtualMfaDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-virtual-mfa-device.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detach-group-policy`.

- **AWS CLI**
- 
            
                    **To detach a policy from a group**This example removes the managed policy with the ARN `arn:aws:iam::123456789012:policy/TesterAccessPolicy`from the group called`Testers`.`aws iam detach-group-policy \ --group-name``Testers`\ --policy-arn`arn:aws:iam::123456789012:policy/TesterAccessPolicy`This command produces no output. For more information, see [Managing IAM user groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage.html)in the*AWS IAM User Guide*.- 
                    For API details, see [DetachGroupPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/detach-group-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detach-role-policy`.

- **AWS CLI**
- 
            
                    **To detach a policy from a role**This example removes the managed policy with the ARN `arn:aws:iam::123456789012:policy/FederatedTesterAccessPolicy`from the role called`FedTesterRole`.`aws iam detach-role-policy \ --role-name``FedTesterRole`\ --policy-arn`arn:aws:iam::123456789012:policy/FederatedTesterAccessPolicy`This command produces no output. For more information, see [Modifying a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_modify.html)in the*AWS IAM User Guide*.- 
                    For API details, see [DetachRolePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/detach-role-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detach-user-policy`.

- **AWS CLI**
- 
            
                    **To detach a policy from a user**This example removes the managed policy with the ARN `arn:aws:iam::123456789012:policy/TesterPolicy`from the user`Bob`.`aws iam detach-user-policy \ --user-name``Bob`\ --policy-arn`arn:aws:iam::123456789012:policy/TesterPolicy`This command produces no output. For more information, see [Changing permissions for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html)in the*AWS IAM User Guide*.- 
                    For API details, see [DetachUserPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/detach-user-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-organizations-root-credentials-management`.

- **AWS CLI**
- 
            
                    **To disable the RootCredentialsManagement feature in your organization**The following `disable-organizations-root-credentials-management`command disables the management of privileged root user credentials across member accounts in your organization.`aws iam disable-organizations-root-credentials-management`Output: `{ "EnabledFeatures": [ "RootSessions" ] "OrganizationId": "o-aa111bb222" }`For more information, see [Centralize root access for member accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html)in the*AWS IAM User Guide*.g- 
                    For API details, see [DisableOrganizationsRootCredentialsManagement](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/disable-organizations-root-credentials-management.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-organizations-root-sessions`.

- **AWS CLI**
- 
            
                    **To disable the RootSessions feature in your organization**The following `disable-organizations-root-sessions`command disables root user sessions for privileged tasks across member accounts in your organization.`aws iam disable-organizations-root-sessions`Output: `{ "EnabledFeatures": [ "RootCredentialsManagement" ] "OrganizationId": "o-aa111bb222" }`For more information, see [Centralize root access for member accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html)in the*AWS IAM User Guide*.- 
                    For API details, see [DisableOrganizationsRootSessions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/disable-organizations-root-sessions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-mfa-device`.

- **AWS CLI**
- 
            
                    **To enable an MFA device**After you use the `create-virtual-mfa-device`command to create a new virtual MFA device, you can assign the MFA device to a user. The following`enable-mfa-device`example assigns the MFA device with the serial number`arn:aws:iam::210987654321:mfa/BobsMFADevice`to the user`Bob`. The command also synchronizes the device with AWS by including the first two codes in sequence from the virtual MFA device.`aws iam enable-mfa-device \ --user-name``Bob`\ --serial-number`arn:aws:iam::210987654321:mfa/BobsMFADevice`\ --authentication-code1`123456`\ --authentication-code2`789012`This command produces no output. For more information, see [Enabling a virtual multi-factor authentication (MFA) device](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html)in the*AWS IAM User Guide*.- 
                    For API details, see [EnableMfaDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/enable-mfa-device.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-organizations-root-credentials-management`.

- **AWS CLI**
- 
            
                    **To enable the RootCredentialsManagement feature in your organization**The following `enable-organizations-root-credentials-management`command enables the management of privileged root user credentials across member accounts in your organization.`aws iam enable-organizations-root-credentials-management`Output: `{ "EnabledFeatures": [ "RootCredentialsManagement" ] "OrganizationId": "o-aa111bb222" }`For more information, see [Centralize root access for member accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html)in the*AWS IAM User Guide*.- 
                    For API details, see [EnableOrganizationsRootCredentialsManagement](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/enable-organizations-root-credentials-management.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-organizations-root-sessions`.

- **AWS CLI**
- 
            
                    **To enable the RootSessions feature in your organization**The following `enable-organizations-root-sessions`command allows the management account or delegated administrator to perform privileged tasks on member accounts in your organization.`aws iam enable-organizations-root-sessions`Output: `{ "EnabledFeatures": [ "RootSessions" ] "OrganizationId": "o-aa111bb222" }`For more information, see [Centralize root access for member accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html)in the*AWS IAM User Guide*.- 
                    For API details, see [EnableOrganizationsRootSessions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/enable-organizations-root-sessions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `generate-credential-report`.

- **AWS CLI**
- 
            
                    **To generate a credential report**The following example attempts to generate a credential report for the AWS account. `aws iam generate-credential-report`Output: `{ "State": "STARTED", "Description": "No report exists. Starting a new report generation task" }`For more information, see [Getting credential reports for your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GenerateCredentialReport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/generate-credential-report.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `generate-organizations-access-report`.

- **AWS CLI**
- 
            
                    **Example 1: To generate an access report for a root in an organization**The following `generate-organizations-access-report`example starts a background job to create an access report for the specified root in an organization. You can display the report after it's created by running the`get-organizations-access-report`command.`aws iam generate-organizations-access-report \ --entity-path``o-4fxmplt198/r-c3xb`Output: `{ "JobId": "a8b6c06f-aaa4-8xmp-28bc-81da71836359" }`**Example 2: To generate an access report for an account in an organization**The following `generate-organizations-access-report`example starts a background job to create an access report for account ID`123456789012`in the organization`o-4fxmplt198`. You can display the report after it's created by running the`get-organizations-access-report`command.`aws iam generate-organizations-access-report \ --entity-path``o-4fxmplt198/r-c3xb/123456789012`Output: `{ "JobId": "14b6c071-75f6-2xmp-fb77-faf6fb4201d2" }`**Example 3: To generate an access report for an account in an organizational unit in an organization**The following `generate-organizations-access-report`example starts a background job to create an access report for account ID`234567890123`in organizational unit`ou-c3xb-lmu7j2yg`in the organization`o-4fxmplt198`. You can display the report after it's created by running the`get-organizations-access-report`command.`aws iam generate-organizations-access-report \ --entity-path``o-4fxmplt198/r-c3xb/ou-c3xb-lmu7j2yg/234567890123`Output: `{ "JobId": "2eb6c2e6-0xmp-ec04-1425-c937916a64af" }`To get details about roots and organizational units in your organization, use the `organizations list-roots`and`organizations list-organizational-units-for-parent`commands.For more information, see [Refining permissions in AWS using last accessed information](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GenerateOrganizationsAccessReport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/generate-organizations-access-report.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `generate-service-last-accessed-details`.

- **AWS CLI**
- 
            
                    **Example 1: To generate a service access report for a custom policy**The following `generate-service-last-accessed-details`example starts a background job to generate a report that lists the services accessed by IAM users and other entities with a custom policy named`intern-boundary`. You can display the report after it is created by running the`get-service-last-accessed-details`command.`aws iam generate-service-last-accessed-details \ --arn``arn:aws:iam::123456789012:policy/intern-boundary`Output: `{ "JobId": "2eb6c2b8-7b4c-3xmp-3c13-03b72c8cdfdc" }`**Example 2: To generate a service access report for the AWS managed AdministratorAccess policy**The following `generate-service-last-accessed-details`example starts a background job to generate a report that lists the services accessed by IAM users and other entities with the AWS managed`AdministratorAccess`policy. You can display the report after it is created by running the`get-service-last-accessed-details`command.`aws iam generate-service-last-accessed-details \ --arn``arn:aws:iam::aws:policy/AdministratorAccess`Output: `{ "JobId": "78b6c2ba-d09e-6xmp-7039-ecde30b26916" }`For more information, see [Refining permissions in AWS using last accessed information](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GenerateServiceLastAccessedDetails](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/generate-service-last-accessed-details.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-access-key-last-used`.

- **AWS CLI**
- 
            
                    **To retrieve information about when the specified access key was last used**The following example retrieves information about when the access key `ABCDEXAMPLE`was last used.`aws iam get-access-key-last-used \ --access-key-id``ABCDEXAMPLE`Output: `{ "UserName": "Bob", "AccessKeyLastUsed": { "Region": "us-east-1", "ServiceName": "iam", "LastUsedDate": "2015-06-16T22:45:00Z" } }`For more information, see [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetAccessKeyLastUsed](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-access-key-last-used.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-account-authorization-details`.

- **AWS CLI**
- 
            
                    **To list an AWS account's IAM users, groups, roles, and policies**The following `get-account-authorization-details`command returns information about all IAM users, groups, roles, and policies in the AWS account.`aws iam get-account-authorization-details`Output: `{ "RoleDetailList": [ { "AssumeRolePolicyDocument": { "Version":"2012-10-17", "Statement": [ { "Sid": "", "Effect": "Allow", "Principal": { "Service": "ec2.amazonaws.com" }, "Action": "sts:AssumeRole" } ] }, "RoleId": "AROA1234567890EXAMPLE", "CreateDate": "2014-07-30T17:09:20Z", "InstanceProfileList": [ { "InstanceProfileId": "AIPA1234567890EXAMPLE", "Roles": [ { "AssumeRolePolicyDocument": { "Version":"2012-10-17", "Statement": [ { "Sid": "", "Effect": "Allow", "Principal": { "Service": "ec2.amazonaws.com" }, "Action": "sts:AssumeRole" } ] }, "RoleId": "AROA1234567890EXAMPLE", "CreateDate": "2014-07-30T17:09:20Z", "RoleName": "EC2role", "Path": "/", "Arn": "arn:aws:iam::123456789012:role/EC2role" } ], "CreateDate": "2014-07-30T17:09:20Z", "InstanceProfileName": "EC2role", "Path": "/", "Arn": "arn:aws:iam::123456789012:instance-profile/EC2role" } ], "RoleName": "EC2role", "Path": "/", "AttachedManagedPolicies": [ { "PolicyName": "AmazonS3FullAccess", "PolicyArn": "arn:aws:iam::aws:policy/AmazonS3FullAccess" }, { "PolicyName": "AmazonDynamoDBFullAccess", "PolicyArn": "arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess" } ], "RoleLastUsed": { "Region": "us-west-2", "LastUsedDate": "2019-11-13T17:30:00Z" }, "RolePolicyList": [], "Arn": "arn:aws:iam::123456789012:role/EC2role" } ], "GroupDetailList": [ { "GroupId": "AIDA1234567890EXAMPLE", "AttachedManagedPolicies": { "PolicyName": "AdministratorAccess", "PolicyArn": "arn:aws:iam::aws:policy/AdministratorAccess" }, "GroupName": "Admins", "Path": "/", "Arn": "arn:aws:iam::123456789012:group/Admins", "CreateDate": "2013-10-14T18:32:24Z", "GroupPolicyList": [] }, { "GroupId": "AIDA1234567890EXAMPLE", "AttachedManagedPolicies": { "PolicyName": "PowerUserAccess", "PolicyArn": "arn:aws:iam::aws:policy/PowerUserAccess" }, "GroupName": "Dev", "Path": "/", "Arn": "arn:aws:iam::123456789012:group/Dev", "CreateDate": "2013-10-14T18:33:55Z", "GroupPolicyList": [] }, { "GroupId": "AIDA1234567890EXAMPLE", "AttachedManagedPolicies": [], "GroupName": "Finance", "Path": "/", "Arn": "arn:aws:iam::123456789012:group/Finance", "CreateDate": "2013-10-14T18:57:48Z", "GroupPolicyList": [ { "PolicyName": "policygen-201310141157", "PolicyDocument": { "Version":"2012-10-17", "Statement": [ { "Action": "aws-portal:*", "Sid": "Stmt1381777017000", "Resource": "*", "Effect": "Allow" } ] } } ] } ], "UserDetailList": [ { "UserName": "Alice", "GroupList": [ "Admins" ], "CreateDate": "2013-10-14T18:32:24Z", "UserId": "AIDA1234567890EXAMPLE", "UserPolicyList": [], "Path": "/", "AttachedManagedPolicies": [], "Arn": "arn:aws:iam::123456789012:user/Alice" }, { "UserName": "Bob", "GroupList": [ "Admins" ], "CreateDate": "2013-10-14T18:32:25Z", "UserId": "AIDA1234567890EXAMPLE", "UserPolicyList": [ { "PolicyName": "DenyBillingAndIAMPolicy", "PolicyDocument": { "Version":"2012-10-17", "Statement": { "Effect": "Deny", "Action": [ "aws-portal:*", "iam:*" ], "Resource": "*" } } } ], "Path": "/", "AttachedManagedPolicies": [], "Arn": "arn:aws:iam::123456789012:user/Bob" }, { "UserName": "Charlie", "GroupList": [ "Dev" ], "CreateDate": "2013-10-14T18:33:56Z", "UserId": "AIDA1234567890EXAMPLE", "UserPolicyList": [], "Path": "/", "AttachedManagedPolicies": [], "Arn": "arn:aws:iam::123456789012:user/Charlie" } ], "Policies": [ { "PolicyName": "create-update-delete-set-managed-policies", "CreateDate": "2015-02-06T19:58:34Z", "AttachmentCount": 1, "IsAttachable": true, "PolicyId": "ANPA1234567890EXAMPLE", "DefaultVersionId": "v1", "PolicyVersionList": [ { "CreateDate": "2015-02-06T19:58:34Z", "VersionId": "v1", "Document": { "Version":"2012-10-17", "Statement": { "Effect": "Allow", "Action": [ "iam:CreatePolicy", "iam:CreatePolicyVersion", "iam:DeletePolicy", "iam:DeletePolicyVersion", "iam:GetPolicy", "iam:GetPolicyVersion", "iam:ListPolicies", "iam:ListPolicyVersions", "iam:SetDefaultPolicyVersion" ], "Resource": "*" } }, "IsDefaultVersion": true } ], "Path": "/", "Arn": "arn:aws:iam::123456789012:policy/create-update-delete-set-managed-policies", "UpdateDate": "2015-02-06T19:58:34Z" }, { "PolicyName": "S3-read-only-specific-bucket", "CreateDate": "2015-01-21T21:39:41Z", "AttachmentCount": 1, "IsAttachable": true, "PolicyId": "ANPA1234567890EXAMPLE", "DefaultVersionId": "v1", "PolicyVersionList": [ { "CreateDate": "2015-01-21T21:39:41Z", "VersionId": "v1", "Document": { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "s3:Get*", "s3:List*" ], "Resource": [ "arn:aws:s3:::amzn-s3-demo-bucket", "arn:aws:s3:::amzn-s3-demo-bucket/*" ] } ] }, "IsDefaultVersion": true } ], "Path": "/", "Arn": "arn:aws:iam::123456789012:policy/S3-read-only-specific-bucket", "UpdateDate": "2015-01-21T23:39:41Z" }, { "PolicyName": "AmazonEC2FullAccess", "CreateDate": "2015-02-06T18:40:15Z", "AttachmentCount": 1, "IsAttachable": true, "PolicyId": "ANPA1234567890EXAMPLE", "DefaultVersionId": "v1", "PolicyVersionList": [ { "CreateDate": "2014-10-30T20:59:46Z", "VersionId": "v1", "Document": { "Version":"2012-10-17", "Statement": [ { "Action": "ec2:*", "Effect": "Allow", "Resource": "*" }, { "Effect": "Allow", "Action": "elasticloadbalancing:*", "Resource": "*" }, { "Effect": "Allow", "Action": "cloudwatch:*", "Resource": "*" }, { "Effect": "Allow", "Action": "autoscaling:*", "Resource": "*" } ] }, "IsDefaultVersion": true } ], "Path": "/", "Arn": "arn:aws:iam::aws:policy/AmazonEC2FullAccess", "UpdateDate": "2015-02-06T18:40:15Z" } ], "Marker": "EXAMPLEkakv9BCuUNFDtxWSyfzetYwEx2ADc8dnzfvERF5S6YMvXKx41t6gCl/eeaCX3Jo94/bKqezEAg8TEVS99EKFLxm3jtbpl25FDWEXAMPLE", "IsTruncated": true }`For more information, see [AWS security audit guidelines](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-audit-guide.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetAccountAuthorizationDetails](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-account-authorization-details.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-account-password-policy`.

- **AWS CLI**
- 
            
                    **To see the current account password policy**The following `get-account-password-policy`command displays details about the password policy for the current account.`aws iam get-account-password-policy`Output: `{ "PasswordPolicy": { "AllowUsersToChangePassword": false, "RequireLowercaseCharacters": false, "RequireUppercaseCharacters": false, "MinimumPasswordLength": 8, "RequireNumbers": true, "RequireSymbols": true } }`If no password policy is defined for the account, the command returns a `NoSuchEntity`error.For more information, see [Setting an account password policy for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetAccountPasswordPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-account-password-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-account-summary`.

- **AWS CLI**
- 
            
                    **To get information about IAM entity usage and IAM quotas in the current account**The following `get-account-summary`command returns information about the current IAM entity usage and current IAM entity quotas in the account.`aws iam get-account-summary`Output: `{ "SummaryMap": { "UsersQuota": 5000, "GroupsQuota": 100, "InstanceProfiles": 6, "SigningCertificatesPerUserQuota": 2, "AccountAccessKeysPresent": 0, "RolesQuota": 250, "RolePolicySizeQuota": 10240, "AccountSigningCertificatesPresent": 0, "Users": 27, "ServerCertificatesQuota": 20, "ServerCertificates": 0, "AssumeRolePolicySizeQuota": 2048, "Groups": 7, "MFADevicesInUse": 1, "Roles": 3, "AccountMFAEnabled": 1, "MFADevices": 3, "GroupsPerUserQuota": 10, "GroupPolicySizeQuota": 5120, "InstanceProfilesQuota": 100, "AccessKeysPerUserQuota": 2, "Providers": 0, "UserPolicySizeQuota": 2048 } }`For more information about entity limitations, see [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetAccountSummary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-account-summary.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-context-keys-for-custom-policy`.

- **AWS CLI**
- 
            
                    **Example 1: To list the context keys referenced by one or more custom JSON policies provided as a parameter on the command line**The following `get-context-keys-for-custom-policy`command parses each supplied policy and lists the context keys used by those policies. Use this command to identify which context key values you must supply to successfully use the policy simulator commands`simulate-custom-policy`and`simulate-custom-policy`. You can also retrieve the list of context keys used by all policies associated by an IAM user or role by using the`get-context-keys-for-custom-policy`command. Parameter values that begin with`file://`instruct the command to read the file and use the contents as the value for the parameter instead of the file name itself.`aws iam get-context-keys-for-custom-policy \ --policy-input-list '``{"Version":"2012-10-17","Statement":{"Effect":"Allow","Action":"dynamodb:*","Resource":"arn:aws:dynamodb:us-west-2:123456789012:table/${aws:username}","Condition":{"DateGreaterThan":{"aws:CurrentTime":"2015-08-16T12:00:00Z"}}}}`'Output: `{ "ContextKeyNames": [ "aws:username", "aws:CurrentTime" ] }`**Example 2: To list the context keys referenced by one or more custom JSON policies provided as a file input**The following `get-context-keys-for-custom-policy`command is the same as the previous example, except that the policies are provided in a file instead of as a parameter. Because the command expects a JSON list of strings, and not a list of JSON structures, the file must be structured as follows, although you can collapse it into one one.`[ "Policy1", "Policy2" ]`So for example, a file that contains the policy from the previous example must look like the following. You must escape each embedded double-quote inside the policy string by preceding it with a backslash ''. `[ "{\"Version\": \"2012-10-17\", \"Statement\": {\"Effect\": \"Allow\", \"Action\": \"dynamodb:*\", \"Resource\": \"arn:aws:dynamodb:us-west-2:128716708097:table/${aws:username}\", \"Condition\": {\"DateGreaterThan\": {\"aws:CurrentTime\": \"2015-08-16T12:00:00Z\"}}}}" ]`This file can then be submitted to the following command. `aws iam get-context-keys-for-custom-policy \ --policy-input-list``file://policyfile.json`Output: `{ "ContextKeyNames": [ "aws:username", "aws:CurrentTime" ] }`For more information, see [Using the IAM Policy Simulator (AWS CLI and AWS API)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html#policies-simulator-using-api)in the*AWS IAM User Guide*.- 
                    For API details, see [GetContextKeysForCustomPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-context-keys-for-custom-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-context-keys-for-principal-policy`.

- **AWS CLI**
- 
            
                    **To list the context keys referenced by all policies associated with an IAM principal**The following `get-context-keys-for-principal-policy`command retrieves all policies that are attached to the user`saanvi`and any groups she is a member of. It then parses each and lists the context keys used by those policies. Use this command to identify which context key values you must supply to successfully use the`simulate-custom-policy`and`simulate-principal-policy`commands. You can also retrieve the list of context keys used by an arbitrary JSON policy by using the`get-context-keys-for-custom-policy`command.`aws iam get-context-keys-for-principal-policy \ --policy-source-arn``arn:aws:iam::123456789012:user/saanvi`Output: `{ "ContextKeyNames": [ "aws:username", "aws:CurrentTime" ] }`For more information, see [Using the IAM Policy Simulator (AWS CLI and AWS API)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html#policies-simulator-using-api)in the*AWS IAM User Guide*.- 
                    For API details, see [GetContextKeysForPrincipalPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-context-keys-for-principal-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-credential-report`.

- **AWS CLI**
- 
            
                    **To get a credential report**This example opens the returned report and outputs it to the pipeline as an array of text lines. `aws iam get-credential-report`Output: `{ "GeneratedTime": "2015-06-17T19:11:50Z", "ReportFormat": "text/csv" }`For more information, see [Getting credential reports for your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetCredentialReport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-credential-report.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-group-policy`.

- **AWS CLI**
- 
            
                    **To get information about a policy attached to an IAM group**The following `get-group-policy`command gets information about the specified policy attached to the group named`Test-Group`.`aws iam get-group-policy \ --group-name``Test-Group`\ --policy-name`S3-ReadOnly-Policy`Output: `{ "GroupName": "Test-Group", "PolicyDocument": { "Statement": [ { "Action": [ "s3:Get*", "s3:List*" ], "Resource": "*", "Effect": "Allow" } ] }, "PolicyName": "S3-ReadOnly-Policy" }`For more information, see [Managing IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetGroupPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-group-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-group`.

- **AWS CLI**
- 
            
                    **To get an IAM group**This example returns details about the IAM group `Admins`.`aws iam get-group \ --group-name``Admins`Output: `{ "Group": { "Path": "/", "CreateDate": "2015-06-16T19:41:48Z", "GroupId": "AIDGPMS9RO4H3FEXAMPLE", "Arn": "arn:aws:iam::123456789012:group/Admins", "GroupName": "Admins" }, "Users": [] }`For more information, see [IAM Identities (users, user groups, and roles)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-instance-profile`.

- **AWS CLI**
- 
            
                    **To get information about an instance profile**The following `get-instance-profile`command gets information about the instance profile named`ExampleInstanceProfile`.`aws iam get-instance-profile \ --instance-profile-name``ExampleInstanceProfile`Output: `{ "InstanceProfile": { "InstanceProfileId": "AID2MAB8DPLSRHEXAMPLE", "Roles": [ { "AssumeRolePolicyDocument": "<URL-encoded-JSON>", "RoleId": "AIDGPMS9RO4H3FEXAMPLE", "CreateDate": "2013-01-09T06:33:26Z", "RoleName": "Test-Role", "Path": "/", "Arn": "arn:aws:iam::336924118301:role/Test-Role" } ], "CreateDate": "2013-06-12T23:52:02Z", "InstanceProfileName": "ExampleInstanceProfile", "Path": "/", "Arn": "arn:aws:iam::336924118301:instance-profile/ExampleInstanceProfile" } }`For more information, see [Using instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetInstanceProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-instance-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-login-profile`.

- **AWS CLI**
- 
            
                    **To get password information for an IAM user**The following `get-login-profile`command gets information about the password for the IAM user named`Bob`.`aws iam get-login-profile \ --user-name``Bob`Output: `{ "LoginProfile": { "UserName": "Bob", "CreateDate": "2012-09-21T23:03:39Z" } }`The `get-login-profile`command can be used to verify that an IAM user has a password. The command returns a`NoSuchEntity`error if no password is defined for the user.You cannot view a password using this command. If the password is lost, you can reset the password ( `update-login-profile`) for the user. Alternatively, you can delete the login profile (`delete-login-profile`) for the user and then create a new one (`create-login-profile`).For more information, see [Managing passwords for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_admin-change-user.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetLoginProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-login-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-mfa-device`.

- **AWS CLI**
- 
            
                    **To retrieve information about a FIDO security key**The following `get-mfa-device`command example retrieves information about the specified FIDO security key.`aws iam get-mfa-device \ --serial-number``arn:aws:iam::123456789012:u2f/user/alice/fidokeyname-EXAMPLEBN5FHTECLFG7EXAMPLE`Output: `{ "UserName": "alice", "SerialNumber": "arn:aws:iam::123456789012:u2f/user/alice/fidokeyname-EXAMPLEBN5FHTECLFG7EXAMPLE", "EnableDate": "2023-09-19T01:49:18+00:00", "Certifications": { "FIDO": "L1" } }`For more information, see [Using multi-factor authentication (MFA) in AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetMfaDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-mfa-device.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-open-id-connect-provider`.

- **AWS CLI**
- 
            
                    **To return information about the specified OpenID Connect provider**This example returns details about the OpenID Connect provider whose ARN is `arn:aws:iam::123456789012:oidc-provider/server.example.com`.`aws iam get-open-id-connect-provider \ --open-id-connect-provider-arn``arn:aws:iam::123456789012:oidc-provider/server.example.com`Output: `{ "Url": "server.example.com" "CreateDate": "2015-06-16T19:41:48Z", "ThumbprintList": [ "12345abcdefghijk67890lmnopqrst987example" ], "ClientIDList": [ "example-application-ID" ] }`For more information, see [Creating OpenID Connect (OIDC) identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetOpenIdConnectProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-open-id-connect-provider.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-organizations-access-report`.

- **AWS CLI**
- 
            
                    **To retrieve an access report**The following `get-organizations-access-report`example displays a previously generated access report for an AWS Organizations entity. To generate a report, use the`generate-organizations-access-report`command.`aws iam get-organizations-access-report \ --job-id``a8b6c06f-aaa4-8xmp-28bc-81da71836359`Output: `{ "JobStatus": "COMPLETED", "JobCreationDate": "2019-09-30T06:53:36.187Z", "JobCompletionDate": "2019-09-30T06:53:37.547Z", "NumberOfServicesAccessible": 188, "NumberOfServicesNotAccessed": 171, "AccessDetails": [ { "ServiceName": "Alexa for Business", "ServiceNamespace": "a4b", "TotalAuthenticatedEntities": 0 }, ... }`For more information, see [Refining permissions in AWS using last accessed information](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetOrganizationsAccessReport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-organizations-access-report.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-policy-version`.

- **AWS CLI**
- 
            
                    **To retrieve information about the specified version of the specified managed policy**This example returns the policy document for the v2 version of the policy whose ARN is `arn:aws:iam::123456789012:policy/MyManagedPolicy`.`aws iam get-policy-version \ --policy-arn``arn:aws:iam::123456789012:policy/MyPolicy`\ --version-id`v2`Output: `{ "PolicyVersion": { "Document": { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "iam:*", "Resource": "*" } ] }, "VersionId": "v2", "IsDefaultVersion": true, "CreateDate": "2023-04-11T00:22:54+00:00" } }`For more information, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetPolicyVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-policy-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-policy`.

- **AWS CLI**
- 
            
                    **To retrieve information about the specified managed policy**This example returns details about the managed policy whose ARN is `arn:aws:iam::123456789012:policy/MySamplePolicy`.`aws iam get-policy \ --policy-arn``arn:aws:iam::123456789012:policy/MySamplePolicy`Output: `{ "Policy": { "PolicyName": "MySamplePolicy", "CreateDate": "2015-06-17T19:23;32Z", "AttachmentCount": 0, "IsAttachable": true, "PolicyId": "Z27SI6FQMGNQ2EXAMPLE1", "DefaultVersionId": "v1", "Path": "/", "Arn": "arn:aws:iam::123456789012:policy/MySamplePolicy", "UpdateDate": "2015-06-17T19:23:32Z" } }`For more information, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-role-policy`.

- **AWS CLI**
- 
            
                    **To get information about a policy attached to an IAM role**The following `get-role-policy`command gets information about the specified policy attached to the role named`Test-Role`.`aws iam get-role-policy \ --role-name``Test-Role`\ --policy-name`ExamplePolicy`Output: `{ "RoleName": "Test-Role", "PolicyDocument": { "Statement": [ { "Action": [ "s3:ListBucket", "s3:Put*", "s3:Get*", "s3:*MultipartUpload*" ], "Resource": "*", "Effect": "Allow", "Sid": "1" } ] } "PolicyName": "ExamplePolicy" }`For more information, see [Creating IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetRolePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-role-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-role`.

- **AWS CLI**
- 
            
                    **To get information about an IAM role**The following `get-role`command gets information about the role named`Test-Role`.`aws iam get-role \ --role-name``Test-Role`Output: `{ "Role": { "Description": "Test Role", "AssumeRolePolicyDocument":"<URL-encoded-JSON>", "MaxSessionDuration": 3600, "RoleId": "AROA1234567890EXAMPLE", "CreateDate": "2019-11-13T16:45:56Z", "RoleName": "Test-Role", "Path": "/", "RoleLastUsed": { "Region": "us-east-1", "LastUsedDate": "2019-11-13T17:14:00Z" }, "Arn": "arn:aws:iam::123456789012:role/Test-Role" } }`The command displays the trust policy attached to the role. To list the permissions policies attached to a role, use the `list-role-policies`command.For more information, see [Creating IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-role.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-saml-provider`.

- **AWS CLI**
- 
            
                    **To retrieve the SAML provider metadocument**This example retrieves the details about the SAML 2.0 provider whose ARM is `arn:aws:iam::123456789012:saml-provider/SAMLADFS`. The response includes the metadata document that you got from the identity provider to create the AWS SAML provider entity as well as the creation and expiration dates.`aws iam get-saml-provider \ --saml-provider-arn``arn:aws:iam::123456789012:saml-provider/SAMLADFS`Output: `{ "SAMLMetadataDocument": "...SAMLMetadataDocument-XML...", "CreateDate": "2017-03-06T22:29:46+00:00", "ValidUntil": "2117-03-06T22:29:46.433000+00:00", "Tags": [ { "Key": "DeptID", "Value": "123456" }, { "Key": "Department", "Value": "Accounting" } ] }`For more information, see [Creating IAM SAML identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetSamlProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-saml-provider.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-server-certificate`.

- **AWS CLI**
- 
            
                    **To get details about a server certificate in your AWS account**The following `get-server-certificate`command retrieves all of the details about the specified server certificate in your AWS account.`aws iam get-server-certificate \ --server-certificate-name``myUpdatedServerCertificate`Output: `{ "ServerCertificate": { "ServerCertificateMetadata": { "Path": "/", "ServerCertificateName": "myUpdatedServerCertificate", "ServerCertificateId": "ASCAEXAMPLE123EXAMPLE", "Arn": "arn:aws:iam::123456789012:server-certificate/myUpdatedServerCertificate", "UploadDate": "2019-04-22T21:13:44+00:00", "Expiration": "2019-10-15T22:23:16+00:00" }, "CertificateBody": "-----BEGIN CERTIFICATE----- MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6 b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ 21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4 nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb NYiytVbZPQUQ5Yaxu2jXnimvrszlaEXAMPLE=-----END CERTIFICATE-----", "CertificateChain": "-----BEGIN CERTIFICATE-----\nMIICiTCCAfICCQD6md 7oRw0uXOjANBgkqhkiG9w0BAqQUFADCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgT AldBMRAwDgYDVQQHEwdTZWF0drGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAs TC0lBTSBDb25zb2xlMRIwEAYDVsQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQ jb20wHhcNMTEwNDI1MjA0NTIxWhtcNMTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBh MCVVMxCzAJBgNVBAgTAldBMRAwDgsYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBb WF6b24xFDASBgNVBAsTC0lBTSBDb2d5zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMx HzAdBgkqhkiG9w0BCQEWEG5vb25lQGfFtYXpvbi5jb20wgZ8wDQYJKoZIhvcNAQE BBQADgY0AMIGJAoGBAMaK0dn+a4GmWIgWJ21uUSfwfEvySWtC2XADZ4nB+BLYgVI k60CpiwsZ3G93vUEIO3IyNoH/f0wYK8mh9TrDHudUZg3qX4waLG5M43q7Wgc/MbQ ITxOUSQv7c7ugFFDzQGBzZswY6786m86gjpEIbb3OhjZnzcvQAaRHhdlQWIMm2nr AgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCku4nUhVVxYUntneD9+h8Mg9q6q+auN KyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0FlkbFFBjvSfpJIlJ00zbhNYS5f6Guo EDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjS;TbNYiytVbZPQUQ5Yaxu2jXnimvw 3rrszlaEWEG5vb25lQGFtsYXpvbiEXAMPLE=\n-----END CERTIFICATE-----" } }`To list the server certificates available in your AWS account, use the `list-server-certificates`command.For more information, see [Managing server certificates in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetServerCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-server-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-service-last-accessed-details-with-entities`.

- **AWS CLI**
- 
            
                    **To retrieve a service access report with details for a service**The following `get-service-last-accessed-details-with-entities`example retrieves a report that contains details about IAM users and other entities that accessed the specified service. To generate a report, use the`generate-service-last-accessed-details`command. To get a list of services accessed with namespaces, use`get-service-last-accessed-details`.`aws iam get-service-last-accessed-details-with-entities \ --job-id``78b6c2ba-d09e-6xmp-7039-ecde30b26916`\ --service-namespace`lambda`Output: `{ "JobStatus": "COMPLETED", "JobCreationDate": "2019-10-01T03:55:41.756Z", "JobCompletionDate": "2019-10-01T03:55:42.533Z", "EntityDetailsList": [ { "EntityInfo": { "Arn": "arn:aws:iam::123456789012:user/admin", "Name": "admin", "Type": "USER", "Id": "AIDAIO2XMPLENQEXAMPLE", "Path": "/" }, "LastAuthenticated": "2019-09-30T23:02:00Z" }, { "EntityInfo": { "Arn": "arn:aws:iam::123456789012:user/developer", "Name": "developer", "Type": "USER", "Id": "AIDAIBEYXMPL2YEXAMPLE", "Path": "/" }, "LastAuthenticated": "2019-09-16T19:34:00Z" } ] }`For more information, see [Refining permissions in AWS using last accessed information](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetServiceLastAccessedDetailsWithEntities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-service-last-accessed-details-with-entities.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-service-last-accessed-details`.

- **AWS CLI**
- 
            
                    **To retrieve a service access report**The following `get-service-last-accessed-details`example retrieves a previously generated report that lists the services accessed by IAM entities. To generate a report, use the`generate-service-last-accessed-details`command.`aws iam get-service-last-accessed-details \ --job-id``2eb6c2b8-7b4c-3xmp-3c13-03b72c8cdfdc`Output: `{ "JobStatus": "COMPLETED", "JobCreationDate": "2019-10-01T03:50:35.929Z", "ServicesLastAccessed": [ ... { "ServiceName": "AWS Lambda", "LastAuthenticated": "2019-09-30T23:02:00Z", "ServiceNamespace": "lambda", "LastAuthenticatedEntity": "arn:aws:iam::123456789012:user/admin", "TotalAuthenticatedEntities": 6 }, ] }`For more information, see [Refining permissions in AWS using last accessed information](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetServiceLastAccessedDetails](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-service-last-accessed-details.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-service-linked-role-deletion-status`.

- **AWS CLI**
- 
            
                    **To check the status of a request to delete a service-linked role**The following `get-service-linked-role-deletion-status`example displays the status of a previously request to delete a service-linked role. The delete operation occurs asynchronously. When you make the request, you get a`DeletionTaskId`value that you provide as a parameter for this command.`aws iam get-service-linked-role-deletion-status \ --deletion-task-id``task/aws-service-role/lex.amazonaws.com/AWSServiceRoleForLexBots/1a2b3c4d-1234-abcd-7890-abcdeEXAMPLE`Output: `{ "Status": "SUCCEEDED" }`For more information, see [Using service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetServiceLinkedRoleDeletionStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-service-linked-role-deletion-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-ssh-public-key`.

- **AWS CLI**
- 
            
                    **Example 1: To retrieve an SSH public key attached to an IAM user in SSH encoded form**The following `get-ssh-public-key`command retrieves the specified SSH public key from the IAM user`sofia`. The output is in SSH encoding.`aws iam get-ssh-public-key \ --user-name``sofia`\ --ssh-public-key-id`APKA123456789EXAMPLE`\ --encoding`SSH`Output: `{ "SSHPublicKey": { "UserName": "sofia", "SSHPublicKeyId": "APKA123456789EXAMPLE", "Fingerprint": "12:34:56:78:90:ab:cd:ef:12:34:56:78:90:ab:cd:ef", "SSHPublicKeyBody": "ssh-rsa <<long encoded SSH string>>", "Status": "Inactive", "UploadDate": "2019-04-18T17:04:49+00:00" } }`**Example 2: To retrieve an SSH public key attached to an IAM user in PEM encoded form**The following `get-ssh-public-key`command retrieves the specified SSH public key from the IAM user`sofia`. The output is in PEM encoding.`aws iam get-ssh-public-key \ --user-name``sofia`\ --ssh-public-key-id`APKA123456789EXAMPLE`\ --encoding`PEM`Output: `{ "SSHPublicKey": { "UserName": "sofia", "SSHPublicKeyId": "APKA123456789EXAMPLE", "Fingerprint": "12:34:56:78:90:ab:cd:ef:12:34:56:78:90:ab:cd:ef", "SSHPublicKeyBody": ""-----BEGIN PUBLIC KEY-----\n<<long encoded PEM string>>\n-----END PUBLIC KEY-----\n"", "Status": "Inactive", "UploadDate": "2019-04-18T17:04:49+00:00" } }`For more information, see [Use SSH keys and SSH with CodeCommit](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_ssh-keys.html#ssh-keys-code-commit)in the*AWS IAM User Guide*.- 
                    For API details, see [GetSshPublicKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-ssh-public-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-user-policy`.

- **AWS CLI**
- 
            
                    **To list policy details for an IAM user**The following `get-user-policy`command lists the details of the specified policy that is attached to the IAM user named`Bob`.`aws iam get-user-policy \ --user-name``Bob`\ --policy-name`ExamplePolicy`Output: `{ "UserName": "Bob", "PolicyName": "ExamplePolicy", "PolicyDocument": { "Version":"2012-10-17", "Statement": [ { "Action": "*", "Resource": "*", "Effect": "Allow" } ] } }`To get a list of policies for an IAM user, use the `list-user-policies`command.For more information, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetUserPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-user-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-user`.

- **AWS CLI**
- 
            
                    **To get information about an IAM user**The following `get-user`command gets information about the IAM user named`Paulo`.`aws iam get-user \ --user-name``Paulo`Output: `{ "User": { "UserName": "Paulo", "Path": "/", "CreateDate": "2019-09-21T23:03:13Z", "UserId": "AIDA123456789EXAMPLE", "Arn": "arn:aws:iam::123456789012:user/Paulo" } }`For more information, see [Managing IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_manage.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-access-keys`.

- **AWS CLI**
- 
            
                    **To list the access key IDs for an IAM user**The following `list-access-keys`command lists the access keys IDs for the IAM user named`Bob`.`aws iam list-access-keys \ --user-name``Bob`Output: `{ "AccessKeyMetadata": [ { "UserName": "Bob", "Status": "Active", "CreateDate": "2013-06-04T18:17:34Z", "AccessKeyId": "AKIAIOSFODNN7EXAMPLE" }, { "UserName": "Bob", "Status": "Inactive", "CreateDate": "2013-06-06T20:42:26Z", "AccessKeyId": "AKIAI44QH8DHBEXAMPLE" } ] }`You cannot list the secret access keys for IAM users. If the secret access keys are lost, you must create new access keys using the `create-access-keys`command.For more information, see [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListAccessKeys](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-access-keys.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-account-aliases`.

- **AWS CLI**
- 
            
                    **To list account aliases**The following `list-account-aliases`command lists the aliases for the current account.`aws iam list-account-aliases`Output: `{ "AccountAliases": [ "mycompany" ] }`For more information, see [Your AWS account ID and its alias](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListAccountAliases](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-account-aliases.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-attached-group-policies`.

- **AWS CLI**
- 
            
                    **To list all managed policies that are attached to the specified group**This example returns the names and ARNs of the managed policies that are attached to the IAM group named `Admins`in the AWS account.`aws iam list-attached-group-policies \ --group-name``Admins`Output: `{ "AttachedPolicies": [ { "PolicyName": "AdministratorAccess", "PolicyArn": "arn:aws:iam::aws:policy/AdministratorAccess" }, { "PolicyName": "SecurityAudit", "PolicyArn": "arn:aws:iam::aws:policy/SecurityAudit" } ], "IsTruncated": false }`For more information, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListAttachedGroupPolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-attached-group-policies.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-attached-role-policies`.

- **AWS CLI**
- 
            
                    **To list all managed policies that are attached to the specified role**This command returns the names and ARNs of the managed policies attached to the IAM role named `SecurityAuditRole`in the AWS account.`aws iam list-attached-role-policies \ --role-name``SecurityAuditRole`Output: `{ "AttachedPolicies": [ { "PolicyName": "SecurityAudit", "PolicyArn": "arn:aws:iam::aws:policy/SecurityAudit" } ], "IsTruncated": false }`For more information, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListAttachedRolePolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-attached-role-policies.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-attached-user-policies`.

- **AWS CLI**
- 
            
                    **To list all managed policies that are attached to the specified user**This command returns the names and ARNs of the managed policies for the IAM user named `Bob`in the AWS account.`aws iam list-attached-user-policies \ --user-name``Bob`Output: `{ "AttachedPolicies": [ { "PolicyName": "AdministratorAccess", "PolicyArn": "arn:aws:iam::aws:policy/AdministratorAccess" }, { "PolicyName": "SecurityAudit", "PolicyArn": "arn:aws:iam::aws:policy/SecurityAudit" } ], "IsTruncated": false }`For more information, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListAttachedUserPolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-attached-user-policies.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-entities-for-policy`.

- **AWS CLI**
- 
            
                    **To list all users, groups, and roles that the specified managed policy is attached to**This example returns a list of IAM groups, roles, and users who have the policy `arn:aws:iam::123456789012:policy/TestPolicy`attached.`aws iam list-entities-for-policy \ --policy-arn``arn:aws:iam::123456789012:policy/TestPolicy`Output: `{ "PolicyGroups": [ { "GroupName": "Admins", "GroupId": "AGPACKCEVSQ6C2EXAMPLE" } ], "PolicyUsers": [ { "UserName": "Alice", "UserId": "AIDACKCEVSQ6C2EXAMPLE" } ], "PolicyRoles": [ { "RoleName": "DevRole", "RoleId": "AROADBQP57FF2AEXAMPLE" } ], "IsTruncated": false }`For more information, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListEntitiesForPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-entities-for-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-group-policies`.

- **AWS CLI**
- 
            
                    **To list all inline policies that are attached to the specified group**The following `list-group-policies`command lists the names of inline policies that are attached to the IAM group named`Admins`in the current account.`aws iam list-group-policies \ --group-name``Admins`Output: `{ "PolicyNames": [ "AdminRoot", "ExamplePolicy" ] }`For more information, see [Managing IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListGroupPolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-group-policies.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-groups-for-user`.

- **AWS CLI**
- 
            
                    **To list the groups that an IAM user belongs to**The following `list-groups-for-user`command displays the groups that the IAM user named`Bob`belongs to.`aws iam list-groups-for-user \ --user-name``Bob`Output: `{ "Groups": [ { "Path": "/", "CreateDate": "2013-05-06T01:18:08Z", "GroupId": "AKIAIOSFODNN7EXAMPLE", "Arn": "arn:aws:iam::123456789012:group/Admin", "GroupName": "Admin" }, { "Path": "/", "CreateDate": "2013-05-06T01:37:28Z", "GroupId": "AKIAI44QH8DHBEXAMPLE", "Arn": "arn:aws:iam::123456789012:group/s3-Users", "GroupName": "s3-Users" } ] }`For more information, see [Managing IAM user groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListGroupsForUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-groups-for-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-groups`.

- **AWS CLI**
- 
            
                    **To list the IAM groups for the current account**The following `list-groups`command lists the IAM groups in the current account.`aws iam list-groups`Output: `{ "Groups": [ { "Path": "/", "CreateDate": "2013-06-04T20:27:27.972Z", "GroupId": "AIDACKCEVSQ6C2EXAMPLE", "Arn": "arn:aws:iam::123456789012:group/Admins", "GroupName": "Admins" }, { "Path": "/", "CreateDate": "2013-04-16T20:30:42Z", "GroupId": "AIDGPMS9RO4H3FEXAMPLE", "Arn": "arn:aws:iam::123456789012:group/S3-Admins", "GroupName": "S3-Admins" } ] }`For more information, see [Managing IAM user groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-instance-profile-tags`.

- **AWS CLI**
- 
            
                    **To list the tags attached to an instance profile**The following `list-instance-profile-tags`command retrieves the list of tags associated with the specified instance profile.`aws iam list-instance-profile-tags \ --instance-profile-name``deployment-role`Output: `{ "Tags": [ { "Key": "DeptID", "Value": "123456" }, { "Key": "Department", "Value": "Accounting" } ] }`For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListInstanceProfileTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-instance-profile-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-instance-profiles-for-role`.

- **AWS CLI**
- 
            
                    **To list the instance profiles for an IAM role**The following `list-instance-profiles-for-role`command lists the instance profiles that are associated with the role`Test-Role`.`aws iam list-instance-profiles-for-role \ --role-name``Test-Role`Output: `{ "InstanceProfiles": [ { "InstanceProfileId": "AIDGPMS9RO4H3FEXAMPLE", "Roles": [ { "AssumeRolePolicyDocument": "<URL-encoded-JSON>", "RoleId": "AIDACKCEVSQ6C2EXAMPLE", "CreateDate": "2013-06-07T20:42:15Z", "RoleName": "Test-Role", "Path": "/", "Arn": "arn:aws:iam::123456789012:role/Test-Role" } ], "CreateDate": "2013-06-07T21:05:24Z", "InstanceProfileName": "ExampleInstanceProfile", "Path": "/", "Arn": "arn:aws:iam::123456789012:instance-profile/ExampleInstanceProfile" } ] }`For more information, see [Using instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListInstanceProfilesForRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-instance-profiles-for-role.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-instance-profiles`.

- **AWS CLI**
- 
            
                    **To lists the instance profiles for the account**The following `list-instance-profiles`command lists the instance profiles that are associated with the current account.`aws iam list-instance-profiles`Output: `{ "InstanceProfiles": [ { "Path": "/", "InstanceProfileName": "example-dev-role", "InstanceProfileId": "AIPAIXEU4NUHUPEXAMPLE", "Arn": "arn:aws:iam::123456789012:instance-profile/example-dev-role", "CreateDate": "2023-09-21T18:17:41+00:00", "Roles": [ { "Path": "/", "RoleName": "example-dev-role", "RoleId": "AROAJ52OTH4H7LEXAMPLE", "Arn": "arn:aws:iam::123456789012:role/example-dev-role", "CreateDate": "2023-09-21T18:17:40+00:00", "AssumeRolePolicyDocument": { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "Service": "ec2.amazonaws.com" }, "Action": "sts:AssumeRole" } ] } } ] }, { "Path": "/", "InstanceProfileName": "example-s3-role", "InstanceProfileId": "AIPAJVJVNRIQFREXAMPLE", "Arn": "arn:aws:iam::123456789012:instance-profile/example-s3-role", "CreateDate": "2023-09-21T18:18:50+00:00", "Roles": [ { "Path": "/", "RoleName": "example-s3-role", "RoleId": "AROAINUBC5O7XLEXAMPLE", "Arn": "arn:aws:iam::123456789012:role/example-s3-role", "CreateDate": "2023-09-21T18:18:49+00:00", "AssumeRolePolicyDocument": { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "Service": "ec2.amazonaws.com" }, "Action": "sts:AssumeRole" } ] } } ] } ] }`For more information, see [Using instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListInstanceProfiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-instance-profiles.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-mfa-device-tags`.

- **AWS CLI**
- 
            
                    **To list the tags attached to an MFA device**The following `list-mfa-device-tags`command retrieves the list of tags associated with the specified MFA device.`aws iam list-mfa-device-tags \ --serial-number``arn:aws:iam::123456789012:mfa/alice`Output: `{ "Tags": [ { "Key": "DeptID", "Value": "123456" }, { "Key": "Department", "Value": "Accounting" } ] }`For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListMfaDeviceTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-mfa-device-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-mfa-devices`.

- **AWS CLI**
- 
            
                    **To list all MFA devices for a specified user**This example returns details about the MFA device assigned to the IAM user `Bob`.`aws iam list-mfa-devices \ --user-name``Bob`Output: `{ "MFADevices": [ { "UserName": "Bob", "SerialNumber": "arn:aws:iam::123456789012:mfa/Bob", "EnableDate": "2019-10-28T20:37:09+00:00" }, { "UserName": "Bob", "SerialNumber": "GAKT12345678", "EnableDate": "2023-02-18T21:44:42+00:00" }, { "UserName": "Bob", "SerialNumber": "arn:aws:iam::123456789012:u2f/user/Bob/fidosecuritykey1-7XNL7NFNLZ123456789EXAMPLE", "EnableDate": "2023-09-19T02:25:35+00:00" }, { "UserName": "Bob", "SerialNumber": "arn:aws:iam::123456789012:u2f/user/Bob/fidosecuritykey2-VDRQTDBBN5123456789EXAMPLE", "EnableDate": "2023-09-19T01:49:18+00:00" } ] }`For more information, see [Using multi-factor authentication (MFA) in AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListMfaDevices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-mfa-devices.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-open-id-connect-provider-tags`.

- **AWS CLI**
- 
            
                    **To list the tags attached to an OpenID Connect (OIDC)-compatible identity provider**The following `list-open-id-connect-provider-tags`command retrieves the list of tags associated with the specified OIDC identity provider.`aws iam list-open-id-connect-provider-tags \ --open-id-connect-provider-arn``arn:aws:iam::123456789012:oidc-provider/server.example.com`Output: `{ "Tags": [ { "Key": "DeptID", "Value": "123456" }, { "Key": "Department", "Value": "Accounting" } ] }`For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListOpenIdConnectProviderTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-open-id-connect-provider-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-open-id-connect-providers`.

- **AWS CLI**
- 
            
                    **To list information about the OpenID Connect providers in the AWS account**This example returns a list of ARNS of all the OpenID Connect providers that are defined in the current AWS account. `aws iam list-open-id-connect-providers`Output: `{ "OpenIDConnectProviderList": [ { "Arn": "arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com" } ] }`For more information, see [Creating OpenID Connect (OIDC) identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListOpenIdConnectProviders](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-open-id-connect-providers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-organizations-features`.

- **AWS CLI**
- 
            
                    **To list the centralized root access features enabled for your organization**The following `list-organizations-features`command lists the centralized root access features enabled for your organization.`aws iam list-organizations-features`Output: `{ "EnabledFeatures": [ "RootCredentialsManagement", "RootSessions" ] "OrganizationId": "o-aa111bb222" }`For more information, see [Centrally manage root access for member accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user-access-management)in the*AWS IAM User Guide*.- 
                    For API details, see [ListOrganizationsFeatures](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-organizations-features.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-policies-granting-service-access`.

- **AWS CLI**
- 
            
                    **To list the policies that grant a principal access to the specified service**The following `list-policies-granting-service-access`example retrieves the list of policies that grant the IAM user`sofia`access to AWS CodeCommit service.`aws iam list-policies-granting-service-access \ --arn``arn:aws:iam::123456789012:user/sofia`\ --service-namespaces`codecommit`Output: `{ "PoliciesGrantingServiceAccess": [ { "ServiceNamespace": "codecommit", "Policies": [ { "PolicyName": "Grant-Sofia-Access-To-CodeCommit", "PolicyType": "INLINE", "EntityType": "USER", "EntityName": "sofia" } ] } ], "IsTruncated": false }`For more information, see [Using IAM with CodeCommit: Git credentials, SSH keys, and AWS access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_ssh-keys.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListPoliciesGrantingServiceAccess](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-policies-granting-service-access.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-policies`.

- **AWS CLI**
- 
            
                    **To list managed policies that are available to your AWS account**This example returns a collection of the first two managed policies available in the current AWS account. `aws iam list-policies \ --max-items``3`Output: `{ "Policies": [ { "PolicyName": "AWSCloudTrailAccessPolicy", "PolicyId": "ANPAXQE2B5PJ7YEXAMPLE", "Arn": "arn:aws:iam::123456789012:policy/AWSCloudTrailAccessPolicy", "Path": "/", "DefaultVersionId": "v1", "AttachmentCount": 0, "PermissionsBoundaryUsageCount": 0, "IsAttachable": true, "CreateDate": "2019-09-04T17:43:42+00:00", "UpdateDate": "2019-09-04T17:43:42+00:00" }, { "PolicyName": "AdministratorAccess", "PolicyId": "ANPAIWMBCKSKIEE64ZLYK", "Arn": "arn:aws:iam::aws:policy/AdministratorAccess", "Path": "/", "DefaultVersionId": "v1", "AttachmentCount": 6, "PermissionsBoundaryUsageCount": 0, "IsAttachable": true, "CreateDate": "2015-02-06T18:39:46+00:00", "UpdateDate": "2015-02-06T18:39:46+00:00" }, { "PolicyName": "PowerUserAccess", "PolicyId": "ANPAJYRXTHIB4FOVS3ZXS", "Arn": "arn:aws:iam::aws:policy/PowerUserAccess", "Path": "/", "DefaultVersionId": "v5", "AttachmentCount": 1, "PermissionsBoundaryUsageCount": 0, "IsAttachable": true, "CreateDate": "2015-02-06T18:39:47+00:00", "UpdateDate": "2023-07-06T22:04:00+00:00" } ], "NextToken": "EXAMPLErZXIiOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiA4fQ==" }`For more information, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListPolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-policies.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-policy-tags`.

- **AWS CLI**
- 
            
                    **To list the tags attached to a managed policy**The following `list-policy-tags`command retrieves the list of tags associated with the specified managed policy.`aws iam list-policy-tags \ --policy-arn``arn:aws:iam::123456789012:policy/billing-access`Output: `{ "Tags": [ { "Key": "DeptID", "Value": "123456" }, { "Key": "Department", "Value": "Accounting" } ] }`For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListPolicyTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-policy-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-policy-versions`.

- **AWS CLI**
- 
            
                    **To list information about the versions of the specified managed policy**This example returns the list of available versions of the policy whose ARN is `arn:aws:iam::123456789012:policy/MySamplePolicy`.`aws iam list-policy-versions \ --policy-arn``arn:aws:iam::123456789012:policy/MySamplePolicy`Output: `{ "IsTruncated": false, "Versions": [ { "VersionId": "v2", "IsDefaultVersion": true, "CreateDate": "2015-06-02T23:19:44Z" }, { "VersionId": "v1", "IsDefaultVersion": false, "CreateDate": "2015-06-02T22:30:47Z" } ] }`For more information, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListPolicyVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-policy-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-role-policies`.

- **AWS CLI**
- 
            
                    **To list the policies attached to an IAM role**The following `list-role-policies`command lists the names of the permissions policies for the specified IAM role.`aws iam list-role-policies \ --role-name``Test-Role`Output: `{ "PolicyNames": [ "ExamplePolicy" ] }`To see the trust policy attached to a role, use the `get-role`command. To see the details of a permissions policy, use the`get-role-policy`command.For more information, see [Creating IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListRolePolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-role-policies.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-role-tags`.

- **AWS CLI**
- 
            
                    **To list the tags attached to a role**The following `list-role-tags`command retrieves the list of tags associated with the specified role.`aws iam list-role-tags \ --role-name``production-role`Output: `{ "Tags": [ { "Key": "Department", "Value": "Accounting" }, { "Key": "DeptID", "Value": "12345" } ], "IsTruncated": false }`For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListRoleTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-role-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-roles`.

- **AWS CLI**
- 
            
                    **To list IAM roles for the current account**The following `list-roles`command lists IAM roles for the current account.`aws iam list-roles`Output: `{ "Roles": [ { "Path": "/", "RoleName": "ExampleRole", "RoleId": "AROAJ52OTH4H7LEXAMPLE", "Arn": "arn:aws:iam::123456789012:role/ExampleRole", "CreateDate": "2017-09-12T19:23:36+00:00", "AssumeRolePolicyDocument": { "Version":"2012-10-17", "Statement": [ { "Sid": "", "Effect": "Allow", "Principal": { "Service": "ec2.amazonaws.com" }, "Action": "sts:AssumeRole" } ] }, "MaxSessionDuration": 3600 }, { "Path": "/example_path/", "RoleName": "ExampleRoleWithPath", "RoleId": "AROAI4QRP7UFT7EXAMPLE", "Arn": "arn:aws:iam::123456789012:role/example_path/ExampleRoleWithPath", "CreateDate": "2023-09-21T20:29:38+00:00", "AssumeRolePolicyDocument": { "Version":"2012-10-17", "Statement": [ { "Sid": "", "Effect": "Allow", "Principal": { "Service": "ec2.amazonaws.com" }, "Action": "sts:AssumeRole" } ] }, "MaxSessionDuration": 3600 } ] }`For more information, see [Creating IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListRoles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-roles.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-saml-provider-tags`.

- **AWS CLI**
- 
            
                    **To list the tags attached to a SAML provider**The following `list-saml-provider-tags`command retrieves the list of tags associated with the specified SAML provider.`aws iam list-saml-provider-tags \ --saml-provider-arn``arn:aws:iam::123456789012:saml-provider/ADFS`Output: `{ "Tags": [ { "Key": "DeptID", "Value": "123456" }, { "Key": "Department", "Value": "Accounting" } ] }`For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListSamlProviderTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-saml-provider-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-saml-providers`.

- **AWS CLI**
- 
            
                    **To list the SAML providers in the AWS account**This example retrieves the list of SAML 2.0 providers created in the current AWS account. `aws iam list-saml-providers`Output: `{ "SAMLProviderList": [ { "Arn": "arn:aws:iam::123456789012:saml-provider/SAML-ADFS", "ValidUntil": "2015-06-05T22:45:14Z", "CreateDate": "2015-06-05T22:45:14Z" } ] }`For more information, see [Creating IAM SAML identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListSAMLProviders](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-saml-providers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-server-certificate-tags`.

- **AWS CLI**
- 
            
                    **To list the tags attached to a server certificate**The following `list-server-certificate-tags`command retrieves the list of tags associated with the specified server certificate.`aws iam list-server-certificate-tags \ --server-certificate-name``ExampleCertificate`Output: `{ "Tags": [ { "Key": "DeptID", "Value": "123456" }, { "Key": "Department", "Value": "Accounting" } ] }`For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListServerCertificateTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-server-certificate-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-server-certificates`.

- **AWS CLI**
- 
            
                    **To list the server certificates in your AWS account**The following `list-server-certificates`command lists all of the server certificates stored and available for use in your AWS account.`aws iam list-server-certificates`Output: `{ "ServerCertificateMetadataList": [ { "Path": "/", "ServerCertificateName": "myUpdatedServerCertificate", "ServerCertificateId": "ASCAEXAMPLE123EXAMPLE", "Arn": "arn:aws:iam::123456789012:server-certificate/myUpdatedServerCertificate", "UploadDate": "2019-04-22T21:13:44+00:00", "Expiration": "2019-10-15T22:23:16+00:00" }, { "Path": "/cloudfront/", "ServerCertificateName": "MyTestCert", "ServerCertificateId": "ASCAEXAMPLE456EXAMPLE", "Arn": "arn:aws:iam::123456789012:server-certificate/Org1/Org2/MyTestCert", "UploadDate": "2015-04-21T18:14:16+00:00", "Expiration": "2018-01-14T17:52:36+00:00" } ] }`For more information, see [Managing server certificates in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListServerCertificates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-server-certificates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-service-specific-credential`.

- **AWS CLI**
- 
            
                    **Example 1: List the service-specific credentials for a user**The following `list-service-specific-credentials`example displays all service-specific credentials assigned to the specified user. Passwords are not included in the response.`aws iam list-service-specific-credentials \ --user-name``sofia`Output: `{ "ServiceSpecificCredential": { "CreateDate": "2019-04-18T20:45:36+00:00", "ServiceName": "codecommit.amazonaws.com", "ServiceUserName": "sofia-at-123456789012", "ServiceSpecificCredentialId": "ACCAEXAMPLE123EXAMPLE", "UserName": "sofia", "Status": "Active" } }`**Example 2: List the service-specific credentials for a user filtered to a specified service**The following `list-service-specific-credentials`example displays the service-specific credentials assigned to the user making the request. The list is filtered to include only those credentials for the specified service. Passwords are not included in the response.`aws iam list-service-specific-credentials \ --service-name``codecommit.amazonaws.com`Output: `{ "ServiceSpecificCredential": { "CreateDate": "2019-04-18T20:45:36+00:00", "ServiceName": "codecommit.amazonaws.com", "ServiceUserName": "sofia-at-123456789012", "ServiceSpecificCredentialId": "ACCAEXAMPLE123EXAMPLE", "UserName": "sofia", "Status": "Active" } }`For more information, see [Create Git credentials for HTTPS connections to CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-gc.html#setting-up-gc-iam)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [ListServiceSpecificCredential](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-service-specific-credential.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-service-specific-credentials`.

- **AWS CLI**
- 
            
                    **To retrieve a list of credentials**The following `list-service-specific-credentials`example lists the credentials generated for HTTPS access to AWS CodeCommit repositories for a user named`developer`.`aws iam list-service-specific-credentials \ --user-name``developer`\ --service-name`codecommit.amazonaws.com`Output: `{ "ServiceSpecificCredentials": [ { "UserName": "developer", "Status": "Inactive", "ServiceUserName": "developer-at-123456789012", "CreateDate": "2019-10-01T04:31:41Z", "ServiceSpecificCredentialId": "ACCAQFODXMPL4YFHP7DZE", "ServiceName": "codecommit.amazonaws.com" }, { "UserName": "developer", "Status": "Active", "ServiceUserName": "developer+1-at-123456789012", "CreateDate": "2019-10-01T04:31:45Z", "ServiceSpecificCredentialId": "ACCAQFOXMPL6VW57M7AJP", "ServiceName": "codecommit.amazonaws.com" } ] }`For more information, see [Create Git credentials for HTTPS connections to CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-gc.html#setting-up-gc-iam)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [ListServiceSpecificCredentials](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-service-specific-credentials.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-signing-certificates`.

- **AWS CLI**
- 
            
                    **To list the signing certificates for an IAM user**The following `list-signing-certificates`command lists the signing certificates for the IAM user named`Bob`.`aws iam list-signing-certificates \ --user-name``Bob`Output: `{ "Certificates": [ { "UserName": "Bob", "Status": "Inactive", "CertificateBody": "-----BEGIN CERTIFICATE-----<certificate-body>-----END CERTIFICATE-----", "CertificateId": "TA7SMP42TDN5Z26OBPJE7EXAMPLE", "UploadDate": "2013-06-06T21:40:08Z" } ] }`For more information, see [Manage signing certificates](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-up-ami-tools.html#ami-tools-managing-certs)in the*Amazon EC2 User Guide*.- 
                    For API details, see [ListSigningCertificates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-signing-certificates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-ssh-public-keys`.

- **AWS CLI**
- 
            
                    **To list the SSH public keys attached to an IAM user**The following `list-ssh-public-keys`example lists the SSH public keys attached to the IAM user`sofia`.`aws iam list-ssh-public-keys \ --user-name``sofia`Output: `{ "SSHPublicKeys": [ { "UserName": "sofia", "SSHPublicKeyId": "APKA1234567890EXAMPLE", "Status": "Inactive", "UploadDate": "2019-04-18T17:04:49+00:00" } ] }`For more information, see [Use SSH keys and SSH with CodeCommit](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_ssh-keys.html#ssh-keys-code-commit)in the*AWS IAM User Guide*- 
                    For API details, see [ListSshPublicKeys](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-ssh-public-keys.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-user-policies`.

- **AWS CLI**
- 
            
                    **To list policies for an IAM user**The following `list-user-policies`command lists the policies that are attached to the IAM user named`Bob`.`aws iam list-user-policies \ --user-name``Bob`Output: `{ "PolicyNames": [ "ExamplePolicy", "TestPolicy" ] }`For more information, see [Creating an IAM user in your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListUserPolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-user-policies.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-user-tags`.

- **AWS CLI**
- 
            
                    **To list the tags attached to a user**The following `list-user-tags`command retrieves the list of tags associated with the specified IAM user.`aws iam list-user-tags \ --user-name``alice`Output: `{ "Tags": [ { "Key": "Department", "Value": "Accounting" }, { "Key": "DeptID", "Value": "12345" } ], "IsTruncated": false }`For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListUserTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-user-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-users`.

- **AWS CLI**
- 
            
                    **To list IAM users**The following `list-users`command lists the IAM users in the current account.`aws iam list-users`Output: `{ "Users": [ { "UserName": "Adele", "Path": "/", "CreateDate": "2013-03-07T05:14:48Z", "UserId": "AKIAI44QH8DHBEXAMPLE", "Arn": "arn:aws:iam::123456789012:user/Adele" }, { "UserName": "Bob", "Path": "/", "CreateDate": "2012-09-21T23:03:13Z", "UserId": "AKIAIOSFODNN7EXAMPLE", "Arn": "arn:aws:iam::123456789012:user/Bob" } ] }`For more information, see [Listing IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_manage.html#id_users_manage_list)in the*AWS IAM User Guide*.- 
                    For API details, see [ListUsers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-users.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-virtual-mfa-devices`.

- **AWS CLI**
- 
            
                    **To list virtual MFA devices**The following `list-virtual-mfa-devices`command lists the virtual MFA devices that have been configured for the current account.`aws iam list-virtual-mfa-devices`Output: `{ "VirtualMFADevices": [ { "SerialNumber": "arn:aws:iam::123456789012:mfa/ExampleMFADevice" }, { "SerialNumber": "arn:aws:iam::123456789012:mfa/Fred" } ] }`For more information, see [Enabling a virtual multi-factor authentication (MFA) device](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListVirtualMfaDevices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-virtual-mfa-devices.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-group-policy`.

- **AWS CLI**
- 
            
                    **To add a policy to a group**The following `put-group-policy`command adds a policy to the IAM group named`Admins`.`aws iam put-group-policy \ --group-name``Admins`\ --policy-document`file://AdminPolicy.json`\ --policy-name`AdminRoot`This command produces no output. The policy is defined as a JSON document in the *AdminPolicy.json*file. (The file name and extension do not have significance.)For more information, see [Managing IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage.html)in the*AWS IAM User Guide*.- 
                    For API details, see [PutGroupPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/put-group-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-role-permissions-boundary`.

- **AWS CLI**
- 
            
                    **Example 1: To apply a permissions boundary based on a custom policy to an IAM role**The following `put-role-permissions-boundary`example applies the custom policy named`intern-boundary`as the permissions boundary for the specified IAM role.`aws iam put-role-permissions-boundary \ --permissions-boundary``arn:aws:iam::123456789012:policy/intern-boundary`\ --role-name`lambda-application-role`This command produces no output. **Example 2: To apply a permissions boundary based on an AWS managed policy to an IAM role**The following `put-role-permissions-boundary`example applies the AWS managed`PowerUserAccess`policy as the permissions boundary for the specified IAM role.`aws iam put-role-permissions-boundary \ --permissions-boundary``arn:aws:iam::aws:policy/PowerUserAccess`\ --role-name`x-account-admin`This command produces no output. For more information, see [Modifying a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_modify.html)in the*AWS IAM User Guide*.- 
                    For API details, see [PutRolePermissionsBoundary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/put-role-permissions-boundary.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-role-policy`.

- **AWS CLI**
- 
            
                    **To attach a permissions policy to an IAM role**The following `put-role-policy`command adds a permissions policy to the role named`Test-Role`.`aws iam put-role-policy \ --role-name``Test-Role`\ --policy-name`ExamplePolicy`\ --policy-document`file://AdminPolicy.json`This command produces no output. The policy is defined as a JSON document in the *AdminPolicy.json*file. (The file name and extension do not have significance.)To attach a trust policy to a role, use the `update-assume-role-policy`command.For more information, see [Modifying a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_modify.html)in the*AWS IAM User Guide*.- 
                    For API details, see [PutRolePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/put-role-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-user-permissions-boundary`.

- **AWS CLI**
- 
            
                    **Example 1: To apply a permissions boundary based on a custom policy to an IAM user**The following `put-user-permissions-boundary`example applies a custom policy named`intern-boundary`as the permissions boundary for the specified IAM user.`aws iam put-user-permissions-boundary \ --permissions-boundary``arn:aws:iam::123456789012:policy/intern-boundary`\ --user-name`intern`This command produces no output. **Example 2: To apply a permissions boundary based on an AWS managed policy to an IAM user**The following `put-user-permissions-boundary`example applies the AWS managed pollicy named`PowerUserAccess`as the permissions boundary for the specified IAM user.`aws iam put-user-permissions-boundary \ --permissions-boundary``arn:aws:iam::aws:policy/PowerUserAccess`\ --user-name`developer`This command produces no output. For more information, see [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html)in the*AWS IAM User Guide*.- 
                    For API details, see [PutUserPermissionsBoundary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/put-user-permissions-boundary.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-user-policy`.

- **AWS CLI**
- 
            
                    **To attach a policy to an IAM user**The following `put-user-policy`command attaches a policy to the IAM user named`Bob`.`aws iam put-user-policy \ --user-name``Bob`\ --policy-name`ExamplePolicy`\ --policy-document`file://AdminPolicy.json`This command produces no output. The policy is defined as a JSON document in the *AdminPolicy.json*file. (The file name and extension do not have significance.)For more information, see [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html)in the*AWS IAM User Guide*.- 
                    For API details, see [PutUserPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/put-user-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-client-id-from-open-id-connect-provider`.

- **AWS CLI**
- 
            
                    **To remove the specified client ID from the list of client IDs registered for the specified IAM OpenID Connect provider**This example removes the client ID `My-TestApp-3`from the list of client IDs associated with the IAM OIDC provider whose ARN is`arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com`.`aws iam remove-client-id-from-open-id-connect-provider --client-id``My-TestApp-3`\ --open-id-connect-provider-arn`arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com`This command produces no output. For more information, see [Creating OpenID Connect (OIDC) identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html)in the*AWS IAM User Guide*.- 
                    For API details, see [RemoveClientIdFromOpenIdConnectProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/remove-client-id-from-open-id-connect-provider.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-role-from-instance-profile`.

- **AWS CLI**
- 
            
                    **To remove a role from an instance profile**The following `remove-role-from-instance-profile`command removes the role named`Test-Role`from the instance profile named`ExampleInstanceProfile`.`aws iam remove-role-from-instance-profile \ --instance-profile-name``ExampleInstanceProfile`\ --role-name`Test-Role`For more information, see [Using instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html)in the*AWS IAM User Guide*.- 
                    For API details, see [RemoveRoleFromInstanceProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/remove-role-from-instance-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-user-from-group`.

- **AWS CLI**
- 
            
                    **To remove a user from an IAM group**The following `remove-user-from-group`command removes the user named`Bob`from the IAM group named`Admins`.`aws iam remove-user-from-group \ --user-name``Bob`\ --group-name`Admins`This command produces no output. For more information, see [Adding and removing users in an IAM user group](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_add-remove-users.html)in the*AWS IAM User Guide*.- 
                    For API details, see [RemoveUserFromGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/remove-user-from-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reset-service-specific-credential`.

- **AWS CLI**
- 
            
                    **Example 1: Reset the password for a service-specific credential attached to the user making the request**The following `reset-service-specific-credential`example generates a new cryptographically strong password for the specified service-specific credential attached to the user making the request.`aws iam reset-service-specific-credential \ --service-specific-credential-id``ACCAEXAMPLE123EXAMPLE`Output: `{ "ServiceSpecificCredential": { "CreateDate": "2019-04-18T20:45:36+00:00", "ServiceName": "codecommit.amazonaws.com", "ServiceUserName": "sofia-at-123456789012", "ServicePassword": "+oaFsNk7tLco+C/obP9GhhcOzGcKOayTmE3LnAmAmH4=", "ServiceSpecificCredentialId": "ACCAEXAMPLE123EXAMPLE", "UserName": "sofia", "Status": "Active" } }`**Example 2: Reset the password for a service-specific credential attached to a specified user**The following `reset-service-specific-credential`example generates a new cryptographically strong password for a service-specific credential attached to the specified user.`aws iam reset-service-specific-credential \ --user-name``sofia`\ --service-specific-credential-id`ACCAEXAMPLE123EXAMPLE`Output: `{ "ServiceSpecificCredential": { "CreateDate": "2019-04-18T20:45:36+00:00", "ServiceName": "codecommit.amazonaws.com", "ServiceUserName": "sofia-at-123456789012", "ServicePassword": "+oaFsNk7tLco+C/obP9GhhcOzGcKOayTmE3LnAmAmH4=", "ServiceSpecificCredentialId": "ACCAEXAMPLE123EXAMPLE", "UserName": "sofia", "Status": "Active" } }`For more information, see [Create Git credentials for HTTPS connections to CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-gc.html#setting-up-gc-iam)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [ResetServiceSpecificCredential](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/reset-service-specific-credential.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `resync-mfa-device`.

- **AWS CLI**
- 
            
                    **To synchronize an MFA device**The following `resync-mfa-device`example synchronizes the MFA device that is associated with the IAM user`Bob`and whose ARN is`arn:aws:iam::123456789012:mfa/BobsMFADevice`with an authenticator program that provided the two authentication codes.`aws iam resync-mfa-device \ --user-name``Bob`\ --serial-number`arn:aws:iam::210987654321:mfa/BobsMFADevice`\ --authentication-code1`123456`\ --authentication-code2`987654`This command produces no output. For more information, see [Using multi-factor authentication (MFA) in AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ResyncMfaDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/resync-mfa-device.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-default-policy-version`.

- **AWS CLI**
- 
            
                    **To set the specified version of the specified policy as the policy's default version.**This example sets the `v2`version of the policy whose ARN is`arn:aws:iam::123456789012:policy/MyPolicy`as the default active version.`aws iam set-default-policy-version \ --policy-arn``arn:aws:iam::123456789012:policy/MyPolicy`\ --version-id`v2`For more information, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)in the*AWS IAM User Guide*.- 
                    For API details, see [SetDefaultPolicyVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/set-default-policy-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-security-token-service-preferences`.

- **AWS CLI**
- 
            
                    **To set the global endpoint token version**The following `set-security-token-service-preferences`example configures Amazon STS to use version 2 tokens when you authenticate against the global endpoint.`aws iam set-security-token-service-preferences \ --global-endpoint-token-version``v2Token`This command produces no output. For more information, see [Managing AWS STS in an AWS Region](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html)in the*AWS IAM User Guide*.- 
                    For API details, see [SetSecurityTokenServicePreferences](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/set-security-token-service-preferences.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `simulate-custom-policy`.

- **AWS CLI**
- 
            
                    **Example 1: To simulate the effects of all IAM policies associated with an IAM user or role**The following `simulate-custom-policy`shows how to provide both the policy and define variable values and simulate an API call to see if it is allowed or denied. The following example shows a policy that enables database access only after a specified date and time. The simulation succeeds because the simulated actions and the specified`aws:CurrentTime`variable all match the requirements of the policy.`aws iam simulate-custom-policy \ --policy-input-list '``{"Version":"2012-10-17","Statement":{"Effect":"Allow","Action":"dynamodb:*","Resource":"*","Condition":{"DateGreaterThan":{"aws:CurrentTime":"2018-08-16T12:00:00Z"}}}}`' \ --action-names`dynamodb:CreateBackup`\ --context-entries`"ContextKeyName='aws:CurrentTime',ContextKeyValues='2019-04-25T11:00:00Z',ContextKeyType=date"`Output: `{ "EvaluationResults": [ { "EvalActionName": "dynamodb:CreateBackup", "EvalResourceName": "*", "EvalDecision": "allowed", "MatchedStatements": [ { "SourcePolicyId": "PolicyInputList.1", "StartPosition": { "Line": 1, "Column": 38 }, "EndPosition": { "Line": 1, "Column": 167 } } ], "MissingContextValues": [] } ] }`**Example 2: To simulate a command that is prohibited by the policy**The following `simulate-custom-policy`example shows the results of simulating a command that is prohibited by the policy. In this example, the provided date is before that required by the policy's condition.`aws iam simulate-custom-policy \ --policy-input-list '``{"Version":"2012-10-17","Statement":{"Effect":"Allow","Action":"dynamodb:*","Resource":"*","Condition":{"DateGreaterThan":{"aws:CurrentTime":"2018-08-16T12:00:00Z"}}}}`' \ --action-names`dynamodb:CreateBackup`\ --context-entries`"ContextKeyName='aws:CurrentTime',ContextKeyValues='2014-04-25T11:00:00Z',ContextKeyType=date"`Output: `{ "EvaluationResults": [ { "EvalActionName": "dynamodb:CreateBackup", "EvalResourceName": "*", "EvalDecision": "implicitDeny", "MatchedStatements": [], "MissingContextValues": [] } ] }`For more information, see [Testing IAM policies with the IAM policy simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html)in the*AWS IAM User Guide*.- 
                    For API details, see [SimulateCustomPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/simulate-custom-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `simulate-principal-policy`.

- **AWS CLI**
- 
            
                    **Example 1: To simulate the effects of an arbitrary IAM policy**The following `simulate-principal-policy`shows how to simulate a user calling an API action and determining whether the policies associated with that user allow or deny the action. In the following example, the user has a policy that allows only the`codecommit:ListRepositories`action.`aws iam simulate-principal-policy \ --policy-source-arn``arn:aws:iam::123456789012:user/alejandro`\ --action-names`codecommit:ListRepositories`Output: `{ "EvaluationResults": [ { "EvalActionName": "codecommit:ListRepositories", "EvalResourceName": "*", "EvalDecision": "allowed", "MatchedStatements": [ { "SourcePolicyId": "Grant-Access-To-CodeCommit-ListRepo", "StartPosition": { "Line": 3, "Column": 19 }, "EndPosition": { "Line": 9, "Column": 10 } } ], "MissingContextValues": [] } ] }`**Example 2: To simulate the effects of a prohibited command**The following `simulate-custom-policy`example shows the results of simulating a command that is prohibited by one of the user's policies. In the following example, the user has a policy that permits access to a DynamoDB database only after a certain date and time. The simulation has the user attempting to access the database with an`aws:CurrentTime`value that is earlier than the policy's condition permits.`aws iam simulate-principal-policy \ --policy-source-arn``arn:aws:iam::123456789012:user/alejandro`\ --action-names`dynamodb:CreateBackup`\ --context-entries`"ContextKeyName='aws:CurrentTime',ContextKeyValues='2018-04-25T11:00:00Z',ContextKeyType=date"`Output: `{ "EvaluationResults": [ { "EvalActionName": "dynamodb:CreateBackup", "EvalResourceName": "*", "EvalDecision": "implicitDeny", "MatchedStatements": [], "MissingContextValues": [] } ] }`For more information, see [Testing IAM policies with the IAM policy simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html)in the*AWS IAM User Guide*.- 
                    For API details, see [SimulatePrincipalPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/simulate-principal-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-instance-profile`.

- **AWS CLI**
- 
            
                    **To add a tag to an instance profile**The following `tag-instance-profile`command adds a tag with a Department name to the specified instance profile.`aws iam tag-instance-profile \ --instance-profile-name``deployment-role`\ --tags '`[{"Key": "Department", "Value": "Accounting"}]`'This command produces no output. For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html)in the*AWS IAM User Guide*.- 
                    For API details, see [TagInstanceProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/tag-instance-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-mfa-device`.

- **AWS CLI**
- 
            
                    **To add a tag to an MFA device**The following `tag-mfa-device`command adds a tag with a Department name to the specified MFA device.`aws iam tag-mfa-device \ --serial-number``arn:aws:iam::123456789012:mfa/alice`\ --tags '`[{"Key": "Department", "Value": "Accounting"}]`'This command produces no output. For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html)in the*AWS IAM User Guide*.- 
                    For API details, see [TagMfaDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/tag-mfa-device.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-open-id-connect-provider`.

- **AWS CLI**
- 
            
                    **To add a tag to an OpenID Connect (OIDC)-compatible identity provider**The following `tag-open-id-connect-provider`command adds a tag with a Department name to the specified OIDC identity provider.`aws iam tag-open-id-connect-provider \ --open-id-connect-provider-arn``arn:aws:iam::123456789012:oidc-provider/server.example.com`\ --tags '`[{"Key": "Department", "Value": "Accounting"}]`'This command produces no output. For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html)in the*AWS IAM User Guide*.- 
                    For API details, see [TagOpenIdConnectProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/tag-open-id-connect-provider.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-policy`.

- **AWS CLI**
- 
            
                    **To add a tag to a customer managed policy**The following `tag-policy`command adds a tag with a Department name to the specified customer managed policy.`aws iam tag-policy \ --policy-arn``arn:aws:iam::123456789012:policy/billing-access`\ --tags '`[{"Key": "Department", "Value": "Accounting"}]`'This command produces no output. For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html)in the*AWS IAM User Guide*.- 
                    For API details, see [TagPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/tag-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-role`.

- **AWS CLI**
- 
            
                    **To add a tag to a role**The following `tag-role`command adds a tag with a Department name to the specified role.`aws iam tag-role --role-name``my-role`\ --tags '`{"Key": "Department", "Value": "Accounting"}`'This command produces no output. For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html)in the*AWS IAM User Guide*.- 
                    For API details, see [TagRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/tag-role.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-saml-provider`.

- **AWS CLI**
- 
            
                    **To add a tag to a SAML provider**The following `tag-saml-provider`command adds a tag with a Department name to the specified SAML provider.`aws iam tag-saml-provider \ --saml-provider-arn``arn:aws:iam::123456789012:saml-provider/ADFS`\ --tags '`[{"Key": "Department", "Value": "Accounting"}]`'This command produces no output. For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html)in the*AWS IAM User Guide*.- 
                    For API details, see [TagSamlProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/tag-saml-provider.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-server-certificate`.

- **AWS CLI**
- 
            
                    **To add a tag to a server certificate**The following `tag-saml-provider`command adds a tag with a Department name to the specified sever certificate.`aws iam tag-server-certificate \ --server-certificate-name``ExampleCertificate`\ --tags '`[{"Key": "Department", "Value": "Accounting"}]`'This command produces no output. For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html)in the*AWS IAM User Guide*.- 
                    For API details, see [TagServerCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/tag-server-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-user`.

- **AWS CLI**
- 
            
                    **To add a tag to a user**The following `tag-user`command adds a tag with the associated Department to the specified user.`aws iam tag-user \ --user-name``alice`\ --tags '`{"Key": "Department", "Value": "Accounting"}`'This command produces no output. For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html)in the*AWS IAM User Guide*.- 
                    For API details, see [TagUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/tag-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-instance-profile`.

- **AWS CLI**
- 
            
                    **To remove a tag from an instance profile**The following `untag-instance-profile`command removes any tag with the key name 'Department' from the specified instance profile.`aws iam untag-instance-profile \ --instance-profile-name``deployment-role`\ --tag-keys`Department`This command produces no output. For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html)in the*AWS IAM User Guide*.- 
                    For API details, see [UntagInstanceProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/untag-instance-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-mfa-device`.

- **AWS CLI**
- 
            
                    **To remove a tag from an MFA device**The following `untag-mfa-device`command removes any tag with the key name 'Department' from the specified MFA device.`aws iam untag-mfa-device \ --serial-number``arn:aws:iam::123456789012:mfa/alice`\ --tag-keys`Department`This command produces no output. For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html)in the*AWS IAM User Guide*.- 
                    For API details, see [UntagMfaDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/untag-mfa-device.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-open-id-connect-provider`.

- **AWS CLI**
- 
            
                    **To remove a tag from an OIDC identity provider**The following `untag-open-id-connect-provider`command removes any tag with the key name 'Department' from the specified OIDC identity provider.`aws iam untag-open-id-connect-provider \ --open-id-connect-provider-arn``arn:aws:iam::123456789012:oidc-provider/server.example.com`\ --tag-keys`Department`This command produces no output. For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html)in the*AWS IAM User Guide*.- 
                    For API details, see [UntagOpenIdConnectProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/untag-open-id-connect-provider.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-policy`.

- **AWS CLI**
- 
            
                    **To remove a tag from a customer managed policy**The following `untag-policy`command removes any tag with the key name 'Department' from the specified customer managed policy.`aws iam untag-policy \ --policy-arn``arn:aws:iam::452925170507:policy/billing-access`\ --tag-keys`Department`This command produces no output. For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html)in the*AWS IAM User Guide*.- 
                    For API details, see [UntagPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/untag-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-role`.

- **AWS CLI**
- 
            
                    **To remove a tag from a role**The following `untag-role`command removes any tag with the key name 'Department' from the specified role.`aws iam untag-role \ --role-name``my-role`\ --tag-keys`Department`This command produces no output. For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html)in the*AWS IAM User Guide*.- 
                    For API details, see [UntagRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/untag-role.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-saml-provider`.

- **AWS CLI**
- 
            
                    **To remove a tag from a SAML provider**The following `untag-saml-provider`command removes any tag with the key name 'Department' from the specified instance profile.`aws iam untag-saml-provider \ --saml-provider-arn``arn:aws:iam::123456789012:saml-provider/ADFS`\ --tag-keys`Department`This command produces no output. For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html)in the*AWS IAM User Guide*.- 
                    For API details, see [UntagSamlProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/untag-saml-provider.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-server-certificate`.

- **AWS CLI**
- 
            
                    **To remove a tag from a server certificate**The following `untag-server-certificate`command removes any tag with the key name 'Department' from the specified server certificate.`aws iam untag-server-certificate \ --server-certificate-name``ExampleCertificate`\ --tag-keys`Department`This command produces no output. For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html)in the*AWS IAM User Guide*.- 
                    For API details, see [UntagServerCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/untag-server-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-user`.

- **AWS CLI**
- 
            
                    **To remove a tag from a user**The following `untag-user`command removes any tag with the key name 'Department' from the specified user.`aws iam untag-user \ --user-name``alice`\ --tag-keys`Department`This command produces no output. For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html)in the*AWS IAM User Guide*.- 
                    For API details, see [UntagUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/untag-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-access-key`.

- **AWS CLI**
- 
            
                    **To activate or deactivate an access key for an IAM user**The following `update-access-key`command deactivates the specified access key (access key ID and secret access key) for the IAM user named`Bob`.`aws iam update-access-key \ --access-key-id``AKIAIOSFODNN7EXAMPLE`\ --status`Inactive`\ --user-name`Bob`This command produces no output. Deactivating the key means that it cannot be used for programmatic access to AWS. However, the key is still available and can be reactivated. For more information, see [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)in the*AWS IAM User Guide*.- 
                    For API details, see [UpdateAccessKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-access-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-account-password-policy`.

- **AWS CLI**
- 
            
                    **To set or change the current account password policy**The following `update-account-password-policy`command sets the password policy to require a minimum length of eight characters and to require one or more numbers in the password.`aws iam update-account-password-policy \ --minimum-password-length``8`\ --require-numbersThis command produces no output. Changes to an account's password policy affect any new passwords that are created for IAM users in the account. Password policy changes do not affect existing passwords. For more information, see [Setting an account password policy for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html)in the*AWS IAM User Guide*.- 
                    For API details, see [UpdateAccountPasswordPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-account-password-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-assume-role-policy`.

- **AWS CLI**
- 
            
                    **To update the trust policy for an IAM role**The following `update-assume-role-policy`command updates the trust policy for the role named`Test-Role`.`aws iam update-assume-role-policy \ --role-name``Test-Role`\ --policy-document`file://Test-Role-Trust-Policy.json`This command produces no output. The trust policy is defined as a JSON document in the *Test-Role-Trust-Policy.json*file. (The file name and extension do not have significance.) The trust policy must specify a principal.To update the permissions policy for a role, use the `put-role-policy`command.For more information, see [Creating IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html)in the*AWS IAM User Guide*.- 
                    For API details, see [UpdateAssumeRolePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-assume-role-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-group`.

- **AWS CLI**
- 
            
                    **To rename an IAM group**The following `update-group`command changes the name of the IAM group`Test`to`Test-1`.`aws iam update-group \ --group-name``Test`\ --new-group-name`Test-1`This command produces no output. For more information, see [Renaming an IAM user group](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_rename.html)in the*AWS IAM User Guide*.- 
                    For API details, see [UpdateGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-login-profile`.

- **AWS CLI**
- 
            
                    **To update the password for an IAM user**The following `update-login-profile`command creates a new password for the IAM user named`Bob`.`aws iam update-login-profile \ --user-name``Bob`\ --password`<password>`This command produces no output. To set a password policy for the account, use the `update-account-password-policy`command. If the new password violates the account password policy, the command returns a`PasswordPolicyViolation`error.If the account password policy allows them to, IAM users can change their own passwords using the `change-password`command.Store the password in a secure place. If the password is lost, it cannot be recovered, and you must create a new one using the `create-login-profile`command.For more information, see [Managing passwords for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_admin-change-user.html)in the*AWS IAM User Guide*.- 
                    For API details, see [UpdateLoginProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-login-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-open-id-connect-provider-thumbprint`.

- **AWS CLI**
- 
            
                    **To replace the existing list of server certificate thumbprints with a new list**This example updates the certificate thumbprint list for the OIDC provider whose ARN is `arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com`to use a new thumbprint.`aws iam update-open-id-connect-provider-thumbprint \ --open-id-connect-provider-arn``arn:aws:iam::123456789012:oidc-provider/example.oidcprovider.com`\ --thumbprint-list`7359755EXAMPLEabc3060bce3EXAMPLEec4542a3`If your OIDC provider's discovery and JWKS endpoints use different certificates, include thumbprints for both endpoints in the `--thumbprint-list`value.This command produces no output. For more information, see [Creating OpenID Connect (OIDC) identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html)in the*AWS IAM User Guide*.- 
                    For API details, see [UpdateOpenIdConnectProviderThumbprint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-open-id-connect-provider-thumbprint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-role-description`.

- **AWS CLI**
- 
            
                    **To change an IAM role's description**The following `update-role`command changes the description of the IAM role`production-role`to`Main production role`.`aws iam update-role-description \ --role-name``production-role`\ --description '`Main production role`'Output: `{ "Role": { "Path": "/", "RoleName": "production-role", "RoleId": "AROA1234567890EXAMPLE", "Arn": "arn:aws:iam::123456789012:role/production-role", "CreateDate": "2017-12-06T17:16:37+00:00", "AssumeRolePolicyDocument": { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "AWS": "arn:aws:iam::123456789012:root" }, "Action": "sts:AssumeRole", "Condition": {} } ] }, "Description": "Main production role" } }`For more information, see [Modifying a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_modify.html)in the*AWS IAM User Guide*.- 
                    For API details, see [UpdateRoleDescription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-role-description.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-role`.

- **AWS CLI**
- 
            
                    **To change an IAM role's description or session duration**The following `update-role`command changes the description of the IAM role`production-role`to`Main production role`and sets the maximum session duration to 12 hours.`aws iam update-role \ --role-name``production-role`\ --description '`Main production role`' \ --max-session-duration`43200`This command produces no output. For more information, see [Modifying a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_modify.html)in the*AWS IAM User Guide*.- 
                    For API details, see [UpdateRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-role.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-saml-provider`.

- **AWS CLI**
- 
            
                    **To update the metadata document for an existing SAML provider**This example updates the SAML provider in IAM whose ARN is `arn:aws:iam::123456789012:saml-provider/SAMLADFS`with a new SAML metadata document from the file`SAMLMetaData.xml`.`aws iam update-saml-provider \ --saml-metadata-document``file://SAMLMetaData.xml`\ --saml-provider-arn`arn:aws:iam::123456789012:saml-provider/SAMLADFS`Output: `{ "SAMLProviderArn": "arn:aws:iam::123456789012:saml-provider/SAMLADFS" }`For more information, see [Creating IAM SAML identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml.html)in the*AWS IAM User Guide*.- 
                    For API details, see [UpdateSamlProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-saml-provider.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-server-certificate`.

- **AWS CLI**
- 
            
                    **To change the path or name of a server certificate in your AWS account**The following `update-server-certificate`command changes the name of the certificate from`myServerCertificate`to`myUpdatedServerCertificate`. It also changes the path to`/cloudfront/`so that it can be accessed by the Amazon CloudFront service. This command produces no output. You can see the results of the update by running the`list-server-certificates`command.`aws-iam update-server-certificate \ --server-certificate-name``myServerCertificate`\ --new-server-certificate-name`myUpdatedServerCertificate`\ --new-path`/cloudfront/`This command produces no output. For more information, see [Managing server certificates in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html)in the*AWS IAM User Guide*.- 
                    For API details, see [UpdateServerCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-server-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-service-specific-credential`.

- **AWS CLI**
- 
            
                    **Example 1: To update the status of the requesting user's service-specific credential**The following `update-service-specific-credential`example changes the status for the specified credential for the user making the request to`Inactive`.`aws iam update-service-specific-credential \ --service-specific-credential-id``ACCAEXAMPLE123EXAMPLE`\ --status`Inactive`This command produces no output. **Example 2: To update the status of a specified user's service-specific credential**The following `update-service-specific-credential`example changes the status for the credential of the specified user to Inactive.`aws iam update-service-specific-credential \ --user-name``sofia`\ --service-specific-credential-id`ACCAEXAMPLE123EXAMPLE`\ --status`Inactive`This command produces no output. For more information, see [Create Git Credentials for HTTPS Connections to CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-gc.html#setting-up-gc-iam)in the*AWS CodeCommit User Guide*- 
                    For API details, see [UpdateServiceSpecificCredential](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-service-specific-credential.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-signing-certificate`.

- **AWS CLI**
- 
            
                    **To activate or deactivate a signing certificate for an IAM user**The following `update-signing-certificate`command deactivates the specified signing certificate for the IAM user named`Bob`.`aws iam update-signing-certificate \ --certificate-id``TA7SMP42TDN5Z26OBPJE7EXAMPLE`\ --status`Inactive`\ --user-name`Bob`To get the ID for a signing certificate, use the `list-signing-certificates`command.For more information, see [Manage signing certificates](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-up-ami-tools.html#ami-tools-managing-certs)in the*Amazon EC2 User Guide*.- 
                    For API details, see [UpdateSigningCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-signing-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-ssh-public-key`.

- **AWS CLI**
- 
            
                    **To change the status of an SSH public key**The following `update-ssh-public-key`command changes the status of the specified public key to`Inactive`.`aws iam update-ssh-public-key \ --user-name``sofia`\ --ssh-public-key-id`APKA1234567890EXAMPLE`\ --status`Inactive`This command produces no output. For more information, see [Use SSH keys and SSH with CodeCommit](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_ssh-keys.html#ssh-keys-code-commit)in the*AWS IAM User Guide*.- 
                    For API details, see [UpdateSshPublicKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-ssh-public-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-user`.

- **AWS CLI**
- 
            
                    **To change an IAM user's name**The following `update-user`command changes the name of the IAM user`Bob`to`Robert`.`aws iam update-user \ --user-name``Bob`\ --new-user-name`Robert`This command produces no output. For more information, see [Renaming an IAM user group](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_rename.html)in the*AWS IAM User Guide*.- 
                    For API details, see [UpdateUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `upload-server-certificate`.

- **AWS CLI**
- 
            
                    **To upload a server certificate to your AWS account**The following **upload-server-certificate**command uploads a server certificate to your AWS account. In this example, the certificate is in the file`public_key_cert_file.pem`, the associated private key is in the file`my_private_key.pem`, and the the certificate chain provided by the certificate authority (CA) is in the`my_certificate_chain_file.pem`file. When the file has finished uploading, it is available under the name*myServerCertificate*. Parameters that begin with`file://`tells the command to read the contents of the file and use that as the parameter value instead of the file name itself.`aws iam upload-server-certificate \ --server-certificate-name``myServerCertificate`\ --certificate-body`file://public_key_cert_file.pem`\ --private-key`file://my_private_key.pem`\ --certificate-chain`file://my_certificate_chain_file.pem`Output: `{ "ServerCertificateMetadata": { "Path": "/", "ServerCertificateName": "myServerCertificate", "ServerCertificateId": "ASCAEXAMPLE123EXAMPLE", "Arn": "arn:aws:iam::1234567989012:server-certificate/myServerCertificate", "UploadDate": "2019-04-22T21:13:44+00:00", "Expiration": "2019-10-15T22:23:16+00:00" } }`For more information, see Creating, Uploading, and Deleting Server Certificates in the *Using IAM*guide.- 
                    For API details, see [UploadServerCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/upload-server-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `upload-signing-certificate`.

- **AWS CLI**
- 
            
                    **To upload a signing certificate for an IAM user**The following `upload-signing-certificate`command uploads a signing certificate for the IAM user named`Bob`.`aws iam upload-signing-certificate \ --user-name``Bob`\ --certificate-body`file://certificate.pem`Output: `{ "Certificate": { "UserName": "Bob", "Status": "Active", "CertificateBody": "-----BEGIN CERTIFICATE-----<certificate-body>-----END CERTIFICATE-----", "CertificateId": "TA7SMP42TDN5Z26OBPJE7EXAMPLE", "UploadDate": "2013-06-06T21:40:08.121Z" } }`The certificate is in a file named *certificate.pem*in PEM format.For more information, see Creating and Uploading a User Signing Certificate in the *Using IAM*guide.- 
                    For API details, see [UploadSigningCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/upload-signing-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `upload-ssh-public-key`.

- **AWS CLI**
- 
            
                    **To upload an SSH public key and associate it with a user**The following `upload-ssh-public-key`command uploads the public key found in the file`sshkey.pub`and attaches it to the user`sofia`.`aws iam upload-ssh-public-key \ --user-name``sofia`\ --ssh-public-key-body`file://sshkey.pub`Output: `{ "SSHPublicKey": { "UserName": "sofia", "SSHPublicKeyId": "APKA1234567890EXAMPLE", "Fingerprint": "12:34:56:78:90:ab:cd:ef:12:34:56:78:90:ab:cd:ef", "SSHPublicKeyBody": "ssh-rsa <<long string generated by ssh-keygen command>>", "Status": "Active", "UploadDate": "2019-04-18T17:04:49+00:00" } }`For more information about how to generate keys in a format suitable for this command, see [SSH and Linux, macOS, or Unix: Set up the public and private keys for Git and CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-ssh-unixes.html#setting-up-ssh-unixes-keys)or[SSH and Windows: Set up the public and private keys for Git and CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-ssh-windows.html#setting-up-ssh-windows-keys-windows)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [UploadSshPublicKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/upload-ssh-public-key.html)in*AWS CLI Command Reference*.
 
-