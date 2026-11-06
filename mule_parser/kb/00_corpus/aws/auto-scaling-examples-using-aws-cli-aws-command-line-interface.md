# Auto Scaling examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_auto-scaling_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_auto-scaling_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Auto Scaling.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `attach-instances`.

- **AWS CLI**
- 
            
                    **To attach an instance to an Auto Scaling group**This example attaches the specified instance to the specified Auto Scaling group. `aws autoscaling attach-instances \ --instance-ids``i-061c63c5eb45f0416`\ --auto-scaling-group-name`my-asg`This command produces no output. - 
                    For API details, see [AttachInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/attach-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `attach-load-balancer-target-groups`.

- **AWS CLI**
- 
            
                    **To attach a target group to an Auto Scaling group**This example attaches the specified target group to the specified Auto Scaling group. `aws autoscaling attach-load-balancer-target-groups \ --auto-scaling-group-name``my-asg`\ --target-group-arns`arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067`This command produces no output. For more information, see [Elastic Load Balancing and Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [AttachLoadBalancerTargetGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/attach-load-balancer-target-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `attach-load-balancers`.

- **AWS CLI**
- 
            
                    **To attach a Classic Load Balancer to an Auto Scaling group**This example attaches the specified Classic Load Balancer to the specified Auto Scaling group. `aws autoscaling attach-load-balancers \ --load-balancer-names``my-load-balancer`\ --auto-scaling-group-name`my-asg`This command produces no output. For more information, see [Elastic Load Balancing and Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [AttachLoadBalancers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/attach-load-balancers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-instance-refresh`.

- **AWS CLI**
- 
            
                    **To cancel an instance refresh**The following `cancel-instance-refresh`example cancels an in-progress instance refresh for the specified Auto Scaling group.`aws autoscaling cancel-instance-refresh \ --auto-scaling-group-name``my-asg`Output: `{ "InstanceRefreshId": "08b91cf7-8fa6-48af-b6a6-d227f40f1b9b" }`For more information, see [Cancel an instance refresh](https://docs.aws.amazon.com/autoscaling/ec2/userguide/cancel-instance-refresh.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [CancelInstanceRefresh](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/cancel-instance-refresh.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `complete-lifecycle-action`.

- **AWS CLI**
- 
            
                    **To complete the lifecycle action**This example notifies Amazon EC2 Auto Scaling that the specified lifecycle action is complete so that it can finish launching or terminating the instance. `aws autoscaling complete-lifecycle-action \ --lifecycle-hook-name``my-launch-hook`\ --auto-scaling-group-name`my-asg`\ --lifecycle-action-result`CONTINUE`\ --lifecycle-action-token`bcd2f1b8-9a78-44d3-8a7a-4dd07d7cf635`This command produces no output. For more information, see [Amazon EC2 Auto Scaling lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [CompleteLifecycleAction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/complete-lifecycle-action.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-auto-scaling-group`.

- **AWS CLI**
- 
            
                    **Example 1: To create an Auto Scaling group**The following `create-auto-scaling-group`example creates an Auto Scaling group in subnets in multiple Availability Zones within a Region. The instances launch with the default version of the specified launch template. Note that defaults are used for most other settings, such as the termination policies and health check configuration.`aws autoscaling create-auto-scaling-group \ --auto-scaling-group-name``my-asg`\ --launch-template`LaunchTemplateId=lt-1234567890abcde12`\ --min-size`1`\ --max-size`5`\ --vpc-zone-identifier`"subnet-5ea0c127,subnet-6194ea3b,subnet-c934b782"`This command produces no output. For more information, see [Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 2: To attach an Application Load Balancer, Network Load Balancer, or Gateway Load Balancer**This example specifies the ARN of a target group for a load balancer that supports the expected traffic. The health check type specifies `ELB`so that when Elastic Load Balancing reports an instance as unhealthy, the Auto Scaling group replaces it. The command also defines a health check grace period of`600`seconds. The grace period helps prevent premature termination of newly launched instances.`aws autoscaling create-auto-scaling-group \ --auto-scaling-group-name``my-asg`\ --launch-template`LaunchTemplateId=lt-1234567890abcde12`\ --target-group-arns`arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/943f017f100becff`\ --health-check-type`ELB`\ --health-check-grace-period`600`\ --min-size`1`\ --max-size`5`\ --vpc-zone-identifier`"subnet-5ea0c127,subnet-6194ea3b,subnet-c934b782"`This command produces no output. For more information, see [Elastic Load Balancing and Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 3: To specify a placement group and use the latest version of the launch template**This example launches instances into a placement group within a single Availability Zone. This can be useful for low-latency groups with HPC workloads. This example also specifies the minimum size, maximum size, and desired capacity of the group. `aws autoscaling create-auto-scaling-group \ --auto-scaling-group-name``my-asg`\ --launch-template LaunchTemplateId=lt-`1`234`5`67890abcde12,Version='$Latest' \ --min-size 1 \ --max-size 5 \ --desired-capacity`3`\ --placement-group`my-placement-group`\ --vpc-zone-identifier`"subnet-6194ea3b"`This command produces no output. For more information, see [Placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html)in the*Amazon EC2 User Guide for Linux Instances*.**Example 4: To specify a single instance Auto Scaling group and use a specific version of the launch template**This example creates an Auto Scaling group with minimum and maximum capacity set to `1`to enforce that one instance will be running. The command also specifies v1 of a launch template in which the ID of an existing ENI is specified. When you use a launch template that specifies an existing ENI for eth0, you must specify an Availability Zone for the Auto Scaling group that matches the network interface, without also specifying a subnet ID in the request.`aws autoscaling create-auto-scaling-group \ --auto-scaling-group-name``my-asg-single-instance`\ --launch-template LaunchTemplateName=my-template-for-auto-scaling,Version='`1`' \ --min-size`1`\ --max-size 1 \ --availability-zones`us-west-2a`This command produces no output. For more information, see [Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 5: To specify a different termination policy**This example creates an Auto Scaling group using a launch configuration and sets the termination policy to terminate the oldest instances first. The command also applies a tag to the group and its instances, with a key of `Role`and a value of`WebServer`.`aws autoscaling create-auto-scaling-group \ --auto-scaling-group-name``my-asg`\ --launch-configuration-name`my-lc`\ --min-size`1`\ --max-size`5`\ --termination-policies`"OldestInstance"`\ --tags`"ResourceId=my-asg,ResourceType=auto-scaling-group,Key=Role,Value=WebServer,PropagateAtLaunch=true"`\ --vpc-zone-identifier`"subnet-5ea0c127,subnet-6194ea3b,subnet-c934b782"`This command produces no output. For more information, see [Working with Amazon EC2 Auto Scaling termination policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-termination-policies.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 6: To specify a launch lifecycle hook**This example creates an Auto Scaling group with a lifecycle hook that supports a custom action at instance launch. `aws autoscaling create-auto-scaling-group \ --cli-input-json``file://~/config.json`Contents of `config.json`file:`{ "AutoScalingGroupName": "my-asg", "LaunchTemplate": { "LaunchTemplateId": "lt-1234567890abcde12" }, "LifecycleHookSpecificationList": [{ "LifecycleHookName": "my-launch-hook", "LifecycleTransition": "autoscaling:EC2_INSTANCE_LAUNCHING", "NotificationTargetARN": "arn:aws:sqs:us-west-2:123456789012:my-sqs-queue", "RoleARN": "arn:aws:iam::123456789012:role/my-notification-role", "NotificationMetadata": "SQS message metadata", "HeartbeatTimeout": 4800, "DefaultResult": "ABANDON" }], "MinSize": 1, "MaxSize": 5, "VPCZoneIdentifier": "subnet-5ea0c127,subnet-6194ea3b,subnet-c934b782", "Tags": [{ "ResourceType": "auto-scaling-group", "ResourceId": "my-asg", "PropagateAtLaunch": true, "Value": "test", "Key": "environment" }] }`This command produces no output. For more information, see [Amazon EC2 Auto Scaling lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 7: To specify a termination lifecycle hook**This example creates an Auto Scaling group with a lifecycle hook that supports a custom action at instance termination. `aws autoscaling create-auto-scaling-group \ --cli-input-json``file://~/config.json`Contents of `config.json`:`{ "AutoScalingGroupName": "my-asg", "LaunchTemplate": { "LaunchTemplateId": "lt-1234567890abcde12" }, "LifecycleHookSpecificationList": [{ "LifecycleHookName": "my-termination-hook", "LifecycleTransition": "autoscaling:EC2_INSTANCE_TERMINATING", "HeartbeatTimeout": 120, "DefaultResult": "CONTINUE" }], "MinSize": 1, "MaxSize": 5, "TargetGroupARNs": [ "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067" ], "VPCZoneIdentifier": "subnet-5ea0c127,subnet-6194ea3b,subnet-c934b782" }`This command produces no output. For more information, see [Amazon EC2 Auto Scaling lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 8: To specify a custom termination policy**This example creates an Auto Scaling group that specifies a custom Lambda function termination policy that tells Amazon EC2 Auto Scaling which instances are safe to terminate on scale in. `aws autoscaling create-auto-scaling-group \ --auto-scaling-group-name``my-asg-single-instance`\ --launch-template`LaunchTemplateName=my-template-for-auto-scaling`\ --min-size`1`\ --max-size`5`\ --termination-policies`"arn:aws:lambda:us-west-2:123456789012:function:HelloFunction:prod"`\ --vpc-zone-identifier`"subnet-5ea0c127,subnet-6194ea3b,subnet-c934b782"`This command produces no output. For more information, see [Creating a custom termination policy with Lambda](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lambda-custom-termination-policy.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [CreateAutoScalingGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-launch-configuration`.

- **AWS CLI**
- 
            
                    **Example 1: To create a launch configuration**This example creates a simple launch configuration. `aws autoscaling create-launch-configuration \ --launch-configuration-name``my-lc`\ --image-id`ami-04d5cc9b88example`\ --instance-type`m5.large`This command produces no output. For more information, see [Creating a launch configuration](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-config.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 2: To create a launch configuration with a security group, key pair, and bootstrapping script**This example creates a launch configuration with a security group, a key pair, and a bootstrapping script contained in the user data. `aws autoscaling create-launch-configuration \ --launch-configuration-name``my-lc`\ --image-id`ami-04d5cc9b88example`\ --instance-type`m5.large`\ --security-groups`sg-eb2af88example`\ --key-name`my-key-pair`\ --user-data`file://myuserdata.txt`This command produces no output. For more information, see [Creating a launch configuration](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-config.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 3: To create a launch configuration with an IAM role**This example creates a launch configuration with the instance profile name of an IAM role. `aws autoscaling create-launch-configuration \ --launch-configuration-name``my-lc`\ --image-id`ami-04d5cc9b88example`\ --instance-type`m5.large`\ --iam-instance-profile`my-autoscaling-role`This command produces no output. For more information, see [IAM role for applications that run on Amazon EC2 instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/us-iam-role.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 4: To create a launch configuration with detailed monitoring enabled**This example creates a launch configuration with EC2 detailed monitoring enabled, which sends EC2 metrics to CloudWatch in 1-minute periods. `aws autoscaling create-launch-configuration \ --launch-configuration-name``my-lc`\ --image-id`ami-04d5cc9b88example`\ --instance-type`m5.large`\ --instance-monitoring`Enabled=true`This command produces no output. For more information, see [Configuring monitoring for Auto Scaling instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/enable-as-instance-metrics.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 5: To create a launch configuration that launches Spot Instances**This example creates a launch configuration that uses Spot Instances as the only purchase option. `aws autoscaling create-launch-configuration \ --launch-configuration-name``my-lc`\ --image-id`ami-04d5cc9b88example`\ --instance-type`m5.large`\ --spot-price`"0.50"`This command produces no output. For more information, see [Requesting Spot Instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-launch-spot-instances.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 6: To create a launch configuration using an EC2 instance**This example creates a launch configuration based on the attributes of an existing instance. It overrides the placement tenancy and whether a public IP address is set by including the `--placement-tenancy`and`--no-associate-public-ip-address`options.`aws autoscaling create-launch-configuration \ --launch-configuration-name``my-lc-from-instance`\ --instance-id`i-0123a456700123456`\ --instance-type`m5.large`\ --no-associate-public-ip-address \ --placement-tenancy`dedicated`This command produces no output. For more information, see [Creating a launch configuration using an EC2 instance](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-lc-with-instanceID.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 7: To create a launch configuration with a block device mapping for an Amazon EBS volume**This example creates a launch configuration with a block device mapping for an Amazon EBS `gp3`volume with the device name`/dev/sdh`and a volume size of 20.`aws autoscaling create-launch-configuration \ --launch-configuration-name``my-lc`\ --image-id`ami-04d5cc9b88example`\ --instance-type`m5.large`\ --block-device-mappings '`[{"DeviceName":"/dev/sdh","Ebs":{"VolumeSize":20,"VolumeType":"gp3"}}]`'This command produces no output. For more information, see [EBS](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_Ebs.html)in the*Amazon EC2 Auto Scaling API Reference*.For information about the syntax for quoting JSON-formatted parameter values, see [Using quotation marks with strings in the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html)in the*AWS Command Line Interface User Guide*.**Example 8: To create a launch configuration with a block device mapping for an instance store volume**This example creates a launch configuration with `ephemeral1`as an instance store volume with the device name`/dev/sdc`.`aws autoscaling create-launch-configuration \ --launch-configuration-name``my-lc`\ --image-id`ami-04d5cc9b88example`\ --instance-type`m5.large`\ --block-device-mappings '`[{"DeviceName":"/dev/sdc","VirtualName":"ephemeral1"}]`'This command produces no output. For more information, see [BlockDeviceMapping](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_BlockDeviceMapping.html)in the*Amazon EC2 Auto Scaling API Reference*.For information about the syntax for quoting JSON-formatted parameter values, see [Using quotation marks with strings in the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html)in the*AWS Command Line Interface User Guide*.**Example 9: To create a launch configuration and suppress a block device from attaching at launch time**This example creates a launch configuration that suppresses a block device specified by the block device mapping of the AMI (for example, `/dev/sdf`).`aws autoscaling create-launch-configuration \ --launch-configuration-name``my-lc`\ --image-id`ami-04d5cc9b88example`\ --instance-type`m5.large`\ --block-device-mappings '`[{"DeviceName":"/dev/sdf","NoDevice":""}]`'This command produces no output. For more information, see [BlockDeviceMapping](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_BlockDeviceMapping.html)in the*Amazon EC2 Auto Scaling API Reference*.For information about the syntax for quoting JSON-formatted parameter values, see [Using quotation marks with strings in the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html)in the*AWS Command Line Interface User Guide*.- 
                    For API details, see [CreateLaunchConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-launch-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-or-update-tags`.

- **AWS CLI**
- 
            
                    **To create or update tags for an Auto Scaling group**This example adds two tags to the specified Auto Scaling group. `aws autoscaling create-or-update-tags \ --tags``ResourceId=my-asg,ResourceType=auto-scaling-group,Key=Role,Value=WebServer,PropagateAtLaunch=true``ResourceId=my-asg,ResourceType=auto-scaling-group,Key=Dept,Value=Research,PropagateAtLaunch=true`This command produces no output. For more information, see [Tagging Auto Scaling groups and instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-tagging.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [CreateOrUpdateTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-or-update-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-auto-scaling-group`.

- **AWS CLI**
- 
            
                    **Example 1: To delete the specified Auto Scaling group**This example deletes the specified Auto Scaling group. `aws autoscaling delete-auto-scaling-group \ --auto-scaling-group-name``my-asg`This command produces no output. For more information, see [Deleting your Auto Scaling infrastructure](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-process-shutdown.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 2: To force delete the specified Auto Scaling group**To delete the Auto Scaling group without waiting for the instances in the group to terminate, use the `--force-delete`option.`aws autoscaling delete-auto-scaling-group \ --auto-scaling-group-name``my-asg`\ --force-deleteThis command produces no output. For more information, see [Deleting your Auto Scaling infrastructure](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-process-shutdown.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [DeleteAutoScalingGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/delete-auto-scaling-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-launch-configuration`.

- **AWS CLI**
- 
            
                    **To delete a launch configuration**This example deletes the specified launch configuration. `aws autoscaling delete-launch-configuration \ --launch-configuration-name``my-launch-config`This command produces no output. For more information, see [Deleting your Auto Scaling infrastructure](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-process-shutdown.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [DeleteLaunchConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/delete-launch-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-lifecycle-hook`.

- **AWS CLI**
- 
            
                    **To delete a lifecycle hook**This example deletes the specified lifecycle hook. `aws autoscaling delete-lifecycle-hook \ --lifecycle-hook-name``my-lifecycle-hook`\ --auto-scaling-group-name`my-asg`This command produces no output. - 
                    For API details, see [DeleteLifecycleHook](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/delete-lifecycle-hook.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-notification-configuration`.

- **AWS CLI**
- 
            
                    **To delete an Auto Scaling notification**This example deletes the specified notification from the specified Auto Scaling group. `aws autoscaling delete-notification-configuration \ --auto-scaling-group-name``my-asg`\ --topic-arn`arn:aws:sns:us-west-2:123456789012:my-sns-topic`This command produces no output. For more information, see [Delete the notification configuration](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ASGettingNotifications.html#delete-settingupnotifications)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [DeleteNotificationConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/delete-notification-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-policy`.

- **AWS CLI**
- 
            
                    **To delete a scaling policy**This example deletes the specified scaling policy. `aws autoscaling delete-policy \ --auto-scaling-group-name``my-asg`\ --policy-name`alb1000-target-tracking-scaling-policy`This command produces no output. - 
                    For API details, see [DeletePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/delete-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-scheduled-action`.

- **AWS CLI**
- 
            
                    **To delete a scheduled action from an Auto Scaling group**This example deletes the specified scheduled action from the specified Auto Scaling group. `aws autoscaling delete-scheduled-action \ --auto-scaling-group-name``my-asg`\ --scheduled-action-name`my-scheduled-action`This command produces no output. - 
                    For API details, see [DeleteScheduledAction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/delete-scheduled-action.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-tags`.

- **AWS CLI**
- 
            
                    **To delete a tag from an Auto Scaling group**This example deletes the specified tag from the specified Auto Scaling group. `aws autoscaling delete-tags \ --tags``ResourceId=my-asg,ResourceType=auto-scaling-group,Key=Dept,Value=Research`This command produces no output. For more information, see [Tagging Auto Scaling groups and instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-tagging.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [DeleteTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/delete-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-warm-pool`.

- **AWS CLI**
- 
            
                    **Example 1: To delete a warm pool**The following example deletes the warm pool for the specified Auto Scaling group. `aws autoscaling delete-warm-pool \ --auto-scaling-group-name``my-asg`This command produces no output. For more information, see [Warm pools for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 2: To force delete a warm pool**To delete the warm pool without waiting for its instances to terminate, use the `--force-delete`option.`aws autoscaling delete-warm-pool \ --auto-scaling-group-name``my-asg`\ --force-deleteThis command produces no output. For more information, see [Warm pools for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [DeleteWarmPool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/delete-warm-pool.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-account-limits`.

- **AWS CLI**
- 
            
                    **To describe your Amazon EC2 Auto Scaling account limits**This example describes the Amazon EC2 Auto Scaling limits for your AWS account. `aws autoscaling describe-account-limits`Output: `{ "NumberOfLaunchConfigurations": 5, "MaxNumberOfLaunchConfigurations": 100, "NumberOfAutoScalingGroups": 3, "MaxNumberOfAutoScalingGroups": 20 }`For more information, see [Amazon EC2 Auto Scaling service quotas](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-account-limits.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [DescribeAccountLimits](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-account-limits.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-adjustment-types`.

- **AWS CLI**
- 
            
                    **To describe the available scaling adjustment types**This example describes the available adjustment types. `aws autoscaling describe-adjustment-types`Output: `{ "AdjustmentTypes": [ { "AdjustmentType": "ChangeInCapacity" }, { "AdjustmentType": "ExactCapacity" }, { "AdjustmentType": "PercentChangeInCapacity" } ] }`For more information, see [Scaling adjustment types](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html#as-scaling-adjustment)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [DescribeAdjustmentTypes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-adjustment-types.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-auto-scaling-groups`.

- **AWS CLI**
- 
            
                    **Example 1: To describe the specified Auto Scaling group**This example describes the specified Auto Scaling group. `aws autoscaling describe-auto-scaling-groups \ --auto-scaling-group-names``my-asg`Output: `{ "AutoScalingGroups": [ { "AutoScalingGroupName": "my-asg", "AutoScalingGroupARN": "arn:aws:autoscaling:us-west-2:123456789012:autoScalingGroup:930d940e-891e-4781-a11a-7b0acd480f03:autoScalingGroupName/my-asg", "LaunchTemplate": { "LaunchTemplateName": "my-launch-template", "Version": "1", "LaunchTemplateId": "lt-1234567890abcde12" }, "MinSize": 0, "MaxSize": 1, "DesiredCapacity": 1, "DefaultCooldown": 300, "AvailabilityZones": [ "us-west-2a", "us-west-2b", "us-west-2c" ], "LoadBalancerNames": [], "TargetGroupARNs": [], "HealthCheckType": "EC2", "HealthCheckGracePeriod": 0, "Instances": [ { "InstanceId": "i-06905f55584de02da", "InstanceType": "t2.micro", "AvailabilityZone": "us-west-2a", "HealthStatus": "Healthy", "LifecycleState": "InService", "ProtectedFromScaleIn": false, "LaunchTemplate": { "LaunchTemplateName": "my-launch-template", "Version": "1", "LaunchTemplateId": "lt-1234567890abcde12" } } ], "CreatedTime": "2023-10-28T02:39:22.152Z", "SuspendedProcesses": [], "VPCZoneIdentifier": "subnet-5ea0c127,subnet-6194ea3b,subnet-c934b782", "EnabledMetrics": [], "Tags": [], "TerminationPolicies": [ "Default" ], "NewInstancesProtectedFromScaleIn": false, "ServiceLinkedRoleARN":"arn", "TrafficSources": [] } ] }`**Example 2: To describe the first 100 specified Auto Scaling group**This example describes the specified Auto Scaling groups. It allows you to specify up to 100 group names. `aws autoscaling describe-auto-scaling-groups \ --max-items``100`\ --auto-scaling-group-names`"group1"``"group2"``"group3"``"group4"`See example 1 for sample output. **Example 3: To describe an Auto Scaling group in the specified region**This example describes the Auto Scaling groups in the specified region, up to a maximum of 75 groups. `aws autoscaling describe-auto-scaling-groups \ --max-items``75`\ --region`us-east-1`See example 1 for sample output. **Example 4: To describe the specified number of Auto Scaling group**To return a specific number of Auto Scaling groups, use the `--max-items`option.`aws autoscaling describe-auto-scaling-groups \ --max-items``1`See example 1 for sample output. If the output includes a `NextToken`field, there are more groups. To get the additional groups, use the value of this field with the`--starting-token`option in a subsequent call as follows.`aws autoscaling describe-auto-scaling-groups \ --starting-token``Z3M3LMPEXAMPLE`See example 1 for sample output. **Example 5: To describe Auto Scaling groups that use launch configurations**This example uses the `--query`option to describe Auto Scaling groups that use launch configurations.`aws autoscaling describe-auto-scaling-groups \ --query '``AutoScalingGroups[?LaunchConfigurationName!=`null`]`'Output: `[ { "AutoScalingGroupName": "my-asg", "AutoScalingGroupARN": "arn:aws:autoscaling:us-west-2:123456789012:autoScalingGroup:930d940e-891e-4781-a11a-7b0acd480f03:autoScalingGroupName/my-asg", "LaunchConfigurationName": "my-lc", "MinSize": 0, "MaxSize": 1, "DesiredCapacity": 1, "DefaultCooldown": 300, "AvailabilityZones": [ "us-west-2a", "us-west-2b", "us-west-2c" ], "LoadBalancerNames": [], "TargetGroupARNs": [], "HealthCheckType": "EC2", "HealthCheckGracePeriod": 0, "Instances": [ { "InstanceId": "i-088c57934a6449037", "InstanceType": "t2.micro", "AvailabilityZone": "us-west-2c", "HealthStatus": "Healthy", "LifecycleState": "InService", "LaunchConfigurationName": "my-lc", "ProtectedFromScaleIn": false } ], "CreatedTime": "2023-10-28T02:39:22.152Z", "SuspendedProcesses": [], "VPCZoneIdentifier": "subnet-5ea0c127,subnet-6194ea3b,subnet-c934b782", "EnabledMetrics": [], "Tags": [], "TerminationPolicies": [ "Default" ], "NewInstancesProtectedFromScaleIn": false, "ServiceLinkedRoleARN":"arn", "TrafficSources": [] } ]`For more information, see [Filter AWS CLI output](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-filter.html)in the*AWS Command Line Interface User Guide*.- 
                    For API details, see [DescribeAutoScalingGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-auto-scaling-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-auto-scaling-instances`.

- **AWS CLI**
- 
            
                    **Example 1: To describe one or more instances**This example describes the specified instance. `aws autoscaling describe-auto-scaling-instances \ --instance-ids``i-06905f55584de02da`Output: `{ "AutoScalingInstances": [ { "InstanceId": "i-06905f55584de02da", "InstanceType": "t2.micro", "AutoScalingGroupName": "my-asg", "AvailabilityZone": "us-west-2b", "LifecycleState": "InService", "HealthStatus": "HEALTHY", "ProtectedFromScaleIn": false, "LaunchTemplate": { "LaunchTemplateId": "lt-1234567890abcde12", "LaunchTemplateName": "my-launch-template", "Version": "1" } } ] }`**Example 2: To describe one or more instances**This example uses the `--max-items`option to specify how many instances to return with this call.`aws autoscaling describe-auto-scaling-instances \ --max-items``1`If the output includes a `NextToken`field, there are more instances. To get the additional instances, use the value of this field with the`--starting-token`option in a subsequent call as follows.`aws autoscaling describe-auto-scaling-instances \ --starting-token``Z3M3LMPEXAMPLE`See example 1 for sample output. **Example 3: To describe instances that use launch configurations**This example uses the `--query`option to describe instances that use launch configurations.`aws autoscaling describe-auto-scaling-instances \ --query '``AutoScalingInstances[?LaunchConfigurationName!=`null`]`'Output: `[ { "InstanceId": "i-088c57934a6449037", "InstanceType": "t2.micro", "AutoScalingGroupName": "my-asg", "AvailabilityZone": "us-west-2c", "LifecycleState": "InService", "HealthStatus": "HEALTHY", "LaunchConfigurationName": "my-lc", "ProtectedFromScaleIn": false } ]`For more information, see [Filter AWS CLI output](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-filter.html)in the*AWS Command Line Interface User Guide*.- 
                    For API details, see [DescribeAutoScalingInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-auto-scaling-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-auto-scaling-notification-types`.

- **AWS CLI**
- 
            
                    **To describe the available notification types**This example describes the available notification types. `aws autoscaling describe-auto-scaling-notification-types`Output: `{ "AutoScalingNotificationTypes": [ "autoscaling:EC2_INSTANCE_LAUNCH", "autoscaling:EC2_INSTANCE_LAUNCH_ERROR", "autoscaling:EC2_INSTANCE_TERMINATE", "autoscaling:EC2_INSTANCE_TERMINATE_ERROR", "autoscaling:TEST_NOTIFICATION" ] }`For more information, see [Getting Amazon SNS notifications when your Auto Scaling group scales](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ASGettingNotifications.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [DescribeAutoScalingNotificationTypes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-auto-scaling-notification-types.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-instance-refreshes`.

- **AWS CLI**
- 
            
                    **To describe instance refreshes**The following `describe-instance-refreshes`example returns a description of all instance refresh requests for the specified Auto Scaling group, including the status message and (if available) the status reason.`aws autoscaling describe-instance-refreshes \ --auto-scaling-group-name``my-asg`Output: `{ "InstanceRefreshes": [ { "InstanceRefreshId": "08b91cf7-8fa6-48af-b6a6-d227f40f1b9b", "AutoScalingGroupName": "my-asg", "Status": "InProgress", "StatusReason": "Waiting for instances to warm up before continuing. For example: 0e69cc3f05f825f4f is warming up.", "EndTime": "2023-03-23T16:42:55Z", "PercentageComplete": 0, "InstancesToUpdate": 0, "Preferences": { "MinHealthyPercentage": 100, "InstanceWarmup": 300, "CheckpointPercentages": [ 50 ], "CheckpointDelay": 3600, "SkipMatching": false, "AutoRollback": true, "ScaleInProtectedInstances": "Ignore", "StandbyInstances": "Ignore" } }, { "InstanceRefreshId": "dd7728d0-5bc4-4575-96a3-1b2c52bf8bb1", "AutoScalingGroupName": "my-asg", "Status": "Successful", "EndTime": "2022-06-02T16:53:37Z", "PercentageComplete": 100, "InstancesToUpdate": 0, "Preferences": { "MinHealthyPercentage": 90, "InstanceWarmup": 300, "SkipMatching": true, "AutoRollback": true, "ScaleInProtectedInstances": "Ignore", "StandbyInstances": "Ignore" } } ] }`For more information, see [Check the status of an instance refresh](https://docs.aws.amazon.com/en_us/autoscaling/ec2/userguide/check-status-instance-refresh.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [DescribeInstanceRefreshes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-instance-refreshes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-launch-configurations`.

- **AWS CLI**
- 
            
                    **Example 1: To describe the specified launch configuration**This example describes the specified launch configuration. `aws autoscaling describe-launch-configurations \ --launch-configuration-names``my-launch-config`Output: `{ "LaunchConfigurations": [ { "LaunchConfigurationName": "my-launch-config", "LaunchConfigurationARN": "arn:aws:autoscaling:us-west-2:123456789012:launchConfiguration:98d3b196-4cf9-4e88-8ca1-8547c24ced8b:launchConfigurationName/my-launch-config", "ImageId": "ami-0528a5175983e7f28", "KeyName": "my-key-pair-uswest2", "SecurityGroups": [ "sg-05eaec502fcdadc2e" ], "ClassicLinkVPCSecurityGroups": [], "UserData": "", "InstanceType": "t2.micro", "KernelId": "", "RamdiskId": "", "BlockDeviceMappings": [ { "DeviceName": "/dev/xvda", "Ebs": { "SnapshotId": "snap-06c1606ba5ca274b1", "VolumeSize": 8, "VolumeType": "gp2", "DeleteOnTermination": true, "Encrypted": false } } ], "InstanceMonitoring": { "Enabled": true }, "CreatedTime": "2020-10-28T02:39:22.321Z", "EbsOptimized": false, "AssociatePublicIpAddress": true, "MetadataOptions": { "HttpTokens": "required", "HttpPutResponseHopLimit": 1, "HttpEndpoint": "disabled" } } ] }`**Example 2: To describe a specified number of launch configurations**To return a specific number of launch configurations, use the `--max-items`option.`aws autoscaling describe-launch-configurations \ --max-items``1`If the output includes a `NextToken`field, there are more launch configurations. To get the additional launch configurations, use the value of this field with the`--starting-token`option in a subsequent call as follows.`aws autoscaling describe-launch-configurations \ --starting-token``Z3M3LMPEXAMPLE`- 
                    For API details, see [DescribeLaunchConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-launch-configurations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-lifecycle-hook-types`.

- **AWS CLI**
- 
            
                    **To describe the available lifecycle hook types**This example describes the available lifecycle hook types. `aws autoscaling describe-lifecycle-hook-types`Output: `{ "LifecycleHookTypes": [ "autoscaling:EC2_INSTANCE_LAUNCHING", "autoscaling:EC2_INSTANCE_TERMINATING" ] }`- 
                    For API details, see [DescribeLifecycleHookTypes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-lifecycle-hook-types.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-lifecycle-hooks`.

- **AWS CLI**
- 
            
                    **To describe your lifecycle hooks**This example describes the lifecycle hooks for the specified Auto Scaling group. `aws autoscaling describe-lifecycle-hooks \ --auto-scaling-group-name``my-asg`Output: `{ "LifecycleHooks": [ { "GlobalTimeout": 3000, "HeartbeatTimeout": 30, "AutoScalingGroupName": "my-asg", "LifecycleHookName": "my-launch-hook", "DefaultResult": "ABANDON", "LifecycleTransition": "autoscaling:EC2_INSTANCE_LAUNCHING" }, { "GlobalTimeout": 6000, "HeartbeatTimeout": 60, "AutoScalingGroupName": "my-asg", "LifecycleHookName": "my-termination-hook", "DefaultResult": "CONTINUE", "LifecycleTransition": "autoscaling:EC2_INSTANCE_TERMINATING" } ] }`- 
                    For API details, see [DescribeLifecycleHooks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-lifecycle-hooks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-load-balancer-target-groups`.

- **AWS CLI**
- 
            
                    **To describe the load balancer target groups for an Auto Scaling group**This example describes the load balancer target groups attached to the specified Auto Scaling group. `aws autoscaling describe-load-balancer-target-groups \ --auto-scaling-group-name``my-asg`Output: `{ "LoadBalancerTargetGroups": [ { "LoadBalancerTargetGroupARN": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067", "State": "Added" } ] }`- 
                    For API details, see [DescribeLoadBalancerTargetGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-load-balancer-target-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-load-balancers`.

- **AWS CLI**
- 
            
                    **To describe the Classic Load Balancers for an Auto Scaling group**This example describes the Classic Load Balancers for the specified Auto Scaling group. `aws autoscaling describe-load-balancers \ --auto-scaling-group-name``my-asg`Output: `{ "LoadBalancers": [ { "State": "Added", "LoadBalancerName": "my-load-balancer" } ] }`- 
                    For API details, see [DescribeLoadBalancers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-load-balancers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-metric-collection-types`.

- **AWS CLI**
- 
            
                    **To describe the available metric collection types**This example describes the available metric collection types. `aws autoscaling describe-metric-collection-types`Output: `{ "Metrics": [ { "Metric": "GroupMinSize" }, { "Metric": "GroupMaxSize" }, { "Metric": "GroupDesiredCapacity" }, { "Metric": "GroupInServiceInstances" }, { "Metric": "GroupInServiceCapacity" }, { "Metric": "GroupPendingInstances" }, { "Metric": "GroupPendingCapacity" }, { "Metric": "GroupTerminatingInstances" }, { "Metric": "GroupTerminatingCapacity" }, { "Metric": "GroupStandbyInstances" }, { "Metric": "GroupStandbyCapacity" }, { "Metric": "GroupTotalInstances" }, { "Metric": "GroupTotalCapacity" } ], "Granularities": [ { "Granularity": "1Minute" } ] }`For more information, see [Auto Scaling group metrics](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-monitoring.html#as-group-metrics)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [DescribeMetricCollectionTypes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-metric-collection-types.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-notification-configurations`.

- **AWS CLI**
- 
            
                    **Example 1: To describe the notification configurations of a specified group**This example describes the notification configurations for the specified Auto Scaling group. `aws autoscaling describe-notification-configurations \ --auto-scaling-group-name``my-asg`Output: `{ "NotificationConfigurations": [ { "AutoScalingGroupName": "my-asg", "NotificationType": "autoscaling:TEST_NOTIFICATION", "TopicARN": "arn:aws:sns:us-west-2:123456789012:my-sns-topic-2" }, { "AutoScalingGroupName": "my-asg", "NotificationType": "autoscaling:TEST_NOTIFICATION", "TopicARN": "arn:aws:sns:us-west-2:123456789012:my-sns-topic" } ] }`For more information, see [Getting Amazon SNS notifications when your Auto Scaling group scales](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ASGettingNotifications.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 1: To describe a specified number of notification configurations**To return a specific number of notification configurations, use the `max-items`parameter.`aws autoscaling describe-notification-configurations \ --auto-scaling-group-name``my-auto-scaling-group`\ --max-items`1`Output: `{ "NotificationConfigurations": [ { "AutoScalingGroupName": "my-asg", "NotificationType": "autoscaling:TEST_NOTIFICATION", "TopicARN": "arn:aws:sns:us-west-2:123456789012:my-sns-topic-2" }, { "AutoScalingGroupName": "my-asg", "NotificationType": "autoscaling:TEST_NOTIFICATION", "TopicARN": "arn:aws:sns:us-west-2:123456789012:my-sns-topic" } ] }`If the output includes a `NextToken`field, there are more notification configurations. To get the additional notification configurations, use the value of this field with the`starting-token`parameter in a subsequent call as follows.`aws autoscaling describe-notification-configurations \ --auto-scaling-group-name``my-asg`\ --starting-token`Z3M3LMPEXAMPLE`For more information, see [Getting Amazon SNS notifications when your Auto Scaling group scales](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ASGettingNotifications.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [DescribeNotificationConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-notification-configurations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-policies`.

- **AWS CLI**
- 
            
                    **Example 1: To describe the scaling policies of a specified group**This example describes the scaling policies for the specified Auto Scaling group. `aws autoscaling describe-policies \ --auto-scaling-group-name``my-asg`Output: `{ "ScalingPolicies": [ { "AutoScalingGroupName": "my-asg", "PolicyName": "alb1000-target-tracking-scaling-policy", "PolicyARN": "arn:aws:autoscaling:us-west-2:123456789012:scalingPolicy:3065d9c8-9969-4bec-bb6a-3fbe5550fde6:autoScalingGroupName/my-asg:policyName/alb1000-target-tracking-scaling-policy", "PolicyType": "TargetTrackingScaling", "StepAdjustments": [], "Alarms": [ { "AlarmName": "TargetTracking-my-asg-AlarmHigh-924887a9-12d7-4e01-8686-6f844d13a196", "AlarmARN": "arn:aws:cloudwatch:us-west-2:123456789012:alarm:TargetTracking-my-asg-AlarmHigh-924887a9-12d7-4e01-8686-6f844d13a196" }, { "AlarmName": "TargetTracking-my-asg-AlarmLow-f96f899d-b8e7-4d09-a010-c1aaa35da296", "AlarmARN": "arn:aws:cloudwatch:us-west-2:123456789012:alarm:TargetTracking-my-asg-AlarmLow-f96f899d-b8e7-4d09-a010-c1aaa35da296" } ], "TargetTrackingConfiguration": { "PredefinedMetricSpecification": { "PredefinedMetricType": "ALBRequestCountPerTarget", "ResourceLabel": "app/my-alb/778d41231b141a0f/targetgroup/my-alb-target-group/943f017f100becff" }, "TargetValue": 1000.0, "DisableScaleIn": false }, "Enabled": true }, { "AutoScalingGroupName": "my-asg", "PolicyName": "cpu40-target-tracking-scaling-policy", "PolicyARN": "arn:aws:autoscaling:us-west-2:123456789012:scalingPolicy:5fd26f71-39d4-4690-82a9-b8515c45cdde:autoScalingGroupName/my-asg:policyName/cpu40-target-tracking-scaling-policy", "PolicyType": "TargetTrackingScaling", "StepAdjustments": [], "Alarms": [ { "AlarmName": "TargetTracking-my-asg-AlarmHigh-139f9789-37b9-42ad-bea5-b5b147d7f473", "AlarmARN": "arn:aws:cloudwatch:us-west-2:123456789012:alarm:TargetTracking-my-asg-AlarmHigh-139f9789-37b9-42ad-bea5-b5b147d7f473" }, { "AlarmName": "TargetTracking-my-asg-AlarmLow-bd681c67-fc18-4c56-8468-fb8e413009c9", "AlarmARN": "arn:aws:cloudwatch:us-west-2:123456789012:alarm:TargetTracking-my-asg-AlarmLow-bd681c67-fc18-4c56-8468-fb8e413009c9" } ], "TargetTrackingConfiguration": { "PredefinedMetricSpecification": { "PredefinedMetricType": "ASGAverageCPUUtilization" }, "TargetValue": 40.0, "DisableScaleIn": false }, "Enabled": true } ] }`For more information, see [Dynamic scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 2: To describe the scaling policies of a specified name**To return specific scaling policies, use the `--policy-names`option.`aws autoscaling describe-policies \ --auto-scaling-group-name``my-asg`\ --policy-names`cpu40-target-tracking-scaling-policy`See example 1 for sample output. For more information, see [Dynamic scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 3: To describe a number of scaling policies**To return a specific number of policies, use the `--max-items`option.`aws autoscaling describe-policies \ --auto-scaling-group-name``my-asg`\ --max-items`1`See example 1 for sample output. If the output includes a `NextToken`field, use the value of this field with the`--starting-token`option in a subsequent call to get the additional policies.`aws autoscaling describe-policies --auto-scaling-group-name``my-asg`--starting-token`Z3M3LMPEXAMPLE`For more information, see [Dynamic scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [DescribePolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-policies.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-scaling-activities`.

- **AWS CLI**
- 
            
                    **Example 1: To describe scaling activities for the specified group**This example describes the scaling activities for the specified Auto Scaling group. `aws autoscaling describe-scaling-activities \ --auto-scaling-group-name``my-asg`Output: `{ "Activities": [ { "ActivityId": "f9f2d65b-f1f2-43e7-b46d-d86756459699", "Description": "Launching a new EC2 instance: i-0d44425630326060f", "AutoScalingGroupName": "my-asg", "Cause": "At 2020-10-30T19:35:51Z a user request update of AutoScalingGroup constraints to min: 0, max: 16, desired: 16 changing the desired capacity from 0 to 16. At 2020-10-30T19:36:07Z an instance was started in response to a difference between desired and actual capacity, increasing the capacity from 0 to 16.", "StartTime": "2020-10-30T19:36:09.766Z", "EndTime": "2020-10-30T19:36:41Z", "StatusCode": "Successful", "Progress": 100, "Details": "{\"Subnet ID\":\"subnet-5ea0c127\",\"Availability Zone\":\"us-west-2b\"}" } ] }`For more information, see [Verify a scaling activity for an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-verify-scaling-activity.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 2: To describe the scaling activities for a deleted group**To describe scaling activities after the Auto Scaling group has been deleted, add the `--include-deleted-groups`option.`aws autoscaling describe-scaling-activities \ --auto-scaling-group-name``my-asg`\ --include-deleted-groupsOutput: `{ "Activities": [ { "ActivityId": "e1f5de0e-f93e-1417-34ac-092a76fba220", "Description": "Launching a new EC2 instance. Status Reason: Your Spot request price of 0.001 is lower than the minimum required Spot request fulfillment price of 0.0031. Launching EC2 instance failed.", "AutoScalingGroupName": "my-asg", "Cause": "At 2021-01-13T20:47:24Z a user request update of AutoScalingGroup constraints to min: 1, max: 5, desired: 3 changing the desired capacity from 0 to 3. At 2021-01-13T20:47:27Z an instance was started in response to a difference between desired and actual capacity, increasing the capacity from 0 to 3.", "StartTime": "2021-01-13T20:47:30.094Z", "EndTime": "2021-01-13T20:47:30Z", "StatusCode": "Failed", "StatusMessage": "Your Spot request price of 0.001 is lower than the minimum required Spot request fulfillment price of 0.0031. Launching EC2 instance failed.", "Progress": 100, "Details": "{\"Subnet ID\":\"subnet-5ea0c127\",\"Availability Zone\":\"us-west-2b\"}", "AutoScalingGroupState": "Deleted", "AutoScalingGroupARN": "arn:aws:autoscaling:us-west-2:123456789012:autoScalingGroup:283179a2-f3ce-423d-93f6-66bb518232f7:autoScalingGroupName/my-asg" } ] }`For more information, see [Troubleshoot Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/CHAP_Troubleshooting.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 3: To describe a specified number of scaling activities**To return a specific number of activities, use the `--max-items`option.`aws autoscaling describe-scaling-activities \ --max-items``1`Output: `{ "Activities": [ { "ActivityId": "f9f2d65b-f1f2-43e7-b46d-d86756459699", "Description": "Launching a new EC2 instance: i-0d44425630326060f", "AutoScalingGroupName": "my-asg", "Cause": "At 2020-10-30T19:35:51Z a user request update of AutoScalingGroup constraints to min: 0, max: 16, desired: 16 changing the desired capacity from 0 to 16. At 2020-10-30T19:36:07Z an instance was started in response to a difference between desired and actual capacity, increasing the capacity from 0 to 16.", "StartTime": "2020-10-30T19:36:09.766Z", "EndTime": "2020-10-30T19:36:41Z", "StatusCode": "Successful", "Progress": 100, "Details": "{\"Subnet ID\":\"subnet-5ea0c127\",\"Availability Zone\":\"us-west-2b\"}" } ] }`If the output includes a `NextToken`field, there are more activities. To get the additional activities, use the value of this field with the`--starting-token`option in a subsequent call as follows.`aws autoscaling describe-scaling-activities \ --starting-token``Z3M3LMPEXAMPLE`For more information, see [Verify a scaling activity for an Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-verify-scaling-activity.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [DescribeScalingActivities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-scaling-activities.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-scaling-process-types`.

- **AWS CLI**
- 
            
                    **To describe the available process types**This example describes the available process types. `aws autoscaling describe-scaling-process-types`Output: `{ "Processes": [ { "ProcessName": "AZRebalance" }, { "ProcessName": "AddToLoadBalancer" }, { "ProcessName": "AlarmNotification" }, { "ProcessName": "HealthCheck" }, { "ProcessName": "InstanceRefresh" }, { "ProcessName": "Launch" }, { "ProcessName": "ReplaceUnhealthy" }, { "ProcessName": "ScheduledActions" }, { "ProcessName": "Terminate" } ] }`For more information, see [Suspending and resuming scaling processes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [DescribeScalingProcessTypes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-scaling-process-types.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-scheduled-actions`.

- **AWS CLI**
- 
            
                    **Example 1: To describe all scheduled actions**This example describes all your scheduled actions. `aws autoscaling describe-scheduled-actions`Output: `{ "ScheduledUpdateGroupActions": [ { "AutoScalingGroupName": "my-asg", "ScheduledActionName": "my-recurring-action", "Recurrence": "30 0 1 1,6,12 *", "ScheduledActionARN": "arn:aws:autoscaling:us-west-2:123456789012:scheduledUpdateGroupAction:8e86b655-b2e6-4410-8f29-b4f094d6871c:autoScalingGroupName/my-asg:scheduledActionName/my-recurring-action", "StartTime": "2023-12-01T04:00:00Z", "Time": "2023-12-01T04:00:00Z", "MinSize": 1, "MaxSize": 6, "DesiredCapacity": 4, "TimeZone": "America/New_York" } ] }`For more information, see [Scheduled scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 2: To describe scheduled actions for the specified group**To describe the scheduled actions for a specific Auto Scaling group, use the `--auto-scaling-group-name`option.`aws autoscaling describe-scheduled-actions \ --auto-scaling-group-name``my-asg`Output: `{ "ScheduledUpdateGroupActions": [ { "AutoScalingGroupName": "my-asg", "ScheduledActionName": "my-recurring-action", "Recurrence": "30 0 1 1,6,12 *", "ScheduledActionARN": "arn:aws:autoscaling:us-west-2:123456789012:scheduledUpdateGroupAction:8e86b655-b2e6-4410-8f29-b4f094d6871c:autoScalingGroupName/my-asg:scheduledActionName/my-recurring-action", "StartTime": "2023-12-01T04:00:00Z", "Time": "2023-12-01T04:00:00Z", "MinSize": 1, "MaxSize": 6, "DesiredCapacity": 4, "TimeZone": "America/New_York" } ] }`For more information, see [Scheduled scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 3: To describe the specified scheduled action**To describe a specific scheduled action, use the `--scheduled-action-names`option.`aws autoscaling describe-scheduled-actions \ --scheduled-action-names``my-recurring-action`Output: `{ "ScheduledUpdateGroupActions": [ { "AutoScalingGroupName": "my-asg", "ScheduledActionName": "my-recurring-action", "Recurrence": "30 0 1 1,6,12 *", "ScheduledActionARN": "arn:aws:autoscaling:us-west-2:123456789012:scheduledUpdateGroupAction:8e86b655-b2e6-4410-8f29-b4f094d6871c:autoScalingGroupName/my-asg:scheduledActionName/my-recurring-action", "StartTime": "2023-12-01T04:00:00Z", "Time": "2023-12-01T04:00:00Z", "MinSize": 1, "MaxSize": 6, "DesiredCapacity": 4, "TimeZone": "America/New_York" } ] }`For more information, see [Scheduled scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 4: To describe scheduled actions with a specified start time**To describe the scheduled actions that start at a specific time, use the `--start-time`option.`aws autoscaling describe-scheduled-actions \ --start-time``"2023-12-01T04:00:00Z"`Output: `{ "ScheduledUpdateGroupActions": [ { "AutoScalingGroupName": "my-asg", "ScheduledActionName": "my-recurring-action", "Recurrence": "30 0 1 1,6,12 *", "ScheduledActionARN": "arn:aws:autoscaling:us-west-2:123456789012:scheduledUpdateGroupAction:8e86b655-b2e6-4410-8f29-b4f094d6871c:autoScalingGroupName/my-asg:scheduledActionName/my-recurring-action", "StartTime": "2023-12-01T04:00:00Z", "Time": "2023-12-01T04:00:00Z", "MinSize": 1, "MaxSize": 6, "DesiredCapacity": 4, "TimeZone": "America/New_York" } ] }`For more information, see [Scheduled scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 5: To describe scheduled actions that end at a specified time**To describe the scheduled actions that end at a specific time, use the `--end-time`option.`aws autoscaling describe-scheduled-actions \ --end-time``"2023-12-01T04:00:00Z"`Output: `{ "ScheduledUpdateGroupActions": [ { "AutoScalingGroupName": "my-asg", "ScheduledActionName": "my-recurring-action", "Recurrence": "30 0 1 1,6,12 *", "ScheduledActionARN": "arn:aws:autoscaling:us-west-2:123456789012:scheduledUpdateGroupAction:8e86b655-b2e6-4410-8f29-b4f094d6871c:autoScalingGroupName/my-asg:scheduledActionName/my-recurring-action", "StartTime": "2023-12-01T04:00:00Z", "Time": "2023-12-01T04:00:00Z", "MinSize": 1, "MaxSize": 6, "DesiredCapacity": 4, "TimeZone": "America/New_York" } ] }`For more information, see [Scheduled scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 6: To describe a specified number of scheduled actions**To return a specific number of scheduled actions, use the `--max-items`option.`aws autoscaling describe-scheduled-actions \ --auto-scaling-group-name``my-asg`\ --max-items`1`Output: `{ "ScheduledUpdateGroupActions": [ { "AutoScalingGroupName": "my-asg", "ScheduledActionName": "my-recurring-action", "Recurrence": "30 0 1 1,6,12 *", "ScheduledActionARN": "arn:aws:autoscaling:us-west-2:123456789012:scheduledUpdateGroupAction:8e86b655-b2e6-4410-8f29-b4f094d6871c:autoScalingGroupName/my-asg:scheduledActionName/my-recurring-action", "StartTime": "2023-12-01T04:00:00Z", "Time": "2023-12-01T04:00:00Z", "MinSize": 1, "MaxSize": 6, "DesiredCapacity": 4, "TimeZone": "America/New_York" } ] }`If the output includes a `NextToken`field, there are more scheduled actions. To get the additional scheduled actions, use the value of this field with the`--starting-token`option in a subsequent call as follows.`aws autoscaling describe-scheduled-actions \ --auto-scaling-group-name``my-asg`\ --starting-token`Z3M3LMPEXAMPLE`For more information, see [Scheduled scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [DescribeScheduledActions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-scheduled-actions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-tags`.

- **AWS CLI**
- 
            
                    **To describe all tags**This example describes all your tags. `aws autoscaling describe-tags`Output: `{ "Tags": [ { "ResourceType": "auto-scaling-group", "ResourceId": "my-asg", "PropagateAtLaunch": true, "Value": "Research", "Key": "Dept" }, { "ResourceType": "auto-scaling-group", "ResourceId": "my-asg", "PropagateAtLaunch": true, "Value": "WebServer", "Key": "Role" } ] }`For more information, see [Tagging Auto Scaling groups and instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-tagging.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 2: To describe tags for a specified group**To describe tags for a specific Auto Scaling group, use the `--filters`option.`aws autoscaling describe-tags --filters``Name=auto-scaling-group,Values=my-asg`For more information, see [Tagging Auto Scaling groups and instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-tagging.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 3: To describe the specified number of tags**To return a specific number of tags, use the `--max-items`option.`aws autoscaling describe-tags \ --max-items``1`If the output includes a `NextToken`field, there are more tags. To get the additional tags, use the value of this field with the`--starting-token`option in a subsequent call as follows.`aws autoscaling describe-tags \ --filters``Name=auto-scaling-group,Values=my-asg`\ --starting-token`Z3M3LMPEXAMPLE`For more information, see [Tagging Auto Scaling groups and instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-tagging.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [DescribeTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-termination-policy-types`.

- **AWS CLI**
- 
            
                    **To describe available termination policy types**This example describes the available termination policy types. `aws autoscaling describe-termination-policy-types`Output: `{ "TerminationPolicyTypes": [ "AllocationStrategy", "ClosestToNextInstanceHour", "Default", "NewestInstance", "OldestInstance", "OldestLaunchConfiguration", "OldestLaunchTemplate" ] }`For more information, see [Controlling which Auto Scaling instances terminate during scale in](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [DescribeTerminationPolicyTypes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-termination-policy-types.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-warm-pool`.

- **AWS CLI**
- 
            
                    **To describe a warm pool**This example describes the warm pool for the specified Auto Scaling group. `aws autoscaling describe-warm-pool \ --auto-scaling-group-name``my-asg`Output: `{ "WarmPoolConfiguration": { "MinSize": 2, "PoolState": "Stopped" }, "Instances": [ { "InstanceId": "i-070a5bbc7e7f40dc5", "InstanceType": "t2.micro", "AvailabilityZone": "us-west-2c", "LifecycleState": "Warmed:Pending", "HealthStatus": "Healthy", "LaunchTemplate": { "LaunchTemplateId": "lt-00a731f6e9fa48610", "LaunchTemplateName": "my-template-for-auto-scaling", "Version": "6" } }, { "InstanceId": "i-0b52f061814d3bd2d", "InstanceType": "t2.micro", "AvailabilityZone": "us-west-2b", "LifecycleState": "Warmed:Pending", "HealthStatus": "Healthy", "LaunchTemplate": { "LaunchTemplateId": "lt-00a731f6e9fa48610", "LaunchTemplateName": "my-template-for-auto-scaling", "Version": "6" } } ] }`For more information, see [Warm pools for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [DescribeWarmPool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-warm-pool.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detach-instances`.

- **AWS CLI**
- 
            
                    **To detach an instance from an Auto Scaling group**This example detaches the specified instance from the specified Auto Scaling group. `aws autoscaling detach-instances \ --instance-ids``i-030017cfa84b20135`\ --auto-scaling-group-name`my-asg`\ --should-decrement-desired-capacityOutput: `{ "Activities": [ { "ActivityId": "5091cb52-547a-47ce-a236-c9ccbc2cb2c9", "AutoScalingGroupName": "my-asg", "Description": "Detaching EC2 instance: i-030017cfa84b20135", "Cause": "At 2020-10-31T17:35:04Z instance i-030017cfa84b20135 was detached in response to a user request, shrinking the capacity from 2 to 1.", "StartTime": "2020-04-12T15:02:16.179Z", "StatusCode": "InProgress", "Progress": 50, "Details": "{\"Subnet ID\":\"subnet-6194ea3b\",\"Availability Zone\":\"us-west-2c\"}" } ] }`- 
                    For API details, see [DetachInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/detach-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detach-load-balancer-target-groups`.

- **AWS CLI**
- 
            
                    **To detach a load balancer target group from an Auto Scaling group**This example detaches the specified load balancer target group from the specified Auto Scaling group. `aws autoscaling detach-load-balancer-target-groups \ --auto-scaling-group-name``my-asg`\ --target-group-arns`arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067`This command produces no output For more information, see [Attaching a load balancer to your Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-load-balancer-asg.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [DetachLoadBalancerTargetGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/detach-load-balancer-target-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detach-load-balancers`.

- **AWS CLI**
- 
            
                    **To detach a Classic Load Balancer from an Auto Scaling group**This example detaches the specified Classic Load Balancer from the specified Auto Scaling group. `aws autoscaling detach-load-balancers \ --load-balancer-names``my-load-balancer`\ --auto-scaling-group-name`my-asg`This command produces no output. For more information, see [Attaching a load balancer to your Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-load-balancer-asg.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [DetachLoadBalancers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/detach-load-balancers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-metrics-collection`.

- **AWS CLI**
- 
            
                    **To disable metrics collection for an Auto Scaling group**This example disables collection of the `GroupDesiredCapacity`metric for the specified Auto Scaling group.`aws autoscaling disable-metrics-collection \ --auto-scaling-group-name``my-asg`\ --metrics`GroupDesiredCapacity`This command produces no output. For more information, see [Monitoring CloudWatch metrics for your Auto Scaling groups and instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-monitoring.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [DisableMetricsCollection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/disable-metrics-collection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-metrics-collection`.

- **AWS CLI**
- 
            
                    **Example 1: To enable metrics collection for an Auto Scaling group**This example enables data collection for the specified Auto Scaling group. `aws autoscaling enable-metrics-collection \ --auto-scaling-group-name``my-asg`\ --granularity`"1Minute"`This command produces no output. For more information, see [Monitoring CloudWatch metrics for your Auto Scaling groups and instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-monitoring.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 2: To collect data for the specified metric for an Auto Scaling group**To collect data for a specific metric, use the `--metrics`option.`aws autoscaling enable-metrics-collection \ --auto-scaling-group-name``my-asg`\ --metrics`GroupDesiredCapacity`--granularity`"1Minute"`This command produces no output. For more information, see [Monitoring CloudWatch metrics for your Auto Scaling groups and instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-monitoring.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [EnableMetricsCollection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/enable-metrics-collection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enter-standby`.

- **AWS CLI**
- 
            
                    **To move instances into standby mode**This example puts the specified instance into standby mode. This is useful for updating or troubleshooting an instance that is currently in service. `aws autoscaling enter-standby \ --instance-ids``i-061c63c5eb45f0416`\ --auto-scaling-group-name`my-asg`\ --should-decrement-desired-capacityOutput: `{ "Activities": [ { "ActivityId": "ffa056b4-6ed3-41ba-ae7c-249dfae6eba1", "AutoScalingGroupName": "my-asg", "Description": "Moving EC2 instance to Standby: i-061c63c5eb45f0416", "Cause": "At 2020-10-31T20:31:00Z instance i-061c63c5eb45f0416 was moved to standby in response to a user request, shrinking the capacity from 1 to 0.", "StartTime": "2020-10-31T20:31:00.949Z", "StatusCode": "InProgress", "Progress": 50, "Details": "{\"Subnet ID\":\"subnet-6194ea3b\",\"Availability Zone\":\"us-west-2c\"}" } ] }`For more information, see [Amazon EC2 Auto Scaling instance lifecycle](https://docs.aws.amazon.com/autoscaling/ec2/userguide/detach-instance-asg.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [EnterStandby](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/enter-standby.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `execute-policy`.

- **AWS CLI**
- 
            
                    **To execute a scaling policy**This example executes the scaling policy named `my-step-scale-out-policy`for the specified Auto Scaling group.`aws autoscaling execute-policy \ --auto-scaling-group-name``my-asg`\ --policy-name`my-step-scale-out-policy`\ --metric-value`95`\ --breach-threshold`80`This command produces no output. For more information, see [Step and simple scaling policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [ExecutePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/execute-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `exit-standby`.

- **AWS CLI**
- 
            
                    **To move instances out of standby mode**This example moves the specified instance out of standby mode. `aws autoscaling exit-standby \ --instance-ids``i-061c63c5eb45f0416`\ --auto-scaling-group-name`my-asg`Output: `{ "Activities": [ { "ActivityId": "142928e1-a2dc-453a-9b24-b85ad6735928", "AutoScalingGroupName": "my-asg", "Description": "Moving EC2 instance out of Standby: i-061c63c5eb45f0416", "Cause": "At 2020-10-31T20:32:50Z instance i-061c63c5eb45f0416 was moved out of standby in response to a user request, increasing the capacity from 0 to 1.", "StartTime": "2020-10-31T20:32:50.222Z", "StatusCode": "PreInService", "Progress": 30, "Details": "{\"Subnet ID\":\"subnet-6194ea3b\",\"Availability Zone\":\"us-west-2c\"}" } ] }`For more information, see [Temporarily removing instances from your Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-enter-exit-standby.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [ExitStandby](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/exit-standby.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-lifecycle-hook`.

- **AWS CLI**
- 
            
                    **Example 1: To create a lifecycle hook**This example creates a lifecycle hook that will invoke on any newly launched instances, with a timeout of 4800 seconds. This is useful for keeping the instances in a wait state until the user data scripts have finished, or for invoking an AWS Lambda function using EventBridge. `aws autoscaling put-lifecycle-hook \ --auto-scaling-group-name``my-asg`\ --lifecycle-hook-name`my-launch-hook`\ --lifecycle-transition`autoscaling:EC2_INSTANCE_LAUNCHING`\ --heartbeat-timeout`4800`This command produces no output. If a lifecycle hook with the same name already exists, it will be overwritten by the new lifecycle hook. For more information, see [Amazon EC2 Auto Scaling lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 2: To send an Amazon SNS email message to notify you of instance state transitions**This example creates a lifecycle hook with the Amazon SNS topic and IAM role to use to receive notification at instance launch. `aws autoscaling put-lifecycle-hook \ --auto-scaling-group-name``my-asg`\ --lifecycle-hook-name`my-launch-hook`\ --lifecycle-transition`autoscaling:EC2_INSTANCE_LAUNCHING`\ --notification-target-arn`arn:aws:sns:us-west-2:123456789012:my-sns-topic`\ --role-arn`arn:aws:iam::123456789012:role/my-auto-scaling-role`This command produces no output. For more information, see [Amazon EC2 Auto Scaling lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 3: To publish a message to an Amazon SQS queue**This example creates a lifecycle hook that publishes a message with metadata to the specified Amazon SQS queue. `aws autoscaling put-lifecycle-hook \ --auto-scaling-group-name``my-asg`\ --lifecycle-hook-name`my-launch-hook`\ --lifecycle-transition`autoscaling:EC2_INSTANCE_LAUNCHING`\ --notification-target-arn`arn:aws:sqs:us-west-2:123456789012:my-sqs-queue`\ --role-arn`arn:aws:iam::123456789012:role/my-notification-role`\ --notification-metadata`"SQS message metadata"`This command produces no output. For more information, see [Amazon EC2 Auto Scaling lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [PutLifecycleHook](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-lifecycle-hook.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-notification-configuration`.

- **AWS CLI**
- 
            
                    **To add a notification**This example adds the specified notification to the specified Auto Scaling group. `aws autoscaling put-notification-configuration \ --auto-scaling-group-name``my-asg`\ --topic-arn`arn:aws:sns:us-west-2:123456789012:my-sns-topic`\ --notification-type`autoscaling:TEST_NOTIFICATION`This command produces no output. For more information, see [Getting Amazon SNS notifications when your Auto Scaling group scales](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ASGettingNotifications.html#as-configure-asg-for-sns)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [PutNotificationConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-notification-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-scaling-policy`.

- **AWS CLI**
- 
            
                    **To add a target tracking scaling policy to an Auto Scaling group**The following `put-scaling-policy`example applies a target tracking scaling policy to the specified Auto Scaling group. The output contains the ARNs and names of the two CloudWatch alarms created on your behalf. If a scaling policy with the same name already exists, it will be overwritten by the new scaling policy.`aws autoscaling put-scaling-policy --auto-scaling-group-name``my-asg`\ --policy-name`alb1000-target-tracking-scaling-policy`\ --policy-type`TargetTrackingScaling`\ --target-tracking-configuration`file://config.json`Contents of `config.json`:`{ "TargetValue": 1000.0, "PredefinedMetricSpecification": { "PredefinedMetricType": "ALBRequestCountPerTarget", "ResourceLabel": "app/my-alb/778d41231b141a0f/targetgroup/my-alb-target-group/943f017f100becff" } }`Output: `{ "PolicyARN": "arn:aws:autoscaling:region:account-id:scalingPolicy:228f02c2-c665-4bfd-aaac-8b04080bea3c:autoScalingGroupName/my-asg:policyName/alb1000-target-tracking-scaling-policy", "Alarms": [ { "AlarmARN": "arn:aws:cloudwatch:region:account-id:alarm:TargetTracking-my-asg-AlarmHigh-fc0e4183-23ac-497e-9992-691c9980c38e", "AlarmName": "TargetTracking-my-asg-AlarmHigh-fc0e4183-23ac-497e-9992-691c9980c38e" }, { "AlarmARN": "arn:aws:cloudwatch:region:account-id:alarm:TargetTracking-my-asg-AlarmLow-61a39305-ed0c-47af-bd9e-471a352ee1a2", "AlarmName": "TargetTracking-my-asg-AlarmLow-61a39305-ed0c-47af-bd9e-471a352ee1a2" } ] }`For more examples, see [Example scaling policies for the AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/autoscaling/ec2/userguide/examples-scaling-policies.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [PutScalingPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-scaling-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-scheduled-update-group-action`.

- **AWS CLI**
- 
            
                    **Example 1: To add a scheduled action to an Auto Scaling group**This example adds the specified scheduled action to the specified Auto Scaling group. `aws autoscaling put-scheduled-update-group-action \ --auto-scaling-group-name``my-asg`\ --scheduled-action-name`my-scheduled-action`\ --start-time`"2023-05-12T08:00:00Z"`\ --min-size`2`\ --max-size`6`\ --desired-capacity`4`This command produces no output. If a scheduled action with the same name already exists, it will be overwritten by the new scheduled action. For more examples, see [Scheduled scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 2: To specify a recurring schedule**This example creates a scheduled action to scale on a recurring schedule that is scheduled to execute at 00:30 hours on the first of January, June, and December every year. `aws autoscaling put-scheduled-update-group-action \ --auto-scaling-group-name``my-asg`\ --scheduled-action-name`my-recurring-action`\ --recurrence`"30 0 1 1,6,12 *"`\ --min-size`2`\ --max-size`6`\ --desired-capacity`4`This command produces no output. If a scheduled action with the same name already exists, it will be overwritten by the new scheduled action. For more examples, see [Scheduled scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [PutScheduledUpdateGroupAction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-scheduled-update-group-action.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-warm-pool`.

- **AWS CLI**
- 
            
                    **To create a warm pool**The following example creates a warm pool for the specified Auto Scaling group. `aws autoscaling put-warm-pool \ --auto-scaling-group-name``my-asg`\ --min-size`2`This command produces no output. If a warm pool already exists, it will be updated. For more information, see [Warm pools for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [PutWarmPool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/put-warm-pool.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `record-lifecycle-action-heartbeat`.

- **AWS CLI**
- 
            
                    **To record a lifecycle action heartbeat**This example records a lifecycle action heartbeat to keep the instance in a pending state. `aws autoscaling record-lifecycle-action-heartbeat \ --lifecycle-hook-name``my-launch-hook`\ --auto-scaling-group-name`my-asg`\ --lifecycle-action-token`bcd2f1b8-9a78-44d3-8a7a-4dd07d7cf635`This command produces no output. For more information, see [Amazon EC2 Auto Scaling lifecycle hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [RecordLifecycleActionHeartbeat](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/record-lifecycle-action-heartbeat.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `resume-processes`.

- **AWS CLI**
- 
            
                    **To resume suspended processes**This example resumes the specified suspended scaling process for the specified Auto Scaling group. `aws autoscaling resume-processes \ --auto-scaling-group-name``my-asg`\ --scaling-processes`AlarmNotification`This command produces no output. For more information, see [Suspending and resuming scaling processes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [ResumeProcesses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/resume-processes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `rollback-instance-refresh`.

- **AWS CLI**
- 
            
                    **To roll back an instance refresh**The following `rollback-instance-refresh`example rolls back an in-progress instance refresh for the specified Auto Scaling group.`aws autoscaling rollback-instance-refresh \ --auto-scaling-group-name``my-asg`Output: `{ "InstanceRefreshId": "08b91cf7-8fa6-48af-b6a6-d227f40f1b9b" }`For more information, see [Undo changes with a rollback](https://docs.aws.amazon.com/autoscaling/ec2/userguide/instance-refresh-rollback.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [RollbackInstanceRefresh](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/rollback-instance-refresh.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-desired-capacity`.

- **AWS CLI**
- 
            
                    **To set the desired capacity for an Auto Scaling group**This example sets the desired capacity for the specified Auto Scaling group. `aws autoscaling set-desired-capacity \ --auto-scaling-group-name``my-asg`\ --desired-capacity`2`\ --honor-cooldownThis command returns to the prompt if successful. - 
                    For API details, see [SetDesiredCapacity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/set-desired-capacity.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-instance-health`.

- **AWS CLI**
- 
            
                    **To set the health status of an instance**This example sets the health status of the specified instance to `Unhealthy`.`aws autoscaling set-instance-health \ --instance-id``i-061c63c5eb45f0416`\ --health-status`Unhealthy`This command produces no output. - 
                    For API details, see [SetInstanceHealth](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/set-instance-health.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-instance-protection`.

- **AWS CLI**
- 
            
                    **Example 1: To enable the instance protection setting for an instance**This example enables instance protection for the specified instance. `aws autoscaling set-instance-protection \ --instance-ids``i-061c63c5eb45f0416`\ --auto-scaling-group-name`my-asg`--protected-from-scale-inThis command produces no output. **Example 2: To disable the instance protection setting for an instance**This example disables instance protection for the specified instance. `aws autoscaling set-instance-protection \ --instance-ids``i-061c63c5eb45f0416`\ --auto-scaling-group-name`my-asg`\ --no-protected-from-scale-inThis command produces no output. - 
                    For API details, see [SetInstanceProtection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/set-instance-protection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-instance-refresh`.

- **AWS CLI**
- 
            
                    **Example 1: To start an instance refresh using command line parameters**The following `start-instance-refresh`example starts an instance refresh using command line arguments. The optional`preferences`parameter specifies an`InstanceWarmup`of`60`seconds and a`MinHealthyPercentage`of`50`percent.`aws autoscaling start-instance-refresh \ --auto-scaling-group-name``my-asg`\ --preferences '`{"InstanceWarmup": 60, "MinHealthyPercentage": 50}`'Output: `{ "InstanceRefreshId": "08b91cf7-8fa6-48af-b6a6-d227f40f1b9b" }`For more information, see [Start an instance refresh](https://docs.aws.amazon.com/en_us/autoscaling/ec2/userguide/start-instance-refresh.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 2: To start an instance refresh using a JSON file**The following `start-instance-refresh`example starts an instance refresh using a JSON file. You can specify the Auto Scaling group and define your desired configuration and preferences in a JSON file, as shown in the following example.`aws autoscaling start-instance-refresh \ --cli-input-json``file://config.json`Contents of `config.json`:`{ "AutoScalingGroupName": "my-asg", "DesiredConfiguration": { "LaunchTemplate": { "LaunchTemplateId": "lt-068f72b729example", "Version": "$Default" } }, "Preferences": { "InstanceWarmup": 60, "MinHealthyPercentage": 50, "AutoRollback": true, "ScaleInProtectedInstances": Ignore, "StandbyInstances": Terminate } }`Output: `{ "InstanceRefreshId": "08b91cf7-8fa6-48af-b6a6-d227f40f1b9b" }`For more information, see [Start an instance refresh](https://docs.aws.amazon.com/en_us/autoscaling/ec2/userguide/start-instance-refresh.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [StartInstanceRefresh](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/start-instance-refresh.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `suspend-processes`.

- **AWS CLI**
- 
            
                    **To suspend Auto Scaling processes**This example suspends the specified scaling process for the specified Auto Scaling group. `aws autoscaling suspend-processes \ --auto-scaling-group-name``my-asg`\ --scaling-processes`AlarmNotification`This command produces no output. For more information, see [Suspending and resuming scaling processes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [SuspendProcesses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/suspend-processes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `terminate-instance-in-auto-scaling-group`.

- **AWS CLI**
- 
            
                    **To terminate an instance in an Auto Scaling group**This example terminates the specified instance from the specified Auto Scaling group without updating the size of the group. Amazon EC2 Auto Scaling launches a replacement instance after the specified instance terminates. `aws autoscaling terminate-instance-in-auto-scaling-group \ --instance-id``i-061c63c5eb45f0416`\ --no-should-decrement-desired-capacityOutput: `{ "Activities": [ { "ActivityId": "8c35d601-793c-400c-fcd0-f64a27530df7", "AutoScalingGroupName": "my-asg", "Description": "Terminating EC2 instance: i-061c63c5eb45f0416", "Cause": "", "StartTime": "2020-10-31T20:34:25.680Z", "StatusCode": "InProgress", "Progress": 0, "Details": "{\"Subnet ID\":\"subnet-6194ea3b\",\"Availability Zone\":\"us-west-2c\"}" } ] }`- 
                    For API details, see [TerminateInstanceInAutoScalingGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/terminate-instance-in-auto-scaling-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-auto-scaling-group`.

- **AWS CLI**
- 
            
                    **Example 1: To update the size limits of an Auto Scaling group**This example updates the specified Auto Scaling group with a minimum size of 2 and a maximum size of 10. `aws autoscaling update-auto-scaling-group \ --auto-scaling-group-name``my-asg`\ --min-size`2`\ --max-size`10`This command produces no output. For more information, see [Setting capacity limits for your Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-capacity-limits.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 2: To add Elastic Load Balancing health checks and specify which Availability Zones and subnets to use**This example updates the specified Auto Scaling group to add Elastic Load Balancing health checks. This command also updates the value of `--vpc-zone-identifier`with a list of subnet IDs in multiple Availability Zones.`aws autoscaling update-auto-scaling-group \ --auto-scaling-group-name``my-asg`\ --health-check-type`ELB`\ --health-check-grace-period`600`\ --vpc-zone-identifier`"subnet-5ea0c127,subnet-6194ea3b,subnet-c934b782"`This command produces no output. For more information, see [Elastic Load Balancing and Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 3: To update the placement group and termination policy**This example updates the placement group and termination policy to use. `aws autoscaling update-auto-scaling-group \ --auto-scaling-group-name``my-asg`\ --placement-group`my-placement-group`\ --termination-policies`"OldestInstance"`This command produces no output. For more information, see [Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 4: To use the latest version of the launch template**This example updates the specified Auto Scaling group to use the latest version of the specified launch template. `aws autoscaling update-auto-scaling-group \ --auto-scaling-group-name``my-asg`\ --launch-template LaunchTemplateId=lt-1234567890abcde12,Version='$Latest'This command produces no output. For more information, see [Launch templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/LaunchTemplates.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 5: To use a specific version of the launch template**This example updates the specified Auto Scaling group to use a specific version of a launch template instead of the latest or default version. `aws autoscaling update-auto-scaling-group \ --auto-scaling-group-name``my-asg`\ --launch-template LaunchTemplateName=my-template-for-auto-scaling,Version='2'This command produces no output. For more information, see [Launch templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/LaunchTemplates.html)in the*Amazon EC2 Auto Scaling User Guide*.**Example 6: To define a mixed instances policy and enable capacity rebalancing**This example updates the specified Auto Scaling group to use a mixed instances policy and enables capacity rebalancing. This structure lets you specify groups with Spot and On-Demand capacities and use different launch templates for different architectures. `aws autoscaling update-auto-scaling-group \ --cli-input-json``file://~/config.json`Contents of `config.json`:`{ "AutoScalingGroupName": "my-asg", "CapacityRebalance": true, "MixedInstancesPolicy": { "LaunchTemplate": { "LaunchTemplateSpecification": { "LaunchTemplateName": "my-launch-template-for-x86", "Version": "$Latest" }, "Overrides": [ { "InstanceType": "c6g.large", "LaunchTemplateSpecification": { "LaunchTemplateName": "my-launch-template-for-arm", "Version": "$Latest" } }, { "InstanceType": "c5.large" }, { "InstanceType": "c5a.large" } ] }, "InstancesDistribution": { "OnDemandPercentageAboveBaseCapacity": 50, "SpotAllocationStrategy": "capacity-optimized" } } }`This command produces no output. For more information, see [Auto Scaling groups with multiple instance types and purchase options](https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-purchase-options.html)in the*Amazon EC2 Auto Scaling User Guide*.- 
                    For API details, see [UpdateAutoScalingGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html)in*AWS CLI Command Reference*.
 
-