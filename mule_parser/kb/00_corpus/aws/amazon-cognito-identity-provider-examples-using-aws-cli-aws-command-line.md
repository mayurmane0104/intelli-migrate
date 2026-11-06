# Amazon Cognito Identity Provider examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_cognito-identity-provider_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_cognito-identity-provider_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon Cognito Identity Provider.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `add-custom-attributes`.

- **AWS CLI**
- 
            
                    **To add a custom attribute**This example adds a custom attribute CustomAttr1 to a user pool. It is a String type, and requires a minimum of 1 character and a maximum of 15. It is not required. Command: `aws cognito-idp add-custom-attributes --user-pool-id``us-west-2_aaaaaaaaa`--custom-attributes Name="CustomAttr1",AttributeDataType="String",DeveloperOnlyAttribute=false,Required=false,StringAttributeConstraints="{MinLength=1,MaxLength=15}"- 
                    For API details, see [AddCustomAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/add-custom-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `admin-add-user-to-group`.

- **AWS CLI**
- 
            
                    **To add a user to a group**This example adds user Jane to group MyGroup. Command: `aws cognito-idp admin-add-user-to-group --user-pool-id``us-west-2_aaaaaaaaa`--username`Jane`--group-name`MyGroup`- 
                    For API details, see [AdminAddUserToGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-add-user-to-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `admin-confirm-sign-up`.

- **AWS CLI**
- 
            
                    **To confirm user registration**This example confirms user jane@example.com. Command: `aws cognito-idp admin-confirm-sign-up --user-pool-id``us-west-2_aaaaaaaaa`--username`jane@example.com`- 
                    For API details, see [AdminConfirmSignUp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-confirm-sign-up.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `admin-create-user`.

- **AWS CLI**
- 
            
                    **To create a user**The following `admin-create-user`example creates a user with the specified settings email address and phone number.`aws cognito-idp admin-create-user \ --user-pool-id``us-west-2_aaaaaaaaa`\ --username`diego`\ --user-attributes`Name=email,Value=diego@example.com`Name=phone_number,Value="+15555551212" \ --message-action`SUPPRESS`Output: `{ "User": { "Username": "diego", "Attributes": [ { "Name": "sub", "Value": "7325c1de-b05b-4f84-b321-9adc6e61f4a2" }, { "Name": "phone_number", "Value": "+15555551212" }, { "Name": "email", "Value": "diego@example.com" } ], "UserCreateDate": 1548099495.428, "UserLastModifiedDate": 1548099495.428, "Enabled": true, "UserStatus": "FORCE_CHANGE_PASSWORD" } }`- 
                    For API details, see [AdminCreateUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-create-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `admin-delete-user-attributes`.

- **AWS CLI**
- 
            
                    **To delete a user attribute**This example deletes a custom attribute CustomAttr1 for user diego@example.com. Command: `aws cognito-idp admin-delete-user-attributes --user-pool-id``us-west-2_aaaaaaaaa`--username`diego@example.com`--user-attribute-names`"custom:CustomAttr1"`- 
                    For API details, see [AdminDeleteUserAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-delete-user-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `admin-delete-user`.

- **AWS CLI**
- 
            
                    **To delete a user**This example deletes a user. Command: `aws cognito-idp admin-delete-user --user-pool-id``us-west-2_aaaaaaaaa`--username`diego@example.com`- 
                    For API details, see [AdminDeleteUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-delete-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `admin-disable-provider-for-user`.

- **AWS CLI**
- 
            
                    **To unlink a federated user from a local user profile**The following `admin-disable-provider-for-user`example disconnects a Google user from their linked local profile.`aws cognito-idp admin-disable-provider-for-user \ --user-pool-id``us-west-2_EXAMPLE`\ --user`ProviderAttributeName=Cognito_Subject,ProviderAttributeValue=0000000000000000,ProviderName=Google`For more information, see [Linking federated users to an existing user profile](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation-consolidate-users.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [AdminDisableProviderForUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-disable-provider-for-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `admin-disable-user`.

- **AWS CLI**
- 
            
                    **To prevent sign-in by a user**The following `admin-disable-user`example prevents sign-in by the user`diego@example.com`.`aws cognito-idp admin-disable-user \ --user-pool-id``us-west-2_EXAMPLE`\ --username`diego@example.com`For more information, see [Managing users](https://docs.aws.amazon.com/cognito/latest/developerguide/managing-users.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [AdminDisableUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-disable-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `admin-enable-user`.

- **AWS CLI**
- 
            
                    **To enable sign-in by a user**The following `admin-enable-user`example enables sign-in by the user diego@example.com.`aws cognito-idp admin-enable-user \ --user-pool-id``us-west-2_EXAMPLE`\ --username`diego@example.com`For more information, see [Managing users](https://docs.aws.amazon.com/cognito/latest/developerguide/managing-users.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [AdminEnableUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-enable-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `admin-forget-device`.

- **AWS CLI**
- 
            
                    **To forget a device**This example forgets device for username jane@example.com Command: `aws cognito-idp admin-forget-device --user-pool-id``us-west-2_aaaaaaaaa`--username`jane@example.com`--device-key`us-west-2_abcd_1234-5678`- 
                    For API details, see [AdminForgetDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-forget-device.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `admin-get-device`.

- **AWS CLI**
- 
            
                    **To get a device**The following `admin-get-device`example displays one device for the user`diego`.`aws cognito-idp admin-get-device \ --user-pool-id``us-west-2_EXAMPLE`\ --username`diego`\ --device-key`us-west-2_a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "Device": { "DeviceKey": "us-west-2_a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "DeviceAttributes": [ { "Name": "device_status", "Value": "valid" }, { "Name": "device_name", "Value": "MyDevice" }, { "Name": "dev:device_arn", "Value": "arn:aws:cognito-idp:us-west-2:123456789012:owner/diego.us-west-2_EXAMPLE/device/us-west-2_a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }, { "Name": "dev:device_owner", "Value": "diego.us-west-2_EXAMPLE" }, { "Name": "last_ip_used", "Value": "192.0.2.1" }, { "Name": "dev:device_remembered_status", "Value": "remembered" }, { "Name": "dev:device_sdk", "Value": "aws-sdk" } ], "DeviceCreateDate": 1715100742.022, "DeviceLastModifiedDate": 1723233651.167, "DeviceLastAuthenticatedDate": 1715100742.0 } }`For more information, see [Working with user devices in your user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [AdminGetDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-get-device.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `admin-get-user`.

- **AWS CLI**
- 
            
                    **To get a user**This example gets information about username jane@example.com. Command: `aws cognito-idp admin-get-user --user-pool-id``us-west-2_aaaaaaaaa`--username`jane@example.com`Output: `{ "Username": "4320de44-2322-4620-999b-5e2e1c8df013", "Enabled": true, "UserStatus": "FORCE_CHANGE_PASSWORD", "UserCreateDate": 1548108509.537, "UserAttributes": [ { "Name": "sub", "Value": "4320de44-2322-4620-999b-5e2e1c8df013" }, { "Name": "email_verified", "Value": "true" }, { "Name": "phone_number_verified", "Value": "true" }, { "Name": "phone_number", "Value": "+01115551212" }, { "Name": "email", "Value": "jane@example.com" } ], "UserLastModifiedDate": 1548108509.537 }`- 
                    For API details, see [AdminGetUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-get-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `admin-initiate-auth`.

- **AWS CLI**
- 
            
                    **To sign in a user as an admin**The following `admin-initiate-auth`example signs in the user diego@example.com. This example also includes metadata for threat protection and ClientMetadata for Lambda triggers. The user is configured for TOTP MFA and receives a challenge to provide a code from their authenticator app before they can complete authentication.`aws cognito-idp admin-initiate-auth \ --user-pool-id``us-west-2_EXAMPLE`\ --client-id`1example23456789`\ --auth-flow`ADMIN_USER_PASSWORD_AUTH`\ --auth-parameters USERNAME=diego@example.com,PASSWORD="My@Example$Password3!",SECRET_HASH=ExampleEncodedClientIdSecretAndUsername= \ --context-data="{\"EncodedData\":\"abc123example\",\"HttpHeaders\":[{\"headerName\":\"UserAgent\",\"headerValue\":\"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0\"}],\"IpAddress\":\"192.0.2.1\",\"ServerName\":\"example.com\",\"ServerPath\":\"/login\"}" \ --client-metadata="{\"MyExampleKey\": \"MyExampleValue\"}"Output: `{ "ChallengeName": "SOFTWARE_TOKEN_MFA", "Session": "AYABeExample...", "ChallengeParameters": { "FRIENDLY_DEVICE_NAME": "MyAuthenticatorApp", "USER_ID_FOR_SRP": "diego@example.com" } }`For more information, see [Admin authentication flow](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-authentication-flow.html#amazon-cognito-user-pools-admin-authentication-flow)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [AdminInitiateAuth](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-initiate-auth.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `admin-link-provider-for-user`.

- **AWS CLI**
- 
            
                    **To link a local user to a federated user**The following `admin-link-provider-for-user`example links the local user diego to a user who will do federated sign-in with Google.`aws cognito-idp admin-link-provider-for-user \ --user-pool-id``us-west-2_EXAMPLE`\ --destination-user`ProviderName=Cognito,ProviderAttributeValue=diego`\ --source-user`ProviderAttributeName=Cognito_Subject,ProviderAttributeValue=0000000000000000,ProviderName=Google`For more information, see [Linking federated users to an existing user profile](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation-consolidate-users.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [AdminLinkProviderForUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-link-provider-for-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `admin-list-devices`.

- **AWS CLI**
- 
            
                    **To list devices for a user**The following `admin-list-devices`example lists devices for the user diego.`aws cognito-idp admin-list-devices \ --user-pool-id``us-west-2_EXAMPLE`\ --username`diego`\ --limit`1`Output: `{ "Devices": [ { "DeviceKey": "us-west-2_a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "DeviceAttributes": [ { "Name": "device_status", "Value": "valid" }, { "Name": "device_name", "Value": "MyDevice" }, { "Name": "dev:device_arn", "Value": "arn:aws:cognito-idp:us-west-2:123456789012:owner/diego.us-west-2_EXAMPLE/device/us-west-2_a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }, { "Name": "dev:device_owner", "Value": "diego.us-west-2_EXAMPLE" }, { "Name": "last_ip_used", "Value": "192.0.2.1" }, { "Name": "dev:device_remembered_status", "Value": "remembered" }, { "Name": "dev:device_sdk", "Value": "aws-sdk" } ], "DeviceCreateDate": 1715100742.022, "DeviceLastModifiedDate": 1723233651.167, "DeviceLastAuthenticatedDate": 1715100742.0 } ] }`For more information, see [Working with user devices in your user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [AdminListDevices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-list-devices.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `admin-list-groups-for-user`.

- **AWS CLI**
- 
            
                    **To list groups for a user**This example lists groups for username jane@example.com. Command: `aws cognito-idp admin-list-groups-for-user --user-pool-id``us-west-2_aaaaaaaaa`--username`diego@example.com`Output: `{ "Groups": [ { "Description": "Sample group", "Precedence": 1, "LastModifiedDate": 1548097827.125, "RoleArn": "arn:aws:iam::111111111111:role/SampleRole", "GroupName": "SampleGroup", "UserPoolId": "us-west-2_aaaaaaaaa", "CreationDate": 1548097827.125 } ] }`- 
                    For API details, see [AdminListGroupsForUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-list-groups-for-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `admin-list-user-auth-events`.

- **AWS CLI**
- 
            
                    **To list authorization events for a user**The following `admin-list-user-auth-events`example lists the most recent user activity log event for the user diego.`aws cognito-idp admin-list-user-auth-events \ --user-pool-id``us-west-2_ywDJHlIfU`\ --username`brcotter+050123`\ --max-results`1`Output: `{ "AuthEvents": [ { "EventId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "EventType": "SignIn", "CreationDate": 1726694203.495, "EventResponse": "InProgress", "EventRisk": { "RiskDecision": "AccountTakeover", "RiskLevel": "Medium", "CompromisedCredentialsDetected": false }, "ChallengeResponses": [ { "ChallengeName": "Password", "ChallengeResponse": "Success" } ], "EventContextData": { "IpAddress": "192.0.2.1", "City": "Seattle", "Country": "United States" } } ], "NextToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222#2024-09-18T21:16:43.495Z" }`For more information, see [Viewing and exporting user event history](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-adaptive-authentication.html#user-pool-settings-adaptive-authentication-event-user-history)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [AdminListUserAuthEvents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-list-user-auth-events.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `admin-remove-user-from-group`.

- **AWS CLI**
- 
            
                    **To remove a user from a group**This example removes jane@example.com from SampleGroup. Command: `aws cognito-idp admin-remove-user-from-group --user-pool-id``us-west-2_aaaaaaaaa`--username`jane@example.com`--group-name`SampleGroup`- 
                    For API details, see [AdminRemoveUserFromGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-remove-user-from-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `admin-reset-user-password`.

- **AWS CLI**
- 
            
                    **To reset a user password**This example resets the password for diego@example.com. Command: `aws cognito-idp admin-reset-user-password --user-pool-id``us-west-2_aaaaaaaaa`--username`diego@example.com`- 
                    For API details, see [AdminResetUserPassword](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-reset-user-password.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `admin-respond-to-auth-challenge`.

- **AWS CLI**
- 
            
                    **To respond to an authentication challenge**There are many ways to respond to different authentication challenges, depending on your authentication flow, user pool configuration, and user settings. The following `admin-respond-to-auth-challenge`example provides a TOTP MFA code for diego@example.com and completes sign-in. This user pool has device remembering turned on, so the authentication result also returns a new device key.`aws cognito-idp admin-respond-to-auth-challenge \ --user-pool-id``us-west-2_EXAMPLE`\ --client-id`1example23456789`\ --challenge-name`SOFTWARE_TOKEN_MFA`\ --challenge-responses`USERNAME=diego@example.com,SOFTWARE_TOKEN_MFA_CODE=000000`\ --session`AYABeExample...`Output: `{ "ChallengeParameters": {}, "AuthenticationResult": { "AccessToken": "eyJra456defEXAMPLE", "ExpiresIn": 3600, "TokenType": "Bearer", "RefreshToken": "eyJra123abcEXAMPLE", "IdToken": "eyJra789ghiEXAMPLE", "NewDeviceMetadata": { "DeviceKey": "us-west-2_a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "DeviceGroupKey": "-ExAmPlE1" } } }`For more information, see [Admin authentication flow](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-authentication-flow.html#amazon-cognito-user-pools-admin-authentication-flow)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [AdminRespondToAuthChallenge](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-respond-to-auth-challenge.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `admin-set-user-mfa-preference`.

- **AWS CLI**
- 
            
                    **To set the user MFA preference**This example sets the SMS MFA preference for username diego@example.com. Command: `aws cognito-idp admin-set-user-mfa-preference --user-pool-id``us-west-2_aaaaaaaaa`--username`diego@example.com`--sms-mfa-settings`Enabled=false,PreferredMfa=false`- 
                    For API details, see [AdminSetUserMfaPreference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-set-user-mfa-preference.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `admin-set-user-password`.

- **AWS CLI**
- 
            
                    **To set a user password as an admin**The following `admin-set-user-password`example permanently sets the password for diego@example.com.`aws cognito-idp admin-set-user-password \ --user-pool-id``us-west-2_EXAMPLE`\ --username`diego@example.com`\ --password`MyExamplePassword1!`\ --permanentThis command produces no output. For more information, see [Passwords, password recovery, and password policies](https://docs.aws.amazon.com/cognito/latest/developerguide/managing-users-passwords.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [AdminSetUserPassword](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-set-user-password.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `admin-set-user-settings`.

- **AWS CLI**
- 
            
                    **To set user settings**This example sets the MFA delivery preference for username diego@example.com to EMAIL. Command: `aws cognito-idp admin-set-user-settings --user-pool-id``us-west-2_aaaaaaaaa`--username`diego@example.com`--mfa-options`DeliveryMedium=EMAIL`- 
                    For API details, see [AdminSetUserSettings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-set-user-settings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `admin-update-auth-event-feedback`.

- **AWS CLI**
- 
            
                    **To provide feedback for an authorization event**This example sets the feedback value for an authorization event identified by event-id to Valid. Command: `aws cognito-idp admin-update-auth-event-feedback --user-pool-id``us-west-2_aaaaaaaaa`--username`diego@example.com`--event-id`c2c2cf89-c0d3-482d-aba6-99d78a5b0bfe`--feedback-value`Valid`- 
                    For API details, see [AdminUpdateAuthEventFeedback](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-update-auth-event-feedback.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `admin-update-device-status`.

- **AWS CLI**
- 
            
                    **To update device status**This example sets the device remembered status for the device identified by device-key to not_remembered. Command: `aws cognito-idp admin-update-device-status --user-pool-id``us-west-2_aaaaaaaaa`--username`diego@example.com`--device-key`xxxx`--device-remembered-status`not_remembered`- 
                    For API details, see [AdminUpdateDeviceStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-update-device-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `admin-update-user-attributes`.

- **AWS CLI**
- 
            
                    **To update user attributes**This example updates a custom user attribute CustomAttr1 for user diego@example.com. Command: `aws cognito-idp admin-update-user-attributes --user-pool-id``us-west-2_aaaaaaaaa`--username`diego@example.com`--user-attributes Name="custom:CustomAttr1",Value="Purple"- 
                    For API details, see [AdminUpdateUserAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-update-user-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `admin-user-global-sign-out`.

- **AWS CLI**
- 
            
                    **To sign out a user as an admin**The following `admin-user-global-sign-out`example signs out the user diego@example.com.`aws cognito-idp admin-user-global-sign-out \ --user-pool-id``us-west-2_EXAMPLE`\ --username`diego@example.com`For more information, see [Authentication with a user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [AdminUserGlobalSignOut](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/admin-user-global-sign-out.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-software-token`.

- **AWS CLI**
- 
            
                    **To generate a secret key for an MFA authenticator app**The following `associate-software-token`example generates a TOTP private key for a user who has signed in and received an access token. The resulting private key can be manually entered into an authenticator app, or applications can render it as a QR code that the user can scan.`aws cognito-idp associate-software-token \ --access-token``eyJra456defEXAMPLE`Output: `{ "SecretCode": "QWERTYUIOP123456EXAMPLE" }`For more information, see [TOTP software token MFA](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa-totp.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [AssociateSoftwareToken](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/associate-software-token.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `change-password`.

- **AWS CLI**
- 
            
                    **To change a password**This example changes a password. Command: `aws cognito-idp change-password --previous-password``OldPassword`--proposed-password`NewPassword`--access-token`ACCESS_TOKEN`- 
                    For API details, see [ChangePassword](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/change-password.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `confirm-device`.

- **AWS CLI**
- 
            
                    **To confirm a user device**The following `confirm-device`example adds a new remembered device for the current user.`aws cognito-idp confirm-device \ --access-token``eyJra456defEXAMPLE`\ --device-key`us-west-2_a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --device-secret-verifier-config`PasswordVerifier=TXlWZXJpZmllclN0cmluZw,Salt=TXlTUlBTYWx0`Output: `{ "UserConfirmationNecessary": false }`For more information, see [Working with user devices in your user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [ConfirmDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/confirm-device.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `confirm-forgot-password`.

- **AWS CLI**
- 
            
                    **To confirm a forgotten password**This example confirms a forgotten password for username diego@example.com. Command: `aws cognito-idp confirm-forgot-password --client-id``3n4b5urk1ft4fl3mg5e62d9ado`--username=diego@example.com --password`PASSWORD`--confirmation-code`CONF_CODE`- 
                    For API details, see [ConfirmForgotPassword](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/confirm-forgot-password.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `confirm-sign-up`.

- **AWS CLI**
- 
            
                    **To confirm sign-up**This example confirms sign-up for username diego@example.com. Command: `aws cognito-idp confirm-sign-up --client-id``3n4b5urk1ft4fl3mg5e62d9ado`--username=diego@example.com --confirmation-code`CONF_CODE`- 
                    For API details, see [ConfirmSignUp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/confirm-sign-up.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-group`.

- **AWS CLI**
- 
            
                    **To create a group**This example creates a group with a description. Command: `aws cognito-idp create-group --user-pool-id``us-west-2_aaaaaaaaa`--group-name`MyNewGroup`--description`"New group."`Output: `{ "Group": { "GroupName": "MyNewGroup", "UserPoolId": "us-west-2_aaaaaaaaa", "Description": "New group.", "LastModifiedDate": 1548270073.795, "CreationDate": 1548270073.795 } }`**To create a group with a role and precedence**This example creates a group with a description. It also includes a role and precedence. Command: `aws cognito-idp create-group --user-pool-id``us-west-2_aaaaaaaaa`--group-name`MyNewGroupWithRole`--description`"New group with a role."`--role-arn`arn:aws:iam::111111111111:role/MyNewGroupRole`--precedence`2`Output: `{ "Group": { "GroupName": "MyNewGroupWithRole", "UserPoolId": "us-west-2_aaaaaaaaa", "Description": "New group with a role.", "RoleArn": "arn:aws:iam::111111111111:role/MyNewGroupRole", "Precedence": 2, "LastModifiedDate": 1548270211.761, "CreationDate": 1548270211.761 } }`- 
                    For API details, see [CreateGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-identity-provider`.

- **AWS CLI**
- 
            
                    **Example 1: To create a user pool SAML identity provider (IdP) with a metadata URL**The following `create-identity-provider`example creates a new SAML IdP with metadata from a public URL, attribute mapping, and two identifiers.`aws cognito-idp create-identity-provider \ --user-pool-id``us-west-2_EXAMPLE`\ --provider-name`MySAML`\ --provider-type`SAML`\ --provider-details`IDPInit=true,IDPSignout=true,EncryptedResponses=true,MetadataURL=https://auth.example.com/sso/saml/metadata,RequestSigningAlgorithm=rsa-sha256`\ --attribute-mapping`email=emailaddress,phone_number=phone,custom:111=department`\ --idp-identifiers`CorpSAML``WestSAML`Output: `{ "IdentityProvider": { "UserPoolId": "us-west-2_EXAMPLE", "ProviderName": "MySAML", "ProviderType": "SAML", "ProviderDetails": { "ActiveEncryptionCertificate": "MIICvTCCAaEXAMPLE", "EncryptedResponses": "true", "IDPInit": "true", "IDPSignout": "true", "MetadataURL": "https://auth.example.com/sso/saml/metadata", "RequestSigningAlgorithm": "rsa-sha256", "SLORedirectBindingURI": "https://auth.example.com/slo/saml", "SSORedirectBindingURI": "https://auth.example.com/sso/saml" }, "AttributeMapping": { "custom:111": "department", "emailaddress": "email", "phone": "phone_number" }, "IdpIdentifiers": [ "CorpSAML", "WestSAML" ], "LastModifiedDate": 1726853833.977, "CreationDate": 1726853833.977 } }`For more information, see [Adding user pool sign-in through a third party](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation.html)in the*Amazon Cognito Developer Guide*.**Example 2: To create a user pool SAML identity provider (IdP) with a metadata file**The following `create-identity-provider`example creates a new SAML IdP with metadata from a file, attribute mapping, and two identifiers. File syntax can differ between operating systems in the`--provider-details`parameter. It's easiest to create a JSON input file for this operation.:`aws cognito-idp create-identity-provider \ --cli-input-json file://.\SAML-identity-provider.json`Contents of `SAML-identity-provider.json`:`{ "AttributeMapping": { "email" : "idp_email", "email_verified" : "idp_email_verified" }, "IdpIdentifiers": [ "platform" ], "ProviderDetails": { "MetadataFile": "<md:EntityDescriptor xmlns:md=\"urn:oasis:names:tc:SAML:2.0:metadata\" entityID=\"http://www.example.com/sso\"><md:IDPSSODescriptor WantAuthnRequestsSigned=\"false\" protocolSupportEnumeration=\"urn:oasis:names:tc:SAML:2.0:protocol\"><md:KeyDescriptor use=\"signing\"><ds:KeyInfo xmlns:ds=\"http://www.w3.org/2000/09/xmldsig#\"><ds:X509Data><ds:X509Certificate>[IDP_CERTIFICATE_DATA]</ds:X509Certificate></ds:X509Data></ds:KeyInfo></md:KeyDescriptor><md:SingleLogoutService Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST\" Location=\"https://www.example.com/slo/saml\"/><md:SingleLogoutService Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect\" Location=\"https://www.example.com/slo/saml\"/><md:NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified</md:NameIDFormat><md:NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</md:NameIDFormat><md:SingleSignOnService Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST\" Location=\"https://www.example.com/sso/saml\"/><md:SingleSignOnService Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect\" Location=\"https://www.example.com/sso/saml\"/></md:IDPSSODescriptor></md:EntityDescriptor>", "IDPSignout" : "true", "RequestSigningAlgorithm" : "rsa-sha256", "EncryptedResponses" : "true", "IDPInit" : "true" }, "ProviderName": "MySAML2", "ProviderType": "SAML", "UserPoolId": "us-west-2_EXAMPLE" }`Output: `{ "IdentityProvider": { "UserPoolId": "us-west-2_EXAMPLE", "ProviderName": "MySAML2", "ProviderType": "SAML", "ProviderDetails": { "ActiveEncryptionCertificate": "[USER_POOL_ENCRYPTION_CERTIFICATE_DATA]", "EncryptedResponses": "true", "IDPInit": "true", "IDPSignout": "true", "MetadataFile": "<md:EntityDescriptor xmlns:md=\"urn:oasis:names:tc:SAML:2.0:metadata\" entityID=\"http://www.example.com/sso\"><md:IDPSSODescriptor WantAuthnRequestsSigned=\"false\" protocolSupportEnumeration=\"urn:oasis:names:tc:SAML:2.0:protocol\"><md:KeyDescriptor use=\"signing\"><ds:KeyInfo xmlns:ds=\"http://www.w3.org/2000/09/xmldsig#\"><ds:X509Data><ds:X509Certificate>[IDP_CERTIFICATE_DATA]</ds:X509Certificate></ds:X509Data></ds:KeyInfo></md:KeyDescriptor><md:SingleLogoutService Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST\" Location=\"https://www.example.com/slo/saml\"/><md:SingleLogoutService Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect\" Location=\"https://www.example.com/slo/saml\"/><md:NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified</md:NameIDFormat><md:NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</md:NameIDFormat><md:SingleSignOnService Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST\" Location=\"https://www.example.com/sso/saml\"/><md:SingleSignOnService Binding=\"urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect\" Location=\"https://www.example.com/sso/saml\"/></md:IDPSSODescriptor></md:EntityDescriptor>", "RequestSigningAlgorithm": "rsa-sha256", "SLORedirectBindingURI": "https://www.example.com/slo/saml", "SSORedirectBindingURI": "https://www.example.com/sso/saml" }, "AttributeMapping": { "email": "idp_email", "email_verified": "idp_email_verified" }, "IdpIdentifiers": [ "platform" ], "LastModifiedDate": 1726855290.731, "CreationDate": 1726855290.731 } }`For more information, see [Adding user pool sign-in through a third party](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [CreateIdentityProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-identity-provider.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-resource-server`.

- **AWS CLI**
- 
            
                    **To create a user pool client**The following `create-resource-server`example creates a new resource server with custom scopes.`aws cognito-idp create-resource-server \ --user-pool-id``us-west-2_EXAMPLE`\ --identifier`solar-system-data`\ --name`"Solar system object tracker"`\ --scopes ScopeName=sunproximity.read,ScopeDescription="Distance in AU from Sol" ScopeName=asteroids.add,ScopeDescription="Enter a new asteroid"Output: `{ "ResourceServer": { "UserPoolId": "us-west-2_EXAMPLE", "Identifier": "solar-system-data", "Name": "Solar system object tracker", "Scopes": [ { "ScopeName": "sunproximity.read", "ScopeDescription": "Distance in AU from Sol" }, { "ScopeName": "asteroids.add", "ScopeDescription": "Enter a new asteroid" } ] } }`For more information, see [Scopes, M2M, and APIs with resource servers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-define-resource-servers.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [CreateResourceServer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-resource-server.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-user-import-job`.

- **AWS CLI**
- 
            
                    **To create a user import job**This example creates a user import job named MyImportJob. For more information about importing users, see Importing Users into User Pools From a CSV File. Command: `aws cognito-idp create-user-import-job --user-pool-id``us-west-2_aaaaaaaaa`--job-name`MyImportJob`--cloud-watch-logs-role-arn`arn:aws:iam::111111111111:role/CognitoCloudWatchLogsRole`Output: `{ "UserImportJob": { "JobName": "MyImportJob", "JobId": "import-qQ0DCt2fRh", "UserPoolId": "us-west-2_aaaaaaaaa", "PreSignedUrl": "PRE_SIGNED_URL", "CreationDate": 1548271795.471, "Status": "Created", "CloudWatchLogsRoleArn": "arn:aws:iam::111111111111:role/CognitoCloudWatchLogsRole", "ImportedUsers": 0, "SkippedUsers": 0, "FailedUsers": 0 } }`Upload the .csv file with curl using the pre-signed URL: Command: `curl -v -T "PATH_TO_CSV_FILE" -H "x-amz-server-side-encryption:aws:kms" "PRE_SIGNED_URL"`- 
                    For API details, see [CreateUserImportJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-user-import-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-user-pool-client`.

- **AWS CLI**
- 
            
                    **To create a user pool client**The following `create-user-pool-client`example creates a new user pool client with a client secret, explicit read and write attributes, sign in with username-password and SRP flows, sign-in with three IdPs, access to a subset of OAuth scopes, PinPoint analytics, and an extended authentication session validity.`aws cognito-idp create-user-pool-client \ --user-pool-id``us-west-2_EXAMPLE`\ --client-name`MyTestClient`\ --generate-secret \ --refresh-token-validity`10`\ --access-token-validity`60`\ --id-token-validity`60`\ --token-validity-units`AccessToken=minutes,IdToken=minutes,RefreshToken=days`\ --read-attributes`email``phone_number``email_verified``phone_number_verified`\ --write-attributes`email``phone_number`\ --explicit-auth-flows`ALLOW_USER_PASSWORD_AUTH``ALLOW_USER_SRP_AUTH``ALLOW_REFRESH_TOKEN_AUTH`\ --supported-identity-providers`Google``Facebook``MyOIDC`\ --callback-urls`https://www.amazon.com``https://example.com``http://localhost:8001``myapp://example`\ --allowed-o-auth-flows`code``implicit`\ --allowed-o-auth-scopes`openid``profile``aws.cognito.signin.user.admin``solar-system-data/asteroids.add`\ --allowed-o-auth-flows-user-pool-client \ --analytics-configuration`ApplicationArn=arn:aws:mobiletargeting:us-west-2:767671399759:apps/thisisanexamplepinpointapplicationid,UserDataShared=TRUE`\ --prevent-user-existence-errors`ENABLED`\ --enable-token-revocation \ --enable-propagate-additional-user-context-data \ --auth-session-validity`4`Output: `{ "UserPoolClient": { "UserPoolId": "us-west-2_EXAMPLE", "ClientName": "MyTestClient", "ClientId": "123abc456defEXAMPLE", "ClientSecret": "this1234is5678my91011example1213client1415secret", "LastModifiedDate": 1726788459.464, "CreationDate": 1726788459.464, "RefreshTokenValidity": 10, "AccessTokenValidity": 60, "IdTokenValidity": 60, "TokenValidityUnits": { "AccessToken": "minutes", "IdToken": "minutes", "RefreshToken": "days" }, "ReadAttributes": [ "email_verified", "phone_number_verified", "phone_number", "email" ], "WriteAttributes": [ "phone_number", "email" ], "ExplicitAuthFlows": [ "ALLOW_USER_PASSWORD_AUTH", "ALLOW_USER_SRP_AUTH", "ALLOW_REFRESH_TOKEN_AUTH" ], "SupportedIdentityProviders": [ "Google", "MyOIDC", "Facebook" ], "CallbackURLs": [ "https://example.com", "https://www.amazon.com", "myapp://example", "http://localhost:8001" ], "AllowedOAuthFlows": [ "implicit", "code" ], "AllowedOAuthScopes": [ "aws.cognito.signin.user.admin", "openid", "profile", "solar-system-data/asteroids.add" ], "AllowedOAuthFlowsUserPoolClient": true, "AnalyticsConfiguration": { "ApplicationArn": "arn:aws:mobiletargeting:us-west-2:123456789012:apps/thisisanexamplepinpointapplicationid", "RoleArn": "arn:aws:iam::123456789012:role/aws-service-role/cognito-idp.amazonaws.com/AWSServiceRoleForAmazonCognitoIdp", "UserDataShared": true }, "PreventUserExistenceErrors": "ENABLED", "EnableTokenRevocation": true, "EnablePropagateAdditionalUserContextData": true, "AuthSessionValidity": 4 } }`For more information, see [Application-specific settings with app clients](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-client-apps.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [CreateUserPoolClient](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-user-pool-client.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-user-pool-domain`.

- **AWS CLI**
- 
            
                    **Example 1: To create a user pool domain**The following `create-user-pool-domain`example creates a new custom domain.`aws cognito-idp create-user-pool-domain \ --user-pool-id``us-west-2_EXAMPLE`\ --domain`auth.example.com`\ --custom-domain-config`CertificateArn=arn:aws:acm:us-east-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`Output: `{ "CloudFrontDomain": "example1domain.cloudfront.net" }`For more information, see [Configuring a user pool domain](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-assign-domain.html)in the*Amazon Cognito Developer Guide*.**Example 2: To create a user pool domain**The following `create-user-pool-domain`example creates a new domain with a service-owned prefix.`aws cognito-idp create-user-pool-domain \ --user-pool-id``us-west-2_EXAMPLE2`\ --domain`mydomainprefix`For more information, see [Configuring a user pool domain](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-assign-domain.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [CreateUserPoolDomain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-user-pool-domain.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-user-pool`.

- **AWS CLI**
- 
            
                    **To create a minimally configured user pool**This example creates a user pool named MyUserPool using default values. There are no required attributes and no application clients. MFA and advanced security is disabled. Command: `aws cognito-idp create-user-pool --pool-name``MyUserPool`Output: `{ "UserPool": { "SchemaAttributes": [ { "Name": "sub", "StringAttributeConstraints": { "MinLength": "1", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": true, "AttributeDataType": "String", "Mutable": false }, { "Name": "name", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "given_name", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "family_name", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "middle_name", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "nickname", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "preferred_username", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "profile", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "picture", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "website", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "email", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "AttributeDataType": "Boolean", "DeveloperOnlyAttribute": false, "Required": false, "Name": "email_verified", "Mutable": true }, { "Name": "gender", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "birthdate", "StringAttributeConstraints": { "MinLength": "10", "MaxLength": "10" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "zoneinfo", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "locale", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "phone_number", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "AttributeDataType": "Boolean", "DeveloperOnlyAttribute": false, "Required": false, "Name": "phone_number_verified", "Mutable": true }, { "Name": "address", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "updated_at", "NumberAttributeConstraints": { "MinValue": "0" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "Number", "Mutable": true } ], "MfaConfiguration": "OFF", "Name": "MyUserPool", "LastModifiedDate": 1547833345.777, "AdminCreateUserConfig": { "UnusedAccountValidityDays": 7, "AllowAdminCreateUserOnly": false }, "EmailConfiguration": {}, "Policies": { "PasswordPolicy": { "RequireLowercase": true, "RequireSymbols": true, "RequireNumbers": true, "MinimumLength": 8, "RequireUppercase": true } }, "CreationDate": 1547833345.777, "EstimatedNumberOfUsers": 0, "Id": "us-west-2_aaaaaaaaa", "LambdaConfig": {} } }`**To create a user pool with two required attributes**This example creates a user pool MyUserPool. The pool is configured to accept email as a username attribute. It also sets the email source address to a validated address using Amazon Simple Email Service. Command: `aws cognito-idp create-user-pool --pool-name``MyUserPool`--username-attributes`"email"`--email-configuration=SourceArn="arn:aws:ses:us-east-1:111111111111:identity/jane@example.com",ReplyToEmailAddress="jane@example.com"Output: `{ "UserPool": { "SchemaAttributes": [ { "Name": "sub", "StringAttributeConstraints": { "MinLength": "1", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": true, "AttributeDataType": "String", "Mutable": false }, { "Name": "name", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "given_name", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "family_name", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "middle_name", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "nickname", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "preferred_username", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "profile", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "picture", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "website", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "email", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "AttributeDataType": "Boolean", "DeveloperOnlyAttribute": false, "Required": false, "Name": "email_verified", "Mutable": true }, { "Name": "gender", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "birthdate", "StringAttributeConstraints": { "MinLength": "10", "MaxLength": "10" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "zoneinfo", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "locale", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "phone_number", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "AttributeDataType": "Boolean", "DeveloperOnlyAttribute": false, "Required": false, "Name": "phone_number_verified", "Mutable": true }, { "Name": "address", "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "String", "Mutable": true }, { "Name": "updated_at", "NumberAttributeConstraints": { "MinValue": "0" }, "DeveloperOnlyAttribute": false, "Required": false, "AttributeDataType": "Number", "Mutable": true } ], "MfaConfiguration": "OFF", "Name": "MyUserPool", "LastModifiedDate": 1547837788.189, "AdminCreateUserConfig": { "UnusedAccountValidityDays": 7, "AllowAdminCreateUserOnly": false }, "EmailConfiguration": { "ReplyToEmailAddress": "jane@example.com", "SourceArn": "arn:aws:ses:us-east-1:111111111111:identity/jane@example.com" }, "Policies": { "PasswordPolicy": { "RequireLowercase": true, "RequireSymbols": true, "RequireNumbers": true, "MinimumLength": 8, "RequireUppercase": true } }, "UsernameAttributes": [ "email" ], "CreationDate": 1547837788.189, "EstimatedNumberOfUsers": 0, "Id": "us-west-2_aaaaaaaaa", "LambdaConfig": {} } }`- 
                    For API details, see [CreateUserPool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/create-user-pool.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-group`.

- **AWS CLI**
- 
            
                    **To delete a group**This example deletes a group. Command: `aws cognito-idp delete-group --user-pool-id``us-west-2_aaaaaaaaa`--group-name`MyGroupName`- 
                    For API details, see [DeleteGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-identity-provider`.

- **AWS CLI**
- 
            
                    **To delete an identity provider**This example deletes an identity provider. Command: `aws cognito-idp delete-identity-provider --user-pool-id``us-west-2_aaaaaaaaa`--provider-name`Facebook`- 
                    For API details, see [DeleteIdentityProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-identity-provider.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-resource-server`.

- **AWS CLI**
- 
            
                    **To delete a resource server**This example deletes a resource server named weather.example.com. Command: `aws cognito-idp delete-resource-server --user-pool-id``us-west-2_aaaaaaaaa`--identifier`weather.example.com`- 
                    For API details, see [DeleteResourceServer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-resource-server.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-user-attributes`.

- **AWS CLI**
- 
            
                    **To delete a user attribute**The following `delete-user-attributes`example deletes the custom attribute "custom:attribute" from the currently signed-in user.`aws cognito-idp delete-user-attributes \ --access-token``ACCESS_TOKEN`\ --user-attribute-names`"custom:department"`This command produces no output. For more information, see [Working with user attributes](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [DeleteUserAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-user-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-user-pool-client`.

- **AWS CLI**
- 
            
                    **To delete a user pool client**This example deletes a user pool client. Command: `aws cognito-idp delete-user-pool-client --user-pool-id``us-west-2_aaaaaaaaa`--client-id`38fjsnc484p94kpqsnet7mpld0`- 
                    For API details, see [DeleteUserPoolClient](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-user-pool-client.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-user-pool-domain`.

- **AWS CLI**
- 
            
                    **To delete a user pool domain**The following `delete-user-pool-domain`example deletes a user pool domain named`my-domain``aws cognito-idp delete-user-pool-domain \ --user-pool-id``us-west-2_aaaaaaaaa`\ --domain`my-domain`- 
                    For API details, see [DeleteUserPoolDomain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-user-pool-domain.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-user-pool`.

- **AWS CLI**
- 
            
                    **To delete a user pool**This example deletes a user pool using the user pool id, us-west-2_aaaaaaaaa. Command: `aws cognito-idp delete-user-pool --user-pool-id``us-west-2_aaaaaaaaa`- 
                    For API details, see [DeleteUserPool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-user-pool.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-user`.

- **AWS CLI**
- 
            
                    **To delete a user**This example deletes a user. Command: `aws cognito-idp delete-user --access-token``ACCESS_TOKEN`- 
                    For API details, see [DeleteUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/delete-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-identity-provider`.

- **AWS CLI**
- 
            
                    **To describe an identity provider**This example describes an identity provider named Facebook. Command: `aws cognito-idp describe-identity-provider --user-pool-id``us-west-2_aaaaaaaaa`--provider-name`Facebook`Output: `{ "IdentityProvider": { "UserPoolId": "us-west-2_aaaaaaaaa", "ProviderName": "Facebook", "ProviderType": "Facebook", "ProviderDetails": { "attributes_url": "https://graph.facebook.com/me?fields=", "attributes_url_add_attributes": "true", "authorize_scopes": myscope", "authorize_url": "https://www.facebook.com/v2.9/dialog/oauth", "client_id": "11111", "client_secret": "11111", "token_request_method": "GET", "token_url": "https://graph.facebook.com/v2.9/oauth/access_token" }, "AttributeMapping": { "username": "id" }, "IdpIdentifiers": [], "LastModifiedDate": 1548105901.736, "CreationDate": 1548105901.736 } }`- 
                    For API details, see [DescribeIdentityProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-identity-provider.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-resource-server`.

- **AWS CLI**
- 
            
                    **To describe a resource server**This example describes the resource server weather.example.com. Command: `aws cognito-idp describe-resource-server --user-pool-id``us-west-2_aaaaaaaaa`--identifier`weather.example.com`Output: `{ "ResourceServer": { "UserPoolId": "us-west-2_aaaaaaaaa", "Identifier": "weather.example.com", "Name": "Weather", "Scopes": [ { "ScopeName": "weather.update", "ScopeDescription": "Update weather forecast" }, { "ScopeName": "weather.read", "ScopeDescription": "Read weather forecasts" }, { "ScopeName": "weather.delete", "ScopeDescription": "Delete a weather forecast" } ] } }`- 
                    For API details, see [DescribeResourceServer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-resource-server.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-risk-configuration`.

- **AWS CLI**
- 
            
                    **To describe a risk configuration**This example describes the risk configuration associated with pool us-west-2_aaaaaaaaa. Command: `aws cognito-idp describe-risk-configuration --user-pool-id``us-west-2_aaaaaaaaa`Output: `{ "RiskConfiguration": { "UserPoolId": "us-west-2_aaaaaaaaa", "CompromisedCredentialsRiskConfiguration": { "EventFilter": [ "SIGN_IN", "SIGN_UP", "PASSWORD_CHANGE" ], "Actions": { "EventAction": "BLOCK" } }, "AccountTakeoverRiskConfiguration": { "NotifyConfiguration": { "From": "diego@example.com", "ReplyTo": "diego@example.com", "SourceArn": "arn:aws:ses:us-east-1:111111111111:identity/diego@example.com", "BlockEmail": { "Subject": "Blocked sign-in attempt", "HtmlBody": "<!DOCTYPE html>\n<html>\n<head>\n\t<title>HTML email context</title>\n\t<meta charset=\"utf-8\">\n</head>\n<body>\n<pre>We blocked an unrecognized sign-in to your account with this information:\n<ul>\n<li>Time: {login-time}</li>\n<li>Device: {device-name}</li>\n<li>Location: {city}, {country}</li>\n</ul>\nIf this sign-in was not by you, you should change your password and notify us by clicking on <a href={one-click-link-invalid}>this link</a>\nIf this sign-in was by you, you can follow <a href={one-click-link-valid}>this link</a> to let us know</pre>\n</body>\n</html>", "TextBody": "We blocked an unrecognized sign-in to your account with this information:\nTime: {login-time}\nDevice: {device-name}\nLocation: {city}, {country}\nIf this sign-in was not by you, you should change your password and notify us by clicking on {one-click-link-invalid}\nIf this sign-in was by you, you can follow {one-click-link-valid} to let us know" }, "NoActionEmail": { "Subject": "New sign-in attempt", "HtmlBody": "<!DOCTYPE html>\n<html>\n<head>\n\t<title>HTML email context</title>\n\t<meta charset=\"utf-8\">\n</head>\n<body>\n<pre>We observed an unrecognized sign-in to your account with this information:\n<ul>\n<li>Time: {login-time}</li>\n<li>Device: {device-name}</li>\n<li>Location: {city}, {country}</li>\n</ul>\nIf this sign-in was not by you, you should change your password and notify us by clicking on <a href={one-click-link-invalid}>this link</a>\nIf this sign-in was by you, you can follow <a href={one-click-link-valid}>this link</a> to let us know</pre>\n</body>\n</html>", "TextBody": "We observed an unrecognized sign-in to your account with this information:\nTime: {login-time}\nDevice: {device-name}\nLocation: {city}, {country}\nIf this sign-in was not by you, you should change your password and notify us by clicking on {one-click-link-invalid}\nIf this sign-in was by you, you can follow {one-click-link-valid} to let us know" }, "MfaEmail": { "Subject": "New sign-in attempt", "HtmlBody": "<!DOCTYPE html>\n<html>\n<head>\n\t<title>HTML email context</title>\n\t<meta charset=\"utf-8\">\n</head>\n<body>\n<pre>We required you to use multi-factor authentication for the following sign-in attempt:\n<ul>\n<li>Time: {login-time}</li>\n<li>Device: {device-name}</li>\n<li>Location: {city}, {country}</li>\n</ul>\nIf this sign-in was not by you, you should change your password and notify us by clicking on <a href={one-click-link-invalid}>this link</a>\nIf this sign-in was by you, you can follow <a href={one-click-link-valid}>this link</a> to let us know</pre>\n</body>\n</html>", "TextBody": "We required you to use multi-factor authentication for the following sign-in attempt:\nTime: {login-time}\nDevice: {device-name}\nLocation: {city}, {country}\nIf this sign-in was not by you, you should change your password and notify us by clicking on {one-click-link-invalid}\nIf this sign-in was by you, you can follow {one-click-link-valid} to let us know" } }, "Actions": { "LowAction": { "Notify": true, "EventAction": "NO_ACTION" }, "MediumAction": { "Notify": true, "EventAction": "MFA_IF_CONFIGURED" }, "HighAction": { "Notify": true, "EventAction": "MFA_IF_CONFIGURED" } } } } }`- 
                    For API details, see [DescribeRiskConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-risk-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-user-import-job`.

- **AWS CLI**
- 
            
                    **To describe a user import job**This example describes a user input job. For more information about importing users, see Importing Users into User Pools From a CSV File. Command: `aws cognito-idp describe-user-import-job --user-pool-id``us-west-2_aaaaaaaaa`--job-id`import-TZqNQvDRnW`Output: `{ "UserImportJob": { "JobName": "import-Test1", "JobId": "import-TZqNQvDRnW", "UserPoolId": "us-west-2_aaaaaaaaa", "PreSignedUrl": "PRE_SIGNED URL", "CreationDate": 1548271708.512, "Status": "Created", "CloudWatchLogsRoleArn": "arn:aws:iam::111111111111:role/CognitoCloudWatchLogsRole", "ImportedUsers": 0, "SkippedUsers": 0, "FailedUsers": 0 } }`- 
                    For API details, see [DescribeUserImportJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-user-import-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-user-pool-client`.

- **AWS CLI**
- 
            
                    **To describe a user pool client**This example describes a user pool client. Command: `aws cognito-idp describe-user-pool-client --user-pool-id``us-west-2_aaaaaaaaa`--client-id`38fjsnc484p94kpqsnet7mpld0`Output: `{ "UserPoolClient": { "UserPoolId": "us-west-2_aaaaaaaaa", "ClientName": "MyApp", "ClientId": "38fjsnc484p94kpqsnet7mpld0", "ClientSecret": "CLIENT_SECRET", "LastModifiedDate": 1548108676.163, "CreationDate": 1548108676.163, "RefreshTokenValidity": 30, "ReadAttributes": [ "address", "birthdate", "custom:CustomAttr1", "custom:CustomAttr2", "email", "email_verified", "family_name", "gender", "given_name", "locale", "middle_name", "name", "nickname", "phone_number", "phone_number_verified", "picture", "preferred_username", "profile", "updated_at", "website", "zoneinfo" ], "WriteAttributes": [ "address", "birthdate", "custom:CustomAttr1", "custom:CustomAttr2", "email", "family_name", "gender", "given_name", "locale", "middle_name", "name", "nickname", "phone_number", "picture", "preferred_username", "profile", "updated_at", "website", "zoneinfo" ], "ExplicitAuthFlows": [ "ADMIN_NO_SRP_AUTH", "USER_PASSWORD_AUTH" ], "AllowedOAuthFlowsUserPoolClient": false } }`- 
                    For API details, see [DescribeUserPoolClient](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-user-pool-client.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-user-pool-domain`.

- **AWS CLI**
- 
            
                    **To describe a user pool client**This example describes a user pool domain named my-domain. Command: `aws cognito-idp describe-user-pool-domain --domain``my-domain`Output: `{ "DomainDescription": { "UserPoolId": "us-west-2_aaaaaaaaa", "AWSAccountId": "111111111111", "Domain": "my-domain", "S3Bucket": "aws-cognito-prod-pdx-assets", "CloudFrontDistribution": "aaaaaaaaaaaaa.cloudfront.net", "Version": "20190128175402", "Status": "ACTIVE", "CustomDomainConfig": {} } }`- 
                    For API details, see [DescribeUserPoolDomain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-user-pool-domain.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-user-pool`.

- **AWS CLI**
- 
            
                    **To describe a user pool**The following example describes a user pool with the user pool id us-west-2_EXAMPLE. `aws cognito-idp describe-user-pool \ --user-pool-id``us-west-2_EXAMPLE`Output: `{ "UserPool": { "Id": "us-west-2_EXAMPLE", "Name": "MyUserPool", "Policies": { "PasswordPolicy": { "MinimumLength": 8, "RequireUppercase": true, "RequireLowercase": true, "RequireNumbers": true, "RequireSymbols": true, "TemporaryPasswordValidityDays": 1 } }, "DeletionProtection": "ACTIVE", "LambdaConfig": { "PreSignUp": "arn:aws:lambda:us-west-2:123456789012:function:MyPreSignUpFunction", "CustomMessage": "arn:aws:lambda:us-west-2:123456789012:function:MyCustomMessageFunction", "PostConfirmation": "arn:aws:lambda:us-west-2:123456789012:function:MyPostConfirmationFunction", "PreAuthentication": "arn:aws:lambda:us-west-2:123456789012:function:MyPreAuthenticationFunction", "PostAuthentication": "arn:aws:lambda:us-west-2:123456789012:function:MyPostAuthenticationFunction", "DefineAuthChallenge": "arn:aws:lambda:us-west-2:123456789012:function:MyDefineAuthChallengeFunction", "CreateAuthChallenge": "arn:aws:lambda:us-west-2:123456789012:function:MyCreateAuthChallengeFunction", "VerifyAuthChallengeResponse": "arn:aws:lambda:us-west-2:123456789012:function:MyVerifyAuthChallengeFunction", "PreTokenGeneration": "arn:aws:lambda:us-west-2:123456789012:function:MyPreTokenGenerationFunction", "UserMigration": "arn:aws:lambda:us-west-2:123456789012:function:MyMigrateUserFunction", "PreTokenGenerationConfig": { "LambdaVersion": "V2_0", "LambdaArn": "arn:aws:lambda:us-west-2:123456789012:function:MyPreTokenGenerationFunction" }, "CustomSMSSender": { "LambdaVersion": "V1_0", "LambdaArn": "arn:aws:lambda:us-west-2:123456789012:function:MyCustomSMSSenderFunction" }, "CustomEmailSender": { "LambdaVersion": "V1_0", "LambdaArn": "arn:aws:lambda:us-west-2:123456789012:function:MyCustomEmailSenderFunction" }, "KMSKeyID": "arn:aws:kms:us-west-2:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222" }, "LastModifiedDate": 1726784814.598, "CreationDate": 1602103465.273, "SchemaAttributes": [ { "Name": "sub", "AttributeDataType": "String", "DeveloperOnlyAttribute": false, "Mutable": false, "Required": true, "StringAttributeConstraints": { "MinLength": "1", "MaxLength": "2048" } }, { "Name": "name", "AttributeDataType": "String", "DeveloperOnlyAttribute": false, "Mutable": true, "Required": false, "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" } }, { "Name": "given_name", "AttributeDataType": "String", "DeveloperOnlyAttribute": false, "Mutable": true, "Required": false, "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" } }, { "Name": "family_name", "AttributeDataType": "String", "DeveloperOnlyAttribute": false, "Mutable": true, "Required": false, "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" } }, { "Name": "middle_name", "AttributeDataType": "String", "DeveloperOnlyAttribute": false, "Mutable": true, "Required": false, "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" } }, { "Name": "nickname", "AttributeDataType": "String", "DeveloperOnlyAttribute": false, "Mutable": true, "Required": false, "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" } }, { "Name": "preferred_username", "AttributeDataType": "String", "DeveloperOnlyAttribute": false, "Mutable": true, "Required": false, "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" } }, { "Name": "profile", "AttributeDataType": "String", "DeveloperOnlyAttribute": false, "Mutable": true, "Required": false, "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" } }, { "Name": "picture", "AttributeDataType": "String", "DeveloperOnlyAttribute": false, "Mutable": true, "Required": false, "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" } }, { "Name": "website", "AttributeDataType": "String", "DeveloperOnlyAttribute": false, "Mutable": true, "Required": false, "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" } }, { "Name": "email", "AttributeDataType": "String", "DeveloperOnlyAttribute": false, "Mutable": true, "Required": true, "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" } }, { "Name": "email_verified", "AttributeDataType": "Boolean", "DeveloperOnlyAttribute": false, "Mutable": true, "Required": false }, { "Name": "gender", "AttributeDataType": "String", "DeveloperOnlyAttribute": false, "Mutable": true, "Required": false, "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" } }, { "Name": "birthdate", "AttributeDataType": "String", "DeveloperOnlyAttribute": false, "Mutable": true, "Required": false, "StringAttributeConstraints": { "MinLength": "10", "MaxLength": "10" } }, { "Name": "zoneinfo", "AttributeDataType": "String", "DeveloperOnlyAttribute": false, "Mutable": true, "Required": false, "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" } }, { "Name": "locale", "AttributeDataType": "String", "DeveloperOnlyAttribute": false, "Mutable": true, "Required": false, "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" } }, { "Name": "phone_number", "AttributeDataType": "String", "DeveloperOnlyAttribute": false, "Mutable": true, "Required": false, "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" } }, { "Name": "phone_number_verified", "AttributeDataType": "Boolean", "DeveloperOnlyAttribute": false, "Mutable": true, "Required": false }, { "Name": "address", "AttributeDataType": "String", "DeveloperOnlyAttribute": false, "Mutable": true, "Required": false, "StringAttributeConstraints": { "MinLength": "0", "MaxLength": "2048" } }, { "Name": "updated_at", "AttributeDataType": "Number", "DeveloperOnlyAttribute": false, "Mutable": true, "Required": false, "NumberAttributeConstraints": { "MinValue": "0" } }, { "Name": "identities", "AttributeDataType": "String", "DeveloperOnlyAttribute": false, "Mutable": true, "Required": false, "StringAttributeConstraints": {} }, { "Name": "custom:111", "AttributeDataType": "String", "DeveloperOnlyAttribute": false, "Mutable": true, "Required": false, "StringAttributeConstraints": { "MinLength": "1", "MaxLength": "256" } }, { "Name": "dev:custom:222", "AttributeDataType": "String", "DeveloperOnlyAttribute": true, "Mutable": true, "Required": false, "StringAttributeConstraints": { "MinLength": "1", "MaxLength": "421" } }, { "Name": "custom:accesstoken", "AttributeDataType": "String", "DeveloperOnlyAttribute": false, "Mutable": true, "Required": false, "StringAttributeConstraints": { "MaxLength": "2048" } }, { "Name": "custom:idtoken", "AttributeDataType": "String", "DeveloperOnlyAttribute": false, "Mutable": true, "Required": false, "StringAttributeConstraints": { "MaxLength": "2048" } } ], "AutoVerifiedAttributes": [ "email" ], "SmsVerificationMessage": "Your verification code is {####}. ", "EmailVerificationMessage": "Your verification code is {####}. ", "EmailVerificationSubject": "Your verification code", "VerificationMessageTemplate": { "SmsMessage": "Your verification code is {####}. ", "EmailMessage": "Your verification code is {####}. ", "EmailSubject": "Your verification code", "EmailMessageByLink": "Please click the link below to verify your email address. <b>{##Verify Your Email##}</b>\n this is from us-west-2_ywDJHlIfU", "EmailSubjectByLink": "Your verification link", "DefaultEmailOption": "CONFIRM_WITH_LINK" }, "SmsAuthenticationMessage": "Your verification code is {####}. ", "UserAttributeUpdateSettings": { "AttributesRequireVerificationBeforeUpdate": [] }, "MfaConfiguration": "OPTIONAL", "DeviceConfiguration": { "ChallengeRequiredOnNewDevice": true, "DeviceOnlyRememberedOnUserPrompt": false }, "EstimatedNumberOfUsers": 166, "EmailConfiguration": { "SourceArn": "arn:aws:ses:us-west-2:123456789012:identity/admin@example.com", "EmailSendingAccount": "DEVELOPER" }, "SmsConfiguration": { "SnsCallerArn": "arn:aws:iam::123456789012:role/service-role/userpool-SMS-Role", "ExternalId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "SnsRegion": "us-west-2" }, "UserPoolTags": {}, "Domain": "myCustomDomain", "CustomDomain": "auth.example.com", "AdminCreateUserConfig": { "AllowAdminCreateUserOnly": false, "UnusedAccountValidityDays": 1, "InviteMessageTemplate": { "SMSMessage": "Your username is {username} and temporary password is {####}. ", "EmailMessage": "Your username is {username} and temporary password is {####}. ", "EmailSubject": "Your temporary password" } }, "UserPoolAddOns": { "AdvancedSecurityMode": "ENFORCED", "AdvancedSecurityAdditionalFlows": {} }, "Arn": "arn:aws:cognito-idp:us-west-2:123456789012:userpool/us-west-2_EXAMPLE", "AccountRecoverySetting": { "RecoveryMechanisms": [ { "Priority": 1, "Name": "verified_email" } ] } } }`For more information, see [Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [DescribeUserPool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/describe-user-pool.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `forget-device`.

- **AWS CLI**
- 
            
                    **To forget a device**This example forgets device a device. Command: `aws cognito-idp forget-device --device-key``us-west-2_abcd_1234-5678`- 
                    For API details, see [ForgetDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/forget-device.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `forgot-password`.

- **AWS CLI**
- 
            
                    **To force a password change**The following `forgot-password`example sends a message to jane@example.com to change their password.`aws cognito-idp forgot-password --client-id``38fjsnc484p94kpqsnet7mpld0`--username`jane@example.com`Output: `{ "CodeDeliveryDetails": { "Destination": "j***@e***.com", "DeliveryMedium": "EMAIL", "AttributeName": "email" } }`- 
                    For API details, see [ForgotPassword](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/forgot-password.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-csv-header`.

- **AWS CLI**
- 
            
                    **To create a csv header**This example creates a csv header. For more information about importing users, see Importing Users into User Pools From a CSV File. Command: `aws cognito-idp get-csv-header --user-pool-id``us-west-2_aaaaaaaaa`Output: `{ "UserPoolId": "us-west-2_aaaaaaaaa", "CSVHeader": [ "name", "given_name", "family_name", "middle_name", "nickname", "preferred_username", "profile", "picture", "website", "email", "email_verified", "gender", "birthdate", "zoneinfo", "locale", "phone_number", "phone_number_verified", "address", "updated_at", "cognito:mfa_enabled", "cognito:username" ] }`... Importing Users into User Pools From a CSV File: https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-using-import-tool.html - 
                    For API details, see [GetCsvHeader](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-csv-header.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-device`.

- **AWS CLI**
- 
            
                    **To get a device**The following `get-device`example displays one device for currently signed-in user.`aws cognito-idp get-device \ --access-token``eyJra456defEXAMPLE`\ --device-key`us-west-2_a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "Device": { "DeviceKey": "us-west-2_a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "DeviceAttributes": [ { "Name": "device_status", "Value": "valid" }, { "Name": "device_name", "Value": "MyDevice" }, { "Name": "dev:device_arn", "Value": "arn:aws:cognito-idp:us-west-2:123456789012:owner/diego.us-west-2_EXAMPLE/device/us-west-2_a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }, { "Name": "dev:device_owner", "Value": "diego.us-west-2_EXAMPLE" }, { "Name": "last_ip_used", "Value": "192.0.2.1" }, { "Name": "dev:device_remembered_status", "Value": "remembered" }, { "Name": "dev:device_sdk", "Value": "aws-sdk" } ], "DeviceCreateDate": 1715100742.022, "DeviceLastModifiedDate": 1723233651.167, "DeviceLastAuthenticatedDate": 1715100742.0 } }`For more information, see [Working with user devices in your user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [GetDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-device.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-group`.

- **AWS CLI**
- 
            
                    **To get information about a group**The following `get-group`example lists the properties of the user group named`MyGroup`. This group has a precedence and an IAM role associated with it.`aws cognito-idp get-group \ --user-pool-id``us-west-2_EXAMPLE`\ --group-name`MyGroup`Output: `{ "Group": { "GroupName": "MyGroup", "UserPoolId": "us-west-2_EXAMPLE", "RoleArn": "arn:aws:iam::123456789012:role/example-cognito-role", "Precedence": 7, "LastModifiedDate": 1697211218.305, "CreationDate": 1611685503.954 } }`For more information, see [Adding groups to a user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-user-groups.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [GetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-identity-provider-by-identifier`.

- **AWS CLI**
- 
            
                    **To get the configuration of an identity provider from the IdP identifier**The following `get-identity-provider-by-identifier`example returns the configuration of the identity provider with the identifier`mysso`.`aws cognito-idp get-identity-provider-by-identifier \ --user-pool-id``us-west-2_EXAMPLE`\ --idp-identifier`mysso`Output: `{ "IdentityProvider": { "UserPoolId": "us-west-2_EXAMPLE", "ProviderName": "MYSAML", "ProviderType": "SAML", "ProviderDetails": { "ActiveEncryptionCertificate": "[Certificate contents]", "IDPSignout": "false", "MetadataURL": "https://auth.example.com/saml/metadata/", "SLORedirectBindingURI": "https://auth.example.com/saml/logout/", "SSORedirectBindingURI": "https://auth.example.com/saml/assertion/" }, "AttributeMapping": { "email": "email" }, "IdpIdentifiers": [ "mysso", "mysamlsso" ], "LastModifiedDate": 1705616729.188, "CreationDate": 1643734622.919 } }`For more information, see [Third-party IdP sign-in](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [GetIdentityProviderByIdentifier](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-identity-provider-by-identifier.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-log-delivery-configuration`.

- **AWS CLI**
- 
            
                    **To display the log delivery configuration**The following `get-log-delivery-configuration`example displays the log export settings of the requested user pool.`aws cognito-idp get-log-delivery-configuration \ --user-pool-id``us-west-2_EXAMPLE`Output: `{ "LogDeliveryConfiguration": { "UserPoolId": "us-west-2_EXAMPLE", "LogConfigurations": [ { "LogLevel": "INFO", "EventSource": "userAuthEvents", "FirehoseConfiguration": { "StreamArn": "arn:aws:firehose:us-west-2:123456789012:deliverystream/my-test-deliverystream" } }, { "LogLevel": "ERROR", "EventSource": "userNotification", "CloudWatchLogsConfiguration": { "LogGroupArn": "arn:aws:logs:us-west-2:123456789012:log-group:my-message-delivery-logs" } } ] } }`For more information, see [Exporting user pool logs](https://docs.aws.amazon.com/cognito/latest/developerguide/exporting-quotas-and-usage.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [GetLogDeliveryConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-log-delivery-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-signing-certificate`.

- **AWS CLI**
- 
            
                    **To display the SAML signing certificate**The following `get-signing-certificate`example displays the SAML 2.0 signing certificate for the request user pool.`aws cognito-idp get-signing-certificate \ --user-pool-id``us-west-2_EXAMPLE`Output: `{ "Certificate": "[Certificate content]" }`For more information, see [SAML signing and encryption](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-SAML-signing-encryption.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [GetSigningCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-signing-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-ui-customization`.

- **AWS CLI**
- 
            
                    **To display the classic hosted UI customization settings for an app client**The following `get-ui-customization`example displays the classic hosted UI customization settings for an app client that doesn't inherit settings from the user pool.`aws cognito-idp get-ui-customization \ --user-pool-id``us-west-2_EXAMPLE`\ --client-id`1example23456789`Output: `{ "UICustomization": { "UserPoolId": "us-west-2_EXAMPLE", "ClientId": "1example23456789", "ImageUrl": "https://example.cloudfront.net/us-west-2_EXAMPLE/1example23456789/20250115191928/assets/images/image.jpg", "CSS": "\n.logo-customizable {\n max-width: 80%;\n max-height: 30%;\n}\n\n.banner-customizable {\n padding: 25px 0px 25px 0px;\n background-color: lightgray;\n}\n\n.label-customizable {\n font-weight: 400;\n}\n\n.textDescription-customizable {\n padding-top: 100px;\n padding-bottom: 10px;\n display: block;\n font-size: 12px;\n}\n\n.idpDescription-customizable {\n padding-top: 10px;\n padding-bottom: 10px;\n display: block;\n font-size: 16px;\n}\n\n.legalText-customizable {\n color: #747474;\n font-size: 11px;\n}\n\n.submitButton-customizable {\n font-size: 14px;\n font-weight: bold;\n margin: 20px 0px 10px 0px;\n height: 50px;\n width: 100%;\n color: #fff;\n background-color: #337ab7;\n}\n\n.submitButton-customizable:hover {\n color: #fff;\n background-color: #286090;\n}\n\n.errorMessage-customizable {\n padding: 5px;\n font-size: 12px;\n width: 100%;\n background: #F5F5F5;\n border: 2px solid #D64958;\n color: #D64958;\n}\n\n.inputField-customizable {\n width: 100%;\n height: 34px;\n color: #555;\n background-color: #fff;\n border: 1px solid #ccc;\n}\n\n.inputField-customizable:focus {\n border-color: #66afe9;\n outline: 0;\n}\n\n.idpButton-customizable {\n height: 40px;\n width: 100%;\n width: 100%;\n text-align: center;\n margin-bottom: 15px;\n color: #fff;\n background-color: #5bc0de;\n border-color: #46b8da;\n}\n\n.idpButton-customizable:hover {\n color: #fff;\n background-color: #31b0d5;\n}\n\n.socialButton-customizable {\n border-radius: 2px;\n height: 60px;\n margin-bottom: 15px;\n padding: 1px;\n text-align: left;\n width: 100%;\n}\n\n.redirect-customizable {\n text-align: center;\n}\n\n.passwordCheck-notValid-customizable {\n color: #DF3312;\n}\n\n.passwordCheck-valid-customizable {\n color: #19BF00;\n}\n\n.background-customizable {\n background-color: #fff;\n}\n", "CSSVersion": "20250115191928" } }`For more information, see [Hosted UI (classic) branding](https://docs.aws.amazon.com/cognito/latest/developerguide/hosted-ui-classic-branding.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [GetUiCustomization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-ui-customization.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-user-attribute-verification-code`.

- **AWS CLI**
- 
            
                    **To send an attribute verification code to the current user**The following `get-user-attribute-verification-code`example sends an attribute verification code to the currently signed-in user's email address.`aws cognito-idp get-user-attribute-verification-code \ --access-token``eyJra456defEXAMPLE`\ --attribute-name`email`Output: `{ "CodeDeliveryDetails": { "Destination": "a***@e***", "DeliveryMedium": "EMAIL", "AttributeName": "email" } }`For more information, see [Signing up and confirming user accounts](https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [GetUserAttributeVerificationCode](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-user-attribute-verification-code.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-user-auth-factors`.

- **AWS CLI**
- 
            
                    **To list the authentication factors available to the current user**The following `get-user-auth-factors`example lists the available authentication factors for the currently signed-in user.`aws cognito-idp get-user-auth-factors \ --access-token``eyJra456defEXAMPLE`Output: `{ "Username": "testuser", "ConfiguredUserAuthFactors": [ "PASSWORD", "EMAIL_OTP", "SMS_OTP", "WEB_AUTHN" ] }`For more information, see [Authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [GetUserAuthFactors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-user-auth-factors.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-user-pool-mfa-config`.

- **AWS CLI**
- 
            
                    **To display the multi-factor authentication and WebAuthn settings of a user pool**The following `get-user-pool-mfa-config`example displays the MFA and WebAuthn configuration of the requested user pool.`aws cognito-idp get-user-pool-mfa-config \ --user-pool-id``us-west-2_EXAMPLE`Output: `{ "SmsMfaConfiguration": { "SmsAuthenticationMessage": "Your OTP for MFA or sign-in: use {####}.", "SmsConfiguration": { "SnsCallerArn": "arn:aws:iam::123456789012:role/service-role/my-SMS-Role", "ExternalId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "SnsRegion": "us-west-2" } }, "SoftwareTokenMfaConfiguration": { "Enabled": true }, "EmailMfaConfiguration": { "Message": "Your OTP for MFA or sign-in: use {####}", "Subject": "OTP test" }, "MfaConfiguration": "OPTIONAL", "WebAuthnConfiguration": { "RelyingPartyId": "auth.example.com", "UserVerification": "preferred" } }`For more information, see [Adding MFA](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [GetUserPoolMfaConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-user-pool-mfa-config.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-user`.

- **AWS CLI**
- 
            
                    **To get the details of the current user**The following `get-user`example displays the profile of the currently signed-in user.`aws cognito-idp get-user \ --access-token``eyJra456defEXAMPLE`Output: `{ "Username": "johndoe", "UserAttributes": [ { "Name": "sub", "Value": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }, { "Name": "identities", "Value": "[{\"userId\":\"a1b2c3d4-5678-90ab-cdef-EXAMPLE22222\",\"providerName\":\"SignInWithApple\",\"providerType\":\"SignInWithApple\",\"issuer\":null,\"primary\":false,\"dateCreated\":1701125599632}]" }, { "Name": "email_verified", "Value": "true" }, { "Name": "custom:state", "Value": "Maine" }, { "Name": "name", "Value": "John Doe" }, { "Name": "phone_number_verified", "Value": "true" }, { "Name": "phone_number", "Value": "+12065551212" }, { "Name": "preferred_username", "Value": "jamesdoe" }, { "Name": "locale", "Value": "EMEA" }, { "Name": "email", "Value": "jamesdoe@example.com" } ] }`For more information, see [Managing users](https://docs.aws.amazon.com/cognito/latest/developerguide/managing-users.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [GetUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/get-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `global-sign-out`.

- **AWS CLI**
- 
            
                    **To sign out the current user**The following `global-sign-out`example signs out the current user.`aws cognito-idp global-sign-out \ --access-token``eyJra456defEXAMPLE`This command produces no output. For more information, see [Managing users](https://docs.aws.amazon.com/cognito/latest/developerguide/managing-users.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [GlobalSignOut](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/global-sign-out.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `initiate-auth`.

- **AWS CLI**
- 
            
                    **To sign in a user**The following `initiate-auth`example signs in a user with the basic username-password flow and no additional challenges.`aws cognito-idp initiate-auth \ --auth-flow``USER_PASSWORD_AUTH`\ --client-id`1example23456789`\ --analytics-metadata`AnalyticsEndpointId=d70b2ba36a8c4dc5a04a0451aEXAMPLE`\ --auth-parameters`USERNAME=testuser,PASSWORD=[Password]`--user-context-data`EncodedData=mycontextdata`--client-metadata`MyTestKey=MyTestValue`Output: `{ "AuthenticationResult": { "AccessToken": "eyJra456defEXAMPLE", "ExpiresIn": 3600, "TokenType": "Bearer", "RefreshToken": "eyJra123abcEXAMPLE", "IdToken": "eyJra789ghiEXAMPLE", "NewDeviceMetadata": { "DeviceKey": "us-west-2_a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "DeviceGroupKey": "-v7w9UcY6" } } }`For more information, see [Authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [InitiateAuth](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/initiate-auth.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-devices`.

- **AWS CLI**
- 
            
                    **To list a user's devices**The following `list-devices`example lists the devices that the current user has registered.`aws cognito-idp list-devices \ --access-token``eyJra456defEXAMPLE`Output: `{ "Devices": [ { "DeviceAttributes": [ { "Name": "device_status", "Value": "valid" }, { "Name": "device_name", "Value": "Dart-device" }, { "Name": "last_ip_used", "Value": "192.0.2.1" } ], "DeviceCreateDate": 1715100742.022, "DeviceKey": "us-west-2_a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "DeviceLastAuthenticatedDate": 1715100742.0, "DeviceLastModifiedDate": 1723233651.167 }, { "DeviceAttributes": [ { "Name": "device_status", "Value": "valid" }, { "Name": "last_ip_used", "Value": "192.0.2.2" } ], "DeviceCreateDate": 1726856147.993, "DeviceKey": "us-west-2_a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "DeviceLastAuthenticatedDate": 1726856147.0, "DeviceLastModifiedDate": 1726856147.993 } ] }`For more information, see [Working with devices](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [ListDevices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-devices.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-groups`.

- **AWS CLI**
- 
            
                    **To list the groups in a user pool**The following `list-groups`example lists the first two groups in the requested user pool.`aws cognito-idp list-groups \ --user-pool-id``us-west-2_EXAMPLE`\ --max-items`2`Output: `{ "Groups": [ { "CreationDate": 1681760899.633, "Description": "My test group", "GroupName": "testgroup", "LastModifiedDate": 1681760899.633, "Precedence": 1, "UserPoolId": "us-west-2_EXAMPLE" }, { "CreationDate": 1642632749.051, "Description": "Autogenerated group for users who sign in using Facebook", "GroupName": "us-west-2_EXAMPLE_Facebook", "LastModifiedDate": 1642632749.051, "UserPoolId": "us-west-2_EXAMPLE" } ], "NextToken": "[Pagination token]" }`For more information, see [Adding groups to a user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-user-groups.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [ListGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-identity-providers`.

- **AWS CLI**
- 
            
                    **To list identity providers**The following `list-identity-providers`example lists the first two identity providers in the requested user pool.`aws cognito-idp list-identity-providers \ --user-pool-id``us-west-2_EXAMPLE`\ --max-items`2`Output: `{ "Providers": [ { "CreationDate": 1619477386.504, "LastModifiedDate": 1703798328.142, "ProviderName": "Azure", "ProviderType": "SAML" }, { "CreationDate": 1642698776.175, "LastModifiedDate": 1642699086.453, "ProviderName": "LoginWithAmazon", "ProviderType": "LoginWithAmazon" } ], "NextToken": "[Pagination token]" }`For more information, see [Third-party IdP sign-in](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [ListIdentityProviders](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-identity-providers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-resource-servers`.

- **AWS CLI**
- 
            
                    **To list resource servers**The following `list-resource-servers`example lists the first two resource servers in the requested user pool.`aws cognito-idp list-resource-servers \ --user-pool-id``us-west-2_EXAMPLE`\ --max-results`2`Output: `{ "ResourceServers": [ { "Identifier": "myapi.example.com", "Name": "Example API with custom access control scopes", "Scopes": [ { "ScopeDescription": "International customers", "ScopeName": "international.read" }, { "ScopeDescription": "Domestic customers", "ScopeName": "domestic.read" } ], "UserPoolId": "us-west-2_EXAMPLE" }, { "Identifier": "myapi2.example.com", "Name": "Another example API for access control", "Scopes": [ { "ScopeDescription": "B2B customers", "ScopeName": "b2b.read" } ], "UserPoolId": "us-west-2_EXAMPLE" } ], "NextToken": "[Pagination token]" }`For more information, see [Access control with resource servers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-define-resource-servers.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [ListResourceServers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-resource-servers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list user pool tags**The following `list-tags-for-resource`example lists the tags assigned to the user pool with the requested ARN.`aws cognito-idp list-tags-for-resource \ --resource-arn``arn:aws:cognito-idp:us-west-2:123456789012:userpool/us-west-2_EXAMPLE`Output: `{ "Tags": { "administrator": "Jie", "tenant": "ExampleCorp" } }`For more information, see [Tagging Amazon Cognito resources](https://docs.aws.amazon.com/cognito/latest/developerguide/tagging.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-user-import-jobs`.

- **AWS CLI**
- 
            
                    **To list user import jobs and statuses**The following `list-user-import-jobs`example lists first three user import jobs and their details in the requested user pool.`aws cognito-idp list-user-import-jobs \ --user-pool-id``us-west-2_EXAMPLE`\ --max-results`3`Output: `{ "PaginationToken": "us-west-2_EXAMPLE#import-example3#1667948397084", "UserImportJobs": [ { "CloudWatchLogsRoleArn": "arn:aws:iam::123456789012:role/service-role/Cognito-UserImport-Role", "CompletionDate": 1735329786.142, "CompletionMessage": "The user import job has expired.", "CreationDate": 1735241621.022, "FailedUsers": 0, "ImportedUsers": 0, "JobId": "import-example1", "JobName": "Test-import-job-1", "PreSignedUrl": "https://aws-cognito-idp-user-import-pdx.s3.us-west-2.amazonaws.com/123456789012/us-west-2_EXAMPLE/import-mAgUtd8PMm?X-Amz-Security-Token=[token]&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20241226T193341Z&X-Amz-SignedHeaders=host%3Bx-amz-server-side-encryption&X-Amz-Expires=899&X-Amz-Credential=[credential]&X-Amz-Signature=[signature]", "SkippedUsers": 0, "Status": "Expired", "UserPoolId": "us-west-2_EXAMPLE" }, { "CloudWatchLogsRoleArn": "arn:aws:iam::123456789012:role/service-role/Cognito-UserImport-Role", "CompletionDate": 1681509058.408, "CompletionMessage": "Too many users have failed or been skipped during the import.", "CreationDate": 1681509001.477, "FailedUsers": 1, "ImportedUsers": 0, "JobId": "import-example2", "JobName": "Test-import-job-2", "PreSignedUrl": "https://aws-cognito-idp-user-import-pdx.s3.us-west-2.amazonaws.com/123456789012/us-west-2_EXAMPLE/import-mAgUtd8PMm?X-Amz-Security-Token=[token]&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20241226T193341Z&X-Amz-SignedHeaders=host%3Bx-amz-server-side-encryption&X-Amz-Expires=899&X-Amz-Credential=[credential]&X-Amz-Signature=[signature]", "SkippedUsers": 0, "StartDate": 1681509057.965, "Status": "Failed", "UserPoolId": "us-west-2_EXAMPLE" }, { "CloudWatchLogsRoleArn": "arn:aws:iam::123456789012:role/service-role/Cognito-UserImport-Role", "CompletionDate": 1.667864578676E9, "CompletionMessage": "Import Job Completed Successfully.", "CreationDate": 1.667864480281E9, "FailedUsers": 0, "ImportedUsers": 6, "JobId": "import-example3", "JobName": "Test-import-job-3", "PreSignedUrl": "https://aws-cognito-idp-user-import-pdx.s3.us-west-2.amazonaws.com/123456789012/us-west-2_EXAMPLE/import-mAgUtd8PMm?X-Amz-Security-Token=[token]&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20241226T193341Z&X-Amz-SignedHeaders=host%3Bx-amz-server-side-encryption&X-Amz-Expires=899&X-Amz-Credential=[credential]&X-Amz-Signature=[signature]", "SkippedUsers": 0, "StartDate": 1.667864578167E9, "Status": "Succeeded", "UserPoolId": "us-west-2_EXAMPLE" } ] }`For more information, see [Importing users from a CSV file](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-using-import-tool.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [ListUserImportJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-user-import-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-user-pool-clients`.

- **AWS CLI**
- 
            
                    **To list app clients**The following `list-user-pool-clients`example lists the first three app clients in the requested user pool.`aws cognito-idp list-user-pool-clients \ --user-pool-id``us-west-2_EXAMPLE`\ --max-results`3`Output: `{ "NextToken": "[Pagination token]", "UserPoolClients": [ { "ClientId": "1example23456789", "ClientName": "app-client-1", "UserPoolId": "us-west-2_EXAMPLE" }, { "ClientId": "2example34567890", "ClientName": "app-client-2", "UserPoolId": "us-west-2_EXAMPLE" }, { "ClientId": "3example45678901", "ClientName": "app-client-3", "UserPoolId": "us-west-2_EXAMPLE" } ] }`For more information, see [App clients](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-client-apps.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [ListUserPoolClients](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-user-pool-clients.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-user-pools`.

- **AWS CLI**
- 
            
                    **To list user pools**The following `list-user-pools`example lists 3 of the available user pools in the AWS account of the current CLI credentials.`aws cognito-idp list-user-pools \ --max-results``3`Output: `{ "NextToken": "[Pagination token]", "UserPools": [ { "CreationDate": 1681502497.741, "Id": "us-west-2_EXAMPLE1", "LambdaConfig": { "CustomMessage": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction", "PreSignUp": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction", "PreTokenGeneration": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction", "PreTokenGenerationConfig": { "LambdaArn": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction", "LambdaVersion": "V1_0" } }, "LastModifiedDate": 1681502497.741, "Name": "user pool 1" }, { "CreationDate": 1686064178.717, "Id": "us-west-2_EXAMPLE2", "LambdaConfig": { }, "LastModifiedDate": 1686064178.873, "Name": "user pool 2" }, { "CreationDate": 1627681712.237, "Id": "us-west-2_EXAMPLE3", "LambdaConfig": { "UserMigration": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction" }, "LastModifiedDate": 1678486942.479, "Name": "user pool 3" } ] }`For more information, see [Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [ListUserPools](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-user-pools.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-users-in-group`.

- **AWS CLI**
- 
            
                    **To list users in a group**This example lists users in group MyGroup. Command: `aws cognito-idp list-users-in-group --user-pool-id``us-west-2_aaaaaaaaa`--group-name`MyGroup`Output: `{ "Users": [ { "Username": "acf10624-80bb-401a-ac61-607bee2110ec", "Attributes": [ { "Name": "sub", "Value": "acf10624-80bb-401a-ac61-607bee2110ec" }, { "Name": "custom:CustomAttr1", "Value": "New Value!" }, { "Name": "email", "Value": "jane@example.com" } ], "UserCreateDate": 1548102770.284, "UserLastModifiedDate": 1548103204.893, "Enabled": true, "UserStatus": "CONFIRMED" }, { "Username": "22704aa3-fc10-479a-97eb-2af5806bd327", "Attributes": [ { "Name": "sub", "Value": "22704aa3-fc10-479a-97eb-2af5806bd327" }, { "Name": "email_verified", "Value": "true" }, { "Name": "email", "Value": "diego@example.com" } ], "UserCreateDate": 1548089817.683, "UserLastModifiedDate": 1548089817.683, "Enabled": true, "UserStatus": "FORCE_CHANGE_PASSWORD" } ] }`- 
                    For API details, see [ListUsersInGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-users-in-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-users`.

- **AWS CLI**
- 
            
                    **Example 1: To list users with a server-side filter**The following `list-users`example lists 3 users in the requested user pool whose email addresses begin with`testuser`.`aws cognito-idp list-users \ --user-pool-id``us-west-2_EXAMPLE`\ --filter email^=\"testuser\" \ --max-items`3`Output: `{ "PaginationToken": "efgh5678EXAMPLE", "Users": [ { "Attributes": [ { "Name": "sub", "Value": "eaad0219-2117-439f-8d46-4db20e59268f" }, { "Name": "email", "Value": "testuser@example.com" } ], "Enabled": true, "UserCreateDate": 1682955829.578, "UserLastModifiedDate": 1689030181.63, "UserStatus": "CONFIRMED", "Username": "testuser" }, { "Attributes": [ { "Name": "sub", "Value": "3b994cfd-0b07-4581-be46-3c82f9a70c90" }, { "Name": "email", "Value": "testuser2@example.com" } ], "Enabled": true, "UserCreateDate": 1684427979.201, "UserLastModifiedDate": 1684427979.201, "UserStatus": "UNCONFIRMED", "Username": "testuser2" }, { "Attributes": [ { "Name": "sub", "Value": "5929e0d1-4c34-42d1-9b79-a5ecacfe66f7" }, { "Name": "email", "Value": "testuser3@example.com" } ], "Enabled": true, "UserCreateDate": 1684427823.641, "UserLastModifiedDate": 1684427823.641, "UserStatus": "UNCONFIRMED", "Username": "testuser3@example.com" } ] }`For more information, see [Managing and searching for users](https://docs.aws.amazon.com/cognito/latest/developerguide/how-to-manage-user-accounts.html)in the*Amazon Cognito Developer Guide*.**Example 2: To list users with a client-side filter**The following `list-users`example lists the attributes of three users who have an attribute, in this case their email address, that contains the email domain "@example.com". If other attributes contained this string, they would also be displayed. The second user has no attributes that match the query and is excluded from the displayed output, but not from the server response.`aws cognito-idp list-users \ --user-pool-id``us-west-2_EXAMPLE`\ --max-items`3`--query Users\[\*\].Attributes\[\?Value\.contains\(\@\,\'@example.com\'\)\]Output: `[ [ { "Name": "email", "Value": "admin@example.com" } ], [], [ { "Name": "email", "Value": "operator@example.com" } ] ]`For more information, see [Managing and searching for users](https://docs.aws.amazon.com/cognito/latest/developerguide/how-to-manage-user-accounts.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [ListUsers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-users.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-web-authn-credentials`.

- **AWS CLI**
- 
            
                    **To list passkey credentials**The following `list-web-authn-credentials`example lists passkey, or WebAuthn, credentials for the current user. They have one registered device.`aws cognito-idp list-web-authn-credentials \ --access-token``eyJra456defEXAMPLE`Output: `{ "Credentials": [ { "AuthenticatorAttachment": "cross-platform", "CreatedAt": 1736293876.115, "CredentialId": "8LApgk4-lNUFHbhm2w6Und7-uxcc8coJGsPxiogvHoItc64xWQc3r4CEXAMPLE", "FriendlyCredentialName": "Roaming passkey", "RelyingPartyId": "auth.example.com" } ] }`For more information, see [Passkey sign-in](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-authentication-flow-methods.html#amazon-cognito-user-pools-authentication-flow-methods-passkey)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [ListWebAuthnCredentials](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/list-web-authn-credentials.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `resend-confirmation-code`.

- **AWS CLI**
- 
            
                    **To resend a confirmation code**The following `resend-confirmation-code`example sends a confirmation code to the user`jane`.`aws cognito-idp resend-confirmation-code \ --client-id``12a3b456c7de890f11g123hijk`\ --username`jane`Output: `{ "CodeDeliveryDetails": { "Destination": "j***@e***.com", "DeliveryMedium": "EMAIL", "AttributeName": "email" } }`For more information, see [Signing up and confirming user accounts](https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [ResendConfirmationCode](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/resend-confirmation-code.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `respond-to-auth-challenge`.

- **AWS CLI**
- 
            
                    **Example 1: To respond to a NEW_PASSWORD_REQUIRED challenge**The following `respond-to-auth-challenge`example responds to a NEW_PASSWORD_REQUIRED challenge that initiate-auth returned. It sets a password for the user`jane@example.com`.`aws cognito-idp respond-to-auth-challenge \ --client-id``1example23456789`\ --challenge-name`NEW_PASSWORD_REQUIRED`\ --challenge-responses`USERNAME=jane@example.com,NEW_PASSWORD=[Password]`\ --session`AYABeEv5HklEXAMPLE`Output: `{ "ChallengeParameters": {}, "AuthenticationResult": { "AccessToken": "ACCESS_TOKEN", "ExpiresIn": 3600, "TokenType": "Bearer", "RefreshToken": "REFRESH_TOKEN", "IdToken": "ID_TOKEN", "NewDeviceMetadata": { "DeviceKey": "us-west-2_a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "DeviceGroupKey": "-wt2ha1Zd" } } }`For more information, see [Authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication.html)in the*Amazon Cognito Developer Guide*.**Example 2: To respond to a SELECT_MFA_TYPE challenge**The following `respond-to-auth-challenge`example chooses TOTP MFA as the MFA option for the current user. The user was prompted to select an MFA type and will next be prompted to enter their MFA code.`aws cognito-idp respond-to-auth-challenge \ --client-id``1example23456789`--session`AYABeEv5HklEXAMPLE`--challenge-name`SELECT_MFA_TYPE`--challenge-responses`USERNAME=testuser,ANSWER=SOFTWARE_TOKEN_MFA`Output: `{ "ChallengeName": "SOFTWARE_TOKEN_MFA", "Session": "AYABeEv5HklEXAMPLE", "ChallengeParameters": { "FRIENDLY_DEVICE_NAME": "transparent" } }`For more information, see [Adding MFA](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html)in the*Amazon Cognito Developer Guide*.**Example 3: To respond to a SOFTWARE_TOKEN_MFA challenge**The following `respond-to-auth-challenge`example provides a TOTP MFA code and completes sign-in.`aws cognito-idp respond-to-auth-challenge \ --client-id``1example23456789`\ --session`AYABeEv5HklEXAMPLE`\ --challenge-name`SOFTWARE_TOKEN_MFA`\ --challenge-responses`USERNAME=testuser,SOFTWARE_TOKEN_MFA_CODE=123456`Output: `{ "AuthenticationResult": { "AccessToken": "eyJra456defEXAMPLE", "ExpiresIn": 3600, "TokenType": "Bearer", "RefreshToken": "eyJra123abcEXAMPLE", "IdToken": "eyJra789ghiEXAMPLE", "NewDeviceMetadata": { "DeviceKey": "us-west-2_a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "DeviceGroupKey": "-v7w9UcY6" } } }`For more information, see [Adding MFA](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [RespondToAuthChallenge](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/respond-to-auth-challenge.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `revoke-token`.

- **AWS CLI**
- 
            
                    **To revoke a refresh token**The following `revoke-token`revokes the requested refresh token and associated access tokens.`aws cognito-idp revoke-token \ --token``eyJjd123abcEXAMPLE`\ --client-id`1example23456789`This command produces no output. For more information, see [Revoking tokens](https://docs.aws.amazon.com/cognito/latest/developerguide/token-revocation.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [RevokeToken](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/revoke-token.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-log-delivery-configuration`.

- **AWS CLI**
- 
            
                    **To set up log export from a user pool**The following `set-log-delivery-configuration`example configures the requested user pool with user-notification error logging to a log group and user-authentication info logging to an S3 bucket.`aws cognito-idp set-log-delivery-configuration \ --user-pool-id``us-west-2_EXAMPLE`\ --log-configurations`LogLevel=ERROR,EventSource=userNotification,CloudWatchLogsConfiguration={LogGroupArn=arn:aws:logs:us-west-2:123456789012:log-group:cognito-exported}``LogLevel=INFO,EventSource=userAuthEvents,S3Configuration={BucketArn=arn:aws:s3:::amzn-s3-demo-bucket1}`Output: `{ "LogDeliveryConfiguration": { "LogConfigurations": [ { "CloudWatchLogsConfiguration": { "LogGroupArn": "arn:aws:logs:us-west-2:123456789012:log-group:cognito-exported" }, "EventSource": "userNotification", "LogLevel": "ERROR" }, { "EventSource": "userAuthEvents", "LogLevel": "INFO", "S3Configuration": { "BucketArn": "arn:aws:s3:::amzn-s3-demo-bucket1" } } ], "UserPoolId": "us-west-2_EXAMPLE" } }`For more information, see [Exporting user pool logs](https://docs.aws.amazon.com/cognito/latest/developerguide/exporting-quotas-and-usage.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [SetLogDeliveryConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/set-log-delivery-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-risk-configuration`.

- **AWS CLI**
- 
            
                    **To set the threat protection risk configuration**The following `set-risk-configuration`example configures threat protection messages and actions, compromised credentials, and IP address exceptions in the requested app client. Because of the complexity of the NotifyConfiguration object, JSON input is a best practice for this command.`aws cognito-idp set-risk-configuration \ --cli-input-json``file://set-risk-configuration.json`Contents of `set-risk-configuration.json`:`{ "AccountTakeoverRiskConfiguration": { "Actions": { "HighAction": { "EventAction": "MFA_REQUIRED", "Notify": true }, "LowAction": { "EventAction": "NO_ACTION", "Notify": true }, "MediumAction": { "EventAction": "MFA_IF_CONFIGURED", "Notify": true } }, "NotifyConfiguration": { "BlockEmail": { "HtmlBody": "<!DOCTYPE html>\n<html>\n<head>\n\t<title>HTML email context</title>\n\t<meta charset=\"utf-8\">\n</head>\n<body>\n<pre>We blocked an unrecognized sign-in to your account with this information:\n<ul>\n<li>Time: {login-time}</li>\n<li>Device: {device-name}</li>\n<li>Location: {city}, {country}</li>\n</ul>\nIf this sign-in was not by you, you should change your password and notify us by clicking on <a href={one-click-link-invalid}>this link</a>\nIf this sign-in was by you, you can follow <a href={one-click-link-valid}>this link</a> to let us know</pre>\n</body>\n</html>", "Subject": "Blocked sign-in attempt", "TextBody": "We blocked an unrecognized sign-in to your account with this information:\nTime: {login-time}\nDevice: {device-name}\nLocation: {city}, {country}\nIf this sign-in was not by you, you should change your password and notify us by clicking on {one-click-link-invalid}\nIf this sign-in was by you, you can follow {one-click-link-valid} to let us know" }, "From": "admin@example.com", "MfaEmail": { "HtmlBody": "<!DOCTYPE html>\n<html>\n<head>\n\t<title>HTML email context</title>\n\t<meta charset=\"utf-8\">\n</head>\n<body>\n<pre>We required you to use multi-factor authentication for the following sign-in attempt:\n<ul>\n<li>Time: {login-time}</li>\n<li>Device: {device-name}</li>\n<li>Location: {city}, {country}</li>\n</ul>\nIf this sign-in was not by you, you should change your password and notify us by clicking on <a href={one-click-link-invalid}>this link</a>\nIf this sign-in was by you, you can follow <a href={one-click-link-valid}>this link</a> to let us know</pre>\n</body>\n</html>", "Subject": "New sign-in attempt", "TextBody": "We required you to use multi-factor authentication for the following sign-in attempt:\nTime: {login-time}\nDevice: {device-name}\nLocation: {city}, {country}\nIf this sign-in was not by you, you should change your password and notify us by clicking on {one-click-link-invalid}\nIf this sign-in was by you, you can follow {one-click-link-valid} to let us know" }, "NoActionEmail": { "HtmlBody": "<!DOCTYPE html>\n<html>\n<head>\n\t<title>HTML email context</title>\n\t<meta charset=\"utf-8\">\n</head>\n<body>\n<pre>We observed an unrecognized sign-in to your account with this information:\n<ul>\n<li>Time: {login-time}</li>\n<li>Device: {device-name}</li>\n<li>Location: {city}, {country}</li>\n</ul>\nIf this sign-in was not by you, you should change your password and notify us by clicking on <a href={one-click-link-invalid}>this link</a>\nIf this sign-in was by you, you can follow <a href={one-click-link-valid}>this link</a> to let us know</pre>\n</body>\n</html>", "Subject": "New sign-in attempt", "TextBody": "We observed an unrecognized sign-in to your account with this information:\nTime: {login-time}\nDevice: {device-name}\nLocation: {city}, {country}\nIf this sign-in was not by you, you should change your password and notify us by clicking on {one-click-link-invalid}\nIf this sign-in was by you, you can follow {one-click-link-valid} to let us know" }, "ReplyTo": "admin@example.com", "SourceArn": "arn:aws:ses:us-west-2:123456789012:identity/admin@example.com" } }, "ClientId": "1example23456789", "CompromisedCredentialsRiskConfiguration": { "Actions": { "EventAction": "BLOCK" }, "EventFilter": [ "PASSWORD_CHANGE", "SIGN_UP", "SIGN_IN" ] }, "RiskExceptionConfiguration": { "BlockedIPRangeList": [ "192.0.2.1/32", "192.0.2.2/32" ], "SkippedIPRangeList": [ "203.0.113.1/32", "203.0.113.2/32" ] }, "UserPoolId": "us-west-2_EXAMPLE" }`Output: `{ "RiskConfiguration": { "AccountTakeoverRiskConfiguration": { "Actions": { "HighAction": { "EventAction": "MFA_REQUIRED", "Notify": true }, "LowAction": { "EventAction": "NO_ACTION", "Notify": true }, "MediumAction": { "EventAction": "MFA_IF_CONFIGURED", "Notify": true } }, "NotifyConfiguration": { "BlockEmail": { "HtmlBody": "<!DOCTYPE html>\n<html>\n<head>\n\t<title>HTML email context</title>\n\t<meta charset=\"utf-8\">\n</head>\n<body>\n<pre>We blocked an unrecognized sign-in to your account with this information:\n<ul>\n<li>Time: {login-time}</li>\n<li>Device: {device-name}</li>\n<li>Location: {city}, {country}</li>\n</ul>\nIf this sign-in was not by you, you should change your password and notify us by clicking on <a href={one-click-link-invalid}>this link</a>\nIf this sign-in was by you, you can follow <a href={one-click-link-valid}>this link</a> to let us know</pre>\n</body>\n</html>", "Subject": "Blocked sign-in attempt", "TextBody": "We blocked an unrecognized sign-in to your account with this information:\nTime: {login-time}\nDevice: {device-name}\nLocation: {city}, {country}\nIf this sign-in was not by you, you should change your password and notify us by clicking on {one-click-link-invalid}\nIf this sign-in was by you, you can follow {one-click-link-valid} to let us know" }, "From": "admin@example.com", "MfaEmail": { "HtmlBody": "<!DOCTYPE html>\n<html>\n<head>\n\t<title>HTML email context</title>\n\t<meta charset=\"utf-8\">\n</head>\n<body>\n<pre>We required you to use multi-factor authentication for the following sign-in attempt:\n<ul>\n<li>Time: {login-time}</li>\n<li>Device: {device-name}</li>\n<li>Location: {city}, {country}</li>\n</ul>\nIf this sign-in was not by you, you should change your password and notify us by clicking on <a href={one-click-link-invalid}>this link</a>\nIf this sign-in was by you, you can follow <a href={one-click-link-valid}>this link</a> to let us know</pre>\n</body>\n</html>", "Subject": "New sign-in attempt", "TextBody": "We required you to use multi-factor authentication for the following sign-in attempt:\nTime: {login-time}\nDevice: {device-name}\nLocation: {city}, {country}\nIf this sign-in was not by you, you should change your password and notify us by clicking on {one-click-link-invalid}\nIf this sign-in was by you, you can follow {one-click-link-valid} to let us know" }, "NoActionEmail": { "HtmlBody": "<!DOCTYPE html>\n<html>\n<head>\n\t<title>HTML email context</title>\n\t<meta charset=\"utf-8\">\n</head>\n<body>\n<pre>We observed an unrecognized sign-in to your account with this information:\n<ul>\n<li>Time: {login-time}</li>\n<li>Device: {device-name}</li>\n<li>Location: {city}, {country}</li>\n</ul>\nIf this sign-in was not by you, you should change your password and notify us by clicking on <a href={one-click-link-invalid}>this link</a>\nIf this sign-in was by you, you can follow <a href={one-click-link-valid}>this link</a> to let us know</pre>\n</body>\n</html>", "Subject": "New sign-in attempt", "TextBody": "We observed an unrecognized sign-in to your account with this information:\nTime: {login-time}\nDevice: {device-name}\nLocation: {city}, {country}\nIf this sign-in was not by you, you should change your password and notify us by clicking on {one-click-link-invalid}\nIf this sign-in was by you, you can follow {one-click-link-valid} to let us know" }, "ReplyTo": "admin@example.com", "SourceArn": "arn:aws:ses:us-west-2:123456789012:identity/admin@example.com" } }, "ClientId": "1example23456789", "CompromisedCredentialsRiskConfiguration": { "Actions": { "EventAction": "BLOCK" }, "EventFilter": [ "PASSWORD_CHANGE", "SIGN_UP", "SIGN_IN" ] }, "RiskExceptionConfiguration": { "BlockedIPRangeList": [ "192.0.2.1/32", "192.0.2.2/32" ], "SkippedIPRangeList": [ "203.0.113.1/32", "203.0.113.2/32" ] }, "UserPoolId": "us-west-2_EXAMPLE" } }`For more information, see [Threat protection](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-threat-protection.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [SetRiskConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/set-risk-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-ui-customization`.

- **AWS CLI**
- 
            
                    **Example 1: To customize the classic hosted UI for an app client**The following `set-ui-customization`example configures the requested app client with some custom CSS and with the Amazon Cognito logo as the application logo.`aws cognito-idp set-ui-customization \ --user-pool-id``us-west-2_ywDJHlIfU`\ --client-id`14pq32c5q2uq2q7keorloqvb23`\ --css`".logo-customizable {\n\tmax-width: 60%;\n\tmax-height: 30%;\n}\n.banner-customizable {\n\tpadding: 25px 0px 25px 0px;\n\tbackground-color: lightgray;\n}\n.label-customizable {\n\tfont-weight: 400;\n}\n.textDescription-customizable {\n\tpadding-top: 10px;\n\tpadding-bottom: 10px;\n\tdisplay: block;\n\tfont-size: 16px;\n}\n.idpDescription-customizable {\n\tpadding-top: 10px;\n\tpadding-bottom: 10px;\n\tdisplay: block;\n\tfont-size: 16px;\n}\n.legalText-customizable {\n\tcolor: #747474;\n\tfont-size: 11px;\n}\n.submitButton-customizable {\n\tfont-size: 11px;\n\tfont-weight: normal;\n\tmargin: 20px -15px 10px -13px;\n\theight: 40px;\n\twidth: 108%;\n\tcolor: #fff;\n\tbackground-color: #337ab7;\n\ttext-align: center;\n}\n.submitButton-customizable:hover {\n\tcolor: #fff;\n\tbackground-color: #286090;\n}\n.errorMessage-customizable {\n\tpadding: 5px;\n\tfont-size: 14px;\n\twidth: 100%;\n\tbackground: #F5F5F5;\n\tborder: 2px solid #D64958;\n\tcolor: #D64958;\n}\n.inputField-customizable {\n\twidth: 100%;\n\theight: 34px;\n\tcolor: #555;\n\tbackground-color: #fff;\n\tborder: 1px solid #ccc;\n\tborder-radius: 0px;\n}\n.inputField-customizable:focus {\n\tborder-color: #66afe9;\n\toutline: 0;\n}\n.idpButton-customizable {\n\theight: 40px;\n\twidth: 100%;\n\twidth: 100%;\n\ttext-align: center;\n\tmargin-bottom: 15px;\n\tcolor: #fff;\n\tbackground-color: #5bc0de;\n\tborder-color: #46b8da;\n}\n.idpButton-customizable:hover {\n\tcolor: #fff;\n\tbackground-color: #31b0d5;\n}\n.socialButton-customizable {\n\tborder-radius: 2px;\n\theight: 40px;\n\tmargin-bottom: 15px;\n\tpadding: 1px;\n\ttext-align: left;\n\twidth: 100%;\n}\n.redirect-customizable {\n\ttext-align: center;\n}\n.passwordCheck-notValid-customizable {\n\tcolor: #DF3312;\n}\n.passwordCheck-valid-customizable {\n\tcolor: #19BF00;\n}\n.background-customizable {\n\tbackground-color: #fff;\n}\n"`\ --image-file`iVBORw0KGgoAAAANSUhEUgAAAFAAAABQCAMAAAC5zwKfAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAA2UExURd00TN9BV/Cmsfvm6f3y9P////fM0uqAj+yNmu6ZpvnZ3eNabuFNYuZneehzhPKzvPTAxwAAAOiMMlkAAAASdFJOU///////////////////////AOK/vxIAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAKDSURBVFhH7ZfpkoMgEISDHKuEw/d/2u2BQWMiBrG29o+fVsKatdPMAeZxc3Nz8w+ISekzmB++sYIw/I/tjHzrPpO2Tx62EbR2PNxFac+jVuKxRaV50IzXkUe76NOCoUuwlvnQKei02gNF0ykotOLRBq/nboeWRxAISx2EbsHFoRhK6Igk2JJlwScfQjgt06dOaWWiTbEDAe/iq8N9kqCw2uCbHkHlYkaXEF8EYeL9RDqT4FhC6XMIIEifdcUwCc4leNyhabadWU6OlKYJE1Oac3NSPhB5rlaXlSgmr/1lww4nPaU/1ylfLGxX1r6Y66ZZkCqvnOlqKWws59ELj7fULc2CubwySYkdDuuiY0/F0L6Q5pZiSG0SfZTSTCOUhxOCH1AdIoCpTTIjtd+VpEjUDDytQH/0Fpc661Aisas/4qmyUItD557pSCOSQQzlx27J+meyDGc5zZgfhWuXE1lGgmVOMwmWdeGdzhjqZV14x5vSj7vsC5JDz/Cl0Vhp56n2NQt1wQIpury1EPbwyaYm+IhmAQKoajkH51wg4cMZ1wQ3QG9efKWWOaDhYWnU6jXjCMdRmm21PArI+Pb5DYoH93hq0ZCPlxeGJho/DI15C6sQc/L2sTC47UFBKZGHT6k+zlXg7WebA0Nr0HTcLMfk/Y4Rc65D3iG6WDd7YLSlVqk87bVhUwhnClrx11RsVQwlAA818Mn+QEs71BhSFU6orsUfKhHp72XMGYXi4q9c64RXRvzkWurRfG2vI2be/VaNcNgpX0Evb/vio7nPMmj5qujkpQgSaPd1UcVqciHFDNZpOcGlcOPyi+AamCbIL9fitxAGeFN2Dl+3vZubm5u/4fH4Bd14HhIPdwZPAAAAAElFTkSuQmCC`Output: `{ "UICustomization": { "UserPoolId": "us-west-2_ywDJHlIfU", "ClientId": "14pq32c5q2uq2q7keorloqvb23", "ImageUrl": "https://cf.thewrong.club/14pq32c5q2uq2q7keorloqvb23/20250117005911/assets/images/image.jpg", "CSS": ".logo-customizable {\n\tmax-width: 60%;\n\tmax-height: 30%;\n}\n.banner-customizable {\n\tpadding: 25px 0px 25px 0px;\n\tbackground-color: lightgray;\n}\n.label-customizable {\n\tfont-weight: 400;\n}\n.textDescription-customizable {\n\tpadding-top: 10px;\n\tpadding-bottom: 10px;\n\tdisplay: block;\n\tfont-size: 16px;\n}\n.idpDescription-customizable {\n\tpadding-top: 10px;\n\tpadding-bottom: 10px;\n\tdisplay: block;\n\tfont-size: 16px;\n}\n.legalText-customizable {\n\tcolor: #747474;\n\tfont-size: 11px;\n}\n.submitButton-customizable {\n\tfont-size: 11px;\n\tfont-weight: normal;\n\tmargin: 20px -15px 10px -13px;\n\theight: 40px;\n\twidth: 108%;\n\tcolor: #fff;\n\tbackground-color: #337ab7;\n\ttext-align: center;\n}\n.submitButton-customizable:hover {\n\tcolor: #fff;\n\tbackground-color: #286090;\n}\n.errorMessage-customizable {\n\tpadding: 5px;\n\tfont-size: 14px;\n\twidth: 100%;\n\tbackground: #F5F5F5;\n\tborder: 2px solid #D64958;\n\tcolor: #D64958;\n}\n.inputField-customizable {\n\twidth: 100%;\n\theight: 34px;\n\tcolor: #555;\n\tbackground-color: #fff;\n\tborder: 1px solid #ccc;\n\tborder-radius: 0px;\n}\n.inputField-customizable:focus {\n\tborder-color: #66afe9;\n\toutline: 0;\n}\n.idpButton-customizable {\n\theight: 40px;\n\twidth: 100%;\n\twidth: 100%;\n\ttext-align: center;\n\tmargin-bottom: 15px;\n\tcolor: #fff;\n\tbackground-color: #5bc0de;\n\tborder-color: #46b8da;\n}\n.idpButton-customizable:hover {\n\tcolor: #fff;\n\tbackground-color: #31b0d5;\n}\n.socialButton-customizable {\n\tborder-radius: 2px;\n\theight: 40px;\n\tmargin-bottom: 15px;\n\tpadding: 1px;\n\ttext-align: left;\n\twidth: 100%;\n}\n.redirect-customizable {\n\ttext-align: center;\n}\n.passwordCheck-notValid-customizable {\n\tcolor: #DF3312;\n}\n.passwordCheck-valid-customizable {\n\tcolor: #19BF00;\n}\n.background-customizable {\n\tbackground-color: #fff;\n}\n", "CSSVersion": "20250117005911" } }`**Example 2: To set the default UI customization for all app clients**The following `set-ui-customization`example configures the requested user pool for all app clients that don't have a client-specific configuration. The command applies some custom CSS and with the Amazon Cognito logo as the application logo.`aws cognito-idp set-ui-customization \ --user-pool-id``us-west-2_ywDJHlIfU`\ --client-id`ALL`\ --css`".logo-customizable {\n\tmax-width: 60%;\n\tmax-height: 30%;\n}\n.banner-customizable {\n\tpadding: 25px 0px 25px 0px;\n\tbackground-color: lightgray;\n}\n.label-customizable {\n\tfont-weight: 400;\n}\n.textDescription-customizable {\n\tpadding-top: 10px;\n\tpadding-bottom: 10px;\n\tdisplay: block;\n\tfont-size: 16px;\n}\n.idpDescription-customizable {\n\tpadding-top: 10px;\n\tpadding-bottom: 10px;\n\tdisplay: block;\n\tfont-size: 16px;\n}\n.legalText-customizable {\n\tcolor: #747474;\n\tfont-size: 11px;\n}\n.submitButton-customizable {\n\tfont-size: 11px;\n\tfont-weight: normal;\n\tmargin: 20px -15px 10px -13px;\n\theight: 40px;\n\twidth: 108%;\n\tcolor: #fff;\n\tbackground-color: #337ab7;\n\ttext-align: center;\n}\n.submitButton-customizable:hover {\n\tcolor: #fff;\n\tbackground-color: #286090;\n}\n.errorMessage-customizable {\n\tpadding: 5px;\n\tfont-size: 14px;\n\twidth: 100%;\n\tbackground: #F5F5F5;\n\tborder: 2px solid #D64958;\n\tcolor: #D64958;\n}\n.inputField-customizable {\n\twidth: 100%;\n\theight: 34px;\n\tcolor: #555;\n\tbackground-color: #fff;\n\tborder: 1px solid #ccc;\n\tborder-radius: 0px;\n}\n.inputField-customizable:focus {\n\tborder-color: #66afe9;\n\toutline: 0;\n}\n.idpButton-customizable {\n\theight: 40px;\n\twidth: 100%;\n\twidth: 100%;\n\ttext-align: center;\n\tmargin-bottom: 15px;\n\tcolor: #fff;\n\tbackground-color: #5bc0de;\n\tborder-color: #46b8da;\n}\n.idpButton-customizable:hover {\n\tcolor: #fff;\n\tbackground-color: #31b0d5;\n}\n.socialButton-customizable {\n\tborder-radius: 2px;\n\theight: 40px;\n\tmargin-bottom: 15px;\n\tpadding: 1px;\n\ttext-align: left;\n\twidth: 100%;\n}\n.redirect-customizable {\n\ttext-align: center;\n}\n.passwordCheck-notValid-customizable {\n\tcolor: #DF3312;\n}\n.passwordCheck-valid-customizable {\n\tcolor: #19BF00;\n}\n.background-customizable {\n\tbackground-color: #fff;\n}\n"`\ --image-file`iVBORw0KGgoAAAANSUhEUgAAAFAAAABQCAMAAAC5zwKfAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAA2UExURd00TN9BV/Cmsfvm6f3y9P////fM0uqAj+yNmu6ZpvnZ3eNabuFNYuZneehzhPKzvPTAxwAAAOiMMlkAAAASdFJOU///////////////////////AOK/vxIAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAKDSURBVFhH7ZfpkoMgEISDHKuEw/d/2u2BQWMiBrG29o+fVsKatdPMAeZxc3Nz8w+ISekzmB++sYIw/I/tjHzrPpO2Tx62EbR2PNxFac+jVuKxRaV50IzXkUe76NOCoUuwlvnQKei02gNF0ykotOLRBq/nboeWRxAISx2EbsHFoRhK6Igk2JJlwScfQjgt06dOaWWiTbEDAe/iq8N9kqCw2uCbHkHlYkaXEF8EYeL9RDqT4FhC6XMIIEifdcUwCc4leNyhabadWU6OlKYJE1Oac3NSPhB5rlaXlSgmr/1lww4nPaU/1ylfLGxX1r6Y66ZZkCqvnOlqKWws59ELj7fULc2CubwySYkdDuuiY0/F0L6Q5pZiSG0SfZTSTCOUhxOCH1AdIoCpTTIjtd+VpEjUDDytQH/0Fpc661Aisas/4qmyUItD557pSCOSQQzlx27J+meyDGc5zZgfhWuXE1lGgmVOMwmWdeGdzhjqZV14x5vSj7vsC5JDz/Cl0Vhp56n2NQt1wQIpury1EPbwyaYm+IhmAQKoajkH51wg4cMZ1wQ3QG9efKWWOaDhYWnU6jXjCMdRmm21PArI+Pb5DYoH93hq0ZCPlxeGJho/DI15C6sQc/L2sTC47UFBKZGHT6k+zlXg7WebA0Nr0HTcLMfk/Y4Rc65D3iG6WDd7YLSlVqk87bVhUwhnClrx11RsVQwlAA818Mn+QEs71BhSFU6orsUfKhHp72XMGYXi4q9c64RXRvzkWurRfG2vI2be/VaNcNgpX0Evb/vio7nPMmj5qujkpQgSaPd1UcVqciHFDNZpOcGlcOPyi+AamCbIL9fitxAGeFN2Dl+3vZubm5u/4fH4Bd14HhIPdwZPAAAAAElFTkSuQmCC`Output: `{ "UICustomization": { "UserPoolId": "us-west-2_ywDJHlIfU", "ClientId": "14pq32c5q2uq2q7keorloqvb23", "ImageUrl": "https://cf.thewrong.club/14pq32c5q2uq2q7keorloqvb23/20250117005911/assets/images/image.jpg", "CSS": ".logo-customizable {\n\tmax-width: 60%;\n\tmax-height: 30%;\n}\n.banner-customizable {\n\tpadding: 25px 0px 25px 0px;\n\tbackground-color: lightgray;\n}\n.label-customizable {\n\tfont-weight: 400;\n}\n.textDescription-customizable {\n\tpadding-top: 10px;\n\tpadding-bottom: 10px;\n\tdisplay: block;\n\tfont-size: 16px;\n}\n.idpDescription-customizable {\n\tpadding-top: 10px;\n\tpadding-bottom: 10px;\n\tdisplay: block;\n\tfont-size: 16px;\n}\n.legalText-customizable {\n\tcolor: #747474;\n\tfont-size: 11px;\n}\n.submitButton-customizable {\n\tfont-size: 11px;\n\tfont-weight: normal;\n\tmargin: 20px -15px 10px -13px;\n\theight: 40px;\n\twidth: 108%;\n\tcolor: #fff;\n\tbackground-color: #337ab7;\n\ttext-align: center;\n}\n.submitButton-customizable:hover {\n\tcolor: #fff;\n\tbackground-color: #286090;\n}\n.errorMessage-customizable {\n\tpadding: 5px;\n\tfont-size: 14px;\n\twidth: 100%;\n\tbackground: #F5F5F5;\n\tborder: 2px solid #D64958;\n\tcolor: #D64958;\n}\n.inputField-customizable {\n\twidth: 100%;\n\theight: 34px;\n\tcolor: #555;\n\tbackground-color: #fff;\n\tborder: 1px solid #ccc;\n\tborder-radius: 0px;\n}\n.inputField-customizable:focus {\n\tborder-color: #66afe9;\n\toutline: 0;\n}\n.idpButton-customizable {\n\theight: 40px;\n\twidth: 100%;\n\twidth: 100%;\n\ttext-align: center;\n\tmargin-bottom: 15px;\n\tcolor: #fff;\n\tbackground-color: #5bc0de;\n\tborder-color: #46b8da;\n}\n.idpButton-customizable:hover {\n\tcolor: #fff;\n\tbackground-color: #31b0d5;\n}\n.socialButton-customizable {\n\tborder-radius: 2px;\n\theight: 40px;\n\tmargin-bottom: 15px;\n\tpadding: 1px;\n\ttext-align: left;\n\twidth: 100%;\n}\n.redirect-customizable {\n\ttext-align: center;\n}\n.passwordCheck-notValid-customizable {\n\tcolor: #DF3312;\n}\n.passwordCheck-valid-customizable {\n\tcolor: #19BF00;\n}\n.background-customizable {\n\tbackground-color: #fff;\n}\n", "CSSVersion": "20250117005911" } }`For more information, see [Hosted UI (classic) branding](https://docs.aws.amazon.com/cognito/latest/developerguide/hosted-ui-classic-branding.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [SetUiCustomization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/set-ui-customization.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-user-mfa-preference`.

- **AWS CLI**
- 
            
                    **To set a user's MFA preference**The following `set-user-mfa-preference`example configures the current user to use TOTP MFA and disables all other MFA factors.`aws cognito-idp set-user-mfa-preference \ --access-token``eyJra456defEXAMPLE`\ --software-token-mfa-settings`Enabled=true,PreferredMfa=true`\ --sms-mfa-settings`Enabled=false,PreferredMfa=false`\ --email-mfa-settings`Enabled=false,PreferredMfa=false`This command produces no output. For more information, see [Adding MFA](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [SetUserMfaPreference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/set-user-mfa-preference.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-user-pool-mfa-config`.

- **AWS CLI**
- 
            
                    **To configure user pool MFA and WebAuthn**The following `set-user-pool-mfa-config`example configures the requested user pool with optional MFA with all available MFA methods, and sets the WebAuthn configuration.`aws cognito-idp set-user-pool-mfa-config \ --user-pool-id``us-west-2_EXAMPLE`\ --sms-mfa-configuration "SmsAuthenticationMessage=\"Your OTP for MFA or sign-in: use {####}.\",SmsConfiguration={SnsCallerArn=arn:aws:iam::123456789012:role/service-role/test-SMS-Role,ExternalId=a1b2c3d4-5678-90ab-cdef-EXAMPLE11111,SnsRegion=us-west-2}" \ --software-token-mfa-configuration`Enabled=true`\ --email-mfa-configuration "Message=\"Your OTP for MFA or sign-in: use {####}\",Subject=\"OTP test\"" \ --mfa-configuration`OPTIONAL`\ --web-authn-configuration`RelyingPartyId=auth.example.com,UserVerification=preferred`Output: `{ "EmailMfaConfiguration": { "Message": "Your OTP for MFA or sign-in: use {####}", "Subject": "OTP test" }, "MfaConfiguration": "OPTIONAL", "SmsMfaConfiguration": { "SmsAuthenticationMessage": "Your OTP for MFA or sign-in: use {####}.", "SmsConfiguration": { "ExternalId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "SnsCallerArn": "arn:aws:iam::123456789012:role/service-role/test-SMS-Role", "SnsRegion": "us-west-2" } }, "SoftwareTokenMfaConfiguration": { "Enabled": true }, "WebAuthnConfiguration": { "RelyingPartyId": "auth.example.com", "UserVerification": "preferred" } }`For more information, see [Adding MFA](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html)and[Passkey sign-in](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-authentication-flow-methods.html#amazon-cognito-user-pools-authentication-flow-methods-passkey)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [SetUserPoolMfaConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/set-user-pool-mfa-config.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-user-settings`.

- **AWS CLI**
- 
            
                    **To set user settings**This example sets the MFA delivery preference to EMAIL. Command: `aws cognito-idp set-user-settings --access-token``ACCESS_TOKEN`--mfa-options`DeliveryMedium=EMAIL`- 
                    For API details, see [SetUserSettings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/set-user-settings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `sign-up`.

- **AWS CLI**
- 
            
                    **To sign up a user**This example signs up jane@example.com. Command: `aws cognito-idp sign-up --client-id``3n4b5urk1ft4fl3mg5e62d9ado`--username`jane@example.com`--password`PASSWORD`--user-attributes Name="email",Value="jane@example.com" Name="name",Value="Jane"Output: `{ "UserConfirmed": false, "UserSub": "e04d60a6-45dc-441c-a40b-e25a787d4862" }`- 
                    For API details, see [SignUp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/sign-up.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-user-import-job`.

- **AWS CLI**
- 
            
                    **To start an import job**The following `start-user-import-job`example starts the requested import job in the requested user pool.`aws cognito-idp start-user-import-job \ --user-pool-id``us-west-2_EXAMPLE`\ --job-id`import-mAgUtd8PMm`Output: `{ "UserImportJob": { "CloudWatchLogsRoleArn": "arn:aws:iam::123456789012:role/example-cloudwatch-logs-role", "CreationDate": 1736442975.904, "FailedUsers": 0, "ImportedUsers": 0, "JobId": "import-mAgUtd8PMm", "JobName": "Customer import", "PreSignedUrl": "https://aws-cognito-idp-user-import-pdx.s3.us-west-2.amazonaws.com/123456789012/us-west-2_EXAMPLE/import-mAgUtd8PMm?X-Amz-Security-Token=[token]&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20241226T193341Z&X-Amz-SignedHeaders=host%3Bx-amz-server-side-encryption&X-Amz-Expires=899&X-Amz-Credential=[credential]&X-Amz-Signature=[signature]", "SkippedUsers": 0, "StartDate": 1736443020.081, "Status": "Pending", "UserPoolId": "us-west-2_EXAMPLE" } }`For more information, see [Importing users into a user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-using-import-tool.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [StartUserImportJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/start-user-import-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-web-authn-registration`.

- **AWS CLI**
- 
            
                    **To get passkey registration information for a signed-in user**The following `start-web-authn-registration`example generates WebAuthn registration options for the current user.`aws cognito-idp start-web-authn-registration \ --access-token``eyJra456defEXAMPLE`Output: `{ "CredentialCreationOptions": { "authenticatorSelection": { "requireResidentKey": true, "residentKey": "required", "userVerification": "preferred" }, "challenge": "wxvbDicyqQqvF2EXAMPLE", "excludeCredentials": [ { "id": "8LApgk4-lNUFHbhm2w6Und7-uxcc8coJGsPxiogvHoItc64xWQc3r4CEXAMPLE", "type": "public-key" } ], "pubKeyCredParams": [ { "alg": -7, "type": "public-key" }, { "alg": -257, "type": "public-key" } ], "rp": { "id": "auth.example.com", "name": "auth.example.com" }, "timeout": 60000, "user": { "displayName": "testuser", "id": "ZWFhZDAyMTktMjExNy00MzlmLThkNDYtNGRiMjBlNEXAMPLE", "name": "testuser" } } }`For more information, see [Passkey sign-in](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-authentication-flow-methods.html#amazon-cognito-user-pools-authentication-flow-methods-passkey)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [StartWebAuthnRegistration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/start-web-authn-registration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-user-import-job`.

- **AWS CLI**
- 
            
                    **To stop an import job**The following `stop-user-import-job`example stops the requested running user import job in the requested user pool.`aws cognito-idp stop-user-import-job \ --user-pool-id``us-west-2_EXAMPLE`\ --job-id`import-mAgUtd8PMm`Output: `{ "UserImportJob": { "CloudWatchLogsRoleArn": "arn:aws:iam::123456789012:role/example-cloudwatch-logs-role", "CompletionDate": 1736443496.379, "CompletionMessage": "The Import Job was stopped by the developer.", "CreationDate": 1736443471.781, "FailedUsers": 0, "ImportedUsers": 0, "JobId": "import-mAgUtd8PMm", "JobName": "Customer import", "PreSignedUrl": "https://aws-cognito-idp-user-import-pdx.s3.us-west-2.amazonaws.com/123456789012/us-west-2_EXAMPLE/import-mAgUtd8PMm?X-Amz-Security-Token=[token]&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20241226T193341Z&X-Amz-SignedHeaders=host%3Bx-amz-server-side-encryption&X-Amz-Expires=899&X-Amz-Credential=[credential]&X-Amz-Signature=[signature]", "SkippedUsers": 0, "StartDate": 1736443494.154, "Status": "Stopped", "UserPoolId": "us-west-2_EXAMPLE" } }`For more information, see [Importing users into a user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-using-import-tool.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [StopUserImportJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/stop-user-import-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To tag a user pool**The following `tag-resource`example applies`administrator`and`department`tags to the requested user pool.`aws cognito-idp tag-resource \ --resource-arn``arn:aws:cognito-idp:us-west-2:123456789012:userpool/us-west-2_EXAMPLE`\ --tags`administrator=Jie,tenant=ExampleCorp`This command produces no output. For more information, see [Tagging Amazon Cognito resources](https://docs.aws.amazon.com/cognito/latest/developerguide/tagging.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove tags from a user pool**The following `untag-resource`example removes`administrator`and`department`tags from the requested user pool.`aws cognito-idp untag-resource \ --resource-arn``arn:aws:cognito-idp:us-west-2:767671399759:userpool/us-west-2_l5cxwdm2K`\ --tag-keys`administrator``tenant`This command produces no output. For more information, see [Tagging Amazon Cognito resources](https://docs.aws.amazon.com/cognito/latest/developerguide/tagging.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-auth-event-feedback`.

- **AWS CLI**
- 
            
                    **To update auth event feedback**This example updates authorization event feedback. It marks the event "Valid". Command: `aws cognito-idp update-auth-event-feedback --user-pool-id``us-west-2_aaaaaaaaa`--username`diego@example.com`--event-id`EVENT_ID`--feedback-token`FEEDBACK_TOKEN`--feedback-value`"Valid"`- 
                    For API details, see [UpdateAuthEventFeedback](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-auth-event-feedback.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-device-status`.

- **AWS CLI**
- 
            
                    **To update device status**This example updates the status for a device to "not_remembered". Command: `aws cognito-idp update-device-status --access-token``ACCESS_TOKEN`--device-key`DEVICE_KEY`--device-remembered-status`"not_remembered"`- 
                    For API details, see [UpdateDeviceStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-device-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-group`.

- **AWS CLI**
- 
            
                    **To update a group**This example updates the description and precedence for MyGroup. Command: `aws cognito-idp update-group --user-pool-id``us-west-2_aaaaaaaaa`--group-name`MyGroup`--description`"New description"`--precedence`2`Output: `{ "Group": { "GroupName": "MyGroup", "UserPoolId": "us-west-2_aaaaaaaaa", "Description": "New description", "RoleArn": "arn:aws:iam::111111111111:role/MyRole", "Precedence": 2, "LastModifiedDate": 1548800862.812, "CreationDate": 1548097827.125 } }`- 
                    For API details, see [UpdateGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-identity-provider`.

- **AWS CLI**
- 
            
                    **To update a user pool identity provider**The following `update-identity-provider`example updates the OIDC provider "MyOIDCIdP" in the requested user pool.`aws cognito-idp update-identity-provider \ --cli-input-json``file://update-identity-provider.json`Contents of `update-identity-provider.json`:`{ "AttributeMapping": { "email": "idp_email", "email_verified": "idp_email_verified", "username": "sub" }, "CreationDate": 1.701129701653E9, "IdpIdentifiers": [ "corp", "dev" ], "LastModifiedDate": 1.701129701653E9, "ProviderDetails": { "attributes_request_method": "GET", "attributes_url": "https://example.com/userInfo", "attributes_url_add_attributes": "false", "authorize_scopes": "openid profile", "authorize_url": "https://example.com/authorize", "client_id": "idpexampleclient123", "client_secret": "idpexamplesecret456", "jwks_uri": "https://example.com/.well-known/jwks.json", "oidc_issuer": "https://example.com", "token_url": "https://example.com/token" }, "ProviderName": "MyOIDCIdP", "UserPoolId": "us-west-2_EXAMPLE" }`Output: `{ "IdentityProvider": { "AttributeMapping": { "email": "idp_email", "email_verified": "idp_email_verified", "username": "sub" }, "CreationDate": 1701129701.653, "IdpIdentifiers": [ "corp", "dev" ], "LastModifiedDate": 1736444278.211, "ProviderDetails": { "attributes_request_method": "GET", "attributes_url": "https://example.com/userInfo", "attributes_url_add_attributes": "false", "authorize_scopes": "openid profile", "authorize_url": "https://example.com/authorize", "client_id": "idpexampleclient123", "client_secret": "idpexamplesecret456", "jwks_uri": "https://example.com/.well-known/jwks.json", "oidc_issuer": "https://example.com", "token_url": "https://example.com/token" }, "ProviderName": "MyOIDCIdP", "ProviderType": "OIDC", "UserPoolId": "us-west-2_EXAMPLE" } }`For more information, see [Configuring a domain](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-assign-domain.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [UpdateIdentityProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-identity-provider.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-managed-login-branding`.

- **AWS CLI**
- 
            
                    **To update a managed login branding style**The following `update-managed-login-branding`example updates the requested app client branding style.`aws cognito-idp update-managed-login-branding \ --cli-input-json``file://update-managed-login-branding.json`Contents of `update-managed-login-branding.json`:`{ "Assets": [ { "Bytes": "PHN2ZyB3aWR0aD0iMjAwMDAiIGhlaWdodD0iNDAwIiB2aWV3Qm94PSIwIDAgMjAwMDAgNDAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8ZyBjbGlwLXBhdGg9InVybCgjY2xpcDBfMTcyNTlfMjM2Njc0KSI+CjxyZWN0IHdpZHRoPSIyMDAwMCIgaGVpZ2h0PSI0MDAiIGZpbGw9InVybCgjcGFpbnQwX2xpbmVhcl8xNzI1OV8yMzY2NzQpIi8+CjxwYXRoIGQ9Ik0wIDBIMjAwMDBWNDAwSDBWMFoiIGZpbGw9IiMxMjIwMzciIGZpbGwtb3BhY2l0eT0iMC41Ii8+CjwvZz4KPGRlZnM+CjxsaW5lYXJHcmFkaWVudCBpZD0icGFpbnQwX2xpbmVhcl8xNzI1OV8yMzY2NzQiIHgxPSItODk0LjI0OSIgeTE9IjE5OS45MzEiIHgyPSIxODAzNC41IiB5Mj0iLTU4OTkuNTciIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj4KPHN0b3Agc3RvcC1jb2xvcj0iI0JGODBGRiIvPgo8c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNGRjhGQUIiLz4KPC9saW5lYXJHcmFkaWVudD4KPGNsaXBQYXRoIGlkPSJjbGlwMF8xNzI1OV8yMzY2NzQiPgo8cmVjdCB3aWR0aD0iMjAwMDAiIGhlaWdodD0iNDAwIiBmaWxsPSJ3aGl0ZSIvPgo8L2NsaXBQYXRoPgo8L2RlZnM+Cjwvc3ZnPgo=", "Category": "PAGE_FOOTER_BACKGROUND", "ColorMode": "DARK", "Extension": "SVG" } ], "ManagedLoginBrandingId": "63f30090-6b1f-4278-b885-2bbb81f8e545", "Settings": { "categories": { "auth": { "authMethodOrder": [ [ { "display": "BUTTON", "type": "FEDERATED" }, { "display": "INPUT", "type": "USERNAME_PASSWORD" } ] ], "federation": { "interfaceStyle": "BUTTON_LIST", "order": [ ] } }, "form": { "displayGraphics": true, "instructions": { "enabled": false }, "languageSelector": { "enabled": false }, "location": { "horizontal": "CENTER", "vertical": "CENTER" }, "sessionTimerDisplay": "NONE" }, "global": { "colorSchemeMode": "LIGHT", "pageFooter": { "enabled": false }, "pageHeader": { "enabled": false }, "spacingDensity": "REGULAR" }, "signUp": { "acceptanceElements": [ { "enforcement": "NONE", "textKey": "en" } ] } }, "componentClasses": { "buttons": { "borderRadius": 8.0 }, "divider": { "darkMode": { "borderColor": "232b37ff" }, "lightMode": { "borderColor": "ebebf0ff" } }, "dropDown": { "borderRadius": 8.0, "darkMode": { "defaults": { "itemBackgroundColor": "192534ff" }, "hover": { "itemBackgroundColor": "081120ff", "itemBorderColor": "5f6b7aff", "itemTextColor": "e9ebedff" }, "match": { "itemBackgroundColor": "d1d5dbff", "itemTextColor": "89bdeeff" } }, "lightMode": { "defaults": { "itemBackgroundColor": "ffffffff" }, "hover": { "itemBackgroundColor": "f4f4f4ff", "itemBorderColor": "7d8998ff", "itemTextColor": "000716ff" }, "match": { "itemBackgroundColor": "414d5cff", "itemTextColor": "0972d3ff" } } }, "focusState": { "darkMode": { "borderColor": "539fe5ff" }, "lightMode": { "borderColor": "0972d3ff" } }, "idpButtons": { "icons": { "enabled": true } }, "input": { "borderRadius": 8.0, "darkMode": { "defaults": { "backgroundColor": "0f1b2aff", "borderColor": "5f6b7aff" }, "placeholderColor": "8d99a8ff" }, "lightMode": { "defaults": { "backgroundColor": "ffffffff", "borderColor": "7d8998ff" }, "placeholderColor": "5f6b7aff" } }, "inputDescription": { "darkMode": { "textColor": "8d99a8ff" }, "lightMode": { "textColor": "5f6b7aff" } }, "inputLabel": { "darkMode": { "textColor": "d1d5dbff" }, "lightMode": { "textColor": "000716ff" } }, "link": { "darkMode": { "defaults": { "textColor": "539fe5ff" }, "hover": { "textColor": "89bdeeff" } }, "lightMode": { "defaults": { "textColor": "0972d3ff" }, "hover": { "textColor": "033160ff" } } }, "optionControls": { "darkMode": { "defaults": { "backgroundColor": "0f1b2aff", "borderColor": "7d8998ff" }, "selected": { "backgroundColor": "539fe5ff", "foregroundColor": "000716ff" } }, "lightMode": { "defaults": { "backgroundColor": "ffffffff", "borderColor": "7d8998ff" }, "selected": { "backgroundColor": "0972d3ff", "foregroundColor": "ffffffff" } } }, "statusIndicator": { "darkMode": { "error": { "backgroundColor": "1a0000ff", "borderColor": "eb6f6fff", "indicatorColor": "eb6f6fff" }, "pending": { "indicatorColor": "AAAAAAAA" }, "success": { "backgroundColor": "001a02ff", "borderColor": "29ad32ff", "indicatorColor": "29ad32ff" }, "warning": { "backgroundColor": "1d1906ff", "borderColor": "e0ca57ff", "indicatorColor": "e0ca57ff" } }, "lightMode": { "error": { "backgroundColor": "fff7f7ff", "borderColor": "d91515ff", "indicatorColor": "d91515ff" }, "pending": { "indicatorColor": "AAAAAAAA" }, "success": { "backgroundColor": "f2fcf3ff", "borderColor": "037f0cff", "indicatorColor": "037f0cff" }, "warning": { "backgroundColor": "fffce9ff", "borderColor": "8d6605ff", "indicatorColor": "8d6605ff" } } } }, "components": { "alert": { "borderRadius": 12.0, "darkMode": { "error": { "backgroundColor": "1a0000ff", "borderColor": "eb6f6fff" } }, "lightMode": { "error": { "backgroundColor": "fff7f7ff", "borderColor": "d91515ff" } } }, "favicon": { "enabledTypes": [ "ICO", "SVG" ] }, "form": { "backgroundImage": { "enabled": false }, "borderRadius": 8.0, "darkMode": { "backgroundColor": "0f1b2aff", "borderColor": "424650ff" }, "lightMode": { "backgroundColor": "ffffffff", "borderColor": "c6c6cdff" }, "logo": { "enabled": false, "formInclusion": "IN", "location": "CENTER", "position": "TOP" } }, "idpButton": { "custom": { }, "standard": { "darkMode": { "active": { "backgroundColor": "354150ff", "borderColor": "89bdeeff", "textColor": "89bdeeff" }, "defaults": { "backgroundColor": "0f1b2aff", "borderColor": "c6c6cdff", "textColor": "c6c6cdff" }, "hover": { "backgroundColor": "192534ff", "borderColor": "89bdeeff", "textColor": "89bdeeff" } }, "lightMode": { "active": { "backgroundColor": "d3e7f9ff", "borderColor": "033160ff", "textColor": "033160ff" }, "defaults": { "backgroundColor": "ffffffff", "borderColor": "424650ff", "textColor": "424650ff" }, "hover": { "backgroundColor": "f2f8fdff", "borderColor": "033160ff", "textColor": "033160ff" } } } }, "pageBackground": { "darkMode": { "color": "0f1b2aff" }, "image": { "enabled": true }, "lightMode": { "color": "ffffffff" } }, "pageFooter": { "backgroundImage": { "enabled": false }, "darkMode": { "background": { "color": "0f141aff" }, "borderColor": "424650ff" }, "lightMode": { "background": { "color": "fafafaff" }, "borderColor": "d5dbdbff" }, "logo": { "enabled": false, "location": "START" } }, "pageHeader": { "backgroundImage": { "enabled": false }, "darkMode": { "background": { "color": "0f141aff" }, "borderColor": "424650ff" }, "lightMode": { "background": { "color": "fafafaff" }, "borderColor": "d5dbdbff" }, "logo": { "enabled": false, "location": "START" } }, "pageText": { "darkMode": { "bodyColor": "b6bec9ff", "descriptionColor": "b6bec9ff", "headingColor": "d1d5dbff" }, "lightMode": { "bodyColor": "414d5cff", "descriptionColor": "414d5cff", "headingColor": "000716ff" } }, "phoneNumberSelector": { "displayType": "TEXT" }, "primaryButton": { "darkMode": { "active": { "backgroundColor": "539fe5ff", "textColor": "000716ff" }, "defaults": { "backgroundColor": "539fe5ff", "textColor": "000716ff" }, "disabled": { "backgroundColor": "ffffffff", "borderColor": "ffffffff" }, "hover": { "backgroundColor": "89bdeeff", "textColor": "000716ff" } }, "lightMode": { "active": { "backgroundColor": "033160ff", "textColor": "ffffffff" }, "defaults": { "backgroundColor": "0972d3ff", "textColor": "ffffffff" }, "disabled": { "backgroundColor": "ffffffff", "borderColor": "ffffffff" }, "hover": { "backgroundColor": "033160ff", "textColor": "ffffffff" } } }, "secondaryButton": { "darkMode": { "active": { "backgroundColor": "354150ff", "borderColor": "89bdeeff", "textColor": "89bdeeff" }, "defaults": { "backgroundColor": "0f1b2aff", "borderColor": "539fe5ff", "textColor": "539fe5ff" }, "hover": { "backgroundColor": "192534ff", "borderColor": "89bdeeff", "textColor": "89bdeeff" } }, "lightMode": { "active": { "backgroundColor": "d3e7f9ff", "borderColor": "033160ff", "textColor": "033160ff" }, "defaults": { "backgroundColor": "ffffffff", "borderColor": "0972d3ff", "textColor": "0972d3ff" }, "hover": { "backgroundColor": "f2f8fdff", "borderColor": "033160ff", "textColor": "033160ff" } } } } }, "UseCognitoProvidedValues": false, "UserPoolId": "ca-central-1_EXAMPLE" }`Output: `{ "ManagedLoginBranding": { "Assets": [ { "Bytes": "PHN2ZyB3aWR0aD0iMjAwMDAiIGhlaWdodD0iNDAwIiB2aWV3Qm94PSIwIDAgMjAwMDAgNDAwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8ZyBjbGlwLXBhdGg9InVybCgjY2xpcDBfMTcyNTlfMjM2Njc0KSI+CjxyZWN0IHdpZHRoPSIyMDAwMCIgaGVpZ2h0PSI0MDAiIGZpbGw9InVybCgjcGFpbnQwX2xpbmVhcl8xNzI1OV8yMzY2NzQpIi8+CjxwYXRoIGQ9Ik0wIDBIMjAwMDBWNDAwSDBWMFoiIGZpbGw9IiMxMjIwMzciIGZpbGwtb3BhY2l0eT0iMC41Ii8+CjwvZz4KPGRlZnM+CjxsaW5lYXJHcmFkaWVudCBpZD0icGFpbnQwX2xpbmVhcl8xNzI1OV8yMzY2NzQiIHgxPSItODk0LjI0OSIgeTE9IjE5OS45MzEiIHgyPSIxODAzNC41IiB5Mj0iLTU4OTkuNTciIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj4KPHN0b3Agc3RvcC1jb2xvcj0iI0JGODBGRiIvPgo8c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiNGRjhGQUIiLz4KPC9saW5lYXJHcmFkaWVudD4KPGNsaXBQYXRoIGlkPSJjbGlwMF8xNzI1OV8yMzY2NzQiPgo8cmVjdCB3aWR0aD0iMjAwMDAiIGhlaWdodD0iNDAwIiBmaWxsPSJ3aGl0ZSIvPgo8L2NsaXBQYXRoPgo8L2RlZnM+Cjwvc3ZnPgo=", "Category": "PAGE_FOOTER_BACKGROUND", "ColorMode": "DARK", "Extension": "SVG" } ], "CreationDate": 1732138490.642, "LastModifiedDate": 1732140420.301, "ManagedLoginBrandingId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Settings": { "categories": { "auth": { "authMethodOrder": [ [ { "display": "BUTTON", "type": "FEDERATED" }, { "display": "INPUT", "type": "USERNAME_PASSWORD" } ] ], "federation": { "interfaceStyle": "BUTTON_LIST", "order": [ ] } }, "form": { "displayGraphics": true, "instructions": { "enabled": false }, "languageSelector": { "enabled": false }, "location": { "horizontal": "CENTER", "vertical": "CENTER" }, "sessionTimerDisplay": "NONE" }, "global": { "colorSchemeMode": "LIGHT", "pageFooter": { "enabled": false }, "pageHeader": { "enabled": false }, "spacingDensity": "REGULAR" }, "signUp": { "acceptanceElements": [ { "enforcement": "NONE", "textKey": "en" } ] } }, "componentClasses": { "buttons": { "borderRadius": 8.0 }, "divider": { "darkMode": { "borderColor": "232b37ff" }, "lightMode": { "borderColor": "ebebf0ff" } }, "dropDown": { "borderRadius": 8.0, "darkMode": { "defaults": { "itemBackgroundColor": "192534ff" }, "hover": { "itemBackgroundColor": "081120ff", "itemBorderColor": "5f6b7aff", "itemTextColor": "e9ebedff" }, "match": { "itemBackgroundColor": "d1d5dbff", "itemTextColor": "89bdeeff" } }, "lightMode": { "defaults": { "itemBackgroundColor": "ffffffff" }, "hover": { "itemBackgroundColor": "f4f4f4ff", "itemBorderColor": "7d8998ff", "itemTextColor": "000716ff" }, "match": { "itemBackgroundColor": "414d5cff", "itemTextColor": "0972d3ff" } } }, "focusState": { "darkMode": { "borderColor": "539fe5ff" }, "lightMode": { "borderColor": "0972d3ff" } }, "idpButtons": { "icons": { "enabled": true } }, "input": { "borderRadius": 8.0, "darkMode": { "defaults": { "backgroundColor": "0f1b2aff", "borderColor": "5f6b7aff" }, "placeholderColor": "8d99a8ff" }, "lightMode": { "defaults": { "backgroundColor": "ffffffff", "borderColor": "7d8998ff" }, "placeholderColor": "5f6b7aff" } }, "inputDescription": { "darkMode": { "textColor": "8d99a8ff" }, "lightMode": { "textColor": "5f6b7aff" } }, "inputLabel": { "darkMode": { "textColor": "d1d5dbff" }, "lightMode": { "textColor": "000716ff" } }, "link": { "darkMode": { "defaults": { "textColor": "539fe5ff" }, "hover": { "textColor": "89bdeeff" } }, "lightMode": { "defaults": { "textColor": "0972d3ff" }, "hover": { "textColor": "033160ff" } } }, "optionControls": { "darkMode": { "defaults": { "backgroundColor": "0f1b2aff", "borderColor": "7d8998ff" }, "selected": { "backgroundColor": "539fe5ff", "foregroundColor": "000716ff" } }, "lightMode": { "defaults": { "backgroundColor": "ffffffff", "borderColor": "7d8998ff" }, "selected": { "backgroundColor": "0972d3ff", "foregroundColor": "ffffffff" } } }, "statusIndicator": { "darkMode": { "error": { "backgroundColor": "1a0000ff", "borderColor": "eb6f6fff", "indicatorColor": "eb6f6fff" }, "pending": { "indicatorColor": "AAAAAAAA" }, "success": { "backgroundColor": "001a02ff", "borderColor": "29ad32ff", "indicatorColor": "29ad32ff" }, "warning": { "backgroundColor": "1d1906ff", "borderColor": "e0ca57ff", "indicatorColor": "e0ca57ff" } }, "lightMode": { "error": { "backgroundColor": "fff7f7ff", "borderColor": "d91515ff", "indicatorColor": "d91515ff" }, "pending": { "indicatorColor": "AAAAAAAA" }, "success": { "backgroundColor": "f2fcf3ff", "borderColor": "037f0cff", "indicatorColor": "037f0cff" }, "warning": { "backgroundColor": "fffce9ff", "borderColor": "8d6605ff", "indicatorColor": "8d6605ff" } } } }, "components": { "alert": { "borderRadius": 12.0, "darkMode": { "error": { "backgroundColor": "1a0000ff", "borderColor": "eb6f6fff" } }, "lightMode": { "error": { "backgroundColor": "fff7f7ff", "borderColor": "d91515ff" } } }, "favicon": { "enabledTypes": [ "ICO", "SVG" ] }, "form": { "backgroundImage": { "enabled": false }, "borderRadius": 8.0, "darkMode": { "backgroundColor": "0f1b2aff", "borderColor": "424650ff" }, "lightMode": { "backgroundColor": "ffffffff", "borderColor": "c6c6cdff" }, "logo": { "enabled": false, "formInclusion": "IN", "location": "CENTER", "position": "TOP" } }, "idpButton": { "custom": { }, "standard": { "darkMode": { "active": { "backgroundColor": "354150ff", "borderColor": "89bdeeff", "textColor": "89bdeeff" }, "defaults": { "backgroundColor": "0f1b2aff", "borderColor": "c6c6cdff", "textColor": "c6c6cdff" }, "hover": { "backgroundColor": "192534ff", "borderColor": "89bdeeff", "textColor": "89bdeeff" } }, "lightMode": { "active": { "backgroundColor": "d3e7f9ff", "borderColor": "033160ff", "textColor": "033160ff" }, "defaults": { "backgroundColor": "ffffffff", "borderColor": "424650ff", "textColor": "424650ff" }, "hover": { "backgroundColor": "f2f8fdff", "borderColor": "033160ff", "textColor": "033160ff" } } } }, "pageBackground": { "darkMode": { "color": "0f1b2aff" }, "image": { "enabled": true }, "lightMode": { "color": "ffffffff" } }, "pageFooter": { "backgroundImage": { "enabled": false }, "darkMode": { "background": { "color": "0f141aff" }, "borderColor": "424650ff" }, "lightMode": { "background": { "color": "fafafaff" }, "borderColor": "d5dbdbff" }, "logo": { "enabled": false, "location": "START" } }, "pageHeader": { "backgroundImage": { "enabled": false }, "darkMode": { "background": { "color": "0f141aff" }, "borderColor": "424650ff" }, "lightMode": { "background": { "color": "fafafaff" }, "borderColor": "d5dbdbff" }, "logo": { "enabled": false, "location": "START" } }, "pageText": { "darkMode": { "bodyColor": "b6bec9ff", "descriptionColor": "b6bec9ff", "headingColor": "d1d5dbff" }, "lightMode": { "bodyColor": "414d5cff", "descriptionColor": "414d5cff", "headingColor": "000716ff" } }, "phoneNumberSelector": { "displayType": "TEXT" }, "primaryButton": { "darkMode": { "active": { "backgroundColor": "539fe5ff", "textColor": "000716ff" }, "defaults": { "backgroundColor": "539fe5ff", "textColor": "000716ff" }, "disabled": { "backgroundColor": "ffffffff", "borderColor": "ffffffff" }, "hover": { "backgroundColor": "89bdeeff", "textColor": "000716ff" } }, "lightMode": { "active": { "backgroundColor": "033160ff", "textColor": "ffffffff" }, "defaults": { "backgroundColor": "0972d3ff", "textColor": "ffffffff" }, "disabled": { "backgroundColor": "ffffffff", "borderColor": "ffffffff" }, "hover": { "backgroundColor": "033160ff", "textColor": "ffffffff" } } }, "secondaryButton": { "darkMode": { "active": { "backgroundColor": "354150ff", "borderColor": "89bdeeff", "textColor": "89bdeeff" }, "defaults": { "backgroundColor": "0f1b2aff", "borderColor": "539fe5ff", "textColor": "539fe5ff" }, "hover": { "backgroundColor": "192534ff", "borderColor": "89bdeeff", "textColor": "89bdeeff" } }, "lightMode": { "active": { "backgroundColor": "d3e7f9ff", "borderColor": "033160ff", "textColor": "033160ff" }, "defaults": { "backgroundColor": "ffffffff", "borderColor": "0972d3ff", "textColor": "0972d3ff" }, "hover": { "backgroundColor": "f2f8fdff", "borderColor": "033160ff", "textColor": "033160ff" } } } } }, "UseCognitoProvidedValues": false, "UserPoolId": "ca-central-1_EXAMPLE" } }`For more information, see [Apply branding to managed login pages](https://docs.aws.amazon.com/cognito/latest/developerguide/managed-login-branding.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [UpdateManagedLoginBranding](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-managed-login-branding.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-resource-server`.

- **AWS CLI**
- 
            
                    **To update a resource server**This example updates the the resource server Weather. It adds a new scope. Command: `aws cognito-idp update-resource-server --user-pool-id``us-west-2_aaaaaaaaa`--identifier`weather.example.com`--name`Weather`--scopes ScopeName=NewScope,ScopeDescription="New scope description"Output: `{ "ResourceServer": { "UserPoolId": "us-west-2_aaaaaaaaa", "Identifier": "weather.example.com", "Name": "Happy", "Scopes": [ { "ScopeName": "NewScope", "ScopeDescription": "New scope description" } ] } }`- 
                    For API details, see [UpdateResourceServer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-resource-server.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-user-attributes`.

- **AWS CLI**
- 
            
                    **To update user attributes**This example updates the user attribute "nickname". Command: `aws cognito-idp update-user-attributes --access-token``ACCESS_TOKEN`--user-attributes Name="nickname",Value="Dan"- 
                    For API details, see [UpdateUserAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-user-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-user-pool-client`.

- **AWS CLI**
- 
            
                    **To update an app client**The following `update-user-pool-client`example updates the configuration of the requested app client.`aws cognito-idp update-user-pool-client \ --user-pool-id``us-west-2_EXAMPLE`\ --client-id`1example23456789`\ --client-name`my-test-app`\ --refresh-token-validity`30`\ --access-token-validity`60`\ --id-token-validity`60`\ --token-validity-units`AccessToken=minutes,IdToken=minutes,RefreshToken=days`\ --read-attributes`"address"``"birthdate"``"email"``"email_verified"``"family_name"``"gender"``"locale"``"middle_name"``"name"``"nickname"``"phone_number"``"phone_number_verified"``"picture"``"preferred_username"``"profile"``"updated_at"``"website"``"zoneinfo"`\ --write-attributes`"address"``"birthdate"``"email"``"family_name"``"gender"``"locale"``"middle_name"``"name"``"nickname"``"phone_number"``"picture"``"preferred_username"``"profile"``"updated_at"``"website"``"zoneinfo"`\ --explicit-auth-flows`"ALLOW_ADMIN_USER_PASSWORD_AUTH"``"ALLOW_CUSTOM_AUTH"``"ALLOW_REFRESH_TOKEN_AUTH"``"ALLOW_USER_PASSWORD_AUTH"``"ALLOW_USER_SRP_AUTH"`\ --supported-identity-providers`"MySAML"``"COGNITO"``"Google"`\ --callback-urls`"https://www.example.com"``"https://app2.example.com"`\ --logout-urls`"https://auth.example.com/login?client_id=1example23456789&response_type=code&redirect_uri=https%3A%2F%2Fwww.example.com"``"https://example.com/logout"`\ --default-redirect-uri`"https://www.example.com"`\ --allowed-o-auth-flows`"code"``"implicit"`\ --allowed-o-auth-scopes`"openid"``"profile"``"aws.cognito.signin.user.admin"`\ --allowed-o-auth-flows-user-pool-client \ --prevent-user-existence-errors`ENABLED`\ --enable-token-revocation \ --no-enable-propagate-additional-user-context-data \ --auth-session-validity`3`Output: `{ "UserPoolClient": { "UserPoolId": "us-west-2_EXAMPLE", "ClientName": "my-test-app", "ClientId": "1example23456789", "LastModifiedDate": "2025-01-31T14:40:12.498000-08:00", "CreationDate": "2023-09-13T16:26:34.408000-07:00", "RefreshTokenValidity": 30, "AccessTokenValidity": 60, "IdTokenValidity": 60, "TokenValidityUnits": { "AccessToken": "minutes", "IdToken": "minutes", "RefreshToken": "days" }, "ReadAttributes": [ "website", "zoneinfo", "address", "birthdate", "email_verified", "gender", "profile", "phone_number_verified", "preferred_username", "locale", "middle_name", "picture", "updated_at", "name", "nickname", "phone_number", "family_name", "email" ], "WriteAttributes": [ "website", "zoneinfo", "address", "birthdate", "gender", "profile", "preferred_username", "locale", "middle_name", "picture", "updated_at", "name", "nickname", "phone_number", "family_name", "email" ], "ExplicitAuthFlows": [ "ALLOW_CUSTOM_AUTH", "ALLOW_USER_PASSWORD_AUTH", "ALLOW_ADMIN_USER_PASSWORD_AUTH", "ALLOW_USER_SRP_AUTH", "ALLOW_REFRESH_TOKEN_AUTH" ], "SupportedIdentityProviders": [ "Google", "COGNITO", "MySAML" ], "CallbackURLs": [ "https://www.example.com", "https://app2.example.com" ], "LogoutURLs": [ "https://example.com/logout", "https://auth.example.com/login?client_id=1example23456789&response_type=code&redirect_uri=https%3A%2F%2Fwww.example.com" ], "DefaultRedirectURI": "https://www.example.com", "AllowedOAuthFlows": [ "implicit", "code" ], "AllowedOAuthScopes": [ "aws.cognito.signin.user.admin", "openid", "profile" ], "AllowedOAuthFlowsUserPoolClient": true, "PreventUserExistenceErrors": "ENABLED", "EnableTokenRevocation": true, "EnablePropagateAdditionalUserContextData": false, "AuthSessionValidity": 3 } }`For more information, see [Application-specific settings with app clients](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-client-apps.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [UpdateUserPoolClient](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-user-pool-client.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-user-pool-domain`.

- **AWS CLI**
- 
            
                    **To update a custom domain**The following `update-user-pool-domain`example configures the branding version and certificate for the custom domain the requested user pool.`aws cognito-idp update-user-pool-domain \ --user-pool-id``ca-central-1_EXAMPLE`\ --domain`auth.example.com`\ --managed-login-version`2`\ --custom-domain-config`CertificateArn=arn:aws:acm:us-east-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "CloudFrontDomain": "example.cloudfront.net", "ManagedLoginVersion": 2 }`For more information, see [Managed login](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html)and[Configuring a domain](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-assign-domain.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [UpdateUserPoolDomain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-user-pool-domain.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-user-pool`.

- **AWS CLI**
- 
            
                    **To update a user pool**The following `update-user-pool`example modifies a user pool with example syntax for each of the available configuration options. To update a user pool, you must specify all previously-configured options or they will reset to a default value.`aws cognito-idp update-user-pool --user-pool-id``us-west-2_EXAMPLE`\ --policies PasswordPolicy=\{MinimumLength=6,RequireUppercase=true,RequireLowercase=true,RequireNumbers=true,RequireSymbols=true,TemporaryPasswordValidityDays=7\} \ --deletion-protection`ACTIVE`\ --lambda-config PreSignUp="arn:aws:lambda:us-west-2:123456789012:function:cognito-test-presignup-function",PreTokenGeneration="arn:aws:lambda:us-west-2:123456789012:function:cognito-test-pretoken-function" \ --auto-verified-attributes`"phone_number"``"email"`\ --verification-message-template \{\"SmsMessage\":\"`"Your code is {####}"`\",\"EmailMessage\":\""Your code is {####}"\",\"EmailSubject\":\""Your verification code"\",\"EmailMessageByLink\":\""Click {##here##} to verify your email address."\",\"EmailSubjectByLink\":\""Your verification link"\",\"DefaultEmailOption\":\"CONFIRM_WITH_LINK\"\} \ --sms-authentication-message "Your code is {####}" \ --user-attribute-update-settings AttributesRequireVerificationBeforeUpdate="email","phone_number" \ --mfa-configuration`"OPTIONAL"`\ --device-configuration`ChallengeRequiredOnNewDevice=true,DeviceOnlyRememberedOnUserPrompt=true`\ --email-configuration SourceArn="arn:aws:ses:us-west-2:123456789012:identity/admin@example.com",ReplyToEmailAddress="amdin+noreply@example.com",EmailSendingAccount=DEVELOPER,From="admin@amazon.com",ConfigurationSet="test-configuration-set" \ --sms-configuration SnsCallerArn="arn:aws:iam::123456789012:role/service-role/SNS-SMS-Role",ExternalId="12345",SnsRegion="us-west-2" \ --admin-create-user-config AllowAdminCreateUserOnly=false,InviteMessageTemplate=\{SMSMessage=\""Welcome {username}. Your confirmation code is {####}"\",EmailMessage=\""Welcome {username}. Your confirmation code is {####}"\",EmailSubject=\""Welcome to MyMobileGame"\"\} \ --user-pool-tags "Function"="MyMobileGame","Developers"="Berlin" \ --admin-create-user-config AllowAdminCreateUserOnly=false,InviteMessageTemplate=\{SMSMessage=\""Welcome {username}. Your confirmation code is {####}"\",EmailMessage=\""Welcome {username}. Your confirmation code is {####}"\",EmailSubject=\""Welcome to MyMobileGame"\"\} \ --user-pool-add-ons AdvancedSecurityMode="AUDIT" \ --account-recovery-setting RecoveryMechanisms=\[\{Priority=1,Name="verified_email"\},\{Priority=2,Name="verified_phone_number"\}\]This command produces no output. For more information, see [Updating user pool configuration](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-updating.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [UpdateUserPool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/update-user-pool.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `verify-software-token`.

- **AWS CLI**
- 
            
                    **To confirm registration of a TOTP authenticator**The following `verify-software-token`example completes TOTP registration for the current user.`aws cognito-idp verify-software-token \ --access-token``eyJra456defEXAMPLE`\ --user-code`123456`Output: `{ "Status": "SUCCESS" }`For more information, see [Adding MFA to a user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [VerifySoftwareToken](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/verify-software-token.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `verify-user-attribute`.

- **AWS CLI**
- 
            
                    **To verify an attribute change**The following `verify-user-attribute`example verifies a change to the current user's email attribute.`aws cognito-idp verify-user-attribute \ --access-token``eyJra456defEXAMPLE`\ --attribute-name`email`\ --code`123456`For more information, see [Configuring email or phone verification](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-email-phone-verification.html)in the*Amazon Cognito Developer Guide*.- 
                    For API details, see [VerifyUserAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/verify-user-attribute.html)in*AWS CLI Command Reference*.
 
-