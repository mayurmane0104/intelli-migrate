# AWS FIS examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_fis_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_fis_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS FIS.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-experiment-template`.

- **AWS CLI**
- 
            
                    **To create an experiment template**The following `create-experiment-template`example creates an experiment template in your AWS FIS account.`aws fis create-experiment-template \ --cli-input-json``file://myfile.json`Contents of `myfile.json`:`{ "description": "experimentTemplate", "stopConditions": [ { "source": "aws:cloudwatch:alarm", "value": "arn:aws:cloudwatch:us-west-2:123456789012:alarm:alarmName" } ], "targets": { "Instances-Target-1": { "resourceType": "aws:ec2:instance", "resourceArns": [ "arn:aws:ec2:us-west-2:123456789012:instance/i-12a3b4c56d78e9012" ], "selectionMode": "ALL" } }, "actions": { "reboot": { "actionId": "aws:ec2:reboot-instances", "description": "reboot", "parameters": {}, "targets": { "Instances": "Instances-Target-1" } } }, "roleArn": "arn:aws:iam::123456789012:role/myRole" }`Output: `{ "experimentTemplate": { "id": "ABCDE1fgHIJkLmNop", "description": "experimentTemplate", "targets": { "Instances-Target-1": { "resourceType": "aws:ec2:instance", "resourceArns": [ "arn:aws:ec2:us-west-2:123456789012:instance/i-12a3b4c56d78e9012" ], "selectionMode": "ALL" } }, "actions": { "reboot": { "actionId": "aws:ec2:reboot-instances", "description": "reboot", "parameters": {}, "targets": { "Instances": "Instances-Target-1" } } }, "stopConditions": [ { "source": "aws:cloudwatch:alarm", "value": "arn:aws:cloudwatch:us-west-2:123456789012:alarm:alarmName" } ], "creationTime": 1616434850.659, "lastUpdateTime": 1616434850.659, "roleArn": "arn:aws:iam::123456789012:role/myRole", "tags": {} } }`For more information, see [Create an experiment template](https://docs.aws.amazon.com/fis/latest/userguide/working-with-templates.html#create-template)in the*AWS Fault Injection Simulator User Guide*.- 
                    For API details, see [CreateExperimentTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/create-experiment-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-experiment-template`.

- **AWS CLI**
- 
            
                    **To delete an experiment template**The following `delete-experiment-template`example deletes the specified experiment template.`aws fis delete-experiment-template \ --id``ABCDE1fgHIJkLmNop`Output: `{ "experimentTemplate": { "id": "ABCDE1fgHIJkLmNop", "description": "myExperimentTemplate", "targets": { "Instances-Target-1": { "resourceType": "aws:ec2:instance", "resourceArns": [ "arn:aws:ec2:us-west-2:123456789012:instance/i-12a3b4c56d78e9012" ], "selectionMode": "ALL" } }, "actions": { "testaction": { "actionId": "aws:ec2:stop-instances", "parameters": {}, "targets": { "Instances": "Instances-Target-1" } } }, "stopConditions": [ { "source": "none" } ], "creationTime": 1616017191.124, "lastUpdateTime": 1616017859.607, "roleArn": "arn:aws:iam::123456789012:role/FISRole" } }`For more information, see [Delete an experiment template](https://docs.aws.amazon.com/fis/latest/userguide/working-with-templates.html#delete-template)in the*AWS Fault Injection Simulator User Guide*.- 
                    For API details, see [DeleteExperimentTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/delete-experiment-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-action`.

- **AWS CLI**
- 
            
                    **To get action details**The following `get-action`example gets the details of the specified action.`aws fis get-action \ --id``aws:ec2:stop-instances`Output: `{ "action": { "id": "aws:ec2:stop-instances", "description": "Stop the specified EC2 instances.", "parameters": { "startInstancesAfterDuration": { "description": "The time to wait before restarting the instances (ISO 8601 duration).", "required": false } }, "targets": { "Instances": { "resourceType": "aws:ec2:instance" } }, "tags": {} } }`For more information, see [Actions](https://docs.aws.amazon.com/fis/latest/userguide/actions.html)in the*AWS Fault Injection Simulator User Guide*.- 
                    For API details, see [GetAction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/get-action.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-experiment-template`.

- **AWS CLI**
- 
            
                    **To get experiment template details**The following `get-experiment-template`example gets the details of the specified experiment template.`aws fis get-experiment-template \ --id``ABCDE1fgHIJkLmNop`Output: `{ "experimentTemplate": { "id": "ABCDE1fgHIJkLmNop", "description": "myExperimentTemplate", "targets": { "Instances-Target-1": { "resourceType": "aws:ec2:instance", "resourceArns": [ "arn:aws:ec2:us-west-2:123456789012:instance/i-12a3b4c56d78e9012" ], "selectionMode": "ALL" } }, "actions": { "testaction": { "actionId": "aws:ec2:stop-instances", "parameters": {}, "targets": { "Instances": "Instances-Target-1" } } }, "stopConditions": [ { "source": "none" } ], "creationTime": 1616017191.124, "lastUpdateTime": 1616017331.51, "roleArn": "arn:aws:iam::123456789012:role/FISRole", "tags": { "key: "value" } } }`For more information, see [Experiment templates](https://docs.aws.amazon.com/fis/latest/userguide/experiment-templates.html)in the*AWS Fault Injection Simulator User Guide*.- 
                    For API details, see [GetExperimentTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/get-experiment-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-experiment`.

- **AWS CLI**
- 
            
                    **To get experiment details**The following `get-experiment`example gets the details of the specified experiment.`aws fis get-experiment \ --id``ABC12DeFGhI3jKLMNOP`Output: `{ "experiment": { "id": "ABC12DeFGhI3jKLMNOP", "experimentTemplateId": "ABCDE1fgHIJkLmNop", "roleArn": "arn:aws:iam::123456789012:role/myRole", "state": { "status": "completed", "reason": "Experiment completed." }, "targets": { "Instances-Target-1": { "resourceType": "aws:ec2:instance", "resourceArns": [ "arn:aws:ec2:us-west-2:123456789012:instance/i-12a3b4c56d78e9012" ], "selectionMode": "ALL" } }, "actions": { "reboot": { "actionId": "aws:ec2:reboot-instances", "parameters": {}, "targets": { "Instances": "Instances-Target-1" }, "state": { "status": "completed", "reason": "Action was completed." } } }, "stopConditions": [ { "source": "none" } ], "creationTime": 1616432509.662, "startTime": 1616432509.962, "endTime": 1616432522.307, "tags": {} } }`For more information, see [Experiments for AWS FIS](https://docs.aws.amazon.com/fis/latest/userguide/experiments.html)in the*AWS Fault Injection Simulator User Guide*.- 
                    For API details, see [GetExperiment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/get-experiment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-actions`.

- **AWS CLI**
- 
            
                    **To list actions**The following `list-actions`example lists the available actions.`aws fis list-actions`Output: `{ "actions": [ { "id": "aws:ec2:reboot-instances", "description": "Reboot the specified EC2 instances.", "targets": { "Instances": { "resourceType": "aws:ec2:instance" } }, "tags": {} }, { "id": "aws:ec2:stop-instances", "description": "Stop the specified EC2 instances.", "targets": { "Instances": { "resourceType": "aws:ec2:instance" } }, "tags": {} }, { "id": "aws:ec2:terminate-instances", "description": "Terminate the specified EC2 instances.", "targets": { "Instances": { "resourceType": "aws:ec2:instance" } }, "tags": {} }, { "id": "aws:ecs:drain-container-instances", "description": "Drain percentage of underlying EC2 instances on an ECS cluster.", "targets": { "Clusters": { "resourceType": "aws:ecs:cluster" } }, "tags": {} }, { "id": "aws:eks:terminate-nodegroup-instances", "description": "Terminates a percentage of the underlying EC2 instances in an EKS cluster.", "targets": { "Nodegroups": { "resourceType": "aws:eks:nodegroup" } }, "tags": {} }, { "id": "aws:fis:inject-api-internal-error", "description": "Cause an AWS service to return internal error responses for specific callers and operations.", "targets": { "Roles": { "resourceType": "aws:iam:role" } }, "tags": {} }, { "id": "aws:fis:inject-api-throttle-error", "description": "Cause an AWS service to return throttled responses for specific callers and operations.", "targets": { "Roles": { "resourceType": "aws:iam:role" } }, "tags": {} }, { "id": "aws:fis:inject-api-unavailable-error", "description": "Cause an AWS service to return unavailable error responses for specific callers and operations.", "targets": { "Roles": { "resourceType": "aws:iam:role" } }, "tags": {} }, { "id": "aws:fis:wait", "description": "Wait for the specified duration. Stop condition monitoring will continue during this time.", "tags": {} }, { "id": "aws:rds:failover-db-cluster", "description": "Failover a DB Cluster to one of the replicas.", "targets": { "Clusters": { "resourceType": "aws:rds:cluster" } }, "tags": {} }, { "id": "aws:rds:reboot-db-instances", "description": "Reboot the specified DB instances.", "targets": { "DBInstances": { "resourceType": "aws:rds:db" } }, "tags": {} }, { "id": "aws:ssm:send-command", "description": "Run the specified SSM document.", "targets": { "Instances": { "resourceType": "aws:ec2:instance" } }, "tags": {} } ] }`For more information, see [Actions](https://docs.aws.amazon.com/fis/latest/userguide/actions.html)in the*AWS Fault Injection Simulator User Guide*.- 
                    For API details, see [ListActions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/list-actions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-experiment-templates`.

- **AWS CLI**
- 
            
                    **To list experiment templates**The following `list-experiment-templates`example lists the experiment templates in your AWS account.`aws fis list-experiment-templates`Output: `{ "experimentTemplates": [ { "id": "ABCDE1fgHIJkLmNop", "description": "myExperimentTemplate", "creationTime": 1616017191.124, "lastUpdateTime": 1616017191.124, "tags": { "key": "value" } } ] }`For more information, see [Experiment templates](https://docs.aws.amazon.com/fis/latest/userguide/experiment-templates.html)in the*AWS Fault Injection Simulator User Guide*.- 
                    For API details, see [ListExperimentTemplates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/list-experiment-templates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-experiments`.

- **AWS CLI**
- 
            
                    **To list experiments**The following `list-experiments`example lists the experiments in your AWS account.`aws fis list-experiments`Output: `{ "experiments": [ { "id": "ABCdeF1GHiJkLM23NO", "experimentTemplateId": "ABCDE1fgHIJkLmNop", "state": { "status": "running", "reason": "Experiment is running." }, "creationTime": 1616017341.197, "tags": { "key": "value" } } ] }`For more information, see [Experiments](https://docs.aws.amazon.com/fis/latest/userguide/experiments.html)in the*AWS Fault Injection Simulator User Guide*.- 
                    For API details, see [ListExperiments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/list-experiments.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list tags for a resource**The following `list-tags-for-resource`example lists the tags for the specified resource.`aws fis list-tags-for-resource \ --resource-arn``arn:aws:fis:us-west-2:123456789012:experiment/ABC12DeFGhI3jKLMNOP`Output: `{ "tags": { "key1": "value1", "key2": "value2" } }`For more information, see [Tag your AWS FIS resources](https://docs.aws.amazon.com/fis/latest/userguide/tagging.html)in the*AWS Fault Injection Simulator User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-experiment`.

- **AWS CLI**
- 
            
                    **To start an experiment**The following `start-experiment`example starts the specified experiment.`aws fis start-experiment \ --experiment-template-id``ABCDE1fgHIJkLmNop`Output: `{ "experiment": { "id": "ABC12DeFGhI3jKLMNOP", "experimentTemplateId": "ABCDE1fgHIJkLmNop", "roleArn": "arn:aws:iam::123456789012:role/myRole", "state": { "status": "initiating", "reason": "Experiment is initiating." }, "targets": { "Instances-Target-1": { "resourceType": "aws:ec2:instance", "resourceArns": [ "arn:aws:ec2:us-west-2:123456789012:instance/i-12a3b4c56d78e9012" ], "selectionMode": "ALL" } }, "actions": { "reboot": { "actionId": "aws:ec2:reboot-instances", "parameters": {}, "targets": { "Instances": "Instances-Target-1" }, "state": { "status": "pending", "reason": "Initial state" } } }, "stopConditions": [ { "source": "none" } ], "creationTime": 1616432464.025, "startTime": 1616432464.374, "tags": {} } }`For more information, see [Experiments for AWS FIS](https://docs.aws.amazon.com/fis/latest/userguide/experiments.html)in the*AWS Fault Injection Simulator User Guide*.- 
                    For API details, see [StartExperiment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/start-experiment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-experiment`.

- **AWS CLI**
- 
            
                    **To stop an experiment**The following `stop-experiment`example stops the specified experiment from running.`aws fis stop-experiment \ --id``ABC12DeFGhI3jKLMNOP`Output: `{ "experiment": { "id": "ABC12DeFGhI3jKLMNOP", "experimentTemplateId": "ABCDE1fgHIJkLmNop", "roleArn": "arn:aws:iam::123456789012:role/myRole", "state": { "status": "stopping", "reason": "Stopping Experiment." }, "targets": { "Instances-Target-1": { "resourceType": "aws:ec2:instance", "resourceArns": [ "arn:aws:ec2:us-west-2:123456789012:instance/i-12a3b4c56d78e9012" ], "selectionMode": "ALL" } }, "actions": { "reboot": { "actionId": "aws:ec2:reboot-instances", "parameters": {}, "targets": { "Instances": "Instances-Target-1" }, "startAfter": [ "wait" ], "state": { "status": "pending", "reason": "Initial state." } }, "wait": { "actionId": "aws:fis:wait", "parameters": { "duration": "PT5M" }, "state": { "status": "running", "reason": "" } } }, "stopConditions": [ { "source": "none" } ], "creationTime": 1616432680.927, "startTime": 1616432681.177, "tags": {} } }`For more information, see [Experiments for AWS FIS](https://docs.aws.amazon.com/fis/latest/userguide/experiments.html)in the*AWS Fault Injection Simulator User Guide*.- 
                    For API details, see [StopExperiment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/stop-experiment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To tag a resource**The following `tag-resource`example tags the specified resource.`aws fis tag-resource \ --resource-arn``arn:aws:fis:us-west-2:123456789012:experiment/ABC12DeFGhI3jKLMNOP`\ --tags`key1=value1,key2=value2`This command produces no output. For more information, see [Tag your AWS FIS resources](https://docs.aws.amazon.com/fis/latest/userguide/tagging.html)in the*AWS Fault Injection Simulator User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To untag a resource**The following `untag-resource`example removes the tags from the specified resource.`aws fis untag-resource \ --resource-arn``arn:aws:fis:us-west-2:123456789012:experiment/ABC12DeFGhI3jKLMNOP`This command produces no output. For more information, see [Tag your AWS FIS resources](https://docs.aws.amazon.com/fis/latest/userguide/tagging.html)in the*AWS Fault Injection Simulator User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-experiment-template`.

- **AWS CLI**
- 
            
                    **To update an experiment template**The following `update-experiment-template`example updates the description of the specified experiment template.`aws fis update-experiment-template \ --id``ABCDE1fgHIJkLmNop`\ ---description`myExperimentTemplate`Output: `{ "experimentTemplate": { "id": "ABCDE1fgHIJkLmNop", "description": "myExperimentTemplate", "targets": { "Instances-Target-1": { "resourceType": "aws:ec2:instance", "resourceArns": [ "arn:aws:ec2:us-west-2:123456789012:instance/i-12a3b4c56d78e9012" ], "selectionMode": "ALL" } }, "actions": { "testaction": { "actionId": "aws:ec2:stop-instances", "parameters": {}, "targets": { "Instances": "Instances-Target-1" } } }, "stopConditions": [ { "source": "none" } ], "creationTime": 1616017191.124, "lastUpdateTime": 1616017859.607, "roleArn": "arn:aws:iam::123456789012:role/FISRole", "tags": { "key": "value" } } }`For more information, see [Update an experiment template](https://docs.aws.amazon.com/fis/latest/userguide/working-with-templates.html#update-template)in the*AWS Fault Injection Simulator User Guide*.- 
                    For API details, see [UpdateExperimentTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/update-experiment-template.html)in*AWS CLI Command Reference*.
 
-