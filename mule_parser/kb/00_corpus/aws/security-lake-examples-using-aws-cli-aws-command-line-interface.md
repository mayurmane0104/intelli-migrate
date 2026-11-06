# Security Lake examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_securitylake_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_securitylake_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Security Lake.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-aws-log-source`.

- **AWS CLI**
- 
            
                    **To add a natively supported Amazon Web Service as an Amazon Security Lake source**The following `create-aws-logsource`example adds VPC Flow Logs as a Security Lake source in the designated accounts and Regions.`aws securitylake create-aws-log-source \ --sources '``[{"regions": ["us-east-1"], "accounts": ["123456789012"], "sourceName": "SH_FINDINGS", "sourceVersion": "2.0"}]`'Output: `{ "failed": [ "123456789012" ] }`For more information, see [Adding an AWS service as a source](https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html#add-internal-sources)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [CreateAwsLogSource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-aws-log-source.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-custom-log-source`.

- **AWS CLI**
- 
            
                    **To add a custom source as an Amazon Security Lake source**The following `create-custom-logsource`example adds a custom source as a Security Lake source in the designated log provider account and the designated Region.`aws securitylake create-custom-log-source \ --source-name``"VPC_FLOW"`\ --event-classes '`["DNS_ACTIVITY", "NETWORK_ACTIVITY"]`' \ --configuration '`{"crawlerConfiguration": {"roleArn": "arn:aws:glue:eu-west-2:123456789012:crawler/E1WG1ZNPRXT0D4"},"providerIdentity": {"principal": "029189416600","externalId": "123456789012"}}`' --region`"us-east-1"`Output: `{ "customLogSource": { "attributes": { "crawlerArn": "arn:aws:glue:eu-west-2:123456789012:crawler/E1WG1ZNPRXT0D4", "databaseArn": "arn:aws:glue:eu-west-2:123456789012:database/E1WG1ZNPRXT0D4", "tableArn": "arn:aws:glue:eu-west-2:123456789012:table/E1WG1ZNPRXT0D4" }, "provider": { "location": "amzn-s3-demo-bucket--usw2-az1--x-s3", "roleArn": "arn:aws:iam::123456789012:role/AmazonSecurityLake-Provider-testCustom2-eu-west-2" }, "sourceName": "testCustom2" "sourceVersion": "2.0" } }`For more information, see [Adding a custom source](https://docs.aws.amazon.com/security-lake/latest/userguide/custom-sources.html#adding-custom-sources)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [CreateCustomLogSource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-custom-log-source.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-data-lake-exception-subscription`.

- **AWS CLI**
- 
            
                    **To send notifications of Security Lake exceptions**The following `create-data-lake-exception-subscription`example sends notifications of Security Lake exceptions to the specified account through SMS delivery. The exception message remains for the specified time period.`aws securitylake create-data-lake-exception-subscription \ --notification-endpoint``"123456789012"`\ --exception-time-to-live`30`\ --subscription-protocol`"sms"`This command produces no output. For more information, see [Troubleshooting Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/security-lake-troubleshoot.html#securitylake-data-lake-troubleshoot)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [CreateDataLakeExceptionSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-data-lake-exception-subscription.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-data-lake-organization-configuration`.

- **AWS CLI**
- 
            
                    **To configure Security Lake in new organization accounts**The following `create-data-lake-organization-configuration`example enables Security Lake and the collection of the specified source events and logs in new organization accounts.`aws securitylake create-data-lake-organization-configuration \ --auto-enable-new-account '``[{"region":"us-east-1","sources":[{"sourceName":"SH_FINDINGS","sourceVersion": "1.0"}]}]`'This command produces no output. For more information, see [Managing multiple accounts with AWS Organizations](https://docs.aws.amazon.com/security-lake/latest/userguide/multi-account-management.html)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [CreateDataLakeOrganizationConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-data-lake-organization-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-data-lake`.

- **AWS CLI**
- 
            
                    **Example 1: To configure your data lake in multiple Regions**The following `create-data-lake`example enables Amazon Security Lake in multiple AWS Regions and configures your data lake.`aws securitylake create-data-lake \ --configurations '``[{"encryptionConfiguration": {"kmsKeyId":"S3_MANAGED_KEY"},"region":"us-east-1","lifecycleConfiguration": {"expiration":{"days":365},"transitions":[{"days":60,"storageClass":"ONEZONE_IA"}]}}, {"encryptionConfiguration": {"kmsKeyId":"S3_MANAGED_KEY"},"region":"us-east-2","lifecycleConfiguration": {"expiration":{"days":365},"transitions":[{"days":60,"storageClass":"ONEZONE_IA"}]}}]`' \ --meta-store-manager-role-arn`"arn:aws:iam:us-east-1:123456789012:role/service-role/AmazonSecurityLakeMetaStoreManager"`Output: `{ "dataLakes": [ { "createStatus": "COMPLETED", "dataLakeArn": "arn:aws:securitylake:us-east-1:522481757177:data-lake/default", "encryptionConfiguration": { "kmsKeyId": "S3_MANAGED_KEY" }, "lifecycleConfiguration": { "expiration": { "days": 365 }, "transitions": [ { "days": 60, "storageClass": "ONEZONE_IA" } ] }, "region": "us-east-1", "replicationConfiguration": { "regions": [ "ap-northeast-3" ], "roleArn": "arn:aws:securitylake:ap-northeast-3:522481757177:data-lake/default" }, "s3BucketArn": "arn:aws:s3:::aws-security-data-lake-us-east-1-gnevt6s8z7bzby8oi3uiaysbr8v2ml", "updateStatus": { "exception": {}, "requestId": "f20a6450-d24a-4f87-a6be-1d4c075a59c2", "status": "INITIALIZED" } }, { "createStatus": "COMPLETED", "dataLakeArn": "arn:aws:securitylake:us-east-2:522481757177:data-lake/default", "encryptionConfiguration": { "kmsKeyId": "S3_MANAGED_KEY" }, "lifecycleConfiguration": { "expiration": { "days": 365 }, "transitions": [ { "days": 60, "storageClass": "ONEZONE_IA" } ] }, "region": "us-east-2", "replicationConfiguration": { "regions": [ "ap-northeast-3" ], "roleArn": "arn:aws:securitylake:ap-northeast-3:522481757177:data-lake/default" }, "s3BucketArn": "arn:aws:s3:::aws-security-data-lake-us-east-2-cehuifzl5rwmhm6m62h7zhvtseogr9", "updateStatus": { "exception": {}, "requestId": "f20a6450-d24a-4f87-a6be-1d4c075a59c2", "status": "INITIALIZED" } } ] }`For more information, see [Getting started with Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/getting-started.html)in the*Amazon Security Lake User Guide*.**Example 2: To configure your data lake in a single Region**The following `create-data-lake`example enables Amazon Security Lake in a single AWS Region and configures your data lake.`aws securitylake create-data-lake \ --configurations '``[{"encryptionConfiguration": {"kmsKeyId":"1234abcd-12ab-34cd-56ef-1234567890ab"},"region":"us-east-2","lifecycleConfiguration": {"expiration":{"days":500},"transitions":[{"days":30,"storageClass":"GLACIER"}]}}]`' \ --meta-store-manager-role-arn`"arn:aws:iam:us-east-1:123456789012:role/service-role/AmazonSecurityLakeMetaStoreManager"`Output: `{ "dataLakes": [ { "createStatus": "COMPLETED", "dataLakeArn": "arn:aws:securitylake:us-east-2:522481757177:data-lake/default", "encryptionConfiguration": { "kmsKeyId": "1234abcd-12ab-34cd-56ef-1234567890ab" }, "lifecycleConfiguration": { "expiration": { "days": 500 }, "transitions": [ { "days": 30, "storageClass": "GLACIER" } ] }, "region": "us-east-2", "replicationConfiguration": { "regions": [ "ap-northeast-3" ], "roleArn": "arn:aws:securitylake:ap-northeast-3:522481757177:data-lake/default" }, "s3BucketArn": "arn:aws:s3:::aws-security-data-lake-us-east-2-cehuifzl5rwmhm6m62h7zhvtseogr9", "updateStatus": { "exception": {}, "requestId": "77702a53-dcbf-493e-b8ef-518e362f3003", "status": "INITIALIZED" } } ] }`For more information, see [Getting started with Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/getting-started.html)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [CreateDataLake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-data-lake.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-subscriber-notification`.

- **AWS CLI**
- 
            
                    **To create a subscriber notification**The following `create-subscriber-notification`example shows how to specify subscriber notification to create a notification when new data is written to the data lake.`aws securitylake create-subscriber-notification \ --subscriber-id``"12345ab8-1a34-1c34-1bd4-12345ab9012"`\ --configuration '`{"httpsNotificationConfiguration": {"targetRoleArn":"arn:aws:iam::XXX:role/service-role/RoleName", "endpoint":"https://account-management.$3.$2.securitylake.aws.dev/v1/datalake"}}`'Output: `{ "subscriberEndpoint": [ "https://account-management.$3.$2.securitylake.aws.dev/v1/datalake" ] }`For more information, see [Subscriber management](https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-management.html)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [CreateSubscriberNotification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-subscriber-notification.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-subscriber`.

- **AWS CLI**
- 
            
                    **Example 1: To create a subscriber with data access**The following `create-subscriber`example creates a subscriber in Security Lake with access to data in the current AWS Region for the specified subscriber identity for an AWS source.`aws securitylake create-subscriber \ --access-types``"S3"`\ --sources '`[{"awsLogSource": {"sourceName": "VPC_FLOW","sourceVersion": "2.0"}}]`' \ --subscriber-name '`opensearch-s3`' \ --subscriber-identity '`{"principal": "029189416600","externalId": "123456789012"}`'Output: `{ "subscriber": { "accessTypes": [ "S3" ], "createdAt": "2024-07-17T19:08:26.787000+00:00", "roleArn": "arn:aws:iam::773172568199:role/AmazonSecurityLake-896f218b-cfba-40be-a255-8b49a65d0407", "s3BucketArn": "arn:aws:s3:::aws-security-data-lake-us-east-1-um632ufwpvxkyz0bc5hkb64atycnf3", "sources": [ { "awsLogSource": { "sourceName": "VPC_FLOW", "sourceVersion": "2.0" } } ], "subscriberArn": "arn:aws:securitylake:us-east-1:773172568199:subscriber/896f218b-cfba-40be-a255-8b49a65d0407", "subscriberId": "896f218b-cfba-40be-a255-8b49a65d0407", "subscriberIdentity": { "externalId": "123456789012", "principal": "029189416600" }, "subscriberName": "opensearch-s3", "subscriberStatus": "ACTIVE", "updatedAt": "2024-07-17T19:08:27.133000+00:00" } }`For more information, see [Creating a subscriber with data access](https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-data-access.html#create-subscriber-data-access)in the*Amazon Security Lake User Guide*.**Example 2: To create a subscriber with query access**The following `create-subscriber`example creates a subscriber in Security Lake with query access in the current AWS Region for the specified subscriber identity.`aws securitylake create-subscriber \ --access-types``"LAKEFORMATION"`\ --sources '`[{"awsLogSource": {"sourceName": "VPC_FLOW","sourceVersion": "2.0"}}]`' \ --subscriber-name '`opensearch-s3`' \ --subscriber-identity '`{"principal": "029189416600","externalId": "123456789012"}`'Output: `{ "subscriber": { "accessTypes": [ "LAKEFORMATION" ], "createdAt": "2024-07-18T01:05:55.853000+00:00", "resourceShareArn": "arn:aws:ram:us-east-1:123456789012:resource-share/8c31da49-c224-4f1e-bb12-37ab756d6d8a", "resourceShareName": "LakeFormation-V2-NAMENAMENA-123456789012", "sources": [ { "awsLogSource": { "sourceName": "VPC_FLOW", "sourceVersion": "2.0" } } ], "subscriberArn": "arn:aws:securitylake:us-east-1:123456789012:subscriber/e762aabb-ce3d-4585-beab-63474597845d", "subscriberId": "e762aabb-ce3d-4585-beab-63474597845d", "subscriberIdentity": { "externalId": "123456789012", "principal": "029189416600" }, "subscriberName": "opensearch-s3", "subscriberStatus": "ACTIVE", "updatedAt": "2024-07-18T01:05:58.393000+00:00" } }`For more information, see [Creating a subscriber with query access](https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-query-access.html#create-query-subscriber-procedures)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [CreateSubscriber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-subscriber.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-aws-log-source`.

- **AWS CLI**
- 
            
                    **To remove a natively-supported AWS service.**The following `delete-aws-logsource`example deletes VPC Flow Logs as a Security Lake source in the designated accounts and Regions.`aws securitylake delete-aws-log-source \ --sources '``[{"regions": ["us-east-1"], "accounts": ["123456789012"], "sourceName": "SH_FINDINGS", "sourceVersion": "2.0"}]`'Output: `{ "failed": [ "123456789012" ] }`For more information, see [Removing an AWS service as a source](https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html#remove-internal-sources)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [DeleteAwsLogSource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-aws-log-source.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-custom-log-source`.

- **AWS CLI**
- 
            
                    **To remove a custom source.**The following `delete-custom-logsource`example deletes a custom source in the designated log provider account in the designated Region.`aws securitylake delete-custom-log-source \ --source-name``"CustomSourceName"`This command produces no output. For more information, see [Deleting a custom source](https://docs.aws.amazon.com/security-lake/latest/userguide/custom-sources.html#delete-custom-source)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [DeleteCustomLogSource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-custom-log-source.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-data-lake-organization-configuration`.

- **AWS CLI**
- 
            
                    **To stop automatic source collection in member accounts**The following `delete-data-lake-organization-configuration`example stops the automatic collection of AWS Security Hub findings from new member accounts that join the organization. Only the delegated Security Lake administrator can run this command. It prevents new member accounts from automatically contributing data to the data lake.`aws securitylake delete-data-lake-organization-configuration \ --auto-enable-new-account '``[{"region":"us-east-1","sources":[{"sourceName":"SH_FINDINGS"}]}]`'This command produces no output. For more information, see [Managing multiple accounts with AWS Organizations](https://docs.aws.amazon.com/securityhub/latest/userguide/multi-account-management.html)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [DeleteDataLakeOrganizationConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-data-lake-organization-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-data-lake`.

- **AWS CLI**
- 
            
                    **To disable your data lake**The following `delete-data-lake`example disables your data lake in the specified AWS Regions. In the specified Regions, sources no longer contribute data to the data lake. For a Security Lake deployment utilizing AWS Organizations, only the delegated Security Lake administrator for the organization can disable Security Lake for accounts in the organization.`aws securitylake delete-data-lake \ --regions``"ap-northeast-1"``"eu-central-1"`This command produces no output. For more information, see [Disabling Amazon Security Lake](https://docs.aws.amazon.com/securityhub/latest/userguide/disable-security-lake.html)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [DeleteDataLake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-data-lake.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-subscriber-notification`.

- **AWS CLI**
- 
            
                    **To delete a subscriber notification**The following `delete-subscriber-notification`example shows how to delete the subscriber notification for specific Security Lake subscriber.`aws securitylake delete-subscriber-notification \ --subscriber-id``"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"`This command produces no output. For more information, see [Subscriber management](https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-management.html)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [DeleteSubscriberNotification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-subscriber-notification.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-subscriber`.

- **AWS CLI**
- 
            
                    **To delete a subscriber**The following `delete-subscriber`example shows how to remove a subscriber if you no longer want a subscriber to consume data from Security Lake.`aws securitylake delete-subscriber \ --subscriber-id``"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"`This command produces no output. For more information, see [Subscriber management](https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-management.html)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [DeleteSubscriber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-subscriber.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-data-lake-exception-subscription`.

- **AWS CLI**
- 
            
                    **To get details about an exception subscription**The following `get-data-lake-exception-subscription`example provides details about a Security Lake exception subscription. In this example, the user of the specified AWS account is notified of errors through SMS delivery. The exception message remains in the account for the specified time period. An exception subscription notifies a Security Lake user about an error through the requester's preferred protocol.`aws securitylake get-data-lake-exception-subscription`Output: `{ "exceptionTimeToLive": 30, "notificationEndpoint": "123456789012", "subscriptionProtocol": "sms" }`For more information, see [Troubleshooting data lake status](https://docs.aws.amazon.com/securityhub/latest/userguide/security-lake-troubleshoot.html#securitylake-data-lake-troubleshoot)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [GetDataLakeExceptionSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/get-data-lake-exception-subscription.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-data-lake-organization-configuration`.

- **AWS CLI**
- 
            
                    **To get details about the configuration for new organization accounts**The following `get-data-lake-organization-configuration`example retrieves details about the source logs that new organization accounts will send after onboarding to Amazon Security Lake.`aws securitylake get-data-lake-organization-configuration`Output: `{ "autoEnableNewAccount": [ { "region": "us-east-1", "sources": [ { "sourceName": "VPC_FLOW", "sourceVersion": "1.0" }, { "sourceName": "ROUTE53", "sourceVersion": "1.0" }, { "sourceName": "SH_FINDINGS", "sourceVersion": "1.0" } ] } ] }`For more information, see [Managing multiple accounts with AWS Organizations](https://docs.aws.amazon.com/security-lake/latest/userguide/multi-account-management.html)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [GetDataLakeOrganizationConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/get-data-lake-organization-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-data-lake-sources`.

- **AWS CLI**
- 
            
                    **To get the status of log collection**The following `get-data-lake-sources`example gets a snapshot of log collection for the specified account in the current AWS Region. The account has Amazon Security Lake enabled.`aws securitylake get-data-lake-sources \ --accounts``"123456789012"`Output: `{ "dataLakeSources": [ { "account": "123456789012", "sourceName": "SH_FINDINGS", "sourceStatuses": [ { "resource": "vpc-1234567890abcdef0", "status": "COLLECTING" } ] }, { "account": "123456789012", "sourceName": "VPC_FLOW", "sourceStatuses": [ { "resource": "vpc-1234567890abcdef0", "status": "NOT_COLLECTING" } ] }, { "account": "123456789012", "sourceName": "LAMBDA_EXECUTION", "sourceStatuses": [ { "resource": "vpc-1234567890abcdef0", "status": "COLLECTING" } ] }, { "account": "123456789012", "sourceName": "ROUTE53", "sourceStatuses": [ { "resource": "vpc-1234567890abcdef0", "status": "COLLECTING" } ] }, { "account": "123456789012", "sourceName": "CLOUD_TRAIL_MGMT", "sourceStatuses": [ { "resource": "vpc-1234567890abcdef0", "status": "COLLECTING" } ] } ], "dataLakeArn": null }`For more information, see [Collecting data from AWS services](https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [GetDataLakeSources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/get-data-lake-sources.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-subscriber`.

- **AWS CLI**
- 
            
                    **To retrieve the subscription information**The following `get-subscriber`example retrieves the subscription information for the specified Security Lake subscriber.`aws securitylake get-subscriber \ --subscriber-id``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "subscriber": { "accessTypes": [ "LAKEFORMATION" ], "createdAt": "2024-04-19T15:19:44.421803+00:00", "resourceShareArn": "arn:aws:ram:eu-west-2:123456789012:resource-share/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "resourceShareName": "LakeFormation-V3-TKJGBHCKTZ-123456789012", "sources": [ { "awsLogSource": { "sourceName": "LAMBDA_EXECUTION", "sourceVersion": "1.0" } }, { "awsLogSource": { "sourceName": "EKS_AUDIT", "sourceVersion": "2.0" } }, { "awsLogSource": { "sourceName": "ROUTE53", "sourceVersion": "1.0" } }, { "awsLogSource": { "sourceName": "SH_FINDINGS", "sourceVersion": "1.0" } }, { "awsLogSource": { "sourceName": "VPC_FLOW", "sourceVersion": "1.0" } }, { "customLogSource": { "attributes": { "crawlerArn": "arn:aws:glue:eu-west-2:123456789012:crawler/testCustom2", "databaseArn": "arn:aws:glue:eu-west-2:123456789012:database/amazon_security_lake_glue_db_eu_west_2", "tableArn": "arn:aws:glue:eu-west-2:123456789012:table/amazon_security_lake_table_eu_west_2_ext_testcustom2" }, "provider": { "location": "s3://aws-security-data-lake-eu-west-2-8ugsus4ztnsfpjbldwbgf4vge98av9/ext/testCustom2/", "roleArn": "arn:aws:iam::123456789012:role/AmazonSecurityLake-Provider-testCustom2-eu-west-2" }, "sourceName": "testCustom2" } }, { "customLogSource": { "attributes": { "crawlerArn": "arn:aws:glue:eu-west-2:123456789012:crawler/TestCustom", "databaseArn": "arn:aws:glue:eu-west-2:123456789012:database/amazon_security_lake_glue_db_eu_west_2", "tableArn": "arn:aws:glue:eu-west-2:123456789012:table/amazon_security_lake_table_eu_west_2_ext_testcustom" }, "provider": { "location": "s3://aws-security-data-lake-eu-west-2-8ugsus4ztnsfpjbldwbgf4vge98av9/ext/TestCustom/", "roleArn": "arn:aws:iam::123456789012:role/AmazonSecurityLake-Provider-TestCustom-eu-west-2" }, "sourceName": "TestCustom" } } ], "subscriberArn": "arn:aws:securitylake:eu-west-2:123456789012:subscriber/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "subscriberId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "subscriberIdentity": { "externalId": "123456789012", "principal": "123456789012" }, "subscriberName": "test", "subscriberStatus": "ACTIVE", "updatedAt": "2024-04-19T15:19:55.230588+00:00" } }`For more information, see [Subscriber management](https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-management.html)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [GetSubscriber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/get-subscriber.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-data-lake-exceptions`.

- **AWS CLI**
- 
            
                    **To list the issues affecting your data lake**The following `list-data-lake-exceptions`example lists the issues that are affecting your data lake in the last 14 days in the specified AWS Regions.`aws securitylake list-data-lake-exceptions \ --regions``"us-east-1"``"eu-west-3"`Output: `{ "exceptions": [ { "exception": "The account does not have the required role permissions. Update your role permissions to use the new data source version.", "region": "us-east-1", "timestamp": "2024-02-29T12:24:15.641725+00:00" }, { "exception": "The account does not have the required role permissions. Update your role permissions to use the new data source version.", "region": "eu-west-3", "timestamp": "2024-02-29T12:24:15.641725+00:00" } ] }`For more information, see [Troubleshooting Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/security-lake-troubleshoot.html#securitylake-data-lake-troubleshoot)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [ListDataLakeExceptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/list-data-lake-exceptions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-data-lakes`.

- **AWS CLI**
- 
            
                    **To list the Security Lake configuration object**The following `list-data-lakes`example lists the Amazon Security Lake configuration object for the specified AWS Region. You can use this command to determine whether Security Lake is enabled in a specified Region or Regions.`aws securitylake list-data-lakes \ --regions``"us-east-1"`Output: `{ "dataLakes": [ { "createStatus": "COMPLETED", "dataLakeArn": "arn:aws:securitylake:us-east-1:123456789012:data-lake/default", "encryptionConfiguration": { "kmsKeyId": "S3_MANAGED_KEY" }, "lifecycleConfiguration": { "expiration": { "days": 365 }, "transitions": [ { "days": 60, "storageClass": "ONEZONE_IA" } ] }, "region": "us-east-1", "replicationConfiguration": { "regions": [ "ap-northeast-3" ], "roleArn": "arn:aws:securitylake:ap-northeast-3:123456789012:data-lake/default" }, "s3BucketArn": "arn:aws:s3:::aws-security-data-lake-us-east-1-1234567890abcdef0", "updateStatus": { "exception": { "code": "software.amazon.awssdk.services.s3.model.S3Exception", "reason": "" }, "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "status": "FAILED" } } ] }`For more information, see [Checking Region status](https://docs.aws.amazon.com/security-lake/latest/userguide/manage-regions.html#check-region-status)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [ListDataLakes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/list-data-lakes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-log-sources`.

- **AWS CLI**
- 
            
                    **To retrieve the Amazon Security Lake log sources**The following `list-log-sources`example lists the Amazon Security Lake log sources in a specified account.`aws securitylake list-log-sources \ --accounts``"123456789012"`Output: `{ "account": "123456789012", "region": "xy-region-1", "sources": [ { "awsLogSource": { "sourceName": "VPC_FLOW", "sourceVersion": "2.0" } }, { "awsLogSource": { "sourceName": "SH_FINDINGS", "sourceVersion": "2.0" } } ] }`For more information, see [Source management](https://docs.aws.amazon.com/security-lake/latest/userguide/source-management.html)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [ListLogSources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/list-log-sources.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-subscribers`.

- **AWS CLI**
- 
            
                    **To retrieve the Amazon Security Lake subscribers**The following `list-subscribers`example lists all the Amazon Security Lake subscribers in a specific account.`aws securitylake list-subscribers`Output: `{ "subscribers": [ { "accessTypes": [ "S3" ], "createdAt": "2024-06-04T15:02:28.921000+00:00", "roleArn": "arn:aws:iam::123456789012:role/AmazonSecurityLake-E1WG1ZNPRXT0D4", "s3BucketArn": "amzn-s3-demo-bucket--usw2-az1--x-s3", "sources": [ { "awsLogSource": { "sourceName": "CLOUD_TRAIL_MGMT", "sourceVersion": "2.0" } }, { "awsLogSource": { "sourceName": "LAMBDA_EXECUTION", "sourceVersion": "1.0" } }, { "customLogSource": { "attributes": { "crawlerArn": "arn:aws:glue:eu-west-2:123456789012:crawler/E1WG1ZNPRXT0D4", "databaseArn": "arn:aws:glue:eu-west-2:123456789012:database/E1WG1ZNPRXT0D4", "tableArn": "arn:aws:glue:eu-west-2:123456789012:table/E1WG1ZNPRXT0D4" }, "provider": { "location": "amzn-s3-demo-bucket--usw2-az1--x-s3", "roleArn": "arn:aws:iam::123456789012:role/AmazonSecurityLake-E1WG1ZNPRXT0D4" }, "sourceName": "testCustom2" } } ], "subscriberArn": "arn:aws:securitylake:eu-west-2:123456789012:subscriber/E1WG1ZNPRXT0D4", "subscriberEndpoint": "arn:aws:sqs:eu-west-2:123456789012:AmazonSecurityLake-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111-Main-Queue", "subscriberId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "subscriberIdentity": { "externalId": "ext123456789012", "principal": "123456789012" }, "subscriberName": "Test", "subscriberStatus": "ACTIVE", "updatedAt": "2024-06-04T15:02:35.617000+00:00" } ] }`For more information, see [Subscriber management](https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-management.html)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [ListSubscribers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/list-subscribers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list tags for an existing resource**The following `list-tags-for-resource`example lists tags for the specified Amazon Security Lake subscriber. In this example, the Owner tag key doesn't have an associated tag value. You can use this operation to list tags for other existing Security Lake resources as well.`aws securitylake list-tags-for-resource \ --resource-arn``"arn:aws:securitylake:us-east-1:123456789012:subscriber/1234abcd-12ab-34cd-56ef-1234567890ab"`Output: `{ "tags": [ { "key": "Environment", "value": "Cloud" }, { "key": "CostCenter", "value": "12345" }, { "key": "Owner", "value": "" } ] }`For more information, see [Tagging Amazon Security Lake resources](https://docs.aws.amazon.com/security-lake/latest/userguide/tagging-resources.html#tags-retrieve)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-data-lake-delegated-administrator`.

- **AWS CLI**
- 
            
                    **To designate the delegated administratore**The following `register-data-lake-delegated-administrator`example designates the specified AWS account as the delegated Amazon Security Lake administrator.`aws securitylake register-data-lake-delegated-administrator \ --account-id``123456789012`This command produces no output. For more information, see [Managing multiple accounts with AWS Organizations](https://docs.aws.amazon.com/security-lake/latest/userguide/multi-account-management.html)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [RegisterDataLakeDelegatedAdministrator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/register-data-lake-delegated-administrator.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add tags to an existing resource**The following `tag-resource`example add tags to an existing subscriber resource. To create a new resource and add one or more tags to it, don't use this operation. Instead, use the appropriate Create operation for the the type of resource that you want to create.`aws securitylake tag-resource \ --resource-arn``"arn:aws:securitylake:us-east-1:123456789012:subscriber/1234abcd-12ab-34cd-56ef-1234567890ab"`\ --tags`key=Environment,value=Cloud`This command produces no output. For more information, see [Tagging Amazon Security Lake resources](https://docs.aws.amazon.com/security-lake/latest/userguide/tagging-resources.html#tags-retrieve)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove tags from an existing resource**The following `untag-resource`example removes the specified tags from an existing subscriber resource.`aws securitylake untag-resource \ --resource-arn``"arn:aws:securitylake:us-east-1:123456789012:subscriber/1234abcd-12ab-34cd-56ef-1234567890ab"`\ --tag-keys`Environment``Owner`This command produces no output. For more information, see [Tagging Amazon Security Lake resources](https://docs.aws.amazon.com/security-lake/latest/userguide/tagging-resources.html#tags-retrieve)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-data-lake-exception-subscription`.

- **AWS CLI**
- 
            
                    **To update notification subscription for Security Lake exceptions**The following `update-data-lake-exception-subscription`example updates the notification subscription that notifies users of Security Lake exceptions.`aws securitylake update-data-lake-exception-subscription \ --notification-endpoint``"123456789012"`\ --exception-time-to-live`30`\ --subscription-protocol`"email"`This command produces no output. For more information, see [Troubleshooting Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/security-lake-troubleshoot.html#securitylake-data-lake-troubleshoot)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [UpdateDataLakeExceptionSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/update-data-lake-exception-subscription.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-data-lake`.

- **AWS CLI**
- 
            
                    **Example 1: To update your data lake settings**The following `update-data-lake`example updates the settings of your Amazon Security Lake data lake. You can use this operation to specify data encryption, storage, and rollup Region settings.`aws securitylake update-data-lake \ --configurations '``[{"encryptionConfiguration": {"kmsKeyId":"S3_MANAGED_KEY"},"region":"us-east-1","lifecycleConfiguration": {"expiration":{"days":365},"transitions":[{"days":60,"storageClass":"ONEZONE_IA"}]}}, {"encryptionConfiguration": {"kmsKeyId":"S3_MANAGED_KEY"},"region":"us-east-2","lifecycleConfiguration": {"expiration":{"days":365},"transitions":[{"days":60,"storageClass":"ONEZONE_IA"}]}}]`' \ --meta-store-manager-role-arn`"arn:aws:iam:us-east-1:123456789012:role/service-role/AmazonSecurityLakeMetaStoreManager"`Output: `{ "dataLakes": [ { "createStatus": "COMPLETED", "dataLakeArn": "arn:aws:securitylake:us-east-1:522481757177:data-lake/default", "encryptionConfiguration": { "kmsKeyId": "S3_MANAGED_KEY" }, "lifecycleConfiguration": { "expiration": { "days": 365 }, "transitions": [ { "days": 60, "storageClass": "ONEZONE_IA" } ] }, "region": "us-east-1", "replicationConfiguration": { "regions": [ "ap-northeast-3" ], "roleArn": "arn:aws:securitylake:ap-northeast-3:522481757177:data-lake/default" }, "s3BucketArn": "arn:aws:s3:::aws-security-data-lake-us-east-1-gnevt6s8z7bzby8oi3uiaysbr8v2ml", "updateStatus": { "exception": {}, "requestId": "f20a6450-d24a-4f87-a6be-1d4c075a59c2", "status": "INITIALIZED" } }, { "createStatus": "COMPLETED", "dataLakeArn": "arn:aws:securitylake:us-east-2:522481757177:data-lake/default", "encryptionConfiguration": { "kmsKeyId": "S3_MANAGED_KEY" }, "lifecycleConfiguration": { "expiration": { "days": 365 }, "transitions": [ { "days": 60, "storageClass": "ONEZONE_IA" } ] }, "region": "us-east-2", "replicationConfiguration": { "regions": [ "ap-northeast-3" ], "roleArn": "arn:aws:securitylake:ap-northeast-3:522481757177:data-lake/default" }, "s3BucketArn": "arn:aws:s3:::aws-security-data-lake-us-east-2-cehuifzl5rwmhm6m62h7zhvtseogr9", "updateStatus": { "exception": {}, "requestId": "f20a6450-d24a-4f87-a6be-1d4c075a59c2", "status": "INITIALIZED" } } ] }`For more information, see [Getting started with Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/getting-started.html)in the*Amazon Security Lake User Guide*.**Example 2: To configure your data lake in a single Region**The following `create-data-lake`example enables Amazon Security Lake in a single AWS Region and configures your data lake.`aws securitylake create-data-lake \ --configurations '``[{"encryptionConfiguration": {"kmsKeyId":"1234abcd-12ab-34cd-56ef-1234567890ab"},"region":"us-east-2","lifecycleConfiguration": {"expiration":{"days":500},"transitions":[{"days":30,"storageClass":"GLACIER"}]}}]`' \ --meta-store-manager-role-arn`"arn:aws:iam:us-east-1:123456789012:role/service-role/AmazonSecurityLakeMetaStoreManager"`Output: `{ "dataLakes": [ { "createStatus": "COMPLETED", "dataLakeArn": "arn:aws:securitylake:us-east-2:522481757177:data-lake/default", "encryptionConfiguration": { "kmsKeyId": "1234abcd-12ab-34cd-56ef-1234567890ab" }, "lifecycleConfiguration": { "expiration": { "days": 500 }, "transitions": [ { "days": 30, "storageClass": "GLACIER" } ] }, "region": "us-east-2", "replicationConfiguration": { "regions": [ "ap-northeast-3" ], "roleArn": "arn:aws:securitylake:ap-northeast-3:522481757177:data-lake/default" }, "s3BucketArn": "arn:aws:s3:::aws-security-data-lake-us-east-2-cehuifzl5rwmhm6m62h7zhvtseogr9", "updateStatus": { "exception": {}, "requestId": "77702a53-dcbf-493e-b8ef-518e362f3003", "status": "INITIALIZED" } } ] }`For more information, see [Getting started with Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/getting-started.html)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [UpdateDataLake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/update-data-lake.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-subscriber-notification`.

- **AWS CLI**
- 
            
                    **To update a subscriber notification**The following `update-subscriber-notification`example shows how you can update the notification method for a subscriber.`aws securitylake update-subscriber-notification \ --subscriber-id``"12345ab8-1a34-1c34-1bd4-12345ab9012"`\ --configuration '`{"httpsNotificationConfiguration": {"targetRoleArn":"arn:aws:iam::XXX:role/service-role/RoleName", "endpoint":"https://account-management.$3.$2.securitylake.aws.dev/v1/datalake"}}`'Output: `{ "subscriberEndpoint": [ "https://account-management.$3.$2.securitylake.aws.dev/v1/datalake" ] }`For more information, see [Subscriber management](https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-management.html)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [UpdateSubscriberNotification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/update-subscriber-notification.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-subscriber`.

- **AWS CLI**
- 
            
                    **To update an Amazon Security Lake subscriber.**The following `update-subscriber`example updates the security lake data access sources for a specific Security Lake subscriber.`aws securitylake update-subscriber \ --subscriber-id``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "subscriber": { "accessTypes": [ "LAKEFORMATION" ], "createdAt": "2024-04-19T15:19:44.421803+00:00", "resourceShareArn": "arn:aws:ram:eu-west-2:123456789012:resource-share/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "resourceShareName": "LakeFormation-V3-TKJGBHCKTZ-123456789012", "sources": [ { "awsLogSource": { "sourceName": "LAMBDA_EXECUTION", "sourceVersion": "1.0" } }, { "awsLogSource": { "sourceName": "EKS_AUDIT", "sourceVersion": "2.0" } }, { "awsLogSource": { "sourceName": "ROUTE53", "sourceVersion": "1.0" } }, { "awsLogSource": { "sourceName": "SH_FINDINGS", "sourceVersion": "1.0" } }, { "awsLogSource": { "sourceName": "VPC_FLOW", "sourceVersion": "1.0" } }, { "customLogSource": { "attributes": { "crawlerArn": "arn:aws:glue:eu-west-2:123456789012:crawler/E1WG1ZNPRXT0D4", "databaseArn": "arn:aws:glue:eu-west-2:123456789012:database/E1WG1ZNPRXT0D4", "tableArn": "arn:aws:glue:eu-west-2:123456789012:table/E1WG1ZNPRXT0D4" }, "provider": { "location": "amzn-s3-demo-bucket--usw2-az1--x-s3", "roleArn": "arn:aws:iam::123456789012:role/AmazonSecurityLake-E1WG1ZNPRXT0D4" }, "sourceName": "testCustom2" } } ], "subscriberArn": "arn:aws:securitylake:eu-west-2:123456789012:subscriber/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "subscriberId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "subscriberIdentity": { "externalId": "123456789012", "principal": "123456789012" }, "subscriberName": "test", "subscriberStatus": "ACTIVE", "updatedAt": "2024-07-18T20:47:37.098000+00:00" } }`For more information, see [Subscriber management](https://docs.aws.amazon.com/security-lake/latest/userguide/subscriber-management.html)in the*Amazon Security Lake User Guide*.- 
                    For API details, see [UpdateSubscriber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/update-subscriber.html)in*AWS CLI Command Reference*.
 
-