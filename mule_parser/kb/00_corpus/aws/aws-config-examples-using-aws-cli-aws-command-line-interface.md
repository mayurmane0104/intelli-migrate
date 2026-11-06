# AWS Config examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_config-service_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_config-service_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS Config.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `delete-config-rule`.

- **AWS CLI**
- 
            
                    **To delete an AWS Config rule**The following command deletes an AWS Config rule named `MyConfigRule`:`aws configservice delete-config-rule --config-rule-name``MyConfigRule`- 
                    For API details, see [DeleteConfigRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-config-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-delivery-channel`.

- **AWS CLI**
- 
            
                    **To delete a delivery channel**The following command deletes the default delivery channel: `aws configservice delete-delivery-channel --delivery-channel-name``default`- 
                    For API details, see [DeleteDeliveryChannel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-delivery-channel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-evaluation-results`.

- **AWS CLI**
- 
            
                    **To manually delete evaluation results**The following command deletes the current evaluation results for the AWS managed rule s3-bucket-versioning-enabled: `aws configservice delete-evaluation-results --config-rule-name``s3-bucket-versioning-enabled`- 
                    For API details, see [DeleteEvaluationResults](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-evaluation-results.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deliver-config-snapshot`.

- **AWS CLI**
- 
            
                    **To deliver a configuration snapshot**The following command delivers a configuration snapshot to the Amazon S3 bucket that belongs to the default delivery channel: `aws configservice deliver-config-snapshot --delivery-channel-name``default`Output: `{ "configSnapshotId": "d0333b00-a683-44af-921e-examplefb794" }`- 
                    For API details, see [DeliverConfigSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/deliver-config-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-compliance-by-config-rule`.

- **AWS CLI**
- 
            
                    **To get compliance information for your AWS Config rules**The following command returns compliance information for each AWS Config rule that is violated by one or more AWS resources: `aws configservice describe-compliance-by-config-rule --compliance-types``NON_COMPLIANT`In the output, the value for each `CappedCount`attribute indicates how many resources do not comply with the related rule. For example, the following output indicates that 3 resources do not comply with the rule named`InstanceTypesAreT2micro`.Output: `{ "ComplianceByConfigRules": [ { "Compliance": { "ComplianceContributorCount": { "CappedCount": 3, "CapExceeded": false }, "ComplianceType": "NON_COMPLIANT" }, "ConfigRuleName": "InstanceTypesAreT2micro" }, { "Compliance": { "ComplianceContributorCount": { "CappedCount": 10, "CapExceeded": false }, "ComplianceType": "NON_COMPLIANT" }, "ConfigRuleName": "RequiredTagsForVolumes" } ] }`- 
                    For API details, see [DescribeComplianceByConfigRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-compliance-by-config-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-compliance-by-resource`.

- **AWS CLI**
- 
            
                    **To get compliance information for your AWS resources**The following command returns compliance information for each EC2 instance that is recorded by AWS Config and that violates one or more rules: `aws configservice describe-compliance-by-resource --resource-type``AWS::EC2::Instance`--compliance-types`NON_COMPLIANT`In the output, the value for each `CappedCount`attribute indicates how many rules the resource violates. For example, the following output indicates that instance`i-1a2b3c4d`violates 2 rules.Output: `{ "ComplianceByResources": [ { "ResourceType": "AWS::EC2::Instance", "ResourceId": "i-1a2b3c4d", "Compliance": { "ComplianceContributorCount": { "CappedCount": 2, "CapExceeded": false }, "ComplianceType": "NON_COMPLIANT" } }, { "ResourceType": "AWS::EC2::Instance", "ResourceId": "i-2a2b3c4d ", "Compliance": { "ComplianceContributorCount": { "CappedCount": 3, "CapExceeded": false }, "ComplianceType": "NON_COMPLIANT" } } ] }`- 
                    For API details, see [DescribeComplianceByResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-compliance-by-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-config-rule-evaluation-status`.

- **AWS CLI**
- 
            
                    **To get status information for an AWS Config rule**The following command returns the status information for an AWS Config rule named `MyConfigRule`:`aws configservice describe-config-rule-evaluation-status --config-rule-names``MyConfigRule`Output: `{ "ConfigRulesEvaluationStatus": [ { "ConfigRuleArn": "arn:aws:config:us-east-1:123456789012:config-rule/config-rule-abcdef", "FirstActivatedTime": 1450311703.844, "ConfigRuleId": "config-rule-abcdef", "LastSuccessfulInvocationTime": 1450314643.156, "ConfigRuleName": "MyConfigRule" } ] }`- 
                    For API details, see [DescribeConfigRuleEvaluationStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-config-rule-evaluation-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-config-rules`.

- **AWS CLI**
- 
            
                    **To get details for an AWS Config rule**The following command returns details for an AWS Config rule named `InstanceTypesAreT2micro`:`aws configservice describe-config-rules --config-rule-names``InstanceTypesAreT2micro`Output: `{ "ConfigRules": [ { "ConfigRuleState": "ACTIVE", "Description": "Evaluates whether EC2 instances are the t2.micro type.", "ConfigRuleName": "InstanceTypesAreT2micro", "ConfigRuleArn": "arn:aws:config:us-east-1:123456789012:config-rule/config-rule-abcdef", "Source": { "Owner": "CUSTOM_LAMBDA", "SourceIdentifier": "arn:aws:lambda:us-east-1:123456789012:function:InstanceTypeCheck", "SourceDetails": [ { "EventSource": "aws.config", "MessageType": "ConfigurationItemChangeNotification" } ] }, "InputParameters": "{\"desiredInstanceType\":\"t2.micro\"}", "Scope": { "ComplianceResourceTypes": [ "AWS::EC2::Instance" ] }, "ConfigRuleId": "config-rule-abcdef" } ] }`- 
                    For API details, see [DescribeConfigRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-config-rules.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-configuration-recorder-status`.

- **AWS CLI**
- 
            
                    **To get status information for the configuration recorder**The following command returns the status of the default configuration recorder: `aws configservice describe-configuration-recorder-status`Output: `{ "ConfigurationRecordersStatus": [ { "name": "default", "lastStatus": "SUCCESS", "recording": true, "lastStatusChangeTime": 1452193834.344, "lastStartTime": 1441039997.819, "lastStopTime": 1441039992.835 } ] }`- 
                    For API details, see [DescribeConfigurationRecorderStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-configuration-recorder-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-configuration-recorders`.

- **AWS CLI**
- 
            
                    **To get details about the configuration recorder**The following command returns details about the default configuration recorder: `aws configservice describe-configuration-recorders`Output: `{ "ConfigurationRecorders": [ { "recordingGroup": { "allSupported": true, "resourceTypes": [], "includeGlobalResourceTypes": true }, "roleARN": "arn:aws:iam::123456789012:role/config-ConfigRole-A1B2C3D4E5F6", "name": "default" } ] }`- 
                    For API details, see [DescribeConfigurationRecorders](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-configuration-recorders.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-delivery-channel-status`.

- **AWS CLI**
- 
            
                    **To get status information for the delivery channel**The following command returns the status of the delivery channel: `aws configservice describe-delivery-channel-status`Output: `{ "DeliveryChannelsStatus": [ { "configStreamDeliveryInfo": { "lastStatusChangeTime": 1452193834.381, "lastStatus": "SUCCESS" }, "configHistoryDeliveryInfo": { "lastSuccessfulTime": 1450317838.412, "lastStatus": "SUCCESS", "lastAttemptTime": 1450317838.412 }, "configSnapshotDeliveryInfo": { "lastSuccessfulTime": 1452185597.094, "lastStatus": "SUCCESS", "lastAttemptTime": 1452185597.094 }, "name": "default" } ] }`- 
                    For API details, see [DescribeDeliveryChannelStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-delivery-channel-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-delivery-channels`.

- **AWS CLI**
- 
            
                    **To get details about the delivery channel**The following command returns details about the delivery channel: `aws configservice describe-delivery-channels`Output: `{ "DeliveryChannels": [ { "snsTopicARN": "arn:aws:sns:us-east-1:123456789012:config-topic", "name": "default", "s3BucketName": "config-bucket-123456789012" } ] }`- 
                    For API details, see [DescribeDeliveryChannels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-delivery-channels.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-compliance-details-by-config-rule`.

- **AWS CLI**
- 
            
                    **To get the evaluation results for an AWS Config rule**The following command returns the evaluation results for all of the resources that don't comply with an AWS Config rule named `InstanceTypesAreT2micro`:`aws configservice get-compliance-details-by-config-rule --config-rule-name``InstanceTypesAreT2micro`--compliance-types`NON_COMPLIANT`Output: `{ "EvaluationResults": [ { "EvaluationResultIdentifier": { "OrderingTimestamp": 1450314635.065, "EvaluationResultQualifier": { "ResourceType": "AWS::EC2::Instance", "ResourceId": "i-1a2b3c4d", "ConfigRuleName": "InstanceTypesAreT2micro" } }, "ResultRecordedTime": 1450314645.261, "ConfigRuleInvokedTime": 1450314642.948, "ComplianceType": "NON_COMPLIANT" }, { "EvaluationResultIdentifier": { "OrderingTimestamp": 1450314635.065, "EvaluationResultQualifier": { "ResourceType": "AWS::EC2::Instance", "ResourceId": "i-2a2b3c4d", "ConfigRuleName": "InstanceTypesAreT2micro" } }, "ResultRecordedTime": 1450314645.18, "ConfigRuleInvokedTime": 1450314642.902, "ComplianceType": "NON_COMPLIANT" }, { "EvaluationResultIdentifier": { "OrderingTimestamp": 1450314635.065, "EvaluationResultQualifier": { "ResourceType": "AWS::EC2::Instance", "ResourceId": "i-3a2b3c4d", "ConfigRuleName": "InstanceTypesAreT2micro" } }, "ResultRecordedTime": 1450314643.346, "ConfigRuleInvokedTime": 1450314643.124, "ComplianceType": "NON_COMPLIANT" } ] }`- 
                    For API details, see [GetComplianceDetailsByConfigRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-compliance-details-by-config-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-compliance-details-by-resource`.

- **AWS CLI**
- 
            
                    **To get the evaluation results for an AWS resource**The following command returns the evaluation results for each rule with which the EC2 instance `i-1a2b3c4d`does not comply:`aws configservice get-compliance-details-by-resource --resource-type``AWS::EC2::Instance`--resource-id`i-1a2b3c4d`--compliance-types`NON_COMPLIANT`Output: `{ "EvaluationResults": [ { "EvaluationResultIdentifier": { "OrderingTimestamp": 1450314635.065, "EvaluationResultQualifier": { "ResourceType": "AWS::EC2::Instance", "ResourceId": "i-1a2b3c4d", "ConfigRuleName": "InstanceTypesAreT2micro" } }, "ResultRecordedTime": 1450314643.288, "ConfigRuleInvokedTime": 1450314643.034, "ComplianceType": "NON_COMPLIANT" }, { "EvaluationResultIdentifier": { "OrderingTimestamp": 1450314635.065, "EvaluationResultQualifier": { "ResourceType": "AWS::EC2::Instance", "ResourceId": "i-1a2b3c4d", "ConfigRuleName": "RequiredTagForEC2Instances" } }, "ResultRecordedTime": 1450314645.261, "ConfigRuleInvokedTime": 1450314642.948, "ComplianceType": "NON_COMPLIANT" } ] }`- 
                    For API details, see [GetComplianceDetailsByResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-compliance-details-by-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-compliance-summary-by-config-rule`.

- **AWS CLI**
- 
            
                    **To get the compliance summary for your AWS Config rules**The following command returns the number of rules that are compliant and the number that are noncompliant: `aws configservice get-compliance-summary-by-config-rule`In the output, the value for each `CappedCount`attribute indicates how many rules are compliant or noncompliant.Output: `{ "ComplianceSummary": { "NonCompliantResourceCount": { "CappedCount": 3, "CapExceeded": false }, "ComplianceSummaryTimestamp": 1452204131.493, "CompliantResourceCount": { "CappedCount": 2, "CapExceeded": false } } }`- 
                    For API details, see [GetComplianceSummaryByConfigRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-compliance-summary-by-config-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-compliance-summary-by-resource-type`.

- **AWS CLI**
- 
            
                    **To get the compliance summary for all resource types**The following command returns the number of AWS resources that are noncompliant and the number that are compliant: `aws configservice get-compliance-summary-by-resource-type`In the output, the value for each `CappedCount`attribute indicates how many resources are compliant or noncompliant.Output: `{ "ComplianceSummariesByResourceType": [ { "ComplianceSummary": { "NonCompliantResourceCount": { "CappedCount": 16, "CapExceeded": false }, "ComplianceSummaryTimestamp": 1453237464.543, "CompliantResourceCount": { "CappedCount": 10, "CapExceeded": false } } } ] }`**To get the compliance summary for a specific resource type**The following command returns the number of EC2 instances that are noncompliant and the number that are compliant: `aws configservice get-compliance-summary-by-resource-type --resource-types``AWS::EC2::Instance`In the output, the value for each `CappedCount`attribute indicates how many resources are compliant or noncompliant.Output: `{ "ComplianceSummariesByResourceType": [ { "ResourceType": "AWS::EC2::Instance", "ComplianceSummary": { "NonCompliantResourceCount": { "CappedCount": 3, "CapExceeded": false }, "ComplianceSummaryTimestamp": 1452204923.518, "CompliantResourceCount": { "CappedCount": 7, "CapExceeded": false } } } ] }`- 
                    For API details, see [GetComplianceSummaryByResourceType](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-compliance-summary-by-resource-type.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-resource-config-history`.

- **AWS CLI**
- 
            
                    **To get the configuration history of an AWS resource**The following command returns a list of configuration items for an EC2 instance with an ID of `i-1a2b3c4d`:`aws configservice get-resource-config-history --resource-type``AWS::EC2::Instance`--resource-id`i-1a2b3c4d`- 
                    For API details, see [GetResourceConfigHistory](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-resource-config-history.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-status`.

- **AWS CLI**
- 
            
                    **To get the status for AWS Config**The following command returns the status of the delivery channel and configuration recorder: `aws configservice get-status`Output: `Configuration Recorders: name: default recorder: ON last status: SUCCESS Delivery Channels: name: default last stream delivery status: SUCCESS last history delivery status: SUCCESS last snapshot delivery status: SUCCESS`- 
                    For API details, see [GetStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-discovered-resources`.

- **AWS CLI**
- 
            
                    **To list resources that AWS Config has discovered**The following command lists the EC2 instances that AWS Config has discovered: `aws configservice list-discovered-resources --resource-type``AWS::EC2::Instance`Output: `{ "resourceIdentifiers": [ { "resourceType": "AWS::EC2::Instance", "resourceId": "i-1a2b3c4d" }, { "resourceType": "AWS::EC2::Instance", "resourceId": "i-2a2b3c4d" }, { "resourceType": "AWS::EC2::Instance", "resourceId": "i-3a2b3c4d" } ] }`- 
                    For API details, see [ListDiscoveredResources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/list-discovered-resources.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-config-rule`.

- **AWS CLI**
- 
            
                    **To add an AWS managed Config rule**The following command provides JSON code to add an AWS managed Config rule: `aws configservice put-config-rule --config-rule``file://RequiredTagsForEC2Instances.json``RequiredTagsForEC2Instances.json`is a JSON file that contains the rule configuration:`{ "ConfigRuleName": "RequiredTagsForEC2Instances", "Description": "Checks whether the CostCenter and Owner tags are applied to EC2 instances.", "Scope": { "ComplianceResourceTypes": [ "AWS::EC2::Instance" ] }, "Source": { "Owner": "AWS", "SourceIdentifier": "REQUIRED_TAGS" }, "InputParameters": "{\"tag1Key\":\"CostCenter\",\"tag2Key\":\"Owner\"}" }`For the `ComplianceResourceTypes`attribute, this JSON code limits the scope to resources of the`AWS::EC2::Instance`type, so AWS Config will evaluate only EC2 instances against the rule. Because the rule is a managed rule, the`Owner`attribute is set to`AWS`, and the`SourceIdentifier`attribute is set to the rule identifier,`REQUIRED_TAGS`. For the`InputParameters`attribute, the tag keys that the rule requires,`CostCenter`and`Owner`, are specified.If the command succeeds, AWS Config returns no output. To verify the rule configuration, run the describe-config-rules command, and specify the rule name. **To add a customer managed Config rule**The following command provides JSON code to add a customer managed Config rule: `aws configservice put-config-rule --config-rule``file://InstanceTypesAreT2micro.json``InstanceTypesAreT2micro.json`is a JSON file that contains the rule configuration:`{ "ConfigRuleName": "InstanceTypesAreT2micro", "Description": "Evaluates whether EC2 instances are the t2.micro type.", "Scope": { "ComplianceResourceTypes": [ "AWS::EC2::Instance" ] }, "Source": { "Owner": "CUSTOM_LAMBDA", "SourceIdentifier": "arn:aws:lambda:us-east-1:123456789012:function:InstanceTypeCheck", "SourceDetails": [ { "EventSource": "aws.config", "MessageType": "ConfigurationItemChangeNotification" } ] }, "InputParameters": "{\"desiredInstanceType\":\"t2.micro\"}" }`For the `ComplianceResourceTypes`attribute, this JSON code limits the scope to resources of the`AWS::EC2::Instance`type, so AWS Config will evaluate only EC2 instances against the rule. Because this rule is a customer managed rule, the`Owner`attribute is set to`CUSTOM_LAMBDA`, and the`SourceIdentifier`attribute is set to the ARN of the AWS Lambda function. The`SourceDetails`object is required. The parameters that are specified for the`InputParameters`attribute are passed to the AWS Lambda function when AWS Config invokes it to evaluate resources against the rule.If the command succeeds, AWS Config returns no output. To verify the rule configuration, run the describe-config-rules command, and specify the rule name. - 
                    For API details, see [PutConfigRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-config-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-configuration-recorder`.

- **AWS CLI**
- 
            
                    **Example 1: To record all supported resources**The following command creates a configuration recorder that tracks changes to all supported resource types, including global resource types: `aws configservice put-configuration-recorder \ --configuration-recorder``name=default,roleARN=arn:aws:iam::123456789012:role/config-role`\ --recording-group`allSupported=true,includeGlobalResourceTypes=true`If the command succeeds, AWS Config returns no output. To verify the settings of your configuration recorder, run the describe-configuration-recorders command. **Example 2: To record specific types of resources**The following command creates a configuration recorder that tracks changes to only those types of resources that are specified in the JSON file for the --recording-group option: `aws configservice put-configuration-recorder \ --configuration-recorder``name=default,roleARN=arn:aws:iam::123456789012:role/config-role`\ --recording-group`file://recordingGroup.json`recordingGroup.json is a JSON file that specifies the types of resources that AWS Config will record: `{ "allSupported": false, "includeGlobalResourceTypes": false, "resourceTypes": [ "AWS::EC2::EIP", "AWS::EC2::Instance", "AWS::EC2::NetworkAcl", "AWS::EC2::SecurityGroup", "AWS::CloudTrail::Trail", "AWS::EC2::Volume", "AWS::EC2::VPC", "AWS::IAM::User", "AWS::IAM::Policy" ] }`Before you can specify resource types for the resourceTypes key, you must set the allSupported and includeGlobalResourceTypes options to false or omit them. If the command succeeds, AWS Config returns no output. To verify the settings of your configuration recorder, run the describe-configuration-recorders command. **Example 3: To select all supported resources excluding specific types of resources**The following command creates a configuration recorder that tracks changes to all current and future supported resource types excluding those types of resources that are specified in the JSON file for the --recording-group option: `aws configservice put-configuration-recorder \ --configuration-recorder``name=default,roleARN=arn:aws:iam::123456789012:role/config-role`\ --recording-group`file://recordingGroup.json`recordingGroup.json is a JSON file that specifies the types of resources that AWS Config will record: `{ "allSupported": false, "exclusionByResourceTypes": { "resourceTypes": [ "AWS::Redshift::ClusterSnapshot", "AWS::RDS::DBClusterSnapshot", "AWS::CloudFront::StreamingDistribution" ] }, "includeGlobalResourceTypes": false, "recordingStrategy": { "useOnly": "EXCLUSION_BY_RESOURCE_TYPES" }, }`Before you can specify resource types to excluding from recording: 1) You must set the allSupported and includeGlobalResourceTypes options to false or omit them, and 2) You must set the useOnly field of RecordingStrategy to EXCLUSION_BY_RESOURCE_TYPES. If the command succeeds, AWS Config returns no output. To verify the settings of your configuration recorder, run the describe-configuration-recorders command. - 
                    For API details, see [PutConfigurationRecorder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-configuration-recorder.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-delivery-channel`.

- **AWS CLI**
- 
            
                    **To create a delivery channel**The following command provides the settings for the delivery channel as JSON code: `aws configservice put-delivery-channel --delivery-channel``file://deliveryChannel.json`The `deliveryChannel.json`file specifies the delivery channel attributes:`{ "name": "default", "s3BucketName": "config-bucket-123456789012", "snsTopicARN": "arn:aws:sns:us-east-1:123456789012:config-topic", "configSnapshotDeliveryProperties": { "deliveryFrequency": "Twelve_Hours" } }`This example sets the following attributes: `name`- The name of the delivery channel. By default, AWS Config assigns the name`default`to a new delivery channel.You cannot update the delivery channel name with the`put-delivery-channel`command. For the steps to change the name, see Renaming the Delivery Channel.`s3BucketName`- The name of the Amazon S3 bucket to which AWS Config delivers configuration snapshots and configuration history files.If you specify a bucket that belongs to another AWS account, that bucket must have policies that grant access permissions to AWS Config. For more information, see Permissions for the Amazon S3 Bucket.`snsTopicARN`- The Amazon Resource Name (ARN) of the Amazon SNS topic to which AWS Config sends notifications about configuration changes.If you choose a topic from another account, the topic must have policies that grant access permissions to AWS Config. For more information, see Permissions for the Amazon SNS Topic.`configSnapshotDeliveryProperties`- Contains the`deliveryFrequency`attribute, which sets how often AWS Config delivers configuration snapshots and how often it invokes evaluations for periodic Config rules.If the command succeeds, AWS Config returns no output. To verify the settings of your delivery channel, run the describe-delivery-channels command. - 
                    For API details, see [PutDeliveryChannel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-delivery-channel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-config-rules-evaluation`.

- **AWS CLI**
- 
            
                    **To run an on-demand evaluation for AWS Config rules**The following command starts an evaluation for two AWS managed rules: `aws configservice start-config-rules-evaluation --config-rule-names``s3-bucket-versioning-enabled``cloudtrail-enabled`- 
                    For API details, see [StartConfigRulesEvaluation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/start-config-rules-evaluation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-configuration-recorder`.

- **AWS CLI**
- 
            
                    **To start the configuration recorder**The following command starts the default configuration recorder: `aws configservice start-configuration-recorder --configuration-recorder-name``default`If the command succeeds, AWS Config returns no output. To verify that AWS Config is recording your resources, run the get-status command. - 
                    For API details, see [StartConfigurationRecorder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/start-configuration-recorder.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-configuration-recorder`.

- **AWS CLI**
- 
            
                    **To stop the configuration recorder**The following command stops the default configuration recorder: `aws configservice stop-configuration-recorder --configuration-recorder-name``default`If the command succeeds, AWS Config returns no output. To verify that AWS Config is not recording your resources, run the get-status command. - 
                    For API details, see [StopConfigurationRecorder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/stop-configuration-recorder.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `subscribe`.

- **AWS CLI**
- 
            
                    **To subscribe to AWS Config**The following command creates the default delivery channel and configuration recorder. The command also specifies the Amazon S3 bucket and Amazon SNS topic to which AWS Config will deliver configuration information: `aws configservice subscribe --s3-bucket``config-bucket-123456789012`--sns-topic`arn:aws:sns:us-east-1:123456789012:config-topic`--iam-role`arn:aws:iam::123456789012:role/ConfigRole-A1B2C3D4E5F6`Output: `Using existing S3 bucket: config-bucket-123456789012 Using existing SNS topic: arn:aws:sns:us-east-1:123456789012:config-topic Subscribe succeeded: Configuration Recorders: [ { "recordingGroup": { "allSupported": true, "resourceTypes": [], "includeGlobalResourceTypes": false }, "roleARN": "arn:aws:iam::123456789012:role/ConfigRole-A1B2C3D4E5F6", "name": "default" } ] Delivery Channels: [ { "snsTopicARN": "arn:aws:sns:us-east-1:123456789012:config-topic", "name": "default", "s3BucketName": "config-bucket-123456789012" } ]`- 
                    For API details, see [Subscribe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/subscribe.html)in*AWS CLI Command Reference*.
 
-