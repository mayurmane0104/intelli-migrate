# Amazon MSK examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_kafka_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_kafka_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon MSK.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-cluster`.

- **AWS CLI**
- 
            
                    **To create an Amazon MSK cluster**The following `create-cluster`example creates an MSK cluster named`MessagingCluster`with three broker nodes. A JSON file named`brokernodegroupinfo.json`specifies the three subnets over which you want Amazon MSK to distribute the broker nodes. This example doesn't specify the monitoring level, so the cluster gets the`DEFAULT`level.`aws kafka create-cluster \ --cluster-name``"MessagingCluster"`\ --broker-node-group-info`file://brokernodegroupinfo.json`\ --kafka-version`"2.2.1"`\ --number-of-broker-nodes`3`Contents of `brokernodegroupinfo.json`:`{ "InstanceType": "kafka.m5.xlarge", "BrokerAZDistribution": "DEFAULT", "ClientSubnets": [ "subnet-0123456789111abcd", "subnet-0123456789222abcd", "subnet-0123456789333abcd" ] }`Output: `{ "ClusterArn": "arn:aws:kafka:us-west-2:123456789012:cluster/MessagingCluster/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE-2", "ClusterName": "MessagingCluster", "State": "CREATING" }`For more information, see [Create an Amazon MSK Cluster](https://docs.aws.amazon.com/msk/latest/developerguide/msk-create-cluster.html)in the*Amazon Managed Streaming for Apache Kafka*.- 
                    For API details, see [CreateCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/create-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-configuration`.

- **AWS CLI**
- 
            
                    **To create a custom Amazon MSK configuration**The following `create-configuration`example creates a custom MSK configuration with the server properties that are specified in the input file.`aws kafka create-configuration \ --name``"CustomConfiguration"`\ --description`"Topic autocreation enabled; Apache ZooKeeper timeout 2000 ms; Log rolling 604800000 ms."`\ --kafka-versions`"2.2.1"`\ --server-properties`file://configuration.txt`Contents of `configuration.txt`:`auto.create.topics.enable = true zookeeper.connection.timeout.ms = 2000 log.roll.ms = 604800000`This command produces no output. Output: `{ "Arn": "arn:aws:kafka:us-west-2:123456789012:configuration/CustomConfiguration/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE-2", "CreationTime": "2019-10-09T15:26:05.548Z", "LatestRevision": { "CreationTime": "2019-10-09T15:26:05.548Z", "Description": "Topic autocreation enabled; Apache ZooKeeper timeout 2000 ms; Log rolling 604800000 ms.", "Revision": 1 }, "Name": "CustomConfiguration" }`For more information, see [Amazon MSK Configuration Operations](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-operations.html)in the*Amazon Managed Streaming for Apache Kafka Developer Guide*.- 
                    For API details, see [CreateConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/create-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-cluster`.

- **AWS CLI**
- 
            
                    **To describe a cluster**The following `describe-cluster`example describes an Amazon MSK cluster.`aws kafka describe-cluster \ --cluster-arn``arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5`Output: `{ "ClusterInfo": { "BrokerNodeGroupInfo": { "BrokerAZDistribution": "DEFAULT", "ClientSubnets": [ "subnet-cbfff283", "subnet-6746046b" ], "InstanceType": "kafka.m5.large", "SecurityGroups": [ "sg-f839b688" ], "StorageInfo": { "EbsStorageInfo": { "VolumeSize": 100 } } }, "ClusterArn": "arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5", "ClusterName": "demo-cluster-1", "CreationTime": "2020-07-09T02:31:36.223000+00:00", "CurrentBrokerSoftwareInfo": { "KafkaVersion": "2.2.1" }, "CurrentVersion": "K3AEGXETSR30VB", "EncryptionInfo": { "EncryptionAtRest": { "DataVolumeKMSKeyId": "arn:aws:kms:us-east-1:123456789012:key/a7ca56d5-0768-4b64-a670-339a9fbef81c" }, "EncryptionInTransit": { "ClientBroker": "TLS_PLAINTEXT", "InCluster": true } }, "EnhancedMonitoring": "DEFAULT", "OpenMonitoring": { "Prometheus": { "JmxExporter": { "EnabledInBroker": false }, "NodeExporter": { "EnabledInBroker": false } } }, "NumberOfBrokerNodes": 2, "State": "ACTIVE", "Tags": {}, "ZookeeperConnectString": "z-2.demo-cluster-1.xuy0sb.c5.kafka.us-east-1.amazonaws.com:2181,z-1.demo-cluster-1.xuy0sb.c5.kafka.us-east-1.amazonaws.com:2181,z-3.demo-cluster-1.xuy0sb.c5.kafka.us-east-1.amazonaws.com:2181" } }`For more information, see [Listing Amazon MSK Clusters](https://docs.aws.amazon.com/msk/latest/developerguide/msk-list-clusters.html)in the*Amazon Managed Streaming for Apache Kafka Developer Guide*.- 
                    For API details, see [DescribeCluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/describe-cluster.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-bootstrap-brokers`.

- **AWS CLI**
- 
            
                    **To get bootstrap brokers**The following `get-bootstrap-brokers`example retrieves the bootstrap broker information for an Amazon MSK cluster.`aws kafka get-bootstrap-brokers \ --cluster-arn``arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5`Output: `{ "BootstrapBrokerString": "b-1.demo-cluster-1.xuy0sb.c5.kafka.us-east-1.amazonaws.com:9092,b-2.demo-cluster-1.xuy0sb.c5.kafka.us-east-1.amazonaws.com:9092", "BootstrapBrokerStringTls": "b-1.demo-cluster-1.xuy0sb.c5.kafka.us-east-1.amazonaws.com:9094,b-2.demo-cluster-1.xuy0sb.c5.kafka.us-east-1.amazonaws.com:9094" }`For more information, see [Getting the Bootstrap Brokers](https://docs.aws.amazon.com/msk/latest/developerguide/msk-get-bootstrap-brokers.html)in the*Amazon Managed Streaming for Apache Kafka Developer Guide*.- 
                    For API details, see [GetBootstrapBrokers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/get-bootstrap-brokers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-clusters`.

- **AWS CLI**
- 
            
                    **To list the available clusters**The following `list-clusters`example lists the Amazon MSK clusters in your AWS account.`aws kafka list-clusters`Output: `{ "ClusterInfoList": [ { "BrokerNodeGroupInfo": { "BrokerAZDistribution": "DEFAULT", "ClientSubnets": [ "subnet-cbfff283", "subnet-6746046b" ], "InstanceType": "kafka.m5.large", "SecurityGroups": [ "sg-f839b688" ], "StorageInfo": { "EbsStorageInfo": { "VolumeSize": 100 } } }, "ClusterArn": "arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5", "ClusterName": "demo-cluster-1", "CreationTime": "2020-07-09T02:31:36.223000+00:00", "CurrentBrokerSoftwareInfo": { "KafkaVersion": "2.2.1" }, "CurrentVersion": "K3AEGXETSR30VB", "EncryptionInfo": { "EncryptionAtRest": { "DataVolumeKMSKeyId": "arn:aws:kms:us-east-1:123456789012:key/a7ca56d5-0768-4b64-a670-339a9fbef81c" }, "EncryptionInTransit": { "ClientBroker": "TLS_PLAINTEXT", "InCluster": true } }, "EnhancedMonitoring": "DEFAULT", "OpenMonitoring": { "Prometheus": { "JmxExporter": { "EnabledInBroker": false }, "NodeExporter": { "EnabledInBroker": false } } }, "NumberOfBrokerNodes": 2, "State": "ACTIVE", "Tags": {}, "ZookeeperConnectString": "z-2.demo-cluster-1.xuy0sb.c5.kafka.us-east-1.amazonaws.com:2181,z-1.demo-cluster-1.xuy0sb.c5.kafka.us-east-1.amazonaws.com:2181,z-3.demo-cluster-1.xuy0sb.c5.kafka.us-east-1.amazonaws.com:2181" } ] }`For more information, see [Listing Amazon MSK Clusters](https://docs.aws.amazon.com/msk/latest/developerguide/msk-list-clusters.html)in the*Amazon Managed Streaming for Apache Kafka Developer Guide*.- 
                    For API details, see [ListClusters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/list-clusters.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-broker-storage`.

- **AWS CLI**
- 
            
                    **To update the EBS storage for brokers**The following `update-broker-storage`example updates the amount of EBS storage for all the brokers in the cluster. Amazon MSK sets the target storage amount for each broker to the amount specified in the example. You can get the current version of the cluster by describing the cluster or by listing all of the clusters.`aws kafka update-broker-storage \ --cluster-arn``"arn:aws:kafka:us-west-2:123456789012:cluster/MessagingCluster/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE-2"`\ --current-version`"K21V3IB1VIZYYH"`\ --target-broker-ebs-volume-info`"KafkaBrokerNodeId=ALL,VolumeSizeGB=1100"`The output returns an ARN for this `update-broker-storage`operation. To determine if this operation is complete, use the`describe-cluster-operation`command with this ARN as input.`{ "ClusterArn": "arn:aws:kafka:us-west-2:123456789012:cluster/MessagingCluster/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE-2", "ClusterOperationArn": "arn:aws:kafka:us-west-2:123456789012:cluster-operation/V123450123/a1b2c3d4-1234-abcd-cdef-22222EXAMPLE-2/a1b2c3d4-abcd-1234-bcde-33333EXAMPLE" }`For more information, see [Update the EBS Storage for Brokers](https://docs.aws.amazon.com/msk/latest/developerguide/msk-update-storage.html)in the*Amazon Managed Streaming for Apache Kafka Developer Guide*.- 
                    For API details, see [UpdateBrokerStorage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/update-broker-storage.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-cluster-configuration`.

- **AWS CLI**
- 
            
                    **To update the configuration of an Amazon MSK cluster**The following `update-cluster-configuration`example updates the configuration of the specified existing MSK cluster. It uses a custom MSK configuration.`aws kafka update-cluster-configuration \ --cluster-arn``"arn:aws:kafka:us-west-2:123456789012:cluster/MessagingCluster/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE-2"`\ --configuration-info`file://configuration-info.json`\ --current-version`"K21V3IB1VIZYYH"`Contents of `configuration-info.json`:`{ "Arn": "arn:aws:kafka:us-west-2:123456789012:configuration/CustomConfiguration/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE-2", "Revision": 1 }`The output returns an ARN for this `update-cluster-configuration`operation. To determine if this operation is complete, use the`describe-cluster-operation`command with this ARN as input.`{ "ClusterArn": "arn:aws:kafka:us-west-2:123456789012:cluster/MessagingCluster/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE-2", "ClusterOperationArn": "arn:aws:kafka:us-west-2:123456789012:cluster-operation/V123450123/a1b2c3d4-1234-abcd-cdef-22222EXAMPLE-2/a1b2c3d4-abcd-1234-bcde-33333EXAMPLE" }`For more information, see [Update the Configuration of an Amazon MSK Cluster](https://docs.aws.amazon.com/msk/latest/developerguide/msk-update-cluster-cofig.html)in the*Amazon Managed Streaming for Apache Kafka Developer Guide*.- 
                    For API details, see [UpdateClusterConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/update-cluster-configuration.html)in*AWS CLI Command Reference*.
 
-