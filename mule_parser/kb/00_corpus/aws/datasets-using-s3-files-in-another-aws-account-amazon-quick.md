# Datasets using S3 files in another AWS account - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/using-s3-files-in-another-aws-account.html](https://docs.aws.amazon.com/quick/latest/userguide/using-s3-files-in-another-aws-account.html)

---

Use this section to learn how to set up security so you can use Quick Sight to access Amazon S3 files in another AWS account.

For you to access files in another account, the owner of the other account must first set Amazon S3 to grant you permissions to read the file. Then, in Quick Sight, you must set up access to the buckets that were shared with you. After both of these steps are finished, you can use a manifest to create a dataset.

###### Note

To access files that are shared with the public, you don't need to set up any special security. However, you still need a manifest file.

###### Topics

## Setting up Amazon S3 to allow access from a different Quick account

                Use this section to learn how to set permissions in Amazon S3 files so they can be accessed by Quick Sight in another AWS account.

For information on accessing another account's Amazon S3 files from your
                    Quick Sight account, see [Setting up Quick Sight to access Amazon S3 files in another AWS account](#setup-quicksight-to-access-S3-in-a-different-account). For more
                    information about S3 permissions, see [Managing
                        access permissions to your Amazon S3 resources](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html) and [How do I set permissions on an object?](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/set-object-permissions.html)

You can use the following procedure to set this access from the S3 console. Or
                    you can grant permissions by using the AWS CLI or by writing a script. If you have
                    a lot of files to share, you can instead create an S3 bucket policy on the
                        `s3:GetObject` action. To use a bucket policy, add it to the
                    bucket permissions, not to the file permissions. For information on bucket
                    policies, see [Bucket policy examples](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html) in the *Amazon S3
                        Developer Guide. *

###### To set access from a different Quick account from the S3 console

- 
                        Get the email address of the AWS account email that you want to share with. Or you can get and use the canonical user ID. For more information on canonical user IDs, see [AWS account identifiers](https://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html)in the*AWS General Reference.*
- Sign in to the AWS Management Console and open the Amazon S3 console at - [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).
- 
                        Find the Amazon S3 bucket that you want to share with Quick Sight. Choose **Permissions**.
- 
                        Choose **Add Account**, and then enter an email address, or paste in a canonical user ID, for the AWS account that you want to share with. This email address should be the primary one for the AWS account.
- 
                        Choose **Yes**for both**Read bucket permissions**and**List objects**.Choose **Save**to confirm.
- 
                        Find the file that you want to share, and open the file's permission settings. 
- 
                        Enter an email address or the canonical user ID for the AWS account that you want to share with. This email address should be the primary one for the AWS account. 
- 
                        Enable **Read object**permissions for each file that Quick Sight needs access to.
- 
                        Notify the Quick user that the files are now available for use. 

## Setting up Quick Sight to access Amazon S3 files in another AWS account

                Use this section to learn how to set up Quick Sight so you can access Amazon S3
                    files in another AWS account. For information on allowing someone else to
                    access your Amazon S3 files from their Quick account, see [Setting up Amazon S3 to allow access from a different Quick account](#setup-S3-to-allow-access-from-a-different-quicksight-account).

Use the following procedure to access another account's Amazon S3 files from Quick Sight. Before you can use this procedure, the users in the other AWS account must share the files in their Amazon S3 bucket with you.

###### To access another account's Amazon S3 files from Quick Sight

- 
                        Verify that the user or users in the other AWS account gave your account read and write permission to the S3 bucket in question. 
- 
                        Choose your profile icon, and then choose **Manage Quick Sight**.
- 
                        Choose **Security & permissions**.
- 
                        Under **Quick Sight access to AWS services**, choose**Manage**.
- 
                        Choose **Select S3 buckets**.
- 
                        On the **Select Amazon S3 buckets**screen, choose the**S3 buckets you can access across AWS**tab.The default tab is named **S3 buckets linked to Quick Sight account**. It shows all the buckets your Quick account has access to.
- 
                        Do one of the following: - 
                                To add all the buckets that you have permission to use, choose **Choose accessible buckets from other AWS accounts**.
- 
                                If you have one or more Amazon S3 buckets that you want to add, enter their names. Each must exactly match the unique name of the Amazon S3 bucket. If you don't have the appropriate permissions, you see the error message "We can't connect to this S3 bucket. Make sure that any S3 buckets you specify are associated with the AWS account used to create this Quick account." This error message appears if you don't have either account permissions or Quick Sight permissions. 
 ###### NoteTo use Amazon Athena, Quick Sight needs to access the Amazon S3 buckets that Athena uses. You can add them here one by one, or use the **Choose accessible buckets from other AWS accounts**option.
- 
                                
- 
                        Choose **Select buckets**to confirm your selection.
- 
                        Create a new dataset based on Amazon S3, and upload your manifest file. For more information Amazon S3 datasets, see [Creating a dataset using Amazon S3 files](./create-a-data-set-s3.html).