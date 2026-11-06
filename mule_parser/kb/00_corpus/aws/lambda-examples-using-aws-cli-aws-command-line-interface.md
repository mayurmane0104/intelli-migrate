# Lambda examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_lambda_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_lambda_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Lambda.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `add-layer-version-permission`.

- **AWS CLI**
- 
            
                    **To add permissions to a layer version**The following `add-layer-version-permission`example grants permission for the specified account to use version 1 of the layer`my-layer`.`aws lambda add-layer-version-permission \ --layer-name``my-layer`\ --statement-id`xaccount`\ --action`lambda:GetLayerVersion`\ --principal`123456789012`\ --version-number`1`Output: `{ "RevisionId": "35d87451-f796-4a3f-a618-95a3671b0a0c", "Statement": { "Sid":"xaccount", "Effect":"Allow", "Principal":{ "AWS":"arn:aws:iam::210987654321:root" }, "Action":"lambda:GetLayerVersion", "Resource":"arn:aws:lambda:us-east-2:123456789012:layer:my-layer:1" } }`For more information, see [AWS Lambda Layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [AddLayerVersionPermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/add-layer-version-permission.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `add-permission`.

- **AWS CLI**
- 
            
                    **To add permissions to an existing Lambda function**The following `add-permission`example grants the Amazon SNS service permission to invoke a function named`my-function`.`aws lambda add-permission \ --function-name``my-function`\ --action`lambda:InvokeFunction`\ --statement-id`sns`\ --principal`sns.amazonaws.com`Output: `{ "Statement": { "Sid":"sns", "Effect":"Allow", "Principal":{ "Service":"sns.amazonaws.com" }, "Action":"lambda:InvokeFunction", "Resource":"arn:aws:lambda:us-east-2:123456789012:function:my-function" } }`For more information, see [Using Resource-based Policies for AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [AddPermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/add-permission.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-alias`.

- **AWS CLI**
- 
            
                    **To create an alias for a Lambda function**The following `create-alias`example creates an alias named`LIVE`that points to version 1 of the`my-function`Lambda function.`aws lambda create-alias \ --function-name``my-function`\ --description`"alias for live version of function"`\ --function-version`1`\ --name`LIVE`Output: `{ "FunctionVersion": "1", "Name": "LIVE", "AliasArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function:LIVE", "RevisionId": "873282ed-4cd3-4dc8-a069-d0c647e470c6", "Description": "alias for live version of function" }`For more information, see [Configuring AWS Lambda Function Aliases](https://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [CreateAlias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-alias.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-event-source-mapping`.

- **AWS CLI**
- 
            
                    **To create a mapping between an event source and an AWS Lambda function**The following `create-event-source-mapping`example creates a mapping between an SQS queue and the`my-function`Lambda function.`aws lambda create-event-source-mapping \ --function-name``my-function`\ --batch-size`5`\ --event-source-arn`arn:aws:sqs:us-west-2:123456789012:mySQSqueue`Output: `{ "UUID": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "StateTransitionReason": "USER_INITIATED", "LastModified": 1569284520.333, "BatchSize": 5, "State": "Creating", "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function", "EventSourceArn": "arn:aws:sqs:us-west-2:123456789012:mySQSqueue" }`For more information, see [AWS Lambda Event Source Mapping](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [CreateEventSourceMapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-event-source-mapping.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-function`.

- **AWS CLI**
- 
            
                    **To create a Lambda function**The following `create-function`example creates a Lambda function named`my-function`.`aws lambda create-function \ --function-name``my-function`\ --runtime`nodejs22.x`\ --zip-file`fileb://my-function.zip`\ --handler`my-function.handler`\ --role`arn:aws:iam::123456789012:role/service-role/MyTestFunction-role-tges6bf4`Contents of `my-function.zip`:`This file is a deployment package that contains your function code and any dependencies.`Output: `{ "TracingConfig": { "Mode": "PassThrough" }, "CodeSha256": "PFn4S+er27qk+UuZSTKEQfNKG/XNn7QJs90mJgq6oH8=", "FunctionName": "my-function", "CodeSize": 308, "RevisionId": "873282ed-4cd3-4dc8-a069-d0c647e470c6", "MemorySize": 128, "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function", "Version": "$LATEST", "Role": "arn:aws:iam::123456789012:role/service-role/MyTestFunction-role-zgur6bf4", "Timeout": 3, "LastModified": "2025-10-14T22:26:11.234+0000", "Handler": "my-function.handler", "Runtime": "nodejs22.x", "Description": "" }`For more information, see [Configure Lambda function memory](https://docs.aws.amazon.com/lambda/latest/dg/configuration-memory.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [CreateFunction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-function.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-alias`.

- **AWS CLI**
- 
            
                    **To delete an alias of a Lambda function**The following `delete-alias`example deletes the alias named`LIVE`from the`my-function`Lambda function.`aws lambda delete-alias \ --function-name``my-function`\ --name`LIVE`This command produces no output. For more information, see [Configuring AWS Lambda Function Aliases](https://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [DeleteAlias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-alias.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-event-source-mapping`.

- **AWS CLI**
- 
            
                    **To delete the mapping between an event source and an AWS Lambda function**The following `delete-event-source-mapping`example deletes the mapping between an SQS queue and the`my-function`Lambda function.`aws lambda delete-event-source-mapping \ --uuid``a1b2c3d4-5678-90ab-cdef-11111EXAMPLE`Output: `{ "UUID": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "StateTransitionReason": "USER_INITIATED", "LastModified": 1569285870.271, "BatchSize": 5, "State": "Deleting", "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function", "EventSourceArn": "arn:aws:sqs:us-west-2:123456789012:mySQSqueue" }`For more information, see [AWS Lambda Event Source Mapping](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [DeleteEventSourceMapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-event-source-mapping.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-function-concurrency`.

- **AWS CLI**
- 
            
                    **To remove the reserved concurrent execution limit from a function**The following `delete-function-concurrency`example deletes the reserved concurrent execution limit from the`my-function`function.`aws lambda delete-function-concurrency \ --function-name``my-function`This command produces no output. For more information, see [Reserving Concurrency for a Lambda Function](https://docs.aws.amazon.com/lambda/latest/dg/per-function-concurrency.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [DeleteFunctionConcurrency](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-function-concurrency.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-function-event-invoke-config`.

- **AWS CLI**
- 
            
                    **To delete an asynchronous invocation configuration**The following `delete-function-event-invoke-config`example deletes the asynchronous invocation configuration for the`GREEN`alias of the specified function.`aws lambda delete-function-event-invoke-config --function-name``my-function:GREEN`- 
                    For API details, see [DeleteFunctionEventInvokeConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-function-event-invoke-config.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-function`.

- **AWS CLI**
- 
            
                    **Example 1: To delete a Lambda function by function name**The following `delete-function`example deletes the Lambda function named`my-function`by specifying the function's name.`aws lambda delete-function \ --function-name``my-function`This command produces no output. **Example 2: To delete a Lambda function by function ARN**The following `delete-function`example deletes the Lambda function named`my-function`by specifying the function's ARN.`aws lambda delete-function \ --function-name``arn:aws:lambda:us-west-2:123456789012:function:my-function`This command produces no output. **Example 3: To delete a Lambda function by partial function ARN**The following `delete-function`example deletes the Lambda function named`my-function`by specifying the function's partial ARN.`aws lambda delete-function \ --function-name``123456789012:function:my-function`This command produces no output. For more information, see [AWS Lambda Function Configuration](https://docs.aws.amazon.com/lambda/latest/dg/resource-model.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [DeleteFunction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-function.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-layer-version`.

- **AWS CLI**
- 
            
                    **To delete a version of a Lambda layer**The following `delete-layer-version`example deletes version 2 of the layer named`my-layer`.`aws lambda delete-layer-version \ --layer-name``my-layer`\ --version-number`2`This command produces no output. For more information, see [AWS Lambda Layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [DeleteLayerVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-layer-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-provisioned-concurrency-config`.

- **AWS CLI**
- 
            
                    **To delete a provisioned concurrency configuration**The following `delete-provisioned-concurrency-config`example deletes the provisioned concurrency configuration for the`GREEN`alias of the specified function.`aws lambda delete-provisioned-concurrency-config \ --function-name``my-function`\ --qualifier`GREEN`- 
                    For API details, see [DeleteProvisionedConcurrencyConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-provisioned-concurrency-config.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-account-settings`.

- **AWS CLI**
- 
            
                    **To retrieve details about your account in an AWS Region**The following `get-account-settings`example displays the Lambda limits and usage information for your account.`aws lambda get-account-settings`Output: `{ "AccountLimit": { "CodeSizeUnzipped": 262144000, "UnreservedConcurrentExecutions": 1000, "ConcurrentExecutions": 1000, "CodeSizeZipped": 52428800, "TotalCodeSize": 80530636800 }, "AccountUsage": { "FunctionCount": 4, "TotalCodeSize": 9426 } }`For more information, see [AWS Lambda Limits](https://docs.aws.amazon.com/lambda/latest/dg/limits.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [GetAccountSettings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-account-settings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-alias`.

- **AWS CLI**
- 
            
                    **To retrieve details about a function alias**The following `get-alias`example displays details for the alias named`LIVE`on the`my-function`Lambda function.`aws lambda get-alias \ --function-name``my-function`\ --name`LIVE`Output: `{ "FunctionVersion": "3", "Name": "LIVE", "AliasArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function:LIVE", "RevisionId": "594f41fb-b85f-4c20-95c7-6ca5f2a92c93", "Description": "alias for live version of function" }`For more information, see [Configuring AWS Lambda Function Aliases](https://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [GetAlias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-alias.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-event-source-mapping`.

- **AWS CLI**
- 
            
                    **To retrieve details about an event source mapping**The following `get-event-source-mapping`example displays the details for the mapping between an SQS queue and the`my-function`Lambda function.`aws lambda get-event-source-mapping \ --uuid``"a1b2c3d4-5678-90ab-cdef-11111EXAMPLE"`Output: `{ "UUID": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "StateTransitionReason": "USER_INITIATED", "LastModified": 1569284520.333, "BatchSize": 5, "State": "Enabled", "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function", "EventSourceArn": "arn:aws:sqs:us-west-2:123456789012:mySQSqueue" }`For more information, see [AWS Lambda Event Source Mapping](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [GetEventSourceMapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-event-source-mapping.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-function-concurrency`.

- **AWS CLI**
- 
            
                    **To view the reserved concurrency setting for a function**The following `get-function-concurrency`example retrieves the reserved concurrency setting for the specified function.`aws lambda get-function-concurrency \ --function-name``my-function`Output: `{ "ReservedConcurrentExecutions": 250 }`- 
                    For API details, see [GetFunctionConcurrency](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function-concurrency.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-function-configuration`.

- **AWS CLI**
- 
            
                    **To retrieve the version-specific settings of a Lambda function**The following `get-function-configuration`example displays the settings for version 2 of the`my-function`function.`aws lambda get-function-configuration \ --function-name``my-function:2`Output: `{ "FunctionName": "my-function", "LastModified": "2019-09-26T20:28:40.438+0000", "RevisionId": "e52502d4-9320-4688-9cd6-152a6ab7490d", "MemorySize": 256, "Version": "2", "Role": "arn:aws:iam::123456789012:role/service-role/my-function-role-uy3l9qyq", "Timeout": 3, "Runtime": "nodejs10.x", "TracingConfig": { "Mode": "PassThrough" }, "CodeSha256": "5tT2qgzYUHaqwR716pZ2dpkn/0J1FrzJmlKidWoaCgk=", "Description": "", "VpcConfig": { "SubnetIds": [], "VpcId": "", "SecurityGroupIds": [] }, "CodeSize": 304, "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function:2", "Handler": "index.handler" }`For more information, see [AWS Lambda Function Configuration](https://docs.aws.amazon.com/lambda/latest/dg/resource-model.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [GetFunctionConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-function-event-invoke-config`.

- **AWS CLI**
- 
            
                    **To view an asynchronous invocation configuration**The following `get-function-event-invoke-config`example retrieves the asynchronous invocation configuration for the`BLUE`alias of the specified function.`aws lambda get-function-event-invoke-config \ --function-name``my-function:BLUE`Output: `{ "LastModified": 1577824396.653, "FunctionArn": "arn:aws:lambda:us-east-2:123456789012:function:my-function:BLUE", "MaximumRetryAttempts": 0, "MaximumEventAgeInSeconds": 3600, "DestinationConfig": { "OnSuccess": {}, "OnFailure": { "Destination": "arn:aws:sqs:us-east-2:123456789012:failed-invocations" } } }`- 
                    For API details, see [GetFunctionEventInvokeConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function-event-invoke-config.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-function`.

- **AWS CLI**
- 
            
                    **To retrieve information about a function**The following `get-function`example displays information about the`my-function`function.`aws lambda get-function \ --function-name``my-function`Output: `{ "Concurrency": { "ReservedConcurrentExecutions": 100 }, "Code": { "RepositoryType": "S3", "Location": "https://awslambda-us-west-2-tasks.s3.us-west-2.amazonaws.com/snapshots/123456789012/my-function..." }, "Configuration": { "TracingConfig": { "Mode": "PassThrough" }, "Version": "$LATEST", "CodeSha256": "5tT2qgzYUHoqwR616pZ2dpkn/0J1FrzJmlKidWaaCgk=", "FunctionName": "my-function", "VpcConfig": { "SubnetIds": [], "VpcId": "", "SecurityGroupIds": [] }, "MemorySize": 128, "RevisionId": "28f0fb31-5c5c-43d3-8955-03e76c5c1075", "CodeSize": 304, "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function", "Handler": "index.handler", "Role": "arn:aws:iam::123456789012:role/service-role/helloWorldPython-role-uy3l9qyq", "Timeout": 3, "LastModified": "2025-09-24T18:20:35.054+0000", "Runtime": "nodejs22.x", "Description": "" } }`For more information, see [Configure Lambda function memory](https://docs.aws.amazon.com/lambda/latest/dg/configuration-memory.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [GetFunction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-function.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-layer-version-by-arn`.

- **AWS CLI**
- 
            
                    **To retrieve information about a Lambda layer version**The following `get-layer-version-by-arn`example displays information about the layer version with the specified Amazon Resource Name (ARN).`aws lambda get-layer-version-by-arn \ --arn``"arn:aws:lambda:us-west-2:123456789012:layer:AWSLambda-Python311-SciPy1x:2"`Output: `{ "LayerVersionArn": "arn:aws:lambda:us-west-2:123456789012:layer:AWSLambda-Python311-SciPy1x:2", "Description": "AWS Lambda SciPy layer for Python 3.11 (scipy-1.1.0, numpy-1.15.4) https://github.com/scipy/scipy/releases/tag/v1.1.0 https://github.com/numpy/numpy/releases/tag/v1.15.4", "CreatedDate": "2023-10-12T10:09:38.398+0000", "LayerArn": "arn:aws:lambda:us-west-2:123456789012:layer:AWSLambda-Python311-SciPy1x", "Content": { "CodeSize": 41784542, "CodeSha256": "GGmv8ocUw4cly0T8HL0Vx/f5V4RmSCGNjDIslY4VskM=", "Location": "https://awslambda-us-west-2-layers.s3.us-west-2.amazonaws.com/snapshots/123456789012/..." }, "Version": 2, "CompatibleRuntimes": [ "python3.11" ], "LicenseInfo": "SciPy: https://github.com/scipy/scipy/blob/main/LICENSE.txt, NumPy: https://github.com/numpy/numpy/blob/main/LICENSE.txt" }`For more information, see [AWS Lambda Layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [GetLayerVersionByArn](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-layer-version-by-arn.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-layer-version-policy`.

- **AWS CLI**
- 
            
                    **To retrieve the permissions policy for a Lambda layer version**The following `get-layer-version-policy`example displays policy information about version 1 for the layer named`my-layer`.`aws lambda get-layer-version-policy \ --layer-name``my-layer`\ --version-number`1`Output: `{ "Policy": { "Version":"2012-10-17", "Id":"default", "Statement": [ { "Sid":"xaccount", "Effect":"Allow", "Principal": {"AWS":"arn:aws:iam::123456789012:root"}, "Action":"lambda:GetLayerVersion", "Resource":"arn:aws:lambda:us-west-2:123456789012:layer:my-layer:1" } ] }, "RevisionId": "c68f21d2-cbf0-4026-90f6-1375ee465cd0" }`For more information, see [AWS Lambda Layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [GetLayerVersionPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-layer-version-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-layer-version`.

- **AWS CLI**
- 
            
                    **To retrieve information about a Lambda layer version**The following `get-layer-version`example displays information for version 1 of the layer named`my-layer`.`aws lambda get-layer-version \ --layer-name``my-layer`\ --version-number`1`Output: `{ "Content": { "Location": "https://awslambda-us-east-2-layers.s3.us-east-2.amazonaws.com/snapshots/123456789012/my-layer-4aaa2fbb-ff77-4b0a-ad92-5b78a716a96a?versionId=27iWyA73cCAYqyH...", "CodeSha256": "tv9jJO+rPbXUUXuRKi7CwHzKtLDkDRJLB3cC3Z/ouXo=", "CodeSize": 169 }, "LayerArn": "arn:aws:lambda:us-east-2:123456789012:layer:my-layer", "LayerVersionArn": "arn:aws:lambda:us-east-2:123456789012:layer:my-layer:1", "Description": "My Python layer", "CreatedDate": "2018-11-14T23:03:52.894+0000", "Version": 1, "LicenseInfo": "MIT", "CompatibleRuntimes": [ "python3.10", "python3.11" ] }`For more information, see [AWS Lambda Layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [GetLayerVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-layer-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-policy`.

- **AWS CLI**
- 
            
                    **To retrieve the resource-based IAM policy for a function, version, or alias**The following `get-policy`example displays policy information about the`my-function`Lambda function.`aws lambda get-policy \ --function-name``my-function`Output: `{ "Policy": { "Version":"2012-10-17", "Id":"default", "Statement": [ { "Sid":"iot-events", "Effect":"Allow", "Principal": {"Service":"iotevents.amazonaws.com"}, "Action":"lambda:InvokeFunction", "Resource":"arn:aws:lambda:us-west-2:123456789012:function:my-function" } ] }, "RevisionId": "93017fc9-59cb-41dc-901b-4845ce4bf668" }`For more information, see [Using Resource-based Policies for AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [GetPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-provisioned-concurrency-config`.

- **AWS CLI**
- 
            
                    **To view a provisioned concurrency configuration**The following `get-provisioned-concurrency-config`example displays details for the provisioned concurrency configuration for the`BLUE`alias of the specified function.`aws lambda get-provisioned-concurrency-config \ --function-name``my-function`\ --qualifier`BLUE`Output: `{ "RequestedProvisionedConcurrentExecutions": 100, "AvailableProvisionedConcurrentExecutions": 100, "AllocatedProvisionedConcurrentExecutions": 100, "Status": "READY", "LastModified": "2019-12-31T20:28:49+0000" }`- 
                    For API details, see [GetProvisionedConcurrencyConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-provisioned-concurrency-config.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `invoke`.

- **AWS CLI**
- 
            
                    **Example 1: To invoke a Lambda function synchronously**The following `invoke`example invokes the`my-function`function synchronously. The`cli-binary-format`option is required if you're using AWS CLI version 2. For more information, see[AWS CLI supported global command line options](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-options.html#cli-configure-options-list)in the*AWS Command Line Interface User Guide*.`aws lambda invoke \ --function-name``my-function`\ --cli-binary-format`raw-in-base64-out`\ --payload '`{ "name": "Bob" }`' \`response.json`Output: `{ "ExecutedVersion": "$LATEST", "StatusCode": 200 }`For more information, see [Invoke a Lambda function synchronously](https://docs.aws.amazon.com/lambda/latest/dg/invocation-sync.html)in the*AWS Lambda Developer Guide*.**Example 2: To invoke a Lambda function asynchronously**The following `invoke`example invokes the`my-function`function asynchronously. The`cli-binary-format`option is required if you're using AWS CLI version 2. For more information, see[AWS CLI supported global command line options](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-options.html#cli-configure-options-list)in the*AWS Command Line Interface User Guide*.`aws lambda invoke \ --function-name``my-function`\ --invocation-type`Event`\ --cli-binary-format`raw-in-base64-out`\ --payload '`{ "name": "Bob" }`' \`response.json`Output: `{ "StatusCode": 202 }`For more information, see [Invoking a Lambda function asynchronously](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [Invoke](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/invoke.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-aliases`.

- **AWS CLI**
- 
            
                    **To retrieve the list of aliases for a Lambda function**The following `list-aliases`example displays a list of the aliases for the`my-function`Lambda function.`aws lambda list-aliases \ --function-name``my-function`Output: `{ "Aliases": [ { "AliasArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function:BETA", "RevisionId": "a410117f-ab16-494e-8035-7e204bb7933b", "FunctionVersion": "2", "Name": "BETA", "Description": "alias for beta version of function" }, { "AliasArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function:LIVE", "RevisionId": "21d40116-f8b1-40ba-9360-3ea284da1bb5", "FunctionVersion": "1", "Name": "LIVE", "Description": "alias for live version of function" } ] }`For more information, see [Configuring AWS Lambda Function Aliases](https://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [ListAliases](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-aliases.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-event-source-mappings`.

- **AWS CLI**
- 
            
                    **To list the event source mappings for a function**The following `list-event-source-mappings`example displays a list of the event source mappings for the`my-function`Lambda function.`aws lambda list-event-source-mappings \ --function-name``my-function`Output: `{ "EventSourceMappings": [ { "UUID": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "StateTransitionReason": "USER_INITIATED", "LastModified": 1569284520.333, "BatchSize": 5, "State": "Enabled", "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function", "EventSourceArn": "arn:aws:sqs:us-west-2:123456789012:mySQSqueue" } ] }`For more information, see [AWS Lambda Event Source Mapping](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [ListEventSourceMappings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-event-source-mappings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-function-event-invoke-configs`.

- **AWS CLI**
- 
            
                    **To view a list of asynchronous invocation configurations**The following `list-function-event-invoke-configs`example lists the asynchronous invocation configurations for the specified function.`aws lambda list-function-event-invoke-configs \ --function-name``my-function`Output: `{ "FunctionEventInvokeConfigs": [ { "LastModified": 1577824406.719, "FunctionArn": "arn:aws:lambda:us-east-2:123456789012:function:my-function:GREEN", "MaximumRetryAttempts": 2, "MaximumEventAgeInSeconds": 1800 }, { "LastModified": 1577824396.653, "FunctionArn": "arn:aws:lambda:us-east-2:123456789012:function:my-function:BLUE", "MaximumRetryAttempts": 0, "MaximumEventAgeInSeconds": 3600 } ] }`- 
                    For API details, see [ListFunctionEventInvokeConfigs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-function-event-invoke-configs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-functions`.

- **AWS CLI**
- 
            
                    **To retrieve a list of Lambda functions**The following `list-functions`example displays a list of all of the functions for the current user.`aws lambda list-functions`Output: `{ "Functions": [ { "TracingConfig": { "Mode": "PassThrough" }, "Version": "$LATEST", "CodeSha256": "dBG9m8SGdmlEjw/JYXlhhvCrAv5TxvXsbL/RMr0fT/I=", "FunctionName": "helloworld", "MemorySize": 128, "RevisionId": "1718e831-badf-4253-9518-d0644210af7b", "CodeSize": 294, "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:helloworld", "Handler": "helloworld.handler", "Role": "arn:aws:iam::123456789012:role/service-role/MyTestFunction-role-zgur6bf4", "Timeout": 3, "LastModified": "2025-09-23T18:32:33.857+0000", "Runtime": "nodejs22.x", "Description": "" }, { "TracingConfig": { "Mode": "PassThrough" }, "Version": "$LATEST", "CodeSha256": "sU0cJ2/hOZevwV/lTxCuQqK3gDZP3i8gUoqUUVRmY6E=", "FunctionName": "my-function", "VpcConfig": { "SubnetIds": [], "VpcId": "", "SecurityGroupIds": [] }, "MemorySize": 256, "RevisionId": "93017fc9-59cb-41dc-901b-4845ce4bf668", "CodeSize": 266, "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function", "Handler": "index.handler", "Role": "arn:aws:iam::123456789012:role/service-role/helloWorldPython-role-uy3l9qyq", "Timeout": 3, "LastModified": "2025-10-01T16:47:28.490+0000", "Runtime": "nodejs22.x", "Description": "" }, { "Layers": [ { "CodeSize": 41784542, "Arn": "arn:aws:lambda:us-west-2:420165488524:layer:AWSLambda-Python37-SciPy1x:2" }, { "CodeSize": 4121, "Arn": "arn:aws:lambda:us-west-2:123456789012:layer:pythonLayer:1" } ], "TracingConfig": { "Mode": "PassThrough" }, "Version": "$LATEST", "CodeSha256": "ZQukCqxtkqFgyF2cU41Avj99TKQ/hNihPtDtRcc08mI=", "FunctionName": "my-python-function", "VpcConfig": { "SubnetIds": [], "VpcId": "", "SecurityGroupIds": [] }, "MemorySize": 128, "RevisionId": "80b4eabc-acf7-4ea8-919a-e874c213707d", "CodeSize": 299, "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-python-function", "Handler": "lambda_function.lambda_handler", "Role": "arn:aws:iam::123456789012:role/service-role/my-python-function-role-z5g7dr6n", "Timeout": 3, "LastModified": "2025-10-01T19:40:41.643+0000", "Runtime": "python3.11", "Description": "" } ] }`For more information, see [Configure Lambda function memory](https://docs.aws.amazon.com/lambda/latest/dg/configuration-memory.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [ListFunctions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-functions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-layer-versions`.

- **AWS CLI**
- 
            
                    **To list the versions of an AWS Lambda layer**The following `list-layers-versions`example displays information about the versions for the layer named`my-layer`.`aws lambda list-layer-versions \ --layer-name``my-layer`Output: `{ "Layers": [ { "LayerVersionArn": "arn:aws:lambda:us-east-2:123456789012:layer:my-layer:2", "Version": 2, "Description": "My layer", "CreatedDate": "2023-11-15T00:37:46.592+0000", "CompatibleRuntimes": [ "python3.10", "python3.11" ] } ] }`For more information, see [AWS Lambda Layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [ListLayerVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-layer-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-layers`.

- **AWS CLI**
- 
            
                    **To list the layers that are compatible with your function's runtime**The following `list-layers`example displays information about layers that are compatible with the Python 3.11 runtime.`aws lambda list-layers \ --compatible-runtime``python3.11`Output: `{ "Layers": [ { "LayerName": "my-layer", "LayerArn": "arn:aws:lambda:us-east-2:123456789012:layer:my-layer", "LatestMatchingVersion": { "LayerVersionArn": "arn:aws:lambda:us-east-2:123456789012:layer:my-layer:2", "Version": 2, "Description": "My layer", "CreatedDate": "2023-11-15T00:37:46.592+0000", "CompatibleRuntimes": [ "python3.10", "python3.11" ] } } ] }`For more information, see [AWS Lambda Layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [ListLayers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-layers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-provisioned-concurrency-configs`.

- **AWS CLI**
- 
            
                    **To get a list of provisioned concurrency configurations**The following `list-provisioned-concurrency-configs`example lists the provisioned concurrency configurations for the specified function.`aws lambda list-provisioned-concurrency-configs \ --function-name``my-function`Output: `{ "ProvisionedConcurrencyConfigs": [ { "FunctionArn": "arn:aws:lambda:us-east-2:123456789012:function:my-function:GREEN", "RequestedProvisionedConcurrentExecutions": 100, "AvailableProvisionedConcurrentExecutions": 100, "AllocatedProvisionedConcurrentExecutions": 100, "Status": "READY", "LastModified": "2019-12-31T20:29:00+0000" }, { "FunctionArn": "arn:aws:lambda:us-east-2:123456789012:function:my-function:BLUE", "RequestedProvisionedConcurrentExecutions": 100, "AvailableProvisionedConcurrentExecutions": 100, "AllocatedProvisionedConcurrentExecutions": 100, "Status": "READY", "LastModified": "2019-12-31T20:28:49+0000" } ] }`- 
                    For API details, see [ListProvisionedConcurrencyConfigs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-provisioned-concurrency-configs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags`.

- **AWS CLI**
- 
            
                    **To retrieve the list of tags for a Lambda function**The following `list-tags`example displays the tags attached to the`my-function`Lambda function.`aws lambda list-tags \ --resource``arn:aws:lambda:us-west-2:123456789012:function:my-function`Output: `{ "Tags": { "Category": "Web Tools", "Department": "Sales" } }`For more information, see [Tagging Lambda Functions](https://docs.aws.amazon.com/lambda/latest/dg/tagging.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [ListTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-versions-by-function`.

- **AWS CLI**
- 
            
                    **To retrieve a list of versions of a function**The following `list-versions-by-function`example displays the list of versions for the`my-function`Lambda function.`aws lambda list-versions-by-function \ --function-name``my-function`Output: `{ "Versions": [ { "TracingConfig": { "Mode": "PassThrough" }, "Version": "$LATEST", "CodeSha256": "sU0cJ2/hOZevwV/lTxCuQqK3gDZP3i8gUoqUUVRmY6E=", "FunctionName": "my-function", "VpcConfig": { "SubnetIds": [], "VpcId": "", "SecurityGroupIds": [] }, "MemorySize": 256, "RevisionId": "93017fc9-59cb-41dc-901b-4845ce4bf668", "CodeSize": 266, "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function:$LATEST", "Handler": "index.handler", "Role": "arn:aws:iam::123456789012:role/service-role/helloWorldPython-role-uy3l9qyq", "Timeout": 3, "LastModified": "2019-10-01T16:47:28.490+0000", "Runtime": "nodejs10.x", "Description": "" }, { "TracingConfig": { "Mode": "PassThrough" }, "Version": "1", "CodeSha256": "5tT2qgzYUHoqwR616pZ2dpkn/0J1FrzJmlKidWaaCgk=", "FunctionName": "my-function", "VpcConfig": { "SubnetIds": [], "VpcId": "", "SecurityGroupIds": [] }, "MemorySize": 256, "RevisionId": "949c8914-012e-4795-998c-e467121951b1", "CodeSize": 304, "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function:1", "Handler": "index.handler", "Role": "arn:aws:iam::123456789012:role/service-role/helloWorldPython-role-uy3l9qyq", "Timeout": 3, "LastModified": "2019-09-26T20:28:40.438+0000", "Runtime": "nodejs10.x", "Description": "new version" }, { "TracingConfig": { "Mode": "PassThrough" }, "Version": "2", "CodeSha256": "sU0cJ2/hOZevwV/lTxCuQqK3gDZP3i8gUoqUUVRmY6E=", "FunctionName": "my-function", "VpcConfig": { "SubnetIds": [], "VpcId": "", "SecurityGroupIds": [] }, "MemorySize": 256, "RevisionId": "cd669f21-0f3d-4e1c-9566-948837f2e2ea", "CodeSize": 266, "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function:2", "Handler": "index.handler", "Role": "arn:aws:iam::123456789012:role/service-role/helloWorldPython-role-uy3l9qyq", "Timeout": 3, "LastModified": "2019-10-01T16:47:28.490+0000", "Runtime": "nodejs10.x", "Description": "newer version" } ] }`For more information, see [Configuring AWS Lambda Function Aliases](https://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [ListVersionsByFunction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-versions-by-function.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `publish-layer-version`.

- **AWS CLI**
- 
            
                    **To create a Lambda layer version**The following `publish-layer-version`example creates a new Python library layer version. The command retrieves the layer content a file named`layer.zip`in the specified S3 bucket.`aws lambda publish-layer-version \ --layer-name``my-layer`\ --description`"My Python layer"`\ --license-info`"MIT"`\ --content`S3Bucket=lambda-layers-us-west-2-123456789012,S3Key=layer.zip`\ --compatible-runtimes`python3.10``python3.11`Output: `{ "Content": { "Location": "https://awslambda-us-west-2-layers.s3.us-west-2.amazonaws.com/snapshots/123456789012/my-layer-4aaa2fbb-ff77-4b0a-ad92-5b78a716a96a?versionId=27iWyA73cCAYqyH...", "CodeSha256": "tv9jJO+rPbXUUXuRKi7CwHzKtLDkDRJLB3cC3Z/ouXo=", "CodeSize": 169 }, "LayerArn": "arn:aws:lambda:us-west-2:123456789012:layer:my-layer", "LayerVersionArn": "arn:aws:lambda:us-west-2:123456789012:layer:my-layer:1", "Description": "My Python layer", "CreatedDate": "2023-11-14T23:03:52.894+0000", "Version": 1, "LicenseInfo": "MIT", "CompatibleRuntimes": [ "python3.10", "python3.11" ] }`For more information, see [AWS Lambda Layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [PublishLayerVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/publish-layer-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `publish-version`.

- **AWS CLI**
- 
            
                    **To publish a new version of a function**The following `publish-version`example publishes a new version of the`my-function`Lambda function.`aws lambda publish-version \ --function-name``my-function`Output: `{ "TracingConfig": { "Mode": "PassThrough" }, "CodeSha256": "dBG9m8SGdmlEjw/JYXlhhvCrAv5TxvXsbL/RMr0fT/I=", "FunctionName": "my-function", "CodeSize": 294, "RevisionId": "f31d3d39-cc63-4520-97d4-43cd44c94c20", "MemorySize": 128, "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function:3", "Version": "2", "Role": "arn:aws:iam::123456789012:role/service-role/MyTestFunction-role-zgur6bf4", "Timeout": 3, "LastModified": "2019-09-23T18:32:33.857+0000", "Handler": "my-function.handler", "Runtime": "nodejs10.x", "Description": "" }`For more information, see [Configuring AWS Lambda Function Aliases](https://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [PublishVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/publish-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-function-concurrency`.

- **AWS CLI**
- 
            
                    **To configure a reserved concurrency limit for a function**The following `put-function-concurrency`example configures 100 reserved concurrent executions for the`my-function`function.`aws lambda put-function-concurrency \ --function-name``my-function`\ --reserved-concurrent-executions`100`Output: `{ "ReservedConcurrentExecutions": 100 }`For more information, see [Reserving Concurrency for a Lambda Function](https://docs.aws.amazon.com/lambda/latest/dg/per-function-concurrency.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [PutFunctionConcurrency](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/put-function-concurrency.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-function-event-invoke-config`.

- **AWS CLI**
- 
            
                    **To configure error handling for asynchronous invocation**The following `put-function-event-invoke-config`example sets a maximum event age of one hour and disables retries for the specified function.`aws lambda put-function-event-invoke-config \ --function-name``my-function`\ --maximum-event-age-in-seconds`3600`\ --maximum-retry-attempts`0`Output: `{ "LastModified": 1573686021.479, "FunctionArn": "arn:aws:lambda:us-east-2:123456789012:function:my-function:$LATEST", "MaximumRetryAttempts": 0, "MaximumEventAgeInSeconds": 3600, "DestinationConfig": { "OnSuccess": {}, "OnFailure": {} } }`- 
                    For API details, see [PutFunctionEventInvokeConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/put-function-event-invoke-config.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-provisioned-concurrency-config`.

- **AWS CLI**
- 
            
                    **To allocate provisioned concurrency**The following `put-provisioned-concurrency-config`example allocates 100 provisioned concurrency for the`BLUE`alias of the specified function.`aws lambda put-provisioned-concurrency-config \ --function-name``my-function`\ --qualifier`BLUE`\ --provisioned-concurrent-executions`100`Output: `{ "Requested ProvisionedConcurrentExecutions": 100, "Allocated ProvisionedConcurrentExecutions": 0, "Status": "IN_PROGRESS", "LastModified": "2019-11-21T19:32:12+0000" }`- 
                    For API details, see [PutProvisionedConcurrencyConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/put-provisioned-concurrency-config.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-layer-version-permission`.

- **AWS CLI**
- 
            
                    **To delete layer-version permissions**The following `remove-layer-version-permission`example deletes permission for an account to configure a layer version.`aws lambda remove-layer-version-permission \ --layer-name``my-layer`\ --statement-id`xaccount`\ --version-number`1`This command produces no output. For more information, see [AWS Lambda Layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [RemoveLayerVersionPermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/remove-layer-version-permission.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-permission`.

- **AWS CLI**
- 
            
                    **To remove permissions from an existing Lambda function**The following `remove-permission`example removes permission to invoke a function named`my-function`.`aws lambda remove-permission \ --function-name``my-function`\ --statement-id`sns`This command produces no output. For more information, see [Using Resource-based Policies for AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [RemovePermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/remove-permission.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add tags to an existing Lambda function**The following `tag-resource`example adds a tag with the key name`DEPARTMENT`and a value of`Department A`to the specified Lambda function.`aws lambda tag-resource \ --resource``arn:aws:lambda:us-west-2:123456789012:function:my-function`\ --tags`"DEPARTMENT=Department A"`This command produces no output. For more information, see [Tagging Lambda Functions](https://docs.aws.amazon.com/lambda/latest/dg/tagging.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove tags from an existing Lambda function**The following `untag-resource`example removes the tag with the key name`DEPARTMENT`tag from the`my-function`Lambda function.`aws lambda untag-resource \ --resource``arn:aws:lambda:us-west-2:123456789012:function:my-function`\ --tag-keys`DEPARTMENT`This command produces no output. For more information, see [Tagging Lambda Functions](https://docs.aws.amazon.com/lambda/latest/dg/tagging.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-alias`.

- **AWS CLI**
- 
            
                    **To update a function alias**The following `update-alias`example updates the alias named`LIVE`to point to version 3 of the`my-function`Lambda function.`aws lambda update-alias \ --function-name``my-function`\ --function-version`3`\ --name`LIVE`Output: `{ "FunctionVersion": "3", "Name": "LIVE", "AliasArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function:LIVE", "RevisionId": "594f41fb-b85f-4c20-95c7-6ca5f2a92c93", "Description": "alias for live version of function" }`For more information, see [Configuring AWS Lambda Function Aliases](https://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [UpdateAlias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-alias.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-event-source-mapping`.

- **AWS CLI**
- 
            
                    **To update the mapping between an event source and an AWS Lambda function**The following `update-event-source-mapping`example updates the batch size to 8 in the specified mapping.`aws lambda update-event-source-mapping \ --uuid``"a1b2c3d4-5678-90ab-cdef-11111EXAMPLE"`\ --batch-size`8`Output: `{ "UUID": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "StateTransitionReason": "USER_INITIATED", "LastModified": 1569284520.333, "BatchSize": 8, "State": "Updating", "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function", "EventSourceArn": "arn:aws:sqs:us-west-2:123456789012:mySQSqueue" }`For more information, see [AWS Lambda Event Source Mapping](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [UpdateEventSourceMapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-event-source-mapping.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-function-code`.

- **AWS CLI**
- 
            
                    **To update the code of a Lambda function**The following `update-function-code`example replaces the code of the unpublished ($LATEST) version of the`my-function`function with the contents of the specified zip file.`aws lambda update-function-code \ --function-name``my-function`\ --zip-file`fileb://my-function.zip`Output: `{ "FunctionName": "my-function", "LastModified": "2019-09-26T20:28:40.438+0000", "RevisionId": "e52502d4-9320-4688-9cd6-152a6ab7490d", "MemorySize": 256, "Version": "$LATEST", "Role": "arn:aws:iam::123456789012:role/service-role/my-function-role-uy3l9qyq", "Timeout": 3, "Runtime": "nodejs10.x", "TracingConfig": { "Mode": "PassThrough" }, "CodeSha256": "5tT2qgzYUHaqwR716pZ2dpkn/0J1FrzJmlKidWoaCgk=", "Description": "", "VpcConfig": { "SubnetIds": [], "VpcId": "", "SecurityGroupIds": [] }, "CodeSize": 304, "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function", "Handler": "index.handler" }`For more information, see [AWS Lambda Function Configuration](https://docs.aws.amazon.com/lambda/latest/dg/resource-model.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [UpdateFunctionCode](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-code.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-function-configuration`.

- **AWS CLI**
- 
            
                    **To modify the configuration of a function**The following `update-function-configuration`example modifies the memory size to be 256 MB for the unpublished ($LATEST) version of the`my-function`function.`aws lambda update-function-configuration \ --function-name``my-function`\ --memory-size`256`Output: `{ "FunctionName": "my-function", "LastModified": "2019-09-26T20:28:40.438+0000", "RevisionId": "e52502d4-9320-4688-9cd6-152a6ab7490d", "MemorySize": 256, "Version": "$LATEST", "Role": "arn:aws:iam::123456789012:role/service-role/my-function-role-uy3l9qyq", "Timeout": 3, "Runtime": "nodejs10.x", "TracingConfig": { "Mode": "PassThrough" }, "CodeSha256": "5tT2qgzYUHaqwR716pZ2dpkn/0J1FrzJmlKidWoaCgk=", "Description": "", "VpcConfig": { "SubnetIds": [], "VpcId": "", "SecurityGroupIds": [] }, "CodeSize": 304, "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function", "Handler": "index.handler" }`For more information, see [AWS Lambda Function Configuration](https://docs.aws.amazon.com/lambda/latest/dg/resource-model.html)in the*AWS Lambda Developer Guide*.- 
                    For API details, see [UpdateFunctionConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-function-event-invoke-config`.

- **AWS CLI**
- 
            
                    **To update an asynchronous invocation configuration**The following `update-function-event-invoke-config`example adds an on-failure destination to the existing asynchronous invocation configuration for the specified function.`aws lambda update-function-event-invoke-config \ --function-name``my-function`\ --destination-config '`{"OnFailure":{"Destination": "arn:aws:sqs:us-east-2:123456789012:destination"}}`'Output: `{ "LastModified": 1573687896.493, "FunctionArn": "arn:aws:lambda:us-east-2:123456789012:function:my-function:$LATEST", "MaximumRetryAttempts": 0, "MaximumEventAgeInSeconds": 3600, "DestinationConfig": { "OnSuccess": {}, "OnFailure": { "Destination": "arn:aws:sqs:us-east-2:123456789012:destination" } } }`- 
                    For API details, see [UpdateFunctionEventInvokeConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-event-invoke-config.html)in*AWS CLI Command Reference*.
 
-