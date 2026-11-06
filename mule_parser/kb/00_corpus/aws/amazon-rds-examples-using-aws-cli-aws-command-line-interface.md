# Amazon RDS examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_rds_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_rds_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon RDS.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `add-option-to-option-group`.

- **AWS CLI**
- 
            
                    **To add an option to an option group**The following `add-option-to-option-group`example adds an option to the specified option group.`aws rds add-option-to-option-group \ --option-group-name``myoptiongroup`\ --options`OptionName=OEM,Port=5500,DBSecurityGroupMemberships=default`\ --apply-immediatelyOutput: `{ "OptionGroup": { "OptionGroupName": "myoptiongroup", "OptionGroupDescription": "Test Option Group", "EngineName": "oracle-ee", "MajorEngineVersion": "12.1", "Options": [ { "OptionName": "Timezone", "OptionDescription": "Change time zone", "Persistent": true, "Permanent": false, "OptionSettings": [ { "Name": "TIME_ZONE", "Value": "Australia/Sydney", "DefaultValue": "UTC", "Description": "Specifies the timezone the user wants to change the system time to", "ApplyType": "DYNAMIC", "DataType": "STRING", "AllowedValues": "Africa/Cairo,Africa/Casablanca,Africa/Harare,Africa/Lagos,Africa/Luanda,Africa/Monrovia,Africa/Nairobi,Africa/Tripoli,Africa/Windhoek,America/Araguaina,America/Argentina/Buenos_Aires,America/Asuncion,America/Bogota,America/Caracas,America/Chicago,America/Chihuahua,America/Cuiaba,America/Denver,America/Detroit,America/Fortaleza,America/Godthab,America/Guatemala,America/Halifax,America/Lima,America/Los_Angeles,America/Manaus,America/Matamoros,America/Mexico_City,America/Monterrey,America/Montevideo,America/New_York,America/Phoenix,America/Santiago,America/Sao_Paulo,America/Tijuana,America/Toronto,Asia/Amman,Asia/Ashgabat,Asia/Baghdad,Asia/Baku,Asia/Bangkok,Asia/Beirut,Asia/Calcutta,Asia/Damascus,Asia/Dhaka,Asia/Hong_Kong,Asia/Irkutsk,Asia/Jakarta,Asia/Jerusalem,Asia/Kabul,Asia/Karachi,Asia/Kathmandu,Asia/Kolkata,Asia/Krasnoyarsk,Asia/Magadan,Asia/Manila,Asia/Muscat,Asia/Novosibirsk,Asia/Rangoon,Asia/Riyadh,Asia/Seoul,Asia/Shanghai,Asia/Singapore,Asia/Taipei,Asia/Tehran,Asia/Tokyo,Asia/Ulaanbaatar,Asia/Vladivostok,Asia/Yakutsk,Asia/Yerevan,Atlantic/Azores,Atlantic/Cape_Verde,Australia/Adelaide,Australia/Brisbane,Australia/Darwin,Australia/Eucla,Australia/Hobart,Australia/Lord_Howe,Australia/Perth,Australia/Sydney,Brazil/DeNoronha,Brazil/East,Canada/Newfoundland,Canada/Saskatchewan,Etc/GMT-3,Europe/Amsterdam,Europe/Athens,Europe/Berlin,Europe/Dublin,Europe/Helsinki,Europe/Kaliningrad,Europe/London,Europe/Madrid,Europe/Moscow,Europe/Paris,Europe/Prague,Europe/Rome,Europe/Sarajevo,Pacific/Apia,Pacific/Auckland,Pacific/Chatham,Pacific/Fiji,Pacific/Guam,Pacific/Honolulu,Pacific/Kiritimati,Pacific/Marquesas,Pacific/Samoa,Pacific/Tongatapu,Pacific/Wake,US/Alaska,US/Central,US/East-Indiana,US/Eastern,US/Pacific,UTC", "IsModifiable": true, "IsCollection": false } ], "DBSecurityGroupMemberships": [], "VpcSecurityGroupMemberships": [] }, { "OptionName": "OEM", "OptionDescription": "Oracle 12c EM Express", "Persistent": false, "Permanent": false, "Port": 5500, "OptionSettings": [], "DBSecurityGroupMemberships": [ { "DBSecurityGroupName": "default", "Status": "authorized" } ], "VpcSecurityGroupMemberships": [] } ], "AllowsVpcAndNonVpcInstanceMemberships": false, "OptionGroupArn": "arn:aws:rds:us-east-1:123456789012:og:myoptiongroup" } }`For more information, see [Adding an Option to an Option Group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.html#USER_WorkingWithOptionGroups.AddOption)in the*Amazon RDS User Guide*.- 
                    For API details, see [AddOptionToOptionGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/add-option-to-option-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `add-role-to-db-cluster`.

- **AWS CLI**
- 
            
                    **To associate an AWS Identity and Access Management (IAM) role with a DB cluster**The following `add-role-to-db-cluster`example associates a role with a DB cluster.`aws rds add-role-to-db-cluster \ --db-cluster-identifier``mydbcluster`\ --role-arn`arn:aws:iam::123456789012:role/RDSLoadFromS3`This command produces no output. For more information, see [Associating an IAM role with an Amazon Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Authorizing.IAM.AddRoleToDBCluster.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [AddRoleToDbCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/add-role-to-db-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `add-role-to-db-instance`.

- **AWS CLI**
- 
            
                    **To associate an AWS Identity and Access Management (IAM) role with a DB instance**The following `add-role-to-db-instance`example adds the role to an Oracle DB instance named`test-instance`.`aws rds add-role-to-db-instance \ --db-instance-identifier``test-instance`\ --feature-name`S3_INTEGRATION`\ --role-arn`arn:aws:iam::111122223333:role/rds-s3-integration-role`This command produces no output. For more information, see [Prerequisites for Amazon RDS Oracle Integration with Amazon S3](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-s3-integration.html#oracle-s3-integration.preparing)in the*Amazon RDS User Guide*.- 
                    For API details, see [AddRoleToDbInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/add-role-to-db-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `add-source-identifier-to-subscription`.

- **AWS CLI**
- 
            
                    **To add a source identifier to a subscription**The following `add-source-identifier`example adds another source identifier to an existing subscription.`aws rds add-source-identifier-to-subscription \ --subscription-name``my-instance-events`\ --source-identifier`test-instance-repl`Output: `{ "EventSubscription": { "SubscriptionCreationTime": "Tue Jul 31 23:22:01 UTC 2018", "CustSubscriptionId": "my-instance-events", "EventSubscriptionArn": "arn:aws:rds:us-east-1:123456789012:es:my-instance-events", "Enabled": false, "Status": "modifying", "EventCategoriesList": [ "backup", "recovery" ], "CustomerAwsId": "123456789012", "SnsTopicArn": "arn:aws:sns:us-east-1:123456789012:interesting-events", "SourceType": "db-instance", "SourceIdsList": [ "test-instance", "test-instance-repl" ] } }`- 
                    For API details, see [AddSourceIdentifierToSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/add-source-identifier-to-subscription.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `add-tags-to-resource`.

- **AWS CLI**
- 
            
                    **To add tags to a resource**The following `add-tags-to-resource`example add tags to an RDS database.`aws rds add-tags-to-resource \ --resource-name``arn:aws:rds:us-east-1:123456789012:db:database-mysql`\ --tags "[{\"Key\": \"Name\",\"Value\": \"MyDatabase\"},{\"Key\": \"Environment\",\"Value\": \"test\"}]"This command produces no output. For more information, see [Tagging Amazon RDS Resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [AddTagsToResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/add-tags-to-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `apply-pending-maintenance-action`.

- **AWS CLI**
- 
            
                    **To apply pending maintenance actions**The following `apply-pending-maintenance-action`example applies the pending maintenance actions for a DB cluster.`aws rds apply-pending-maintenance-action \ --resource-identifier``arn:aws:rds:us-east-1:123456789012:cluster:my-db-cluster`\ --apply-action`system-update`\ --opt-in-type`immediate`Output: `{ "ResourcePendingMaintenanceActions": { "ResourceIdentifier": "arn:aws:rds:us-east-1:123456789012:cluster:my-db-cluster", "PendingMaintenanceActionDetails": [ { "Action": "system-update", "OptInStatus": "immediate", "CurrentApplyDate": "2021-01-23T01:07:36.100Z", "Description": "Upgrade to Aurora PostgreSQL 3.3.2" } ] } }`For more information, see [Maintaining a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html)in the*Amazon RDS User Guide*and[Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [ApplyPendingMaintenanceAction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/apply-pending-maintenance-action.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `authorize-db-security-group-ingress`.

- **AWS CLI**
- 
            
                    **To associate an AWS Identity and Access Management (IAM) role with a DB instance**The following `authorize-db-security-group-ingress`example configures the default security group with an ingress rule for the CIDR IP range 192.0.2.0/24.`aws rds authorize-db-security-group-ingress \ --db-security-group-name``default`\ --cidrip`192.0.2.0/24`Output: `{ "DBSecurityGroup": { "OwnerId": "123456789012", "DBSecurityGroupName": "default", "DBSecurityGroupDescription": "default", "EC2SecurityGroups": [], "IPRanges": [ { "Status": "authorizing", "CIDRIP": "192.0.2.0/24" } ], "DBSecurityGroupArn": "arn:aws:rds:us-east-1:111122223333:secgrp:default" } }`For more information, see [Authorizing Network Access to a DB Security Group from an IP Range](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithSecurityGroups.html#USER_WorkingWithSecurityGroups.Authorizing)in the*Amazon RDS User Guide*.- 
                    For API details, see [AuthorizeDbSecurityGroupIngress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/authorize-db-security-group-ingress.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `backtrack-db-cluster`.

- **AWS CLI**
- 
            
                    **To backtrack an Aurora DB cluster**The following `backtrack-db-cluster`example backtracks the specified DB cluster sample-cluster to March 19, 2018, at 10 a.m.`aws rds backtrack-db-cluster --db-cluster-identifier``sample-cluster`--backtrack-to`2018-03-19T10:00:00+00:00`This command outputs a JSON block that acknowledges the change to the RDS resource. - 
                    For API details, see [BacktrackDbCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/backtrack-db-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-export-task`.

- **AWS CLI**
- 
            
                    **To cancel a snapshot export to Amazon S3**The following `cancel-export-task`example cancels an export task in progress that is exporting a snapshot to Amazon S3.`aws rds cancel-export-task \ --export-task-identifier``my-s3-export-1`Output: `{ "ExportTaskIdentifier": "my-s3-export-1", "SourceArn": "arn:aws:rds:us-east-1:123456789012:snapshot:publisher-final-snapshot", "SnapshotTime": "2019-03-24T20:01:09.815Z", "S3Bucket": "amzn-s3-demo-bucket", "S3Prefix": "", "IamRoleArn": "arn:aws:iam::123456789012:role/service-role/export-snap-S3-role", "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/abcd0000-7bfd-4594-af38-aabbccddeeff", "Status": "CANCELING", "PercentProgress": 0, "TotalExtractedDataInGB": 0 }`For more information, see [Canceling a snapshot export task](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ExportSnapshot.html#USER_ExportSnapshot.Canceling)in the*Amazon RDS User Guide*or[Canceling a snapshot export task](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_ExportSnapshot.html#USER_ExportSnapshot.Canceling)in the*Amazon Aurora User Guide*.- 
                    For API details, see [CancelExportTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/cancel-export-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `copy-db-cluster-parameter-group`.

- **AWS CLI**
- 
            
                    **To copy a DB cluster parameter group**The following `copy-db-cluster-parameter-group`example makes a copy of a DB cluster parameter group.`aws rds copy-db-cluster-parameter-group \ --source-db-cluster-parameter-group-identifier``mydbclusterpg`\ --target-db-cluster-parameter-group-identifier`mydbclusterpgcopy`\ --target-db-cluster-parameter-group-description`"Copy of mydbclusterpg parameter group"`Output: `{ "DBClusterParameterGroup": { "DBClusterParameterGroupName": "mydbclusterpgcopy", "DBClusterParameterGroupArn": "arn:aws:rds:us-east-1:123456789012:cluster-pg:mydbclusterpgcopy", "DBParameterGroupFamily": "aurora-mysql5.7", "Description": "Copy of mydbclusterpg parameter group" } }`For more information, see [Copying a DB Cluster Parameter Group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html#USER_WorkingWithParamGroups.CopyingCluster)in the*Amazon Aurora Users Guide*.- 
                    For API details, see [CopyDbClusterParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/copy-db-cluster-parameter-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `copy-db-cluster-snapshot`.

- **AWS CLI**
- 
            
                    **To copy a DB cluster snapshot**The following `copy-db-cluster-snapshot`example creates a copy of a DB cluster snapshot, including its tags.`aws rds copy-db-cluster-snapshot \ --source-db-cluster-snapshot-identifier``arn:aws:rds:us-east-1:123456789012:cluster-snapshot:rds:myaurora-2019-06-04-09-16`--target-db-cluster-snapshot-identifier`myclustersnapshotcopy`\ --copy-tagsOutput: `{ "DBClusterSnapshot": { "AvailabilityZones": [ "us-east-1a", "us-east-1b", "us-east-1e" ], "DBClusterSnapshotIdentifier": "myclustersnapshotcopy", "DBClusterIdentifier": "myaurora", "SnapshotCreateTime": "2019-06-04T09:16:42.649Z", "Engine": "aurora-mysql", "AllocatedStorage": 0, "Status": "available", "Port": 0, "VpcId": "vpc-6594f31c", "ClusterCreateTime": "2019-04-15T14:18:42.785Z", "MasterUsername": "myadmin", "EngineVersion": "5.7.mysql_aurora.2.04.2", "LicenseModel": "aurora-mysql", "SnapshotType": "manual", "PercentProgress": 100, "StorageEncrypted": true, "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/AKIAIOSFODNN7EXAMPLE", "DBClusterSnapshotArn": "arn:aws:rds:us-east-1:123456789012:cluster-snapshot:myclustersnapshotcopy", "IAMDatabaseAuthenticationEnabled": false } }`For more information, see [Copying a Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_CopySnapshot.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [CopyDbClusterSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/copy-db-cluster-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `copy-db-parameter-group`.

- **AWS CLI**
- 
            
                    **To copy a DB cluster parameter group**The following `copy-db-parameter-group`example makes a copy of a DB parameter group.`aws rds copy-db-parameter-group \ --source-db-parameter-group-identifier``mydbpg`\ --target-db-parameter-group-identifier`mydbpgcopy`\ --target-db-parameter-group-description`"Copy of mydbpg parameter group"`Output: `{ "DBParameterGroup": { "DBParameterGroupName": "mydbpgcopy", "DBParameterGroupArn": "arn:aws:rds:us-east-1:814387698303:pg:mydbpgcopy", "DBParameterGroupFamily": "mysql5.7", "Description": "Copy of mydbpg parameter group" } }`For more information, see [Copying a DB Parameter Group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html#USER_WorkingWithParamGroups.Copying)in the*Amazon RDS Users Guide*.- 
                    For API details, see [CopyDbParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/copy-db-parameter-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `copy-db-snapshot`.

- **AWS CLI**
- 
            
                    **To copy a DB snapshot**The following `copy-db-snapshot`example creates a copy of a DB snapshot.`aws rds copy-db-snapshot \ --source-db-snapshot-identifier``rds:database-mysql-2019-06-06-08-38`--target-db-snapshot-identifier`mydbsnapshotcopy`Output: `{ "DBSnapshot": { "VpcId": "vpc-6594f31c", "Status": "creating", "Encrypted": true, "SourceDBSnapshotIdentifier": "arn:aws:rds:us-east-1:123456789012:snapshot:rds:database-mysql-2019-06-06-08-38", "MasterUsername": "admin", "Iops": 1000, "Port": 3306, "LicenseModel": "general-public-license", "DBSnapshotArn": "arn:aws:rds:us-east-1:123456789012:snapshot:mydbsnapshotcopy", "EngineVersion": "5.6.40", "OptionGroupName": "default:mysql-5-6", "ProcessorFeatures": [], "Engine": "mysql", "StorageType": "io1", "DbiResourceId": "db-ZI7UJ5BLKMBYFGX7FDENCKADC4", "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/AKIAIOSFODNN7EXAMPLE", "SnapshotType": "manual", "IAMDatabaseAuthenticationEnabled": false, "SourceRegion": "us-east-1", "DBInstanceIdentifier": "database-mysql", "InstanceCreateTime": "2019-04-30T15:45:53.663Z", "AvailabilityZone": "us-east-1f", "PercentProgress": 0, "AllocatedStorage": 100, "DBSnapshotIdentifier": "mydbsnapshotcopy" } }`For more information, see [Copying a Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CopySnapshot.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [CopyDbSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/copy-db-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `copy-option-group`.

- **AWS CLI**
- 
            
                    **To copy an option group**The following `copy-option-group`example makes a copy of an option group.`aws rds copy-option-group \ --source-option-group-identifier``myoptiongroup`\ --target-option-group-identifier`new-option-group`\ --target-option-group-description`"My option group copy"`Output: `{ "OptionGroup": { "Options": [], "OptionGroupName": "new-option-group", "MajorEngineVersion": "11.2", "OptionGroupDescription": "My option group copy", "AllowsVpcAndNonVpcInstanceMemberships": true, "EngineName": "oracle-ee", "OptionGroupArn": "arn:aws:rds:us-east-1:123456789012:og:new-option-group" } }`For more information, see [Making a Copy of an Option Group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.html#USER_WorkingWithOptionGroups.Copy)in the*Amazon RDS User Guide*.- 
                    For API details, see [CopyOptionGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/copy-option-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-blue-green-deployment`.

- **AWS CLI**
- 
            
                    **Example 1: To create a blue/green deployment for an RDS for MySQL DB instance**The following `create-blue-green-deployment`example creates a blue/green deployment for a MySQL DB instance.`aws rds create-blue-green-deployment \ --blue-green-deployment-name``bgd-cli-test-instance`\ --source`arn:aws:rds:us-east-1:123456789012:db:my-db-instance`\ --target-engine-version`8.0`\ --target-db-parameter-group-name`mysql-80-group`Output: `{ "BlueGreenDeployment": { "BlueGreenDeploymentIdentifier": "bgd-v53303651eexfake", "BlueGreenDeploymentName": "bgd-cli-test-instance", "Source": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance", "SwitchoverDetails": [ { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-replica-1" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-replica-2" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-replica-3" } ], "Tasks": [ { "Name": "CREATING_READ_REPLICA_OF_SOURCE", "Status": "PENDING" }, { "Name": "DB_ENGINE_VERSION_UPGRADE", "Status": "PENDING" }, { "Name": "CONFIGURE_BACKUPS", "Status": "PENDING" }, { "Name": "CREATING_TOPOLOGY_OF_SOURCE", "Status": "PENDING" } ], "Status": "PROVISIONING", "CreateTime": "2022-02-25T21:18:51.183000+00:00" } }`For more information, see [Creating a blue/green deployment](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments-creating.html)in the*Amazon RDS User Guide*.**Example 2: To create a blue/green deployment for an Aurora MySQL DB cluster**The following `create-blue-green-deployment`example creates a blue/green deployment for an Aurora MySQL DB cluster.`aws rds create-blue-green-deployment \ --blue-green-deployment-name``my-blue-green-deployment`\ --source`arn:aws:rds:us-east-1:123456789012:cluster:my-aurora-mysql-cluster`\ --target-engine-version`8.0`\ --target-db-cluster-parameter-group-name`ams-80-binlog-enabled`\ --target-db-parameter-group-name`mysql-80-cluster-group`Output: `{ "BlueGreenDeployment": { "BlueGreenDeploymentIdentifier": "bgd-wi89nwzglccsfake", "BlueGreenDeploymentName": "my-blue-green-deployment", "Source": "arn:aws:rds:us-east-1:123456789012:cluster:my-aurora-mysql-cluster", "SwitchoverDetails": [ { "SourceMember": "arn:aws:rds:us-east-1:123456789012:cluster:my-aurora-mysql-cluster", "Status": "PROVISIONING" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-1", "Status": "PROVISIONING" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-2", "Status": "PROVISIONING" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-3", "Status": "PROVISIONING" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:cluster-endpoint:my-excluded-member-endpoint", "Status": "PROVISIONING" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:cluster-endpoint:my-reader-endpoint", "Status": "PROVISIONING" } ], "Tasks": [ { "Name": "CREATING_READ_REPLICA_OF_SOURCE", "Status": "PENDING" }, { "Name": "DB_ENGINE_VERSION_UPGRADE", "Status": "PENDING" }, { "Name": "CREATE_DB_INSTANCES_FOR_CLUSTER", "Status": "PENDING" }, { "Name": "CREATE_CUSTOM_ENDPOINTS", "Status": "PENDING" } ], "Status": "PROVISIONING", "CreateTime": "2022-02-25T21:12:00.288000+00:00" } }`For more information, see [Creating a blue/green deployment](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-creating.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [CreateBlueGreenDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-blue-green-deployment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-db-cluster-endpoint`.

- **AWS CLI**
- 
            
                    **To create a custom DB cluster endpoint**The following `create-db-cluster-endpoint`example creates a custom DB cluster endpoint and associate it with the specified Aurora DB cluster.`aws rds create-db-cluster-endpoint \ --db-cluster-endpoint-identifier``mycustomendpoint`\ --endpoint-type`reader`\ --db-cluster-identifier`mydbcluster`\ --static-members`dbinstance1``dbinstance2`Output: `{ "DBClusterEndpointIdentifier": "mycustomendpoint", "DBClusterIdentifier": "mydbcluster", "DBClusterEndpointResourceIdentifier": "cluster-endpoint-ANPAJ4AE5446DAEXAMPLE", "Endpoint": "mycustomendpoint.cluster-custom-cnpexample.us-east-1.rds.amazonaws.com", "Status": "creating", "EndpointType": "CUSTOM", "CustomEndpointType": "READER", "StaticMembers": [ "dbinstance1", "dbinstance2" ], "ExcludedMembers": [], "DBClusterEndpointArn": "arn:aws:rds:us-east-1:123456789012:cluster-endpoint:mycustomendpoint" }`For more information, see [Amazon Aurora Connection Management](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.Endpoints.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [CreateDbClusterEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-cluster-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-db-cluster-parameter-group`.

- **AWS CLI**
- 
            
                    **To create a DB cluster parameter group**The following `create-db-cluster-parameter-group`example creates a DB cluster parameter group.`aws rds create-db-cluster-parameter-group \ --db-cluster-parameter-group-name``mydbclusterparametergroup`\ --db-parameter-group-family`aurora5.6`\ --description`"My new cluster parameter group"`Output: `{ "DBClusterParameterGroup": { "DBClusterParameterGroupName": "mydbclusterparametergroup", "DBParameterGroupFamily": "aurora5.6", "Description": "My new cluster parameter group", "DBClusterParameterGroupArn": "arn:aws:rds:us-east-1:123456789012:cluster-pg:mydbclusterparametergroup" } }`For more information, see [Creating a DB Cluster Parameter Group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html#USER_WorkingWithParamGroups.CreatingCluster)in the*Amazon Aurora User Guide*.- 
                    For API details, see [CreateDbClusterParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-cluster-parameter-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-db-cluster-snapshot`.

- **AWS CLI**
- 
            
                    **To create a DB cluster snapshot**The following `create-db-cluster-snapshot`example creates a DB cluster snapshot.`aws rds create-db-cluster-snapshot \ --db-cluster-identifier``mydbcluster`\ --db-cluster-snapshot-identifier`mydbclustersnapshot`Output: `{ "DBClusterSnapshot": { "AvailabilityZones": [ "us-east-1a", "us-east-1b", "us-east-1e" ], "DBClusterSnapshotIdentifier": "mydbclustersnapshot", "DBClusterIdentifier": "mydbcluster", "SnapshotCreateTime": "2019-06-18T21:21:00.469Z", "Engine": "aurora-mysql", "AllocatedStorage": 1, "Status": "creating", "Port": 0, "VpcId": "vpc-6594f31c", "ClusterCreateTime": "2019-04-15T14:18:42.785Z", "MasterUsername": "myadmin", "EngineVersion": "5.7.mysql_aurora.2.04.2", "LicenseModel": "aurora-mysql", "SnapshotType": "manual", "PercentProgress": 0, "StorageEncrypted": true, "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/AKIAIOSFODNN7EXAMPLE", "DBClusterSnapshotArn": "arn:aws:rds:us-east-1:123456789012:cluster-snapshot:mydbclustersnapshot", "IAMDatabaseAuthenticationEnabled": false } }`For more information, see [Creating a DB Cluster Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_CreateSnapshotCluster.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [CreateDbClusterSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-cluster-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-db-cluster`.

- **AWS CLI**
- 
            
                    **Example 1: To create a MySQL 5.7--compatible DB cluster**The following `create-db-cluster`example creates a MySQL 5.7-compatible DB cluster using the default engine version. Replace the sample password`secret99`with a secure password. When you use the console to create a DB cluster, Amazon RDS automatically creates the writer DB instance for your DB cluster. However, when you use the AWS CLI to create a DB cluster, you must explicitly create the writer DB instance for your DB cluster using the`create-db-instance`AWS CLI command.`aws rds create-db-cluster \ --db-cluster-identifier``sample-cluster`\ --engine`aurora-mysql`\ --engine-version`5.7`\ --master-username`admin`\ --master-user-password`secret99`\ --db-subnet-group-name`default`\ --vpc-security-group-ids`sg-0b9130572daf3dc16`Output: `{ "DBCluster": { "DBSubnetGroup": "default", "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sg-0b9130572daf3dc16", "Status": "active" } ], "AllocatedStorage": 1, "AssociatedRoles": [], "PreferredBackupWindow": "09:12-09:42", "ClusterCreateTime": "2023-02-27T23:21:33.048Z", "DeletionProtection": false, "IAMDatabaseAuthenticationEnabled": false, "ReadReplicaIdentifiers": [], "EngineMode": "provisioned", "Engine": "aurora-mysql", "StorageEncrypted": false, "MultiAZ": false, "PreferredMaintenanceWindow": "mon:04:31-mon:05:01", "HttpEndpointEnabled": false, "BackupRetentionPeriod": 1, "DbClusterResourceId": "cluster-ANPAJ4AE5446DAEXAMPLE", "DBClusterIdentifier": "sample-cluster", "AvailabilityZones": [ "us-east-1a", "us-east-1b", "us-east-1e" ], "MasterUsername": "master", "EngineVersion": "5.7.mysql_aurora.2.11.1", "DBClusterArn": "arn:aws:rds:us-east-1:123456789012:cluster:sample-cluster", "DBClusterMembers": [], "Port": 3306, "Status": "creating", "Endpoint": "sample-cluster.cluster-cnpexample.us-east-1.rds.amazonaws.com", "DBClusterParameterGroup": "default.aurora-mysql5.7", "HostedZoneId": "Z2R2ITUGPM61AM", "ReaderEndpoint": "sample-cluster.cluster-ro-cnpexample.us-east-1.rds.amazonaws.com", "CopyTagsToSnapshot": false } }`**Example 2: To create a PostgreSQL--compatible DB cluster**The following `create-db-cluster`example creates a PostgreSQL-compatible DB cluster using the default engine version. Replace the example password`secret99`with a secure password. When you use the console to create a DB cluster, Amazon RDS automatically creates the writer DB instance for your DB cluster. However, when you use the AWS CLI to create a DB cluster, you must explicitly create the writer DB instance for your DB cluster using the`create-db-instance`AWS CLI command.`aws rds create-db-cluster \ --db-cluster-identifier``sample-pg-cluster`\ --engine`aurora-postgresql`\ --`master`-username master \ --master-user-password`secret99`\ --db-subnet-group-name`default`\ --vpc-security-group-ids`sg-0b9130572daf3dc16`Output: `{ "DBCluster": { "Endpoint": "sample-pg-cluster.cluster-cnpexample.us-east-1.rds.amazonaws.com", "HttpEndpointEnabled": false, "DBClusterMembers": [], "EngineMode": "provisioned", "CopyTagsToSnapshot": false, "HostedZoneId": "Z2R2ITUGPM61AM", "IAMDatabaseAuthenticationEnabled": false, "AllocatedStorage": 1, "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sg-0b9130572daf3dc16", "Status": "active" } ], "DeletionProtection": false, "StorageEncrypted": false, "BackupRetentionPeriod": 1, "PreferredBackupWindow": "09:56-10:26", "ClusterCreateTime": "2023-02-27T23:26:08.371Z", "DBClusterParameterGroup": "default.aurora-postgresql13", "EngineVersion": "13.7", "Engine": "aurora-postgresql", "Status": "creating", "DBClusterIdentifier": "sample-pg-cluster", "MultiAZ": false, "Port": 5432, "DBClusterArn": "arn:aws:rds:us-east-1:123456789012:cluster:sample-pg-cluster", "AssociatedRoles": [], "DbClusterResourceId": "cluster-ANPAJ4AE5446DAEXAMPLE", "PreferredMaintenanceWindow": "wed:03:33-wed:04:03", "ReaderEndpoint": "sample-pg-cluster.cluster-ro-cnpexample.us-east-1.rds.amazonaws.com", "MasterUsername": "master", "AvailabilityZones": [ "us-east-1a", "us-east-1b", "us-east-1c" ], "ReadReplicaIdentifiers": [], "DBSubnetGroup": "default" } }`**Example 3: To create an Aurora PostgreSQL DB cluster with Express Configuration**The following `create-db-cluster`example creates an Aurora PostgreSQL-compatible DB cluster with Express Configuration enabled. Unlike the standard create cluster, Express Configuration automatically adds a DB instance`sample-cluster-instance-1`for your DB cluster, so you don't need to separately call the`create-db-instance`AWS CLI command.`aws rds create-db-cluster \ --db-cluster-identifier``sample-cluster`\ --engine`aurora-postgresql`\ --with-express-configurationOutput: `{ "DBCluster": { "AllocatedStorage": 1, "AvailabilityZones": [ "us-east-1c", "us-east-1a", "us-east-1b" ], "BackupRetentionPeriod": 7, "DBClusterIdentifier": "sample-cluster", "DBClusterParameterGroup": "default.aurora-postgresql17", "Status": "creating", "MultiAZ": false, "Engine": "aurora-postgresql", "EngineVersion": "17.7", "Port": 5432, "MasterUsername": "postgres", "PreferredBackupWindow": "06:15-06:45", "PreferredMaintenanceWindow": "sat:03:44-sat:04:14", "ReadReplicaIdentifiers": [], "DBClusterMembers": [ { "DBInstanceIdentifier": "sample-cluster-instance-1", "IsClusterWriter": false, "DBClusterParameterGroupStatus": "in-sync", "PromotionTier": 1 } ], "VpcSecurityGroups": [], "StorageEncrypted": false, "DbClusterResourceId": "cluster-EXAMPLE4RESOURCE", "DBClusterArn": "arn:aws:rds:us-east-1:123456789012:cluster:sample-cluster", "AssociatedRoles": [], "IAMDatabaseAuthenticationEnabled": true, "ClusterCreateTime": "2026-01-10T22:14:02Z", "EngineMode": "provisioned", "AutoMinorVersionUpgrade": true, "DeletionProtection": false, "HttpEndpointEnabled": false, "CopyTagsToSnapshot": false, "CrossAccountClone": false, "DomainMemberships": [], "TagList": [], "ServerlessV2ScalingConfiguration": { "MinCapacity": 0.0, "MaxCapacity": 16.0, "SecondsUntilAutoPause": 300 }, "ServerlessV2PlatformVersion": "3", "DatabaseInsightsMode": "standard", "PerformanceInsightsEnabled": false, "LocalWriteForwardingStatus": "disabled", "EngineLifecycleSupport": "open-source-rds-extended-support" } }`For more information, see [Creating an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.CreateInstance.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [CreateDbCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-db-instance-read-replica`.

- **AWS CLI**
- 
            
                    **To create a DB instance read replica**This example creates a read replica of an existing DB instance named `test-instance`. The read replica is named`test-instance-repl`.`aws rds create-db-instance-read-replica \ --db-instance-identifier``test-instance-repl`\ --source-db-instance-identifier`test-instance`Output: `{ "DBInstance": { "IAMDatabaseAuthenticationEnabled": false, "MonitoringInterval": 0, "DBInstanceArn": "arn:aws:rds:us-east-1:123456789012:db:test-instance-repl", "ReadReplicaSourceDBInstanceIdentifier": "test-instance", "DBInstanceIdentifier": "test-instance-repl", ...some output truncated... } }`- 
                    For API details, see [CreateDbInstanceReadReplica](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-instance-read-replica.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-db-instance`.

- **AWS CLI**
- 
            
                    **To create a DB instance**The following `create-db-instance`example uses the required options to launch a new DB instance.`aws rds create-db-instance \ --db-instance-identifier``test-mysql-instance`\ --db-instance-class`db.t3.micro`\ --engine`mysql`\ --master-username`admin`\ --master-user-password`secret99`\ --allocated-storage`20`Output: `{ "DBInstance": { "DBInstanceIdentifier": "test-mysql-instance", "DBInstanceClass": "db.t3.micro", "Engine": "mysql", "DBInstanceStatus": "creating", "MasterUsername": "admin", "AllocatedStorage": 20, "PreferredBackupWindow": "12:55-13:25", "BackupRetentionPeriod": 1, "DBSecurityGroups": [], "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sg-12345abc", "Status": "active" } ], "DBParameterGroups": [ { "DBParameterGroupName": "default.mysql5.7", "ParameterApplyStatus": "in-sync" } ], "DBSubnetGroup": { "DBSubnetGroupName": "default", "DBSubnetGroupDescription": "default", "VpcId": "vpc-2ff2ff2f", "SubnetGroupStatus": "Complete", "Subnets": [ { "SubnetIdentifier": "subnet-########", "SubnetAvailabilityZone": { "Name": "us-west-2c" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-########", "SubnetAvailabilityZone": { "Name": "us-west-2d" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-########", "SubnetAvailabilityZone": { "Name": "us-west-2a" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-########", "SubnetAvailabilityZone": { "Name": "us-west-2b" }, "SubnetStatus": "Active" } ] }, "PreferredMaintenanceWindow": "sun:08:07-sun:08:37", "PendingModifiedValues": { "MasterUserPassword": "****" }, "MultiAZ": false, "EngineVersion": "5.7.22", "AutoMinorVersionUpgrade": true, "ReadReplicaDBInstanceIdentifiers": [], "LicenseModel": "general-public-license", "OptionGroupMemberships": [ { "OptionGroupName": "default:mysql-5-7", "Status": "in-sync" } ], "PubliclyAccessible": true, "StorageType": "gp2", "DbInstancePort": 0, "StorageEncrypted": false, "DbiResourceId": "db-5555EXAMPLE44444444EXAMPLE", "CACertificateIdentifier": "rds-ca-2019", "DomainMemberships": [], "CopyTagsToSnapshot": false, "MonitoringInterval": 0, "DBInstanceArn": "arn:aws:rds:us-west-2:123456789012:db:test-mysql-instance", "IAMDatabaseAuthenticationEnabled": false, "PerformanceInsightsEnabled": false, "DeletionProtection": false, "AssociatedRoles": [] } }`For more information, see [Creating an Amazon RDS DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [CreateDBInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-db-parameter-group`.

- **AWS CLI**
- 
            
                    **To create a DB parameter group**The following `create-db-parameter-group`example creates a DB parameter group.`aws rds create-db-parameter-group \ --db-parameter-group-name``mydbparametergroup`\ --db-parameter-group-family`MySQL5.6`\ --description`"My new parameter group"`Output: `{ "DBParameterGroup": { "DBParameterGroupName": "mydbparametergroup", "DBParameterGroupFamily": "mysql5.6", "Description": "My new parameter group", "DBParameterGroupArn": "arn:aws:rds:us-east-1:123456789012:pg:mydbparametergroup" } }`For more information, see [Creating a DB Parameter Group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html#USER_WorkingWithParamGroups.Creating)in the*Amazon RDS User Guide*.- 
                    For API details, see [CreateDBParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-parameter-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-db-proxy-endpoint`.

- **AWS CLI**
- 
            
                    **To create a DB proxy endpoint for an RDS database**The following `create-db-proxy-endpoint`example creates a DB proxy endpoint.`aws rds create-db-proxy-endpoint \ --db-proxy-name``proxyExample`\ --db-proxy-endpoint-name`"proxyep1"`\ --vpc-subnet-ids`subnetgroup1``subnetgroup2`Output: `{ "DBProxyEndpoint": { "DBProxyEndpointName": "proxyep1", "DBProxyEndpointArn": "arn:aws:rds:us-east-1:123456789012:db-proxy-endpoint:prx-endpoint-0123a01b12345c0ab", "DBProxyName": "proxyExample", "Status": "creating", "VpcId": "vpc-1234567", "VpcSecurityGroupIds": [ "sg-1234", "sg-5678" ], "VpcSubnetIds": [ "subnetgroup1", "subnetgroup2" ], "Endpoint": "proxyep1.endpoint.proxy-ab0cd1efghij.us-east-1.rds.amazonaws.com", "CreatedDate": "2023-04-05T16:09:33.452000+00:00", "TargetRole": "READ_WRITE", "IsDefault": false } }`For more information, see [Creating a proxy endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-endpoints.html#rds-proxy-endpoints.CreatingEndpoint)in the*Amazon RDS User Guide*and[Creating a proxy endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-endpoints.html#rds-proxy-endpoints.CreatingEndpoint)in the*Amazon Aurora User Guide*.- 
                    For API details, see [CreateDbProxyEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-proxy-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-db-proxy`.

- **AWS CLI**
- 
            
                    **To create a DB proxy for an RDS database**The following `create-db-proxy`example creates a DB proxy.`aws rds create-db-proxy \ --db-proxy-name``proxyExample`\ --engine-family`MYSQL`\ --auth Description="proxydescription1",AuthScheme="SECRETS",SecretArn="arn:aws:secretsmanager:us-west-2:123456789123:secret:secretName-1234f",IAMAuth="DISABLED",ClientPasswordAuthType="MYSQL_NATIVE_PASSWORD" \ --role-arn`arn:aws:iam::123456789123:role/ProxyRole`\ --vpc-subnet-ids`subnetgroup1``subnetgroup2`Output: `{ "DBProxy": { "DBProxyName": "proxyExample", "DBProxyArn": "arn:aws:rds:us-east-1:123456789012:db-proxy:prx-0123a01b12345c0ab", "EngineFamily": "MYSQL", "VpcId": "vpc-1234567", "VpcSecuritytGroupIds": [ "sg-1234", "sg-5678", "sg-9101" ], "VpcSubnetIds": [ "subnetgroup1", "subnetgroup2" ], "Auth": "[ { "Description": "proxydescription1", "AuthScheme": "SECRETS", "SecretArn": "arn:aws:secretsmanager:us-west-2:123456789123:secret:proxysecret1-Abcd1e", "IAMAuth": "DISABLED" } ]", "RoleArn": "arn:aws:iam::12345678912:role/ProxyRole", "Endpoint": "proxyExample.proxy-ab0cd1efghij.us-east-1.rds.amazonaws.com", "RequireTLS": false, "IdleClientTimeout": 1800, "DebuggingLogging": false, "CreatedDate": "2023-04-05T16:09:33.452000+00:00", "UpdatedDate": "2023-04-13T01:49:38.568000+00:00" } }`For more information, see [Creating an RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-setup.html#rds-proxy-creating)in the*Amazon RDS User Guide*and[Creating an RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-setup.html#rds-proxy-creating)in the*Amazon Aurora User Guide*.- 
                    For API details, see [CreateDbProxy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-proxy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-db-security-group`.

- **AWS CLI**
- 
            
                    **To create an Amazon RDS DB security group**The following `create-db-security-group`command creates a new Amazon RDS DB security group:`aws rds create-db-security-group --db-security-group-name``mysecgroup`--db-security-group-description`"My Test Security Group"`In the example, the new DB security group is named `mysecgroup`and has a description.Output: `{ "DBSecurityGroup": { "OwnerId": "123456789012", "DBSecurityGroupName": "mysecgroup", "DBSecurityGroupDescription": "My Test Security Group", "VpcId": "vpc-a1b2c3d4", "EC2SecurityGroups": [], "IPRanges": [], "DBSecurityGroupArn": "arn:aws:rds:us-west-2:123456789012:secgrp:mysecgroup" } }`- 
                    For API details, see [CreateDbSecurityGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-security-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-db-shard-group`.

- **AWS CLI**
- 
            
                    **Example 1: To create an Aurora PostgreSQL primary DB cluster**The following `create-db-cluster`example creates an Aurora PostgreSQL SQL primary DB cluster that's compatible with Aurora Serverless v2 and Aurora Limitless Database.`aws rds create-db-cluster \ --db-cluster-identifier``my-sv2-cluster`\ --engine`aurora-postgresql`\ --engine-version`15.2-limitless`\ --storage-type`aurora-iopt1`\ --serverless-v2-scaling-configuration`MinCapacity=2,MaxCapacity=16`\ --enable-limitless-database \ --master-username`myuser`\ --master-user-password`mypassword`\ --enable-cloudwatch-logs-exports`postgresql`Output: `{ "DBCluster": { "AllocatedStorage": 1, "AvailabilityZones": [ "us-east-2b", "us-east-2c", "us-east-2a" ], "BackupRetentionPeriod": 1, "DBClusterIdentifier": "my-sv2-cluster", "DBClusterParameterGroup": "default.aurora-postgresql15", "DBSubnetGroup": "default", "Status": "creating", "Endpoint": "my-sv2-cluster.cluster-cekycexample.us-east-2.rds.amazonaws.com", "ReaderEndpoint": "my-sv2-cluster.cluster-ro-cekycexample.us-east-2.rds.amazonaws.com", "MultiAZ": false, "Engine": "aurora-postgresql", "EngineVersion": "15.2-limitless", "Port": 5432, "MasterUsername": "myuser", "PreferredBackupWindow": "06:05-06:35", "PreferredMaintenanceWindow": "mon:08:25-mon:08:55", "ReadReplicaIdentifiers": [], "DBClusterMembers": [], "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sg-########", "Status": "active" } ], "HostedZoneId": "Z2XHWR1EXAMPLE", "StorageEncrypted": false, "DbClusterResourceId": "cluster-XYEDT6ML6FHIXH4Q2J1EXAMPLE", "DBClusterArn": "arn:aws:rds:us-east-2:123456789012:cluster:my-sv2-cluster", "AssociatedRoles": [], "IAMDatabaseAuthenticationEnabled": false, "ClusterCreateTime": "2024-02-19T16:24:07.771000+00:00", "EnabledCloudwatchLogsExports": [ "postgresql" ], "EngineMode": "provisioned", "DeletionProtection": false, "HttpEndpointEnabled": false, "CopyTagsToSnapshot": false, "CrossAccountClone": false, "DomainMemberships": [], "TagList": [], "StorageType": "aurora-iopt1", "AutoMinorVersionUpgrade": true, "ServerlessV2ScalingConfiguration": { "MinCapacity": 2.0, "MaxCapacity": 16.0 }, "NetworkType": "IPV4", "IOOptimizedNextAllowedModificationTime": "2024-03-21T16:24:07.781000+00:00", "LimitlessDatabase": { "Status": "not-in-use", "MinRequiredACU": 96.0 } } }`**Example 2: To create the primary (writer) DB instance**The following `create-db-instance`example creates an Aurora Serverless v2 primary (writer) DB instance. When you use the console to create a DB cluster, Amazon RDS automatically creates the writer DB instance for your DB cluster. However, when you use the AWS CLI to create a DB cluster, you must explicitly create the writer DB instance for your DB cluster using the`create-db-instance`AWS CLI command.`aws rds create-db-instance \ --db-instance-identifier``my-sv2-instance`\ --db-cluster-identifier`my-sv2-cluster`\ --engine`aurora-postgresql`\ --db-instance-class`db.serverless`Output: `{ "DBInstance": { "DBInstanceIdentifier": "my-sv2-instance", "DBInstanceClass": "db.serverless", "Engine": "aurora-postgresql", "DBInstanceStatus": "creating", "MasterUsername": "myuser", "AllocatedStorage": 1, "PreferredBackupWindow": "06:05-06:35", "BackupRetentionPeriod": 1, "DBSecurityGroups": [], "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sg-########", "Status": "active" } ], "DBParameterGroups": [ { "DBParameterGroupName": "default.aurora-postgresql15", "ParameterApplyStatus": "in-sync" } ], "DBSubnetGroup": { "DBSubnetGroupName": "default", "DBSubnetGroupDescription": "default", "VpcId": "vpc-########", "SubnetGroupStatus": "Complete", "Subnets": [ { "SubnetIdentifier": "subnet-########", "SubnetAvailabilityZone": { "Name": "us-east-2c" }, "SubnetOutpost": {}, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-########", "SubnetAvailabilityZone": { "Name": "us-east-2a" }, "SubnetOutpost": {}, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-########", "SubnetAvailabilityZone": { "Name": "us-east-2b" }, "SubnetOutpost": {}, "SubnetStatus": "Active" } ] }, "PreferredMaintenanceWindow": "fri:09:01-fri:09:31", "PendingModifiedValues": { "PendingCloudwatchLogsExports": { "LogTypesToEnable": [ "postgresql" ] } }, "MultiAZ": false, "EngineVersion": "15.2-limitless", "AutoMinorVersionUpgrade": true, "ReadReplicaDBInstanceIdentifiers": [], "LicenseModel": "postgresql-license", "OptionGroupMemberships": [ { "OptionGroupName": "default:aurora-postgresql-15", "Status": "in-sync" } ], "PubliclyAccessible": false, "StorageType": "aurora-iopt1", "DbInstancePort": 0, "DBClusterIdentifier": "my-sv2-cluster", "StorageEncrypted": false, "DbiResourceId": "db-BIQTE3B3K3RM7M74SK5EXAMPLE", "CACertificateIdentifier": "rds-ca-rsa2048-g1", "DomainMemberships": [], "CopyTagsToSnapshot": false, "MonitoringInterval": 0, "PromotionTier": 1, "DBInstanceArn": "arn:aws:rds:us-east-2:123456789012:db:my-sv2-instance", "IAMDatabaseAuthenticationEnabled": false, "PerformanceInsightsEnabled": false, "DeletionProtection": false, "AssociatedRoles": [], "TagList": [], "CustomerOwnedIpEnabled": false, "BackupTarget": "region", "NetworkType": "IPV4", "StorageThroughput": 0, "CertificateDetails": { "CAIdentifier": "rds-ca-rsa2048-g1" }, "DedicatedLogVolume": false } }`**Example 3: To create the DB shard group**The following `create-db-shard-group`example creates a DB shard group in your Aurora PostgreSQL primary DB cluster.`aws rds create-db-shard-group \ --db-shard-group-identifier``my-db-shard-group`\ --db-cluster-identifier`my-sv2-cluster`\ --max-acu`768`Output: `{ "DBShardGroupResourceId": "shardgroup-a6e3a0226aa243e2ac6c7a1234567890", "DBShardGroupIdentifier": "my-db-shard-group", "DBClusterIdentifier": "my-sv2-cluster", "MaxACU": 768.0, "ComputeRedundancy": 0, "Status": "creating", "PubliclyAccessible": false, "Endpoint": "my-sv2-cluster.limitless-cekycexample.us-east-2.rds.amazonaws.com" }`For more information, see [Using Aurora Serverless v2](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [CreateDbShardGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-shard-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-db-snapshot`.

- **AWS CLI**
- 
            
                    **To create a DB snapshot**The following `create-db-snapshot`example creates a DB snapshot.`aws rds create-db-snapshot \ --db-instance-identifier``database-mysql`\ --db-snapshot-identifier`mydbsnapshot`Output: `{ "DBSnapshot": { "DBSnapshotIdentifier": "mydbsnapshot", "DBInstanceIdentifier": "database-mysql", "Engine": "mysql", "AllocatedStorage": 100, "Status": "creating", "Port": 3306, "AvailabilityZone": "us-east-1b", "VpcId": "vpc-6594f31c", "InstanceCreateTime": "2019-04-30T15:45:53.663Z", "MasterUsername": "admin", "EngineVersion": "5.6.40", "LicenseModel": "general-public-license", "SnapshotType": "manual", "Iops": 1000, "OptionGroupName": "default:mysql-5-6", "PercentProgress": 0, "StorageType": "io1", "Encrypted": true, "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/AKIAIOSFODNN7EXAMPLE", "DBSnapshotArn": "arn:aws:rds:us-east-1:123456789012:snapshot:mydbsnapshot", "IAMDatabaseAuthenticationEnabled": false, "ProcessorFeatures": [], "DbiResourceId": "db-AKIAIOSFODNN7EXAMPLE" } }`For more information, see [Creating a DB Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateSnapshot.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [CreateDBSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-db-subnet-group`.

- **AWS CLI**
- 
            
                    **To create a DB subnet group**The following `create-db-subnet-group`example creates a DB subnet group called`mysubnetgroup`using existing subnets.`aws rds create-db-subnet-group \ --db-subnet-group-name``mysubnetgroup`\ --db-subnet-group-description`"test DB subnet group"`\ --subnet-ids '`["subnet-0a1dc4e1a6f123456","subnet-070dd7ecb3aaaaaaa","subnet-00f5b198bc0abcdef"]`'Output: `{ "DBSubnetGroup": { "DBSubnetGroupName": "mysubnetgroup", "DBSubnetGroupDescription": "test DB subnet group", "VpcId": "vpc-0f08e7610a1b2c3d4", "SubnetGroupStatus": "Complete", "Subnets": [ { "SubnetIdentifier": "subnet-070dd7ecb3aaaaaaa", "SubnetAvailabilityZone": { "Name": "us-west-2b" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-00f5b198bc0abcdef", "SubnetAvailabilityZone": { "Name": "us-west-2d" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-0a1dc4e1a6f123456", "SubnetAvailabilityZone": { "Name": "us-west-2b" }, "SubnetStatus": "Active" } ], "DBSubnetGroupArn": "arn:aws:rds:us-west-2:0123456789012:subgrp:mysubnetgroup" } }`For more information, see [Creating a DB Instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.InstanceInVPC)in the*Amazon RDS User Guide*.- 
                    For API details, see [CreateDbSubnetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-db-subnet-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-event-subscription`.

- **AWS CLI**
- 
            
                    **To create an event subscription**The following `create-event-subscription`example creates a subscription for backup and recovery events for DB instances in the current AWS account. Notifications are sent to an Amazon Simple Notification Service topic, specified by`--sns-topic-arn`.`aws rds create-event-subscription \ --subscription-name``my-instance-events`\ --source-type`db-instance`\ --event-categories '`["backup","recovery"]`' \ --sns-topic-arn`arn:aws:sns:us-east-1:123456789012:interesting-events`Output: `{ "EventSubscription": { "Status": "creating", "CustSubscriptionId": "my-instance-events", "SubscriptionCreationTime": "Tue Jul 31 23:22:01 UTC 2018", "EventCategoriesList": [ "backup", "recovery" ], "SnsTopicArn": "arn:aws:sns:us-east-1:123456789012:interesting-events", "CustomerAwsId": "123456789012", "EventSubscriptionArn": "arn:aws:rds:us-east-1:123456789012:es:my-instance-events", "SourceType": "db-instance", "Enabled": true } }`- 
                    For API details, see [CreateEventSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-event-subscription.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-global-cluster`.

- **AWS CLI**
- 
            
                    **To create a global DB cluster**The following `create-global-cluster`example creates a new Aurora MySQL-compatible global DB cluster.`aws rds create-global-cluster \ --global-cluster-identifier``myglobalcluster`\ --engine`aurora-mysql`Output: `{ "GlobalCluster": { "GlobalClusterIdentifier": "myglobalcluster", "GlobalClusterResourceId": "cluster-f0e523bfe07aabb", "GlobalClusterArn": "arn:aws:rds::123456789012:global-cluster:myglobalcluster", "Status": "available", "Engine": "aurora-mysql", "EngineVersion": "5.7.mysql_aurora.2.07.2", "StorageEncrypted": false, "DeletionProtection": false, "GlobalClusterMembers": [] } }`For more information, see [Creating an Aurora global database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-getting-started.html#aurora-global-database-creating)in the*Amazon Aurora User Guide*.- 
                    For API details, see [CreateGlobalCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-global-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-option-group`.

- **AWS CLI**
- 
            
                    **To Create an Amazon RDS option group**The following `create-option-group`command creates a new Amazon RDS option group for`Oracle Enterprise Edition`version`11.2`, is named ``MyOptionGroup`and includes a description.`aws rds create-option-group \ --option-group-name``MyOptionGroup`\ --engine-name`oracle-ee`\ --major-engine-version`11.2`\ --option-group-description`"Oracle Database Manager Database Control"`Output: `{ "OptionGroup": { "OptionGroupName": "myoptiongroup", "OptionGroupDescription": "Oracle Database Manager Database Control", "EngineName": "oracle-ee", "MajorEngineVersion": "11.2", "Options": [], "AllowsVpcAndNonVpcInstanceMemberships": true, "OptionGroupArn": "arn:aws:rds:us-west-2:123456789012:og:myoptiongroup" } }`- 
                    For API details, see [CreateOptionGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/create-option-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-blue-green-deployment`.

- **AWS CLI**
- 
            
                    **Example 1: To delete resources in green environment for an RDS for MySQL DB instance**The following `delete-blue-green-deployment`example deletes the resources in a green environment for an RDS for MySQL DB instance.`aws rds delete-blue-green-deployment \ --blue-green-deployment-identifier``bgd-v53303651eexfake`\ --delete-targetOutput: `{ "BlueGreenDeployment": { "BlueGreenDeploymentIdentifier": "bgd-v53303651eexfake", "BlueGreenDeploymentName": "bgd-cli-test-instance", "Source": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance", "Target": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-green-rkfbpe", "SwitchoverDetails": [ { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-green-rkfbpe", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-replica-1", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-replica-1-green-j382ha", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-replica-2", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-replica-2-green-ejv4ao", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-replica-3", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-replica-3-green-vlpz3t", "Status": "AVAILABLE" } ], "Tasks": [ { "Name": "CREATING_READ_REPLICA_OF_SOURCE", "Status": "COMPLETED" }, { "Name": "DB_ENGINE_VERSION_UPGRADE", "Status": "COMPLETED" }, { "Name": "CONFIGURE_BACKUPS", "Status": "COMPLETED" }, { "Name": "CREATING_TOPOLOGY_OF_SOURCE", "Status": "COMPLETED" } ], "Status": "DELETING", "CreateTime": "2022-02-25T21:18:51.183000+00:00", "DeleteTime": "2022-02-25T22:25:31.331000+00:00" } }`For more information, see [Deleting a blue/green deployment](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments-deleting.html)in the*Amazon RDS User Guide*.**Example 2: To delete resources in green environment for an Aurora MySQL DB cluster**The following `delete-blue-green-deployment`example deletes the resources in a green environment for an Aurora MySQL DB cluster.`aws rds delete-blue-green-deployment \ --blue-green-deployment-identifier``bgd-wi89nwzglccsfake`\ --delete-targetOutput: `{ "BlueGreenDeployment": { "BlueGreenDeploymentIdentifier": "bgd-wi89nwzglccsfake", "BlueGreenDeploymentName": "my-blue-green-deployment", "Source": "arn:aws:rds:us-east-1:123456789012:cluster:my-aurora-mysql-cluster", "Target": "arn:aws:rds:us-east-1:123456789012:cluster:my-aurora-mysql-cluster-green-3rnukl", "SwitchoverDetails": [ { "SourceMember": "arn:aws:rds:us-east-1:123456789012:cluster:my-aurora-mysql-cluster", "TargetMember": "arn:aws:rds:us-east-1:123456789012:cluster:my-aurora-mysql-cluster-green-3rnukl", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-1", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-1-green-gpmaxf", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-2", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-2-green-j2oajq", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-3", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-3-green-mkxies", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:cluster-endpoint:my-excluded-member-endpoint", "TargetMember": "arn:aws:rds:us-east-1:123456789012:cluster-endpoint:my-excluded-member-endpoint-green-4sqjrq", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:cluster-endpoint:my-reader-endpoint", "TargetMember": "arn:aws:rds:us-east-1:123456789012:cluster-endpoint:my-reader-endpoint-green-gwwzlg", "Status": "AVAILABLE" } ], "Tasks": [ { "Name": "CREATING_READ_REPLICA_OF_SOURCE", "Status": "COMPLETED" }, { "Name": "DB_ENGINE_VERSION_UPGRADE", "Status": "COMPLETED" }, { "Name": "CREATE_DB_INSTANCES_FOR_CLUSTER", "Status": "COMPLETED" }, { "Name": "CREATE_CUSTOM_ENDPOINTS", "Status": "COMPLETED" } ], "Status": "DELETING", "CreateTime": "2022-02-25T21:12:00.288000+00:00", "DeleteTime": "2022-02-25T22:29:11.336000+00:00" } }`For more information, see [Deleting a blue/green deployment](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-deleting.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DeleteBlueGreenDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-blue-green-deployment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-db-cluster-endpoint`.

- **AWS CLI**
- 
            
                    **To delete a custom DB cluster endpoint**The following `delete-db-cluster-endpoint`example deletes the specified custom DB cluster endpoint.`aws rds delete-db-cluster-endpoint \ --db-cluster-endpoint-identifier``mycustomendpoint`Output: `{ "DBClusterEndpointIdentifier": "mycustomendpoint", "DBClusterIdentifier": "mydbcluster", "DBClusterEndpointResourceIdentifier": "cluster-endpoint-ANPAJ4AE5446DAEXAMPLE", "Endpoint": "mycustomendpoint.cluster-custom-cnpexample.us-east-1.rds.amazonaws.com", "Status": "deleting", "EndpointType": "CUSTOM", "CustomEndpointType": "READER", "StaticMembers": [ "dbinstance1", "dbinstance2", "dbinstance3" ], "ExcludedMembers": [], "DBClusterEndpointArn": "arn:aws:rds:us-east-1:123456789012:cluster-endpoint:mycustomendpoint" }`For more information, see [Amazon Aurora Connection Management](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.Endpoints.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DeleteDbClusterEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-cluster-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-db-cluster-parameter-group`.

- **AWS CLI**
- 
            
                    **To delete a DB cluster parameter group**The following `delete-db-cluster-parameter-group`example deletes the specified DB cluster parameter group.`aws rds delete-db-cluster-parameter-group \ --db-cluster-parameter-group-name``mydbclusterparametergroup`This command produces no output. For more information, see [Working with DB Parameter Groups and DB Cluster Parameter Groups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DeleteDbClusterParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-cluster-parameter-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-db-cluster-snapshot`.

- **AWS CLI**
- 
            
                    **To delete a DB cluster snapshot**The following `delete-db-cluster-snapshot`example deletes the specified DB cluster snapshot.`aws rds delete-db-cluster-snapshot \ --db-cluster-snapshot-identifier``mydbclustersnapshot`Output: `{ "DBClusterSnapshot": { "AvailabilityZones": [ "us-east-1a", "us-east-1b", "us-east-1e" ], "DBClusterSnapshotIdentifier": "mydbclustersnapshot", "DBClusterIdentifier": "mydbcluster", "SnapshotCreateTime": "2019-06-18T21:21:00.469Z", "Engine": "aurora-mysql", "AllocatedStorage": 0, "Status": "available", "Port": 0, "VpcId": "vpc-6594f31c", "ClusterCreateTime": "2019-04-15T14:18:42.785Z", "MasterUsername": "myadmin", "EngineVersion": "5.7.mysql_aurora.2.04.2", "LicenseModel": "aurora-mysql", "SnapshotType": "manual", "PercentProgress": 100, "StorageEncrypted": true, "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/AKIAIOSFODNN7EXAMPLE", "DBClusterSnapshotArn": "arn:aws:rds:us-east-1:123456789012:cluster-snapshot:mydbclustersnapshot", "IAMDatabaseAuthenticationEnabled": false } }`For more information, see [Deleting a Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_DeleteSnapshot.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DeleteDbClusterSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-cluster-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-db-cluster`.

- **AWS CLI**
- 
            
                    **Example 1: To delete a DB instance in a DB cluster**The following `delete-db-instance`example deletes the final DB instance in a DB cluster. You can't delete a DB cluster if it contains DB instances that aren't in the**deleting**state. You can't take a final snapshot when deleting a DB instance in a DB cluster.`aws rds delete-db-instance \ --db-instance-identifier``database-3`Output: `{ "DBInstance": { "DBInstanceIdentifier": "database-3", "DBInstanceClass": "db.r4.large", "Engine": "aurora-postgresql", "DBInstanceStatus": "deleting", ...output omitted... } }`For more information, see [Deleting a DB Instance in an Aurora DB Cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_DeleteInstance.html)in the*Amazon Aurora User Guide*.**Example 2: To delete a DB cluster**The following `delete-db-cluster`example deletes the DB cluster named`mycluster`and takes a final snapshot named`mycluster-final-snapshot`. The status of the DB cluster is**available**while the snapshot is being taken. To follow the progress of the deletion, use the`describe-db-clusters`CLI command.`aws rds delete-db-cluster \ --db-cluster-identifier``mycluster`\ --no-skip-final-snapshot \ --final-db-snapshot-identifier`mycluster-final-snapshot`Output: `{ "DBCluster": { "AllocatedStorage": 20, "AvailabilityZones": [ "eu-central-1b", "eu-central-1c", "eu-central-1a" ], "BackupRetentionPeriod": 7, "DBClusterIdentifier": "mycluster", "DBClusterParameterGroup": "default.aurora-postgresql10", "DBSubnetGroup": "default-vpc-aa11bb22", "Status": "available", ...output omitted... } }`For more information, see [Aurora Clusters with a Single DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_DeleteInstance.html#USER_DeleteInstance.LastInstance)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DeleteDbCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-db-instance-automated-backup`.

- **AWS CLI**
- 
            
                    **To delete a replicated automated backup from a Region**The following `delete-db-instance-automated-backup`example deletes the automated backup with the specified Amazon Resource Name (ARN).`aws rds delete-db-instance-automated-backup \ --db-instance-automated-backups-arn``"arn:aws:rds:us-west-2:123456789012:auto-backup:ab-jkib2gfq5rv7replzadausbrktni2bn4example"`Output: `{ "DBInstanceAutomatedBackup": { "DBInstanceArn": "arn:aws:rds:us-east-1:123456789012:db:new-orcl-db", "DbiResourceId": "db-JKIB2GFQ5RV7REPLZA4EXAMPLE", "Region": "us-east-1", "DBInstanceIdentifier": "new-orcl-db", "RestoreWindow": {}, "AllocatedStorage": 20, "Status": "deleting", "Port": 1521, "AvailabilityZone": "us-east-1b", "VpcId": "vpc-########", "InstanceCreateTime": "2020-12-04T15:28:31Z", "MasterUsername": "admin", "Engine": "oracle-se2", "EngineVersion": "12.1.0.2.v21", "LicenseModel": "bring-your-own-license", "OptionGroupName": "default:oracle-se2-12-1", "Encrypted": false, "StorageType": "gp2", "IAMDatabaseAuthenticationEnabled": false, "BackupRetentionPeriod": 7, "DBInstanceAutomatedBackupsArn": "arn:aws:rds:us-west-2:123456789012:auto-backup:ab-jkib2gfq5rv7replzadausbrktni2bn4example" } }`For more information, see [Deleting replicated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReplicateBackups.html#AutomatedBackups.Delete)in the*Amazon RDS User Guide*.- 
                    For API details, see [DeleteDbInstanceAutomatedBackup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-instance-automated-backup.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-db-instance`.

- **AWS CLI**
- 
            
                    **To delete a DB instance**The following `delete-db-instance`example deletes the specified DB instance after creating a final DB snapshot named`test-instance-final-snap`.`aws rds delete-db-instance \ --db-instance-identifier``test-instance`\ --final-db-snapshot-identifier`test-instance-final-snap`Output: `{ "DBInstance": { "DBInstanceIdentifier": "test-instance", "DBInstanceStatus": "deleting", ...some output truncated... } }`- 
                    For API details, see [DeleteDBInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-db-parameter-group`.

- **AWS CLI**
- 
            
                    **To delete a DB parameter group**The following `command`example deletes a DB parameter group.`aws rds delete-db-parameter-group \ --db-parameter-group-name``mydbparametergroup`This command produces no output. For more information, see [Working with DB Parameter Groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [DeleteDBParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-parameter-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-db-proxy-endpoint`.

- **AWS CLI**
- 
            
                    **To delete a DB proxy endpoint for an RDS database**The following `delete-db-proxy-endpoint`example deletes a DB proxy endpoint for the target database.`aws rds delete-db-proxy-endpoint \ --db-proxy-endpoint-name``proxyEP1`Output: `{ "DBProxyEndpoint": { "DBProxyEndpointName": "proxyEP1", "DBProxyEndpointArn": "arn:aws:rds:us-east-1:123456789012:db-proxy-endpoint:prx-endpoint-0123a01b12345c0ab", "DBProxyName": "proxyExample", "Status": "deleting", "VpcId": "vpc-1234567", "VpcSecurityGroupIds": [ "sg-1234", "sg-5678" ], "VpcSubnetIds": [ "subnetgroup1", "subnetgroup2" ], "Endpoint": "proxyEP1.endpoint.proxy-ab0cd1efghij.us-east-1.rds.amazonaws.com", "CreatedDate": "2023-04-13T01:49:38.568000+00:00", "TargetRole": "READ_ONLY", "IsDefault": false } }`For more information, see [Deleting a proxy endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-endpoints.html#rds-proxy-endpoints.DeletingEndpoint)in the*Amazon RDS User Guide*and[Deleting a proxy endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-endpoints.html#rds-proxy-endpoints.DeletingEndpoint)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DeleteDbProxyEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-proxy-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-db-proxy`.

- **AWS CLI**
- 
            
                    **To delete a DB proxy for an RDS database**The following `delete-db-proxy`example deletes a DB proxy.`aws rds delete-db-proxy \ --db-proxy-name``proxyExample`Output: `{ "DBProxy": { "DBProxyName": "proxyExample", "DBProxyArn": "arn:aws:rds:us-east-1:123456789012:db-proxy:prx-0123a01b12345c0ab", "Status": "deleting", "EngineFamily": "PostgreSQL", "VpcId": "vpc-1234567", "VpcSecurityGroupIds": [ "sg-1234", "sg-5678" ], "VpcSubnetIds": [ "subnetgroup1", "subnetgroup2" ], "Auth": "[ { "Description": "proxydescription`" "AuthScheme": "SECRETS", "SecretArn": "arn:aws:secretsmanager:us-west-2:123456789123:secret:proxysecret1-Abcd1e", "IAMAuth": "DISABLED" } ], "RoleArn": "arn:aws:iam::12345678912:role/ProxyPostgreSQLRole", "Endpoint": "proxyExample.proxy-ab0cd1efghij.us-east-1.rds.amazonaws.com", "RequireTLS": false, "IdleClientTimeout": 1800, "DebuggingLogging": false, "CreatedDate": "2023-04-05T16:09:33.452000+00:00", "UpdatedDate": "2023-04-13T01:49:38.568000+00:00" } }`For more information, see [Deleting an RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-managing.html#rds-proxy-deleting)in the*Amazon RDS User Guide*and[Deleting an RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-managing.html#rds-proxy-deleting)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DeleteDbProxy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-proxy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-db-security-group`.

- **AWS CLI**
- 
            
                    **To delete a DB security group**The following `delete-db-security-group`example deletes a DB security group named`mysecuritygroup`.`aws rds delete-db-security-group \ --db-security-group-name``mysecuritygroup`This command produces no output. For more information, see [Working with DB security groups (EC2-Classic platform)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithSecurityGroups.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [DeleteDbSecurityGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-security-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-db-shard-group`.

- **AWS CLI**
- 
            
                    **Example 1: To delete a DB shard group unsuccessfully**The following `delete-db-shard-group`example shows the error that occurs when you try to delete a DB shard group before deleting all of your databases and schemas.`aws rds delete-db-shard-group \ --db-shard-group-identifier``limitless-test-shard-grp`Output: `An error occurred (InvalidDBShardGroupState) when calling the DeleteDBShardGroup operation: Unable to delete the DB shard group limitless-test-db-shard-group. Delete all of your Limitless Database databases and schemas, then try again.`**Example 2: To delete a DB shard group successfully**The following `delete-db-shard-group`example deletes a DB shard group after you've deleted all of your databases and schemas, including the`public`schema.`aws rds delete-db-shard-group \ --db-shard-group-identifier``limitless-test-shard-grp`Output: `{ "DBShardGroupResourceId": "shardgroup-7bb446329da94788b3f957746example", "DBShardGroupIdentifier": "limitless-test-shard-grp", "DBClusterIdentifier": "limitless-test-cluster", "MaxACU": 768.0, "ComputeRedundancy": 0, "Status": "deleting", "PubliclyAccessible": true, "Endpoint": "limitless-test-cluster.limitless-cekycexample.us-east-2.rds.amazonaws.com" }`For more information, see [Deleting Aurora DB clusters and DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_DeleteCluster.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DeleteDbShardGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-shard-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-db-snapshot`.

- **AWS CLI**
- 
            
                    **To delete a DB snapshot**The following `delete-db-snapshot`example deletes the specified DB snapshot.`aws rds delete-db-snapshot \ --db-snapshot-identifier``mydbsnapshot`Output: `{ "DBSnapshot": { "DBSnapshotIdentifier": "mydbsnapshot", "DBInstanceIdentifier": "database-mysql", "SnapshotCreateTime": "2019-06-18T22:08:40.702Z", "Engine": "mysql", "AllocatedStorage": 100, "Status": "deleted", "Port": 3306, "AvailabilityZone": "us-east-1b", "VpcId": "vpc-6594f31c", "InstanceCreateTime": "2019-04-30T15:45:53.663Z", "MasterUsername": "admin", "EngineVersion": "5.6.40", "LicenseModel": "general-public-license", "SnapshotType": "manual", "Iops": 1000, "OptionGroupName": "default:mysql-5-6", "PercentProgress": 100, "StorageType": "io1", "Encrypted": true, "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/AKIAIOSFODNN7EXAMPLE", "DBSnapshotArn": "arn:aws:rds:us-east-1:123456789012:snapshot:mydbsnapshot", "IAMDatabaseAuthenticationEnabled": false, "ProcessorFeatures": [], "DbiResourceId": "db-AKIAIOSFODNN7EXAMPLE" } }`For more information, see [Deleting a Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteSnapshot.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [DeleteDbSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-db-subnet-group`.

- **AWS CLI**
- 
            
                    **To delete a DB subnet group**The following `delete-db-subnet-group`example deletes the DB subnet group called`mysubnetgroup`.`aws rds delete-db-subnet-group --db-subnet-group-name``mysubnetgroup`This command produces no output. For more information, see [Working with a DB Instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [DeleteDbSubnetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-db-subnet-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-event-subscription`.

- **AWS CLI**
- 
            
                    **To delete an event subscription**The following `delete-event-subscription`example deletes the specified event subscription.`aws rds delete-event-subscription --subscription-name``my-instance-events`Output: `{ "EventSubscription": { "EventSubscriptionArn": "arn:aws:rds:us-east-1:123456789012:es:my-instance-events", "CustomerAwsId": "123456789012", "Enabled": false, "SourceIdsList": [ "test-instance" ], "SourceType": "db-instance", "EventCategoriesList": [ "backup", "recovery" ], "SubscriptionCreationTime": "2018-07-31 23:22:01.893", "CustSubscriptionId": "my-instance-events", "SnsTopicArn": "arn:aws:sns:us-east-1:123456789012:interesting-events", "Status": "deleting" } }`- 
                    For API details, see [DeleteEventSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-event-subscription.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-global-cluster`.

- **AWS CLI**
- 
            
                    **To delete a global DB cluster**The following `delete-global-cluster`example deletes an Aurora MySQL-compatible global DB cluster. The output shows the cluster that you're deleting, but subsequent`describe-global-clusters`commands don't list that DB cluster.`aws rds delete-global-cluster \ --global-cluster-identifier``myglobalcluster`Output: `{ "GlobalCluster": { "GlobalClusterIdentifier": "myglobalcluster", "GlobalClusterResourceId": "cluster-f0e523bfe07aabb", "GlobalClusterArn": "arn:aws:rds::123456789012:global-cluster:myglobalcluster", "Status": "available", "Engine": "aurora-mysql", "EngineVersion": "5.7.mysql_aurora.2.07.2", "StorageEncrypted": false, "DeletionProtection": false, "GlobalClusterMembers": [] } }`For more information, see [Deleting an Aurora global database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-managing.html#aurora-global-database-deleting)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DeleteGlobalCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-global-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-option-group`.

- **AWS CLI**
- 
            
                    **To delete an option group**The following `delete-option-group`example deletes the specified option group.`aws rds delete-option-group \ --option-group-name``myoptiongroup`This command produces no output. For more information, see [Deleting an Option Group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.html#USER_WorkingWithOptionGroups.Delete)in the*Amazon RDS User Guide*.- 
                    For API details, see [DeleteOptionGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-option-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deregister-db-proxy-targets`.

- **AWS CLI**
- 
            
                    **To deregister a DB proxy target from database target group**The following `deregister-db-proxy-targets`example removes the association between the proxy`proxyExample`and its target.`aws rds deregister-db-proxy-targets \ --db-proxy-name``proxyExample`\ --db-instance-identifiers`database-1`This command produces no output. For more information, see [Deleting an RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-managing.html#rds-proxy-deleting)in the*Amazon RDS User Guide*and[Deleting an RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-managing.html#rds-proxy-deleting)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DeregisterDbProxyTargets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/deregister-db-proxy-targets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-account-attributes`.

- **AWS CLI**
- 
            
                    **To describe account attributes**The following `describe-account-attributes`example retrieves the attributes for the current AWS account.`aws rds describe-account-attributes`Output: `{ "AccountQuotas": [ { "Max": 40, "Used": 4, "AccountQuotaName": "DBInstances" }, { "Max": 40, "Used": 0, "AccountQuotaName": "ReservedDBInstances" }, { "Max": 100000, "Used": 40, "AccountQuotaName": "AllocatedStorage" }, { "Max": 25, "Used": 0, "AccountQuotaName": "DBSecurityGroups" }, { "Max": 20, "Used": 0, "AccountQuotaName": "AuthorizationsPerDBSecurityGroup" }, { "Max": 50, "Used": 1, "AccountQuotaName": "DBParameterGroups" }, { "Max": 100, "Used": 3, "AccountQuotaName": "ManualSnapshots" }, { "Max": 20, "Used": 0, "AccountQuotaName": "EventSubscriptions" }, { "Max": 50, "Used": 1, "AccountQuotaName": "DBSubnetGroups" }, { "Max": 20, "Used": 1, "AccountQuotaName": "OptionGroups" }, { "Max": 20, "Used": 6, "AccountQuotaName": "SubnetsPerDBSubnetGroup" }, { "Max": 5, "Used": 0, "AccountQuotaName": "ReadReplicasPerMaster" }, { "Max": 40, "Used": 1, "AccountQuotaName": "DBClusters" }, { "Max": 50, "Used": 0, "AccountQuotaName": "DBClusterParameterGroups" }, { "Max": 5, "Used": 0, "AccountQuotaName": "DBClusterRoles" } ] }`- 
                    For API details, see [DescribeAccountAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-account-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-blue-green-deployments`.

- **AWS CLI**
- 
            
                    **Example 1: To describe a blue/green deployment of an RDS DB instance after creation completes**The following `describe-blue-green-deployment`example retrieves the details of a blue/green deployment after creation completes.`aws rds describe-blue-green-deployments \ --blue-green-deployment-identifier``bgd-v53303651eexfake`Output: `{ "BlueGreenDeployments": [ { "BlueGreenDeploymentIdentifier": "bgd-v53303651eexfake", "BlueGreenDeploymentName": "bgd-cli-test-instance", "Source": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance", "Target": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-green-rkfbpe", "SwitchoverDetails": [ { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-green-rkfbpe", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-replica-1", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-replica-1-green-j382ha", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-replica-2", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-replica-2-green-ejv4ao", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-replica-3", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-replica-3-green-vlpz3t", "Status": "AVAILABLE" } ], "Tasks": [ { "Name": "CREATING_READ_REPLICA_OF_SOURCE", "Status": "COMPLETED" }, { "Name": "DB_ENGINE_VERSION_UPGRADE", "Status": "COMPLETED" }, { "Name": "CONFIGURE_BACKUPS", "Status": "COMPLETED" }, { "Name": "CREATING_TOPOLOGY_OF_SOURCE", "Status": "COMPLETED" } ], "Status": "AVAILABLE", "CreateTime": "2022-02-25T21:18:51.183000+00:00" } ] }`For more information, see [Viewing a blue/green deployment](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments-viewing.html)in the*Amazon RDS User Guide*.**Example 2: To describe a blue/green deployment for an Aurora MySQL DB cluster**The following `describe-blue-green-deployment`example retrieves the details of a blue/green deployment.`aws rds describe-blue-green-deployments \ --blue-green-deployment-identifier``bgd-wi89nwzglccsfake`Output: `{ "BlueGreenDeployments": [ { "BlueGreenDeploymentIdentifier": "bgd-wi89nwzglccsfake", "BlueGreenDeploymentName": "my-blue-green-deployment", "Source": "arn:aws:rds:us-east-1:123456789012:cluster:my-aurora-mysql-cluster", "Target": "arn:aws:rds:us-east-1:123456789012:cluster:my-aurora-mysql-cluster-green-3rnukl", "SwitchoverDetails": [ { "SourceMember": "arn:aws:rds:us-east-1:123456789012:cluster:my-aurora-mysql-cluster", "TargetMember": "arn:aws:rds:us-east-1:123456789012:cluster:my-aurora-mysql-cluster-green-3rnukl", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-1", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-1-green-gpmaxf", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-2", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-2-green-j2oajq", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-3", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-3-green-mkxies", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:cluster-endpoint:my-excluded-member-endpoint", "TargetMember": "arn:aws:rds:us-east-1:123456789012:cluster-endpoint:my-excluded-member-endpoint-green-4sqjrq", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:cluster-endpoint:my-reader-endpoint", "TargetMember": "arn:aws:rds:us-east-1:123456789012:cluster-endpoint:my-reader-endpoint-green-gwwzlg", "Status": "AVAILABLE" } ], "Tasks": [ { "Name": "CREATING_READ_REPLICA_OF_SOURCE", "Status": "COMPLETED" }, { "Name": "DB_ENGINE_VERSION_UPGRADE", "Status": "COMPLETED" }, { "Name": "CREATE_DB_INSTANCES_FOR_CLUSTER", "Status": "COMPLETED" }, { "Name": "CREATE_CUSTOM_ENDPOINTS", "Status": "COMPLETED" } ], "Status": "AVAILABLE", "CreateTime": "2022-02-25T21:12:00.288000+00:00" } ] }`For more information, see [Viewing a blue/green deployment](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-viewing.html)in the*Amazon Aurora User Guide*.**Example 3: To describe a blue/green deployment for an Aurora MySQL cluster after switchover**The following `describe-blue-green-deployment`example retrieves the details about a blue/green deployment after the green environment is promoted to be the production environment.`aws rds describe-blue-green-deployments \ --blue-green-deployment-identifier``bgd-wi89nwzglccsfake`Output: `{ "BlueGreenDeployments": [ { "BlueGreenDeploymentIdentifier": "bgd-wi89nwzglccsfake", "BlueGreenDeploymentName": "my-blue-green-deployment", "Source": "arn:aws:rds:us-east-1:123456789012:cluster:my-aurora-mysql-cluster-old1", "Target": "arn:aws:rds:us-east-1:123456789012:cluster:my-aurora-mysql-cluster", "SwitchoverDetails": [ { "SourceMember": "arn:aws:rds:us-east-1:123456789012:cluster:my-aurora-mysql-cluster-old1", "TargetMember": "arn:aws:rds:us-east-1:123456789012:cluster:my-aurora-mysql-cluster", "Status": "SWITCHOVER_COMPLETED" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-1-old1", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-1", "Status": "SWITCHOVER_COMPLETED" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-2-old1", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-2", "Status": "SWITCHOVER_COMPLETED" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-3-old1", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-3", "Status": "SWITCHOVER_COMPLETED" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:cluster-endpoint:my-excluded-member-endpoint-old1", "TargetMember": "arn:aws:rds:us-east-1:123456789012:cluster-endpoint:my-excluded-member-endpoint", "Status": "SWITCHOVER_COMPLETED" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:cluster-endpoint:my-reader-endpoint-old1", "TargetMember": "arn:aws:rds:us-east-1:123456789012:cluster-endpoint:my-reader-endpoint", "Status": "SWITCHOVER_COMPLETED" } ], "Tasks": [ { "Name": "CREATING_READ_REPLICA_OF_SOURCE", "Status": "COMPLETED" }, { "Name": "DB_ENGINE_VERSION_UPGRADE", "Status": "COMPLETED" }, { "Name": "CREATE_DB_INSTANCES_FOR_CLUSTER", "Status": "COMPLETED" }, { "Name": "CREATE_CUSTOM_ENDPOINTS", "Status": "COMPLETED" } ], "Status": "SWITCHOVER_COMPLETED", "CreateTime": "2022-02-25T22:38:49.522000+00:00" } ] }`For more information, see [Viewing a blue/green deployment](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-viewing.html)in the*Amazon Aurora User Guide*.**Example 4: To describe a combined blue/green deployment**The following `describe-blue-green-deployment`example retrieves the details of a combined blue/green deployment.`aws rds describe-blue-green-deployments`Output: `{ "BlueGreenDeployments": [ { "BlueGreenDeploymentIdentifier": "bgd-wi89nwzgfakelccs", "BlueGreenDeploymentName": "my-blue-green-deployment", "Source": "arn:aws:rds:us-east-1:123456789012:cluster:my-aurora-mysql-cluster", "Target": "arn:aws:rds:us-east-1:123456789012:cluster:my-aurora-mysql-cluster-green-3rnukl", "SwitchoverDetails": [ { "SourceMember": "arn:aws:rds:us-east-1:123456789012:cluster:my-aurora-mysql-cluster", "TargetMember": "arn:aws:rds:us-east-1:123456789012:cluster:my-aurora-mysql-cluster-green-3rnukl", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-1", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-1-green-gpmaxf", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-2", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-2-green-j2oajq", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-3", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-3-green-mkxies", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:cluster-endpoint:my-excluded-member-endpoint", "TargetMember": "arn:aws:rds:us-east-1:123456789012:cluster-endpoint:my-excluded-member-endpoint-green-4sqjrq", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:cluster-endpoint:my-reader-endpoint", "TargetMember": "arn:aws:rds:us-east-1:123456789012:cluster-endpoint:my-reader-endpoint-green-gwwzlg", "Status": "AVAILABLE" } ], "Tasks": [ { "Name": "CREATING_READ_REPLICA_OF_SOURCE", "Status": "COMPLETED" }, { "Name": "DB_ENGINE_VERSION_UPGRADE", "Status": "COMPLETED" }, { "Name": "CREATE_DB_INSTANCES_FOR_CLUSTER", "Status": "COMPLETED" }, { "Name": "CREATE_CUSTOM_ENDPOINTS", "Status": "COMPLETED" } ], "Status": "AVAILABLE", "CreateTime": "2022-02-25T21:12:00.288000+00:00" }, { "BlueGreenDeploymentIdentifier": "bgd-v5330365fake1eex", "BlueGreenDeploymentName": "bgd-cli-test-instance", "Source": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-old1", "Target": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance", "SwitchoverDetails": [ { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-old1", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance", "Status": "SWITCHOVER_COMPLETED" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-replica-1-old1", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-replica-1", "Status": "SWITCHOVER_COMPLETED" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-replica-2-old1", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-replica-2", "Status": "SWITCHOVER_COMPLETED" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-replica-3-old1", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-replica-3", "Status": "SWITCHOVER_COMPLETED" } ], "Tasks": [ { "Name": "CREATING_READ_REPLICA_OF_SOURCE", "Status": "COMPLETED" }, { "Name": "DB_ENGINE_VERSION_UPGRADE", "Status": "COMPLETED" }, { "Name": "CONFIGURE_BACKUPS", "Status": "COMPLETED" }, { "Name": "CREATING_TOPOLOGY_OF_SOURCE", "Status": "COMPLETED" } ], "Status": "SWITCHOVER_COMPLETED", "CreateTime": "2022-02-25T22:33:22.225000+00:00" } ] }`For more information, see [Viewing a blue/green deployment](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments-viewing.html)in the*Amazon RDS User Guide*and[Viewing a blue/green deployment](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-viewing.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DescribeBlueGreenDeployments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-blue-green-deployments.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-certificates`.

- **AWS CLI**
- 
            
                    **To describe certificates**The following `describe-certificates`example retrieves the details of the certificate associated with the user's default region.`aws rds describe-certificates`Output: `{ "Certificates": [ { "CertificateIdentifier": "rds-ca-ecc384-g1", "CertificateType": "CA", "Thumbprint": "2ee3dcc06e50192559b13929e73484354f23387d", "ValidFrom": "2021-05-24T22:06:59+00:00", "ValidTill": "2121-05-24T23:06:59+00:00", "CertificateArn": "arn:aws:rds:us-west-2::cert:rds-ca-ecc384-g1", "CustomerOverride": false }, { "CertificateIdentifier": "rds-ca-rsa4096-g1", "CertificateType": "CA", "Thumbprint": "19da4f2af579a8ae1f6a0fa77aa5befd874b4cab", "ValidFrom": "2021-05-24T22:03:20+00:00", "ValidTill": "2121-05-24T23:03:20+00:00", "CertificateArn": "arn:aws:rds:us-west-2::cert:rds-ca-rsa4096-g1", "CustomerOverride": false }, { "CertificateIdentifier": "rds-ca-rsa2048-g1", "CertificateType": "CA", "Thumbprint": "7c40cb42714b6fdb2b296f9bbd0e8bb364436a76", "ValidFrom": "2021-05-24T21:59:00+00:00", "ValidTill": "2061-05-24T22:59:00+00:00", "CertificateArn": "arn:aws:rds:us-west-2::cert:rds-ca-rsa2048-g1", "CustomerOverride": true, "CustomerOverrideValidTill": "2061-05-24T22:59:00+00:00" }, { "CertificateIdentifier": "rds-ca-2019", "CertificateType": "CA", "Thumbprint": "d40ddb29e3750dffa671c3140bbf5f478d1c8096", "ValidFrom": "2019-08-22T17:08:50+00:00", "ValidTill": "2024-08-22T17:08:50+00:00", "CertificateArn": "arn:aws:rds:us-west-2::cert:rds-ca-2019", "CustomerOverride": false } ], "DefaultCertificateForNewLaunches": "rds-ca-rsa2048-g1" }`For more information, see [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html)in the*Amazon RDS User Guide*and[Using SSL/TLS to encrypt a connection to a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DescribeCertificates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-certificates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-cluster-backtracks`.

- **AWS CLI**
- 
            
                    **To describe backtracks for a DB cluster**The following `describe-db-cluster-backtracks`example retrieves details about the specified DB cluster.`aws rds describe-db-cluster-backtracks \ --db-cluster-identifier``mydbcluster`Output: `{ "DBClusterBacktracks": [ { "DBClusterIdentifier": "mydbcluster", "BacktrackIdentifier": "2f5f5294-0dd2-44c9-9f50-EXAMPLE", "BacktrackTo": "2021-02-12T04:59:22Z", "BacktrackedFrom": "2021-02-12T14:37:31.640Z", "BacktrackRequestCreationTime": "2021-02-12T14:36:18.819Z", "Status": "COMPLETED" }, { "DBClusterIdentifier": "mydbcluster", "BacktrackIdentifier": "3c7a6421-af2a-4ea3-ae95-EXAMPLE", "BacktrackTo": "2021-02-11T22:53:46Z", "BacktrackedFrom": "2021-02-12T00:09:27.006Z", "BacktrackRequestCreationTime": "2021-02-12T00:07:53.487Z", "Status": "COMPLETED" } ] }`For more information, see [Backtracking an Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Backtrack.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DescribeDbClusterBacktracks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-cluster-backtracks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-cluster-endpoints`.

- **AWS CLI**
- 
            
                    **Example 1: To describe DB cluster endpoints**The following `describe-db-cluster-endpoints`example retrieves details for your DB cluster endpoints. The most common kinds of Aurora clusters have two endpoints. One endpoint has type`WRITER`. You can use this endpoint for all SQL statements. The other endpoint has type`READER`. You can use this endpoint only for SELECT and other read-only SQL statements.`aws rds describe-db-cluster-endpoints`Output: `{ "DBClusterEndpoints": [ { "DBClusterIdentifier": "my-database-1", "Endpoint": "my-database-1.cluster-cnpexample.us-east-1.rds.amazonaws.com", "Status": "creating", "EndpointType": "WRITER" }, { "DBClusterIdentifier": "my-database-1", "Endpoint": "my-database-1.cluster-ro-cnpexample.us-east-1.rds.amazonaws.com", "Status": "creating", "EndpointType": "READER" }, { "DBClusterIdentifier": "mydbcluster", "Endpoint": "mydbcluster.cluster-cnpexamle.us-east-1.rds.amazonaws.com", "Status": "available", "EndpointType": "WRITER" }, { "DBClusterIdentifier": "mydbcluster", "Endpoint": "mydbcluster.cluster-ro-cnpexample.us-east-1.rds.amazonaws.com", "Status": "available", "EndpointType": "READER" } ] }`**Example 2: To describe DB cluster endpoints of a single DB cluster**The following `describe-db-cluster-endpoints`example retrieves details for the DB cluster endpoints of a single specified DB cluster. Aurora Serverless clusters have only a single endpoint with a type of`WRITER`.`aws rds describe-db-cluster-endpoints \ --db-cluster-identifier``serverless-cluster`Output: `{ "DBClusterEndpoints": [ { "Status": "available", "Endpoint": "serverless-cluster.cluster-cnpexample.us-east-1.rds.amazonaws.com", "DBClusterIdentifier": "serverless-cluster", "EndpointType": "WRITER" } ] }`For more information, see [Amazon Aurora Connection Management](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.Endpoints.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DescribeDbClusterEndpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-cluster-endpoints.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-cluster-parameter-groups`.

- **AWS CLI**
- 
            
                    **To describe DB cluster parameter groups**The following `describe-db-cluster-parameter-groups`example retrieves details for your DB cluster parameter groups.`aws rds describe-db-cluster-parameter-groups`Output: `{ "DBClusterParameterGroups": [ { "DBClusterParameterGroupName": "default.aurora-mysql5.7", "DBParameterGroupFamily": "aurora-mysql5.7", "Description": "Default cluster parameter group for aurora-mysql5.7", "DBClusterParameterGroupArn": "arn:aws:rds:us-east-1:123456789012:cluster-pg:default.aurora-mysql5.7" }, { "DBClusterParameterGroupName": "default.aurora-postgresql9.6", "DBParameterGroupFamily": "aurora-postgresql9.6", "Description": "Default cluster parameter group for aurora-postgresql9.6", "DBClusterParameterGroupArn": "arn:aws:rds:us-east-1:123456789012:cluster-pg:default.aurora-postgresql9.6" }, { "DBClusterParameterGroupName": "default.aurora5.6", "DBParameterGroupFamily": "aurora5.6", "Description": "Default cluster parameter group for aurora5.6", "DBClusterParameterGroupArn": "arn:aws:rds:us-east-1:123456789012:cluster-pg:default.aurora5.6" }, { "DBClusterParameterGroupName": "mydbclusterpg", "DBParameterGroupFamily": "aurora-mysql5.7", "Description": "My DB cluster parameter group", "DBClusterParameterGroupArn": "arn:aws:rds:us-east-1:123456789012:cluster-pg:mydbclusterpg" }, { "DBClusterParameterGroupName": "mydbclusterpgcopy", "DBParameterGroupFamily": "aurora-mysql5.7", "Description": "Copy of mydbclusterpg parameter group", "DBClusterParameterGroupArn": "arn:aws:rds:us-east-1:123456789012:cluster-pg:mydbclusterpgcopy" } ] }`For more information, see [Working with DB Parameter Groups and DB Cluster Parameter Groups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DescribeDbClusterParameterGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-cluster-parameter-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-cluster-parameters`.

- **AWS CLI**
- 
            
                    **Example 1: To describe the parameters in a DB cluster parameter group**The following `describe-db-cluster-parameters`example retrieves details about the parameters in a DB cluster parameter group.`aws rds describe-db-cluster-parameters \ --db-cluster-parameter-group-name``mydbclusterpg`Output: `{ "Parameters": [ { "ParameterName": "allow-suspicious-udfs", "Description": "Controls whether user-defined functions that have only an xxx symbol for the main function can be loaded", "Source": "engine-default", "ApplyType": "static", "DataType": "boolean", "AllowedValues": "0,1", "IsModifiable": false, "ApplyMethod": "pending-reboot", "SupportedEngineModes": [ "provisioned" ] }, { "ParameterName": "aurora_lab_mode", "ParameterValue": "0", "Description": "Enables new features in the Aurora engine.", "Source": "engine-default", "ApplyType": "static", "DataType": "boolean", "AllowedValues": "0,1", "IsModifiable": true, "ApplyMethod": "pending-reboot", "SupportedEngineModes": [ "provisioned" ] }, ...some output truncated... ] }`**Example 2: To list only the parameter names in a DB cluster parameter group**The following `describe-db-cluster-parameters`example retrieves only the names of the parameters in a DB cluster parameter group.`aws rds describe-db-cluster-parameters \ --db-cluster-parameter-group-name``default.aurora-mysql5.7`\ --query '`Parameters[].{ParameterName:ParameterName}`'Output: `[ { "ParameterName": "allow-suspicious-udfs" }, { "ParameterName": "aurora_binlog_read_buffer_size" }, { "ParameterName": "aurora_binlog_replication_max_yield_seconds" }, { "ParameterName": "aurora_binlog_use_large_read_buffer" }, { "ParameterName": "aurora_lab_mode" }, ...some output truncated... } ]`**Example 3: To describe only the modifiable parameters in a DB cluster parameter group**The following `describe-db-cluster-parameters`example retrieves the names of only the parameters that you can modify in a DB cluster parameter group.`aws rds describe-db-cluster-parameters \ --db-cluster-parameter-group-name``default.aurora-mysql5.7`\ --query '`Parameters[].{ParameterName:ParameterName,IsModifiable:IsModifiable} | [?IsModifiable == `true`]`'Output: `[ { "ParameterName": "aurora_binlog_read_buffer_size", "IsModifiable": true }, { "ParameterName": "aurora_binlog_replication_max_yield_seconds", "IsModifiable": true }, { "ParameterName": "aurora_binlog_use_large_read_buffer", "IsModifiable": true }, { "ParameterName": "aurora_lab_mode", "IsModifiable": true }, ...some output truncated... } ]`**Example 4: To describe only the modifiable Boolean parameters in a DB cluster parameter group**The following `describe-db-cluster-parameters`example retrieves the names of only the parameters that you can modify in a DB cluster parameter group and that have a Boolean data type.`aws rds describe-db-cluster-parameters \ --db-cluster-parameter-group-name``default.aurora-mysql5.7`\ --query '`Parameters[].{ParameterName:ParameterName,DataType:DataType,IsModifiable:IsModifiable} | [?DataType == `boolean`] | [?IsModifiable == `true`]`'Output: `[ { "DataType": "boolean", "ParameterName": "aurora_binlog_use_large_read_buffer", "IsModifiable": true }, { "DataType": "boolean", "ParameterName": "aurora_lab_mode", "IsModifiable": true }, { "DataType": "boolean", "ParameterName": "autocommit", "IsModifiable": true }, { "DataType": "boolean", "ParameterName": "automatic_sp_privileges", "IsModifiable": true }, ...some output truncated... } ]`For more information, see [Working with DB Parameter Groups and DB Cluster Parameter Groups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DescribeDbClusterParameters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-cluster-parameters.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-cluster-snapshot-attributes`.

- **AWS CLI**
- 
            
                    **To describe the attribute names and values for a DB cluster snapshot**The following `describe-db-cluster-snapshot-attributes`example retrieves details of the attribute names and values for the specified DB cluster snapshot.`aws rds describe-db-cluster-snapshot-attributes \ --db-cluster-snapshot-identifier``myclustersnapshot`Output: `{ "DBClusterSnapshotAttributesResult": { "DBClusterSnapshotIdentifier": "myclustersnapshot", "DBClusterSnapshotAttributes": [ { "AttributeName": "restore", "AttributeValues": [ "123456789012" ] } ] } }`For more information, see [Sharing a DB Cluster Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_ShareSnapshot.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DescribeDbClusterSnapshotAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-cluster-snapshot-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-cluster-snapshots`.

- **AWS CLI**
- 
            
                    **To describe a DB cluster snapshot for a DB cluster**The following `describe-db-cluster-snapshots`example retrieves the details for the DB cluster snapshots for the specified DB cluster.`aws rds describe-db-cluster-snapshots \ --db-cluster-identifier``mydbcluster`Output: `{ "DBClusterSnapshots": [ { "AvailabilityZones": [ "us-east-1a", "us-east-1b", "us-east-1e" ], "DBClusterSnapshotIdentifier": "myclustersnapshotcopy", "DBClusterIdentifier": "mydbcluster", "SnapshotCreateTime": "2019-06-04T09:16:42.649Z", "Engine": "aurora-mysql", "AllocatedStorage": 0, "Status": "available", "Port": 0, "VpcId": "vpc-6594f31c", "ClusterCreateTime": "2019-04-15T14:18:42.785Z", "MasterUsername": "myadmin", "EngineVersion": "5.7.mysql_aurora.2.04.2", "LicenseModel": "aurora-mysql", "SnapshotType": "manual", "PercentProgress": 100, "StorageEncrypted": true, "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/AKIAIOSFODNN7EXAMPLE", "DBClusterSnapshotArn": "arn:aws:rds:us-east-1:814387698303:cluster-snapshot:myclustersnapshotcopy", "IAMDatabaseAuthenticationEnabled": false }, { "AvailabilityZones": [ "us-east-1a", "us-east-1b", "us-east-1e" ], "DBClusterSnapshotIdentifier": "rds:mydbcluster-2019-06-20-09-16", "DBClusterIdentifier": "mydbcluster", "SnapshotCreateTime": "2019-06-20T09:16:26.569Z", "Engine": "aurora-mysql", "AllocatedStorage": 0, "Status": "available", "Port": 0, "VpcId": "vpc-6594f31c", "ClusterCreateTime": "2019-04-15T14:18:42.785Z", "MasterUsername": "myadmin", "EngineVersion": "5.7.mysql_aurora.2.04.2", "LicenseModel": "aurora-mysql", "SnapshotType": "automated", "PercentProgress": 100, "StorageEncrypted": true, "KmsKeyId": "arn:aws:kms:us-east-1:814387698303:key/AKIAIOSFODNN7EXAMPLE", "DBClusterSnapshotArn": "arn:aws:rds:us-east-1:123456789012:cluster-snapshot:rds:mydbcluster-2019-06-20-09-16", "IAMDatabaseAuthenticationEnabled": false } ] }`For more information, see [Creating a DB Cluster Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_CreateSnapshotCluster.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DescribeDbClusterSnapshots](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-cluster-snapshots.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-clusters`.

- **AWS CLI**
- 
            
                    **Example 1: To describe a DB cluster**The following `describe-db-clusters`example retrieves the details of the specified DB cluster.`aws rds describe-db-clusters \ --db-cluster-identifier``mydbcluster`Output: `{ "DBClusters": [ { "AllocatedStorage": 1, "AvailabilityZones": [ "us-east-1a", "us-east-1b", "us-east-1e" ], "BackupRetentionPeriod": 1, "DatabaseName": "mydbcluster", "DBClusterIdentifier": "mydbcluster", "DBClusterParameterGroup": "default.aurora-mysql5.7", "DBSubnetGroup": "default", "Status": "available", "EarliestRestorableTime": "2019-06-19T09:16:28.210Z", "Endpoint": "mydbcluster.cluster-cnpexample.us-east-1.rds.amazonaws.com", "ReaderEndpoint": "mydbcluster.cluster-ro-cnpexample.us-east-1.rds.amazonaws.com", "MultiAZ": true, "Engine": "aurora-mysql", "EngineVersion": "5.7.mysql_aurora.2.04.2", "LatestRestorableTime": "2019-06-20T22:38:14.908Z", "Port": 3306, "MasterUsername": "myadmin", "PreferredBackupWindow": "09:09-09:39", "PreferredMaintenanceWindow": "sat:04:09-sat:04:39", "ReadReplicaIdentifiers": [], "DBClusterMembers": [ { "DBInstanceIdentifier": "dbinstance3", "IsClusterWriter": false, "DBClusterParameterGroupStatus": "in-sync", "PromotionTier": 1 }, { "DBInstanceIdentifier": "dbinstance1", "IsClusterWriter": false, "DBClusterParameterGroupStatus": "in-sync", "PromotionTier": 1 }, { "DBInstanceIdentifier": "dbinstance2", "IsClusterWriter": false, "DBClusterParameterGroupStatus": "in-sync", "PromotionTier": 1 }, { "DBInstanceIdentifier": "mydbcluster", "IsClusterWriter": false, "DBClusterParameterGroupStatus": "in-sync", "PromotionTier": 1 }, { "DBInstanceIdentifier": "mydbcluster-us-east-1b", "IsClusterWriter": false, "DBClusterParameterGroupStatus": "in-sync", "PromotionTier": 1 }, { "DBInstanceIdentifier": "mydbcluster", "IsClusterWriter": true, "DBClusterParameterGroupStatus": "in-sync", "PromotionTier": 1 } ], "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sg-0b9130572daf3dc16", "Status": "active" } ], "HostedZoneId": "Z2R2ITUGPM61AM", "StorageEncrypted": true, "KmsKeyId": "arn:aws:kms:us-east-1:814387698303:key/AKIAIOSFODNN7EXAMPLE", "DbClusterResourceId": "cluster-AKIAIOSFODNN7EXAMPLE", "DBClusterArn": "arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster", "AssociatedRoles": [], "IAMDatabaseAuthenticationEnabled": false, "ClusterCreateTime": "2019-04-15T14:18:42.785Z", "EngineMode": "provisioned", "DeletionProtection": false, "HttpEndpointEnabled": false } ] }`**Example 2: To list certain attributes of all DB clusters**The following `describe-db-clusters`example retrieves only the`DBClusterIdentifier`,`Endpoint`, and`ReaderEndpoint`attributes of all your DB clusters in the current AWS Region.`aws rds describe-db-clusters \ --query '``DBClusters[].{DBClusterIdentifier:DBClusterIdentifier,Endpoint:Endpoint,ReaderEndpoint:ReaderEndpoint}`'Output: `[ { "Endpoint": "cluster-57-2020-05-01-2270.cluster-cnpexample.us-east-1.rds.amazonaws.com", "ReaderEndpoint": "cluster-57-2020-05-01-2270.cluster-ro-cnpexample.us-east-1.rds.amazonaws.com", "DBClusterIdentifier": "cluster-57-2020-05-01-2270" }, { "Endpoint": "cluster-57-2020-05-01-4615.cluster-cnpexample.us-east-1.rds.amazonaws.com", "ReaderEndpoint": "cluster-57-2020-05-01-4615.cluster-ro-cnpexample.us-east-1.rds.amazonaws.com", "DBClusterIdentifier": "cluster-57-2020-05-01-4615" }, { "Endpoint": "pg2-cluster.cluster-cnpexample.us-east-1.rds.amazonaws.com", "ReaderEndpoint": "pg2-cluster.cluster-ro-cnpexample.us-east-1.rds.amazonaws.com", "DBClusterIdentifier": "pg2-cluster" }, ...output omitted... } ]`**Example 3: To list DB clusters with a specific attribute**The following `describe-db-clusters`example retrieves only the`DBClusterIdentifier`and`Engine`attributes of your DB clusters that use the`aurora-postgresql`DB engine.`aws rds describe-db-clusters \ --query '``DBClusters[].{DBClusterIdentifier:DBClusterIdentifier,Engine:Engine} | [?Engine == `aurora-postgresql`]`'Output: `[ { "Engine": "aurora-postgresql", "DBClusterIdentifier": "pg2-cluster" } ]`For more information, see [Amazon Aurora DB Clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DescribeDbClusters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-clusters.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-engine-versions`.

- **AWS CLI**
- 
            
                    **To describe the DB engine versions for the MySQL DB engine**The following `describe-db-engine-versions`example displays details about each of the DB engine versions for the specified DB engine.`aws rds describe-db-engine-versions \ --engine``mysql`Output: `{ "DBEngineVersions": [ { "Engine": "mysql", "EngineVersion": "5.5.46", "DBParameterGroupFamily": "mysql5.5", "DBEngineDescription": "MySQL Community Edition", "DBEngineVersionDescription": "MySQL 5.5.46", "ValidUpgradeTarget": [ { "Engine": "mysql", "EngineVersion": "5.5.53", "Description": "MySQL 5.5.53", "AutoUpgrade": false, "IsMajorVersionUpgrade": false }, { "Engine": "mysql", "EngineVersion": "5.5.54", "Description": "MySQL 5.5.54", "AutoUpgrade": false, "IsMajorVersionUpgrade": false }, { "Engine": "mysql", "EngineVersion": "5.5.57", "Description": "MySQL 5.5.57", "AutoUpgrade": false, "IsMajorVersionUpgrade": false }, ...some output truncated... ] }`For more information, see [What Is Amazon Relational Database Service (Amazon RDS)?](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [DescribeDBEngineVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-engine-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-instance-automated-backups`.

- **AWS CLI**
- 
            
                    **To describe the automated backups for a DB instance**The following `describe-db-instance-automated-backups`example displays details about the automated backups for the specified DB instance. The details include replicated automated backups in other AWS Regions.`aws rds describe-db-instance-automated-backups \ --db-instance-identifier``new-orcl-db`Output: `{ "DBInstanceAutomatedBackups": [ { "DBInstanceArn": "arn:aws:rds:us-east-1:123456789012:db:new-orcl-db", "DbiResourceId": "db-JKIB2GFQ5RV7REPLZA4EXAMPLE", "Region": "us-east-1", "DBInstanceIdentifier": "new-orcl-db", "RestoreWindow": { "EarliestTime": "2020-12-07T21:05:20.939Z", "LatestTime": "2020-12-07T21:05:20.939Z" }, "AllocatedStorage": 20, "Status": "replicating", "Port": 1521, "InstanceCreateTime": "2020-12-04T15:28:31Z", "MasterUsername": "admin", "Engine": "oracle-se2", "EngineVersion": "12.1.0.2.v21", "LicenseModel": "bring-your-own-license", "OptionGroupName": "default:oracle-se2-12-1", "Encrypted": false, "StorageType": "gp2", "IAMDatabaseAuthenticationEnabled": false, "BackupRetentionPeriod": 14, "DBInstanceAutomatedBackupsArn": "arn:aws:rds:us-west-2:123456789012:auto-backup:ab-jkib2gfq5rv7replzadausbrktni2bn4example" } ] }`For more information, see [Finding information about replicated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReplicateBackups.html#AutomatedBackups.Replicating.Describe)in the*Amazon RDS User Guide*.- 
                    For API details, see [DescribeDbInstanceAutomatedBackups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-instance-automated-backups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-instances`.

- **AWS CLI**
- 
            
                    **To describe a DB instance**The following `describe-db-instances`example retrieves details about the specified DB instance.`aws rds describe-db-instances \ --db-instance-identifier``mydbinstancecf`Output: `{ "DBInstances": [ { "DBInstanceIdentifier": "mydbinstancecf", "DBInstanceClass": "db.t3.small", "Engine": "mysql", "DBInstanceStatus": "available", "MasterUsername": "masterawsuser", "Endpoint": { "Address": "mydbinstancecf.abcexample.us-east-1.rds.amazonaws.com", "Port": 3306, "HostedZoneId": "Z2R2ITUGPM61AM" }, ...some output truncated... } ] }`- 
                    For API details, see [DescribeDBInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-log-files`.

- **AWS CLI**
- 
            
                    **To describe the log files for a DB instance**The following `describe-db-log-files`example retrieves details about the log files for the specified DB instance.`aws rds describe-db-log-files \ --db-instance-identifier``test-instance`Output: `{ "DescribeDBLogFiles": [ { "Size": 0, "LastWritten": 1533060000000, "LogFileName": "error/mysql-error-running.log" }, { "Size": 2683, "LastWritten": 1532994300000, "LogFileName": "error/mysql-error-running.log.0" }, { "Size": 107, "LastWritten": 1533057300000, "LogFileName": "error/mysql-error-running.log.18" }, { "Size": 13105, "LastWritten": 1532991000000, "LogFileName": "error/mysql-error-running.log.23" }, { "Size": 0, "LastWritten": 1533061200000, "LogFileName": "error/mysql-error.log" }, { "Size": 3519, "LastWritten": 1532989252000, "LogFileName": "mysqlUpgrade" } ] }`- 
                    For API details, see [DescribeDbLogFiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-log-files.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-parameter-groups`.

- **AWS CLI**
- 
            
                    **To describe your DB parameter group**The following `describe-db-parameter-groups`example retrieves details about your DB parameter groups.`aws rds describe-db-parameter-groups`Output: `{ "DBParameterGroups": [ { "DBParameterGroupName": "default.aurora-mysql5.7", "DBParameterGroupFamily": "aurora-mysql5.7", "Description": "Default parameter group for aurora-mysql5.7", "DBParameterGroupArn": "arn:aws:rds:us-east-1:123456789012:pg:default.aurora-mysql5.7" }, { "DBParameterGroupName": "default.aurora-postgresql9.6", "DBParameterGroupFamily": "aurora-postgresql9.6", "Description": "Default parameter group for aurora-postgresql9.6", "DBParameterGroupArn": "arn:aws:rds:us-east-1:123456789012:pg:default.aurora-postgresql9.6" }, { "DBParameterGroupName": "default.aurora5.6", "DBParameterGroupFamily": "aurora5.6", "Description": "Default parameter group for aurora5.6", "DBParameterGroupArn": "arn:aws:rds:us-east-1:123456789012:pg:default.aurora5.6" }, { "DBParameterGroupName": "default.mariadb10.1", "DBParameterGroupFamily": "mariadb10.1", "Description": "Default parameter group for mariadb10.1", "DBParameterGroupArn": "arn:aws:rds:us-east-1:123456789012:pg:default.mariadb10.1" }, ...some output truncated... ] }`For more information, see [Working with DB Parameter Groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [DescribeDBParameterGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-parameter-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-parameters`.

- **AWS CLI**
- 
            
                    **To describe the parameters in a DB parameter group**The following `describe-db-parameters`example retrieves the details of the specified DB parameter group.`aws rds describe-db-parameters \ --db-parameter-group-name``mydbpg`Output: `{ "Parameters": [ { "ParameterName": "allow-suspicious-udfs", "Description": "Controls whether user-defined functions that have only an xxx symbol for the main function can be loaded", "Source": "engine-default", "ApplyType": "static", "DataType": "boolean", "AllowedValues": "0,1", "IsModifiable": false, "ApplyMethod": "pending-reboot" }, { "ParameterName": "auto_generate_certs", "Description": "Controls whether the server autogenerates SSL key and certificate files in the data directory, if they do not already exist.", "Source": "engine-default", "ApplyType": "static", "DataType": "boolean", "AllowedValues": "0,1", "IsModifiable": false, "ApplyMethod": "pending-reboot" }, ...some output truncated... ] }`For more information, see [Working with DB Parameter Groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [DescribeDBParameters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-parameters.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-proxies`.

- **AWS CLI**
- 
            
                    **To describe a DB proxy for an RDS database**The following `describe-db-proxies`example returns information about DB proxies.`aws rds describe-db-proxies`Output: `{ "DBProxies": [ { "DBProxyName": "proxyExample1", "DBProxyArn": "arn:aws:rds:us-east-1:123456789012:db-proxy:prx-0123a01b12345c0ab", "Status": "available", "EngineFamily": "PostgreSQL", "VpcId": "vpc-1234567", "VpcSecurityGroupIds": [ "sg-1234" ], "VpcSubnetIds": [ "subnetgroup1", "subnetgroup2" ], "Auth": "[ { "Description": "proxydescription1" "AuthScheme": "SECRETS", "SecretArn": "arn:aws:secretsmanager:us-west-2:123456789123:secret:secretName-1234f", "IAMAuth": "DISABLED" } ]", "RoleArn": "arn:aws:iam::12345678912??:role/ProxyPostgreSQLRole", "Endpoint": "proxyExample1.proxy-ab0cd1efghij.us-east-1.rds.amazonaws.com", "RequireTLS": false, "IdleClientTimeout": 1800, "DebuggingLogging": false, "CreatedDate": "2023-04-05T16:09:33.452000+00:00", "UpdatedDate": "2023-04-13T01:49:38.568000+00:00" }, { "DBProxyName": "proxyExample2", "DBProxyArn": "arn:aws:rds:us-east-1:123456789012:db-proxy:prx-1234a12b23456c1ab", "Status": "available", "EngineFamily": "PostgreSQL", "VpcId": "sg-1234567", "VpcSecurityGroupIds": [ "sg-1234" ], "VpcSubnetIds": [ "subnetgroup1", "subnetgroup2" ], "Auth": "[ { "Description": "proxydescription2" "AuthScheme": "SECRETS", "SecretArn": "aarn:aws:secretsmanager:us-west-2:123456789123:secret:secretName-1234f", "IAMAuth": "DISABLED" } ]", "RoleArn": "arn:aws:iam::12345678912:role/ProxyPostgreSQLRole", "Endpoint": "proxyExample2.proxy-ab0cd1efghij.us-east-1.rds.amazonaws.com", "RequireTLS": false, "IdleClientTimeout": 1800, "DebuggingLogging": false, "CreatedDate": "2022-01-05T16:19:33.452000+00:00", "UpdatedDate": "2023-04-13T01:49:38.568000+00:00" } ] }`For more information, see [Viewing an RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-setup.html#rds-proxy-viewing)in the*Amazon RDS User Guide*and[Viewing an RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-setup.html#rds-proxy-viewing)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DescribeDbProxies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-proxies.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-proxy-endpoints`.

- **AWS CLI**
- 
            
                    **To describe a DB proxy endpoints**The following `describe-db-proxy-endpoints`example returns information about DB proxy endpoints.`aws rds describe-db-proxy-endpoints`Output: `{ "DBProxyEndpoints": [ { "DBProxyEndpointName": "proxyEndpoint1", "DBProxyEndpointArn": "arn:aws:rds:us-east-1:123456789012:db-proxy-endpoint:prx-endpoint-0123a01b12345c0ab", "DBProxyName": "proxyExample", "Status": "available", "VpcId": "vpc-1234567", "VpcSecurityGroupIds": [ "sg-1234" ], "VpcSubnetIds": [ "subnetgroup1", "subnetgroup2" ], "Endpoint": "proxyEndpoint1.endpoint.proxy-ab0cd1efghij.us-east-1.rds.amazonaws.com", "CreatedDate": "2023-04-05T16:09:33.452000+00:00", "TargetRole": "READ_WRITE", "IsDefault": false }, { "DBProxyEndpointName": "proxyEndpoint2", "DBProxyEndpointArn": "arn:aws:rds:us-east-1:123456789012:db-proxy-endpoint:prx-endpoint-4567a01b12345c0ab", "DBProxyName": "proxyExample2", "Status": "available", "VpcId": "vpc1234567", "VpcSecurityGroupIds": [ "sg-5678" ], "VpcSubnetIds": [ "subnetgroup1", "subnetgroup2" ], "Endpoint": "proxyEndpoint2.endpoint.proxy-cd1ef2klmnop.us-east-1.rds.amazonaws.com", "CreatedDate": "2023-04-05T16:09:33.452000+00:00", "TargetRole": "READ_WRITE", "IsDefault": false } ] }`For more information, see [Viewing a proxy endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-endpoints.html#rds-proxy-endpoints.DescribingEndpoint)in the*Amazon RDS User Guide*and[Creating a proxy endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-endpoints.html#rds-proxy-endpoints.DescribingEndpoint)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DescribeDbProxyEndpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-proxy-endpoints.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-proxy-target-groups`.

- **AWS CLI**
- 
            
                    **To describe a DB proxy endpoints**The following `describe-db-proxy-target-groups`example returns information about DB proxy target groups.`aws rds describe-db-proxy-target-groups \ --db-proxy-name``proxyExample`Output: `{ "TargetGroups": { "DBProxyName": "proxyExample", "TargetGroupName": "default", "TargetGroupArn": "arn:aws:rds:us-east-1:123456789012:target-group:prx-tg-0123a01b12345c0ab", "IsDefault": true, "Status": "available", "ConnectionPoolConfig": { "MaxConnectionsPercent": 100, "MaxIdleConnectionsPercent": 50, "ConnectionBorrowTimeout": 120, "SessionPinningFilters": [] }, "CreatedDate": "2023-05-02T18:41:19.495000+00:00", "UpdatedDate": "2023-05-02T18:41:21.762000+00:00" } }`For more information, see [Viewing an RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-setup.html#rds-proxy-viewing)in the*Amazon RDS User Guide*and[Viewing an RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-setup.html#rds-proxy-viewing)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DescribeDbProxyTargetGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-proxy-target-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-proxy-targets`.

- **AWS CLI**
- 
            
                    **To describe DB proxy targets**The following `describe-db-proxy-targets`example returns information about DB proxy targets.`aws rds describe-db-proxy-targets \ --db-proxy-name``proxyExample`Output: `{ "Targets": [ { "Endpoint": "database1.ab0cd1efghij.us-east-1.rds.amazonaws.com", "TrackedClusterId": "database1", "RdsResourceId": "database1-instance-1", "Port": 3306, "Type": "RDS_INSTANCE", "Role": "READ_WRITE", "TargetHealth": { "State": "UNAVAILABLE", "Reason": "PENDING_PROXY_CAPACITY", "Description": "DBProxy Target is waiting for proxy to scale to desired capacity" } } ] }`For more information, see [Viewing an RDS proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-setup.html#rds-proxy-viewing)in the*Amazon RDS User Guide*and[Viewing an RDS proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-setup.html#rds-proxy-viewing)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DescribeDbProxyTargets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-proxy-targets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-recommendations`.

- **AWS CLI**
- 
            
                    **Example 1: To list all DB recommendations**The following `describe-db-recommendations`example lists all DB recommendations in your AWS account.`aws rds describe-db-recommendations`Output: `{ "DBRecommendations": [ { "RecommendationId": "12ab3cde-f456-7g8h-9012-i3j45678k9lm", "TypeId": "config_recommendation::old_minor_version", "Severity": "informational", "ResourceArn": "arn:aws:rds:us-west-2:111122223333:db:database-1", "Status": "active", "CreatedTime": "2024-02-21T23:14:19.292000+00:00", "UpdatedTime": "2024-02-21T23:14:19+00:00", "Detection": "**[resource-name]** is not running the latest minor DB engine version", "Recommendation": "Upgrade to latest engine version", "Description": "Your database resources aren't running the latest minor DB engine version. The latest minor version contains the latest security fixes and other improvements.", "RecommendedActions": [ { "ActionId": "12ab34c5de6fg7h89i0jk1lm234n5678", "Operation": "modifyDbInstance", "Parameters": [ { "Key": "EngineVersion", "Value": "5.7.44" }, { "Key": "DBInstanceIdentifier", "Value": "database-1" } ], "ApplyModes": [ "immediately", "next-maintenance-window" ], "Status": "ready", "ContextAttributes": [ { "Key": "Recommended value", "Value": "5.7.44" }, { "Key": "Current engine version", "Value": "5.7.42" } ] } ], "Category": "security", "Source": "RDS", "TypeDetection": "**[resource-count] resources** are not running the latest minor DB engine version", "TypeRecommendation": "Upgrade to latest engine version", "Impact": "Reduced database performance and data security at risk", "AdditionalInfo": "We recommend that you maintain your database with the latest DB engine minor version as this version includes the latest security and functionality fixes. The DB engine minor version upgrades contain only the changes which are backward-compatible with earlier minor versions of the same major version of the DB engine.", "Links": [ { "Text": "Upgrading an RDS DB instance engine version", "Url": "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html" }, { "Text": "Using Amazon RDS Blue/Green Deployments for database updates for Amazon Aurora", "Url": "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html" }, { "Text": "Using Amazon RDS Blue/Green Deployments for database updates for Amazon RDS", "Url": "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html" } ] } ] }`For more information, see [Viewing and responding to Amazon RDS recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/monitoring-recommendations.html)in the*Amazon RDS User Guide*and[Viewing and responding to Amazon RDS recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/monitoring-recommendations.html)in the*Amazon Aurora User Guide*.**Example 2: To list high severity DB recommendations**The following `describe-db-recommendations`example lists high severity DB recommendations in your AWS account.`aws rds describe-db-recommendations \ --filters``Name=severity,Values=high`Output: `{ "DBRecommendations": [ { "RecommendationId": "12ab3cde-f456-7g8h-9012-i3j45678k9lm", "TypeId": "config_recommendation::rds_extended_support", "Severity": "high", "ResourceArn": "arn:aws:rds:us-west-2:111122223333:db:database-1", "Status": "active", "CreatedTime": "2024-02-21T23:14:19.392000+00:00", "UpdatedTime": "2024-02-21T23:14:19+00:00", "Detection": "Your databases will be auto-enrolled to RDS Extended Support on February 29", "Recommendation": "Upgrade your major version before February 29, 2024 to avoid additional charges", "Description": "Your PostgreSQL 11 and MySQL 5.7 databases will be automatically enrolled into RDS Extended Support on February 29, 2024. To avoid the increase in charges due to RDS Extended Support, we recommend upgrading your databases to a newer major engine version before February 29, 2024.\nTo learn more about the RDS Extended Support pricing, refer to the pricing page.", "RecommendedActions": [ { "ActionId": "12ab34c5de6fg7h89i0jk1lm234n5678", "Parameters": [], "ApplyModes": [ "manual" ], "Status": "ready", "ContextAttributes": [] } ], "Category": "cost optimization", "Source": "RDS", "TypeDetection": "Your database will be auto-enrolled to RDS Extended Support on February 29", "TypeRecommendation": "Upgrade your major version before February 29, 2024 to avoid additional charges", "Impact": "Increase in charges due to RDS Extended Support", "AdditionalInfo": "With Amazon RDS Extended Support, you can continue running your database on a major engine version past the RDS end of standard support date for an additional cost. This paid feature gives you more time to upgrade to a supported major engine version.\nDuring Extended Support, Amazon RDS will supply critical CVE patches and bug fixes.", "Links": [ { "Text": "Amazon RDS Extended Support pricing for RDS for MySQL", "Url": "https://aws.amazon.com/rds/mysql/pricing/" }, { "Text": "Amazon RDS Extended Support for RDS for MySQL and PostgreSQL databases", "Url": "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support.html" }, { "Text": "Amazon RDS Extended Support pricing for Amazon Aurora PostgreSQL", "Url": "https://aws.amazon.com/rds/aurora/pricing/" }, { "Text": "Amazon RDS Extended Support for Aurora PostgreSQL databases", "Url": "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support.html" }, { "Text": "Amazon RDS Extended Support pricing for RDS for PostgreSQL", "Url": "https://aws.amazon.com/rds/postgresql/pricing/" } ] } ] }`For more information, see [Viewing and responding to Amazon RDS recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/monitoring-recommendations.html)in the*Amazon RDS User Guide*and[Viewing and responding to Amazon RDS recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/monitoring-recommendations.html)in the*Amazon Aurora User Guide*.**Example 3: To list DB recommendations for a specified DB instance**The following `describe-db-recommendations`example lists all DB recommendations for a specified DB instance.`aws rds describe-db-recommendations \ --filters``Name=dbi-resource-id,Values=database-1`Output: `{ "DBRecommendations": [ { "RecommendationId": "12ab3cde-f456-7g8h-9012-i3j45678k9lm", "TypeId": "config_recommendation::old_minor_version", "Severity": "informational", "ResourceArn": "arn:aws:rds:us-west-2:111122223333:db:database-1", "Status": "active", "CreatedTime": "2024-02-21T23:14:19.292000+00:00", "UpdatedTime": "2024-02-21T23:14:19+00:00", "Detection": "**[resource-name]** is not running the latest minor DB engine version", "Recommendation": "Upgrade to latest engine version", "Description": "Your database resources aren't running the latest minor DB engine version. The latest minor version contains the latest security fixes and other improvements.", "RecommendedActions": [ { "ActionId": "12ab34c5de6fg7h89i0jk1lm234n5678", "Operation": "modifyDbInstance", "Parameters": [ { "Key": "EngineVersion", "Value": "5.7.44" }, { "Key": "DBInstanceIdentifier", "Value": "database-1" } ], "ApplyModes": [ "immediately", "next-maintenance-window" ], "Status": "ready", "ContextAttributes": [ { "Key": "Recommended value", "Value": "5.7.44" }, { "Key": "Current engine version", "Value": "5.7.42" } ] } ], "Category": "security", "Source": "RDS", "TypeDetection": "**[resource-count] resources** are not running the latest minor DB engine version", "TypeRecommendation": "Upgrade to latest engine version", "Impact": "Reduced database performance and data security at risk", "AdditionalInfo": "We recommend that you maintain your database with the latest DB engine minor version as this version includes the latest security and functionality fixes. The DB engine minor version upgrades contain only the changes which are backward-compatible with earlier minor versions of the same major version of the DB engine.", "Links": [ { "Text": "Upgrading an RDS DB instance engine version", "Url": "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html" }, { "Text": "Using Amazon RDS Blue/Green Deployments for database updates for Amazon Aurora", "Url": "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html" }, { "Text": "Using Amazon RDS Blue/Green Deployments for database updates for Amazon RDS", "Url": "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html" } ] } ] }`For more information, see [Viewing and responding to Amazon RDS recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/monitoring-recommendations.html)in the*Amazon RDS User Guide*and[Viewing and responding to Amazon RDS recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/monitoring-recommendations.html)in the*Amazon Aurora User Guide*.**Example 4: To list all active DB recommendations**The following `describe-db-recommendations`example lists all active DB recommendations in your AWS account.`aws rds describe-db-recommendations \ --filters``Name=status,Values=active`Output: `{ "DBRecommendations": [ { "RecommendationId": "12ab3cde-f456-7g8h-9012-i3j45678k9lm", "TypeId": "config_recommendation::old_minor_version", "Severity": "informational", "ResourceArn": "arn:aws:rds:us-west-2:111122223333:db:database-1", "Status": "active", "CreatedTime": "2024-02-21T23:14:19.292000+00:00", "UpdatedTime": "2024-02-21T23:14:19+00:00", "Detection": "**[resource-name]** is not running the latest minor DB engine version", "Recommendation": "Upgrade to latest engine version", "Description": "Your database resources aren't running the latest minor DB engine version. The latest minor version contains the latest security fixes and other improvements.", "RecommendedActions": [ { "ActionId": "12ab34c5de6fg7h89i0jk1lm234n5678", "Operation": "modifyDbInstance", "Parameters": [ { "Key": "EngineVersion", "Value": "5.7.44" }, { "Key": "DBInstanceIdentifier", "Value": "database-1" } ], "ApplyModes": [ "immediately", "next-maintenance-window" ], "Status": "ready", "ContextAttributes": [ { "Key": "Recommended value", "Value": "5.7.44" }, { "Key": "Current engine version", "Value": "5.7.42" } ] } ], "Category": "security", "Source": "RDS", "TypeDetection": "**[resource-count] resources** are not running the latest minor DB engine version", "TypeRecommendation": "Upgrade to latest engine version", "Impact": "Reduced database performance and data security at risk", "AdditionalInfo": "We recommend that you maintain your database with the latest DB engine minor version as this version includes the latest security and functionality fixes. The DB engine minor version upgrades contain only the changes which are backward-compatible with earlier minor versions of the same major version of the DB engine.", "Links": [ { "Text": "Upgrading an RDS DB instance engine version", "Url": "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html" }, { "Text": "Using Amazon RDS Blue/Green Deployments for database updates for Amazon Aurora", "Url": "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html" }, { "Text": "Using Amazon RDS Blue/Green Deployments for database updates for Amazon RDS", "Url": "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html" } ] } ] }`For more information, see [Viewing and responding to Amazon RDS recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/monitoring-recommendations.html)in the*Amazon RDS User Guide*and[Viewing and responding to Amazon RDS recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/monitoring-recommendations.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DescribeDbRecommendations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-recommendations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-security-groups`.

- **AWS CLI**
- 
            
                    **To list DB security groups**The following `describe-db-security-groups`example lists DB security groups.`aws rds describe-db-security-groups`Output: `{ "DBSecurityGroups": [ { "OwnerId": "123456789012", "DBSecurityGroupName": "default", "DBSecurityGroupDescription": "default", "EC2SecurityGroups": [], "IPRanges": [], "DBSecurityGroupArn": "arn:aws:rds:us-west-1:111122223333:secgrp:default" }, { "OwnerId": "123456789012", "DBSecurityGroupName": "mysecgroup", "DBSecurityGroupDescription": "My Test Security Group", "VpcId": "vpc-1234567f", "EC2SecurityGroups": [], "IPRanges": [], "DBSecurityGroupArn": "arn:aws:rds:us-west-1:111122223333:secgrp:mysecgroup" } ] }`For more information, see [Listing Available DB Security Groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithSecurityGroups.html#USER_WorkingWithSecurityGroups.Listing)in the*Amazon RDS User Guide*.- 
                    For API details, see [DescribeDbSecurityGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-security-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-shard-groups`.

- **AWS CLI**
- 
            
                    **Example 1: To describe DB shard groups**The following `describe-db-shard-groups`example retrieves the details of your DB shard groups.`aws rds describe-db-shard-groups`Output: `{ "DBShardGroups": [ { "DBShardGroupResourceId": "shardgroup-7bb446329da94788b3f957746example", "DBShardGroupIdentifier": "limitless-test-shard-grp", "DBClusterIdentifier": "limitless-test-cluster", "MaxACU": 768.0, "ComputeRedundancy": 0, "Status": "available", "PubliclyAccessible": true, "Endpoint": "limitless-test-cluster.limitless-cekycexample.us-east-2.rds.amazonaws.com" }, { "DBShardGroupResourceId": "shardgroup-a6e3a0226aa243e2ac6c7a1234567890", "DBShardGroupIdentifier": "my-db-shard-group", "DBClusterIdentifier": "my-sv2-cluster", "MaxACU": 768.0, "ComputeRedundancy": 0, "Status": "available", "PubliclyAccessible": false, "Endpoint": "my-sv2-cluster.limitless-cekycexample.us-east-2.rds.amazonaws.com" } ] }`For more information, see [Amazon Aurora DB Clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DescribeDbShardGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-shard-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-snapshot-attributes`.

- **AWS CLI**
- 
            
                    **To describe the attribute names and values for a DB snapshot**The following `describe-db-snapshot-attributes`example describes the attribute names and values for a DB snapshot.`aws rds describe-db-snapshot-attributes \ --db-snapshot-identifier``mydbsnapshot`Output: `{ "DBSnapshotAttributesResult": { "DBSnapshotIdentifier": "mydbsnapshot", "DBSnapshotAttributes": [ { "AttributeName": "restore", "AttributeValues": [ "123456789012", "210987654321" ] } ] } }`For more information, see [Sharing a DB Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ShareSnapshot.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [DescribeDbSnapshotAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-snapshot-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-snapshots`.

- **AWS CLI**
- 
            
                    **Example 1: To describe a DB snapshot for a DB instance**The following `describe-db-snapshots`example retrieves the details of a DB snapshot for a DB instance.`aws rds describe-db-snapshots \ --db-snapshot-identifier``mydbsnapshot`Output: `{ "DBSnapshots": [ { "DBSnapshotIdentifier": "mydbsnapshot", "DBInstanceIdentifier": "mysqldb", "SnapshotCreateTime": "2018-02-08T22:28:08.598Z", "Engine": "mysql", "AllocatedStorage": 20, "Status": "available", "Port": 3306, "AvailabilityZone": "us-east-1f", "VpcId": "vpc-6594f31c", "InstanceCreateTime": "2018-02-08T22:24:55.973Z", "MasterUsername": "mysqladmin", "EngineVersion": "5.6.37", "LicenseModel": "general-public-license", "SnapshotType": "manual", "OptionGroupName": "default:mysql-5-6", "PercentProgress": 100, "StorageType": "gp2", "Encrypted": false, "DBSnapshotArn": "arn:aws:rds:us-east-1:123456789012:snapshot:mydbsnapshot", "IAMDatabaseAuthenticationEnabled": false, "ProcessorFeatures": [], "DbiResourceId": "db-AKIAIOSFODNN7EXAMPLE" } ] }`For more information, see [Creating a DB Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateSnapshot.html)in the*Amazon RDS User Guide*.**Example 2: To find the number of manual snapshots taken**The following `describe-db-snapshots`example uses the`length`operator in the`--query`option to return the number of manual snapshots that have been taken in a particular AWS Region.`aws rds describe-db-snapshots \ --snapshot-type``manual`\ --query`"length(*[].{DBSnapshots:SnapshotType})"`\ --region`eu-central-1`Output: `35`For more information, see [Creating a DB Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateSnapshot.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [DescribeDBSnapshots](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-snapshots.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-subnet-groups`.

- **AWS CLI**
- 
            
                    **To describe a DB subnet group**The following `describe-db-subnet-groups`example retrieves the details of the specified DB subnet group.`aws rds describe-db-subnet-groups`Output: `{ "DBSubnetGroups": [ { "DBSubnetGroupName": "mydbsubnetgroup", "DBSubnetGroupDescription": "My DB Subnet Group", "VpcId": "vpc-971c12ee", "SubnetGroupStatus": "Complete", "Subnets": [ { "SubnetIdentifier": "subnet-d8c8e7f4", "SubnetAvailabilityZone": { "Name": "us-east-1a" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-718fdc7d", "SubnetAvailabilityZone": { "Name": "us-east-1f" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-cbc8e7e7", "SubnetAvailabilityZone": { "Name": "us-east-1a" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-0ccde220", "SubnetAvailabilityZone": { "Name": "us-east-1a" }, "SubnetStatus": "Active" } ], "DBSubnetGroupArn": "arn:aws:rds:us-east-1:123456789012:subgrp:mydbsubnetgroup" } ] }`For more information, see [Amazon Virtual Private Cloud VPCs and Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [DescribeDbSubnetGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-db-subnet-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-engine-default-cluster-parameters`.

- **AWS CLI**
- 
            
                    **To describe the default engine and system parameter information for the Aurora database engine**The following `describe-engine-default-cluster-parameters`example retrieves the details of the default engine and system parameter information for Aurora DB clusters with MySQL 5.7 compatibility.`aws rds describe-engine-default-cluster-parameters \ --db-parameter-group-family``aurora-mysql5.7`Output: `{ "EngineDefaults": { "Parameters": [ { "ParameterName": "aurora_load_from_s3_role", "Description": "IAM role ARN used to load data from AWS S3", "Source": "engine-default", "ApplyType": "dynamic", "DataType": "string", "IsModifiable": true, "SupportedEngineModes": [ "provisioned" ] }, ...some output truncated... ] } }`For more information, see [Working with DB Parameter Groups and DB Cluster Parameter Groups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DescribeEngineDefaultClusterParameters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-engine-default-cluster-parameters.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-engine-default-parameters`.

- **AWS CLI**
- 
            
                    **To describe the default engine and system parameter information for the database engine**The following `describe-engine-default-parameters`example retrieves details for the default engine and system parameter information for MySQL 5.7 DB instances.`aws rds describe-engine-default-parameters \ --db-parameter-group-family``mysql5.7`Output: `{ "EngineDefaults": { "Parameters": [ { "ParameterName": "allow-suspicious-udfs", "Description": "Controls whether user-defined functions that have only an xxx symbol for the main function can be loaded", "Source": "engine-default", "ApplyType": "static", "DataType": "boolean", "AllowedValues": "0,1", "IsModifiable": false }, ...some output truncated... ] } }`For more information, see [Working with DB Parameter Groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [DescribeEngineDefaultParameters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-engine-default-parameters.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-event-categories`.

- **AWS CLI**
- 
            
                    **To describe event categories**The following `describe-event-categories`example retrieves details about the event categories for all available event sources.`aws rds describe-event-categories`Output: `{ "EventCategoriesMapList": [ { "SourceType": "db-instance", "EventCategories": [ "deletion", "read replica", "failover", "restoration", "maintenance", "low storage", "configuration change", "backup", "creation", "availability", "recovery", "failure", "backtrack", "notification" ] }, { "SourceType": "db-security-group", "EventCategories": [ "configuration change", "failure" ] }, { "SourceType": "db-parameter-group", "EventCategories": [ "configuration change" ] }, { "SourceType": "db-snapshot", "EventCategories": [ "deletion", "creation", "restoration", "notification" ] }, { "SourceType": "db-cluster", "EventCategories": [ "failover", "failure", "notification" ] }, { "SourceType": "db-cluster-snapshot", "EventCategories": [ "backup" ] } ] }`- 
                    For API details, see [DescribeEventCategories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-event-categories.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-event-subscriptions`.

- **AWS CLI**
- 
            
                    **To describe event subscriptions**This example describes all of the Amazon RDS event subscriptions for the current AWS account. `aws rds describe-event-subscriptions`Output: `{ "EventSubscriptionsList": [ { "EventCategoriesList": [ "backup", "recovery" ], "Enabled": true, "EventSubscriptionArn": "arn:aws:rds:us-east-1:123456789012:es:my-instance-events", "Status": "creating", "SourceType": "db-instance", "CustomerAwsId": "123456789012", "SubscriptionCreationTime": "2018-07-31 23:22:01.893", "CustSubscriptionId": "my-instance-events", "SnsTopicArn": "arn:aws:sns:us-east-1:123456789012:interesting-events" }, ...some output truncated... ] }`- 
                    For API details, see [DescribeEventSubscriptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-event-subscriptions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-events`.

- **AWS CLI**
- 
            
                    **To describe events**The following `describe-events`example retrieves details for the events that have occurred for the specified DB instance.`aws rds describe-events \ --source-identifier``test-instance`\ --source-type`db-instance`Output: `{ "Events": [ { "SourceType": "db-instance", "SourceIdentifier": "test-instance", "EventCategories": [ "backup" ], "Message": "Backing up DB instance", "Date": "2018-07-31T23:09:23.983Z", "SourceArn": "arn:aws:rds:us-east-1:123456789012:db:test-instance" }, { "SourceType": "db-instance", "SourceIdentifier": "test-instance", "EventCategories": [ "backup" ], "Message": "Finished DB Instance backup", "Date": "2018-07-31T23:15:13.049Z", "SourceArn": "arn:aws:rds:us-east-1:123456789012:db:test-instance" } ] }`- 
                    For API details, see [DescribeEvents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-events.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-export-tasks`.

- **AWS CLI**
- 
            
                    **To describe snapshot export tasks**The following `describe-export-tasks`example returns information about snapshot exports to Amazon S3.`aws rds describe-export-tasks`Output: `{ "ExportTasks": [ { "ExportTaskIdentifier": "test-snapshot-export", "SourceArn": "arn:aws:rds:us-west-2:123456789012:snapshot:test-snapshot", "SnapshotTime": "2020-03-02T18:26:28.163Z", "TaskStartTime": "2020-03-02T18:57:56.896Z", "TaskEndTime": "2020-03-02T19:10:31.985Z", "S3Bucket": "amzn-s3-demo-bucket", "S3Prefix": "", "IamRoleArn": "arn:aws:iam::123456789012:role/service-role/ExportRole", "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/abcd0000-7fca-4128-82f2-aabbccddeeff", "Status": "COMPLETE", "PercentProgress": 100, "TotalExtractedDataInGB": 0 }, { "ExportTaskIdentifier": "my-s3-export", "SourceArn": "arn:aws:rds:us-west-2:123456789012:snapshot:db5-snapshot-test", "SnapshotTime": "2020-03-27T20:48:42.023Z", "S3Bucket": "amzn-s3-demo-bucket", "S3Prefix": "", "IamRoleArn": "arn:aws:iam::123456789012:role/service-role/ExportRole", "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/abcd0000-7fca-4128-82f2-aabbccddeeff", "Status": "STARTING", "PercentProgress": 0, "TotalExtractedDataInGB": 0 } ] }`For more information, see [Monitoring Snapshot Exports](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ExportSnapshot.html#USER_ExportSnapshot.Monitoring)in the*Amazon RDS User Guide*.- 
                    For API details, see [DescribeExportTasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-export-tasks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-global-clusters`.

- **AWS CLI**
- 
            
                    **To describe global DB clusters**The following `describe-global-clusters`example lists Aurora global DB clusters in the current AWS Region.`aws rds describe-global-clusters`Output: `{ "GlobalClusters": [ { "GlobalClusterIdentifier": "myglobalcluster", "GlobalClusterResourceId": "cluster-f5982077e3b5aabb", "GlobalClusterArn": "arn:aws:rds::123456789012:global-cluster:myglobalcluster", "Status": "available", "Engine": "aurora-mysql", "EngineVersion": "5.7.mysql_aurora.2.07.2", "StorageEncrypted": false, "DeletionProtection": false, "GlobalClusterMembers": [] } ] }`For more information, see [Managing an Aurora global database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-managing.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [DescribeGlobalClusters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-global-clusters.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-option-group-options`.

- **AWS CLI**
- 
            
                    **To describe all available options**The following `describe-option-group-options`example lists two options for an Oracle Database 19c instance.`aws rds describe-option-group-options \ --engine-name``oracle-ee`\ --major-engine-version`19`\ --max-items`2`Output: `{ "OptionGroupOptions": [ { "Name": "APEX", "Description": "Oracle Application Express Runtime Environment", "EngineName": "oracle-ee", "MajorEngineVersion": "19", "MinimumRequiredMinorEngineVersion": "0.0.0.ru-2019-07.rur-2019-07.r1", "PortRequired": false, "OptionsDependedOn": [], "OptionsConflictsWith": [], "Persistent": false, "Permanent": false, "RequiresAutoMinorEngineVersionUpgrade": false, "VpcOnly": false, "SupportsOptionVersionDowngrade": false, "OptionGroupOptionSettings": [], "OptionGroupOptionVersions": [ { "Version": "19.1.v1", "IsDefault": true }, { "Version": "19.2.v1", "IsDefault": false } ] }, { "Name": "APEX-DEV", "Description": "Oracle Application Express Development Environment", "EngineName": "oracle-ee", "MajorEngineVersion": "19", "MinimumRequiredMinorEngineVersion": "0.0.0.ru-2019-07.rur-2019-07.r1", "PortRequired": false, "OptionsDependedOn": [ "APEX" ], "OptionsConflictsWith": [], "Persistent": false, "Permanent": false, "RequiresAutoMinorEngineVersionUpgrade": false, "VpcOnly": false, "OptionGroupOptionSettings": [] } ], "NextToken": "eyJNYXJrZXIiOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAyfQ==" }`For more information, see [Listing the Options and Option Settings for an Option Group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.html#USER_WorkingWithOptionGroups.ListOption)in the*Amazon RDS User Guide*.- 
                    For API details, see [DescribeOptionGroupOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-option-group-options.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-option-groups`.

- **AWS CLI**
- 
            
                    **To describe the available option groups**The following `describe-option-groups`example lists the options groups for an Oracle Database 19c instance.`aws rds describe-option-groups \ --engine-name``oracle-ee`\ --major-engine-version`19`Output: `{ "OptionGroupsList": [ { "OptionGroupName": "default:oracle-ee-19", "OptionGroupDescription": "Default option group for oracle-ee 19", "EngineName": "oracle-ee", "MajorEngineVersion": "19", "Options": [], "AllowsVpcAndNonVpcInstanceMemberships": true, "OptionGroupArn": "arn:aws:rds:us-west-1:111122223333:og:default:oracle-ee-19" } ] }`For more information, see [Listing the Options and Option Settings for an Option Group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.html#USER_WorkingWithOptionGroups.ListOption)in the*Amazon RDS User Guide*.- 
                    For API details, see [DescribeOptionGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-option-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-orderable-db-instance-options`.

- **AWS CLI**
- 
            
                    **To describe orderable DB instance options**The following `describe-orderable-db-instance-options`example retrieves details about the orderable options for a DB instances running the MySQL DB engine.`aws rds describe-orderable-db-instance-options \ --engine``mysql`Output: `{ "OrderableDBInstanceOptions": [ { "MinStorageSize": 5, "ReadReplicaCapable": true, "MaxStorageSize": 6144, "AvailabilityZones": [ { "Name": "us-east-1a" }, { "Name": "us-east-1b" }, { "Name": "us-east-1c" }, { "Name": "us-east-1d" } ], "SupportsIops": false, "AvailableProcessorFeatures": [], "MultiAZCapable": true, "DBInstanceClass": "db.m1.large", "Vpc": true, "StorageType": "gp2", "LicenseModel": "general-public-license", "EngineVersion": "5.5.46", "SupportsStorageEncryption": false, "SupportsEnhancedMonitoring": true, "Engine": "mysql", "SupportsIAMDatabaseAuthentication": false, "SupportsPerformanceInsights": false } ] ...some output truncated... }`- 
                    For API details, see [DescribeOrderableDBInstanceOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-orderable-db-instance-options.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-pending-maintenance-actions`.

- **AWS CLI**
- 
            
                    **To list resources with at least one pending maintenance action**The following `describe-pending-maintenance-actions`example lists the pending maintenance action for a DB instance.`aws rds describe-pending-maintenance-actions`Output: `{ "PendingMaintenanceActions": [ { "ResourceIdentifier": "arn:aws:rds:us-west-2:123456789012:cluster:global-db1-cl1", "PendingMaintenanceActionDetails": [ { "Action": "system-update", "Description": "Upgrade to Aurora PostgreSQL 2.4.2" } ] } ] }`For more information, see [Maintaining a DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [DescribePendingMaintenanceActions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-pending-maintenance-actions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-reserved-db-instances-offerings`.

- **AWS CLI**
- 
            
                    **To describe reserved DB instance offerings**The following `describe-reserved-db-instances-offerings`example retrieves details about reserved DB instance options for`oracle`.`aws rds describe-reserved-db-instances-offerings \ --product-description``oracle`Output: `{ "ReservedDBInstancesOfferings": [ { "CurrencyCode": "USD", "UsagePrice": 0.0, "ProductDescription": "oracle-se2(li)", "ReservedDBInstancesOfferingId": "005bdee3-9ef4-4182-aa0c-58ef7cb6c2f8", "MultiAZ": true, "DBInstanceClass": "db.m4.xlarge", "OfferingType": "Partial Upfront", "RecurringCharges": [ { "RecurringChargeAmount": 0.594, "RecurringChargeFrequency": "Hourly" } ], "FixedPrice": 4089.0, "Duration": 31536000 }, ...some output truncated... }`- 
                    For API details, see [DescribeReservedDbInstancesOfferings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-reserved-db-instances-offerings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-reserved-db-instances`.

- **AWS CLI**
- 
            
                    **To describe reserved DB instances**The following `describe-reserved-db-instances`example retrieves details about any reserved DB instances in the current AWS account.`aws rds describe-reserved-db-instances`Output: `{ "ReservedDBInstances": [ { "ReservedDBInstanceId": "myreservedinstance", "ReservedDBInstancesOfferingId": "12ab34cd-59af-4b2c-a660-1abcdef23456", "DBInstanceClass": "db.t3.micro", "StartTime": "2020-06-01T13:44:21.436Z", "Duration": 31536000, "FixedPrice": 0.0, "UsagePrice": 0.0, "CurrencyCode": "USD", "DBInstanceCount": 1, "ProductDescription": "sqlserver-ex(li)", "OfferingType": "No Upfront", "MultiAZ": false, "State": "payment-pending", "RecurringCharges": [ { "RecurringChargeAmount": 0.014, "RecurringChargeFrequency": "Hourly" } ], "ReservedDBInstanceArn": "arn:aws:rds:us-west-2:123456789012:ri:myreservedinstance", "LeaseId": "a1b2c3d4-6b69-4a59-be89-5e11aa446666" } ] }`For more information, see [Reserved DB Instances for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [DescribeReservedDbInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-reserved-db-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-source-regions`.

- **AWS CLI**
- 
            
                    **To describe source Regions**The following `describe-source-regions`example retrieves details about all source AWS Regions. It also shows that automated backups can be replicated only from US West (Oregon) to the destination AWS Region, US East (N. Virginia).`aws rds describe-source-regions \ --region``us-east-1`Output: `{ "SourceRegions": [ { "RegionName": "af-south-1", "Endpoint": "https://rds.af-south-1.amazonaws.com", "Status": "available", "SupportsDBInstanceAutomatedBackupsReplication": false }, { "RegionName": "ap-east-1", "Endpoint": "https://rds.ap-east-1.amazonaws.com", "Status": "available", "SupportsDBInstanceAutomatedBackupsReplication": false }, { "RegionName": "ap-northeast-1", "Endpoint": "https://rds.ap-northeast-1.amazonaws.com", "Status": "available", "SupportsDBInstanceAutomatedBackupsReplication": true }, { "RegionName": "ap-northeast-2", "Endpoint": "https://rds.ap-northeast-2.amazonaws.com", "Status": "available", "SupportsDBInstanceAutomatedBackupsReplication": true }, { "RegionName": "ap-northeast-3", "Endpoint": "https://rds.ap-northeast-3.amazonaws.com", "Status": "available", "SupportsDBInstanceAutomatedBackupsReplication": false }, { "RegionName": "ap-south-1", "Endpoint": "https://rds.ap-south-1.amazonaws.com", "Status": "available", "SupportsDBInstanceAutomatedBackupsReplication": true }, { "RegionName": "ap-southeast-1", "Endpoint": "https://rds.ap-southeast-1.amazonaws.com", "Status": "available", "SupportsDBInstanceAutomatedBackupsReplication": true }, { "RegionName": "ap-southeast-2", "Endpoint": "https://rds.ap-southeast-2.amazonaws.com", "Status": "available", "SupportsDBInstanceAutomatedBackupsReplication": true }, { "RegionName": "ap-southeast-3", "Endpoint": "https://rds.ap-southeast-3.amazonaws.com", "Status": "available", "SupportsDBInstanceAutomatedBackupsReplication": false }, { "RegionName": "ca-central-1", "Endpoint": "https://rds.ca-central-1.amazonaws.com", "Status": "available", "SupportsDBInstanceAutomatedBackupsReplication": true }, { "RegionName": "eu-north-1", "Endpoint": "https://rds.eu-north-1.amazonaws.com", "Status": "available", "SupportsDBInstanceAutomatedBackupsReplication": true }, { "RegionName": "eu-south-1", "Endpoint": "https://rds.eu-south-1.amazonaws.com", "Status": "available", "SupportsDBInstanceAutomatedBackupsReplication": false }, { "RegionName": "eu-west-1", "Endpoint": "https://rds.eu-west-1.amazonaws.com", "Status": "available", "SupportsDBInstanceAutomatedBackupsReplication": true }, { "RegionName": "eu-west-2", "Endpoint": "https://rds.eu-west-2.amazonaws.com", "Status": "available", "SupportsDBInstanceAutomatedBackupsReplication": true }, { "RegionName": "eu-west-3", "Endpoint": "https://rds.eu-west-3.amazonaws.com", "Status": "available", "SupportsDBInstanceAutomatedBackupsReplication": true }, { "RegionName": "me-central-1", "Endpoint": "https://rds.me-central-1.amazonaws.com", "Status": "available", "SupportsDBInstanceAutomatedBackupsReplication": false }, { "RegionName": "me-south-1", "Endpoint": "https://rds.me-south-1.amazonaws.com", "Status": "available", "SupportsDBInstanceAutomatedBackupsReplication": false }, { "RegionName": "sa-east-1", "Endpoint": "https://rds.sa-east-1.amazonaws.com", "Status": "available", "SupportsDBInstanceAutomatedBackupsReplication": true }, { "RegionName": "us-east-2", "Endpoint": "https://rds.us-east-2.amazonaws.com", "Status": "available", "SupportsDBInstanceAutomatedBackupsReplication": true }, { "RegionName": "us-west-1", "Endpoint": "https://rds.us-west-1.amazonaws.com", "Status": "available", "SupportsDBInstanceAutomatedBackupsReplication": true }, { "RegionName": "us-west-2", "Endpoint": "https://rds.us-west-2.amazonaws.com", "Status": "available", "SupportsDBInstanceAutomatedBackupsReplication": true } ] }`For more information, see [Finding information about replicated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReplicateBackups.html#AutomatedBackups.Replicating.Describe)in the*Amazon RDS User Guide*.- 
                    For API details, see [DescribeSourceRegions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-source-regions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-valid-db-instance-modifications`.

- **AWS CLI**
- 
            
                    **To describe valid modifications for a DB instance**The following `describe-valid-db-instance-modifications`example retrieves details about the valid modifications for the specified DB instance.`aws rds describe-valid-db-instance-modifications \ --db-instance-identifier``test-instance`Output: `{ "ValidDBInstanceModificationsMessage": { "ValidProcessorFeatures": [], "Storage": [ { "StorageSize": [ { "Step": 1, "To": 20, "From": 20 }, { "Step": 1, "To": 6144, "From": 22 } ], "ProvisionedIops": [ { "Step": 1, "To": 0, "From": 0 } ], "IopsToStorageRatio": [ { "To": 0.0, "From": 0.0 } ], "StorageType": "gp2" }, { "StorageSize": [ { "Step": 1, "To": 6144, "From": 100 } ], "ProvisionedIops": [ { "Step": 1, "To": 40000, "From": 1000 } ], "IopsToStorageRatio": [ { "To": 50.0, "From": 1.0 } ], "StorageType": "io1" }, { "StorageSize": [ { "Step": 1, "To": 20, "From": 20 }, { "Step": 1, "To": 3072, "From": 22 } ], "ProvisionedIops": [ { "Step": 1, "To": 0, "From": 0 } ], "IopsToStorageRatio": [ { "To": 0.0, "From": 0.0 } ], "StorageType": "magnetic" } ] } }`- 
                    For API details, see [DescribeValidDbInstanceModifications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-valid-db-instance-modifications.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `download-db-log-file-portion`.

- **AWS CLI**
- 
            
                    **Example 1: To download the latest part of a DB log file**The following `download-db-log-file-portion`example downloads only the latest part of your log file, saving it to a local file named`tail.txt`.`aws rds download-db-log-file-portion \ --db-instance-identifier``test-instance`\ --log-file-name`log.txt`\ --output`text``>``tail.txt`The saved file might contain blank lines. They appear at the end of each part of the log file while being downloaded. **Example 2: To download an entire DB log file**The following `download-db-log-file-portion`example downloads the entire log file, using the`--starting-token 0`parameter, and saves the output to a local file named`full.txt`.`aws rds download-db-log-file-portion \ --db-instance-identifier``test-instance`\ --log-file-name`log.txt`\ --starting-token`0`\ --output`text``>``full.txt`The saved file might contain blank lines. They appear at the end of each part of the log file while being downloaded. - 
                    For API details, see [DownloadDbLogFilePortion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/download-db-log-file-portion.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `generate-auth-token`.

- **AWS CLI**
- 
            
                    **To generate an authentication token**The following `generate-db-auth-token`example generates an authentication token for use with IAM database authentication.`aws rds generate-db-auth-token \ --hostname``aurmysql-test.cdgmuqiadpid.us-west-2.rds.amazonaws.com`\ --port`3306`\ --region`us-east-1`\ --username`jane_doe`Output: `aurmysql-test.cdgmuqiadpid.us-west-2.rds.amazonaws.com:3306/?Action=connect&DBUser=jane_doe&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIESZCNJ3OEXAMPLE%2F20180731%2Fus-east-1%2Frds-db%2Faws4_request&X-Amz-Date=20180731T235209Z&X-Amz-Expires=900&X-Amz-SignedHeaders=host&X-Amz-Signature=5a8753ebEXAMPLEa2c724e5667797EXAMPLE9d6ec6e3f427191fa41aeEXAMPLE`- 
                    For API details, see [GenerateAuthToken](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/generate-auth-token.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `generate-db-auth-token`.

- **AWS CLI**
- 
            
                    **To generate an IAM authentication token**The following `generate-db-auth-token`example generates IAM authentication token to connect to a database.`aws rds generate-db-auth-token \ --hostname``mydb.123456789012.us-east-1.rds.amazonaws.com`\ --port`3306`\ --region`us-east-1`\ --username`db_user`Output: `mydb.123456789012.us-east-1.rds.amazonaws.com:3306/?Action=connect&DBUser=db_user&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIEXAMPLE%2Fus-east-1%2Frds-db%2Faws4_request&X-Amz-Date=20210123T011543Z&X-Amz-Expires=900&X-Amz-SignedHeaders=host&X-Amz-Signature=88987EXAMPLE1EXAMPLE2EXAMPLE3EXAMPLE4EXAMPLE5EXAMPLE6`For more information, see [Connecting to your DB instance using IAM authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.Connecting.html)in the*Amazon RDS User Guide*and[Connecting to your DB cluster using IAM authentication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.Connecting.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [GenerateDbAuthToken](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/generate-db-auth-token.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list tags on an Amazon RDS resource**The following `list-tags-for-resource`example lists all tags on a DB instance.`aws rds list-tags-for-resource \ --resource-name``arn:aws:rds:us-east-1:123456789012:db:orcl1`Output: `{ "TagList": [ { "Key": "Environment", "Value": "test" }, { "Key": "Name", "Value": "MyDatabase" } ] }`For more information, see [Tagging Amazon RDS Resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-certificates`.

- **AWS CLI**
- 
            
                    **To temporarily override the system-default SSL/TLS certificate for new DB instances**The following `modify-certificates`example temporarily overrides the system-default SSL/TLS certificate for new DB instances.`aws rds modify-certificates \ --certificate-identifier``rds-ca-2019`Output: `{ "Certificate": { "CertificateIdentifier": "rds-ca-2019", "CertificateType": "CA", "Thumbprint": "EXAMPLE123456789012", "ValidFrom": "2019-09-19T18:16:53Z", "ValidTill": "2024-08-22T17:08:50Z", "CertificateArn": "arn:aws:rds:us-east-1::cert:rds-ca-2019", "CustomerOverride": true, "CustomerOverrideValidTill": "2024-08-22T17:08:50Z" } }`For more information, see [Rotating your SSL/TLS certificate](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL-certificate-rotation.html)in the*Amazon RDS User Guide*and[Rotating your SSL/TLS certificate](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL-certificate-rotation.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [ModifyCertificates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-certificates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-current-db-cluster-capacity`.

- **AWS CLI**
- 
            
                    **To scale the capacity of an Aurora Serverless DB cluster**The following `modify-current-db-cluster-capacity`example scales the capacity of an Aurora Serverless DB cluster to 8.`aws rds modify-current-db-cluster-capacity \ --db-cluster-identifier``mydbcluster`\ --capacity`8`Output: `{ "DBClusterIdentifier": "mydbcluster", "PendingCapacity": 8, "CurrentCapacity": 1, "SecondsBeforeTimeout": 300, "TimeoutAction": "ForceApplyCapacityChange" }`For more information, see [Scaling Aurora Serverless v1 DB cluster capacity manually](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.setting-capacity.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [ModifyCurrentDbClusterCapacity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-current-db-cluster-capacity.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-db-cluster-endpoint`.

- **AWS CLI**
- 
            
                    **To modify a custom DB cluster endpoint**The following `modify-db-cluster-endpoint`example modifies the specified custom DB cluster endpoint.`aws rds modify-db-cluster-endpoint \ --db-cluster-endpoint-identifier``mycustomendpoint`\ --static-members`dbinstance1``dbinstance2``dbinstance3`Output: `{ "DBClusterEndpointIdentifier": "mycustomendpoint", "DBClusterIdentifier": "mydbcluster", "DBClusterEndpointResourceIdentifier": "cluster-endpoint-ANPAJ4AE5446DAEXAMPLE", "Endpoint": "mycustomendpoint.cluster-custom-cnpexample.us-east-1.rds.amazonaws.com", "Status": "modifying", "EndpointType": "CUSTOM", "CustomEndpointType": "READER", "StaticMembers": [ "dbinstance1", "dbinstance2", "dbinstance3" ], "ExcludedMembers": [], "DBClusterEndpointArn": "arn:aws:rds:us-east-1:123456789012:cluster-endpoint:mycustomendpoint" }`For more information, see [Amazon Aurora Connection Management](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.Endpoints.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [ModifyDbClusterEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-cluster-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-db-cluster-parameter-group`.

- **AWS CLI**
- 
            
                    **To modify parameters in a DB cluster parameter group**The following `modify-db-cluster-parameter-group`example modifies the values of parameters in a DB cluster parameter group.`aws rds modify-db-cluster-parameter-group \ --db-cluster-parameter-group-name``mydbclusterpg`\ --parameters`"ParameterName=server_audit_logging,ParameterValue=1,ApplyMethod=immediate"`\`"ParameterName=server_audit_logs_upload,ParameterValue=1,ApplyMethod=immediate"`Output: `{ "DBClusterParameterGroupName": "mydbclusterpg" }`For more information, see [Working with DB parameter groups and DB cluster parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [ModifyDbClusterParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-cluster-parameter-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-db-cluster-snapshot-attribute`.

- **AWS CLI**
- 
            
                    **To modify a DB cluster snapshot attribute**The following `modify-db-cluster-snapshot-attribute`example makes changes to the specified DB cluster snapshot attribute.`aws rds modify-db-cluster-snapshot-attribute \ --db-cluster-snapshot-identifier``myclustersnapshot`\ --attribute-name`restore`\ --values-to-add`123456789012`Output: `{ "DBClusterSnapshotAttributesResult": { "DBClusterSnapshotIdentifier": "myclustersnapshot", "DBClusterSnapshotAttributes": [ { "AttributeName": "restore", "AttributeValues": [ "123456789012" ] } ] } }`For more information, see [Restoring from a DB Cluster Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_RestoreFromSnapshot.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [ModifyDbClusterSnapshotAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-cluster-snapshot-attribute.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-db-cluster`.

- **AWS CLI**
- 
            
                    **Example 1: To modify a DB cluster**The following `modify-db-cluster`example changes the master user password for the DB cluster named`cluster-2`and sets the backup retention period to 14 days. The`--apply-immediately`parameter causes the changes to be made immediately, instead of waiting until the next maintenance window.`aws rds modify-db-cluster \ --db-cluster-identifier``cluster-2`\ --backup-retention-period`14`\ --master-user-password`newpassword99`\ --apply-immediatelyOutput: `{ "DBCluster": { "AllocatedStorage": 1, "AvailabilityZones": [ "eu-central-1b", "eu-central-1c", "eu-central-1a" ], "BackupRetentionPeriod": 14, "DatabaseName": "", "DBClusterIdentifier": "cluster-2", "DBClusterParameterGroup": "default.aurora5.6", "DBSubnetGroup": "default-vpc-2305ca49", "Status": "available", "EarliestRestorableTime": "2020-06-03T02:07:29.637Z", "Endpoint": "cluster-2.cluster-############.eu-central-1.rds.amazonaws.com", "ReaderEndpoint": "cluster-2.cluster-ro-############.eu-central-1.rds.amazonaws.com", "MultiAZ": false, "Engine": "aurora", "EngineVersion": "5.6.10a", "LatestRestorableTime": "2020-06-04T15:11:25.748Z", "Port": 3306, "MasterUsername": "admin", "PreferredBackupWindow": "01:55-02:25", "PreferredMaintenanceWindow": "thu:21:14-thu:21:44", "ReadReplicaIdentifiers": [], "DBClusterMembers": [ { "DBInstanceIdentifier": "cluster-2-instance-1", "IsClusterWriter": true, "DBClusterParameterGroupStatus": "in-sync", "PromotionTier": 1 } ], "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sg-20a5c047", "Status": "active" } ], "HostedZoneId": "Z1RLNU0EXAMPLE", "StorageEncrypted": true, "KmsKeyId": "arn:aws:kms:eu-central-1:123456789012:key/d1bd7c8f-5cdb-49ca-8a62-a1b2c3d4e5f6", "DbClusterResourceId": "cluster-AGJ7XI77XVIS6FUXHU1EXAMPLE", "DBClusterArn": "arn:aws:rds:eu-central-1:123456789012:cluster:cluster-2", "AssociatedRoles": [], "IAMDatabaseAuthenticationEnabled": false, "ClusterCreateTime": "2020-04-03T14:44:02.764Z", "EngineMode": "provisioned", "DeletionProtection": false, "HttpEndpointEnabled": false, "CopyTagsToSnapshot": true, "CrossAccountClone": false, "DomainMemberships": [] } }`For more information, see [Modifying an Amazon Aurora DB Cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Modifying.html)in the*Amazon Aurora User Guide*.**Example 2: To associate VPC security group with a DB cluster**The following `modify-db-instance`example associates a specific VPC security group and removes DB security groups from a DB cluster.`aws rds modify-db-cluster \ --db-cluster-identifier``dbName`\ --vpc-security-group-ids`sg-ID`Output: `{ "DBCluster": { "AllocatedStorage": 1, "AvailabilityZones": [ "us-west-2c", "us-west-2b", "us-west-2a" ], "BackupRetentionPeriod": 1, "DBClusterIdentifier": "dbName", "DBClusterParameterGroup": "default.aurora-mysql8.0", "DBSubnetGroup": "default", "Status": "available", "EarliestRestorableTime": "2024-02-15T01:12:13.966000+00:00", "Endpoint": "dbName.cluster-abcdefghji.us-west-2.rds.amazonaws.com", "ReaderEndpoint": "dbName.cluster-ro-abcdefghji.us-west-2.rds.amazonaws.com", "MultiAZ": false, "Engine": "aurora-mysql", "EngineVersion": "8.0.mysql_aurora.3.04.1", "LatestRestorableTime": "2024-02-15T02:25:33.696000+00:00", "Port": 3306, "MasterUsername": "admin", "PreferredBackupWindow": "10:59-11:29", "PreferredMaintenanceWindow": "thu:08:54-thu:09:24", "ReadReplicaIdentifiers": [], "DBClusterMembers": [ { "DBInstanceIdentifier": "dbName-instance-1", "IsClusterWriter": true, "DBClusterParameterGroupStatus": "in-sync", "PromotionTier": 1 } ], "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sg-ID", "Status": "active" } ], ...output omitted... } }`For more information, see [Controlling access with security groups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.RDSSecurityGroups.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [ModifyDbCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-db-instance`.

- **AWS CLI**
- 
            
                    **Example 1: To modify a DB instance**The following `modify-db-instance`example associates an option group and a parameter group with a compatible Microsoft SQL Server DB instance. The`--apply-immediately`parameter causes the option and parameter groups to be associated immediately, instead of waiting until the next maintenance window.`aws rds modify-db-instance \ --db-instance-identifier``database-2`\ --option-group-name`test-se-2017`\ --db-parameter-group-name`test-sqlserver-se-2017`\ --apply-immediatelyOutput: `{ "DBInstance": { "DBInstanceIdentifier": "database-2", "DBInstanceClass": "db.r4.large", "Engine": "sqlserver-se", "DBInstanceStatus": "available", ...output omitted... "DBParameterGroups": [ { "DBParameterGroupName": "test-sqlserver-se-2017", "ParameterApplyStatus": "applying" } ], "AvailabilityZone": "us-west-2d", ...output omitted... "MultiAZ": true, "EngineVersion": "14.00.3281.6.v1", "AutoMinorVersionUpgrade": false, "ReadReplicaDBInstanceIdentifiers": [], "LicenseModel": "license-included", "OptionGroupMemberships": [ { "OptionGroupName": "test-se-2017", "Status": "pending-apply" } ], "CharacterSetName": "SQL_Latin1_General_CP1_CI_AS", "SecondaryAvailabilityZone": "us-west-2c", "PubliclyAccessible": true, "StorageType": "gp2", ...output omitted... "DeletionProtection": false, "AssociatedRoles": [], "MaxAllocatedStorage": 1000 } }`For more information, see [Modifying an Amazon RDS DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)in the*Amazon RDS User Guide*.**Example 2: To associate VPC security group with a DB instance**The following `modify-db-instance`example associates a specific VPC security group and removes DB security groups from a DB instance:`aws rds modify-db-instance \ --db-instance-identifier``dbName`\ --vpc-security-group-ids`sg-ID`Output: `{ "DBInstance": { "DBInstanceIdentifier": "dbName", "DBInstanceClass": "db.t3.micro", "Engine": "mysql", "DBInstanceStatus": "available", "MasterUsername": "admin", "Endpoint": { "Address": "dbName.abcdefghijk.us-west-2.rds.amazonaws.com", "Port": 3306, "HostedZoneId": "ABCDEFGHIJK1234" }, "AllocatedStorage": 20, "InstanceCreateTime": "2024-02-15T00:37:58.793000+00:00", "PreferredBackupWindow": "11:57-12:27", "BackupRetentionPeriod": 7, "DBSecurityGroups": [], "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sg-ID", "Status": "active" } ], ... output omitted ... "MultiAZ": false, "EngineVersion": "8.0.35", "AutoMinorVersionUpgrade": true, "ReadReplicaDBInstanceIdentifiers": [], "LicenseModel": "general-public-license", ... output omitted ... } }`For more information, see [Controlling access with security groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [ModifyDBInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-db-parameter-group`.

- **AWS CLI**
- 
            
                    **To modify a DB parameter group**The following `modify-db-parameter-group`example changes the value of the`clr enabled`parameter in a DB parameter group. The`--apply-immediately`parameter causes the DB parameter group to be modified immediately, instead of waiting until the next maintenance window.`aws rds modify-db-parameter-group \ --db-parameter-group-name``test-sqlserver-se-2017`\ --parameters`"ParameterName='clr enabled',ParameterValue=1,ApplyMethod=immediate"`Output: `{ "DBParameterGroupName": "test-sqlserver-se-2017" }`For more information, see [Modifying Parameters in a DB Parameter Group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html#USER_WorkingWithParamGroups.Modifying)in the*Amazon RDS User Guide*.- 
                    For API details, see [ModifyDBParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-parameter-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-db-proxy-endpoint`.

- **AWS CLI**
- 
            
                    **To modify a DB proxy endpoint for an RDS database**The following `modify-db-proxy-endpoint`example modifies a DB proxy endpoint`proxyEndpoint`to set the read-timeout to 65 seconds.`aws rds modify-db-proxy-endpoint \ --db-proxy-endpoint-name``proxyEndpoint`\ --cli-read-timeout`65`Output: `{ "DBProxyEndpoint": { "DBProxyEndpointName": "proxyEndpoint", "DBProxyEndpointArn": "arn:aws:rds:us-east-1:123456789012:db-proxy-endpoint:prx-endpoint-0123a01b12345c0ab", "DBProxyName": "proxyExample", "Status": "available", "VpcId": "vpc-1234567", "VpcSecurityGroupIds": [ "sg-1234" ], "VpcSubnetIds": [ "subnetgroup1", "subnetgroup2" ], "Endpoint": "proxyEndpoint.endpoint.proxyExample-ab0cd1efghij.us-east-1.rds.amazonaws.com", "CreatedDate": "2023-04-05T16:09:33.452000+00:00", "TargetRole": "READ_WRITE", "IsDefault": "false" } }`For more information, see [Modifying a proxy endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-endpoints.html#rds-proxy-endpoints.ModifyingEndpoint)in the*Amazon RDS User Guide*and[Modifying a proxy endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-endpoints.html#rds-proxy-endpoints.ModifyingEndpoint)in the*Amazon Aurora User Guide*.- 
                    For API details, see [ModifyDbProxyEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-proxy-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-db-proxy-target-group`.

- **AWS CLI**
- 
            
                    **To modify a DB proxy endpoints**The following `modify-db-proxy-target-group`example modifies a DB proxy target group to set the maximum connections to 80 percent and maximum idle connections to 10 percent.`aws rds modify-db-proxy-target-group \ --target-group-name``default`\ --db-proxy-name`proxyExample`\ --connection-pool-config`MaxConnectionsPercent=80,MaxIdleConnectionsPercent=10`Output: `{ "DBProxyTargetGroup": { "DBProxyName": "proxyExample", "TargetGroupName": "default", "TargetGroupArn": "arn:aws:rds:us-east-1:123456789012:target-group:prx-tg-0123a01b12345c0ab", "IsDefault": true, "Status": "available", "ConnectionPoolConfig": { "MaxConnectionsPercent": 80, "MaxIdleConnectionsPercent": 10, "ConnectionBorrowTimeout": 120, "SessionPinningFilters": [] }, "CreatedDate": "2023-05-02T18:41:19.495000+00:00", "UpdatedDate": "2023-05-02T18:41:21.762000+00:00" } }`For more information, see [Modifying an RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-managing.html#rds-proxy-modifying-proxy)in the*Amazon RDS User Guide*and[Modifying an RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-managing.html#rds-proxy-modifying-proxy)in the*Amazon Aurora User Guide*.- 
                    For API details, see [ModifyDbProxyTargetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-proxy-target-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-db-proxy`.

- **AWS CLI**
- 
            
                    **To modify a DB proxy for an RDS database**The following `modify-db-proxy`example modifies a DB proxy named`proxyExample`to require SSL for its connections.`aws rds modify-db-proxy \ --db-proxy-name``proxyExample`\ --require-tlsOutput: `{ "DBProxy": { "DBProxyName": "proxyExample", "DBProxyArn": "arn:aws:rds:us-east-1:123456789012:db-proxy:prx-0123a01b12345c0ab", "Status": "modifying" "EngineFamily": "PostgreSQL", "VpcId": "sg-1234567", "VpcSecurityGroupIds": [ "sg-1234" ], "VpcSubnetIds": [ "subnetgroup1", "subnetgroup2" ], "Auth": "[ { "Description": "proxydescription1", "AuthScheme": "SECRETS", "SecretArn": "arn:aws:secretsmanager:us-west-2:123456789123:secret:proxysecret1-Abcd1e", "IAMAuth": "DISABLED" } ]", "RoleArn": "arn:aws:iam::12345678912:role/ProxyPostgreSQLRole", "Endpoint": "proxyExample.proxy-ab0cd1efghij.us-east-1.rds.amazonaws.com", "RequireTLS": true, "IdleClientTimeout": 1800, "DebuggingLogging": false, "CreatedDate": "2023-04-05T16:09:33.452000+00:00", "UpdatedDate": "2023-04-13T01:49:38.568000+00:00" } }`For more information, see [Modify an RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-managing.html#rds-proxy-modifying-proxy)in the*Amazon RDS User Guide*and[Creating an RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-managing.html#rds-proxy-modifying-proxy)in the*Amazon Aurora User Guide*.- 
                    For API details, see [ModifyDbProxy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-proxy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-db-shard-group`.

- **AWS CLI**
- 
            
                    **Example 1: To modify a DB shard group**The following `modify-db-shard-group`example changes the maximum capacity of a DB shard group.`aws rds modify-db-shard-group \ --db-shard-group-identifier``my-db-shard-group`\ --max-acu`1000`Output: `{ "DBShardGroups": [ { "DBShardGroupResourceId": "shardgroup-a6e3a0226aa243e2ac6c7a1234567890", "DBShardGroupIdentifier": "my-db-shard-group", "DBClusterIdentifier": "my-sv2-cluster", "MaxACU": 768.0, "ComputeRedundancy": 0, "Status": "available", "PubliclyAccessible": false, "Endpoint": "my-sv2-cluster.limitless-cekycexample.us-east-2.rds.amazonaws.com" } ] }`For more information, see [Amazon Aurora DB Clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.html)in the*Amazon Aurora User Guide*.**Example 2: To describe your DB shard groups**The following `describe-db-shard-groups`example retrieves the details of your DB shard groups after you run the`modify-db-shard-group`command. The maximum capacity of the DB shard group`my-db-shard-group`is now 1000 Aurora capacity units (ACUs).`aws rds describe-db-shard-groups`Output: `{ "DBShardGroups": [ { "DBShardGroupResourceId": "shardgroup-7bb446329da94788b3f957746example", "DBShardGroupIdentifier": "limitless-test-shard-grp", "DBClusterIdentifier": "limitless-test-cluster", "MaxACU": 768.0, "ComputeRedundancy": 0, "Status": "available", "PubliclyAccessible": true, "Endpoint": "limitless-test-cluster.limitless-cekycexample.us-east-2.rds.amazonaws.com" }, { "DBShardGroupResourceId": "shardgroup-a6e3a0226aa243e2ac6c7a1234567890", "DBShardGroupIdentifier": "my-db-shard-group", "DBClusterIdentifier": "my-sv2-cluster", "MaxACU": 1000.0, "ComputeRedundancy": 0, "Status": "available", "PubliclyAccessible": false, "Endpoint": "my-sv2-cluster.limitless-cekycexample.us-east-2.rds.amazonaws.com" } ] }`For more information, see [Amazon Aurora DB Clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [ModifyDbShardGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-shard-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-db-snapshot-attribute`.

- **AWS CLI**
- 
            
                    **Example 1: To enable two AWS accounts to restore a DB snapshot**The following `modify-db-snapshot-attribute`example grants permission to two AWS accounts, with the identifiers`111122223333`and`444455556666`, to restore the DB snapshot named`mydbsnapshot`.`aws rds modify-db-snapshot-attribute \ --db-snapshot-identifier``mydbsnapshot`\ --attribute-name`restore`\ --values-to-add {"111122223333","444455556666"}Output: `{ "DBSnapshotAttributesResult": { "DBSnapshotIdentifier": "mydbsnapshot", "DBSnapshotAttributes": [ { "AttributeName": "restore", "AttributeValues": [ "111122223333", "444455556666" ] } ] } }`For more information, see [Sharing a Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ShareSnapshot.html#USER_ShareSnapshot.Sharing)in the*Amazon RDS User Guide*.**Example 2: To prevent an AWS account from restoring a DB snapshot**The following `modify-db-snapshot-attribute`example removes permission from a particular AWS account to restore the DB snapshot named`mydbsnapshot`. When specifying a single account, the account identifier can't be surrounded by quotations marks or braces.`aws rds modify-db-snapshot-attribute \ --db-snapshot-identifier``mydbsnapshot`\ --attribute-name`restore`\ --values-to-remove`444455556666`Output: `{ "DBSnapshotAttributesResult": { "DBSnapshotIdentifier": "mydbsnapshot", "DBSnapshotAttributes": [ { "AttributeName": "restore", "AttributeValues": [ "111122223333" ] } ] } }`For more information, see [Sharing a Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ShareSnapshot.html#USER_ShareSnapshot.Sharing)in the*Amazon RDS User Guide*.- 
                    For API details, see [ModifyDbSnapshotAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-snapshot-attribute.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-db-snapshot-attributes`.

- **AWS CLI**
- 
            
                    **To modify a DB snapshot attribute**The following `modify-db-snapshot-attribute`example permits two AWS account identifiers,`111122223333`and`444455556666`, to restore the DB snapshot named`mydbsnapshot`.`aws rds modify-db-snapshot-attribute \ --db-snapshot-identifier``mydbsnapshot`\ --attribute-name`restore`\ --values-to-add '`["111122223333","444455556666"]`'Output: `{ "DBSnapshotAttributesResult": { "DBSnapshotIdentifier": "mydbsnapshot", "DBSnapshotAttributes": [ { "AttributeName": "restore", "AttributeValues": [ "111122223333", "444455556666" ] } ] } }`For more information, see [Sharing a Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ShareSnapshot.html#USER_ShareSnapshot.Sharing)in the*Amazon RDS User Guide*.- 
                    For API details, see [ModifyDbSnapshotAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-snapshot-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-db-snapshot`.

- **AWS CLI**
- 
            
                    **To modify a DB snapshot**The following `modify-db-snapshot`example upgrades a PostgeSQL 10.6 snapshot named`db5-snapshot-upg-test`to PostgreSQL 11.7. The new DB engine version is shown after the snapshot has finished upgrading and its status is**available**.`aws rds modify-db-snapshot \ --db-snapshot-identifier``db5-snapshot-upg-test`\ --engine-version`11.7`Output: `{ "DBSnapshot": { "DBSnapshotIdentifier": "db5-snapshot-upg-test", "DBInstanceIdentifier": "database-5", "SnapshotCreateTime": "2020-03-27T20:49:17.092Z", "Engine": "postgres", "AllocatedStorage": 20, "Status": "upgrading", "Port": 5432, "AvailabilityZone": "us-west-2a", "VpcId": "vpc-2ff27557", "InstanceCreateTime": "2020-03-27T19:59:04.735Z", "MasterUsername": "postgres", "EngineVersion": "10.6", "LicenseModel": "postgresql-license", "SnapshotType": "manual", "OptionGroupName": "default:postgres-11", "PercentProgress": 100, "StorageType": "gp2", "Encrypted": false, "DBSnapshotArn": "arn:aws:rds:us-west-2:123456789012:snapshot:db5-snapshot-upg-test", "IAMDatabaseAuthenticationEnabled": false, "ProcessorFeatures": [], "DbiResourceId": "db-GJMF75LM42IL6BTFRE4UZJ5YM4" } }`For more information, see [Upgrading a PostgreSQL DB Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBSnapshot.PostgreSQL.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [ModifyDbSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-db-subnet-group`.

- **AWS CLI**
- 
            
                    **To modify a DB subnet group**The following `modify-db-subnet-group`example adds a subnet with the ID`subnet-08e41f9e230222222`to the DB subnet group named`mysubnetgroup`. To keep the existing subnets in the subnet group, include their IDs as values in the`--subnet-ids`option. Make sure to have subnets with at least two different Availability Zones in the DB subnet group.`aws rds modify-db-subnet-group \ --db-subnet-group-name``mysubnetgroup`\ --subnet-ids '`["subnet-0a1dc4e1a6f123456","subnet-070dd7ecb3aaaaaaa","subnet-00f5b198bc0abcdef","subnet-08e41f9e230222222"]`'Output: `{ "DBSubnetGroup": { "DBSubnetGroupName": "mysubnetgroup", "DBSubnetGroupDescription": "test DB subnet group", "VpcId": "vpc-0f08e7610a1b2c3d4", "SubnetGroupStatus": "Complete", "Subnets": [ { "SubnetIdentifier": "subnet-08e41f9e230222222", "SubnetAvailabilityZone": { "Name": "us-west-2a" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-070dd7ecb3aaaaaaa", "SubnetAvailabilityZone": { "Name": "us-west-2b" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-00f5b198bc0abcdef", "SubnetAvailabilityZone": { "Name": "us-west-2d" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-0a1dc4e1a6f123456", "SubnetAvailabilityZone": { "Name": "us-west-2b" }, "SubnetStatus": "Active" } ], "DBSubnetGroupArn": "arn:aws:rds:us-west-2:534026745191:subgrp:mysubnetgroup" } }`For more information, see [Step 3: Create a DB Subnet Group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.CreateDBSubnetGroup)in the*Amazon RDS User Guide*.- 
                    For API details, see [ModifyDbSubnetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-subnet-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-event-subscription`.

- **AWS CLI**
- 
            
                    **To modify an event subscription**The following `modify-event-subscription`example disables the specified event subscription, so that it no longer publishes notifications to the specified Amazon Simple Notification Service topic.`aws rds modify-event-subscription \ --subscription-name``my-instance-events`\ --no-enabledOutput: `{ "EventSubscription": { "EventCategoriesList": [ "backup", "recovery" ], "CustomerAwsId": "123456789012", "SourceType": "db-instance", "SubscriptionCreationTime": "Tue Jul 31 23:22:01 UTC 2018", "EventSubscriptionArn": "arn:aws:rds:us-east-1:123456789012:es:my-instance-events", "SnsTopicArn": "arn:aws:sns:us-east-1:123456789012:interesting-events", "CustSubscriptionId": "my-instance-events", "Status": "modifying", "Enabled": false } }`- 
                    For API details, see [ModifyEventSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-event-subscription.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-global-cluster`.

- **AWS CLI**
- 
            
                    **To modify a global DB cluster**The following `modify-global-cluster`example enables deletion protection for an Aurora MySQL-compatible global DB cluster.`aws rds modify-global-cluster \ --global-cluster-identifier``myglobalcluster`\ --deletion-protectionOutput: `{ "GlobalCluster": { "GlobalClusterIdentifier": "myglobalcluster", "GlobalClusterResourceId": "cluster-f0e523bfe07aabb", "GlobalClusterArn": "arn:aws:rds::123456789012:global-cluster:myglobalcluster", "Status": "available", "Engine": "aurora-mysql", "EngineVersion": "5.7.mysql_aurora.2.07.2", "StorageEncrypted": false, "DeletionProtection": true, "GlobalClusterMembers": [] } }`For more information, see [Managing an Aurora global database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-managing.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [ModifyGlobalCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-global-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `promote-read-replica-db-cluster`.

- **AWS CLI**
- 
            
                    **To promote a DB cluster read replica**The following `promote-read-replica-db-cluster`example promotes the specified read replica to become a standalone DB cluster.`aws rds promote-read-replica-db-cluster \ --db-cluster-identifier``mydbcluster-1`Output: `{ "DBCluster": { "AllocatedStorage": 1, "AvailabilityZones": [ "us-east-1a", "us-east-1b", "us-east-1c" ], "BackupRetentionPeriod": 1, "DatabaseName": "", "DBClusterIdentifier": "mydbcluster-1", ...some output truncated... } }`For more information, see [Promoting a read replica to be a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.CrossRegion.html#AuroraMySQL.Replication.CrossRegion.Promote)in the*Amazon Aurora User Guide*.- 
                    For API details, see [PromoteReadReplicaDbCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/promote-read-replica-db-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `promote-read-replica`.

- **AWS CLI**
- 
            
                    **To promote a read replica**The following `promote-read-replica`example promotes the specified read replica to become a standalone DB instance.`aws rds promote-read-replica \ --db-instance-identifier``test-instance-repl`Output: `{ "DBInstance": { "DBInstanceArn": "arn:aws:rds:us-east-1:123456789012:db:test-instance-repl", "StorageType": "standard", "ReadReplicaSourceDBInstanceIdentifier": "test-instance", "DBInstanceStatus": "modifying", ...some output truncated... } }`- 
                    For API details, see [PromoteReadReplica](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/promote-read-replica.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `purchase-reserved-db-instance`.

- **AWS CLI**
- 
            
                    **To purchase a reserved DB instance offering**The following `purchase-reserved-db-instances-offering`example purchases a reserved DB instance offering. The`reserved-db-instances-offering-id`must be a valid offering ID, as returned by the`describe-reserved-db-instances-offering`command.aws rds purchase-reserved-db-instances-offering --reserved-db-instances-offering-id 438012d3-4a52-4cc7-b2e3-8dff72e0e706 - 
                    For API details, see [PurchaseReservedDbInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/purchase-reserved-db-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `purchase-reserved-db-instances-offerings`.

- **AWS CLI**
- 
            
                    **Example 1: To find a reserved DB instance to purchase**The following `describe-reserved-db-instances-offerings`example lists the available reserved MySQL DB instances with the db.t2.micro instance class and a duration of one year. The offering ID is required for purchasing a reserved DB instance.`aws rds describe-reserved-db-instances-offerings \ --product-description``mysql`\ --db-instance-class`db.t2.micro`\ --duration`1`Output: `{ "ReservedDBInstancesOfferings": [ { "ReservedDBInstancesOfferingId": "8ba30be1-b9ec-447f-8f23-6114e3f4c7b4", "DBInstanceClass": "db.t2.micro", "Duration": 31536000, "FixedPrice": 51.0, "UsagePrice": 0.0, "CurrencyCode": "USD", "ProductDescription": "mysql", "OfferingType": "Partial Upfront", "MultiAZ": false, "RecurringCharges": [ { "RecurringChargeAmount": 0.006, "RecurringChargeFrequency": "Hourly" } ] }, ... some output truncated ... ] }`For more information, see [Reserved DB Instances for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html)in the*Amazon RDS User Guide*.**Example 2: To purchase a reserved DB instance**The following `purchase-reserved-db-instances-offering`example shows how to buy the reserved DB instance offering from the previous example.aws rds purchase-reserved-db-instances-offering --reserved-db-instances-offering-id 8ba30be1-b9ec-447f-8f23-6114e3f4c7b4 Output: `{ "ReservedDBInstance": { "ReservedDBInstanceId": "ri-2020-06-29-16-54-57-670", "ReservedDBInstancesOfferingId": "8ba30be1-b9ec-447f-8f23-6114e3f4c7b4", "DBInstanceClass": "db.t2.micro", "StartTime": "2020-06-29T16:54:57.670Z", "Duration": 31536000, "FixedPrice": 51.0, "UsagePrice": 0.0, "CurrencyCode": "USD", "DBInstanceCount": 1, "ProductDescription": "mysql", "OfferingType": "Partial Upfront", "MultiAZ": false, "State": "payment-pending", "RecurringCharges": [ { "RecurringChargeAmount": 0.006, "RecurringChargeFrequency": "Hourly" } ], "ReservedDBInstanceArn": "arn:aws:rds:us-west-2:123456789012:ri:ri-2020-06-29-16-54-57-670" } }`For more information, see [Reserved DB Instances for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [PurchaseReservedDbInstancesOfferings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/purchase-reserved-db-instances-offerings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reboot-db-instance`.

- **AWS CLI**
- 
            
                    **To reboot a DB instance**The following `reboot-db-instance`example starts a reboot of the specified DB instance.`aws rds reboot-db-instance \ --db-instance-identifier``test-mysql-instance`Output: `{ "DBInstance": { "DBInstanceIdentifier": "test-mysql-instance", "DBInstanceClass": "db.t3.micro", "Engine": "mysql", "DBInstanceStatus": "rebooting", "MasterUsername": "admin", "Endpoint": { "Address": "test-mysql-instance.############.us-west-2.rds.amazonaws.com", "Port": 3306, "HostedZoneId": "Z1PVIF0EXAMPLE" }, ... output omitted... } }`For more information, see [Rebooting a DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_RebootInstance.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [RebootDBInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/reboot-db-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reboot-db-shard-group`.

- **AWS CLI**
- 
            
                    **Example 1: To reboot a DB shard group**The following `reboot-db-shard-group`example reboots a DB shard group.`aws rds reboot-db-shard-group \ --db-shard-group-identifier``my-db-shard-group`Output: `{ "DBShardGroups": [ { "DBShardGroupResourceId": "shardgroup-a6e3a0226aa243e2ac6c7a1234567890", "DBShardGroupIdentifier": "my-db-shard-group", "DBClusterIdentifier": "my-sv2-cluster", "MaxACU": 1000.0, "ComputeRedundancy": 0, "Status": "available", "PubliclyAccessible": false, "Endpoint": "my-sv2-cluster.limitless-cekycexample.us-east-2.rds.amazonaws.com" } ] }`For more information, see [Rebooting an Amazon Aurora DB cluster or Amazon Aurora DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_RebootCluster.html)in the*Amazon Aurora User Guide*.**Example 2: To describe your DB shard groups**The following `describe-db-shard-groups`example retrieves the details of your DB shard groups after you run the`reboot-db-shard-group`command. The DB shard group`my-db-shard-group`is now rebooting.`aws rds describe-db-shard-groups`Output: `{ "DBShardGroups": [ { "DBShardGroupResourceId": "shardgroup-7bb446329da94788b3f957746example", "DBShardGroupIdentifier": "limitless-test-shard-grp", "DBClusterIdentifier": "limitless-test-cluster", "MaxACU": 768.0, "ComputeRedundancy": 0, "Status": "available", "PubliclyAccessible": true, "Endpoint": "limitless-test-cluster.limitless-cekycexample.us-east-2.rds.amazonaws.com" }, { "DBShardGroupResourceId": "shardgroup-a6e3a0226aa243e2ac6c7a1234567890", "DBShardGroupIdentifier": "my-db-shard-group", "DBClusterIdentifier": "my-sv2-cluster", "MaxACU": 1000.0, "ComputeRedundancy": 0, "Status": "rebooting", "PubliclyAccessible": false, "Endpoint": "my-sv2-cluster.limitless-cekycexample.us-east-2.rds.amazonaws.com" } ] }`For more information, see [Rebooting an Amazon Aurora DB cluster or Amazon Aurora DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_RebootCluster.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [RebootDbShardGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/reboot-db-shard-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-db-proxy-targets`.

- **AWS CLI**
- 
            
                    **To register a DB proxy with a database**The following `register-db-proxy-targets`example creates the association between a database and a proxy.`aws rds register-db-proxy-targets \ --db-proxy-name``proxyExample`\ --db-cluster-identifiers`database-5`Output: `{ "DBProxyTargets": [ { "RdsResourceId": "database-5", "Port": 3306, "Type": "TRACKED_CLUSTER", "TargetHealth": { "State": "REGISTERING" } }, { "Endpoint": "database-5instance-1.ab0cd1efghij.us-east-1.rds.amazonaws.com", "RdsResourceId": "database-5", "Port": 3306, "Type": "RDS_INSTANCE", "TargetHealth": { "State": "REGISTERING" } } ] }`For more information, see [Creating an RDS proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-setup.html#rds-proxy-creating)in the*Amazon RDS User Guide*and[Creating an RDS proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-setup.html#rds-proxy-creating)in the*Amazon Aurora User Guide*.- 
                    For API details, see [RegisterDbProxyTargets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/register-db-proxy-targets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-from-global-cluster`.

- **AWS CLI**
- 
            
                    **To detach an Aurora secondary cluster from an Aurora global database cluster**The following `remove-from-global-cluster`example detaches an Aurora secondary cluster from an Aurora global database cluster. The cluster changes from being read-only to a standalone cluster with read-write capability.`aws rds remove-from-global-cluster \ --region``us-west-2`\ --global-cluster-identifier`myglobalcluster`\ --db-cluster-identifier`arn:aws:rds:us-west-2:123456789012:cluster:DB-1`Output: `{ "GlobalCluster": { "GlobalClusterIdentifier": "myglobalcluster", "GlobalClusterResourceId": "cluster-abc123def456gh", "GlobalClusterArn": "arn:aws:rds::123456789012:global-cluster:myglobalcluster", "Status": "available", "Engine": "aurora-postgresql", "EngineVersion": "10.11", "StorageEncrypted": true, "DeletionProtection": false, "GlobalClusterMembers": [ { "DBClusterArn": "arn:aws:rds:us-east-1:123456789012:cluster:js-global-cluster", "Readers": [ "arn:aws:rds:us-west-2:123456789012:cluster:DB-1" ], "IsWriter": true }, { "DBClusterArn": "arn:aws:rds:us-west-2:123456789012:cluster:DB-1", "Readers": [], "IsWriter": false, "GlobalWriteForwardingStatus": "disabled" } ] } }`For more information, see [Removing a cluster from an Amazon Aurora global database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-managing.html#aurora-global-database-detaching)in the*Amazon Aurora User Guide*.- 
                    For API details, see [RemoveFromGlobalCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/remove-from-global-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-option-from-option-group`.

- **AWS CLI**
- 
            
                    **To delete an option from an option group**The following `remove-option-from-option-group`example removes the`OEM`option from`myoptiongroup`.`aws rds remove-option-from-option-group \ --option-group-name``myoptiongroup`\ --options`OEM`\ --apply-immediatelyOutput: `{ "OptionGroup": { "OptionGroupName": "myoptiongroup", "OptionGroupDescription": "Test", "EngineName": "oracle-ee", "MajorEngineVersion": "19", "Options": [], "AllowsVpcAndNonVpcInstanceMemberships": true, "OptionGroupArn": "arn:aws:rds:us-east-1:123456789012:og:myoptiongroup" } }`For more information, see [Removing an Option from an Option Group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.html#USER_WorkingWithOptionGroups.RemoveOption)in the*Amazon Aurora User Guide*.- 
                    For API details, see [RemoveOptionFromOptionGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/remove-option-from-option-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-role-from-db-cluster`.

- **AWS CLI**
- 
            
                    **To disassociate an AWS Identity and Access Management (IAM) role from a DB cluster**The following `remove-role-from-db-cluster`example removes a role from a DB cluster.`aws rds remove-role-from-db-cluster \ --db-cluster-identifier``mydbcluster`\ --role-arn`arn:aws:iam::123456789012:role/RDSLoadFromS3`This command produces no output. For more information, see [Associating an IAM role with an Amazon Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Authorizing.IAM.AddRoleToDBCluster.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [RemoveRoleFromDbCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/remove-role-from-db-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-role-from-db-instance`.

- **AWS CLI**
- 
            
                    **To disassociate an AWS Identity and Access Management (IAM) role from a DB instance**The following `remove-role-from-db-instance`example removes the role named`rds-s3-integration-role`from an Oracle DB instance named`test-instance`.`aws rds remove-role-from-db-instance \ --db-instance-identifier``test-instance`\ --feature-name`S3_INTEGRATION`\ --role-arn`arn:aws:iam::111122223333:role/rds-s3-integration-role`This command produces no output. For more information, see [Disabling RDS SQL Server Integration with S3](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/User.SQLServer.Options.S3-integration.html#Appendix.SQLServer.Options.S3-integration.disabling)in the*Amazon RDS User Guide*.- 
                    For API details, see [RemoveRoleFromDbInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/remove-role-from-db-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-source-identifier-from-subscription`.

- **AWS CLI**
- 
            
                    **To remove a source identifier from a subscription**The following `remove-source-identifier`example removes the specified source identifier from an existing subscription.`aws rds remove-source-identifier-from-subscription \ --subscription-name``my-instance-events`\ --source-identifier`test-instance-repl`Output: `{ "EventSubscription": { "EventSubscriptionArn": "arn:aws:rds:us-east-1:123456789012:es:my-instance-events", "SubscriptionCreationTime": "Tue Jul 31 23:22:01 UTC 2018", "EventCategoriesList": [ "backup", "recovery" ], "SnsTopicArn": "arn:aws:sns:us-east-1:123456789012:interesting-events", "Status": "modifying", "CustSubscriptionId": "my-instance-events", "CustomerAwsId": "123456789012", "SourceIdsList": [ "test-instance" ], "SourceType": "db-instance", "Enabled": false } }`- 
                    For API details, see [RemoveSourceIdentifierFromSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/remove-source-identifier-from-subscription.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-tags-from-resource`.

- **AWS CLI**
- 
            
                    **To remove tags from a resource**The following `remove-tags-from-resource`example removes tags from a resource.`aws rds remove-tags-from-resource \ --resource-name``arn:aws:rds:us-east-1:123456789012:db:mydbinstance`\ --tag-keys`Name``Environment`This command produces no output. For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html)in the*Amazon RDS User Guide*and[Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [RemoveTagsFromResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/remove-tags-from-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reset-db-cluster-parameter-group`.

- **AWS CLI**
- 
            
                    **Example 1: To reset all parameters to their default values**The following `reset-db-cluster-parameter-group`example resets all parameter values in a customer-created DB cluster parameter group to their default values.`aws rds reset-db-cluster-parameter-group \ --db-cluster-parameter-group-name``mydbclpg`\ --reset-all-parametersOutput: `{ "DBClusterParameterGroupName": "mydbclpg" }`For more information, see [Working with DB parameter groups and DB cluster parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html)in the*Amazon Aurora User Guide*.**Example 2: To reset specific parameters to their default values**The following `reset-db-cluster-parameter-group`example resets the parameter values for specific parameters to their default values in a customer-created DB cluster parameter group.`aws rds reset-db-cluster-parameter-group \ --db-cluster-parameter-group-name``mydbclpgy`\ --parameters`"ParameterName=max_connections,ApplyMethod=immediate"`\`"ParameterName=max_allowed_packet,ApplyMethod=immediate"`Output: `{ "DBClusterParameterGroupName": "mydbclpg" }`For more information, see [Working with DB parameter groups and DB cluster parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [ResetDbClusterParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/reset-db-cluster-parameter-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reset-db-parameter-group`.

- **AWS CLI**
- 
            
                    **Example 1: To reset all parameters to their default values**The following `reset-db-parameter-group`example resets all parameter values in a customer-created DB parameter group to their default values.`aws rds reset-db-parameter-group \ --db-parameter-group-name``mypg`\ --reset-all-parametersOutput: `{ "DBParameterGroupName": "mypg" }`For more information, see [Working with DB parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html)in the*Amazon RDS User Guide*and[Working with DB parameter groups and DB cluster parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html)in the*Amazon Aurora User Guide*.**Example 2: To reset specific parameters to their default values**The following `reset-db-parameter-group`example resets the parameter values for specific parameters to their default values in a customer-created DB parameter group.`aws rds reset-db-parameter-group \ --db-parameter-group-name``mypg`\ --parameters`"ParameterName=max_connections,ApplyMethod=immediate"`\`"ParameterName=max_allowed_packet,ApplyMethod=immediate"`Output: `{ "DBParameterGroupName": "mypg" }`For more information, see [Working with DB parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html)in the*Amazon RDS User Guide*and[Working with DB parameter groups and DB cluster parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [ResetDbParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/reset-db-parameter-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `restore-db-cluster-from-s3`.

- **AWS CLI**
- 
            
                    **To restore an Amazon Aurora DB cluster from Amazon S3**The following `restore-db-cluster-from-s3`example restores an Amazon Aurora MySQL version 5.7-compatible DB cluster from a MySQL 5.7 DB backup file in Amazon S3.`aws rds restore-db-cluster-from-s3 \ --db-cluster-identifier``cluster-s3-restore`\ --engine`aurora-mysql`\ --master-username`admin`\ --master-user-password`mypassword`\ --s3-bucket-name`amzn-s3-demo-bucket`\ --s3-prefix`test-backup`\ --s3-ingestion-role-arn`arn:aws:iam::123456789012:role/service-role/TestBackup`\ --source-engine`mysql`\ --source-engine-version`5.7.28`Output: `{ "DBCluster": { "AllocatedStorage": 1, "AvailabilityZones": [ "us-west-2c", "us-west-2a", "us-west-2b" ], "BackupRetentionPeriod": 1, "DBClusterIdentifier": "cluster-s3-restore", "DBClusterParameterGroup": "default.aurora-mysql5.7", "DBSubnetGroup": "default", "Status": "creating", "Endpoint": "cluster-s3-restore.cluster-co3xyzabc123.us-west-2.rds.amazonaws.com", "ReaderEndpoint": "cluster-s3-restore.cluster-ro-co3xyzabc123.us-west-2.rds.amazonaws.com", "MultiAZ": false, "Engine": "aurora-mysql", "EngineVersion": "5.7.12", "Port": 3306, "MasterUsername": "admin", "PreferredBackupWindow": "11:15-11:45", "PreferredMaintenanceWindow": "thu:12:19-thu:12:49", "ReadReplicaIdentifiers": [], "DBClusterMembers": [], "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sg-########", "Status": "active" } ], "HostedZoneId": "Z1PVIF0EXAMPLE", "StorageEncrypted": false, "DbClusterResourceId": "cluster-SU5THYQQHOWCXZZDGXREXAMPLE", "DBClusterArn": "arn:aws:rds:us-west-2:123456789012:cluster:cluster-s3-restore", "AssociatedRoles": [], "IAMDatabaseAuthenticationEnabled": false, "ClusterCreateTime": "2020-07-27T14:22:08.095Z", "EngineMode": "provisioned", "DeletionProtection": false, "HttpEndpointEnabled": false, "CopyTagsToSnapshot": false, "CrossAccountClone": false, "DomainMemberships": [] } }`For more information, see [Migrating Data from MySQL by Using an Amazon S3 Bucket](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.ExtMySQL.html#AuroraMySQL.Migrating.ExtMySQL.S3)in the*Amazon Aurora User Guide*.- 
                    For API details, see [RestoreDbClusterFromS3](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/restore-db-cluster-from-s3.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `restore-db-cluster-from-snapshot`.

- **AWS CLI**
- 
            
                    **To restore a DB cluster from a snapshot**The following `restore-db-cluster-from-snapshot`restores an Aurora PostgreSQL DB cluster compatible with PostgreSQL version 10.7 from a DB cluster snapshot named`test-instance-snapshot`.`aws rds restore-db-cluster-from-snapshot \ --db-cluster-identifier``newdbcluster`\ --snapshot-identifier`test-instance-snapshot`\ --engine`aurora-postgresql`\ --engine-version`10.7`Output: `{ "DBCluster": { "AllocatedStorage": 1, "AvailabilityZones": [ "us-west-2c", "us-west-2a", "us-west-2b" ], "BackupRetentionPeriod": 7, "DatabaseName": "", "DBClusterIdentifier": "newdbcluster", "DBClusterParameterGroup": "default.aurora-postgresql10", "DBSubnetGroup": "default", "Status": "creating", "Endpoint": "newdbcluster.cluster-############.us-west-2.rds.amazonaws.com", "ReaderEndpoint": "newdbcluster.cluster-ro-############.us-west-2.rds.amazonaws.com", "MultiAZ": false, "Engine": "aurora-postgresql", "EngineVersion": "10.7", "Port": 5432, "MasterUsername": "postgres", "PreferredBackupWindow": "09:33-10:03", "PreferredMaintenanceWindow": "sun:12:22-sun:12:52", "ReadReplicaIdentifiers": [], "DBClusterMembers": [], "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sg-########", "Status": "active" } ], "HostedZoneId": "Z1PVIF0EXAMPLE", "StorageEncrypted": true, "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/287364e4-33e3-4755-a3b0-a1b2c3d4e5f6", "DbClusterResourceId": "cluster-5DSB5IFQDDUVAWOUWM1EXAMPLE", "DBClusterArn": "arn:aws:rds:us-west-2:123456789012:cluster:newdbcluster", "AssociatedRoles": [], "IAMDatabaseAuthenticationEnabled": false, "ClusterCreateTime": "2020-06-05T15:06:58.634Z", "EngineMode": "provisioned", "DeletionProtection": false, "HttpEndpointEnabled": false, "CopyTagsToSnapshot": false, "CrossAccountClone": false, "DomainMemberships": [] } }`For more information, see [Restoring from a DB Cluster Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_RestoreFromSnapshot.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [RestoreDbClusterFromSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/restore-db-cluster-from-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `restore-db-cluster-to-point-in-time`.

- **AWS CLI**
- 
            
                    **To restore a DB cluster to a specified time**The following `restore-db-cluster-to-point-in-time`example restores the DB cluster named`database-4`to the latest possible time. Using`copy-on-write`as the restore type restores the new DB cluster as a clone of the source DB cluster.`aws rds restore-db-cluster-to-point-in-time \ --source-db-cluster-identifier``database-4`\ --db-cluster-identifier`sample-cluster-clone`\ --restore-type`copy-on-write`\ --use-latest-restorable-timeOutput: `{ "DBCluster": { "AllocatedStorage": 1, "AvailabilityZones": [ "us-west-2c", "us-west-2a", "us-west-2b" ], "BackupRetentionPeriod": 7, "DatabaseName": "", "DBClusterIdentifier": "sample-cluster-clone", "DBClusterParameterGroup": "default.aurora-postgresql10", "DBSubnetGroup": "default", "Status": "creating", "Endpoint": "sample-cluster-clone.cluster-############.us-west-2.rds.amazonaws.com", "ReaderEndpoint": "sample-cluster-clone.cluster-ro-############.us-west-2.rds.amazonaws.com", "MultiAZ": false, "Engine": "aurora-postgresql", "EngineVersion": "10.7", "Port": 5432, "MasterUsername": "postgres", "PreferredBackupWindow": "09:33-10:03", "PreferredMaintenanceWindow": "sun:12:22-sun:12:52", "ReadReplicaIdentifiers": [], "DBClusterMembers": [], "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sg-########", "Status": "active" } ], "HostedZoneId": "Z1PVIF0EXAMPLE", "StorageEncrypted": true, "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/287364e4-33e3-4755-a3b0-a1b2c3d4e5f6", "DbClusterResourceId": "cluster-BIZ77GDSA2XBSTNPFW1EXAMPLE", "DBClusterArn": "arn:aws:rds:us-west-2:123456789012:cluster:sample-cluster-clone", "AssociatedRoles": [], "IAMDatabaseAuthenticationEnabled": false, "CloneGroupId": "8d19331a-099a-45a4-b4aa-11aa22bb33cc44dd", "ClusterCreateTime": "2020-03-10T19:57:38.967Z", "EngineMode": "provisioned", "DeletionProtection": false, "HttpEndpointEnabled": false, "CopyTagsToSnapshot": false, "CrossAccountClone": false } }`For more information, see [Restoring a DB Cluster to a Specified Time](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PIT.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [RestoreDbClusterToPointInTime](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/restore-db-cluster-to-point-in-time.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `restore-db-instance-from-db-snapshot`.

- **AWS CLI**
- 
            
                    **To restore a DB instance from a DB snapshot**The following `restore-db-instance-from-db-snapshot`example creates a new DB instance named`db7-new-instance`with the`db.t3.small`DB instance class from the specified DB snapshot. The source DB instance from which the snapshot was taken uses a deprecated DB instance class, so you can't upgrade it.`aws rds restore-db-instance-from-db-snapshot \ --db-instance-identifier``db7-new-instance`\ --db-snapshot-identifier`db7-test-snapshot`\ --db-instance-class`db.t3.small`Output: `{ "DBInstance": { "DBInstanceIdentifier": "db7-new-instance", "DBInstanceClass": "db.t3.small", "Engine": "mysql", "DBInstanceStatus": "creating", ...output omitted... "PreferredMaintenanceWindow": "mon:07:37-mon:08:07", "PendingModifiedValues": {}, "MultiAZ": false, "EngineVersion": "5.7.22", "AutoMinorVersionUpgrade": true, "ReadReplicaDBInstanceIdentifiers": [], "LicenseModel": "general-public-license", ...output omitted... "DBInstanceArn": "arn:aws:rds:us-west-2:123456789012:db:db7-new-instance", "IAMDatabaseAuthenticationEnabled": false, "PerformanceInsightsEnabled": false, "DeletionProtection": false, "AssociatedRoles": [] } }`For more information, see [Restoring from a DB Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_RestoreFromSnapshot.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [RestoreDbInstanceFromDbSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/restore-db-instance-from-db-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `restore-db-instance-from-s3`.

- **AWS CLI**
- 
            
                    **To restore a DB instance from a backup in Amazon S3**The following `restore-db-instance-from-s3`example creates a new DB instance named`restored-test-instance`from an existing backup in the`my-backups`S3 bucket.`aws rds restore-db-instance-from-s3 \ --db-instance-identifier``restored-test-instance`\ --allocated-storage`250`--db-instance-class`db.m4.large`--engine`mysql`\ --`master`-username master --master-user-password`secret99`\ --s3-bucket-name`my-backups`--s3-ingestion-role-arn`arn:aws:iam::123456789012:role/my-role`\ --source-engine`mysql`--source-engine-version`5.6.27`- 
                    For API details, see [RestoreDbInstanceFromS3](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/restore-db-instance-from-s3.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `restore-db-instance-to-point-in-time`.

- **AWS CLI**
- 
            
                    **Example 1: To restore a DB instance to a point in time**The following `restore-db-instance-to-point-in-time`example restores`test-instance`to a new DB instance named`restored-test-instance`, as of the specified time.`aws rds restore-db-instance-to-point-in-time \ --source-db-instance-identifier``test-instance`\ --target-db-instance`restored-test-instance`\ --restore-time`2018-07-30T23:45:00.000Z`Output: `{ "DBInstance": { "AllocatedStorage": 20, "DBInstanceArn": "arn:aws:rds:us-east-1:123456789012:db:restored-test-instance", "DBInstanceStatus": "creating", "DBInstanceIdentifier": "restored-test-instance", ...some output omitted... } }`For more information, see [Restoring a DB instance to a specified time](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIT.html)in the*Amazon RDS User Guide*.**Example 2: To restore a DB instance to a specified time from a replicated backup**The following `restore-db-instance-to-point-in-time`example restores an Oracle DB instance to the specified time from a replicated automated backup.`aws rds restore-db-instance-to-point-in-time \ --source-db-instance-automated-backups-arn``"arn:aws:rds:us-west-2:123456789012:auto-backup:ab-jkib2gfq5rv7replzadausbrktni2bn4example"`\ --target-db-instance-identifier`myorclinstance-from-replicated-backup`\ --restore-time`2020-12-08T18:45:00.000Z`Output: `{ "DBInstance": { "DBInstanceIdentifier": "myorclinstance-from-replicated-backup", "DBInstanceClass": "db.t3.micro", "Engine": "oracle-se2", "DBInstanceStatus": "creating", "MasterUsername": "admin", "DBName": "ORCL", "AllocatedStorage": 20, "PreferredBackupWindow": "07:45-08:15", "BackupRetentionPeriod": 14, ... some output omitted ... "DbiResourceId": "db-KGLXG75BGVIWKQT7NQ4EXAMPLE", "CACertificateIdentifier": "rds-ca-2019", "DomainMemberships": [], "CopyTagsToSnapshot": false, "MonitoringInterval": 0, "DBInstanceArn": "arn:aws:rds:us-west-2:123456789012:db:myorclinstance-from-replicated-backup", "IAMDatabaseAuthenticationEnabled": false, "PerformanceInsightsEnabled": false, "DeletionProtection": false, "AssociatedRoles": [], "TagList": [] } }`For more information, see [Restoring to a specified time from a replicated backup](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReplicateBackups.html#AutomatedBackups.PiTR)in the*Amazon RDS User Guide*.- 
                    For API details, see [RestoreDbInstanceToPointInTime](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/restore-db-instance-to-point-in-time.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-activity-stream`.

- **AWS CLI**
- 
            
                    **To start a database activity stream**The following `start-activity-stream`example starts an asynchronous activity stream to monitor an Aurora cluster named my-pg-cluster.`aws rds start-activity-stream \ --region``us-east-1`\ --mode`async`\ --kms-key-id`arn:aws:kms:us-east-1:1234567890123:key/a12c345d-6ef7-890g-h123-456i789jk0l1`\ --resource-arn`arn:aws:rds:us-east-1:1234567890123:cluster:my-pg-cluster`\ --apply-immediatelyOutput: `{ "KmsKeyId": "arn:aws:kms:us-east-1:1234567890123:key/a12c345d-6ef7-890g-h123-456i789jk0l1", "KinesisStreamName": "aws-rds-das-cluster-0ABCDEFGHI1JKLM2NOPQ3R4S", "Status": "starting", "Mode": "async", "ApplyImmediately": true }`For more information, see [Starting a database activity stream](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/DBActivityStreams.html#DBActivityStreams.Enabling)in the*Amazon Aurora User Guide*.- 
                    For API details, see [StartActivityStream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/start-activity-stream.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-db-cluster`.

- **AWS CLI**
- 
            
                    **To start a DB cluster**The following `start-db-cluster`example starts a DB cluster and its DB instances.`aws rds start-db-cluster \ --db-cluster-identifier``mydbcluster`Output: `{ "DBCluster": { "AllocatedStorage": 1, "AvailabilityZones": [ "us-east-1a", "us-east-1e", "us-east-1b" ], "BackupRetentionPeriod": 1, "DatabaseName": "mydb", "DBClusterIdentifier": "mydbcluster", ...some output truncated... } }`For more information, see [Stopping and starting an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-cluster-stop-start.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [StartDbCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/start-db-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-db-instance-automated-backups-replication`.

- **AWS CLI**
- 
            
                    **To enable cross-Region automated backups**The following `start-db-instance-automated-backups-replication`example replicates automated backups from a DB instance in the US East (N. Virginia) Region to US West (Oregon). The backup retention period is 14 days.`aws rds start-db-instance-automated-backups-replication \ --region``us-west-2`\ --source-db-instance-arn`"arn:aws:rds:us-east-1:123456789012:db:new-orcl-db"`\ --backup-retention-period`14`Output: `{ "DBInstanceAutomatedBackup": { "DBInstanceArn": "arn:aws:rds:us-east-1:123456789012:db:new-orcl-db", "DbiResourceId": "db-JKIB2GFQ5RV7REPLZA4EXAMPLE", "Region": "us-east-1", "DBInstanceIdentifier": "new-orcl-db", "RestoreWindow": {}, "AllocatedStorage": 20, "Status": "pending", "Port": 1521, "InstanceCreateTime": "2020-12-04T15:28:31Z", "MasterUsername": "admin", "Engine": "oracle-se2", "EngineVersion": "12.1.0.2.v21", "LicenseModel": "bring-your-own-license", "OptionGroupName": "default:oracle-se2-12-1", "Encrypted": false, "StorageType": "gp2", "IAMDatabaseAuthenticationEnabled": false, "BackupRetentionPeriod": 14, "DBInstanceAutomatedBackupsArn": "arn:aws:rds:us-west-2:123456789012:auto-backup:ab-jkib2gfq5rv7replzadausbrktni2bn4example" } }`For more information, see [Enabling cross-Region automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReplicateBackups.html#AutomatedBackups.Replicating.Enable)in the*Amazon RDS User Guide*.- 
                    For API details, see [StartDbInstanceAutomatedBackupsReplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/start-db-instance-automated-backups-replication.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-db-instance`.

- **AWS CLI**
- 
            
                    **To start a DB instance**The following `start-db-instance`example starts the specified DB instance.`aws rds start-db-instance \ --db-instance-identifier``test-instance`Output: `{ "DBInstance": { "DBInstanceStatus": "starting", ...some output truncated... } }`- 
                    For API details, see [StartDbInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/start-db-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-export-task`.

- **AWS CLI**
- 
            
                    **To export a snapshot to Amazon S3**The following `start-export-task`example exports a DB snapshot named`db5-snapshot-test`to the Amazon S3 bucket named`amzn-s3-demo-bucket`.`aws rds start-export-task \ --export-task-identifier``my-s3-export`\ --source-arn`arn:aws:rds:us-west-2:123456789012:snapshot:db5-snapshot-test`\ --s3-bucket-name`amzn-s3-demo-bucket`\ --iam-role-arn`arn:aws:iam::123456789012:role/service-role/ExportRole`\ --kms-key-id`arn:aws:kms:us-west-2:123456789012:key/abcd0000-7fca-4128-82f2-aabbccddeeff`Output: `{ "ExportTaskIdentifier": "my-s3-export", "SourceArn": "arn:aws:rds:us-west-2:123456789012:snapshot:db5-snapshot-test", "SnapshotTime": "2020-03-27T20:48:42.023Z", "S3Bucket": "amzn-s3-demo-bucket", "IamRoleArn": "arn:aws:iam::123456789012:role/service-role/ExportRole", "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/abcd0000-7fca-4128-82f2-aabbccddeeff", "Status": "STARTING", "PercentProgress": 0, "TotalExtractedDataInGB": 0 }`For more information, see [Exporting a Snapshot to an Amazon S3 Bucket](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ExportSnapshot.html#USER_ExportSnapshot.Exporting)in the*Amazon RDS User Guide*.- 
                    For API details, see [StartExportTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/start-export-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-activity-stream`.

- **AWS CLI**
- 
            
                    **To stop a database activity stream**The following `stop-activity-stream`example stops an activity stream in an Aurora cluster named my-pg-cluster.`aws rds stop-activity-stream \ --region``us-east-1`\ --resource-arn`arn:aws:rds:us-east-1:1234567890123:cluster:my-pg-cluster`\ --apply-immediatelyOutput: `{ "KmsKeyId": "arn:aws:kms:us-east-1:1234567890123:key/a12c345d-6ef7-890g-h123-456i789jk0l1", "KinesisStreamName": "aws-rds-das-cluster-0ABCDEFGHI1JKLM2NOPQ3R4S", "Status": "stopping" }`For more information, see [Stopping an activity stream](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/DBActivityStreams.html#DBActivityStreams.Disabling)in the*Amazon Aurora User Guide*.- 
                    For API details, see [StopActivityStream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/stop-activity-stream.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-db-cluster`.

- **AWS CLI**
- 
            
                    **To stop a DB cluster**The following `stop-db-cluster`example stops a DB cluster and its DB instances.`aws rds stop-db-cluster \ --db-cluster-identifier``mydbcluster`Output: `{ "DBCluster": { "AllocatedStorage": 1, "AvailabilityZones": [ "us-east-1a", "us-east-1e", "us-east-1b" ], "BackupRetentionPeriod": 1, "DatabaseName": "mydb", "DBClusterIdentifier": "mydbcluster", ...some output truncated... } }`For more information, see [Stopping and starting an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-cluster-stop-start.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [StopDbCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/stop-db-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-db-instance-automated-backups-replication`.

- **AWS CLI**
- 
            
                    **To stop replicating automated backups**The following `stop-db-instance-automated-backups-replication`ends replication of automated backups to the US West (Oregon) Region. Replicated backups are retained according to the set backup retention period.`aws rds stop-db-instance-automated-backups-replication \ --region``us-west-2`\ --source-db-instance-arn`"arn:aws:rds:us-east-1:123456789012:db:new-orcl-db"`Output: `{ "DBInstanceAutomatedBackup": { "DBInstanceArn": "arn:aws:rds:us-east-1:123456789012:db:new-orcl-db", "DbiResourceId": "db-JKIB2GFQ5RV7REPLZA4EXAMPLE", "Region": "us-east-1", "DBInstanceIdentifier": "new-orcl-db", "RestoreWindow": { "EarliestTime": "2020-12-04T23:13:21.030Z", "LatestTime": "2020-12-07T19:59:57Z" }, "AllocatedStorage": 20, "Status": "replicating", "Port": 1521, "InstanceCreateTime": "2020-12-04T15:28:31Z", "MasterUsername": "admin", "Engine": "oracle-se2", "EngineVersion": "12.1.0.2.v21", "LicenseModel": "bring-your-own-license", "OptionGroupName": "default:oracle-se2-12-1", "Encrypted": false, "StorageType": "gp2", "IAMDatabaseAuthenticationEnabled": false, "BackupRetentionPeriod": 7, "DBInstanceAutomatedBackupsArn": "arn:aws:rds:us-west-2:123456789012:auto-backup:ab-jkib2gfq5rv7replzadausbrktni2bn4example" } }`For more information, see [Stopping automated backup replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReplicateBackups.html#AutomatedBackups.StopReplicating)in the*Amazon RDS User Guide*.- 
                    For API details, see [StopDbInstanceAutomatedBackupsReplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/stop-db-instance-automated-backups-replication.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-db-instance`.

- **AWS CLI**
- 
            
                    **To stop a DB instance**The following `stop-db-instance`example stops the specified DB instance.`aws rds stop-db-instance \ --db-instance-identifier``test-instance`Output: `{ "DBInstance": { "DBInstanceStatus": "stopping", ...some output truncated... } }`- 
                    For API details, see [StopDbInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/stop-db-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `switchover-blue-green-deployment`.

- **AWS CLI**
- 
            
                    **Example 1: To switch a blue/green deployment for an RDS DB instance**The following `switchover-blue-green-deployment`example promotes the specified green environment as the new production environment.`aws rds switchover-blue-green-deployment \ --blue-green-deployment-identifier``bgd-wi89nwzglccsfake`\ --switchover-timeout`300`Output: `{ "BlueGreenDeployment": { "BlueGreenDeploymentIdentifier": "bgd-v53303651eexfake", "BlueGreenDeploymentName": "bgd-cli-test-instance", "Source": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance", "Target": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-green-blhi1e", "SwitchoverDetails": [ { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-green-blhi1e", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-replica-1", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-replica-1-green-k5fv7u", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-replica-2", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-replica-2-green-ggsh8m", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-replica-3", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-db-instance-replica-3-green-o2vwm0", "Status": "AVAILABLE" } ], "Tasks": [ { "Name": "CREATING_READ_REPLICA_OF_SOURCE", "Status": "COMPLETED" }, { "Name": "DB_ENGINE_VERSION_UPGRADE", "Status": "COMPLETED" }, { "Name": "CONFIGURE_BACKUPS", "Status": "COMPLETED" }, { "Name": "CREATING_TOPOLOGY_OF_SOURCE", "Status": "COMPLETED" } ], "Status": "SWITCHOVER_IN_PROGRESS", "CreateTime": "2022-02-25T22:33:22.225000+00:00" } }`For more information, see [Switching a blue/green deployment](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments-switching.html)in the*Amazon RDS User Guide*.**Example 2: To promote a blue/green deployment for an Aurora MySQL DB cluster**The following `switchover-blue-green-deployment`example promotes the specified green environment as the new production environment.`aws rds switchover-blue-green-deployment \ --blue-green-deployment-identifier``bgd-wi89nwzglccsfake`\ --switchover-timeout`300`Output: `{ "BlueGreenDeployment": { "BlueGreenDeploymentIdentifier": "bgd-wi89nwzglccsfake", "BlueGreenDeploymentName": "my-blue-green-deployment", "Source": "arn:aws:rds:us-east-1:123456789012:cluster:my-aurora-mysql-cluster", "Target": "arn:aws:rds:us-east-1:123456789012:cluster:my-aurora-mysql-cluster-green-3ud8z6", "SwitchoverDetails": [ { "SourceMember": "arn:aws:rds:us-east-1:123456789012:cluster:my-aurora-mysql-cluster", "TargetMember": "arn:aws:rds:us-east-1:123456789012:cluster:my-aurora-mysql-cluster-green-3ud8z6", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-1", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-1-green-bvxc73", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-2", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-2-green-7wc4ie", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-3", "TargetMember": "arn:aws:rds:us-east-1:123456789012:db:my-aurora-mysql-cluster-3-green-p4xxkz", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:cluster-endpoint:my-excluded-member-endpoint", "TargetMember": "arn:aws:rds:us-east-1:123456789012:cluster-endpoint:my-excluded-member-endpoint-green-np1ikl", "Status": "AVAILABLE" }, { "SourceMember": "arn:aws:rds:us-east-1:123456789012:cluster-endpoint:my-reader-endpoint", "TargetMember": "arn:aws:rds:us-east-1:123456789012:cluster-endpoint:my-reader-endpoint-green-miszlf", "Status": "AVAILABLE" } ], "Tasks": [ { "Name": "CREATING_READ_REPLICA_OF_SOURCE", "Status": "COMPLETED" }, { "Name": "DB_ENGINE_VERSION_UPGRADE", "Status": "COMPLETED" }, { "Name": "CREATE_DB_INSTANCES_FOR_CLUSTER", "Status": "COMPLETED" }, { "Name": "CREATE_CUSTOM_ENDPOINTS", "Status": "COMPLETED" } ], "Status": "SWITCHOVER_IN_PROGRESS", "CreateTime": "2022-02-25T22:38:49.522000+00:00" } }`For more information, see [Switching a blue/green deployment](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-switching.html)in the*Amazon Aurora User Guide*.- 
                    For API details, see [SwitchoverBlueGreenDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/switchover-blue-green-deployment.html)in*AWS CLI Command Reference*.
 
-