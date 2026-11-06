# AWS STS examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_sts_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_sts_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS STS.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `assume-role-with-saml`.

- **AWS CLI**
- 
            
                    **To get short-term credentials for a role authenticated with SAML**The following `assume-role-with-saml`command retrieves a set of short-term credentials for the IAM role`TestSaml`. The request in this example is authenticated by using the SAML assertion supplied by your identity provider when you authenticate to it.`aws sts assume-role-with-saml \ --role-arn``arn:aws:iam::123456789012:role/TestSaml`\ --principal-arn`arn:aws:iam::123456789012:saml-provider/SAML-test`\ --saml-assertion`"VERYLONGENCODEDASSERTIONEXAMPLExzYW1sOkF1ZGllbmNlPmJsYW5rPC9zYW1sOkF1ZGllbmNlPjwvc2FtbDpBdWRpZW5jZVJlc3RyaWN0aW9uPjwvc2FtbDpDb25kaXRpb25zPjxzYW1sOlN1YmplY3Q+PHNhbWw6TmFtZUlEIEZvcm1hdD0idXJuOm9hc2lzOm5hbWVzOnRjOlNBTUw6Mi4wOm5hbWVpZC1mb3JtYXQ6dHJhbnNpZW50Ij5TYW1sRXhhbXBsZTwvc2FtbDpOYW1lSUQ+PHNhbWw6U3ViamVjdENvbmZpcm1hdGlvbiBNZXRob2Q9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjIuMDpjbTpiZWFyZXIiPjxzYW1sOlN1YmplY3RDb25maXJtYXRpb25EYXRhIE5vdE9uT3JBZnRlcj0iMjAxOS0xMS0wMVQyMDoyNTowNS4xNDVaIiBSZWNpcGllbnQ9Imh0dHBzOi8vc2lnbmluLmF3cy5hbWF6b24uY29tL3NhbWwiLz48L3NhbWw6U3ViamVjdENvbmZpcm1hdGlvbj48L3NhbWw6U3ViamVjdD48c2FtbDpBdXRoblN0YXRlbWVudCBBdXRoPD94bWwgdmpSZXNwb25zZT4="`Output: `{ "Issuer": "https://integ.example.com/idp/shibboleth</Issuer", "AssumedRoleUser": { "Arn": "arn:aws:sts::123456789012:assumed-role/TestSaml", "AssumedRoleId": "ARO456EXAMPLE789:TestSaml" }, "Credentials": { "AccessKeyId": "ASIAV3ZUEFP6EXAMPLE", "SecretAccessKey": "8P+SQvWIuLnKhh8d++jpw0nNmQRBZvNEXAMPLEKEY", "SessionToken": "IQoJb3JpZ2luX2VjEOz////////////////////wEXAMPLEtMSJHMEUCIDoKK3JH9uGQE1z0sINr5M4jk+Na8KHDcCYRVjJCZEvOAiEA3OvJGtw1EcViOleS2vhs8VdCKFJQWPQrmGdeehM4IC1NtBmUpp2wUE8phUZampKsburEDy0KPkyQDYwT7WZ0wq5VSXDvp75YU9HFvlRd8Tx6q6fE8YQcHNVXAkiY9q6d+xo0rKwT38xVqr7ZD0u0iPPkUL64lIZbqBAz+scqKmlzm8FDrypNC9Yjc8fPOLn9FX9KSYvKTr4rvx3iSIlTJabIQwj2ICCR/oLxBA==", "Expiration": "2019-11-01T20:26:47Z" }, "Audience": "https://signin.aws.amazon.com/saml", "SubjectType": "transient", "PackedPolicySize": "6", "NameQualifier": "SbdGOnUkh1i4+EXAMPLExL/jEvs=", "Subject": "SamlExample" }`For more information, see [Requesting Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#api_assumerolewithsaml)in the*AWS IAM User Guide*.- 
                    For API details, see [AssumeRoleWithSaml](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/assume-role-with-saml.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `assume-role-with-web-identity`.

- **AWS CLI**
- 
            
                    **To get short-term credentials for a role authenticated with Web Identity (OAuth 2."0)**The following `assume-role-with-web-identity`command retrieves a set of short-term credentials for the IAM role`app1`. The request is authenticated by using the web identity token supplied by the specified web identity provider. Two additional policies are applied to the session to further restrict what the user can do. The returned credentials expire one hour after they are generated.`aws sts assume-role-with-web-identity \ --duration-seconds``3600`\ --role-session-name`"app1"`\ --provider-id`"www.amazon.com"`\ --policy-arns "arn:aws:iam::123456789012:policy/q=webidentitydemopolicy1","arn:aws:iam::123456789012:policy/webidentitydemopolicy2" \ --role-arn`arn:aws:iam::123456789012:role/FederatedWebIdentityRole`\ --web-identity-token`"Atza%7CIQEBLjAsAhRFiXuWpUXuRvQ9PZL3GMFcYevydwIUFAHZwXZXXXXXXXXJnrulxKDHwy87oGKPznh0D6bEQZTSCzyoCtL_8S07pLpr0zMbn6w1lfVZKNTBdDansFBmtGnIsIapjI6xKR02Yc_2bQ8LZbUXSGm6Ry6_BG7PrtLZtj_dfCTj92xNGed-CrKqjG7nPBjNIL016GGvuS5gSvPRUxWES3VYfm1wl7WTI7jn-Pcb6M-buCgHhFOzTQxod27L9CqnOLio7N3gZAGpsp6n1-AJBOCJckcyXe2c6uD0srOJeZlKUm2eTDVMf8IehDVI0r1QOnTV6KzzAI3OY87Vd_cVMQ"`Output: `{ "SubjectFromWebIdentityToken": "amzn1.account.AF6RHO7KZU5XRVQJGXK6HB56KR2A", "Audience": "client.5498841531868486423.1548@apps.example.com", "AssumedRoleUser": { "Arn": "arn:aws:sts::123456789012:assumed-role/FederatedWebIdentityRole/app1", "AssumedRoleId": "AROACLKWSDQRAOEXAMPLE:app1" }, "Credentials": { "AccessKeyId": "AKIAIOSFODNN7EXAMPLE", "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY", "SessionToken": "AQoEXAMPLEH4aoAH0gNCAPyJxz4BlCFFxWNE1OPTgk5TthT+FvwqnKwRcOIfrRh3c/LTo6UDdyJwOOvEVPvLXCrrrUtdnniCEXAMPLE/IvU1dYUg2RVAJBanLiHb4IgRmpRV3zrkuWJOgQs8IZZaIv2BXIa2R4OlgkBN9bkUDNCJiBeb/AXlzBBko7b15fjrBs2+cTQtpZ3CYWFXG8C5zqx37wnOE49mRl/+OtkIKGO7fAE", "Expiration": "2020-05-19T18:06:10+00:00" }, "Provider": "www.amazon.com" }`For more information, see [Requesting Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#api_assumerolewithwebidentity)in the*AWS IAM User Guide*.- 
                    For API details, see [AssumeRoleWithWebIdentity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/assume-role-with-web-identity.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `assume-role`.

- **AWS CLI**
- 
            
                    **To assume a role**The following `assume-role`command retrieves a set of short-term credentials for the IAM role`s3-access-example`.`aws sts assume-role \ --role-arn``arn:aws:iam::123456789012:role/xaccounts3access`\ --role-session-name`s3-access-example`Output: `{ "AssumedRoleUser": { "AssumedRoleId": "AROA3XFRBF535PLBIFPI4:s3-access-example", "Arn": "arn:aws:sts::123456789012:assumed-role/xaccounts3access/s3-access-example" }, "Credentials": { "SecretAccessKey": "9drTJvcXLB89EXAMPLELB8923FB892xMFI", "SessionToken": "AQoXdzELDDY//////////wEaoAK1wvxJY12r2IrDFT2IvAzTCn3zHoZ7YNtpiQLF0MqZye/qwjzP2iEXAMPLEbw/m3hsj8VBTkPORGvr9jM5sgP+w9IZWZnU+LWhmg+a5fDi2oTGUYcdg9uexQ4mtCHIHfi4citgqZTgco40Yqr4lIlo4V2b2Dyauk0eYFNebHtYlFVgAUj+7Indz3LU0aTWk1WKIjHmmMCIoTkyYp/k7kUG7moeEYKSitwQIi6Gjn+nyzM+PtoA3685ixzv0R7i5rjQi0YE0lf1oeie3bDiNHncmzosRM6SFiPzSvp6h/32xQuZsjcypmwsPSDtTPYcs0+YN/8BRi2/IcrxSpnWEXAMPLEXSDFTAQAM6Dl9zR0tXoybnlrZIwMLlMi1Kcgo5OytwU=", "Expiration": "2016-03-15T00:05:07Z", "AccessKeyId": "ASIAJEXAMPLEXEG2JICEA" } }`The output of the command contains an access key, secret key, and session token that you can use to authenticate to AWS. For AWS CLI use, you can set up a named profile associated with a role. When you use the profile, the AWS CLI will call assume-role and manage credentials for you. For more information, see [Use an IAM role in the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-role.html)in the*AWS CLI User Guide*.- 
                    For API details, see [AssumeRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/assume-role.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `assume-root`.

- **AWS CLI**
- 
            
                    **To launch a privileged session**The following `assume-root`command retrieves a set of short-term credentials you can use to remove a misconfigured Amazon S3 bucket policy for a member account in your organization.`aws sts assume-root \ --duration-seconds``900`\ --target-principal`111122223333`\ --task-policy-arn`arn=arn:aws:iam::aws:policy/root-task/S3UnlockBucketPolicy`Output: `{ "Credentials": { "SecretAccessKey": "9drTJvcXLB89EXAMPLELB8923FB892xMFI", "SessionToken": "AQoXdzELDDY//////////wEaoAK1wvxJY12r2IrDFT2IvAzTCn3zHoZ7YNtpiQLF0MqZye/qwjzP2iEXAMPLEbw/m3hsj8VBTkPORGvr9jM5sgP+w9IZWZnU+LWhmg+a5fDi2oTGUYcdg9uexQ4mtCHIHfi4citgqZTgco40Yqr4lIlo4V2b2Dyauk0eYFNebHtYlFVgAUj+7Indz3LU0aTWk1WKIjHmmMCIoTkyYp/k7kUG7moeEYKSitwQIi6Gjn+nyzM+PtoA3685ixzv0R7i5rjQi0YE0lf1oeie3bDiNHncmzosRM6SFiPzSvp6h/32xQuZsjcypmwsPSDtTPYcs0+YN/8BRi2/IcrxSpnWEXAMPLEXSDFTAQAM6Dl9zR0tXoybnlrZIwMLlMi1Kcgo5OytwU=", "Expiration": "2024-11-15T00:05:07Z", "AccessKeyId": "ASIAJEXAMPLEXEG2JICEA" }, "SourceIdentity": "Alice", }`The output of the command contains an access key, secret key, and session token that you can use to to perform privileged actions in the member account. For more information, see [Perform a privileged task on an AWS Organizations member account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user-privileged-task.html)in the*AWS IAM User Guide*.- 
                    For API details, see [AssumeRoot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/assume-root.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `decode-authorization-message`.

- **AWS CLI**
- 
            
                    **To decode an encoded authorization message returned in response to a request**The following `decode-authorization-message`example decodes additional information about the authorization status of a request from an encoded message returned in response to an Amazon Web Services request.`aws sts decode-authorization-message \ --encoded-message``EXAMPLEWodyRNrtlQARDip-eTA6i6DrlUhHhPQrLWB_lAbl5pAKxl9mPDLexYcGBreyIKQC1BGBIpBKr3dFDkwqeO7e2NMk5j_hmzAiChJN-8oy3EwiCjkUW5fdRNjcRvscGlUo_MhqHqHpR-Ojau7BMjOTWwOtHPhV_Zaz87yENdipr745EjQwRd5LaoL3vN8_5ZfA9UiBMKDgVh1gjqZJFUiQoubv78V1RbHNYnK44ElGKmUWYa020I1y6TNS9LXoNmc62GzkfGvoPGhD13br5tXEOo1rAm3vsPewRDFNkYL-4_1MWWezhRNEpqvXBDXLI9xEux7YYkRtjd45NJLFzZynBUubV8NHOevVuighd1Mvz3OiA-1_oPSe4TBtjfN9s7kjU1z70WpVbUgrLVp1xXTK1rf9Ea7t8shPd-3VzKhjS5tLrweFxNOKwV2GtT76B_fRp8HTYz-pOu3FZjwYStfvTb3GHs3-6rLribGO9jZOktkfE6vqxlFzLyeDr4P2ihC1wty9tArCvvGzIAUNmARQJ2VVWPxioqgoqCzMaDMZEO7wkku7QeakEVZdf00qlNLMmcaVZb1UPNqD-JWP5pwe_mAyqh0NLw-r1S56YC_90onj9A80sNrHlI-tIiNd7tgNTYzDuPQYD2FMDBnp82V9eVmYGtPp5NIeSpuf3fOHanFuBZgENxZQZ2dlH3xJGMTtYayzZrRXjiq_SfX9zeBbpCvrD-0AJK477RM84vmtCrsUpJgx-FaoPIb8LmmKVBLpIB0iFhU9sEHPqKHVPi6jdxXqKaZaFGvYVmVOiuQdNQKuyk0p067POFrZECLjjOtNPBOZCcuEKEXAMPLE`Output: `{ "DecodedMessage": "{\"allowed\":false,\"explicitDeny\":true,\"matchedStatements\":{\"items\":[{\"statementId\":\"VisualEditor0\",\"effect\":\"DENY\",\"principals\":{\"items\":[{\"value\":\"AROA123456789EXAMPLE\"}]},\"principalGroups\":{\"items\":[]},\"actions\":{\"items\":[{\"value\":\"ec2:RunInstances\"}]},\"resources\":{\"items\":[{\"value\":\"*\"}]},\"conditions\":{\"items\":[]}}]},\"failures\":{\"items\":[]},\"context\":{\"principal\":{\"id\":\"AROA123456789EXAMPLE:Ana\",\"arn\":\"arn:aws:sts::111122223333:assumed-role/Developer/Ana\"},\"action\":\"RunInstances\",\"resource\":\"arn:aws:ec2:us-east-1:111122223333:instance/*\",\"conditions\":{\"items\":[{\"key\":\"ec2:MetadataHttpPutResponseHopLimit\",\"values\":{\"items\":[{\"value\":\"2\"}]}},{\"key\":\"ec2:InstanceMarketType\",\"values\":{\"items\":[{\"value\":\"on-demand\"}]}},{\"key\":\"aws:Resource\",\"values\":{\"items\":[{\"value\":\"instance/*\"}]}},{\"key\":\"aws:Account\",\"values\":{\"items\":[{\"value\":\"111122223333\"}]}},{\"key\":\"ec2:AvailabilityZone\",\"values\":{\"items\":[{\"value\":\"us-east-1f\"}]}},{\"key\":\"ec2:ebsOptimized\",\"values\":{\"items\":[{\"value\":\"false\"}]}},{\"key\":\"ec2:IsLaunchTemplateResource\",\"values\":{\"items\":[{\"value\":\"false\"}]}},{\"key\":\"ec2:InstanceType\",\"values\":{\"items\":[{\"value\":\"t2.micro\"}]}},{\"key\":\"ec2:RootDeviceType\",\"values\":{\"items\":[{\"value\":\"ebs\"}]}},{\"key\":\"aws:Region\",\"values\":{\"items\":[{\"value\":\"us-east-1\"}]}},{\"key\":\"ec2:MetadataHttpEndpoint\",\"values\":{\"items\":[{\"value\":\"enabled\"}]}},{\"key\":\"aws:Service\",\"values\":{\"items\":[{\"value\":\"ec2\"}]}},{\"key\":\"ec2:InstanceID\",\"values\":{\"items\":[{\"value\":\"*\"}]}},{\"key\":\"ec2:MetadataHttpTokens\",\"values\":{\"items\":[{\"value\":\"required\"}]}},{\"key\":\"aws:Type\",\"values\":{\"items\":[{\"value\":\"instance\"}]}},{\"key\":\"ec2:Tenancy\",\"values\":{\"items\":[{\"value\":\"default\"}]}},{\"key\":\"ec2:Region\",\"values\":{\"items\":[{\"value\":\"us-east-1\"}]}},{\"key\":\"aws:ARN\",\"values\":{\"items\":[{\"value\":\"arn:aws:ec2:us-east-1:111122223333:instance/*\"}]}}]}}}" }`For more information, see [Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html)in the*AWS IAM User Guide*.- 
                    For API details, see [DecodeAuthorizationMessage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/decode-authorization-message.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-caller-identity`.

- **AWS CLI**
- 
            
                    **To get details about the current IAM identity**The following `get-caller-identity`command displays information about the IAM identity used to authenticate the request. The caller is an IAM user.`aws sts get-caller-identity`Output: `{ "UserId": "AIDASAMPLEUSERID", "Account": "123456789012", "Arn": "arn:aws:iam::123456789012:user/DevAdmin" }`- 
                    For API details, see [GetCallerIdentity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/get-caller-identity.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-federation-token`.

- **AWS CLI**
- 
            
                    **To return a set of temporary security credentials using IAM user access key credentials**The following `get-federation-token`example returns a set of temporary security credentials (consisting of an access key ID, a secret access key, and a security token) for a user. You must call the`GetFederationToken`operation using the long-term security credentials of an IAM user.`aws sts get-federation-token \ --name``Bob`\ --policy`file://myfile.json`\ --policy-arns`arn=arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess`\ --duration-seconds`900`Contents of `myfile.json`:`{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "ec2:Describe*", "Resource": "*" }, { "Effect": "Allow", "Action": "elasticloadbalancing:Describe*", "Resource": "*" }, { "Effect": "Allow", "Action": [ "cloudwatch:ListMetrics", "cloudwatch:GetMetricStatistics", "cloudwatch:Describe*" ], "Resource": "*" }, { "Effect": "Allow", "Action": "autoscaling:Describe*", "Resource": "*" } ] }`Output: `{ "Credentials": { "AccessKeyId": "ASIAIOSFODNN7EXAMPLE", "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY", "SessionToken": "EXAMPLEpZ2luX2VjEGoaCXVzLXdlc3QtMiJIMEYCIQC/W9pL5ArQyDD5JwFL3/h5+WGopQ24GEXweNctwhi9sgIhAMkg+MZE35iWM8s4r5Lr25f9rSTVPFH98G42QQunWMTfKq0DCOP//////////wEQAxoMNDUyOTI1MTcwNTA3Igxuy3AOpuuoLsk3MJwqgQPg8QOd9HuoClUxq26wnc/nm+eZLjHDyGf2KUAHK2DuaS/nrGSEXAMPLE", "Expiration": "2023-12-20T02:06:07+00:00" }, "FederatedUser": { "FederatedUserId": "111122223333:Bob", "Arn": "arn:aws:sts::111122223333:federated-user/Bob" }, "PackedPolicySize": 36 }`For more information, see [Requesting Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#api_getfederationtoken)in the*AWS IAM User Guide*.- 
                    For API details, see [GetFederationToken](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/get-federation-token.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-session-token`.

- **AWS CLI**
- 
            
                    **To get a set of short term credentials for an IAM identity**The following `get-session-token`command retrieves a set of short-term credentials for the IAM identity making the call. The resulting credentials can be used for requests where multi-factor authentication (MFA) is required by policy. The credentials expire 15 minutes after they are generated.`aws sts get-session-token \ --duration-seconds``900`\ --serial-number`"YourMFADeviceSerialNumber"`\ --token-code`123456`Output: `{ "Credentials": { "AccessKeyId": "ASIAIOSFODNN7EXAMPLE", "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY", "SessionToken": "AQoEXAMPLEH4aoAH0gNCAPyJxz4BlCFFxWNE1OPTgk5TthT+FvwqnKwRcOIfrRh3c/LTo6UDdyJwOOvEVPvLXCrrrUtdnniCEXAMPLE/IvU1dYUg2RVAJBanLiHb4IgRmpRV3zrkuWJOgQs8IZZaIv2BXIa2R4OlgkBN9bkUDNCJiBeb/AXlzBBko7b15fjrBs2+cTQtpZ3CYWFXG8C5zqx37wnOE49mRl/+OtkIKGO7fAE", "Expiration": "2020-05-19T18:06:10+00:00" } }`For more information, see [Requesting Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#api_getsessiontoken)in the*AWS IAM User Guide*.- 
                    For API details, see [GetSessionToken](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/get-session-token.html)in*AWS CLI Command Reference*.
 
-