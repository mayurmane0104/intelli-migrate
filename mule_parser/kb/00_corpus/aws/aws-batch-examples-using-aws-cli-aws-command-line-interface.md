# AWS Batch examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_batch_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_batch_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS Batch.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `cancel-job`.

- **AWS CLI**
- 
            
                    **To cancel a job**This example cancels a job with the specified job ID. Command: `aws batch cancel-job --job-id``bcf0b186-a532-4122-842e-2ccab8d54efb`--reason`"Cancelling job."`- 
                    For API details, see [CancelJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/cancel-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-compute-environment`.

- **AWS CLI**
- 
            
                    **To create a managed compute environment with On-Demand instances**This example creates a managed compute environment with specific C4 instance types that are launched on demand. The compute environment is called C4OnDemand. Command: `aws batch create-compute-environment --cli-input-json``file://<path_to_json_file>/C4OnDemand.json`JSON file format: `{ "computeEnvironmentName": "C4OnDemand", "type": "MANAGED", "state": "ENABLED", "computeResources": { "type": "EC2", "minvCpus": 0, "maxvCpus": 128, "desiredvCpus": 48, "instanceTypes": [ "c4.large", "c4.xlarge", "c4.2xlarge", "c4.4xlarge", "c4.8xlarge" ], "subnets": [ "subnet-220c0e0a", "subnet-1a95556d", "subnet-978f6dce" ], "securityGroupIds": [ "sg-cf5093b2" ], "ec2KeyPair": "id_rsa", "instanceRole": "ecsInstanceRole", "tags": { "Name": "Batch Instance - C4OnDemand" } }, "serviceRole": "arn:aws:iam::012345678910:role/AWSBatchServiceRole" }`Output: `{ "computeEnvironmentName": "C4OnDemand", "computeEnvironmentArn": "arn:aws:batch:us-east-1:012345678910:compute-environment/C4OnDemand" }`**To create a managed compute environment with Spot Instances**This example creates a managed compute environment with the M4 instance type that is launched when the Spot bid price is at or below 20% of the On-Demand price for the instance type. The compute environment is called M4Spot. Command: `aws batch create-compute-environment --cli-input-json``file://<path_to_json_file>/M4Spot.json`JSON file format: `{ "computeEnvironmentName": "M4Spot", "type": "MANAGED", "state": "ENABLED", "computeResources": { "type": "SPOT", "spotIamFleetRole": "arn:aws:iam::012345678910:role/aws-ec2-spot-fleet-role", "minvCpus": 0, "maxvCpus": 128, "desiredvCpus": 4, "instanceTypes": [ "m4" ], "bidPercentage": 20, "subnets": [ "subnet-220c0e0a", "subnet-1a95556d", "subnet-978f6dce" ], "securityGroupIds": [ "sg-cf5093b2" ], "ec2KeyPair": "id_rsa", "instanceRole": "ecsInstanceRole", "tags": { "Name": "Batch Instance - M4Spot" } }, "serviceRole": "arn:aws:iam::012345678910:role/AWSBatchServiceRole" }`Output: `{ "computeEnvironmentName": "M4Spot", "computeEnvironmentArn": "arn:aws:batch:us-east-1:012345678910:compute-environment/M4Spot" }`- 
                    For API details, see [CreateComputeEnvironment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/create-compute-environment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-job-queue`.

- **AWS CLI**
- 
            
                    **To create a low priority job queue with a single compute environment**This example creates a job queue called LowPriority that uses the M4Spot compute environment. Command: `aws batch create-job-queue --cli-input-json``file://<path_to_json_file>/LowPriority.json`JSON file format: `{ "jobQueueName": "LowPriority", "state": "ENABLED", "priority": 10, "computeEnvironmentOrder": [ { "order": 1, "computeEnvironment": "M4Spot" } ] }`Output: `{ "jobQueueArn": "arn:aws:batch:us-east-1:012345678910:job-queue/LowPriority", "jobQueueName": "LowPriority" }`**To create a high priority job queue with two compute environments**This example creates a job queue called HighPriority that uses the C4OnDemand compute environment with an order of 1 and the M4Spot compute environment with an order of 2. The scheduler will attempt to place jobs on the C4OnDemand compute environment first. Command: `aws batch create-job-queue --cli-input-json``file://<path_to_json_file>/HighPriority.json`JSON file format: `{ "jobQueueName": "HighPriority", "state": "ENABLED", "priority": 1, "computeEnvironmentOrder": [ { "order": 1, "computeEnvironment": "C4OnDemand" }, { "order": 2, "computeEnvironment": "M4Spot" } ] }`Output: `{ "jobQueueArn": "arn:aws:batch:us-east-1:012345678910:job-queue/HighPriority", "jobQueueName": "HighPriority" }`- 
                    For API details, see [CreateJobQueue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/create-job-queue.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-compute-environment`.

- **AWS CLI**
- 
            
                    **To delete a compute environment**This example deletes the P2OnDemand compute environment. Command: `aws batch delete-compute-environment --compute-environment``P2OnDemand`- 
                    For API details, see [DeleteComputeEnvironment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/delete-compute-environment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-job-queue`.

- **AWS CLI**
- 
            
                    **To delete a job queue**This example deletes the GPGPU job queue. Command: `aws batch delete-job-queue --job-queue``GPGPU`- 
                    For API details, see [DeleteJobQueue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/delete-job-queue.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deregister-job-definition`.

- **AWS CLI**
- 
            
                    **To deregister a job definition**This example deregisters a job definition called sleep10. Command: `aws batch deregister-job-definition --job-definition``sleep10`- 
                    For API details, see [DeregisterJobDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/deregister-job-definition.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-compute-environments`.

- **AWS CLI**
- 
            
                    **To describe a compute environment**This example describes the P2OnDemand compute environment. Command: `aws batch describe-compute-environments --compute-environments``P2OnDemand`Output: `{ "computeEnvironments": [ { "status": "VALID", "serviceRole": "arn:aws:iam::012345678910:role/AWSBatchServiceRole", "computeEnvironmentArn": "arn:aws:batch:us-east-1:012345678910:compute-environment/P2OnDemand", "computeResources": { "subnets": [ "subnet-220c0e0a", "subnet-1a95556d", "subnet-978f6dce" ], "tags": { "Name": "Batch Instance - P2OnDemand" }, "desiredvCpus": 48, "minvCpus": 0, "instanceTypes": [ "p2" ], "securityGroupIds": [ "sg-cf5093b2" ], "instanceRole": "ecsInstanceRole", "maxvCpus": 128, "type": "EC2", "ec2KeyPair": "id_rsa" }, "statusReason": "ComputeEnvironment Healthy", "ecsClusterArn": "arn:aws:ecs:us-east-1:012345678910:cluster/P2OnDemand_Batch_2c06f29d-d1fe-3a49-879d-42394c86effc", "state": "ENABLED", "computeEnvironmentName": "P2OnDemand", "type": "MANAGED" } ] }`- 
                    For API details, see [DescribeComputeEnvironments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/describe-compute-environments.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-job-definitions`.

- **AWS CLI**
- 
            
                    **To describe active job definitions**This example describes all of your active job definitions. Command: `aws batch describe-job-definitions --status``ACTIVE`Output: `{ "jobDefinitions": [ { "status": "ACTIVE", "jobDefinitionArn": "arn:aws:batch:us-east-1:012345678910:job-definition/sleep60:1", "containerProperties": { "mountPoints": [], "parameters": {}, "image": "busybox", "environment": {}, "vcpus": 1, "command": [ "sleep", "60" ], "volumes": [], "memory": 128, "ulimits": [] }, "type": "container", "jobDefinitionName": "sleep60", "revision": 1 } ] }`- 
                    For API details, see [DescribeJobDefinitions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/describe-job-definitions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-job-queues`.

- **AWS CLI**
- 
            
                    **To describe a job queue**This example describes the HighPriority job queue. Command: `aws batch describe-job-queues --job-queues``HighPriority`Output: `{ "jobQueues": [ { "status": "VALID", "jobQueueArn": "arn:aws:batch:us-east-1:012345678910:job-queue/HighPriority", "computeEnvironmentOrder": [ { "computeEnvironment": "arn:aws:batch:us-east-1:012345678910:compute-environment/C4OnDemand", "order": 1 } ], "statusReason": "JobQueue Healthy", "priority": 1, "state": "ENABLED", "jobQueueName": "HighPriority" } ] }`- 
                    For API details, see [DescribeJobQueues](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/describe-job-queues.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-jobs`.

- **AWS CLI**
- 
            
                    **To describe a job**The following `describe-jobs`example describes a job with the specified job ID.`aws batch describe-jobs \ --jobs``bcf0b186-a532-4122-842e-2ccab8d54efb`Output: `{ "jobs": [ { "status": "SUBMITTED", "container": { "mountPoints": [], "image": "busybox", "environment": [], "vcpus": 1, "command": [ "sleep", "60" ], "volumes": [], "memory": 128, "ulimits": [] }, "parameters": {}, "jobDefinition": "arn:aws:batch:us-east-1:012345678910:job-definition/sleep60:1", "jobQueue": "arn:aws:batch:us-east-1:012345678910:job-queue/HighPriority", "jobId": "bcf0b186-a532-4122-842e-2ccab8d54efb", "dependsOn": [], "jobName": "example", "createdAt": 1480483387803 } ] }`- 
                    For API details, see [DescribeJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/describe-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-jobs`.

- **AWS CLI**
- 
            
                    **To list running jobs**This example lists the running jobs in the HighPriority job queue. Command: `aws batch list-jobs --job-queue``HighPriority`Output: `{ "jobSummaryList": [ { "jobName": "example", "jobId": "e66ff5fd-a1ff-4640-b1a2-0b0a142f49bb" } ] }`**To list submitted jobs**This example lists jobs in the HighPriority job queue that are in the SUBMITTED job status. Command: `aws batch list-jobs --job-queue``HighPriority`--job-status`SUBMITTED`Output: `{ "jobSummaryList": [ { "jobName": "example", "jobId": "68f0c163-fbd4-44e6-9fd1-25b14a434786" } ] }`- 
                    For API details, see [ListJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/list-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-job-definition`.

- **AWS CLI**
- 
            
                    **To register a job definition**This example registers a job definition for a simple container job. Command: `aws batch register-job-definition --job-definition-name``sleep30`--type`container`--container-properties '`{ "image": "busybox", "vcpus": 1, "memory": 128, "command": [ "sleep", "30"]}`'Output: `{ "jobDefinitionArn": "arn:aws:batch:us-east-1:012345678910:job-definition/sleep30:1", "jobDefinitionName": "sleep30", "revision": 1 }`- 
                    For API details, see [RegisterJobDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/register-job-definition.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `submit-job`.

- **AWS CLI**
- 
            
                    **To submit a job**This example submits a simple container job called example to the HighPriority job queue. Command: `aws batch submit-job --job-name``example`--job-queue`HighPriority`--job-definition`sleep60`Output: `{ "jobName": "example", "jobId": "876da822-4198-45f2-a252-6cea32512ea8" }`- 
                    For API details, see [SubmitJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/submit-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `terminate-job`.

- **AWS CLI**
- 
            
                    **To terminate a job**This example terminates a job with the specified job ID. Command: `aws batch terminate-job --job-id``61e743ed-35e4-48da-b2de-5c8333821c84`--reason`"Terminating job."`- 
                    For API details, see [TerminateJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/terminate-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-compute-environment`.

- **AWS CLI**
- 
            
                    **To update a compute environment**This example disables the P2OnDemand compute environment so it can be deleted. Command: `aws batch update-compute-environment --compute-environment``P2OnDemand`--state`DISABLED`Output: `{ "computeEnvironmentName": "P2OnDemand", "computeEnvironmentArn": "arn:aws:batch:us-east-1:012345678910:compute-environment/P2OnDemand" }`- 
                    For API details, see [UpdateComputeEnvironment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/update-compute-environment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-job-queue`.

- **AWS CLI**
- 
            
                    **To update a job queue**This example disables a job queue so that it can be deleted. Command: `aws batch update-job-queue --job-queue``GPGPU`--state`DISABLED`Output: `{ "jobQueueArn": "arn:aws:batch:us-east-1:012345678910:job-queue/GPGPU", "jobQueueName": "GPGPU" }`- 
                    For API details, see [UpdateJobQueue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/update-job-queue.html)in*AWS CLI Command Reference*.
 
-