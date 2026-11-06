# Insufficient permissions when using Athena with Amazon Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/troubleshoot-athena-insufficient-permissions.html](https://docs.aws.amazon.com/quick/latest/userguide/troubleshoot-athena-insufficient-permissions.html)

---

If you receive an error message that says you have insufficient permissions, try the following steps to resolve your problem.

You need administrator permissions to troubleshoot this issue.

###### To resolve an insufficient permissions error

- 
					Make sure that Amazon Quick Sight can access the Amazon S3 buckets used by Athena: - 
							To do this, choose your profile name (upper right). Choose **Manage Quick Sight**, and then scroll down to the**Custom permissions**section.
- 
							Choose **AWS resources**then choose**Add or remove**.
- 
							Locate Athena in the list. Clear the check box by Athena, then select it again to enable Athena. Choose **Connect both**.
- 
							Choose the buckets that you want to access from Amazon Quick Sight. The settings for S3 buckets that you access here are the same ones that you access by choosing Amazon S3 from the list of AWS services. Be careful that you don't inadvertently disable a bucket that someone else uses. 
- 
							Choose **Select**to save your S3 buckets.
- 
							Choose **Update**to save your new settings for Amazon Quick Sight access to AWS services. Or choose**Cancel**to exit without making any changes.
 
- 
							
- 
					If your data file is encrypted with an AWS KMS key, grant permissions to the Amazon Quick Sight IAM role to decrypt the key. The easiest way to do this is to use the AWS CLI. You can run the [create-grant](https://docs.aws.amazon.com/cli/latest/reference/kms/create-grant.html)command in AWS CLI to do this.`aws kms create-grant --key-id <AWS KMS key ARN> --grantee-principal``<Your Amazon Quick Sight Role ARN>`--operations DecryptThe Amazon Resource Name (ARN) for the Amazon Quick Sight role has the format `arn:aws:iam::<account id>:role/service-role/aws-quicksight-service-role-v<version number>`and can be accessed from the IAM console. To find your AWS KMS key ARN, use the S3 console. Go to the bucket that contains your data file and choose the**Overview**tab. The key is located near**KMS key ID**.

For Amazon Athena, Amazon S3, and Athena Query Federation connections, Quick Sight uses the following IAM role by default:

`arn:aws:iam::``AWS-ACCOUNT-ID`:role/service-role/aws-quicksight-s3-consumers-role-v0

If the `aws-quicksight-s3-consumers-role-v0` is not present, then
				Quick Sight uses:

`arn:aws:iam::``AWS-ACCOUNT-ID`:role/service-role/aws-quicksight-service-role-v0