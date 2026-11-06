# Amazon Glacier examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_glacier_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_glacier_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon Glacier.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `abort-multipart-upload`.

- **AWS CLI**
- 
            
                    The following command deletes an in-progress multipart upload to a vault named `my-vault`:`aws glacier abort``-`multipart-upload --account-id - --vault-name`my-vault`--upload-id`19gaRezEXAMPLES6Ry5YYdqthHOC_kGRCT03L9yetr220UmPtBYKk-OssZtLqyFu7sY1_lR7vgFuJV6NtcV5zpsJ`This command does not produce any output. Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account. The upload ID is returned by the `aws glacier initiate-multipart-upload`command and can also be obtained by using`aws glacier list-multipart-uploads`.For more information on multipart uploads to Amazon Glacier using the AWS CLI, see Using Amazon Glacier in the *AWS CLI User Guide*.- 
                    For API details, see [AbortMultipartUpload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/abort-multipart-upload.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `abort-vault-lock`.

- **AWS CLI**
- 
            
                    **To abort an in-progress vault lock process**The following `abort-vault-lock`example deletes a vault lock policy from the specified vault and resets the lock state of the vault lock to unlocked.`aws glacier abort``-`vault-lock \ --account-id - \ --vault-name`MyVaultName`This command produces no output. For more information, see [Abort Vault Lock (DELETE lock-policy)](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-AbortVaultLock.html)in the*Amazon Glacier API Developer Guide*.- 
                    For API details, see [AbortVaultLock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/abort-vault-lock.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `add-tags-to-vault`.

- **AWS CLI**
- 
            
                    The following command adds two tags to a vault named `my-vault`:`aws glacier add``-`tags-to-vault --account-id - --vault-name`my-vault`--tags`id=1234,date=july2015`Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account. - 
                    For API details, see [AddTagsToVault](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/add-tags-to-vault.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `complete-multipart-upload`.

- **AWS CLI**
- 
            
                    The following command completes multipart upload for a 3 MiB archive: `aws glacier complete-multipart-upload --archive-size``3145728`--checksum`9628195fcdbcbbe76cdde456d4646fa7de5f219fb39823836d81f0cc0e18aa67`--upload-id`19gaRezEXAMPLES6Ry5YYdqthHOC_kGRCT03L9yetr220UmPtBYKk-OssZtLqyFu7sY1_lR7vgFuJV6NtcV5zpsJ``-`-account-id - --vault-name`my-vault`Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account. The upload ID is returned by the `aws glacier initiate-multipart-upload`command and can also be obtained by using`aws glacier list-multipart-uploads`. The checksum parameter takes a SHA-256 tree hash of the archive in hexadecimal.For more information on multipart uploads to Amazon Glacier using the AWS CLI, including instructions on calculating a tree hash, see Using Amazon Glacier in the *AWS CLI User Guide*.- 
                    For API details, see [CompleteMultipartUpload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/complete-multipart-upload.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `complete-vault-lock`.

- **AWS CLI**
- 
            
                    **To complete an in-progress vault lock process**The following `complete-vault-lock`example completes the in-progress locking progress for the specified vault and sets the lock state of the vault lock to`Locked`. You get the value for the`lock-id`parameter when you run`initiate-lock-process`.`aws glacier complete``-`vault-lock \ --account-id - \ --vault-name`MyVaultName`\ --lock-id`9QZgEXAMPLEPhvL6xEXAMPLE`This command produces no output. For more information, see [Complete Vault Lock (POST lockId)](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-CompleteVaultLock.html)in the*Amazon Glacier API Developer Guide*.- 
                    For API details, see [CompleteVaultLock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/complete-vault-lock.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-vault`.

- **AWS CLI**
- 
            
                    The following command creates a new vault named `my-vault`:`aws glacier create-vault --vault-name``my-vault``-`-account-id -Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account. - 
                    For API details, see [CreateVault](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/create-vault.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-archive`.

- **AWS CLI**
- 
            
                    **To delete an archive from a vault**The following `delete-archive`example removes the specified archive from`example_vault`.`aws glacier delete-archive \ --account-id``111122223333`\ --vault-name`example_vault`\ --archive-id`Sc0u9ZP8yaWkmh-XGlIvAVprtLhaLCGnNwNl5I5x9HqPIkX5mjc0DrId3Ln-Gi_k2HzmlIDZUz117KSdVMdMXLuFWi9PJUitxWO73edQ43eTlMWkH0pd9zVSAuV_XXZBVhKhyGhJ7w`This command produces no output. - 
                    For API details, see [DeleteArchive](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/delete-archive.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-vault-access-policy`.

- **AWS CLI**
- 
            
                    **To remove the access policy of a vault**The following `delete-vault-access-policy`example removes the access policy for the specified vault.`aws glacier delete-vault-access-policy \ --account-id``111122223333`\ --vault-name`example_vault`This command produces no output. - 
                    For API details, see [DeleteVaultAccessPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/delete-vault-access-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-vault-notifications`.

- **AWS CLI**
- 
            
                    **To remove the SNS notifications for a vault**The following `delete-vault-notifications`example removes notifications sent by Amazon Simple Notification Service (Amazon SNS) for the specified vault.`aws glacier delete-vault-notifications \ --account-id``111122223333`\ --vault-name`example_vault`This command produces no output. - 
                    For API details, see [DeleteVaultNotifications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/delete-vault-notifications.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-vault`.

- **AWS CLI**
- 
            
                    The following command deletes a vault named `my-vault`:`aws glacier delete-vault --vault-name``my-vault``-`-account-id -This command does not produce any output. Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account. - 
                    For API details, see [DeleteVault](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/delete-vault.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-job`.

- **AWS CLI**
- 
            
                    The following command retrieves information about an inventory retrieval job on a vault named `my-vault`:`aws glacier describe``-`job --account-id - --vault-name`my-vault`--job-id`zbxcm3Z_3z5UkoroF7SuZKrxgGoDc3RloGduS7Eg-RO47Yc6FxsdGBgf_Q2DK5Ejh18CnTS5XW4_XqlNHS61dsO4CnMW`Output: `{ "InventoryRetrievalParameters": { "Format": "JSON" }, "VaultARN": "arn:aws:glacier:us-west-2:0123456789012:vaults/my-vault", "Completed": false, "JobId": "zbxcm3Z_3z5UkoroF7SuZKrxgGoDc3RloGduS7Eg-RO47Yc6FxsdGBgf_Q2DK5Ejh18CnTS5XW4_XqlNHS61dsO4CnMW", "Action": "InventoryRetrieval", "CreationDate": "2015-07-17T20:23:41.616Z", "StatusCode": "InProgress" }`The job ID can be found in the output of `aws glacier initiate-job`and`aws glacier list-jobs`. Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account.- 
                    For API details, see [DescribeJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/describe-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-vault`.

- **AWS CLI**
- 
            
                    The following command retrieves data about a vault named `my-vault`:`aws glacier describe-vault --vault-name``my-vault``-`-account-id -Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account. - 
                    For API details, see [DescribeVault](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/describe-vault.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-data-retrieval-policy`.

- **AWS CLI**
- 
            
                    The following command gets the data retrieval policy for the in-use account: `aws glacier get``-`data-retrieval-policy --account-id -Output: `{ "Policy": { "Rules": [ { "BytesPerHour": 10737418240, "Strategy": "BytesPerHour" } ] } }`Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account. - 
                    For API details, see [GetDataRetrievalPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/get-data-retrieval-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-job-output`.

- **AWS CLI**
- 
            
                    The following command saves the output from a vault inventory job to a file in the current directory named `output.json`:`aws glacier get``-`job-output --account-id - --vault-name`my-vault`--job-id`zbxcm3Z_3z5UkoroF7SuZKrxgGoDc3RloGduS7Eg-RO47Yc6FxsdGBgf_Q2DK5Ejh18CnTS5XW4_XqlNHS61dsO4CnMW``output.json`The `job-id`is available in the output of`aws glacier list-jobs`. Note that the output file name is a positional argument that is not prefixed by an option name. Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account.Output: `{ "status": 200, "acceptRanges": "bytes", "contentType": "application/json" }``output.json`:`{"VaultARN":"arn:aws:glacier:us-west-2:0123456789012:vaults/my-vault","InventoryDate":"2015-04-07T00:26:18Z","ArchiveList":[{"ArchiveId":"kKB7ymWJVpPSwhGP6ycSOAekp9ZYe_--zM_mw6k76ZFGEIWQX-ybtRDvc2VkPSDtfKmQrj0IRQLSGsNuDp-AJVlu2ccmDSyDUmZwKbwbpAdGATGDiB3hHO0bjbGehXTcApVud_wyDw","ArchiveDescription":"multipart upload test","CreationDate":"2015-04-06T22:24:34Z","Size":3145728,"SHA256TreeHash":"9628195fcdbcbbe76cdde932d4646fa7de5f219fb39823836d81f0cc0e18aa67"}]}`- 
                    For API details, see [GetJobOutput](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/get-job-output.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-vault-access-policy`.

- **AWS CLI**
- 
            
                    **To retrieve the access policy of a vault**The following `get-vault-access-policy`example retrieves the access policy for the specified vault.`aws glacier get-vault-access-policy \ --account-id``111122223333`\ --vault-name`example_vault`Output: `{ "policy": { "Policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::444455556666:root\"},\"Action\":\"glacier:ListJobs\",\"Resource\":\"arn:aws:glacier:us-east-1:111122223333:vaults/example_vault\"},{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::444455556666:root\"},\"Action\":\"glacier:UploadArchive\",\"Resource\":\"arn:aws:glacier:us-east-1:111122223333:vaults/example_vault\"}]}" } }`- 
                    For API details, see [GetVaultAccessPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/get-vault-access-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-vault-lock`.

- **AWS CLI**
- 
            
                    **To get the details of a vault lock**The following `get-vault-lock`example retrieved the details about the lock for the specified vault.`aws glacier get``-`vault-lock \ --account-id - \ --vault-name`MyVaultName`Output: `{ "Policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"Define-vault-lock\",\"Effect\":\"Deny\",\"Principal\":{\"AWS\":\"arn:aws:iam::999999999999:root\"},\"Action\":\"glacier:DeleteArchive\",\"Resource\":\"arn:aws:glacier:us-west-2:99999999999:vaults/MyVaultName\",\"Condition\":{\"NumericLessThanEquals\":{\"glacier:ArchiveAgeinDays\":\"365\"}}}]}", "State": "Locked", "CreationDate": "2019-07-29T22:25:28.640Z" }`For more information, see [Get Vault Lock (GET lock-policy)](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-GetVaultLock.html)in the*Amazon Glacier API Developer Guide*.- 
                    For API details, see [GetVaultLock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/get-vault-lock.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-vault-notifications`.

- **AWS CLI**
- 
            
                    The following command gets a description of the notification configuration for a vault named `my-vault`:`aws glacier get``-`vault-notifications --account-id - --vault-name`my-vault`Output: `{ "vaultNotificationConfig": { "Events": [ "InventoryRetrievalCompleted", "ArchiveRetrievalCompleted" ], "SNSTopic": "arn:aws:sns:us-west-2:0123456789012:my-vault" } }`If no notifications have been configured for the vault, an error is returned. Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account. - 
                    For API details, see [GetVaultNotifications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/get-vault-notifications.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `initiate-job`.

- **AWS CLI**
- 
            
                    The following command initiates a job to get an inventory of the vault `my-vault`:`aws glacier initiate``-`job --account-id - --vault-name`my-vault`--job-parameters '`{"Type": "inventory-retrieval"}`'Output: `{ "location": "/0123456789012/vaults/my-vault/jobs/zbxcm3Z_3z5UkoroF7SuZKrxgGoDc3RloGduS7Eg-RO47Yc6FxsdGBgf_Q2DK5Ejh18CnTS5XW4_XqlNHS61dsO4CnMW", "jobId": "zbxcm3Z_3z5UkoroF7SuZKrxgGoDc3RloGduS7Eg-RO47Yc6FxsdGBgf_Q2DK5Ejh18CnTS5XW4_XqlNHS61dsO4CnMW" }`Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account. The following command initiates a job to retrieve an archive from the vault `my-vault`:`aws glacier initiate``-`job --account-id - --vault-name`my-vault`--job-parameters`file://job-archive-retrieval.json``job-archive-retrieval.json`is a JSON file in the local folder that specifies the type of job, archive ID, and some optional parameters:`{ "Type": "archive-retrieval", "ArchiveId": "kKB7ymWJVpPSwhGP6ycSOAekp9ZYe_--zM_mw6k76ZFGEIWQX-ybtRDvc2VkPSDtfKmQrj0IRQLSGsNuDp-AJVlu2ccmDSyDUmZwKbwbpAdGATGDiB3hHO0bjbGehXTcApVud_wyDw", "Description": "Retrieve archive on 2015-07-17", "SNSTopic": "arn:aws:sns:us-west-2:0123456789012:my-topic" }`Archive IDs are available in the output of `aws glacier upload-archive`and`aws glacier get-job-output`.Output: `{ "location": "/011685312445/vaults/mwunderl/jobs/l7IL5-EkXyEY9Ws95fClzIbk2O5uLYaFdAYOi-azsX_Z8V6NH4yERHzars8wTKYQMX6nBDI9cMNHzyZJO59-8N9aHWav", "jobId": "l7IL5-EkXy2O5uLYaFdAYOiEY9Ws95fClzIbk-azsX_Z8V6NH4yERHzars8wTKYQMX6nBDI9cMNHzyZJO59-8N9aHWav" }`See Initiate Job in the *Amazon Glacier API Reference*for details on the job parameters format.- 
                    For API details, see [InitiateJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/initiate-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `initiate-multipart-upload`.

- **AWS CLI**
- 
            
                    The following command initiates a multipart upload to a vault named `my-vault`with a part size of 1 MiB (1024 x 1024 bytes) per file:`aws glacier initiate``-`multipart-upload --account-id - --part-size`1048576`--vault-name`my-vault`--archive-description`"multipart upload test"`The archive description parameter is optional. Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account. This command outputs an upload ID when successful. Use the upload ID when uploading each part of your archive with `aws glacier upload-multipart-part`. For more information on multipart uploads to Amazon Glacier using the AWS CLI, see Using Amazon Glacier in the*AWS CLI User Guide*.- 
                    For API details, see [InitiateMultipartUpload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/initiate-multipart-upload.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `initiate-vault-lock`.

- **AWS CLI**
- 
            
                    **To initiate the vault locking process**The following `initiate-vault-lock`example installs a vault lock policy on the specified vault and sets the lock state of the vault lock to`InProgress`. You must complete the process by calling`complete-vault-lock`within 24 hours to set the state of the vault lock to`Locked`.`aws glacier initiate``-`vault-lock \ --account-id - \ --vault-name`MyVaultName`\ --policy`file://vault_lock_policy.json`Contents of `vault_lock_policy.json`:`{"Policy":"{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"Define-vault-lock\",\"Effect\":\"Deny\",\"Principal\":{\"AWS\":\"arn:aws:iam::999999999999:root\"},\"Action\":\"glacier:DeleteArchive\",\"Resource\":\"arn:aws:glacier:us-west-2:999999999999:vaults/examplevault\",\"Condition\":{\"NumericLessThanEquals\":{\"glacier:ArchiveAgeinDays\":\"365\"}}}]}"}`The output is the vault lock ID that you can use to complete the vault lock process. `{ "lockId": "9QZgEXAMPLEPhvL6xEXAMPLE" }`For more information, see [Initiate Vault Lock (POST lock-policy)](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-InitiateVaultLock.html)in the*Amazon Glacier API Developer Guide*.- 
                    For API details, see [InitiateVaultLock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/initiate-vault-lock.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-jobs`.

- **AWS CLI**
- 
            
                    The following command lists in-progress and recently completed jobs for a vault named `my-vault`:`aws glacier list``-`jobs --account-id - --vault-name`my-vault`Output: `{ "JobList": [ { "VaultARN": "arn:aws:glacier:us-west-2:0123456789012:vaults/my-vault", "RetrievalByteRange": "0-3145727", "SNSTopic": "arn:aws:sns:us-west-2:0123456789012:my-vault", "Completed": false, "SHA256TreeHash": "9628195fcdbcbbe76cdde932d4646fa7de5f219fb39823836d81f0cc0e18aa67", "JobId": "l7IL5-EkXyEY9Ws95fClzIbk2O5uLYaFdAYOi-azsX_Z8V6NH4yERHzars8wTKYQMX6nBDI9cMNHzyZJO59-8N9aHWav", "ArchiveId": "kKB7ymWJVpPSwhGP6ycSOAekp9ZYe_--zM_mw6k76ZFGEIWQX-ybtRDvc2VkPSDtfKmQrj0IRQLSGsNuDp-AJVlu2ccmDSyDUmZwKbwbpAdGATGDiB3hHO0bjbGehXTcApVud_wyDw", "JobDescription": "Retrieve archive on 2015-07-17", "ArchiveSizeInBytes": 3145728, "Action": "ArchiveRetrieval", "ArchiveSHA256TreeHash": "9628195fcdbcbbe76cdde932d4646fa7de5f219fb39823836d81f0cc0e18aa67", "CreationDate": "2015-07-17T21:16:13.840Z", "StatusCode": "InProgress" }, { "InventoryRetrievalParameters": { "Format": "JSON" }, "VaultARN": "arn:aws:glacier:us-west-2:0123456789012:vaults/my-vault", "Completed": false, "JobId": "zbxcm3Z_3z5UkoroF7SuZKrxgGoDc3RloGduS7Eg-RO47Yc6FxsdGBgf_Q2DK5Ejh18CnTS5XW4_XqlNHS61dsO4CnMW", "Action": "InventoryRetrieval", "CreationDate": "2015-07-17T20:23:41.616Z", "StatusCode": ""InProgress"" } ] }`Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account. - 
                    For API details, see [ListJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/list-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-multipart-uploads`.

- **AWS CLI**
- 
            
                    The following command shows all of the in-progress multipart uploads for a vault named `my-vault`:`aws glacier list``-`multipart-uploads --account-id - --vault-name`my-vault`Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account. For more information on multipart uploads to Amazon Glacier using the AWS CLI, see Using Amazon Glacier in the *AWS CLI User Guide*.- 
                    For API details, see [ListMultipartUploads](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/list-multipart-uploads.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-parts`.

- **AWS CLI**
- 
            
                    The following command lists the uploaded parts for a multipart upload to a vault named `my-vault`:`aws glacier list``-`parts --account-id - --vault-name`my-vault`--upload-id`"SYZi7qnL-YGqGwAm8Kn3BLP2ElNCvnB-5961R09CSaPmPwkYGHOqeN_nX3-Vhnd2yF0KfB5FkmbnBU9GubbdrCs8ut-D"`Output: `{ "MultipartUploadId": "SYZi7qnL-YGqGwAm8Kn3BLP2ElNCvnB-5961R09CSaPmPwkYGHOqeN_nX3-Vhnd2yF0KfB5FkmbnBU9GubbdrCs8ut-D", "Parts": [ { "RangeInBytes": "0-1048575", "SHA256TreeHash": "e1f2a7cd6e047350f69b9f8cfa60fa606fe2f02802097a9a026360a7edc1f553" }, { "RangeInBytes": "1048576-2097151", "SHA256TreeHash": "43cf3061fb95796aed99a11a6aa3cd8f839eed15e655ab0a597126210636aee6" } ], "VaultARN": "arn:aws:glacier:us-west-2:0123456789012:vaults/my-vault", "CreationDate": "2015-07-18T00:05:23.830Z", "PartSizeInBytes": 1048576 }`Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account. For more information on multipart uploads to Amazon Glacier using the AWS CLI, see Using Amazon Glacier in the *AWS CLI User Guide*.- 
                    For API details, see [ListParts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/list-parts.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-provisioned-capacity`.

- **AWS CLI**
- 
            
                    **To retrieve the provisioned capacity units**The following `list-provisioned-capacity`example retrieves details for any provisioned capacity units for the specified account.`aws glacier list-provisioned-capacity \ --account-id``111122223333`Output: `{ "ProvisionedCapacityList": [ { "CapacityId": "HpASAuvfRFiVDbOjMfEIcr8K", "ExpirationDate": "2020-03-18T19:59:24.000Z", "StartDate": "2020-02-18T19:59:24.912Z" } ] }`- 
                    For API details, see [ListProvisionedCapacity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/list-provisioned-capacity.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-vault`.

- **AWS CLI**
- 
            
                    The following command lists the tags applied to a vault named `my-vault`:`aws glacier list``-`tags-for-vault --account-id - --vault-name`my-vault`Output: `{ "Tags": { "date": "july2015", "id": "1234" } }`Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account. - 
                    For API details, see [ListTagsForVault](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/list-tags-for-vault.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-vaults`.

- **AWS CLI**
- 
            
                    The following command lists the vaults in the default account and region: `aws glacier list``-`vaults --account-id -Output: `{ "VaultList": [ { "SizeInBytes": 3178496, "VaultARN": "arn:aws:glacier:us-west-2:0123456789012:vaults/my-vault", "LastInventoryDate": "2015-04-07T00:26:19.028Z", "VaultName": "my-vault", "NumberOfArchives": 1, "CreationDate": "2015-04-06T21:23:45.708Z" } ] }`Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account. - 
                    For API details, see [ListVaults](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/list-vaults.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `purchase-provisioned-capacity`.

- **AWS CLI**
- 
            
                    **To purchase a provisioned capacity unit**The following `purchase-provisioned-capacity`example purchases a provisioned capacity unit.`aws glacier purchase-provisioned-capacity \ --account-id``111122223333`Output: `{ "capacityId": "HpASAuvfRFiVDbOjMfEIcr8K" }`- 
                    For API details, see [PurchaseProvisionedCapacity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/purchase-provisioned-capacity.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-tags-from-vault`.

- **AWS CLI**
- 
            
                    The following command removes a tag with the key `date`from a vault named`my-vault`:`aws glacier remove``-`tags-from-vault --account-id - --vault-name`my-vault`--tag-keys`date`Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account. - 
                    For API details, see [RemoveTagsFromVault](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/remove-tags-from-vault.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-data-retrieval-policy`.

- **AWS CLI**
- 
            
                    The following command configures a data retrieval policy for the in-use account: `aws glacier set``-`data-retrieval-policy --account-id - --policy`file://data-retrieval-policy.json``data-retrieval-policy.json`is a JSON file in the current folder that specifies a data retrieval policy:`{ "Rules":[ { "Strategy":"BytesPerHour", "BytesPerHour":10737418240 } ] }`Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account. The following command sets the data retrieval policy to `FreeTier`using inline JSON:`aws glacier set``-`data-retrieval-policy --account-id - --policy '`{"Rules":[{"Strategy":"FreeTier"}]}`'See Set Data Retrieval Policy in the *Amazon Glacier API Reference*for details on the policy format.- 
                    For API details, see [SetDataRetrievalPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/set-data-retrieval-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-vault-access-policy`.

- **AWS CLI**
- 
            
                    **To set the access policy of a vault**The following `set-vault-access-policy`example attaches a permission policy to the specified vault.`aws glacier set-vault-access-policy \ --account-id``111122223333`\ --vault-name`example_vault`--policy '`{"Policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::444455556666:root\"},\"Action\":\"glacier:ListJobs\",\"Resource\":\"arn:aws:glacier:us-east-1:111122223333:vaults/example_vault\"},{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::444455556666:root\"},\"Action\":\"glacier:UploadArchive\",\"Resource\":\"arn:aws:glacier:us-east-1:111122223333:vaults/example_vault\"}]}"}`'This command produces no output. - 
                    For API details, see [SetVaultAccessPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/set-vault-access-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-vault-notifications`.

- **AWS CLI**
- 
            
                    The following command configures SNS notifications for a vault named `my-vault`:`aws glacier set``-`vault-notifications --account-id - --vault-name`my-vault`--vault-notification-config`file://notificationconfig.json``notificationconfig.json`is a JSON file in the current folder that specifies an SNS topic and the events to publish:`{ "SNSTopic": "arn:aws:sns:us-west-2:0123456789012:my-vault", "Events": ["ArchiveRetrievalCompleted", "InventoryRetrievalCompleted"] }`Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account. - 
                    For API details, see [SetVaultNotifications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/set-vault-notifications.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `upload-archive`.

- **AWS CLI**
- 
            
                    The following command uploads an archive in the current folder named `archive.zip`to a vault named`my-vault`:`aws glacier upload``-`archive --account-id - --vault-name`my-vault`--body`archive.zip`Output: `{ "archiveId": "kKB7ymWJVpPSwhGP6ycSOAekp9ZYe_--zM_mw6k76ZFGEIWQX-ybtRDvc2VkPSDtfKmQrj0IRQLSGsNuDp-AJVlu2ccmDSyDUmZwKbwbpAdGATGDiB3hHO0bjbGehXTcApVud_wyDw", "checksum": "969fb39823836d81f0cc028195fcdbcbbe76cdde932d4646fa7de5f21e18aa67", "location": "/0123456789012/vaults/my-vault/archives/kKB7ymWJVpPSwhGP6ycSOAekp9ZYe_--zM_mw6k76ZFGEIWQX-ybtRDvc2VkPSDtfKmQrj0IRQLSGsNuDp-AJVlu2ccmDSyDUmZwKbwbpAdGATGDiB3hHO0bjbGehXTcApVud_wyDw" }`Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account. To retrieve an uploaded archive, initiate a retrieval job with the aws glacier initiate-job command. - 
                    For API details, see [UploadArchive](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/upload-archive.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `upload-multipart-part`.

- **AWS CLI**
- 
            
                    The following command uploads the first 1 MiB (1024 x 1024 bytes) part of an archive: `aws glacier upload-multipart-part --body``part1`--range '`bytes 0-1048575/*`'`-`-account-id - --vault-name`my-vault`--upload-id`19gaRezEXAMPLES6Ry5YYdqthHOC_kGRCT03L9yetr220UmPtBYKk-OssZtLqyFu7sY1_lR7vgFuJV6NtcV5zpsJ`Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account. The body parameter takes a path to a part file on the local filesystem. The range parameter takes an HTTP content range indicating the bytes that the part occupies in the completed archive. The upload ID is returned by the `aws glacier initiate-multipart-upload`command and can also be obtained by using`aws glacier list-multipart-uploads`.For more information on multipart uploads to Amazon Glacier using the AWS CLI, see Using Amazon Glacier in the *AWS CLI User Guide*.- 
                    For API details, see [UploadMultipartPart](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/upload-multipart-part.html)in*AWS CLI Command Reference*.
 
-