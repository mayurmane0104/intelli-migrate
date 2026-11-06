# MemoryDB examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_memorydb_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_memorydb_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with MemoryDB.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `copy-snapshot`.

- **AWS CLI**
- 
            
                    **To copy a snapshot**The following `copy-snapshot`example creates a copy of a snapshot.`aws memorydb copy-snapshot \ --source-snapshot-name``my-cluster-snapshot`\ --target-snapshot-name`my-cluster-snapshot-copy`Output `{ "Snapshot": { "Name": "my-cluster-snapshot-copy", "Status": "creating", "Source": "manual", "ARN": "arn:aws:memorydb:us-east-1:491658xxxxxx:snapshot/my-cluster-snapshot-copy", "ClusterConfiguration": { "Name": "my-cluster", "Description": " ", "NodeType": "db.r6g.large", "EngineVersion": "6.2", "MaintenanceWindow": "wed:03:00-wed:04:00", "Port": 6379, "ParameterGroupName": "default.memorydb-redis6", "SubnetGroupName": "my-sg", "VpcId": "vpc-xx2574fc", "SnapshotRetentionLimit": 0, "SnapshotWindow": "04:30-05:30", "NumShards": 2 } } }`For more information, see [Copying a snapshot](https://docs.aws.amazon.com/memorydb/latest/devguide/snapshots-copying.html)in the*MemoryDB User Guide*.- 
                    For API details, see [CopySnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/copy-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-acl`.

- **AWS CLI**
- 
            
                    **To create an ACL**The following `create-acl`example creates a new Access control list.`aws memorydb create-acl \ --acl-name``"new-acl-1"`\ --user-names`"my-user"`Output: `{ "ACL": { "Name": "new-acl-1", "Status": "creating", "UserNames": [ "my-user" ], "MinimumEngineVersion": "6.2", "Clusters": [], "ARN": "arn:aws:memorydb:us-east-1:491658xxxxxx:acl/new-acl-1" } }`For more information, see [Authenticating users with Access Control Lists](https://docs.aws.amazon.com/memorydb/latest/devguide/clusters.acls.html)in the*MemoryDB User Guide*.- 
                    For API details, see [CreateAcl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/create-acl.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-cluster`.

- **AWS CLI**
- 
            
                    **To create a cluster**The following `create-cluster`example creates a new cluster.`aws memorydb create-cluster \ --cluster-name``my-new-cluster`\ --node-type`db.r6g.large`\ --acl-name`my-acl`\ --subnet-group`my-sg`Output: `{ "Cluster": { "Name": "my-new-cluster", "Status": "creating", "NumberOfShards": 1, "AvailabilityMode": "MultiAZ", "ClusterEndpoint": { "Port": 6379 }, "NodeType": "db.r6g.large", "EngineVersion": "6.2", "EnginePatchVersion": "6.2.6", "ParameterGroupName": "default.memorydb-redis6", "ParameterGroupStatus": "in-sync", "SubnetGroupName": "my-sg", "TLSEnabled": true, "ARN": "arn:aws:memorydb:us-east-1:49165xxxxxx:cluster/my-new-cluster", "SnapshotRetentionLimit": 0, "MaintenanceWindow": "sat:10:00-sat:11:00", "SnapshotWindow": "07:30-08:30", "ACLName": "my-acl", "AutoMinorVersionUpgrade": true } }`For more information, see [Managing Clusters](https://docs.aws.amazon.com/memorydb/latest/devguide/clusters.html)in the*MemoryDB User Guide*.- 
                    For API details, see [CreateCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/create-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-parameter-group`.

- **AWS CLI**
- 
            
                    **To create a parameter group**The following `create-parameter-group`example creates a parameter group.`aws memorydb create-parameter-group \ --parameter-group-name``myRedis6x`\ --family`memorydb_redis6`\ --description`"my-parameter-group"`Output: `{ "ParameterGroup": { "Name": "myredis6x", "Family": "memorydb_redis6", "Description": "my-parameter-group", "ARN": "arn:aws:memorydb:us-east-1:49165xxxxxx:parametergroup/myredis6x" } }`For more information, see [Creating a parameter group](https://docs.aws.amazon.com/memorydb/latest/devguide/parametergroups.creating.html)in the*MemoryDB User Guide*.- 
                    For API details, see [CreateParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/create-parameter-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-snapshot`.

- **AWS CLI**
- 
            
                    **To create a snapshot**The following `create-snapshot`example creates a snapshot.`aws memorydb create-snapshot \ --cluster-name``my-cluster`\ --snapshot-name`my-cluster-snapshot`Output: `{ "Snapshot": { "Name": "my-cluster-snapshot1", "Status": "creating", "Source": "manual", "ARN": "arn:aws:memorydb:us-east-1:49165xxxxxx:snapshot/my-cluster-snapshot", "ClusterConfiguration": { "Name": "my-cluster", "Description": "", "NodeType": "db.r6g.large", "EngineVersion": "6.2", "MaintenanceWindow": "wed:03:00-wed:04:00", "Port": 6379, "ParameterGroupName": "default.memorydb-redis6", "SubnetGroupName": "my-sg", "VpcId": "vpc-862xxxxc", "SnapshotRetentionLimit": 0, "SnapshotWindow": "04:30-05:30", "NumShards": 2 } } }`For more information, see [Making manual snapshots](https://docs.aws.amazon.com/memorydb/latest/devguide/snapshots-manual.html)in the*MemoryDB User Guide*.- 
                    For API details, see [CreateSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/create-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-subnet-group`.

- **AWS CLI**
- 
            
                    **To create a subnet group**The following `create-subnet-group`example creates a subnet group.`aws memorydb create-subnet-group \ --subnet-group-name``mysubnetgroup`\ --description`"my subnet group"`\ --subnet-ids`subnet-5623xxxx`Output: `{ "SubnetGroup": { "Name": "mysubnetgroup", "Description": "my subnet group", "VpcId": "vpc-86257xxx", "Subnets": [ { "Identifier": "subnet-5623xxxx", "AvailabilityZone": { "Name": "us-east-1a" } } ], "ARN": "arn:aws:memorydb:us-east-1:491658xxxxxx:subnetgroup/mysubnetgroup" } }`For more information, see [Creating a subnet group](https://docs.aws.amazon.com/memorydb/latest/devguide/subnetgroups.creating.html)in the*MemoryDB User Guide*.- 
                    For API details, see [CreateSubnetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/create-subnet-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-user`.

- **AWS CLI**
- 
            
                    **To create a user**The following `create-user`example creates a new user.`aws memorydb create-user \ --user-name``user-name-1`\ --access-string`"~objects:* ~items:* ~public:*"`\ --authentication-mode \ Passwords="enterapasswordhere",Type=passwordOutput: `{ "User": { "Name": "user-name-1", "Status": "active", "AccessString": "off ~objects:* ~items:* ~public:* resetchannels -@all", "ACLNames": [], "MinimumEngineVersion": "6.2", "Authentication": { "Type": "password", "PasswordCount": 1 }, "ARN": "arn:aws:memorydb:us-west-2:491658xxxxxx:user/user-name-1" } }`For more information, see [Authenticating users with Access Control Lists](https://docs.aws.amazon.com/memorydb/latest/devguide/clusters.acls.html)in the*MemoryDB User Guide*.- 
                    For API details, see [CreateUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/create-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-acl`.

- **AWS CLI**
- 
            
                    **To delete an ACL**The following `delete-acl`example deletes an Access control list.`aws memorydb delete-acl \ --acl-name``"new-acl-1"`Output: `{ "ACL": { "Name": "new-acl-1", "Status": "deleting", "UserNames": [ "pat" ], "MinimumEngineVersion": "6.2", "Clusters": [], "ARN": "arn:aws:memorydb:us-east-1:491658xxxxxx:acl/new-acl-1" } }`For more information, see [Authenticating users with Access Control Lists](https://docs.aws.amazon.com/memorydb/latest/devguide/clusters.acls.html)in the*MemoryDB User Guide*.- 
                    For API details, see [DeleteAcl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/delete-acl.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-cluster`.

- **AWS CLI**
- 
            
                    **To delete a cluster**The following `delete-cluster`example deletes a cluster.`aws memorydb delete-cluster \ --cluster-name``my-new-cluster`Output: `{ "Cluster": { "Name": "my-new-cluster", "Status": "deleting", "NumberOfShards": 1, "ClusterEndpoint": { "Address": "clustercfg.my-new-cluster.xxxxx.memorydb.us-east-1.amazonaws.com", "Port": 6379 }, "NodeType": "db.r6g.large", "EngineVersion": "6.2", "EnginePatchVersion": "6.2.6", "ParameterGroupName": "default.memorydb-redis6", "ParameterGroupStatus": "in-sync", "SubnetGroupName": "my-sg", "TLSEnabled": true, "ARN": "arn:aws:memorydb:us-east-1:491658xxxxxx:cluster/my-new-cluster", "SnapshotRetentionLimit": 0, "MaintenanceWindow": "sat:10:00-sat:11:00", "SnapshotWindow": "07:30-08:30", "AutoMinorVersionUpgrade": true } }`For more information, see [Deleting a cluster](https://docs.aws.amazon.com/memorydb/latest/devguide/clusters.delete.html)in the*MemoryDB User Guide*.- 
                    For API details, see [DeleteCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/delete-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-parameter-group`.

- **AWS CLI**
- 
            
                    **To delete a parameter group**The following `delete-parameter-group`example deletes a parameter group.`aws memorydb delete-parameter-group \ --parameter-group-name``myRedis6x`Output: `{ "ParameterGroup": { "Name": "myredis6x", "Family": "memorydb_redis6", "Description": "my-parameter-group", "ARN": "arn:aws:memorydb:us-east-1:491658xxxxxx:parametergroup/myredis6x" } }`For more information, see [Deleting a parameter group](https://docs.aws.amazon.com/memorydb/latest/devguide/parametergroups.deleting.html)in the*MemoryDB User Guide*.- 
                    For API details, see [DeleteParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/delete-parameter-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-snapshot`.

- **AWS CLI**
- 
            
                    **To delete a snapshot**The following `delete-snapshot`example deletes a snapshot.`aws memorydb delete-snapshot \ --snapshot-name``my-cluster-snapshot`Output: `{ "Snapshot": { "Name": "my-cluster-snapshot", "Status": "deleting", "Source": "manual", "ARN": "arn:aws:memorydb:us-east-1:49165xxxxxx:snapshot/my-cluster-snapshot", "ClusterConfiguration": { "Name": "my-cluster", "Description": "", "NodeType": "db.r6g.large", "EngineVersion": "6.2", "MaintenanceWindow": "wed:03:00-wed:04:00", "Port": 6379, "ParameterGroupName": "default.memorydb-redis6", "SubnetGroupName": "my-sg", "VpcId": "vpc-862xxxxc", "SnapshotRetentionLimit": 0, "SnapshotWindow": "04:30-05:30", "NumShards": 2 } } }`For more information, see [Deleting a snapshot](https://docs.aws.amazon.com/memorydb/latest/devguide/snapshots-deleting.html)in the*MemoryDB User Guide*.- 
                    For API details, see [DeleteSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/delete-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-subnet-group`.

- **AWS CLI**
- 
            
                    **To delete a subnet group**The following `delete-subnet-group`example deletes a subnet.`aws memorydb delete-subnet-group \ --subnet-group-name``mysubnetgroup`Output: `{ "SubnetGroup": { "Name": "mysubnetgroup", "Description": "my subnet group", "VpcId": "vpc-86xxxx4fc", "Subnets": [ { "Identifier": "subnet-56xxx61b", "AvailabilityZone": { "Name": "us-east-1a" } } ], "ARN": "arn:aws:memorydb:us-east-1:491658xxxxxx:subnetgroup/mysubnetgroup" } }`For more information, see [Deleting a subnet group](https://docs.aws.amazon.com/memorydb/latest/devguide/subnetgroups.deleting.html)in the*MemoryDB User Guide*.- 
                    For API details, see [DeleteSubnetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/delete-subnet-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-user`.

- **AWS CLI**
- 
            
                    **To delete a user**The following `delete-user`example deletes a user.`aws memorydb delete-user \ --user-name``my-user`Output: `{ "User": { "Name": "my-user", "Status": "deleting", "AccessString": "on ~app::* resetchannels -@all +@read", "ACLNames": [ "my-acl" ], "MinimumEngineVersion": "6.2", "Authentication": { "Type": "password", "PasswordCount": 1 }, "ARN": "arn:aws:memorydb:us-east-1:491658xxxxxx:user/my-user" } }`For more information, see [Authenticating users with Access Control Lists](https://docs.aws.amazon.com/memorydb/latest/devguide/clusters.acls.html)in the*MemoryDB User Guide*.- 
                    For API details, see [DeleteUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/delete-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-acls`.

- **AWS CLI**
- 
            
                    **To return a list of ACLs**The following describe-acls` returns a list of ACLs. `aws memorydb describe-acls`Output: `{ "ACLs": [ { "Name": "open-access", "Status": "active", "UserNames": [ "default" ], "MinimumEngineVersion": "6.2", "Clusters": [], "ARN": "arn:aws:memorydb:us-east-1:491658xxxxxx:acl/open-access" }, { "Name": my-acl", "Status": "active", "UserNames": [], "MinimumEngineVersion": "6.2", "Clusters": [ "my-cluster" ], "ARN": "arn:aws:memorydb:us-east-1:49165xxxxxxx:acl/my-acl" } ] }`For more information, see [Authenticating users with Access Control Lists](https://docs.aws.amazon.com/memorydb/latest/devguide/clusters.acls.html)in the*MemoryDB User Guide*.- 
                    For API details, see [DescribeAcls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/describe-acls.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-clusters`.

- **AWS CLI**
- 
            
                    **To return a list of clusters**The following describe-clusters` returns a list of clusters. `aws memorydb describe-clusters`Output: `{ "Clusters": [ { "Name": "my-cluster", "Status": "available", "NumberOfShards": 2, "ClusterEndpoint": { "Address": "clustercfg.my-cluster.llru6f.memorydb.us-east-1.amazonaws.com", "Port": 6379 }, "NodeType": "db.r6g.large", "EngineVersion": "6.2", "EnginePatchVersion": "6.2.6", "ParameterGroupName": "default.memorydb-redis6", "ParameterGroupStatus": "in-sync", "SecurityGroups": [ { "SecurityGroupId": "sg-0a1434xxxxxc9fae", "Status": "active" } ], "SubnetGroupName": "pat-sg", "TLSEnabled": true, "ARN": "arn:aws:memorydb:us-east-1:49165xxxxxx:cluster/my-cluster", "SnapshotRetentionLimit": 0, "MaintenanceWindow": "wed:03:00-wed:04:00", "SnapshotWindow": "04:30-05:30", "ACLName": "my-acl", "AutoMinorVersionUpgrade": true } ] }`For more information, see [Managing clusters](https://docs.aws.amazon.com/memorydb/latest/devguide/clusters.html)in the*MemoryDB User Guide*.- 
                    For API details, see [DescribeClusters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/describe-clusters.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-engine-versions`.

- **AWS CLI**
- 
            
                    **To return a list of engine versions**The following describe-engine-versions` returns a list of engine versions. `aws memorydb describe-engine-versions`Output: `{ "EngineVersions": [ { "EngineVersion": "6.2", "EnginePatchVersion": "6.2.6", "ParameterGroupFamily": "memorydb_redis6" } ] }`For more information, see [Engine versions and upgrading](https://docs.aws.amazon.com/memorydb/latest/devguide/engine-versions.htmll)in the*MemoryDB User Guide*.- 
                    For API details, see [DescribeEngineVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/describe-engine-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-events`.

- **AWS CLI**
- 
            
                    **To return a list of events**The following describe-events` returns a list of events. `aws memorydb describe-events`Output: `{ "Events": [ { "SourceName": "my-cluster", "SourceType": "cluster", "Message": "Increase replica count started for replication group my-cluster on 2022-07-22T14:09:01.440Z", "Date": "2022-07-22T07:09:01.443000-07:00" }, { "SourceName": "my-user", "SourceType": "user", "Message": "Create user my-user operation completed.", "Date": "2022-07-22T07:00:02.975000-07:00" } ] }`For more information, see [Monitoring events](https://docs.aws.amazon.com/memorydb/latest/devguide/monitoring-events.html)in the*MemoryDB User Guide*.- 
                    For API details, see [DescribeEvents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/describe-events.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-parameter-groups`.

- **AWS CLI**
- 
            
                    **To return a list of parameter groups**The following describe-parameter-groups` returns a list of parameter groups. `aws memorydb describe-parameter-groups`Output: `{ "ParameterGroups": [ { "Name": "default.memorydb-redis6", "Family": "memorydb_redis6", "Description": "Default parameter group for memorydb_redis6", "ARN": "arn:aws:memorydb:us-east-1:491658xxxxxx:parametergroup/default.memorydb-redis6" } ] }`For more information, see [Configuring engine parameters using parameter groups](https://docs.aws.amazon.com/memorydb/latest/devguide/parametergroups.html)in the*MemoryDB User Guide*.- 
                    For API details, see [DescribeParameterGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/describe-parameter-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-parameters`.

- **AWS CLI**
- 
            
                    **To return a list of parameters**The following `describe-parameters`returns a list of parameters.`aws memorydb describe-parameters \ --parameter-group-name``default.memorydb-redis6`Output: `{ "Parameters": [ { "Name": "acllog-max-len", "Value": "128", "Description": "The maximum length of the ACL Log", "DataType": "integer", "AllowedValues": "1-10000", "MinimumEngineVersion": "6.2.4" }, { "Name": "activedefrag", "Value": "no", "Description": "Enabled active memory defragmentation", "DataType": "string", "AllowedValues": "yes,no", "MinimumEngineVersion": "6.2.4" }, { "Name": "active-defrag-cycle-max", "Value": "75", "Description": "Maximal effort for defrag in CPU percentage", "DataType": "integer", "AllowedValues": "1-75", "MinimumEngineVersion": "6.2.4" }, { "Name": "active-defrag-cycle-min", "Value": "5", "Description": "Minimal effort for defrag in CPU percentage", "DataType": "integer", "AllowedValues": "1-75", "MinimumEngineVersion": "6.2.4" }, { "Name": "active-defrag-ignore-bytes", "Value": "104857600", "Description": "Minimum amount of fragmentation waste to start active defrag", "DataType": "integer", "AllowedValues": "1048576-", "MinimumEngineVersion": "6.2.4" }, { "Name": "active-defrag-max-scan-fields", "Value": "1000", "Description": "Maximum number of set/hash/zset/list fields that will be processed from the main dictionary scan", "DataType": "integer", "AllowedValues": "1-1000000", "MinimumEngineVersion": "6.2.4" }, { "Name": "active-defrag-threshold-lower", "Value": "10", "Description": "Minimum percentage of fragmentation to start active defrag", "DataType": "integer", "AllowedValues": "1-100", "MinimumEngineVersion": "6.2.4" }, { "Name": "active-defrag-threshold-upper", "Value": "100", "Description": "Maximum percentage of fragmentation at which we use maximum effort", "DataType": "integer", "AllowedValues": "1-100", "MinimumEngineVersion": "6.2.4" }, { "Name": "active-expire-effort", "Value": "1", "Description": "The amount of effort that redis uses to expire items in the active expiration job", "DataType": "integer", "AllowedValues": "1-10", "MinimumEngineVersion": "6.2.4" }, { "Name": "activerehashing", "Value": "yes", "Description": "Apply rehashing or not", "DataType": "string", "AllowedValues": "yes,no", "MinimumEngineVersion": "6.2.4" }, { "Name": "client-output-buffer-limit-normal-hard-limit", "Value": "0", "Description": "Normal client output buffer hard limit in bytes", "DataType": "integer", "AllowedValues": "0-", "MinimumEngineVersion": "6.2.4" }, { "Name": "client-output-buffer-limit-normal-soft-limit", "Value": "0", "Description": "Normal client output buffer soft limit in bytes", "DataType": "integer", "AllowedValues": "0-", "MinimumEngineVersion": "6.2.4" }, { "Name": "client-output-buffer-limit-normal-soft-seconds", "Value": "0", "Description": "Normal client output buffer soft limit in seconds", "DataType": "integer", "AllowedValues": "0-", "MinimumEngineVersion": "6.2.4" }, { "Name": "client-output-buffer-limit-pubsub-hard-limit", "Value": "33554432", "Description": "Pubsub client output buffer hard limit in bytes", "DataType": "integer", "AllowedValues": "0-", "MinimumEngineVersion": "6.2.4" }, { "Name": "client-output-buffer-limit-pubsub-soft-limit", "Value": "8388608", "Description": "Pubsub client output buffer soft limit in bytes", "DataType": "integer", "AllowedValues": "0-", "MinimumEngineVersion": "6.2.4" }, { "Name": "client-output-buffer-limit-pubsub-soft-seconds", "Value": "60", "Description": "Pubsub client output buffer soft limit in seconds", "DataType": "integer", "AllowedValues": "0-", "MinimumEngineVersion": "6.2.4" }, { "Name": "hash-max-ziplist-entries", "Value": "512", "Description": "The maximum number of hash entries in order for the dataset to be compressed", "DataType": "integer", "AllowedValues": "0-", "MinimumEngineVersion": "6.2.4" }, { "Name": "hash-max-ziplist-value", "Value": "64", "Description": "The threshold of biggest hash entries in order for the dataset to be compressed", "DataType": "integer", "AllowedValues": "0-", "MinimumEngineVersion": "6.2.4" }, { "Name": "hll-sparse-max-bytes", "Value": "3000", "Description": "HyperLogLog sparse representation bytes limit", "DataType": "integer", "AllowedValues": "1-16000", "MinimumEngineVersion": "6.2.4" }, { "Name": "lazyfree-lazy-eviction", "Value": "no", "Description": "Perform an asynchronous delete on evictions", "DataType": "string", "AllowedValues": "yes,no", "MinimumEngineVersion": "6.2.4" }, { "Name": "lazyfree-lazy-expire", "Value": "no", "Description": "Perform an asynchronous delete on expired keys", "DataType": "string", "AllowedValues": "yes,no", "MinimumEngineVersion": "6.2.4" }, { "Name": "lazyfree-lazy-server-del", "Value": "no", "Description": "Perform an asynchronous delete on key updates", "DataType": "string", "AllowedValues": "yes,no", "MinimumEngineVersion": "6.2.4" }, { "Name": "lazyfree-lazy-user-del", "Value": "no", "Description": "Specifies whether the default behavior of DEL command acts the same as UNLINK", "DataType": "string", "AllowedValues": "yes,no", "MinimumEngineVersion": "6.2.4" }, { "Name": "lfu-decay-time", "Value": "1", "Description": "The amount of time in minutes to decrement the key counter for LFU eviction policyd", "DataType": "integer", "AllowedValues": "0-", "MinimumEngineVersion": "6.2.4" }, { "Name": "lfu-log-factor", "Value": "10", "Description": "The log factor for incrementing key counter for LFU eviction policy", "DataType": "integer", "AllowedValues": "1-", "MinimumEngineVersion": "6.2.4" }, { "Name": "list-compress-depth", "Value": "0", "Description": "Number of quicklist ziplist nodes from each side of the list to exclude from compression. The head and tail of the list are always uncompressed for fast push/pop operations", "DataType": "integer", "AllowedValues": "0-", "MinimumEngineVersion": "6.2.4" }, { "Name": "maxmemory-policy", "Value": "noeviction", "Description": "Max memory policy", "DataType": "string", "AllowedValues": "volatile-lru,allkeys-lru,volatile-lfu,allkeys-lfu,volatile-random,allkeys-random,volatile-ttl,noeviction", "MinimumEngineVersion": "6.2.4" }, { "Name": "maxmemory-samples", "Value": "3", "Description": "Max memory samples", "DataType": "integer", "AllowedValues": "1-", "MinimumEngineVersion": "6.2.4" }, { "Name": "notify-keyspace-events", "Description": "The keyspace events for Redis to notify Pub/Sub clients about. By default all notifications are disabled", "DataType": "string", "MinimumEngineVersion": "6.2.4" }, { "Name": "set-max-intset-entries", "Value": "512", "Description": "The limit in the size of the set in order for the dataset to be compressed", "DataType": "integer", "AllowedValues": "0-", "MinimumEngineVersion": "6.2.4" }, { "Name": "slowlog-log-slower-than", "Value": "10000", "Description": "The execution time, in microseconds, to exceed in order for the command to get logged. Note that a negative number disables the slow log, while a value of zero forces the logging of every command", "DataType": "integer", "AllowedValues": "-", "MinimumEngineVersion": "6.2.4" }, { "Name": "slowlog-max-len", "Value": "128", "Description": "The length of the slow log. There is no limit to this length. Just be aware that it will consume memory. You can reclaim memory used by the slow log with SLOWLOG RESET.", "DataType": "integer", "AllowedValues": "0-", "MinimumEngineVersion": "6.2.4" }, { "Name": "stream-node-max-bytes", "Value": "4096", "Description": "The maximum size of a single node in a stream in bytes", "DataType": "integer", "AllowedValues": "0-", "MinimumEngineVersion": "6.2.4" }, { "Name": "stream-node-max-entries", "Value": "100", "Description": "The maximum number of items a single node in a stream can contain", "DataType": "integer", "AllowedValues": "0-", "MinimumEngineVersion": "6.2.4" }, { "Name": "tcp-keepalive", "Value": "300", "Description": "If non-zero, send ACKs every given number of seconds", "DataType": "integer", "AllowedValues": "0-", "MinimumEngineVersion": "6.2.4" }, { "Name": "timeout", "Value": "0", "Description": "Close connection if client is idle for a given number of seconds, or never if 0", "DataType": "integer", "AllowedValues": "0,20-", "MinimumEngineVersion": "6.2.4" }, { "Name": "tracking-table-max-keys", "Value": "1000000", "Description": "The maximum number of keys allowed for the tracking table for client side caching", "DataType": "integer", "AllowedValues": "1-100000000", "MinimumEngineVersion": "6.2.4" }, { "Name": "zset-max-ziplist-entries", "Value": "128", "Description": "The maximum number of sorted set entries in order for the dataset to be compressed", "DataType": "integer", "AllowedValues": "0-", "MinimumEngineVersion": "6.2.4" }, { "Name": "zset-max-ziplist-value", "Value": "64", "Description": "The threshold of biggest sorted set entries in order for the dataset to be compressed", "DataType": "integer", "AllowedValues": "0-", "MinimumEngineVersion": "6.2.4" } ] }`For more information, see [Configuring engine parameters using parameter groups](https://docs.aws.amazon.com/memorydb/latest/devguide/parametergroups.html)in the*MemoryDB User Guide*.- 
                    For API details, see [DescribeParameters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/describe-parameters.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-snapshots`.

- **AWS CLI**
- 
            
                    **To return a list of snapshots**The following describe-snapshots` returns a list of snapshots. `aws memorydb describe-snapshots`Output: `{ "Snapshots": [ { "Name": "my-cluster-snapshot", "Status": "available", "Source": "manual", "ARN": "arn:aws:memorydb:us-east-1:491658xxxxxx2:snapshot/my-cluster-snapshot", "ClusterConfiguration": { "Name": "my-cluster", "Description": " ", "NodeType": "db.r6g.large", "EngineVersion": "6.2", "MaintenanceWindow": "wed:03:00-wed:04:00", "Port": 6379, "ParameterGroupName": "default.memorydb-redis6", "SubnetGroupName": "my-sg", "VpcId": "vpc-862574fc", "SnapshotRetentionLimit": 0, "SnapshotWindow": "04:30-05:30", "NumShards": 2 } } }`For more information, see [Snapshot and restore](https://docs.aws.amazon.com/memorydb/latest/devguide/snapshots.html)in the*MemoryDB User Guide*.- 
                    For API details, see [DescribeSnapshots](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/describe-snapshots.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-subnet-groups`.

- **AWS CLI**
- 
            
                    **To return a list of subnet groups**The following describe-subnet-groups` returns a list of subnet groups. `aws memorydb describe-subnet-groups`Output `{ "SubnetGroups": [ { "Name": "my-sg", "Description": "pat-sg", "VpcId": "vpc-86xxx4fc", "Subnets": [ { "Identifier": "subnet-faxx84a6", "AvailabilityZone": { "Name": "us-east-1b" } }, { "Identifier": "subnet-56xxf61b", "AvailabilityZone": { "Name": "us-east-1a" } } ], "ARN": "arn:aws:memorydb:us-east-1:49165xxxxxx:subnetgroup/my-sg" } ] }`For more information, see [Subnets and subnet groups](https://docs.aws.amazon.com/memorydb/latest/devguide/subnetgroups.html)in the*MemoryDB User Guide*.- 
                    For API details, see [DescribeSubnetGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/describe-subnet-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-users`.

- **AWS CLI**
- 
            
                    **To return a list of users**The following describe-users` returns a list of users. `aws memorydb describe-users`Output `{ "Users": [ { "Name": "default", "Status": "active", "AccessString": "on ~* &* +@all", "ACLNames": [ "open-access" ], "MinimumEngineVersion": "6.0", "Authentication": { "Type": "no-password" }, "ARN": "arn:aws:memorydb:us-east-1:491658xxxxxx:user/default" }, { "Name": "my-user", "Status": "active", "AccessString": "off ~objects:* ~items:* ~public:* resetchannels -@all", "ACLNames": [], "MinimumEngineVersion": "6.2", "Authentication": { "Type": "password", "PasswordCount": 2 }, "ARN": "arn:aws:memorydb:us-east-1:491658xxxxxx:user/my-user" } ] }`For more information, see [Authenticating users with Access Control Lists](https://docs.aws.amazon.com/memorydb/latest/devguide/clusters.acls.html)in the*MemoryDB User Guide*.- 
                    For API details, see [DescribeUsers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/describe-users.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `failover-shard`.

- **AWS CLI**
- 
            
                    **To fail over a shard**The following failover-shard` fails over a shard. `aws memorydb failover-shard \ --cluster-name``my-cluster`--shard-name`0001`Output: `{ "Cluster": { "Name": "my-cluster", "Status": "available", "NumberOfShards": 2, "ClusterEndpoint": { "Address": "clustercfg.my-cluster.xxxxxx.memorydb.us-east-1.amazonaws.com", "Port": 6379 }, "NodeType": "db.r6g.large", "EngineVersion": "6.2", "EnginePatchVersion": "6.2.6", "ParameterGroupName": "default.memorydb-redis6", "ParameterGroupStatus": "in-sync", "SecurityGroups": [ { "SecurityGroupId": "sg-0a143xxxx45c9fae", "Status": "active" } ], "SubnetGroupName": "my-sg", "TLSEnabled": true, "ARN": "arn:aws:memorydb:us-east-1:491658xxxxxx:cluster/my-cluster", "SnapshotRetentionLimit": 0, "MaintenanceWindow": "wed:03:00-wed:04:00", "SnapshotWindow": "04:30-05:30", "AutoMinorVersionUpgrade": true } }`For more information, see [Minimizing downtime with MultiAZ](https://docs.aws.amazon.com/memorydb/latest/devguide/autofailover.html)in the*MemoryDB User Guide*.- 
                    For API details, see [FailoverShard](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/failover-shard.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-allowed-node-type-updates`.

- **AWS CLI**
- 
            
                    **To return a list of allowed node type updates**The following `list-allowed-node-type-updates`returns a list of available node type updates.`aws memorydb list-allowed-node-type-updates \ --cluster-name``my-cluster`Output: `{ "Cluster": { "Name": "my-cluster", "Status": "available", "NumberOfShards": 2, "ClusterEndpoint": { "Address": "clustercfg.my-cluster.xxxxxx.memorydb.us-east-1.amazonaws.com", "Port": 6379 }, "NodeType": "db.r6g.large", "EngineVersion": "6.2", "EnginePatchVersion": "6.2.6", "ParameterGroupName": "default.memorydb-redis6", "ParameterGroupStatus": "in-sync", "SecurityGroups": [ { "SecurityGroupId": "sg-0a143xxxx45c9fae", "Status": "active" } ], "SubnetGroupName": "my-sg", "TLSEnabled": true, "ARN": "arn:aws:memorydb:us-east-1:491658xxxxxx:cluster/my-cluster", "SnapshotRetentionLimit": 0, "MaintenanceWindow": "wed:03:00-wed:04:00", "SnapshotWindow": "04:30-05:30", "AutoMinorVersionUpgrade": true } }`For more information, see [Scaling](https://docs.aws.amazon.com/memorydb/latest/devguide/scaling.html)in the*MemoryDB User Guide*.- 
                    For API details, see [ListAllowedNodeTypeUpdates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/list-allowed-node-type-updates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags`.

- **AWS CLI**
- 
            
                    **To return a list of tags**The following list-tags returns a list of tags. `aws memorydb list-tags \ --resource-arn``arn:aws:memorydb:us-east-1:491658xxxxxx:cluster/my-cluster`Output: `{ "TagList": [ { "Key": "mytag", "Value": "myvalue" } ] }`For more information, see [Tagging resources](https://docs.aws.amazon.com/memorydb/latest/devguide/tagging-resources.html)in the*MemoryDB User Guide*.- 
                    For API details, see [ListTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/list-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reset-parameter-group`.

- **AWS CLI**
- 
            
                    **To reset a parameter group**The following reset-parameter-group` resets a parameter group. `aws memorydb reset-parameter-group \ --parameter-group-name``my-parameter-group`\ --all-parametersOutput: `{ "ParameterGroup": { "Name": "my-parameter-group", "Family": "memorydb_redis6", "Description": "my parameter group", "ARN": "arn:aws:memorydb:us-east-1:491658xxxxxx:parametergroup/my-parameter-group" } }`For more information, see [Configuring engine parameters using parameter groups](https://docs.aws.amazon.com/memorydb/latest/devguide/parametergroups.html)in the*MemoryDB User Guide*.- 
                    For API details, see [ResetParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/reset-parameter-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To tag a resource**The following tag-resource` adds a tag to a resource. `aws memorydb tag-resource \ --resource-arn``arn:aws:memorydb:us-east-1:491658xxxxxx:cluster/my-cluster`\ --tags Key="mykey",Value="myvalue"Output: `{ "TagList": [ { "Key": "mytag", "Value": "myvalue" }, { "Key": "mykey", "Value": "myvalue" } ] }`For more information, see [Tagging resources](https://docs.aws.amazon.com/memorydb/latest/devguide/tagging-resources.html)in the*MemoryDB User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To update an ACL**The following update-acl` updates an ACL by adding a user. `aws memorydb untag-resource \ --resource-arn``arn:aws:memorydb:us-east-1:491658xxxxx:cluster/my-cluster`\ --tag-keys`mykey`Output: `{ "TagList": [ { "Key": "mytag", "Value": "myvalue" } ] }`For more information, see [Tagging resources](https://docs.aws.amazon.com/memorydb/latest/devguide/tagging-resources.html)in the*MemoryDB User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-cluster`.

- **AWS CLI**
- 
            
                    **To update a cluster**The following update-cluster`` updates the parameter group of a cluster to my-parameter-group. `aws memorydb update-cluster \ --cluster-name``my-cluster`\ --parameter-group-name`my-parameter-group`Output: `{ "Cluster": { "Name": "my-cluster", "Status": "available", "NumberOfShards": 2, "AvailabilityMode": "MultiAZ", "ClusterEndpoint": { "Address": "clustercfg.my-cluster.llru6f.memorydb.us-east-1.amazonaws.com", "Port": 6379 }, "NodeType": "db.r6g.large", "EngineVersion": "6.2", "EnginePatchVersion": "6.2.6", "ParameterGroupName": "my-parameter-group", "ParameterGroupStatus": "in-sync", "SecurityGroups": [ { "SecurityGroupId": "sg-0a143xxxxxc9fae", "Status": "active" } ], "SubnetGroupName": "pat-sg", "TLSEnabled": true, "ARN": "arn:aws:memorydb:us-east-1:491658xxxxxx:cluster/my-cluster", "SnapshotRetentionLimit": 0, "MaintenanceWindow": "wed:03:00-wed:04:00", "SnapshotWindow": "04:30-05:30", "ACLName": "my-acl", "AutoMinorVersionUpgrade": true } }`For more information, see [Modifying a cluster](https://docs.aws.amazon.com/memorydb/latest/devguide/clusters.modify.html)in the*MemoryDB User Guide*.- 
                    For API details, see [UpdateCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/update-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-parameter-group`.

- **AWS CLI**
- 
            
                    **To update a parameter group**The following update-parameter-group`` updates a parameter group. `aws memorydb update-parameter-group \ --parameter-group-name``my-parameter-group`\ --parameter-name-values`"ParameterName=activedefrag, ParameterValue=no"`Output: `{ "ParameterGroup": { "Name": "my-parameter-group", "Family": "memorydb_redis6", "Description": "my parameter group", "ARN": "arn:aws:memorydb:us-east-1:49165xxxxxx:parametergroup/my-parameter-group" } }`For more information, see [Modifying a parameter group](https://docs.aws.amazon.com/memorydb/latest/devguide/parametergroups.modifying.html)in the*MemoryDB User Guide*.- 
                    For API details, see [UpdateParameterGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/update-parameter-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-subnet-group`.

- **AWS CLI**
- 
            
                    **To update a subnet group**The following update-subnet-group` updates a subnet group's subnet ID. `aws memorydb update-subnet-group \ --subnet-group-name``my-sg`\ --subnet-ids`subnet-01f29d458f3xxxxx`Output: `{ "SubnetGroup": { "Name": "my-sg-1", "Description": "my-sg", "VpcId": "vpc-09d2cfc01xxxxxxx", "Subnets": [ { "Identifier": "subnet-01f29d458fxxxxxx", "AvailabilityZone": { "Name": "us-east-1a" } } ], "ARN": "arn:aws:memorydb:us-east-1:491658xxxxxx:subnetgroup/my-sg" } }`For more information, see [Subnets and subnet groups](https://docs.aws.amazon.com/memorydb/latest/devguide/subnetgroups.html)in the*MemoryDB User Guide*.- 
                    For API details, see [UpdateSubnetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/update-subnet-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-user`.

- **AWS CLI**
- 
            
                    **To update a user**The following `update-user`modifies a user's access string.`aws memorydb update-user \ --user-name``my-user`\ --access-string`"off ~objects:* ~items:* ~public:* resetchannels -@all"`Output: `{ "User": { "Name": "my-user", "Status": "modifying", "AccessString": "off ~objects:* ~items:* ~public:* resetchannels -@all", "ACLNames": [ "myt-acl" ], "MinimumEngineVersion": "6.2", "Authentication": { "Type": "password", "PasswordCount": 2 }, "ARN": "arn:aws:memorydb:us-east-1:491658xxxxxx:user/my-user" } }`For more information, see [Authenticating users with Access Control Lists](https://docs.aws.amazon.com/memorydb/latest/devguide/clusters.acls.html)in the*MemoryDB User Guide*.- 
                    For API details, see [UpdateUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/memorydb/update-user.html)in*AWS CLI Command Reference*.
 
-