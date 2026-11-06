# Auto Scaling Plans examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_auto-scaling-plans_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_auto-scaling-plans_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Auto Scaling Plans.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-scaling-plan`.

- **AWS CLI**
- 
            
                    **To create a scaling plan**The following `create-scaling-plan`example creates a scaling plan named`my-scaling-plan`using an already-created JSON file (named config.json). The structure of the scaling plan includes a scaling instruction for an Auto Scaling group named`my-asg`. It specifies the`TagFilters`property as the application source and enables predictive scaling and dynamic scaling.`aws autoscaling-plans create-scaling-plan \ --scaling-plan-name``my-scaling-plan`\ --cli-input-json`file://~/config.json`Contents of `config.json`file:`{ "ApplicationSource": { "TagFilters": [ { "Key": "purpose", "Values": [ "my-application" ] } ] }, "ScalingInstructions": [ { "ServiceNamespace": "autoscaling", "ResourceId": "autoScalingGroup/my-asg", "ScalableDimension": "autoscaling:autoScalingGroup:DesiredCapacity", "ScheduledActionBufferTime": 300, "PredictiveScalingMaxCapacityBehavior": "SetForecastCapacityToMaxCapacity", "PredictiveScalingMode": "ForecastAndScale", "PredefinedLoadMetricSpecification": { "PredefinedLoadMetricType": "ASGTotalCPUUtilization" }, "ScalingPolicyUpdateBehavior": "ReplaceExternalPolicies", "MinCapacity": 1, "MaxCapacity": 4, "TargetTrackingConfigurations": [ { "PredefinedScalingMetricSpecification": { "PredefinedScalingMetricType": "ASGAverageCPUUtilization" }, "TargetValue": 50 } ] } ] }`Output: `{ "ScalingPlanVersion": 1 }`For more information, see the [AWS Auto Scaling User Guide](https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-aws-auto-scaling.html).- 
                    For API details, see [CreateScalingPlan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling-plans/create-scaling-plan.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-scaling-plan`.

- **AWS CLI**
- 
            
                    **To delete a scaling plan**The following `delete-scaling-plan`example deletes the specified scaling plan.`aws autoscaling-plans delete-scaling-plan \ --scaling-plan-name``my-scaling-plan`\ --scaling-plan-version`1`This command produces no output. For more information, see the [AWS Auto Scaling User Guide](https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-aws-auto-scaling.html).- 
                    For API details, see [DeleteScalingPlan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling-plans/delete-scaling-plan.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-scaling-plan-resources`.

- **AWS CLI**
- 
            
                    **To describe the scalable resources for a scaling plan**The following `describe-scaling-plan-resources`example displays details about the single scalable resource (an Auto Scaling group) that is associated with the specified scaling plan.`aws autoscaling-plans describe-scaling-plan-resources \ --scaling-plan-name``my-scaling-plan`\ --scaling-plan-version`1`Output: `{ "ScalingPlanResources": [ { "ScalableDimension": "autoscaling:autoScalingGroup:DesiredCapacity", "ScalingPlanVersion": 1, "ResourceId": "autoScalingGroup/my-asg", "ScalingStatusCode": "Active", "ScalingStatusMessage": "Target tracking scaling policies have been applied to the resource.", "ScalingPolicies": [ { "PolicyName": "AutoScaling-my-asg-b1ab65ae-4be3-4634-bd64-c7471662b251", "PolicyType": "TargetTrackingScaling", "TargetTrackingConfiguration": { "PredefinedScalingMetricSpecification": { "PredefinedScalingMetricType": "ALBRequestCountPerTarget", "ResourceLabel": "app/my-alb/f37c06a68c1748aa/targetgroup/my-target-group/6d4ea56ca2d6a18d" }, "TargetValue": 40.0 } } ], "ServiceNamespace": "autoscaling", "ScalingPlanName": "my-scaling-plan" } ] }`For more information, see [What Is AWS Auto Scaling?](https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-aws-auto-scaling.html)in the*AWS Auto Scaling User Guide*.- 
                    For API details, see [DescribeScalingPlanResources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling-plans/describe-scaling-plan-resources.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-scaling-plans`.

- **AWS CLI**
- 
            
                    **To describe a scaling plan**The following `describe-scaling-plans`example displays the details of the specified scaling plan.`aws autoscaling-plans describe-scaling-plans \ --scaling-plan-names``scaling-plan-with-asg-and-ddb`Output: `{ "ScalingPlans": [ { "LastMutatingRequestTime": 1565388443.963, "ScalingPlanVersion": 1, "CreationTime": 1565388443.963, "ScalingInstructions": [ { "ScalingPolicyUpdateBehavior": "ReplaceExternalPolicies", "ScalableDimension": "autoscaling:autoScalingGroup:DesiredCapacity", "TargetTrackingConfigurations": [ { "PredefinedScalingMetricSpecification": { "PredefinedScalingMetricType": "ASGAverageCPUUtilization" }, "TargetValue": 50.0, "EstimatedInstanceWarmup": 300, "DisableScaleIn": false } ], "ResourceId": "autoScalingGroup/my-asg", "DisableDynamicScaling": false, "MinCapacity": 1, "ServiceNamespace": "autoscaling", "MaxCapacity": 10 }, { "ScalingPolicyUpdateBehavior": "ReplaceExternalPolicies", "ScalableDimension": "dynamodb:table:ReadCapacityUnits", "TargetTrackingConfigurations": [ { "PredefinedScalingMetricSpecification": { "PredefinedScalingMetricType": "DynamoDBReadCapacityUtilization" }, "TargetValue": 50.0, "ScaleInCooldown": 60, "DisableScaleIn": false, "ScaleOutCooldown": 60 } ], "ResourceId": "table/my-table", "DisableDynamicScaling": false, "MinCapacity": 5, "ServiceNamespace": "dynamodb", "MaxCapacity": 10000 }, { "ScalingPolicyUpdateBehavior": "ReplaceExternalPolicies", "ScalableDimension": "dynamodb:table:WriteCapacityUnits", "TargetTrackingConfigurations": [ { "PredefinedScalingMetricSpecification": { "PredefinedScalingMetricType": "DynamoDBWriteCapacityUtilization" }, "TargetValue": 50.0, "ScaleInCooldown": 60, "DisableScaleIn": false, "ScaleOutCooldown": 60 } ], "ResourceId": "table/my-table", "DisableDynamicScaling": false, "MinCapacity": 5, "ServiceNamespace": "dynamodb", "MaxCapacity": 10000 } ], "ApplicationSource": { "TagFilters": [ { "Values": [ "my-application-id" ], "Key": "application" } ] }, "StatusStartTime": 1565388455.836, "ScalingPlanName": "scaling-plan-with-asg-and-ddb", "StatusMessage": "Scaling plan has been created and applied to all resources.", "StatusCode": "Active" } ] }`For more information, see [What Is AWS Auto Scaling?](https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-aws-auto-scaling.html)in the*AWS Auto Scaling User Guide*.- 
                    For API details, see [DescribeScalingPlans](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling-plans/describe-scaling-plans.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-scaling-plan-resource-forecast-data`.

- **AWS CLI**
- 
            
                    **To retrieve load forecast data**This example retrieves load forecast data for a scalable resource (an Auto Scaling group) that is associated with the specified scaling plan. `aws autoscaling-plans get-scaling-plan-resource-forecast-data \ --scaling-plan-name``my-scaling-plan`\ --scaling-plan-version`1`\ --service-namespace`"autoscaling"`\ --resource-id`autoScalingGroup/my-asg`\ --scalable-dimension`"autoscaling:autoScalingGroup:DesiredCapacity"`\ --forecast-data-type`"LoadForecast"`\ --start-time`"2019-08-30T00:00:00Z"`\ --end-time`"2019-09-06T00:00:00Z"`Output: `{ "Datapoints": [...] }`For more information, see [What Is AWS Auto Scaling](https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-aws-auto-scaling.html)in the*AWS Auto Scaling User Guide*.- 
                    For API details, see [GetScalingPlanResourceForecastData](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling-plans/get-scaling-plan-resource-forecast-data.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-scaling-plan`.

- **AWS CLI**
- 
            
                    **To update a scaling plan**The following `update-scaling-plan`example modifies the scaling metric for an Auto Scaling group in the specified scaling plan.`aws autoscaling-plans update-scaling-plan \ --scaling-plan-name``my-scaling-plan`\ --scaling-plan-version`1`\ --scaling-instructions '`{"ScalableDimension":"autoscaling:autoScalingGroup:DesiredCapacity","ResourceId":"autoScalingGroup/my-asg","ServiceNamespace":"autoscaling","TargetTrackingConfigurations":[{"PredefinedScalingMetricSpecification": {"PredefinedScalingMetricType":"ALBRequestCountPerTarget","ResourceLabel":"app/my-alb/f37c06a68c1748aa/targetgroup/my-target-group/6d4ea56ca2d6a18d"},"TargetValue":40.0}],"MinCapacity": 1,"MaxCapacity": 10}`'This command produces no output. For more information, see [What Is AWS Auto Scaling?](https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-aws-auto-scaling.html)in the*AWS Auto Scaling User Guide*.- 
                    For API details, see [UpdateScalingPlan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling-plans/update-scaling-plan.html)in*AWS CLI Command Reference*.
 
-