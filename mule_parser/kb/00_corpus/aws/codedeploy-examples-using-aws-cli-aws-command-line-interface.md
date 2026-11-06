# CodeDeploy examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_codedeploy_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_codedeploy_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with CodeDeploy.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `add-tags-to-on-premises-instances`.

- **AWS CLI**
- 
            
                    **To add tags to on-premises instances**The following `add-tags-to-on-premises-instances`example associates in AWS CodeDeploy the same on-premises instance tag to two on-premises instances. It does not register the on-premises instances with AWS CodeDeploy.`aws deploy add-tags-to-on-premises-instances \ --instance-names``AssetTag12010298EX``AssetTag23121309EX`\ --tags`Key=Name,Value=CodeDeployDemo-OnPrem`This command produces no output. - 
                    For API details, see [AddTagsToOnPremisesInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/add-tags-to-on-premises-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-get-application-revisions`.

- **AWS CLI**
- 
            
                    **To retrieve information about application revisions**The following `batch-get-application-revisions`example retrieves information about the specified revision stored in a GitHub repository.`aws deploy batch-get-application-revisions \ --application-name``my-codedeploy-application`\ --revisions "[{\"gitHubLocation\": {\"commitId\": \"fa85936EXAMPLEa31736c051f10d77297EXAMPLE\",\"repository\": \"my-github-token/my-repository\"},\"revisionType\": \"GitHub\"}]"Output: `{ "revisions": [ { "genericRevisionInfo": { "description": "Application revision registered by Deployment ID: d-A1B2C3111", "lastUsedTime": 1556912355.884, "registerTime": 1556912355.884, "firstUsedTime": 1556912355.884, "deploymentGroups": [] }, "revisionLocation": { "revisionType": "GitHub", "gitHubLocation": { "commitId": "fa85936EXAMPLEa31736c051f10d77297EXAMPLE", "repository": "my-github-token/my-repository" } } } ], "applicationName": "my-codedeploy-application", "errorMessage": "" }`For more information, see [BatchGetApplicationRevisions](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetApplicationRevisions.html)in the*AWS CodeDeploy API Reference*.- 
                    For API details, see [BatchGetApplicationRevisions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/batch-get-application-revisions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-get-applications`.

- **AWS CLI**
- 
            
                    **To get information about multiple applications**The following `batch-get-applications`example displays information about multiple applications that are associated with the user's AWS account.`aws deploy batch-get-applications --application-names``WordPress_App``MyOther_App`Output: `{ "applicationsInfo": [ { "applicationName": "WordPress_App", "applicationId": "d9dd6993-f171-44fa-a811-211e4EXAMPLE", "createTime": 1407878168.078, "linkedToGitHub": false }, { "applicationName": "MyOther_App", "applicationId": "8ca57519-31da-42b2-9194-8bb16EXAMPLE", "createTime": 1407453571.63, "linkedToGitHub": false } ] }`- 
                    For API details, see [BatchGetApplications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/batch-get-applications.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-get-deployment-groups`.

- **AWS CLI**
- 
            
                    **To retrieve information about one or more deployment groups**The following `batch-get-deployment-groups`example retrieves information about two of the deployment groups that are associated with the specified CodeDeploy application.`aws deploy batch-get-deployment-groups \ --application-name``my-codedeploy-application`\ --deployment-group-names "[\"my-deployment-group-1\",\"my-deployment-group-2\"]"Output: `{ "deploymentGroupsInfo": [ { "deploymentStyle": { "deploymentOption": "WITHOUT_TRAFFIC_CONTROL", "deploymentType": "IN_PLACE" }, "autoRollbackConfiguration": { "enabled": false }, "onPremisesTagSet": { "onPremisesTagSetList": [] }, "serviceRoleArn": "arn:aws:iam::123456789012:role/CodeDeployServiceRole", "lastAttemptedDeployment": { "endTime": 1556912366.415, "status": "Failed", "createTime": 1556912355.884, "deploymentId": "d-A1B2C3111" }, "autoScalingGroups": [], "deploymentGroupName": "my-deployment-group-1", "ec2TagSet": { "ec2TagSetList": [ [ { "Type": "KEY_AND_VALUE", "Value": "my-EC2-instance", "Key": "Name" } ] ] }, "deploymentGroupId": "a1b2c3d4-5678-90ab-cdef-11111example", "triggerConfigurations": [], "applicationName": "my-codedeploy-application", "computePlatform": "Server", "deploymentConfigName": "CodeDeployDefault.AllAtOnce" }, { "deploymentStyle": { "deploymentOption": "WITHOUT_TRAFFIC_CONTROL", "deploymentType": "IN_PLACE" }, "autoRollbackConfiguration": { "enabled": false }, "onPremisesTagSet": { "onPremisesTagSetList": [] }, "serviceRoleArn": "arn:aws:iam::123456789012:role/CodeDeployServiceRole", "autoScalingGroups": [], "deploymentGroupName": "my-deployment-group-2", "ec2TagSet": { "ec2TagSetList": [ [ { "Type": "KEY_AND_VALUE", "Value": "my-EC2-instance", "Key": "Name" } ] ] }, "deploymentGroupId": "a1b2c3d4-5678-90ab-cdef-22222example", "triggerConfigurations": [], "applicationName": "my-codedeploy-application", "computePlatform": "Server", "deploymentConfigName": "CodeDeployDefault.AllAtOnce" } ], "errorMessage": "" }`For more information, see [BatchGetDeploymentGroups](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetDeploymentGroups.html)in the*AWS CodeDeploy API Reference*.- 
                    For API details, see [BatchGetDeploymentGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/batch-get-deployment-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-get-deployment-targets`.

- **AWS CLI**
- 
            
                    **To retrieve the targets associated with a deployment**The following `batch-get-deployment-targets`example returns information about one of the targets associated with the specified deployment.`aws deploy batch-get-deployment-targets \ --deployment-id``"d-1A2B3C4D5"`\ --target-ids`"i-01a2b3c4d5e6f1111"`Output: `{ "deploymentTargets": [ { "deploymentTargetType": "InstanceTarget", "instanceTarget": { "lifecycleEvents": [ { "startTime": 1556918592.162, "lifecycleEventName": "ApplicationStop", "status": "Succeeded", "endTime": 1556918592.247, "diagnostics": { "scriptName": "", "errorCode": "Success", "logTail": "", "message": "Succeeded" } }, { "startTime": 1556918593.193, "lifecycleEventName": "DownloadBundle", "status": "Succeeded", "endTime": 1556918593.981, "diagnostics": { "scriptName": "", "errorCode": "Success", "logTail": "", "message": "Succeeded" } }, { "startTime": 1556918594.805, "lifecycleEventName": "BeforeInstall", "status": "Succeeded", "endTime": 1556918681.807, "diagnostics": { "scriptName": "", "errorCode": "Success", "logTail": "", "message": "Succeeded" } } ], "targetArn": "arn:aws:ec2:us-west-2:123456789012:instance/i-01a2b3c4d5e6f1111", "deploymentId": "d-1A2B3C4D5", "lastUpdatedAt": 1556918687.504, "targetId": "i-01a2b3c4d5e6f1111", "status": "Succeeded" } } ] }`For more information, see [BatchGetDeploymentTargets](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_BatchGetDeploymentTargets.html)in the*AWS CodeDeploy API Reference*.- 
                    For API details, see [BatchGetDeploymentTargets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/batch-get-deployment-targets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-get-deployments`.

- **AWS CLI**
- 
            
                    **To get information about multiple deployments**The following `batch-get-deployments`example displays information about multiple deployments that are associated with the user's AWS account.`aws deploy batch-get-deployments --deployment-ids``d-A1B2C3111``d-A1B2C3222`Output: `{ "deploymentsInfo": [ { "applicationName": "WordPress_App", "status": "Failed", "deploymentOverview": { "Failed": 0, "InProgress": 0, "Skipped": 0, "Succeeded": 1, "Pending": 0 }, "deploymentConfigName": "CodeDeployDefault.OneAtATime", "creator": "user", "deploymentGroupName": "WordPress_DG", "revision": { "revisionType": "S3", "s3Location": { "bundleType": "zip", "version": "uTecLusEXAMPLEFXtfUcyfV8bEXAMPLE", "bucket": "amzn-s3-demo-bucket", "key": "WordPressApp.zip" } }, "deploymentId": "d-A1B2C3111", "createTime": 1408480721.9, "completeTime": 1408480741.822 }, { "applicationName": "MyOther_App", "status": "Failed", "deploymentOverview": { "Failed": 1, "InProgress": 0, "Skipped": 0, "Succeeded": 0, "Pending": 0 }, "deploymentConfigName": "CodeDeployDefault.OneAtATime", "creator": "user", "errorInformation": { "message": "Deployment failed: Constraint default violated: No hosts succeeded.", "code": "HEALTH_CONSTRAINTS" }, "deploymentGroupName": "MyOther_DG", "revision": { "revisionType": "S3", "s3Location": { "bundleType": "zip", "eTag": "\"dd56cfdEXAMPLE8e768f9d77fEXAMPLE\"", "bucket": "amzn-s3-demo-bucket", "key": "MyOtherApp.zip" } }, "deploymentId": "d-A1B2C3222", "createTime": 1409764576.589, "completeTime": 1409764596.101 } ] }`- 
                    For API details, see [BatchGetDeployments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/batch-get-deployments.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-get-on-premises-instances`.

- **AWS CLI**
- 
            
                    **To get information about one or more on-premises instances**The following `batch-get-on-premises-instances`example gets information about two on-premises instances.`aws deploy batch-get-on-premises-instances --instance-names``AssetTag12010298EX``AssetTag23121309EX`Output: `{ "instanceInfos": [ { "iamUserArn": "arn:aws:iam::123456789012:user/AWS/CodeDeploy/AssetTag12010298EX", "tags": [ { "Value": "CodeDeployDemo-OnPrem", "Key": "Name" } ], "instanceName": "AssetTag12010298EX", "registerTime": 1425579465.228, "instanceArn": "arn:aws:codedeploy:us-west-2:123456789012:instance/AssetTag12010298EX_4IwLNI2Alh" }, { "iamUserArn": "arn:aws:iam::123456789012:user/AWS/CodeDeploy/AssetTag23121309EX", "tags": [ { "Value": "CodeDeployDemo-OnPrem", "Key": "Name" } ], "instanceName": "AssetTag23121309EX", "registerTime": 1425595585.988, "instanceArn": "arn:aws:codedeploy:us-west-2:80398EXAMPLE:instance/AssetTag23121309EX_PomUy64Was" } ] }`- 
                    For API details, see [BatchGetOnPremisesInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/batch-get-on-premises-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `continue-deployment`.

- **AWS CLI**
- 
            
                    **To start rerouting traffic without waiting for a specified wait time to elapse.**The following `continue-deployment`example starts rerouting traffic from instances in the original environment that are ready to start shifting traffic to instances in the replacement environment.`aws deploy continue-deployment \ --deployment-id``"d-A1B2C3111"`\ --deployment-wait-type`"READY_WAIT"`This command produces no output. For more information, see [ContinueDeployment](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ContinueDeployment.html)in the*AWS CodeDeploy API Reference*.- 
                    For API details, see [ContinueDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/continue-deployment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-application`.

- **AWS CLI**
- 
            
                    **To create an application**The following `create-application`example creates an application and associates it with the user's AWS account.`aws deploy create-application --application-name``MyOther_App`Output: `{ "applicationId": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE" }`- 
                    For API details, see [CreateApplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/create-application.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-deployment-config`.

- **AWS CLI**
- 
            
                    **To create a custom deployment configuration**The following `create-deployment-config`example creates a custom deployment configuration and associates it with the user's AWS account.`aws deploy create-deployment-config \ --deployment-config-name``ThreeQuartersHealthy`\ --minimum-healthy-hosts`type=FLEET_PERCENT,value=75`Output: `{ "deploymentConfigId": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE" }`- 
                    For API details, see [CreateDeploymentConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/create-deployment-config.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-deployment-group`.

- **AWS CLI**
- 
            
                    **To create a deployment group**The following `create-deployment-group`example creates a deployment group and associates it with the specified application and the user's AWS account.`aws deploy create-deployment-group \ --application-name``WordPress_App`\ --auto-scaling-groups`CodeDeployDemo-ASG`\ --deployment-config-name`CodeDeployDefault.OneAtATime`\ --deployment-group-name`WordPress_DG`\ --ec2-tag-filters`Key=Name,Value=CodeDeployDemo,Type=KEY_AND_VALUE`\ --service-role-arn`arn:aws:iam::123456789012:role/CodeDeployDemoRole`Output: `{ "deploymentGroupId": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE" }`- 
                    For API details, see [CreateDeploymentGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/create-deployment-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-deployment`.

- **AWS CLI**
- 
            
                    **Example 1: To create a CodeDeploy deployment using the EC2/On-premises compute platform**The following `create-deployment`example creates a deployment and associates it with the user's AWS account.`aws deploy create-deployment \ --application-name``WordPress_App`\ --deployment-config-name`CodeDeployDefault.OneAtATime`\ --deployment-group-name`WordPress_DG`\ --description`"My demo deployment"`\ --s3-location`bucket=amzn-s3-demo-bucket,bundleType=zip,eTag=dd56cfdEXAMPLE8e768f9d77fEXAMPLE,key=WordPressApp.zip`Output: `{ "deploymentId": "d-A1B2C3111" }`**Example 2: To create a CodeDeploy deployment using the Amazon ECS compute platform**The following `create-deployment`example uses the following two files to deploy an Amazon ECS service.Contents of `create-deployment.json`file:`{ "applicationName": "ecs-deployment", "deploymentGroupName": "ecs-deployment-dg", "revision": { "revisionType": "S3", "s3Location": { "bucket": "ecs-deployment-bucket", "key": "appspec.yaml", "bundleType": "YAML" } } }`That file, in turn, retrieves the following file `appspec.yaml`from an S3 bucket called`ecs-deployment-bucket`.`version: 0.0 Resources: - TargetService: Type: AWS::ECS::Service Properties: TaskDefinition: "arn:aws:ecs:region:123456789012:task-definition/ecs-task-def:2" LoadBalancerInfo: ContainerName: "sample-app" ContainerPort: 80 PlatformVersion: "LATEST"`Command: `aws deploy create-deployment \ --cli-input-json``file://create-deployment.json`\ --region`us-east-1`Output: `{ "deploymentId": "d-1234ABCDE" }`For more information, see [CreateDeployment](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateDeployment.html)in the*AWS CodeDeploy API Reference*.- 
                    For API details, see [CreateDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/create-deployment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-application`.

- **AWS CLI**
- 
            
                    **To delete an application**The following `delete-application`example deletes the specified application that is associated with the user's AWS account.`aws deploy delete-application --application-name``WordPress_App`This command produces no output. - 
                    For API details, see [DeleteApplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/delete-application.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-deployment-config`.

- **AWS CLI**
- 
            
                    **To delete a deployment configuration**The following `delete-deployment-config`example deletes a custom deployment configuration that is associated with the user's AWS account.`aws deploy delete-deployment-config --deployment-config-name``ThreeQuartersHealthy`This command produces no output. - 
                    For API details, see [DeleteDeploymentConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/delete-deployment-config.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-deployment-group`.

- **AWS CLI**
- 
            
                    **To delete a deployment group**The following `delete-deployment-group`example deletes a deployment group that is associated with the specified application.`aws deploy delete-deployment-group \ --application-name``WordPress_App`\ --deployment-group-name`WordPress_DG`Output: `{ "hooksNotCleanedUp": [] }`- 
                    For API details, see [DeleteDeploymentGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/delete-deployment-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-git-hub-account-token`.

- **AWS CLI**
- 
            
                    **To deletes a GitHub account connection**The following `delete-git-hub-account-token`example deletes the connection of the specified GitHub account.`aws deploy delete-git-hub-account-token --token-name``my-github-account`Output: `{ "tokenName": "my-github-account" }`For more information, see [DeleteGitHubAccountToken](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeleteGitHubAccountToken.html)in the*AWS CodeDeploy API Reference*.- 
                    For API details, see [DeleteGitHubAccountToken](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/delete-git-hub-account-token.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deregister-on-premises-instance`.

- **AWS CLI**
- 
            
                    **To deregister an on-premises instance**The following `deregister-on-premises-instance`example deregisters an on-premises instance with AWS CodeDeploy, but it does not delete the IAM user associated with the instance, nor does it disassociate in AWS CodeDeploy the on-premises instance tags from the instance. It also does not uninstall the AWS CodeDeploy Agent from the instance nor remove the on-premises configuration file from the instance.`aws deploy deregister-on-premises-instance --instance-name``AssetTag12010298EX`This command produces no output. - 
                    For API details, see [DeregisterOnPremisesInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/deregister-on-premises-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deregister`.

- **AWS CLI**
- 
            
                    **To deregister an on-premises instance**The following `deregister`example deregisters an on-premises instance with AWS CodeDeploy. It does not delete the IAM user that is associated with the instance. It disassociates in AWS CodeDeploy the on-premises tags from the instance. It does not uninstall the AWS CodeDeploy Agent from the instance nor remove the on-premises configuration file from the instance.`aws deploy deregister \ --instance-name``AssetTag12010298EX`\ --no-delete-iam-user \ --region`us-west-2`Output: `Retrieving on-premises instance information... DONE IamUserArn: arn:aws:iam::80398EXAMPLE:user/AWS/CodeDeploy/AssetTag12010298EX Tags: Key=Name,Value=CodeDeployDemo-OnPrem Removing tags from the on-premises instance... DONE Deregistering the on-premises instance... DONE Run the following command on the on-premises instance to uninstall the codedeploy-agent: aws deploy uninstall`- 
                    For API details, see [Deregister](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/deregister.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-application-revision`.

- **AWS CLI**
- 
            
                    **To get information about an application revision**The following `get-application-revision`example displays information about an application revision that is associated with the specified application.`aws deploy get-application-revision \ --application-name``WordPress_App`\ --s3-location`bucket=amzn-s3-demo-bucket,bundleType=zip,eTag=dd56cfdEXAMPLE8e768f9d77fEXAMPLE,key=WordPressApp.zip`Output: `{ "applicationName": "WordPress_App", "revisionInfo": { "description": "Application revision registered by Deployment ID: d-A1B2C3111", "registerTime": 1411076520.009, "deploymentGroups": "WordPress_DG", "lastUsedTime": 1411076520.009, "firstUsedTime": 1411076520.009 }, "revision": { "revisionType": "S3", "s3Location": { "bundleType": "zip", "eTag": "dd56cfdEXAMPLE8e768f9d77fEXAMPLE", "bucket": "amzn-s3-demo-bucket", "key": "WordPressApp.zip" } } }`- 
                    For API details, see [GetApplicationRevision](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-application-revision.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-application`.

- **AWS CLI**
- 
            
                    **To get information about an application**The following `get-application`example displays information about an application that is associated with the user's AWS account.`aws deploy get-application --application-name``WordPress_App`Output: `{ "application": { "applicationName": "WordPress_App", "applicationId": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "createTime": 1407878168.078, "linkedToGitHub": false } }`- 
                    For API details, see [GetApplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-application.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-deployment-config`.

- **AWS CLI**
- 
            
                    **To get information about a deployment configuration**The following `get-deployment-config`example displays information about a deployment configuration that is associated with the user's AWS account.`aws deploy get-deployment-config --deployment-config-name``ThreeQuartersHealthy`Output: `{ "deploymentConfigInfo": { "deploymentConfigId": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "minimumHealthyHosts": { "type": "FLEET_PERCENT", "value": 75 }, "createTime": 1411081164.379, "deploymentConfigName": "ThreeQuartersHealthy" } }`- 
                    For API details, see [GetDeploymentConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-deployment-config.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-deployment-group`.

- **AWS CLI**
- 
            
                    **To view information about a deployment group**The following `get-deployment-group`example displays information about a deployment group that is associated with the specified application.`aws deploy get-deployment-group \ --application-name``WordPress_App`\ --deployment-group-name`WordPress_DG`Output: `{ "deploymentGroupInfo": { "applicationName": "WordPress_App", "autoScalingGroups": [ "CodeDeployDemo-ASG" ], "deploymentConfigName": "CodeDeployDefault.OneAtATime", "ec2TagFilters": [ { "Type": "KEY_AND_VALUE", "Value": "CodeDeployDemo", "Key": "Name" } ], "deploymentGroupId": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "serviceRoleArn": "arn:aws:iam::123456789012:role/CodeDeployDemoRole", "deploymentGroupName": "WordPress_DG" } }`- 
                    For API details, see [GetDeploymentGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-deployment-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-deployment-instance`.

- **AWS CLI**
- 
            
                    **To get information about a deployment instance**The following `get-deployment-instance`example displays information about a deployment instance that is associated with the specified deployment.`aws deploy get-deployment-instance --deployment-id``d-QA4G4F9EX`--instance-id`i-902e9fEX`Output: `{ "instanceSummary": { "instanceId": "arn:aws:ec2:us-east-1:80398EXAMPLE:instance/i-902e9fEX", "lifecycleEvents": [ { "status": "Succeeded", "endTime": 1408480726.569, "startTime": 1408480726.437, "lifecycleEventName": "ApplicationStop" }, { "status": "Succeeded", "endTime": 1408480728.016, "startTime": 1408480727.665, "lifecycleEventName": "DownloadBundle" }, { "status": "Succeeded", "endTime": 1408480729.744, "startTime": 1408480729.125, "lifecycleEventName": "BeforeInstall" }, { "status": "Succeeded", "endTime": 1408480730.979, "startTime": 1408480730.844, "lifecycleEventName": "Install" }, { "status": "Failed", "endTime": 1408480732.603, "startTime": 1408480732.1, "lifecycleEventName": "AfterInstall" }, { "status": "Skipped", "endTime": 1408480732.606, "lifecycleEventName": "ApplicationStart" }, { "status": "Skipped", "endTime": 1408480732.606, "lifecycleEventName": "ValidateService" } ], "deploymentId": "d-QA4G4F9EX", "lastUpdatedAt": 1408480733.152, "status": "Failed" } }`- 
                    For API details, see [GetDeploymentInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-deployment-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-deployment-target`.

- **AWS CLI**
- 
            
                    **To return information about a deployment target**The following `get-deployment-target`example returns information about a deployment target that is associated with the specified deployment.`aws deploy get-deployment-target \ --deployment-id``"d-A1B2C3111"`\ --target-id`"i-a1b2c3d4e5f611111"`Output: `{ "deploymentTarget": { "deploymentTargetType": "InstanceTarget", "instanceTarget": { "lastUpdatedAt": 1556918687.504, "targetId": "i-a1b2c3d4e5f611111", "targetArn": "arn:aws:ec2:us-west-2:123456789012:instance/i-a1b2c3d4e5f611111", "status": "Succeeded", "lifecycleEvents": [ { "status": "Succeeded", "diagnostics": { "errorCode": "Success", "message": "Succeeded", "logTail": "", "scriptName": "" }, "lifecycleEventName": "ApplicationStop", "startTime": 1556918592.162, "endTime": 1556918592.247 }, { "status": "Succeeded", "diagnostics": { "errorCode": "Success", "message": "Succeeded", "logTail": "", "scriptName": "" }, "lifecycleEventName": "DownloadBundle", "startTime": 1556918593.193, "endTime": 1556918593.981 }, { "status": "Succeeded", "diagnostics": { "errorCode": "Success", "message": "Succeeded", "logTail": "", "scriptName": "" }, "lifecycleEventName": "BeforeInstall", "startTime": 1556918594.805, "endTime": 1556918681.807 }, { "status": "Succeeded", "diagnostics": { "errorCode": "Success", "message": "Succeeded", "logTail": "", "scriptName": "" }, "lifecycleEventName": "Install", "startTime": 1556918682.696, "endTime": 1556918683.005 }, { "status": "Succeeded", "diagnostics": { "errorCode": "Success", "message": "Succeeded", "logTail": "", "scriptName": "" }, "lifecycleEventName": "AfterInstall", "startTime": 1556918684.135, "endTime": 1556918684.216 }, { "status": "Succeeded", "diagnostics": { "errorCode": "Success", "message": "Succeeded", "logTail": "", "scriptName": "" }, "lifecycleEventName": "ApplicationStart", "startTime": 1556918685.211, "endTime": 1556918685.295 }, { "status": "Succeeded", "diagnostics": { "errorCode": "Success", "message": "Succeeded", "logTail": "", "scriptName": "" }, "lifecycleEventName": "ValidateService", "startTime": 1556918686.65, "endTime": 1556918686.747 } ], "deploymentId": "d-A1B2C3111" } } }`For more information, see [GetDeploymentTarget](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetDeploymentTarget.html)in the*AWS CodeDeploy API Reference*.- 
                    For API details, see [GetDeploymentTarget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-deployment-target.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-deployment`.

- **AWS CLI**
- 
            
                    **To get information about a deployment**The following `get-deployment`example displays information about a deployment that is associated with the user's AWS account.`aws deploy get-deployment --deployment-id``d-A1B2C3123`Output: `{ "deploymentInfo": { "applicationName": "WordPress_App", "status": "Succeeded", "deploymentOverview": { "Failed": 0, "InProgress": 0, "Skipped": 0, "Succeeded": 1, "Pending": 0 }, "deploymentConfigName": "CodeDeployDefault.OneAtATime", "creator": "user", "description": "My WordPress app deployment", "revision": { "revisionType": "S3", "s3Location": { "bundleType": "zip", "eTag": "\"dd56cfdEXAMPLE8e768f9d77fEXAMPLE\"", "bucket": "amzn-s3-demo-bucket", "key": "WordPressApp.zip" } }, "deploymentId": "d-A1B2C3123", "deploymentGroupName": "WordPress_DG", "createTime": 1409764576.589, "completeTime": 1409764596.101, "ignoreApplicationStopFailures": false } }`- 
                    For API details, see [GetDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-deployment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-on-premises-instance`.

- **AWS CLI**
- 
            
                    **To get information about an on-premises instance**The following `get-on-premises-instance`example retrieves information about the specified on-premises instance.`aws deploy get-on-premises-instance --instance-name``AssetTag12010298EX`Output: `{ "instanceInfo": { "iamUserArn": "arn:aws:iam::123456789012:user/AWS/CodeDeploy/AssetTag12010298EX", "tags": [ { "Value": "CodeDeployDemo-OnPrem", "Key": "Name" } ], "instanceName": "AssetTag12010298EX", "registerTime": 1425579465.228, "instanceArn": "arn:aws:codedeploy:us-east-1:123456789012:instance/AssetTag12010298EX_4IwLNI2Alh" } }`- 
                    For API details, see [GetOnPremisesInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-on-premises-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `install`.

- **AWS CLI**
- 
            
                    **To install an on-premises instance**The following `install`example copies the on-premises configuration file from the specified location on the instance to the location on the instance that the AWS CodeDeploy Agent expects to find it. It also installs the AWS CodeDeploy Agent on the instance. It does not create any IAM user, nor register the on-premises instance with AWS CodeDeploy, nor associate any on-premises instance tags in AWS CodeDeploy for the instance.`aws deploy install \ --override-config \ --config-file C:\temp\codedeploy.onpremises.yml \ --region``us-west-2`\ --agent-installer`s3://aws-codedeploy-us-west-2/latest/codedeploy-agent.msi`Output: `Creating the on-premises instance configuration file... DONE Installing the AWS CodeDeploy Agent... DONE`- 
                    For API details, see [Install](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/install.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-application-revisions`.

- **AWS CLI**
- 
            
                    **To get information about application revisions**The following `list-application-revisions`example displays information about all application revisions that are associated with the specified application.`aws deploy list-application-revisions \ --application-name``WordPress_App`\ --s-3-bucket`amzn-s3-demo-bucket`\ --deployed`exclude`\ --s-3-key-prefix`WordPress_`\ --sort-by`lastUsedTime`\ --sort-order`descending`Output: `{ "revisions": [ { "revisionType": "S3", "s3Location": { "version": "uTecLusvCB_JqHFXtfUcyfV8bEXAMPLE", "bucket": "amzn-s3-demo-bucket", "key": "WordPress_App.zip", "bundleType": "zip" } }, { "revisionType": "S3", "s3Location": { "version": "tMk.UxgDpMEVb7V187ZM6wVAWEXAMPLE", "bucket": "amzn-s3-demo-bucket", "key": "WordPress_App_2-0.zip", "bundleType": "zip" } } ] }`- 
                    For API details, see [ListApplicationRevisions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-application-revisions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-applications`.

- **AWS CLI**
- 
            
                    **To get information about applications**The following `list-applications`example displays information about all applications that are associated with the user's AWS account.`aws deploy list-applications`Output: `{ "applications": [ "WordPress_App", "MyOther_App" ] }`- 
                    For API details, see [ListApplications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-applications.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-deployment-configs`.

- **AWS CLI**
- 
            
                    **To get information about deployment configurations**The following `list-deployment-configs`example displays information about all deployment configurations that are associated with the user's AWS account.`aws deploy list-deployment-configs`Output: `{ "deploymentConfigsList": [ "ThreeQuartersHealthy", "CodeDeployDefault.AllAtOnce", "CodeDeployDefault.HalfAtATime", "CodeDeployDefault.OneAtATime" ] }`- 
                    For API details, see [ListDeploymentConfigs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-deployment-configs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-deployment-groups`.

- **AWS CLI**
- 
            
                    **To get information about deployment groups**The following `list-deployment-groups`example displays information about all deployment groups that are associated with the specified application.`aws deploy list-deployment-groups --application-name``WordPress_App`Output: `{ "applicationName": "WordPress_App", "deploymentGroups": [ "WordPress_DG", "WordPress_Beta_DG" ] }`- 
                    For API details, see [ListDeploymentGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-deployment-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-deployment-instances`.

- **AWS CLI**
- 
            
                    **To get information about deployment instances**The following `list-deployment-instances`example displays information about all deployment instances that are associated with the specified deployment.`aws deploy list-deployment-instances \ --deployment-id``d-A1B2C3111`\ --instance-status-filter`Succeeded`Output: `{ "instancesList": [ "i-EXAMPLE11", "i-EXAMPLE22" ] }`- 
                    For API details, see [ListDeploymentInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-deployment-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-deployment-targets`.

- **AWS CLI**
- 
            
                    **To retrieve a list of target IDs that are associated with a deployment**The following `list-deployment-targets`example retrieves a list of target IDs associated with deployments that have a status of "Failed" or "InProgress."`aws deploy list-deployment-targets \ --deployment-id``"d-A1B2C3111"`\ --target-filters "{\"TargetStatus\":[\"Failed\",\"InProgress\"]}"Output: `{ "targetIds": [ "i-0f1558aaf90e5f1f9" ] }`For more information, see [ListDeploymentTargets](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListDeploymentTargets.html)in the*AWS CodeDeploy API Reference*.- 
                    For API details, see [ListDeploymentTargets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-deployment-targets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-deployments`.

- **AWS CLI**
- 
            
                    **To get information about deployments**The following `list-deployments`example displays information about all deployments that are associated with the specified application and deployment group.`aws deploy list-deployments \ --application-name``WordPress_App`\ --create-time-range`start=2014-08-19T00:00:00,end=2014-08-20T00:00:00`\ --deployment-group-name`WordPress_DG`\ --include-only-statuses`Failed`Output: `{ "deployments": [ "d-EXAMPLE11", "d-EXAMPLE22", "d-EXAMPLE33" ] }`- 
                    For API details, see [ListDeployments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-deployments.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-git-hub-account-token-names`.

- **AWS CLI**
- 
            
                    **To lists the names of stored connections to GitHub accounts**The following `list-git-hub-account-token-names`example lists the names of the stored connections to GitHub accounts for the current AWS user.`aws deploy list-git-hub-account-token-names`Output: `{ "tokenNameList": [ "my-first-token", "my-second-token", "my-third-token" ] }`For more information, see [ListGitHubAccountTokenNames](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListGitHubAccountTokenNames.html)in the*AWS CodeDeploy API Reference*.- 
                    For API details, see [ListGitHubAccountTokenNames](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-git-hub-account-token-names.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-on-premises-instances`.

- **AWS CLI**
- 
            
                    **To get information about one or more on-premises instances**The following `list-on-premises-instances`example retrieves a list of available on-premises instance names for instances that are registered in AWS CodeDeploy and also have the specified on-premises instance tag associated in AWS CodeDeploy with the instance.`aws deploy list-on-premises-instances \ --registration-status``Registered`\ --tag-filters`Key=Name,Value=CodeDeployDemo-OnPrem,Type=KEY_AND_VALUE`Output: `{ "instanceNames": [ "AssetTag12010298EX" ] }`- 
                    For API details, see [ListOnPremisesInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-on-premises-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list tags for a resource (application)**The following `list-tags-for-resource`example lists the tags applied to an application named testApp in CodeDeploy.`aws deploy list-tags-for-resource \ --resource-arn``arn:aws:codedeploy:us-west-2:111122223333:application:testApp`Output: `{ "Tags": [ { "Key": "Type", "Value": "testType" }, { "Key": "Name", "Value": "testName" } ] }`For more information, see [Tagging instances for deployment groups in CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-tagging.html)in the*AWS CodeDeploy User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `push`.

- **AWS CLI**
- 
            
                    **To bundle and deploy an AWS CodeDeploy compatible application revision to Amazon S3**The following `push`example bundles and deploys an application revision to Amazon S3 and then associates the application revision with the specified application.`aws deploy push \ --application-name``WordPress_App`\ --description`"This is my deployment"`\ --ignore-hidden-files \ --s3-location`s3://amzn-s3-demo-bucket/WordPressApp.zip`\ --source`/tmp/MyLocalDeploymentFolder/`The output describes how to use the `create-deployment`command to create a deployment that uses the uploaded application revision.`To deploy with this revision, run: aws deploy create-deployment --application-name WordPress_App --deployment-config-name <deployment-config-name> --deployment-group-name <deployment-group-name> --s3-location bucket=amzn-s3-demo-bucket,key=WordPressApp.zip,bundleType=zip,eTag="cecc9b8EXAMPLE50a6e71fdb88EXAMPLE",version=LFsJAUdEXAMPLEfvKtvi79L8EXAMPLE`- 
                    For API details, see [Push](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/push.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-application-revision`.

- **AWS CLI**
- 
            
                    **To register information about an already-uploaded application revision**The following `register-application-revision`example registers information about an already-uploaded application revision stored in Amazon S3 with AWS CodeDeploy.`aws deploy register-application-revision \ --application-name``WordPress_App`\ --description`"Revised WordPress application"`\ --s3-location`bucket=amzn-s3-demo-bucket,key=RevisedWordPressApp.zip,bundleType=zip,eTag=cecc9b8a08eac650a6e71fdb88EXAMPLE`This command produces no output. - 
                    For API details, see [RegisterApplicationRevision](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/register-application-revision.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-on-premises-instance`.

- **AWS CLI**
- 
            
                    **To register an on-premises instance**The following `register-on-premises-instance`example registers an on-premises instance with AWS CodeDeploy. It does not create the specified IAM user, nor does it associate in AWS CodeDeploy any on-premises instances tags with the registered instance.`aws deploy register-on-premises-instance \ --instance-name``AssetTag12010298EX`\ --iam-user-arn`arn:aws:iam::80398EXAMPLE:user/CodeDeployDemoUser-OnPrem`This command produces no output. - 
                    For API details, see [RegisterOnPremisesInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/register-on-premises-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register`.

- **AWS CLI**
- 
            
                    **To register an on-premises instance**The following `register`example registers an on-premises instance with AWS CodeDeploy, associates in AWS CodeDeploy the specified on-premises instance tag with the registered instance, and creates an on-premises configuration file that can be copied to the instance. It does not create the IAM user, nor does it install the AWS CodeDeploy Agent on the instance.`aws deploy register \ --instance-name``AssetTag12010298EX`\ --iam-user-arn`arn:aws:iam::80398EXAMPLE:user/CodeDeployUser-OnPrem`\ --tags`Key=Name,Value=CodeDeployDemo-OnPrem`\ --region`us-west-2`Output: `Registering the on-premises instance... DONE Adding tags to the on-premises instance... DONE Copy the on-premises configuration file named codedeploy.onpremises.yml to the on-premises instance, and run the following command on the on-premises instance to install and configure the AWS CodeDeploy Agent: aws deploy install --config-file codedeploy.onpremises.yml`- 
                    For API details, see [Register](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/register.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-tags-from-on-premises-instances`.

- **AWS CLI**
- 
            
                    **To remove tags from one or more on-premises instances**The following `remove-tags-from-on-premises-instances`example disassociates the specified on-premises tags in AWS CodeDeploy from on-premises instances. It does not deregister the on-premises instances in AWS CodeDeploy, nor uninstall the AWS CodeDeploy Agent from the instance, nor remove the on-premises configuration file from the instances, nor delete the IAM users that are associated with the instances.`aws deploy remove-tags-from-on-premises-instances \ --instance-names``AssetTag12010298EX``AssetTag23121309EX`\ --tags`Key=Name,Value=CodeDeployDemo-OnPrem`This command produces no output. - 
                    For API details, see [RemoveTagsFromOnPremisesInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/remove-tags-from-on-premises-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-deployment`.

- **AWS CLI**
- 
            
                    **To attempt to stop a deployment**The following `stop-deployment`example attempts to stop an in-progress deployment that is associated with the user's AWS account.aws deploy stop-deployment --deployment-id d-A1B2C3111 Output: `{ "status": "Succeeded", "statusMessage": "No more commands will be scheduled for execution in the deployment instances" }`- 
                    For API details, see [StopDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/stop-deployment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To tag a resource (application)**The following `tag-resource`example adds two tags with keys Name and Type, and values testName and testType to an application named testApp in CodeDeploy.:`aws deploy tag-resource \ --resource-arn``arn:aws:codedeploy:us-west-2:111122223333:application:testApp`\ --tags`Key=Name,Value=testName``Key=Type,Value=testType`If successful, this command produces no output. For more information, see [Tagging instances for deployment groups in CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-tagging.html)in the*AWS CodeDeploy User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `uninstall`.

- **AWS CLI**
- 
            
                    **To uninstall an on-premises instance**The following `uninstall`example uninstalls the AWS CodeDeploy Agent from the on-premises instance and removes the on-premises configuration file from the instance. It doesn't deregister the instance in AWS CodeDeploy, nor disassociate any on-premises instance tags in AWS CodeDeploy from the instance, nor delete the IAM user that is associated with the instance.`aws deploy uninstall`This command produces no output. - 
                    For API details, see [Uninstall](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/uninstall.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove tags from a resource (application)**The following `untag-resource`example removes two tags with keys Name and Type from an application named testApp in CodeDeploy.`aws deploy untag-resource \ --resource-arn``arn:aws:codedeploy:us-west-2:111122223333:application:testApp`\ --tag-keys`Name``Type`If successful, this command produces no output. For more information, see [Tagging instances for deployment groups in CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-tagging.html)in the*AWS CodeDeploy User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-application`.

- **AWS CLI**
- 
            
                    **To change details of an application**The following `update-application`example changes the name of an application that is associated with the user's AWS account.`aws deploy update-application \ --application-name``WordPress_App`\ --new-application-name`My_WordPress_App`This command produces no output. - 
                    For API details, see [UpdateApplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/update-application.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-deployment-group`.

- **AWS CLI**
- 
            
                    **To change information about a deployment group**The following `update-deployment-group`example changes the settings of a deployment group that is associated with the specified application.`aws deploy update-deployment-group \ --application-name``WordPress_App`\ --auto-scaling-groups`My_CodeDeployDemo_ASG`\ --current-deployment-group-name`WordPress_DG`\ --deployment-config-name`CodeDeployDefault.AllAtOnce`\ --ec2-tag-filters`Key=Name,Type=KEY_AND_VALUE,Value=My_CodeDeployDemo`\ --new-deployment-group-name`My_WordPress_DepGroup`\ --service-role-arn`arn:aws:iam::80398EXAMPLE:role/CodeDeployDemo-2`This command produces no output. - 
                    For API details, see [UpdateDeploymentGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/update-deployment-group.html)in*AWS CLI Command Reference*.
 
-