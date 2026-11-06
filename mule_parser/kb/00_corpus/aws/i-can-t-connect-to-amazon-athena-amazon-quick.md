# I can't connect to Amazon Athena - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/troubleshoot-connect-athena.html](https://docs.aws.amazon.com/quick/latest/userguide/troubleshoot-connect-athena.html)

---

| Intended audience: Amazon Quick administrators | 

Use this section to help troubleshoot connecting to Athena.

If you can't connect to Amazon Athena, you might get an insufficient permissions error when you run a query, showing that the permissions aren't configured. To verify that you can connect Amazon Quick Sight to Athena, check the following settings:

- 
					AWS resource permissions inside of Amazon Quick Sight 
- 
					AWS Identity and Access Management (IAM) policies 
- 
					Amazon S3 location 
- 
					Query results location 
- 
					AWS KMS key policy (for encrypted datasets only) 

For details, see following. For information about troubleshooting other Athena
				issues, see [Connectivity issues when using Amazon Athena with Amazon Quick Sight](./troubleshoot-athena.html).

## Make sure that you authorized Amazon Quick Sight to use Athena

				| Intended audience: Amazon Quick administrators | 

Use the following procedure to make sure that you successfully authorized Amazon Quick Sight to use Athena. Permissions to AWS resources apply to all Amazon Quick Sight users.

To perform this action, you must be an Amazon Quick Sight administrator. To check if you
					have access, verify that you see the **Manage QuickSight**
					option when you open the menu from your profile at upper right.

###### To authorize Amazon Quick Sight to access Athena

- 
						Choose your profile name (upper right). Choose **Manage Quick Sight**, and then scroll down to the**Custom permissions**section.
- 
						Choose **AWS resources**then choose**Add or remove**.
- 
						Find Athena in the list. Clear the box by Athena, then select it again to enable Athena. Then choose **Connect both**.
- 
						Choose the buckets that you want to access from Amazon Quick Sight. The settings for S3 buckets that you access here are the same ones that you access by choosing Amazon S3 from the list of AWS services. Be careful that you don't inadvertently disable a bucket that someone else uses. 
- 
						Choose **Finish**to confirm your selection. Or choose**Cancel**to exit without saving.
- 
						Choose **Update**to save your new settings for Amazon Quick Sight access to AWS services. Or choose**Cancel**to exit without making any changes.
- 
						Make sure that you are using the correct AWS Region when you are finished. If you had to change your AWS Region as part of the first step of this process, change it back to the AWS Region that you were using before. 

## Make sure that your IAM policies grant the right permissions

				| Intended audience: System administrators | 

Your AWS Identity and Access Management (IAM) policies must grant permissions to specific actions. Your IAM user or role must be able to read and write both the input and the output of the S3 buckets that Athena uses for your query.

If the dataset is encrypted, the IAM user needs to be a key user in the specified AWS KMS key's policy.

###### To verify that your IAM policies have permission to use S3 buckets for your query

- Open the IAM console at - [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).
- 
						Locate the IAM user or role that you are using. Choose the user or role name to see the associated policies. 
- 
						Verify that your policy has the correct permissions. Choose a policy that you want to verify, and then choose **Edit policy**. Use the visual editor, which opens by default. If you have the JSON editor open instead, choose the**Visual editor**tab.
- 
						Choose the S3 entry in the list to see its contents. The policy needs to grant permissions to list, read, and write. If S3 is not in the list, or it doesn't have the correct permissions, you can add them here. 

For examples of IAM policies that work with Quick Sight, see [IAM policy examples for Quick](./iam-policy-examples.html).

## Make sure that the IAM user has read/write access to your S3 location

				| Intended audience: Amazon Quick administrators | 

