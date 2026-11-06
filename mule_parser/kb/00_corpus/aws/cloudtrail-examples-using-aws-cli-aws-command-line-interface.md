# CloudTrail examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_cloudtrail_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_cloudtrail_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with CloudTrail.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `add-tags`.

- **AWS CLI**
- 
            
                    **To add tags to trail**The following `add-tags`command adds tags for`Trail1`:`aws cloudtrail add-tags --resource-id``arn:aws:cloudtrail:us-east-1:123456789012:trail/Trail1`--tags-list`Key=name,Value=Alice``Key=location,Value=us`- 
                    For API details, see [AddTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/add-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-subscription`.

- **AWS CLI**
- 
            
                    **To create and configure AWS resources for a trail**The following `create-subscription`command creates a new S3 bucket and SNS topic for`Trail1`.`aws cloudtrail create-subscription \ --name``Trail1`\ --s3-new-bucket`amzn-s3-demo-bucket`\ --sns-new-topic`my-topic`Output: `Setting up new S3 bucket amzn-s3-demo-bucket... Setting up new SNS topic my-topic... Creating/updating CloudTrail configuration... CloudTrail configuration: { "trailList": [ { "IncludeGlobalServiceEvents": true, "Name": "Trail1", "TrailARN": "arn:aws:cloudtrail:us-east-1:123456789012:trail/Trail1", "LogFileValidationEnabled": false, "IsMultiRegionTrail": false, "S3BucketName": "amzn-s3-demo-bucket", "SnsTopicName": "my-topic", "HomeRegion": "us-east-1" } ], "ResponseMetadata": { "HTTPStatusCode": 200, "RequestId": "f39e51f6-c615-11e5-85bd-d35ca21ee3e2" } } Starting CloudTrail service... Logs will be delivered to my-bucket`- 
                    For API details, see [CreateSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/create-subscription.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-trail`.

- **AWS CLI**
- 
            
                    **To create a trail**The following `create-trail`example creates a multi-region trail named`Trail1`and specifies an S3 bucket.`aws cloudtrail create-trail \ --name``Trail1`\ --s3-bucket-name`amzn-s3-demo-bucket`\ --is-multi-region-trailOutput: `{ "IncludeGlobalServiceEvents": true, "Name": "Trail1", "TrailARN": "arn:aws:cloudtrail:us-west-2:123456789012:trail/Trail1", "LogFileValidationEnabled": false, "IsMultiRegionTrail": true, "S3BucketName": "amzn-s3-demo-bucket" }`- 
                    For API details, see [CreateTrail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/create-trail.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-trail`.

- **AWS CLI**
- 
            
                    **To delete a trail**The following `delete-trail`command deletes a trail named`Trail1`:`aws cloudtrail delete-trail --name``Trail1`- 
                    For API details, see [DeleteTrail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/delete-trail.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-trails`.

- **AWS CLI**
- 
            
                    **To describe a trail**The following `describe-trails`example returns the settings for`Trail1`and`Trail2`.`aws cloudtrail describe-trails \ --trail-name-list``Trail1``Trail2`Output: `{ "trailList": [ { "IncludeGlobalServiceEvents": true, "Name": "Trail1", "TrailARN": "arn:aws:cloudtrail:us-east-1:123456789012:trail/Trail1", "LogFileValidationEnabled": false, "IsMultiRegionTrail": false, "S3BucketName": "amzn-s3-demo-bucket", "CloudWatchLogsRoleArn": "arn:aws:iam::123456789012:role/CloudTrail_CloudWatchLogs_Role", "CloudWatchLogsLogGroupArn": "arn:aws:logs:us-east-1:123456789012:log-group:CloudTrail:*", "SnsTopicName": "my-topic", "HomeRegion": "us-east-1" }, { "IncludeGlobalServiceEvents": true, "Name": "Trail2", "S3KeyPrefix": "my-prefix", "TrailARN": "arn:aws:cloudtrail:us-east-1:123456789012:trail/Trail2", "LogFileValidationEnabled": false, "IsMultiRegionTrail": false, "S3BucketName": "amzn-s3-demo-bucket2", "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/4c5ae5ac-3c13-421e-8335-c7868ef6a769", "HomeRegion": "us-east-1" } ] }`- 
                    For API details, see [DescribeTrails](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/describe-trails.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-event-selectors`.

- **AWS CLI**
- 
            
                    **To view the event selector settings for a trail**The following `get-event-selectors`command returns the settings for`Trail1`:`aws cloudtrail get-event-selectors --trail-name``Trail1`Output: `{ "EventSelectors": [ { "IncludeManagementEvents": true, "DataResources": [], "ReadWriteType": "All" } ], "TrailARN": "arn:aws:cloudtrail:us-east-1:123456789012:trail/Trail1" }`- 
                    For API details, see [GetEventSelectors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-event-selectors.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-trail-status`.

- **AWS CLI**
- 
            
                    **To get the status of a trail**The following `get-trail-status`command returns the delivery and logging details for`Trail1`:`aws cloudtrail get-trail-status --name``Trail1`Output: `{ "LatestNotificationTime": 1454022144.869, "LatestNotificationAttemptSucceeded": "2016-01-28T23:02:24Z", "LatestDeliveryAttemptTime": "2016-01-28T23:02:24Z", "LatestDeliveryTime": 1454022144.869, "TimeLoggingStarted": "2015-11-06T18:36:38Z", "LatestDeliveryAttemptSucceeded": "2016-01-28T23:02:24Z", "IsLogging": true, "LatestCloudWatchLogsDeliveryTime": 1454022144.918, "StartLoggingTime": 1446834998.695, "StopLoggingTime": 1446834996.933, "LatestNotificationAttemptTime": "2016-01-28T23:02:24Z", "TimeLoggingStopped": "2015-11-06T18:36:36Z" }`- 
                    For API details, see [GetTrailStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/get-trail-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-public-keys`.

- **AWS CLI**
- 
            
                    **To list all public keys for a trail**The following `list-public-keys`command returns all public keys whose private keys were used to sign the digest files within the specified time range:`aws cloudtrail list-public-keys --start-time``2016-01-01T20:30:00.000Z`Output: `{ "PublicKeyList": [ { "ValidityStartTime": 1453076702.0, "ValidityEndTime": 1455668702.0, "Value": "MIIBCgKCAQEAlSS3cl92HDycr/MTj0moOhas8habjrraXw+KzlWF0axSI2tcF+3iJ9BKQAVSKxGwxwu3m0wG3J+kUl1xboEcEPHYoIYMbgfSw7KGnuDKwkLzsQWhUJ0cIbOHASox1vv/5fNXkrHhGbDCHeVXm804c83nvHUEFYThr1PfyP/8HwrCtR3FX5OANtQCP61C1nJtSSkC8JSQUOrIP4CuwJjc+4WGDk+BGH5m9iuiAKkipEHWmUl8/P7XpfpWQuk4h8g3pXZOrNXr08lbh4d39svj7UqdhvOXoBISp9t/EXYuePGEtBdrKD9Dz+VHwyUPtBQvYr9BnkF88qBnaPNhS44rzwIDAQAB", "Fingerprint": "7f3f401420072e50a65a141430817ab3" } ] }`- 
                    For API details, see [ListPublicKeys](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/list-public-keys.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags`.

- **AWS CLI**
- 
            
                    **To list the tags for a trail**The following `list-tags`command lists the tags for`Trail1`and`Trail2`:`aws cloudtrail list-tags --resource-id-list``arn:aws:cloudtrail:us-east-1:123456789012:trail/Trail1``arn:aws:cloudtrail:us-east-1:123456789012:trail/Trail2`Output: `{ "ResourceTagList": [ { "ResourceId": "arn:aws:cloudtrail:us-east-1:123456789012:trail/Trail1", "TagsList": [ { "Value": "Alice", "Key": "name" }, { "Value": "us", "Key": "location" } ] }, { "ResourceId": "arn:aws:cloudtrail:us-east-1:123456789012:trail/Trail2", "TagsList": [ { "Value": "Bob", "Key": "name" } ] } ] }`- 
                    For API details, see [ListTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/list-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `lookup-events`.

- **AWS CLI**
- 
            
                    **To look up events for a trail**The following `lookup-events`command looks up API activity events by the attribute`EventName`:`aws cloudtrail lookup-events --lookup-attributes``AttributeKey=EventName,AttributeValue=ConsoleLogin`Output: `{ "Events": [ { "EventId": "654ccbc0-ba0d-486a-9076-dbf7274677a7", "Username": "my-session-name", "EventTime": "2021-11-18T09:41:02-08:00", "CloudTrailEvent": "{\"eventVersion\":\"1.02\",\"userIdentity\":{\"type\":\"AssumedRole\",\"principalId\":\"AROAJIKPFTA72SWU4L7T4:my-session-name\",\"arn\":\"arn:aws:sts::123456789012:assumed-role/my-role/my-session-name\",\"accountId\":\"123456789012\",\"sessionContext\":{\"attributes\":{\"mfaAuthenticated\":\"false\",\"creationDate\":\"2016-01-26T21:42:12Z\"},\"sessionIssuer\":{\"type\":\"Role\",\"principalId\":\"AROAJIKPFTA72SWU4L7T4\",\"arn\":\"arn:aws:iam::123456789012:role/my-role\",\"accountId\":\"123456789012\",\"userName\":\"my-role\"}}},\"eventTime\":\"2016-01-26T21:42:12Z\",\"eventSource\":\"signin.amazonaws.com\",\"eventName\":\"ConsoleLogin\",\"awsRegion\":\"us-east-1\",\"sourceIPAddress\":\"72.21.198.70\",\"userAgent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36\",\"requestParameters\":null,\"responseElements\":{\"ConsoleLogin\":\"Success\"},\"additionalEventData\":{\"MobileVersion\":\"No\",\"MFAUsed\":\"No\"},\"eventID\":\"654ccbc0-ba0d-486a-9076-dbf7274677a7\",\"eventType\":\"AwsConsoleSignIn\",\"recipientAccountId\":\"123456789012\"}", "EventName": "ConsoleLogin", "Resources": [] } ] }`- 
                    For API details, see [LookupEvents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/lookup-events.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-event-selectors`.

- **AWS CLI**
- 
            
                    **Example 1: Configure a trail to log management events and data events by using advanced event selectors**You can add advanced event selectors, and conditions for your advanced event selectors, up to a maximum of 500 values for all conditions and selectors on a trail. You can use advanced event selectors to log all available data event types. You can use either advanced event selectors or basic event selectors, but not both. If you apply advanced event selectors to a trail, any existing basic event selectors are overwritten. The following `put-event-selectors`example creates an advanced event selector for a trail named`myTrail`to log all management events, log S3 PutObject and DeleteObject API calls for all but one S3 bucket, log data API calls for a Lambda function named`myFunction`, and log Publish API calls on an SNS topic named`myTopic`.`aws cloudtrail put-event-selectors \ --trail-name``myTrail`\ --advanced-event-selectors '`[{"Name": "Log all management events", "FieldSelectors": [{ "Field": "eventCategory", "Equals": ["Management"] }] },{"Name": "Log PutObject and DeleteObject events for all but one bucket","FieldSelectors": [{ "Field": "eventCategory", "Equals": ["Data"] },{ "Field": "resources.type", "Equals": ["AWS::S3::Object"] },{ "Field": "eventName", "Equals": ["PutObject","DeleteObject"] },{ "Field": "resources.ARN", "NotStartsWith": ["arn:aws:s3:::amzn-s3-demo-bucket/"] }]},{"Name": "Log data events for a specific Lambda function","FieldSelectors": [{ "Field": "eventCategory", "Equals": ["Data"] },{ "Field": "resources.type", "Equals": ["AWS::Lambda::Function"] },{ "Field": "resources.ARN", "Equals": ["arn:aws:lambda:us-east-1:123456789012:function:myFunction"] }]},{"Name": "Log all Publish API calls on a specific SNS topic","FieldSelectors": [{ "Field": "eventCategory", "Equals": ["Data"] },{ "Field": "resources.type", "Equals": ["AWS::SNS::Topic"] },{ "Field": "eventName", "Equals": ["Publish"] },{ "Field": "resources.ARN", "Equals": ["arn:aws:sns:us-east-1:123456789012:myTopic.fifo"] }]}]`'Output: `{ "TrailARN": "arn:aws:cloudtrail:us-east-1:123456789012:trail/myTrail", "AdvancedEventSelectors": [ { "Name": "Log all management events", "FieldSelectors": [ { "Field": "eventCategory", "Equals": [ "Management" ] } ] }, { "Name": "Log PutObject and DeleteObject events for all but one bucket", "FieldSelectors": [ { "Field": "eventCategory", "Equals": [ "Data" ] }, { "Field": "resources.type", "Equals": [ "AWS::S3::Object" ] }, { "Field": "eventName", "Equals": [ "PutObject", "DeleteObject" ] }, { "Field": "resources.ARN", "NotStartsWith": [ "arn:aws:s3:::amzn-s3-demo-bucket/" ] } ] }, { "Name": "Log data events for a specific Lambda function", "FieldSelectors": [ { "Field": "eventCategory", "Equals": [ "Data" ] }, { "Field": "resources.type", "Equals": [ "AWS::Lambda::Function" ] }, { "Field": "resources.ARN", "Equals": [ "arn:aws:lambda:us-east-1:123456789012:function:myFunction" ] } ] }, { "Name": "Log all Publish API calls on a specific SNS topic", "FieldSelectors": [ { "Field": "eventCategory", "Equals": [ "Data" ] }, { "Field": "resources.type", "Equals": [ "AWS::SNS::Topic" ] }, { "Field": "eventName", "Equals": [ "Publish" ] }, { "Field": "resources.ARN", "Equals": [ "arn:aws:sns:us-east-1:123456789012:myTopic.fifo" ] } ] } ] }`For more information, see [Log events by using advanced event selectors](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#creating-data-event-selectors-advanced)in the*AWS CloudTrail User Guide*.**Example 2: Configure event selectors for a trail to log all management events and data events**You can configure up to 5 event selectors for a trail and up to 250 data resources for a trail. Event selectors are also referred to as basic event selectors. You can use event selectors to log management events and data events for S3 objects, Lambda functions, and DynnamoDB tables. To log data events for other resource types, you must use advanced event selectors. The following `put-event-selectors`example creates an event selector for a trail named`TrailName`to include all management events, data events for two Amazon S3 bucket/prefix combinations, and data events for a single AWS Lambda function named`hello-world-python-function`.`aws cloudtrail put-event-selectors \ --trail-name``TrailName`\ --event-selectors '`[{"ReadWriteType": "All","IncludeManagementEvents": true,"DataResources": [{"Type":"AWS::S3::Object", "Values": ["arn:aws:s3:::amzn-s3-demo-bucket/prefix","arn:aws:s3:::amzn-s3-demo-bucket2/prefix2"]},{"Type": "AWS::Lambda::Function","Values": ["arn:aws:lambda:us-west-2:999999999999:function:hello-world-python-function"]}]}]`'Output: `{ "EventSelectors": [ { "IncludeManagementEvents": true, "DataResources": [ { "Values": [ "arn:aws:s3:::amzn-s3-demo-bucket/prefix", "arn:aws:s3:::amzn-s3-demo-bucket2/prefix2" ], "Type": "AWS::S3::Object" }, { "Values": [ "arn:aws:lambda:us-west-2:123456789012:function:hello-world-python-function" ], "Type": "AWS::Lambda::Function" }, ], "ReadWriteType": "All" } ], "TrailARN": "arn:aws:cloudtrail:us-east-2:123456789012:trail/TrailName" }`For more information, see [Log events by using basic event selectors](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#creating-data-event-selectors-basic)in the*AWS CloudTrail User Guide*.**Example 3: Configure event selectors for a trail to log management events, all S3 data events on S3 objects, and all Lambda data events on functions in your account**The following `put-event-selectors`example creates an event selector for a trail named`TrailName2`that includes all management events, and all data events for all Amazon S3 buckets and AWS Lambda functions in the AWS account.`aws cloudtrail put-event-selectors \ --trail-name``TrailName2`\ --event-selectors '`[{"ReadWriteType": "All","IncludeManagementEvents": true,"DataResources": [{"Type":"AWS::S3::Object", "Values": ["arn:aws:s3"]},{"Type": "AWS::Lambda::Function","Values": ["arn:aws:lambda"]}]}]`'Output: `{ "EventSelectors": [ { "IncludeManagementEvents": true, "DataResources": [ { "Values": [ "arn:aws:s3" ], "Type": "AWS::S3::Object" }, { "Values": [ "arn:aws:lambda" ], "Type": "AWS::Lambda::Function" }, ], "ReadWriteType": "All" } ], "TrailARN": "arn:aws:cloudtrail:us-east-2:123456789012:trail/TrailName2" }`For more information, see [Log events by using basic event selectors](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#creating-data-event-selectors-basic)in the*AWS CloudTrail User Guide*.- 
                    For API details, see [PutEventSelectors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/put-event-selectors.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-tags`.

- **AWS CLI**
- 
            
                    **To remove tags for a trail**The following `remove-tags`command removes the specified tags for`Trail1`:`aws cloudtrail remove-tags --resource-id``arn:aws:cloudtrail:us-east-1:123456789012:trail/Trail1`--tags-list`Key=name``Key=location`- 
                    For API details, see [RemoveTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/remove-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-logging`.

- **AWS CLI**
- 
            
                    **To start logging for a trail**The following `start-logging`command turns on logging for`Trail1`:`aws cloudtrail start-logging --name``Trail1`- 
                    For API details, see [StartLogging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/start-logging.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-logging`.

- **AWS CLI**
- 
            
                    **To stop logging a trail**The following `stop-logging`command turns off logging for`Trail1`:`aws cloudtrail stop-logging --name``Trail1`- 
                    For API details, see [StopLogging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/stop-logging.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-subscription`.

- **AWS CLI**
- 
            
                    **To update the configuration settings for a trail**The following `update-subscription`example updates the trail to specify a new S3 bucket and SNS topic.`aws cloudtrail update-subscription \ --name``Trail1`\ --s3-new-bucket`amzn-s3-demo-bucket`\ --sns-new-topic`my-topic-new`Output: `Setting up new S3 bucket amzn-s3-demo-bucket... Setting up new SNS topic my-topic-new... Creating/updating CloudTrail configuration... CloudTrail configuration: { "trailList": [ { "IncludeGlobalServiceEvents": true, "Name": "Trail1", "TrailARN": "arn:aws:cloudtrail:us-east-1:123456789012:trail/Trail1", "LogFileValidationEnabled": false, "IsMultiRegionTrail": false, "S3BucketName": "amzn-s3-demo-bucket", "SnsTopicName": "my-topic-new", "HomeRegion": "us-east-1" } ], "ResponseMetadata": { "HTTPStatusCode": 200, "RequestId": "31126f8a-c616-11e5-9cc6-2fd637936879" } }`- 
                    For API details, see [UpdateSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/update-subscription.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-trail`.

- **AWS CLI**
- 
            
                    **To update a trail**The following `update-trail`example updates a trail to use an existing bucket for log delivery.`aws cloudtrail update-trail \ --name``Trail1`\ --s3-bucket-name`amzn-s3-demo-bucket`Output: `{ "IncludeGlobalServiceEvents": true, "Name": "Trail1", "TrailARN": "arn:aws:cloudtrail:us-west-2:123456789012:trail/Trail1", "LogFileValidationEnabled": false, "IsMultiRegionTrail": true, "S3BucketName": "amzn-s3-demo-bucket" }`- 
                    For API details, see [UpdateTrail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/update-trail.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `validate-logs`.

- **AWS CLI**
- 
            
                    **To validate a log file**The following `validate-logs`command validates the logs for`Trail1`:`aws cloudtrail validate-logs --trail-arn``arn:aws:cloudtrail:us-east-1:123456789012:trail/Trail1`--start-time`20160129T19:00:00Z`Output: `Validating log files for trail arn:aws:cloudtrail:us-east-1:123456789012:trail/Trail1 between 2016-01-29T19:00:00Z and 2016-01-29T22:15:43Z Results requested for 2016-01-29T19:00:00Z to 2016-01-29T22:15:43Z Results found for 2016-01-29T19:24:57Z to 2016-01-29T21:24:57Z: 3/3 digest files valid 15/15 log files valid`- 
                    For API details, see [ValidateLogs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/validate-logs.html)in*AWS CLI Command Reference*.
 
-