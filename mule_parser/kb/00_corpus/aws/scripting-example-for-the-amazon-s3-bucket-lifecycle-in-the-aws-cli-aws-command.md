# Scripting example for the Amazon S3 bucket lifecycle in the AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-lifecycle-example.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-lifecycle-example.html)

---

This topic uses a bash scripting example for Amazon S3 bucket lifecycle operations using the
    AWS Command Line Interface (AWS CLI). This scripting example uses the
      [ aws s3api](https://docs.aws.amazon.com/cli/latest/reference/s3api/index.html)
    set of commands. Shell scripts are programs designed to run in a command line interface.

## Before you start

    Before you can run any of the below examples, the following things need to be completed.

- Install and configure the AWS CLI. For more information, see - [Installing or updating to the latest version of the AWS CLI](./getting-started-install.html)and- [Authentication and access credentials for the AWS CLI](./cli-chap-authentication.html).
- 
        The profile that you use must have permissions that allow the AWS operations performed by the examples. 

- 
        As an AWS best practice, grant this code least privilege, or only the permissions required to perform a task. For more information, see [Grant Least Privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege)in the*IAM User Guide*.
- 
        This code has not been tested in all AWS Regions. Some AWS services are available only in specific Regions. For more information, see [Service Endpoints and Quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html)in the*AWS General Reference Guide*.
- 
        Running this code can result in charges to your AWS account. It is your responsibility to ensure that any resources created by this script are removed when you are done with them. 

The Amazon S3 service uses the following terms:

- 
        Bucket — A top level Amazon S3 folder. 
- 
        Prefix — An Amazon S3 folder in a bucket. 
- 
        Object — Any item hosted in an Amazon S3 bucket. 

## About this example

    This example demonstrates how to interact with some of the basic Amazon S3 operations using a
      set of functions in shell script files. The functions are located in the shell script file
      named `bucket-operations.sh`. You can call these functions in another file.
      Each script file contains comments describing each of the functions.

To see the intermediate results of each step, run the script with a `-i`
      parameter. You can view the current status of the bucket or its contents using the Amazon S3
      console. The script only proceeds to the next step when you press **enter** at the prompt. 

For the full example and downloadable script files, see [Amazon S3 Bucket Lifecycle Operations](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/aws-cli/bash-linux/s3/bucket-lifecycle-operations) in the 

*AWS Code Examples Repository*on

*GitHub*.

## Files

    The example contains the following files:

- **bucket-operations.sh**
- 
          This main script file can be sourced from another file. It includes functions that perform the following tasks: - 
              Creating a bucket and verifying that it exists 
- 
              Copying a file from the local computer to a bucket 
- 
              Copying a file from one bucket location to a different bucket location 
- 
              Listing the contents of a bucket 
- 
              Deleting a file from a bucket 
- 
              Deleting a bucket 
 View the code for [bucket-operations.sh](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/aws-cli/bash-linux/s3/bucket-lifecycle-operations/bucket_operations.sh)*GitHub*.
- 
              

- **test-bucket-operations.sh**
- 
          The shell script file `test-bucket-operations.sh`demonstrates how to call the functions by sourcing the`bucket-operations.sh`file and calling each of the functions. After calling functions, the test script removes all resources that it created.View the code for [test-bucket-operations.sh](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/aws-cli/bash-linux/s3/bucket-lifecycle-operations/test_bucket_operations.sh)*GitHub*.

- **awsdocs-general.sh**
- 
          The script file `awsdocs-general.sh`holds general purpose functions used across advanced code examples for the AWS CLI.View the code for [awsdocs-general.sh](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/aws-cli/bash-linux/s3/bucket-lifecycle-operations/awsdocs_general.sh)*GitHub*.

## References

      **AWS CLI reference:**

**Other reference:**

- 
        [Working with Amazon S3 buckets](https://docs.aws.amazon.com//AmazonS3/latest/userguide/UsingBucket.html)in the*Amazon S3 User Guide*
- 
        [Working with Amazon S3 objects](https://docs.aws.amazon.com//AmazonS3/latest/userguide/UsingObjects.html)in the*Amazon S3 User Guide*
- 
        To view and contribute to AWS SDK and AWS CLI code examples, see the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/)on*GitHub*.