# CloudWatch Synthetics examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_synthetics_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_synthetics_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with CloudWatch Synthetics.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `associate-resource`.

- **AWS CLI**
- 
            
                    **To associate a canary with a group**The following `associate-resource`example associates a canary with a group named`demo_group`.`aws synthetics associate-resource \ --group-identifier``demo_group`\ --resource-arn`arn:aws:synthetics:us-east-1:123456789012:canary:demo_canary`This command produces no output. For more information, see [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [AssociateResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/associate-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-canary`.

- **AWS CLI**
- 
            
                    **To create a canary**The following `create-canary`example creates a canary named`demo_canary`.`aws synthetics create-canary \ --name``demo_canary`\ --code '`{"S3Bucket": "artifacts3bucket", "S3Key":"demo_canary.zip", "Handler": "index.lambda_handler"}`' \ --artifact-s3-location`s3://amzn-s3-demo-bucket/demo_canary.zip`\ --execution-role-arn`arn:aws:iam::123456789012:role/demo_canary_role`\ --schedule Expression="rate(10 minutes)" \ --runtime-version`syn-nodejs-puppeteer-9.1`Output: `{ "Canary": { "Id": "a1b2c3d4-5678-90ab-cdef-example11111", "Name": "demo_canary", "Code": { "Handler": "index.lambda_handler" }, "ExecutionRoleArn": "arn:aws:iam::123456789012:role/demo_canary_role", "Schedule": { "Expression": "rate(10 minutes)", "DurationInSeconds": 0 }, "RunConfig": { "TimeoutInSeconds": 600, "MemoryInMB": 1000, "ActiveTracing": false }, "SuccessRetentionPeriodInDays": 31, "FailureRetentionPeriodInDays": 31, "Status": { "State": "CREATING", "StateReasonCode": "CREATE_PENDING" }, "Timeline": { "Created": "2024-10-15T19:03:08.826000+05:30", "LastModified": "2024-10-15T19:03:08.826000+05:30" }, "ArtifactS3Location": "amzn-s3-demo-bucket/demo_canary.zip", "RuntimeVersion": "syn-nodejs-puppeteer-9.1", "Tags": {} } }`For more information, see [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [CreateCanary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/create-canary.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-group`.

- **AWS CLI**
- 
            
                    **To create a group**The following `create-group`example creates a group named`demo_group`.`aws synthetics create-group \ --name``demo_group`Output: `{ "Group": { "Id": "example123", "Name": "demo_group", "Arn": "arn:aws:synthetics:us-east-1:123456789012:group:example123", "Tags": {}, "CreatedTime": "2024-10-15T14:47:23.811000+05:30", "LastModifiedTime": "2024-10-15T14:47:23.811000+05:30" } }`For more information, see [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [CreateGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/create-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-canary`.

- **AWS CLI**
- 
            
                    **To permanently delete a canary**The following `delete-canary`example deletes a canary named`demo_canary`.`aws synthetics delete-canary \ --name``demo_canary`This command produces no output. For more information, see [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [DeleteCanary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/delete-canary.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-group`.

- **AWS CLI**
- 
            
                    **To delete a group**The following `delete-group`example deletes a group named`demo_group`.`aws synthetics delete-group \ --group-identifier``demo_group`This command produces no output. For more information, see [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [DeleteGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/delete-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-canaries-last-run`.

- **AWS CLI**
- 
            
                    **To see information from the most recent run of each canary**The following `describe-canaries-last-run`example returns the most recent run of each canary that you have created.`aws synthetics describe-canaries-last-run`Output: `{ "CanariesLastRun": [ { "CanaryName": "demo_canary", "LastRun": { "Id": "a1b2c3d4-5678-90ab-cdef-example11111", "Name": "demo_canary", "Status": { "State": "PASSED", "StateReason": "", "StateReasonCode": "" }, "Timeline": { "Started": "2024-10-15T19:20:39.691000+05:30", "Completed": "2024-10-15T19:20:58.211000+05:30" }, "ArtifactS3Location": "cw-syn-results-123456789012-us-east-1/canary/us-east-1/demo_canary-abc-example1234/2024/10/15/13/50-39-690" } } ] }`For more information, see [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [DescribeCanariesLastRun](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/describe-canaries-last-run.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-canaries`.

- **AWS CLI**
- 
            
                    **To list canaries in your account**The following `describe-canaries`example lists the details of canaries in your account.`aws synthetics describe-canaries`Output: `{ "Canaries": [ { "Id": "a1b2c3d4-5678-90ab-cdef-example11111", "Name": "demo_canary", "Code": { "SourceLocationArn": "arn:aws:lambda:us-east-1:123456789012:layer:cwsyn-demo_canary-a1b2c3d4-5678-90ab-cdef-example11111b8:1", "Handler": "pageLoadBlueprint.handler" }, "ExecutionRoleArn": "arn:aws:iam::123456789012:role/service-role/CloudWatchSyntheticsRole-demo_canary-a12-a123bc456789", "Schedule": { "Expression": "rate(5 minutes)", "DurationInSeconds": 0 }, "RunConfig": { "TimeoutInSeconds": 300, "MemoryInMB": 1000, "ActiveTracing": false }, "SuccessRetentionPeriodInDays": 31, "FailureRetentionPeriodInDays": 31, "Status": { "State": "RUNNING" }, "Timeline": { "Created": "2024-10-15T18:55:15.168000+05:30", "LastModified": "2024-10-15T18:55:40.540000+05:30", "LastStarted": "2024-10-15T18:55:40.540000+05:30" }, "ArtifactS3Location": "cw-syn-results-123456789012-us-east-1/canary/us-east-1/demo_canary-a12-a123bc456789", "EngineArn": "arn:aws:lambda:us-east-1:123456789012:function:cwsyn-demo_canary-a1b2c3d4-5678-90ab-cdef-example111118:1", "RuntimeVersion": "syn-nodejs-puppeteer-9.1", "Tags": { "blueprint": "heartbeat" } } ] }`For more information, see [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [DescribeCanaries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/describe-canaries.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-runtime-versions`.

- **AWS CLI**
- 
            
                    **To return a list of synthetics canary runtime versions**The following `describe-runtime-versions`example returns the list of synthetics canary runtime versions.`aws synthetics describe-runtime-versions`Output: `{ "RuntimeVersions": [ { "VersionName": "syn-nodejs-puppeteer-9.1", "Description": "Security fixes and bug fix for date range error in har. Dependencies: Node JS 20.x, Puppeteer-core 22.12.1, Chromium 126.0.6478.126", "ReleaseDate": "2024-10-02T05:30:00+05:30" }, { "VersionName": "syn-nodejs-puppeteer-9.0", "Description": "Upgraded Chromium and Puppeteer. Dependencies: Node JS 20.x, Puppeteer-core 22.12.1, Chromium 126.0.6478.126", "ReleaseDate": "2024-07-22T05:30:00+05:30" }, { "VersionName": "syn-nodejs-puppeteer-8.0", "Description": "Upgraded Chromium and Puppeteer. Dependencies: Node JS 20.x, Puppeteer-core 22.10.0, Chromium 125.0.6422.112", "ReleaseDate": "2024-06-21T05:30:00+05:30" }, { "VersionName": "syn-nodejs-puppeteer-7.0", "Description": "Upgraded Chromium and Puppeteer. Dependencies: Node JS 18.x, Puppeteer-core 21.9.0, Chromium 121.0.6167.139", "ReleaseDate": "2024-03-08T05:30:00+05:30" }, { "VersionName": "syn-nodejs-puppeteer-6.2", "Description": "Updated shared libraries for Chromium and added ephemeral storage monitoring. Dependencies: Node JS 18.x, Puppeteer-core 19.7.0, Chromium 111.0.5563.146", "ReleaseDate": "2024-02-02T05:30:00+05:30" }, { "VersionName": "syn-nodejs-puppeteer-6.1", "Description": "Added puppeteer launch retry. Dependencies: Node JS 18.x, Puppeteer-core 19.7.0, Chromium 111.0.5563.146", "ReleaseDate": "2023-11-13T05:30:00+05:30", "DeprecationDate": "2024-03-08T13:30:00+05:30" }, { "VersionName": "syn-nodejs-puppeteer-6.0", "Description": "Reduced X-Ray traces of a canary run, improved duration metric and upgraded to NodeJS 18.x. Dependencies: Node JS 18.x, Puppeteer-core 19.7.0, Chromium 111.0.5563.146", "ReleaseDate": "2023-09-15T05:30:00+05:30", "DeprecationDate": "2024-03-08T13:30:00+05:30" }, { "VersionName": "syn-nodejs-puppeteer-5.2", "Description": "Updated shared libraries for Chromium. Dependencies: Node JS 16.x, Puppeteer-core 19.7.0, Chromium 111.0.5563.146", "ReleaseDate": "2024-02-01T05:30:00+05:30" }, { "VersionName": "syn-nodejs-puppeteer-5.1", "Description": "Fixes a bug about missing request headers in har. Dependencies: Node JS 16.x, Puppeteer-core 19.7.0, Chromium 111.0.5563.146", "ReleaseDate": "2023-08-09T05:30:00+05:30", "DeprecationDate": "2024-03-08T13:30:00+05:30" }, { "VersionName": "syn-nodejs-puppeteer-5.0", "Description": "Upgraded Puppeteer and Chromium. Dependencies: Node JS 16.x, Puppeteer-core 19.7.0, Chromium 111.0.5563.146", "ReleaseDate": "2023-07-21T05:30:00+05:30", "DeprecationDate": "2024-03-08T13:30:00+05:30" }, { "VersionName": "syn-nodejs-puppeteer-4.0", "Description": "Upgraded to NodeJS 16.x. Dependencies: Node JS 16.x, Puppeteer-core 5.5.0, Chromium 92.0.4512.0", "ReleaseDate": "2023-05-01T05:30:00+05:30", "DeprecationDate": "2024-03-08T13:30:00+05:30" } ] }`For more information, see [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [DescribeRuntimeVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/describe-runtime-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-resource`.

- **AWS CLI**
- 
            
                    **To remove a canary from a group**The following `disassociate-resource`example removes a canary from the group named`demo_group`.`aws synthetics disassociate-resource \ --group-identifier``demo_group`\ --resource-arn`arn:aws:synthetics:us-east-1:123456789012:canary:demo_canary`This command produces no output. For more information, see [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [DisassociateResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/disassociate-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-canary-runs`.

- **AWS CLI**
- 
            
                    **To retrieve a list of runs for a specified canary**The following `get-canary-runs`example retrieves a list of runs for the canary named`demo_canary`.`aws synthetics get-canary-runs \ --name``demo_canary`Output: `{ "CanaryRuns": [ { "Id": "a1b2c3d4-5678-90ab-cdef-example11111", "Name": "demo_canary", "Status": { "State": "PASSED", "StateReason": "", "StateReasonCode": "" }, "Timeline": { "Started": "2024-10-16T10:38:57.013000+05:30", "Completed": "2024-10-16T10:39:25.793000+05:30" }, "ArtifactS3Location": "cw-syn-results-123456789012-us-east-1/canary/us-east-1/demo_canary-abc-example1234/2024/10/15/13/50-39-690" } ] }`For more information, see [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [GetCanaryRuns](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/get-canary-runs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-canary`.

- **AWS CLI**
- 
            
                    **To retrieve complete information about one canary**The following `get-canary`example retrieves complete information about the canary named`demo_canary`.`aws synthetics get-canary \ --name``demo_canary`Output: `{ "Canary": { "Id": "a1b2c3d4-5678-90ab-cdef-example11111", "Name": "demo_canary", "Code": { "SourceLocationArn": "arn:aws:lambda:us-east-1:123456789012:layer:cwsyn-demo_canary-a1b2c3d4-5678-90ab-cdef-example111118:1", "Handler": "pageLoadBlueprint.handler" }, "ExecutionRoleArn": "arn:aws:iam::123456789012:role/demo_canary_role", "Schedule": { "Expression": "rate(10 minutes)", "DurationInSeconds": 0 }, "RunConfig": { "TimeoutInSeconds": 300, "MemoryInMB": 1000, "ActiveTracing": false }, "SuccessRetentionPeriodInDays": 31, "FailureRetentionPeriodInDays": 31, "Status": { "State": "RUNNING" }, "Timeline": { "Created": "2024-10-15T18:55:15.168000+05:30", "LastModified": "2024-10-15T18:55:40.540000+05:30", "LastStarted": "2024-10-15T18:55:40.540000+05:30" }, "ArtifactS3Location": "cw-syn-results-123456789012-us-east-1/canary/us-east-1/demo_canary-a12-a123bc456789", "EngineArn": "arn:aws:lambda:us-east-1:123456789012:function:cwsyn-demo_canary-a1b2c3d4-5678-90ab-cdef-example111118:1", "RuntimeVersion": "syn-nodejs-puppeteer-9.1", "Tags": { "blueprint": "heartbeat" } } }`For more information, see [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [GetCanary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/get-canary.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-group`.

- **AWS CLI**
- 
            
                    **To return information about one group**The following `get-group`example returns information about the group named`demo_group`.`aws synthetics get-group \ --group-identifier``demo_group`Output: `{ "Group": { "Id": "example123", "Name": "demo_group", "Arn": "arn:aws:synthetics:us-east-1:123456789012:group:example123", "Tags": {}, "CreatedTime": "2024-10-15T14:47:23.811000+05:30", "LastModifiedTime": "2024-10-15T14:47:23.811000+05:30" } }`For more information, see [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [GetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/get-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-associated-groups`.

- **AWS CLI**
- 
            
                    **To return a list of the groups**The following `list-associated-groups`example returns a list of the groups associated with the canary named`demo_canary`.`aws synthetics list-associated-groups \ --resource-arn``arn:aws:synthetics:us-east-1:123456789012:canary:demo_canary`Output: `{ "Groups": [ { "Id": "example123", "Name": "demo_group", "Arn": "arn:aws:synthetics:us-east-1:123456789012:group:example123" } ] }`For more information, see [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [ListAssociatedGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/list-associated-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-group-resources`.

- **AWS CLI**
- 
            
                    **To return a list of the ARNs of the canaries that are associated with the specified group**The following `list-group-resources`example returns a list of the ARNs of the canaries that are associated with the group named`demo_group`.`aws synthetics list-group-resources \ --group-identifier``demo_group`Output: `{ "Resources": [ "arn:aws:synthetics:us-east-1:123456789012:canary:demo_canary" ] }`For more information, see [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [ListGroupResources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/list-group-resources.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-groups`.

- **AWS CLI**
- 
            
                    **To return a list of all groups in the account**The following `list-groups`example returns a list of all groups in the account.`aws synthetics list-groups`Output: `{ "Groups": [ { "Id": "example123", "Name": "demo_group", "Arn": "arn:aws:synthetics:us-east-1:123456789012:group:example123" } ] }`For more information, see [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [ListGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/list-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **Example 1: To display the tags associated with a canary**The following `list-tags-for-resource`example returns the tags associated with a canary named`demo_canary`.`aws synthetics list-tags-for-resource \ --resource-arn``arn:aws:synthetics:us-east-1:123456789012:canary:demo_canary`Output: `{ "Tags": { "blueprint": "heartbeat" } }`**Example 2: To display the tags associated with a group**The following `list-tags-for-resource`example returns the tags associated with a group named`demo_group`.`aws synthetics list-tags-for-resource \ --resource-arn``arn:aws:synthetics:us-east-1:123456789012:group:example123`Output: `{ "Tags": { "team": "Devops" } }`For more information, see [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-canary`.

- **AWS CLI**
- 
            
                    **To run a canary**The following `start-canary`example runs a canary named`demo_canary`.`aws synthetics start-canary \ --name``demo_canary`This command produces no output. For more information, see [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [StartCanary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/start-canary.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-canary`.

- **AWS CLI**
- 
            
                    **To stop a canary**The following `stop-canary`example stops the canary named`demo_canary`.`aws synthetics stop-canary \ --name``demo_canary`This command produces no output. For more information, see [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [StopCanary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/stop-canary.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **Example 1: To assign a tag to the canary**The following `tag-resource`example assigns a tag to the canary named`demo_canary`.`aws synthetics tag-resource \ --resource-arn``arn:aws:synthetics:us-east-1:123456789012:canary:demo_canary`\ --tags`blueprint=heartbeat`This command produces no output. **Example 2: To assign a tag to the group**The following `tag-resource`example assigns a tag to the group named`demo_group`.`aws synthetics tag-resource \ --resource-arn``arn:aws:synthetics:us-east-1:123456789012:group:example123`\ --tags`team=Devops`This command produces no output. For more information, see [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **Example 1: To remove a tag from the canary**The following `untag-resource`example removes a tag from the canary named`demo_canary`.`aws synthetics untag-resource \ --resource-arn``arn:aws:synthetics:us-east-1:123456789012:canary:demo_canary`\ --tag-keys`blueprint`This command produces no output. **Example 2: To remove a tag from the group**The following `untag-resource`example assigns a removes a tag from the group named`demo_group`.`aws synthetics untag-resource \ --resource-arn``arn:aws:synthetics:us-east-1:123456789012:group:example123`\ --tag-keys`team`This command produces no output. For more information, see [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-canary`.

- **AWS CLI**
- 
            
                    **To update a canary**The following `update-canary`example updates the configuration of a canary named`demo_canary`.`aws synthetics update-canary \ --name``demo_canary`\ --schedule Expression="rate(15 minutes)"This command produces no output. For more information, see [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [UpdateCanary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/synthetics/update-canary.html)in*AWS CLI Command Reference*.
 
-