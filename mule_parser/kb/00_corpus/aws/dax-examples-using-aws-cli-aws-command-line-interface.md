# DAX examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_dax_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_dax_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with DAX.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-cluster`.

- **AWS CLI**
- 
            
                    **To create a DAX cluster**The following `create-cluster`example creates a DAX cluster with the specified settings.`aws dax create-cluster \ --cluster-name``daxcluster`\ --node-type`dax.r4.large`\ --replication-factor`3`\ --iam-role-arn`roleARN`\ --sse-specification`Enabled=true`Output: `{ "Cluster": { "ClusterName": "daxcluster", "ClusterArn": "arn:aws:dax:us-west-2:123456789012:cache/daxcluster", "TotalNodes": 3, "ActiveNodes": 0, "NodeType": "dax.r4.large", "Status": "creating", "ClusterDiscoveryEndpoint": { "Port": 8111 }, "PreferredMaintenanceWindow": "thu:13:00-thu:14:00", "SubnetGroup": "default", "SecurityGroups": [ { "SecurityGroupIdentifier": "sg-1af6e36e", "Status": "active" } ], "IamRoleArn": "arn:aws:iam::123456789012:role/DAXServiceRoleForDynamoDBAccess", "ParameterGroup": { "ParameterGroupName": "default.dax1.0", "ParameterApplyStatus": "in-sync", "NodeIdsToReboot": [] }, "SSEDescription": { "Status": "ENABLED" } } }`For more information, see [Step 3: Create a DAX Cluster](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.create-cluster.cli.create-cluster.html)in the*Amazon DynamoDB Developer Guide*.- 
                    For API details, see [CreateCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/create-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-parameter-group`.

- **AWS CLI**
- 
            
                    **To create a parameter group**The following `` create-parameter-group`` example creates a parameter group with the specified settings. `aws dax create-parameter-group \ --parameter-group-name``daxparametergroup`\ --description`"A new parameter group"`Output: `{ "ParameterGroup": { "ParameterGroupName": "daxparametergroup", "Description": "A new parameter group" } }`For more information, see [Managing DAX Clusters](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.cluster-management.html#DAX.cluster-management.custom-settings.ttl)in the*Amazon DynamoDB Developer Guide*.- 
                    For API details, see [CreateParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/create-parameter-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-subnet-group`.

- **AWS CLI**
- 
            
                    **To create a DAX subnet group**The following `create-subnet-group`example creates a subnet group with the specified settings.`aws dax create-subnet-group \ --subnet-group-name``daxSubnetGroup`\ --subnet-ids`subnet-11111111``subnet-22222222`Output: `{ "SubnetGroup": { "SubnetGroupName": "daxSubnetGroup", "VpcId": "vpc-05a1fa8e00c325226", "Subnets": [ { "SubnetIdentifier": "subnet-11111111", "SubnetAvailabilityZone": "us-west-2b" }, { "SubnetIdentifier": "subnet-22222222", "SubnetAvailabilityZone": "us-west-2c" } ] } }`For more information, see [Step 2: Create a Subnet Group](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.create-cluster.cli.create-subnet-group.html)in the*Amazon DynamoDB Developer Guide*.- 
                    For API details, see [CreateSubnetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/create-subnet-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `decrease-replication-factor`.

- **AWS CLI**
- 
            
                    **To remove one or more nodes from the cluster**The following `decrease-replication-factor`example decreases the number of nodes in the specified DAX cluster to one.`aws dax decrease-replication-factor \ --cluster-name``daxcluster`\ --new-replication-factor`1`Output: `{ "Cluster": { "ClusterName": "daxcluster", "ClusterArn": "arn:aws:dax:us-west-2:123456789012:cache/daxcluster", "TotalNodes": 3, "ActiveNodes": 3, "NodeType": "dax.r4.large", "Status": "modifying", "ClusterDiscoveryEndpoint": { "Address": "daxcluster.ey3o9d.clustercfg.dax.usw2.cache.amazonaws.com", "Port": 8111 }, "Nodes": [ { "NodeId": "daxcluster-a", "Endpoint": { "Address": "daxcluster-a.ey3o9d.0001.dax.usw2.cache.amazonaws.com", "Port": 8111 }, "NodeCreateTime": 1576625059.509, "AvailabilityZone": "us-west-2c", "NodeStatus": "available", "ParameterGroupStatus": "in-sync" }, { "NodeId": "daxcluster-b", "Endpoint": { "Address": "daxcluster-b.ey3o9d.0001.dax.usw2.cache.amazonaws.com", "Port": 8111 }, "NodeCreateTime": 1576625059.509, "AvailabilityZone": "us-west-2a", "NodeStatus": "available", "ParameterGroupStatus": "in-sync" }, { "NodeId": "daxcluster-c", "Endpoint": { "Address": "daxcluster-c.ey3o9d.0001.dax.usw2.cache.amazonaws.com", "Port": 8111 }, "NodeCreateTime": 1576625059.509, "AvailabilityZone": "us-west-2b", "NodeStatus": "available", "ParameterGroupStatus": "in-sync" } ], "PreferredMaintenanceWindow": "thu:13:00-thu:14:00", "SubnetGroup": "default", "SecurityGroups": [ { "SecurityGroupIdentifier": "sg-1af6e36e", "Status": "active" } ], "IamRoleArn": "arn:aws:iam::123456789012:role/DAXServiceRoleForDynamoDBAccess", "ParameterGroup": { "ParameterGroupName": "default.dax1.0", "ParameterApplyStatus": "in-sync", "NodeIdsToReboot": [] }, "SSEDescription": { "Status": "ENABLED" } } }`For more information, see [Managing DAX Clusters](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.cluster-management.html#DAX.cluster-management.custom-settings)in the*Amazon DynamoDB Developer Guide*.- 
                    For API details, see [DecreaseReplicationFactor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/decrease-replication-factor.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-cluster`.

- **AWS CLI**
- 
            
                    **To delete a DAX cluster**The following `delete-cluster`example deletes the specified DAX cluster.`aws dax delete-cluster \ --cluster-name``daxcluster`Output: `{ "Cluster": { "ClusterName": "daxcluster", "ClusterArn": "arn:aws:dax:us-west-2:123456789012:cache/daxcluster", "TotalNodes": 3, "ActiveNodes": 0, "NodeType": "dax.r4.large", "Status": "deleting", "ClusterDiscoveryEndpoint": { "Address": "dd.ey3o9d.clustercfg.dax.usw2.cache.amazonaws.com", "Port": 8111 }, "PreferredMaintenanceWindow": "fri:06:00-fri:07:00", "SubnetGroup": "default", "SecurityGroups": [ { "SecurityGroupIdentifier": "sg-1af6e36e", "Status": "active" } ], "IamRoleArn": "arn:aws:iam::123456789012:role/DAXServiceRoleForDynamoDBAccess", "ParameterGroup": { "ParameterGroupName": "default.dax1.0", "ParameterApplyStatus": "in-sync", "NodeIdsToReboot": [] }, "SSEDescription": { "Status": "ENABLED" } } }`For more information, see [Managing DAX Clusters](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.cluster-management.html#DAX.cluster-management.deleting)in the*Amazon DynamoDB Developer Guide*.- 
                    For API details, see [DeleteCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/delete-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-parameter-group`.

- **AWS CLI**
- 
            
                    **To delete a parameter group**The following `delete-parameter-group`example deletes the specified DAX parameter group.`aws dax delete-parameter-group \ --parameter-group-name``daxparametergroup`Output: `{ "DeletionMessage": "Parameter group daxparametergroup has been deleted." }`For more information, see [Managing DAX Clusters](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.cluster-management.html)in the*Amazon DynamoDB Developer Guide*.- 
                    For API details, see [DeleteParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/delete-parameter-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-subnet-group`.

- **AWS CLI**
- 
            
                    **To delete a subnet group**The following `delete-subnet-group`example deletes the specified DAX subnet group.`aws dax delete-subnet-group \ --subnet-group-name``daxSubnetGroup`Output: `{ "DeletionMessage": "Subnet group daxSubnetGroup has been deleted." }`For more information, see [Managing DAX Clusters](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.cluster-management.html)in the*Amazon DynamoDB Developer Guide*.- 
                    For API details, see [DeleteSubnetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/delete-subnet-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-clusters`.

- **AWS CLI**
- 
            
                    **To return information about all provisioned DAX clusters**The following `describe-clusters`example displays details about all provisioned DAX clusters.`aws dax describe-clusters`Output: `{ "Clusters": [ { "ClusterName": "daxcluster", "ClusterArn": "arn:aws:dax:us-west-2:123456789012:cache/daxcluster", "TotalNodes": 1, "ActiveNodes": 1, "NodeType": "dax.r4.large", "Status": "available", "ClusterDiscoveryEndpoint": { "Address": "daxcluster.ey3o9d.clustercfg.dax.usw2.cache.amazonaws.com", "Port": 8111 }, "Nodes": [ { "NodeId": "daxcluster-a", "Endpoint": { "Address": "daxcluster-a.ey3o9d.0001.dax.usw2.cache.amazonaws.com", "Port": 8111 }, "NodeCreateTime": 1576625059.509, "AvailabilityZone": "us-west-2c", "NodeStatus": "available", "ParameterGroupStatus": "in-sync" } ], "PreferredMaintenanceWindow": "thu:13:00-thu:14:00", "SubnetGroup": "default", "SecurityGroups": [ { "SecurityGroupIdentifier": "sg-1af6e36e", "Status": "active" } ], "IamRoleArn": "arn:aws:iam::123456789012:role/DAXServiceRoleForDynamoDBAccess", "ParameterGroup": { "ParameterGroupName": "default.dax1.0", "ParameterApplyStatus": "in-sync", "NodeIdsToReboot": [] }, "SSEDescription": { "Status": "ENABLED" } } ] }`For more information, see [Managing DAX Clusters](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.cluster-management.html)in the*Amazon DynamoDB Developer Guide*.- 
                    For API details, see [DescribeClusters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/describe-clusters.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-default-parameters`.

- **AWS CLI**
- 
            
                    **To return the default system parameter information for DAX**The following `describe-default-parameters`example displays the default system parameter information for DAX.`aws dax describe-default-parameters`Output: `{ "Parameters": [ { "ParameterName": "query-ttl-millis", "ParameterType": "DEFAULT", "ParameterValue": "300000", "NodeTypeSpecificValues": [], "Description": "Duration in milliseconds for queries to remain cached", "Source": "user", "DataType": "integer", "AllowedValues": "0-", "IsModifiable": "TRUE", "ChangeType": "IMMEDIATE" }, { "ParameterName": "record-ttl-millis", "ParameterType": "DEFAULT", "ParameterValue": "300000", "NodeTypeSpecificValues": [], "Description": "Duration in milliseconds for records to remain valid in cache (Default: 0 = infinite)", "Source": "user", "DataType": "integer", "AllowedValues": "0-", "IsModifiable": "TRUE", "ChangeType": "IMMEDIATE" } ] }`For more information, see [Managing DAX Clusters](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.cluster-management.html)in the*Amazon DynamoDB Developer Guide*.- 
                    For API details, see [DescribeDefaultParameters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/describe-default-parameters.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-events`.

- **AWS CLI**
- 
            
                    **To return all events related to DAX clusters and parameter groups**The following `describe-events`example displays details of events that are related to DAX clusters and parameter groups.`aws dax describe-events`Output: `{ "Events": [ { "SourceName": "daxcluster", "SourceType": "CLUSTER", "Message": "Cluster deleted.", "Date": 1576702736.706 }, { "SourceName": "daxcluster", "SourceType": "CLUSTER", "Message": "Removed node daxcluster-b.", "Date": 1576702691.738 }, { "SourceName": "daxcluster", "SourceType": "CLUSTER", "Message": "Removed node daxcluster-a.", "Date": 1576702633.498 }, { "SourceName": "daxcluster", "SourceType": "CLUSTER", "Message": "Removed node daxcluster-c.", "Date": 1576702631.329 }, { "SourceName": "daxcluster", "SourceType": "CLUSTER", "Message": "Cluster created.", "Date": 1576626560.057 } ] }`For more information, see [Managing DAX Clusters](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.cluster-management.html)in the*Amazon DynamoDB Developer Guide*.- 
                    For API details, see [DescribeEvents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/describe-events.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-parameter-groups`.

- **AWS CLI**
- 
            
                    **To describe the parameter groups defined in DAX**The following `describe-parameter-groups`example retrieves details about the parameter groups that are defined in DAX.`aws dax describe-parameter-groups`Output: `{ "ParameterGroups": [ { "ParameterGroupName": "default.dax1.0", "Description": "Default parameter group for dax1.0" } ] }`For more information, see [Managing DAX Clusters](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.cluster-management.html)in the*Amazon DynamoDB Developer Guide*.- 
                    For API details, see [DescribeParameterGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/describe-parameter-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-parameters`.

- **AWS CLI**
- 
            
                    **To describe the parameters defined in a DAX parameter group**The following `describe-parameters`example retrieves details about the parameters that are defined in the specified DAX parameter group.`aws dax describe-parameters \ --parameter-group-name``default.dax1.0`Output: `{ "Parameters": [ { "ParameterName": "query-ttl-millis", "ParameterType": "DEFAULT", "ParameterValue": "300000", "NodeTypeSpecificValues": [], "Description": "Duration in milliseconds for queries to remain cached", "Source": "user", "DataType": "integer", "AllowedValues": "0-", "IsModifiable": "TRUE", "ChangeType": "IMMEDIATE" }, { "ParameterName": "record-ttl-millis", "ParameterType": "DEFAULT", "ParameterValue": "300000", "NodeTypeSpecificValues": [], "Description": "Duration in milliseconds for records to remain valid in cache (Default: 0 = infinite)", "Source": "user", "DataType": "integer", "AllowedValues": "0-", "IsModifiable": "TRUE", "ChangeType": "IMMEDIATE" } ] }`For more information, see [Managing DAX Clusters](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.cluster-management.html)in the*Amazon DynamoDB Developer Guide*.- 
                    For API details, see [DescribeParameters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/describe-parameters.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-subnet-groups`.

- **AWS CLI**
- 
            
                    **To describe subnet groups defined in DAX**The following `describe-subnet-groups`example retrieves details for the subnet groups defined in DAX.`aws dax describe-subnet-groups`Output: `{ "SubnetGroups": [ { "SubnetGroupName": "default", "Description": "Default CacheSubnetGroup", "VpcId": "vpc-ee70a196", "Subnets": [ { "SubnetIdentifier": "subnet-874953af", "SubnetAvailabilityZone": "us-west-2d" }, { "SubnetIdentifier": "subnet-bd3d1fc4", "SubnetAvailabilityZone": "us-west-2a" }, { "SubnetIdentifier": "subnet-72c2ff28", "SubnetAvailabilityZone": "us-west-2c" }, { "SubnetIdentifier": "subnet-09e6aa42", "SubnetAvailabilityZone": "us-west-2b" } ] } ] }`For more information, see [Managing DAX Clusters](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.concepts.cluster.html#DAX.concepts.cluster.security)in the*Amazon DynamoDB Developer Guide*.- 
                    For API details, see [DescribeSubnetGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/describe-subnet-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `increase-replication-factor`.

- **AWS CLI**
- 
            
                    **To increase the replication factor for a DAX cluster**The following `increase-replication-factor`example increases the specified DAX cluster's replication factor to 3.`aws dax increase-replication-factor \ --cluster-name``daxcluster`\ --new-replication-factor`3`Output: `{ "Cluster": { "ClusterName": "daxcluster", "ClusterArn": "arn:aws:dax:us-west-2:123456789012:cache/daxcluster", "TotalNodes": 3, "ActiveNodes": 1, "NodeType": "dax.r4.large", "Status": "modifying", "ClusterDiscoveryEndpoint": { "Address": "daxcluster.ey3o9d.clustercfg.dax.usw2.cache.amazonaws.com", "Port": 8111 }, "Nodes": [ { "NodeId": "daxcluster-a", "Endpoint": { "Address": "daxcluster-a.ey3o9d.0001.dax.usw2.cache.amazonaws.com", "Port": 8111 }, "NodeCreateTime": 1576625059.509, "AvailabilityZone": "us-west-2c", "NodeStatus": "available", "ParameterGroupStatus": "in-sync" }, { "NodeId": "daxcluster-b", "NodeStatus": "creating" }, { "NodeId": "daxcluster-c", "NodeStatus": "creating" } ], "PreferredMaintenanceWindow": "thu:13:00-thu:14:00", "SubnetGroup": "default", "SecurityGroups": [ { "SecurityGroupIdentifier": "sg-1af6e36e", "Status": "active" } ], "IamRoleArn": "arn:aws:iam::123456789012:role/DAXServiceRoleForDynamoDBAccess", "ParameterGroup": { "ParameterGroupName": "default.dax1.0", "ParameterApplyStatus": "in-sync", "NodeIdsToReboot": [] }, "SSEDescription": { "Status": "ENABLED" } } }`For more information, see [Managing DAX Clusters](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.cluster-management.html#DAX.cluster-management.custom-settings)in the*Amazon DynamoDB Developer Guide*.- 
                    For API details, see [IncreaseReplicationFactor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/increase-replication-factor.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags`.

- **AWS CLI**
- 
            
                    **To list tags on a DAX resource**The following `list-tags`example lists the tag keys and values attached to the specified DAX cluster.`aws dax list-tags \ --resource-name``arn:aws:dax:us-west-2:123456789012:cache/daxcluster`Output: `{ "Tags": [ { "Key": "ClusterUsage", "Value": "prod" } ] }`For more information, see [Managing DAX Clusters](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.cluster-management.html#DAX.management.tagging)in the*Amazon DynamoDB Developer Guide*.- 
                    For API details, see [ListTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/list-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To tag a DAX resource**The following `tag-resource`example attaches the specified tag key name and associated value to the specified DAX cluster to describe the cluster usage.`aws dax tag-resource \ --resource-name``arn:aws:dax:us-west-2:123456789012:cache/daxcluster`\ --tags="Key=ClusterUsage,Value=prod"Output: `{ "Tags": [ { "Key": "ClusterUsage", "Value": "prod" } ] }`For more information, see [Managing DAX Clusters](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.cluster-management.html#DAX.management.tagging)in the*Amazon DynamoDB Developer Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove tags from a DAX resource**The following `untag-resource`example removes the tag with the specified key name from a DAX cluster.`aws dax untag-resource \ --resource-name``arn:aws:dax:us-west-2:123456789012:cache/daxcluster`\ --tag-keys="ClusterUsage"Output: `{ "Tags": [] }`For more information, see [Managing DAX Clusters](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.cluster-management.html#DAX.management.tagging)in the*Amazon DynamoDB Developer Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dax/untag-resource.html)in*AWS CLI Command Reference*.
 
-