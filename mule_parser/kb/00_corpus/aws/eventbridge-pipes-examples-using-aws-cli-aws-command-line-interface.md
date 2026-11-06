# EventBridge Pipes examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_pipes_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_pipes_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with EventBridge Pipes.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-pipe`.

- **AWS CLI**
- 
            
                    **To Create a pipe**The following `create-pipe`example creates a Pipe named`Demo_Pipe`with SQS as the source and CloudWatch Log Group as the target for the Pipe.`aws pipes create-pipe \ --name``Demo_Pipe`\ --desired-state`RUNNING`\ --role-arn`arn:aws:iam::123456789012:role/service-role/Amazon_EventBridge_Pipe_Demo_Pipe_28b3aa4f`\ --source`arn:aws:sqs:us-east-1:123456789012:Demo_Queue`\ --target`arn:aws:logs:us-east-1:123456789012:log-group:/aws/pipes/Demo_LogGroup`Output: `{ "Arn": "arn:aws:pipes:us-east-1:123456789012:pipe/Demo_Pipe", "Name": "Demo_Pipe", "DesiredState": "RUNNING", "CurrentState": "CREATING", "CreationTime": "2024-10-08T12:33:59-05:00", "LastModifiedTime": "2024-10-08T12:33:59.684839-05:00" }`For more information, see [Amazon EventBridge Pipes concepts](https://docs.aws.amazon.com/eventbridge/latest/userguide/pipes-concepts.html)in the*Amazon EventBridge User Guide*.- 
                    For API details, see [CreatePipe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pipes/create-pipe.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-pipe`.

- **AWS CLI**
- 
            
                    **To delete an existing pipe**The following `delete-pipe`example deletes a Pipe named`Demo_Pipe`in the specified account.`aws pipes delete-pipe \ --name``Demo_Pipe`Output: `{ "Arn": "arn:aws:pipes:us-east-1:123456789012:pipe/Demo_Pipe", "Name": "Demo_Pipe", "DesiredState": "STOPPED", "CurrentState": "DELETING", "CreationTime": "2024-10-08T09:29:10-05:00", "LastModifiedTime": "2024-10-08T11:57:22-05:00" }`For more information, see [Amazon EventBridge Pipes concepts](https://docs.aws.amazon.com/eventbridge/latest/userguide/pipes-concepts.html)in the*Amazon EventBridge User Guide*.- 
                    For API details, see [DeletePipe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pipes/delete-pipe.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-pipe`.

- **AWS CLI**
- 
            
                    **To retrieve information about a Pipe**The following `describe-pipe`example displays information about the Pipe`Demo_Pipe`in the specified account.`aws pipes describe-pipe \ --name``Demo_Pipe`Output: `{ "Arn": "arn:aws:pipes:us-east-1:123456789012:pipe/Demo_Pipe", "Name": "Demo_Pipe", "DesiredState": "RUNNING", "CurrentState": "RUNNING", "StateReason": "User initiated", "Source": "arn:aws:sqs:us-east-1:123456789012:Demo_Queue", "SourceParameters": { "SqsQueueParameters": { "BatchSize": 1 } }, "EnrichmentParameters": {}, "Target": "arn:aws:logs:us-east-1:123456789012:log-group:/aws/pipes/Demo_LogGroup", "TargetParameters": {}, "RoleArn": "arn:aws:iam::123456789012:role/service-role/Amazon_EventBridge_Pipe_Demo_Pipe_28b3aa4f", "Tags": {}, "CreationTime": "2024-10-08T09:29:10-05:00", "LastModifiedTime": "2024-10-08T10:23:47-05:00", "LogConfiguration": { "CloudwatchLogsLogDestination": { "LogGroupArn": "arn:aws:logs:us-east-1:123456789012:log-group:/aws/vendedlogs/pipes/Demo_Pipe" }, "Level": "ERROR" } }`For more information, see [Amazon EventBridge Pipes concepts](https://docs.aws.amazon.com/eventbridge/latest/userguide/pipes-concepts.html)in the*Amazon EventBridge User Guide*.- 
                    For API details, see [DescribePipe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pipes/describe-pipe.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-pipes`.

- **AWS CLI**
- 
            
                    **To retrieve a list of Pipes**The following `list-pipes`example shows all the pipes in the specified account.`aws pipes list-pipes`Output: `{ "Pipes": [ { "Name": "Demo_Pipe", "Arn": "arn:aws:pipes:us-east-1:123456789012:pipe/Demo_Pipe", "DesiredState": "RUNNING", "CurrentState": "RUNNING", "StateReason": "User initiated", "CreationTime": "2024-10-08T09:29:10-05:00", "LastModifiedTime": "2024-10-08T10:23:47-05:00", "Source": "arn:aws:sqs:us-east-1:123456789012:Demo_Queue", "Target": "arn:aws:logs:us-east-1:123456789012:log-group:/aws/pipes/Demo_LogGroup" } ] }`For more information, see [Amazon EventBridge Pipes concepts](https://docs.aws.amazon.com/eventbridge/latest/userguide/pipes-concepts.html)in the*Amazon EventBridge User Guide*.- 
                    For API details, see [ListPipes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pipes/list-pipes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list the tags associated with an existing pipe**The following `list-tags-for-resource`example lists all the tags associated with a pipe named`Demo_Pipe`in the specified account.`aws pipes list-tags-for-resource \ --resource-arn``arn:aws:pipes:us-east-1:123456789012:pipe/Demo_Pipe`Output: `{ "tags": { "stack": "Production", "team": "DevOps" } }`For more information, see [Amazon EventBridge Pipes concepts](https://docs.aws.amazon.com/eventbridge/latest/userguide/pipes-concepts.html)in the*Amazon EventBridge User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pipes/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-pipe`.

- **AWS CLI**
- 
            
                    **To start an existing pipe**The following `start-pipe`example starts a Pipe named`Demo_Pipe`in the specified account.`aws pipes start-pipe \ --name``Demo_Pipe`Output: `{ "Arn": "arn:aws:pipes:us-east-1:123456789012:pipe/Demo_Pipe", "Name": "Demo_Pipe", "DesiredState": "RUNNING", "CurrentState": "STARTING", "CreationTime": "2024-10-08T09:29:10-05:00", "LastModifiedTime": "2024-10-08T10:17:24-05:00" }`For more information, see [Starting or stopping an Amazon EventBridge pipe](https://docs.aws.amazon.com/eventbridge/latest/userguide/pipes-start-stop.html)in the*Amazon EventBridge User Guide*.- 
                    For API details, see [StartPipe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pipes/start-pipe.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-pipe`.

- **AWS CLI**
- 
            
                    **To stop an existing pipe**The following `stop-pipe`example stops a Pipe named`Demo_Pipe`in the specified account.`aws pipes stop-pipe \ --name``Demo_Pipe`Output: `{ "Arn": "arn:aws:pipes:us-east-1:123456789012:pipe/Demo_Pipe", "Name": "Demo_Pipe", "DesiredState": "STOPPED", "CurrentState": "STOPPING", "CreationTime": "2024-10-08T09:29:10-05:00", "LastModifiedTime": "2024-10-08T09:29:49-05:00" }`For more information, see [Starting or stopping an Amazon EventBridge pipe](https://docs.aws.amazon.com/eventbridge/latest/userguide/pipes-start-stop.html)in the*Amazon EventBridge User Guide*.- 
                    For API details, see [StopPipe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pipes/stop-pipe.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To Tag an existing pipe**The following `tag-resource`example tags a Pipe named`Demo_Pipe`. If the command succeeds, no output is returned.`aws pipes tag-resource \ --resource-arn``arn:aws:pipes:us-east-1:123456789012:pipe/Demo_Pipe`\ --tags`stack=Production`For more information, see [Amazon EventBridge Pipes concepts](https://docs.aws.amazon.com/eventbridge/latest/userguide/pipes-concepts.html)in the*Amazon EventBridge User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pipes/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove a Tag from an existing pipe**The following `untag-resource`example removes a tag with the key`stack`from the Pipe named`Demo_Pipe`. If the command succeeds, no output is returned.`aws pipes untag-resource \ --resource-arn``arn:aws:pipes:us-east-1:123456789012:pipe/Demo_Pipe`\ --tag-keys`stack`For more information, see [Amazon EventBridge Pipes concepts](https://docs.aws.amazon.com/eventbridge/latest/userguide/pipes-concepts.html)in the*Amazon EventBridge User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pipes/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-pipe`.

- **AWS CLI**
- 
            
                    **To update an existing pipe**The following `update-pipe`example updates the Pipe named`Demo_Pipe`by adding a CloudWatch Log configuration parameter, enure to update the execution role of the pipe so that it has the correct permissions for Log destination.`aws pipes update-pipe \ --name``Demo_Pipe`\ --desired-state`RUNNING`\ --log-configuration`CloudwatchLogsLogDestination={LogGroupArn=arn:aws:logs:us-east-1:123456789012:log-group:/aws/vendedlogs/pipes/Demo_Pipe},Level=TRACE`\ --role-arn`arn:aws:iam::123456789012:role/service-role/Amazon_EventBridge_Pipe_Demo_Pipe_28b3aa4f`Output: `{ "Arn": "arn:aws:pipes:us-east-1:123456789012:pipe/Demo_Pipe", "Name": "Demo_Pipe", "DesiredState": "RUNNING", "CurrentState": "UPDATING", "CreationTime": "2024-10-08T09:29:10-05:00", "LastModifiedTime": "2024-10-08T11:35:48-05:00" }`For more information, see [Amazon EventBridge Pipes concepts](https://docs.aws.amazon.com/eventbridge/latest/userguide/pipes-concepts.html)in the*Amazon EventBridge User Guide*.- 
                    For API details, see [UpdatePipe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pipes/update-pipe.html)in*AWS CLI Command Reference*.
 
-