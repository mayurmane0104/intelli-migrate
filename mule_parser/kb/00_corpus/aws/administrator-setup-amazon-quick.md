# Administrator setup - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/s3-admin-setup.html](https://docs.aws.amazon.com/quick/latest/userguide/s3-admin-setup.html)

---

Before users can create Amazon S3 integrations and knowledge bases, an Amazon Quick administrator must complete the following setup tasks.

## Grant Amazon Quick access to Amazon S3 buckets

        Grant Amazon Quick access to the Amazon S3 buckets your organization needs. This applies whether the buckets are in the same AWS account or a different account.

- 
                In the Amazon Quick admin console, under **Permissions**, choose**AWS resources**.
- 
                Under **Allow access and autodiscovery for these resources**, select the**Amazon S3**checkbox.
- 
                Choose **Select S3 buckets**.
- 
                In the **Select Amazon S3 buckets**dialog, choose the tab that matches your bucket location:- 
                        **S3 Buckets Linked To Quick Account**– Select the buckets from the list that you want Amazon Quick to access. Selected buckets have read-only permissions by default.
- 
                        **S3 Buckets You Can Access Across AWS**– For cross-account buckets, make sure the account owner has authorized your account. Choose**Use a different bucket**, enter the bucket name, and choose**Add S3 bucket**.
 
- 
                        
- 
                (Optional) For cross-account buckets, select **Restrict bucket access to knowledge base creator**to limit access so that only the user who creates the knowledge base can use the bucket.
- 
                Choose **Finish**.

The selected buckets are now accessible to users during knowledge base creation.

## Prepare IAM role and policy setup

        
        Amazon S3 integration uses AWS authentication to access your Amazon S3 buckets. Prepare your IAM role and policy configuration before users set up the integration.

### Required IAM permissions

Make sure your AWS account has the following minimum permissions for the Amazon S3 bucket:

- `s3:GetObject`– Read objects from the bucket.
- `s3:ListBucket`– List bucket contents.
- `s3:GetBucketLocation`– Get bucket region information.
- `s3:GetObjectVersion`– Get object versions.
- `s3:ListBucketVersions`– List bucket versions.

### Configure Amazon S3 bucket permissions for cross-account access

If you're accessing Amazon S3 buckets in a different AWS account, you must configure IAM policies in the source AWS account.

###### To configure Amazon S3 bucket permissions for cross-account access

- 
                    Sign in to the AWS Management Console for the account that contains the Amazon S3 bucket. 
- 
                    Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).
- 
                    Choose the bucket that you want to grant access to. 
- 
                    Choose **Permissions**, and then choose**Bucket Policy**.
- 
                    Add a bucket policy with the following elements: - `Version`– Set to "2012-10-17"
- `Statement`– Array containing policy statements with:- `Sid`– "AllowQuickSuiteS3Access"
- `Effect`– "Allow"
- `Principal`– AWS ARN for the Amazon Quick service role in your account. For example, the principal should look like this:- `"Principal": { "AWS": "arn:aws:iam::<quick_account_id>:role/service-role/aws-quicksight-service-role-v0" }`
- `Action`– Array of Amazon S3 permissions: s3:GetObject, s3:ListBucket, s3:GetBucketLocation, s3:GetObjectVersion, s3:ListBucketVersions
- `Resource`– "*" (applies to the current key), the Amazon S3 bucket path should look like the following:- `"Resource": [ "arn:aws:s3:::bucket_name"]`
 
 
- 
                    Choose **Save changes**.

### Configure KMS key permissions (if your bucket uses encryption)

If your Amazon S3 bucket uses AWS KMS encryption, complete the following steps.

###### To configure KMS key permissions

- 
                    Open the AWS Key Management Service (AWS KMS) console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms).
- 
                    Choose the KMS key that is used to encrypt your Amazon S3 bucket. 
- 
                    Choose **Key policy**, and then choose**Edit**.
- 
                    Add a statement to the key policy with the following structural elements: - `Sid`– "AllowQuickSuiteKMSAccess"
- `Effect`– "Allow"
- `Principal`– AWS ARN for the Amazon Quick service role in your account. For example, the principal should look like this:- `"Principal": { "AWS": "arn:aws:iam::<quick_account_id>:role/service-role/aws-quicksight-service-role-v0" }`
- `Action`– Array of KMS permissions: kms:Decrypt, kms:DescribeKey
- `Resource`– "*" (applies to the current key), the Amazon S3 bucket path should look like the following:- `"Resource": [ "arn:aws:s3:::bucket_name"]`
 
- 
                    Choose **Save changes**.
- 
                    Wait 2-3 minutes for the policy changes to propagate. 

## Configure VPC access for Amazon S3 Connector in Amazon Quick

        
        VPC permissions ensure Amazon Quick can only access your Amazon S3 bucket through secure VPC or VPC endpoint connections.

### Required policy change

Add this statement to your bucket access policy to allow Amazon Quick to access your bucket through VPC endpoints:

```
{
  "Sid": "Allow-Quick-access",
  "Principal": "arn:aws:iam::Quick Account:role/service-role/aws-quicksight-service-role-v0",
  "Action": "s3:*",
  "Effect": "Allow",
  "Resource": [
    "arn:aws:s3:::amzn-s3-demo-bucket",
    "arn:aws:s3:::amzn-s3-demo-bucket/*"
  ],
  "Condition": {
    "Null": {
      "aws:SourceVpce": "false"
    }
  }
}
```
- 
                    Replace `amzn-s3-demo-bucket`with your bucket name.
