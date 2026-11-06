# I can't connect to Amazon S3 - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/troubleshoot-connect-S3.html](https://docs.aws.amazon.com/quick/latest/userguide/troubleshoot-connect-S3.html)

---

To successfully connect to Amazon S3, make sure that you configure authentication and create a valid manifest file inside the bucket you are trying to access. Also, make sure that the file described by the manifest is available.

To verify authentication, make sure that you authorized Amazon Quick Sight to access the S3 account. It's not enough that you, the user, are authorized. Amazon Quick Sight must be authorized separately.

###### To authorize Amazon Quick Sight to access your Amazon S3 bucket

- 
					In the AWS Region list at upper right, choose the US East (N. Virginia) Region. You use this AWS Region temporarily while you edit your account permissions. 
- 
					Inside Amazon Quick Sight, choose your profile name (upper right). Choose **Manage Quick Sight**, and then scroll down to the**Custom permissions**section.
- 
					Choose **AWS resources**then choose**Add or remove**.
- 
					Locate Amazon S3 in the list. Choose one of the following actions to open the screen where you can choose S3 buckets: - 
							If the check box is clear, select the check box next to Amazon S3. 
- 
							If the check box is selected, choose **Details**, and then choose**Select S3 buckets**.
 
- 
							
- 
					Choose the buckets that you want to access from Amazon Quick Sight. Then choose **Select**.
- 
					Choose **Update**.
- 
					If you changed your AWS Region during the first step of this process, change it back to the AWS Region that you want to use. 

We strongly recommend that you make sure that your manifest file is valid. If Amazon Quick Sight can't parse your file, it gives you an error message. That might be something like "We can't parse the manifest file as valid JSON" or "We can't connect to the S3 bucket."

###### To verify your manifest file

- 
					Open your manifest file. You can do this directly from the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/). Go to your manifest file and choose**Open**.
- 
					Make sure that the URI or URLs provided inside the manifest file indicate the file or files that you want connect to. 
- 
					Make sure that your manifest file is formed correctly, if you use a link to the manifest file rather than uploading the file. The link shouldn't have any additional phrases after the word `.json`. You can get the correct link to an S3 file by viewing its**Link**value in the details on the S3 console.
- 
					Make sure that the content of the manifest file is valid by using a JSON validator, like the one at [https://jsonlint.com](https://jsonlint.com).
- 
					Verify permissions on your bucket or file. In the [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/), navigate to your Amazon S3 bucket, choose the**Permissions**tab, and add the appropriate permissions. Make sure that the permissions are at the right level, either on the bucket or on the file or files.
- 
					If you are using the `s3://`protocol, rather than`https://`, make sure that you reference your bucket directly. For example, use`s3://awsexamplebucket/myfile.csv`instead of`s3://s3-us-west-2.amazonaws.com/awsexamplebucket/myfile.csv`. Doubly specifying Amazon S3, by using`s3://`and also`s3-us-west-2.amazonaws.com`, causes an error.For more information about manifest files and connecting to Amazon S3, see [Supported formats for Amazon S3 manifest files](./supported-manifest-file-format.html).

In addition, verify that your Amazon S3 dataset was created according to the steps in
					[Creating a dataset using Amazon S3 files](./create-a-data-set-s3.html).

If you use Athena to connect to Amazon S3, see [I can't connect to Amazon Athena](./troubleshoot-connect-athena.html).