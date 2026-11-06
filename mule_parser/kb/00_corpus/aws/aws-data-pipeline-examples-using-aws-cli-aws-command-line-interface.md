# AWS Data Pipeline examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_data-pipeline_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_data-pipeline_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS Data Pipeline.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `activate-pipeline`.

- **AWS CLI**
- 
            
                    **To activate a pipeline**This example activates the specified pipeline: `aws datapipeline activate-pipeline --pipeline-id``df-00627471SOVYZEXAMPLE`To activate the pipeline at a specific date and time, use the following command: `aws datapipeline activate-pipeline --pipeline-id``df-00627471SOVYZEXAMPLE`--start-timestamp`2015-04-07T00:00:00Z`- 
                    For API details, see [ActivatePipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/activate-pipeline.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `add-tags`.

- **AWS CLI**
- 
            
                    **To add a tag to a pipeline**This example adds the specified tag to the specified pipeline: `aws datapipeline add-tags --pipeline-id``df-00627471SOVYZEXAMPLE`--tags`key=environment,value=production``key=owner,value=sales`To view the tags, use the describe-pipelines command. For example, the tags added in the example command appear as follows in the output for describe-pipelines: `{ ... "tags": [ { "value": "production", "key": "environment" }, { "value": "sales", "key": "owner" } ] ... }`- 
                    For API details, see [AddTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/add-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-pipeline`.

- **AWS CLI**
- 
            
                    **To create a pipeline**This example creates a pipeline: `aws datapipeline create-pipeline --name``my-pipeline`--unique-id`my-pipeline-token`The following is example output: `{ "pipelineId": "df-00627471SOVYZEXAMPLE" }`- 
                    For API details, see [CreatePipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/create-pipeline.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deactivate-pipeline`.

- **AWS CLI**
- 
            
                    **To deactivate a pipeline**This example deactivates the specified pipeline: `aws datapipeline deactivate-pipeline --pipeline-id``df-00627471SOVYZEXAMPLE`To deactivate the pipeline only after all running activities finish, use the following command: `aws datapipeline deactivate-pipeline --pipeline-id``df-00627471SOVYZEXAMPLE`--no-cancel-active- 
                    For API details, see [DeactivatePipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/deactivate-pipeline.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-pipeline`.

- **AWS CLI**
- 
            
                    **To delete a pipeline**This example deletes the specified pipeline: `aws datapipeline delete-pipeline --pipeline-id``df-00627471SOVYZEXAMPLE`- 
                    For API details, see [DeletePipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/delete-pipeline.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-pipelines`.

- **AWS CLI**
- 
            
                    **To describe your pipelines**This example describes the specified pipeline: `aws datapipeline describe-pipelines --pipeline-ids``df-00627471SOVYZEXAMPLE`The following is example output: `{ "pipelineDescriptionList": [ { "fields": [ { "stringValue": "PENDING", "key": "@pipelineState" }, { "stringValue": "my-pipeline", "key": "name" }, { "stringValue": "2015-04-07T16:05:58", "key": "@creationTime" }, { "stringValue": "df-00627471SOVYZEXAMPLE", "key": "@id" }, { "stringValue": "123456789012", "key": "pipelineCreator" }, { "stringValue": "PIPELINE", "key": "@sphere" }, { "stringValue": "123456789012", "key": "@userId" }, { "stringValue": "123456789012", "key": "@accountId" }, { "stringValue": "my-pipeline-token", "key": "uniqueId" } ], "pipelineId": "df-00627471SOVYZEXAMPLE", "name": "my-pipeline", "tags": [] } ] }`- 
                    For API details, see [DescribePipelines](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/describe-pipelines.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-pipeline-definition`.

- **AWS CLI**
- 
            
                    **To get a pipeline definition**This example gets the pipeline definition for the specified pipeline: `aws datapipeline get-pipeline-definition --pipeline-id``df-00627471SOVYZEXAMPLE`The following is example output: `{ "parameters": [ { "type": "AWS::S3::ObjectKey", "id": "myS3OutputLoc", "description": "S3 output folder" }, { "default": "s3://us-east-1.elasticmapreduce.samples/pig-apache-logs/data", "type": "AWS::S3::ObjectKey", "id": "myS3InputLoc", "description": "S3 input folder" }, { "default": "grep -rc \"GET\" ${INPUT1_STAGING_DIR}/* > ${OUTPUT1_STAGING_DIR}/output.txt", "type": "String", "id": "myShellCmd", "description": "Shell command to run" } ], "objects": [ { "type": "Ec2Resource", "terminateAfter": "20 Minutes", "instanceType": "t1.micro", "id": "EC2ResourceObj", "name": "EC2ResourceObj" }, { "name": "Default", "failureAndRerunMode": "CASCADE", "resourceRole": "DataPipelineDefaultResourceRole", "schedule": { "ref": "DefaultSchedule" }, "role": "DataPipelineDefaultRole", "scheduleType": "cron", "id": "Default" }, { "directoryPath": "#{myS3OutputLoc}/#{format(@scheduledStartTime, 'YYYY-MM-dd-HH-mm-ss')}", "type": "S3DataNode", "id": "S3OutputLocation", "name": "S3OutputLocation" }, { "directoryPath": "#{myS3InputLoc}", "type": "S3DataNode", "id": "S3InputLocation", "name": "S3InputLocation" }, { "startAt": "FIRST_ACTIVATION_DATE_TIME", "name": "Every 15 minutes", "period": "15 minutes", "occurrences": "4", "type": "Schedule", "id": "DefaultSchedule" }, { "name": "ShellCommandActivityObj", "command": "#{myShellCmd}", "output": { "ref": "S3OutputLocation" }, "input": { "ref": "S3InputLocation" }, "stage": "true", "type": "ShellCommandActivity", "id": "ShellCommandActivityObj", "runsOn": { "ref": "EC2ResourceObj" } } ], "values": { "myS3OutputLoc": "s3://amzn-s3-demo-bucket/", "myS3InputLoc": "s3://us-east-1.elasticmapreduce.samples/pig-apache-logs/data", "myShellCmd": "grep -rc \"GET\" ${INPUT1_STAGING_DIR}/* > ${OUTPUT1_STAGING_DIR}/output.txt" } }`- 
                    For API details, see [GetPipelineDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/get-pipeline-definition.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-pipelines`.

- **AWS CLI**
- 
            
                    **To list your pipelines**This example lists your pipelines: `aws datapipeline list-pipelines`The following is example output: `{ "pipelineIdList": [ { "id": "df-00627471SOVYZEXAMPLE", "name": "my-pipeline" }, { "id": "df-09028963KNVMREXAMPLE", "name": "ImportDDB" }, { "id": "df-0870198233ZYVEXAMPLE", "name": "CrossRegionDDB" }, { "id": "df-00189603TB4MZEXAMPLE", "name": "CopyRedshift" } ] }`- 
                    For API details, see [ListPipelines](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/list-pipelines.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-runs`.

- **AWS CLI**
- 
            
                    **Example 1: To list your pipeline runs**The following `list-runs`example lists the runs for the specified pipeline.`aws datapipeline list-runs --pipeline-id``df-00627471SOVYZEXAMPLE`Output: `Name Scheduled Start Status ID Started Ended ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 1. EC2ResourceObj 2015-04-12T17:33:02 CREATING @EC2ResourceObj_2015-04-12T17:33:02 2015-04-12T17:33:10 2. S3InputLocation 2015-04-12T17:33:02 FINISHED @S3InputLocation_2015-04-12T17:33:02 2015-04-12T17:33:09 2015-04-12T17:33:09 3. S3OutputLocation 2015-04-12T17:33:02 WAITING_ON_DEPENDENCIES @S3OutputLocation_2015-04-12T17:33:02 2015-04-12T17:33:09 4. ShellCommandActivityObj 2015-04-12T17:33:02 WAITING_FOR_RUNNER @ShellCommandActivityObj_2015-04-12T17:33:02 2015-04-12T17:33:09`**Example 2: To list the pipeline runs between the specified dates**The following `list-runs`example uses the`--start-interval`to specify the dates to include in the output.`aws datapipeline list-runs --pipeline-id``df-01434553B58A2SHZUKO5`--start-interval`2017-10-07T00:00:00,2017-10-08T00:00:00`- 
                    For API details, see [ListRuns](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/list-runs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-pipeline-definition`.

- **AWS CLI**
- 
            
                    **To upload a pipeline definition**This example uploads the specified pipeline definition to the specified pipeline: `aws datapipeline put-pipeline-definition --pipeline-id``df-00627471SOVYZEXAMPLE`--pipeline-definition`file://my-pipeline-definition.json`The following is example output: `{ "validationErrors": [], "errored": false, "validationWarnings": [] }`- 
                    For API details, see [PutPipelineDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/put-pipeline-definition.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-tags`.

- **AWS CLI**
- 
            
                    **To remove a tag from a pipeline**This example removes the specified tag from the specified pipeline: `aws datapipeline remove-tags --pipeline-id``df-00627471SOVYZEXAMPLE`--tag-keys`environment`- 
                    For API details, see [RemoveTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datapipeline/remove-tags.html)in*AWS CLI Command Reference*.
 
-