# Application Auto Scaling examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_application-auto-scaling_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_application-auto-scaling_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Application Auto Scaling.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `delete-scaling-policy`.

- **AWS CLI**
- 
            
                    **To delete a scaling policy**This example deletes a scaling policy for the Amazon ECS service web-app running in the default cluster. Command: `aws application-autoscaling delete-scaling-policy --policy-name``web-app-cpu-lt-25`--scalable-dimension`ecs:service:DesiredCount`--resource-id`service/default/web-app`--service-namespace`ecs`- 
                    For API details, see [DeleteScalingPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/delete-scaling-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-scheduled-action`.

- **AWS CLI**
- 
            
                    **To delete a scheduled action**The following `delete-scheduled-action`example deletes the specified scheduled action from the specified Amazon AppStream 2.0 fleet:`aws application-autoscaling delete-scheduled-action \ --service-namespace``appstream`\ --scalable-dimension`appstream:fleet:DesiredCapacity`\ --resource-id`fleet/sample-fleet`\ --scheduled-action-name`my-recurring-action`This command produces no output. For more information, see [Scheduled Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.html)in the*Application Auto Scaling User Guide*.- 
                    For API details, see [DeleteScheduledAction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/delete-scheduled-action.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deregister-scalable-target`.

- **AWS CLI**
- 
            
                    **To deregister a scalable target**This example deregisters a scalable target for an Amazon ECS service called web-app that is running in the default cluster. Command: `aws application-autoscaling deregister-scalable-target --service-namespace``ecs`--scalable-dimension`ecs:service:DesiredCount`--resource-id`service/default/web-app`This example deregisters a scalable target for a custom resource. The custom-resource-id.txt file contains a string that identifies the Resource ID, which, for a custom resource, is the path to the custom resource through your Amazon API Gateway endpoint. Command: `aws application-autoscaling deregister-scalable-target --service-namespace``custom-resource`--scalable-dimension`custom-resource:ResourceType:Property`--resource-id`file://~/custom-resource-id.txt`Contents of custom-resource-id.txt file: `https://example.execute-api.us-west-2.amazonaws.com/prod/scalableTargetDimensions/1-23456789`- 
                    For API details, see [DeregisterScalableTarget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/deregister-scalable-target.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-scalable-targets`.

- **AWS CLI**
- 
            
                    **To describe scalable targets**The following `describe-scalable-targets`example describes the scalable targets for the`ecs`service namespace.`aws application-autoscaling describe-scalable-targets \ --service-namespace``ecs`Output: `{ "ScalableTargets": [ { "ServiceNamespace": "ecs", "ScalableDimension": "ecs:service:DesiredCount", "ResourceId": "service/default/web-app", "MinCapacity": 1, "MaxCapacity": 10, "RoleARN": "arn:aws:iam::123456789012:role/aws-service-role/ecs.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_ECSService", "CreationTime": 1462558906.199, "SuspendedState": { "DynamicScalingOutSuspended": false, "ScheduledScalingSuspended": false, "DynamicScalingInSuspended": false }, "ScalableTargetARN": "arn:aws:application-autoscaling:us-west-2:123456789012:scalable-target/1234abcd56ab78cd901ef1234567890ab123" } ] }`For more information, see [AWS services that you can use with Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/integrated-services-list.html)in the*Application Auto Scaling User Guide*.- 
                    For API details, see [DescribeScalableTargets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/describe-scalable-targets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-scaling-activities`.

- **AWS CLI**
- 
            
                    **Example 1: To describe scaling activities for the specified Amazon ECS service**The following `describe-scaling-activities`example describes the scaling activities for an Amazon ECS service called`web-app`that is running in the`default`cluster. The output shows a scaling activity initiated by a scaling policy.`aws application-autoscaling describe-scaling-activities \ --service-namespace``ecs`\ --resource-id`service/default/web-app`Output: `{ "ScalingActivities": [ { "ScalableDimension": "ecs:service:DesiredCount", "Description": "Setting desired count to 1.", "ResourceId": "service/default/web-app", "ActivityId": "e6c5f7d1-dbbb-4a3f-89b2-51f33e766399", "StartTime": 1462575838.171, "ServiceNamespace": "ecs", "EndTime": 1462575872.111, "Cause": "monitor alarm web-app-cpu-lt-25 in state ALARM triggered policy web-app-cpu-lt-25", "StatusMessage": "Successfully set desired count to 1. Change successfully fulfilled by ecs.", "StatusCode": "Successful" } ] }`For more information, see [Scaling activities for Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scaling-activities.html)in the*Application Auto Scaling User Guide*.**Example 2: To describe scaling activities for the specified DynamoDB table**The following `describe-scaling-activities`example describes the scaling activities for a DynamoDB table called`TestTable`. The output shows scaling activities initiated by two different scheduled actions.`aws application-autoscaling describe-scaling-activities \ --service-namespace``dynamodb`\ --resource-id`table/TestTable`Output: `{ "ScalingActivities": [ { "ScalableDimension": "dynamodb:table:WriteCapacityUnits", "Description": "Setting write capacity units to 10.", "ResourceId": "table/my-table", "ActivityId": "4d1308c0-bbcf-4514-a673-b0220ae38547", "StartTime": 1561574415.086, "ServiceNamespace": "dynamodb", "EndTime": 1561574449.51, "Cause": "maximum capacity was set to 10", "StatusMessage": "Successfully set write capacity units to 10. Change successfully fulfilled by dynamodb.", "StatusCode": "Successful" }, { "ScalableDimension": "dynamodb:table:WriteCapacityUnits", "Description": "Setting min capacity to 5 and max capacity to 10", "ResourceId": "table/my-table", "ActivityId": "f2b7847b-721d-4e01-8ef0-0c8d3bacc1c7", "StartTime": 1561574414.644, "ServiceNamespace": "dynamodb", "Cause": "scheduled action name my-second-scheduled-action was triggered", "StatusMessage": "Successfully set min capacity to 5 and max capacity to 10", "StatusCode": "Successful" }, { "ScalableDimension": "dynamodb:table:WriteCapacityUnits", "Description": "Setting write capacity units to 15.", "ResourceId": "table/my-table", "ActivityId": "d8ea4de6-9eaa-499f-b466-2cc5e681ba8b", "StartTime": 1561574108.904, "ServiceNamespace": "dynamodb", "EndTime": 1561574140.255, "Cause": "minimum capacity was set to 15", "StatusMessage": "Successfully set write capacity units to 15. Change successfully fulfilled by dynamodb.", "StatusCode": "Successful" }, { "ScalableDimension": "dynamodb:table:WriteCapacityUnits", "Description": "Setting min capacity to 15 and max capacity to 20", "ResourceId": "table/my-table", "ActivityId": "3250fd06-6940-4e8e-bb1f-d494db7554d2", "StartTime": 1561574108.512, "ServiceNamespace": "dynamodb", "Cause": "scheduled action name my-first-scheduled-action was triggered", "StatusMessage": "Successfully set min capacity to 15 and max capacity to 20", "StatusCode": "Successful" } ] }`For more information, see [Scaling activities for Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scaling-activities.html)in the*Application Auto Scaling User Guide*.- 
                    For API details, see [DescribeScalingActivities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/describe-scaling-activities.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-scaling-policies`.

- **AWS CLI**
- 
            
                    **To describe scaling policies**This example command describes the scaling policies for the ecs service namespace. Command: `aws application-autoscaling describe-scaling-policies --service-namespace``ecs`Output: `{ "ScalingPolicies": [ { "PolicyName": "web-app-cpu-gt-75", "ScalableDimension": "ecs:service:DesiredCount", "ResourceId": "service/default/web-app", "CreationTime": 1462561899.23, "StepScalingPolicyConfiguration": { "Cooldown": 60, "StepAdjustments": [ { "ScalingAdjustment": 200, "MetricIntervalLowerBound": 0.0 } ], "AdjustmentType": "PercentChangeInCapacity" }, "PolicyARN": "arn:aws:autoscaling:us-west-2:012345678910:scalingPolicy:6d8972f3-efc8-437c-92d1-6270f29a66e7:resource/ecs/service/default/web-app:policyName/web-app-cpu-gt-75", "PolicyType": "StepScaling", "Alarms": [ { "AlarmName": "web-app-cpu-gt-75", "AlarmARN": "arn:aws:cloudwatch:us-west-2:012345678910:alarm:web-app-cpu-gt-75" } ], "ServiceNamespace": "ecs" }, { "PolicyName": "web-app-cpu-lt-25", "ScalableDimension": "ecs:service:DesiredCount", "ResourceId": "service/default/web-app", "CreationTime": 1462562575.099, "StepScalingPolicyConfiguration": { "Cooldown": 1, "StepAdjustments": [ { "ScalingAdjustment": -50, "MetricIntervalUpperBound": 0.0 } ], "AdjustmentType": "PercentChangeInCapacity" }, "PolicyARN": "arn:aws:autoscaling:us-west-2:012345678910:scalingPolicy:6d8972f3-efc8-437c-92d1-6270f29a66e7:resource/ecs/service/default/web-app:policyName/web-app-cpu-lt-25", "PolicyType": "StepScaling", "Alarms": [ { "AlarmName": "web-app-cpu-lt-25", "AlarmARN": "arn:aws:cloudwatch:us-west-2:012345678910:alarm:web-app-cpu-lt-25" } ], "ServiceNamespace": "ecs" } ] }`- 
                    For API details, see [DescribeScalingPolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/describe-scaling-policies.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-scheduled-actions`.

- **AWS CLI**
- 
            
                    **To describe scheduled actions**The following `describe-scheduled-actions`example displays details for the scheduled actions for the specified service namespace:`aws application-autoscaling describe-scheduled-actions \ --service-namespace``dynamodb`Output: `{ "ScheduledActions": [ { "ScalableDimension": "dynamodb:table:WriteCapacityUnits", "Schedule": "at(2019-05-20T18:35:00)", "ResourceId": "table/my-table", "CreationTime": 1561571888.361, "ScheduledActionARN": "arn:aws:autoscaling:us-west-2:123456789012:scheduledAction:2d36aa3b-cdf9-4565-b290-81db519b227d:resource/dynamodb/table/my-table:scheduledActionName/my-first-scheduled-action", "ScalableTargetAction": { "MinCapacity": 15, "MaxCapacity": 20 }, "ScheduledActionName": "my-first-scheduled-action", "ServiceNamespace": "dynamodb" }, { "ScalableDimension": "dynamodb:table:WriteCapacityUnits", "Schedule": "at(2019-05-20T18:40:00)", "ResourceId": "table/my-table", "CreationTime": 1561571946.021, "ScheduledActionARN": "arn:aws:autoscaling:us-west-2:123456789012:scheduledAction:2d36aa3b-cdf9-4565-b290-81db519b227d:resource/dynamodb/table/my-table:scheduledActionName/my-second-scheduled-action", "ScalableTargetAction": { "MinCapacity": 5, "MaxCapacity": 10 }, "ScheduledActionName": "my-second-scheduled-action", "ServiceNamespace": "dynamodb" } ] }`For more information, see [Scheduled Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.html)in the*Application Auto Scaling User Guide*.- 
                    For API details, see [DescribeScheduledActions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/describe-scheduled-actions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list the tags for a scalable target**The following `list-tags-for-resource`example lists the tag key names and values that are attached to the scalable target specified by its ARN.`aws application-autoscaling list-tags-for-resource \ --resource-arn``arn:aws:application-autoscaling:us-west-2:123456789012:scalable-target/1234abcd56ab78cd901ef1234567890ab123`Output: `{ "Tags": { "environment": "production" } }`For more information, see [Tagging support for Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/resource-tagging-support.html)in the*Application Auto Scaling User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-scaling-policy`.

- **AWS CLI**
- 
            
                    **Example 1: To apply a target tracking scaling policy with a predefined metric specification**The following `put-scaling-policy`example applies a target tracking scaling policy with a predefined metric specification to an Amazon ECS service called web-app in the default cluster. The policy keeps the average CPU utilization of the service at 75 percent, with scale-out and scale-in cooldown periods of 60 seconds. The output contains the ARNs and names of the two CloudWatch alarms created on your behalf.`aws application-autoscaling put-scaling-policy --service-namespace``ecs`\ --scalable-dimension`ecs:service:DesiredCount`\ --resource-id`service/default/web-app`\ --policy-name`cpu75-target-tracking-scaling-policy`--policy-type`TargetTrackingScaling`\ --target-tracking-scaling-policy-configuration`file://config.json`This example assumes that you have a config.json file in the current directory with the following contents: `{ "TargetValue": 75.0, "PredefinedMetricSpecification": { "PredefinedMetricType": "ECSServiceAverageCPUUtilization" }, "ScaleOutCooldown": 60, "ScaleInCooldown": 60 }`Output: `{ "PolicyARN": "arn:aws:autoscaling:us-west-2:012345678910:scalingPolicy:6d8972f3-efc8-437c-92d1-6270f29a66e7:resource/ecs/service/default/web-app:policyName/cpu75-target-tracking-scaling-policy", "Alarms": [ { "AlarmARN": "arn:aws:cloudwatch:us-west-2:012345678910:alarm:TargetTracking-service/default/web-app-AlarmHigh-d4f0770c-b46e-434a-a60f-3b36d653feca", "AlarmName": "TargetTracking-service/default/web-app-AlarmHigh-d4f0770c-b46e-434a-a60f-3b36d653feca" }, { "AlarmARN": "arn:aws:cloudwatch:us-west-2:012345678910:alarm:TargetTracking-service/default/web-app-AlarmLow-1b437334-d19b-4a63-a812-6c67aaf2910d", "AlarmName": "TargetTracking-service/default/web-app-AlarmLow-1b437334-d19b-4a63-a812-6c67aaf2910d" } ] }`**Example 2: To apply a target tracking scaling policy with a customized metric specification**The following `put-scaling-policy`example applies a target tracking scaling policy with a customized metric specification to an Amazon ECS service called web-app in the default cluster. The policy keeps the average utilization of the service at 75 percent, with scale-out and scale-in cooldown periods of 60 seconds. The output contains the ARNs and names of the two CloudWatch alarms created on your behalf.`aws application-autoscaling put-scaling-policy --service-namespace``ecs`\ --scalable-dimension`ecs:service:DesiredCount`\ --resource-id`service/default/web-app`\ --policy-name`cms75-target-tracking-scaling-policy`--policy-type`TargetTrackingScaling`\ --target-tracking-scaling-policy-configuration`file://config.json`This example assumes that you have a config.json file in the current directory with the following contents: `{ "TargetValue":75.0, "CustomizedMetricSpecification":{ "MetricName":"MyUtilizationMetric", "Namespace":"MyNamespace", "Dimensions": [ { "Name":"MyOptionalMetricDimensionName", "Value":"MyOptionalMetricDimensionValue" } ], "Statistic":"Average", "Unit":"Percent" }, "ScaleOutCooldown": 60, "ScaleInCooldown": 60 }`Output: `{ "PolicyARN": "arn:aws:autoscaling:us-west-2:012345678910:scalingPolicy: 8784a896-b2ba-47a1-b08c-27301cc499a1:resource/ecs/service/default/web-app:policyName/cms75-target-tracking-scaling-policy", "Alarms": [ { "AlarmARN": "arn:aws:cloudwatch:us-west-2:012345678910:alarm:TargetTracking-service/default/web-app-AlarmHigh-9bc77b56-0571-4276-ba0f-d4178882e0a0", "AlarmName": "TargetTracking-service/default/web-app-AlarmHigh-9bc77b56-0571-4276-ba0f-d4178882e0a0" }, { "AlarmARN": "arn:aws:cloudwatch:us-west-2:012345678910:alarm:TargetTracking-service/default/web-app-AlarmLow-9b6ad934-6d37-438e-9e05-02836ddcbdc4", "AlarmName": "TargetTracking-service/default/web-app-AlarmLow-9b6ad934-6d37-438e-9e05-02836ddcbdc4" } ] }`**Example 3: To apply a target tracking scaling policy for scale out only**The following `put-scaling-policy`example applies a target tracking scaling policy to an Amazon ECS service called`web-app`in the default cluster. The policy is used to scale out the ECS service when the`RequestCountPerTarget`metric from the Application Load Balancer exceeds the threshold. The output contains the ARN and name of the CloudWatch alarm created on your behalf.`aws application-autoscaling put-scaling-policy \ --service-namespace``ecs`\ --scalable-dimension`ecs:service:DesiredCount`\ --resource-id`service/default/web-app`\ --policy-name`alb-scale-out-target-tracking-scaling-policy`\ --policy-type`TargetTrackingScaling`\ --target-tracking-scaling-policy-configuration`file://config.json`Contents of `config.json`:`{ "TargetValue": 1000.0, "PredefinedMetricSpecification": { "PredefinedMetricType": "ALBRequestCountPerTarget", "ResourceLabel": "app/EC2Co-EcsEl-1TKLTMITMM0EO/f37c06a68c1748aa/targetgroup/EC2Co-Defau-LDNM7Q3ZH1ZN/6d4ea56ca2d6a18d" }, "ScaleOutCooldown": 60, "ScaleInCooldown": 60, "DisableScaleIn": true }`Output: `{ "PolicyARN": "arn:aws:autoscaling:us-west-2:123456789012:scalingPolicy:6d8972f3-efc8-437c-92d1-6270f29a66e7:resource/ecs/service/default/web-app:policyName/alb-scale-out-target-tracking-scaling-policy", "Alarms": [ { "AlarmName": "TargetTracking-service/default/web-app-AlarmHigh-d4f0770c-b46e-434a-a60f-3b36d653feca", "AlarmARN": "arn:aws:cloudwatch:us-west-2:123456789012:alarm:TargetTracking-service/default/web-app-AlarmHigh-d4f0770c-b46e-434a-a60f-3b36d653feca" } ] }`For more information, see [Target Tracking Scaling Policies for Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html)in the*AWS Application Auto Scaling User Guide*.- 
                    For API details, see [PutScalingPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/put-scaling-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-scheduled-action`.

- **AWS CLI**
- 
            
                    **To add a scheduled action to a DynamoDB table**This example adds a scheduled action to a DynamoDB table called TestTable to scale out on a recurring schedule. On the specified schedule (every day at 12:15pm UTC), if the current capacity is below the value specified for MinCapacity, Application Auto Scaling scales out to the value specified by MinCapacity. Command: `aws application-autoscaling put-scheduled-action --service-namespace``dynamodb`--scheduled-action-name`my-recurring-action`--schedule`"cron(15 12 * * ? *)"`--resource-id`table/TestTable`--scalable-dimension`dynamodb:table:WriteCapacityUnits`--scalable-target-action`MinCapacity=6`For more information, see Scheduled Scaling in the *Application Auto Scaling User Guide*.- 
                    For API details, see [PutScheduledAction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/put-scheduled-action.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-scalable-target`.

- **AWS CLI**
- 
            
                    **Example 1: To register an ECS service as a scalable target**The following `register-scalable-target`example registers an Amazon ECS service with Application Auto Scaling. It also adds a tag with the key name`environment`and the value`production`to the scalable target.`aws application-autoscaling register-scalable-target \ --service-namespace``ecs`\ --scalable-dimension`ecs:service:DesiredCount`\ --resource-id`service/default/web-app`\ --min-capacity`1`--max-capacity`10`\ --tags`environment=production`Output: `{ "ScalableTargetARN": "arn:aws:application-autoscaling:us-west-2:123456789012:scalable-target/1234abcd56ab78cd901ef1234567890ab123" }`For examples for other AWS services and custom resources, see the topics in [AWS services that you can use with Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/integrated-services-list.html)in the*Application Auto Scaling User Guide*.**Example 2: To suspend scaling activities for a scalable target**The following `register-scalable-target`example suspends scaling activities for an existing scalable target.`aws application-autoscaling register-scalable-target \ --service-namespace``dynamodb`\ --scalable-dimension`dynamodb:table:ReadCapacityUnits`\ --resource-id`table/my-table`\ --suspended-state`DynamicScalingInSuspended=true,DynamicScalingOutSuspended=true,ScheduledScalingSuspended=true`Output: `{ "ScalableTargetARN": "arn:aws:application-autoscaling:us-west-2:123456789012:scalable-target/1234abcd56ab78cd901ef1234567890ab123" }`For more information, see [Suspending and resuming scaling for Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-suspend-resume-scaling.html)in the*Application Auto Scaling User Guide*.**Example 3: To resume scaling activities for a scalable target**The following `register-scalable-target`example resumes scaling activities for an existing scalable target.`aws application-autoscaling register-scalable-target \ --service-namespace``dynamodb`\ --scalable-dimension`dynamodb:table:ReadCapacityUnits`\ --resource-id`table/my-table`\ --suspended-state`DynamicScalingInSuspended=false,DynamicScalingOutSuspended=false,ScheduledScalingSuspended=false`Output: `{ "ScalableTargetARN": "arn:aws:application-autoscaling:us-west-2:123456789012:scalable-target/1234abcd56ab78cd901ef1234567890ab123" }`For more information, see [Suspending and resuming scaling for Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-suspend-resume-scaling.html)in the*Application Auto Scaling User Guide*.- 
                    For API details, see [RegisterScalableTarget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/register-scalable-target.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add a tag to a scalable target**The following `tag-resource`example adds a tag with the key name`environment`and the value`production`to the scalable target specified by its ARN.`aws application-autoscaling tag-resource \ --resource-arn``arn:aws:application-autoscaling:us-west-2:123456789012:scalable-target/1234abcd56ab78cd901ef1234567890ab123`\ --tags`environment=production`This command produces no output. For more information, see [Tagging support for Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/resource-tagging-support.html)in the*Application Auto Scaling User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove a tag from a scalable target**The following `untag-resource`example removes the tag pair with the key name`environment`from the scalable target specified by its ARN.`aws application-autoscaling untag-resource \ --resource-arn``arn:aws:application-autoscaling:us-west-2:123456789012:scalable-target/1234abcd56ab78cd901ef1234567890ab123`\ --tag-keys`"environment"`This command produces no output. For more information, see [Tagging support for Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/resource-tagging-support.html)in the*Application Auto Scaling User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-autoscaling/untag-resource.html)in*AWS CLI Command Reference*.
 
-