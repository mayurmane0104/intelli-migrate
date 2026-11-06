# Amazon Redshift examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_redshift_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_redshift_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon Redshift.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `accept-reserved-node-exchange`.

- **AWS CLI**
- 
            
                    **To accept reserved node exchange**The following `accept-reserved-node-exchange`example accepts exchange of a DC1 reserved node for a DC2 reserved node.`aws redshift accept-reserved-node-exchange``/`--reserved-node-id`12345678-12ab-12a1-1a2a-12ab-12a12EXAMPLE``/`--target-reserved-node-offering-id`12345678-12ab-12a1-1a2a-12ab-12a12EXAMPLE`Output: `{ "ExchangedReservedNode": { "ReservedNodeId": "12345678-12ab-12a1-1a2a-12ab-12a12EXAMPLE", "ReservedNodeOfferingId": "12345678-12ab-12a1-1a2a-12ab-12a12EXAMPLE", "NodeType": "dc2.large", "StartTime": "2019-12-06T21:17:26Z", "Duration": 31536000, "FixedPrice": 0.0, "UsagePrice": 0.0, "CurrencyCode": "USD", "NodeCount": 1, "State": "exchanging", "OfferingType": "All Upfront", "RecurringCharges": [ { "RecurringChargeAmount": 0.0, "RecurringChargeFrequency": "Hourly" } ], "ReservedNodeOfferingType": "Regular" } }`For more information, see [Upgrading Reserved Nodes With the AWS CLI](https://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-offering-console.html)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [AcceptReservedNodeExchange](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/accept-reserved-node-exchange.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `authorize-cluster-security-group-ingress`.

- **AWS CLI**
- 
            
                    Authorizing Access to an EC2 Security GroupThis example authorizes access to a named Amazon EC2 security group.Command: `aws redshift authorize-cluster-security-group-ingress --cluster-security-group-name mysecuritygroup --ec2-security-group-name myec2securitygroup --ec2-security-group-owner-id 123445677890`Authorizing Access to a CIDR rangeThis example authorizes access to a CIDR range.Command: `aws redshift authorize-cluster-security-group-ingress --cluster-security-group-name mysecuritygroup --cidrip 192.168.100.100/32`- 
                    For API details, see [AuthorizeClusterSecurityGroupIngress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/authorize-cluster-security-group-ingress.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `authorize-snapshot-access`.

- **AWS CLI**
- 
            
                    Authorize an AWS Account to Restore a SnapshotThis example authorizes the AWS account `444455556666`to restore the snapshot`my-snapshot-id`. By default, the output is in JSON format.Command:`aws redshift authorize-snapshot-access --snapshot-id my-snapshot-id --account-with-restore-access 444455556666`Result: `{ "Snapshot": { "Status": "available", "SnapshotCreateTime": "2013-07-17T22:04:18.947Z", "EstimatedSecondsToCompletion": 0, "AvailabilityZone": "us-east-1a", "ClusterVersion": "1.0", "MasterUsername": "adminuser", "Encrypted": false, "OwnerAccount": "111122223333", "BackupProgressInMegabytes": 11.0, "ElapsedTimeInSeconds": 0, "DBName": "dev", "CurrentBackupRateInMegabytesPerSecond: 0.1534, "ClusterCreateTime": "2013-01-22T21:59:29.559Z", "ActualIncrementalBackupSizeInMegabytes"; 11.0, "SnapshotType": "manual", "NodeType": "dw.hs1.xlarge", "ClusterIdentifier": "mycluster", "TotalBackupSizeInMegabytes": 20.0, "Port": 5439, "NumberOfNodes": 2, "SnapshotIdentifier": "my-snapshot-id" } }`- 
                    For API details, see [AuthorizeSnapshotAccess](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/authorize-snapshot-access.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-delete-cluster-snapshots`.

- **AWS CLI**
- 
            
                    **To delete a set of cluster snapshots**The following `batch-delete-cluster-snapshots`example deletes a set of manual cluster snapshots.`aws redshift batch-delete-cluster-snapshots \ --identifiers``SnapshotIdentifier=mycluster-2019-11-06-14-12``SnapshotIdentifier=mycluster-2019-11-06-14-20`Output: `{ "Resources": [ "mycluster-2019-11-06-14-12", "mycluster-2019-11-06-14-20" ] }`For more information, see [Amazon Redshift Snapshots](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [BatchDeleteClusterSnapshots](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/batch-delete-cluster-snapshots.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-modify-cluster-snapshots`.

- **AWS CLI**
- 
            
                    **To modify a set of cluster snapshots**The following `batch-modify-cluster-snapshots`example modifies the settings for a set of cluster snapshots.`aws redshift batch-modify-cluster-snapshots \ --snapshot-identifier-list``mycluster-2019-11-06-16-31``mycluster-2019-11-06-16-32`\ --manual-snapshot-retention-period`30`Output: `{ "Resources": [ "mycluster-2019-11-06-16-31", "mycluster-2019-11-06-16-32" ], "Errors": [], "ResponseMetadata": { "RequestId": "12345678-12ab-12a1-1a2a-12ab-12a12EXAMPLE", "HTTPStatusCode": 200, "HTTPHeaders": { "x-amzn-requestid": "12345678-12ab-12a1-1a2a-12ab-12a12EXAMPLE, "content-type": "text/xml", "content-length": "480", "date": "Sat, 07 Dec 2019 00:36:09 GMT", "connection": "keep-alive" }, "RetryAttempts": 0 } }`For more information, see [Amazon Redshift Snapshots](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [BatchModifyClusterSnapshots](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/batch-modify-cluster-snapshots.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-resize`.

- **AWS CLI**
- 
            
                    **To cancel resize of a cluster**The following `cancel-resize`example cancels a classic resize operation for a cluster.`aws redshift cancel-resize \ --cluster-identifier``mycluster`Output: `{ "TargetNodeType": "dc2.large", "TargetNumberOfNodes": 2, "TargetClusterType": "multi-node", "Status": "CANCELLING", "ResizeType": "ClassicResize", "TargetEncryptionType": "NONE" }`For more information, see [Resizing Clusters in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/rs-resize-tutorial.html)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [CancelResize](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/cancel-resize.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `copy-cluster-snapshot`.

- **AWS CLI**
- 
            
                    Get a Description of All Cluster VersionsThis example returns a description of all cluster versions. By default, the output is in JSON format.Command: `aws redshift copy-cluster-snapshot --source-snapshot-identifier cm:examplecluster-2013-01-22-19-27-58 --target-snapshot-identifier my-saved-snapshot-copy`Result: `{ "Snapshot": { "Status": "available", "SnapshotCreateTime": "2013-01-22T19:27:58.931Z", "AvailabilityZone": "us-east-1c", "ClusterVersion": "1.0", "MasterUsername": "adminuser", "DBName": "dev", "ClusterCreateTime": "2013-01-22T19:23:59.368Z", "SnapshotType": "manual", "NodeType": "dw.hs1.xlarge", "ClusterIdentifier": "examplecluster", "Port": 5439, "NumberOfNodes": "2", "SnapshotIdentifier": "my-saved-snapshot-copy" }, "ResponseMetadata": { "RequestId": "3b279691-64e3-11e2-bec0-17624ad140dd" } }`- 
                    For API details, see [CopyClusterSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/copy-cluster-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-cluster-parameter-group`.

- **AWS CLI**
- 
            
                    Create a Cluster Parameter GroupThis example creates a new cluster parameter group.Command: `aws redshift create-cluster-parameter-group --parameter-group-name myclusterparametergroup --parameter-group-family redshift-1.0 --description "My first cluster parameter group"`Result: `{ "ClusterParameterGroup": { "ParameterGroupFamily": "redshift-1.0", "Description": "My first cluster parameter group", "ParameterGroupName": "myclusterparametergroup" }, "ResponseMetadata": { "RequestId": "739448f0-64cc-11e2-8f7d-3b939af52818" } }`- 
                    For API details, see [CreateClusterParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster-parameter-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-cluster-security-group`.

- **AWS CLI**
- 
            
                    Creating a Cluster Security GroupThis example creates a new cluster security group. By default, the output is in JSON format.Command: `aws redshift create-cluster-security-group --cluster-security-group-name mysecuritygroup --description "This is my cluster security group"`Result: `{ "create_cluster_security_group_response": { "create_cluster_security_group_result": { "cluster_security_group": { "description": "This is my cluster security group", "owner_id": "300454760768", "cluster_security_group_name": "mysecuritygroup", "ec2_security_groups": \[], "ip_ranges": \[] } }, "response_metadata": { "request_id": "5df486a0-343a-11e2-b0d8-d15d0ef48549" } } }`You can also obtain the same information in text format using the `--output text`option.Command:`--output text`option.Command:option.Command: `aws redshift create-cluster-security-group --cluster-security-group-name mysecuritygroup --description "This is my cluster security group" --output text`Result: `This is my cluster security group 300454760768 mysecuritygroup a0c0bfab-343a-11e2-95d2-c3dc9fe8ab57`- 
                    For API details, see [CreateClusterSecurityGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster-security-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-cluster-snapshot`.

- **AWS CLI**
- 
            
                    Create a Cluster SnapshotThis example creates a new cluster snapshot. By default, the output is in JSON format.Command: `aws redshift create-cluster-snapshot --cluster-identifier mycluster --snapshot-identifier my-snapshot-id`Result: `{ "Snapshot": { "Status": "creating", "SnapshotCreateTime": "2013-01-22T22:20:33.548Z", "AvailabilityZone": "us-east-1a", "ClusterVersion": "1.0", "MasterUsername": "adminuser", "DBName": "dev", "ClusterCreateTime": "2013-01-22T21:59:29.559Z", "SnapshotType": "manual", "NodeType": "dw.hs1.xlarge", "ClusterIdentifier": "mycluster", "Port": 5439, "NumberOfNodes": "2", "SnapshotIdentifier": "my-snapshot-id" }, "ResponseMetadata": { "RequestId": "f024d1a5-64e1-11e2-88c5-53eb05787dfb" } }`- 
                    For API details, see [CreateClusterSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-cluster-subnet-group`.

- **AWS CLI**
- 
            
                    Create a Cluster Subnet GroupThis example creates a new cluster subnet group.Command: `aws redshift create-cluster-subnet-group --cluster-subnet-group-name mysubnetgroup --description "My subnet group" --subnet-ids subnet-763fdd1c`Result: `{ "ClusterSubnetGroup": { "Subnets": [ { "SubnetStatus": "Active", "SubnetIdentifier": "subnet-763fdd1c", "SubnetAvailabilityZone": { "Name": "us-east-1a" } } ], "VpcId": "vpc-7e3fdd14", "SubnetGroupStatus": "Complete", "Description": "My subnet group", "ClusterSubnetGroupName": "mysubnetgroup" }, "ResponseMetadata": { "RequestId": "500b8ce2-698f-11e2-9790-fd67517fb6fd" } }`- 
                    For API details, see [CreateClusterSubnetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster-subnet-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-cluster`.

- **AWS CLI**
- 
            
                    Create a Cluster with Minimal ParametersThis example creates a cluster with the minimal set of parameters. By default, the output is in JSON format.Command: `aws redshift create-cluster --node-type dw.hs1.xlarge --number-of-nodes 2 --master-username adminuser --master-user-password TopSecret1 --cluster-identifier mycluster`Result: `{ "Cluster": { "NodeType": "dw.hs1.xlarge", "ClusterVersion": "1.0", "PubliclyAccessible": "true", "MasterUsername": "adminuser", "ClusterParameterGroups": [ { "ParameterApplyStatus": "in-sync", "ParameterGroupName": "default.redshift-1.0" } ], "ClusterSecurityGroups": [ { "Status": "active", "ClusterSecurityGroupName": "default" } ], "AllowVersionUpgrade": true, "VpcSecurityGroups": \[], "PreferredMaintenanceWindow": "sat:03:30-sat:04:00", "AutomatedSnapshotRetentionPeriod": 1, "ClusterStatus": "creating", "ClusterIdentifier": "mycluster", "DBName": "dev", "NumberOfNodes": 2, "PendingModifiedValues": { "MasterUserPassword": "\****" } }, "ResponseMetadata": { "RequestId": "7cf4bcfc-64dd-11e2-bea9-49e0ce183f07" } }`- 
                    For API details, see [CreateCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-event-subscription`.

- **AWS CLI**
- 
            
                    **To create a notification subscription for an event**The following `create-event-subscription`example creates an event notification subscription.`aws redshift create-event-subscription \ --subscription-name``mysubscription`\ --sns-topic-arn`arn:aws:sns:us-west-2:123456789012:MySNStopic`\ --source-type`cluster`\ --source-ids`mycluster`Output: `{ "EventSubscription": { "CustomerAwsId": "123456789012", "CustSubscriptionId": "mysubscription", "SnsTopicArn": "arn:aws:sns:us-west-2:123456789012:MySNStopic", "Status": "active", "SubscriptionCreationTime": "2019-12-09T20:05:19.365Z", "SourceType": "cluster", "SourceIdsList": [ "mycluster" ], "EventCategoriesList": [], "Severity": "INFO", "Enabled": true, "Tags": [] } }`For more information, see [Subscribing to Amazon Redshift Event Notifications](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-event-notifications.html)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [CreateEventSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-event-subscription.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-hsm-client-certificate`.

- **AWS CLI**
- 
            
                    **To create an HSM client certificate**The following `create-hsm-client-certificate`example generates an HSM client certificate that a cluster can use to connect to an HSM.`aws redshift create-hsm-client-certificate \ --hsm-client-certificate-identifier``myhsmclientcert`Output: `{ "HsmClientCertificate": { "HsmClientCertificateIdentifier": "myhsmclientcert", "HsmClientCertificatePublicKey": "-----BEGIN CERTIFICATE----- MIICiEXAMPLECQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC VVMxCzAJBgNVBAgTEXAMPLEwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6 b24xFDASBgNVBAsTC0lBTSBDb25EXAMPLEIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb2EXAMPLETEwNDI1MjA0NTIxWhcN MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBEXAMPLEMRAwDgYD EXAMPLETZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z b2xlMRIwEAEXAMPLEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt YXpvbi5jb20wgZ8wDQYJKEXAMPLEAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ 21uUSfwfEvySWtC2XADZ4nB+BLYgVIk6EXAMPLE3G93vUEIO3IyNoH/f0wYK8m9T rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugEXAMPLEzZswY6786m86gpE Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEEXAMPLEEAtCu4 nUhVVxYUEXAMPLEh8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb FFBjvSfpJIlJ00zbhNYS5f6GEXAMPLEl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb NYiytVbZPQUQ5Yaxu2jXnimvw3rEXAMPLE=-----END CERTIFICATE-----\n", "Tags": [] } }`For more information, see [Amazon Redshift API Permissions Reference](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [CreateHsmClientCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-hsm-client-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-hsm-configuration`.

- **AWS CLI**
- 
            
                    **To create an HSM configuration**The following `create-hsm-configuration`example creates the specified HSM configuration that contains information required by a cluster to store and use database encryption keys in a hardware security module (HSM).`aws redshift create-hsm-configuration``/`--hsm-configuration-identifier`myhsmconnection`--description`"My HSM connection"`--hsm-ip-address`192.0.2.09`--hsm-partition-name`myhsmpartition``/`--hsm-partition-password`A1b2c3d4``/`--hsm-server-public-certificate`myhsmclientcert`Output: `{ "HsmConfiguration": { "HsmConfigurationIdentifier": "myhsmconnection", "Description": "My HSM connection", "HsmIpAddress": "192.0.2.09", "HsmPartitionName": "myhsmpartition", "Tags": [] } }`- 
                    For API details, see [CreateHsmConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-hsm-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-snapshot-copy-grant`.

- **AWS CLI**
- 
            
                    **To create a snapshot copy grant**The following `create-snapshot-copy-grant`example creates a snapshot copy grant and encrypts copied snapshots in a destination AWS Region.`aws redshift create-snapshot-copy-grant \ --snapshot-copy-grant-name``mysnapshotcopygrantname`Output: `{ "SnapshotCopyGrant": { "SnapshotCopyGrantName": "mysnapshotcopygrantname", "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/bPxRfih3yCo8nvbEXAMPLEKEY", "Tags": [] } }`For more information, see [Amazon Redshift Database Encryption](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [CreateSnapshotCopyGrant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-snapshot-copy-grant.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-snapshot-schedule`.

- **AWS CLI**
- 
            
                    **To create snapshot schedule**The following `create-snapshot-schedule`example creates a snapshot schedule with the specified description and a rate of every 12 hours.`aws redshift create-snapshot-schedule \ --schedule-definitions``"rate(12 hours)"`\ --schedule-identifier`mysnapshotschedule`\ --schedule-description`"My schedule description"`Output: `{ "ScheduleDefinitions": [ "rate(12 hours)" ], "ScheduleIdentifier": "mysnapshotschedule", "ScheduleDescription": "My schedule description", "Tags": [] }`For more information, see [Automated Snapshot Schedules](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html#automated-snapshot-schedules)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [CreateSnapshotSchedule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-snapshot-schedule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-tags`.

- **AWS CLI**
- 
            
                    **To create tags for a cluster**The following `create-tags`example adds the specified tag key/value pair to the specified cluster.`aws redshift create-tags \ --resource-name``arn:aws:redshift:us-west-2:123456789012:cluster:mycluster`\ --tags "Key"="mytags","Value"="tag1"This command does not produce any output. For more information, see [Tagging Resources in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-tagging.html)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [CreateTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-cluster-parameter-group`.

- **AWS CLI**
- 
            
                    Delete a Cluster Parameter GroupThis example deletes a cluster parameter group.Command: `aws redshift delete-cluster-parameter-group --parameter-group-name myclusterparametergroup`- 
                    For API details, see [DeleteClusterParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster-parameter-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-cluster-security-group`.

- **AWS CLI**
- 
            
                    Delete a Cluster Security GroupThis example deletes a cluster security group.Command: `aws redshift delete-cluster-security-group --cluster-security-group-name mysecuritygroup`- 
                    For API details, see [DeleteClusterSecurityGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster-security-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-cluster-snapshot`.

- **AWS CLI**
- 
            
                    Delete a Cluster SnapshotThis example deletes a cluster snapshot.Command: `aws redshift delete-cluster-snapshot --snapshot-identifier my-snapshot-id`- 
                    For API details, see [DeleteClusterSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-cluster-subnet-group`.

- **AWS CLI**
- 
            
                    Delete a Cluster subnet GroupThis example deletes a cluster subnet group.Command: `aws redshift delete-cluster-subnet-group --cluster-subnet-group-name mysubnetgroup`Result: `{ "ResponseMetadata": { "RequestId": "253fbffd-6993-11e2-bc3a-47431073908a" } }`- 
                    For API details, see [DeleteClusterSubnetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster-subnet-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-cluster`.

- **AWS CLI**
- 
            
                    Delete a Cluster with No Final Cluster SnapshotThis example deletes a cluster, forcing data deletion so no final cluster snapshot is created.Command: `aws redshift delete-cluster --cluster-identifier mycluster --skip-final-cluster-snapshot`Delete a Cluster, Allowing a Final Cluster SnapshotThis example deletes a cluster, but specifies a final cluster snapshot.Command: `aws redshift delete-cluster --cluster-identifier mycluster --final-cluster-snapshot-identifier myfinalsnapshot`- 
                    For API details, see [DeleteCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-event-subscription`.

- **AWS CLI**
- 
            
                    **To delete event subscription**The following `delete-event-subscription`example deletes the specified event notification subscription.`aws redshift delete-event-subscription \ --subscription-name``mysubscription`This command does not produce any output. For more information, see [Subscribing to Amazon Redshift Event Notifications](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-event-notifications.html)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [DeleteEventSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-event-subscription.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-hsm-client-certificate`.

- **AWS CLI**
- 
            
                    **To delete HSM client certificate**The following `delete-hsm-client-certificate`example deletes an HSM client certificate.`aws redshift delete-hsm-client-certificate \ --hsm-client-certificate-identifier``myhsmclientcert`This command does not produce any output. For more information, see [Amazon Redshift API Permissions Reference](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [DeleteHsmClientCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-hsm-client-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-hsm-configuration`.

- **AWS CLI**
- 
            
                    **To delete an HSM configuration**The following `delete-hsm-configuration`example deletes the specified HSM configuration from the current AWS account.`aws redshift delete-hsm-configuration``/`--hsm-configuration-identifier`myhsmconnection`This command does not produce any output. - 
                    For API details, see [DeleteHsmConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-hsm-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-scheduled-action`.

- **AWS CLI**
- 
            
                    **To delete scheduled action**The following `delete-scheduled-action`example deletes the specified scheduled action.`aws redshift delete-scheduled-action \ --scheduled-action-name``myscheduledaction`This command does not produce any output. - 
                    For API details, see [DeleteScheduledAction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-scheduled-action.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-snapshot-copy-grant`.

- **AWS CLI**
- 
            
                    **To delete snapshot copy grant**The following `delete-snapshot-copy-grant`example deletes the specified snapshot copy grant.`aws redshift delete-snapshot-copy-grant \ --snapshot-copy-grant-name``mysnapshotcopygrantname`This command does not produce any output. For more information, see [Amazon Redshift Database Encryption](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [DeleteSnapshotCopyGrant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-snapshot-copy-grant.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-snapshot-schedule`.

- **AWS CLI**
- 
            
                    **To delete snapshot schedule**The following `delete-snapshot-schedule`example deletes the specified snapshot schedule. You must disassociate clusters before deleting the schedule.`aws redshift delete-snapshot-schedule \ --schedule-identifier``mysnapshotschedule`This command does not produce any output. For more information, see [Automated Snapshot Schedules](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html#automated-snapshot-schedules)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [DeleteSnapshotSchedule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-snapshot-schedule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-tags`.

- **AWS CLI**
- 
            
                    **To delete tags from a cluster**The following `delete-tags`example deletes the tags with the specified key names from the specified cluster.`aws redshift delete-tags \ --resource-name``arn:aws:redshift:us-west-2:123456789012:cluster:mycluster`\ --tag-keys`"clustertagkey"``"clustertagvalue"`This command does not produce any output. For more information, see [Tagging Resources in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-tagging.html)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [DeleteTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-account-attributes`.

- **AWS CLI**
- 
            
                    **To describe attributes of an AWS account**The following `describe-account-attributes`example displays the attributes attached to the calling AWS account.`aws redshift describe-account-attributes`Output: `{ "AccountAttributes": [ { "AttributeName": "max-defer-maintenance-duration", "AttributeValues": [ { "AttributeValue": "45" } ] } ] }`- 
                    For API details, see [DescribeAccountAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-account-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-cluster-db-revisions`.

- **AWS CLI**
- 
            
                    **To describe DB revisions for a cluster**The following `describe-cluster-db-revisions`example displays the details of an array of`ClusterDbRevision`objects for the specified cluster.`aws redshift describe-cluster-db-revisions \ --cluster-identifier``mycluster`Output: `{ "ClusterDbRevisions": [ { "ClusterIdentifier": "mycluster", "CurrentDatabaseRevision": "11420", "DatabaseRevisionReleaseDate": "2019-11-22T16:43:49.597Z", "RevisionTargets": [] } ] }`- 
                    For API details, see [DescribeClusterDbRevisions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-db-revisions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-cluster-parameter-groups`.

- **AWS CLI**
- 
            
                    Get a Description of All Cluster Parameter GroupsThis example returns a description of all cluster parameter groups for the account, with column headers. By default, the output is in JSON format.Command: `aws redshift describe-cluster-parameter-groups`Result: `{ "ParameterGroups": [ { "ParameterGroupFamily": "redshift-1.0", "Description": "My first cluster parameter group", "ParameterGroupName": "myclusterparametergroup" } ], "ResponseMetadata": { "RequestId": "8ceb8f6f-64cc-11e2-bea9-49e0ce183f07" } }`You can also obtain the same information in text format using the `--output text`option.Command:`--output text`option.Command:option.Command: `aws redshift describe-cluster-parameter-groups --output text`Result: `redshift-1.0 My first cluster parameter group myclusterparametergroup RESPONSEMETADATA 9e665a36-64cc-11e2-8f7d-3b939af52818`- 
                    For API details, see [DescribeClusterParameterGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-parameter-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-cluster-parameters`.

- **AWS CLI**
- 
            
                    Retrieve the Parameters for a Specified Cluster Parameter GroupThis example retrieves the parameters for the named parameter group. By default, the output is in JSON format.Command: `aws redshift describe-cluster-parameters --parameter-group-name myclusterparametergroup`Result: `{ "Parameters": [ { "Description": "Sets the display format for date and time values.", "DataType": "string", "IsModifiable": true, "Source": "engine-default", "ParameterValue": "ISO, MDY", "ParameterName": "datestyle" }, { "Description": "Sets the number of digits displayed for floating-point values", "DataType": "integer", "IsModifiable": true, "AllowedValues": "-15-2", "Source": "engine-default", "ParameterValue": "0", "ParameterName": "extra_float_digits" }, (...remaining output omitted...) ] }`You can also obtain the same information in text format using the `--output text`option.Command:`--output text`option.Command:option.Command: `aws redshift describe-cluster-parameters --parameter-group-name myclusterparametergroup --output text`Result: `RESPONSEMETADATA cdac40aa-64cc-11e2-9e70-918437dd236d Sets the display format for date and time values. string True engine-default ISO, MDY datestyle Sets the number of digits displayed for floating-point values integer True -15-2 engine-default 0 extra_float_digits This parameter applies a user-defined label to a group of queries that are run during the same session.. string True engine-default default query_group require ssl for all databaseconnections boolean True true,false engine-default false require_ssl Sets the schema search order for names that are not schema-qualified. string True engine-default $user, public search_path Aborts any statement that takes over the specified number of milliseconds. integer True engine-default 0 statement_timeout wlm json configuration string True engine-default \[{"query_concurrency":5}] wlm_json_configuration`- 
                    For API details, see [DescribeClusterParameters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-parameters.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-cluster-security-groups`.

- **AWS CLI**
- 
            
                    Get a Description of All Cluster Security GroupsThis example returns a description of all cluster security groups for the account. By default, the output is in JSON format.Command: `aws redshift describe-cluster-security-groups`Result: `{ "ClusterSecurityGroups": [ { "OwnerId": "100447751468", "Description": "default", "ClusterSecurityGroupName": "default", "EC2SecurityGroups": \[], "IPRanges": [ { "Status": "authorized", "CIDRIP": "0.0.0.0/0" } ] }, { "OwnerId": "100447751468", "Description": "This is my cluster security group", "ClusterSecurityGroupName": "mysecuritygroup", "EC2SecurityGroups": \[], "IPRanges": \[] }, (...remaining output omitted...) ] }`- 
                    For API details, see [DescribeClusterSecurityGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-security-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-cluster-snapshots`.

- **AWS CLI**
- 
            
                    Get a Description of All Cluster SnapshotsThis example returns a description of all cluster snapshots for the account. By default, the output is in JSON format.Command: `aws redshift describe-cluster-snapshots`Result: `{ "Snapshots": [ { "Status": "available", "SnapshotCreateTime": "2013-07-17T22:02:22.852Z", "EstimatedSecondsToCompletion": -1, "AvailabilityZone": "us-east-1a", "ClusterVersion": "1.0", "MasterUsername": "adminuser", "Encrypted": false, "OwnerAccount": "111122223333", "BackupProgressInMegabytes": 20.0, "ElapsedTimeInSeconds": 0, "DBName": "dev", "CurrentBackupRateInMegabytesPerSecond: 0.0, "ClusterCreateTime": "2013-01-22T21:59:29.559Z", "ActualIncrementalBackupSizeInMegabytes"; 20.0 "SnapshotType": "automated", "NodeType": "dw.hs1.xlarge", "ClusterIdentifier": "mycluster", "Port": 5439, "TotalBackupSizeInMegabytes": 20.0, "NumberOfNodes": "2", "SnapshotIdentifier": "cm:mycluster-2013-01-22-22-04-18" }, { "EstimatedSecondsToCompletion": 0, "OwnerAccount": "111122223333", "CurrentBackupRateInMegabytesPerSecond: 0.1534, "ActualIncrementalBackupSizeInMegabytes"; 11.0, "NumberOfNodes": "2", "Status": "available", "ClusterVersion": "1.0", "MasterUsername": "adminuser", "AccountsWithRestoreAccess": [ { "AccountID": "444455556666" } ], "TotalBackupSizeInMegabytes": 20.0, "DBName": "dev", "BackupProgressInMegabytes": 11.0, "ClusterCreateTime": "2013-01-22T21:59:29.559Z", "ElapsedTimeInSeconds": 0, "ClusterIdentifier": "mycluster", "SnapshotCreateTime": "2013-07-17T22:04:18.947Z", "AvailabilityZone": "us-east-1a", "NodeType": "dw.hs1.xlarge", "Encrypted": false, "SnapshotType": "manual", "Port": 5439, "SnapshotIdentifier": "my-snapshot-id" } ] } (...remaining output omitted...)`- 
                    For API details, see [DescribeClusterSnapshots](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-snapshots.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-cluster-subnet-groups`.

- **AWS CLI**
- 
            
                    Get a Description of All Cluster Subnet GroupsThis example returns a description of all cluster subnet groups. By default, the output is in JSON format.Command: `aws redshift describe-cluster-subnet-groups`Result: `{ "ClusterSubnetGroups": [ { "Subnets": [ { "SubnetStatus": "Active", "SubnetIdentifier": "subnet-763fdd1c", "SubnetAvailabilityZone": { "Name": "us-east-1a" } } ], "VpcId": "vpc-7e3fdd14", "SubnetGroupStatus": "Complete", "Description": "My subnet group", "ClusterSubnetGroupName": "mysubnetgroup" } ], "ResponseMetadata": { "RequestId": "37fa8c89-6990-11e2-8f75-ab4018764c77" } }`- 
                    For API details, see [DescribeClusterSubnetGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-subnet-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-cluster-tracks`.

- **AWS CLI**
- 
            
                    **To describe cluster tracks**The following `describe-cluster-tracks`example displays details of the available maintenance tracks.`aws redshift describe-cluster-tracks \ --maintenance-track-name``current`Output: `{ "MaintenanceTracks": [ { "MaintenanceTrackName": "current", "DatabaseVersion": "1.0.11420", "UpdateTargets": [ { "MaintenanceTrackName": "preview_features", "DatabaseVersion": "1.0.11746", "SupportedOperations": [ { "OperationName": "restore-from-cluster-snapshot" } ] }, { "MaintenanceTrackName": "trailing", "DatabaseVersion": "1.0.11116", "SupportedOperations": [ { "OperationName": "restore-from-cluster-snapshot" }, { "OperationName": "modify-cluster" } ] } ] } ] }`For more information, see [Choosing Cluster Maintenance Tracks](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-mgmt-maintenance-tracks)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [DescribeClusterTracks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-tracks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-cluster-versions`.

- **AWS CLI**
- 
            
                    Get a Description of All Cluster VersionsThis example returns a description of all cluster versions. By default, the output is in JSON format.Command: `aws redshift describe-cluster-versions`Result: `{ "ClusterVersions": [ { "ClusterVersion": "1.0", "Description": "Initial release", "ClusterParameterGroupFamily": "redshift-1.0" } ], "ResponseMetadata": { "RequestId": "16a53de3-64cc-11e2-bec0-17624ad140dd" } }`- 
                    For API details, see [DescribeClusterVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-clusters`.

- **AWS CLI**
- 
            
                    Get a Description of All ClustersThis example returns a description of all clusters for the account. By default, the output is in JSON format.Command: `aws redshift describe-clusters`Result: `{ "Clusters": [ { "NodeType": "dw.hs1.xlarge", "Endpoint": { "Port": 5439, "Address": "mycluster.coqoarplqhsn.us-east-1.redshift.amazonaws.com" }, "ClusterVersion": "1.0", "PubliclyAccessible": "true", "MasterUsername": "adminuser", "ClusterParameterGroups": [ { "ParameterApplyStatus": "in-sync", "ParameterGroupName": "default.redshift-1.0" } ], "ClusterSecurityGroups": [ { "Status": "active", "ClusterSecurityGroupName": "default" } ], "AllowVersionUpgrade": true, "VpcSecurityGroups": \[], "AvailabilityZone": "us-east-1a", "ClusterCreateTime": "2013-01-22T21:59:29.559Z", "PreferredMaintenanceWindow": "sat:03:30-sat:04:00", "AutomatedSnapshotRetentionPeriod": 1, "ClusterStatus": "available", "ClusterIdentifier": "mycluster", "DBName": "dev", "NumberOfNodes": 2, "PendingModifiedValues": {} } ], "ResponseMetadata": { "RequestId": "65b71cac-64df-11e2-8f5b-e90bd6c77476" } }`You can also obtain the same information in text format using the `--output text`option.Command:`--output text`option.Command:option.Command: `aws redshift describe-clusters --output text`Result: `dw.hs1.xlarge 1.0 true adminuser True us-east-1a 2013-01-22T21:59:29.559Z sat:03:30-sat:04:00 1 available mycluster dev 2 ENDPOINT 5439 mycluster.coqoarplqhsn.us-east-1.redshift.amazonaws.com in-sync default.redshift-1.0 active default PENDINGMODIFIEDVALUES RESPONSEMETADATA 934281a8-64df-11e2-b07c-f7fbdd006c67`- 
                    For API details, see [DescribeClusters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-clusters.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-default-cluster-parameters`.

- **AWS CLI**
- 
            
                    Get a Description of Default Cluster ParametersThis example returns a description of the default cluster parameters for the `redshift-1.0`family. By default, the output is in JSON format.Command:`aws redshift describe-default-cluster-parameters --parameter-group-family redshift-1.0`Result: `{ "DefaultClusterParameters": { "ParameterGroupFamily": "redshift-1.0", "Parameters": [ { "Description": "Sets the display format for date and time values.", "DataType": "string", "IsModifiable": true, "Source": "engine-default", "ParameterValue": "ISO, MDY", "ParameterName": "datestyle" }, { "Description": "Sets the number of digits displayed for floating-point values", "DataType": "integer", "IsModifiable": true, "AllowedValues": "-15-2", "Source": "engine-default", "ParameterValue": "0", "ParameterName": "extra_float_digits" }, (...remaining output omitted...) ] } }`To see a list of valid parameter group families, use the `describe-cluster-parameter-groups`command.`describe-cluster-parameter-groups`command.command. - 
                    For API details, see [DescribeDefaultClusterParameters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-default-cluster-parameters.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-event-categories`.

- **AWS CLI**
- 
            
                    **To describe event categories for a cluster**The following `describe-event-categories`example displays details for the event categories for a cluster.`aws redshift describe-event-categories \ --source-type``cluster`Output: `{ "EventCategoriesMapList": [ { "SourceType": "cluster", "Events": [ { "EventId": "REDSHIFT-EVENT-2000", "EventCategories": [ "management" ], "EventDescription": "Cluster <cluster name> created at <time in UTC>.", "Severity": "INFO" }, { "EventId": "REDSHIFT-EVENT-2001", "EventCategories": [ "management" ], "EventDescription": "Cluster <cluster name> deleted at <time in UTC>.", "Severity": "INFO" }, { "EventId": "REDSHIFT-EVENT-3625", "EventCategories": [ "monitoring" ], "EventDescription": "The cluster <cluster name> can't be resumed with its previous elastic network interface <ENI id>. We will allocate a new elastic network interface and associate it with the cluster node.", "Severity": "INFO" } ] } ] }`- 
                    For API details, see [DescribeEventCategories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-event-categories.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-event-subscriptions`.

- **AWS CLI**
- 
            
                    **To describe event subscriptions**The following `describe-event-subscriptions`example displays event notification subscriptions for the specified subscription.`aws redshift describe-event-subscriptions \ --subscription-name``mysubscription`Output: `{ "EventSubscriptionsList": [ { "CustomerAwsId": "123456789012", "CustSubscriptionId": "mysubscription", "SnsTopicArn": "arn:aws:sns:us-west-2:123456789012:MySNStopic", "Status": "active", "SubscriptionCreationTime": "2019-12-09T21:50:21.332Z", "SourceIdsList": [], "EventCategoriesList": [ "management" ], "Severity": "ERROR", "Enabled": true, "Tags": [] } ] }`For more information, see [Subscribing to Amazon Redshift Event Notifications](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-event-notifications.html)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [DescribeEventSubscriptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-event-subscriptions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-events`.

- **AWS CLI**
- 
            
                    Describe All Eventsthis example returns all events. By default, the output is in JSON format.Command: `aws redshift describe-events`Result: `{ "Events": [ { "Date": "2013-01-22T19:17:03.640Z", "SourceIdentifier": "myclusterparametergroup", "Message": "Cluster parameter group myclusterparametergroup has been created.", "SourceType": "cluster-parameter-group" } ], "ResponseMetadata": { "RequestId": "9f056111-64c9-11e2-9390-ff04f2c1e638" } }`You can also obtain the same information in text format using the `--output text`option.Command:`--output text`option.Command:option.Command: `aws redshift describe-events --output text`Result: `2013-01-22T19:17:03.640Z myclusterparametergroup Cluster parameter group myclusterparametergroup has been created. cluster-parameter-group RESPONSEMETADATA 8e5fe765-64c9-11e2-bce3-e56f52c50e17`- 
                    For API details, see [DescribeEvents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-events.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-hsm-client-certificates`.

- **AWS CLI**
- 
            
                    **To describe HSM client certificates**The following `describe-hsm-client-certificates`example displays details for the specified HSM client certificate.`aws redshift describe-hsm-client-certificates \ --hsm-client-certificate-identifier``myhsmclientcert`Output: `{ "HsmClientCertificates": [ { "HsmClientCertificateIdentifier": "myhsmclientcert", "HsmClientCertificatePublicKey": "-----BEGIN CERTIFICATE-----\ EXAMPLECAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC VVMxCzAJBgNVBAEXAMPLERAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6 b24xFDASBgNVBAsTC0lBTSBDb25zEXAMPLEwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhEXAMPLEDI1MjA0EXAMPLEN EXAMPLE0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD VQQHEwdTZWF0dGEXAMPLEQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z b2xlMRIwEAYDVQQDEwlUZXN0Q2lsEXAMPLEdBgkqhkiG9w0BCQEWEG5vb25lQGFt YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIEXAMPLEMaK0dn+a4GmWIWJ 21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY67EXAMPLEE EXAMPLEZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4 nUhVVxYUntneD9EXAMPLE6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb FFBjvSfpJIlJ00zbhNYS5f6GuoEDEXAMPLEBHjJnyp378OD8uTs7fLvjx79LjSTb NYiytVbZPQUQ5Yaxu2jXnimvw3rEXAMPLE=-----END CERTIFICATE-----\n", "Tags": [] } ] }`For more information, see [Amazon Redshift API Permissions Reference](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-policy-resources.resource-permissions.html)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [DescribeHsmClientCertificates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-hsm-client-certificates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-hsm-configurations`.

- **AWS CLI**
- 
            
                    **To describe HSM configurations**The following `describe-hsm-configurations`example displays details for the available HSM configurations for the calling AWS account.`aws redshift describe-hsm-configurations``/`--hsm-configuration-identifier`myhsmconnection`Output: `{ "HsmConfigurations": [ { "HsmConfigurationIdentifier": "myhsmconnection", "Description": "My HSM connection", "HsmIpAddress": "192.0.2.09", "HsmPartitionName": "myhsmpartition", "Tags": [] } ] }`- 
                    For API details, see [DescribeHsmConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-hsm-configurations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-logging-status`.

- **AWS CLI**
- 
            
                    **To describe logging status for a cluster**The following `describe-logging-status`example displays whether information, such as queries and connection attempts, is being logged for a cluster.`aws redshift describe-logging-status \ --cluster-identifier``mycluster`Output: `{ "LoggingEnabled": false }`For more information, see [Database Audit Logging](https://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing.html)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [DescribeLoggingStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-logging-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-node-configuration-options`.

- **AWS CLI**
- 
            
                    **To describe node configuration options**The following `describe-node-configuration-options`example displays the properties of possible node configurations such as node type, number of nodes, and disk usage for the specified cluster snapshot.`aws redshift describe-node-configuration-options \ --action-type``restore-cluster`\ --snapshot-identifier`rs:mycluster-2019-12-09-16-42-43`Output: `{ "NodeConfigurationOptionList": [ { "NodeType": "dc2.large", "NumberOfNodes": 2, "EstimatedDiskUtilizationPercent": 19.61 }, { "NodeType": "dc2.large", "NumberOfNodes": 4, "EstimatedDiskUtilizationPercent": 9.96 }, { "NodeType": "ds2.xlarge", "NumberOfNodes": 2, "EstimatedDiskUtilizationPercent": 1.53 }, { "NodeType": "ds2.xlarge", "NumberOfNodes": 4, "EstimatedDiskUtilizationPercent": 0.78 } ] }`For more information, see [Purchasing Amazon Redshift Reserved Nodes](https://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-instance.html)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [DescribeNodeConfigurationOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-node-configuration-options.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-orderable-cluster-options`.

- **AWS CLI**
- 
            
                    Describing All Orderable Cluster OptionsThis example returns descriptions of all orderable cluster options. By default, the output is in JSON format.Command: `aws redshift describe-orderable-cluster-options`Result: `{ "OrderableClusterOptions": [ { "NodeType": "dw.hs1.8xlarge", "AvailabilityZones": [ { "Name": "us-east-1a" }, { "Name": "us-east-1b" }, { "Name": "us-east-1c" } ], "ClusterVersion": "1.0", "ClusterType": "multi-node" }, { "NodeType": "dw.hs1.xlarge", "AvailabilityZones": [ { "Name": "us-east-1a" }, { "Name": "us-east-1b" }, { "Name": "us-east-1c" } ], "ClusterVersion": "1.0", "ClusterType": "multi-node" }, { "NodeType": "dw.hs1.xlarge", "AvailabilityZones": [ { "Name": "us-east-1a" }, { "Name": "us-east-1b" }, { "Name": "us-east-1c" } ], "ClusterVersion": "1.0", "ClusterType": "single-node" } ], "ResponseMetadata": { "RequestId": "f6000035-64cb-11e2-9135-ff82df53a51a" } }`You can also obtain the same information in text format using the `--output text`option.Command:`--output text`option.Command:option.Command: `aws redshift describe-orderable-cluster-options --output text`Result: `dw.hs1.8xlarge 1.0 multi-node us-east-1a us-east-1b us-east-1c dw.hs1.xlarge 1.0 multi-node us-east-1a us-east-1b us-east-1c dw.hs1.xlarge 1.0 single-node us-east-1a us-east-1b us-east-1c RESPONSEMETADATA e648696b-64cb-11e2-bec0-17624ad140dd`- 
                    For API details, see [DescribeOrderableClusterOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-orderable-cluster-options.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-reserved-node-offerings`.

- **AWS CLI**
- 
            
                    Describe Reserved Node OfferingsThis example shows all of the reserved node offerings that are available for purchase.Command: `aws redshift describe-reserved-node-offerings`Result: `{ "ReservedNodeOfferings": [ { "OfferingType": "Heavy Utilization", "FixedPrice": "", "NodeType": "dw.hs1.xlarge", "UsagePrice": "", "RecurringCharges": [ { "RecurringChargeAmount": "", "RecurringChargeFrequency": "Hourly" } ], "Duration": 31536000, "ReservedNodeOfferingId": "ceb6a579-cf4c-4343-be8b-d832c45ab51c" }, { "OfferingType": "Heavy Utilization", "FixedPrice": "", "NodeType": "dw.hs1.8xlarge", "UsagePrice": "", "RecurringCharges": [ { "RecurringChargeAmount": "", "RecurringChargeFrequency": "Hourly" } ], "Duration": 31536000, "ReservedNodeOfferingId": "e5a2ff3b-352d-4a9c-ad7d-373c4cab5dd2" }, ...remaining output omitted... ], "ResponseMetadata": { "RequestId": "8b1a1a43-75ff-11e2-9666-e142fe91ddd1" } }`If you want to purchase a reserved node offering, you can call `purchase-reserved-node-offering`using a valid*ReservedNodeOfferingId*.`purchase-reserved-node-offering`using a valid*ReservedNodeOfferingId*.using a valid *ReservedNodeOfferingId*.*ReservedNodeOfferingId*.. - 
                    For API details, see [DescribeReservedNodeOfferings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-reserved-node-offerings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-reserved-nodes`.

- **AWS CLI**
- 
            
                    Describe Reserved NodesThis example shows a reserved node offering that has been purchased.Command: `aws redshift describe-reserved-nodes`Result: `{ "ResponseMetadata": { "RequestId": "bc29ce2e-7600-11e2-9949-4b361e7420b7" }, "ReservedNodes": [ { "OfferingType": "Heavy Utilization", "FixedPrice": "", "NodeType": "dw.hs1.xlarge", "ReservedNodeId": "1ba8e2e3-bc01-4d65-b35d-a4a3e931547e", "UsagePrice": "", "RecurringCharges": [ { "RecurringChargeAmount": "", "RecurringChargeFrequency": "Hourly" } ], "NodeCount": 1, "State": "payment-pending", "StartTime": "2013-02-13T17:08:39.051Z", "Duration": 31536000, "ReservedNodeOfferingId": "ceb6a579-cf4c-4343-be8b-d832c45ab51c" } ] }`- 
                    For API details, see [DescribeReservedNodes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-reserved-nodes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-resize`.

- **AWS CLI**
- 
            
                    Describe ResizeThis example describes the latest resize of a cluster. The request was for 3 nodes of type `dw.hs1.8xlarge`.Command:`aws redshift describe-resize --cluster-identifier mycluster`Result: `{ "Status": "NONE", "TargetClusterType": "multi-node", "TargetNodeType": "dw.hs1.8xlarge", "ResponseMetadata": { "RequestId": "9f52b0b4-7733-11e2-aa9b-318b2909bd27" }, "TargetNumberOfNodes": "3" }`- 
                    For API details, see [DescribeResize](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-resize.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-scheduled-actions`.

- **AWS CLI**
- 
            
                    **To describe scheduled actions**The following `describe-scheduled-actions`example displays details for any currently scheduled actions.`aws redshift describe-scheduled-actions`Output: `{ "ScheduledActions": [ { "ScheduledActionName": "resizecluster", "TargetAction": { "ResizeCluster": { "ClusterIdentifier": "mycluster", "NumberOfNodes": 4, "Classic": false } }, "Schedule": "at(2019-12-10T00:07:00)", "IamRole": "arn:aws:iam::123456789012:role/myRedshiftRole", "State": "ACTIVE", "NextInvocations": [ "2019-12-10T00:07:00Z" ] } ] }`- 
                    For API details, see [DescribeScheduledActions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-scheduled-actions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-snapshot-copy-grants`.

- **AWS CLI**
- 
            
                    **To describe snapshot copy grants**The following `describe-snapshot-copy-grants`example displays details for the specified cluster snapshot copy grant.`aws redshift describe-snapshot-copy-grants \ --snapshot-copy-grant-name``mysnapshotcopygrantname`Output: `{ "SnapshotCopyGrants": [ { "SnapshotCopyGrantName": "mysnapshotcopygrantname", "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/bPxRfih3yCo8nvbEXAMPLEKEY", "Tags": [] } ] }`For more information, see [Amazon Redshift Database Encryption](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [DescribeSnapshotCopyGrants](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-snapshot-copy-grants.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-snapshot-schedules`.

- **AWS CLI**
- 
            
                    **To describe snapshot schedules**The following `describe-snapshot-schedules`example displays details for the specified cluster snapshot schedule.`aws redshift describe-snapshot-schedules \ --cluster-identifier``mycluster`\ --schedule-identifier`mysnapshotschedule`Output: `{ "SnapshotSchedules": [ { "ScheduleDefinitions": [ "rate(12 hours)" ], "ScheduleIdentifier": "mysnapshotschedule", "ScheduleDescription": "My schedule description", "Tags": [], "AssociatedClusterCount": 1, "AssociatedClusters": [ { "ClusterIdentifier": "mycluster", "ScheduleAssociationState": "ACTIVE" } ] } ] }`For more information, see [Automated Snapshot Schedules](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html#automated-snapshot-schedules)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [DescribeSnapshotSchedules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-snapshot-schedules.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-storage`.

- **AWS CLI**
- 
            
                    **To describe storage**The following `describe-storage`example displays details about the backup storage and provisional storage sizes for the account.`aws redshift describe-storage`Output: `{ "TotalBackupSizeInMegaBytes": 193149.0, "TotalProvisionedStorageInMegaBytes": 655360.0 }`For more information, see [Managing Snapshot Storage](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html#managing-snapshot-storage)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [DescribeStorage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-storage.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-table-restore-status`.

- **AWS CLI**
- 
            
                    **To describe status of table restore requests from a cluster snapshot**The following `describe-table-restore-status`example displays details for table restore requests made for the specified cluster.`aws redshift describe-table-restore-status``/`--cluster-identifier`mycluster`Output: `{ "TableRestoreStatusDetails": [ { "TableRestoreRequestId": "z1116630-0e80-46f4-ba86-bd9670411ebd", "Status": "IN_PROGRESS", "RequestTime": "2019-12-27T18:22:12.257Z", "ClusterIdentifier": "mycluster", "SnapshotIdentifier": "mysnapshotid", "SourceDatabaseName": "dev", "SourceSchemaName": "public", "SourceTableName": "mytable", "TargetDatabaseName": "dev", "TargetSchemaName": "public", "NewTableName": "mytable-clone" } ] }`For more information, see [Restoring a Table from a Snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html#working-with-snapshot-restore-table-from-snapshot)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [DescribeTableRestoreStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-table-restore-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-tags`.

- **AWS CLI**
- 
            
                    **To describe tags**The following `describe-tags`example displays the resources the specified cluster associated with the specified tag names and values.`aws redshift describe-tags \ --resource-name``arn:aws:redshift:us-west-2:123456789012:cluster:mycluster`\ --tag-keys`clustertagkey`\ --tag-values`clustertagvalue`Output: `{ "TaggedResources": [ { "Tag": { "Key": "clustertagkey", "Value": "clustertagvalue" }, "ResourceName": "arn:aws:redshift:us-west-2:123456789012:cluster:mycluster", "ResourceType": "cluster" } ] }`For more information, see [Tagging Resources in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-tagging.html)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [DescribeTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-snapshot-copy`.

- **AWS CLI**
- 
            
                    **To disable snapshot copy for a cluster**The following `disable-snapshot-copy`example disables the automatic copy of a snapshot for the specified cluster.`aws redshift disable-snapshot-copy \ --cluster-identifier``mycluster`Output: `{ "Cluster": { "ClusterIdentifier": "mycluster", "NodeType": "dc2.large", "ClusterStatus": "available", "ClusterAvailabilityStatus": "Available", "MasterUsername": "adminuser", "DBName": "dev", "Endpoint": { "Address": "mycluster.cmeaswqeuae.us-west-2.redshift.amazonaws.com", "Port": 5439 }, "ClusterCreateTime": "2019-12-05T18:44:36.991Z", "AutomatedSnapshotRetentionPeriod": 3, "ManualSnapshotRetentionPeriod": -1, "ClusterSecurityGroups": [], "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sh-i9b431cd", "Status": "active" } ], "ClusterParameterGroups": [ { "ParameterGroupName": "default.redshift-1.0", "ParameterApplyStatus": "in-sync" } ], "ClusterSubnetGroupName": "default", "VpcId": "vpc-b1fel7t9", "AvailabilityZone": "us-west-2f", "PreferredMaintenanceWindow": "sat:16:00-sat:16:30", "PendingModifiedValues": { "NodeType": "dc2.large", "NumberOfNodes": 2, "ClusterType": "multi-node" }, "ClusterVersion": "1.0", "AllowVersionUpgrade": true, "NumberOfNodes": 4, "PubliclyAccessible": false, "Encrypted": false, "Tags": [ { "Key": "mytags", "Value": "tag1" } ], "EnhancedVpcRouting": false, "IamRoles": [ { "IamRoleArn": "arn:aws:iam::123456789012:role/myRedshiftRole", "ApplyStatus": "in-sync" } ], "MaintenanceTrackName": "current", "DeferredMaintenanceWindows": [], "ExpectedNextSnapshotScheduleTime": "2019-12-10T04:42:43.390Z", "ExpectedNextSnapshotScheduleTimeStatus": "OnTrack", "NextMaintenanceWindowStartTime": "2019-12-14T16:00:00Z" } }`For more information, see [Copying Snapshots to Another AWS Region](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html#cross-region-snapshot-copy)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [DisableSnapshotCopy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/disable-snapshot-copy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-snapshot-copy`.

- **AWS CLI**
- 
            
                    **To enable snapshot copy for a cluster**The following `enable-snapshot-copy`example enables the automatic copy of a snapshot for the specified cluster.`aws redshift enable-snapshot-copy \ --cluster-identifier``mycluster`\ --destination-region`us-west-1`Output: `{ "Cluster": { "ClusterIdentifier": "mycluster", "NodeType": "dc2.large", "ClusterStatus": "available", "ClusterAvailabilityStatus": "Available", "MasterUsername": "adminuser", "DBName": "dev", "Endpoint": { "Address": "mycluster.cmeaswqeuae.us-west-2.redshift.amazonaws.com", "Port": 5439 }, "ClusterCreateTime": "2019-12-05T18:44:36.991Z", "AutomatedSnapshotRetentionPeriod": 3, "ManualSnapshotRetentionPeriod": -1, "ClusterSecurityGroups": [], "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sh-f4c731cd", "Status": "active" } ], "ClusterParameterGroups": [ { "ParameterGroupName": "default.redshift-1.0", "ParameterApplyStatus": "in-sync" } ], "ClusterSubnetGroupName": "default", "VpcId": "vpc-b1ael7t9", "AvailabilityZone": "us-west-2f", "PreferredMaintenanceWindow": "sat:16:00-sat:16:30", "PendingModifiedValues": { "NodeType": "dc2.large", "NumberOfNodes": 2, "ClusterType": "multi-node" }, "ClusterVersion": "1.0", "AllowVersionUpgrade": true, "NumberOfNodes": 4, "PubliclyAccessible": false, "Encrypted": false, "ClusterSnapshotCopyStatus": { "DestinationRegion": "us-west-1", "RetentionPeriod": 7, "ManualSnapshotRetentionPeriod": -1 }, "Tags": [ { "Key": "mytags", "Value": "tag1" } ], "EnhancedVpcRouting": false, "IamRoles": [ { "IamRoleArn": "arn:aws:iam::123456789012:role/myRedshiftRole", "ApplyStatus": "in-sync" } ], "MaintenanceTrackName": "current", "DeferredMaintenanceWindows": [], "ExpectedNextSnapshotScheduleTime": "2019-12-10T04:42:43.390Z", "ExpectedNextSnapshotScheduleTimeStatus": "OnTrack", "NextMaintenanceWindowStartTime": "2019-12-14T16:00:00Z" } }`For more information, see [Copying Snapshots to Another AWS Region](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html#cross-region-snapshot-copy)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [EnableSnapshotCopy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/enable-snapshot-copy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-cluster-credentials`.

- **AWS CLI**
- 
            
                    **To get cluster credentials for an AWS account**The following `get-cluster-credentials`example retrieves temporary credentials that enable access to an Amazon Redshift database.`aws redshift get-cluster-credentials \ --db-user``adminuser`--db-name`dev`\ --cluster-identifier`mycluster`Output: `{ "DbUser": "IAM:adminuser", "DbPassword": "AMAFUyyuros/QjxPTtgzcsuQsqzIasdzJEN04aCtWDzXx1O9d6UmpkBtvEeqFly/EXAMPLE==", "Expiration": "2019-12-10T17:25:05.770Z" }`For more information, see [Generating IAM Database Credentials Using the Amazon Redshift CLI or API](https://docs.aws.amazon.com/redshift/latest/mgmt/generating-iam-credentials-cli-api.html)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [GetClusterCredentials](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/get-cluster-credentials.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-reserved-node-exchange-offerings`.

- **AWS CLI**
- 
            
                    **To get reserved node exchange offerings**The following `get-reserved-node-exchange-offerings`example retrieves an array of`DC2``ReservedNodeOfferings`that match the specified`DC1`reserved node.`aws redshift get-reserved-node-exchange-offerings \ --reserved-node-id``12345678-12ab-12a1-1a2a-12ab-12a12EXAMPLE`Output: `{ "ReservedNodeOfferings": [ { "ReservedNodeOfferingId": "12345678-12ab-12a1-1a2a-12ab-12a12EXAMPLE", "NodeType": "dc2.large", "Duration": 31536000, "FixedPrice": 0.0, "UsagePrice": 0.0, "CurrencyCode": "USD", "OfferingType": "All Upfront", "RecurringCharges": [ { "RecurringChargeAmount": 0.0, "RecurringChargeFrequency": "Hourly" } ], "ReservedNodeOfferingType": "Regular" } ] }`For more information, see [Upgrading Reserved Nodes With the AWS CLI](https://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-offering-console.html)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [GetReservedNodeExchangeOfferings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/get-reserved-node-exchange-offerings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-cluster-iam-roles`.

- **AWS CLI**
- 
            
                    **To modify the IAM role for a cluster**The following `modify-cluster-iam-roles`example removes the specified AWS IAM role from the specified cluster.`aws redshift modify-cluster-iam-roles \ --cluster-identifier``mycluster`\ --remove-iam-roles`arn:aws:iam::123456789012:role/myRedshiftRole`Output: `{ "Cluster": { "ClusterIdentifier": "mycluster", "NodeType": "dc2.large", "ClusterStatus": "available", "ClusterAvailabilityStatus": "Available", "MasterUsername": "adminuser", "DBName": "dev", "Endpoint": { "Address": "mycluster.cmeaswqeuae.us-west-2.redshift.amazonaws.com", "Port": 5439 }, "ClusterCreateTime": "2019-12-05T18:44:36.991Z", "AutomatedSnapshotRetentionPeriod": 3, "ManualSnapshotRetentionPeriod": -1, "ClusterSecurityGroups": [], "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sh-f9b731sd", "Status": "active" } ], "ClusterParameterGroups": [ { "ParameterGroupName": "default.redshift-1.0", "ParameterApplyStatus": "in-sync" } ], "ClusterSubnetGroupName": "default", "VpcId": "vpc-b2fal7t9", "AvailabilityZone": "us-west-2f", "PreferredMaintenanceWindow": "sat:16:00-sat:16:30", "PendingModifiedValues": { "NodeType": "dc2.large", "NumberOfNodes": 2, "ClusterType": "multi-node" }, "ClusterVersion": "1.0", "AllowVersionUpgrade": true, "NumberOfNodes": 4, "PubliclyAccessible": false, "Encrypted": false, "ClusterSnapshotCopyStatus": { "DestinationRegion": "us-west-1", "RetentionPeriod": 7, "ManualSnapshotRetentionPeriod": -1 }, "Tags": [ { "Key": "mytags", "Value": "tag1" } ], "EnhancedVpcRouting": false, "IamRoles": [], "MaintenanceTrackName": "current", "DeferredMaintenanceWindows": [], "ExpectedNextSnapshotScheduleTime": "2019-12-11T04:42:55.631Z", "ExpectedNextSnapshotScheduleTimeStatus": "OnTrack", "NextMaintenanceWindowStartTime": "2019-12-14T16:00:00Z" } }`For more information, see [Using Identity-Based Policies (IAM Policies) for Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [ModifyClusterIamRoles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-iam-roles.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-cluster-maintenance`.

- **AWS CLI**
- 
            
                    **To modify cluster maintenance**The following `modify-cluster-maintenance`example defers the maintenance of the specified cluster by 30 days.`aws redshift modify-cluster-maintenance \ --cluster-identifier``mycluster`\ --defer-maintenance \ --defer-maintenance-duration`30`Output: `{ "Cluster": { "ClusterIdentifier": "mycluster", "NodeType": "dc2.large", "ClusterStatus": "available", "ClusterAvailabilityStatus": "Available", "MasterUsername": "adminuser", "DBName": "dev", "Endpoint": { "Address": "mycluster.cmeaswqeuae.us-west-2.redshift.amazonaws.com", "Port": 5439 }, "ClusterCreateTime": "2019-12-05T18:44:36.991Z", "AutomatedSnapshotRetentionPeriod": 3, "ManualSnapshotRetentionPeriod": -1, "ClusterSecurityGroups": [], "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sh-a1a123ab", "Status": "active" } ], "ClusterParameterGroups": [ { "ParameterGroupName": "default.redshift-1.0", "ParameterApplyStatus": "in-sync" } ], "ClusterSubnetGroupName": "default", "VpcId": "vpc-b1ael7t9", "AvailabilityZone": "us-west-2f", "PreferredMaintenanceWindow": "sat:16:00-sat:16:30", "PendingModifiedValues": { "NodeType": "dc2.large", "NumberOfNodes": 2, "ClusterType": "multi-node" }, "ClusterVersion": "1.0", "AllowVersionUpgrade": true, "NumberOfNodes": 4, "PubliclyAccessible": false, "Encrypted": false, "ClusterSnapshotCopyStatus": { "DestinationRegion": "us-west-1", "RetentionPeriod": 7, "ManualSnapshotRetentionPeriod": -1 }, "Tags": [ { "Key": "mytags", "Value": "tag1" } ], "EnhancedVpcRouting": false, "IamRoles": [], "MaintenanceTrackName": "current", "DeferredMaintenanceWindows": [ { "DeferMaintenanceIdentifier": "dfm-mUdVIfFcT1B4SGhw6fyF", "DeferMaintenanceStartTime": "2019-12-10T18:18:39.354Z", "DeferMaintenanceEndTime": "2020-01-09T18:18:39.354Z" } ], "ExpectedNextSnapshotScheduleTime": "2019-12-11T04:42:55.631Z", "ExpectedNextSnapshotScheduleTimeStatus": "OnTrack", "NextMaintenanceWindowStartTime": "2020-01-11T16:00:00Z" } }`For more information, see [Cluster Maintenance](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-cluster-maintenance)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [ModifyClusterMaintenance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-maintenance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-cluster-parameter-group`.

- **AWS CLI**
- 
            
                    **Modify a parameter in a parameter group**The following `modify-cluster-parameter-group`example modifies the*wlm_json_configuration*parameter for workload management. It accepts the parameters from a file that contains the JSON contents shown below.`aws redshift modify-cluster-parameter-group \ --parameter-group-name``myclusterparametergroup`\ --parameters`file://modify_pg.json`Contents of `modify_pg.json`:`[ { "ParameterName": "wlm_json_configuration", "ParameterValue": "[{\"user_group\":\"example_user_group1\",\"query_group\": \"example_query_group1\", \"query_concurrency\":7},{\"query_concurrency\":5}]" } ]`Output: `{ "ParameterGroupStatus": "Your parameter group has been updated but changes won't get applied until you reboot the associated Clusters.", "ParameterGroupName": "myclusterparametergroup", "ResponseMetadata": { "RequestId": "09974cc0-64cd-11e2-bea9-49e0ce183f07" } }`- 
                    For API details, see [ModifyClusterParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-parameter-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-cluster-snapshot-schedule`.

- **AWS CLI**
- 
            
                    **To modify cluster snapshot schedule**The following `modify-cluster-snapshot-schedule`example removes the specified snapshot schedule from the specified cluster.`aws redshift modify-cluster-snapshot-schedule \ --cluster-identifier``mycluster`\ --schedule-identifier`mysnapshotschedule`\ --disassociate-scheduleThis command does not produce any output. For more information, see [Automated Snapshot Schedules](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html#automated-snapshot-schedules)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [ModifyClusterSnapshotSchedule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-snapshot-schedule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-cluster-snapshot`.

- **AWS CLI**
- 
            
                    **To modify cluster snapshot**The following `modify-cluster-snapshot`example sets the manual retention period setting for the specified cluster snapshot to value of 10 days.`aws redshift modify-cluster-snapshot \ --snapshot-identifier``mycluster-2019-11-06-16-32`\ --manual-snapshot-retention-period`10`Output: `{ "Snapshot": { "SnapshotIdentifier": "mycluster-2019-11-06-16-32", "ClusterIdentifier": "mycluster", "SnapshotCreateTime": "2019-12-07T00:34:05.633Z", "Status": "available", "Port": 5439, "AvailabilityZone": "us-west-2f", "ClusterCreateTime": "2019-12-05T18:44:36.991Z", "MasterUsername": "adminuser", "ClusterVersion": "1.0", "SnapshotType": "manual", "NodeType": "dc2.large", "NumberOfNodes": 2, "DBName": "dev", "VpcId": "vpc-b1cel7t9", "Encrypted": false, "EncryptedWithHSM": false, "OwnerAccount": "123456789012", "TotalBackupSizeInMegaBytes": 64384.0, "ActualIncrementalBackupSizeInMegaBytes": 24.0, "BackupProgressInMegaBytes": 24.0, "CurrentBackupRateInMegaBytesPerSecond": 13.0011, "EstimatedSecondsToCompletion": 0, "ElapsedTimeInSeconds": 1, "Tags": [ { "Key": "mytagkey", "Value": "mytagvalue" } ], "EnhancedVpcRouting": false, "MaintenanceTrackName": "current", "ManualSnapshotRetentionPeriod": 10, "ManualSnapshotRemainingDays": 6, "SnapshotRetentionStartTime": "2019-12-07T00:34:07.479Z" } }`For more information, see [Amazon Redshift Snapshots](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [ModifyClusterSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-cluster-subnet-group`.

- **AWS CLI**
- 
            
                    Modify the Subnets in a Cluster Subnet GroupThis example shows how to modify the list of subnets in a cache subnet group. By default, the output is in JSON format.Command: `aws redshift modify-cluster-subnet-group --cluster-subnet-group-name mysubnetgroup --subnet-ids subnet-763fdd1 subnet-ac830e9`Result: `{ "ClusterSubnetGroup": { "Subnets": [ { "SubnetStatus": "Active", "SubnetIdentifier": "subnet-763fdd1c", "SubnetAvailabilityZone": { "Name": "us-east-1a" } }, { "SubnetStatus": "Active", "SubnetIdentifier": "subnet-ac830e9", "SubnetAvailabilityZone": { "Name": "us-east-1b" } } ], "VpcId": "vpc-7e3fdd14", "SubnetGroupStatus": "Complete", "Description": "My subnet group", "ClusterSubnetGroupName": "mysubnetgroup" }, "ResponseMetadata": { "RequestId": "8da93e89-8372-f936-93a8-873918938197a" } }`- 
                    For API details, see [ModifyClusterSubnetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-subnet-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-cluster`.

- **AWS CLI**
- 
            
                    Associate a Security Group with a ClusterThis example shows how to associate a cluster security group with the specified cluster.Command: `aws redshift modify-cluster --cluster-identifier mycluster --cluster-security-groups mysecuritygroup`Modify the Maintenance Window for a ClusterThis shows how to change the weekly preferred maintenance window for a cluster to be the minimum four hour window starting Sundays at 11:15 PM, and ending Mondays at 3:15 AM.Command: `aws redshift modify-cluster --cluster-identifier mycluster --preferred-maintenance-window Sun:23:15-Mon:03:15`Change the Master Password for the ClusterThis example shows how to change the master password for a cluster.Command: `aws redshift modify-cluster --cluster-identifier mycluster --master-user-password A1b2c3d4`- 
                    For API details, see [ModifyCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-event-subscription`.

- **AWS CLI**
- 
            
                    **To modify event subscription**The following `modify-event-subscription`example disables the specified event notification subscription.`aws redshift modify-event-subscription \ --subscription-name``mysubscription`\ --no-enabledOutput: `{ "EventSubscription": { "CustomerAwsId": "123456789012", "CustSubscriptionId": "mysubscription", "SnsTopicArn": "arn:aws:sns:us-west-2:123456789012:MySNStopic", "Status": "active", "SubscriptionCreationTime": "2019-12-09T21:50:21.332Z", "SourceIdsList": [], "EventCategoriesList": [ "management" ], "Severity": "ERROR", "Enabled": false, "Tags": [] } }`For more information, see [Subscribing to Amazon Redshift Event Notifications](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-event-notifications.html)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [ModifyEventSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-event-subscription.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-scheduled-action`.

- **AWS CLI**
- 
            
                    **To modify scheduled action**The following `modify-scheduled-action`example adds a description to the specified existing scheduled action.`aws redshift modify-scheduled-action \ --scheduled-action-name``myscheduledaction`\ --scheduled-action-description`"My scheduled action"`Output: `{ "ScheduledActionName": "myscheduledaction", "TargetAction": { "ResizeCluster": { "ClusterIdentifier": "mycluster", "NumberOfNodes": 2, "Classic": false } }, "Schedule": "at(2019-12-25T00:00:00)", "IamRole": "arn:aws:iam::123456789012:role/myRedshiftRole", "ScheduledActionDescription": "My scheduled action", "State": "ACTIVE", "NextInvocations": [ "2019-12-25T00:00:00Z" ] }`- 
                    For API details, see [ModifyScheduledAction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-scheduled-action.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-snapshot-copy-retention-period`.

- **AWS CLI**
- 
            
                    **To modify snapshot copy retention period**The following `modify-snapshot-copy-retention-period`example modifies the number of days to retain snapshots for the specified cluster in the destination AWS Region after they are copied from the source AWS Region.`aws redshift modify-snapshot-copy-retention-period \ --cluster-identifier``mycluster`\ --retention-period`15`Output: `{ "Cluster": { "ClusterIdentifier": "mycluster", "NodeType": "dc2.large", "ClusterStatus": "available", "ClusterAvailabilityStatus": "Available", "MasterUsername": "adminuser", "DBName": "dev", "Endpoint": { "Address": "mycluster.cmeaswqeuae.us-west-2.redshift.amazonaws.com", "Port": 5439 }, "ClusterCreateTime": "2019-12-05T18:44:36.991Z", "AutomatedSnapshotRetentionPeriod": 3, "ManualSnapshotRetentionPeriod": -1, "ClusterSecurityGroups": [], "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sh-a1a123ab", "Status": "active" } ], "ClusterParameterGroups": [ { "ParameterGroupName": "default.redshift-1.0", "ParameterApplyStatus": "in-sync" } ], "ClusterSubnetGroupName": "default", "VpcId": "vpc-b1fet7t9", "AvailabilityZone": "us-west-2f", "PreferredMaintenanceWindow": "sat:16:00-sat:16:30", "PendingModifiedValues": { "NodeType": "dc2.large", "NumberOfNodes": 2, "ClusterType": "multi-node" }, "ClusterVersion": "1.0", "AllowVersionUpgrade": true, "NumberOfNodes": 4, "PubliclyAccessible": false, "Encrypted": false, "ClusterSnapshotCopyStatus": { "DestinationRegion": "us-west-1", "RetentionPeriod": 15, "ManualSnapshotRetentionPeriod": -1 }, "Tags": [ { "Key": "mytags", "Value": "tag1" } ], "EnhancedVpcRouting": false, "IamRoles": [], "MaintenanceTrackName": "current", "DeferredMaintenanceWindows": [ { "DeferMaintenanceIdentifier": "dfm-mUdVSfDcT1F4SGhw6fyF", "DeferMaintenanceStartTime": "2019-12-10T18:18:39.354Z", "DeferMaintenanceEndTime": "2020-01-09T18:18:39.354Z" } ], "NextMaintenanceWindowStartTime": "2020-01-11T16:00:00Z" } }`For more information, see [Snapshot Schedule Format](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html#working-with-snapshot-scheduling)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [ModifySnapshotCopyRetentionPeriod](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-snapshot-copy-retention-period.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-snapshot-schedule`.

- **AWS CLI**
- 
            
                    **To modify snapshot schedule**The following `modify-snapshot-schedule`example modifies the rate of the specified snapshot schedule to every 10 hours.`aws redshift modify-snapshot-schedule \ --schedule-identifier``mysnapshotschedule`\ --schedule-definitions`"rate(10 hours)"`Output: `{ "ScheduleDefinitions": [ "rate(10 hours)" ], "ScheduleIdentifier": "mysnapshotschedule", "ScheduleDescription": "My schedule description", "Tags": [] }`For more information, see [Snapshot Schedule Format](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html#working-with-snapshot-scheduling)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [ModifySnapshotSchedule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-snapshot-schedule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `purchase-reserved-node-offering`.

- **AWS CLI**
- 
            
                    Purchase a Reserved NodeThis example shows how to purchase a reserved node offering. The `reserved-node-offering-id`is obtained by calling`describe-reserved-node-offerings`.Command:`aws redshift purchase-reserved-node-offering --reserved-node-offering-id ceb6a579-cf4c-4343-be8b-d832c45ab51c`Result: `{ "ReservedNode": { "OfferingType": "Heavy Utilization", "FixedPrice": "", "NodeType": "dw.hs1.xlarge", "ReservedNodeId": "1ba8e2e3-bc01-4d65-b35d-a4a3e931547e", "UsagePrice": "", "RecurringCharges": [ { "RecurringChargeAmount": "", "RecurringChargeFrequency": "Hourly" } ], "NodeCount": 1, "State": "payment-pending", "StartTime": "2013-02-13T17:08:39.051Z", "Duration": 31536000, "ReservedNodeOfferingId": "ceb6a579-cf4c-4343-be8b-d832c45ab51c" }, "ResponseMetadata": { "RequestId": "01bda7bf-7600-11e2-b605-2568d7396e7f" } }`- 
                    For API details, see [PurchaseReservedNodeOffering](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/purchase-reserved-node-offering.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reboot-cluster`.

- **AWS CLI**
- 
            
                    Reboot a ClusterThis example reboots a cluster. By default, the output is in JSON format.Command: `aws redshift reboot-cluster --cluster-identifier mycluster`Result: `{ "Cluster": { "NodeType": "dw.hs1.xlarge", "Endpoint": { "Port": 5439, "Address": "mycluster.coqoarplqhsn.us-east-1.redshift.amazonaws.com" }, "ClusterVersion": "1.0", "PubliclyAccessible": "true", "MasterUsername": "adminuser", "ClusterParameterGroups": [ { "ParameterApplyStatus": "in-sync", "ParameterGroupName": "default.redshift-1.0" } ], "ClusterSecurityGroups": [ { "Status": "active", "ClusterSecurityGroupName": "default" } ], "AllowVersionUpgrade": true, "VpcSecurityGroups": \[], "AvailabilityZone": "us-east-1a", "ClusterCreateTime": "2013-01-22T21:59:29.559Z", "PreferredMaintenanceWindow": "sun:23:15-mon:03:15", "AutomatedSnapshotRetentionPeriod": 1, "ClusterStatus": "rebooting", "ClusterIdentifier": "mycluster", "DBName": "dev", "NumberOfNodes": 2, "PendingModifiedValues": {} }, "ResponseMetadata": { "RequestId": "61c8b564-64e8-11e2-8f7d-3b939af52818" } }`- 
                    For API details, see [RebootCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/reboot-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reset-cluster-parameter-group`.

- **AWS CLI**
- 
            
                    Reset Parameters in a Parameter GroupThis example shows how to reset all of the parameters in a parameter group.Command: `aws redshift reset-cluster-parameter-group --parameter-group-name myclusterparametergroup --reset-all-parameters`- 
                    For API details, see [ResetClusterParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/reset-cluster-parameter-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `resize-cluster`.

- **AWS CLI**
- 
            
                    **To resize cluster**The following `resize-cluster`example resizes the specified cluster.`aws redshift resize-cluster \ --cluster-identifier``mycluster`\ --cluster-type`multi-node`\ --node-type`dc2.large`\ --number-of-nodes`6`\ --classicOutput: `{ "Cluster": { "ClusterIdentifier": "mycluster", "NodeType": "dc2.large", "ClusterStatus": "resizing", "ClusterAvailabilityStatus": "Modifying", "MasterUsername": "adminuser", "DBName": "dev", "Endpoint": { "Address": "mycluster.cmeaswqeuae.us-west-2.redshift.amazonaws.com", "Port": 5439 }, "ClusterCreateTime": "2019-12-05T18:44:36.991Z", "AutomatedSnapshotRetentionPeriod": 3, "ManualSnapshotRetentionPeriod": -1, "ClusterSecurityGroups": [], "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sh-a1a123ab", "Status": "active" } ], "ClusterParameterGroups": [ { "ParameterGroupName": "default.redshift-1.0", "ParameterApplyStatus": "in-sync" } ], "ClusterSubnetGroupName": "default", "VpcId": "vpc-a1abc1a1", "AvailabilityZone": "us-west-2f", "PreferredMaintenanceWindow": "sat:16:00-sat:16:30", "PendingModifiedValues": { "NodeType": "dc2.large", "NumberOfNodes": 6, "ClusterType": "multi-node" }, "ClusterVersion": "1.0", "AllowVersionUpgrade": true, "NumberOfNodes": 4, "PubliclyAccessible": false, "Encrypted": false, "ClusterSnapshotCopyStatus": { "DestinationRegion": "us-west-1", "RetentionPeriod": 15, "ManualSnapshotRetentionPeriod": -1 }, "Tags": [ { "Key": "mytags", "Value": "tag1" } ], "EnhancedVpcRouting": false, "IamRoles": [], "MaintenanceTrackName": "current", "DeferredMaintenanceWindows": [ { "DeferMaintenanceIdentifier": "dfm-mUdVCfDcT1B4SGhw6fyF", "DeferMaintenanceStartTime": "2019-12-10T18:18:39.354Z", "DeferMaintenanceEndTime": "2020-01-09T18:18:39.354Z" } ], "NextMaintenanceWindowStartTime": "2020-01-11T16:00:00Z", "ResizeInfo": { "ResizeType": "ClassicResize", "AllowCancelResize": true } } }`For more information, see [Resizing a Cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#cluster-resize-intro)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [ResizeCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/resize-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `restore-from-cluster-snapshot`.

- **AWS CLI**
- 
            
                    Restore a Cluster From a SnapshotThis example restores a cluster from a snapshot.Command: `aws redshift restore-from-cluster-snapshot --cluster-identifier mycluster-clone --snapshot-identifier my-snapshot-id`Result: `{ "Cluster": { "NodeType": "dw.hs1.xlarge", "ClusterVersion": "1.0", "PubliclyAccessible": "true", "MasterUsername": "adminuser", "ClusterParameterGroups": [ { "ParameterApplyStatus": "in-sync", "ParameterGroupName": "default.redshift-1.0" } ], "ClusterSecurityGroups": [ { "Status": "active", "ClusterSecurityGroupName": "default" } ], "AllowVersionUpgrade": true, "VpcSecurityGroups": \[], "PreferredMaintenanceWindow": "sun:23:15-mon:03:15", "AutomatedSnapshotRetentionPeriod": 1, "ClusterStatus": "creating", "ClusterIdentifier": "mycluster-clone", "DBName": "dev", "NumberOfNodes": 2, "PendingModifiedValues": {} }, "ResponseMetadata": { "RequestId": "77fd512b-64e3-11e2-8f5b-e90bd6c77476" } }`- 
                    For API details, see [RestoreFromClusterSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/restore-from-cluster-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `restore-table-from-cluster-snapshot`.

- **AWS CLI**
- 
            
                    **To restore table from a cluster snapshot**The following `restore-table-from-cluster-snapshot`example creates a new table from the specified table in the specified cluster snapshot.`aws redshift restore-table-from-cluster-snapshot``/`--cluster-identifier`mycluster``/`--snapshot-identifier`mycluster-2019-11-19-16-17``/`--source-database-name`dev``/`--source-schema-name`public``/`--source-table-name`mytable``/`--target-database-name`dev``/`--target-schema-name`public``/`--new-table-name`mytable-clone`Output: `{ "TableRestoreStatus": { "TableRestoreRequestId": "a123a12b-abc1-1a1a-a123-a1234ab12345", "Status": "PENDING", "RequestTime": "2019-12-20T00:20:16.402Z", "ClusterIdentifier": "mycluster", "SnapshotIdentifier": "mycluster-2019-11-19-16-17", "SourceDatabaseName": "dev", "SourceSchemaName": "public", "SourceTableName": "mytable", "TargetDatabaseName": "dev", "TargetSchemaName": "public", "NewTableName": "mytable-clone" } }`For more information, see [Restoring a Table from a Snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html#working-with-snapshot-restore-table-from-snapshot)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [RestoreTableFromClusterSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/restore-table-from-cluster-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `revoke-cluster-security-group-ingress`.

- **AWS CLI**
- 
            
                    Revoke Access from an EC2 Security GroupThis example revokes access to a named Amazon EC2 security group.Command: `aws redshift revoke-cluster-security-group-ingress --cluster-security-group-name mysecuritygroup --ec2-security-group-name myec2securitygroup --ec2-security-group-owner-id 123445677890`Revoking Access to a CIDR rangeThis example revokes access to a CIDR range.Command: `aws redshift revoke-cluster-security-group-ingress --cluster-security-group-name mysecuritygroup --cidrip 192.168.100.100/32`- 
                    For API details, see [RevokeClusterSecurityGroupIngress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/revoke-cluster-security-group-ingress.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `revoke-snapshot-access`.

- **AWS CLI**
- 
            
                    Revoke the Authorization of an AWS Account to Restore a SnapshotThis example revokes the authorization of the AWS account `444455556666`to restore the snapshot`my-snapshot-id`. By default, the output is in JSON format.Command:`aws redshift revoke-snapshot-access --snapshot-id my-snapshot-id --account-with-restore-access 444455556666`Result: `{ "Snapshot": { "Status": "available", "SnapshotCreateTime": "2013-07-17T22:04:18.947Z", "EstimatedSecondsToCompletion": 0, "AvailabilityZone": "us-east-1a", "ClusterVersion": "1.0", "MasterUsername": "adminuser", "Encrypted": false, "OwnerAccount": "111122223333", "BackupProgressInMegabytes": 11.0, "ElapsedTimeInSeconds": 0, "DBName": "dev", "CurrentBackupRateInMegabytesPerSecond: 0.1534, "ClusterCreateTime": "2013-01-22T21:59:29.559Z", "ActualIncrementalBackupSizeInMegabytes"; 11.0, "SnapshotType": "manual", "NodeType": "dw.hs1.xlarge", "ClusterIdentifier": "mycluster", "TotalBackupSizeInMegabytes": 20.0, "Port": 5439, "NumberOfNodes": 2, "SnapshotIdentifier": "my-snapshot-id" } }`- 
                    For API details, see [RevokeSnapshotAccess](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/revoke-snapshot-access.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `rotate-encryption-key`.

- **AWS CLI**
- 
            
                    **To rotate encryption key for a cluster**The following `rotate-encryption-key`example rotates the encryption key for the specified cluster.`aws redshift rotate-encryption-key \ --cluster-identifier``mycluster`Output: `{ "Cluster": { "ClusterIdentifier": "mycluster", "NodeType": "dc2.large", "ClusterStatus": "rotating-keys", "ClusterAvailabilityStatus": "Modifying", "MasterUsername": "adminuser", "DBName": "dev", "Endpoint": { "Address": "mycluster.cmeaswqeuae.us-west-2.redshift.amazonaws.com", "Port": 5439 }, "ClusterCreateTime": "2019-12-10T19:25:45.886Z", "AutomatedSnapshotRetentionPeriod": 30, "ManualSnapshotRetentionPeriod": -1, "ClusterSecurityGroups": [], "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sh-a1a123ab", "Status": "active" } ], "ClusterParameterGroups": [ { "ParameterGroupName": "default.redshift-1.0", "ParameterApplyStatus": "in-sync" } ], "ClusterSubnetGroupName": "default", "VpcId": "vpc-a1abc1a1", "AvailabilityZone": "us-west-2a", "PreferredMaintenanceWindow": "sat:16:00-sat:16:30", "PendingModifiedValues": {}, "ClusterVersion": "1.0", "AllowVersionUpgrade": true, "NumberOfNodes": 2, "PubliclyAccessible": false, "Encrypted": true, "Tags": [], "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/bPxRfih3yCo8nvbEXAMPLEKEY", "EnhancedVpcRouting": false, "IamRoles": [ { "IamRoleArn": "arn:aws:iam::123456789012:role/myRedshiftRole", "ApplyStatus": "in-sync" } ], "MaintenanceTrackName": "current", "DeferredMaintenanceWindows": [], "NextMaintenanceWindowStartTime": "2019-12-14T16:00:00Z" } }`For more information, see [Amazon Redshift Database Encryption](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html)in the*Amazon Redshift Cluster Management Guide*.- 
                    For API details, see [RotateEncryptionKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/rotate-encryption-key.html)in*AWS CLI Command Reference*.
 
-