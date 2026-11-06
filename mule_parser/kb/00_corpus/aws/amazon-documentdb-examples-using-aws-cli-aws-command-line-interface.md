# Amazon DocumentDB examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_docdb_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_docdb_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon DocumentDB.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `add-tags-to-resource`.

- **AWS CLI**
- 
            
                    **To add one or more tags to a specified resource**The following `add-tags-to-resource`example adds three tags to`sample-cluster`. One tag (`CropB`) has a key name but no value.`aws docdb add-tags-to-resource \ --resource-name``arn:aws:rds:us-west-2:123456789012:cluster:sample-cluster`\ --tags Key="CropA",Value="Apple" Key="CropB" Key="CropC",Value="Corn"This command produces no output. For more information, see [Tagging Amazon DocumentDB Resources](https://docs.aws.amazon.com/documentdb/latest/developerguide/tagging.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [AddTagsToResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/add-tags-to-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `apply-pending-maintenance-action`.

- **AWS CLI**
- 
            
                    **To have pending maintenance actions take place during the next maintenance window**The following `apply-pending-maintenance-action`example causes all system-update actions to be performed during the next scheduled maintenance window.`aws docdb apply-pending-maintenance-action \ --resource-identifier``arn:aws:rds:us-west-2:123456789012:cluster:sample-cluster`\ --apply-action`system-update`\ --opt-in-type`next-maintenance`This command produces no output. For more information, see [Applying Amazon DocumentDB Updates](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-maintain.html#db-instance-updates-apply)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [ApplyPendingMaintenanceAction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/apply-pending-maintenance-action.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `copy-db-cluster-parameter-group`.

- **AWS CLI**
- 
            
                    **To duplicate an existing DB cluster parameter group**The following `copy-db-cluster-parameter-group`example makes a copy of the parameter group`custom-docdb3-6`named`custom-docdb3-6-copy`. When making the copy it adds tags to the new parameter group.`aws docdb copy-db-cluster-parameter-group \ --source-db-cluster-parameter-group-identifier``custom-docdb3-6`\ --target-db-cluster-parameter-group-identifier`custom-docdb3-6-copy`\ --target-db-cluster-parameter-group-description`"Copy of custom-docdb3-6"`\ --tags Key="CopyNumber",Value="1" Key="Modifiable",Value="Yes"Output: `{ "DBClusterParameterGroup": { "DBParameterGroupFamily": "docdb3.6", "DBClusterParameterGroupArn": "arn:aws:rds:us-east-1:12345678901:cluster-pg:custom-docdb3-6-copy", "DBClusterParameterGroupName": "custom-docdb3-6-copy", "Description": "Copy of custom-docdb3-6" } }`For more information, see [Copying an Amazon DocumentDB Cluster Parameter Group](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-parameter-group-copy.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [CopyDbClusterParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/copy-db-cluster-parameter-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `copy-db-cluster-snapshot`.

- **AWS CLI**
- 
            
                    **To create a copy of a snapshot**The following `copy-db-cluster-snapshot`example makes a copy of`sample-cluster-snapshot`named`sample-cluster-snapshot-copy`. The copy has all the tags of the original plus a new tag with the key name`CopyNumber`.`aws docdb copy-db-cluster-snapshot \ --source-db-cluster-snapshot-identifier``sample-cluster-snapshot`\ --target-db-cluster-snapshot-identifier`sample-cluster-snapshot-copy`\ --copy-tags \ --tags Key="CopyNumber",Value="1"This command produces no output. For more information, see [Copying a Cluster Snapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/backup-restore.db-cluster-snapshot-copy.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [CopyDbClusterSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/copy-db-cluster-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-db-cluster-parameter-group`.

- **AWS CLI**
- 
            
                    **To create an Amazon DocumentDB cluster parameter group**The following `create-db-cluster-parameter-group`example creates the DB cluster parameter group`sample-parameter-group`using the`docdb3.6`family.`aws docdb create-db-cluster-parameter-group \ --db-cluster-parameter-group-name``sample-parameter-group`\ --db-parameter-group-family`docdb3.6`\ --description`"Sample parameter group based on docdb3.6"`Output: `{ "DBClusterParameterGroup": { "Description": "Sample parameter group based on docdb3.6", "DBParameterGroupFamily": "docdb3.6", "DBClusterParameterGroupArn": "arn:aws:rds:us-west-2:123456789012:cluster-pg:sample-parameter-group", "DBClusterParameterGroupName": "sample-parameter-group" } }`For more information, see [Creating an Amazon DocumentDB Cluster Parameter Group](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-parameter-group-create.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [CreateDbClusterParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/create-db-cluster-parameter-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-db-cluster-snapshot`.

- **AWS CLI**
- 
            
                    **To create a manual Amazon DocumentDB cluster snapshot**The following `create-db-cluster-snapshot`example creates an Amazon DB cluster snapshot named sample-cluster-snapshot.`aws docdb create-db-cluster-snapshot \ --db-cluster-identifier``sample-cluster`\ --db-cluster-snapshot-identifier`sample-cluster-snapshot`Output: `{ "DBClusterSnapshot": { "MasterUsername": "master-user", "SnapshotCreateTime": "2019-03-18T18:27:14.794Z", "AvailabilityZones": [ "us-west-2a", "us-west-2b", "us-west-2c", "us-west-2d", "us-west-2e", "us-west-2f" ], "SnapshotType": "manual", "DBClusterSnapshotArn": "arn:aws:rds:us-west-2:123456789012:cluster-snapshot:sample-cluster-snapshot", "EngineVersion": "3.6.0", "PercentProgress": 0, "DBClusterSnapshotIdentifier": "sample-cluster-snapshot", "Engine": "docdb", "DBClusterIdentifier": "sample-cluster", "Status": "creating", "ClusterCreateTime": "2019-03-15T20:29:58.836Z", "Port": 0, "StorageEncrypted": false, "VpcId": "vpc-91280df6" } }`For more information, see [Creating a Manual Cluster Snapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/backup-restore.db-cluster-snapshot-create.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [CreateDbClusterSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/create-db-cluster-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-db-cluster`.

- **AWS CLI**
- 
            
                    **To create an Amazon DocumentDB cluster**The following `create-db-cluster`example creates an Amazon DocumentDB cluster named`sample-cluster`with the preferred maintenance window on Sundays between 20:30 and 11:00.`aws docdb create-db-cluster \ --db-cluster-identifier``sample-cluster`\ --engine`docdb`\ --`master-user`name master-user \ --master-user-`password`password \ --preferred-maintenance-window`Sun:20:30-Sun:21:00`Output: `{ "DBCluster": { "DBClusterParameterGroup": "default.docdb3.6", "AssociatedRoles": [], "DBSubnetGroup": "default", "ClusterCreateTime": "2019-03-18T18:06:34.616Z", "Status": "creating", "Port": 27017, "PreferredMaintenanceWindow": "sun:20:30-sun:21:00", "HostedZoneId": "ZNKXH85TT8WVW", "DBClusterMembers": [], "Engine": "docdb", "DBClusterIdentifier": "sample-cluster", "PreferredBackupWindow": "10:12-10:42", "AvailabilityZones": [ "us-west-2d", "us-west-2f", "us-west-2e" ], "MasterUsername": "master-user", "BackupRetentionPeriod": 1, "ReaderEndpoint": "sample-cluster.cluster-ro-corcjozrlsfc.us-west-2.docdb.amazonaws.com", "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sg-77186e0d", "Status": "active" } ], "StorageEncrypted": false, "DBClusterArn": "arn:aws:rds:us-west-2:123456789012:cluster:sample-cluster", "DbClusterResourceId": "cluster-L3R4YRSBUYDP4GLMTJ2WF5GH5Q", "MultiAZ": false, "Endpoint": "sample-cluster.cluster-corcjozrlsfc.us-west-2.docdb.amazonaws.com", "EngineVersion": "3.6.0" } }`For more information, see [Creating an Amazon DocumentDB Cluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-create.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [CreateDbCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/create-db-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-db-instance`.

- **AWS CLI**
- 
            
                    **To create an Amazon DocumentDB cluster instance**The following `create-db-instance`example code creates the instance`sample-cluster-instance-2`in the Amazon DocumentDB cluster`sample-cluster`.`aws docdb create-db-instance \ --db-cluster-identifier``sample-cluster`\ --db-instance-class`db.r4.xlarge`\ --db-instance-identifier`sample-cluster-instance-2`\ --engine`docdb`Output: `{ "DBInstance": { "DBInstanceStatus": "creating", "PendingModifiedValues": { "PendingCloudwatchLogsExports": { "LogTypesToEnable": [ "audit" ] } }, "PubliclyAccessible": false, "PreferredBackupWindow": "00:00-00:30", "PromotionTier": 1, "EngineVersion": "3.6.0", "BackupRetentionPeriod": 3, "DBInstanceIdentifier": "sample-cluster-instance-2", "PreferredMaintenanceWindow": "tue:10:28-tue:10:58", "StorageEncrypted": false, "Engine": "docdb", "DBClusterIdentifier": "sample-cluster", "DBSubnetGroup": { "Subnets": [ { "SubnetAvailabilityZone": { "Name": "us-west-2a" }, "SubnetStatus": "Active", "SubnetIdentifier": "subnet-4e26d263" }, { "SubnetAvailabilityZone": { "Name": "us-west-2c" }, "SubnetStatus": "Active", "SubnetIdentifier": "subnet-afc329f4" }, { "SubnetAvailabilityZone": { "Name": "us-west-2d" }, "SubnetStatus": "Active", "SubnetIdentifier": "subnet-53ab3636" }, { "SubnetAvailabilityZone": { "Name": "us-west-2b" }, "SubnetStatus": "Active", "SubnetIdentifier": "subnet-991cb8d0" } ], "DBSubnetGroupDescription": "default", "SubnetGroupStatus": "Complete", "VpcId": "vpc-91280df6", "DBSubnetGroupName": "default" }, "DBInstanceClass": "db.r4.xlarge", "VpcSecurityGroups": [ { "Status": "active", "VpcSecurityGroupId": "sg-77186e0d" } ], "DBInstanceArn": "arn:aws:rds:us-west-2:123456789012:db:sample-cluster-instance-2", "DbiResourceId": "db-XEKJLEMGRV5ZKCARUVA4HO3ITE" } }`For more information, see [Adding an Amazon DocumentDB Instance to a Cluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-add.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [CreateDbInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/create-db-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-db-subnet-group`.

- **AWS CLI**
- 
            
                    **To create an Amazon DocumentDB subnet group**The following `create-db-subnet-group`example creates an Amazon DocumentDB subnet group named`sample-subnet-group`.`aws docdb create-db-subnet-group \ --db-subnet-group-description``"a sample subnet group"`\ --db-subnet-group-name`sample-subnet-group`\ --subnet-ids`"subnet-29ab1025"``"subnet-991cb8d0"``"subnet-53ab3636"`Output: `{ "DBSubnetGroup": { "SubnetGroupStatus": "Complete", "DBSubnetGroupName": "sample-subnet-group", "DBSubnetGroupDescription": "a sample subnet group", "VpcId": "vpc-91280df6", "DBSubnetGroupArn": "arn:aws:rds:us-west-2:123456789012:subgrp:sample-subnet-group", "Subnets": [ { "SubnetStatus": "Active", "SubnetIdentifier": "subnet-53ab3636", "SubnetAvailabilityZone": { "Name": "us-west-2d" } }, { "SubnetStatus": "Active", "SubnetIdentifier": "subnet-991cb8d0", "SubnetAvailabilityZone": { "Name": "us-west-2b" } }, { "SubnetStatus": "Active", "SubnetIdentifier": "subnet-29ab1025", "SubnetAvailabilityZone": { "Name": "us-west-2c" } } ] } }`For more information, see [Creating an Amazon DocumentDB Subnet Group](https://docs.aws.amazon.com/documentdb/latest/developerguide/document-db-subnet-groups.html#document-db-subnet-group-create)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [CreateDbSubnetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/create-db-subnet-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-db-cluster-parameter-group`.

- **AWS CLI**
- 
            
                    **To delete an Amazon DocumentDB cluster parameter group**The following `delete-db-cluster-parameter-group`example deletes the Amazon DocumentDB parameter group`sample-parameter-group`.`aws docdb delete-db-cluster-parameter-group \ --db-cluster-parameter-group-name``sample-parameter-group`This command produces no output. For more information, see [Deleting an Amazon DocumentDB Cluster Parameter Group](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-parameter-group-delete.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [DeleteDbClusterParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/delete-db-cluster-parameter-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-db-cluster-snapshot`.

- **AWS CLI**
- 
            
                    **To delete an Amazon DocumentDB cluster snapshot**The following `delete-db-cluster-snapshot`example deletes the Amazon DocumentDB cluster snapshot`sample-cluster-snapshot`.`aws docdb delete-db-cluster-snapshot \ --db-cluster-snapshot-identifier``sample-cluster-snapshot`Output: `{ "DBClusterSnapshot": { "DBClusterIdentifier": "sample-cluster", "AvailabilityZones": [ "us-west-2a", "us-west-2b", "us-west-2c", "us-west-2d" ], "DBClusterSnapshotIdentifier": "sample-cluster-snapshot", "VpcId": "vpc-91280df6", "DBClusterSnapshotArn": "arn:aws:rds:us-west-2:123456789012:cluster-snapshot:sample-cluster-snapshot", "EngineVersion": "3.6.0", "Engine": "docdb", "SnapshotCreateTime": "2019-03-18T18:27:14.794Z", "Status": "available", "MasterUsername": "master-user", "ClusterCreateTime": "2019-03-15T20:29:58.836Z", "PercentProgress": 100, "StorageEncrypted": false, "SnapshotType": "manual", "Port": 0 } }`For more information, see [Deleting a Cluster Snapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/backup-restore.db-cluster-snapshot-delete.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [DeleteDbClusterSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/delete-db-cluster-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-db-cluster`.

- **AWS CLI**
- 
            
                    **To delete an Amazon DocumentDB cluster**The following `delete-db-cluster`example deletes the Amazon DocumentDB cluster`sample-cluster`. No backup of the cluster is made prior to deleting it. NOTE: You must delete all instances associated with the cluster before you can delete it.`aws docdb delete-db-cluster \ --db-cluster-identifier``sample-cluster`\ --skip-final-snapshotOutput: `{ "DBCluster": { "DBClusterIdentifier": "sample-cluster", "DBSubnetGroup": "default", "EngineVersion": "3.6.0", "Engine": "docdb", "LatestRestorableTime": "2019-03-18T18:07:24.610Z", "PreferredMaintenanceWindow": "sun:20:30-sun:21:00", "StorageEncrypted": false, "EarliestRestorableTime": "2019-03-18T18:07:24.610Z", "Port": 27017, "VpcSecurityGroups": [ { "Status": "active", "VpcSecurityGroupId": "sg-77186e0d" } ], "MultiAZ": false, "MasterUsername": "master-user", "DBClusterArn": "arn:aws:rds:us-west-2:123456789012:cluster:sample-cluster", "Status": "available", "PreferredBackupWindow": "10:12-10:42", "ReaderEndpoint": "sample-cluster.cluster-ro-corcjozrlsfc.us-west-2.docdb.amazonaws.com", "AvailabilityZones": [ "us-west-2c", "us-west-2b", "us-west-2a" ], "Endpoint": "sample-cluster.cluster-corcjozrlsfc.us-west-2.docdb.amazonaws.com", "DbClusterResourceId": "cluster-L3R4YRSBUYDP4GLMTJ2WF5GH5Q", "ClusterCreateTime": "2019-03-18T18:06:34.616Z", "AssociatedRoles": [], "DBClusterParameterGroup": "default.docdb3.6", "HostedZoneId": "ZNKXH85TT8WVW", "BackupRetentionPeriod": 1, "DBClusterMembers": [] } }`For more information, see [Deleting an Amazon DocumentDB Cluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-delete.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [DeleteDbCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/delete-db-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-db-instance`.

- **AWS CLI**
- 
            
                    **To delete an Amazon DocumentDB instance**The following `delete-db-instance`example deletes the Amazon DocumentDB instance`sample-cluster-instance-2`.`aws docdb delete-db-instance \ --db-instance-identifier``sample-cluster-instance-2`Output: `{ "DBInstance": { "DBSubnetGroup": { "Subnets": [ { "SubnetAvailabilityZone": { "Name": "us-west-2a" }, "SubnetStatus": "Active", "SubnetIdentifier": "subnet-4e26d263" }, { "SubnetAvailabilityZone": { "Name": "us-west-2c" }, "SubnetStatus": "Active", "SubnetIdentifier": "subnet-afc329f4" }, { "SubnetAvailabilityZone": { "Name": "us-west-2d" }, "SubnetStatus": "Active", "SubnetIdentifier": "subnet-53ab3636" }, { "SubnetAvailabilityZone": { "Name": "us-west-2b" }, "SubnetStatus": "Active", "SubnetIdentifier": "subnet-991cb8d0" } ], "DBSubnetGroupName": "default", "DBSubnetGroupDescription": "default", "VpcId": "vpc-91280df6", "SubnetGroupStatus": "Complete" }, "PreferredBackupWindow": "00:00-00:30", "InstanceCreateTime": "2019-03-18T18:37:33.709Z", "DBInstanceClass": "db.r4.xlarge", "DbiResourceId": "db-XEKJLEMGRV5ZKCARUVA4HO3ITE", "BackupRetentionPeriod": 3, "Engine": "docdb", "VpcSecurityGroups": [ { "Status": "active", "VpcSecurityGroupId": "sg-77186e0d" } ], "AutoMinorVersionUpgrade": true, "PromotionTier": 1, "EngineVersion": "3.6.0", "Endpoint": { "Address": "sample-cluster-instance-2.corcjozrlsfc.us-west-2.docdb.amazonaws.com", "HostedZoneId": "ZNKXH85TT8WVW", "Port": 27017 }, "DBInstanceIdentifier": "sample-cluster-instance-2", "PreferredMaintenanceWindow": "tue:10:28-tue:10:58", "EnabledCloudwatchLogsExports": [ "audit" ], "PendingModifiedValues": {}, "DBInstanceStatus": "deleting", "PubliclyAccessible": false, "DBInstanceArn": "arn:aws:rds:us-west-2:123456789012:db:sample-cluster-instance-2", "DBClusterIdentifier": "sample-cluster", "AvailabilityZone": "us-west-2c", "StorageEncrypted": false } }`For more information, see [Deleting an Amazon DocumentDB Instance](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-delete.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [DeleteDbInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/delete-db-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-db-subnet-group`.

- **AWS CLI**
- 
            
                    **To delete an Amazon DocumentDB subnet group**The following `delete-db-subnet-group`example deletes the Amazon DocumentDB subnet group`sample-subnet-group`.`aws docdb delete-db-subnet-group \ --db-subnet-group-name``sample-subnet-group`This command produces no output. For more information, see [Deleting an Amazon DocumentDB Subnet Group](https://docs.aws.amazon.com/documentdb/latest/developerguide/document-db-subnet-groups.html#document-db-subnet-group-delete)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [DeleteDbSubnetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/delete-db-subnet-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-cluster-parameter-groups`.

- **AWS CLI**
- 
            
                    **To see the details of one or more Amazon DocumentDB cluster parameter groups**The following `describe-db-cluster-parameter-groups`example displays details for the Amazon DocumentDB cluster parameter group`custom3-6-param-grp`.`aws docdb describe-db-cluster-parameter-groups \ --db-cluster-parameter-group-name``custom3-6-param-grp`Output: `{ "DBClusterParameterGroups": [ { "DBParameterGroupFamily": "docdb3.6", "DBClusterParameterGroupArn": "arn:aws:rds:us-east-1:123456789012:cluster-pg:custom3-6-param-grp", "Description": "Custom docdb3.6 parameter group", "DBClusterParameterGroupName": "custom3-6-param-grp" } ] }`For more information, see [Viewing Amazon DocumentDB Cluster Parameter Groups](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-parameter-group-describe.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [DescribeDbClusterParameterGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-cluster-parameter-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-cluster-parameters`.

- **AWS CLI**
- 
            
                    **To view the detailed parameter list for an Amazon DocumentDB cluster parameter group.**The following `describe-db-cluster-parameters`example lists the parameters for the Amazon DocumentDB parameter group custom3-6-param-grp.`aws docdb describe-db-cluster-parameters \ --db-cluster-parameter-group-name``custom3-6-param-grp`Output: `{ "Parameters": [ { "DataType": "string", "ParameterName": "audit_logs", "IsModifiable": true, "ApplyMethod": "pending-reboot", "Source": "system", "ApplyType": "dynamic", "AllowedValues": "enabled,disabled", "Description": "Enables auditing on cluster.", "ParameterValue": "disabled" }, { "DataType": "string", "ParameterName": "tls", "IsModifiable": true, "ApplyMethod": "pending-reboot", "Source": "system", "ApplyType": "static", "AllowedValues": "disabled,enabled", "Description": "Config to enable/disable TLS", "ParameterValue": "enabled" }, { "DataType": "string", "ParameterName": "ttl_monitor", "IsModifiable": true, "ApplyMethod": "pending-reboot", "Source": "user", "ApplyType": "dynamic", "AllowedValues": "disabled,enabled", "Description": "Enables TTL Monitoring", "ParameterValue": "enabled" } ] }`For more information, see [Viewing Amazon DocumentDB Cluster Parameters](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-parameters-describe.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [DescribeDbClusterParameters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-cluster-parameters.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-cluster-snapshot-attributes`.

- **AWS CLI**
- 
            
                    **To list an Amazon DocumentDB snapshot attribute names and values**The following `describe-db-cluster-snapshot-attributes`example lists the attribute names and values for the Amazon DocumentDB snapshot`sample-cluster-snapshot`.`aws docdb describe-db-cluster-snapshot-attributes \ --db-cluster-snapshot-identifier``sample-cluster-snapshot`Output: `{ "DBClusterSnapshotAttributesResult": { "DBClusterSnapshotAttributes": [ { "AttributeName": "restore", "AttributeValues": [] } ], "DBClusterSnapshotIdentifier": "sample-cluster-snapshot" } }`For more information, see [DescribeDBClusterSnapshotAttributes](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DescribeDBClusterSnapshotAttributes.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [DescribeDbClusterSnapshotAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-cluster-snapshot-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-cluster-snapshots`.

- **AWS CLI**
- 
            
                    **To describe Amazon DocumentDB snapshots**The following `describe-db-cluster-snapshots`example displays details for the Amazon DocumentDB snapshot`sample-cluster-snapshot`.`aws docdb describe-db-cluster-snapshots \ --db-cluster-snapshot-identifier``sample-cluster-snapshot`Output: `{ "DBClusterSnapshots": [ { "AvailabilityZones": [ "us-west-2a", "us-west-2b", "us-west-2c", "us-west-2d" ], "Status": "available", "DBClusterSnapshotArn": "arn:aws:rds:us-west-2:123456789012:cluster-snapshot:sample-cluster-snapshot", "SnapshotCreateTime": "2019-03-15T20:41:26.515Z", "SnapshotType": "manual", "DBClusterSnapshotIdentifier": "sample-cluster-snapshot", "DBClusterIdentifier": "sample-cluster", "MasterUsername": "master-user", "StorageEncrypted": false, "VpcId": "vpc-91280df6", "EngineVersion": "3.6.0", "PercentProgress": 100, "Port": 0, "Engine": "docdb", "ClusterCreateTime": "2019-03-15T20:29:58.836Z" } ] }`For more information, see [DescribeDBClusterSnapshots](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DescribeDBClusterSnapshots.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [DescribeDbClusterSnapshots](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-cluster-snapshots.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-clusters`.

- **AWS CLI**
- 
            
                    **To get detailed information about one or more Amazon DocumentDB clusters.**The following `describe-db-clusters`example displays details for the Amazon DocumentDB cluster`sample-cluster`. By omitting the`--db-cluster-identifier`parameter you can get information of up to 100 clusters.`aws docdb describe-db-clusters --db-cluster-identifier``sample-cluster`Output: `{ "DBClusters": [ { "DBClusterParameterGroup": "default.docdb3.6", "Endpoint": "sample-cluster.cluster-corcjozrlsfc.us-west-2.docdb.amazonaws.com", "PreferredBackupWindow": "00:00-00:30", "DBClusterIdentifier": "sample-cluster", "ClusterCreateTime": "2019-03-15T20:29:58.836Z", "LatestRestorableTime": "2019-03-18T20:28:03.239Z", "MasterUsername": "master-user", "DBClusterMembers": [ { "PromotionTier": 1, "DBClusterParameterGroupStatus": "in-sync", "IsClusterWriter": false, "DBInstanceIdentifier": "sample-cluster" }, { "PromotionTier": 1, "DBClusterParameterGroupStatus": "in-sync", "IsClusterWriter": true, "DBInstanceIdentifier": "sample-cluster2" } ], "PreferredMaintenanceWindow": "sat:04:30-sat:05:00", "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sg-77186e0d", "Status": "active" } ], "Engine": "docdb", "ReaderEndpoint": "sample-cluster.cluster-ro-corcjozrlsfc.us-west-2.docdb.amazonaws.com", "DBSubnetGroup": "default", "MultiAZ": true, "AvailabilityZones": [ "us-west-2a", "us-west-2c", "us-west-2b" ], "EarliestRestorableTime": "2019-03-15T20:30:47.020Z", "DbClusterResourceId": "cluster-UP4EF2PVDDFVHHDJQTYDAIGHLE", "DBClusterArn": "arn:aws:rds:us-west-2:123456789012:cluster:sample-cluster", "BackupRetentionPeriod": 3, "HostedZoneId": "ZNKXH85TT8WVW", "StorageEncrypted": false, "EnabledCloudwatchLogsExports": [ "audit" ], "AssociatedRoles": [], "EngineVersion": "3.6.0", "Port": 27017, "Status": "available" } ] }`For more information, see [Describing Amazon DocumentDB Clusters](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-view-details.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [DescribeDbClusters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-clusters.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-engine-versions`.

- **AWS CLI**
- 
            
                    **To list available Amazon DocumentDB engine versions**The following `describe-db-engine-versions`example lists all available Amazon DocumentDB engine versions.`aws``docdb`describe-db-engine-versions \ --engine docdbOutput: `{ "DBEngineVersions": [ { "DBEngineVersionDescription": "DocDB version 1.0.200837", "DBParameterGroupFamily": "docdb3.6", "EngineVersion": "3.6.0", "ValidUpgradeTarget": [], "DBEngineDescription": "Amazon DocumentDB (with MongoDB compatibility)", "SupportsLogExportsToCloudwatchLogs": true, "Engine": "docdb", "ExportableLogTypes": [ "audit" ] } ] }`For more information, see [DescribeDBEngineVersions](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DescribeDBEngineVersions.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [DescribeDbEngineVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-engine-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-instances`.

- **AWS CLI**
- 
            
                    **To find information about provisioned Amazon DocumentDB instances**The following `describe-db-instances`example displays details for about the Amazon DocumentDB instance`sample-cluster-instance`. By omitting the`--db-instance-identifier`parameter you get information on up to 100 instances.`aws docdb describe-db-instances \ --db-instance-identifier``sample-cluster-instance`Output: `{ "DBInstances": [ { "Endpoint": { "HostedZoneId": "ZNKXH85TT8WVW", "Address": "sample-cluster-instance.corcjozrlsfc.us-west-2.docdb.amazonaws.com", "Port": 27017 }, "PreferredBackupWindow": "00:00-00:30", "DBInstanceStatus": "available", "DBInstanceClass": "db.r4.large", "EnabledCloudwatchLogsExports": [ "audit" ], "DBInstanceIdentifier": "sample-cluster-instance", "DBSubnetGroup": { "Subnets": [ { "SubnetStatus": "Active", "SubnetIdentifier": "subnet-4e26d263", "SubnetAvailabilityZone": { "Name": "us-west-2a" } }, { "SubnetStatus": "Active", "SubnetIdentifier": "subnet-afc329f4", "SubnetAvailabilityZone": { "Name": "us-west-2c" } }, { "SubnetStatus": "Active", "SubnetIdentifier": "subnet-53ab3636", "SubnetAvailabilityZone": { "Name": "us-west-2d" } }, { "SubnetStatus": "Active", "SubnetIdentifier": "subnet-991cb8d0", "SubnetAvailabilityZone": { "Name": "us-west-2b" } } ], "DBSubnetGroupName": "default", "SubnetGroupStatus": "Complete", "DBSubnetGroupDescription": "default", "VpcId": "vpc-91280df6" }, "InstanceCreateTime": "2019-03-15T20:36:06.338Z", "Engine": "docdb", "StorageEncrypted": false, "AutoMinorVersionUpgrade": true, "DBInstanceArn": "arn:aws:rds:us-west-2:123456789012:db:sample-cluster-instance", "PreferredMaintenanceWindow": "tue:08:39-tue:09:09", "VpcSecurityGroups": [ { "Status": "active", "VpcSecurityGroupId": "sg-77186e0d" } ], "DBClusterIdentifier": "sample-cluster", "PendingModifiedValues": {}, "BackupRetentionPeriod": 3, "PubliclyAccessible": false, "EngineVersion": "3.6.0", "PromotionTier": 1, "AvailabilityZone": "us-west-2c", "DbiResourceId": "db-A2GIKUV6KPOHITGGKI2NHVISZA" } ] }`For more information, see [Describing Amazon DocumentDB Instances](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-view-details.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [DescribeDbInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-db-subnet-groups`.

- **AWS CLI**
- 
            
                    **To retrieve a list of Amazon DocumentDB subnet descriptions**The following `describe-db-subnet-groups`example describes details for the Amazon DocumentDB subnet named`default`.`aws docdb describe-db-subnet-groups \ --db-subnet-group-name``default`Output: `{ "DBSubnetGroups": [ { "VpcId": "vpc-91280df6", "DBSubnetGroupArn": "arn:aws:rds:us-west-2:123456789012:subgrp:default", "Subnets": [ { "SubnetIdentifier": "subnet-4e26d263", "SubnetStatus": "Active", "SubnetAvailabilityZone": { "Name": "us-west-2a" } }, { "SubnetIdentifier": "subnet-afc329f4", "SubnetStatus": "Active", "SubnetAvailabilityZone": { "Name": "us-west-2c" } }, { "SubnetIdentifier": "subnet-53ab3636", "SubnetStatus": "Active", "SubnetAvailabilityZone": { "Name": "us-west-2d" } }, { "SubnetIdentifier": "subnet-991cb8d0", "SubnetStatus": "Active", "SubnetAvailabilityZone": { "Name": "us-west-2b" } } ], "DBSubnetGroupName": "default", "SubnetGroupStatus": "Complete", "DBSubnetGroupDescription": "default" } ] }`For more information, see [Describing Subnet Groups](https://docs.aws.amazon.com/documentdb/latest/developerguide/document-db-subnet-groups.html#document-db-subnet-groups-describe)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [DescribeDbSubnetGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-subnet-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-engine-default-cluster-parameters`.

- **AWS CLI**
- 
            
                    **To describe the default engine and system parameter information for Amazon DocumentDB**The following `describe-engine-default-cluster-parameters`example displays details for the default engine and system parameter information for the Amazon DocumentDB parameter group`docdb3.6`.`aws docdb describe-engine-default-cluster-parameters \ --db-parameter-group-family``docdb3.6`Output: `{ "EngineDefaults": { "DBParameterGroupFamily": "docdb3.6", "Parameters": [ { "ApplyType": "dynamic", "ParameterValue": "disabled", "Description": "Enables auditing on cluster.", "Source": "system", "DataType": "string", "MinimumEngineVersion": "3.6.0", "AllowedValues": "enabled,disabled", "ParameterName": "audit_logs", "IsModifiable": true }, { "ApplyType": "static", "ParameterValue": "enabled", "Description": "Config to enable/disable TLS", "Source": "system", "DataType": "string", "MinimumEngineVersion": "3.6.0", "AllowedValues": "disabled,enabled", "ParameterName": "tls", "IsModifiable": true }, { "ApplyType": "dynamic", "ParameterValue": "enabled", "Description": "Enables TTL Monitoring", "Source": "system", "DataType": "string", "MinimumEngineVersion": "3.6.0", "AllowedValues": "disabled,enabled", "ParameterName": "ttl_monitor", "IsModifiable": true } ] } }`For more information, see [DescribeEngineDefaultClusterParameters](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_DescribeEngineDefaultClusterParameters.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [DescribeEngineDefaultClusterParameters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-engine-default-cluster-parameters.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-event-categories`.

- **AWS CLI**
- 
            
                    **To describe all Amazon DocumentDB event categories**The following `describe-event-categories`example lists all categories for the Amazon DocumentDB event source type`db-instance`.`aws docdb describe-event-categories \ --source-type``db-cluster`Output: `{ "EventCategoriesMapList": [ { "SourceType": "db-cluster", "EventCategories": [ "failover", "maintenance", "notification", "failure" ] } ] }`For more information, see [Viewing Event Categories](https://docs.aws.amazon.com/documentdb/latest/developerguide/managing-events.html#viewing-event-categories)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [DescribeEventCategories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-event-categories.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-events`.

- **AWS CLI**
- 
            
                    **To list Amazon DocumentDB events**The following `describe-events`example list all the Amazon DocumentDB events for the last 24 hours (1440 minutes).`aws docdb describe-events \ --duration``1440`This command produces no output. Output: `{ "Events": [ { "EventCategories": [ "failover" ], "Message": "Started cross AZ failover to DB instance: sample-cluster", "Date": "2019-03-18T21:36:29.807Z", "SourceArn": "arn:aws:rds:us-west-2:123456789012:cluster:sample-cluster", "SourceIdentifier": "sample-cluster", "SourceType": "db-cluster" }, { "EventCategories": [ "availability" ], "Message": "DB instance restarted", "Date": "2019-03-18T21:36:40.793Z", "SourceArn": "arn:aws:rds:us-west-2:123456789012:db:sample-cluster", "SourceIdentifier": "sample-cluster", "SourceType": "db-instance" }, { "EventCategories": [], "Message": "A new writer was promoted. Restarting database as a reader.", "Date": "2019-03-18T21:36:43.873Z", "SourceArn": "arn:aws:rds:us-west-2:123456789012:db:sample-cluster2", "SourceIdentifier": "sample-cluster2", "SourceType": "db-instance" }, { "EventCategories": [ "availability" ], "Message": "DB instance restarted", "Date": "2019-03-18T21:36:51.257Z", "SourceArn": "arn:aws:rds:us-west-2:123456789012:db:sample-cluster2", "SourceIdentifier": "sample-cluster2", "SourceType": "db-instance" }, { "EventCategories": [ "failover" ], "Message": "Completed failover to DB instance: sample-cluster", "Date": "2019-03-18T21:36:53.462Z", "SourceArn": "arn:aws:rds:us-west-2:123456789012:cluster:sample-cluster", "SourceIdentifier": "sample-cluster", "SourceType": "db-cluster" }, { "Date": "2019-03-19T16:51:48.847Z", "EventCategories": [ "configuration change" ], "Message": "Updated parameter audit_logs to enabled with apply method pending-reboot", "SourceIdentifier": "custom3-6-param-grp", "SourceType": "db-parameter-group" }, { "EventCategories": [ "configuration change" ], "Message": "Applying modification to database instance class", "Date": "2019-03-19T17:55:20.095Z", "SourceArn": "arn:aws:rds:us-west-2:123456789012:db:sample-cluster2", "SourceIdentifier": "sample-cluster2", "SourceType": "db-instance" }, { "EventCategories": [ "availability" ], "Message": "DB instance shutdown", "Date": "2019-03-19T17:56:31.127Z", "SourceArn": "arn:aws:rds:us-west-2:123456789012:db:sample-cluster2", "SourceIdentifier": "sample-cluster2", "SourceType": "db-instance" }, { "EventCategories": [ "configuration change" ], "Message": "Finished applying modification to DB instance class", "Date": "2019-03-19T18:00:45.822Z", "SourceArn": "arn:aws:rds:us-west-2:123456789012:db:sample-cluster2", "SourceIdentifier": "sample-cluster2", "SourceType": "db-instance" }, { "EventCategories": [ "availability" ], "Message": "DB instance restarted", "Date": "2019-03-19T18:00:53.397Z", "SourceArn": "arn:aws:rds:us-west-2:123456789012:db:sample-cluster2", "SourceIdentifier": "sample-cluster2", "SourceType": "db-instance" }, { "EventCategories": [ "availability" ], "Message": "DB instance shutdown", "Date": "2019-03-19T18:23:36.045Z", "SourceArn": "arn:aws:rds:us-west-2:123456789012:db:sample-cluster2", "SourceIdentifier": "sample-cluster2", "SourceType": "db-instance" }, { "EventCategories": [ "availability" ], "Message": "DB instance restarted", "Date": "2019-03-19T18:23:46.209Z", "SourceArn": "arn:aws:rds:us-west-2:123456789012:db:sample-cluster2", "SourceIdentifier": "sample-cluster2", "SourceType": "db-instance" }, { "Date": "2019-03-19T18:39:05.822Z", "EventCategories": [ "configuration change" ], "Message": "Updated parameter ttl_monitor to enabled with apply method immediate", "SourceIdentifier": "custom3-6-param-grp", "SourceType": "db-parameter-group" }, { "Date": "2019-03-19T18:39:48.067Z", "EventCategories": [ "configuration change" ], "Message": "Updated parameter audit_logs to disabled with apply method immediate", "SourceIdentifier": "custom3-6-param-grp", "SourceType": "db-parameter-group" } ] }`For more information, see [Viewing Amazon DocumentDB Events](https://docs.aws.amazon.com/documentdb/latest/developerguide/managing-events.html#viewing-events)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [DescribeEvents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-events.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-orderable-db-instance-options`.

- **AWS CLI**
- 
            
                    **To find the Amazon DocumentDB instance options you can order**The following `describe-orderable-db-instance-options`example lists all instance options for Amazon DocumentDB for a region.`aws``docdb`describe-orderable-db-instance-options \ --engine docdb \ --region`us-east-1`Output: `{ "OrderableDBInstanceOptions": [ { "Vpc": true, "AvailabilityZones": [ { "Name": "us-east-1a" }, { "Name": "us-east-1b" }, { "Name": "us-east-1c" }, { "Name": "us-east-1d" } ], "EngineVersion": "3.6.0", "DBInstanceClass": "db.r4.16xlarge", "LicenseModel": "na", "Engine": "docdb" }, { "Vpc": true, "AvailabilityZones": [ { "Name": "us-east-1a" }, { "Name": "us-east-1b" }, { "Name": "us-east-1c" }, { "Name": "us-east-1d" } } ], "EngineVersion": "3.6.0", "DBInstanceClass": "db.r4.2xlarge", "LicenseModel": "na", "Engine": "docdb" }, { "Vpc": true, "AvailabilityZones": [ { "Name": "us-east-1a" }, { "Name": "us-east-1b" }, { "Name": "us-east-1c" }, { "Name": "us-east-1d" } ], "EngineVersion": "3.6.0", "DBInstanceClass": "db.r4.4xlarge", "LicenseModel": "na", "Engine": "docdb" }, { "Vpc": true, "AvailabilityZones": [ { "Name": "us-east-1a" }, { "Name": "us-east-1b" }, { "Name": "us-east-1c" }, { "Name": "us-east-1d" } ], "EngineVersion": "3.6.0", "DBInstanceClass": "db.r4.8xlarge", "LicenseModel": "na", "Engine": "docdb" }, { "Vpc": true, "AvailabilityZones": [ { "Name": "us-east-1a" }, { "Name": "us-east-1b" }, { "Name": "us-east-1c" }, { "Name": "us-east-1d" } ], "EngineVersion": "3.6.0", "DBInstanceClass": "db.r4.large", "LicenseModel": "na", "Engine": "docdb" }, { "Vpc": true, "AvailabilityZones": [ { "Name": "us-east-1a" }, { "Name": "us-east-1b" }, { "Name": "us-east-1c" }, { "Name": "us-east-1d" } ], "EngineVersion": "3.6.0", "DBInstanceClass": "db.r4.xlarge", "LicenseModel": "na", "Engine": "docdb" } ] }`For more information, see [Adding an Amazon DocumentDB Instance to a Cluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-add.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [DescribeOrderableDbInstanceOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-orderable-db-instance-options.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-pending-maintenance-actions`.

- **AWS CLI**
- 
            
                    **To list your pending Amazon DocumentDB maintenance actions**The following `describe-pending-maintenance-actions`example lists all your pending Amazon DocumentDB maintenance actions.`aws docdb describe-pending-maintenance-actions`Output: `{ "PendingMaintenanceActions": [] }`For more information, see [Maintaining Amazon DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-maintain.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [DescribePendingMaintenanceActions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-pending-maintenance-actions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `failover-db-cluster`.

- **AWS CLI**
- 
            
                    **To force an Amazon DocumentDB cluster to failover to a replica**The following `failover-db-cluster`example causes the primary instance in the Amazon DocumentDB cluster sample-cluster to failover to a replica.`aws docdb failover-db-cluster \ --db-cluster-identifier``sample-cluster`Output: `{ "DBCluster": { "AssociatedRoles": [], "DBClusterIdentifier": "sample-cluster", "EngineVersion": "3.6.0", "DBSubnetGroup": "default", "MasterUsername": "master-user", "EarliestRestorableTime": "2019-03-15T20:30:47.020Z", "Endpoint": "sample-cluster.cluster-corcjozrlsfc.us-west-2.docdb.amazonaws.com", "AvailabilityZones": [ "us-west-2a", "us-west-2c", "us-west-2b" ], "LatestRestorableTime": "2019-03-18T21:35:23.548Z", "PreferredMaintenanceWindow": "sat:04:30-sat:05:00", "PreferredBackupWindow": "00:00-00:30", "Port": 27017, "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sg-77186e0d", "Status": "active" } ], "StorageEncrypted": false, "ClusterCreateTime": "2019-03-15T20:29:58.836Z", "MultiAZ": true, "Status": "available", "DBClusterMembers": [ { "DBClusterParameterGroupStatus": "in-sync", "IsClusterWriter": false, "DBInstanceIdentifier": "sample-cluster", "PromotionTier": 1 }, { "DBClusterParameterGroupStatus": "in-sync", "IsClusterWriter": true, "DBInstanceIdentifier": "sample-cluster2", "PromotionTier": 2 } ], "EnabledCloudwatchLogsExports": [ "audit" ], "DBClusterParameterGroup": "default.docdb3.6", "HostedZoneId": "ZNKXH85TT8WVW", "DBClusterArn": "arn:aws:rds:us-west-2:123456789012:cluster:sample-cluster", "BackupRetentionPeriod": 3, "DbClusterResourceId": "cluster-UP4EF2PVDDFVHHDJQTYDAIGHLE", "ReaderEndpoint": "sample-cluster.cluster-ro-corcjozrlsfc.us-west-2.docdb.amazonaws.com", "Engine": "docdb" } }`For more information, see [Amazon DocumentDB Failover](https://docs.aws.amazon.com/documentdb/latest/developerguide/failover.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [FailoverDbCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/failover-db-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list all the tags on an Amazon DocumentDB resource**The following `list-tags-for-resource`example lists all tags on the Amazon DocumentDB cluster`sample-cluster`.`aws docdb list-tags-for-resource \ --resource-name``arn:aws:rds:us-west-2:123456789012:cluster:sample-cluster`Output: `{ "TagList": [ { "Key": "A", "Value": "ALPHA" }, { "Key": "B", "Value": "" }, { "Key": "C", "Value": "CHARLIE" } ] }`For more information, see [Listing Tags on an Amazon DocumentDB Resource](https://docs.aws.amazon.com/documentdb/latest/developerguide/tagging.html#tagging-list)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-db-cluster-parameter-group`.

- **AWS CLI**
- 
            
                    **To modify an Amazon DocumentDB DB cluster parameter group**The following `modify-db-cluster-parameter-group`example modifies the Amazon DocumentDB cluster parameter group`custom3-6-param-grp`by setting the two parameters`audit_logs`and`ttl_monitor`to enabled. The changes are applied at the next reboot.`aws docdb modify-db-cluster-parameter-group \ --db-cluster-parameter-group-name``custom3-6-param-grp`\ --parameters`ParameterName=audit_logs,ParameterValue=enabled,ApplyMethod=pending-reboot`\`ParameterName=ttl_monitor,ParameterValue=enabled,ApplyMethod=pending-reboot`Output: `{ "DBClusterParameterGroupName": "custom3-6-param-grp" }`For more information, see [Modifying an Amazon DocumentDB Cluster Parameter Group](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-parameter-group-modify.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [ModifyDbClusterParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/modify-db-cluster-parameter-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-db-cluster-snapshot-attribute`.

- **AWS CLI**
- 
            
                    **Example 1: To add an attribute to an Amazon DocumentDB snapshot**The following `modify-db-cluster-snapshot-attribute`example adds four attribute values to an Amazon DocumentDB cluster snapshot.`aws docdb modify-db-cluster-snapshot-attribute \ --db-cluster-snapshot-identifier``sample-cluster-snapshot`\ --attribute-name`restore`\ --values-to-add`123456789011``123456789012``123456789013`Output: `{ "DBClusterSnapshotAttributesResult": { "DBClusterSnapshotAttributes": [ { "AttributeName": "restore", "AttributeValues": [ "123456789011", "123456789012", "123456789013" ] } ], "DBClusterSnapshotIdentifier": "sample-cluster-snapshot" } }`**Example 2: To remove attributes from an Amazon DocumentDB snapshot**The following `modify-db-cluster-snapshot-attribute`example removes two attribute values from an Amazon DocumentDB cluster snapshot.`aws docdb modify-db-cluster-snapshot-attribute \ --db-cluster-snapshot-identifier``sample-cluster-snapshot`\ --attribute-name`restore`\ --values-to-remove`123456789012`Output: `{ "DBClusterSnapshotAttributesResult": { "DBClusterSnapshotAttributes": [ { "AttributeName": "restore", "AttributeValues": [ "123456789011", "123456789013" ] } ], "DBClusterSnapshotIdentifier": "sample-cluster-snapshot" } }`For more information, see [ModifyDBClusterSnapshotAttribute](https://docs.aws.amazon.com/documentdb/latest/developerguide/API_ModifyDBClusterSnapshotAttribute.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [ModifyDbClusterSnapshotAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/modify-db-cluster-snapshot-attribute.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-db-cluster`.

- **AWS CLI**
- 
            
                    **To modify an Amazon DocumentDB cluster**The following `modify-db-cluster`example modifies the Amazon DocumentDB cluster`sample-cluster`by making the retention period for automatic backups 7 days, and changing the preferred windows for both backups and maintenance. All changes are applied at the next maintenance window.`aws docdb modify-db-cluster \ --db-cluster-identifier``sample-cluster`\ --no-apply-immediately \ --backup-retention-period`7`\ --preferred-backup-window`18:00-18:30`\ --preferred-maintenance-window`sun:20:00-sun:20:30`Output: `{ "DBCluster": { "Endpoint": "sample-cluster.cluster-corcjozrlsfc.us-west-2.docdb.amazonaws.com", "DBClusterMembers": [ { "DBClusterParameterGroupStatus": "in-sync", "DBInstanceIdentifier": "sample-cluster", "IsClusterWriter": true, "PromotionTier": 1 }, { "DBClusterParameterGroupStatus": "in-sync", "DBInstanceIdentifier": "sample-cluster2", "IsClusterWriter": false, "PromotionTier": 2 } ], "HostedZoneId": "ZNKXH85TT8WVW", "StorageEncrypted": false, "PreferredBackupWindow": "18:00-18:30", "MultiAZ": true, "EngineVersion": "3.6.0", "MasterUsername": "master-user", "ReaderEndpoint": "sample-cluster.cluster-ro-corcjozrlsfc.us-west-2.docdb.amazonaws.com", "DBSubnetGroup": "default", "LatestRestorableTime": "2019-03-18T22:08:13.408Z", "EarliestRestorableTime": "2019-03-15T20:30:47.020Z", "PreferredMaintenanceWindow": "sun:20:00-sun:20:30", "AssociatedRoles": [], "EnabledCloudwatchLogsExports": [ "audit" ], "Engine": "docdb", "DBClusterParameterGroup": "default.docdb3.6", "DBClusterArn": "arn:aws:rds:us-west-2:123456789012:cluster:sample-cluster", "BackupRetentionPeriod": 7, "DBClusterIdentifier": "sample-cluster", "AvailabilityZones": [ "us-west-2a", "us-west-2c", "us-west-2b" ], "Status": "available", "DbClusterResourceId": "cluster-UP4EF2PVDDFVHHDJQTYDAIGHLE", "ClusterCreateTime": "2019-03-15T20:29:58.836Z", "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sg-77186e0d", "Status": "active" } ], "Port": 27017 } }`For more information, see [Modifying an Amazon DocumentDB Cluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-modify.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [ModifyDbCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/modify-db-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-db-instance`.

- **AWS CLI**
- 
            
                    **To modify an Amazon DocumentDB instance**The following `modify-db-instance`example modifies the Amazon DocumentDB instance`sample-cluster2`by changing its instance class to`db.r4.4xlarge`and its promotion tier to`5`. The changes are applied immediately but can only be seen after the instances status is available.`aws docdb modify-db-instance \ --db-instance-identifier``sample-cluster2`\ --apply-immediately \ --db-instance-class`db.r4.4xlarge`\ --promotion-tier`5`Output: `{ "DBInstance": { "EngineVersion": "3.6.0", "StorageEncrypted": false, "DBInstanceClass": "db.r4.large", "PreferredMaintenanceWindow": "mon:08:39-mon:09:09", "AutoMinorVersionUpgrade": true, "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sg-77186e0d", "Status": "active" } ], "PreferredBackupWindow": "18:00-18:30", "EnabledCloudwatchLogsExports": [ "audit" ], "AvailabilityZone": "us-west-2f", "DBInstanceIdentifier": "sample-cluster2", "InstanceCreateTime": "2019-03-15T20:36:06.338Z", "Engine": "docdb", "BackupRetentionPeriod": 7, "DBSubnetGroup": { "DBSubnetGroupName": "default", "DBSubnetGroupDescription": "default", "SubnetGroupStatus": "Complete", "Subnets": [ { "SubnetIdentifier": "subnet-4e26d263", "SubnetAvailabilityZone": { "Name": "us-west-2a" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-afc329f4", "SubnetAvailabilityZone": { "Name": "us-west-2c" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-53ab3636", "SubnetAvailabilityZone": { "Name": "us-west-2d" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-991cb8d0", "SubnetAvailabilityZone": { "Name": "us-west-2b" }, "SubnetStatus": "Active" } ], "VpcId": "vpc-91280df6" }, "PromotionTier": 2, "Endpoint": { "Address": "sample-cluster2.corcjozrlsfc.us-west-2.docdb.amazonaws.com", "HostedZoneId": "ZNKXH85TT8WVW", "Port": 27017 }, "DbiResourceId": "db-A2GIKUV6KPOHITGGKI2NHVISZA", "DBClusterIdentifier": "sample-cluster", "DBInstanceArn": "arn:aws:rds:us-west-2:123456789012:db:sample-cluster2", "PendingModifiedValues": { "DBInstanceClass": "db.r4.4xlarge" }, "PubliclyAccessible": false, "DBInstanceStatus": "available" } }`For more information, see [Modifying an Amazon DocumentDB Instance](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-modify.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [ModifyDbInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/modify-db-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-db-subnet-group`.

- **AWS CLI**
- 
            
                    **To modify an Amazon DocumentDB subnet group**The following `modify-db-subnet-group`example modifies the subnet group`sample-subnet-group`by adding the specified subnets and a new description.`aws docdb modify-db-subnet-group \ --db-subnet-group-name``sample-subnet-group`\ --subnet-ids`subnet-b3806e8f``subnet-53ab3636``subnet-991cb8d0`\ --db-subnet-group-description`"New subnet description"`Output: `{ "DBSubnetGroup": { "DBSubnetGroupName": "sample-subnet-group", "SubnetGroupStatus": "Complete", "DBSubnetGroupArn": "arn:aws:rds:us-west-2:123456789012:subgrp:sample-subnet-group", "VpcId": "vpc-91280df6", "DBSubnetGroupDescription": "New subnet description", "Subnets": [ { "SubnetIdentifier": "subnet-b3806e8f", "SubnetStatus": "Active", "SubnetAvailabilityZone": { "Name": "us-west-2a" } }, { "SubnetIdentifier": "subnet-53ab3636", "SubnetStatus": "Active", "SubnetAvailabilityZone": { "Name": "us-west-2c" } }, { "SubnetIdentifier": "subnet-991cb8d0", "SubnetStatus": "Active", "SubnetAvailabilityZone": { "Name": "us-west-2b" } } ] } }`For more information, see [Modifying an Amazon DocumentDB Subnet Group](https://docs.aws.amazon.com/documentdb/latest/developerguide/document-db-subnet-groups.html#document-db-subnet-group-modify)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [ModifyDbSubnetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/modify-db-subnet-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reboot-db-instance`.

- **AWS CLI**
- 
            
                    **To reboot an Amazon DocumentDB instance**The following `reboot-db-instance`example reboots the Amazon DocumentDB instance`sample-cluster2`.`aws docdb reboot-db-instance \ --db-instance-identifier``sample-cluster2`This command produces no output. Output: `{ "DBInstance": { "PreferredBackupWindow": "18:00-18:30", "DBInstanceIdentifier": "sample-cluster2", "VpcSecurityGroups": [ { "Status": "active", "VpcSecurityGroupId": "sg-77186e0d" } ], "DBSubnetGroup": { "VpcId": "vpc-91280df6", "Subnets": [ { "SubnetStatus": "Active", "SubnetAvailabilityZone": { "Name": "us-west-2a" }, "SubnetIdentifier": "subnet-4e26d263" }, { "SubnetStatus": "Active", "SubnetAvailabilityZone": { "Name": "us-west-2c" }, "SubnetIdentifier": "subnet-afc329f4" }, { "SubnetStatus": "Active", "SubnetAvailabilityZone": { "Name": "us-west-2d" }, "SubnetIdentifier": "subnet-53ab3636" }, { "SubnetStatus": "Active", "SubnetAvailabilityZone": { "Name": "us-west-2b" }, "SubnetIdentifier": "subnet-991cb8d0" } ], "SubnetGroupStatus": "Complete", "DBSubnetGroupName": "default", "DBSubnetGroupDescription": "default" }, "PendingModifiedValues": {}, "Endpoint": { "Address": "sample-cluster2.corcjozrlsfc.us-west-2.docdb.amazonaws.com", "HostedZoneId": "ZNKXH85TT8WVW", "Port": 27017 }, "EnabledCloudwatchLogsExports": [ "audit" ], "StorageEncrypted": false, "DbiResourceId": "db-A2GIKUV6KPOHITGGKI2NHVISZA", "AutoMinorVersionUpgrade": true, "Engine": "docdb", "InstanceCreateTime": "2019-03-15T20:36:06.338Z", "EngineVersion": "3.6.0", "PromotionTier": 5, "BackupRetentionPeriod": 7, "DBClusterIdentifier": "sample-cluster", "PreferredMaintenanceWindow": "mon:08:39-mon:09:09", "PubliclyAccessible": false, "DBInstanceClass": "db.r4.4xlarge", "AvailabilityZone": "us-west-2d", "DBInstanceArn": "arn:aws:rds:us-west-2:123456789012:db:sample-cluster2", "DBInstanceStatus": "rebooting" } }`For more information, see [Rebooting an Amazon DocumentDB ILnstance](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-instance-reboot.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [RebootDbInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/reboot-db-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-tags-from-resource`.

- **AWS CLI**
- 
            
                    **To remove tags from an Amazon DocumentDB resource**The following `remove-tags-from-resource`example removes the tag with the key named`B`from the Amazon DocumentDB cluster`sample-cluster`.`aws docdb remove-tags-from-resource \ --resource-name``arn:aws:rds:us-west-2:123456789012:cluster:sample-cluster`\ --tag-keys`B`This command produces no output. For more information, see [Removing Tags from an Amazon DocumentDBResource](https://docs.aws.amazon.com/documentdb/latest/developerguide/tagging.html#tagging-remove)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [RemoveTagsFromResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/remove-tags-from-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reset-db-cluster-parameter-group`.

- **AWS CLI**
- 
            
                    **To reset the specified parameter value to its defaults in an Amazon DocumentDB parameter group**The following `reset-db-cluster-parameter-group`example resets the parameter`ttl_monitor`in the Amazon DocumentDB parameter group`custom3-6-param-grp`to its default value.`aws docdb reset-db-cluster-parameter-group \ --db-cluster-parameter-group-name``custom3-6-param-grp`\ --parameters`ParameterName=ttl_monitor,ApplyMethod=immediate`Output: `{ "DBClusterParameterGroupName": "custom3-6-param-grp" }`For more information, see title in the *Amazon DocumentDB Developer Guide*.**To reset specified or all parameter values to their defaults in an Amazon DocumentDB parameter group**The following `reset-db-cluster-parameter-group`example resets all parameters in the Amazon DocumentDB parameter group`custom3-6-param-grp`to their default value.`aws docdb reset-db-cluster-parameter-group \ --db-cluster-parameter-group-name``custom3-6-param-grp`\ --reset-all-parametersOutput: `{ "DBClusterParameterGroupName": "custom3-6-param-grp" }`For more information, see [Resetting an Amazon DocumentDB Cluster Parameter Group](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-parameter-group-reset.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [ResetDbClusterParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/reset-db-cluster-parameter-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `restore-db-cluster-from-snapshot`.

- **AWS CLI**
- 
            
                    **To restore an Amazon DocumentDB cluster from an automatic or manual snapshot**The following `restore-db-cluster-from-snapshot`example creates a new Amazon DocumentDB cluster named`sample-cluster-2019-03-16-00-01-restored`from the snapshot`rds:sample-cluster-2019-03-16-00-01`.`aws docdb restore-db-cluster-from-snapshot \ --db-cluster-identifier``sample-cluster-2019-03-16-00-01-restored`\ --engine`docdb`\ --snapshot-identifier`rds:sample-cluster-2019-03-16-00-01`Output: `{ "DBCluster": { "ClusterCreateTime": "2019-03-19T18:45:01.857Z", "HostedZoneId": "ZNKXH85TT8WVW", "Engine": "docdb", "DBClusterMembers": [], "MultiAZ": false, "AvailabilityZones": [ "us-west-2a", "us-west-2c", "us-west-2b" ], "StorageEncrypted": false, "ReaderEndpoint": "sample-cluster-2019-03-16-00-01-restored.cluster-ro-corcjozrlsfc.us-west-2.docdb.amazonaws.com", "Endpoint": "sample-cluster-2019-03-16-00-01-restored.cluster-corcjozrlsfc.us-west-2.docdb.amazonaws.com", "Port": 27017, "PreferredBackupWindow": "00:00-00:30", "DBSubnetGroup": "default", "DBClusterIdentifier": "sample-cluster-2019-03-16-00-01-restored", "PreferredMaintenanceWindow": "sat:04:30-sat:05:00", "DBClusterArn": "arn:aws:rds:us-west-2:123456789012:cluster:sample-cluster-2019-03-16-00-01-restored", "DBClusterParameterGroup": "default.docdb3.6", "DbClusterResourceId": "cluster-XOO46Q3RH4LWSYNH3NMZKXPISU", "MasterUsername": "master-user", "EngineVersion": "3.6.0", "BackupRetentionPeriod": 3, "AssociatedRoles": [], "Status": "creating", "VpcSecurityGroups": [ { "Status": "active", "VpcSecurityGroupId": "sg-77186e0d" } ] } }`For more information, see [Restoring from a Cluster Snapshot](https://docs.aws.amazon.com/documentdb/latest/developerguide/backup-restore.restore-from-snapshot.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [RestoreDbClusterFromSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/restore-db-cluster-from-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `restore-db-cluster-to-point-in-time`.

- **AWS CLI**
- 
            
                    **To restore an Amazon DocumentDB cluster to a point-in-time from a manual snapshot**The following `restore-db-cluster-to-point-in-time`example uses the`sample-cluster-snapshot`to create a new Amazon DocumentDB cluster,`sample-cluster-pit`, using the latest restorable time.`aws docdb restore-db-cluster-to-point-in-time \ --db-cluster-identifier``sample-cluster-pit`\ --source-db-cluster-identifier`arn:aws:rds:us-west-2:123456789012:cluster:sample-cluster`\ --use-latest-restorable-timeOutput: `{ "DBCluster": { "StorageEncrypted": false, "BackupRetentionPeriod": 3, "MasterUsername": "master-user", "HostedZoneId": "ZNKXH85TT8WVW", "PreferredBackupWindow": "00:00-00:30", "MultiAZ": false, "DBClusterIdentifier": "sample-cluster-pit", "DBSubnetGroup": "default", "ClusterCreateTime": "2019-04-03T15:55:21.320Z", "AssociatedRoles": [], "DBClusterParameterGroup": "default.docdb3.6", "DBClusterMembers": [], "Status": "creating", "AvailabilityZones": [ "us-west-2a", "us-west-2d", "us-west-2b" ], "ReaderEndpoint": "sample-cluster-pit.cluster-ro-corcjozrlsfc.us-west-2.docdb.amazonaws.com", "Port": 27017, "Engine": "docdb", "EngineVersion": "3.6.0", "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sg-77186e0d", "Status": "active" } ], "PreferredMaintenanceWindow": "sat:04:30-sat:05:00", "Endpoint": "sample-cluster-pit.cluster-corcjozrlsfc.us-west-2.docdb.amazonaws.com", "DbClusterResourceId": "cluster-NLCABBXOSE2QPQ4GOLZIFWEPLM", "DBClusterArn": "arn:aws:rds:us-west-2:123456789012:cluster:sample-cluster-pit" } }`For more information, see [Restoring a Snapshot to a Point in Time](https://docs.aws.amazon.com/documentdb/latest/developerguide/backup-restore.point-in-time-recovery.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [RestoreDbClusterToPointInTime](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/restore-db-cluster-to-point-in-time.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-db-cluster`.

- **AWS CLI**
- 
            
                    **To start a stopped Amazon DocumentDB cluster**The following `start-db-cluster`example starts the specified Amazon DocumentDB cluster.`aws docdb start-db-cluster \ --db-cluster-identifier``sample-cluster`Output: `{ "DBCluster": { "ClusterCreateTime": "2019-03-19T18:45:01.857Z", "HostedZoneId": "ZNKXH85TT8WVW", "Engine": "docdb", "DBClusterMembers": [], "MultiAZ": false, "AvailabilityZones": [ "us-east-1a", "us-east-1c", "us-east-1f" ], "StorageEncrypted": false, "ReaderEndpoint": "sample-cluster-2019-03-16-00-01-restored.cluster-ro-corcjozrlsfc.us-east-1.docdb.amazonaws.com", "Endpoint": "sample-cluster-2019-03-16-00-01-restored.cluster-corcjozrlsfc.us-east-1.docdb.amazonaws.com", "Port": 27017, "PreferredBackupWindow": "00:00-00:30", "DBSubnetGroup": "default", "DBClusterIdentifier": "sample-cluster-2019-03-16-00-01-restored", "PreferredMaintenanceWindow": "sat:04:30-sat:05:00", "DBClusterArn": "arn:aws:rds:us-east-1:123456789012:cluster:sample-cluster-2019-03-16-00-01-restored", "DBClusterParameterGroup": "default.docdb3.6", "DbClusterResourceId": "cluster-XOO46Q3RH4LWSYNH3NMZKXPISU", "MasterUsername": "master-user", "EngineVersion": "3.6.0", "BackupRetentionPeriod": 3, "AssociatedRoles": [], "Status": "creating", "VpcSecurityGroups": [ { "Status": "active", "VpcSecurityGroupId": "sg-77186e0d" } ] } }`For more information, see [Stopping and Starting an Amazon DocumentDB Cluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-stop-start.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [StartDbCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/start-db-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-db-cluster`.

- **AWS CLI**
- 
            
                    **To stop a running Amazon DocumentDB cluster**The following `stop-db-cluster`example stops the specified Amazon DocumentDB cluster.`aws docdb stop-db-cluster \ --db-cluster-identifier``sample-cluster`Output: `{ "DBCluster": { "ClusterCreateTime": "2019-03-19T18:45:01.857Z", "HostedZoneId": "ZNKXH85TT8WVW", "Engine": "docdb", "DBClusterMembers": [], "MultiAZ": false, "AvailabilityZones": [ "us-east-1a", "us-east-1c", "us-east-1f" ], "StorageEncrypted": false, "ReaderEndpoint": "sample-cluster-2019-03-16-00-01-restored.cluster-ro-corcjozrlsfc.us-east-1.docdb.amazonaws.com", "Endpoint": "sample-cluster-2019-03-16-00-01-restored.cluster-corcjozrlsfc.us-east-1.docdb.amazonaws.com", "Port": 27017, "PreferredBackupWindow": "00:00-00:30", "DBSubnetGroup": "default", "DBClusterIdentifier": "sample-cluster-2019-03-16-00-01-restored", "PreferredMaintenanceWindow": "sat:04:30-sat:05:00", "DBClusterArn": "arn:aws:rds:us-east-1:123456789012:cluster:sample-cluster-2019-03-16-00-01-restored", "DBClusterParameterGroup": "default.docdb3.6", "DbClusterResourceId": "cluster-XOO46Q3RH4LWSYNH3NMZKXPISU", "MasterUsername": "master-user", "EngineVersion": "3.6.0", "BackupRetentionPeriod": 3, "AssociatedRoles": [], "Status": "creating", "VpcSecurityGroups": [ { "Status": "active", "VpcSecurityGroupId": "sg-77186e0d" } ] } }`For more information, see [Stopping and Starting an Amazon DocumentDB Cluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-stop-start.html)in the*Amazon DocumentDB Developer Guide*.- 
                    For API details, see [StopDbCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/stop-db-cluster.html)in*AWS CLI Command Reference*.
 
-