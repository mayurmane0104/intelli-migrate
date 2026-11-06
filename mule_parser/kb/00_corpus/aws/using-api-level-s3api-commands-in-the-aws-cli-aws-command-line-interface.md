# Using API-Level (s3api) commands in the AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-apicommands.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-apicommands.html)

---

The API-level commands (contained in the `s3api` command set) provide direct
    access to the Amazon Simple Storage Service (Amazon S3) APIs, and enable some operations that are not exposed in the
    high-level `s3` commands. These commands are the equivalent of the other AWS
    services that provide API-level access to the services' functionality. For more information on
    the `s3` commands, see [Using high-level (s3) commands in the AWS CLI](./cli-services-s3-commands.html)

This topic provides examples that demonstrate how to use the lower-level commands that map
    to the Amazon S3 APIs. In addition, you can find examples for each S3 API command in the
      `s3api` section of the
      [AWS CLI version 2 reference
    guide](https://docs.aws.amazon.com/cli/latest/reference/s3api/index.html).

## Prerequisites

    To run the `s3api` commands, you need to:

- Install and configure the AWS CLI. For more information, see - [Installing or updating to the latest version of the AWS CLI](./getting-started-install.html)and- [Authentication and access credentials for the AWS CLI](./cli-chap-authentication.html).
- 
        The profile that you use must have permissions that allow the AWS operations performed by the examples. 
- 
        Understand these Amazon S3 terms: - 
            Bucket – A top-level Amazon S3 folder. 
- 
            Prefix – An Amazon S3 folder in a bucket. 
- 
            Object – Any item that's hosted in an Amazon S3 bucket. 
 
- 
            

## Apply a custom ACL

    With high-level commands, you can use the `--acl` option to apply predefined
      access control lists (ACLs) to Amazon S3 objects. But you can't use that command to set bucket-wide
      ACLs. However, you can do this by using the
          [put-bucket-acl](https://docs.aws.amazon.com/cli/latest/reference/s3api/put-bucket-acl.html)

The following example shows how to grant full control to two AWS users
        (*user1@example.com* and *user2@example.com*) and read
      permission to everyone. The identifier for "everyone" comes from a special URI that you pass
      as a parameter.

`$``aws s3api put-bucket-acl --bucket``amzn-s3-demo-bucket`--grant-full-control 'emailaddress="`user1@example.com`",emailaddress="`user2@example.com`"' --grant-read 'uri="http://acs.amazonaws.com/groups/global/AllUsers"'

For details about how to construct the ACLs, see [PUT Bucket acl](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTacl.html) in the *Amazon Simple Storage Service API Reference*. The `s3api` ACL commands in the CLI,
      such as `put-bucket-acl`, use the same [shorthand argument notation](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-shorthand.html).

## Configure a logging policy

    The API command `put-bucket-logging` configures a bucket logging policy. 

In the following example, the AWS user *user@example.com* is granted
      full control over the log files, and all users have read access to them. Notice that the
        `put-bucket-acl` command is also required to grant the Amazon S3 log delivery system
      (specified by a URI) the permissions needed to read and write the logs to the bucket.

`$``aws s3api put-bucket-acl --bucket``amzn-s3-demo-bucket`--grant-read-acp 'URI="http://acs.amazonaws.com/groups/s3/LogDelivery"' --grant-write 'URI="http://acs.amazonaws.com/groups/s3/LogDelivery"'`$``aws s3api put-bucket-logging --bucket``amzn-s3-demo-bucket`--bucket-logging-status file://logging.json

The `logging.json` file in the previous command has the following
      content.

`{ "LoggingEnabled": { "TargetBucket": "amzn-s3-demo-bucket", "TargetPrefix": "amzn-s3-demo-bucketLogs/", "TargetGrants": [ { "Grantee": { "Type": "AmazonCustomerByEmail", "EmailAddress": "``user@example.com`" }, "Permission": "FULL_CONTROL" }, { "Grantee": { "Type": "Group", "URI": "http://acs.amazonaws.com/groups/global/AllUsers" }, "Permission": "READ" } ] } }

## Resources

    **AWS CLI reference:**

**Service reference:**

- 
        [Working with Amazon S3 buckets](https://docs.aws.amazon.com//AmazonS3/latest/userguide/UsingBucket.html)in the*Amazon S3 User Guide*
- 
        [Working with Amazon S3 objects](https://docs.aws.amazon.com//AmazonS3/latest/userguide/UsingObjects.html)in the*Amazon S3 User Guide*
- 
        [Listing keys hierarchically using a prefix and delimiter](https://docs.aws.amazon.com//AmazonS3/latest/userguide/ListingKeysHierarchy.html)in the*Amazon S3 User Guide*
- 
        [Abort multipart uploads to an S3 bucket using the AWS SDK for .NET (low-level)](https://docs.aws.amazon.com//AmazonS3/latest/userguide/LLAbortMPUnet.html)in the*Amazon S3 User Guide*