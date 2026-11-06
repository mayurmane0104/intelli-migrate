# Amazon S3 Control examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_s3-control_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_s3-control_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon S3 Control.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-access-point`.

- **AWS CLI**
- 
            
                    **To create an access point**The following `create-access-point`example creates an access point named`finance-ap`for the bucket`business-records`in account 123456789012. Before running this example, replace the access point name, bucket name, and account number with appropriate values for your use case.`aws s3control create-access-point \ --account-id``123456789012`\ --bucket`business-records`\ --name`finance-ap`This command produces no output. For more information, see [Creating Access Points](https://docs.aws.amazon.com/AmazonS3/latest/dev/creating-access-points.html)in the*Amazon Simple Storage Service Developer Guide*.- 
                    For API details, see [CreateAccessPoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/create-access-point.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-job`.

- **AWS CLI**
- 
            
                    **To create an Amazon S3 batch operations job**The following `create-job`example creates an Amazon S3 batch operations job to tag objects as`confidential` in the bucket ``employee-records`.`aws s3control create-job \ --account-id``123456789012`\ --operation '`{"S3PutObjectTagging": { "TagSet": [{"Key":"confidential", "Value":"true"}] }}`' \ --report '`{"Bucket":"arn:aws:s3:::employee-records-logs","Prefix":"batch-op-create-job", "Format":"Report_CSV_20180820","Enabled":true,"ReportScope":"AllTasks"}`' \ --manifest '`{"Spec":{"Format":"S3BatchOperations_CSV_20180820","Fields":["Bucket","Key"]},"Location":{"ObjectArn":"arn:aws:s3:::employee-records-logs/inv-report/7a6a9be4-072c-407e-85a2-ec3e982f773e.csv","ETag":"69f52a4e9f797e987155d9c8f5880897"}}`' \ --priority`42`\ --role-arn`arn:aws:iam::123456789012:role/S3BatchJobRole`Output: `{ "JobId": "93735294-df46-44d5-8638-6356f335324e" }`- 
                    For API details, see [CreateJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/create-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-access-point-policy`.

- **AWS CLI**
- 
            
                    **To delete an access point policy**The following `delete-access-point-policy`example deletes the access point policy from the access point named`finance-ap`in account 123456789012. Before running this example, replace the access point name and account number with appropriate values for your use case.`aws s3control delete-access-point-policy \ --account-id``123456789012`\ --name`finance-ap`This command produces no output. For more information, see [Managing Data Access with Amazon S3 Access Points](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-points.html)in the*Amazon Simple Storage Service Developer Guide*.- 
                    For API details, see [DeleteAccessPointPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-access-point-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-access-point`.

- **AWS CLI**
- 
            
                    **To delete an access point**The following `delete-access-point`example deletes an access point named`finance-ap`in account 123456789012. Before running this example, replace the access point name and account number with appropriate values for your use case.`aws s3control delete-access-point \ --account-id``123456789012`\ --name`finance-ap`This command produces no output. For more information, see [Managing Data Access with Amazon S3 Access Points](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-points.html)in the*Amazon Simple Storage Service Developer Guide*.- 
                    For API details, see [DeleteAccessPoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-access-point.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-public-access-block`.

- **AWS CLI**
- 
            
                    **To delete block public access settings for an account**The following `delete-public-access-block`example deletes block public access settings for the specified account.`aws s3control delete-public-access-block \ --account-id``123456789012`This command produces no output. - 
                    For API details, see [DeletePublicAccessBlock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/delete-public-access-block.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-job`.

- **AWS CLI**
- 
            
                    **To describe an Amazon S3 batch operations job**The following `describe-job`provides configuration parameters and status for the specified batch operations job.`aws s3control describe-job \ --account-id``123456789012`\ --job-id`93735294-df46-44d5-8638-6356f335324e`Output: `{ "Job": { "TerminationDate": "2019-10-03T21:49:53.944Z", "JobId": "93735294-df46-44d5-8638-6356f335324e", "FailureReasons": [], "Manifest": { "Spec": { "Fields": [ "Bucket", "Key" ], "Format": "S3BatchOperations_CSV_20180820" }, "Location": { "ETag": "69f52a4e9f797e987155d9c8f5880897", "ObjectArn": "arn:aws:s3:::employee-records-logs/inv-report/7a6a9be4-072c-407e-85a2-ec3e982f773e.csv" } }, "Operation": { "S3PutObjectTagging": { "TagSet": [ { "Value": "true", "Key": "confidential" } ] } }, "RoleArn": "arn:aws:iam::123456789012:role/S3BatchJobRole", "ProgressSummary": { "TotalNumberOfTasks": 8, "NumberOfTasksFailed": 0, "NumberOfTasksSucceeded": 8 }, "Priority": 42, "Report": { "ReportScope": "AllTasks", "Format": "Report_CSV_20180820", "Enabled": true, "Prefix": "batch-op-create-job", "Bucket": "arn:aws:s3:::employee-records-logs" }, "JobArn": "arn:aws:s3:us-west-2:123456789012:job/93735294-df46-44d5-8638-6356f335324e", "CreationTime": "2019-10-03T21:48:48.048Z", "Status": "Complete" } }`- 
                    For API details, see [DescribeJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/describe-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-access-point-policy-status`.

- **AWS CLI**
- 
            
                    **To retrieve the access point policy status**The following `get-access-point-policy-status`example retrieves the access point policy status for the access point named`finance-ap`in account 123456789012. The access point policy status indicates whether the access point's policy allows public access. Before running this example, replace the access point name and account number with appropriate values for your use case.`aws s3control get-access-point-policy-status \ --account-id``123456789012`\ --name`finance-ap`Output: `{ "PolicyStatus": { "IsPublic": false } }`For more information about when an access point policy is considered public, see [The Meaning of "Public"](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status)in the*Amazon Simple Storage Service Developer Guide*.- 
                    For API details, see [GetAccessPointPolicyStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-access-point-policy-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-access-point-policy`.

- **AWS CLI**
- 
            
                    **To retrieve an access point policy**The following `get-access-point-policy`example retrieves the access point policy from the access point named`finance-ap`in account 123456789012. Before running this example, replace the access point name and account number with appropriate values for your use case.`aws s3control get-access-point-policy \ --account-id``123456789012`\ --name`finance-ap`Output: `{ "Policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::123456789012:role/Admin\"},\"Action\":\"s3:GetObject\",\"Resource\":\"arn:aws:s3:us-west-2:123456789012:accesspoint/finance-ap/object/records/*\"}]}" }`For more information, see [Managing Data Access with Amazon S3 Access Points](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-points.html)in the*Amazon Simple Storage Service Developer Guide*.- 
                    For API details, see [GetAccessPointPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-access-point-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-access-point`.

- **AWS CLI**
- 
            
                    **To retrieve access point configuration details**The following `get-access-point`example retrieves the configuration details for the access point named`finance-ap`in account 123456789012. Before running this example, replace the access point name and account number with appropriate values for your use case.`aws s3control get-access-point \ --account-id``123456789012`\ --name`finance-ap`Output: `{ "Name": "finance-ap", "Bucket": "business-records", "NetworkOrigin": "Internet", "PublicAccessBlockConfiguration": { "BlockPublicAcls": false, "IgnorePublicAcls": false, "BlockPublicPolicy": false, "RestrictPublicBuckets": false }, "CreationDate": "2020-01-01T00:00:00Z" }`For more information, see [Managing Data Access with Amazon S3 Access Points](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-points.html)in the*Amazon Simple Storage Service Developer Guide*.- 
                    For API details, see [GetAccessPoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-access-point.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-multi-region-access-point-routes`.

- **AWS CLI**
- 
            
                    **To query the current Multi-Region Access Point route configuration**The following `get-multi-region-access-point-routes`example returns the current routing configuration for the specified Multi-Region Access Point.`aws s3control get-multi-region-access-point-routes \ --region``Region`\ --account-id`111122223333`\ --mrap`MultiRegionAccessPoint_ARN`Output: `{ "Mrap": "arn:aws:s3::111122223333:accesspoint/0000000000000.mrap", "Routes": [ { "Bucket": "amzn-s3-demo-bucket1", "Region": "ap-southeast-2", "TrafficDialPercentage": 100 }, { "Bucket": "amzn-s3-demo-bucket2", "Region": "us-west-1", "TrafficDialPercentage": 0 } ] }`- 
                    For API details, see [GetMultiRegionAccessPointRoutes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-multi-region-access-point-routes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-public-access-block`.

- **AWS CLI**
- 
            
                    **To list public block access settings for an account**The following `get-public-access-block`example displays the block public access settings for the specified account.`aws s3control get-public-access-block \ --account-id``123456789012`Output: `{ "PublicAccessBlockConfiguration": { "BlockPublicPolicy": true, "RestrictPublicBuckets": true, "IgnorePublicAcls": true, "BlockPublicAcls": true } }`- 
                    For API details, see [GetPublicAccessBlock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/get-public-access-block.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-access-points`.

- **AWS CLI**
- 
            
                    **Example 1: To retrieve a list of all access points for an account**The following `list-access-points`example displays a list of all access points attached to buckets owned by account 123456789012.`aws s3control list-access-points \ --account-id``123456789012`Output: `{ "AccessPointList": [ { "Name": "finance-ap", "NetworkOrigin": "Internet", "Bucket": "business-records" }, { "Name": "managers-ap", "NetworkOrigin": "Internet", "Bucket": "business-records" }, { "Name": "private-network-ap", "NetworkOrigin": "VPC", "VpcConfiguration": { "VpcId": "1a2b3c" }, "Bucket": "business-records" }, { "Name": "customer-ap", "NetworkOrigin": "Internet", "Bucket": "external-docs" }, { "Name": "public-ap", "NetworkOrigin": "Internet", "Bucket": "external-docs" } ] }`**Example 2: To retrieve a list of all access points for a bucket**The following `list-access-points`example retrieves a list of all access points attached to the bucket`external-docs`owned by account 123456789012.`aws s3control list-access-points \ --account-id``123456789012`\ --bucket`external-docs`Output: `{ "AccessPointList": [ { "Name": "customer-ap", "NetworkOrigin": "Internet", "Bucket": "external-docs" }, { "Name": "public-ap", "NetworkOrigin": "Internet", "Bucket": "external-docs" } ] }`For more information, see [Managing Data Access with Amazon S3 Access Points](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-points.html)in the*Amazon Simple Storage Service Developer Guide*.- 
                    For API details, see [ListAccessPoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/list-access-points.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-jobs`.

- **AWS CLI**
- 
            
                    **To list an accounts Amazon S3 batch operations jobs**The following `list-jobs`example lists all recent batch operations jobs for the specified account.`aws s3control list-jobs \ --account-id``123456789012`Output: `{ "Jobs": [ { "Operation": "S3PutObjectTagging", "ProgressSummary": { "NumberOfTasksFailed": 0, "NumberOfTasksSucceeded": 8, "TotalNumberOfTasks": 8 }, "CreationTime": "2019-10-03T21:48:48.048Z", "Status": "Complete", "JobId": "93735294-df46-44d5-8638-6356f335324e", "Priority": 42 }, { "Operation": "S3PutObjectTagging", "ProgressSummary": { "NumberOfTasksFailed": 0, "NumberOfTasksSucceeded": 0, "TotalNumberOfTasks": 0 }, "CreationTime": "2019-10-03T21:46:07.084Z", "Status": "Failed", "JobId": "3f3c7619-02d3-4779-97f6-1d98dd313108", "Priority": 42 }, ] }`- 
                    For API details, see [ListJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/list-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-access-point-policy`.

- **AWS CLI**
- 
            
                    **To set an access point policy**The following `put-access-point-policy`example places the specified access point policy for the access point`finance-ap`in account 123456789012. If the access point`finance-ap`already has a policy, this command replaces the existing policy with the one specified in this command. Before running this example, replace the account number, access point name, and policy statements with appropriate values for your use case.`aws s3control put-access-point-policy \ --account-id``123456789012`\ --name`finance-ap`\ --policy`file://ap-policy.json`Contents of `ap-policy.json`:`{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "AWS": "arn:aws:iam::123456789012:user/Alice" }, "Action": "s3:GetObject", "Resource": "arn:aws:s3:us-west-2:123456789012:accesspoint/finance-ap/object/Alice/*" } ] }`This command produces no output. For more information, see [Managing Data Access with Amazon S3 Access Points](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-points.html)in the*Amazon Simple Storage Service Developer Guide*.- 
                    For API details, see [PutAccessPointPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/put-access-point-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-public-access-block`.

- **AWS CLI**
- 
            
                    **To edit block public access settings for an account**The following `put-public-access-block`example toggles all block public access settings to`true`for the specified account.`aws s3control put-public-access-block \ --account-id``123456789012`\ --public-access-block-configuration '`{"BlockPublicAcls": true, "IgnorePublicAcls": true, "BlockPublicPolicy": true, "RestrictPublicBuckets": true}`'This command produces no output. - 
                    For API details, see [PutPublicAccessBlock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/put-public-access-block.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `submit-multi-region-access-point-routes`.

- **AWS CLI**
- 
            
                    **To update your Multi-Region Access Point routing configuration**The following `submit-multi-region-access-point-routes`example updates the routing statuses of`amzn-s3-demo-bucket1`and`amzn-s3-demo-bucket2`in the`ap-southeast-2`Region for your Multi-Region Access Point.`aws s3control submit-multi-region-access-point-routes \ --region``ap-southeast-2`\ --account-id`111122223333`\ --mrap`MultiRegionAccessPoint_ARN`\ --route-updates`Bucket=amzn-s3-demo-bucket1,TrafficDialPercentage=100``Bucket=amzn-s3-demo-bucket2,TrafficDialPercentage=0`This command produces no output. - 
                    For API details, see [SubmitMultiRegionAccessPointRoutes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/submit-multi-region-access-point-routes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-job-priority`.

- **AWS CLI**
- 
            
                    **To update the job priority of an Amazon S3 batch operations job**The following `update-job-priority`example updates the specified job to a new priority.`aws s3control update-job-priority \ --account-id``123456789012`\ --job-id`8d9a18fe-c303-4d39-8ccc-860d372da386`\ --priority`52`Output: `{ "JobId": "8d9a18fe-c303-4d39-8ccc-860d372da386", "Priority": 52 }`- 
                    For API details, see [UpdateJobPriority](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/update-job-priority.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-job-status`.

- **AWS CLI**
- 
            
                    **To update the status of an Amazon S3 batch operations job**The following `update-job-status`example cancels the specified job which is awaiting approval.`aws s3control update-job-status \ --account-id``123456789012`\ --job-id`8d9a18fe-c303-4d39-8ccc-860d372da386`\ --requested-job-status`Cancelled`Output: `{ "Status": "Cancelled", "JobId": "8d9a18fe-c303-4d39-8ccc-860d372da386" }`The following `update-job-status`example confirms and runs the specified which is awaiting approval.`aws s3control update-job-status \ --account-id``123456789012`\ --job-id`5782949f-3301-4fb3-be34-8d5bab54dbca`\ --requested-job-status`Ready``Output::``{`"Status": "Ready", "JobId":`"5782949f-3301-4fb3-be34-8d5bab54dbca"``}`The following `update-job-status`example cancels the specified job which is running.`aws s3control update-job-status \ --account-id 123456789012 \ --job-id 5782949f-3301-4fb3-be34-8d5bab54dbca \ --requested-job-status Cancelled Output:: { "Status": "Cancelling", "JobId": "5782949f-3301-4fb3-be34-8d5bab54dbca" }`- 
                    For API details, see [UpdateJobStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/update-job-status.html)in*AWS CLI Command Reference*.
 
-