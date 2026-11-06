# Amazon S3 examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_s3_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_s3_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon S3.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `abort-multipart-upload`.

- **AWS CLI**
- 
            
                    **To abort the specified multipart upload**The following `abort-multipart-upload`command aborts a multipart upload for the key`multipart/01`in the bucket`amzn-s3-demo-bucket`.`aws s3api abort-multipart-upload \ --bucket``amzn-s3-demo-bucket`\ --key`multipart/01`\ --upload-id`dfRtDYU0WWCCcH43C3WFbkRONycyCpTJJvxu2i5GYkZljF.Yxwh6XG7WfS2vC4to6HiV6Yjlx.cph0gtNBtJ8P3URCSbB7rjxI5iEwVDmgaXZOGgkk5nVTW16HOQ5l0R`The upload ID required by this command is output by `create-multipart-upload`and can also be retrieved with`list-multipart-uploads`.- 
                    For API details, see [AbortMultipartUpload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/abort-multipart-upload.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `complete-multipart-upload`.

- **AWS CLI**
- 
            
                    The following command completes a multipart upload for the key `multipart/01`in the bucket`amzn-s3-demo-bucket`:`aws s3api complete-multipart-upload --multipart-upload``file://mpustruct`--bucket`amzn-s3-demo-bucket`--key '`multipart/01`' --upload-id`dfRtDYU0WWCCcH43C3WFbkRONycyCpTJJvxu2i5GYkZljF.Yxwh6XG7WfS2vC4to6HiV6Yjlx.cph0gtNBtJ8P3URCSbB7rjxI5iEwVDmgaXZOGgkk5nVTW16HOQ5l0R`The upload ID required by this command is output by `create-multipart-upload`and can also be retrieved with`list-multipart-uploads`.The multipart upload option in the above command takes a JSON structure that describes the parts of the multipart upload that should be reassembled into the complete file. In this example, the `file://`prefix is used to load the JSON structure from a file in the local folder named`mpustruct`.mpustruct: `{ "Parts": [ { "ETag": "e868e0f4719e394144ef36531ee6824c", "PartNumber": 1 }, { "ETag": "6bb2b12753d66fe86da4998aa33fffb0", "PartNumber": 2 }, { "ETag": "d0a0112e841abec9c9ec83406f0159c8", "PartNumber": 3 } ] }`The ETag value for each part is upload is output each time you upload a part using the `upload-part`command and can also be retrieved by calling`list-parts`or calculated by taking the MD5 checksum of each part.Output: `{ "ETag": "\"3944a9f7a4faab7f78788ff6210f63f0-3\"", "Bucket": "amzn-s3-demo-bucket", "Location": "https://amzn-s3-demo-bucket.s3.amazonaws.com/multipart%2F01", "Key": "multipart/01" }`- 
                    For API details, see [CompleteMultipartUpload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/complete-multipart-upload.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `copy-object`.

- **AWS CLI**
- 
            
                    The following command copies an object from `bucket-1`to`bucket-2`:`aws s3api copy-object --copy-source``bucket-1/test.txt`--key`test.txt`--bucket`bucket-2`Output: `{ "CopyObjectResult": { "LastModified": "2015-11-10T01:07:25.000Z", "ETag": "\"589c8b79c230a6ecd5a7e1d040a9a030\"" }, "VersionId": "YdnYvTCVDqRRFA.NFJjy36p0hxifMlkA" }`- 
                    For API details, see [CopyObject](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/copy-object.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cp`.

- **AWS CLI**
- 
            
                    **Example 1: Copying a local file to S3**The following `cp`command copies a single file to a specified bucket and key:`aws s3 cp``test.txt``s3://amzn-s3-demo-bucket/test2.txt`Output: `upload: test.txt to s3://amzn-s3-demo-bucket/test2.txt`**Example 2: Copying a local file to S3 with an expiration date**The following `cp`command copies a single file to a specified bucket and key that expires at the specified ISO 8601 timestamp:`aws s3 cp``test.txt``s3://amzn-s3-demo-bucket/test2.txt`\ --expires`2014-10-01T20:30:00Z`Output: `upload: test.txt to s3://amzn-s3-demo-bucket/test2.txt`**Example 3: Copying a file from S3 to S3**The following `cp`command copies a single s3 object to a specified bucket and key:`aws s3 cp``s3://amzn-s3-demo-bucket/test.txt``s3://amzn-s3-demo-bucket/test2.txt`Output: `copy: s3://amzn-s3-demo-bucket/test.txt to s3://amzn-s3-demo-bucket/test2.txt`**Example 4: Copying an S3 object to a local file**The following `cp`command copies a single object to a specified file locally:`aws s3 cp``s3://amzn-s3-demo-bucket/test.txt``test2.txt`Output: `download: s3://amzn-s3-demo-bucket/test.txt to test2.txt`**Example 5: Copying an S3 object from one bucket to another**The following `cp`command copies a single object to a specified bucket while retaining its original name:`aws s3 cp``s3://amzn-s3-demo-bucket/test.txt``s3://amzn-s3-demo-bucket2/`Output: `copy: s3://amzn-s3-demo-bucket/test.txt to s3://amzn-s3-demo-bucket2/test.txt`**Example 6: Recursively copying S3 objects to a local directory**When passed with the parameter `--recursive`, the following`cp`command recursively copies all objects under a specified prefix and bucket to a specified directory. In this example, the bucket`amzn-s3-demo-bucket`has the objects`test1.txt`and`test2.txt`:`aws s3 cp``s3://amzn-s3-demo-bucket``.`\ --recursiveOutput: `download: s3://amzn-s3-demo-bucket/test1.txt to test1.txt download: s3://amzn-s3-demo-bucket/test2.txt to test2.txt`**Example 7: Recursively copying local files to S3**When passed with the parameter `--recursive`, the following`cp`command recursively copies all files under a specified directory to a specified bucket and prefix while excluding some files by using an`--exclude`parameter. In this example, the directory`myDir`has the files`test1.txt`and`test2.jpg`:`aws s3 cp``myDir``s3://amzn-s3-demo-bucket/`\ --recursive \ --exclude`"*.jpg"`Output: `upload: myDir/test1.txt to s3://amzn-s3-demo-bucket/test1.txt`**Example 8: Recursively copying S3 objects to another bucket**When passed with the parameter `--recursive`, the following`cp`command recursively copies all objects under a specified bucket to another bucket while excluding some objects by using an`--exclude`parameter. In this example, the bucket`amzn-s3-demo-bucket`has the objects`test1.txt`and`another/test1.txt`:`aws s3 cp``s3://amzn-s3-demo-bucket/``s3://amzn-s3-demo-bucket2/`\ --recursive \ --exclude`"another/*"`Output: `copy: s3://amzn-s3-demo-bucket/test1.txt to s3://amzn-s3-demo-bucket2/test1.txt`You can combine `--exclude`and`--include`options to copy only objects that match a pattern, excluding all others:`aws s3 cp``s3://amzn-s3-demo-bucket/logs/``s3://amzn-s3-demo-bucket2/logs/`\ --recursive \ --exclude`"*"`\ --include`"*.log"`Output: `copy: s3://amzn-s3-demo-bucket/logs/test/test.log to s3://amzn-s3-demo-bucket2/logs/test/test.log copy: s3://amzn-s3-demo-bucket/logs/test3.log to s3://amzn-s3-demo-bucket2/logs/test3.log`**Example 9: Setting the Access Control List (ACL) while copying an S3 object**The following `cp`command copies a single object to a specified bucket and key while setting the ACL to`public-read-write`:`aws s3 cp``s3://amzn-s3-demo-bucket/test.txt``s3://amzn-s3-demo-bucket/test2.txt`\ --acl`public-read-write`Output: `copy: s3://amzn-s3-demo-bucket/test.txt to s3://amzn-s3-demo-bucket/test2.txt`Note that if you're using the `--acl`option, ensure that any associated IAM policies include the`"s3:PutObjectAcl"`action:`aws iam get-user-policy \ --user-name``myuser`\ --policy-name`mypolicy`Output: `{ "UserName": "myuser", "PolicyName": "mypolicy", "PolicyDocument": { "Version":"2012-10-17", "Statement": [ { "Action": [ "s3:PutObject", "s3:PutObjectAcl" ], "Resource": [ "arn:aws:s3:::amzn-s3-demo-bucket/*" ], "Effect": "Allow", "Sid": "Stmt1234567891234" } ] } }`**Example 10: Granting permissions for an S3 object**The following `cp`command illustrates the use of the`--grants`option to grant read access to all users identified by URI and full control to a specific user identified by their Canonical ID:`aws s3 cp``file.txt``s3://amzn-s3-demo-bucket/`--grants`read=uri=http://acs.amazonaws.com/groups/global/AllUsers``full=id=79a59df900b949e55d96a1e698fbacedfd6e09d98eacf8f8d5218e7cd47ef2be`Output: `upload: file.txt to s3://amzn-s3-demo-bucket/file.txt`**Example 11: Uploading a local file stream to S3**PowerShell may alter the encoding of or add a CRLF to piped input. The following `cp`command uploads a local file stream from standard input to a specified bucket and key:`aws s3 cp``-``s3://amzn-s3-demo-bucket/stream.txt`**Example 12: Uploading a local file stream that is larger than 50GB to S3**The following `cp`command uploads a 51GB local file stream from standard input to a specified bucket and key. The`--expected-size`option must be provided, or the upload may fail when it reaches the default part limit of 10,000:`aws s3 cp``-``s3://amzn-s3-demo-bucket/stream.txt`--expected-size`54760833024`**Example 13: Downloading an S3 object as a local file stream**PowerShell may alter the encoding of or add a CRLF to piped or redirected output. The following `cp`command downloads an S3 object locally as a stream to standard output. Downloading as a stream is not currently compatible with the`--recursive`parameter:`aws s3 cp``s3://amzn-s3-demo-bucket/stream.txt``-`**Example 14: Uploading to an S3 access point**The following `cp`command uploads a single file (`mydoc.txt`) to the access point (`myaccesspoint`) at the key (`mykey`):`aws s3 cp``mydoc.txt``s3://arn:aws:s3:us-west-2:123456789012:accesspoint/myaccesspoint/mykey`Output: `upload: mydoc.txt to s3://arn:aws:s3:us-west-2:123456789012:accesspoint/myaccesspoint/mykey`**Example 15: Downloading from an S3 access point**The following `cp`command downloads a single object (`mykey`) from the access point (`myaccesspoint`) to the local file (`mydoc.txt`):`aws s3 cp``s3://arn:aws:s3:us-west-2:123456789012:accesspoint/myaccesspoint/mykey``mydoc.txt`Output: `download: s3://arn:aws:s3:us-west-2:123456789012:accesspoint/myaccesspoint/mykey to mydoc.txt`- 
                    For API details, see [Cp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/cp.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-bucket`.

- **AWS CLI**
- 
            
                    **Example 1: To create a bucket**The following `create-bucket`example creates a bucket named`amzn-s3-demo-bucket`:`aws s3api create-bucket \ --bucket``amzn-s3-demo-bucket`\ --region`us-east-1`Output: `{ "Location": "/amzn-s3-demo-bucket" }`For more information, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html)in the*Amazon S3 User Guide*.**Example 2: To create a bucket with owner enforced**The following `create-bucket`example creates a bucket named`amzn-s3-demo-bucket`that uses the bucket owner enforced setting for S3 Object Ownership.`aws s3api create-bucket \ --bucket``amzn-s3-demo-bucket`\ --region`us-east-1`\ --object-ownership`BucketOwnerEnforced`Output: `{ "Location": "/amzn-s3-demo-bucket" }`For more information, see [Controlling ownership of objects and disabling ACLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html)in the*Amazon S3 User Guide*.**Example 3: To create a bucket outside of the ``us-east-1`` region**The following `create-bucket`example creates a bucket named`amzn-s3-demo-bucket`in the`eu-west-1`region. Regions outside of`us-east-1`require the appropriate`LocationConstraint`to be specified in order to create the bucket in the desired region.`aws s3api create-bucket \ --bucket``amzn-s3-demo-bucket`\ --region`eu-west-1`\ --create-bucket-configuration`LocationConstraint=eu-west-1`Output: `{ "Location": "http://amzn-s3-demo-bucket.s3.amazonaws.com/" }`For more information, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html)in the*Amazon S3 User Guide*.- 
                    For API details, see [CreateBucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-bucket.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-multipart-upload`.

- **AWS CLI**
- 
            
                    The following command creates a multipart upload in the bucket `amzn-s3-demo-bucket`with the key`multipart/01`:`aws s3api create-multipart-upload --bucket``amzn-s3-demo-bucket`--key '`multipart/01`'Output: `{ "Bucket": "amzn-s3-demo-bucket", "UploadId": "dfRtDYU0WWCCcH43C3WFbkRONycyCpTJJvxu2i5GYkZljF.Yxwh6XG7WfS2vC4to6HiV6Yjlx.cph0gtNBtJ8P3URCSbB7rjxI5iEwVDmgaXZOGgkk5nVTW16HOQ5l0R", "Key": "multipart/01" }`The completed file will be named `01`in a folder called`multipart`in the bucket`amzn-s3-demo-bucket`. Save the upload ID, key and bucket name for use with the`upload-part`command.- 
                    For API details, see [CreateMultipartUpload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-multipart-upload.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-bucket-analytics-configuration`.

- **AWS CLI**
- 
            
                    **To delete an analytics configuration for a bucket**The following `delete-bucket-analytics-configuration`example removes the analytics configuration for the specified bucket and ID.`aws s3api delete-bucket-analytics-configuration \ --bucket``amzn-s3-demo-bucket`\ --id`1`This command produces no output. - 
                    For API details, see [DeleteBucketAnalyticsConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-analytics-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-bucket-cors`.

- **AWS CLI**
- 
            
                    The following command deletes a Cross-Origin Resource Sharing configuration from a bucket named `amzn-s3-demo-bucket`:`aws s3api delete-bucket-cors --bucket``amzn-s3-demo-bucket`- 
                    For API details, see [DeleteBucketCors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-cors.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-bucket-encryption`.

- **AWS CLI**
- 
            
                    **To delete the server-side encryption configuration of a bucket**The following `delete-bucket-encryption`example deletes the server-side encryption configuration of the specified bucket.`aws s3api delete-bucket-encryption \ --bucket``amzn-s3-demo-bucket`This command produces no output. - 
                    For API details, see [DeleteBucketEncryption](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-encryption.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-bucket-intelligent-tiering-configuration`.

- **AWS CLI**
- 
            
                    **To remove an S3 Intelligent-Tiering configuration on a bucket**The following `delete-bucket-intelligent-tiering-configuration`example removes an S3 Intelligent-Tiering configuration, named ExampleConfig, on a bucket.`aws s3api delete-bucket-intelligent-tiering-configuration \ --bucket``amzn-s3-demo-bucket`\ --id`ExampleConfig`This command produces no output. For more information, see [Using S3 Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-intelligent-tiering.html)in the*Amazon S3 User Guide*.- 
                    For API details, see [DeleteBucketIntelligentTieringConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-intelligent-tiering-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-bucket-inventory-configuration`.

- **AWS CLI**
- 
            
                    **To delete the inventory configuration of a bucket**The following `delete-bucket-inventory-configuration`example deletes the inventory configuration with ID`1`for the specified bucket.`aws s3api delete-bucket-inventory-configuration \ --bucket``amzn-s3-demo-bucket`\ --id`1`This command produces no output. - 
                    For API details, see [DeleteBucketInventoryConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-inventory-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-bucket-lifecycle`.

- **AWS CLI**
- 
            
                    The following command deletes a lifecycle configuration from a bucket named `amzn-s3-demo-bucket`:`aws s3api delete-bucket-lifecycle --bucket``amzn-s3-demo-bucket`- 
                    For API details, see [DeleteBucketLifecycle](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-lifecycle.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-bucket-metrics-configuration`.

- **AWS CLI**
- 
            
                    **To delete a metrics configuration for a bucket**The following `delete-bucket-metrics-configuration`example removes the metrics configuration for the specified bucket and ID.`aws s3api delete-bucket-metrics-configuration \ --bucket``amzn-s3-demo-bucket`\ --id`123`This command produces no output. - 
                    For API details, see [DeleteBucketMetricsConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-metrics-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-bucket-ownership-controls`.

- **AWS CLI**
- 
            
                    **To remove the bucket ownership settings of a bucket**The following `delete-bucket-ownership-controls`example removes the bucket ownership settings of a bucket.`aws s3api delete-bucket-ownership-controls \ --bucket``amzn-s3-demo-bucket`This command produces no output. For more information, see [Setting Object Ownership on an existing bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-ownership-existing-bucket.html)in the*Amazon S3 User Guide*.- 
                    For API details, see [DeleteBucketOwnershipControls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-ownership-controls.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-bucket-policy`.

- **AWS CLI**
- 
            
                    The following command deletes a bucket policy from a bucket named `amzn-s3-demo-bucket`:`aws s3api delete-bucket-policy --bucket``amzn-s3-demo-bucket`- 
                    For API details, see [DeleteBucketPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-bucket-replication`.

- **AWS CLI**
- 
            
                    The following command deletes a replication configuration from a bucket named `amzn-s3-demo-bucket`:`aws s3api delete-bucket-replication --bucket``amzn-s3-demo-bucket`- 
                    For API details, see [DeleteBucketReplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-replication.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-bucket-tagging`.

- **AWS CLI**
- 
            
                    The following command deletes a tagging configuration from a bucket named `amzn-s3-demo-bucket`:`aws s3api delete-bucket-tagging --bucket``amzn-s3-demo-bucket`- 
                    For API details, see [DeleteBucketTagging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-tagging.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-bucket-website`.

- **AWS CLI**
- 
            
                    The following command deletes a website configuration from a bucket named `amzn-s3-demo-bucket`:`aws s3api delete-bucket-website --bucket``amzn-s3-demo-bucket`- 
                    For API details, see [DeleteBucketWebsite](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-website.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-bucket`.

- **AWS CLI**
- 
            
                    The following command deletes a bucket named `amzn-s3-demo-bucket`:`aws s3api delete-bucket --bucket``amzn-s3-demo-bucket`--region`us-east-1`- 
                    For API details, see [DeleteBucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-object-tagging`.

- **AWS CLI**
- 
            
                    **To delete the tag sets of an object**The following `delete-object-tagging`example deletes the tag with the specified key from the object`doc1.rtf`.`aws s3api delete-object-tagging \ --bucket``amzn-s3-demo-bucket`\ --key`doc1.rtf`This command produces no output. - 
                    For API details, see [DeleteObjectTagging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-object-tagging.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-object`.

- **AWS CLI**
- 
            
                    The following command deletes an object named `test.txt`from a bucket named`amzn-s3-demo-bucket`:`aws s3api delete-object --bucket``amzn-s3-demo-bucket`--key`test.txt`If bucket versioning is enabled, the output will contain the version ID of the delete marker: `{ "VersionId": "9_gKg5vG56F.TTEUdwkxGpJ3tNDlWlGq", "DeleteMarker": true }`For more information about deleting objects, see Deleting Objects in the *Amazon S3 Developer Guide*.- 
                    For API details, see [DeleteObject](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-object.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-objects`.

- **AWS CLI**
- 
            
                    The following command deletes an object from a bucket named `amzn-s3-demo-bucket`:`aws s3api delete-objects --bucket``amzn-s3-demo-bucket`--delete`file://delete.json``delete.json`is a JSON document in the current directory that specifies the object to delete:`{ "Objects": [ { "Key": "test1.txt" } ], "Quiet": false }`Output: `{ "Deleted": [ { "DeleteMarkerVersionId": "mYAT5Mc6F7aeUL8SS7FAAqUPO1koHwzU", "Key": "test1.txt", "DeleteMarker": true } ] }`- 
                    For API details, see [DeleteObjects](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-objects.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-public-access-block`.

- **AWS CLI**
- 
            
                    **To delete the block public access configuration for a bucket**The following `delete-public-access-block`example removes the block public access configuration on the specified bucket.`aws s3api delete-public-access-block \ --bucket``amzn-s3-demo-bucket`This command produces no output. - 
                    For API details, see [DeletePublicAccessBlock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-public-access-block.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-bucket-accelerate-configuration`.

- **AWS CLI**
- 
            
                    **To retrieve the accelerate configuration of a bucket**The following `get-bucket-accelerate-configuration`example retrieves the accelerate configuration for the specified bucket.`aws s3api get-bucket-accelerate-configuration \ --bucket``amzn-s3-demo-bucket`Output: `{ "Status": "Enabled" }`- 
                    For API details, see [GetBucketAccelerateConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-accelerate-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-bucket-acl`.

- **AWS CLI**
- 
            
                    The following command retrieves the access control list for a bucket named `amzn-s3-demo-bucket`:`aws s3api get-bucket-acl --bucket``amzn-s3-demo-bucket`Output: `{ "Owner": { "DisplayName": "my-username", "ID": "7009a8971cd538e11f6b6606438875e7c86c5b672f46db45460ddcd087d36c32" }, "Grants": [ { "Grantee": { "DisplayName": "my-username", "ID": "7009a8971cd538e11f6b6606438875e7c86c5b672f46db45460ddcd087d36c32" }, "Permission": "FULL_CONTROL" } ] }`- 
                    For API details, see [GetBucketAcl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-acl.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-bucket-analytics-configuration`.

- **AWS CLI**
- 
            
                    **To retrieve the analytics configuration for a bucket with a specific ID**The following `get-bucket-analytics-configuration`example displays the analytics configuration for the specified bucket and ID.`aws s3api get-bucket-analytics-configuration \ --bucket``amzn-s3-demo-bucket`\ --id`1`Output: `{ "AnalyticsConfiguration": { "StorageClassAnalysis": {}, "Id": "1" } }`- 
                    For API details, see [GetBucketAnalyticsConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-analytics-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-bucket-cors`.

- **AWS CLI**
- 
            
                    The following command retrieves the Cross-Origin Resource Sharing configuration for a bucket named `amzn-s3-demo-bucket`:`aws s3api get-bucket-cors --bucket``amzn-s3-demo-bucket`Output: `{ "CORSRules": [ { "AllowedHeaders": [ "*" ], "ExposeHeaders": [ "x-amz-server-side-encryption" ], "AllowedMethods": [ "PUT", "POST", "DELETE" ], "MaxAgeSeconds": 3000, "AllowedOrigins": [ "http://www.example.com" ] }, { "AllowedHeaders": [ "Authorization" ], "MaxAgeSeconds": 3000, "AllowedMethods": [ "GET" ], "AllowedOrigins": [ "*" ] } ] }`- 
                    For API details, see [GetBucketCors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-cors.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-bucket-encryption`.

- **AWS CLI**
- 
            
                    **To retrieve the server-side encryption configuration for a bucket**The following `get-bucket-encryption`example retrieves the server-side encryption configuration for the bucket`amzn-s3-demo-bucket`.`aws s3api get-bucket-encryption \ --bucket``amzn-s3-demo-bucket`Output: `{ "ServerSideEncryptionConfiguration": { "Rules": [ { "ApplyServerSideEncryptionByDefault": { "SSEAlgorithm": "AES256" } } ] } }`- 
                    For API details, see [GetBucketEncryption](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-encryption.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-bucket-intelligent-tiering-configuration`.

- **AWS CLI**
- 
            
                    **To retrieve an S3 Intelligent-Tiering configuration on a bucket**The following `get-bucket-intelligent-tiering-configuration`example retrieves an S3 Intelligent-Tiering configuration, named ExampleConfig, on a bucket.`aws s3api get-bucket-intelligent-tiering-configuration \ --bucket``amzn-s3-demo-bucket`\ --id`ExampleConfig`Output: `{ "IntelligentTieringConfiguration": { "Id": "ExampleConfig2", "Filter": { "Prefix": "images" }, "Status": "Enabled", "Tierings": [ { "Days": 90, "AccessTier": "ARCHIVE_ACCESS" }, { "Days": 180, "AccessTier": "DEEP_ARCHIVE_ACCESS" } ] } }`For more information, see [Using S3 Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-intelligent-tiering.html)in the*Amazon S3 User Guide*.- 
                    For API details, see [GetBucketIntelligentTieringConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-intelligent-tiering-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-bucket-inventory-configuration`.

- **AWS CLI**
- 
            
                    **To retrieve the inventory configuration for a bucket**The following `get-bucket-inventory-configuration`example retrieves the inventory configuration for the specified bucket with ID`1`.`aws s3api get-bucket-inventory-configuration \ --bucket``amzn-s3-demo-bucket`\ --id`1`Output: `{ "InventoryConfiguration": { "IsEnabled": true, "Destination": { "S3BucketDestination": { "Format": "ORC", "Bucket": "arn:aws:s3:::amzn-s3-demo-bucket", "AccountId": "123456789012" } }, "IncludedObjectVersions": "Current", "Id": "1", "Schedule": { "Frequency": "Weekly" } } }`- 
                    For API details, see [GetBucketInventoryConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-inventory-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-bucket-lifecycle-configuration`.

- **AWS CLI**
- 
            
                    The following command retrieves the lifecycle configuration for a bucket named `amzn-s3-demo-bucket`:`aws s3api get-bucket-lifecycle-configuration --bucket``amzn-s3-demo-bucket`Output: `{ "Rules": [ { "ID": "Move rotated logs to Glacier", "Prefix": "rotated/", "Status": "Enabled", "Transitions": [ { "Date": "2015-11-10T00:00:00.000Z", "StorageClass": "GLACIER" } ] }, { "Status": "Enabled", "Prefix": "", "NoncurrentVersionTransitions": [ { "NoncurrentDays": 0, "StorageClass": "GLACIER" } ], "ID": "Move old versions to Glacier" } ] }`- 
                    For API details, see [GetBucketLifecycleConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-lifecycle-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-bucket-lifecycle`.

- **AWS CLI**
- 
            
                    The following command retrieves the lifecycle configuration for a bucket named `amzn-s3-demo-bucket`:`aws s3api get-bucket-lifecycle --bucket``amzn-s3-demo-bucket`Output: `{ "Rules": [ { "ID": "Move to Glacier after sixty days (objects in logs/2015/)", "Prefix": "logs/2015/", "Status": "Enabled", "Transition": { "Days": 60, "StorageClass": "GLACIER" } }, { "Expiration": { "Date": "2016-01-01T00:00:00.000Z" }, "ID": "Delete 2014 logs in 2016.", "Prefix": "logs/2014/", "Status": "Enabled" } ] }`- 
                    For API details, see [GetBucketLifecycle](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-lifecycle.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-bucket-location`.

- **AWS CLI**
- 
            
                    The following command retrieves the location constraint for a bucket named `amzn-s3-demo-bucket`, if a constraint exists:`aws s3api get-bucket-location --bucket``amzn-s3-demo-bucket`Output: `{ "LocationConstraint": "us-west-2" }`- 
                    For API details, see [GetBucketLocation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-location.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-bucket-logging`.

- **AWS CLI**
- 
            
                    **To retrieve the logging status for a bucket**The following `get-bucket-logging`example retrieves the logging status for the specified bucket.`aws s3api get-bucket-logging \ --bucket``amzn-s3-demo-bucket`Output: `{ "LoggingEnabled": { "TargetPrefix": "", "TargetBucket": "amzn-s3-demo-bucket-logs" } }`- 
                    For API details, see [GetBucketLogging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-logging.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-bucket-metrics-configuration`.

- **AWS CLI**
- 
            
                    **To retrieve the metrics configuration for a bucket with a specific ID**The following `get-bucket-metrics-configuration`example displays the metrics configuration for the specified bucket and ID.`aws s3api get-bucket-metrics-configuration \ --bucket``amzn-s3-demo-bucket`\ --id`123`Output: `{ "MetricsConfiguration": { "Filter": { "Prefix": "logs" }, "Id": "123" } }`- 
                    For API details, see [GetBucketMetricsConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-metrics-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-bucket-notification-configuration`.

- **AWS CLI**
- 
            
                    The following command retrieves the notification configuration for a bucket named `amzn-s3-demo-bucket`:`aws s3api get-bucket-notification-configuration --bucket``amzn-s3-demo-bucket`Output: `{ "TopicConfigurations": [ { "Id": "YmQzMmEwM2EjZWVlI0NGItNzVtZjI1MC00ZjgyLWZDBiZWNl", "TopicArn": "arn:aws:sns:us-west-2:123456789012:my-notification-topic", "Events": [ "s3:ObjectCreated:*" ] } ] }`- 
                    For API details, see [GetBucketNotificationConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-notification-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-bucket-notification`.

- **AWS CLI**
- 
            
                    The following command retrieves the notification configuration for a bucket named `amzn-s3-demo-bucket`:`aws s3api get-bucket-notification --bucket``amzn-s3-demo-bucket`Output: `{ "TopicConfiguration": { "Topic": "arn:aws:sns:us-west-2:123456789012:my-notification-topic", "Id": "YmQzMmEwM2EjZWVlI0NGItNzVtZjI1MC00ZjgyLWZDBiZWNl", "Event": "s3:ObjectCreated:*", "Events": [ "s3:ObjectCreated:*" ] } }`- 
                    For API details, see [GetBucketNotification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-notification.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-bucket-ownership-controls`.

- **AWS CLI**
- 
            
                    **To retrieve the bucket ownership settings of a bucket**The following `get-bucket-ownership-controls`example retrieves the bucket ownership settings of a bucket.`aws s3api get-bucket-ownership-controls \ --bucket``amzn-s3-demo-bucket`Output: `{ "OwnershipControls": { "Rules": [ { "ObjectOwnership": "BucketOwnerEnforced" } ] } }`For more information, see [Viewing the Object Ownership setting for an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-ownership-retrieving.html)in the*Amazon S3 User Guide*.- 
                    For API details, see [GetBucketOwnershipControls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-ownership-controls.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-bucket-policy-status`.

- **AWS CLI**
- 
            
                    **To retrieve the policy status for a bucket indicating whether the bucket is public**The following `get-bucket-policy-status`example retrieves the policy status for the bucket`amzn-s3-demo-bucket`.`aws s3api get-bucket-policy-status \ --bucket``amzn-s3-demo-bucket`Output: `{ "PolicyStatus": { "IsPublic": false } }`- 
                    For API details, see [GetBucketPolicyStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-policy-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-bucket-policy`.

- **AWS CLI**
- 
            
                    The following command retrieves the bucket policy for a bucket named `amzn-s3-demo-bucket`:`aws s3api get-bucket-policy --bucket``amzn-s3-demo-bucket`Output: `{ "Policy": "{\"Version\":\"2008-10-17\",\"Statement\":[{\"Sid\":\"\",\"Effect\":\"Allow\",\"Principal\":\"*\",\"Action\":\"s3:GetObject\",\"Resource\":\"arn:aws:s3:::amzn-s3-demo-bucket/*\"},{\"Sid\":\"\",\"Effect\":\"Deny\",\"Principal\":\"*\",\"Action\":\"s3:GetObject\",\"Resource\":\"arn:aws:s3:::amzn-s3-demo-bucket/secret/*\"}]}" }`Get and put a bucket policyThe following example shows how you can download an Amazon S3 bucket policy, make modifications to the file, and then use `put-bucket-policy`to apply the modified bucket policy. To download the bucket policy to a file, you can run:`aws s3api get-bucket-policy --bucket amzn-s3-demo-bucket --query Policy --output text > policy.json`You can then modify the `policy.json`file as needed. Finally you can apply this modified policy back to the S3 bucket by running:`policy.json`file as needed. Finally you can apply this modified policy back to the S3 bucket by running:file as needed. Finally you can apply this modified policy back to the S3 bucket by running: `aws s3api put-bucket-policy --bucket amzn-s3-demo-bucket --policy file://policy.json`- 
                    For API details, see [GetBucketPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-bucket-replication`.

- **AWS CLI**
- 
            
                    The following command retrieves the replication configuration for a bucket named `amzn-s3-demo-bucket`:`aws s3api get-bucket-replication --bucket``amzn-s3-demo-bucket`Output: `{ "ReplicationConfiguration": { "Rules": [ { "Status": "Enabled", "Prefix": "", "Destination": { "Bucket": "arn:aws:s3:::amzn-s3-demo-bucket-backup", "StorageClass": "STANDARD" }, "ID": "ZmUwNzE4ZmQ4tMjVhOS00MTlkLOGI4NDkzZTIWJjNTUtYTA1" } ], "Role": "arn:aws:iam::123456789012:role/s3-replication-role" } }`- 
                    For API details, see [GetBucketReplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-replication.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-bucket-request-payment`.

- **AWS CLI**
- 
            
                    **To retrieve the request payment configuration for a bucket**The following `get-bucket-request-payment`example retrieves the requester pays configuration for the specified bucket.`aws s3api get-bucket-request-payment \ --bucket``amzn-s3-demo-bucket`Output: `{ "Payer": "BucketOwner" }`- 
                    For API details, see [GetBucketRequestPayment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-request-payment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-bucket-tagging`.

- **AWS CLI**
- 
            
                    The following command retrieves the tagging configuration for a bucket named `amzn-s3-demo-bucket`:`aws s3api get-bucket-tagging --bucket``amzn-s3-demo-bucket`Output: `{ "TagSet": [ { "Value": "marketing", "Key": "organization" } ] }`- 
                    For API details, see [GetBucketTagging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-tagging.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-bucket-versioning`.

- **AWS CLI**
- 
            
                    The following command retrieves the versioning configuration for a bucket named `amzn-s3-demo-bucket`:`aws s3api get-bucket-versioning --bucket``amzn-s3-demo-bucket`Output: `{ "Status": "Enabled" }`- 
                    For API details, see [GetBucketVersioning](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-versioning.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-bucket-website`.

- **AWS CLI**
- 
            
                    The following command retrieves the static website configuration for a bucket named `amzn-s3-demo-bucket`:`aws s3api get-bucket-website --bucket``amzn-s3-demo-bucket`Output: `{ "IndexDocument": { "Suffix": "index.html" }, "ErrorDocument": { "Key": "error.html" } }`- 
                    For API details, see [GetBucketWebsite](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-website.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-object-acl`.

- **AWS CLI**
- 
            
                    The following command retrieves the access control list for an object in a bucket named `amzn-s3-demo-bucket`:`aws s3api get-object-acl --bucket``amzn-s3-demo-bucket`--key`index.html`Output: `{ "Owner": { "DisplayName": "my-username", "ID": "7009a8971cd538e11f6b6606438875e7c86c5b672f46db45460ddcd087d36c32" }, "Grants": [ { "Grantee": { "DisplayName": "my-username", "ID": "7009a8971cd538e11f6b6606438875e7c86c5b672f46db45460ddcd087d36c32" }, "Permission": "FULL_CONTROL" }, { "Grantee": { "URI": "http://acs.amazonaws.com/groups/global/AllUsers" }, "Permission": "READ" } ] }`- 
                    For API details, see [GetObjectAcl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object-acl.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-object-attributes`.

- **AWS CLI**
- 
            
                    **To retrieves metadata from an object without returning the object itself**The following `get-object-attributes`example retrieves metadata from the object`doc1.rtf`.`aws s3api get-object-attributes \ --bucket``amzn-s3-demo-bucket`\ --key`doc1.rtf`\ --object-attributes`"StorageClass"``"ETag"``"ObjectSize"`Output: `{ "LastModified": "2022-03-15T19:37:31+00:00", "VersionId": "IuCPjXTDzHNfldAuitVBIKJpF2p1fg4P", "ETag": "b662d79adeb7c8d787ea7eafb9ef6207", "StorageClass": "STANDARD", "ObjectSize": 405 }`For more information, see [GetObjectAttributes](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributes.html)in the Amazon S3 API Reference.- 
                    For API details, see [GetObjectAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-object-legal-hold`.

- **AWS CLI**
- 
            
                    **Retrieves the Legal Hold status of an object**The following `get-object-legal-hold`example retrieves the Legal Hold status for the specified object.`aws s3api get-object-legal-hold \ --bucket``amzn-s3-demo-bucket-with-object-lock`\ --key`doc1.rtf`Output: `{ "LegalHold": { "Status": "ON" } }`- 
                    For API details, see [GetObjectLegalHold](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object-legal-hold.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-object-lock-configuration`.

- **AWS CLI**
- 
            
                    **To retrieve an object lock configuration for a bucket**The following `get-object-lock-configuration`example retrieves the object lock configuration for the specified bucket.`aws s3api get-object-lock-configuration \ --bucket``amzn-s3-demo-bucket-with-object-lock`Output: `{ "ObjectLockConfiguration": { "ObjectLockEnabled": "Enabled", "Rule": { "DefaultRetention": { "Mode": "COMPLIANCE", "Days": 50 } } } }`- 
                    For API details, see [GetObjectLockConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object-lock-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-object-retention`.

- **AWS CLI**
- 
            
                    **To retrieve the object retention configuration for an object**The following `get-object-retention`example retrieves the object retention configuration for the specified object.`aws s3api get-object-retention \ --bucket``amzn-s3-demo-bucket-with-object-lock`\ --key`doc1.rtf`Output: `{ "Retention": { "Mode": "GOVERNANCE", "RetainUntilDate": "2025-01-01T00:00:00.000Z" } }`- 
                    For API details, see [GetObjectRetention](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object-retention.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-object-tagging`.

- **AWS CLI**
- 
            
                    **To retrieve the tags attached to an object**The following `get-object-tagging`example retrieves the values for the specified key from the specified object.`aws s3api get-object-tagging \ --bucket``amzn-s3-demo-bucket`\ --key`doc1.rtf`Output: `{ "TagSet": [ { "Value": "confidential", "Key": "designation" } ] }`The following `get-object-tagging`example tries to retrieve the tag sets of the object`doc2.rtf`, which has no tags.`aws s3api get-object-tagging \ --bucket``amzn-s3-demo-bucket`\ --key`doc2.rtf`Output: `{ "TagSet": [] }`The following `get-object-tagging`example retrieves the tag sets of the object`doc3.rtf`, which has multiple tags.`aws s3api get-object-tagging \ --bucket``amzn-s3-demo-bucket`\ --key`doc3.rtf`Output: `{ "TagSet": [ { "Value": "confidential", "Key": "designation" }, { "Value": "finance", "Key": "department" }, { "Value": "payroll", "Key": "team" } ] }`- 
                    For API details, see [GetObjectTagging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object-tagging.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-object-torrent`.

- **AWS CLI**
- 
            
                    The following command creates a torrent for an object in a bucket named `amzn-s3-demo-bucket`:`aws s3api get-object-torrent --bucket``amzn-s3-demo-bucket`--key`large-video-file.mp4``large-video-file.torrent`The torrent file is saved locally in the current folder. Note that the output filename ( `large-video-file.torrent`) is specified without an option name and must be the last argument in the command.- 
                    For API details, see [GetObjectTorrent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object-torrent.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-object`.

- **AWS CLI**
- 
            
                    The following example uses the `get-object`command to download an object from Amazon S3:`aws s3api get-object --bucket``text-content`--key`dir/my_images.tar.bz2``my_images.tar.bz2`Note that the outfile parameter is specified without an option name such as "--outfile". The name of the output file must be the last parameter in the command. The example below demonstrates the use of `--range`to download a specific byte range from an object. Note the byte ranges needs to be prefixed with "bytes=":`aws s3api get-object --bucket``text-content`--key`dir/my_data`--range`bytes=8888-9999``my_data_range`For more information about retrieving objects, see Getting Objects in the *Amazon S3 Developer Guide*.- 
                    For API details, see [GetObject](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-public-access-block`.

- **AWS CLI**
- 
            
                    **To set or modify the block public access configuration for a bucket**The following `get-public-access-block`example displays the block public access configuration for the specified bucket.`aws s3api get-public-access-block \ --bucket``amzn-s3-demo-bucket`Output: `{ "PublicAccessBlockConfiguration": { "IgnorePublicAcls": true, "BlockPublicPolicy": true, "BlockPublicAcls": true, "RestrictPublicBuckets": true } }`- 
                    For API details, see [GetPublicAccessBlock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-public-access-block.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `head-bucket`.

- **AWS CLI**
- 
            
                    The following command verifies access to a bucket named `amzn-s3-demo-bucket`:`aws s3api head-bucket --bucket``amzn-s3-demo-bucket`If the bucket exists and you have access to it, no output is returned. Otherwise, an error message will be shown. For example: `A client error (404) occurred when calling the HeadBucket operation: Not Found`- 
                    For API details, see [HeadBucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/head-bucket.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `head-object`.

- **AWS CLI**
- 
            
                    The following command retrieves metadata for an object in a bucket named `amzn-s3-demo-bucket`:`aws s3api head-object --bucket``amzn-s3-demo-bucket`--key`index.html`Output: `{ "AcceptRanges": "bytes", "ContentType": "text/html", "LastModified": "Thu, 16 Apr 2015 18:19:14 GMT", "ContentLength": 77, "VersionId": "null", "ETag": "\"30a6ec7e1a9ad79c203d05a589c8b400\"", "Metadata": {} }`- 
                    For API details, see [HeadObject](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/head-object.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-bucket-analytics-configurations`.

- **AWS CLI**
- 
            
                    **To retrieve a list of analytics configurations for a bucket**The following `list-bucket-analytics-configurations`retrieves a list of analytics configurations for the specified bucket.`aws s3api list-bucket-analytics-configurations \ --bucket``amzn-s3-demo-bucket`Output: `{ "AnalyticsConfigurationList": [ { "StorageClassAnalysis": {}, "Id": "1" } ], "IsTruncated": false }`- 
                    For API details, see [ListBucketAnalyticsConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-bucket-analytics-configurations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-bucket-intelligent-tiering-configurations`.

- **AWS CLI**
- 
            
                    **To retrieve all S3 Intelligent-Tiering configurations on a bucket**The following `list-bucket-intelligent-tiering-configurations`example retrieves all S3 Intelligent-Tiering configuration on a bucket.`aws s3api list-bucket-intelligent-tiering-configurations \ --bucket``amzn-s3-demo-bucket`Output: `{ "IsTruncated": false, "IntelligentTieringConfigurationList": [ { "Id": "ExampleConfig", "Filter": { "Prefix": "images" }, "Status": "Enabled", "Tierings": [ { "Days": 90, "AccessTier": "ARCHIVE_ACCESS" }, { "Days": 180, "AccessTier": "DEEP_ARCHIVE_ACCESS" } ] }, { "Id": "ExampleConfig2", "Status": "Disabled", "Tierings": [ { "Days": 730, "AccessTier": "ARCHIVE_ACCESS" } ] }, { "Id": "ExampleConfig3", "Filter": { "Tag": { "Key": "documents", "Value": "taxes" } }, "Status": "Enabled", "Tierings": [ { "Days": 90, "AccessTier": "ARCHIVE_ACCESS" }, { "Days": 365, "AccessTier": "DEEP_ARCHIVE_ACCESS" } ] } ] }`For more information, see [Using S3 Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-intelligent-tiering.html)in the*Amazon S3 User Guide*.- 
                    For API details, see [ListBucketIntelligentTieringConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-bucket-intelligent-tiering-configurations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-bucket-inventory-configurations`.

- **AWS CLI**
- 
            
                    **To retrieve a list of inventory configurations for a bucket**The following `list-bucket-inventory-configurations`example lists the inventory configurations for the specified bucket.`aws s3api list-bucket-inventory-configurations \ --bucket``amzn-s3-demo-bucket`Output: `{ "InventoryConfigurationList": [ { "IsEnabled": true, "Destination": { "S3BucketDestination": { "Format": "ORC", "Bucket": "arn:aws:s3:::amzn-s3-demo-bucket", "AccountId": "123456789012" } }, "IncludedObjectVersions": "Current", "Id": "1", "Schedule": { "Frequency": "Weekly" } }, { "IsEnabled": true, "Destination": { "S3BucketDestination": { "Format": "CSV", "Bucket": "arn:aws:s3:::amzn-s3-demo-bucket", "AccountId": "123456789012" } }, "IncludedObjectVersions": "Current", "Id": "2", "Schedule": { "Frequency": "Daily" } } ], "IsTruncated": false }`- 
                    For API details, see [ListBucketInventoryConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-bucket-inventory-configurations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-bucket-metrics-configurations`.

- **AWS CLI**
- 
            
                    **To retrieve a list of metrics configurations for a bucket**The following `list-bucket-metrics-configurations`example retrieves a list of metrics configurations for the specified bucket.`aws s3api list-bucket-metrics-configurations \ --bucket``amzn-s3-demo-bucket`Output: `{ "IsTruncated": false, "MetricsConfigurationList": [ { "Filter": { "Prefix": "logs" }, "Id": "123" }, { "Filter": { "Prefix": "tmp" }, "Id": "234" } ] }`- 
                    For API details, see [ListBucketMetricsConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-bucket-metrics-configurations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-buckets`.

- **AWS CLI**
- 
            
                    The following command uses the `list-buckets`command to display the names of all your Amazon S3 buckets (across all regions):`aws s3api list-buckets --query``"Buckets[].Name"`The query option filters the output of `list-buckets`down to only the bucket names.For more information about buckets, see Working with Amazon S3 Buckets in the *Amazon S3 Developer Guide*.- 
                    For API details, see [ListBuckets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-buckets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-multipart-uploads`.

- **AWS CLI**
- 
            
                    The following command lists all of the active multipart uploads for a bucket named `amzn-s3-demo-bucket`:`aws s3api list-multipart-uploads --bucket``amzn-s3-demo-bucket`Output: `{ "Uploads": [ { "Initiator": { "DisplayName": "username", "ID": "arn:aws:iam::0123456789012:user/username" }, "Initiated": "2015-06-02T18:01:30.000Z", "UploadId": "dfRtDYU0WWCCcH43C3WFbkRONycyCpTJJvxu2i5GYkZljF.Yxwh6XG7WfS2vC4to6HiV6Yjlx.cph0gtNBtJ8P3URCSbB7rjxI5iEwVDmgaXZOGgkk5nVTW16HOQ5l0R", "StorageClass": "STANDARD", "Key": "multipart/01", "Owner": { "DisplayName": "aws-account-name", "ID": "100719349fc3b6dcd7c820a124bf7aecd408092c3d7b51b38494939801fc248b" } } ], "CommonPrefixes": [] }`In progress multipart uploads incur storage costs in Amazon S3. Complete or abort an active multipart upload to remove its parts from your account. - 
                    For API details, see [ListMultipartUploads](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-multipart-uploads.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-object-versions`.

- **AWS CLI**
- 
            
                    The following command retrieves version information for an object in a bucket named `amzn-s3-demo-bucket`:`aws s3api list-object-versions --bucket``amzn-s3-demo-bucket`--prefix`index.html`Output: `{ "DeleteMarkers": [ { "Owner": { "DisplayName": "my-username", "ID": "7009a8971cd660687538875e7c86c5b672fe116bd438f46db45460ddcd036c32" }, "IsLatest": true, "VersionId": "B2VsEK5saUNNHKcOAJj7hIE86RozToyq", "Key": "index.html", "LastModified": "2015-11-10T00:57:03.000Z" }, { "Owner": { "DisplayName": "my-username", "ID": "7009a8971cd660687538875e7c86c5b672fe116bd438f46db45460ddcd036c32" }, "IsLatest": false, "VersionId": ".FLQEZscLIcfxSq.jsFJ.szUkmng2Yw6", "Key": "index.html", "LastModified": "2015-11-09T23:32:20.000Z" } ], "Versions": [ { "LastModified": "2015-11-10T00:20:11.000Z", "VersionId": "Rb_l2T8UHDkFEwCgJjhlgPOZC0qJ.vpD", "ETag": "\"0622528de826c0df5db1258a23b80be5\"", "StorageClass": "STANDARD", "Key": "index.html", "Owner": { "DisplayName": "my-username", "ID": "7009a8971cd660687538875e7c86c5b672fe116bd438f46db45460ddcd036c32" }, "IsLatest": false, "Size": 38 }, { "LastModified": "2015-11-09T23:26:41.000Z", "VersionId": "rasWWGpgk9E4s0LyTJgusGeRQKLVIAFf", "ETag": "\"06225825b8028de826c0df5db1a23be5\"", "StorageClass": "STANDARD", "Key": "index.html", "Owner": { "DisplayName": "my-username", "ID": "7009a8971cd660687538875e7c86c5b672fe116bd438f46db45460ddcd036c32" }, "IsLatest": false, "Size": 38 }, { "LastModified": "2015-11-09T22:50:50.000Z", "VersionId": "null", "ETag": "\"d1f45267a863c8392e07d24dd592f1b9\"", "StorageClass": "STANDARD", "Key": "index.html", "Owner": { "DisplayName": "my-username", "ID": "7009a8971cd660687538875e7c86c5b672fe116bd438f46db45460ddcd036c32" }, "IsLatest": false, "Size": 533823 } ] }`- 
                    For API details, see [ListObjectVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-object-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-objects-v2`.

- **AWS CLI**
- 
            
                    **To get a list of objects in a bucket**The following `list-objects-v2`example lists the objects in the specified bucket.`aws s3api list-objects-v2 \ --bucket``amzn-s3-demo-bucket`Output: `{ "Contents": [ { "LastModified": "2019-11-05T23:11:50.000Z", "ETag": "\"621503c373607d548b37cff8778d992c\"", "StorageClass": "STANDARD", "Key": "doc1.rtf", "Size": 391 }, { "LastModified": "2019-11-05T23:11:50.000Z", "ETag": "\"a2cecc36ab7c7fe3a71a273b9d45b1b5\"", "StorageClass": "STANDARD", "Key": "doc2.rtf", "Size": 373 }, { "LastModified": "2019-11-05T23:11:50.000Z", "ETag": "\"08210852f65a2e9cb999972539a64d68\"", "StorageClass": "STANDARD", "Key": "doc3.rtf", "Size": 399 }, { "LastModified": "2019-11-05T23:11:50.000Z", "ETag": "\"d1852dd683f404306569471af106988e\"", "StorageClass": "STANDARD", "Key": "doc4.rtf", "Size": 6225 } ] }`- 
                    For API details, see [ListObjectsV2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-objects-v2.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-objects`.

- **AWS CLI**
- 
            
                    The following example uses the `list-objects`command to display the names of all the objects in the specified bucket:`aws s3api list-objects --bucket``text-content`--query '`Contents[].{Key: Key, Size: Size}`'The example uses the `--query`argument to filter the output of`list-objects`down to the key value and size for each objectFor more information about objects, see Working with Amazon S3 Objects in the *Amazon S3 Developer Guide*.- 
                    For API details, see [ListObjects](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-objects.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-parts`.

- **AWS CLI**
- 
            
                    The following command lists all of the parts that have been uploaded for a multipart upload with key `multipart/01`in the bucket`amzn-s3-demo-bucket`:`aws s3api list-parts --bucket``amzn-s3-demo-bucket`--key '`multipart/01`' --upload-id`dfRtDYU0WWCCcH43C3WFbkRONycyCpTJJvxu2i5GYkZljF.Yxwh6XG7WfS2vC4to6HiV6Yjlx.cph0gtNBtJ8P3URCSbB7rjxI5iEwVDmgaXZOGgkk5nVTW16HOQ5l0R`Output: `{ "Owner": { "DisplayName": "aws-account-name", "ID": "100719349fc3b6dcd7c820a124bf7aecd408092c3d7b51b38494939801fc248b" }, "Initiator": { "DisplayName": "username", "ID": "arn:aws:iam::0123456789012:user/username" }, "Parts": [ { "LastModified": "2015-06-02T18:07:35.000Z", "PartNumber": 1, "ETag": "\"e868e0f4719e394144ef36531ee6824c\"", "Size": 5242880 }, { "LastModified": "2015-06-02T18:07:42.000Z", "PartNumber": 2, "ETag": "\"6bb2b12753d66fe86da4998aa33fffb0\"", "Size": 5242880 }, { "LastModified": "2015-06-02T18:07:47.000Z", "PartNumber": 3, "ETag": "\"d0a0112e841abec9c9ec83406f0159c8\"", "Size": 5242880 } ], "StorageClass": "STANDARD" }`- 
                    For API details, see [ListParts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-parts.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `ls`.

- **AWS CLI**
- 
            
                    **Example 1: Listing all user owned buckets**The following `ls`command lists all of the bucket owned by the user. In this example, the user owns the buckets`amzn-s3-demo-bucket`and`amzn-s3-demo-bucket2`. The timestamp is the date the bucket was created, shown in your machine's time zone. This date can change when making changes to your bucket, such as editing its bucket policy. Note if`s3://`is used for the path argument`<S3Uri>`, it will list all of the buckets as well.`aws s3 ls`Output: `2013-07-11 17:08:50 amzn-s3-demo-bucket 2013-07-24 14:55:44 amzn-s3-demo-bucket2`**Example 2: Listing all prefixes and objects in a bucket**The following `ls`command lists objects and common prefixes under a specified bucket and prefix. In this example, the user owns the bucket`amzn-s3-demo-bucket`with the objects`test.txt`and`somePrefix/test.txt`. The`LastWriteTime`and`Length`are arbitrary. Note that since the`ls`command has no interaction with the local filesystem, the`s3://`URI scheme is not required to resolve ambiguity and may be omitted.`aws s3 ls``s3://amzn-s3-demo-bucket`Output: `PRE somePrefix/ 2013-07-25 17:06:27 88 test.txt`**Example 3: Listing all prefixes and objects in a specific bucket and prefix**The following `ls`command lists objects and common prefixes under a specified bucket and prefix. However, there are no objects nor common prefixes under the specified bucket and prefix.`aws s3 ls``s3://amzn-s3-demo-bucket/noExistPrefix`Output: `None`**Example 4: Recursively listing all prefixes and objects in a bucket**The following `ls`command will recursively list objects in a bucket. Rather than showing`PRE dirname/`in the output, all the content in a bucket will be listed in order.`aws s3 ls``s3://amzn-s3-demo-bucket`\ --recursiveOutput: `2013-09-02 21:37:53 10 a.txt 2013-09-02 21:37:53 2863288 foo.zip 2013-09-02 21:32:57 23 foo/bar/.baz/a 2013-09-02 21:32:58 41 foo/bar/.baz/b 2013-09-02 21:32:57 281 foo/bar/.baz/c 2013-09-02 21:32:57 73 foo/bar/.baz/d 2013-09-02 21:32:57 452 foo/bar/.baz/e 2013-09-02 21:32:57 896 foo/bar/.baz/hooks/bar 2013-09-02 21:32:57 189 foo/bar/.baz/hooks/foo 2013-09-02 21:32:57 398 z.txt`**Example 5: Summarizing all prefixes and objects in a bucket**The following `ls`command demonstrates the same command using the --human-readable and --summarize options. --human-readable displays file size in Bytes/MiB/KiB/GiB/TiB/PiB/EiB. --summarize displays the total number of objects and total size at the end of the result listing:`aws s3 ls``s3://amzn-s3-demo-bucket`\ --recursive \ --human-readable \ --summarizeOutput: `2013-09-02 21:37:53 10 Bytes a.txt 2013-09-02 21:37:53 2.9 MiB foo.zip 2013-09-02 21:32:57 23 Bytes foo/bar/.baz/a 2013-09-02 21:32:58 41 Bytes foo/bar/.baz/b 2013-09-02 21:32:57 281 Bytes foo/bar/.baz/c 2013-09-02 21:32:57 73 Bytes foo/bar/.baz/d 2013-09-02 21:32:57 452 Bytes foo/bar/.baz/e 2013-09-02 21:32:57 896 Bytes foo/bar/.baz/hooks/bar 2013-09-02 21:32:57 189 Bytes foo/bar/.baz/hooks/foo 2013-09-02 21:32:57 398 Bytes z.txt Total Objects: 10 Total Size: 2.9 MiB`**Example 6: Listing from an S3 access point**The following `ls`command list objects from access point (`myaccesspoint`):`aws s3 ls``s3://arn:aws:s3:us-west-2:123456789012:accesspoint/myaccesspoint/`Output: `PRE somePrefix/ 2013-07-25 17:06:27 88 test.txt`- 
                    For API details, see [Ls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/ls.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `mb`.

- **AWS CLI**
- 
            
                    **Example 1: Create a bucket**The following `mb`command creates a bucket. In this example, the user makes the bucket`amzn-s3-demo-bucket`. The bucket is created in the region specified in the user's configuration file:`aws s3 mb``s3://amzn-s3-demo-bucket`Output: `make_bucket: s3://amzn-s3-demo-bucket`**Example 2: Create a bucket in the specified region**The following `mb`command creates a bucket in a region specified by the`--region`parameter. In this example, the user makes the bucket`amzn-s3-demo-bucket`in the region`us-west-1`:`aws s3 mb``s3://amzn-s3-demo-bucket`\ --region`us-west-1`Output: `make_bucket: s3://amzn-s3-demo-bucket`**Example 3: Create a bucket with specified tags**The following `mb`command creates a bucket with specified tags using the`--tags`parameter. In this example, the user makes the bucket`amzn-s3-demo-bucket`with two tags with keys`Key1`and`Key2`, respectively.`aws s3 mb``s3://amzn-s3-demo-bucket`\ --tags`Key1``Value1`\ --tags`Key2``Value2`Output: `make_bucket: s3://amzn-s3-demo-bucket`- 
                    For API details, see [Mb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/mb.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `mv`.

- **AWS CLI**
- 
            
                    **Example 1: Move a local file to the specified bucket**The following `mv`command moves a single file to a specified bucket and key.`aws s3 mv``test.txt``s3://amzn-s3-demo-bucket/test2.txt`Output: `move: test.txt to s3://amzn-s3-demo-bucket/test2.txt`**Example 2: Move an object to the specified bucket and key**The following `mv`command moves a single s3 object to a specified bucket and key.`aws s3 mv``s3://amzn-s3-demo-bucket/test.txt``s3://amzn-s3-demo-bucket/test2.txt`Output: `move: s3://amzn-s3-demo-bucket/test.txt to s3://amzn-s3-demo-bucket/test2.txt`**Example 3: Move an S3 object to the local directory**The following `mv`command moves a single object to a specified file locally.`aws s3 mv``s3://amzn-s3-demo-bucket/test.txt``test2.txt`Output: `move: s3://amzn-s3-demo-bucket/test.txt to test2.txt`**Example 4: Move an object with it's original name to the specified bucket**The following `mv`command moves a single object to a specified bucket while retaining its original name:`aws s3 mv``s3://amzn-s3-demo-bucket/test.txt``s3://amzn-s3-demo-bucket2/`Output: `move: s3://amzn-s3-demo-bucket/test.txt to s3://amzn-s3-demo-bucket2/test.txt`**Example 5: Move all objects and prefixes in a bucket to the local directory**When passed with the parameter `--recursive`, the following`mv`command recursively moves all objects under a specified prefix and bucket to a specified directory. In this example, the bucket`amzn-s3-demo-bucket`has the objects`test1.txt`and`test2.txt`.`aws s3 mv``s3://amzn-s3-demo-bucket``.`\ --recursiveOutput: `move: s3://amzn-s3-demo-bucket/test1.txt to test1.txt move: s3://amzn-s3-demo-bucket/test2.txt to test2.txt`**Example 6: Move all objects and prefixes in a bucket to the local directory, except ``.jpg`` files**When passed with the parameter `--recursive`, the following`mv`command recursively moves all files under a specified directory to a specified bucket and prefix while excluding some files by using an`--exclude`parameter. In this example, the directory`myDir`has the files`test1.txt`and`test2.jpg`.`aws s3 mv``myDir``s3://amzn-s3-demo-bucket/`\ --recursive \ --exclude`"*.jpg"`Output: `move: myDir/test1.txt to s3://amzn-s3-demo-bucket2/test1.txt`**Example 7: Move all objects and prefixes in a bucket to the local directory, except specified prefix**When passed with the parameter `--recursive`, the following`mv`command recursively moves all objects under a specified bucket to another bucket while excluding some objects by using an`--exclude`parameter. In this example, the bucket`amzn-s3-demo-bucket`has the objects`test1.txt`and`another/test1.txt`.`aws s3 mv``s3://amzn-s3-demo-bucket/``s3://amzn-s3-demo-bucket2/`\ --recursive \ --exclude`"amzn-s3-demo-bucket/another/*"`Output: `move: s3://amzn-s3-demo-bucket/test1.txt to s3://amzn-s3-demo-bucket2/test1.txt`**Example 8: Move an object to the specified bucket and set the ACL**The following `mv`command moves a single object to a specified bucket and key while setting the ACL to`public-read-write`.`aws s3 mv``s3://amzn-s3-demo-bucket/test.txt``s3://amzn-s3-demo-bucket/test2.txt`\ --acl`public-read-write`Output: `move: s3://amzn-s3-demo-bucket/test.txt to s3://amzn-s3-demo-bucket/test2.txt`**Example 9: Move a local file to the specified bucket and grant permissions**The following `mv`command illustrates the use of the`--grants`option to grant read access to all users and full control to a specific user identified by their email address.`aws s3 mv``file.txt``s3://amzn-s3-demo-bucket/`\ --grants`read=uri=http://acs.amazonaws.com/groups/global/AllUsers``full=emailaddress=user@example.com`Output: `move: file.txt to s3://amzn-s3-demo-bucket/file.txt`**Example 10: Move a file to an S3 access point**The following `mv`command moves a single file named`mydoc.txt`to the access point named`myaccesspoint`at the key named`mykey`.`aws s3 mv``mydoc.txt``s3://arn:aws:s3:us-west-2:123456789012:accesspoint/myaccesspoint/mykey`Output: `move: mydoc.txt to s3://arn:aws:s3:us-west-2:123456789012:accesspoint/myaccesspoint/mykey`- 
                    For API details, see [Mv](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/mv.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `presign`.

- **AWS CLI**
- 
            
                    **Example 1: To create a pre-signed URL with the default one hour lifetime that links to an object in an S3 bucket**The following `presign`command generates a pre-signed URL for a specified bucket and key that is valid for one hour.`aws s3 presign``s3://amzn-s3-demo-bucket/test2.txt`Output: `https://amzn-s3-demo-bucket.s3.us-west-2.amazonaws.com/key?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAEXAMPLE123456789%2F20210621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210621T041609Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=EXAMBLE1234494d5fba3fed607f98018e1dfc62e2529ae96d844123456`**Example 2: To create a pre-signed URL with a custom lifetime that links to an object in an S3 bucket**The following `presign`command generates a pre-signed URL for a specified bucket and key that is valid for one week.`aws s3 presign``s3://amzn-s3-demo-bucket/test2.txt`\ --expires-in`604800`Output: `https://amzn-s3-demo-bucket.s3.us-west-2.amazonaws.com/key?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAEXAMPLE123456789%2F20210621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210621T041609Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=EXAMBLE1234494d5fba3fed607f98018e1dfc62e2529ae96d844123456`For more information, see [Share an Object with Others](https://docs.aws.amazon.com/AmazonS3/latest/dev/ShareObjectPreSignedURL.html)in the*S3 Developer Guide*guide.- 
                    For API details, see [Presign](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/presign.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-bucket-accelerate-configuration`.

- **AWS CLI**
- 
            
                    **To set the accelerate configuration of a bucket**The following `put-bucket-accelerate-configuration`example enables the accelerate configuration for the specified bucket.`aws s3api put-bucket-accelerate-configuration \ --bucket``amzn-s3-demo-bucket`\ --accelerate-configuration`Status=Enabled`This command produces no output. - 
                    For API details, see [PutBucketAccelerateConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-accelerate-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-bucket-acl`.

- **AWS CLI**
- 
            
                    This example grants `full control`to two AWS users (*user1@example.com*and*user2@example.com*) and`read`permission to everyone:`aws s3api put-bucket-acl --bucket``amzn-s3-demo-bucket`--grant-full-control`emailaddress=user1@example.com,emailaddress=user2@example.com`--grant-read`uri=http://acs.amazonaws.com/groups/global/AllUsers`See http://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTacl.html for details on custom ACLs (the s3api ACL commands, such as `put-bucket-acl`, use the same shorthand argument notation).- 
                    For API details, see [PutBucketAcl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-acl.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-bucket-analytics-configuration`.

- **AWS CLI**
- 
            
                    **To sets an analytics configuration for the bucket**The following `put-bucket-analytics-configuration`example configures analytics for the specified bucket.`aws s3api put-bucket-analytics-configuration \ --bucket``amzn-s3-demo-bucket`--id`1`\ --analytics-configuration '`{"Id": "1","StorageClassAnalysis": {}}`'This command produces no output. - 
                    For API details, see [PutBucketAnalyticsConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-analytics-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-bucket-cors`.

- **AWS CLI**
- 
            
                    The following example enables `PUT`,`POST`, and`DELETE`requests from*www.example.com*, and enables`GET`requests from any domain:`aws s3api put-bucket-cors --bucket``amzn-s3-demo-bucket`--cors-configuration`file://cors.json``cors.json:``{`"CORSRules":`[``{`"AllowedOrigins": ["http://www.example.com"], "AllowedHeaders": ["*"], "AllowedMethods": ["PUT", "POST", "DELETE"], "MaxAgeSeconds":`3000,`"ExposeHeaders": ["x-amz-server-side-encryption"]`},``{`"AllowedOrigins": ["*"], "AllowedHeaders": ["Authorization"], "AllowedMethods": ["GET"], "MaxAgeSeconds":`3000``}``]``}`- 
                    For API details, see [PutBucketCors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-cors.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-bucket-encryption`.

- **AWS CLI**
- 
            
                    **To configure server-side encryption for a bucket**The following `put-bucket-encryption`example sets AES256 encryption as the default for the specified bucket.`aws s3api put-bucket-encryption \ --bucket``amzn-s3-demo-bucket`\ --server-side-encryption-configuration '`{"Rules": [{"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}]}`'This command produces no output. - 
                    For API details, see [PutBucketEncryption](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-encryption.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-bucket-intelligent-tiering-configuration`.

- **AWS CLI**
- 
            
                    **To update an S3 Intelligent-Tiering configuration on a bucket**The following `put-bucket-intelligent-tiering-configuration`example updates an S3 Intelligent-Tiering configuration, named ExampleConfig, on a bucket. The configuration will transition objects that have not been accessed under the prefix images to Archive Access after 90 days and Deep Archive Access after 180 days.`aws s3api put-bucket-intelligent-tiering-configuration \ --bucket``amzn-s3-demo-bucket`\ --id`"ExampleConfig"`\ --intelligent-tiering-configuration`file://intelligent-tiering-configuration.json`Contents of `intelligent-tiering-configuration.json`:`{ "Id": "ExampleConfig", "Status": "Enabled", "Filter": { "Prefix": "images" }, "Tierings": [ { "Days": 90, "AccessTier": "ARCHIVE_ACCESS" }, { "Days": 180, "AccessTier": "DEEP_ARCHIVE_ACCESS" } ] }`This command produces no output. For more information, see [Setting Object Ownership on an existing bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-ownership-existing-bucket.html)in the*Amazon S3 User Guide*.- 
                    For API details, see [PutBucketIntelligentTieringConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-intelligent-tiering-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-bucket-inventory-configuration`.

- **AWS CLI**
- 
            
                    **Example 1: To set an inventory configuration for a bucket**The following `put-bucket-inventory-configuration`example sets a weekly ORC-formatted inventory report for the bucket`amzn-s3-demo-bucket`.`aws s3api put-bucket-inventory-configuration \ --bucket``amzn-s3-demo-bucket`\ --id`1`\ --inventory-configuration '`{"Destination": { "S3BucketDestination": { "AccountId": "123456789012", "Bucket": "arn:aws:s3:::amzn-s3-demo-bucket", "Format": "ORC" }}, "IsEnabled": true, "Id": "1", "IncludedObjectVersions": "Current", "Schedule": { "Frequency": "Weekly" }}`'This command produces no output. **Example 2: To set an inventory configuration for a bucket**The following `put-bucket-inventory-configuration`example sets a daily CSV-formatted inventory report for the bucket`amzn-s3-demo-bucket`.`aws s3api put-bucket-inventory-configuration \ --bucket``amzn-s3-demo-bucket`\ --id`2`\ --inventory-configuration '`{"Destination": { "S3BucketDestination": { "AccountId": "123456789012", "Bucket": "arn:aws:s3:::amzn-s3-demo-bucket", "Format": "CSV" }}, "IsEnabled": true, "Id": "2", "IncludedObjectVersions": "Current", "Schedule": { "Frequency": "Daily" }}`'This command produces no output. - 
                    For API details, see [PutBucketInventoryConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-inventory-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-bucket-lifecycle-configuration`.

- **AWS CLI**
- 
            
                    The following command applies a lifecycle configuration to a bucket named `amzn-s3-demo-bucket`:`aws s3api put-bucket-lifecycle-configuration --bucket``amzn-s3-demo-bucket`--lifecycle-configuration`file://lifecycle.json`The file `lifecycle.json`is a JSON document in the current folder that specifies two rules:`{ "Rules": [ { "ID": "Move rotated logs to Glacier", "Prefix": "rotated/", "Status": "Enabled", "Transitions": [ { "Date": "2015-11-10T00:00:00.000Z", "StorageClass": "GLACIER" } ] }, { "Status": "Enabled", "Prefix": "", "NoncurrentVersionTransitions": [ { "NoncurrentDays": 2, "StorageClass": "GLACIER" } ], "ID": "Move old versions to Glacier" } ] }`The first rule moves files with the prefix `rotated`to Glacier on the specified date. The second rule moves old object versions to Glacier when they are no longer current. For information on acceptable timestamp formats, see Specifying Parameter Values in the*AWS CLI User Guide*.- 
                    For API details, see [PutBucketLifecycleConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-lifecycle-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-bucket-lifecycle`.

- **AWS CLI**
- 
            
                    The following command applies a lifecycle configuration to the bucket `amzn-s3-demo-bucket`:`aws s3api put-bucket-lifecycle --bucket``amzn-s3-demo-bucket`--lifecycle-configuration`file://lifecycle.json`The file `lifecycle.json`is a JSON document in the current folder that specifies two rules:`{ "Rules": [ { "ID": "Move to Glacier after sixty days (objects in logs/2015/)", "Prefix": "logs/2015/", "Status": "Enabled", "Transition": { "Days": 60, "StorageClass": "GLACIER" } }, { "Expiration": { "Date": "2016-01-01T00:00:00.000Z" }, "ID": "Delete 2014 logs in 2016.", "Prefix": "logs/2014/", "Status": "Enabled" } ] }`The first rule moves files to Amazon Glacier after sixty days. The second rule deletes files from Amazon S3 on the specified date. For information on acceptable timestamp formats, see Specifying Parameter Values in the *AWS CLI User Guide*.Each rule in the above example specifies a policy ( `Transition`or`Expiration`) and file prefix (folder name) to which it applies. You can also create a rule that applies to an entire bucket by specifying a blank prefix:`{ "Rules": [ { "ID": "Move to Glacier after sixty days (all objects in bucket)", "Prefix": "", "Status": "Enabled", "Transition": { "Days": 60, "StorageClass": "GLACIER" } } ] }`- 
                    For API details, see [PutBucketLifecycle](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-lifecycle.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-bucket-logging`.

- **AWS CLI**
- 
            
                    **Example 1: To set bucket policy logging**The following `put-bucket-logging`example sets the logging policy for*amzn-s3-demo-bucket*. First, grant the logging service principal permission in your bucket policy using the`put-bucket-policy`command.`aws s3api put-bucket-policy \ --bucket``amzn-s3-demo-bucket`\ --policy`file://policy.json`Contents of `policy.json`:`{ "Version":"2012-10-17", "Statement": [ { "Sid": "S3ServerAccessLogsPolicy", "Effect": "Allow", "Principal": {"Service": "logging.s3.amazonaws.com"}, "Action": "s3:PutObject", "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/Logs/*", "Condition": { "ArnLike": {"aws:SourceARN": "arn:aws:s3:::SOURCE-BUCKET-NAME"}, "StringEquals": {"aws:SourceAccount": "SOURCE-AWS-ACCOUNT-ID"} } } ] }`To apply the logging policy, use `put-bucket-logging`.`aws s3api put-bucket-logging \ --bucket``amzn-s3-demo-bucket`\ --bucket-logging-status`file://logging.json`Contents of `logging.json`:`{ "LoggingEnabled": { "TargetBucket": "amzn-s3-demo-bucket", "TargetPrefix": "Logs/" } }`The `put-bucket-policy`command is required to grant`s3:PutObject`permissions to the logging service principal.For more information, see [Amazon S3 Server Access Logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html)in the*Amazon S3 User Guide*.**Example 2: To set a bucket policy for logging access to only a single user**The following `put-bucket-logging`example sets the logging policy for*amzn-s3-demo-bucket*. The AWS user*bob@example.com*will have full control over the log files, and no one else has any access. First, grant S3 permission with`put-bucket-acl`.`aws s3api put-bucket-acl \ --bucket``amzn-s3-demo-bucket`\ --grant-write`URI=http://acs.amazonaws.com/groups/s3/LogDelivery`\ --grant-read-acp`URI=http://acs.amazonaws.com/groups/s3/LogDelivery`Then apply the logging policy using `put-bucket-logging`.`aws s3api put-bucket-logging \ --bucket``amzn-s3-demo-bucket`\ --bucket-logging-status`file://logging.json`Contents of `logging.json`:`{ "LoggingEnabled": { "TargetBucket": "amzn-s3-demo-bucket", "TargetPrefix": "amzn-s3-demo-bucket-logs/", "TargetGrants": [ { "Grantee": { "Type": "AmazonCustomerByEmail", "EmailAddress": "bob@example.com" }, "Permission": "FULL_CONTROL" } ] } }`the `put-bucket-acl`command is required to grant S3's log delivery system the necessary permissions (write and read-acp permissions).For more information, see [Amazon S3 Server Access Logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html)in the*Amazon S3 Developer Guide*.- 
                    For API details, see [PutBucketLogging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-logging.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-bucket-metrics-configuration`.

- **AWS CLI**
- 
            
                    **To set a metrics configuration for a bucket**The following `put-bucket-metrics-configuration`example sets a metric configuration with ID 123 for the specified bucket.`aws s3api put-bucket-metrics-configuration \ --bucket``amzn-s3-demo-bucket`\ --id`123`\ --metrics-configuration '`{"Id": "123", "Filter": {"Prefix": "logs"}}`'This command produces no output. - 
                    For API details, see [PutBucketMetricsConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-metrics-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-bucket-notification-configuration`.

- **AWS CLI**
- 
            
                    **To enable the specified notifications to a bucket**The following `put-bucket-notification-configuration`example applies a notification configuration to a bucket named`amzn-s3-demo-bucket`. The file`notification.json`is a JSON document in the current folder that specifies an SNS topic and an event type to monitor.`aws s3api put-bucket-notification-configuration \ --bucket``amzn-s3-demo-bucket`\ --notification-configuration`file://notification.json`Contents of `notification.json`:`{ "TopicConfigurations": [ { "TopicArn": "arn:aws:sns:us-west-2:123456789012:s3-notification-topic", "Events": [ "s3:ObjectCreated:*" ] } ] }`The SNS topic must have an IAM policy attached to it that allows Amazon S3 to publish to it. `{ "Version":"2012-10-17", "Id": "example-ID", "Statement": [ { "Sid": "example-statement-ID", "Effect": "Allow", "Principal": { "Service": "s3.amazonaws.com" }, "Action": [ "SNS:Publish" ], "Resource": "arn:aws:sns:us-west-2:123456789012::s3-notification-topic", "Condition": { "ArnLike": { "aws:SourceArn": "arn:aws:s3:*:*:amzn-s3-demo-bucket" } } } ] }`- 
                    For API details, see [PutBucketNotificationConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-notification-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-bucket-notification`.

- **AWS CLI**
- 
            
                    The applies a notification configuration to a bucket named `amzn-s3-demo-bucket`:`aws s3api put-bucket-notification --bucket``amzn-s3-demo-bucket`--notification-configuration`file://notification.json`The file `notification.json`is a JSON document in the current folder that specifies an SNS topic and an event type to monitor:`{ "TopicConfiguration": { "Event": "s3:ObjectCreated:*", "Topic": "arn:aws:sns:us-west-2:123456789012:s3-notification-topic" } }`The SNS topic must have an IAM policy attached to it that allows Amazon S3 to publish to it: `{ "Version":"2012-10-17", "Id": "example-ID", "Statement": [ { "Sid": "example-statement-ID", "Effect": "Allow", "Principal": { "Service": "s3.amazonaws.com" }, "Action": [ "SNS:Publish" ], "Resource": "arn:aws:sns:us-west-2:123456789012:amzn-s3-demo-bucket", "Condition": { "ArnLike": { "aws:SourceArn": "arn:aws:s3:*:*:amzn-s3-demo-bucket" } } } ] }`- 
                    For API details, see [PutBucketNotification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-notification.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-bucket-ownership-controls`.

- **AWS CLI**
- 
            
                    **To update the bucket ownership settings of a bucket**The following `put-bucket-ownership-controls`example updates the bucket ownership settings of a bucket.`aws s3api put-bucket-ownership-controls \ --bucket``amzn-s3-demo-bucket`\ --ownership-controls="Rules=[{ObjectOwnership=BucketOwnerEnforced}]"This command produces no output. For more information, see [Setting Object Ownership on an existing bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-ownership-existing-bucket.html)in the*Amazon S3 User Guide*.- 
                    For API details, see [PutBucketOwnershipControls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-ownership-controls.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-bucket-policy`.

- **AWS CLI**
- 
            
                    This example allows all users to retrieve any object in *amzn-s3-demo-bucket*except those in the*MySecretFolder*. It also grants`put`and`delete`permission to the root user of the AWS account`1234-5678-9012`:`aws s3api put-bucket-policy --bucket``amzn-s3-demo-bucket`--policy`file://policy.json``policy.json:``{`"Statement":`[``{`"Effect": "Allow", "Principal": "*", "Action": "s3:GetObject", "Resource":`"arn:aws:s3:::amzn-s3-demo-bucket/*"``},``{`"Effect": "Deny", "Principal": "*", "Action": "s3:GetObject", "Resource":`"arn:aws:s3:::amzn-s3-demo-bucket/MySecretFolder/*"``},``{`"Effect": "Allow", "Principal":`{`"AWS":`"arn:aws:iam::123456789012:root"``},`"Action":`[`"s3:DeleteObject",`"s3:PutObject"``],`"Resource":`"arn:aws:s3:::amzn-s3-demo-bucket/*"``}``]``}`- 
                    For API details, see [PutBucketPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-bucket-replication`.

- **AWS CLI**
- 
            
                    **To configure replication for an S3 bucket**The following `put-bucket-replication`example applies a replication configuration to the specified S3 bucket.`aws s3api put-bucket-replication \ --bucket``amzn-s3-demo-bucket1`\ --replication-configuration`file://replication.json`Contents of `replication.json`:`{ "Role": "arn:aws:iam::123456789012:role/s3-replication-role", "Rules": [ { "Status": "Enabled", "Priority": 1, "DeleteMarkerReplication": { "Status": "Disabled" }, "Filter" : { "Prefix": ""}, "Destination": { "Bucket": "arn:aws:s3:::amzn-s3-demo-bucket2" } } ] }`The destination bucket must have versioning enabled. The specified role must have permission to write to the destination bucket and have a trust relationship that allows Amazon S3 to assume the role. Example role permission policy: `{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "s3:GetReplicationConfiguration", "s3:ListBucket" ], "Resource": [ "arn:aws:s3:::amzn-s3-demo-bucket1" ] }, { "Effect": "Allow", "Action": [ "s3:GetObjectVersion", "s3:GetObjectVersionAcl", "s3:GetObjectVersionTagging" ], "Resource": [ "arn:aws:s3:::amzn-s3-demo-bucket1/*" ] }, { "Effect": "Allow", "Action": [ "s3:ReplicateObject", "s3:ReplicateDelete", "s3:ReplicateTags" ], "Resource": "arn:aws:s3:::amzn-s3-demo-bucket2/*" } ] }`Example trust relationship policy: `{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "Service": "s3.amazonaws.com" }, "Action": "sts:AssumeRole" } ] }`This command produces no output. For more information, see [This is the topic title](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/enable-replication.html)in the*Amazon Simple Storage Service Console User Guide*.- 
                    For API details, see [PutBucketReplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-replication.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-bucket-request-payment`.

- **AWS CLI**
- 
            
                    **Example 1: To enable ``requester pays`` configuration for a bucket**The following `put-bucket-request-payment`example enables`requester pays`for the specified bucket.`aws s3api put-bucket-request-payment \ --bucket``amzn-s3-demo-bucket`\ --request-payment-configuration '`{"Payer":"Requester"}`'This command produces no output. **Example 2: To disable ``requester pays`` configuration for a bucket**The following `put-bucket-request-payment`example disables`requester pays`for the specified bucket.`aws s3api put-bucket-request-payment \ --bucket``amzn-s3-demo-bucket`\ --request-payment-configuration '`{"Payer":"BucketOwner"}`'This command produces no output. - 
                    For API details, see [PutBucketRequestPayment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-request-payment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-bucket-tagging`.

- **AWS CLI**
- 
            
                    The following command applies a tagging configuration to a bucket named `amzn-s3-demo-bucket`:`aws s3api put-bucket-tagging --bucket``amzn-s3-demo-bucket`--tagging`file://tagging.json`The file `tagging.json`is a JSON document in the current folder that specifies tags:`{ "TagSet": [ { "Key": "organization", "Value": "marketing" } ] }`Or apply a tagging configuration to `amzn-s3-demo-bucket`directly from the command line:`aws s3api put-bucket-tagging --bucket``amzn-s3-demo-bucket`--tagging '`TagSet=[{Key=organization,Value=marketing}]`'- 
                    For API details, see [PutBucketTagging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-tagging.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-bucket-versioning`.

- **AWS CLI**
- 
            
                    The following command enables versioning on a bucket named `amzn-s3-demo-bucket`:`aws s3api put-bucket-versioning --bucket``amzn-s3-demo-bucket`--versioning-configuration`Status=Enabled`The following command enables versioning, and uses an mfa code `aws s3api put-bucket-versioning --bucket``amzn-s3-demo-bucket`--versioning-configuration`Status=Enabled`--mfa`"SERIAL 123456"`- 
                    For API details, see [PutBucketVersioning](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-versioning.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-bucket-website`.

- **AWS CLI**
- 
            
                    The applies a static website configuration to a bucket named `amzn-s3-demo-bucket`:`aws s3api put-bucket-website --bucket``amzn-s3-demo-bucket`--website-configuration`file://website.json`The file `website.json`is a JSON document in the current folder that specifies index and error pages for the website:`{ "IndexDocument": { "Suffix": "index.html" }, "ErrorDocument": { "Key": "error.html" } }`- 
                    For API details, see [PutBucketWebsite](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-website.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-object-acl`.

- **AWS CLI**
- 
            
                    The following command grants `full control`to two AWS users (*user1@example.com*and*user2@example.com*) and`read`permission to everyone:`aws s3api put-object-acl --bucket``amzn-s3-demo-bucket`--key`file.txt`--grant-full-control`emailaddress=user1@example.com,emailaddress=user2@example.com`--grant-read`uri=http://acs.amazonaws.com/groups/global/AllUsers`See http://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTacl.html for details on custom ACLs (the s3api ACL commands, such as `put-object-acl`, use the same shorthand argument notation).- 
                    For API details, see [PutObjectAcl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object-acl.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-object-legal-hold`.

- **AWS CLI**
- 
            
                    **To apply a Legal Hold to an object**The following `put-object-legal-hold`example sets a Legal Hold on the object`doc1.rtf`.`aws s3api put-object-legal-hold \ --bucket``amzn-s3-demo-bucket-with-object-lock`\ --key`doc1.rtf`\ --legal-hold`Status=ON`This command produces no output. - 
                    For API details, see [PutObjectLegalHold](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object-legal-hold.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-object-lock-configuration`.

- **AWS CLI**
- 
            
                    **To set an object lock configuration on a bucket**The following `put-object-lock-configuration`example sets a 50-day object lock on the specified bucket.`aws s3api put-object-lock-configuration \ --bucket``amzn-s3-demo-bucket-with-object-lock`\ --object-lock-configuration '`{ "ObjectLockEnabled": "Enabled", "Rule": { "DefaultRetention": { "Mode": "COMPLIANCE", "Days": 50 }}}`'This command produces no output. - 
                    For API details, see [PutObjectLockConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object-lock-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-object-retention`.

- **AWS CLI**
- 
            
                    **To set an object retention configuration for an object**The following `put-object-retention`example sets an object retention configuration for the specified object until 2025-01-01.`aws s3api put-object-retention \ --bucket``amzn-s3-demo-bucket-with-object-lock`\ --key`doc1.rtf`\ --retention '`{ "Mode": "GOVERNANCE", "RetainUntilDate": "2025-01-01T00:00:00" }`'This command produces no output. - 
                    For API details, see [PutObjectRetention](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object-retention.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-object-tagging`.

- **AWS CLI**
- 
            
                    **To set a tag on an object**The following `put-object-tagging`example sets a tag with the key`designation`and the value`confidential`on the specified object.`aws s3api put-object-tagging \ --bucket``amzn-s3-demo-bucket`\ --key`doc1.rtf`\ --tagging '`{"TagSet": [{ "Key": "designation", "Value": "confidential" }]}`'This command produces no output. The following `put-object-tagging`example sets multiple tags sets on the specified object.`aws s3api put-object-tagging \ --bucket``amzn-s3-demo-bucket-example`\ --key`doc3.rtf`\ --tagging '`{"TagSet": [{ "Key": "designation", "Value": "confidential" }, { "Key": "department", "Value": "finance" }, { "Key": "team", "Value": "payroll" } ]}`'This command produces no output. - 
                    For API details, see [PutObjectTagging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object-tagging.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-object`.

- **AWS CLI**
- 
            
                    **Example 1: Upload an object to Amazon S3**The following `put-object`command example uploads an object to Amazon S3.`aws s3api put-object \ --bucket``amzn-s3-demo-bucket`\ --key`my-dir/MySampleImage.png`\ --body`MySampleImage.png`For more information about uploading objects, see Uploading Objects < http://docs.aws.amazon.com/AmazonS3/latest/dev/UploadingObjects.html> in the *Amazon S3 Developer Guide*.**Example 2: Upload a video file to Amazon S3**The following `put-object`command example uploads a video file.`aws s3api put-object \ --bucket``amzn-s3-demo-bucket`\ --key`my-dir/big-video-file.mp4`\ --body`/media/videos/f-sharp-3-data-services.mp4`For more information about uploading objects, see Uploading Objects < http://docs.aws.amazon.com/AmazonS3/latest/dev/UploadingObjects.html> in the *Amazon S3 Developer Guide*.- 
                    For API details, see [PutObject](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-object.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-public-access-block`.

- **AWS CLI**
- 
            
                    **To set the block public access configuration for a bucket**The following `put-public-access-block`example sets a restrictive block public access configuration for the specified bucket.`aws s3api put-public-access-block \ --bucket``amzn-s3-demo-bucket`\ --public-access-block-configuration`"BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"`This command produces no output. - 
                    For API details, see [PutPublicAccessBlock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-public-access-block.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `rb`.

- **AWS CLI**
- 
            
                    **Example 1: Delete a bucket**The following `rb`command removes a bucket. In this example, the user's bucket is`amzn-s3-demo-bucket`. Note that the bucket must be empty in order to remove:`aws s3 rb``s3://amzn-s3-demo-bucket`Output: `remove_bucket: amzn-s3-demo-bucket`**Example 2: Force delete a bucket**The following `rb`command uses the`--force`parameter to first remove all of the objects in the bucket and then remove the bucket itself. In this example, the user's bucket is`amzn-s3-demo-bucket`and the objects in`amzn-s3-demo-bucket`are`test1.txt`and`test2.txt`:`aws s3 rb``s3://amzn-s3-demo-bucket`\ --forceOutput: `delete: s3://amzn-s3-demo-bucket/test1.txt delete: s3://amzn-s3-demo-bucket/test2.txt remove_bucket: amzn-s3-demo-bucket`- 
                    For API details, see [Rb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/rb.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `restore-object`.

- **AWS CLI**
- 
            
                    **To create a restore request for an object**The following `restore-object`example restores the specified Amazon S3 Glacier object for the bucket`my-glacier-bucket`for 10 days.`aws s3api restore-object \ --bucket``my-glacier-bucket`\ --key`doc1.rtf`\ --restore-request`Days=10`This command produces no output. - 
                    For API details, see [RestoreObject](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/restore-object.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `rm`.

- **AWS CLI**
- 
            
                    **Example 1: Delete an S3 object**The following `rm`command deletes a single s3 object:`aws s3 rm``s3://amzn-s3-demo-bucket/test2.txt`Output: `delete: s3://amzn-s3-demo-bucket/test2.txt`**Example 2: Delete all contents in a bucket**The following `rm`command recursively deletes all objects under a specified bucket and prefix when passed with the parameter`--recursive`. In this example, the bucket`amzn-s3-demo-bucket`contains the objects`test1.txt`and`test2.txt`:`aws s3 rm``s3://amzn-s3-demo-bucket`\ --recursiveOutput: `delete: s3://amzn-s3-demo-bucket/test1.txt delete: s3://amzn-s3-demo-bucket/test2.txt`**Example 3: Delete all contents in a bucket, except ``.jpg`` files**The following `rm`command recursively deletes all objects under a specified bucket and prefix when passed with the parameter`--recursive`while excluding some objects by using an`--exclude`parameter. In this example, the bucket`amzn-s3-demo-bucket`has the objects`test1.txt`and`test2.jpg`:`aws s3 rm``s3://amzn-s3-demo-bucket/`\ --recursive \ --exclude`"*.jpg"`Output: `delete: s3://amzn-s3-demo-bucket/test1.txt`**Example 4: Delete all contents in a bucket, except objects under the specified prefix**The following `rm`command recursively deletes all objects under a specified bucket and prefix when passed with the parameter`--recursive`while excluding all objects under a particular prefix by using an`--exclude`parameter. In this example, the bucket`amzn-s3-demo-bucket`has the objects`test1.txt`and`another/test.txt`:`aws s3 rm``s3://amzn-s3-demo-bucket/`\ --recursive \ --exclude`"another/*"`Output: `delete: s3://amzn-s3-demo-bucket/test1.txt`**Example 5: Delete an object from an S3 access point**The following `rm`command deletes a single object (`mykey`) from the access point (`myaccesspoint`).`aws s3 rm``s3://arn:aws:s3:us-west-2:123456789012:accesspoint/myaccesspoint/mykey`Output: `delete: s3://arn:aws:s3:us-west-2:123456789012:accesspoint/myaccesspoint/mykey`- 
                    For API details, see [Rm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/rm.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `select-object-content`.

- **AWS CLI**
- 
            
                    **To filter the contents of an Amazon S3 object based on an SQL statement**The following `select-object-content`example filters the object`my-data-file.csv`with the specified SQL statement and sends output to a file.`aws s3api select-object-content \ --bucket``amzn-s3-demo-bucket`\ --key`my-data-file.csv`\ --expression`"select * from s3object limit 100"`\ --expression-type '`SQL`' \ --input-serialization '`{"CSV": {}, "CompressionType": "NONE"}`' \ --output-serialization '`{"CSV": {}}`'`"output.csv"`This command produces no output. - 
                    For API details, see [SelectObjectContent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/select-object-content.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `sync`.

- **AWS CLI**
- 
            
                    **Example 1: Sync all local objects to the specified bucket**The following `sync`command syncs objects from a local directory to the specified prefix and bucket by uploading the local files to S3. A local file will require uploading if the size of the local file is different than the size of the S3 object, the last modified time of the local file is newer than the last modified time of the S3 object, or the local file does not exist under the specified bucket and prefix. In this example, the user syncs the bucket`amzn-s3-demo-bucket`to the local current directory. The local current directory contains the files`test.txt`and`test2.txt`. The bucket`amzn-s3-demo-bucket`contains no objects.`aws s3 sync``.``s3://amzn-s3-demo-bucket`Output: `upload: test.txt to s3://amzn-s3-demo-bucket/test.txt upload: test2.txt to s3://amzn-s3-demo-bucket/test2.txt`**Example 2: Sync all S3 objects from the specified S3 bucket to another bucket**The following `sync`command syncs objects under a specified prefix and bucket to objects under another specified prefix and bucket by copying S3 objects. An S3 object will require copying if the sizes of the two S3 objects differ, the last modified time of the source is newer than the last modified time of the destination, or the S3 object does not exist under the specified bucket and prefix destination.In this example, the user syncs the bucket `amzn-s3-demo-bucket`to the bucket`amzn-s3-demo-bucket2`. The bucket`amzn-s3-demo-bucket`contains the objects`test.txt`and`test2.txt`. The bucket`amzn-s3-demo-bucket2`contains no objects:`aws s3 sync``s3://amzn-s3-demo-bucket``s3://amzn-s3-demo-bucket2`Output: `copy: s3://amzn-s3-demo-bucket/test.txt to s3://amzn-s3-demo-bucket2/test.txt copy: s3://amzn-s3-demo-bucket/test2.txt to s3://amzn-s3-demo-bucket2/test2.txt`**Example 3: Sync all S3 objects from the specified S3 bucket to the local directory**The following `sync`command syncs files from the specified S3 bucket to the local directory by downloading S3 objects. An S3 object will require downloading if the size of the S3 object differs from the size of the local file, the last modified time of the S3 object is newer than the last modified time of the local file, or the S3 object does not exist in the local directory. Take note that when objects are downloaded from S3, the last modified time of the local file is changed to the last modified time of the S3 object. In this example, the user syncs the bucket`amzn-s3-demo-bucket`to the current local directory. The bucket`amzn-s3-demo-bucket`contains the objects`test.txt`and`test2.txt`. The current local directory has no files:`aws s3 sync``s3://amzn-s3-demo-bucket``.`Output: `download: s3://amzn-s3-demo-bucket/test.txt to test.txt download: s3://amzn-s3-demo-bucket/test2.txt to test2.txt`**Example 4: Sync all local objects to the specified bucket and delete all files that do not match**The following `sync`command syncs objects under a specified prefix and bucket to files in a local directory by uploading the local files to S3. Because of the`--delete`parameter, any files existing under the specified prefix and bucket but not existing in the local directory will be deleted. In this example, the user syncs the bucket`amzn-s3-demo-bucket`to the local current directory. The local current directory contains the files`test.txt`and`test2.txt`. The bucket`amzn-s3-demo-bucket`contains the object`test3.txt`:`aws s3 sync``.``s3://amzn-s3-demo-bucket`\ --deleteOutput: `upload: test.txt to s3://amzn-s3-demo-bucket/test.txt upload: test2.txt to s3://amzn-s3-demo-bucket/test2.txt delete: s3://amzn-s3-demo-bucket/test3.txt`**Example 5: Sync all local objects to the specified bucket except ``.jpg`` files**The following `sync`command syncs objects under a specified prefix and bucket to files in a local directory by uploading the local files to S3. Because of the`--exclude`parameter, all files matching the pattern existing both in S3 and locally will be excluded from the sync. In this example, the user syncs the bucket`amzn-s3-demo-bucket`to the local current directory. The local current directory contains the files`test.jpg`and`test2.txt`. The bucket`amzn-s3-demo-bucket`contains the object`test.jpg`of a different size than the local`test.jpg`:`aws s3 sync``.``s3://amzn-s3-demo-bucket`\ --exclude`"*.jpg"`Output: `upload: test2.txt to s3://amzn-s3-demo-bucket/test2.txt`**Example 6: Sync all local objects to the specified bucket except specified directory files**The following `sync`command syncs files under a local directory to objects under a specified prefix and bucket by downloading S3 objects. This example uses the`--exclude`parameter flag to exclude a specified directory and S3 prefix from the`sync`command. In this example, the user syncs the local current directory to the bucket`amzn-s3-demo-bucket`. The local current directory contains the files`test.txt`and`another/test2.txt`. The bucket`amzn-s3-demo-bucket`contains the objects`another/test5.txt`and`test1.txt`:`aws s3 sync``s3://amzn-s3-demo-bucket/``.`\ --exclude`"*another/*"`Output: `download: s3://amzn-s3-demo-bucket/test1.txt to test1.txt`**Example 7: Sync all objects between buckets in different regions**The following `sync`command syncs files between two buckets in different regions:`aws s3 sync``s3://my-us-west-2-bucket``s3://my-us-east-1-bucket`\ --source-region`us-west-2`\ --region`us-east-1`Output: `download: s3://my-us-west-2-bucket/test1.txt to s3://my-us-east-1-bucket/test1.txt`**Example 8: Sync to an S3 access point**The following `sync`command syncs the current directory to the access point (`myaccesspoint`):`aws s3 sync``.``s3://arn:aws:s3:us-west-2:123456789012:accesspoint/myaccesspoint/`Output: `upload: test.txt to s3://arn:aws:s3:us-west-2:123456789012:accesspoint/myaccesspoint/test.txt upload: test2.txt to s3://arn:aws:s3:us-west-2:123456789012:accesspoint/myaccesspoint/test2.txt`- 
                    For API details, see [Sync](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/sync.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `upload-part-copy`.

- **AWS CLI**
- 
            
                    **To upload part of an object by copying data from an existing object as the data source**The following `upload-part-copy`example uploads a part by copying data from an existing object as a data source.`aws s3api upload-part-copy \ --bucket``amzn-s3-demo-bucket`\ --key`"Map_Data_June.mp4"`\ --copy-source`"amzn-s3-demo-bucket/copy_of_Map_Data_June.mp4"`\ --part-number`1`\ --upload-id`"bq0tdE1CDpWQYRPLHuNG50xAT6pA5D.m_RiBy0ggOH6b13pVRY7QjvLlf75iFdJqp_2wztk5hvpUM2SesXgrzbehG5hViyktrfANpAD0NO.Nk3XREBqvGeZF6U3ipiSm"`Output: `{ "CopyPartResult": { "LastModified": "2019-12-13T23:16:03.000Z", "ETag": "\"711470fc377698c393d94aed6305e245\"" } }`- 
                    For API details, see [UploadPartCopy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/upload-part-copy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `upload-part`.

- **AWS CLI**
- 
            
                    The following command uploads the first part in a multipart upload initiated with the `create-multipart-upload`command:`aws s3api upload-part --bucket``amzn-s3-demo-bucket`--key '`multipart/01`' --part-number`1`--body`part01`--upload-id`"dfRtDYU0WWCCcH43C3WFbkRONycyCpTJJvxu2i5GYkZljF.Yxwh6XG7WfS2vC4to6HiV6Yjlx.cph0gtNBtJ8P3URCSbB7rjxI5iEwVDmgaXZOGgkk5nVTW16HOQ5l0R"`The `body`option takes the name or path of a local file for upload (do not use the file:// prefix). The minimum part size is 5 MB. Upload ID is returned by`create-multipart-upload`and can also be retrieved with`list-multipart-uploads`. Bucket and key are specified when you create the multipart upload.Output: `{ "ETag": "\"e868e0f4719e394144ef36531ee6824c\"" }`Save the ETag value of each part for later. They are required to complete the multipart upload. - 
                    For API details, see [UploadPart](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/upload-part.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `website`.

- **AWS CLI**
- 
            
                    **Configure an S3 bucket as a static website**The following command configures a bucket named `amzn-s3-demo-bucket`as a static website. The index document option specifies the file in`amzn-s3-demo-bucket`that visitors will be directed to when they navigate to the website URL. In this case, the bucket is in the us-west-2 region, so the site would appear at`http://amzn-s3-demo-bucket.s3-website-us-west-2.amazonaws.com`.All files in the bucket that appear on the static site must be configured to allow visitors to open them. File permissions are configured separately from the bucket website configuration. `aws s3 website``s3://amzn-s3-demo-bucket/`\ --index-document`index.html`\ --error-document`error.html`For information on hosting a static website in Amazon S3, see [Hosting a Static Website](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html)in the*Amazon Simple Storage Service Developer Guide*.- 
                    For API details, see [Website](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/website.html)in*AWS CLI Command Reference*.
 
-