- 
                    Replace `Quick Account`with your Amazon Quick account.

The `"aws:SourceVpce": "false"` condition ensures Amazon Quick can only access your bucket through VPC endpoints, maintaining your security requirements.

### Deny policies

If your bucket has a policy that restricts traffic to a specific VPC or VPC endpoint via Deny Policy, you must reverse this policy because deny policies take precedence over allow policies.

For example:

```
{
   "Version":"2012-10-17",                   
   "Id": "Policy1415115909152",
   "Statement": [
     {
       "Sid": "Access-to-specific-VPCE-only",
       "Principal": "*",
       "Action": "s3:*",
       "Effect": "Deny",
       "Resource": ["arn:aws:s3:::amzn-s3-demo-bucket",
                    "arn:aws:s3:::amzn-s3-demo-bucket/*"],
       "Condition": {
         "StringNotEquals": {
           "aws:SourceVpce": "vpce-0abcdef1234567890"
         }
       }
     }
   ]
}
```
Should be reversed into:

```
{
   "Version":"2012-10-17",                   
   "Id": "Policy1415115909152",
   "Statement": [
     {
       "Sid": "Access-to-specific-VPCE-only",
       "Principal": "*",
       "Action": "s3:*",
       "Effect": "Allow",
       "Resource": ["arn:aws:s3:::amzn-s3-demo-bucket",
                    "arn:aws:s3:::amzn-s3-demo-bucket/*"],
       "Condition": {
         "StringEquals": {
           "aws:SourceVpce": "vpce-0abcdef1234567890"
         }
       }
     }
   ]
}
```
### Best practices

**Restrict access to your Amazon Quick role**

Access policies should enforce that the caller is your Amazon Quick role ARN or, at minimum, your Amazon Quick account. This ensures that despite allowing VPC traffic, calls come only from expected sources.

### Security recommendations

- 
                    Restrict policies to your Amazon Quick role for most secure traffic 
- 
                    Review your bucket policies regularly to ensure they follow the principle of least privilege 

## Restrict Amazon S3 bucket access with IAM policy assignments

        You can control which Amazon S3 buckets your Amazon Quick users can use to create knowledge bases by creating IAM policies and assigning them to specific users, groups, or all users through Amazon Quick IAM policy assignments. This allows you to restrict who can create knowledge bases against specific buckets, including ACL-aware knowledge bases.

###### Note

IAM policies assigned through Amazon Quick take precedence over AWS resource-level policies. To ensure your access requirements are met, configure your IAM policies appropriately.

For example, you can assign a restrictive policy to specific users who need access to ACL-aware buckets, while assigning a broader policy to all users for non-ACL buckets.

### Step 1: Create an Amazon S3 access policy in IAM

Create an IAM policy in the AWS IAM console that defines which Amazon S3 buckets users can access for knowledge base creation. The following example policy grants access to two specific buckets:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:ListAllMyBuckets",
            "Resource": "arn:aws:s3:::*"
        },
        {
            "Action": [
                "s3:ListBucket"
            ],
            "Effect": "Allow",
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket-1",
                "arn:aws:s3:::amzn-s3-demo-bucket-2"
            ]
        },
        {
            "Action": [
                "s3:GetObject",
                "s3:GetObjectVersion"
            ],
            "Effect": "Allow",
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket-1/*",
                "arn:aws:s3:::amzn-s3-demo-bucket-2/*"
            ]
        },
        {
            "Action": [
                "s3:ListBucketMultipartUploads",
                "s3:GetBucketLocation"
            ],
            "Effect": "Allow",
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket-1",
                "arn:aws:s3:::amzn-s3-demo-bucket-2"
            ]
        },
        {
            "Action": [
                "s3:PutObject",
                "s3:AbortMultipartUpload",
                "s3:ListMultipartUploadParts"
            ],
            "Effect": "Allow",
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket-1/*",
                "arn:aws:s3:::amzn-s3-demo-bucket-2/*"
            ]
        }
    ]
}
```
Replace `amzn-s3-demo-bucket-1` and
                `amzn-s3-demo-bucket-2` with the names of the Amazon S3 buckets you want
                to grant access to.

### Step 2: Assign the policy in Amazon Quick

After creating the IAM policy, assign it to Amazon Quick users or groups.

- 
                    In the Amazon Quick admin console, under **Permissions**, choose**IAM policy assignments**.
- 
                    Choose **Add new assignment**.
- 
                    Enter a name for the assignment. 
- 
                    On the **Select an IAM policy**page, search for and select the IAM policy you created in Step 1. Choose**Next**.
- 
                    On the **Assign users and groups**page, choose one of the following:- 
                            Select **Assign to all users and groups**to apply the policy to all current and future users.
- 
                            Search for and select specific users or groups to assign the policy to. 
 Choose **Next**.
- 
                            
- 
                    On the **Review and enable changes**page, verify your assignment details and choose**Save and enable**.

Users who are not explicitly granted access through an IAM policy assignment will not be able to access the restricted Amazon S3 buckets for creating integrations or knowledge bases.