To access Athena data from Quick Sight, first make sure that Athena and its S3
					location are authorized in **Manage QuickSight** screen. For
					more information, see [Make sure that you authorized Amazon Quick Sight to use Athena](#troubleshoot-connect-athena-authorizing). 

Next, verify the relevant IAM permissions. The IAM user for your Athena
					connection needs read/write access to the location where your results go in S3.
					Start by verifying that the IAM user has an attached policy that [allows access to Athena](https://docs.aws.amazon.com/athena/latest/ug/setting-up.html#attach-managed-policies-for-using-ate), such as
					`AmazonAthenaFullAccess`. Let Athena create the bucket using the name
					that it requires, and then add this bucket to the list of buckets that
					QuickSight can access. If you change the default location of the results bucket
						(`aws-athena-query-results-*`), be sure that the IAM user has
					permission to read and write to the new location.

Verify that you don't include the AWS Region code in the S3 URL. For
					example, use `s3://awsexamplebucket/path` and not
						`s3://us-east-1.amazonaws.com/awsexamplebucket/path`. Using the
					wrong S3 URL causes an `Access Denied` error. 

Also verify that the bucket policies and object access control lists (ACLs)
						[allow the IAM user to access the objects in the buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html). If the
					IAM user is in a different AWS account, see [Cross-account Access](https://docs.aws.amazon.com/athena/latest/ug/cross-account-permissions.html) in the
					*Amazon Athena User Guide*.

If the dataset is encrypted, verify that the IAM user is a key user in the
					specified AWS KMS key's policy. You can do this in the AWS KMS console at
					[https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms).

###### To set permissions to your Athena query results location

- 
						Open the Athena console at [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home).
- 
						Verify that you have selected the workgroup you want to use: - 
								Examine the **Workgroup**option at the top. It has the format**Workgroup:**. If the group name is the one that you want to use, skip to the next step.`group-name`
- 
								To choose a different workgroup, chose **Workgroup**at the top. Choose the workgroup that you want to use, and choose**Switch workgroup**.
 
- 
								
- 
						Choose **Settings**at upper right.(Not common) If you get an error that your workgroup is not found, use these steps to fix it: - 
								Ignore the error message for now, and instead find **Workgroup:**on the`group-name`**Settings**page. Your workgroup's name is a hyperlink. Open it.
- 
								On the **Workgroup:**page, choose`<groupname>`**Edit workgroup**at left. Now close the error message.
- 
								Near **Query result location**, open the S3 location selector by choosing the**Select**button that has the file folder icon.
- 
								Choose the small arrow at the end of the name of the S3 location for Athena. The name must begin with `aws-athena-query-results`.
- 
								(Optional) Encrypt query results by selecting the **Encrypt results stored in S3**check box.
- 
								Choose **Save**to confirm your choices.
- 
								If the error doesn't reappear, return to **Settings**.Occasionally, the error might appear again. If so, take the following steps: - 
										Choose the workgroup and then choose **View details**.
- 
										(Optional) To preserve your settings, take notes or a screenshot of the workgroup configuration. 
- 
										Choose **Create workgroup**.
- 
										Replace the workgroup with a new one. Configure the correct S3 location and encryption options. Note the S3 location because you need it later. 
- 
										Choose **Save**to proceed.
- 
										When you no longer need the original workgroup, disable it. Make sure to carefully read the warning that appears, because it tells you what you lose if you choose to disable it. 
 
- 
										
 
- 
								
- 
						If you didn't get this by troubleshooting in the previous step, choose **Settings**at upper right and get the S3 location value shown as**Query result location**.
- 
						If **Encrypt query results**is enabled, check whether it uses SSE-KMS or CSE-KMS. Note the key.
- 
						Open the S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/), open the correct bucket, and then choose the**Permissions**tab.
- 
						Check that your IAM user has access by viewing **Bucket Policy**.If you manage access with ACLs, make sure that the access control lists (ACLs) are set up by viewing **Access Control List**.
- 
						If your dataset is encrypted ( **Encrypt query results**is selected in the workgroup settings), make sure that the IAM user or role is added as a key user in that AWS KMS key's policy. You can access AWS KMS settings at[https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms).

###### To grant access to the S3 bucket used by Athena

- Open the Amazon S3 console at - [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).
- 
						Choose the S3 bucket used by Athena in the **Query result location**.
- 
						On the **Permissions**tab, verify the permissions.

For more information, see the AWS Support article [When I run an Athena query, I get an "Access Denied" error](https://aws.amazon.com/premiumsupport/knowledge-center/access-denied-athena/).