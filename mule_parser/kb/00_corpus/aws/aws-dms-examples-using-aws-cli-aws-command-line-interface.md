# AWS DMS examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_database-migration-service_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_database-migration-service_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS DMS.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `add-tags-to-resource`.

- **AWS CLI**
- 
            
                    **To add tags to a resource**The following `add-tags-to-resource`example adds tags to a replication instance.`aws dms add-tags-to-resource \ --resource-arn``arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE`\ --tags`Key=Environment,Value=PROD``Key=Project,Value=dbMigration`This command produces no output. For more information, see [Tagging Resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tagging.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [AddTagsToResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/add-tags-to-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-endpoint`.

- **AWS CLI**
- 
            
                    **To create an endpoint**The following `create-endpoint`example creates an endpoint for an Amazon S3 source.`aws dms create-endpoint \ --endpoint-type``source`\ --engine-name`s3`\ --endpoint-identifier`src-endpoint`\ --s3-settings`file://s3-settings.json`Contents of `s3-settings.json`:`{ "BucketName":"my-corp-data", "BucketFolder":"sourcedata", "ServiceAccessRoleArn":"arn:aws:iam::123456789012:role/my-s3-access-role" }`Output: `{ "Endpoint": { "EndpointIdentifier": "src-endpoint", "EndpointType": "SOURCE", "EngineName": "s3", "EngineDisplayName": "Amazon S3", "ExtraConnectionAttributes": "bucketFolder=sourcedata;bucketName=my-corp-data;compressionType=NONE;csvDelimiter=,;csvRowDelimiter=\\n;", "Status": "active", "EndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:GUVAFG34EECUOJ6QVZ56DAHT3U", "SslMode": "none", "ServiceAccessRoleArn": "arn:aws:iam::123456789012:role/my-s3-access-role", "S3Settings": { "ServiceAccessRoleArn": "arn:aws:iam::123456789012:role/my-s3-access-role", "CsvRowDelimiter": "\\n", "CsvDelimiter": ",", "BucketFolder": "sourcedata", "BucketName": "my-corp-data", "CompressionType": "NONE", "EnableStatistics": true } } }`For more information, see [Working with AWS DMS Endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [CreateEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-event-subscription`.

- **AWS CLI**
- 
            
                    **To list event subscriptions**The following `create-event-subscription`example creates an event subscription to an Amazon SNS topic (my-sns-topic).`aws dms create-event-subscription \ --subscription-name``my-dms-events`\ --sns-topic-arn`arn:aws:sns:us-east-1:123456789012:my-sns-topic`Output: `{ "EventSubscription": { "CustomerAwsId": "123456789012", "CustSubscriptionId": "my-dms-events", "SnsTopicArn": "arn:aws:sns:us-east-1:123456789012:my-sns-topic", "Status": "creating", "SubscriptionCreationTime": "2020-05-21 21:58:38.598", "Enabled": true } }`For more information, see [Working with Events and Notifications](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [CreateEventSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-event-subscription.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-replication-instance`.

- **AWS CLI**
- 
            
                    **To create a replication instance**The following `create-replication-instance`example creates a replication instance.`aws dms create-replication-instance \ --replication-instance-identifier``my-repl-instance`\ --replication-instance-class`dms.t2.micro`\ --allocated-storage`5`Output: `{ "ReplicationInstance": { "ReplicationInstanceIdentifier": "my-repl-instance", "ReplicationInstanceClass": "dms.t2.micro", "ReplicationInstanceStatus": "creating", "AllocatedStorage": 5, "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sg-f839b688", "Status": "active" } ], "ReplicationSubnetGroup": { "ReplicationSubnetGroupIdentifier": "default", "ReplicationSubnetGroupDescription": "default", "VpcId": "vpc-136a4c6a", "SubnetGroupStatus": "Complete", "Subnets": [ { "SubnetIdentifier": "subnet-da327bf6", "SubnetAvailabilityZone": { "Name": "us-east-1a" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-42599426", "SubnetAvailabilityZone": { "Name": "us-east-1d" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-bac383e0", "SubnetAvailabilityZone": { "Name": "us-east-1c" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-6746046b", "SubnetAvailabilityZone": { "Name": "us-east-1f" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-d7c825e8", "SubnetAvailabilityZone": { "Name": "us-east-1e" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-cbfff283", "SubnetAvailabilityZone": { "Name": "us-east-1b" }, "SubnetStatus": "Active" } ] }, "PreferredMaintenanceWindow": "sat:12:35-sat:13:05", "PendingModifiedValues": {}, "MultiAZ": false, "EngineVersion": "3.3.2", "AutoMinorVersionUpgrade": true, "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/f7bc0f8e-1a3a-4ace-9faa-e8494fa3921a", "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:ZK2VQBUWFDBAWHIXHAYG5G2PKY", "PubliclyAccessible": true } }`For more information, see [Working with an AWS DMS Replication Instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [CreateReplicationInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-replication-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-replication-subnet-group`.

- **AWS CLI**
- 
            
                    **To create a subnet group**The following `create-replication-subnet-group`example creates a group consisting of 3 subnets.`aws dms create-replication-subnet-group \ --replication-subnet-group-identifier``my-subnet-group`\ --replication-subnet-group-description`"my subnet group"`\ --subnet-ids`subnet-da327bf6``subnet-bac383e0``subnet-d7c825e8`Output: `{ "ReplicationSubnetGroup": { "ReplicationSubnetGroupIdentifier": "my-subnet-group", "ReplicationSubnetGroupDescription": "my subnet group", "VpcId": "vpc-136a4c6a", "SubnetGroupStatus": "Complete", "Subnets": [ { "SubnetIdentifier": "subnet-da327bf6", "SubnetAvailabilityZone": { "Name": "us-east-1a" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-bac383e0", "SubnetAvailabilityZone": { "Name": "us-east-1c" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-d7c825e8", "SubnetAvailabilityZone": { "Name": "us-east-1e" }, "SubnetStatus": "Active" } ] } }`For more information, see [Setting Up a Network for a Replication Instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.VPC.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [CreateReplicationSubnetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-replication-subnet-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-replication-task`.

- **AWS CLI**
- 
            
                    **To create a replication task**The following `create-replication-task`example creates a replication task.`aws dms create-replication-task \ --replication-task-identifier``movedata`\ --source-endpoint-arn`arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA`\ --target-endpoint-arn`arn:aws:dms:us-east-1:123456789012:endpoint:EOM4SFKCZEYHZBFGAGZT3QEC5U`\ --replication-instance-arn`$RI_ARN`\ --migration-type`full-load`\ --table-mappings`file://table-mappings.json`Contents of `table-mappings.json`:`{ "rules": [ { "rule-type": "selection", "rule-id": "1", "rule-name": "1", "object-locator": { "schema-name": "prodrep", "table-name": "%" }, "rule-action": "include", "filters": [] } ] }`Output: `{ "ReplicationTask": { "ReplicationTaskIdentifier": "moveit2", "SourceEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA", "TargetEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:EOM4SFKCZEYHZBFGAGZT3QEC5U", "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE", "MigrationType": "full-load", "TableMappings": ...output omitted... , "ReplicationTaskSettings": ...output omitted... , "Status": "creating", "ReplicationTaskCreationDate": 1590524772.505, "ReplicationTaskArn": "arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII" } }`For more information, see [Working with AWS DMS Tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [CreateReplicationTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/create-replication-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-connection`.

- **AWS CLI**
- 
            
                    **To delete a connection**The following `delete-connection`example disassociates an endpoint from a replication instance.`aws dms delete-connection \ --endpoint-arn``arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA`\ --replication-instance-arn`arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE`Output: `{ "Connection": { "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE", "EndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA", "Status": "deleting", "EndpointIdentifier": "src-database-1", "ReplicationInstanceIdentifier": "my-repl-instance" } }`For more information, see [https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.Creating.html](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.Creating.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [DeleteConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-connection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-endpoint`.

- **AWS CLI**
- 
            
                    **To delete an endpoint**The following `delete-endpoint`example deletes an endpoint.`aws dms delete-endpoint \ --endpoint-arn``arn:aws:dms:us-east-1:123456789012:endpoint:OUJJVXO4XZ4CYTSEG5XGMN2R3Y`Output: `{ "Endpoint": { "EndpointIdentifier": "src-endpoint", "EndpointType": "SOURCE", "EngineName": "s3", "EngineDisplayName": "Amazon S3", "ExtraConnectionAttributes": "bucketFolder=sourcedata;bucketName=my-corp-data;compressionType=NONE;csvDelimiter=,;csvRowDelimiter=\\n;", "Status": "deleting", "EndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:OUJJVXO4XZ4CYTSEG5XGMN2R3Y", "SslMode": "none", "ServiceAccessRoleArn": "arn:aws:iam::123456789012:role/my-s3-access-role", "S3Settings": { "ServiceAccessRoleArn": "arn:aws:iam::123456789012:role/my-s3-access-role", "CsvRowDelimiter": "\\n", "CsvDelimiter": ",", "BucketFolder": "sourcedata", "BucketName": "my-corp-data", "CompressionType": "NONE", "EnableStatistics": true } } }`For more information, see [Working with AWS DMS Endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [DeleteEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-event-subscription`.

- **AWS CLI**
- 
            
                    **To delete an event subscription**The following `delete-event-subscription`example deletes a subscription to an Amazon SNS topic.`aws dms delete-event-subscription \ --subscription-name``"my-dms-events"`Output: `{ "EventSubscription": { "CustomerAwsId": "123456789012", "CustSubscriptionId": "my-dms-events", "SnsTopicArn": "arn:aws:sns:us-east-1:123456789012:my-sns-topic", "Status": "deleting", "SubscriptionCreationTime": "2020-05-21 21:58:38.598", "Enabled": true } }`For more information, see [Working with Events and Notifications](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [DeleteEventSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-event-subscription.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-replication-instance`.

- **AWS CLI**
- 
            
                    **To delete a replication instance**The following `delete-replication-instance`example deletes a replication instance.`aws dms delete-replication-instance \ --replication-instance-arn``arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE`Output: `{ "ReplicationInstance": { "ReplicationInstanceIdentifier": "my-repl-instance", "ReplicationInstanceClass": "dms.t2.micro", "ReplicationInstanceStatus": "deleting", "AllocatedStorage": 5, "InstanceCreateTime": 1590011235.952, "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sg-f839b688", "Status": "active" } ], "AvailabilityZone": "us-east-1e", "ReplicationSubnetGroup": { "ReplicationSubnetGroupIdentifier": "default", "ReplicationSubnetGroupDescription": "default", "VpcId": "vpc-136a4c6a", "SubnetGroupStatus": "Complete", "Subnets": [ { "SubnetIdentifier": "subnet-da327bf6", "SubnetAvailabilityZone": { "Name": "us-east-1a" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-42599426", "SubnetAvailabilityZone": { "Name": "us-east-1d" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-bac383e0", "SubnetAvailabilityZone": { "Name": "us-east-1c" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-6746046b", "SubnetAvailabilityZone": { "Name": "us-east-1f" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-d7c825e8", "SubnetAvailabilityZone": { "Name": "us-east-1e" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-cbfff283", "SubnetAvailabilityZone": { "Name": "us-east-1b" }, "SubnetStatus": "Active" } ] }, "PreferredMaintenanceWindow": "wed:11:42-wed:12:12", "PendingModifiedValues": {}, "MultiAZ": true, "EngineVersion": "3.3.2", "AutoMinorVersionUpgrade": true, "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/f7bc0f8e-1a3a-4ace-9faa-e8494fa3921a", "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE", "ReplicationInstancePublicIpAddress": "54.225.120.92", "ReplicationInstancePrivateIpAddress": "172.31.30.121", "ReplicationInstancePublicIpAddresses": [ "54.225.120.92", "3.230.18.248" ], "ReplicationInstancePrivateIpAddresses": [ "172.31.30.121", "172.31.75.90" ], "PubliclyAccessible": true, "SecondaryAvailabilityZone": "us-east-1b" } }`For more information, see [Working with an AWS DMS Replication Instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [DeleteReplicationInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-replication-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-replication-subnet-group`.

- **AWS CLI**
- 
            
                    **To delete a subnet group**The following `delete-replication-subnet-group`example deletes a subnet group.`aws dms delete-replication-subnet-group \ --replication-subnet-group-identifier``my-subnet-group`Output: `(none)`For more information, see [Setting Up a Network for a Replication Instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.VPC.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [DeleteReplicationSubnetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-replication-subnet-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-replication-task`.

- **AWS CLI**
- 
            
                    **To delete a replication task**The following `delete-replication-task`example deletes a replication task.`aws dms delete-replication-task \ --replication-task-arn``arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII`Output: `{ "ReplicationTask": { "ReplicationTaskIdentifier": "moveit2", "SourceEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA", "TargetEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:EOM4SFKCZEYHZBFGAGZT3QEC5U", "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE", "MigrationType": "full-load", "TableMappings": ...output omitted..., "ReplicationTaskSettings": ...output omitted..., "Status": "deleting", "StopReason": "Stop Reason FULL_LOAD_ONLY_FINISHED", "ReplicationTaskCreationDate": 1590524772.505, "ReplicationTaskStartDate": 1590789988.677, "ReplicationTaskArn": "arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII" } }`For more information, see [Working with AWS DMS Tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [DeleteReplicationTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/delete-replication-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-account-attributes`.

- **AWS CLI**
- 
            
                    **To describe account attributes**The following `describe-account-attributes`example lists the attributes for your AWS account.`aws dms describe-account-attributes`Output: `{ "AccountQuotas": [ { "AccountQuotaName": "ReplicationInstances", "Used": 1, "Max": 20 }, { "AccountQuotaName": "AllocatedStorage", "Used": 5, "Max": 10000 }, ...remaining output omitted... ], "UniqueAccountIdentifier": "cqahfbfy5xee" }`- 
                    For API details, see [DescribeAccountAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-account-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-certificates`.

- **AWS CLI**
- 
            
                    **To list the available certificates**The following `describe-certificates`example lists the available certificates in your AWS account.`aws dms describe-certificates`Output: `{ "Certificates": [ { "CertificateIdentifier": "my-cert", "CertificateCreationDate": 1543259542.506, "CertificatePem": "-----BEGIN CERTIFICATE-----\nMIID9DCCAtygAwIBAgIBQjANBgkqhkiG9w0BAQ ...U" ... remaining output omittted ... } ] }`For more information, see [Using SSL](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#CHAP_Security.SSL)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [DescribeCertificates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-certificates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-connections`.

- **AWS CLI**
- 
            
                    **To describe connections**The following `describe-connections`example lists the connections that you have tested between a replication instance and an endpoint.`aws dms describe-connections`Output: `{ "Connections": [ { "Status": "successful", "ReplicationInstanceIdentifier": "test", "EndpointArn": "arn:aws:dms:us-east-arn:aws:dms:us-east-1:123456789012:endpoint:ZW5UAN6P4E77EC7YWHK4RZZ3BE", "EndpointIdentifier": "testsrc1", "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:6UTDJGBOUS3VI3SUWA66XFJCJQ" } ] }`For more information, see [Creating Source and Target Endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.Creating.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [DescribeConnections](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-connections.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-endpoint-types`.

- **AWS CLI**
- 
            
                    **To list the available endpoint types**The following `describe-endpoint-types`example lists the MySQL endpoint types that are available.`aws dms describe-endpoint-types \ --filters``"Name=engine-name,Values=mysql"`Output: `{ "SupportedEndpointTypes": [ { "EngineName": "mysql", "SupportsCDC": true, "EndpointType": "source", "EngineDisplayName": "MySQL" }, { "EngineName": "mysql", "SupportsCDC": true, "EndpointType": "target", "EngineDisplayName": "MySQL" } ] }`For more information, see Working with AWS DMS Endpoints <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.html>`__ in the *AWS Database Migration Service User Guide*.- 
                    For API details, see [DescribeEndpointTypes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-endpoint-types.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-endpoints`.

- **AWS CLI**
- 
            
                    **To describe endpoints**The following `describe-endpoints`example lists the endpoints in your AWS account.`aws dms describe-endpoints`Output: `{ "Endpoints": [ { "Username": "dms", "Status": "active", "EndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:SF2WOFLWYWKVEOHID2EKLP3SJI", "ServerName": "ec2-52-32-48-61.us-west-2.compute.amazonaws.com", "EndpointType": "SOURCE", "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/94d5c4e7-4e4c-44be-b58a-c8da7adf57cd", "DatabaseName": "test", "EngineName": "mysql", "EndpointIdentifier": "pri100", "Port": 8193 }, { "Username": "admin", "Status": "active", "EndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:TJJZCIH3CJ24TJRU4VC32WEWFR", "ServerName": "test.example.com", "EndpointType": "SOURCE", "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/2431021b-1cf2-a2d4-77b2-59a9e4bce323", "DatabaseName": "EMPL", "EngineName": "oracle", "EndpointIdentifier": "test", "Port": 1521 } ] }`For more information, see [Working with AWS DMS Endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [DescribeEndpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-endpoints.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-event-categories`.

- **AWS CLI**
- 
            
                    **To describe event categories**The following `describe-event-categories`example lists the available event categories.`aws dms describe-event-categories`Output: `{ "EventCategoryGroupList": [ { "SourceType": "replication-instance", "EventCategories": [ "low storage", "configuration change", "maintenance", "deletion", "creation", "failover", "failure" ] }, { "SourceType": "replication-task", "EventCategories": [ "configuration change", "state change", "deletion", "creation", "failure" ] } ] }`For more information, see [Working with Events and Notifications](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [DescribeEventCategories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-event-categories.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-event-subscriptions`.

- **AWS CLI**
- 
            
                    **To describe event subscriptions**The following `describe-event-subscriptions`example lists the event subscriptions to an Amazon SNS topic.`aws dms describe-event-subscriptions`Output: `{ "EventSubscriptionsList": [ { "CustomerAwsId": "123456789012", "CustSubscriptionId": "my-dms-events", "SnsTopicArn": "arn:aws:sns:us-east-1:123456789012:my-sns-topic", "Status": "deleting", "SubscriptionCreationTime": "2020-05-21 22:28:51.924", "Enabled": true } ] }`For more information, see [Working with Events and Notifications](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [DescribeEventSubscriptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-event-subscriptions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-events`.

- **AWS CLI**
- 
            
                    **To list DMS events**The following `describe-events`example lists the events that originated from a replication instance.`aws dms describe-events \ --source-type``"replication-instance"`Output: `{ "Events": [ { "SourceIdentifier": "my-repl-instance", "SourceType": "replication-instance", "Message": "Replication application shutdown", "EventCategories": [], "Date": 1590771645.776 } ] }`For more information, see [Working with Events and Notifications](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [DescribeEvents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-events.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-orderable-replication-instances`.

- **AWS CLI**
- 
            
                    **To describe orderable replication instances**The following `describe-orderable-replication-instances`example lists replication instance types that you can order.`aws dms describe-orderable-replication-instances`Output: `{ "OrderableReplicationInstances": [ { "EngineVersion": "3.3.2", "ReplicationInstanceClass": "dms.c4.2xlarge", "StorageType": "gp2", "MinAllocatedStorage": 5, "MaxAllocatedStorage": 6144, "DefaultAllocatedStorage": 100, "IncludedAllocatedStorage": 100, "AvailabilityZones": [ "us-east-1a", "us-east-1b", "us-east-1c", "us-east-1d", "us-east-1e", "us-east-1f" ] }, { "EngineVersion": "3.3.2", "ReplicationInstanceClass": "dms.c4.4xlarge", "StorageType": "gp2", "MinAllocatedStorage": 5, "MaxAllocatedStorage": 6144, "DefaultAllocatedStorage": 100, "IncludedAllocatedStorage": 100, "AvailabilityZones": [ "us-east-1a", "us-east-1b", "us-east-1c", "us-east-1d", "us-east-1e", "us-east-1f" ] }, ...remaining output omitted... }`For more information, see [Working with an AWS DMS Replication Instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [DescribeOrderableReplicationInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-orderable-replication-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-refresh-schemas-status`.

- **AWS CLI**
- 
            
                    **To list the refresh status for an endpoint**The following `describe-refresh-schemas-status`example returns the status of a previous refresh request.`aws dms describe-refresh-schemas-status \ --endpoint-arn``arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA`Output: `{ "RefreshSchemasStatus": { "EndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA", "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE", "Status": "successful", "LastRefreshDate": 1590786544.605 } }`- 
                    For API details, see [DescribeRefreshSchemasStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-refresh-schemas-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-replication-instances`.

- **AWS CLI**
- 
            
                    **To describe replication instances**The following `describe-replication-instances`example lists the replication instances in your AWS account.`aws dms describe-replication-instances`Output: `{ "ReplicationInstances": [ { "ReplicationInstanceIdentifier": "my-repl-instance", "ReplicationInstanceClass": "dms.t2.micro", "ReplicationInstanceStatus": "available", "AllocatedStorage": 5, "InstanceCreateTime": 1590011235.952, "VpcSecurityGroups": [ { "VpcSecurityGroupId": "sg-f839b688", "Status": "active" } ], "AvailabilityZone": "us-east-1e", "ReplicationSubnetGroup": { "ReplicationSubnetGroupIdentifier": "default", "ReplicationSubnetGroupDescription": "default", "VpcId": "vpc-136a4c6a", "SubnetGroupStatus": "Complete", "Subnets": [ { "SubnetIdentifier": "subnet-da327bf6", "SubnetAvailabilityZone": { "Name": "us-east-1a" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-42599426", "SubnetAvailabilityZone": { "Name": "us-east-1d" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-bac383e0", "SubnetAvailabilityZone": { "Name": "us-east-1c" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-6746046b", "SubnetAvailabilityZone": { "Name": "us-east-1f" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-d7c825e8", "SubnetAvailabilityZone": { "Name": "us-east-1e" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-cbfff283", "SubnetAvailabilityZone": { "Name": "us-east-1b" }, "SubnetStatus": "Active" } ] }, "PreferredMaintenanceWindow": "wed:11:42-wed:12:12", "PendingModifiedValues": { "MultiAZ": true }, "MultiAZ": false, "EngineVersion": "3.3.2", "AutoMinorVersionUpgrade": true, "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/f7bc0f8e-1a3a-4ace-9faa-e8494fa3921a", "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE", "ReplicationInstancePublicIpAddress": "3.230.18.248", "ReplicationInstancePrivateIpAddress": "172.31.75.90", "ReplicationInstancePublicIpAddresses": [ "3.230.18.248" ], "ReplicationInstancePrivateIpAddresses": [ "172.31.75.90" ], "PubliclyAccessible": true, "FreeUntil": 1590194829.267 } ] }`For more information, see [Working with an AWS DMS Replication Instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [DescribeReplicationInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-replication-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-replication-subnet-groups`.

- **AWS CLI**
- 
            
                    **To display the available subnet groups**The following `describe-replication-subnet-groups`example lists the available subnet groups.`aws dms describe-replication-subnet-groups \ --filter``"Name=replication-subnet-group-id,Values=my-subnet-group"`Output: `{ "ReplicationSubnetGroups": [ { "ReplicationSubnetGroupIdentifier": "my-subnet-group", "ReplicationSubnetGroupDescription": "my subnet group", "VpcId": "vpc-136a4c6a", "SubnetGroupStatus": "Complete", "Subnets": [ { "SubnetIdentifier": "subnet-da327bf6", "SubnetAvailabilityZone": { "Name": "us-east-1a" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-bac383e0", "SubnetAvailabilityZone": { "Name": "us-east-1c" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-d7c825e8", "SubnetAvailabilityZone": { "Name": "us-east-1e" }, "SubnetStatus": "Active" } ] } ] }`For more information, see [Setting Up a Network for a Replication Instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.VPC.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [DescribeReplicationSubnetGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-replication-subnet-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-replication-task-assessment-results`.

- **AWS CLI**
- 
            
                    **To list the results of replication task assessmentss**The following `describe-replication-task-assessment-results`example lists the results of a prior task assesssment.`aws dms describe-replication-task-assessment-results`Output: `{ "ReplicationTaskAssessmentResults": [ { "ReplicationTaskIdentifier": "moveit2", "ReplicationTaskArn": "arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII", "ReplicationTaskLastAssessmentDate": 1590790230.0, "AssessmentStatus": "No issues found", "AssessmentResultsFile": "moveit2/2020-05-29-22-10" } ] }`For more information, see [Creating a Task Assessment Report](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.AssessmentReport.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [DescribeReplicationTaskAssessmentResults](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-replication-task-assessment-results.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-replication-tasks`.

- **AWS CLI**
- 
            
                    **To describe a replication task**The following `describe-replication-tasks`example describes current replication tasks.`aws dms describe-replication-tasks`Output: `{ "ReplicationTasks": [ { "ReplicationTaskIdentifier": "moveit2", "SourceEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA", "TargetEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:EOM4SFKCZEYHZBFGAGZT3QEC5U", "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE", "MigrationType": "full-load", "TableMappings": ...output omitted... , "ReplicationTaskSettings": ...output omitted... , "Status": "stopped", "StopReason": "Stop Reason FULL_LOAD_ONLY_FINISHED", "ReplicationTaskCreationDate": 1590524772.505, "ReplicationTaskStartDate": 1590619805.212, "ReplicationTaskArn": "arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII", "ReplicationTaskStats": { "FullLoadProgressPercent": 100, "ElapsedTimeMillis": 0, "TablesLoaded": 0, "TablesLoading": 0, "TablesQueued": 0, "TablesErrored": 0, "FreshStartDate": 1590619811.528, "StartDate": 1590619811.528, "StopDate": 1590619842.068 } } ] }`For more information, see [Working with AWS DMS Tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [DescribeReplicationTasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-replication-tasks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-schemas`.

- **AWS CLI**
- 
            
                    **To describe database schemas**The following `describe-schemas`example lists the available tables at an endpoint.`aws dms describe-schemas \ --endpoint-arn``"arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA"`Output: `{ "Schemas": [ "prodrep" ] }`For more information, see [This is the topic title](https://link.to.the/topic/page)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [DescribeSchemas](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-schemas.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list the tags for a resource**The following `list-tags-for-resource`example lists the tags for a replication instance.`aws dms list-tags-for-resource \ --resource-arn``arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE`Output: `{ "TagList": [ { "Key": "Project", "Value": "dbMigration" }, { "Key": "Environment", "Value": "PROD" } ] }`For more information, see [Tagging Resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tagging.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-endpoint`.

- **AWS CLI**
- 
            
                    **To modify an endpoint**The following `modify-endpoint`example adds an extra connection attribute to an endpoint.`aws dms modify-endpoint \ --endpoint-arn``"arn:aws:dms:us-east-1:123456789012:endpoint:GUVAFG34EECUOJ6QVZ56DAHT3U"`\ --extra-connection-attributes`"compressionType=GZIP"`Output: `{ "Endpoint": { "EndpointIdentifier": "src-endpoint", "EndpointType": "SOURCE", "EngineName": "s3", "EngineDisplayName": "Amazon S3", "ExtraConnectionAttributes": "compressionType=GZIP;csvDelimiter=,;csvRowDelimiter=\\n;", "Status": "active", "EndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:GUVAFG34EECUOJ6QVZ56DAHT3U", "SslMode": "none", "ServiceAccessRoleArn": "arn:aws:iam::123456789012:role/my-s3-access-role", "S3Settings": { "ServiceAccessRoleArn": "arn:aws:iam::123456789012:role/my-s3-access-role", "CsvRowDelimiter": "\\n", "CsvDelimiter": ",", "BucketFolder": "", "BucketName": "", "CompressionType": "GZIP", "EnableStatistics": true } } }`For more information, see Working with AWS DMS Endpoints <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.html>`__ in the *AWS Database Migration Service User Guide*.- 
                    For API details, see [ModifyEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-event-subscription`.

- **AWS CLI**
- 
            
                    **To modify an event subscription**The following `modify-event-subscription`example changes the source type of an event subscription.`aws dms modify-event-subscription \ --subscription-name``"my-dms-events"`\ --source-type`replication-task`Output: `{ "EventSubscription": { "CustomerAwsId": "123456789012", "CustSubscriptionId": "my-dms-events", "SnsTopicArn": "arn:aws:sns:us-east-1:123456789012:my-sns-topic", "Status": "modifying", "SubscriptionCreationTime": "2020-05-29 17:04:40.262", "SourceType": "replication-task", "Enabled": true } }`For more information, see [Working with Events and Notifications](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [ModifyEventSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-event-subscription.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-replication-instance`.

- **AWS CLI**
- 
            
                    **To modify a replication instance**The following `modify-replication-instance`example modifies a replication instance so that it uses a Multi-AZ deployment.`aws dms modify-replication-instance \ --replication-instance-arn``arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE`\ --multi-azOutput: `{ "ReplicationInstance": { "ReplicationInstanceIdentifier": "my-repl-instance", "ReplicationInstanceClass": "dms.t2.micro", "ReplicationInstanceStatus": "available", "AllocatedStorage": 5, "InstanceCreateTime": 1590011235.952, ...output omitted... "PendingModifiedValues": { "MultiAZ": true }, "MultiAZ": false, "EngineVersion": "3.3.2", "AutoMinorVersionUpgrade": true, "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/f7bc0f8e-1a3a-4ace-9faa-e8494fa3921a", ...output omitted... } }`For more information, see [Working with an AWS DMS Replication Instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [ModifyReplicationInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-replication-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-replication-subnet-group`.

- **AWS CLI**
- 
            
                    **To modify a subnet group**The following `modify-replication-subnet-group`example changes the lists of subnets associated with a subnet group.`aws dms modify-replication-subnet-group \ --replication-subnet-group-identifier``my-subnet-group`\ --subnet-id`subnet-da327bf6``subnet-bac383e0`Output: `{ "ReplicationSubnetGroup": { "ReplicationSubnetGroupIdentifier": "my-subnet-group", "ReplicationSubnetGroupDescription": "my subnet group", "VpcId": "vpc-136a4c6a", "SubnetGroupStatus": "Complete", "Subnets": [ { "SubnetIdentifier": "subnet-da327bf6", "SubnetAvailabilityZone": { "Name": "us-east-1a" }, "SubnetStatus": "Active" }, { "SubnetIdentifier": "subnet-bac383e0", "SubnetAvailabilityZone": { "Name": "us-east-1c" }, "SubnetStatus": "Active" } ] } }`For more information, see [Setting Up a Network for a Replication Instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.VPC.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [ModifyReplicationSubnetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-replication-subnet-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-replication-task`.

- **AWS CLI**
- 
            
                    **To modify a replication task**The following `modify-replication-task`example changes the table mappings for a task.`aws dms modify-replication-task \ --replication-task-arn``"arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII"`\ --table-mappings`file://table-mappings.json`Contents of `table-mappings.json`:`{ "rules": [ { "rule-type": "selection", "rule-id": "1", "rule-name": "1", "object-locator": { "schema-name": "prodrep", "table-name": "ACCT_%" }, "rule-action": "include", "filters": [] } ] }`Output: `{ "ReplicationTask": { "ReplicationTaskIdentifier": "moveit2", "SourceEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA", "TargetEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:EOM4SFKCZEYHZBFGAGZT3QEC5U", "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE", "MigrationType": "full-load", "TableMappings": ...output omitted..., "ReplicationTaskSettings": ...output omitted..., "Status": "modifying", "StopReason": "Stop Reason FULL_LOAD_ONLY_FINISHED", "ReplicationTaskCreationDate": 1590524772.505, "ReplicationTaskStartDate": 1590789424.653, "ReplicationTaskArn": "arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII" } }`For more information, see [Working with AWS DMS Tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [ModifyReplicationTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-replication-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reboot-replication-instance`.

- **AWS CLI**
- 
            
                    **To reboot a replication instance**The following `reboot-replication-instance`example reboots a replication instance.`aws dms reboot-replication-instance \ --replication-instance-arn``arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE`Output: `{ "ReplicationInstance": { "ReplicationInstanceIdentifier": "my-repl-instance", "ReplicationInstanceClass": "dms.t2.micro", "ReplicationInstanceStatus": "rebooting", "AllocatedStorage": 5, "InstanceCreateTime": 1590011235.952, ... output omitted ... } }`For more information, see [Working with an AWS DMS Replication Instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [RebootReplicationInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/reboot-replication-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `refresh-schemas`.

- **AWS CLI**
- 
            
                    **To refresh database schemas**The following `refresh-schemas`example requests that AWS DMS refresh the list of schemas at an endpoint.`aws dms refresh-schemas \ --replication-instance-arn``arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE`\ --endpoint-arn`"arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA"`Output: `{ "RefreshSchemasStatus": { "EndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA", "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE", "Status": "refreshing", "LastRefreshDate": 1590019949.103 } }`- 
                    For API details, see [RefreshSchemas](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/refresh-schemas.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reload-tables`.

- **AWS CLI**
- 
            
                    **To refresh the list of tables available at an endpoint**The following `reload-tables`example reloads the list of available tables at an endpoint.`aws dms reload-tables \ --replication-task-arn``"arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII"`\ --tables-to-reload`"SchemaName=prodrep,TableName=ACCT_BAL"`Output: `{ "ReplicationTaskArn": "arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII" }`- 
                    For API details, see [ReloadTables](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/reload-tables.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-tags-from-resource`.

- **AWS CLI**
- 
            
                    **To remove tags from a replication instance**The following `remove-tags-from-resource`example removes tags from a replication instance.`aws dms remove-tags-from-resource \ --resource-arn``arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE`\ --tag-keys`Environment``Project`This command produces no output. For more information, see [Tagging Resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tagging.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [RemoveTagsFromResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/remove-tags-from-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-replication-task-assessment`.

- **AWS CLI**
- 
            
                    **To start a task assessment**The following `start-replication-task-assessment`example starts a replication task assessment.`aws dms start-replication-task-assessment \ --replication-task-arn``arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII`Output: `{ "ReplicationTask": { "ReplicationTaskIdentifier": "moveit2", "SourceEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA", "TargetEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:EOM4SFKCZEYHZBFGAGZT3QEC5U", "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE", "MigrationType": "full-load", "TableMappings": ...output omitted..., "ReplicationTaskSettings": ...output omitted..., "Status": "testing", "StopReason": "Stop Reason FULL_LOAD_ONLY_FINISHED", "ReplicationTaskCreationDate": 1590524772.505, "ReplicationTaskStartDate": 1590789988.677, "ReplicationTaskArn": "arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII" } }`For more information, see [Creating a Task Assessment Report](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.AssessmentReport.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [StartReplicationTaskAssessment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/start-replication-task-assessment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-replication-task`.

- **AWS CLI**
- 
            
                    **To start a replication task**The following `command-name`example lists the available widgets in your AWS account.`aws dms start-replication-task \ --replication-task-arn``arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII`\ --start-replication-task-type`reload-target`Output: `{ "ReplicationTask": { "ReplicationTaskIdentifier": "moveit2", "SourceEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA", "TargetEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:EOM4SFKCZEYHZBFGAGZT3QEC5U", "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE", "MigrationType": "full-load", "TableMappings": ...output omitted... , "ReplicationTaskSettings": ...output omitted... , "Status": "starting", "ReplicationTaskCreationDate": 1590524772.505, "ReplicationTaskStartDate": 1590619805.212, "ReplicationTaskArn": "arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII" } }`For more information, see [Working with AWS DMS Tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [StartReplicationTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/start-replication-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-replication-task`.

- **AWS CLI**
- 
            
                    **To stop a task**The following `stop-replication-task`example stops a task.`aws dms stop-replication-task \ --replication-task-arn``arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII`Output: `{ "ReplicationTask": { "ReplicationTaskIdentifier": "moveit2", "SourceEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA", "TargetEndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:EOM4SFKCZEYHZBFGAGZT3QEC5U", "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE", "MigrationType": "full-load", "TableMappings": ...output omitted..., "ReplicationTaskSettings": ...output omitted..., "Status": "stopping", "ReplicationTaskCreationDate": 1590524772.505, "ReplicationTaskStartDate": 1590789424.653, "ReplicationTaskArn": "arn:aws:dms:us-east-1:123456789012:task:K55IUCGBASJS5VHZJIINA45FII" } }`For more information, see [Working with AWS DMS Tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [StopReplicationTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/stop-replication-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `test-connection`.

- **AWS CLI**
- 
            
                    **To test a connection to an endpoint**The following `test-connection`example tests whether an endpoint can be accessed from a replication instance.`aws dms test-connection \ --replication-instance-arn``arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE`\ --endpoint-arn`arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA`Output: `{ "Connection": { "ReplicationInstanceArn": "arn:aws:dms:us-east-1:123456789012:rep:T3OM7OUB5NM2LCVZF7JPGJRNUE", "EndpointArn": "arn:aws:dms:us-east-1:123456789012:endpoint:6GGI6YPWWGAYUVLKIB732KEVWA", "Status": "testing", "EndpointIdentifier": "src-database-1", "ReplicationInstanceIdentifier": "my-repl-instance" } }`For more information, see [Creating source and target endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.Creating.html)in the*AWS Database Migration Service User Guide*.- 
                    For API details, see [TestConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/test-connection.html)in*AWS CLI Command Reference*.
 
-