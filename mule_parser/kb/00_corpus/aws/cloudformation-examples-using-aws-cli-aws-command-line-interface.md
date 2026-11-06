# CloudFormation examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_cloudformation_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_cloudformation_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with CloudFormation.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `activate-type`.

- **AWS CLI**
- 
            
                    **To activate a type**The following `activate-type`example activates a public third-party extension, making it available for use in stack templates.`aws cloudformation activate-type \ --region``us-west-2`\ --type`RESOURCE`\ --type-name`Example::Test::1234567890abcdef0`\ --type-name-alias`Example::Test::Alias`Output: `{ "Arn": "arn:aws:cloudformation:us-west-2:123456789012:type/resource/Example-Test-Alias" }`For more information, see [Using the AWS CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html)in the*AWS CloudFormation User Guide*.- 
                    For API details, see [ActivateType](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/activate-type.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-describe-type-configurations`.

- **AWS CLI**
- 
            
                    **To batch describe a type configuration**The following `batch-describe-type-configurations`example configures the data for the type.`aws cloudformation batch-describe-type-configurations \ --region``us-west-2`\ --type-configuration-identifiers TypeArn="arn:aws:cloudformation:us-west-2:123456789012:type/resource/Example-Test-Type,TypeConfigurationAlias=MyConfiguration"Output: `{ "Errors": [], "UnprocessedTypeConfigurations": [], "TypeConfigurations": [ { "Arn": "arn:aws:cloudformation:us-west-2:123456789012:type/resource/Example-Test-Type", "Alias": "MyConfiguration", "Configuration": "{\n \"Example\": {\n \"ApiKey\": \"examplekey\",\n \"ApplicationKey\": \"examplekey1\",\n \"ApiURL\": \"exampleurl\"\n }\n}", "LastUpdated": "2021-10-01T15:25:46.210000+00:00", "TypeArn": "arn:aws:cloudformation:us-east-1:123456789012:type/resource/Example-Test-Type" } ] }`For more information, see [Using the AWS CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html)in the*AWS CloudFormation User Guide*.- 
                    For API details, see [BatchDescribeTypeConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/batch-describe-type-configurations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-update-stack`.

- **AWS CLI**
- 
            
                    **To cancel a stack update that is in progress**The following `cancel-update-stack`command cancels a stack update on the`myteststack`stack:`aws cloudformation cancel-update-stack --stack-name``myteststack`- 
                    For API details, see [CancelUpdateStack](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/cancel-update-stack.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `continue-update-rollback`.

- **AWS CLI**
- 
            
                    **To retry an update rollback**The following `continue-update-rollback`example resumes a rollback operation from a previously failed stack update.`aws cloudformation continue-update-rollback \ --stack-name``my-stack`This command produces no output. - 
                    For API details, see [ContinueUpdateRollback](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/continue-update-rollback.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-change-set`.

- **AWS CLI**
- 
            
                    **To create a change set**The following `create-change-set`example creates a change set with the`CAPABILITY_IAM`capability. The file`template.yaml`is an AWS CloudFormation template in the current folder that defines a stack that includes IAM resources.`aws cloudformation create-change-set \ --stack-name``my-application`\ --change-set-name`my-change-set`\ --template-body`file://template.yaml`\ --capabilities`CAPABILITY_IAM`Output: `{ "Id": "arn:aws:cloudformation:us-west-2:123456789012:changeSet/my-change-set/bc9555ba-a949-xmpl-bfb8-f41d04ec5784", "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-application/d0a825a0-e4cd-xmpl-b9fb-061c69e99204" }`- 
                    For API details, see [CreateChangeSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-change-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-generated-template`.

- **AWS CLI**
- 
            
                    **To create a generated template from scanned resources**The following `create-generated-template`example creates a generated template named`MyTemplate`from scanned resources.`aws cloudformation create-generated-template \ --generated-template-name``MyTemplate`\ --resources`file://resources.json`Contents of `resources.json`:`[ { "ResourceType": "AWS::EKS::Cluster", "LogicalResourceId":"MyCluster", "ResourceIdentifier": { "ClusterName": "MyAppClusterName" } }, { "ResourceType": "AWS::AutoScaling::AutoScalingGroup", "LogicalResourceId":"MyASG", "ResourceIdentifier": { "AutoScalingGroupName": "MyAppASGName" } }, { "ResourceType": "AWS::EKS::Nodegroup", "LogicalResourceId":"MyNodegroup", "ResourceIdentifier": { "NodegroupName": "MyAppNodegroupName" } }, { "ResourceType": "AWS::IAM::Role", "LogicalResourceId":"MyRole", "ResourceIdentifier": { "RoleId": "arn:aws::iam::123456789012:role/MyAppIAMRole" } } ]`Output: `{ "Arn": "arn:aws:cloudformation:us-east-1:123456789012:generatedtemplate/7fc8512c-d8cb-4e02-b266-d39c48344e48", "Name": "MyTemplate" }`For more information, see [Create a CloudFormation template from resources scanned with IaC generator](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/iac-generator-create-template-from-scanned-resources.html)in the*AWS CloudFormation User Guide*.- 
                    For API details, see [CreateGeneratedTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-generated-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-stack-instances`.

- **AWS CLI**
- 
            
                    **To create stack instances**The following `create-stack-instances`example creates instances of a stack set in two accounts and in four regions. The fault tolerance setting ensures that the update is attempted in all accounts and regions, even if some stacks cannot be created.`aws cloudformation create-stack-instances \ --stack-set-name``my-stack-set`\ --accounts`123456789012``223456789012`\ --regions`us-east-1``us-east-2``us-west-1``us-west-2`\ --operation-preferences`FailureToleranceCount=7`Output: `{ "OperationId": "d7995c31-83c2-xmpl-a3d4-e9ca2811563f" }`To create a stack set, use the `create-stack-set`command.- 
                    For API details, see [CreateStackInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-stack-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-stack-refactor`.

- **AWS CLI**
- 
            
                    **To create the stack definition for a stack refactor operation**The following `create-stack-refactor`example creates the stack definition for stack refactoring.`aws cloudformation create-stack-refactor \ --stack-definitions \``StackName=Stack1,TemplateBody@=file://template1-updated.yaml`\`StackName=Stack2,TemplateBody@=file://template2-updated.yaml`Output: `{ "StackRefactorId": "9c384f70-4e07-4ed7-a65d-fee5eb430841" }`For more information, see [Stack refactoring](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stack-refactoring.html)in the*AWS CloudFormation User Guide*.- 
                    For API details, see [CreateStackRefactor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-stack-refactor.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-stack-set`.

- **AWS CLI**
- 
            
                    **To create a stack set**The following `create-stack-set`example creates a stack set using the specified YAML file temlplate.`template.yaml`is an AWS CloudFormation template in the current folder that defines a stack.`aws cloudformation create-stack-set \ --stack-set-name``my-stack-set`\ --template-body`file://template.yaml`\ --description`"SNS topic"`Output: `{ "StackSetId": "my-stack-set:8d0f160b-d157-xmpl-a8e6-c0ce8e5d8cc1" }`To add stack instances to the stack set, use the `create-stack-instances`command.- 
                    For API details, see [CreateStackSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-stack-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-stack`.

- **AWS CLI**
- 
            
                    **To create an AWS CloudFormation stack**The following `create-stacks`command creates a stack with the name`myteststack`using the`sampletemplate.json`template:`aws cloudformation create-stack --stack-name``myteststack`--template-body`file://sampletemplate.json`--parameters`ParameterKey=KeyPairName,ParameterValue=TestKey`ParameterKey=SubnetIDs,ParameterValue=SubnetID1\\,SubnetID2Output: `{ "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/myteststack/466df9e0-0dff-08e3-8e2f-5088487c4896" }`For more information, see Stacks in the *AWS CloudFormation User Guide*.- 
                    For API details, see [CreateStack](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/create-stack.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deactivate-type`.

- **AWS CLI**
- 
            
                    **To deactivate a type**The following `deactivate-type`example deactivates a public extension that was previously activated in this account and Region.`aws cloudformation deactivate-type \ --region``us-west-2`\ --type`MODULE`\ --type-name`Example::Test::Type::MODULE`This command produces no output. For more information, see [Using the AWS CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html)in the*AWS CloudFormation User Guide*.- 
                    For API details, see [DeactivateType](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/deactivate-type.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-change-set`.

- **AWS CLI**
- 
            
                    **To delete a change set**The following `delete-change-set`example deletes a change set by specifying the change set name and stack name.`aws cloudformation delete-change-set \ --stack-name``my-stack`\ --change-set-name`my-change-set`This command produces no output. The following `delete-change-set`example deletes a change set by specifying the full ARN of the change set.`aws cloudformation delete-change-set \ --change-set-name``arn:aws:cloudformation:us-east-2:123456789012:changeSet/my-change-set/4eca1a01-e285-xmpl-8026-9a1967bfb4b0`This command produces no output. - 
                    For API details, see [DeleteChangeSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/delete-change-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-generated-template`.

- **AWS CLI**
- 
            
                    **To delete a generated template**The following `delete-generated-template`example deletes the specified template.`aws cloudformation delete-generated-template \ --generated-template-name``MyTemplate`This command produces no output. For more information, see [Generating templates from existing resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/generate-IaC.html)in the*AWS CloudFormation User Guide*.- 
                    For API details, see [DeleteGeneratedTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/delete-generated-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-stack-instances`.

- **AWS CLI**
- 
            
                    **To delete stack instances**The following `delete-stack-instances`example deletes instances of a stack set in two accounts in two regions and terminates the stacks.`aws cloudformation delete-stack-instances \ --stack-set-name``my-stack-set`\ --accounts`123456789012``567890123456`\ --regions`us-east-1``us-west-1`\ --no-retain-stacksOutput: `{ "OperationId": "ad49f10c-fd1d-413f-a20a-8de6e2fa8f27" }`To delete an empty stack set, use the `delete-stack-set`command.- 
                    For API details, see [DeleteStackInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/delete-stack-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-stack-set`.

- **AWS CLI**
- 
            
                    **To delete a stack set**The following command deletes the specified empty stack set. The stack set must be empty. `aws cloudformation delete-stack-set \ --stack-set-name``my-stack-set`This command produces no output. To delete instances from the stack set, use the `delete-stack-instances`command.- 
                    For API details, see [DeleteStackSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/delete-stack-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-stack`.

- **AWS CLI**
- 
            
                    **To delete a stack**The following `delete-stack`example deletes the specified stack.`aws cloudformation delete-stack \ --stack-name``my-stack`This command produces no output. - 
                    For API details, see [DeleteStack](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/delete-stack.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deploy`.

- **AWS CLI**
- 
            
                    Following command deploys template named `template.json`to a stack named`my-new-stack`:`aws cloudformation deploy --template-file``/path_to_template/template.json`--stack-name`my-new-stack`--parameter-overrides`Key1=Value1``Key2=Value2`--tags`Key1=Value1``Key2=Value2`- 
                    For API details, see [Deploy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/deploy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deregister-type`.

- **AWS CLI**
- 
            
                    **To deregister a type version**The following `deregister-type`example removes the specified type version from active use in the CloudFormation registry, so that it can no longer be used in CloudFormation operations.`aws cloudformation deregister-type \ --type``RESOURCE`\ --type-name`My::Logs::LogGroup`\ --version-id`00000002`This command produces no output. For more information, see [Using the CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html)in the*AWS CloudFormation Users Guide*.- 
                    For API details, see [DeregisterType](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/deregister-type.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-account-limits`.

- **AWS CLI**
- 
            
                    **To get information about your account limits**The following command retrieves a list of regional limits for the current account. `aws cloudformation describe-account-limits`Output: `{ "AccountLimits": [ { "Name": "StackLimit", "Value": 200 }, { "Name": "StackOutputsLimit", "Value": 60 }, { "Name": "ConcurrentResourcesLimit", "Value": 2500 } ] }`- 
                    For API details, see [DescribeAccountLimits](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-account-limits.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-change-set`.

- **AWS CLI**
- 
            
                    **To get information about a change set**The following `describe-change-set`example displays the details of the change set specified by change set name and stack name.`aws cloudformation describe-change-set \ --change-set-name``my-change-set`\ --stack-name`my-stack`The following `describe-change-set`example displays the details of the change set specified by the full ARN of the change set:`aws cloudformation describe-change-set \ --change-set-name``arn:aws:cloudformation:us-west-2:123456789012:changeSet/my-change-set/bc9555ba-a949-xmpl-bfb8-f41d04ec5784`Output: `{ "Changes": [ { "Type": "Resource", "ResourceChange": { "Action": "Modify", "LogicalResourceId": "function", "PhysicalResourceId": "my-function-SEZV4XMPL4S5", "ResourceType": "AWS::Lambda::Function", "Replacement": "False", "Scope": [ "Properties" ], "Details": [ { "Target": { "Attribute": "Properties", "Name": "Timeout", "RequiresRecreation": "Never" }, "Evaluation": "Static", "ChangeSource": "DirectModification" } ] } } ], "ChangeSetName": "my-change-set", "ChangeSetId": "arn:aws:cloudformation:us-west-2:123456789012:changeSet/my-change-set/4eca1a01-e285-xmpl-8026-9a1967bfb4b0", "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-stack/d0a825a0-e4cd-xmpl-b9fb-061c69e99204", "StackName": "my-stack", "Description": null, "Parameters": null, "CreationTime": "2019-10-02T05:20:56.651Z", "ExecutionStatus": "AVAILABLE", "Status": "CREATE_COMPLETE", "StatusReason": null, "NotificationARNs": [], "RollbackConfiguration": {}, "Capabilities": [ "CAPABILITY_IAM" ], "Tags": null }`- 
                    For API details, see [DescribeChangeSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-change-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-generated-template`.

- **AWS CLI**
- 
            
                    **To describe a generated template**The following `describe-generated-template`example describes the specified template.`aws cloudformation describe-generated-template \ --generated-template-name``MyTemplate`Output: `{ "GeneratedTemplateId": "arn:aws:cloudformation:us-east-1:123456789012:generatedTemplate/7d881acf-f307-4ded-910e-f8fb49b96894", "GeneratedTemplateName": "MyTemplate", "Resources": [ { "ResourceType": "AWS::EC2::SecurityGroup", "LogicalResourceId": "EC2SecurityGroup", "ResourceIdentifier": { "Id": "sg-1234567890abcdef0" }, "ResourceStatus": "COMPLETE", "ResourceStatusReason": "Resource Template complete", "Warnings": [] }, { "ResourceType": "AWS::EC2::Instance", "LogicalResourceId": "EC2Instance", "ResourceIdentifier": { "InstanceId": "i-1234567890abcdef0" }, "ResourceStatus": "COMPLETE", "ResourceStatusReason": "Resource Template complete", "Warnings": [] }, { "ResourceType": "AWS::EC2::KeyPair", "LogicalResourceId": "EC2KeyPairSshkeypair", "ResourceIdentifier": { "KeyName": "sshkeypair" }, "ResourceStatus": "COMPLETE", "ResourceStatusReason": "Resource Template complete", "Warnings": [] } ], "Status": "COMPLETE", "StatusReason": "All resources complete", "CreationTime": "2025-09-23T19:38:06.435000+00:00", "LastUpdatedTime": "2025-09-23T19:38:10.798000+00:00", "Progress": { "ResourcesSucceeded": 3, "ResourcesFailed": 0, "ResourcesProcessing": 0, "ResourcesPending": 0 }, "TemplateConfiguration": { "DeletionPolicy": "RETAIN", "UpdateReplacePolicy": "RETAIN" }, "TotalWarnings": 0 }`For more information, see [Generating templates from existing resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/generate-IaC.html)in the*AWS CloudFormation User Guide*.- 
                    For API details, see [DescribeGeneratedTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-generated-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-publisher`.

- **AWS CLI**
- 
            
                    **To describe a publisher**The following `describe-publisher`example configures the information for a publisher.`aws cloudformation describe-publisher \ --region``us-west-2`\ --publisher-id`000q6TfUovXsEMmgKowxDZLlwqr2QUsh`Output: `{ "PublisherId": "000q6TfUovXsEMmgKowxDZLlwqr2QUshd2e75c8c", "PublisherStatus": "VERIFIED", "IdentityProvider": "AWS_Marketplace", "PublisherProfile": "https://aws.amazon.com/marketplace/seller-profile?id=2c5dc1f0-17cd-4259-8e46-822a83gdtegd" }`For more information, see [Using the AWS CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html)in the*AWS CloudFormation User Guide*.- 
                    For API details, see [DescribePublisher](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-publisher.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-resource-scan`.

- **AWS CLI**
- 
            
                    **To describe a resource scan**The following `describe-resource-scan`example describes the resource scan with the specified scan ID.`aws cloudformation describe-resource-scan --region \ --resource-scan-id``arn:aws:cloudformation:us-east-1:123456789012:resourceScan/0a699f15-489c-43ca-a3ef-3e6ecfa5da60`Output: `{ "ResourceScanId": "arn:aws:cloudformation:us-east-1:123456789012:resourceScan/0a699f15-489c-43ca-a3ef-3e6ecfa5da60", "Status": "COMPLETE", "StartTime": "2025-08-21T03:10:38.485000+00:00", "EndTime": "2025-08-21T03:20:28.485000+00:00", "PercentageCompleted": 100.0, "ResourceTypes": [ "AWS::CloudFront::CachePolicy", "AWS::CloudFront::OriginRequestPolicy", "AWS::EC2::DHCPOptions", "AWS::EC2::InternetGateway", "AWS::EC2::KeyPair", "AWS::EC2::NetworkAcl", "AWS::EC2::NetworkInsightsPath", "AWS::EC2::NetworkInterface", "AWS::EC2::PlacementGroup", "AWS::EC2::Route", "AWS::EC2::RouteTable", "AWS::EC2::SecurityGroup", "AWS::EC2::Subnet", "AWS::EC2::SubnetCidrBlock", "AWS::EC2::SubnetNetworkAclAssociation", "AWS::EC2::SubnetRouteTableAssociation", ... ], "ResourcesRead": 676 }`For more information, see [Generating templates from existing resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/generate-IaC.html)in the*AWS CloudFormation User Guide*.- 
                    For API details, see [DescribeResourceScan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-resource-scan.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-stack-drift-detection-status`.

- **AWS CLI**
- 
            
                    **To check a drift detection operation's status**The following `describe-stack-drift-detection-status`example displays the status of a drift detection operation. Get the by ID running the`detect-stack-drift`command.`aws cloudformation describe-stack-drift-detection-status \ --stack-drift-detection-id``1a229160-e4d9-xmpl-ab67-0a4f93df83d4`Output: `{ "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-stack/d0a825a0-e4cd-xmpl-b9fb-061c69e99204", "StackDriftDetectionId": "1a229160-e4d9-xmpl-ab67-0a4f93df83d4", "StackDriftStatus": "DRIFTED", "DetectionStatus": "DETECTION_COMPLETE", "DriftedStackResourceCount": 1, "Timestamp": "2019-10-02T05:54:30.902Z" }`- 
                    For API details, see [DescribeStackDriftDetectionStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-drift-detection-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-stack-events`.

- **AWS CLI**
- 
            
                    **To describe stack events**The following `describe-stack-events`example displays the 2 most recent events for the specified stack.`aws cloudformation describe-stack-events \ --stack-name``my-stack`\ --max-items`2``{`"StackEvents":`[``{`"StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-stack/d0a825a0-e4cd-xmpl-b9fb-061c69e99204", "EventId": "4e1516d0-e4d6-xmpl-b94f-0a51958a168c", "StackName": "my-stack", "LogicalResourceId": "my-stack", "PhysicalResourceId": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-stack/d0a825a0-e4cd-xmpl-b9fb-061c69e99204", "ResourceType": "AWS::CloudFormation::Stack", "Timestamp": "2019-10-02T05:34:29.556Z", "ResourceStatus":`"UPDATE_COMPLETE"``},``{`"StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-stack/d0a825a0-e4cd-xmpl-b9fb-061c69e99204", "EventId": "4dd3c810-e4d6-xmpl-bade-0aaf8b31ab7a", "StackName": "my-stack", "LogicalResourceId": "my-stack", "PhysicalResourceId": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-stack/d0a825a0-e4cd-xmpl-b9fb-061c69e99204", "ResourceType": "AWS::CloudFormation::Stack", "Timestamp": "2019-10-02T05:34:29.127Z", "ResourceStatus":`"UPDATE_COMPLETE_CLEANUP_IN_PROGRESS"``}``],`"NextToken":`"eyJOZXh0VG9XMPLiOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAyfQ=="``}`- 
                    For API details, see [DescribeStackEvents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-events.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-stack-instance`.

- **AWS CLI**
- 
            
                    **To describe a stack instance**The following command describes an instance of the specified stack set in the specified account and Region. The stack set is in the current region and account, and the instance is in the `us-west-2`region in account`123456789012`.:`aws cloudformation describe-stack-instance \ --stack-set-name``my-stack-set`\ --stack-instance-account`123456789012`\ --stack-instance-region`us-west-2`Output: `{ "StackInstance": { "StackSetId": "enable-config:296a3360-xmpl-40af-be78-9341e95bf743", "Region": "us-west-2", "Account": "123456789012", "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/StackSet-enable-config-e6cac20f-xmpl-46e9-8314-53e0d4591532/4287f9a0-e615-xmpl-894a-12b31d3117be", "ParameterOverrides": [], "Status": "OUTDATED", "StatusReason": "ResourceLogicalId:ConfigBucket, ResourceType:AWS::S3::Bucket, ResourceStatusReason:You have attempted to create more buckets than allowed (Service: Amazon S3; Status Code: 400; Error Code: TooManyBuckets; Request ID: F7F21CXMPL580224; S3 Extended Request ID: egd/Fdt89BXMPLyiqbMNljVk55Yqqvi3NYW2nKLUVWhUGEhNfCmZdyj967lhriaG/dWMobSO40o=)." } }`- 
                    For API details, see [DescribeStackInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-stack-refactor`.

- **AWS CLI**
- 
            
                    **To describe a stack refactor operation**The following `describe-stack-refactor`example describes the stack refactor operation with the specified stack refactor ID.`aws cloudformation describe-stack-refactor \ --stack-refactor-id``9c384f70-4e07-4ed7-a65d-fee5eb430841`Output: `{ "StackRefactorId": "9c384f70-4e07-4ed7-a65d-fee5eb430841", "StackIds": [ "arn:aws:cloudformation:us-east-1:123456789012:stack/Stack1/3e6a1ff0-94b1-11f0-aa6f-0a88d2e03acf", "arn:aws:cloudformation:us-east-1:123456789012:stack/Stack2/5da91650-94b1-11f0-81cf-0a23500e151b" ], "ExecutionStatus": "AVAILABLE", "Status": "CREATE_COMPLETE" }`For more information, see [Stack refactoring](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stack-refactoring.html)in the*AWS CloudFormation User Guide*.- 
                    For API details, see [DescribeStackRefactor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-refactor.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-stack-resource-drifts`.

- **AWS CLI**
- 
            
                    **To get information about resources that drifted from the stack definition**The following command displays information about drifted resources for the specified stack. To initiate drift detection, use the `detect-stack-drift`command.:`aws cloudformation describe-stack-resource-drifts \ --stack-name``my-stack`The output shows an AWS Lambda function that was modified out-of-band: `{ "StackResourceDrifts": [ { "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-stack/d0a825a0-e4cd-xmpl-b9fb-061c69e99204", "LogicalResourceId": "function", "PhysicalResourceId": "my-function-SEZV4XMPL4S5", "ResourceType": "AWS::Lambda::Function", "ExpectedProperties": "{\"Description\":\"Write a file to S3.\",\"Environment\":{\"Variables\":{\"bucket\":\"my-stack-bucket-1vc62xmplgguf\"}},\"Handler\":\"index.handler\",\"MemorySize\":128,\"Role\":\"arn:aws:iam::123456789012:role/my-functionRole-HIZXMPLEOM9E\",\"Runtime\":\"nodejs10.x\",\"Tags\":[{\"Key\":\"lambda:createdBy\",\"Value\":\"SAM\"}],\"Timeout\":900,\"TracingConfig\":{\"Mode\":\"Active\"}}", "ActualProperties": "{\"Description\":\"Write a file to S3.\",\"Environment\":{\"Variables\":{\"bucket\":\"my-stack-bucket-1vc62xmplgguf\"}},\"Handler\":\"index.handler\",\"MemorySize\":256,\"Role\":\"arn:aws:iam::123456789012:role/my-functionRole-HIZXMPLEOM9E\",\"Runtime\":\"nodejs10.x\",\"Tags\":[{\"Key\":\"lambda:createdBy\",\"Value\":\"SAM\"}],\"Timeout\":22,\"TracingConfig\":{\"Mode\":\"Active\"}}", "PropertyDifferences": [ { "PropertyPath": "/MemorySize", "ExpectedValue": "128", "ActualValue": "256", "DifferenceType": "NOT_EQUAL" }, { "PropertyPath": "/Timeout", "ExpectedValue": "900", "ActualValue": "22", "DifferenceType": "NOT_EQUAL" } ], "StackResourceDriftStatus": "MODIFIED", "Timestamp": "2019-10-02T05:54:44.064Z" } ] }`- 
                    For API details, see [DescribeStackResourceDrifts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-resource-drifts.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-stack-resource`.

- **AWS CLI**
- 
            
                    **To get information about a stack resource**The following `describe-stack-resource`example displays details for the resource named`MyFunction`in the specified stack.`aws cloudformation describe-stack-resource \ --stack-name``MyStack`\ --logical-resource-id`MyFunction`Output: `{ "StackResourceDetail": { "StackName": "MyStack", "StackId": "arn:aws:cloudformation:us-east-2:123456789012:stack/MyStack/d0a825a0-e4cd-xmpl-b9fb-061c69e99204", "LogicalResourceId": "MyFunction", "PhysicalResourceId": "my-function-SEZV4XMPL4S5", "ResourceType": "AWS::Lambda::Function", "LastUpdatedTimestamp": "2019-10-02T05:34:27.989Z", "ResourceStatus": "UPDATE_COMPLETE", "Metadata": "{}", "DriftInformation": { "StackResourceDriftStatus": "IN_SYNC" } } }`- 
                    For API details, see [DescribeStackResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-stack-resources`.

- **AWS CLI**
- 
            
                    **To get information about a stack resource**The following `describe-stack-resources`example displays details for the resources in the specified stack.`aws cloudformation describe-stack-resources \ --stack-name``my-stack`Output: `{ "StackResources": [ { "StackName": "my-stack", "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-stack/d0a825a0-e4cd-xmpl-b9fb-061c69e99204", "LogicalResourceId": "bucket", "PhysicalResourceId": "my-stack-bucket-1vc62xmplgguf", "ResourceType": "AWS::S3::Bucket", "Timestamp": "2019-10-02T04:34:11.345Z", "ResourceStatus": "CREATE_COMPLETE", "DriftInformation": { "StackResourceDriftStatus": "IN_SYNC" } }, { "StackName": "my-stack", "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-stack/d0a825a0-e4cd-xmpl-b9fb-061c69e99204", "LogicalResourceId": "function", "PhysicalResourceId": "my-function-SEZV4XMPL4S5", "ResourceType": "AWS::Lambda::Function", "Timestamp": "2019-10-02T05:34:27.989Z", "ResourceStatus": "UPDATE_COMPLETE", "DriftInformation": { "StackResourceDriftStatus": "IN_SYNC" } }, { "StackName": "my-stack", "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-stack/d0a825a0-e4cd-xmpl-b9fb-061c69e99204", "LogicalResourceId": "functionRole", "PhysicalResourceId": "my-functionRole-HIZXMPLEOM9E", "ResourceType": "AWS::IAM::Role", "Timestamp": "2019-10-02T04:34:06.350Z", "ResourceStatus": "CREATE_COMPLETE", "DriftInformation": { "StackResourceDriftStatus": "IN_SYNC" } } ] }`- 
                    For API details, see [DescribeStackResources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-resources.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-stack-set-operation`.

- **AWS CLI**
- 
            
                    **To get information about a stack set operation**The following describe-stack-set-operation` example displays details for an update operation on the specified stack set. `aws cloudformation describe-stack-set-operation \ --stack-set-name``enable-config`\ --operation-id`35d45ebc-ed88-xmpl-ab59-0197a1fc83a0`Output: `{ "StackSetOperation": { "OperationId": "35d45ebc-ed88-xmpl-ab59-0197a1fc83a0", "StackSetId": "enable-config:296a3360-xmpl-40af-be78-9341e95bf743", "Action": "UPDATE", "Status": "SUCCEEDED", "OperationPreferences": { "RegionOrder": [ "us-east-1", "us-west-2", "eu-west-1", "us-west-1" ], "FailureToleranceCount": 7, "MaxConcurrentCount": 2 }, "AdministrationRoleARN": "arn:aws:iam::123456789012:role/AWSCloudFormationStackSetAdministrationRole", "ExecutionRoleName": "AWSCloudFormationStackSetExecutionRole", "CreationTimestamp": "2019-10-03T16:28:44.377Z", "EndTimestamp": "2019-10-03T16:42:08.607Z" } }`- 
                    For API details, see [DescribeStackSetOperation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-set-operation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-stack-set`.

- **AWS CLI**
- 
            
                    **To get information about a stack set**The following describe-stack-set` example displays details about the specified stack set. `aws cloudformation describe-stack-set \ --stack-set-name``my-stack-set`Output: `{ "StackSet": { "StackSetName": "my-stack-set", "StackSetId": "my-stack-set:296a3360-xmpl-40af-be78-9341e95bf743", "Description": "Create an Amazon SNS topic", "Status": "ACTIVE", "TemplateBody": "AWSTemplateFormatVersion: '2010-09-09'\nDescription: An AWS SNS topic\nResources:\n topic:\n Type: AWS::SNS::Topic", "Parameters": [], "Capabilities": [], "Tags": [], "StackSetARN": "arn:aws:cloudformation:us-west-2:123456789012:stackset/enable-config:296a3360-xmpl-40af-be78-9341e95bf743", "AdministrationRoleARN": "arn:aws:iam::123456789012:role/AWSCloudFormationStackSetAdministrationRole", "ExecutionRoleName": "AWSCloudFormationStackSetExecutionRole" } }`- 
                    For API details, see [DescribeStackSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-stacks`.

- **AWS CLI**
- 
            
                    **To describe AWS CloudFormation stacks**The following `describe-stacks`command shows summary information for the`myteststack`stack:`aws cloudformation describe-stacks --stack-name``myteststack`Output: `{ "Stacks": [ { "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/myteststack/466df9e0-0dff-08e3-8e2f-5088487c4896", "Description": "AWS CloudFormation Sample Template S3_Bucket: Sample template showing how to create a publicly accessible S3 bucket. **WARNING** This template creates an S3 bucket. You will be billed for the AWS resources used if you create a stack from this template.", "Tags": [], "Outputs": [ { "Description": "Name of S3 bucket to hold website content", "OutputKey": "BucketName", "OutputValue": "myteststack-s3bucket-jssofi1zie2w" } ], "StackStatusReason": null, "CreationTime": "2013-08-23T01:02:15.422Z", "Capabilities": [], "StackName": "myteststack", "StackStatus": "CREATE_COMPLETE", "DisableRollback": false } ] }`For more information, see Stacks in the *AWS CloudFormation User Guide*.- 
                    For API details, see [DescribeStacks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stacks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-type-registration`.

- **AWS CLI**
- 
            
                    **To display type registration information**The following `describe-type-registration`example displays information about the specified type registration, including the type's current status, type, and version.`aws cloudformation describe-type-registration \ --registration-token``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "ProgressStatus": "COMPLETE", "TypeArn": "arn:aws:cloudformation:us-west-2:123456789012:type/resource/My-Logs-LogGroup", "Description": "Deployment is currently in DEPLOY_STAGE of status COMPLETED; ", "TypeVersionArn": "arn:aws:cloudformation:us-west-2:123456789012:type/resource/My-Logs-LogGroup/00000001" }`For more information, see [Using the CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html)in the*AWS CloudFormation Users Guide*.- 
                    For API details, see [DescribeTypeRegistration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-type-registration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-type`.

- **AWS CLI**
- 
            
                    **To display type information**The following `describe-type`example displays information for the specified type.`aws cloudformation describe-type \ --type-name``My::Logs::LogGroup`\ --type`RESOURCE`Output: `{ "SourceUrl": "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-logs.git", "Description": "Customized resource derived from AWS::Logs::LogGroup", "TimeCreated": "2019-12-03T23:29:33.321Z", "Visibility": "PRIVATE", "TypeName": "My::Logs::LogGroup", "LastUpdated": "2019-12-03T23:29:33.321Z", "DeprecatedStatus": "LIVE", "ProvisioningType": "FULLY_MUTABLE", "Type": "RESOURCE", "Arn": "arn:aws:cloudformation:us-west-2:123456789012:type/resource/My-Logs-LogGroup/00000001", "Schema": "[details omitted]" }`For more information, see [Using the CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html)in the*AWS CloudFormation Users Guide*.- 
                    For API details, see [DescribeType](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-type.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detect-stack-drift`.

- **AWS CLI**
- 
            
                    **To detect drifted resources**The following `detect-stack-drift`example initiates drift detection for the specified stack.`aws cloudformation detect-stack-drift \ --stack-name``my-stack`Output: `{ "StackDriftDetectionId": "1a229160-e4d9-xmpl-ab67-0a4f93df83d4" }`You can then use this ID with the `describe-stack-resource-drifts`command to describe drifted resources.- 
                    For API details, see [DetectStackDrift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/detect-stack-drift.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detect-stack-resource-drift`.

- **AWS CLI**
- 
            
                    **To detect drift for a resource**The following `detect-stack-resource-drift`example checks a resource named`MyFunction`in a stack named`MyStack`for drift:`aws cloudformation detect-stack-resource-drift \ --stack-name``MyStack`\ --logical-resource-id`MyFunction`The output shows an AWS Lambda function that was modified out-of-band: `{ "StackResourceDrift": { "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/MyStack/d0a825a0-e4cd-xmpl-b9fb-061c69e99204", "LogicalResourceId": "MyFunction", "PhysicalResourceId": "my-function-SEZV4XMPL4S5", "ResourceType": "AWS::Lambda::Function", "ExpectedProperties": "{\"Description\":\"Write a file to S3.\",\"Environment\":{\"Variables\":{\"bucket\":\"my-stack-bucket-1vc62xmplgguf\"}},\"Handler\":\"index.handler\",\"MemorySize\":128,\"Role\":\"arn:aws:iam::123456789012:role/my-functionRole-HIZXMPLEOM9E\",\"Runtime\":\"nodejs10.x\",\"Tags\":[{\"Key\":\"lambda:createdBy\",\"Value\":\"SAM\"}],\"Timeout\":900,\"TracingConfig\":{\"Mode\":\"Active\"}}", "ActualProperties": "{\"Description\":\"Write a file to S3.\",\"Environment\":{\"Variables\":{\"bucket\":\"my-stack-bucket-1vc62xmplgguf\"}},\"Handler\":\"index.handler\",\"MemorySize\":256,\"Role\":\"arn:aws:iam::123456789012:role/my-functionRole-HIZXMPLEOM9E\",\"Runtime\":\"nodejs10.x\",\"Tags\":[{\"Key\":\"lambda:createdBy\",\"Value\":\"SAM\"}],\"Timeout\":22,\"TracingConfig\":{\"Mode\":\"Active\"}}", "PropertyDifferences": [ { "PropertyPath": "/MemorySize", "ExpectedValue": "128", "ActualValue": "256", "DifferenceType": "NOT_EQUAL" }, { "PropertyPath": "/Timeout", "ExpectedValue": "900", "ActualValue": "22", "DifferenceType": "NOT_EQUAL" } ], "StackResourceDriftStatus": "MODIFIED", "Timestamp": "2019-10-02T05:58:47.433Z" } }`- 
                    For API details, see [DetectStackResourceDrift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/detect-stack-resource-drift.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detect-stack-set-drift`.

- **AWS CLI**
- 
            
                    **To detect drift on a stack set and all associated stack instances**The following `detect-stack-set-drift`example initiates drift detection operations on the specified stack set, including all the stack instances associated with that stack set, and returns an operation ID that can be used to track the status of the drift operation.`aws cloudformation detect-stack-set-drift \ --stack-set-name``stack-set-drift-example`Output: `{ "OperationId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }`For more information, see [Detecting Unmanaged Configuration Changes in Stack Sets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html)in the*AWS CloudFormation Users Guide*.- 
                    For API details, see [DetectStackSetDrift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/detect-stack-set-drift.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `estimate-template-cost`.

- **AWS CLI**
- 
            
                    **To estimate template cost**The following `estimate-template-cost`example generates a cost estimate for a template named`template.yaml`in the current folder.`aws cloudformation estimate-template-cost \ --template-body``file://template.yaml`Output: `{ "Url": "http://calculator.s3.amazonaws.com/calc5.html?key=cloudformation/7870825a-xmpl-4def-92e7-c4f8dd360cca" }`- 
                    For API details, see [EstimateTemplateCost](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/estimate-template-cost.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `execute-change-set`.

- **AWS CLI**
- 
            
                    **To execute a change set**The following `execute-change-set`example executes a change set specified by change set name and stack name.`aws cloudformation execute-change-set \ --change-set-name``my-change-set`\ --stack-name`my-stack`The following `execute-change-set`example executes a change set specified by the full ARN of the change set.`aws cloudformation execute-change-set \ --change-set-name``arn:aws:cloudformation:us-west-2:123456789012:changeSet/my-change-set/bc9555ba-a949-xmpl-bfb8-f41d04ec5784`- 
                    For API details, see [ExecuteChangeSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/execute-change-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `execute-stack-refactor`.

- **AWS CLI**
- 
            
                    **To complete a stack refactor operation**The following `execute-stack-refactor`example completes the stack refactor operation with the specified stack refactor ID.`aws cloudformation execute-stack-refactor \ --stack-refactor-id``9c384f70-4e07-4ed7-a65d-fee5eb430841`This command produces no output. For more information, see [Stack refactoring](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stack-refactoring.html)in the*AWS CloudFormation User Guide*.- 
                    For API details, see [ExecuteStackRefactor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/execute-stack-refactor.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-stack-policy`.

- **AWS CLI**
- 
            
                    **To view a stack policy**The following `get-stack-policy`example displays the stack policy for the specified stack. To attach a policy to a stack, use the`set-stack-policy`command.`aws cloudformation get-stack-policy \ --stack-name``my-stack`Output: `{ "StackPolicyBody": "{\n \"Statement\" : [\n {\n \"Effect\" : \"Allow\",\n \"Action\" : \"Update:*\",\n \"Principal\": \"*\",\n \"Resource\" : \"*\"\n },\n {\n \"Effect\" : \"Deny\",\n \"Action\" : \"Update:*\",\n \"Principal\": \"*\",\n \"Resource\" : \"LogicalResourceId/bucket\"\n }\n ]\n}\n" }`- 
                    For API details, see [GetStackPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/get-stack-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-template-summary`.

- **AWS CLI**
- 
            
                    **To display a template summary**The following command displays summary information about the resources and metadata for the specified template file. `aws cloudformation get-template-summary \ --template-body``file://template.yaml`Output: `{ "Parameters": [], "Description": "A VPC and subnets.", "ResourceTypes": [ "AWS::EC2::VPC", "AWS::EC2::Subnet", "AWS::EC2::Subnet", "AWS::EC2::RouteTable", "AWS::EC2::VPCEndpoint", "AWS::EC2::SubnetRouteTableAssociation", "AWS::EC2::SubnetRouteTableAssociation", "AWS::EC2::VPCEndpoint" ], "Version": "2010-09-09" }`- 
                    For API details, see [GetTemplateSummary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/get-template-summary.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-template`.

- **AWS CLI**
- 
            
                    **To view the template body for an AWS CloudFormation stack**The following `get-template`command shows the template for the`myteststack`stack:`aws cloudformation get-template --stack-name``myteststack`Output: `{ "TemplateBody": { "AWSTemplateFormatVersion": "2010-09-09", "Outputs": { "BucketName": { "Description": "Name of S3 bucket to hold website content", "Value": { "Ref": "S3Bucket" } } }, "Description": "AWS CloudFormation Sample Template S3_Bucket: Sample template showing how to create a publicly accessible S3 bucket. **WARNING** This template creates an S3 bucket. You will be billed for the AWS resources used if you create a stack from this template.", "Resources": { "S3Bucket": { "Type": "AWS::S3::Bucket", "Properties": { "AccessControl": "PublicRead" } } } } }`- 
                    For API details, see [GetTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/get-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-change-sets`.

- **AWS CLI**
- 
            
                    **To list change sets**The following `list-change-sets`example displays a list of the pending change sets for the specified stack.`aws cloudformation list-change-sets \ --stack-name``my-stack`Output: `{ "Summaries": [ { "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-stack/d0a825a0-e4cd-xmpl-b9fb-061c69e99204", "StackName": "my-stack", "ChangeSetId": "arn:aws:cloudformation:us-west-2:123456789012:changeSet/my-change-set/70160340-7914-xmpl-bcbf-128a1fa78b5d", "ChangeSetName": "my-change-set", "ExecutionStatus": "AVAILABLE", "Status": "CREATE_COMPLETE", "CreationTime": "2019-10-02T05:38:54.297Z" } ] }`- 
                    For API details, see [ListChangeSets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-change-sets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-exports`.

- **AWS CLI**
- 
            
                    **To list exports**The following `list-exports`example displays a list of the exports from stacks in the current region.`aws cloudformation list-exports`Output: `{ "Exports": [ { "ExportingStackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/private-vpc/99764070-b56c-xmpl-bee8-062a88d1d800", "Name": "private-vpc-subnet-a", "Value": "subnet-07b410xmplddcfa03" }, { "ExportingStackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/private-vpc/99764070-b56c-xmpl-bee8-062a88d1d800", "Name": "private-vpc-subnet-b", "Value": "subnet-075ed3xmplebd2fb1" }, { "ExportingStackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/private-vpc/99764070-b56c-xmpl-bee8-062a88d1d800", "Name": "private-vpc-vpcid", "Value": "vpc-011d7xmpl100e9841" } ] }`- 
                    For API details, see [ListExports](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-exports.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-generated-templates`.

- **AWS CLI**
- 
            
                    **To list generated templates**The following `list-generated-templates`example lists all generated templates.`aws cloudformation list-generated-templates`Output: `{ "Summaries": [ { "GeneratedTemplateId": "arn:aws:cloudformation:us-east-1:123456789012:generatedtemplate/7fc8512c-d8cb-4e02-b266-d39c48344e48", "GeneratedTemplateName": "MyTemplate", "Status": "COMPLETE", "StatusReason": "All resources complete", "CreationTime": "2025-09-23T20:13:24.283000+00:00", "LastUpdatedTime": "2025-09-23T20:13:28.610000+00:00", "NumberOfResources": 4 }, { "GeneratedTemplateId": "arn:aws:cloudformation:us-east-1:123456789012:generatedTemplate/f10dd1c4-edc6-4823-8153-ab6112b8d051", "GeneratedTemplateName": "MyEC2InstanceTemplate", "Status": "COMPLETE", "StatusReason": "All resources complete", "CreationTime": "2024-08-08T19:35:49.790000+00:00", "LastUpdatedTime": "2024-08-08T19:35:52.207000+00:00", "NumberOfResources": 3 }, { "GeneratedTemplateId": "arn:aws:cloudformation:us-east-1:123456789012:generatedTemplate/e5a1c89f-7ce2-41bd-9bdf-75b7c852e3ca", "GeneratedTemplateName": "MyEKSNodeGroupTemplate", "Status": "COMPLETE", "StatusReason": "All resources complete", "CreationTime": "2024-07-16T20:39:27.883000+00:00", "LastUpdatedTime": "2024-07-16T20:39:35.766000+00:00", "NumberOfResources": 4 } ] }`For more information, see [Generating templates from existing resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/generate-IaC.html)in the*AWS CloudFormation User Guide*.- 
                    For API details, see [ListGeneratedTemplates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-generated-templates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-imports`.

- **AWS CLI**
- 
            
                    **To list imports**The following `list-imports`example lists the stacks that import the specified export. To get the list of available exports, use the`list-exports`command.`aws cloudformation list-imports \ --export-name``private-vpc-vpcid`Output: `{ "Imports": [ "my-database-stack" ] }`- 
                    For API details, see [ListImports](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-imports.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-resource-scan-related-resources`.

- **AWS CLI**
- 
            
                    **To list related resources from a resource scan**The following `list-resource-scan-related-resources`example lists resources from the specified resource scan that are related to resources in`resources.json`.`aws cloudformation list-resource-scan-related-resources \ --resource-scan-id``arn:aws:cloudformation:us-east-1:123456789012:resourceScan/0a699f15-489c-43ca-a3ef-3e6ecfa5da60`\ --resources`file://resources.json`Contents of `resources.json`:`[ { "ResourceType": "AWS::EKS::Cluster", "ResourceIdentifier": { "ClusterName": "MyAppClusterName" } }, { "ResourceType": "AWS::AutoScaling::AutoScalingGroup", "ResourceIdentifier": { "AutoScalingGroupName": "MyAppASGName" } } ]`Output: `{ "RelatedResources": [ { "ResourceType": "AWS::EKS::Nodegroup", "ResourceIdentifier": { "NodegroupName": "MyAppNodegroupName" }, "ManagedByStack": false }, { "ResourceType": "AWS::IAM::Role", "ResourceIdentifier": { "RoleId": "arn:aws::iam::123456789012:role/MyAppIAMRole" }, "ManagedByStack": false } ] }`For more information, see [Create a CloudFormation template from resources scanned with IaC generator](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/iac-generator-create-template-from-scanned-resources.html)in the*AWS CloudFormation User Guide*.- 
                    For API details, see [ListResourceScanRelatedResources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-resource-scan-related-resources.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-resource-scan-resources`.

- **AWS CLI**
- 
            
                    **To list resources from a resource scan**The following `list-resource-scan-resources`example lists resources from the specified resource scan, filtered by resource identifier.`aws cloudformation list-resource-scan-resources \ --resource-scan-id``arn:aws:cloudformation:us-east-1:123456789012:resourceScan/0a699f15-489c-43ca-a3ef-3e6ecfa5da60`\ --resource-identifier`MyApp`Output: `{ "Resources": [ { "ResourceType": "AWS::EKS::Cluster", "ResourceIdentifier": { "ClusterName": "MyAppClusterName" }, "ManagedByStack": false }, { "ResourceType": "AWS::AutoScaling::AutoScalingGroup", "ResourceIdentifier": { "AutoScalingGroupName": "MyAppASGName" }, "ManagedByStack": false } ] }`For more information, see [Create a CloudFormation template from resources scanned with IaC generator](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/iac-generator-create-template-from-scanned-resources.html)in the*AWS CloudFormation User Guide*.- 
                    For API details, see [ListResourceScanResources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-resource-scan-resources.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-stack-instances`.

- **AWS CLI**
- 
            
                    **To list instances for a stack**The following `list-stack-instances`example lists the instances created from the specified stack set.`aws cloudformation list-stack-instances \ --stack-set-name``enable-config`The example output includes details about a stack that failed to update due to an error: `{ "Summaries": [ { "StackSetId": "enable-config:296a3360-xmpl-40af-be78-9341e95bf743", "Region": "us-west-2", "Account": "123456789012", "StackId": "arn:aws:cloudformation:ap-northeast-1:123456789012:stack/StackSet-enable-config-35a6ac50-d9f8-4084-86e4-7da34d5de4c4/a1631cd0-e5fb-xmpl-b474-0aa20f14f06e", "Status": "CURRENT" }, { "StackSetId": "enable-config:296a3360-xmpl-40af-be78-9341e95bf743", "Region": "us-west-2", "Account": "123456789012", "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/StackSet-enable-config-e6cac20f-xmpl-46e9-8314-53e0d4591532/eab53680-e5fa-xmpl-ba14-0a522351f81e", "Status": "OUTDATED", "StatusReason": "ResourceLogicalId:ConfigDeliveryChannel, ResourceType:AWS::Config::DeliveryChannel, ResourceStatusReason:Failed to put delivery channel 'StackSet-enable-config-e6cac20f-xmpl-46e9-8314-53e0d4591532-ConfigDeliveryChannel-1OJWJ7XD59WR0' because the maximum number of delivery channels: 1 is reached. (Service: AmazonConfig; Status Code: 400; Error Code: MaxNumberOfDeliveryChannelsExceededException; Request ID: d14b34a0-ef7c-xmpl-acf8-8a864370ae56)." } ] }`- 
                    For API details, see [ListStackInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stack-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-stack-refactor-actions`.

- **AWS CLI**
- 
            
                    **To list actions for a stack refactor operation**The following `list-stack-refactor-actions`example lists actions for the stack refactor operation with the specified stack refactor ID.`aws cloudformation list-stack-refactor-actions \ --stack-refactor-id``9c384f70-4e07-4ed7-a65d-fee5eb430841`Output: `{ "StackRefactorActions": [ { "Action": "MOVE", "Entity": "RESOURCE", "PhysicalResourceId": "MyTestLambdaRole", "Description": "No configuration changes detected.", "Detection": "AUTO", "TagResources": [], "UntagResources": [], "ResourceMapping": { "Source": { "StackName": "arn:aws:cloudformation:us-east-1:123456789012:stack/Stack1/3e6a1ff0-94b1-11f0-aa6f-0a88d2e03acf", "LogicalResourceId": "MyLambdaRole" }, "Destination": { "StackName": "arn:aws:cloudformation:us-east-1:123456789012:stack/Stack2/5da91650-94b1-11f0-81cf-0a23500e151b", "LogicalResourceId": "MyLambdaRole" } } }, { "Action": "MOVE", "Entity": "RESOURCE", "PhysicalResourceId": "MyTestFunction", "Description": "Resource configuration changes will be validated during refactor execution.", "Detection": "AUTO", "TagResources": [ { "Key": "aws:cloudformation:stack-name", "Value": "Stack2" }, { "Key": "aws:cloudformation:logical-id", "Value": "MyFunction" }, { "Key": "aws:cloudformation:stack-id", "Value": "arn:aws:cloudformation:us-east-1:123456789012:stack/Stack2/5da91650-94b1-11f0-81cf-0a23500e151b" } ], "UntagResources": [ "aws:cloudformation:stack-name", "aws:cloudformation:logical-id", "aws:cloudformation:stack-id" ], "ResourceMapping": { "Source": { "StackName": "arn:aws:cloudformation:us-east-1:123456789012:stack/Stack1/3e6a1ff0-94b1-11f0-aa6f-0a88d2e03acf", "LogicalResourceId": "MyFunction" }, "Destination": { "StackName": "arn:aws:cloudformation:us-east-1:123456789012:stack/Stack2/5da91650-94b1-11f0-81cf-0a23500e151b", "LogicalResourceId": "MyFunction" } } } ] }`For more information, see [Stack refactoring](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stack-refactoring.html)in the*AWS CloudFormation User Guide*.- 
                    For API details, see [ListStackRefactorActions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stack-refactor-actions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-stack-resources`.

- **AWS CLI**
- 
            
                    **To list resources in a stack**The following command displays the list of resources in the specified stack. `aws cloudformation list-stack-resources \ --stack-name``my-stack`Output: `{ "StackResourceSummaries": [ { "LogicalResourceId": "bucket", "PhysicalResourceId": "my-stack-bucket-1vc62xmplgguf", "ResourceType": "AWS::S3::Bucket", "LastUpdatedTimestamp": "2019-10-02T04:34:11.345Z", "ResourceStatus": "CREATE_COMPLETE", "DriftInformation": { "StackResourceDriftStatus": "IN_SYNC" } }, { "LogicalResourceId": "function", "PhysicalResourceId": "my-function-SEZV4XMPL4S5", "ResourceType": "AWS::Lambda::Function", "LastUpdatedTimestamp": "2019-10-02T05:34:27.989Z", "ResourceStatus": "UPDATE_COMPLETE", "DriftInformation": { "StackResourceDriftStatus": "IN_SYNC" } }, { "LogicalResourceId": "functionRole", "PhysicalResourceId": "my-functionRole-HIZXMPLEOM9E", "ResourceType": "AWS::IAM::Role", "LastUpdatedTimestamp": "2019-10-02T04:34:06.350Z", "ResourceStatus": "CREATE_COMPLETE", "DriftInformation": { "StackResourceDriftStatus": "IN_SYNC" } } ] }`- 
                    For API details, see [ListStackResources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stack-resources.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-stack-set-operation-results`.

- **AWS CLI**
- 
            
                    **To list stack set operation results**The following command displays the results of an update operation on instances in the specified stack set. `aws cloudformation list-stack-set-operation-results \ --stack-set-name``enable-config`\ --operation-id`35d45ebc-ed88-xmpl-ab59-0197a1fc83a0`Output: `{ "Summaries": [ { "Account": "223456789012", "Region": "us-west-2", "Status": "SUCCEEDED", "AccountGateResult": { "Status": "SKIPPED", "StatusReason": "Function not found: arn:aws:lambda:eu-west-1:223456789012:function:AWSCloudFormationStackSetAccountGate" } }, { "Account": "223456789012", "Region": "ap-south-1", "Status": "CANCELLED", "StatusReason": "Cancelled since failure tolerance has exceeded" } ] }`**Note:**The`SKIPPED`status for`AccountGateResult`is expected for successful operations unless you create an account gate function.- 
                    For API details, see [ListStackSetOperationResults](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stack-set-operation-results.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-stack-set-operations`.

- **AWS CLI**
- 
            
                    **To list stack set operations**The following `list-stack-set-operations`example displays the list of the most recent operations on the specified stack set.`aws cloudformation list-stack-set-operations \ --stack-set-name``my-stack-set`Output: `{ "Summaries": [ { "OperationId": "35d45ebc-ed88-xmpl-ab59-0197a1fc83a0", "Action": "UPDATE", "Status": "SUCCEEDED", "CreationTimestamp": "2019-10-03T16:28:44.377Z", "EndTimestamp": "2019-10-03T16:42:08.607Z" }, { "OperationId": "891aa98f-7118-xmpl-00b2-00954d1dd0d6", "Action": "UPDATE", "Status": "FAILED", "CreationTimestamp": "2019-10-03T15:43:53.916Z", "EndTimestamp": "2019-10-03T15:45:58.925Z" } ] }`- 
                    For API details, see [ListStackSetOperations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stack-set-operations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-stack-sets`.

- **AWS CLI**
- 
            
                    **To list stack sets**The following `list-stack-sets`example displays the list of stack sets in the current region and account.`aws cloudformation list-stack-sets`Output: `{ "Summaries": [ { "StackSetName": "enable-config", "StackSetId": "enable-config:296a3360-xmpl-40af-be78-9341e95bf743", "Description": "Enable AWS Config", "Status": "ACTIVE" } ] }`- 
                    For API details, see [ListStackSets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stack-sets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-stacks`.

- **AWS CLI**
- 
            
                    **To list AWS CloudFormation stacks**The following `list-stacks`command shows a summary of all stacks that have a status of`CREATE_COMPLETE`:`aws cloudformation list-stacks --stack-status-filter``CREATE_COMPLETE`Output: `[ { "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/myteststack/466df9e0-0dff-08e3-8e2f-5088487c4896", "TemplateDescription": "AWS CloudFormation Sample Template S3_Bucket: Sample template showing how to create a publicly accessible S3 bucket. **WARNING** This template creates an S3 bucket. You will be billed for the AWS resources used if you create a stack from this template.", "StackStatusReason": null, "CreationTime": "2013-08-26T03:27:10.190Z", "StackName": "myteststack", "StackStatus": "CREATE_COMPLETE" } ]`- 
                    For API details, see [ListStacks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stacks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-type-registrations`.

- **AWS CLI**
- 
            
                    **To list the completed registrations of a type**The following `list-type-registrations`example displays a list of the completed type registrations for the specified type.`aws cloudformation list-type-registrations \ --type``RESOURCE`\ --type-name`My::Logs::LogGroup`\ --registration-status-filter`COMPLETE`Output: `{ "RegistrationTokenList": [ "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333" ] }`For more information, see [Using the CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html)in the*AWS CloudFormation Users Guide*.- 
                    For API details, see [ListTypeRegistrations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-type-registrations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-type-versions`.

- **AWS CLI**
- 
            
                    **To list an extension's version**The following `list-type-versions`example returns summary information about the versions of an extension.`aws cloudformation list-type-versions \ --endpoint``https://example.com`\ --region`us-west-2`\ --type`RESOURCE`\ --type-name`My::Resource::Example`\ --publisher-id`123456789012`This command produces no output. For more information, see [Using the AWS CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html)in the*AWS CloudFormation User Guide*.- 
                    For API details, see [ListTypeVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-type-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-types`.

- **AWS CLI**
- 
            
                    **To list the private resource types in an account**The following `list-types`example displays a list of the private resource types currently registered in the current AWS account.`aws cloudformation list-types`Output: `{ "TypeSummaries": [ { "Description": "WordPress blog resource for internal use", "LastUpdated": "2019-12-04T18:28:15.059Z", "TypeName": "My::WordPress::BlogExample", "TypeArn": "arn:aws:cloudformation:us-west-2:123456789012:type/resource/My-WordPress-BlogExample", "DefaultVersionId": "00000005", "Type": "RESOURCE" }, { "Description": "Customized resource derived from AWS::Logs::LogGroup", "LastUpdated": "2019-12-04T18:28:15.059Z", "TypeName": "My::Logs::LogGroup", "TypeArn": "arn:aws:cloudformation:us-west-2:123456789012:type/resource/My-Logs-LogGroup", "DefaultVersionId": "00000003", "Type": "RESOURCE" } ] }`For more information, see [Using the CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html)in the*AWS CloudFormation Users Guide*.- 
                    For API details, see [ListTypes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-types.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `package`.

- **AWS CLI**
- 
            
                    Following command exports a template named `template.json`by uploading local artifacts to S3 bucket`bucket-name`and writes the exported template to`packaged-template.json`:`aws cloudformation package --template-file``/path_to_template/template.json`--s3-bucket`bucket-name`--output-template-file`packaged-template.json`--use-json- 
                    For API details, see [Package](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/package.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `publish-type`.

- **AWS CLI**
- 
            
                    **To publish an extension**The following `publish-type`example publishes the specified extension to the CloudFormation registry as a public extension in this Region.`aws cloudformation publish-type \ --region``us-west-2`\ --type`RESOURCE`\ --type-name`Example::Test::1234567890abcdef0`Output: `{ "PublicTypeArn":"arn:aws:cloudformation:us-west-2::type/resource/000q6TfUovXsEMmgKowxDZLlwqr2QUshd2e75c8c/Example-Test-1234567890abcdef0/1.0.0" }`For more information, see [Using the AWS CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html)in the*AWS CloudFormation User Guide*.- 
                    For API details, see [PublishType](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/publish-type.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-publisher`.

- **AWS CLI**
- 
            
                    **To register a publisher**The following `register-publisher`example registers a publisher and accepts the terms and condition parameter.`aws cloudformation register-publisher \ --region``us-west-2`\ --accept-terms-and-conditionsOutput: `{ "PublisherId": "000q6TfUovXsEMmgKowxDZLlwqr2QUshd2e75c8c" }`For more information, see [Using the AWS CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html)in the*AWS CloudFormation User Guide*.- 
                    For API details, see [RegisterPublisher](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/register-publisher.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-type`.

- **AWS CLI**
- 
            
                    **To register a resource type**The following `register-type`example registers the specified resource type as a private resource type in the user's account.`aws cloudformation register-type \ --type-name``My::Organization::ResourceName`\ --schema-handler-package`s3://bucket_name/my-organization-resource_name.zip`\ --type`RESOURCE`Output: `{ "RegistrationToken": "f5525280-104e-4d35-bef5-8f1f1example" }`For more information, see [Registering Resource Providers](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-register.html)in the*CloudFormation Command Line Interface User Guide for Type Development*.- 
                    For API details, see [RegisterType](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/register-type.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-stack-policy`.

- **AWS CLI**
- 
            
                    **To apply a stack policy**The following `set-stack-policy`example disables updates for the specified resource in the specified stack.`stack-policy.json`is a JSON document that defines the operations allowed on resources in the stack.`aws cloudformation set-stack-policy \ --stack-name``my-stack`\ --stack-policy-body`file://stack-policy.json`Output: `{ "Statement" : [ { "Effect" : "Allow", "Action" : "Update:*", "Principal": "*", "Resource" : "*" }, { "Effect" : "Deny", "Action" : "Update:*", "Principal": "*", "Resource" : "LogicalResourceId/bucket" } ] }`- 
                    For API details, see [SetStackPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/set-stack-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-type-configuration`.

- **AWS CLI**
- 
            
                    **To configure data**The following `set-type-configuration`example specifies the configuration data for a registered CloudFormation extension, in the given account and Region.`aws cloudformation set-type-configuration \ --region``us-west-2`\ --type`RESOURCE`\ --type-name`Example::Test::Type`\ --configuration-alias`default`\ --configuration "{\"CredentialKey\": \"testUserCredential\"}"Output: `{ "ConfigurationArn": "arn:aws:cloudformation:us-west-2:123456789012:type-configuration/resource/Example-Test-Type/default" }`For more information, see [Using the AWS CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html)in the*AWS CloudFormation User Guide*.- 
                    For API details, see [SetTypeConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/set-type-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-type-default-version`.

- **AWS CLI**
- 
            
                    **To set a type's default version**The following `set-type-default-version`example sets the specified type version to be used as the default for this type.`aws cloudformation set-type-default-version \ --type``RESOURCE`\ --type-name`My::Logs::LogGroup`\ --version-id`00000003`This command produces no output. For more information, see [Using the CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html)in the*AWS CloudFormation Users Guide*.- 
                    For API details, see [SetTypeDefaultVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/set-type-default-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `signal-resource`.

- **AWS CLI**
- 
            
                    **To signal a resource**The following `signal-resource`example signals`success`to fulfill the wait condition named`MyWaitCondition`in the stack named`my-stack`.`aws cloudformation signal-resource \ --stack-name``my-stack`\ --logical-resource-id`MyWaitCondition`\ --unique-id`1234`\ --status`SUCCESS`This command produces no output. - 
                    For API details, see [SignalResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/signal-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-resource-scan`.

- **AWS CLI**
- 
            
                    **To start a resource scan**The following `start-resource-scan`example starts a resource scan that scans all existing resources in the current account and Region.`aws cloudformation start-resource-scan`Output: `{ "ResourceScanId": "arn:aws:cloudformation:us-east-1:123456789012:resourceScan/0a699f15-489c-43ca-a3ef-3e6ecfa5da60" }`For more information, see [Start a resource scan with CloudFormation IaC generator](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/iac-generator-start-resource-scan.html)in the*AWS CloudFormation User Guide*.- 
                    For API details, see [StartResourceScan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/start-resource-scan.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-stack-set-operation`.

- **AWS CLI**
- 
            
                    **To stop a stack set operation**The following `stop-stack-set-operation`example stops an in-progess update operation on the specified stack set.`aws cloudformation stop-stack-set-operation \ --stack-set-name``my-stack-set`\ --operation-id`1261cd27-490b-xmpl-ab42-793a896c69e6`This command produces no output. - 
                    For API details, see [StopStackSetOperation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/stop-stack-set-operation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `test-type`.

- **AWS CLI**
- 
            
                    **To test an extension**The following `test-type`example tests a registered extension to make sure it meets all necessary requirements for being published in the CloudFormation registry.`aws cloudformation test-type \ --arn``arn:aws:cloudformation:us-west-2:123456789012:type/resource/Sample-Test-Resource123/00000001`Output: `{ "TypeVersionArn": "arn:aws:cloudformation:us-west-2:123456789012:type/resource/Sample-Test-Resource123/00000001" }`For more information, see [Using the AWS CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html)in the*AWS CloudFormation User Guide*.- 
                    For API details, see [TestType](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/test-type.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-stack-instances`.

- **AWS CLI**
- 
            
                    **To update stack instances**The following `update-stack-instances`example retries an update on stack instances in two accounts in two regions with the most recent settings. The specified fault tolerance setting ensures that the update is attempted in all accounts and regions, even if some stacks cannot be updated.`aws cloudformation update-stack-instances \ --stack-set-name``my-stack-set`\ --accounts`123456789012``567890123456`\ --regions`us-east-1``us-west-2`\ --operation-preferences`FailureToleranceCount=3`Output: `{ "OperationId": "103ebdf2-21ea-xmpl-8892-de5e30733132" }`- 
                    For API details, see [UpdateStackInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/update-stack-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-stack-set`.

- **AWS CLI**
- 
            
                    **To update a stack set**The following `update-stack-set`example adds a tag with the key name`Owner`and a value of`IT`to the stack instances in the specified stack set.`aws cloudformation update-stack-set \ --stack-set-name``my-stack-set`\ --use-previous-template \ --tags`Key=Owner,Value=IT`Output: `{ "OperationId": "e2b60321-6cab-xmpl-bde7-530c6f47950e" }`- 
                    For API details, see [UpdateStackSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/update-stack-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-stack`.

- **AWS CLI**
- 
            
                    **To update AWS CloudFormation stacks**The following `update-stack`command updates the template and input parameters for the`mystack`stack:`aws cloudformation update-stack --stack-name``mystack`--template-url`https://s3.amazonaws.com/sample/updated.template`--parameters`ParameterKey=KeyPairName,ParameterValue=SampleKeyPair`ParameterKey=SubnetIDs,ParameterValue=SampleSubnetID1\\,SampleSubnetID2The following `update-stack`command updates just the`SubnetIDs`parameter value for the`mystack`stack. If you don't specify a parameter value, the default value that is specified in the template is used:`aws cloudformation update-stack --stack-name``mystack`--template-url`https://s3.amazonaws.com/sample/updated.template`--parameters`ParameterKey=KeyPairName,UsePreviousValue=true`ParameterKey=SubnetIDs,ParameterValue=SampleSubnetID1\\,UpdatedSampleSubnetID2The following `update-stack`command adds two stack notification topics to the`mystack`stack:`aws cloudformation update-stack --stack-name``mystack`--use-previous-template --notification-arns`"arn:aws:sns:use-east-1:123456789012:mytopic1"``"arn:aws:sns:us-east-1:123456789012:mytopic2"`For more information, see [AWS CloudFormation stack updates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html)in the*AWS CloudFormation User Guide*.- 
                    For API details, see [UpdateStack](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/update-stack.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-termination-protection`.

- **AWS CLI**
- 
            
                    **To enable termination protection**The following `update-termination-protection`example enables termination protection on the specified stack.`aws cloudformation update-termination-protection \ --stack-name``my-stack`\ --enable-termination-protectionOutput: `{ "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-stack/d0a825a0-e4cd-xmpl-b9fb-061c69e99204" }`- 
                    For API details, see [UpdateTerminationProtection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/update-termination-protection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `validate-template`.

- **AWS CLI**
- 
            
                    **To validate an AWS CloudFormation template**The following `validate-template`command validates the`sampletemplate.json`template:`aws cloudformation validate-template --template-body``file://sampletemplate.json`Output: `{ "Description": "AWS CloudFormation Sample Template S3_Bucket: Sample template showing how to create a publicly accessible S3 bucket. **WARNING** This template creates an S3 bucket. You will be billed for the AWS resources used if you create a stack from this template.", "Parameters": [], "Capabilities": [] }`For more information, see Working with AWS CloudFormation Templates in the *AWS CloudFormation User Guide*.- 
                    For API details, see [ValidateTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/validate-template.html)in*AWS CLI Command Reference*.
 
-