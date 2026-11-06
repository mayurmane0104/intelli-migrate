# AWS Backup examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_backup_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_backup_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS Backup.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-backup-plan`.

- **AWS CLI**
- 
            
                    **To create a backup plan**The following `create-backup-plan`example creates the specified backup plan with a 35 day retention.`aws backup create-backup-plan \ --backup-plan "{\"BackupPlanName\":\"Example-Backup-Plan\",\"Rules\":[{\"RuleName\":\"DailyBackups\",\"ScheduleExpression\":\"cron(0 5 ? * * *)\",\"StartWindowMinutes\":480,\"TargetBackupVaultName\":\"Default\",\"Lifecycle\":{\"DeleteAfterDays\":35}}]}"`Output: `{ "BackupPlanId": "1fa3895c-a7f5-484a-a371-2dd6a1a9f729", "BackupPlanArn": "arn:aws:backup:us-west-2:123456789012:backup-plan:1fa3895c-a7f5-484a-a371-2dd6a1a9f729", "CreationDate": 1568928754.747, "VersionId": "ZjQ2ZTI5YWQtZDg5Yi00MzYzLWJmZTAtMDI1MzhlMDhjYjEz" }`For more information, see [Creating a Backup Plan](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup-plan.html)in the*AWS Backup Developer Guide*.- 
                    For API details, see [CreateBackupPlan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-backup-plan.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-backup-vault`.

- **AWS CLI**
- 
            
                    **To create a backup vault**The following `create-backup-vault`example creates a backup vault with the specified name.`aws backup create-backup-vault --backup-vault-name``sample-vault`This command produces no output. Output: `{ "BackupVaultName": "sample-vault", "BackupVaultArn": "arn:aws:backup:us-west-2:123456789012:backup-vault:sample-vault", "CreationDate": 1568928338.385 }`For more information, see [Creating a Backup Vault](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-vault.html)in the*AWS Backup Developer Guide*.- 
                    For API details, see [CreateBackupVault](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-backup-vault.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-backup-plan-from-template`.

- **AWS CLI**
- 
            
                    **To get an existing backup plan from a template**The following `get-backup-plan-from-template`example gets an existing backup plan from a template that specifies a daily backup with a 35 day retention.`aws backup get-backup-plan-from-template \ --backup-plan-template-id``"87c0c1ef-254d-4180-8fef-2e76a2c38aaa"`Output: `{ "BackupPlanDocument": { "Rules": [ { "RuleName": "DailyBackups", "ScheduleExpression": "cron(0 5 ? * * *)", "StartWindowMinutes": 480, "Lifecycle": { "DeleteAfterDays": 35 } } ] } }`For more information, see [Creating a Backup Plan](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup-plan.html)in the*AWS Backup Developer Guide*.- 
                    For API details, see [GetBackupPlanFromTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/get-backup-plan-from-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-backup-plan`.

- **AWS CLI**
- 
            
                    **To get the details of a backup plan**The following `get-backup-plan`example displays the details of the specified backup plan.`aws backup get-backup-plan \ --backup-plan-id``"fcbf5d8f-bd77-4f3a-9c97-f24fb3d373a5"`Output: `{ "BackupPlan": { "BackupPlanName": "Example-Backup-Plan", "Rules": [ { "RuleName": "DailyBackups", "TargetBackupVaultName": "Default", "ScheduleExpression": "cron(0 5 ? * * *)", "StartWindowMinutes": 480, "CompletionWindowMinutes": 10080, "Lifecycle": { "DeleteAfterDays": 35 }, "RuleId": "70e0ccdc-e9df-4e83-82ad-c1e5a9471cc3" } ] }, "BackupPlanId": "fcbf5d8f-bd77-4f3a-9c97-f24fb3d373a5", "BackupPlanArn": "arn:aws:backup:us-west-2:123456789012:backup-plan:fcbf5d8f-bd77-4f3a-9c97-f24fb3d373a5", "VersionId": "NjQ2ZTZkODktMGVhNy00MmQ0LWE4YjktZTkwNTQ3OTkyYTcw", "CreationDate": 1568926091.57 }`For more information, see [Creating a Backup Plan](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup-plan.html)in the*AWS Backup Developer Guide*.- 
                    For API details, see [GetBackupPlan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/get-backup-plan.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-backup-jobs`.

- **AWS CLI**
- 
            
                    **Example 1: To list all backup jobs**The following `list-backup-jobs`example returns metadata about your backup jobs in your AWS account.`aws backup list-backup-jobs`Output: `{ "BackupJobs": [ { "BackupJobId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "BackupVaultName": "Default", "BackupVaultArn": "arn:aws:backup:us-west-2:123456789012:backup-vault:Default", "ResourceArn": "arn:aws:ec2:us-west-2:123456789012:instance/i-12345678901234567", "CreationDate": 1600721892.929, "State": "CREATED", "PercentDone": "0.0", "IamRoleArn": "arn:aws:iam::123456789012:role/service-role/AWSBackupDefaultServiceRole", "StartBy": 1600725492.929, "ResourceType": "EC2" }, { "BackupJobId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "BackupVaultName": "Default", "BackupVaultArn": "arn:aws:backup:us-west-2:123456789012:backup-vault:Default", "RecoveryPointArn": "arn:aws:backup:us-west-2:123456789012:recovery-point:a1b2c3d4-5678-90ab-cdef-EXAMPLE33333", "ResourceArn": "arn:aws:elasticfilesystem:us-west-2:123456789012:file-system/fs-12345678", "CreationDate": 1600721724.77, "CompletionDate": 1600721744.488, "State": "COMPLETED", "PercentDone": "100.0", "BackupSizeInBytes": 71, "IamRoleArn": "arn:aws:iam::123456789012:role/service-role/AWSBackupDefaultServiceRole", "StartBy": 1600725324.77, "ResourceType": "EFS" } ] }`For more information, see [Creating a Backup](https://https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup.html)in the*AWS Backup Developer Guide*.**Example 2: To list completed backup jobs**The following `list-backup-jobs`example returns metadata about your completed backup jobs in your AWS account.`aws backup list-backup-jobs \ --by-state``COMPLETED`Output: `{ "BackupJobs": [ { "BackupJobId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "BackupVaultName": "Default", "BackupVaultArn": "arn:aws:backup:us-west-2:123456789012:backup-vault:Default", "RecoveryPointArn": "arn:aws:backup:us-west-2:123456789012:recovery-point:a1b2c3d4-5678-90ab-cdef-EXAMPLE33333", "ResourceArn": "arn:aws:elasticfilesystem:us-west-2:123456789012:file-system/fs-12345678", "CreationDate": 1600721724.77, "CompletionDate": 1600721744.488, "State": "COMPLETED", "PercentDone": "100.0", "BackupSizeInBytes": 71, "IamRoleArn": "arn:aws:iam::123456789012:role/service-role/AWSBackupDefaultServiceRole", "StartBy": 1600725324.77, "ResourceType": "EFS" } ] }`For more information, see [Creating a Backup](https://https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup.html)in the*AWS Backup Developer Guide*.- 
                    For API details, see [ListBackupJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-backup-jobs.html)in*AWS CLI Command Reference*.
 
-