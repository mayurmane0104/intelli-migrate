# AWS Control Tower examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_controltower_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_controltower_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS Control Tower.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-landing-zone`.

- **AWS CLI**
- 
            
                    **To create a Control Tower landing zone**The following `create-landing-zone`example creates AWS Control Tower landing zone.`aws controltower create-landing-zone \ --landing-zone-version``3.3`\ --manifest`"file://LandingZoneManifest.json"`Output: `{ "arn": "arn:aws:controltower:us-east-1:123456789012:landingzone/13CJG46WZKXXX4X5", "operationIdentifier": "55XXXXXX-e2XX-41XX-a7XX-446XXXXXXXXX" }`For more information, see [Getting started with AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [CreateLandingZone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/create-landing-zone.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-landing-zone`.

- **AWS CLI**
- 
            
                    **To decommission a landing zone**The following `delete-landing-zone`example decommissions the AWS Control Tower landing zone.`aws controltower delete-landing-zone \ --landing-zone-identifier``arn:aws:controltower:us-east-1:123456789012:landingzone/13CJG46WZKXXX4X5`Output: `{ "operationIdentifier": "47XXXXXX-a6XX-82XX-c9XX-432XXXXXXXXX" }`For more information, see [Decommission an AWS Control Tower landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/decommission-landing-zone.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [DeleteLandingZone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/delete-landing-zone.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-baseline`.

- **AWS CLI**
- 
            
                    **To disable a Control Tower baseline**The following `disable-baseline`example disables an AWS Control Tower baseline.`aws controltower disable-baseline \ --enabled-baseline-identifier``arn:aws:controltower:us-east-1:123456789012:enabledbaseline/XOM12BEL4YD578CQ2`Output: `{ "operationIdentifier": "b33486d7-5396-4ad0-9eae-3a57969fe8cd" }`For more information, see [Types of baselines](https://docs.aws.amazon.com/controltower/latest/userguide/types-of-baselines.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [DisableBaseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/disable-baseline.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-control`.

- **AWS CLI**
- 
            
                    **To disable a Control Tower control**The following `disable-control`example disables an AWS Control Tower enabled control.`aws controltower disable-control \ --control-identifier``arn:aws:controlcatalog:::control/497wrm2xnk1wxlf4obrxxxxxx`\ --target-identifier`arn:aws:organizations::123456789012:ou/o-s64ryxxxxx/ou-oqxx-i5wnxxxx`Output: `{ "operationIdentifier": "b8f0dxxx-08xx-43xx-a2xx-568e9922xxxx" }`For more information, see [About controls in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [DisableControl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/disable-control.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-baseline`.

- **AWS CLI**
- 
            
                    **Example 1: To enable a Control Tower baseline that is disabled**The following `enable-baseline`example enables an AWS Control Tower baseline if baseline`IdentityCenterBaseline`is disabled.`aws controltower enable-baseline \ --baseline-identifier``arn:aws:controltower:us-east-1::baseline/17BSJV3IGJ2QSGA2`\ --baseline-version`4.0`\ --target-identifier`arn:aws:organizations::123456789012:ou/o-s64ryixxxx/ou-oq9f-i5wnxxxx`Output: `{ "arn": "arn:aws:controltower:us-east-1:123456789012:enabledbaseline/XOM12BEL4YD578CQ2", "operationIdentifier": "51e190ac-8a37-4f6d-b63c-fb5104b5db38" }`For more information, see [Types of baselines](https://docs.aws.amazon.com/controltower/latest/userguide/types-of-baselines.html)in the*AWS Control Tower User Guide*.**Example 2: To enable a Control Tower baseline that is enabled**The following `enable-baseline`example enables an AWS Control Tower baseline if baseline`IdentityCenterBaseline`is enabled.`aws controltower enable-baseline \ --baseline-identifier``arn:aws:controltower:us-east-1::baseline/17BSJV3IGJ2QSGA2`\ --baseline-version`4.0`\ --target-identifier`arn:aws:organizations::123456789012:ou/o-s64ryixxxx/ou-oqxx-i5wnxxxx`\ --parameters '`[{"key":"IdentityCenterEnabledBaselineArn","value":"arn:aws:controltower:us-east-1:123456789012:enabledbaseline/XAJNZNCBC1I386C7B"}]`'Output: `{ "arn": "arn:aws:controltower:us-east-1:123456789012:enabledbaseline/XOM12BEL4YD578CQ2", "operationIdentifier": "51e190ac-8a37-4f6d-b63c-fb5104b5db38" }`For more information, see [Types of baselines](https://docs.aws.amazon.com/controltower/latest/userguide/types-of-baselines.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [EnableBaseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/enable-baseline.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-control`.

- **AWS CLI**
- 
            
                    **To enable a Control Tower control**The following `enable-control`example enables an AWS Control Tower control.`aws controltower enable-control \ --control-identifier``arn:aws:controlcatalog:::control/497wrm2xnk1wxlf4obrxxxxxx`\ --target-identifier`arn:aws:organizations::123456789012:ou/o-s64ryxxxxx/ou-oqxx-i5wnxxxx`Output: `{ "arn": "arn:aws:controltower:us-east-1:123456789012:enabledcontrol/18J5KBJ3W3VTIRLV", "operationIdentifier": "7691fc5a-de87-4540-8c95-b0aabd56382c" }`For more information, see [About controls in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [EnableControl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/enable-control.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-baseline-operation`.

- **AWS CLI**
- 
            
                    **To get a Control Tower baseline operation**The following `get-baseline-operation`example gets details of an AWS Control Tower baseline operation.`aws controltower get-baseline-operation \ --operation-identifier``"51e190ac-8a37-4f6d-b63c-fb5104b5db38"`Output: `{ "baselineOperation": { "endTime": "2025-04-17T23:48:46+00:00", "operationIdentifier": "51e190ac-8a37-4f6d-b63c-fb5104b5db38", "operationType": "ENABLE_BASELINE", "startTime": "2025-04-17T23:46:37+00:00", "status": "SUCCEEDED", "statusMessage": "AWS Control Tower completed the baseline operation successfully." } }`For more information, see [Types of baselines](https://docs.aws.amazon.com/controltower/latest/userguide/types-of-baselines.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [GetBaselineOperation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/get-baseline-operation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-baseline`.

- **AWS CLI**
- 
            
                    **To get a Control Tower baseline**The following `get-baseline`example gets details of an AWS Control Tower baseline.`aws controltower get-baseline \ --baseline-identifier``arn:aws:controltower:us-east-1::baseline/LN25R72TTG6IGPTQ`Output: `{ "arn": "arn:aws:controltower:us-east-1::baseline/LN25R72TTG6IGPTQ", "description": "Sets up shared resources for AWS Identity Center, which prepares the AWSControlTowerBaseline to set up Identity Center access for accounts.", "name": "IdentityCenterBaseline" }`For more information, see [Types of baselines](https://docs.aws.amazon.com/controltower/latest/userguide/types-of-baselines.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [GetBaseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/get-baseline.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-control-operation`.

- **AWS CLI**
- 
            
                    **To get Control Tower control operations**The following `get-control-operation`example gets details of an AWS Control Tower control operation.`aws controltower get-control-operation \ --operation-identifier``"7691fc5a-de87-4540-8c95-b0aabd56382c"`Output: `{ "controlOperation": { "controlIdentifier": "arn:aws:controlcatalog:::control/497wrm2xnk1wxlf4obrdo7mej", "enabledControlIdentifier": "arn:aws:controltower:us-east-1:123456789012:enabledcontrol/18J5KBJ3W3VTIRLV", "endTime": "2025-04-17T03:08:55+00:00", "operationIdentifier": "7691fc5a-de87-4540-8c95-b0aabd56382c", "operationType": "ENABLE_CONTROL", "startTime": "2025-04-17T03:07:52+00:00", "status": "SUCCEEDED", "statusMessage": "Operation was successful.", "targetIdentifier": "arn:aws:organizations::123456789012:ou/o-s64ryixxxx/ou-oqxx-i5wnxxxx" } }`For more information, see [About controls in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [GetControlOperation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/get-control-operation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-enabled-baseline`.

- **AWS CLI**
- 
            
                    **To get a Control Tower enabled baseline**The following `get-enabled-baseline`example gets details of an AWS Control Tower enabled baseline.`aws controltower get-enabled-baseline \ --enabled-baseline-identifier``arn:aws:controltower:us-east-1:123456789012:enabledbaseline/XOM12BEL4YD578CQ2`Output: `{ "enabledBaselineDetails": { "arn": "arn:aws:controltower:us-east-1:123456789012:enabledbaseline/XOM12BEL4YD578CQ2", "baselineIdentifier": "arn:aws:controltower:us-east-1::baseline/17BSJV3IGJ2QSGA2", "baselineVersion": "4.0", "parameters": [ { "key": "IdentityCenterEnabledBaselineArn", "value": "arn:aws:controltower:us-east-1:123456789012:enabledbaseline/XAJNZNCBC1I386C7B" } ], "statusSummary": { "lastOperationIdentifier": "51e190ac-8a37-4f6d-b63c-fb5104b5db38", "status": "SUCCEEDED" }, "targetIdentifier": "arn:aws:organizations::123456789012:ou/o-3onqfufxxx/ou-g8xx-5kluxxxx" } }`For more information, see [Types of baselines](https://docs.aws.amazon.com/controltower/latest/userguide/types-of-baselines.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [GetEnabledBaseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/get-enabled-baseline.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-enabled-control`.

- **AWS CLI**
- 
            
                    **To get a Control Tower enabled control**The following `get-enabled-control`example gets details of an AWS Control Tower enabled control.`aws controltower get-enabled-control \ --enabled-control-identifier``arn:aws:controltower:us-east-1:123456789012:enabledcontrol/26RGJRSLXCP1KW8D`Output: `{ "enabledControlDetails": { "arn": "arn:aws:controltower:us-east-1:123456789012:enabledcontrol/26RGJRSLXCP1KW8D", "controlIdentifier": "arn:aws:controltower:us-east-1::control/AWS-GR_CLOUDTRAIL_CHANGE_PROHIBITED", "driftStatusSummary": { "driftStatus": "NOT_CHECKING" }, "parameters": [], "statusSummary": { "status": "SUCCEEDED" }, "targetIdentifier": "arn:aws:organizations::123456789012:ou/o-s64ryixxxx/ou-oqxx-i5wnxxxx", "targetRegions": [ { "name": "ap-south-2" }, { "name": "ap-south-1" }, { "name": "eu-south-1" }, { "name": "us-east-1" } ] } }`For more information, see [About controls in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [GetEnabledControl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/get-enabled-control.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-landing-zone-operation`.

- **AWS CLI**
- 
            
                    **To get a Control Tower landing zone operation**The following `get-landing-zone-operation`example gets details of an AWS Control Tower landing zone operation.`aws controltower get-landing-zone-operation \ --operation-identifier``ee9d0d2d-6532-42d8-9b85-3fbb0700a606`Output: `{ "operationDetails": { "operationIdentifier": "ee9d0d2d-6532-42d8-9b85-3fbb0700xxxx", "operationType": "RESET", "startTime": "2025-04-17T03:19:33+00:00", "status": "IN_PROGRESS" } }`For more information, see [Getting started with AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [GetLandingZoneOperation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/get-landing-zone-operation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-landing-zone`.

- **AWS CLI**
- 
            
                    **To describe a Control Tower landing zone**The following `get-landing-zone`example gets details of an AWS Control Tower landing zone.`aws controltower get-landing-zone \ --landing-zone-identifier``arn:aws:controltower:us-east-1:123456789012:landingzone/13CJG46WZKXXX4X5`Output: `{ "landingZone": { "arn": "arn:aws:controltower:us-east-1:123456789012:landingzone/13CJG46WZKXXX4X5", "driftStatus": { "status": "IN_SYNC" }, "latestAvailableVersion": "3.3", "manifest": { "accessManagement": { "enabled": true }, "securityRoles": { "accountId": "098765432101" }, "governedRegions": [ "us-east-1", "us-west-2" ], "organizationStructure": { "security": { "name": "Security" } }, "centralizedLogging": { "accountId": "111122223333", "configurations": { "loggingBucket": { "retentionDays": 365 }, "kmsKeyArn": "arn:aws:kms:us-east-1:123456789012:key/example-key-id", "accessLoggingBucket": { "retentionDays": 3650 } }, "enabled": true } }, "status": "ACTIVE", "version": "3.3" } }`For more information, see [Getting started with AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [GetLandingZone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/get-landing-zone.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-baselines`.

- **AWS CLI**
- 
            
                    **To list Control Tower baselines**The following `list-baselines`example lists all available AWS Control Tower baselines.`aws controltower list-baselines`Output: `{ "baselines": [ { "arn": "arn:aws:controltower:us-east-1::baseline/4T4HA1KMO10S6311", "description": "Sets up resources to monitor security and compliance of accounts in your organization.", "name": "AuditBaseline" }, { "arn": "arn:aws:controltower:us-east-1::baseline/J8HX46AHS5MIKQPD", "description": "Sets up a central repository for logs of API activities and resource configurations from accounts in your organization.", "name": "LogArchiveBaseline" }, { "arn": "arn:aws:controltower:us-east-1::baseline/LN25R72TTG6IGPTQ", "description": "Sets up shared resources for AWS Identity Center, which prepares the AWSControlTowerBaseline to set up Identity Center access for accounts.", "name": "IdentityCenterBaseline" }, { "arn": "arn:aws:controltower:us-east-1::baseline/17BSJV3IGJ2QSGA2", "description": "Sets up resources and mandatory controls for member accounts within the target OU, required for AWS Control Tower governance.", "name": "AWSControlTowerBaseline" }, { "arn": "arn:aws:controltower:us-east-1::baseline/3WPD0NA6TJ9AOMU2", "description": "Sets up a central AWS Backup vault in your organization.", "name": "BackupCentralVaultBaseline" }, { "arn": "arn:aws:controltower:us-east-1::baseline/H6C5JFCJJ3CPU3J5", "description": "Sets up AWS Backup Audit Manager.", "name": "BackupAdminBaseline" }, { "arn": "arn:aws:controltower:us-east-1::baseline/APO9ATVPBKFRRGLK", "description": "Sets up a local AWS Backup vault and attaches multiple AWS Backup plans.", "name": "BackupBaseline" } ] }`For more information, see [Types of baselines](https://docs.aws.amazon.com/controltower/latest/userguide/types-of-baselines.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [ListBaselines](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/list-baselines.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-control-operations`.

- **AWS CLI**
- 
            
                    **To list Control Tower control operations**The following `list-control-operations`example lists details of AWS Control Tower controls in progress or queued.`aws controltower list-control-operations`Output: `{ "controlOperations": [ { "startTime": "2024-02-19T19:22:08+00:00", "operationType": "ENABLE_CONTROL", "status": "IN_PROGRESS", "statusMessage": "Operation is in progress.", "operationIdentifier": "f9f43b45-db27-44df-89d8-f9129e3632XX", "controlIdentifier": "arn:aws:controltower:us-east-1::control/SKIBWKYUQAAC", "targetIdentifier": "arn:aws:organizations::123456789012:ou/o-yy67i3pfv2/ou-slt4-8abknXXX", "enabledControlIdentifier": "arn:aws:controltower:us-east-1:123456789012:enabledcontrol/RWZFSHV2BBRU6JSE" }, { "startTime": "2024-02-19T19:21:09+00:00", "operationType": "ENABLE_CONTROL", "status": "IN_PROGRESS", "statusMessage": "Operation is in progress", "operationIdentifier": "171ee0b1-e926-486e-9775-005bd244ccXX", "controlIdentifier": "arn:aws:controltower:us-east-1::control/PDKYAANJEWJE", "targetIdentifier": "arn:aws:organizations::123456789012:ou/o-yy67i3pfv2/ou-slt4-fl6miXXX", "enabledControlIdentifier": "arn:aws:controltower:us-east-2:123456789012:enabledcontrol/XCNJARWZFSHV6JSE" } ] }`For more information, see [About controls in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [ListControlOperations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/list-control-operations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-enabled-baselines`.

- **AWS CLI**
- 
            
                    **To list Control Tower enabled baselines**The following `list-enabled-baselines`example lists all enabled AWS Control Tower baselines.`aws controltower list-enabled-baselines`Output: `{ "enabledBaselines": [ { "arn": "arn:aws:controltower:us-east-1:123456789012:enabledbaseline/XAJNZNCBC1I386C7B", "baselineIdentifier": "arn:aws:controltower:us-east-1::baseline/LN25R72TTG6IGPTQ", "statusSummary": { "status": "SUCCEEDED" }, "targetIdentifier": "arn:aws:organizations::123456789012:account/o-3onqfuxxxx/123456789012" }, { "arn": "arn:aws:controltower:us-east-1:123456789012:enabledbaseline/XAH3ZJL9DWA386CA5", "baselineIdentifier": "arn:aws:controltower:us-east-1::baseline/4T4HA1KMO10S6311", "statusSummary": { "status": "SUCCEEDED" }, "targetIdentifier": "arn:aws:organizations::123456789012:account/o-3onqfuxxxx/012345098765" }, { "arn": "arn:aws:controltower:us-east-1:123456789012:enabledbaseline/XALFJ9548TL386CBT", "baselineIdentifier": "arn:aws:controltower:us-east-1::baseline/J8HX46AHS5MIKQPD", "statusSummary": { "status": "SUCCEEDED" }, "targetIdentifier": "arn:aws:organizations::123456789012:account/o-3onqfuxxxx/098765432109" } ] }`For more information, see [Types of baselines](https://docs.aws.amazon.com/controltower/latest/userguide/types-of-baselines.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [ListEnabledBaselines](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/list-enabled-baselines.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-enabled-controls`.

- **AWS CLI**
- 
            
                    **To list Control Tower enabled controls**The following `list-enabled-controls`example gets details of AWS Control Tower enabled controls.`aws controltower list-enabled-controls \ --target-identifier``arn:aws:organizations::123456789012:ou/o-s64ryxxxxx/ou-oqxx-i5wnxxxx`Output: `{ "enabledControls": [ { "arn": "arn:aws:controltower:us-east-1:123456789012:enabledcontrol/26RGJRSLXCP1KW8D", "controlIdentifier": "arn:aws:controltower:us-east-1::control/AWS-GR_CLOUDTRAIL_CHANGE_PROHIBITED", "driftStatusSummary": { "driftStatus": "NOT_CHECKING" }, "statusSummary": { "status": "SUCCEEDED" }, "targetIdentifier": "arn:aws:organizations::123456789012:ou/o-s64ryxxxxx/ou-oqxx-i5wnxxxx" }, { "arn": "arn:aws:controltower:us-east-1:123456789012:enabledcontrol/18AY24CWKM6IVSLU", "controlIdentifier": "arn:aws:controltower:us-east-1::control/AWS-GR_CLOUDTRAIL_CLOUDWATCH_LOGS_ENABLED", "driftStatusSummary": { "driftStatus": "NOT_CHECKING" }, "statusSummary": { "status": "SUCCEEDED" }, "targetIdentifier": "arn:aws:organizations::123456789012:ou/o-s64ryxxxxx/ou-oqxx-i5wnxxxx" } ] }`For more information, see [About controls in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [ListEnabledControls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/list-enabled-controls.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-landing-zone-operations`.

- **AWS CLI**
- 
            
                    **To list Control Tower landing zone operations**The following `list-landing-zone-operations`example lists AWS Control Tower landing zone operations.`aws controltower list-landing-zone-operations`Output: `{ "landingZoneOperations": [ { "operationIdentifier": "202ee056-5147-49fd-a7ad-8161e3bf043a", "operationType": "RESET", "status": "SUCCEEDED" }, { "operationIdentifier": "dbd4a4b1-baf9-48cc-bd71-6b923d0f2339", "operationType": "RESET", "status": "SUCCEEDED" }, { "operationIdentifier": "e6261ab8-3247-4052-af31-1afe7bb0593e", "operationType": "UPDATE", "status": "SUCCEEDED" }, { "operationIdentifier": "507c6c87-89a8-435f-8697-b257a800f129", "operationType": "UPDATE", "status": "SUCCEEDED" } ] }`For more information, see [Getting started with AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [ListLandingZoneOperations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/list-landing-zone-operations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-landing-zones`.

- **AWS CLI**
- 
            
                    **To list a Control Tower landing zone identifier**The following `list-landing-zones`example lists a Control Tower landing zone`identifier`.`aws controltower list-landing-zones`Output: `{ "landingZones": [ { "arn": "arn:aws:controltower:us-east-1:123456789012:landingzone/13CJG46WZKXXX4X5" } ] }`For more information, see [Getting started with AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [ListLandingZones](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/list-landing-zones.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list tags for Control Tower enabled controls**The following `list-tags-for-resource`example lists the tags for AWS Control Tower Enabled Controls.`aws controltower list-tags-for-resource \ --resource-arn``"arn:aws:controltower:us-east-1:123456789012:enabledcontrol/2H2AWUG4SKG81855"`Output: `{ "tags": { "TestTagKey": "TestTagValue" } }`For more information, see [About controls in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reset-enabled-baseline`.

- **AWS CLI**
- 
            
                    **To reset a Control Tower enabled baseline**The following `reset-enabled-baseline`example resets an AWS Control Tower enabled baseline.`aws controltower reset-enabled-baseline \ --enabled-baseline-identifier``arn:aws:controltower:us-east-1:123456789012:enabledbaseline/XOM12BEL4YD578CQ2`Output: `{ "operationIdentifier": "214cde95-5c39-46b9-b429-4fad550a7096" }`For more information, see [Types of baselines](https://docs.aws.amazon.com/controltower/latest/userguide/types-of-baselines.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [ResetEnabledBaseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/reset-enabled-baseline.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reset-enabled-control`.

- **AWS CLI**
- 
            
                    **To reset a Control Tower enabled control**The following `reset-enabled-control`example resets an AWS Control Tower enabled control.`aws controltower reset-enabled-control \ --enabled-control-identifier``arn:aws:controltower:us-east-1:123456789012:enabledcontrol/2H2AWUG4SKG81855`Output: `{ "operationIdentifier": "8276XXXX-b4XX-4eXX-96XX-881d2a4XXXXX" }`For more information, see [About controls in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [ResetEnabledControl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/reset-enabled-control.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reset-landing-zone`.

- **AWS CLI**
- 
            
                    **To reset a Control Tower landing zone**The following `reset-landing-zone`example resets a AWS Control Tower landing zone.`aws controltower reset-landing-zone \ --landing-zone-identifier``arn:aws:controltower:us-east-1:123456789012:landingzone/13CJG46WZKXXX4X5`Output: `{ "operationIdentifier": "73XXXXXX-b2XX-77XX-c6XX-374XXXXXXXXX" }`For more information, see [Getting started with AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [ResetLandingZone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/reset-landing-zone.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To tag a Control Tower enabled control**The following `tag-resource`example tags an AWS Control Tower enabled control.`aws controltower tag-resource \ --resource-arn``"arn:aws:controltower:us-east-1:123456789012:enabledcontrol/2H2AWUG4SKG81855"`\ --tags`"TestTagKey=TestTagValue"`This command produces no output. For more information, see [About controls in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To untag a Control Tower enabled control**The following `untag-resource`example untags an AWS Control Tower enabled control.`aws controltower untag-resource \ --resource-arn``"arn:aws:controltower:us-east-1:123456789012:enabledcontrol/2H2AWUG4SKG81855"`\ --tag-keys`"TestTagKey"`This command produces no output. For more information, see [About controls in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-enabled-baseline`.

- **AWS CLI**
- 
            
                    **Example 1: To update a disabled Control Tower baseline**The following `update-enabled-baseline`example updates an AWS Control Tower enabled baseline if baseline 'IdentityCenterBaseline' is disabled.`aws controltower update-enabled-baseline \ --baseline-version``4.0`\ --enabled-baseline-identifier`arn:aws:controltower:us-east-1:123456789012:enabledbaseline/XOM12BEL4YD578CQ2`Output: `{ "operationIdentifier": "214cde95-5c39-46b9-b429-4fad550a7096" }`**Example 2: To update an enabled Control Tower baseline**The following `update-enabled-baseline`example updates an AWS Control Tower enabled baseline if baseline 'IdentityCenterBaseline' is enabled.`aws controltower update-enabled-baseline \ --baseline-version``4.0`\ --enabled-baseline-identifier`arn:aws:controltower:us-east-1:123456789012:enabledbaseline/XOM12BEL4YD578CQ2`\ --parameters '`[{"key":"IdentityCenterEnabledBaselineArn","value":"arn:aws:controltower:us-east-1:123456789012:enabledbaseline/XAJNZNCBC1I386C7B"}]`'Output: `{ "operationIdentifier": "b0f4a7c2-334d-48d9-971e-47fea9db3e8b" }`For more information, see [Types of baselines](https://docs.aws.amazon.com/controltower/latest/userguide/types-of-baselines.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [UpdateEnabledBaseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/update-enabled-baseline.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-enabled-control`.

- **AWS CLI**
- 
            
                    **To update a Control Tower enabled control**The following `update-enabled-control`example updates an AWS Control Tower enabled control.`aws controltower update-enabled-control \ --enabled-control-identifier``arn:aws:controltower:us-east-1:123456789012:enabledcontrol/JSJN8UL0G2MWGRTZ`\ --parameters '`[{"key":"AllowedRegions","value":["us-east-1","us-west-1","us-west-2","us-east-2"]}]`'Output: `{ "operationIdentifier": "b8f0dxxx-08xx-43xx-a2xx-568e9922xxxx" }`For more information, see [About controls in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [UpdateEnabledControl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/update-enabled-control.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-landing-zone`.

- **AWS CLI**
- 
            
                    **To update a Control Tower landing zone**The following `update-landing-zone`example updates AWS Control Tower landing zone.`aws controltower update-landing-zone \ --landing-zone-identifier``arn:aws:controltower:us-east-1:123456789012:landingzone/13CJG46WZKXXX4X5`\ --landing-zone-version`3.3`\ --manifest`"file://UpdateLandingZoneManifest.json"`Output: `{ "operationIdentifier": "53XXXXXX-b2XX-97XX-c6XX-474XXXXXXXXX" }`For more information, see [Getting started with AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html)in the*AWS Control Tower User Guide*.- 
                    For API details, see [UpdateLandingZone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/update-landing-zone.html)in*AWS CLI Command Reference*.
 
-