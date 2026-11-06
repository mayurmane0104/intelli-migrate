# AWS IoT examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_iot_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_iot_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS IoT.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `accept-certificate-transfer`.

- **AWS CLI**
- 
            
                    **To accept a device certificate transferred from a different AWS account**The following `accept-certificate-transfer`example accepts a device certificate transferred from another AWS account. The certificate is identified by its ID.`aws iot accept-certificate-transfer \ --certificate-id``488b6a7f2acdeb00a77384e63c4e40b18bEXAMPLEe57b7272ba44c45e3448142`This command does not produce any output. For more information, see [Transfer a certificate to another account](https://docs.aws.amazon.com/iot/latest/developerguide/transfer-cert.html)in the*AWS IoT Core Developer Guide*.- 
                    For API details, see [AcceptCertificateTransfer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/accept-certificate-transfer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `add-thing-to-billing-group`.

- **AWS CLI**
- 
            
                    **Example 1: To add a thing by name to a billing group**The following `add-thing-to-billing-group`example adds the thing named`MyLightBulb`to the billing group named`GroupOne`.`aws iot add-thing-to-billing-group \ --billing-group-name``GroupOne`\ --thing-name`MyLightBulb`This command produces no output. **Example 2: To add a thing by ARN to a billing group**The following `add-thing-to-billing-group`example adds a thing with a specified ARN to a billing group with the specified ARN. Specifying an ARN is helpful if you work with multiple AWS Regions or accounts. It can help ensure that you are adding to the right Region and account.`aws iot add-thing-to-thing-group \ --billing-group-arn``"arn:aws:iot:us-west-2:123456789012:billinggroup/GroupOne"`\ --thing-arn`"arn:aws:iot:us-west-2:123456789012:thing/MyOtherLightBulb"`This command produces no output. For more information, see [Billing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/tagging-iot-billing-groups.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [AddThingToBillingGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/add-thing-to-billing-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `add-thing-to-thing-group`.

- **AWS CLI**
- 
            
                    **To add a thing to a group**The following `add-thing-to-thing-group`example adds the specified thing to the specified thing group.`aws iot add-thing-to-thing-group \ --thing-name``MyLightBulb`\ --thing-group-name`LightBulbs`This command produces no output. For more information, see [Thing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/thing-groups.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [AddThingToThingGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/add-thing-to-thing-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-targets-with-job`.

- **AWS CLI**
- 
            
                    **To associate a thing group with a continuous job**The following `associate-targets-with-job`example associates the specified thing group with the specified continuous job.`aws iot associate-targets-with-job \ --targets``"arn:aws:iot:us-west-2:123456789012:thinggroup/LightBulbs"`\ --job-id`"example-job-04"`Output: `{ "jobArn": "arn:aws:iot:us-west-2:123456789012:job/example-job-04", "jobId": "example-job-04", "description": "example continuous job" }`For more information, see [Creating and Managing Jobs (CLI)](https://docs.aws.amazon.com/iot/latest/developerguide/manage-job-cli.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [AssociateTargetsWithJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/associate-targets-with-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `attach-policy`.

- **AWS CLI**
- 
            
                    **Example 1: To attach a policy to a thing group**The following `attach-policy`example attaches the specified policy to a thing group identified by its ARN.`aws iot attach-policy \ --target``"arn:aws:iot:us-west-2:123456789012:thinggroup/LightBulbs"`\ --policy-name`"UpdateDeviceCertPolicy"`This command does not produce any output. For more information, see [Thing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/thing-groups.html)in the*AWS IoT Developers Guide*.**Example 2: To attach a policy to a certificate**The following `attach-policy`example attaches the policy`UpdateDeviceCertPolicy`to the principal specified by a certificate.`aws iot attach-policy \ --policy-name``UpdateDeviceCertPolicy`\ --target`"arn:aws:iot:us-west-2:123456789012:cert/4f0ba725787aa94d67d2fca420eca022242532e8b3c58e7465c7778b443fd65e"`This command does not produce any output. For more information, see [Attach an AWS IoT Policy to a Device Certificate](https://docs.aws.amazon.com/iot/latest/developerguide/attach-policy-to-certificate.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [AttachPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/attach-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `attach-security-profile`.

- **AWS CLI**
- 
            
                    **To associate a security profile with all unregistered devices**The following `attach-security-profile`example associates the AWS IoT Device Defender security profile named`Testprofile`with all unregistered devices in the`us-west-2`region for this AWS account.`aws iot attach-security-profile \ --security-profile-name``Testprofile`\ --security-profile-target-arn`"arn:aws:iot:us-west-2:123456789012:all/unregistered-things"`This command produces no output. For more information, see [Detect Commands](https://docs.aws.amazon.com/iot/latest/developerguide/DetectCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [AttachSecurityProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/attach-security-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `attach-thing-principal`.

- **AWS CLI**
- 
            
                    **To attach a certificate to your thing**The following `attach-thing-principal`example attaches a certificate to the MyTemperatureSensor thing. The certificate is identified by an ARN. You can find the ARN for a certificate in the AWS IoT console.`aws iot attach-thing-principal \ --thing-name``MyTemperatureSensor`\ --principal`arn:aws:iot:us-west-2:123456789012:cert/2e1eb273792174ec2b9bf4e9b37e6c6c692345499506002a35159767055278e8`This command produces no output. For more information, see [How to Manage Things with the Registry](https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [AttachThingPrincipal](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/attach-thing-principal.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-audit-mitigation-actions-task`.

- **AWS CLI**
- 
            
                    **To cancel an audit mitigation actions task**The following `cancel-audit-mitigations-action-task`example cancels the application of mitigation actions for the specified task. You cannot cancel tasks that are already completed.`aws iot cancel-audit-mitigation-actions-task --task-id``"myActionsTaskId"`This command produces no output. For more information, see [CancelAuditMitigationActionsTask (Mitigation Action Commands)](https://docs.aws.amazon.com/iot/latest/developerguide/mitigation-action-commands.html#dd-api-iot-CancelAuditMitigationActionsTask)in the*AWS IoT Developer Guide*.- 
                    For API details, see [CancelAuditMitigationActionsTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/cancel-audit-mitigation-actions-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-audit-task`.

- **AWS CLI**
- 
            
                    **To cancel an audit task**The following `cancel-audit-task`example cancels an audit task with the specified task ID. You cannot cancel a task that is complete.`aws iot cancel-audit-task \ --task-id``a3aea009955e501a31b764abe1bebd3d`This command produces no output. For more information, see [Audit Commands](https://docs.aws.amazon.com/iot/latest/developerguide/AuditCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [CancelAuditTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/cancel-audit-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-certificate-transfer`.

- **AWS CLI**
- 
            
                    **To cancel the transfer a certificate to a different AWS account**The following `cancel-certificate-transfer`example cancels the transfer of the specified certificate transfer. The certificate is identified by a certificate ID. You can find the ID for a certificate in the AWS IoT console.`aws iot cancel-certificate-transfer \ --certificate-id``f0f33678c7c9a046e5cc87b2b1a58dfa0beec26db78addd5e605d630e05c7fc8`This command produces no output. For more information, see [Transfer a certificate to another account](https://docs.aws.amazon.com/iot/latest/developerguide/transfer-cert.html)in the*AWS IoT Core Developer Guide*.- 
                    For API details, see [CancelCertificateTransfer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/cancel-certificate-transfer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-job-execution`.

- **AWS CLI**
- 
            
                    **To cancel a job execution on a device**The following `cancel-job-execution`example cancels the execution of the specified job on a device. If the job is not in the`QUEUED`state, you must add the`--force`parameter.`aws iot cancel-job-execution \ --job-id``"example-job-03"`\ --thing-name`"MyRPi"`This command produces no output. For more information, see [Creating and Managing Jobs (CLI)](https://docs.aws.amazon.com/iot/latest/developerguide/manage-job-cli.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [CancelJobExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/cancel-job-execution.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-job`.

- **AWS CLI**
- 
            
                    **To cancel a job**The following `cancel-job`example cancels the specified job.`aws iot cancel-job \ --job-id``"example-job-03"`Output: `{ "jobArn": "arn:aws:iot:us-west-2:123456789012:job/example-job-03", "jobId": "example-job-03", "description": "example job test" }`For more information, see [Creating and Managing Jobs (CLI)](https://docs.aws.amazon.com/iot/latest/developerguide/manage-job-cli.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [CancelJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/cancel-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `clear-default-authorizer`.

- **AWS CLI**
- 
            
                    **To clear the default authorizer**The following `clear-default-authorizer`example clears the currently configured default custom authorizer. After you run this command, there is no default authorizer. When you use a custom authorizer, you must specify it by name in the HTTP request headers.`aws iot clear-default-authorizer`This command produces no output. For more information, see [ClearDefaultAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_ClearDefaultAuthorizer.html)in the*AWS IoT API Reference*.- 
                    For API details, see [ClearDefaultAuthorizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/clear-default-authorizer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `confirm-topic-rule-destination`.

- **AWS CLI**
- 
            
                    **To confirm a topic rule destination**The following `confirm-topic-rule-destination`example confirms a topic rule destination with a confirmation token received at an HTTP endpoint.`aws iot confirm-topic-rule-destination \ --confirmation-token``"AYADeIcmtq-ZkxfpiWIQqHWM5ucAXwABABVhd3MtY3J5cHRvLXB1YmxpYy1rZXkAREFxY1E0UmlGeDg0V21BZWZ1VjZtZWFRVUJJUktUYXJaN09OZlJOczJhRENSZmZYL3JHZC9PR3NNcis5T3ZlSitnQT09AAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo5ODc5NTE4NTI0OTk6a2V5L2U4YmU3ODViLTU5NWMtNDcxYi1iOWJmLWQ2Y2I4ZjQxODlmNwC4AQIBAHhwz48UWTGWE1ua0P8U1hj27nsFzEaAdf6Hs2K_7wBheAF62zwMuk_A4dPiC6eyPGuMAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQM9vtRMpf9D3CiZ8sMAgEQgDuFd0Txy-aywpPqg8YEsa1lD4B40aJ2s1wEHKMybiF1RoOZzYisI0IvslzQY5UmCkqq3tV-3f7-nKfosgIAAAAADAAAEAAAAAAAAAAAAAAAAAAi9RMgy-V19V9m6Iw2xfbw_____wAAAAEAAAAAAAAAAAAAAAEAAAB1hw4SokgUcxiJ3gTO6n50NLJVpzyQR1UmPIj5sShqXEQGcOsWmXzpYOOx_PWyPVNsIFHApyK7Cc3g4bW8VaLVwOLkC83g6YaZAh7dFEl2-iufgrzTePl8RZYOWr0O6Aj9DiVzJZx-1iD6Pu-G6PUw1kaO7Knzs2B4AD0qfrHUF4pYRTvyUgBnMGUCMQC8ZRmhKqntd_c6Kgrow3bMUDBvNqo2qZr8Z8Jm2rzgseROlAnLgFLGpGShr99oSZkCMEd1v62NBRKX9HQXnybyF3fkg__-PIetJ803Z4IlIlF8xXlcdPGP-PV1dOXFemyL8g"`This command produces no output. For more information, see [Confirming a topic rule destination](https://docs.aws.amazon.com/iot/latest/developerguide/rule-destination.html#confirm-destination)in the*AWS IoT Developer Guide*.- 
                    For API details, see [ConfirmTopicRuleDestination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/confirm-topic-rule-destination.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-audit-suppression`.

- **AWS CLI**
- 
            
                    **To create an audit finding suppression**The following `create-audit-suppression`example creates an audit finding suppression for a policy named "virtualMachinePolicy" that has been flagged for being overly permissive.`aws iot create-audit-suppression \ --check-name``IOT_POLICY_OVERLY_PERMISSIVE_CHECK`\ --resource-identifier policyVersionIdentifier={"policyName"="virtualMachinePolicy","policyVersionId"="1"} \ --no-suppress-indefinitely \ --expiration-date`2020-10-20`This command produces no output. For more information, see [Audit finding suppressions](https://docs.aws.amazon.com/iot/latest/developerguide/audit-finding-suppressions.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [CreateAuditSuppression](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-audit-suppression.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-authorizer`.

- **AWS CLI**
- 
            
                    **To create a custom authorizer**The following `create-authorizer`example creates a custom authorizer that uses the specified Lambda function as part of a custom authentication service.`aws iot create-authorizer \ --authorizer-name "CustomAuthorizer" \ --authorizer-function-arn "arn:aws:lambda:us-west-2:123456789012:function:CustomAuthorizerFunction" \ --token-key-name "MyAuthToken" \ --status ACTIVE \ --token-signing-public-keys FIRST_KEY="-----BEGIN PUBLIC KEY----- MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1uJOB4lQPgG/lM6ZfIwo Z+7ENxAio9q6QD4FFqjGZsvjtYwjoe1RKK0U8Eq9xb5O3kRSmyIwTzwzm/f4Gf0Y ZUloJ+t3PUUwHrmbYTAgTrCUgRFygjfgVwGCPs5ZAX4Eyqt5cr+AIHIiUDbxSa7p zwOBKPeic0asNJpqT8PkBbRaKyleJh5oo81NDHHmVtbBm5A5YiJjqYXLaVAowKzZ +GqsNvAQ9Jy1wI2VrEa1OfL8flDB/BJLm7zjpfPOHDJQgID0XnZwAlNnZcOhCwIx 50g2LW2Oy9R/dmqtDmJiVP97Z4GykxPvwlYHrUXY0iW1R3AR/Ac1NhCTGZMwVDB1 lQIDAQAB -----END PUBLIC KEY-----"`Output: `{ "authorizerName": "CustomAuthorizer", "authorizerArn": "arn:aws:iot:us-west-2:123456789012:authorizer/CustomAuthorizer2" }`For more information, see [CreateAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateAuthorizer.html)in the*AWS IoT API Reference*.- 
                    For API details, see [CreateAuthorizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-authorizer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-billing-group`.

- **AWS CLI**
- 
            
                    **To create a billing group**The following `create-billing-group`example creates a simple billing group named`GroupOne`.`aws iot create-billing-group \ --billing-group-name``GroupOne`Output: `{ "billingGroupName": "GroupOne", "billingGroupArn": "arn:aws:iot:us-west-2:123456789012:billinggroup/GroupOne", "billingGroupId": "103de383-114b-4f51-8266-18f209ef5562" }`For more information, see [Billing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/tagging-iot-billing-groups.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [CreateBillingGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-billing-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-certificate-from-csr`.

- **AWS CLI**
- 
            
                    **To create a device certificate from a certificate signing request (CSR)**The following `create-certificate-from-csr`example creates a device certificate from a CSR. You can use the`openssl`command to create a CSR.`aws iot create-certificate-from-csr \ --certificate-signing-request=file://certificate.csr`Output: `{ "certificateArn": "arn:aws:iot:us-west-2:123456789012:cert/c0c57bbc8baaf4631a9a0345c957657f5e710473e3ddbee1428d216d54d53ac9", "certificateId": "c0c57bbc8baaf4631a9a0345c957657f5e710473e3ddbee1428d216d54d53ac9", "certificatePem": "<certificate-text>" }`For more information, see [CreateCertificateFromCSR](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateCertificateFromCsr.html)in the*AWS IoT API Reference*.- 
                    For API details, see [CreateCertificateFromCsr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-certificate-from-csr.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-custom-metric`.

- **AWS CLI**
- 
            
                    **To create a custom metric published by your devices to Device Defender**The following `create-custom-metric`example creates a custom metric that measures battery percentage.`aws iot create-custom-metric \ --metric-name``"batteryPercentage"`\ --metric-type`"number"`\ --display-name`"Remaining battery percentage."`\ --region`us-east-1`\ --client-request-token`"02ccb92b-33e8-4dfa-a0c1-35b181ed26b0"`Output: `{ "metricName": "batteryPercentage", "metricArn": "arn:aws:iot:us-east-1:1234564789012:custommetric/batteryPercentage" }`For more information, see [Custom metrics](https://docs.aws.amazon.com/iot/latest/developerguide/dd-detect-custom-metrics.html)in the*AWS IoT Core Developer Guide*.- 
                    For API details, see [CreateCustomMetric](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-custom-metric.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-dimension`.

- **AWS CLI**
- 
            
                    **To create a dimension**The following `create-dimension`creates a dimension with a single topic filter called`TopicFilterForAuthMessages`.`aws iot create-dimension \ --name``TopicFilterForAuthMessages`\ --type`TOPIC_FILTER`\ --string-values`device/+/auth`Output: `{ "name": "TopicFilterForAuthMessages", "arn": "arn:aws:iot:eu-west-2:123456789012:dimension/TopicFilterForAuthMessages" }`For more information, see [Detect Commands](https://docs.aws.amazon.com/iot/latest/developerguide/DetectCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [CreateDimension](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-dimension.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-domain-configuration`.

- **AWS CLI**
- 
            
                    **To create a domain configuration**The following `create-domain-configuration`example creates an AWS-managed domain configuration with a service type of`DATA`.`aws iot create-domain-configuration \ --domain-configuration-name``"additionalDataDomain"`\ --service-type`"DATA"`Output: `{ "domainConfigurationName": "additionalDataDomain", "domainConfigurationArn": "arn:aws:iot:us-west-2:123456789012:domainconfiguration/additionalDataDomain/dikMh" }`For more information, see [Configurable Endpoints](https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-configurable-aws.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [CreateDomainConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-domain-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-dynamic-thing-group`.

- **AWS CLI**
- 
            
                    **To create a dynamic thing group**The following `create-dynamic-thing-group`example creates a dynamic thing group that contains any thing with a temperature attribute that is greater than 60 degrees. You must enable AWS IoT fleet indexing before you can use dynamic thing groups.`aws iot create-dynamic-thing-group \ --thing-group-name``"RoomTooWarm"`\ --query-string`"attributes.temperature>60"`Output: `{ "thingGroupName": "RoomTooWarm", "thingGroupArn": "arn:aws:iot:us-west-2:123456789012:thinggroup/RoomTooWarm", "thingGroupId": "9d52492a-fc87-43f4-b6e2-e571d2ffcad1", "indexName": "AWS_Things", "queryString": "attributes.temperature>60", "queryVersion": "2017-09-30" }`For more information, see [Dynamic Thing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/dynamic-thing-groups.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [CreateDynamicThingGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-dynamic-thing-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-job`.

- **AWS CLI**
- 
            
                    **Example 1: To create a job**The following `create-job`example creates a simple AWS IoT job that sends a JSON document to the`MyRaspberryPi`device.`aws iot create-job \ --job-id``"example-job-01"`\ --targets`"arn:aws:iot:us-west-2:123456789012:thing/MyRaspberryPi"`\ --document`file://example-job.json`\ --description`"example job test"`\ --target-selection`SNAPSHOT`Output: `{ "jobArn": "arn:aws:iot:us-west-2:123456789012:job/example-job-01", "jobId": "example-job-01", "description": "example job test" }`**Example 2: To create a continuous job**The following `create-job`example creates a job that continues to run after the things specified as targets have completed the job. In this example, the target is a thing group, so when new devices are added to the group, the continuous job runs on those new things.aws iot create-job --job-id "example-job-04" --targets "arn:aws:iot:us-west-2:123456789012:thinggroup/DeadBulbs" --document file://example-job.json --description "example continuous job" --target-selection CONTINUOUS Output: `{ "jobArn": "arn:aws:iot:us-west-2:123456789012:job/example-job-04", "jobId": "example-job-04", "description": "example continuous job" }`For more information, see [Creating and Managing Jobs (CLI)](https://docs.aws.amazon.com/iot/latest/developerguide/manage-job-cli.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [CreateJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-keys-and-certificate`.

- **AWS CLI**
- 
            
                    **To create an RSA key pair and issue an X.509 certificate**The following `create-keys-and-certificate`creates a 2048-bit RSA key pair and issues an X.509 certificate using the issued public key. Because this is the only time that AWS IoT provides the private key for this certificate, be sure to keep it in a secure location.`aws iot create-keys-and-certificate \ --certificate-pem-outfile``"myTest.cert.pem"`\ --public-key-outfile`"myTest.public.key"`\ --private-key-outfile`"myTest.private.key"`Output: `{ "certificateArn": "arn:aws:iot:us-west-2:123456789012:cert/9894ba17925e663f1d29c23af4582b8e3b7619c31f3fbd93adcb51ae54b83dc2", "certificateId": "9894ba17925e663f1d29c23af4582b8e3b7619c31f3fbd93adcb51ae54b83dc2", "certificatePem": " -----BEGIN CERTIFICATE----- MIICiTCCEXAMPLE6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC VVMxCzAJBgNVBAgEXAMPLEAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6 b24xFDASBgNVBAsTC0lBTSEXAMPLE2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd BgkqhkiG9w0BCQEWEG5vb25lQGFtYEXAMPLEb20wHhcNMTEwNDI1MjA0NTIxWhcN MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCEXAMPLEJBgNVBAgTAldBMRAwDgYD VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDAEXAMPLEsTC0lBTSBDb25z b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEXAMPLE25lQGFt YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+aEXAMPLE EXAMPLEfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T rDHudUZEXAMPLELG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE Ibb3OhjZnzcvQAEXAMPLEWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4 nUhVVxYUntneD9+h8Mg9qEXAMPLEyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb FFBjvSfpJIlJ00zbhNYS5f6GuoEDEXAMPLEBHjJnyp378OD8uTs7fLvjx79LjSTb NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE= -----END CERTIFICATE-----\n", "keyPair": { "PublicKey": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkEXAMPLEQEFAAOCAQ8AMIIBCgKCAQEAEXAMPLE1nnyJwKSMHw4h\nMMEXAMPLEuuN/dMAS3fyce8DW/4+EXAMPLEyjmoF/YVF/gHr99VEEXAMPLE5VF13\n59VK7cEXAMPLE67GK+y+jikqXOgHh/xJTwo+sGpWEXAMPLEDz18xOd2ka4tCzuWEXAMPLEahJbYkCPUBSU8opVkR7qkEXAMPLE1DR6sx2HocliOOLtu6Fkw91swQWEXAMPLE\GB3ZPrNh0PzQYvjUStZeccyNCx2EXAMPLEvp9mQOUXP6plfgxwKRX2fEXAMPLEDa\nhJLXkX3rHU2xbxJSq7D+XEXAMPLEcw+LyFhI5mgFRl88eGdsAEXAMPLElnI9EesG\nFQIDAQAB\n-----END PUBLIC KEY-----\n", "PrivateKey": "-----BEGIN RSA PRIVATE KEY-----\nkey omittted for security reasons\n-----END RSA PRIVATE KEY-----\n" } }`For more information, see [Create and Register an AWS IoT Device Certificate](https://docs.aws.amazon.com/iot/latest/developerguide/device-certs-create.html)in the**AWS IoT Developer Guide**.- 
                    For API details, see [CreateKeysAndCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-keys-and-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-mitigation-action`.

- **AWS CLI**
- 
            
                    **To create a mitigation action**The following `create-mitigation-action`example defines a mitigation action named`AddThingsToQuarantineGroup1Action`that, when applied, moves things into the thing group named`QuarantineGroup1`. This action overrides dynamic thing groups.`aws iot create-mitigation-action --cli-input-json``file::params.json`Contents of `params.json`:`{ "actionName": "AddThingsToQuarantineGroup1Action", "actionParams": { "addThingsToThingGroupParams": { "thingGroupNames": [ "QuarantineGroup1" ], "overrideDynamicGroups": true } }, "roleArn": "arn:aws:iam::123456789012:role/service-role/MoveThingsToQuarantineGroupRole" }`Output: `{ "actionArn": "arn:aws:iot:us-west-2:123456789012:mitigationaction/AddThingsToQuarantineGroup1Action", "actionId": "992e9a63-a899-439a-aa50-4e20c52367e1" }`For more information, see [CreateMitigationAction (Mitigation Action Commands)](https://docs.aws.amazon.com/iot/latest/developerguide/iot/latest/developerguide/iot/latest/developerguide/mitigation-action-commands.html.html#dd-api-iot-CreateMitigationAction)in the*AWS IoT Developer Guide*.- 
                    For API details, see [CreateMitigationAction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-mitigation-action.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-ota-update`.

- **AWS CLI**
- 
            
                    **To create an OTA update for use with Amazon FreeRTOS**The following `create-ota-update`example creates an AWS IoT OTAUpdate on a target group of things or groups. This is part of an Amazon FreeRTOS over-the-air update which makes it possible for you to deploy new firmware images to a single device or a group of devices.`aws iot create-ota-update \ --cli-input-json``file://create-ota-update.json`Contents of `create-ota-update.json`:`{ "otaUpdateId": "ota12345", "description": "A critical update needed right away.", "targets": [ "device1", "device2", "device3", "device4" ], "targetSelection": "SNAPSHOT", "awsJobExecutionsRolloutConfig": { "maximumPerMinute": 10 }, "files": [ { "fileName": "firmware.bin", "fileLocation": { "stream": { "streamId": "004", "fileId":123 } }, "codeSigning": { "awsSignerJobId": "48c67f3c-63bb-4f92-a98a-4ee0fbc2bef6" } } ] "roleArn": "arn:aws:iam:123456789012:role/service-role/my_ota_role" }`Output: `{ "otaUpdateId": "ota12345", "awsIotJobId": "job54321", "otaUpdateArn": "arn:aws:iot:us-west-2:123456789012:otaupdate/itsaupdate", "awsIotJobArn": "arn:aws:iot:us-west-2:123456789012:job/itsajob", "otaUpdateStatus": "CREATE_IN_PROGRESS" }`For more information, see [CreateOTAUpdate](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateOTAUpdate.html)in the*AWS IoT API Reference*.- 
                    For API details, see [CreateOtaUpdate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-ota-update.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-policy-version`.

- **AWS CLI**
- 
            
                    **To update a policy with a new version**The following `create-policy-version`example updates a policy definition, creating a new policy version. This example also makes the new version the default.`aws iot create-policy-version \ --policy-name``UpdateDeviceCertPolicy`\ --policy-document`file://policy.json`\ --set-as-defaultContents of `policy.json`:`{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "iot:UpdateCertificate", "Resource": "*" } ] }`Output: `{ "policyArn": "arn:aws:iot:us-west-2:123456789012:policy/UpdateDeviceCertPolicy", "policyDocument": "{ \"Version\": \"2012-10-17\", \"Statement\": [ { \"Effect\": \"Allow\", \"Action\": \"iot:UpdateCertificate\", \"Resource\": \"*\" } ] }", "policyVersionId": "2", "isDefaultVersion": true }`For more information, see [AWS IoT Policies](https://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [CreatePolicyVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-policy-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-policy`.

- **AWS CLI**
- 
            
                    **To create an AWS IoT policy**The following `create-policy`example creates an AWS IoT policy named TemperatureSensorPolicy. The`policy.json`file contains statements that allow AWS IoT policy actions.`aws iot create-policy \ --policy-name``TemperatureSensorPolicy`\ --policy-document`file://policy.json`Contents of `policy.json`:`{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "iot:Publish", "iot:Receive" ], "Resource": [ "arn:aws:iot:us-west-2:123456789012:topic/topic_1", "arn:aws:iot:us-west-2:123456789012:topic/topic_2" ] }, { "Effect": "Allow", "Action": [ "iot:Subscribe" ], "Resource": [ "arn:aws:iot:us-west-2:123456789012:topicfilter/topic_1", "arn:aws:iot:us-west-2:123456789012:topicfilter/topic_2" ] }, { "Effect": "Allow", "Action": [ "iot:Connect" ], "Resource": [ "arn:aws:iot:us-west-2:123456789012:client/basicPubSub" ] } ] }`Output: `{ "policyName": "TemperatureSensorPolicy", "policyArn": "arn:aws:iot:us-west-2:123456789012:policy/TemperatureSensorPolicy", "policyDocument": "{ \"Version\": \"2012-10-17\", \"Statement\": [ { \"Effect\": \"Allow\", \"Action\": [ \"iot:Publish\", \"iot:Receive\" ], \"Resource\": [ \"arn:aws:iot:us-west-2:123456789012:topic/topic_1\", \"arn:aws:iot:us-west-2:123456789012:topic/topic_2\" ] }, { \"Effect\": \"Allow\", \"Action\": [ \"iot:Subscribe\" ], \"Resource\": [ \"arn:aws:iot:us-west-2:123456789012:topicfilter/topic_1\", \"arn:aws:iot:us-west-2:123456789012:topicfilter/topic_2\" ] }, { \"Effect\": \"Allow\", \"Action\": [ \"iot:Connect\" ], \"Resource\": [ \"arn:aws:iot:us-west-2:123456789012:client/basicPubSub\" ] } ] }", "policyVersionId": "1" }`For more information, see [AWS IoT Policies](https://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [CreatePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-provisioning-claim`.

- **AWS CLI**
- 
            
                    **To create a provisioning claim**The following `create-provisioning-claim`example creates a provisioning claim from a provisioning template.`aws iot create-provisioning-claim \ --template-name``MyTestProvisioningTemplate`Output: `{ "certificateId": "78de02184b2ce80cf8fb709bda59e62b19fb83513590483eb0434589476ab09f", "certificatePem": "-----BEGIN CERTIFICATE-----\nMIIDdzCCAl+gAwIBAgIUXSZhEBLztMLZ2fHG 14gV0NymYY0wDQYJKoZIhvcNAQEL\nBQAwfjELMAkGA1UEBhMCVVMxEzARBgNVBAgMCldhc2hpbmd0b24xEDAOBg VBAcM\nB1NlYXR0bGUxGDAWBgNVBAoMD0FtYXpvbi5jb20gSW5jLjEgMB4GA1UECwwXQW1h\nem9uIElvVCBQcm9 2aXNpb25pbmcxDDAKBgNVBAUTAzEuMDAeFw0yMDA3MjgxNjQ0\nMDZaFw0yMDA3MjgxNjUxMDZaMEsxSTBHBgNVB AMMQDFhNDEyM2VkNmIxYjU3MzE3\nZTgzMTJmY2MzN2FiNTdhY2MzYTZkZGVjOGQ5OGY3NzUwMWRlMjc0YjhmYTQ xN2Iw\nggEiMA0GCSqGSIb3EXAMPLEAA4IBDwAwggEKAoIBAQDBhKI94ktKLqTwnj+ayOq1\nTAJt/N6s6IJDZvl rYjkC0E7wzaeY3TprWk03S29vUzVuEOXHXQXZbihgpg2m6fza\nkWm9/wpjzE9ny5+xkPGVH4Wnwz7yK5m8S0agL T96cRBSWnWmonOWdY0GKVzni0CA\n+iyGudgrFKm7Eae/v18oXrf82KtOAGO4xG0KE2WKYHsT1fx3c9xZhlXP/eX Lhv00\n+lGp0WVw9PbhKfrxliKJ5q6sL5nVUaUHq6hlQPYwsATeOvAp3u0ak5zgTyL0fg7Y\nPyKk6VYwLW62r+V YBSForEMOAhkq3LsP/rjxpEKmi2W4lPVS6oFZRKcD+H1Kyil5\nAgMBAAGjIDAeMAwGA1UdEwEB/wQCMAAwDgYDV R0PAQH/BAQDAgeAMA0GCSqGSIb3\nDQEBCwUAA4IBAQAGgix2k6nVqbZFKq97/fZBzLGS0dyz5rT/E41cDIRX+1j EPW41\nw0D+2sXheCZLZZnSkvIiP74IToNeXDrjdcaodeGFVHIElRjhMIq+4ZebPbRLtidF\nRc2hfcTAlqq9Z6v 5Vk6BeM1tu0RqH1wPoVUccLPya8EjNCbnJZUmGdOfrN/Y9pho\n5ikV+HPeZhG/k6dhE2GsQJyKFVHL/uBgKSily 1bRyWU1r6qcpWBNBHjUoD7HgOwD\nnzMh4XRb2FQDsqFalkCSYmeL8IVC49sgPD9Otyp5uteGMTy62usAAUQdq/f ZvrWg\nOkFpwMVnGKVKT7Kg0kKOLzKWOBB2Jm4/gmrJ\n-----END CERTIFICATE-----\n", "keyPair": { "PublicKey": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCg KCAQEAwYSiPeJLSi6k8J4/msjq\ntUwCbfzerOiCQ2b5a2I5AtBO8M2nmN06a1pNN0tvb1M1bhDlx10F2W4oYKYN pun8\n2pFpvf8KY8xPZ8ufsZDxlR+Fp8M+8iuZvEtGoC0/enEQUlp1pqJzlnWNBilc54tA\ngPoshrnYKxSpuxGn v79fKF63/NirTgBjuMRtChNlimEXAMPLE3PcWYZVz/3ly4b9\nNPpRqdFlcPT24Sn68ZYiieaurC+Z1VGlB6uoZU D2MLAE3jrwKd7tGpOc4E8i9H4O\n2D8ipOlWMC1utq/lWAUhaKxDDgIZKty7D/648aRCpotluJT1UuqBWUSnA/h9 Ssop\neQIDAQAB\n-----END PUBLIC KEY-----\n", "PrivateKey": "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAwYSiPeJLSi6k8J4/ msjqtUwCbfzerOiCQ2b5a2I5AtBO8M2n\nmN06a1pNN0tvb1M1bhDlx10F2W4oYKYNpun82pFpvf8KY8xPZ8ufsZ DxlR+Fp8M+\n8iuZvEtGoC0/enEQUlp1pqJzlnWNBilc54tAgPoshrnYKxSpuxGnv79fKF63/Nir\nTgBjuMRtCh NlimB7E9X8d3PcWYZVz/3ly4b9NPpRqdFlcPT24Sn68ZYiieaurC+Z\n1VGlB6uoZUD2MLAE3jrwKd7tGpOc4E8i 9H4O2D8ipOlWMC1utq/lWAUhaKxDDgIZ\nKty7D/648aRCpotluJT1UuqBWUSnA/h9SsopeQIDAQABAoIBAEAybN QUtx9T2/nK\ntZT2pA4iugecxI4dz+DmT0XVXs5VJmrx/nBSq6ejXExEpSIMO4RY7LE3ZdJcnd56\nF7tQkkY7yR VzfxHeXFU1krOIPuxWebNOrRoPZr+1RSer+wv2aBC525+88pVuR6tM\nm3pgkrR2ycCj9FdOUoQxdjHBHaM5PDmJ 9aSxCKdg3nReepeGwsR2TQA+m2vVxWk7\nou0+91eTOP+/QfP7P8ZjOIkO2XivlRcVDyN/E4QXPKuIkM/8vS8VK+ E9pATQ0MtB\n2lw8R/YU5AJd6jlEXAMPLEGU2UzRzInNWiLtkPPPqgqXXhxOf+mxByjcMalVJk0L\nhOG2ROUCgY EA+ROcHNHy/XbsP7FihOhEh+6Q2QxQ2ncBUPYbBazrR8Hn+7SCICQK\nVyYfd8Ajfq3e7RsKVL5SlMBp7Slidxak bIn28fKfPn62DaemGCIoyDgLpF+eUxBx\ngzbCiBZga8brfurza43UZjKZLpg3hq721+FeAiXi1Nma4Yr9YWEHEN 8CgYEAxuWt\npzdWWmsiFzfsAw0sy9ySDA/xr5WRWzJyAqUsjsks6rxNzWebpufnYHcmtW7pLdqM\nkboHwN2pXa kmZvrk2nKkEMq5brBYGDXuxDe+V369Bianx8aZFyIsckA7OwXW1w1h\ngRC5rQ4XOgp3+Jmw7eAO8LRYDjaN846+ QbtO2KcCgYAWS0UL51bijQR0ZwI0dz27\nFQVuCAYsp748aurcRTACCj8jbnK/QbqTNlxWsaH7ssBjZKo2D5sAqY BRtASWODab\naHXsDhVm2Jye+ESLoHMaCLoyCkT3ll8yqXIcEDStMO7fO1Ryag164EiJvSIrMfny\nNL/fXVjCSH /udCxdzPt+7QKBgQC+LAD7rxdr4J9538hTqpc4XK9vxRbrMXEH55XH\nHbMa2xONZXpmeTgEQBukyohCVceyRhK9 i0e6irZTjVXghOeoTpC8VXkzcnzouTiQ\neFQQSGfnp7Ioe6UIz23715pKduzSNkMSKrG924ktv7CyDBF1gBQI5g aDoHnddJBJ\nPRTIZQKBgA8MASXtTxQntRwXXzR92U0vAighiuRkB/mx9jQpUcK1qiqHbkAMqgNF\nPFCBYIUbFT iYKKKeJNbyJQvjfsJCkAnaFJ+RnTxk0Q6Wjm20peJ/ii4QiDdnigoE\nvdlc5cFQewWb4/zqAtPdinkPlN94ileI 79XQdc7RlJ0jpgTimL+V\n-----END RSA PRIVATE KEY-----\n" }, "expiration": 1595955066.0 }`For more information, see [Provisioning by trusted user](https://docs.aws.amazon.com/iot/latest/developerguide/provision-wo-cert.html#trusted-user)in the*AWS IoT Core Developers Guide*.- 
                    For API details, see [CreateProvisioningClaim](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-provisioning-claim.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-provisioning-template-version`.

- **AWS CLI**
- 
            
                    **To create a provisioning template version**The following example creates a version for the specified provisioning template. The body of the new version is supplied in the file `template.json`.`aws iot create-provisioning-template-version \ --template-name``widget-template`\ --template-body`file://template.json`Contents of `template.json`:`{ "Parameters" : { "DeviceLocation": { "Type": "String" } }, "Mappings": { "LocationTable": { "Seattle": { "LocationUrl": "https://example.aws" } } }, "Resources" : { "thing" : { "Type" : "AWS::IoT::Thing", "Properties" : { "AttributePayload" : { "version" : "v1", "serialNumber" : "serialNumber" }, "ThingName" : {"Fn::Join":["",["ThingPrefix_",{"Ref":"SerialNumber"}]]}, "ThingTypeName" : {"Fn::Join":["",["ThingTypePrefix_",{"Ref":"SerialNumber"}]]}, "ThingGroups" : ["widgets", "WA"], "BillingGroup": "BillingGroup" }, "OverrideSettings" : { "AttributePayload" : "MERGE", "ThingTypeName" : "REPLACE", "ThingGroups" : "DO_NOTHING" } }, "certificate" : { "Type" : "AWS::IoT::Certificate", "Properties" : { "CertificateId": {"Ref": "AWS::IoT::Certificate::Id"}, "Status" : "Active" } }, "policy" : { "Type" : "AWS::IoT::Policy", "Properties" : { "PolicyDocument" : { "Version":"2012-10-17", "Statement": [{ "Effect": "Allow", "Action":["iot:Publish"], "Resource": ["arn:aws:iot:us-east-1:123456789012:topic/foo/bar"] }] } } } }, "DeviceConfiguration": { "FallbackUrl": "https://www.example.com/test-site", "LocationUrl": { "Fn::FindInMap": ["LocationTable",{"Ref": "DeviceLocation"}, "LocationUrl"]} } } }`Output: `{ "templateArn": "arn:aws:iot:us-east-1:123456789012:provisioningtemplate/widget-template", "templateName": "widget-template", "versionId": 2, "isDefaultVersion": false }`For more information, see [AWS IoT Secure Tunneling](https://docs.aws.amazon.com/iot/latest/developerguide/secure-tunneling.html)in the*AWS IoT Core Developer Guide*.- 
                    For API details, see [CreateProvisioningTemplateVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-provisioning-template-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-provisioning-template`.

- **AWS CLI**
- 
            
                    **To create a provisioning template**The following `create-provisioning-template`example creates a provisioning template as defined by the file`template.json`.`aws iot create-provisioning-template \ --template-name``widget-template`\ --description`"A provisioning template for widgets"`\ --provisioning-role-arn`arn:aws:iam::123456789012:role/Provision_role`\ --template-body`file://template.json`Contents of `template.json`:`{ "Parameters" : { "DeviceLocation": { "Type": "String" } }, "Mappings": { "LocationTable": { "Seattle": { "LocationUrl": "https://example.aws" } } }, "Resources" : { "thing" : { "Type" : "AWS::IoT::Thing", "Properties" : { "AttributePayload" : { "version" : "v1", "serialNumber" : "serialNumber" }, "ThingName" : {"Fn::Join":["",["ThingPrefix_",{"Ref":"SerialNumber"}]]}, "ThingTypeName" : {"Fn::Join":["",["ThingTypePrefix_",{"Ref":"SerialNumber"}]]}, "ThingGroups" : ["widgets", "WA"], "BillingGroup": "BillingGroup" }, "OverrideSettings" : { "AttributePayload" : "MERGE", "ThingTypeName" : "REPLACE", "ThingGroups" : "DO_NOTHING" } }, "certificate" : { "Type" : "AWS::IoT::Certificate", "Properties" : { "CertificateId": {"Ref": "AWS::IoT::Certificate::Id"}, "Status" : "Active" } }, "policy" : { "Type" : "AWS::IoT::Policy", "Properties" : { "PolicyDocument" : { "Version":"2012-10-17", "Statement": [{ "Effect": "Allow", "Action":["iot:Publish"], "Resource": ["arn:aws:iot:us-east-1:504350838278:topic/foo/bar"] }] } } } }, "DeviceConfiguration": { "FallbackUrl": "https://www.example.com/test-site", "LocationUrl": { "Fn::FindInMap": ["LocationTable",{"Ref": "DeviceLocation"}, "LocationUrl"]} } } }`Output: `{ "templateArn": "arn:aws:iot:us-east-1:123456789012:provisioningtemplate/widget-template", "templateName": "widget-template", "defaultVersionId": 1 }`For more information, see [AWS IoT Secure Tunneling](https://docs.aws.amazon.com/iot/latest/developerguide/secure-tunneling.html)in the*AWS IoT Core Developer Guide*.- 
                    For API details, see [CreateProvisioningTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-provisioning-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-role-alias`.

- **AWS CLI**
- 
            
                    **To create a role alias**The following `create-role-alias`example creates a role alias called`LightBulbRole`for the specified role.`aws iot create-role-alias \ --role-alias``LightBulbRole`\ --role-arn`arn:aws:iam::123456789012:role/lightbulbrole-001`Output: `{ "roleAlias": "LightBulbRole", "roleAliasArn": "arn:aws:iot:us-west-2:123456789012:rolealias/LightBulbRole" }`For more information, see [CreateRoleAlias](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateRoleAlias.html)in the*AWS IoT API Reference*.- 
                    For API details, see [CreateRoleAlias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-role-alias.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-scheduled-audit`.

- **AWS CLI**
- 
            
                    **To create a scheduled audit**The following `create-scheduled-audit`example creates a scheduled audit that runs weekly, on Wednesday, to check if CA certificates or device certificates are expiring.`aws iot create-scheduled-audit \ --scheduled-audit-name``WednesdayCertCheck`\ --frequency`WEEKLY`\ --day-of-week`WED`\ --target-check-names`CA_CERTIFICATE_EXPIRING_CHECK``DEVICE_CERTIFICATE_EXPIRING_CHECK`Output: `{ "scheduledAuditArn": "arn:aws:iot:us-west-2:123456789012:scheduledaudit/WednesdayCertCheck" }`For more information, see [Audit Commands](https://docs.aws.amazon.com/iot/latest/developerguide/AuditCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [CreateScheduledAudit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-scheduled-audit.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-security-profile`.

- **AWS CLI**
- 
            
                    **To create a security profile**The following `create-security-profile`example creates a security profile that checks if cellular bandwidth exceeds a threshold or if more than 10 authorization failures occur within a five-minute period.`aws iot create-security-profile \ --security-profile-name``PossibleIssue`\ --security-profile-description`"Check to see if authorization fails 10 times in 5 minutes or if cellular bandwidth exceeds 128"`\ --behaviors "[{\"name\":\"CellularBandwidth\",\"metric\":\"aws:message-byte-size\",\"criteria\":{\"comparisonOperator\":\"greater-than\",\"value\":{\"count\":128},\"consecutiveDatapointsToAlarm\":1,\"consecutiveDatapointsToClear\":1}},{\"name\":\"Authorization\",\"metric\":\"aws:num-authorization-failures\",\"criteria\":{\"comparisonOperator\":\"less-than\",\"value\":{\"count\":10},\"durationSeconds\":300,\"consecutiveDatapointsToAlarm\":1,\"consecutiveDatapointsToClear\":1}}]"Output: `{ "securityProfileName": "PossibleIssue", "securityProfileArn": "arn:aws:iot:us-west-2:123456789012:securityprofile/PossibleIssue" }`For more information, see [Detect Commands](https://docs.aws.amazon.com/iot/latest/developerguide/DetectCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [CreateSecurityProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-security-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-stream`.

- **AWS CLI**
- 
            
                    **To create a stream for delivering one or more large files in chunks over MQTT**The following `create-stream`example creates a stream for delivering one or more large files in chunks over MQTT. A stream transports data bytes in chunks or blocks packaged as MQTT messages from a source like S3. You can have one or more files associated with a stream.`aws iot create-stream \ --cli-input-json``file://create-stream.json`Contents of `create-stream.json`:`{ "streamId": "stream12345", "description": "This stream is used for Amazon FreeRTOS OTA Update 12345.", "files": [ { "fileId": 123, "s3Location": { "bucket":"codesign-ota-bucket", "key":"48c67f3c-63bb-4f92-a98a-4ee0fbc2bef6" } } ], "roleArn": "arn:aws:iam:123456789012:role/service-role/my_ota_stream_role" }`Output: `{ "streamId": "stream12345", "streamArn": "arn:aws:iot:us-west-2:123456789012:stream/stream12345", "description": "This stream is used for Amazon FreeRTOS OTA Update 12345.", "streamVersion": "1" }`For more information, see [CreateStream](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateStream.html)in the*AWS IoT API Reference*.- 
                    For API details, see [CreateStream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-stream.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-thing-group`.

- **AWS CLI**
- 
            
                    **Example 1: To create a thing group**The following `create-thing-group`example creates a thing group named`LightBulbs`with a description and two attributes.`aws iot create-thing-group \ --thing-group-name``LightBulbs`\ --thing-group-properties "thingGroupDescription=\"Generic bulb group\", attributePayload={attributes={Manufacturer=AnyCompany,wattage=60}}"Output: `{ "thingGroupName": "LightBulbs", "thingGroupArn": "arn:aws:iot:us-west-2:123456789012:thinggroup/LightBulbs", "thingGroupId": "9198bf9f-1e76-4a88-8e8c-e7140142c331" }`**Example 2: To create a thing group that's part of a parent group**The following `create-thing-group`creates a thing group named`HalogenBulbs`that has a parent thing group named`LightBulbs`.`aws iot create-thing-group \ --thing-group-name``HalogenBulbs`\ --parent-group-name`LightBulbs`Output: `{ "thingGroupName": "HalogenBulbs", "thingGroupArn": "arn:aws:iot:us-west-2:123456789012:thinggroup/HalogenBulbs", "thingGroupId": "f4ec6b84-b42b-499d-9ce1-4dbd4d4f6f6e" }`For more information, see [Thing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/thing-groups.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [CreateThingGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-thing-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-thing-type`.

- **AWS CLI**
- 
            
                    **To define a thing type**The following `create-thing-type`example defines a thing type and associated attributes.`aws iot create-thing-type \ --thing-type-name``"LightBulb"`\ --thing-type-properties`"thingTypeDescription=light bulb type, searchableAttributes=wattage,model"`Output: `{ "thingTypeName": "LightBulb", "thingTypeArn": "arn:aws:iot:us-west-2:123456789012:thingtype/LightBulb", "thingTypeId": "ce3573b0-0a3c-45a7-ac93-4e0ce14cd190" }`For more information, see [Thing Types](https://docs.aws.amazon.com/iot/latest/developerguide/thing-types.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [CreateThingType](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-thing-type.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-thing`.

- **AWS CLI**
- 
            
                    **Example 1: To create a thing record in the registry**The following `create-thing`example creates an entry for a device in the AWS IoT thing registry.`aws iot create-thing \ --thing-name``SampleIoTThing`Output: `{ "thingName": "SampleIoTThing", "thingArn": "arn:aws:iot:us-west-2: 123456789012:thing/SampleIoTThing", "thingId": " EXAMPLE1-90ab-cdef-fedc-ba987EXAMPLE " }`**Example 2: To define a thing that is associated with a thing type**The following `create-thing`example create a thing that has the specified thing type and its attributes.`aws iot create-thing \ --thing-name``"MyLightBulb"`\ --thing-type-name`"LightBulb"`\ --attribute-payload "{"attributes": {"wattage":"75", "model":"123"}}"Output: `{ "thingName": "MyLightBulb", "thingArn": "arn:aws:iot:us-west-2:123456789012:thing/MyLightBulb", "thingId": "40da2e73-c6af-406e-b415-15acae538797" }`For more information, see [How to Manage Things with the Registry](https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html)and[Thing Types](https://docs.aws.amazon.com/iot/latest/developerguide/thing-types.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [CreateThing](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-thing.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-topic-rule-destination`.

- **AWS CLI**
- 
            
                    **To create a topic rule destination**The following `create-topic-rule-destination`example creates a topic rule destination for an HTTP endpoint.`aws iot create-topic-rule-destination \ --destination-configuration``httpUrlConfiguration={confirmationUrl=https://example.com}`Output: `{ "topicRuleDestination": { "arn": "arn:aws:iot:us-west-2:123456789012:ruledestination/http/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "status": "IN_PROGRESS", "statusReason": "Awaiting confirmation. Confirmation message sent on 2020-07-09T22:47:54.154Z; no response received from the endpoint.", "httpUrlProperties": { "confirmationUrl": "https://example.com" } } }`For more information, see [Creating a topic rule destination](https://docs.aws.amazon.com/iot/latest/developerguide/rule-destination.html#create-destination)in the*AWS IoT Developer Guide*.- 
                    For API details, see [CreateTopicRuleDestination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-topic-rule-destination.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-topic-rule`.

- **AWS CLI**
- 
            
                    **To create a rule that sends an Amazon SNS alert**The following `create-topic-rule`example creates a rule that sends an Amazon SNS message when soil moisture level readings, as found in a device shadow, are low.`aws iot create-topic-rule \ --rule-name``"LowMoistureRule"`\ --topic-rule-payload`file://plant-rule.json`The example requires the following JSON code to be saved to a file named `plant-rule.json`:`{ "sql": "SELECT * FROM '$aws/things/MyRPi/shadow/update/accepted' WHERE state.reported.moisture = 'low'\n", "description": "Sends an alert whenever soil moisture level readings are too low.", "ruleDisabled": false, "awsIotSqlVersion": "2016-03-23", "actions": [{ "sns": { "targetArn": "arn:aws:sns:us-west-2:123456789012:MyRPiLowMoistureTopic", "roleArn": "arn:aws:iam::123456789012:role/service-role/MyRPiLowMoistureTopicRole", "messageFormat": "RAW" } }] }`This command produces no output. For more information, see [Creating an AWS IoT Rule](https://docs.aws.amazon.com/iot/latest/developerguide/iot-create-rule.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [CreateTopicRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-topic-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-account-audit-configuration`.

- **AWS CLI**
- 
            
                    **To disable all audit checks for your AWS account**The following `delete-account-audit-configuration`example restores the default settings for AWS IoT Device Defender for this account, disabling all audit checks and clearing configuration data. It also deletes any scheduled audits for this account.**Use this command with caution.**`aws iot delete-account-audit-configuration \ --delete-scheduled-audits`This command produces no output. For more information, see [Audit Commands](https://docs.aws.amazon.com/iot/latest/developerguide/AuditCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DeleteAccountAuditConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-account-audit-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-audit-suppression`.

- **AWS CLI**
- 
            
                    **To delete an audit finding suppression**The following `delete-audit-suppression`example deletes an audit finding suppression for DEVICE_CERTIFICATE_EXPIRING_CHECK.`aws iot delete-audit-suppression \ --check-name``DEVICE_CERTIFICATE_EXPIRING_CHECK`\ --resource-identifier deviceCertificateId="c7691e<shortened>"This command produces no output. For more information, see [Audit finding suppressions](https://docs.aws.amazon.com/iot/latest/developerguide/audit-finding-suppressions.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [DeleteAuditSuppression](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-audit-suppression.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-authorizer`.

- **AWS CLI**
- 
            
                    **To delete a custom authorizer**The following `delete-authorizer`example deletes the authorizer named`CustomAuthorizer`. A custom authorizer must be in the`INACTIVE`state before you can delete it.`aws iot delete-authorizer \ --authorizer-name``CustomAuthorizer`This command produces no output. For more information, see [DeleteAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteAuthorizer.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DeleteAuthorizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-authorizer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-billing-group`.

- **AWS CLI**
- 
            
                    **To delete a billing group**The following `delete-billing-group`example deletes the specified billing group. You can delete a billing group even if it contains one or more things.`aws iot delete-billing-group \ --billing-group-name``BillingGroupTwo`This command does not produce any output. For more information, see [Billing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/tagging-iot-billing-groups.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [DeleteBillingGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-billing-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-ca-certificate`.

- **AWS CLI**
- 
            
                    **To delete a CA certificate**The following `delete-ca-certificate`example deletes the CA certificate with the specified certificate ID.`aws iot delete-ca-certificate \ --certificate-id``f4efed62c0142f16af278166f61962501165c4f0536295207426460058cd1467`This command produces no output. For more information, see [DeleteCACertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteCACertificate.html)in the*AWS IoT API Reference*.- 
                    For API details, see [DeleteCaCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-ca-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-certificate`.

- **AWS CLI**
- 
            
                    **To delete a device certificate**The following `delete-certificate`example deletes the device certificate with the specified ID.`aws iot delete-certificate \ --certificate-id``c0c57bbc8baaf4631a9a0345c957657f5e710473e3ddbee1428d216d54d53ac9`This command produces no output. For more information, see [DeleteCertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteCertificate.html)in the*AWS IoT API Reference*.- 
                    For API details, see [DeleteCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-custom-metric`.

- **AWS CLI**
- 
            
                    **To delete a custom metric**The following `delete-custom-metric`example deletes a custom metric.`aws iot delete-custom-metric \ --metric-name``batteryPercentage`\ --region`us-east-1`Output: `HTTP 200`For more information, see [Custom metrics](https://docs.aws.amazon.com/iot/latest/developerguide/dd-detect-custom-metrics.html)in the*AWS IoT Core Developer Guide*.- 
                    For API details, see [DeleteCustomMetric](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-custom-metric.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-dimension`.

- **AWS CLI**
- 
            
                    **To delete a dimension**The following `delete-dimension`example deletes a dimension called`TopicFilterForAuthMessages`.`aws iot delete-dimension \ --name``TopicFilterForAuthMessages`This command produces no output. For more information, see [Detect Commands](https://docs.aws.amazon.com/iot/latest/developerguide/DetectCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DeleteDimension](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-dimension.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-domain-configuration`.

- **AWS CLI**
- 
            
                    **To delete a domain configuration**The following `delete-domain-configuration`example deletes a domain configuration named`additionalDataDomain`from your AWS account.`aws iot delete-domain-configuration \ --domain-configuration-name``"additionalDataDomain"`\ --domain-configuration-status`"OK"`This command produces no output. For more information, see [Configurable Endpoints](https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-configurable-aws.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DeleteDomainConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-domain-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-dynamic-thing-group`.

- **AWS CLI**
- 
            
                    **To delete a dynamic thing group**The following `delete-dynamic-thing-group`example deletes the specified dynamic thing group.`aws iot delete-dynamic-thing-group \ --thing-group-name``"RoomTooWarm"`This command produces no output. For more information, see [Dynamic Thing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/dynamic-thing-groups.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [DeleteDynamicThingGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-dynamic-thing-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-job-execution`.

- **AWS CLI**
- 
            
                    **To delete a job execution**The following `delete-job-execution`example deletes the job execution of the specified job on a device. Use`describe-job-execution`to get the execution number.`aws iot delete-job-execution --job-id``"example-job-02"`--thing-name`"MyRaspberryPi"`--execution-number`1`This command produces no output. For more information, see [Creating and Managing Jobs (CLI)](https://docs.aws.amazon.com/iot/latest/developerguide/manage-job-cli.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DeleteJobExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-job-execution.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-job`.

- **AWS CLI**
- 
            
                    **To delete a job**The following `delete-job`example deletes the specified job. By specifying the`--force`option, the job is deleted even if the status is`IN_PROGRESS`.`aws iot delete-job \ --job-id``"example-job-04"`\ --forceThis command produces no output. For more information, see [Creating and Managing Jobs (CLI)](https://docs.aws.amazon.com/iot/latest/developerguide/manage-job-cli.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DeleteJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-mitigation-action`.

- **AWS CLI**
- 
            
                    **To delete a mitigation action**The following `delete-mitigation-action`example deletes the specified mitigation action.`aws iot delete-mitigation-action \ --action-name``AddThingsToQuarantineGroup1Action`This command produces no output. For more information, see [DeleteMitigationAction (Mitigation Action Commands)](https://docs.aws.amazon.com/iot/latest/developerguide/mitigation-action-commands.html#dd-api-iot-DeleteMitigationAction)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DeleteMitigationAction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-mitigation-action.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-ota-update`.

- **AWS CLI**
- 
            
                    **To delete an OTA update**The following `delete-ota-update`example deletes the specified OTA update.`aws iot delete-ota-update \ --ota-update-id``ota12345`\ --delete-stream \ --force-delete-aws-jobThis command produces no output. For more information, see [DeleteOTAUpdate](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteOTAUpdate.html)in the*AWS IoT API Reference*.- 
                    For API details, see [DeleteOtaUpdate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-ota-update.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-policy-version`.

- **AWS CLI**
- 
            
                    **To delete a version of policy**The following `delete-policy-version`example deletes version 2 of the specified policy from your AWS account.`aws iot delete-policy-version \ --policy-name``UpdateDeviceCertPolicy`\ --policy-version-id`2`This command produces no output. For more information, see [AWS IoT Policies](https://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DeletePolicyVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-policy-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-policy`.

- **AWS CLI**
- 
            
                    **To delete a policy**The following `delete-policy`example deletes the specified policy from your AWS account.`aws iot delete-policy --policy-name``UpdateDeviceCertPolicy`This command produces no output. For more information, see [AWS IoT Policies](https://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [DeletePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-provisioning-template-version`.

- **AWS CLI**
- 
            
                    **To delete a provisioning template version**The following `delete-provisioning-template-version`example deletes version 2 of the specified provisioning template.`aws iot delete-provisioning-template-version \ --version-id``2`\ --template-name`"widget-template"`This command produces no output. For more information, see [AWS IoT Secure Tunneling](https://docs.aws.amazon.com/iot/latest/developerguide/secure-tunneling.html)in the*AWS IoT Core Developer Guide*.- 
                    For API details, see [DeleteProvisioningTemplateVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-provisioning-template-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-provisioning-template`.

- **AWS CLI**
- 
            
                    **To delete a provisioning template**The following `delete-provisioning-template`example deletes the specified provisioning template.`aws iot delete-provisioning-template \ --template-name``widget-template`This command produces no output. For more information, see [AWS IoT Secure Tunneling](https://docs.aws.amazon.com/iot/latest/developerguide/secure-tunneling.html)in the*AWS IoT Core Developer Guide*.- 
                    For API details, see [DeleteProvisioningTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-provisioning-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-registration-code`.

- **AWS CLI**
- 
            
                    **To delete your registration cod**The following `delete-registration-code`example deletes an AWS IoT account-specific registration code.`aws iot delete-registration-code`This command produces no output. For more information, see [Use Your Own Certificate](https://docs.aws.amazon.com/iot/latest/developerguide/device-certs-your-own.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DeleteRegistrationCode](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-registration-code.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-role-alias`.

- **AWS CLI**
- 
            
                    **To delete an AWS IoT role alias**The following `delete-role-alias`example deletes an AWS IoT role alias named`LightBulbRole`.`aws iot delete-role-alias \ --role-alias``LightBulbRole`This command produces no output. For more information, see [Authorizing Direct Calls to AWS Services](https://docs.aws.amazon.com/iot/latest/developerguide/authorizing-direct-aws.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DeleteRoleAlias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-role-alias.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-scheduled-audit`.

- **AWS CLI**
- 
            
                    **To delete a scheduled audit**The following `delete-scheduled-audit`example deletes the AWS IoT Device Defender scheduled audit named`AWSIoTDeviceDefenderDailyAudit`.`aws iot delete-scheduled-audit \ --scheduled-audit-name``AWSIoTDeviceDefenderDailyAudit`This command produces no output. For more information, see [Audit Commands](https://docs.aws.amazon.com/iot/latest/developerguide/AuditCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DeleteScheduledAudit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-scheduled-audit.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-security-profile`.

- **AWS CLI**
- 
            
                    **To delete a security profile**The following `delete-security-profile`example deletes a security profile named`PossibleIssue`.`aws iot delete-security-profile \ --security-profile-name``PossibleIssue`This command produces no output. For more information, see [Detect Commands](https://docs.aws.amazon.com/iot/latest/developerguide/DetectCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DeleteSecurityProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-security-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-stream`.

- **AWS CLI**
- 
            
                    **To delete a stream**The following `delete-stream`example deletes the specified stream.`aws iot delete-stream \ --stream-id``stream12345`This command produces no output. For more information, see [DeleteStream](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteStream.html)in the*AWS IoT API Reference*.- 
                    For API details, see [DeleteStream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-stream.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-thing-group`.

- **AWS CLI**
- 
            
                    **To delete a thing group**The following `delete-thing-group`example deletes the specified thing group. You cannot delete a thing group if it contains child thing groups.`aws iot delete-thing-group \ --thing-group-name``DefectiveBulbs`This command produces no output. For more information, see [Thing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/thing-groups.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [DeleteThingGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-thing-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-thing-type`.

- **AWS CLI**
- 
            
                    **Example 1: To delete a thing type**The following `delete-thing-type`example deletes a deprecated thing type.`aws iot delete-thing-type \ --thing-type-name``"obsoleteThingType"`This command produces no output. For more information, see [Thing Types](https://docs.aws.amazon.com/iot/latest/developerguide/thing-types.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [DeleteThingType](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-thing-type.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-thing`.

- **AWS CLI**
- 
            
                    **To display detailed information about a thing**The following `delete-thing`example deletes a thing from the AWS IoT registry for your AWS account.aws iot delete-thing --thing-name "FourthBulb" This command produces no output. For more information, see [How to Manage Things with the Registry](https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [DeleteThing](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-thing.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-topic-rule-destination`.

- **AWS CLI**
- 
            
                    **To delete a topic rule destination**The following `delete-topic-rule-destination`example deletes the specified topic rule destination.`aws iot delete-topic-rule-destination \ --arn``"arn:aws:iot:us-west-2:123456789012:ruledestination/http/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE"`This command produces no output. For more information, see [Deleting a topic rule destination](https://docs.aws.amazon.com/iot/latest/developerguide/rule-destination.html#delete-destination)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DeleteTopicRuleDestination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-topic-rule-destination.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-topic-rule`.

- **AWS CLI**
- 
            
                    **To delete a rule**The following `delete-topic-rule`example deletes the specified rule.`aws iot delete-topic-rule \ --rule-name``"LowMoistureRule"`This command produces no output. For more information, see [Deleting a Rule](https://docs.aws.amazon.com/iot/latest/developerguide/iot-delete-rule.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [DeleteTopicRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-topic-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-v2-logging-level`.

- **AWS CLI**
- 
            
                    **To delete the logging level for a thing group**The following `delete-v2-logging-level`example deletes the logging level for the specified thing group.`aws iot delete-v2-logging-level \ --target-type``THING_GROUP`\ --target-name`LightBulbs`This command produces no output. - 
                    For API details, see [DeleteV2LoggingLevel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-v2-logging-level.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deprecate-thing-type`.

- **AWS CLI**
- 
            
                    **Example 1: To deprecate a thing type**The following `deprecate-thing-type`example deprecates a thing type so that users can't associate any new things with it.`aws iot deprecate-thing-type \ --thing-type-name``"obsoleteThingType"`This command produces no output. **Example 2: To reverse the deprecation of a thing type**The following `deprecate-thing-type`example reverses the deprecation of a thing type, which makes it possible for users to associate new things with it again.`aws iot deprecate-thing-type \ --thing-type-name``"obsoleteThingType"`\ --undo-deprecateThis command produces no output. For more information, see [Thing Types](https://docs.aws.amazon.com/iot/latest/developerguide/thing-types.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [DeprecateThingType](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/deprecate-thing-type.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-account-audit-configuration`.

- **AWS CLI**
- 
            
                    **To view current audit configuration settings**The following `describe-account-audit-configuration`example lists the current settings for your AWS IoT Device Defender audit configuration.`aws iot describe-account-audit-configuration`Output: `{ "roleArn": "arn:aws:iam::123456789012:role/service-role/AWSIoTDeviceDefenderAudit_1551201085996", "auditNotificationTargetConfigurations": { "SNS": { "targetArn": "arn:aws:sns:us-west-2:123456789012:ddaudits", "roleArn": "arn:aws:iam::123456789012:role/service-role/AWSIoTDeviceDefenderAudit", "enabled": true } }, "auditCheckConfigurations": { "AUTHENTICATED_COGNITO_ROLE_OVERLY_PERMISSIVE_CHECK": { "enabled": true }, "CA_CERTIFICATE_EXPIRING_CHECK": { "enabled": true }, "CONFLICTING_CLIENT_IDS_CHECK": { "enabled": true }, "DEVICE_CERTIFICATE_EXPIRING_CHECK": { "enabled": true }, "DEVICE_CERTIFICATE_SHARED_CHECK": { "enabled": true }, "IOT_POLICY_OVERLY_PERMISSIVE_CHECK": { "enabled": true }, "LOGGING_DISABLED_CHECK": { "enabled": true }, "REVOKED_CA_CERTIFICATE_STILL_ACTIVE_CHECK": { "enabled": true }, "REVOKED_DEVICE_CERTIFICATE_STILL_ACTIVE_CHECK": { "enabled": true }, "UNAUTHENTICATED_COGNITO_ROLE_OVERLY_PERMISSIVE_CHECK": { "enabled": true } } }`For more information, see [Audit Commands](https://docs.aws.amazon.com/iot/latest/developerguide/AuditCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DescribeAccountAuditConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-account-audit-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-audit-finding`.

- **AWS CLI**
- 
            
                    **To list details for an audit finding**The following `describe-audit-finding`example lists the details for the specified AWS IoT Device Defender audit finding. An audit can produce multiple findings. Use the`list-audit-findings`command to get a list of the findings from an audit to get the`findingId`.`aws iot describe-audit-finding \ --finding-id``"ef4826b8-e55a-44b9-b460-5c485355371b"`Output: `{ "finding": { "findingId": "ef4826b8-e55a-44b9-b460-5c485355371b", "taskId": "873ed69c74a9ec8fa9b8e88e9abc4661", "checkName": "IOT_POLICY_OVERLY_PERMISSIVE_CHECK", "taskStartTime": 1576012045.745, "findingTime": 1576012046.168, "severity": "CRITICAL", "nonCompliantResource": { "resourceType": "IOT_POLICY", "resourceIdentifier": { "policyVersionIdentifier": { "policyName": "smp-ggrass-group_Core-policy", "policyVersionId": "1" } } }, "reasonForNonCompliance": "Policy allows broad access to IoT data plane actions: [iot:Subscribe, iot:Connect, iot:GetThingShadow, iot:DeleteThingShadow, iot:UpdateThingShadow, iot:Publish].", "reasonForNonComplianceCode": "ALLOWS_BROAD_ACCESS_TO_IOT_DATA_PLANE_ACTIONS" } }`For more information, see [Check Audit Results (Audit Commands)](https://docs.aws.amazon.com/iot/latest/developerguide/AuditCommands.html#device-defender-AuditCommandsFindings)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DescribeAuditFinding](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-audit-finding.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-audit-mitigation-actions-task`.

- **AWS CLI**
- 
            
                    **To show the details of an audit mitigation actions task**The following `describe-audit-mitigation-actions-task`example shows the details for the specified task, where the`ResetPolicyVersionAction`was applied to a finding. The results include when the task started and ended, how many findings were targeted (and the outcome), and the definition of the action that is applied as part of this task.`aws iot describe-audit-mitigation-actions-task \ --task-id``ResetPolicyTask01`Output: `{ "taskStatus": "COMPLETED", "startTime": "2019-12-10T15:13:19.457000-08:00", "endTime": "2019-12-10T15:13:19.947000-08:00", "taskStatistics": { "IOT_POLICY_OVERLY_PERMISSIVE_CHECK": { "totalFindingsCount": 1, "failedFindingsCount": 0, "succeededFindingsCount": 1, "skippedFindingsCount": 0, "canceledFindingsCount": 0 } }, "target": { "findingIds": [ "ef4826b8-e55a-44b9-b460-5c485355371b" ] }, "auditCheckToActionsMapping": { "IOT_POLICY_OVERLY_PERMISSIVE_CHECK": [ "ResetPolicyVersionAction" ] }, "actionsDefinition": [ { "name": "ResetPolicyVersionAction", "id": "1ea0b415-bef1-4a01-bd13-72fb63c59afb", "roleArn": "arn:aws:iam::123456789012:role/service-role/ReplacePolicyVersionRole", "actionParams": { "replaceDefaultPolicyVersionParams": { "templateName": "BLANK_POLICY" } } } ] }`For more information, see [DescribeAuditMitigationActionsTask (Mitigation Action Commands)](https://docs.aws.amazon.com/iot/latest/developerguide/mitigation-action-commands.html#dd-api-iot-DescribeAuditMitigationActionsTask)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DescribeAuditMitigationActionsTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-audit-mitigation-actions-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-audit-suppression`.

- **AWS CLI**
- 
            
                    **To get details about an audit finding suppression**The following `describe-audit-suppression`example lists details about an audit finding suppression.`aws iot describe-audit-task \ --task-id``"787ed873b69cb4d6cdbae6ddd06996c5"`Output: `{ "taskStatus": "COMPLETED", "taskType": "SCHEDULED_AUDIT_TASK", "taskStartTime": 1596168096.157, "taskStatistics": { "totalChecks": 1, "inProgressChecks": 0, "waitingForDataCollectionChecks": 0, "compliantChecks": 0, "nonCompliantChecks": 1, "failedChecks": 0, "canceledChecks": 0 }, "scheduledAuditName": "AWSIoTDeviceDefenderDailyAudit", "auditDetails": { "DEVICE_CERTIFICATE_EXPIRING_CHECK": { "checkRunStatus": "COMPLETED_NON_COMPLIANT", "checkCompliant": false, "totalResourcesCount": 195, "nonCompliantResourcesCount": 2 } } }`For more information, see [Audit finding suppressions](https://docs.aws.amazon.com/iot/latest/developerguide/audit-finding-suppressions.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [DescribeAuditSuppression](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-audit-suppression.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-audit-task`.

- **AWS CLI**
- 
            
                    **To get information about an audit instance**The following `describe-audit-task`example gets information about an instance of an AWS IoT Device Defender audit. If the audit is complete, summary statistics for the run are included in the results.`aws iot describe-audit-task \ --task-id``a3aea009955e501a31b764abe1bebd3d`Output: `{ "taskStatus": "COMPLETED", "taskType": "ON_DEMAND_AUDIT_TASK", "taskStartTime": 1560356923.434, "taskStatistics": { "totalChecks": 3, "inProgressChecks": 0, "waitingForDataCollectionChecks": 0, "compliantChecks": 3, "nonCompliantChecks": 0, "failedChecks": 0, "canceledChecks": 0 }, "auditDetails": { "CA_CERTIFICATE_EXPIRING_CHECK": { "checkRunStatus": "COMPLETED_COMPLIANT", "checkCompliant": true, "totalResourcesCount": 0, "nonCompliantResourcesCount": 0 }, "DEVICE_CERTIFICATE_EXPIRING_CHECK": { "checkRunStatus": "COMPLETED_COMPLIANT", "checkCompliant": true, "totalResourcesCount": 6, "nonCompliantResourcesCount": 0 }, "REVOKED_CA_CERTIFICATE_STILL_ACTIVE_CHECK": { "checkRunStatus": "COMPLETED_COMPLIANT", "checkCompliant": true, "totalResourcesCount": 0, "nonCompliantResourcesCount": 0 } } }`For more information, see [Audit Commands](https://docs.aws.amazon.com/iot/latest/developerguide/AuditCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DescribeAuditTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-audit-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-authorizer`.

- **AWS CLI**
- 
            
                    **To get information about a custom authorizer**The following `describe-authorizer`example displays details for the specified custom authorizer.`aws iot describe-authorizer \ --authorizer-name``CustomAuthorizer`Output: `{ "authorizerDescription": { "authorizerName": "CustomAuthorizer", "authorizerArn": "arn:aws:iot:us-west-2:123456789012:authorizer/CustomAuthorizer", "authorizerFunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:CustomAuthorizerFunction", "tokenKeyName": "MyAuthToken", "tokenSigningPublicKeys": { "FIRST_KEY": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1uJOB4lQPgG/lM6ZfIwo\nZ+7ENxAio9q6QD4FFqjGZsvjtYwjoe1RKK0U8Eq9xb5O3kRSmyIwTzwzm/f4Gf0Y\nZUloJ+t3PUUwHrmbYTAgTrCUgRFygjfgVwGCPs5ZAX4Eyqt5cr+AIHIiUDbxSa7p\nzwOBKPeic0asNJpqT8PkBbRaKyleJh5oo81NDHHmVtbBm5A5YiJjqYXLaVAowKzZ\n+GqsNvAQ9Jy1wI2VrEa1OfL8flDB/BJLm7zjpfPOHDJQgID0XnZwAlNnZcOhCwIx\n50g2LW2Oy9R/dmqtDmJiVP97Z4GykxPvwlYHrUXY0iW1R3AR/Ac1NhCTGZMwVDB1\nlQIDAQAB\n-----END PUBLIC KEY-----" }, "status": "ACTIVE", "creationDate": 1571245658.069, "lastModifiedDate": 1571245658.069 } }`For more information, see [DescribeAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeAuthorizer.html)in the*AWS IoT API Reference*.- 
                    For API details, see [DescribeAuthorizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-authorizer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-billing-group`.

- **AWS CLI**
- 
            
                    **To get information about a billing group**The following `describe-billing-group`example gets information for the specified billing group.`aws iot describe-billing-group --billing-group-name``GroupOne`Output: `{ "billingGroupName": "GroupOne", "billingGroupId": "103de383-114b-4f51-8266-18f209ef5562", "billingGroupArn": "arn:aws:iot:us-west-2:123456789012:billinggroup/GroupOne", "version": 1, "billingGroupProperties": {}, "billingGroupMetadata": { "creationDate": 1560199355.378 } }`For more information, see [Billing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/tagging-iot-billing-groups.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [DescribeBillingGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-billing-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-ca-certificate`.

- **AWS CLI**
- 
            
                    **To get details about a CA certificate**The following `describe-ca-certificate`example displays the details for the specified CA certificate.`aws iot describe-ca-certificate \ --certificate-id``f4efed62c0142f16af278166f61962501165c4f0536295207426460058cd1467`Output: `{ "certificateDescription": { "certificateArn": "arn:aws:iot:us-west-2:123456789012:cacert/f4efed62c0142f16af278166f61962501165c4f0536295207426460058cd1467", "certificateId": "f4efed62c0142f16af278166f61962501165c4f0536295207426460058cd1467", "status": "INACTIVE", "certificatePem": "-----BEGIN CERTIFICATE-----\nMIICzzCCAbegEXAMPLEJANVEPWXl8taPMA0GCSqGSIb3DQEBBQUAMB4xCzAJBgNV\nBAYTAlVTMQ8wDQYDVQQKDAZBbWF6b24wHhcNMTkwOTI0MjEzMTE1WhcNMjkwOTIx\nMjEzMTE1WjAeMQswCQYDVQQGEwJVUzEPMA0GA1UECgwGQW1hem9uMIIBIjANBgkq\nhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzd3R3ioalCS0MhFWfBrVGR036EK07UAf\nVdz9EXAMPLE1VczICbADnATK522kEIB51/18VzlFtAhQL5V5eybXKnB7QebNer5m\n4Yibx7shR5oqNzFsrXWxuugN5+w5gEfqNMawOjhF4LsculKG49yuqjcDU19/13ua\n3B2gxs1Pe7TiWWvUskzxnbO1F2WCshbEJvqY8fIWtGYCjTeJAgQ9hvZx/69XhKen\nwV9LJwOQxrsUS0Ty8IHwbB8fRy72VM3u7fJoaU+nO4jD5cqaoEPtzoeFUEXAMPLE\nyVAJpqHwgbYbcUfn7V+AB6yh1+0Fa1rEQGuZDPGyJslxwr5vh8nRewIDAQABoxAw\nDjAMBgNVHRMEBTADAQH/MA0GCSqGSIb3DQEBBQUAA4IBAQA+3a5CV3IJgOnd0AgI\nBgVMtmYzTvqAngx26aG9/spvCjXckh2SBF+EcBlCFwH1yakwjJL1dR4yarnrfxgI\nEqP4AOYVimAVoQ5FBwnloHe16+3qtDiblU9DeXBUCtS55EcfrEXAMPLEYtXdqU5C\nU9ia4KAjV0dxW1+EFYMwX5eGeb0gDTNHBylV6B/fOSZiQAwDYp4x3B+gAP+a/bWB\nu1umOqtBdWe6L6/83L+JhaTByqV25iVJ4c/UZUnG8926wUlDM9zQvEXuEVvzZ7+m\n4PSNqst/nVOvnLpoG4e0WgcJgANuB33CSWtjWSuYsbhmqQRknGhREXAMPLEZT4fm\nfo0e\n-----END CERTIFICATE-----\n", "ownedBy": "123456789012", "creationDate": 1569365372.053, "autoRegistrationStatus": "DISABLE", "lastModifiedDate": 1569365372.053, "customerVersion": 1, "generationId": "c5c2eb95-140b-4f49-9393-6aaac85b2a90", "validity": { "notBefore": 1569360675.0, "notAfter": 1884720675.0 } } }`For more information, see [DescribeCACertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeCACertificate.html)in the*AWS IoT API Reference*.- 
                    For API details, see [DescribeCaCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-ca-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-certificate`.

- **AWS CLI**
- 
            
                    **To get information about a certificate**The following `describe-certificate`example displays the details for the specified certificate.`aws iot describe-certificate \ --certificate-id``"4f0ba725787aa94d67d2fca420eca022242532e8b3c58e7465c7778b443fd65e"`Output: `{ "certificateDescription": { "certificateArn": "arn:aws:iot:us-west-2:123456789012:cert/4f0ba725787aa94d67d2fca420eca022242532e8b3c58e7465c7778b443fd65e", "certificateId": "4f0ba725787aa94d67d2fca420eca022242532e8b3c58e7465c7778b443fd65e", "status": "ACTIVE", "certificatePem": "-----BEGIN CERTIFICATE----- MIICiTEXAMPLEQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC VVMxCzAJBgNVBEXAMPLEMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6 b24xFDASBgNVBAsTC0lBTSBDEXAMPLElMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5EXAMPLEcNMTEwNDI1MjA0NTIxWhcN MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNEXAMPLEdBMRAwDgYD VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBEXAMPLEz b2xEXAMPLEYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt YXpvbi5jb20wgZ8EXAMPLEZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ 21uUSfwfEvySWtC2XADZ4nB+BLYEXAMPLEpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7EXAMPLEGBzZswY6786m86gpE Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFEXAMPLEAtCu4 nUhVVxYUnEXAMPLE8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb FFBjvSfpJIlJ00zbhNYS5f6GEXAMPLEl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE= -----END CERTIFICATE-----", "ownedBy": "123456789012", "creationDate": 1541022751.983, "lastModifiedDate": 1541022751.983, "customerVersion": 1, "transferData": {}, "generationId": "6974fbed-2e61-4114-bc5e-4204cc79b045", "validity": { "notBefore": 1541022631.0, "notAfter": 2524607999.0 } } }`For more information, see [DescribeCertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeCertificate.html)in the*AWS IoT API Reference*.- 
                    For API details, see [DescribeCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-custom-metric`.

- **AWS CLI**
- 
            
                    **To get information about a Device Defender custom metric**The following `describe-custom-metric`example gets information about a custom metric named`myCustomMetric`.`aws iot describe-custom-metric \ --metric-name``myCustomMetric`Output: `{ "metricName": "myCustomMetric", "metricArn": "arn:aws:iot:us-east-1:1234564789012:custommetric/myCustomMetric", "metricType": "number", "displayName": "My custom metric", "creationDate": 2020-11-17T23:02:12.879000-09:00, "lastModifiedDate": 2020-11-17T23:02:12.879000-09:00 }`For more information, see [Custom metrics](https://docs.aws.amazon.com/iot/latest/developerguide/dd-detect-custom-metrics.html)in the*AWS IoT Core Developer Guide*.- 
                    For API details, see [DescribeCustomMetric](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-custom-metric.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-default-authorizer`.

- **AWS CLI**
- 
            
                    **To get information about the default custom authorizer**The following `describe-default-authorizer`example displays details for the default custom authorizer.`aws iot describe-default-authorizer`Output: `{ "authorizerName": "CustomAuthorizer", "authorizerArn": "arn:aws:iot:us-west-2:123456789012:authorizer/CustomAuthorizer" }`For more information, see [DescribeDefaultAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeDefautAuthorizer.html)in the*AWS IoT API Reference*.- 
                    For API details, see [DescribeDefaultAuthorizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-default-authorizer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-dimension`.

- **AWS CLI**
- 
            
                    **To get information about a dimension**The following `describe-dimension`example gets information about a dimension named`TopicFilterForAuthMessages`.`aws iot describe-dimension \ --name``TopicFilterForAuthMessages`Output: `{ "name": "TopicFilterForAuthMessages", "arn": "arn:aws:iot:eu-west-2:123456789012:dimension/TopicFilterForAuthMessages", "type": "TOPIC_FILTER", "stringValues": [ "device/+/auth" ], "creationDate": 1578620223.255, "lastModifiedDate": 1578620223.255 }`For more information, see [Detect Commands](https://docs.aws.amazon.com/iot/latest/developerguide/DetectCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DescribeDimension](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-dimension.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-domain-configuration`.

- **AWS CLI**
- 
            
                    **To describe a domain configuration**The following `describe-domain-configuration`example displays details about the specified domain configuration.`aws iot describe-domain-configuration \ --domain-configuration-name``"additionalDataDomain"`Output: `{ "domainConfigurationName": "additionalDataDomain", "domainConfigurationArn": "arn:aws:iot:us-east-1:758EXAMPLE143:domainconfiguration/additionalDataDomain/norpw", "domainName": "d055exampleed74y71zfd-ats.beta.us-east-1.iot.amazonaws.com", "serverCertificates": [], "domainConfigurationStatus": "ENABLED", "serviceType": "DATA", "domainType": "AWS_MANAGED", "lastStatusChangeDate": 1601923783.774 }`For more information, see [Configurable Endpoints](https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-configurable-aws.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DescribeDomainConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-domain-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-endpoint`.

- **AWS CLI**
- 
            
                    **Example 1: To get your current AWS endpoint**The following `describe-endpoint`example retrieves the default AWS endpoint to which all commands are applied.`aws iot describe-endpoint`Output: `{ "endpointAddress": "abc123defghijk.iot.us-west-2.amazonaws.com" }`For more information, see [DescribeEndpoint](https://docs.aws.amazon.com/iot/latest/developerguide/iot-commands.html#api-iot-DescribeEndpoint)in the*AWS IoT Developer Guide*.**Example 2: To get your ATS endpoint**The following `describe-endpoint`example retrieves the Amazon Trust Services (ATS) endpoint.`aws iot describe-endpoint \ --endpoint-type``iot:Data-ATS`Output: `{ "endpointAddress": "abc123defghijk-ats.iot.us-west-2.amazonaws.com" }`For more information, see [X.509 Certificates and AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/managing-device-certs.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DescribeEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-event-configurations`.

- **AWS CLI**
- 
            
                    **To show which event types are published**The following `describe-event-configurations`example lists the configuration that controls which events are generated when something is added, updated, or deleted.`aws iot describe-event-configurations`Output: `{ "eventConfigurations": { "CA_CERTIFICATE": { "Enabled": false }, "CERTIFICATE": { "Enabled": false }, "JOB": { "Enabled": false }, "JOB_EXECUTION": { "Enabled": false }, "POLICY": { "Enabled": false }, "THING": { "Enabled": false }, "THING_GROUP": { "Enabled": false }, "THING_GROUP_HIERARCHY": { "Enabled": false }, "THING_GROUP_MEMBERSHIP": { "Enabled": false }, "THING_TYPE": { "Enabled": false }, "THING_TYPE_ASSOCIATION": { "Enabled": false } } }`For more information, see [Event Messages](https://docs.aws.amazon.com/iot/latest/developerguide/iot-events.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DescribeEventConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-event-configurations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-index`.

- **AWS CLI**
- 
            
                    **To retrieve the current status of the thing index**The following `describe-index`example retrieves the current status of the thing index.`aws iot describe-index \ --index-name``"AWS_Things"`Output: `{ "indexName": "AWS_Things", "indexStatus": "ACTIVE", "schema": "REGISTRY_AND_SHADOW_AND_CONNECTIVITY_STATUS" }`For more information, see [Managing Thing Indexing](https://docs.aws.amazon.com/iot/latest/developerguide/managing-index.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DescribeIndex](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-index.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-job-execution`.

- **AWS CLI**
- 
            
                    **To get execution details for a job on a device**The following `describe-job-execution`example gets execution details for the specified job.`aws iot describe-job-execution \ --job-id``"example-job-01"`\ --thing-name`"MyRaspberryPi"`Output: `{ "execution": { "jobId": "example-job-01", "status": "QUEUED", "statusDetails": {}, "thingArn": "arn:aws:iot:us-west-2:123456789012:thing/MyRaspberryPi", "queuedAt": 1560787023.636, "lastUpdatedAt": 1560787023.636, "executionNumber": 1, "versionNumber": 1 } }`For more information, see [Creating and Managing Jobs (CLI)](https://docs.aws.amazon.com/iot/latest/developerguide/manage-job-cli.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DescribeJobExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-job-execution.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-job`.

- **AWS CLI**
- 
            
                    **To get detailed status for a job**The following `describe-job`example gets detailed status for the job whose ID is`example-job-01`.`aws iot describe-job \ --job-id``"example-job-01"`Output: `{ "job": { "jobArn": "arn:aws:iot:us-west-2:123456789012:job/example-job-01", "jobId": "example-job-01", "targetSelection": "SNAPSHOT", "status": "IN_PROGRESS", "targets": [ "arn:aws:iot:us-west-2:123456789012:thing/MyRaspberryPi" ], "description": "example job test", "presignedUrlConfig": {}, "jobExecutionsRolloutConfig": {}, "createdAt": 1560787022.733, "lastUpdatedAt": 1560787026.294, "jobProcessDetails": { "numberOfCanceledThings": 0, "numberOfSucceededThings": 0, "numberOfFailedThings": 0, "numberOfRejectedThings": 0, "numberOfQueuedThings": 1, "numberOfInProgressThings": 0, "numberOfRemovedThings": 0, "numberOfTimedOutThings": 0 }, "timeoutConfig": {} } }`For more information, see [Creating and Managing Jobs (CLI)](https://docs.aws.amazon.com/iot/latest/developerguide/manage-job-cli.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DescribeJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-mitigation-action`.

- **AWS CLI**
- 
            
                    **To view the details for a defined mitigation action**The following `describe-mitigation-action`example displays details for the specified mitigation action.`aws iot describe-mitigation-action \ --action-name``AddThingsToQuarantineGroupAction`Output: `{ "actionName": "AddThingsToQuarantineGroupAction", "actionType": "ADD_THINGS_TO_THING_GROUP", "actionArn": "arn:aws:iot:us-west-2:123456789012:mitigationaction/AddThingsToQuarantineGroupAction", "actionId": "2fd2726d-98e1-4abf-b10f-09465ccd6bfa", "roleArn": "arn:aws:iam::123456789012:role/service-role/MoveThingsToQuarantineGroupRole", "actionParams": { "addThingsToThingGroupParams": { "thingGroupNames": [ "QuarantineGroup1" ], "overrideDynamicGroups": true } }, "creationDate": "2019-12-10T11:09:35.999000-08:00", "lastModifiedDate": "2019-12-10T11:09:35.999000-08:00" }`For more information, see [DescribeMitigationAction (Mitigation Action Commands)](https://docs.aws.amazon.com/iot/latest/developerguide/mitigation-action-commands.html#dd-api-iot-DescribeMitigationAction)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DescribeMitigationAction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-mitigation-action.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-provisioning-template-version`.

- **AWS CLI**
- 
            
                    **To describe a provisioning template version**The following `describe-provisioning-template-version`example describes a provisioning template version.`aws iot describe-provisioning-template-version \ --template-name``MyTestProvisioningTemplate`\ --version-id`1`Output: `{ "versionId": 1, "creationDate": 1589308310.574, "templateBody": "{ \"Parameters\":{ \"SerialNumber\":{ \"Type\":\"String\" }, \"AWS::IoT::Certificate::Id\":{ \"Type\":\"String\" } }, \"Resources\":{ \"certificate\":{ \"Properties\":{ \"CertificateId\":{ \"Ref\":\"AWS::IoT::Certificate::Id\" }, \"Status\":\"Active\" }, \"Type\":\"AWS::IoT::Certificate\" }, \"policy\":{ \"Properties\":{ \"PolicyName\":\"MyIotPolicy\" }, \"Type\":\"AWS::IoT::Policy\" }, \"thing\":{ \"OverrideSettings\":{ \"AttributePayload\":\"MERGE\", \"ThingGroups\":\"DO_NOTHING\", \"ThingTypeName\":\"REPLACE\" }, \"Properties\":{ \"AttributePayload\":{}, \"ThingGroups\":[], \"ThingName\":{ \"Fn::Join\":[ \"\", [ \"DemoGroup_\", {\"Ref\":\"SerialNumber\"} ] ] }, \"ThingTypeName\":\"VirtualThings\" }, \"Type\":\"AWS::IoT::Thing\" } } }", "isDefaultVersion": true }`For more information, see [Provisioning devices that don't have device certificates using fleet provisioning](https://docs.aws.amazon.com/iot/latest/developerguide/provision-wo-cert.html)in the*AWS IoT Core Developers Guide*.- 
                    For API details, see [DescribeProvisioningTemplateVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-provisioning-template-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-provisioning-template`.

- **AWS CLI**
- 
            
                    **To describe a provisioning template**The following `describe-provisioning-template`example describes a provisioning template.`aws iot describe-provisioning-template \ --template-name``MyTestProvisioningTemplate`Output: `{ "templateArn": "arn:aws:iot:us-west-2:57EXAMPLE833:provisioningtemplate/MyTestProvisioningTemplate", "templateName": "MyTestProvisioningTemplate", "creationDate": 1589308310.574, "lastModifiedDate": 1589308345.539, "defaultVersionId": 1, "templateBody": "{ \"Parameters\":{ \"SerialNumber\":{ \"Type\":\"String\" }, \"AWS::IoT::Certificate::Id\":{ \"Type\":\"String\" } }, \"Resources\":{ \"certificate\":{ \"Properties\":{ \"CertificateId\":{ \"Ref\":\"AWS::IoT::Certificate::Id\" }, \"Status\":\"Active\" }, \"Type\":\"AWS::IoT::Certificate\" }, \"policy\":{ \"Properties\":{ \"PolicyName\":\"MyIotPolicy\" }, \"Type\":\"AWS::IoT::Policy\" }, \"thing\":{ \"OverrideSettings\":{ \"AttributePayload\":\"MERGE\", \"ThingGroups\":\"DO_NOTHING\", \"ThingTypeName\":\"REPLACE\" }, \"Properties\":{ \"AttributePayload\":{}, \"ThingGroups\":[], \"ThingName\":{ \"Fn::Join\":[ \"\", [ \"DemoGroup_\", {\"Ref\":\"SerialNumber\"} ] ] }, \"ThingTypeName\":\"VirtualThings\" }, \"Type\":\"AWS::IoT::Thing\" } } }", "enabled": true, "provisioningRoleArn": "arn:aws:iam::571032923833:role/service-role/IoT_access" }`For more information, see [Provisioning devices that don't have device certificates using fleet provisioning](https://docs.aws.amazon.com/iot/latest/developerguide/provision-wo-cert.html)in the*AWS IoT Core Developers Guide*.- 
                    For API details, see [DescribeProvisioningTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-provisioning-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-role-alias`.

- **AWS CLI**
- 
            
                    **To get information about an AWS IoT role alias**The following `describe-role-alias`example displays details for the specified role alias.`aws iot describe-role-alias \ --role-alias``LightBulbRole`Output: `{ "roleAliasDescription": { "roleAlias": "LightBulbRole", "roleAliasArn": "arn:aws:iot:us-west-2:123456789012:rolealias/LightBulbRole", "roleArn": "arn:aws:iam::123456789012:role/light_bulb_role_001", "owner": "123456789012", "credentialDurationSeconds": 3600, "creationDate": 1570558643.221, "lastModifiedDate": 1570558643.221 } }`For more information, see [DescribeRoleAlias](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeRoleAlias.html)in the*AWS IoT API Reference*.- 
                    For API details, see [DescribeRoleAlias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-role-alias.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-scheduled-audit`.

- **AWS CLI**
- 
            
                    **To get information about a scheduled audit**The following `describe-scheduled-audit`example gets detailed information about an AWS IOT Device Defender scheduled audit named`AWSIoTDeviceDefenderDailyAudit`.`aws iot describe-scheduled-audit \ --scheduled-audit-name``AWSIoTDeviceDefenderDailyAudit`Output: `{ "frequency": "DAILY", "targetCheckNames": [ "AUTHENTICATED_COGNITO_ROLE_OVERLY_PERMISSIVE_CHECK", "CONFLICTING_CLIENT_IDS_CHECK", "DEVICE_CERTIFICATE_SHARED_CHECK", "IOT_POLICY_OVERLY_PERMISSIVE_CHECK", "REVOKED_CA_CERTIFICATE_STILL_ACTIVE_CHECK", "UNAUTHENTICATED_COGNITO_ROLE_OVERLY_PERMISSIVE_CHECK" ], "scheduledAuditName": "AWSIoTDeviceDefenderDailyAudit", "scheduledAuditArn": "arn:aws:iot:us-west-2:123456789012:scheduledaudit/AWSIoTDeviceDefenderDailyAudit" }`For more information, see [Audit Commands](https://docs.aws.amazon.com/iot/latest/developerguide/AuditCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DescribeScheduledAudit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-scheduled-audit.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-security-profile`.

- **AWS CLI**
- 
            
                    **To get information about a security profile**The following `describe-security-profile`example gets information about the AWS IoT Device Defender security profile named`PossibleIssue.``aws iot describe-security-profile \ --security-profile-name``PossibleIssue`Output: `{ "securityProfileName": "PossibleIssue", "securityProfileArn": "arn:aws:iot:us-west-2:123456789012:securityprofile/PossibleIssue", "securityProfileDescription": "check to see if authorization fails 10 times in 5 minutes or if cellular bandwidth exceeds 128", "behaviors": [ { "name": "CellularBandwidth", "metric": "aws:message-byte-size", "criteria": { "comparisonOperator": "greater-than", "value": { "count": 128 }, "consecutiveDatapointsToAlarm": 1, "consecutiveDatapointsToClear": 1 } }, { "name": "Authorization", "metric": "aws:num-authorization-failures", "criteria": { "comparisonOperator": "greater-than", "value": { "count": 10 }, "durationSeconds": 300, "consecutiveDatapointsToAlarm": 1, "consecutiveDatapointsToClear": 1 } } ], "version": 1, "creationDate": 1560278102.528, "lastModifiedDate": 1560278102.528 }`For more information, see [Detect Commands](https://docs.aws.amazon.com/iot/latest/developerguide/DetectCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DescribeSecurityProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-security-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-stream`.

- **AWS CLI**
- 
            
                    **To get information about a stream**The following `describe-stream`example displays the details about the specified stream.`aws iot describe-stream \ --stream-id``stream12345`Output: `{ "streamInfo": { "streamId": "stream12345", "streamArn": "arn:aws:iot:us-west-2:123456789012:stream/stream12345", "streamVersion": 1, "description": "This stream is used for Amazon FreeRTOS OTA Update 12345.", "files": [ { "fileId": "123", "s3Location": { "bucket":"codesign-ota-bucket", "key":"48c67f3c-63bb-4f92-a98a-4ee0fbc2bef6" } } ], "createdAt": 1557863215.995, "lastUpdatedAt": 1557863215.995, "roleArn": "arn:aws:iam:123456789012:role/service-role/my_ota_stream_role" } }`For more information, see [DescribeStream](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeStream.html)in the*AWS IoT API Reference*.- 
                    For API details, see [DescribeStream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-stream.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-thing-group`.

- **AWS CLI**
- 
            
                    **To get information about a thing group**The following `describe-thing-group`example gets information about the thing group named`HalogenBulbs`.`aws iot describe-thing-group \ --thing-group-name``HalogenBulbs`Output: `{ "thingGroupName": "HalogenBulbs", "thingGroupId": "f4ec6b84-b42b-499d-9ce1-4dbd4d4f6f6e", "thingGroupArn": "arn:aws:iot:us-west-2:123456789012:thinggroup/HalogenBulbs", "version": 1, "thingGroupProperties": {}, "thingGroupMetadata": { "parentGroupName": "LightBulbs", "rootToParentThingGroups": [ { "groupName": "LightBulbs", "groupArn": "arn:aws:iot:us-west-2:123456789012:thinggroup/LightBulbs" } ], "creationDate": 1559927609.897 } }`For more information, see [Thing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/thing-groups.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [DescribeThingGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-thing-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-thing-type`.

- **AWS CLI**
- 
            
                    **To get information about a thing type**The following `describe-thing-type`example display information about the specified thing type defined in your AWS account.`aws iot describe-thing-type \ --thing-type-name``"LightBulb"`Output: `{ "thingTypeName": "LightBulb", "thingTypeId": "ce3573b0-0a3c-45a7-ac93-4e0ce14cd190", "thingTypeArn": "arn:aws:iot:us-west-2:123456789012:thingtype/LightBulb", "thingTypeProperties": { "thingTypeDescription": "light bulb type", "searchableAttributes": [ "model", "wattage" ] }, "thingTypeMetadata": { "deprecated": false, "creationDate": 1559772562.498 } }`For more information, see [Thing Types](https://docs.aws.amazon.com/iot/latest/developerguide/thing-types.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [DescribeThingType](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-thing-type.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-thing`.

- **AWS CLI**
- 
            
                    **To display detailed information about a thing**The following `describe-thing`example display information about a thing (device) that is defined in the AWS IoT registry for your AWS account.aws iot describe-thing --thing-name "MyLightBulb" Output: `{ "defaultClientId": "MyLightBulb", "thingName": "MyLightBulb", "thingId": "40da2e73-c6af-406e-b415-15acae538797", "thingArn": "arn:aws:iot:us-west-2:123456789012:thing/MyLightBulb", "thingTypeName": "LightBulb", "attributes": { "model": "123", "wattage": "75" }, "version": 1 }`For more information, see [How to Manage Things with the Registry](https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [DescribeThing](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-thing.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detach-policy`.

- **AWS CLI**
- 
            
                    **Example 1: To detach an AWS IoT policy from a thing group**The following `detach-policy`example detaches the specified policy from a thing group and, by extension, from all things in that group and any of the group's child groups.`aws iot detach-policy \ --target``"arn:aws:iot:us-west-2:123456789012:thinggroup/LightBulbs"`\ --policy-name`"MyFirstGroup_Core-policy"`This command produces no output. For more information, see [Thing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/thing-groups.html)in the*AWS IoT Developers Guide*.**Example 2: To detach an AWS IoT policy from a device certificate**The following `detach-policy`example detaches the TemperatureSensorPolicy policy from a device certificate identified by ARN.`aws iot detach-policy \ --policy-name``TemperatureSensorPolicy`\ --target`arn:aws:iot:us-west-2:123456789012:cert/488b6a7f2acdeb00a77384e63c4e40b18b1b3caaae57b7272ba44c45e3448142`This command produces no output. - 
                    For API details, see [DetachPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/detach-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detach-security-profile`.

- **AWS CLI**
- 
            
                    **To disassociate a security profile from a target**The following `detach-security-profile`example removes the association between the AWS IoT Device Defender security profile named`Testprofile`and the all registered things target.`aws iot detach-security-profile \ --security-profile-name``Testprofile`\ --security-profile-target-arn`"arn:aws:iot:us-west-2:123456789012:all/registered-things"`This command produces no output. For more information, see [Detect Commands](https://docs.aws.amazon.com/iot/latest/developerguide/DetectCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DetachSecurityProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/detach-security-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detach-thing-principal`.

- **AWS CLI**
- 
            
                    **To detach a certificate/principal from a thing**The following `detach-thing-principal`example removes a certificate that represents a principal from the specified thing.`aws iot detach-thing-principal \ --thing-name``"MyLightBulb"`\ --principal`"arn:aws:iot:us-west-2:123456789012:cert/604c48437a57b7d5fc5d137c5be75011c6ee67c9a6943683a1acb4b1626bac36"`This command produces no output. For more information, see [How to Manage Things with the Registry](https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [DetachThingPrincipal](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/detach-thing-principal.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-topic-rule`.

- **AWS CLI**
- 
            
                    **To disable a topic rule**The following `disable-topic-rule`example disables the specified topic rule.`aws iot disable-topic-rule \ --rule-name``"MyPlantPiMoistureAlertRule"`This command produces no output. For more information, see [Viewing Your Rules](https://docs.aws.amazon.com/iot/latest/developerguide/iot-view-rules.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [DisableTopicRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/disable-topic-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-topic-rule`.

- **AWS CLI**
- 
            
                    **To enable a topic rule**The following `enable-topic-rule`example enables (or re-enables) the specified topic rule.`aws iot enable-topic-rule \ --rule-name``"MyPlantPiMoistureAlertRule"`This command produces no output. For more information, see [Viewing Your Rules](https://docs.aws.amazon.com/iot/latest/developerguide/iot-view-rules.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [EnableTopicRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/enable-topic-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-behavior-model-training-summaries`.

- **AWS CLI**
- 
            
                    **To list a Device Defender's ML Detect Security Profile training model's status**The following `get-behavior-model-training-summaries`example lists model training status for the configured behaviors in the chosen Security Profile. For each behavior, the name, model status, and percentage of datapoints collected are listed.`aws iot get-behavior-model-training-summaries \ --security-profile-name``MySecuirtyProfileName`Output: `{ "summaries": [ { "securityProfileName": "MySecuirtyProfileName", "behaviorName": "Messages_sent_ML_behavior", "modelStatus": "PENDING_BUILD", "datapointsCollectionPercentage": 0.0 }, { "securityProfileName": "MySecuirtyProfileName", "behaviorName": "Messages_received_ML_behavior", "modelStatus": "PENDING_BUILD", "datapointsCollectionPercentage": 0.0 }, { "securityProfileName": "MySecuirtyProfileName", "behaviorName": "Authorization_failures_ML_behavior", "modelStatus": "PENDING_BUILD", "datapointsCollectionPercentage": 0.0 }, { "securityProfileName": "MySecuirtyProfileName", "behaviorName": "Message_size_ML_behavior", "modelStatus": "PENDING_BUILD", "datapointsCollectionPercentage": 0.0 }, { "securityProfileName": "MySecuirtyProfileName", "behaviorName": "Connection_attempts_ML_behavior", "modelStatus": "PENDING_BUILD", "datapointsCollectionPercentage": 0.0 }, { "securityProfileName": "MySPNoALerts", "behaviorName": "Disconnects_ML_behavior", "modelStatus": "PENDING_BUILD", "datapointsCollectionPercentage": 0.0 } ] }`For more information, see [GetBehaviorModelTrainingSummaries (Detect Commands)](https://docs.aws.amazon.com/iot/latest/developerguide/detect-commands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [GetBehaviorModelTrainingSummaries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-behavior-model-training-summaries.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-cardinality`.

- **AWS CLI**
- 
            
                    **To return the approximate count of unique values that match the query**You can use the following setup script to create 10 things representing 10 temperature sensors. Each new thing has 3 attributes. `# Bash script. If in other shells, type `bash` before running Temperatures=(70 71 72 73 74 75 47 97 98 99) Racks=(Rack1 Rack1 Rack2 Rack2 Rack3 Rack4 Rack5 Rack6 Rack6 Rack6) IsNormal=(true true true true true true false false false false) for ((i=0; i<10 ; i++)) do thing=$(aws iot create-thing --thing-name "TempSensor$i" --attribute-payload attributes="{temperature=${Temperatures[i]},rackId=${Racks[i]},stateNormal=${IsNormal[i]}}") aws iot describe-thing --thing-name "TempSensor$i" done`Example output of the setup script: `{ "version": 1, "thingName": "TempSensor0", "defaultClientId": "TempSensor0", "attributes": { "rackId": "Rack1", "stateNormal": "true", "temperature": "70" }, "thingArn": "arn:aws:iot:us-east-1:123456789012:thing/TempSensor0", "thingId": "example1-90ab-cdef-fedc-ba987example" }`The following `get-cardinality`example queries the 10 sensors created by the setup script and returns the number of racks that have temperature sensors reporting abnormal temperature values. If the temperature value is below 60 or above 80, the temperature sensor is in an abnormal state.`aws iot get-cardinality \ --aggregation-field``"attributes.rackId"`\ --query-string`"thingName:TempSensor* AND attributes.stateNormal:false"`Output: `{ "cardinality": 2 }`For more information, see Querying for Aggregate Data<https://docs.aws.amazon.com/iot/latest/developerguide/index-aggregate.html> in the *AWS IoT Developer Guide*.- 
                    For API details, see [GetCardinality](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-cardinality.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-effective-policies`.

- **AWS CLI**
- 
            
                    **To list the policies that effect a thing**The following `get-effective-policies`example lists the policies that effect the specified thing, including policies attached to any groups to which it belongs.`aws iot get-effective-policies \ --thing-name``TemperatureSensor-001`\ --principal`arn:aws:iot:us-west-2:123456789012:cert/488b6a7f2acdeb00a77384e63c4e40b18b1b3caaae57b7272ba44c45e3448142`Output: `{ "effectivePolicies": [ { "policyName": "TemperatureSensorPolicy", "policyArn": "arn:aws:iot:us-west-2:123456789012:policy/TemperatureSensorPolicy", "policyDocument": "{ \"Version\": \"2012-10-17\", \"Statement\": [ { \"Effect\": \"Allow\", \"Action\": [ \"iot:Publish\", \"iot:Receive\" ], \"Resource\": [ \"arn:aws:iot:us-west-2:123456789012:topic/topic_1\", \"arn:aws:iot:us-west-2:123456789012:topic/topic_2\" ] }, { \"Effect\": \"Allow\", \"Action\": [ \"iot:Subscribe\" ], \"Resource\": [ \"arn:aws:iot:us-west-2:123456789012:topicfilter/topic_1\", \"arn:aws:iot:us-west-2:123456789012:topicfilter/topic_2\" ] }, { \"Effect\": \"Allow\", \"Action\": [ \"iot:Connect\" ], \"Resource\": [ \"arn:aws:iot:us-west-2:123456789012:client/basicPubSub\" ] } ] }" } ] }`For more information, see [Get Effective Policies for a Thing](https://docs.aws.amazon.com/iot/latest/developerguide/thing-groups.html#group-get-effective-policies)in the*AWS IoT Developers Guide*.- 
                    For API details, see [GetEffectivePolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-effective-policies.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-indexing-configuration`.

- **AWS CLI**
- 
            
                    **To get the thing indexing configuration**The following `get-indexing-configuration`example gets the current configuration data for AWS IoT fleet indexing.`aws iot get-indexing-configuration`Output: `{ "thingIndexingConfiguration": { "thingIndexingMode": "OFF", "thingConnectivityIndexingMode": "OFF" }, "thingGroupIndexingConfiguration": { "thingGroupIndexingMode": "OFF" } }`For more information, see [Managing Thing Indexing](https://docs.aws.amazon.com/iot/latest/developerguide/managing-index.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [GetIndexingConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-indexing-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-job-document`.

- **AWS CLI**
- 
            
                    **To retrieve the document for a job**The following `get-job-document`example displays details about the document for the job whose ID is`example-job-01`.`aws iot get-job-document \ --job-id``"example-job-01"`Output: `{ "document": "\n{\n \"operation\":\"customJob\",\n \"otherInfo\":\"someValue\"\n}\n" }`For more information, see [Creating and Managing Jobs (CLI)](https://docs.aws.amazon.com/iot/latest/developerguide/manage-job-cli.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [GetJobDocument](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-job-document.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-logging-options`.

- **AWS CLI**
- 
            
                    **To get the logging options**The following `get-logging-options`example gets the current logging options for your AWS account.`aws iot get-logging-options`Output: `{ "roleArn": "arn:aws:iam::123456789012:role/service-role/iotLoggingRole", "logLevel": "ERROR" }`For more information, see title in the *AWS IoT Developer Guide*.- 
                    For API details, see [GetLoggingOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-logging-options.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-ota-update`.

- **AWS CLI**
- 
            
                    **To retrieve information about an OTA Update**The following `get-ota-update`example displays details about the specified OTA Update.`aws iot get-ota-update \ --ota-update-id``ota12345`Output: `{ "otaUpdateInfo": { "otaUpdateId": "ota12345", "otaUpdateArn": "arn:aws:iot:us-west-2:123456789012:otaupdate/itsaupdate", "creationDate": 1557863215.995, "lastModifiedDate": 1557863215.995, "description": "A critical update needed right away.", "targets": [ "device1", "device2", "device3", "device4" ], "targetSelection": "SNAPSHOT", "protocols": ["HTTP"], "awsJobExecutionsRolloutConfig": { "maximumPerMinute": 10 }, "otaUpdateFiles": [ { "fileName": "firmware.bin", "fileLocation": { "stream": { "streamId": "004", "fileId":123 } }, "codeSigning": { "awsSignerJobId": "48c67f3c-63bb-4f92-a98a-4ee0fbc2bef6" } } ], "roleArn": "arn:aws:iam:123456789012:role/service-role/my_ota_role" "otaUpdateStatus": "CREATE_COMPLETE", "awsIotJobId": "job54321", "awsIotJobArn": "arn:aws:iot:us-west-2:123456789012:job/job54321", "errorInfo": { } } }`For more information, see [GetOTAUpdate](https://docs.aws.amazon.com/iot/latest/apireference/API_GetOTAUpdate.html)in the*AWS IoT API Reference*.- 
                    For API details, see [GetOtaUpdate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-ota-update.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-percentiles`.

- **AWS CLI**
- 
            
                    **To group the aggregated values that match the query into percentile groupings**You can use the following setup script to create 10 things representing 10 temperature sensors. Each new thing has 1 attribute. `# Bash script. If in other shells, type `bash` before running Temperatures=(70 71 72 73 74 75 47 97 98 99) for ((i=0; i<10 ; i++)) do thing=$(aws iot create-thing --thing-name "TempSensor$i" --attribute-payload attributes="{temperature=${Temperatures[i]}}") aws iot describe-thing --thing-name "TempSensor$i" done`Example output of the setup script: `{ "version": 1, "thingName": "TempSensor0", "defaultClientId": "TempSensor0", "attributes": { "temperature": "70" }, "thingArn": "arn:aws:iot:us-east-1:123456789012:thing/TempSensor0", "thingId": "example1-90ab-cdef-fedc-ba987example" }`The following `get-percentiles`example queries the 10 sensors created by the setup script and returns a value for each percentile group specified. The percentile group "10" contains the aggregated field value that occurs in approximately 10 percent of the values that match the query. In the following output, {"percent": 10.0, "value": 67.7} means approximately 10.0% of the temperature values are below 67.7.`aws iot get-percentiles \ --aggregation-field``"attributes.temperature"`\ --query-string`"thingName:TempSensor*"`\ --percents`10``25``50``75``90`Output: `{ "percentiles": [ { "percent": 10.0, "value": 67.7 }, { "percent": 25.0, "value": 71.25 }, { "percent": 50.0, "value": 73.5 }, { "percent": 75.0, "value": 91.5 }, { "percent": 90.0, "value": 98.1 } ] }`For more information, see [Querying for Aggregate Data](https://docs.aws.amazon.com/iot/latest/developerguide/index-aggregate.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [GetPercentiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-percentiles.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-policy-version`.

- **AWS CLI**
- 
            
                    **To get information about a specific version of a policy**The following `get-policy-version`example gets information about the first version of the specified policy.`aws iot get-policy \ --policy-name``UpdateDeviceCertPolicy`--policy-version-id`"1"`Output: `{ "policyArn": "arn:aws:iot:us-west-2:123456789012:policy/UpdateDeviceCertPolicy", "policyName": "UpdateDeviceCertPolicy", "policyDocument": "{ \"Version\": \"2012-10-17\", \"Statement\": [ { \"Effect\": \"Allow\", \"Action\": \"iot:UpdateCertificate\", \"Resource\": \"*\" } ] }", "policyVersionId": "1", "isDefaultVersion": false, "creationDate": 1559925941.924, "lastModifiedDate": 1559926175.458, "generationId": "5066f1b6712ce9d2a1e56399771649a272d6a921762fead080e24fe52f24e042" }`For more information, see [AWS IoT Policies](https://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [GetPolicyVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-policy-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-policy`.

- **AWS CLI**
- 
            
                    **To get information about the default version of a policy**The following `get-policy`example retrieves information about the default version of the specified policy.`aws iot get-policy \ --policy-name``UpdateDeviceCertPolicy`Output: `{ "policyName": "UpdateDeviceCertPolicy", "policyArn": "arn:aws:iot:us-west-2:123456789012:policy/UpdateDeviceCertPolicy", "policyDocument": "{ \"Version\": \"2012-10-17\", \"Statement\": [ { \"Effect\": \"Allow\", \"Action\": \"iot:UpdateCertificate\", \"Resource\": \"*\" } ] }", "defaultVersionId": "2", "creationDate": 1559925941.924, "lastModifiedDate": 1559925941.924, "generationId": "5066f1b6712ce9d2a1e56399771649a272d6a921762fead080e24fe52f24e042" }`For more information, see [AWS IoT Policies](https://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [GetPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-registration-code`.

- **AWS CLI**
- 
            
                    **To get your AWS account-specific registration code**The following `get-registration-code`example retrieves your AWS account-specific registration code.`aws iot get-registration-code`Output: `{ "registrationCode": "15c51ae5e36ba59ba77042df1115862076bea4bd15841c838fcb68d5010a614c" }`For more information, see [Use Your Own Certificate](https://docs.aws.amazon.com/iot/latest/developerguide/device-certs-your-own.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [GetRegistrationCode](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-registration-code.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-statistics`.

- **AWS CLI**
- 
            
                    **To search the device index for aggregate data**The following `get-statistics`example returns the number of things that have a property called`connectivity.connected`set to`false`(that is, the number of devices that are not connected) in their device shadow.`aws iot get-statistics \ --index-name``AWS_Things`\ --query-string`"connectivity.connected:false"`Output: `{ "statistics": { "count": 6 } }`For more information, see [Getting Statistics About Your Device Fleet](https://docs.aws.amazon.com/iot/latest/developerguide/index-aggregate.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [GetStatistics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-statistics.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-topic-rule-destination`.

- **AWS CLI**
- 
            
                    **To get a topic rule destination**The following `get-topic-rule-destination`example gets information about a topic rule destination.`aws iot get-topic-rule-destination \ --arn``"arn:aws:iot:us-west-2:123456789012:ruledestination/http/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE"`Output: `{ "topicRuleDestination": { "arn": "arn:aws:iot:us-west-2:123456789012:ruledestination/http/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "status": "DISABLED", "httpUrlProperties": { "confirmationUrl": "https://example.com" } } }`For more information, see [Working with topic rule destinations](https://docs.aws.amazon.com/iot/latest/developerguide/rule-destination.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [GetTopicRuleDestination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-topic-rule-destination.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-topic-rule`.

- **AWS CLI**
- 
            
                    **To get information about a rule**The following `get-topic-rule`example gets information about the specified rule.`aws iot get-topic-rule \ --rule-name``MyRPiLowMoistureAlertRule`Output: `{ "ruleArn": "arn:aws:iot:us-west-2:123456789012:rule/MyRPiLowMoistureAlertRule", "rule": { "ruleName": "MyRPiLowMoistureAlertRule", "sql": "SELECT * FROM '$aws/things/MyRPi/shadow/update/accepted' WHERE state.reported.moisture = 'low'\n ", "description": "Sends an alert whenever soil moisture level readings are too low.", "createdAt": 1558624363.0, "actions": [ { "sns": { "targetArn": "arn:aws:sns:us-west-2:123456789012:MyRPiLowMoistureTopic", "roleArn": "arn:aws:iam::123456789012:role/service-role/MyRPiLowMoistureTopicRole", "messageFormat": "RAW" } } ], "ruleDisabled": false, "awsIotSqlVersion": "2016-03-23" } }`For more information, see [Viewing Your Rules](https://docs.aws.amazon.com/iot/latest/developerguide/iot-managae-rule.html#iot-view-rules)in the*AWS IoT Developers Guide*.- 
                    For API details, see [GetTopicRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-topic-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-v2-logging-options`.

- **AWS CLI**
- 
            
                    **To list the current logging options**The following `get-v2-logging-options`example lists the current logging options for AWS IoT.`aws iot get-v2-logging-options`Output: `{ "roleArn": "arn:aws:iam::094249569039:role/service-role/iotLoggingRole", "defaultLogLevel": "WARN", "disableAllLogs": false }`For more information, see title in the *AWS IoT Developer Guide*.- 
                    For API details, see [GetV2LoggingOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-v2-logging-options.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-active-violations`.

- **AWS CLI**
- 
            
                    **To list the active violations**The following `list-active-violations`example lists all violations for the specified security profile.`aws iot list-active-violations \ --security-profile-name``Testprofile`Output: `{ "activeViolations": [ { "violationId": "174db59167fa474c80a652ad1583fd44", "thingName": "iotconsole-1560269126751-1", "securityProfileName": "Testprofile", "behavior": { "name": "Authorization", "metric": "aws:num-authorization-failures", "criteria": { "comparisonOperator": "greater-than", "value": { "count": 10 }, "durationSeconds": 300, "consecutiveDatapointsToAlarm": 1, "consecutiveDatapointsToClear": 1 } }, "lastViolationValue": { "count": 0 }, "lastViolationTime": 1560293700.0, "violationStartTime": 1560279000.0 }, { "violationId": "c8a9466a093d3b7b35cd44ca58bdbeab", "thingName": "TvnQoEoU", "securityProfileName": "Testprofile", "behavior": { "name": "CellularBandwidth", "metric": "aws:message-byte-size", "criteria": { "comparisonOperator": "greater-than", "value": { "count": 128 }, "consecutiveDatapointsToAlarm": 1, "consecutiveDatapointsToClear": 1 } }, "lastViolationValue": { "count": 110 }, "lastViolationTime": 1560369000.0, "violationStartTime": 1560276600.0 }, { "violationId": "74aa393adea02e6648f3ac362beed55e", "thingName": "iotconsole-1560269232412-2", "securityProfileName": "Testprofile", "behavior": { "name": "Authorization", "metric": "aws:num-authorization-failures", "criteria": { "comparisonOperator": "greater-than", "value": { "count": 10 }, "durationSeconds": 300, "consecutiveDatapointsToAlarm": 1, "consecutiveDatapointsToClear": 1 } }, "lastViolationValue": { "count": 0 }, "lastViolationTime": 1560276600.0, "violationStartTime": 1560276600.0 }, { "violationId": "1e6ab5f7cf39a1466fcd154e1377e406", "thingName": "TvnQoEoU", "securityProfileName": "Testprofile", "behavior": { "name": "Authorization", "metric": "aws:num-authorization-failures", "criteria": { "comparisonOperator": "greater-than", "value": { "count": 10 }, "durationSeconds": 300, "consecutiveDatapointsToAlarm": 1, "consecutiveDatapointsToClear": 1 } }, "lastViolationValue": { "count": 0 }, "lastViolationTime": 1560369000.0, "violationStartTime": 1560276600.0 } ] }`- 
                    For API details, see [ListActiveViolations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-active-violations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-attached-policies`.

- **AWS CLI**
- 
            
                    **Example 1: To list the policies attached to a group**The following `list-attached-policies`example lists the policies that are attached to the specified group.`aws iot list-attached-policies \ --target``"arn:aws:iot:us-west-2:123456789012:thinggroup/LightBulbs"`Output: `{ "policies": [ { "policyName": "UpdateDeviceCertPolicy", "policyArn": "arn:aws:iot:us-west-2:123456789012:policy/UpdateDeviceCertPolicy" } ] }`For more information, see [Thing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/thing-groups.html)in the*AWS IoT Developers Guide*.**Example 2: To list the policies attached to a device certificate**The following `list-attached-policies`example lists the AWS IoT policies attached to the device certificate. The certificate is identified by its ARN.`aws iot list-attached-policies \ --target``arn:aws:iot:us-west-2:123456789012:cert/488b6a7f2acdeb00a77384e63c4e40b18b1b3caaae57b7272ba44c45e3448142`Output: `{ "policies": [ { "policyName": "TemperatureSensorPolicy", "policyArn": "arn:aws:iot:us-west-2:123456789012:policy/TemperatureSensorPolicy" } ] }`For more information, see [Thing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/thing-groups.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [ListAttachedPolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-attached-policies.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-audit-findings`.

- **AWS CLI**
- 
            
                    **Example 1: To list all findings from an audit**The following `list-audit-findings`example lists all findings from an AWS IoT Device Defender audit with a specified task ID.`aws iot list-audit-findings \ --task-id``a3aea009955e501a31b764abe1bebd3d`Output: `{ "findings": [] }`**Example 2: To list findings for an audit check type**The following `list-audit-findings`example shows findings from AWS IoT Device Defender audits that ran between June 5, 2019 and June 19, 2019 in which devices are sharing a device certificate. When you specify a check name, you must provide a start and end time.`aws iot list-audit-findings \ --check-name``DEVICE_CERTIFICATE_SHARED_CHECK`\ --start-time`1559747125`\ --end-time`1560962028`Output: `{ "findings": [ { "taskId": "eeef61068b0eb03c456d746c5a26ee04", "checkName": "DEVICE_CERTIFICATE_SHARED_CHECK", "taskStartTime": 1560161017.172, "findingTime": 1560161017.592, "severity": "CRITICAL", "nonCompliantResource": { "resourceType": "DEVICE_CERTIFICATE", "resourceIdentifier": { "deviceCertificateId": "b193ab7162c0fadca83246d24fa090300a1236fe58137e121b011804d8ac1d6b" } }, "relatedResources": [ { "resourceType": "CLIENT_ID", "resourceIdentifier": { "clientId": "ZipxgAIl" }, "additionalInfo": { "CONNECTION_TIME": "1560086374068" } }, { "resourceType": "CLIENT_ID", "resourceIdentifier": { "clientId": "ZipxgAIl" }, "additionalInfo": { "CONNECTION_TIME": "1560081552187", "DISCONNECTION_TIME": "1560086371552" } }, { "resourceType": "CLIENT_ID", "resourceIdentifier": { "clientId": "ZipxgAIl" }, "additionalInfo": { "CONNECTION_TIME": "1559289863631", "DISCONNECTION_TIME": "1560081532716" } } ], "reasonForNonCompliance": "Certificate shared by one or more devices.", "reasonForNonComplianceCode": "CERTIFICATE_SHARED_BY_MULTIPLE_DEVICES" }, { "taskId": "bade6b5efd2e1b1569822f6021b39cf5", "checkName": "DEVICE_CERTIFICATE_SHARED_CHECK", "taskStartTime": 1559988217.27, "findingTime": 1559988217.655, "severity": "CRITICAL", "nonCompliantResource": { "resourceType": "DEVICE_CERTIFICATE", "resourceIdentifier": { "deviceCertificateId": "b193ab7162c0fadca83246d24fa090300a1236fe58137e121b011804d8ac1d6b" } }, "relatedResources": [ { "resourceType": "CLIENT_ID", "resourceIdentifier": { "clientId": "xShGENLW" }, "additionalInfo": { "CONNECTION_TIME": "1559972350825" } }, { "resourceType": "CLIENT_ID", "resourceIdentifier": { "clientId": "xShGENLW" }, "additionalInfo": { "CONNECTION_TIME": "1559255062002", "DISCONNECTION_TIME": "1559972350616" } } ], "reasonForNonCompliance": "Certificate shared by one or more devices.", "reasonForNonComplianceCode": "CERTIFICATE_SHARED_BY_MULTIPLE_DEVICES" }, { "taskId": "c23f6233ba2d35879c4bb2810fb5ffd6", "checkName": "DEVICE_CERTIFICATE_SHARED_CHECK", "taskStartTime": 1559901817.31, "findingTime": 1559901817.767, "severity": "CRITICAL", "nonCompliantResource": { "resourceType": "DEVICE_CERTIFICATE", "resourceIdentifier": { "deviceCertificateId": "b193ab7162c0fadca83246d24fa090300a1236fe58137e121b011804d8ac1d6b" } }, "relatedResources": [ { "resourceType": "CLIENT_ID", "resourceIdentifier": { "clientId": "TvnQoEoU" }, "additionalInfo": { "CONNECTION_TIME": "1559826729768" } }, { "resourceType": "CLIENT_ID", "resourceIdentifier": { "clientId": "TvnQoEoU" }, "additionalInfo": { "CONNECTION_TIME": "1559345920964", "DISCONNECTION_TIME": "1559826728402" } } ], "reasonForNonCompliance": "Certificate shared by one or more devices.", "reasonForNonComplianceCode": "CERTIFICATE_SHARED_BY_MULTIPLE_DEVICES" } ] }`For more information, see [Audit Commands](https://docs.aws.amazon.com/iot/latest/developerguide/AuditCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [ListAuditFindings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-audit-findings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-audit-mitigation-actions-executions`.

- **AWS CLI**
- 
            
                    **To list the details of an audit mitigation action execution**An audit mitigation action task applies a mitigation action to one or more findings from an AWS IoT Device Defender audit. The following `list-audit-mitigation-actions-executions`example lists the details for the mitigation action task with the specified`taskId`and for the specified finding.`aws iot list-audit-mitigation-actions-executions \ --task-id``myActionsTaskId`\ --finding-id`0edbaaec-2fe1-4cf5-abc9-d4c3e51f7464`Output: `{ "actionsExecutions": [ { "taskId": "myActionsTaskId", "findingId": "0edbaaec-2fe1-4cf5-abc9-d4c3e51f7464", "actionName": "ResetPolicyVersionAction", "actionId": "1ea0b415-bef1-4a01-bd13-72fb63c59afb", "status": "COMPLETED", "startTime": "2019-12-10T15:19:13.279000-08:00", "endTime": "2019-12-10T15:19:13.337000-08:00" } ] }`For more information, see [ListAuditMitigationActionsExecutions (Mitigation Action Commands)](https://docs.aws.amazon.com/iot/latest/developerguide/mitigation-action-commands.html#dd-api-iot-ListAuditMitigationActionsExecutions)in the*AWS IoT Developer Guide*.- 
                    For API details, see [ListAuditMitigationActionsExecutions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-audit-mitigation-actions-executions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-audit-mitigation-actions-tasks`.

- **AWS CLI**
- 
            
                    **To list audit mitigation action tasks**The following `list-audit-mitigation-actions-tasks`example lists the mitigation actions that were applied to findings within the specified time period.`aws iot list-audit-mitigation-actions-tasks \ --start-time``1594157400`\ --end-time`1594157430`Output: `{ "tasks": [ { "taskId": "0062f2d6-3999-488f-88c7-bef005414103", "startTime": "2020-07-07T14:30:15.172000-07:00", "taskStatus": "COMPLETED" } ] }`For more information, see [ListAuditMitigationActionsTasks (Mitigation Action Commands)](https://docs.aws.amazon.com/iot/latest/developerguide/mitigation-action-commands.html#dd-api-iot-ListAuditMitigationActionsTasks)in the*AWS IoT Developer Guide*.- 
                    For API details, see [ListAuditMitigationActionsTasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-audit-mitigation-actions-tasks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-audit-suppressions`.

- **AWS CLI**
- 
            
                    **To list all audit finding suppressions**The following `list-audit-suppressions`example lists all active audit finding suppressions.`aws iot list-audit-suppressions`Output: `{ "suppressions": [ { "checkName": "DEVICE_CERTIFICATE_EXPIRING_CHECK", "resourceIdentifier": { "deviceCertificateId": "c7691e<shortened>" }, "expirationDate": 1597881600.0, "suppressIndefinitely": false } ] }`For more information, see [Audit finding suppressions](https://docs.aws.amazon.com/iot/latest/developerguide/audit-finding-suppressions.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [ListAuditSuppressions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-audit-suppressions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-audit-tasks`.

- **AWS CLI**
- 
            
                    **To list all findings from an audit**The following `list-audit-tasks`example lists the audit tasks that ran between June 5, 2019 and June 12, 2019.`aws iot list-audit-tasks \ --start-time``1559747125`\ --end-time`1560357228`Output: `{ "tasks": [ { "taskId": "a3aea009955e501a31b764abe1bebd3d", "taskStatus": "COMPLETED", "taskType": "ON_DEMAND_AUDIT_TASK" }, { "taskId": "f76b4b5102b632cd9ae38a279c266da1", "taskStatus": "COMPLETED", "taskType": "SCHEDULED_AUDIT_TASK" }, { "taskId": "51d9967d9f9ff4d26529505f6d2c444a", "taskStatus": "COMPLETED", "taskType": "SCHEDULED_AUDIT_TASK" }, { "taskId": "eeef61068b0eb03c456d746c5a26ee04", "taskStatus": "COMPLETED", "taskType": "SCHEDULED_AUDIT_TASK" }, { "taskId": "041c49557b7c7b04c079a49514b55589", "taskStatus": "COMPLETED", "taskType": "SCHEDULED_AUDIT_TASK" }, { "taskId": "82c7f2afac1562d18a4560be73998acc", "taskStatus": "COMPLETED", "taskType": "SCHEDULED_AUDIT_TASK" }, { "taskId": "bade6b5efd2e1b1569822f6021b39cf5", "taskStatus": "COMPLETED", "taskType": "SCHEDULED_AUDIT_TASK" }, { "taskId": "c23f6233ba2d35879c4bb2810fb5ffd6", "taskStatus": "COMPLETED", "taskType": "SCHEDULED_AUDIT_TASK" }, { "taskId": "ac9086b7222a2f5e2e17bb6fd30b3aeb", "taskStatus": "COMPLETED", "taskType": "SCHEDULED_AUDIT_TASK" } ] }`For more information, see [Audit Commands](https://docs.aws.amazon.com/iot/latest/developerguide/AuditCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [ListAuditTasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-audit-tasks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-authorizers`.

- **AWS CLI**
- 
            
                    **To list your custom authorizer**The following `list-authorizers`example lists the custom authorizers in your AWS account.`aws iot list-authorizers`Output: `{ "authorizers": [ { "authorizerName": "CustomAuthorizer", "authorizerArn": "arn:aws:iot:us-west-2:123456789012:authorizer/CustomAuthorizer" }, { "authorizerName": "CustomAuthorizer2", "authorizerArn": "arn:aws:iot:us-west-2:123456789012:authorizer/CustomAuthorizer2" }, { "authorizerName": "CustomAuthorizer3", "authorizerArn": "arn:aws:iot:us-west-2:123456789012:authorizer/CustomAuthorizer3" } ] }`For more information, see [ListAuthorizers](https://docs.aws.amazon.com/iot/latest/apireference/API_ListAuthorizers.html)in the*AWS IoT API Reference*.- 
                    For API details, see [ListAuthorizers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-authorizers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-billing-groups`.

- **AWS CLI**
- 
            
                    **To list the billing groups for your AWS account and region**The following `list-billing-groups`example lists all billing groups that are defined for your AWS account and AWS Region.`aws iot list-billing-groups`Output: `{ "billingGroups": [ { "groupName": "GroupOne", "groupArn": "arn:aws:iot:us-west-2:123456789012:billinggroup/GroupOne" } ] }`For more information, see [Billing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/tagging-iot-billing-groups.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [ListBillingGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-billing-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-ca-certificates`.

- **AWS CLI**
- 
            
                    **To list the CA certificates registered in your AWS account**The following `list-ca-certificates`example lists the CA certificates registered in your AWS account.`aws iot list-ca-certificates`Output: `{ "certificates": [ { "certificateArn": "arn:aws:iot:us-west-2:123456789012:cacert/f4efed62c0142f16af278166f61962501165c4f0536295207426460058cd1467", "certificateId": "f4efed62c0142f16af278166f61962501165c4f0536295207426460058cd1467", "status": "INACTIVE", "creationDate": 1569365372.053 } ] }`For more information, see [Use Your Own Certificate](https://docs.aws.amazon.com/iot/latest/developerguide/device-certs-your-own.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [ListCaCertificates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-ca-certificates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-certificates-by-ca`.

- **AWS CLI**
- 
            
                    **To list all device certificates signed with a CA certificate**The following `list-certificates-by-ca`example lists all device certificates in your AWS account that are signed with the specified CA certificate.`aws iot list-certificates-by-ca \ --ca-certificate-id``f4efed62c0142f16af278166f61962501165c4f0536295207426460058cd1467`Output: `{ "certificates": [ { "certificateArn": "arn:aws:iot:us-west-2:123456789012:cert/488b6a7f2acdeb00a77384e63c4e40b18b1b3caaae57b7272ba44c45e3448142", "certificateId": "488b6a7f2acdeb00a77384e63c4e40b18b1b3caaae57b7272ba44c45e3448142", "status": "ACTIVE", "creationDate": 1569363250.557 } ] }`For more information, see [ListCertificatesByCA](https://docs.aws.amazon.com/iot/latest/apireference/API_ListCertificatesByCA.html)in the*AWS IoT API Reference*.- 
                    For API details, see [ListCertificatesByCa](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-certificates-by-ca.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-certificates`.

- **AWS CLI**
- 
            
                    **Example 1: To list the certificates registered in your AWS account**The following `list-certificates`example lists all certificates registered in your account. If you have more than the default paging limit of 25, you can use the`nextMarker`response value from this command and supply it to the next command to get the next batch of results. Repeat until`nextMarker`returns without a value.`aws iot list-certificates`Output: `{ "certificates": [ { "certificateArn": "arn:aws:iot:us-west-2:123456789012:cert/604c48437a57b7d5fc5d137c5be75011c6ee67c9a6943683a1acb4b1626bac36", "certificateId": "604c48437a57b7d5fc5d137c5be75011c6ee67c9a6943683a1acb4b1626bac36", "status": "ACTIVE", "creationDate": 1556810537.617 }, { "certificateArn": "arn:aws:iot:us-west-2:123456789012:cert/262a1ac8a7d8aa72f6e96e365480f7313aa9db74b8339ec65d34dc3074e1c31e", "certificateId": "262a1ac8a7d8aa72f6e96e365480f7313aa9db74b8339ec65d34dc3074e1c31e", "status": "ACTIVE", "creationDate": 1546447050.885 }, { "certificateArn": "arn:aws:iot:us-west-2:123456789012:cert/b193ab7162c0fadca83246d24fa090300a1236fe58137e121b011804d8ac1d6b", "certificateId": "b193ab7162c0fadca83246d24fa090300a1236fe58137e121b011804d8ac1d6b", "status": "ACTIVE", "creationDate": 1546292258.322 }, { "certificateArn": "arn:aws:iot:us-west-2:123456789012:cert/7aebeea3845d14a44ec80b06b8b78a89f3f8a706974b8b34d18f5adf0741db42", "certificateId": "7aebeea3845d14a44ec80b06b8b78a89f3f8a706974b8b34d18f5adf0741db42", "status": "ACTIVE", "creationDate": 1541457693.453 }, { "certificateArn": "arn:aws:iot:us-west-2:123456789012:cert/54458aa39ebb3eb39c91ffbbdcc3a6ca1c7c094d1644b889f735a6fc2cd9a7e3", "certificateId": "54458aa39ebb3eb39c91ffbbdcc3a6ca1c7c094d1644b889f735a6fc2cd9a7e3", "status": "ACTIVE", "creationDate": 1541113568.611 }, { "certificateArn": "arn:aws:iot:us-west-2:123456789012:cert/4f0ba725787aa94d67d2fca420eca022242532e8b3c58e7465c7778b443fd65e", "certificateId": "4f0ba725787aa94d67d2fca420eca022242532e8b3c58e7465c7778b443fd65e", "status": "ACTIVE", "creationDate": 1541022751.983 } ] }`- 
                    For API details, see [ListCertificates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-certificates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-custom-metrics`.

- **AWS CLI**
- 
            
                    **To list your custom metrics**The following `list-custom-metrics`example lists all of your custom metrics.`aws iot list-custom-metrics \ --region``us-east-1`Output: `{ "metricNames": [ "batteryPercentage" ] }`For more information, see [Custom metrics](https://docs.aws.amazon.com/iot/latest/developerguide/dd-detect-custom-metrics.html)in the*AWS IoT Core Developer Guide*.- 
                    For API details, see [ListCustomMetrics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-custom-metrics.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-dimensions`.

- **AWS CLI**
- 
            
                    **To list the dimensions for your AWS account**The following `list-dimensions`example lists all AWS IoT Device Defender dimensions that are defined in your AWS account.`aws iot list-dimensions`Output: `{ "dimensionNames": [ "TopicFilterForAuthMessages", "TopicFilterForActivityMessages" ] }`For more information, see [Detect Commands](https://docs.aws.amazon.com/iot/latest/developerguide/DetectCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [ListDimensions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-dimensions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-domain-configurations`.

- **AWS CLI**
- 
            
                    **To list domain configurations**The following `list-domain-configurations`example lists the domain configurations in your AWS account that have the specified service type.`aws iot list-domain-configurations \ --service-type``"DATA"`Output: `{ "domainConfigurations": [ { "domainConfigurationName": "additionalDataDomain", "domainConfigurationArn": "arn:aws:iot:us-west-2:123456789012:domainconfiguration/additionalDataDomain/dikMh", "serviceType": "DATA" }, { "domainConfigurationName": "iot:Jobs", "domainConfigurationArn": "arn:aws:iot:us-west-2:123456789012:domainconfiguration/iot:Jobs", "serviceType": "JOBS" }, { "domainConfigurationName": "iot:Data-ATS", "domainConfigurationArn": "arn:aws:iot:us-west-2:123456789012:domainconfiguration/iot:Data-ATS", "serviceType": "DATA" }, { "domainConfigurationName": "iot:CredentialProvider", "domainConfigurationArn": "arn:aws:iot:us-west-2:123456789012:domainconfiguration/iot:CredentialProvider", "serviceType": "CREDENTIAL_PROVIDER" } ] }`For more information, see [Configurable Endpoints](https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-configurable-aws.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [ListDomainConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-domain-configurations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-indices`.

- **AWS CLI**
- 
            
                    **To list the configured search indices**The following `list-indices`example lists all configured search indices in your AWS account. If you have not enabled thing indexing, you might not have any indices.`aws iot list-indices`Output: `{ "indexNames": [ "AWS_Things" ] }`For more information, see [Managing Thing Indexing](https://docs.aws.amazon.com/iot/latest/developerguide/managing-index.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [ListIndices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-indices.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-job-executions-for-job`.

- **AWS CLI**
- 
            
                    **To list the jobs in your AWS account**The following `list-job-executions-for-job`example lists all job executions for a job in your AWS account, specified by the jobId.`aws iot list-job-executions-for-job \ --job-id``my-ota-job`Output: `{ "executionSummaries": [ { "thingArn": "arn:aws:iot:us-east-1:123456789012:thing/my_thing", "jobExecutionSummary": { "status": "QUEUED", "queuedAt": "2022-03-07T15:58:42.195000-08:00", "lastUpdatedAt": "2022-03-07T15:58:42.195000-08:00", "executionNumber": 1, "retryAttempt": 0 } } ] }`For more information, see [Creating and Managing Jobs (CLI)](https://docs.aws.amazon.com/iot/latest/developerguide/manage-job-cli.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [ListJobExecutionsForJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-job-executions-for-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-job-executions-for-thing`.

- **AWS CLI**
- 
            
                    **To list the jobs that were executed for a thing**The following `list-job-executions-for-thing`example lists all jobs that were executed for the thing named`MyRaspberryPi`.`aws iot list-job-executions-for-thing \ --thing-name``"MyRaspberryPi"`Output: `{ "executionSummaries": [ { "jobId": "example-job-01", "jobExecutionSummary": { "status": "QUEUED", "queuedAt": 1560787023.636, "lastUpdatedAt": 1560787023.636, "executionNumber": 1 } } ] }`For more information, see [Creating and Managing Jobs (CLI)](https://docs.aws.amazon.com/iot/latest/developerguide/manage-job-cli.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [ListJobExecutionsForThing](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-job-executions-for-thing.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-jobs`.

- **AWS CLI**
- 
            
                    **To list the jobs in your AWS account**The following `list-jobs`example lists all jobs in your AWS account, sorted by the job status.`aws iot list-jobs`Output: `{ "jobs": [ { "jobArn": "arn:aws:iot:us-west-2:123456789012:job/example-job-01", "jobId": "example-job-01", "targetSelection": "SNAPSHOT", "status": "IN_PROGRESS", "createdAt": 1560787022.733, "lastUpdatedAt": 1560787026.294 } ] }`For more information, see [Creating and Managing Jobs (CLI)](https://docs.aws.amazon.com/iot/latest/developerguide/manage-job-cli.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [ListJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-mitigation-actions`.

- **AWS CLI**
- 
            
                    **To list all defined mitigation actions**The following `list-mitigation-actions`example lists all defined mitigation actions for your AWS account and Region. For each action, the name, ARN, and creation date are listed.`aws iot list-mitigation-actions`Output: `{ "actionIdentifiers": [ { "actionName": "DeactivateCACertAction", "actionArn": "arn:aws:iot:us-west-2:123456789012:mitigationaction/DeactivateCACertAction", "creationDate": "2019-12-10T11:12:47.574000-08:00" }, { "actionName": "ResetPolicyVersionAction", "actionArn": "arn:aws:iot:us-west-2:123456789012:mitigationaction/ResetPolicyVersionAction", "creationDate": "2019-12-10T11:11:48.920000-08:00" }, { "actionName": "PublishFindingToSNSAction", "actionArn": "arn:aws:iot:us-west-2:123456789012:mitigationaction/PublishFindingToSNSAction", "creationDate": "2019-12-10T11:10:49.546000-08:00" }, { "actionName": "AddThingsToQuarantineGroupAction", "actionArn": "arn:aws:iot:us-west-2:123456789012:mitigationaction/AddThingsToQuarantineGroupAction", "creationDate": "2019-12-10T11:09:35.999000-08:00" }, { "actionName": "UpdateDeviceCertAction", "actionArn": "arn:aws:iot:us-west-2:123456789012:mitigationaction/UpdateDeviceCertAction", "creationDate": "2019-12-10T11:08:44.263000-08:00" }, { "actionName": "SampleMitigationAction", "actionArn": "arn:aws:iot:us-west-2:123456789012:mitigationaction/SampleMitigationAction", "creationDate": "2019-12-10T11:03:41.840000-08:00" } ] }`For more information, see [ListMitigationActions (Mitigation Action Commands)](https://docs.aws.amazon.com/iot/latest/developerguide/mitigation-action-commands.html#dd-api-iot-ListMitigationActions)in the*AWS IoT Developer Guide*.- 
                    For API details, see [ListMitigationActions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-mitigation-actions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-mitigations-actions`.

- **AWS CLI**
- 
            
                    **To list all defined mitigation actions**The following `list-mitigations-actions`example lists all defined mitigation actions for your AWS account and Region. For each action, the name, ARN, and creation date are listed.`aws iot list-mitigation-actions`Output: `{ "actionIdentifiers": [ { "actionName": "DeactivateCACertAction", "actionArn": "arn:aws:iot:us-west-2:123456789012:mitigationaction/DeactivateCACertAction", "creationDate": "2019-12-10T11:12:47.574000-08:00" }, { "actionName": "ResetPolicyVersionAction", "actionArn": "arn:aws:iot:us-west-2:123456789012:mitigationaction/ResetPolicyVersionAction", "creationDate": "2019-12-10T11:11:48.920000-08:00" }, { "actionName": "PublishFindingToSNSAction", "actionArn": "arn:aws:iot:us-west-2:123456789012:mitigationaction/PublishFindingToSNSAction", "creationDate": "2019-12-10T11:10:49.546000-08:00" }, { "actionName": "AddThingsToQuarantineGroupAction", "actionArn": "arn:aws:iot:us-west-2:123456789012:mitigationaction/AddThingsToQuarantineGroupAction", "creationDate": "2019-12-10T11:09:35.999000-08:00" }, { "actionName": "UpdateDeviceCertAction", "actionArn": "arn:aws:iot:us-west-2:123456789012:mitigationaction/UpdateDeviceCertAction", "creationDate": "2019-12-10T11:08:44.263000-08:00" }, { "actionName": "SampleMitigationAction", "actionArn": "arn:aws:iot:us-west-2:123456789012:mitigationaction/SampleMitigationAction", "creationDate": "2019-12-10T11:03:41.840000-08:00" } ] }`For more information, see [ListMitigationActions (Mitigation Action Commands)](https://docs.aws.amazon.com/iot/latest/developerguide/mitigation-action-commands.html#dd-api-iot-ListMitigationActions)in the*AWS IoT Developer Guide*.- 
                    For API details, see [ListMitigationsActions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-mitigations-actions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-ota-updates`.

- **AWS CLI**
- 
            
                    **To list OTA Updates for the account**The following `list-ota-updates`example lists the available OTA updates.`aws iot list-ota-updates`Output: `{ "otaUpdates": [ { "otaUpdateId": "itsaupdate", "otaUpdateArn": "arn:aws:iot:us-west-2:123456789012:otaupdate/itsaupdate", "creationDate": 1557863215.995 } ] }`For more information, see [ListOTAUpdates](https://docs.aws.amazon.com/iot/latest/apireference/API_ListOTAUpdates.html)in the*AWS IoT API Reference*.- 
                    For API details, see [ListOtaUpdates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-ota-updates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-outgoing-certificates`.

- **AWS CLI**
- 
            
                    **To list certificates being transferred to a different AWS account**The following `list-outgoing-certificates`example lists all device certificates that are in the process of being transferred to a different AWS account using the`transfer-certificate`command.`aws iot list-outgoing-certificates`Output: `{ "outgoingCertificates": [ { "certificateArn": "arn:aws:iot:us-west-2:030714055129:cert/488b6a7f2acdeb00a77384e63c4e40b18b1b3caaae57b7272ba44c45e3448142", "certificateId": "488b6a7f2acdeb00a77384e63c4e40b18b1b3caaae57b7272ba44c45e3448142", "transferredTo": "030714055129", "transferDate": 1569427780.441, "creationDate": 1569363250.557 } ] }`For more information, see [ListOutgoingCertificates](https://docs.aws.amazon.com/iot/latest/apireference/API_ListOutgoingCertificates.html)in the*AWS IoT API Reference*.- 
                    For API details, see [ListOutgoingCertificates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-outgoing-certificates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-policies`.

- **AWS CLI**
- 
            
                    **To list the policies defined in your AWS account**The following `list-policies`example lists all policies defined in your AWS account.`aws iot list-policies`Output: `{ "policies": [ { "policyName": "UpdateDeviceCertPolicy", "policyArn": "arn:aws:iot:us-west-2:123456789012:policy/UpdateDeviceCertPolicy" }, { "policyName": "PlantIoTPolicy", "policyArn": "arn:aws:iot:us-west-2:123456789012:policy/PlantIoTPolicy" }, { "policyName": "MyPiGroup_Core-policy", "policyArn": "arn:aws:iot:us-west-2:123456789012:policy/MyPiGroup_Core-policy" } ] }`For more information, see [AWS IoT Policies](https://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [ListPolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-policies.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-policy-versions`.

- **AWS CLI**
- 
            
                    **Example 1: To see all versions of a policy**The following `list-policy-versions`example lists all versions of the specified policy and their creation dates.`aws iot list-policy-versions \ --policy-name``LightBulbPolicy`Output: `{ "policyVersions": [ { "versionId": "2", "isDefaultVersion": true, "createDate": 1559925941.924 }, { "versionId": "1", "isDefaultVersion": false, "createDate": 1559925941.924 } ] }`For more information, see [AWS IoT Policies](https://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [ListPolicyVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-policy-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-principal-things`.

- **AWS CLI**
- 
            
                    **To list the things attached with a principal**The following `list-principal-things`example lists the things attached to the principal specified by an ARN.`aws iot list-principal-things \ --principal``arn:aws:iot:us-west-2:123456789012:cert/2e1eb273792174ec2b9bf4e9b37e6c6c692345499506002a35159767055278e8`Output: `{ "things": [ "DeskLamp", "TableLamp" ] }`For more information, see [ListPrincipalThings](https://docs.aws.amazon.com/iot/latest/apireference/API_ListPrincipleThings.html)in the*AWS IoT API Reference*.- 
                    For API details, see [ListPrincipalThings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-principal-things.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-provisioning-template-versions`.

- **AWS CLI**
- 
            
                    **To list provisioning template versions**The following `list-provisioning-template-versions`example lists the available versions of the specified provisioning template.`aws iot list-provisioning-template-versions \ --template-name``"widget-template"`Output: `{ "versions": [ { "versionId": 1, "creationDate": 1574800471.339, "isDefaultVersion": true }, { "versionId": 2, "creationDate": 1574801192.317, "isDefaultVersion": false } ] }`For more information, see [AWS IoT Secure Tunneling](https://docs.aws.amazon.com/iot/latest/developerguide/secure-tunneling.html)in the*AWS IoT Core Developer Guide*.- 
                    For API details, see [ListProvisioningTemplateVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-provisioning-template-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-provisioning-templates`.

- **AWS CLI**
- 
            
                    **To list provisioning templates**The following `list-provisioning-templates`example lists all of the provisioning templates in your AWS account.`aws iot list-provisioning-templates`Output: `{ "templates": [ { "templateArn": "arn:aws:iot:us-east-1:123456789012:provisioningtemplate/widget-template", "templateName": "widget-template", "description": "A provisioning template for widgets", "creationDate": 1574800471.367, "lastModifiedDate": 1574801192.324, "enabled": false } ] }`For more information, see [AWS IoT Secure Tunneling](https://docs.aws.amazon.com/iot/latest/developerguide/secure-tunneling.html)in the*AWS IoT Core Developer Guide*.- 
                    For API details, see [ListProvisioningTemplates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-provisioning-templates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-role-aliases`.

- **AWS CLI**
- 
            
                    **To list the AWS IoT role aliases in your AWS account**The following `list-role-aliases`example lists the AWS IoT role aliases in your AWS account.`aws iot list-role-aliases`Output: `{ "roleAliases": [ "ResidentAlias", "ElectricianAlias" ] }`For more information, see [ListRoleAliases](https://docs.aws.amazon.com/iot/latest/apireference/API_ListRoleAliases.html)in the*AWS IoT API Reference*.- 
                    For API details, see [ListRoleAliases](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-role-aliases.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-scheduled-audits`.

- **AWS CLI**
- 
            
                    **To list the scheduled audits for your AWS account**The following `list-scheduled-audits`example lists any audits scheduled for your AWS account.`aws iot list-scheduled-audits`Output: `{ "scheduledAudits": [ { "scheduledAuditName": "AWSIoTDeviceDefenderDailyAudit", "scheduledAuditArn": "arn:aws:iot:us-west-2:123456789012:scheduledaudit/AWSIoTDeviceDefenderDailyAudit", "frequency": "DAILY" }, { "scheduledAuditName": "AWSDeviceDefenderWeeklyAudit", "scheduledAuditArn": "arn:aws:iot:us-west-2:123456789012:scheduledaudit/AWSDeviceDefenderWeeklyAudit", "frequency": "WEEKLY", "dayOfWeek": "SUN" } ] }`For more information, see [Audit Commands](https://docs.aws.amazon.com/iot/latest/developerguide/AuditCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [ListScheduledAudits](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-scheduled-audits.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-security-profiles-for-target`.

- **AWS CLI**
- 
            
                    **To list the security profiles attached to a target**The following `list-security-profiles-for-target`example lists the AWS IoT Device Defender security profiles that are attached to unregistered devices.`aws iot list-security-profiles-for-target \ --security-profile-target-arn``"arn:aws:iot:us-west-2:123456789012:all/unregistered-things"`Output: `{ "securityProfileTargetMappings": [ { "securityProfileIdentifier": { "name": "Testprofile", "arn": "arn:aws:iot:us-west-2:123456789012:securityprofile/Testprofile" }, "target": { "arn": "arn:aws:iot:us-west-2:123456789012:all/unregistered-things" } } ] }`For more information, see [Detect Commands](https://docs.aws.amazon.com/iot/latest/developerguide/DetectCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [ListSecurityProfilesForTarget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-security-profiles-for-target.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-security-profiles`.

- **AWS CLI**
- 
            
                    **To list the security profiles for your AWS account**The following `list-security-profiles`example lists all AWS IoT Device Defender security profiles that are defined in your AWS account.`aws iot list-security-profiles`Output: `{ "securityProfileIdentifiers": [ { "name": "Testprofile", "arn": "arn:aws:iot:us-west-2:123456789012:securityprofile/Testprofile" } ] }`For more information, see [Detect Commands](https://docs.aws.amazon.com/iot/latest/developerguide/DetectCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [ListSecurityProfiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-security-profiles.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-streams`.

- **AWS CLI**
- 
            
                    **To list the streams in the account**The following `list-streams`example lists all of the streams in your AWS account.`aws iot list-streams`Output: `{ "streams": [ { "streamId": "stream12345", "streamArn": "arn:aws:iot:us-west-2:123456789012:stream/stream12345", "streamVersion": 1, "description": "This stream is used for Amazon FreeRTOS OTA Update 12345." }, { "streamId": "stream54321", "streamArn": "arn:aws:iot:us-west-2:123456789012:stream/stream54321", "streamVersion": 1, "description": "This stream is used for Amazon FreeRTOS OTA Update 54321." } ] }`For more information, see [ListStreams](https://docs.aws.amazon.com/iot/latest/apireference/API_ListStreams.html)in the*AWS IoT API Reference*.- 
                    For API details, see [ListStreams](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-streams.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To display the tags and their values associated with a resource**The following `list-tags-for-resource`example displays the tags and values associated with the thing group`LightBulbs`.`aws iot list-tags-for-resource \ --resource-arn``"arn:aws:iot:us-west-2:094249569039:thinggroup/LightBulbs"`Output: `{ "tags": [ { "Key": "Assembly", "Value": "Fact1NW" }, { "Key": "MyTag", "Value": "777" } ] }`For more information, see [Tagging Your AWS IoT Resources](https://docs.aws.amazon.com/iot/latest/developerguide/tagging-iot.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-targets-for-policy`.

- **AWS CLI**
- 
            
                    **To list the principals associated with an AWS IoT policy**The following `list-targets-for-policy`example lists the device certificates to which the specified policy is attached.`aws iot list-targets-for-policy \ --policy-name``UpdateDeviceCertPolicy`Output: `{ "targets": [ "arn:aws:iot:us-west-2:123456789012:cert/488b6a7f2acdeb00a77384e63c4e40b18b1b3caaae57b7272ba44c45e3448142", "arn:aws:iot:us-west-2:123456789012:cert/d1eb269fb55a628552143c8f96eb3c258fcd5331ea113e766ba0c82bf225f0be" ] }`For more information, see [Thing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/thing-groups.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [ListTargetsForPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-targets-for-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-targets-for-security-profile`.

- **AWS CLI**
- 
            
                    **To list the targets to which a security profile is applied**The following `list-targets-for-security-profile`example lists the targets to which the AWS IoT Device Defender security profile named`PossibleIssue`is applied.`aws iot list-targets-for-security-profile \ --security-profile-name``Testprofile`Output: `{ "securityProfileTargets": [ { "arn": "arn:aws:iot:us-west-2:123456789012:all/unregistered-things" }, { "arn": "arn:aws:iot:us-west-2:123456789012:all/registered-things" } ] }`For more information, see [Detect Commands](https://docs.aws.amazon.com/iot/latest/developerguide/DetectCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [ListTargetsForSecurityProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-targets-for-security-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-thing-groups-for-thing`.

- **AWS CLI**
- 
            
                    **To list the groups that a thing belongs to**The following `list-thing-groups-for-thing`example lists the groups to which the specified thing belongs.`aws iot list-thing-groups-for-thing \ --thing-name``MyLightBulb`Output: `{ "thingGroups": [ { "groupName": "DeadBulbs", "groupArn": "arn:aws:iot:us-west-2:123456789012:thinggroup/DeadBulbs" }, { "groupName": "LightBulbs", "groupArn": "arn:aws:iot:us-west-2:123456789012:thinggroup/LightBulbs" } ] }`For more information, see [Thing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/thing-groups.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [ListThingGroupsForThing](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-thing-groups-for-thing.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-thing-groups`.

- **AWS CLI**
- 
            
                    **To list the thing groups defined in your AWS account**The following `describe-thing-group`example lists all thing groups defined in your AWS account.`aws iot list-thing-groups`Output: `{ "thingGroups": [ { "groupName": "HalogenBulbs", "groupArn": "arn:aws:iot:us-west-2:123456789012:thinggroup/HalogenBulbs" }, { "groupName": "LightBulbs", "groupArn": "arn:aws:iot:us-west-2:123456789012:thinggroup/LightBulbs" } ] }`For more information, see [Thing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/thing-groups.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [ListThingGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-thing-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-thing-principals`.

- **AWS CLI**
- 
            
                    **To list the principals associated with a thing**The following `list-thing-principals`example lists the principals (X.509 certificates, IAM users, groups, roles, Amazon Cognito identities, or federated identities) associated with the specified thing.`aws iot list-thing-principals \ --thing-name``MyRaspberryPi`Output: `{ "principals": [ "arn:aws:iot:us-west-2:123456789012:cert/33475ac865079a5ffd5ecd44240640349293facc760642d7d8d5dbb6b4c86893" ] }`For more information, see [ListThingPrincipals](https://docs.aws.amazon.com/iot/latest/apireference/API_ListThingPrincipals.html)in the*AWS IoT API Reference*.- 
                    For API details, see [ListThingPrincipals](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-thing-principals.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-thing-types`.

- **AWS CLI**
- 
            
                    **To list the defined thing types**The following `list-thing-types`example displays a list of thing types defined in your AWS account.`aws iot list-thing-types`Output: `{ "thingTypes": [ { "thingTypeName": "LightBulb", "thingTypeArn": "arn:aws:iot:us-west-2:123456789012:thingtype/LightBulb", "thingTypeProperties": { "thingTypeDescription": "light bulb type", "searchableAttributes": [ "model", "wattage" ] }, "thingTypeMetadata": { "deprecated": false, "creationDate": 1559772562.498 } } ] }`For more information, see [Thing Types](https://docs.aws.amazon.com/iot/latest/developerguide/thing-types.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [ListThingTypes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-thing-types.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-things-in-billing-group`.

- **AWS CLI**
- 
            
                    **To list the things in a billing group**The following `list-things-in-billing-group`example lists the things that are in the specified billing group.`aws iot list-things-in-billing-group \ --billing-group-name``GroupOne`Output: `{ "things": [ "MyOtherLightBulb", "MyLightBulb" ] }`For more information, see [Billing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/tagging-iot-billing-groups.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [ListThingsInBillingGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-things-in-billing-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-things-in-thing-group`.

- **AWS CLI**
- 
            
                    **To list the things that belong to a group**The following `list-things-in-thing-group`example lists the things that belong to the specified thing group.`aws iot list-things-in-thing-group \ --thing-group-name``LightBulbs`Output: `{ "things": [ "MyLightBulb" ] }`For more information, see [Thing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/thing-groups.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [ListThingsInThingGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-things-in-thing-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-things`.

- **AWS CLI**
- 
            
                    **Example 1: To list all things in the registry**The following `list-things`example lists the things (devices) that are defined in the AWS IoT registry for your AWS account.`aws iot list-things`Output: `{ "things": [ { "thingName": "ThirdBulb", "thingTypeName": "LightBulb", "thingArn": "arn:aws:iot:us-west-2:123456789012:thing/ThirdBulb", "attributes": { "model": "123", "wattage": "75" }, "version": 2 }, { "thingName": "MyOtherLightBulb", "thingTypeName": "LightBulb", "thingArn": "arn:aws:iot:us-west-2:123456789012:thing/MyOtherLightBulb", "attributes": { "model": "123", "wattage": "75" }, "version": 3 }, { "thingName": "MyLightBulb", "thingTypeName": "LightBulb", "thingArn": "arn:aws:iot:us-west-2:123456789012:thing/MyLightBulb", "attributes": { "model": "123", "wattage": "75" }, "version": 1 }, { "thingName": "SampleIoTThing", "thingArn": "arn:aws:iot:us-west-2:123456789012:thing/SampleIoTThing", "attributes": {}, "version": 1 } ] }`**Example 2: To list the defined things that have a specific attribute**The following `list-things`example displays a list of things that have an attribute named`wattage`.`aws iot list-things \ --attribute-name``wattage`Output: `{ "things": [ { "thingName": "MyLightBulb", "thingTypeName": "LightBulb", "thingArn": "arn:aws:iot:us-west-2:123456789012:thing/MyLightBulb", "attributes": { "model": "123", "wattage": "75" }, "version": 1 }, { "thingName": "MyOtherLightBulb", "thingTypeName": "LightBulb", "thingArn": "arn:aws:iot:us-west-2:123456789012:thing/MyOtherLightBulb", "attributes": { "model": "123", "wattage": "75" }, "version": 3 } ] }`For more information, see [How to Manage Things with the Registry](https://docs.aws.amazon.com/iot/latest/developerguide/thing-registry.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [ListThings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-things.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-topic-rule-destinations`.

- **AWS CLI**
- 
            
                    **To list your topic rule destinations**The following `list-topic-rule-destinations`example lists all topic rule destinations that you have defined in the current AWS Region.`aws iot list-topic-rule-destinations`Output: `{ "destinationSummaries": [ { "arn": "arn:aws:iot:us-west-2:123456789012:ruledestination/http/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "status": "ENABLED", "httpUrlSummary": { "confirmationUrl": "https://example.com" } } ] }`For more information, see [Working with topic rule destinations](https://docs.aws.amazon.com/iot/latest/developerguide/rule-destination.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [ListTopicRuleDestinations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-topic-rule-destinations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-topic-rules`.

- **AWS CLI**
- 
            
                    **To list your rules**The following `list-topic-rules`example lists all rules that you have defined.`aws iot list-topic-rules`Output: `{ "rules": [ { "ruleArn": "arn:aws:iot:us-west-2:123456789012:rule/MyRPiLowMoistureAlertRule", "ruleName": "MyRPiLowMoistureAlertRule", "topicPattern": "$aws/things/MyRPi/shadow/update/accepted", "createdAt": 1558624363.0, "ruleDisabled": false }, { "ruleArn": "arn:aws:iot:us-west-2:123456789012:rule/MyPlantPiMoistureAlertRule", "ruleName": "MyPlantPiMoistureAlertRule", "topicPattern": "$aws/things/MyPlantPi/shadow/update/accepted", "createdAt": 1541458459.0, "ruleDisabled": false } ] }`For more information, see [Viewing Your Rules](https://docs.aws.amazon.com/iot/latest/developerguide/iot-managae-rule.html#iot-view-rules)in the*AWS IoT Developers Guide*.- 
                    For API details, see [ListTopicRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-topic-rules.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-v2-logging-levels`.

- **AWS CLI**
- 
            
                    **To list logging levels**The following `list-v2-logging-levels`example lists the configured logging levels. If logging levels were not set, a`NotConfiguredException`occurs when you run this command.`aws iot list-v2-logging-levels`Output: `{ "logTargetConfigurations": [ { "logTarget": { "targetType": "DEFAULT" }, "logLevel": "ERROR" } ] }`- 
                    For API details, see [ListV2LoggingLevels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-v2-logging-levels.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-violation-events`.

- **AWS CLI**
- 
            
                    **To list the security profile violations during a time period**The following `list-violation-events`example lists violations that occurred between June 5, 2019 and June 12, 2019 for all AWS IoT Device Defender security profiles for the current AWS account and AWS Region.`aws iot list-violation-events \ --start-time``1559747125`\ --end-time`1560351925`Output: `{ "violationEvents": [ { "violationId": "174db59167fa474c80a652ad1583fd44", "thingName": "iotconsole-1560269126751-1", "securityProfileName": "Testprofile", "behavior": { "name": "Authorization", "metric": "aws:num-authorization-failures", "criteria": { "comparisonOperator": "greater-than", "value": { "count": 10 }, "durationSeconds": 300, "consecutiveDatapointsToAlarm": 1, "consecutiveDatapointsToClear": 1 } }, "metricValue": { "count": 0 }, "violationEventType": "in-alarm", "violationEventTime": 1560279000.0 }, { "violationId": "c8a9466a093d3b7b35cd44ca58bdbeab", "thingName": "TvnQoEoU", "securityProfileName": "Testprofile", "behavior": { "name": "CellularBandwidth", "metric": "aws:message-byte-size", "criteria": { "comparisonOperator": "greater-than", "value": { "count": 128 }, "consecutiveDatapointsToAlarm": 1, "consecutiveDatapointsToClear": 1 } }, "metricValue": { "count": 110 }, "violationEventType": "in-alarm", "violationEventTime": 1560276600.0 }, { "violationId": "74aa393adea02e6648f3ac362beed55e", "thingName": "iotconsole-1560269232412-2", "securityProfileName": "Testprofile", "behavior": { "name": "Authorization", "metric": "aws:num-authorization-failures", "criteria": { "comparisonOperator": "greater-than", "value": { "count": 10 }, "durationSeconds": 300, "consecutiveDatapointsToAlarm": 1, "consecutiveDatapointsToClear": 1 } }, "metricValue": { "count": 0 }, "violationEventType": "in-alarm", "violationEventTime": 1560276600.0 }, { "violationId": "1e6ab5f7cf39a1466fcd154e1377e406", "thingName": "TvnQoEoU", "securityProfileName": "Testprofile", "behavior": { "name": "Authorization", "metric": "aws:num-authorization-failures", "criteria": { "comparisonOperator": "greater-than", "value": { "count": 10 }, "durationSeconds": 300, "consecutiveDatapointsToAlarm": 1, "consecutiveDatapointsToClear": 1 } }, "metricValue": { "count": 0 }, "violationEventType": "in-alarm", "violationEventTime": 1560276600.0 } ] }`For more information, see [Detect Commands](https://docs.aws.amazon.com/iot/latest/developerguide/DetectCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [ListViolationEvents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-violation-events.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-ca-certificate`.

- **AWS CLI**
- 
            
                    **To register a certificate authority (CA) certificate**The following `register-ca-certificate`example registers a CA certificate. The command supplies the CA certificate and a key verification certificate that proves you own the private key associated with the CA certificate.`aws iot register-ca-certificate \ --ca-certificate``file://rootCA.pem`\ --verification-cert`file://verificationCert.pem`Output: `{ "certificateArn": "arn:aws:iot:us-west-2:123456789012:cacert/f4efed62c0142f16af278166f61962501165c4f0536295207426460058cd1467", "certificateId": "f4efed62c0142f16af278166f61962501165c4f0536295207426460058cd1467" }`For more information, see [RegisterCACertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_RegisterCACertificate.html)in the*AWS IoT API Reference*.- 
                    For API details, see [RegisterCaCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/register-ca-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-certificate`.

- **AWS CLI**
- 
            
                    **To register a self signed device certificate**The following `register-certificate`example registers the`deviceCert.pem`device certificate signed by the`rootCA.pem`CA certificate. The CA certificate must be registered before you use it to register a self-signed device certificate. The self-signed certificate must be signed by the same CA certificate you pass to this command.`aws iot register-certificate \ --certificate-pem``file://deviceCert.pem`\ --ca-certificate-pem`file://rootCA.pem`Output: `{ "certificateArn": "arn:aws:iot:us-west-2:123456789012:cert/488b6a7f2acdeb00a77384e63c4e40b18b1b3caaae57b7272ba44c45e3448142", "certificateId": "488b6a7f2acdeb00a77384e63c4e40b18b1b3caaae57b7272ba44c45e3448142" }`For more information, see [RegisterCertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_RegisterCertificate.html)in the*AWS IoT API Reference*.- 
                    For API details, see [RegisterCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/register-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-thing`.

- **AWS CLI**
- 
            
                    **To register a thing**The following `register-thing`example registers a thing using a provisioning template.`aws iot register-thing \ --template-body '``{"Parameters":{"ThingName":{"Type":"String"},"AWS::IoT::Certificate::Id":{"Type":"String"}},"Resources": {"certificate":{"Properties":{"CertificateId":{"Ref":"AWS::IoT::Certificate::Id"},"Status":"Active"},"Type":"AWS::IoT::Certificate"},"policy":{"Properties":{"PolicyName":"MyIotPolicy"},"Type":"AWS::IoT::Policy"},"thing":{"OverrideSettings":{"AttributePayload":"MERGE","ThingGroups":"DO_NOTHING","ThingTypeName":"REPLACE"},"Properties":{"AttributePayload":{},"ThingGroups":[],"ThingName":{"Ref":"ThingName"},"ThingTypeName":"VirtualThings"},"Type":"AWS::IoT::Thing"}}}`' \ --parameters '`{"ThingName":"Register-thing-trial-1","AWS::IoT::Certificate::Id":"799a9ea048a1e6aea42b55EXAMPLEf8697b4bafcd77a318a3068e30404b9233c"}`'Output: `{ "certificatePem": "-----BEGIN CERTIFICATE-----\nMIIDWTCCAkGgAwIBAgIUYLk81I35cIppobpw HiOJ2jNjboIwDQYJKoZIhvcNAQEL\nBQAwTTFLMEkGA1UECwxCQW1hem9uIFdlYiBTZXJ2aWNlcyBPPUFtYXpvbi 5jb20g\nSW5jLiBMPVNlYXR0bGUgU1Q9V2FzaGluZ3RvbiBDPVVTMB4XDTIwMDcyMzE2NDUw\nOVoXDTQ5MTIzMT IzNTk1OVowHjEcMBoGA1UEAwwTQVdTIElvVCBDZXJ0aWZpY2F0\nZTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCC AQoCggEBAO71uADhdBajqTmgrMV5\nmCFfBZQRMo1MdtVoZr2X+M4MzL+RARrtUzH9a2SMAckeX8KeblIOTKzORI RDXnyE\n6lVOwjgAsd0ku22rFxex4eG2ikha7pYYkvuToqA7L3TxItRvfKrxRI4ZfJoFPip4\nKqiuBJVNOGKTcQ Hd1RNOrddwwu6kFJLeKDmEXAMPLEdUF0N+qfR9yKnZQkm+g6Q2\nGXu7u0W3hn6nlRN8qVoka0uW12p53xM7oHVz Gf+cxKBxlbOhGkp6yCfTSkUBm3Sp\n9zLw35kiHXVm4EVpwgNlnk6XcIGIkw8a/iy4pzmvuGAANY1/uU/zgCjymw ZT5S30\nBV0CAwEAAaNgMF4wHwYDVR0jBBgwFoAUGx0tCcU3q2n1WXAuUCv6hugXjKswHQYD\nVR0OBBYEFOVtvZ 9Aj2RYFnkX7Iu01XTRUdxgMAwGA1UdEwEB/wQCMAAwDgYDVR0P\nAQH/BAQDAgeAMA0GCSqGSIb3DQEBCwUAA4IB AQCXCQcpOtubS5ftOsDMTcpP/jNX\nDHyArxmjpSc2aCdmm7WX59lTKWyAdxGAvqaDVWqTo0oXI7tZ8w7aINlGi5 pXnifx\n3SBebMUoBbTktrC97yUaeL025mCFv8emDnTR/fE7PTsBKjW0g/rrfpwBxZLXDFwN\nnqkQjy3EDfifj2 6j0xYIqqWMPogyn4srOCKynS5wMJuQZlHQOnabVwnwK4Y0Mflp\np9+4susFUR9aT3BT1AcIwqSpzhlKhh4Iz7ND kRn4amsUT210jg/zOO1Ow+BTHcVQ\nJly8XDu0CWSu04q6SnaBzHmlySIajxuRTP/AdfRouP1OXe+qlbPOBcvVvF 8o\n-----END CERTIFICATE-----\n", "resourceArns": { "certificate": "arn:aws:iot:us-west-2:571032923833:cert/799a9ea048a1e6aea42b55EXAMPLEf8697b4bafcd77a318a3068e30404b9233c", "thing": "arn:aws:iot:us-west-2:571032923833:thing/Register-thing-trial-1" } }`For more information, see [Provisioning by trusted user](https://docs.aws.amazon.com/iot/latest/developerguide/provision-wo-cert.html#trusted-user)in the*AWS IoT Core Developers Guide*.- 
                    For API details, see [RegisterThing](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/register-thing.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reject-certificate-transfer`.

- **AWS CLI**
- 
            
                    **To reject a certificate transfer**The following `reject-certificate-transfer`example rejects the transfer of the specified device certificate from another AWS account.`aws iot reject-certificate-transfer \ --certificate-id``f0f33678c7c9a046e5cc87b2b1a58dfa0beec26db78addd5e605d630e05c7fc8`This command produces no output. For more information, see [Transfer a certificate to another account](https://docs.aws.amazon.com/iot/latest/developerguide/transfer-cert.html)in the*AWS IoT Core Developer Guide*.- 
                    For API details, see [RejectCertificateTransfer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/reject-certificate-transfer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-thing-from-billing-group`.

- **AWS CLI**
- 
            
                    **To remove a thing from a billing group**The following `remove-thing-from-billing-group`example removes the specified thing from a billing group.`aws iot remove-thing-from-billing-group \ --billing-group-name``GroupOne`\ --thing-name`MyOtherLightBulb`This command produces no output. For more information, see [Billing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/tagging-iot-billing-groups.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [RemoveThingFromBillingGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/remove-thing-from-billing-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-thing-from-thing-group`.

- **AWS CLI**
- 
            
                    **To remove a thing from a thing group**The following `remove-thing-from-thing-group`example removes the specified thing from a thing group.`aws iot remove-thing-from-thing-group \ --thing-name``bulb7`\ --thing-group-name`DeadBulbs`This command produces no output. For more information, see Thing Groups <https://docs.aws.amazon.com/iot/latest/developerguide/thing-groups.html > in the *AWS IoT Developer Guide*.- 
                    For API details, see [RemoveThingFromThingGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/remove-thing-from-thing-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `replace-topic-rule`.

- **AWS CLI**
- 
            
                    **To update a topic's rule definition**The following `replace-topic-rule`example updates the specified rule to send an SNS alert when soil moisture level readings are too low.`aws iot replace-topic-rule \ --rule-name``MyRPiLowMoistureAlertRule`\ --topic-rule-payload "{\"sql\": \"SELECT * FROM '$aws/things/MyRPi/shadow/update/accepted' WHERE state.reported.moisture = 'low'\", \"description\": \"Sends an alert when soil moisture level readings are too low.\",\"actions\": [{\"sns\":{\"targetArn\":\"arn:aws:sns:us-west-2:123456789012:MyRPiLowMoistureTopic\",\"roleArn\":\"arn:aws:iam::123456789012:role/service-role/MyRPiLowMoistureTopicRole\",\"messageFormat\": \"RAW\"}}],\"ruleDisabled\": false,\"awsIotSqlVersion\":\"2016-03-23\"}"This command produces no output. For more information, see [Creating an AWS IoT Rule](https://docs.aws.amazon.com/iot/latest/developerguide/iot-create-rule.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [ReplaceTopicRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/replace-topic-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `search-index`.

- **AWS CLI**
- 
            
                    **To query the thing index**The following `search-index`example queries the`AWS_Things`index for things that have a type of`LightBulb`.`aws iot search-index \ --index-name``"AWS_Things"`\ --query-string`"thingTypeName:LightBulb"`Output: `{ "things": [ { "thingName": "MyLightBulb", "thingId": "40da2e73-c6af-406e-b415-15acae538797", "thingTypeName": "LightBulb", "thingGroupNames": [ "LightBulbs", "DeadBulbs" ], "attributes": { "model": "123", "wattage": "75" }, "connectivity": { "connected": false } }, { "thingName": "ThirdBulb", "thingId": "615c8455-33d5-40e8-95fd-3ee8b24490af", "thingTypeName": "LightBulb", "attributes": { "model": "123", "wattage": "75" }, "connectivity": { "connected": false } }, { "thingName": "MyOtherLightBulb", "thingId": "6dae0d3f-40c1-476a-80c4-1ed24ba6aa11", "thingTypeName": "LightBulb", "attributes": { "model": "123", "wattage": "75" }, "connectivity": { "connected": false } } ] }`For more information, see [Managing Thing Indexing](https://docs.aws.amazon.com/iot/latest/developerguide/managing-index.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [SearchIndex](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/search-index.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-default-authorizer`.

- **AWS CLI**
- 
            
                    **To set a default authorizer**The following `set-default-authorizer`example sets the custom authorizer named`CustomAuthorizer`as the default authorizer.`aws iot set-default-authorizer \ --authorizer-name``CustomAuthorizer`Output: `{ "authorizerName": "CustomAuthorizer", "authorizerArn": "arn:aws:iot:us-west-2:123456789012:authorizer/CustomAuthorizer" }`For more information, see [CreateDefaultAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateDefaultAuthorizer.html)in the*AWS IoT API Reference*.- 
                    For API details, see [SetDefaultAuthorizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/set-default-authorizer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-default-policy-version`.

- **AWS CLI**
- 
            
                    **To set the default version for a policy**The following `set-default-policy-version`example sets the default version to`2`for the policy named`UpdateDeviceCertPolicy`.`aws iot set-default-policy-version \ --policy-name``UpdateDeviceCertPolicy`\ --policy-version-id`2`This command produces no output. - 
                    For API details, see [SetDefaultPolicyVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/set-default-policy-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-v2-logging-level`.

- **AWS CLI**
- 
            
                    **To set the logging level for a thing group**The following `set-v2-logging-level`example sets the logging level to log warnings for the specified thing group.`aws iot set-v2-logging-level \ --log-target "{\"targetType\":\"THING_GROUP\",\"targetName\":\"LightBulbs\"}" \ --log-level``WARN`This command produces no output. - 
                    For API details, see [SetV2LoggingLevel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/set-v2-logging-level.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-v2-logging-options`.

- **AWS CLI**
- 
            
                    **To set the logging options**The following `set-v2-logging-options`example sets the default logging verbosity level to ERROR and specifies the ARN to use for logging.`aws iot set-v2-logging-options \ --default-log-level``ERROR`\ --role-arn`"arn:aws:iam::094249569039:role/service-role/iotLoggingRole"`This command produces no output. - 
                    For API details, see [SetV2LoggingOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/set-v2-logging-options.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-audit-mitigation-actions-task`.

- **AWS CLI**
- 
            
                    **To apply a mitigation action to the findings from an audit**The following `start-audit-mitigation-actions-task`example applies the`ResetPolicyVersionAction`action (which clears the policy) to the specified single finding.`aws iot start-audit-mitigation-actions-task \ --task-id``"myActionsTaskId"`\ --target "findingIds=[\"0edbaaec-2fe1-4cf5-abc9-d4c3e51f7464\"]" \ --audit-check-to-actions-mapping "IOT_POLICY_OVERLY_PERMISSIVE_CHECK=[\"ResetPolicyVersionAction\"]" \ --client-request-token`"adhadhahda"`Output: `{ "taskId": "myActionsTaskId" }`For more information, see [StartAuditMitigationActionsTask (Mitigation Action Commands)](https://docs.aws.amazon.com/iot/latest/developerguide/mitigation-action-commands.html#dd-api-iot-StartAuditMitigationActionsTask)in the*AWS IoT Developer Guide*.- 
                    For API details, see [StartAuditMitigationActionsTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/start-audit-mitigation-actions-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-on-demand-audit-task`.

- **AWS CLI**
- 
            
                    **To start an audit right away**The following `start-on-demand-audit-task`example starts an AWS IoT Device Defender audit and performs three certificate checks.`aws iot start-on-demand-audit-task \ --target-check-names``CA_CERTIFICATE_EXPIRING_CHECK``DEVICE_CERTIFICATE_EXPIRING_CHECK``REVOKED_CA_CERTIFICATE_STILL_ACTIVE_CHECK`Output: `{ "taskId": "a3aea009955e501a31b764abe1bebd3d" }`For more information, see [Audit Commands](https://docs.aws.amazon.com/iot/latest/developerguide/AuditCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [StartOnDemandAuditTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/start-on-demand-audit-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To specify a tag key and value for a resource**The following `tag-resource`example applies the tag with a key`Assembly`and the value`Fact1NW`to the thing group`LightBulbs`.`aws iot tag-resource \ --tags Key=Assembly,Value="Fact1NW" \ --resource-arn``"arn:aws:iot:us-west-2:094249569039:thinggroup/LightBulbs"`This command produces no output. For more information, see [Tagging Your AWS IoT Resources](https://docs.aws.amazon.com/iot/latest/developerguide/tagging-iot.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `test-authorization`.

- **AWS CLI**
- 
            
                    **To test your AWS IoT policies**The following `test-authorization`example tests the AWS IoT policies associated with the specified principal.`aws iot test-authorization \ --auth-infos``actionType=CONNECT,resources=arn:aws:iot:us-east-1:123456789012:client/client1`\ --principal`arn:aws:iot:us-west-2:123456789012:cert/aab1068f7f43ac3e3cae4b3a8aa3f308d2a750e6350507962e32c1eb465d9775`Output: `{ "authResults": [ { "authInfo": { "actionType": "CONNECT", "resources": [ "arn:aws:iot:us-east-1:123456789012:client/client1" ] }, "allowed": { "policies": [ { "policyName": "TestPolicyAllowed", "policyArn": "arn:aws:iot:us-west-2:123456789012:policy/TestPolicyAllowed" } ] }, "denied": { "implicitDeny": { "policies": [ { "policyName": "TestPolicyDenied", "policyArn": "arn:aws:iot:us-west-2:123456789012:policy/TestPolicyDenied" } ] }, "explicitDeny": { "policies": [ { "policyName": "TestPolicyExplicitDenied", "policyArn": "arn:aws:iot:us-west-2:123456789012:policy/TestPolicyExplicitDenied" } ] } }, "authDecision": "IMPLICIT_DENY", "missingContextValues": [] } ] }`For more information, see [TestAuthorization](https://docs.aws.amazon.com/iot/latest/apireference/API_TestAuthorization.html)in the*AWS IoT API Reference*.- 
                    For API details, see [TestAuthorization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/test-authorization.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `test-invoke-authorizer`.

- **AWS CLI**
- 
            
                    **To test your custom authorizer**The following `test-invoke-authorizer`example testS your custom authorizer.`aws iot test-invoke-authorizer \ --authorizer-name``IoTAuthorizer`\ --token`allow`\ --token-signature`"mE0GvaHqy9nER/FdgtJX5lXYEJ3b3vE7t1gEszc0TKGgLKWXTnPkb2AbKnOAZ8lGyoN5dVtWDWVmr25m7++zjbYIMk2TBvyGXhOmvKFBPkdgyA43KL6SiZy0cTqlPMcQDsP7VX2rXr7CTowCxSNKphGXdQe0/I5dQ+JO6KUaHwCmupt0/MejKtaNwiia064j6wprOAUwG5S1IYFuRd0X+wfo8pb0DubAIX1Ua705kuhRUcTx4SxUShEYKmN4IDEvLB6FsIr0B2wvB7y4iPmcajxzGl02ExvyCUNctCV9dYlRRGJj0nsGzBIXOI4sGytPfqlA7obdgmN22pkDzYvwjQ=="`Output: `{ "isAuthenticated": true, "principalId": "principalId", "policyDocuments": [ "{"Version":"2012-10-17","Statement":[{"Action":"iot:Publish","Effect":"Allow","Resource":"arn:aws:iot:us-west-2:123456789012:topic/customauthtesting"}]}" ], "refreshAfterInSeconds": 600, "disconnectAfterInSeconds": 3600 }`For more information, see [TestInvokeAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_TestInvokeAuthorizers.html)in the*AWS IoT API Reference*.- 
                    For API details, see [TestInvokeAuthorizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/test-invoke-authorizer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `transfer-certificate`.

- **AWS CLI**
- 
            
                    **To transfer a device certificate to a different AWS account**The following `transfer-certificate`example transfers a device certificate to another AWS account. The certificate and AWS account are identified by ID.`aws iot transfer-certificate \ --certificate-id``488b6a7f2acdeb00a77384e63c4e40b18b1b3caaae57b7272ba44c45e3448142`\ --target-aws-account`030714055129`Output: `{ "transferredCertificateArn": "arn:aws:iot:us-west-2:030714055129:cert/488b6a7f2acdeb00a77384e63c4e40b18b1b3caaae57b7272ba44c45e3448142" }`For more information, see [Transfer a certificate to another account](https://docs.aws.amazon.com/iot/latest/developerguide/transfer-cert.html)in the*AWS IoT Core Developer Guide*.- 
                    For API details, see [TransferCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/transfer-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove a tag key from a resource**The following `untag-resource`example removes the tag`MyTag`and its value from the thing group`LightBulbs`.`command`This command produces no output. For more information, see [Tagging Your AWS IoT Resources](https://docs.aws.amazon.com/iot/latest/developerguide/tagging-iot.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-account-audit-configuration`.

- **AWS CLI**
- 
            
                    **Example 1: To enable Amazon SNS notifications for audit notifications**The following `update-account-audit-configuration`example enables Amazon SNS notifications for AWS IoT Device Defender audit notifications, specifying a target and the role used to write to that target.`aws iot update-account-audit-configuration \ --audit-notification-target-configurations "SNS={targetArn=\"arn:aws:sns:us-west-2:123456789012:ddaudits\",roleArn=\"arn:aws:iam::123456789012:role/service-role/AWSIoTDeviceDefenderAudit\",enabled=true}"`This command produces no output. **Example 2: To enable an audit check**The following `update-account-audit-configuration`example enables the AWS IoT Device Defender audit check named`AUTHENTICATED_COGNITO_ROLE_OVERLY_PERMISSIVE_CHECK`. You cannot disable an audit check if it is part of the`targetCheckNames`for one or more scheduled audits for the AWS account.`aws iot update-account-audit-configuration \ --audit-check-configurations "{\"AUTHENTICATED_COGNITO_ROLE_OVERLY_PERMISSIVE_CHECK\":{\"enabled\":true}}"`This command produces no output. For more information, see [Audit Commands](https://docs.aws.amazon.com/iot/latest/developerguide/AuditCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [UpdateAccountAuditConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-account-audit-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-audit-suppression`.

- **AWS CLI**
- 
            
                    **To update an audit finding suppression**The following `update-audit-suppression`example updates an audit finding suppression's expiration date to 2020-09-21.`aws iot update-audit-suppression \ --check-name``DEVICE_CERTIFICATE_EXPIRING_CHECK`\ --resource-identifier`deviceCertificateId=c7691e<shortened>`\ --no-suppress-indefinitely \ --expiration-date`2020-09-21`This command produces no output. For more information, see [Audit finding suppressions](https://docs.aws.amazon.com/iot/latest/developerguide/audit-finding-suppressions.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [UpdateAuditSuppression](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-audit-suppression.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-authorizer`.

- **AWS CLI**
- 
            
                    **To update a custom authorizer**The following `update-authorizer`example he state of`CustomAuthorizer2`to`INACTIVE`.`aws iot update-authorizer \ --authorizer-name``CustomAuthorizer2`\ --status`INACTIVE`Output: `{ "authorizerName": "CustomAuthorizer2", "authorizerArn": "arn:aws:iot:us-west-2:123456789012:authorizer/CustomAuthorizer2" }`For more information, see [UpdateAuthorizer](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateAuthorizer.html)in the*AWS IoT API Reference*.- 
                    For API details, see [UpdateAuthorizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-authorizer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-billing-group`.

- **AWS CLI**
- 
            
                    **To update information about a billing group**The following `update-billing-group`example updates the description for the specified billing group.`aws iot update-billing-group \ --billing-group-name``GroupOne`\ --billing-group-properties "billingGroupDescription=\"Primary bulb billing group\""Output: `{ "version": 2 }`For more information, see [Billing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/tagging-iot-billing-groups.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [UpdateBillingGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-billing-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-ca-certificate`.

- **AWS CLI**
- 
            
                    **To update a certificate authority (CA) certificate**The following `update-ca-certificate`example sets the specified CA certificate to ACTIVE status.`aws iot update-ca-certificate \ --certificate-id``f4efed62c0142f16af278166f61962501165c4f0536295207426460058cd1467`\ --new-status`ACTIVE`This command produces no output. For more information, see [UpdateCACertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateCACertificate.html)in the*AWS IoT API Reference*.- 
                    For API details, see [UpdateCaCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-ca-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-certificate`.

- **AWS CLI**
- 
            
                    **To update a device certificate**The following `update-certificate`example sets the specified device certificate to INACTIVE status.`aws iot update-certificate \ --certificate-id``d1eb269fb55a628552143c8f96eb3c258fcd5331ea113e766ba0c82bf225f0be`\ --new-status`INACTIVE`This command produces no output. For more information, see [UpdateCertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateCertificate.html)in the*AWS IoT API Reference*.- 
                    For API details, see [UpdateCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-custom-metric`.

- **AWS CLI**
- 
            
                    **To update a custom metric**The following `update-custom-metric`example updates a custom metric to have a new`display-name`.`aws iot update-custom-metric \ --metric-name``batteryPercentage`\ --display-name '`remaining battery percentage on device`' \ --region`us-east-1`Output: `{ "metricName": "batteryPercentage", "metricArn": "arn:aws:iot:us-east-1:1234564789012:custommetric/batteryPercentage", "metricType": "number", "displayName": "remaining battery percentage on device", "creationDate": "2020-11-17T23:01:35.110000-08:00", "lastModifiedDate": "2020-11-17T23:02:12.879000-08:00" }`For more information, see [Custom metrics](https://docs.aws.amazon.com/iot/latest/developerguide/dd-detect-custom-metrics.html)in the*AWS IoT Core Developer Guide*.- 
                    For API details, see [UpdateCustomMetric](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-custom-metric.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-dimension`.

- **AWS CLI**
- 
            
                    **To update a dimension**The following `update-dimension`example updates a dimension.`aws iot update-dimension \ --name``TopicFilterForAuthMessages`\ --string-values`device/${iot:ClientId}/auth`Output: `{ "name": "TopicFilterForAuthMessages", "lastModifiedDate": 1585866222.317, "stringValues": [ "device/${iot:ClientId}/auth" ], "creationDate": 1585854500.474, "type": "TOPIC_FILTER", "arn": "arn:aws:iot:us-west-2:1234564789012:dimension/TopicFilterForAuthMessages" }`For more information, see [Scoping metrics in security profiles using dimensions](https://docs.aws.amazon.com/iot/latest/developerguide/scoping-security-behavior.html)in the*AWS IoT Core Developer Guide*.- 
                    For API details, see [UpdateDimension](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-dimension.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-domain-configuration`.

- **AWS CLI**
- 
            
                    **To update a domain configuration**The following `update-domain-configuration`example disables the specified domain configuration.`aws iot update-domain-configuration \ --domain-configuration-name``"additionalDataDomain"`\ --domain-configuration-status`"DISABLED"`Output: `{ "domainConfigurationName": "additionalDataDomain", "domainConfigurationArn": "arn:aws:iot:us-west-2:123456789012:domainconfiguration/additionalDataDomain/dikMh" }`For more information, see [Configurable Endpoints](https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-configurable-aws.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [UpdateDomainConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-domain-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-dynamic-thing-group`.

- **AWS CLI**
- 
            
                    **To update a dynamic thing group**The following `update-dynamic-thing-group`example updates the specified dynamic thing group. It provides a description and updates the query string to change the group membership criteria.`aws iot update-dynamic-thing-group \ --thing-group-name``"RoomTooWarm"`--thing-group-properties "thingGroupDescription=\"This thing group contains rooms warmer than 65F.\"" \ --query-string`"attributes.temperature>65"`Output: `{ "version": 2 }`For more information, see [Dynamic Thing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/dynamic-thing-groups.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [UpdateDynamicThingGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-dynamic-thing-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-event-configurations`.

- **AWS CLI**
- 
            
                    **To show which event types are published**The following `update-event-configurations`example updates the configuration to enable messages when the CA certificate is added, updated, or deleted.`aws iot update-event-configurations \ --event-configurations "{\"CA_CERTIFICATE\":{\"Enabled\":true}}"`This command produces no output. For more information, see [Event Messages](https://docs.aws.amazon.com/iot/latest/developerguide/iot-events.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [UpdateEventConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-event-configurations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-indexing-configuration`.

- **AWS CLI**
- 
            
                    **To enable thing indexing**The following `update-indexing-configuration`example enables thing indexing to support searching registry data, shadow data, and thing connectivity status using the AWS_Things index.`aws iot update-indexing-configuration --thing-indexing-configuration``thingIndexingMode=REGISTRY_AND_SHADOW,thingConnectivityIndexingMode=STATUS`This command produces no output. For more information, see [Managing Thing Indexing](https://docs.aws.amazon.com/iot/latest/developerguide/managing-index.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [UpdateIndexingConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-indexing-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-job`.

- **AWS CLI**
- 
            
                    **To get detailed status for a job**The following `update-job`example gets detailed status for the job whose ID is`example-job-01`.`aws iot describe-job \ --job-id``"example-job-01"`Output: `{ "job": { "jobArn": "arn:aws:iot:us-west-2:123456789012:job/example-job-01", "jobId": "example-job-01", "targetSelection": "SNAPSHOT", "status": "IN_PROGRESS", "targets": [ "arn:aws:iot:us-west-2:123456789012:thing/MyRaspberryPi" ], "description": "example job test", "presignedUrlConfig": {}, "jobExecutionsRolloutConfig": {}, "createdAt": 1560787022.733, "lastUpdatedAt": 1560787026.294, "jobProcessDetails": { "numberOfCanceledThings": 0, "numberOfSucceededThings": 0, "numberOfFailedThings": 0, "numberOfRejectedThings": 0, "numberOfQueuedThings": 1, "numberOfInProgressThings": 0, "numberOfRemovedThings": 0, "numberOfTimedOutThings": 0 }, "timeoutConfig": {} } }`For more information, see [Creating and Managing Jobs (CLI)](https://docs.aws.amazon.com/iot/latest/developerguide/manage-job-cli.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [UpdateJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-mitigation-action`.

- **AWS CLI**
- 
            
                    **To update a mitigation action**The following `update-mitigation-action`example updates the specified mitigation action named`AddThingsToQuarantineGroupAction`, changes the thing group name, and sets`overrideDynamicGroups`to`false`. You can verify your changes by using the`describe-mitigation-action`command.`aws iot update-mitigation-action \ --cli-input-json "{ \"actionName\": \"AddThingsToQuarantineGroupAction\", \"actionParams\": { \"addThingsToThingGroupParams\": {\"thingGroupNames\":[\"QuarantineGroup2\"],\"overrideDynamicGroups\": false}}}"`Output: `{ "actionArn": "arn:aws:iot:us-west-2:123456789012:mitigationaction/AddThingsToQuarantineGroupAction", "actionId": "2fd2726d-98e1-4abf-b10f-09465ccd6bfa" }`For more information, see [UpdateMitigationAction (Mitigation Action Commands)](https://docs.aws.amazon.com/iot/latest/developerguide/mitigation-action-commands.html#dd-api-iot-UpdateMitigationAction)in the*AWS IoT Developer Guide*.- 
                    For API details, see [UpdateMitigationAction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-mitigation-action.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-provisioning-template`.

- **AWS CLI**
- 
            
                    **To update a provisioning template**The following `update-provisioning-template`example modifies the description and role arn for the specified provisioning template and enables the template.`aws iot update-provisioning-template \ --template-name``widget-template`\ --enabled \ --description`"An updated provisioning template for widgets"`\ --provisioning-role-arn`arn:aws:iam::504350838278:role/Provision_role`This command produces no output. For more information, see [AWS IoT Secure Tunneling](https://docs.aws.amazon.com/iot/latest/developerguide/secure-tunneling.html)in the*AWS IoT Core Developer Guide*.- 
                    For API details, see [UpdateProvisioningTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-provisioning-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-role-alias`.

- **AWS CLI**
- 
            
                    **To update a role alias**The following `update-role-alias`example updates the`LightBulbRole`role alias.`aws iot update-role-alias \ --role-alias``LightBulbRole`\ --role-arn`arn:aws:iam::123456789012:role/lightbulbrole-001`Output: `{ "roleAlias": "LightBulbRole", "roleAliasArn": "arn:aws:iot:us-west-2:123456789012:rolealias/LightBulbRole" }`For more information, see [UpdateRoleAlias](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateRoleAlias.html)in the*AWS IoT API Reference*.- 
                    For API details, see [UpdateRoleAlias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-role-alias.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-scheduled-audit`.

- **AWS CLI**
- 
            
                    **To update a scheduled audit definition**The following `update-scheduled-audit`example changes the target check names for an AWS IoT Device Defender scheduled audit.`aws iot update-scheduled-audit \ --scheduled-audit-name``WednesdayCertCheck`\ --target-check-names`CA_CERTIFICATE_EXPIRING_CHECK``DEVICE_CERTIFICATE_EXPIRING_CHECK``REVOKED_CA_CERTIFICATE_STILL_ACTIVE_CHECK`Output: `{ "scheduledAuditArn": "arn:aws:iot:us-west-2:123456789012:scheduledaudit/WednesdayCertCheck" }`For more information, see [Audit Commands](https://docs.aws.amazon.com/iot/latest/developerguide/AuditCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [UpdateScheduledAudit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-scheduled-audit.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-security-profile`.

- **AWS CLI**
- 
            
                    **To change a security profile**The following `update-security-profile`example updates both the description and the behaviors for an AWS IoT Device Defender security profile.`aws iot update-security-profile \ --security-profile-name``PossibleIssue`\ --security-profile-description`"Check to see if authorization fails 12 times in 5 minutes or if cellular bandwidth exceeds 128"`\ --behaviors "[{\"name\":\"CellularBandwidth\",\"metric\":\"aws:message-byte-size\",\"criteria\":{\"comparisonOperator\":\"greater-than\",\"value\":{\"count\":128},\"consecutiveDatapointsToAlarm\":1,\"consecutiveDatapointsToClear\":1}},{\"name\":\"Authorization\",\"metric\":\"aws:num-authorization-failures\",\"criteria\":{\"comparisonOperator\":\"less-than\",\"value\":{\"count\":12},\"durationSeconds\":300,\"consecutiveDatapointsToAlarm\":1,\"consecutiveDatapointsToClear\":1}}]"Output: `{ "securityProfileName": "PossibleIssue", "securityProfileArn": "arn:aws:iot:us-west-2:123456789012:securityprofile/PossibleIssue", "securityProfileDescription": "check to see if authorization fails 12 times in 5 minutes or if cellular bandwidth exceeds 128", "behaviors": [ { "name": "CellularBandwidth", "metric": "aws:message-byte-size", "criteria": { "comparisonOperator": "greater-than", "value": { "count": 128 }, "consecutiveDatapointsToAlarm": 1, "consecutiveDatapointsToClear": 1 } }, { "name": "Authorization", "metric": "aws:num-authorization-failures", "criteria": { "comparisonOperator": "less-than", "value": { "count": 12 }, "durationSeconds": 300, "consecutiveDatapointsToAlarm": 1, "consecutiveDatapointsToClear": 1 } } ], "version": 2, "creationDate": 1560278102.528, "lastModifiedDate": 1560352711.207 }`For more information, see [Detect Commands](https://docs.aws.amazon.com/iot/latest/developerguide/DetectCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [UpdateSecurityProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-security-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-stream`.

- **AWS CLI**
- 
            
                    **To update a stream**The following `update-stream`example updates an existing stream. The stream version is incremented by one.`aws iot update-stream \ --cli-input-json``file://update-stream.json`Contents of `update-stream.json`:`{ "streamId": "stream12345", "description": "This stream is used for Amazon FreeRTOS OTA Update 12345.", "files": [ { "fileId": 123, "s3Location": { "bucket":"codesign-ota-bucket", "key":"48c67f3c-63bb-4f92-a98a-4ee0fbc2bef6" } } ] "roleArn": "arn:aws:iam:us-west-2:123456789012:role/service-role/my_ota_stream_role" }`Output: `{ "streamId": "stream12345", "streamArn": "arn:aws:iot:us-west-2:123456789012:stream/stream12345", "description": "This stream is used for Amazon FreeRTOS OTA Update 12345.", "streamVersion": 2 }`For more information, see [UpdateStream](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateStream.html)in the*AWS IoT API Reference*.- 
                    For API details, see [UpdateStream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-stream.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-thing-group`.

- **AWS CLI**
- 
            
                    **To update the definition for a thing group**The following `update-thing-group`example updates the definition for the specified thing group, changing the description and two attributes.`aws iot update-thing-group \ --thing-group-name``HalogenBulbs`\ --thing-group-properties "thingGroupDescription=\"Halogen bulb group\", attributePayload={attributes={Manufacturer=AnyCompany,wattage=60}}"Output: `{ "version": 2 }`For more information, see [Thing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/thing-groups.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [UpdateThingGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-thing-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-thing-groups-for-thing`.

- **AWS CLI**
- 
            
                    **To change the groups to which a thing belongs**The following `update-thing-groups-for-thing`example removes the thing named`MyLightBulb`from the group named`DeadBulbs`and adds it to the group named`replaceableItems`at the same time.`aws iot update-thing-groups-for-thing \ --thing-name``MyLightBulb`\ --thing-groups-to-add`"replaceableItems"`\ --thing-groups-to-remove`"DeadBulbs"`This command produces no output. For more information, see [Thing Groups](https://docs.aws.amazon.com/iot/latest/developerguide/thing-groups.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [UpdateThingGroupsForThing](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-thing-groups-for-thing.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-thing`.

- **AWS CLI**
- 
            
                    **To associate a thing with a thing type**The following `update-thing`example associates a thing in the AWS IoT registry with a thing type. When you make the association, you provide values for the attributes defined by the thing type.`aws iot update-thing \ --thing-name``"MyOtherLightBulb"`\ --thing-type-name`"LightBulb"`\ --attribute-payload "{"attributes": {"wattage":"75", "model":"123"}}"This command does not produce output. Use the `describe-thing`command to see the result.For more information, see [Thing Types](https://docs.aws.amazon.com/iot/latest/developerguide/thing-types.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [UpdateThing](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-thing.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-topic-rule-destination`.

- **AWS CLI**
- 
            
                    **Example 1: To enable a topic rule destination**The following `update-topic-rule-destination`example enables traffic to a topic rule destination.`aws iot update-topic-rule-destination \ --arn``"arn:aws:iot:us-west-2:123456789012:ruledestination/http/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE"`\ --status`ENABLED`This command produces no output. For more information, see [Enabling a topic rule destination](https://docs.aws.amazon.com/iot/latest/developerguide/rule-destination.html#enable-destination)in the*AWS IoT Developer Guide*.**Example 2: To disable a topic rule destination**The following `update-topic-rule-destination`example disables traffic to a topic rule destination.`aws iot update-topic-rule-destination \ --arn``"arn:aws:iot:us-west-2:123456789012:ruledestination/http/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE"`\ --status`DISABLED`This command produces no output. For more information, see [Disabling a topic rule destination](https://docs.aws.amazon.com/iot/latest/developerguide/rule-destination.html#disable-destination)in the*AWS IoT Developer Guide*.**Example 3: To send a new confirmation message**The following `update-topic-rule-destination`example sends a new confirmation message for a topic rule destination.`aws iot update-topic-rule-destination \ --arn``"arn:aws:iot:us-west-2:123456789012:ruledestination/http/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE"`\ --status`IN_PROGRESS`This command produces no output. For more information, see [Sending a new confirmation message](https://docs.aws.amazon.com/iot/latest/developerguide/rule-destination.html#trigger-confirm)in the*AWS IoT Developer Guide*.- 
                    For API details, see [UpdateTopicRuleDestination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/update-topic-rule-destination.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `validate-security-profile-behaviors`.

- **AWS CLI**
- 
            
                    **Example 1: To validate the behaviors parameters for a security profile**The following `validate-security-profile-behaviors`example validates a well-formed and correct set of behaviors for an AWS IoT Device Defender security profile.`aws iot validate-security-profile-behaviors \ --behaviors "[{\"name\":\"CellularBandwidth\",\"metric\":\"aws:message-byte-size\",\"criteria\":{\"comparisonOperator\":\"greater-than\",\"value\":{\"count\":128},\"consecutiveDatapointsToAlarm\":1,\"consecutiveDatapointsToClear\":1}},{\"name\":\"Authorization\",\"metric\":\"aws:num-authorization-failures\",\"criteria\":{\"comparisonOperator\":\"greater-than\",\"value\":{\"count\":12},\"durationSeconds\":300,\"consecutiveDatapointsToAlarm\":1,\"consecutiveDatapointsToClear\":1}}]"`Output: `{ "valid": true, "validationErrors": [] }`**Example 2: To validate incorrect behaviors parameters for a security profile**The following `validate-security-profile-behaviors`example validates a set of behaviors that contains an error for an AWS IoT Device Defender security profile.`aws iot validate-security-profile-behaviors \ --behaviors "[{\"name\":\"CellularBandwidth\",\"metric\":\"aws:message-byte-size\",\"criteria\":{\"comparisonOperator\":\"greater-than\",\"value\":{\"count\":128},\"consecutiveDatapointsToAlarm\":1,\"consecutiveDatapointsToClear\":1}},{\"name\":\"Authorization\",\"metric\":\"aws:num-authorization-failures\",\"criteria\":{\"comparisonOperator\":\"greater-than\",\"value\":{\"count\":12},\"durationSeconds\":300,\"consecutiveDatapointsToAlarm\":100000,\"consecutiveDatapointsToClear\":1}}]"`Output: `{ "valid": false, "validationErrors": [ { "errorMessage": "Behavior Authorization is malformed. consecutiveDatapointsToAlarm 100000 should be in range[1,10]" } ] }`For more information, see [Detect Commands](https://docs.aws.amazon.com/iot/latest/developerguide/DetectCommands.html)in the*AWS IoT Developer Guide*.- 
                    For API details, see [ValidateSecurityProfileBehaviors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/validate-security-profile-behaviors.html)in*AWS CLI Command Reference*.
 
-