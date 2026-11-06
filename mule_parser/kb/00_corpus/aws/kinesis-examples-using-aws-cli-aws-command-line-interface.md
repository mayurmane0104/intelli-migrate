# Kinesis examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_kinesis_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_kinesis_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Kinesis.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `add-tags-to-stream`.

- **AWS CLI**
- 
            
                    **To add tags to a data stream**The following `add-tags-to-stream`example assigns a tag with the key`samplekey`and value`example`to the specified stream.`aws kinesis add-tags-to-stream \ --stream-name``samplestream`\ --tags`samplekey=example`This command produces no output. For more information, see [Tagging Your Streams](https://docs.aws.amazon.com/streams/latest/dev/tagging.html)in the*Amazon Kinesis Data Streams Developer Guide*.- 
                    For API details, see [AddTagsToStream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/add-tags-to-stream.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-stream`.

- **AWS CLI**
- 
            
                    **To create a data stream**The following `create-stream`example creates a data stream named samplestream with 3 shards.`aws kinesis create-stream \ --stream-name``samplestream`\ --shard-count`3`This command produces no output. For more information, see [Creating a Stream](https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-create-stream.html)in the*Amazon Kinesis Data Streams Developer Guide*.- 
                    For API details, see [CreateStream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/create-stream.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `decrease-stream-retention-period`.

- **AWS CLI**
- 
            
                    **To decrease data stream retention period**The following `decrease-stream-retention-period`example decreases the retention period (the length of time data records are accessible after they are added to the stream) of a stream named samplestream to 48 hours.`aws kinesis decrease-stream-retention-period \ --stream-name``samplestream`\ --retention-period-hours`48`This command produces no output. For more information, see [Changing the Data Retention Period](https://docs.aws.amazon.com/streams/latest/dev/kinesis-extended-retention.html)in the*Amazon Kinesis Data Streams Developer Guide*.- 
                    For API details, see [DecreaseStreamRetentionPeriod](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/decrease-stream-retention-period.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-stream`.

- **AWS CLI**
- 
            
                    **To delete a data stream**The following `delete-stream`example deletes the specified data stream.`aws kinesis delete-stream \ --stream-name``samplestream`This command produces no output. For more information, see [Deleting a Stream](https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-delete-stream.html)in the*Amazon Kinesis Data Streams Developer Guide*.- 
                    For API details, see [DeleteStream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/delete-stream.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deregister-stream-consumer`.

- **AWS CLI**
- 
            
                    **To deregister a data stream consumer**The following `deregister-stream-consumer`example deregisters the specified consumer from the specified data stream.`aws kinesis deregister-stream-consumer \ --stream-arn``arn:aws:kinesis:us-west-2:123456789012:stream/samplestream`\ --consumer-name`KinesisConsumerApplication`This command produces no output. For more information, see [Developing Consumers with Enhanced Fan-Out Using the Kinesis Data Streams API](https://docs.aws.amazon.com/streams/latest/dev/building-enhanced-consumers-api.html)in the*Amazon Kinesis Data Streams Developer Guide*.- 
                    For API details, see [DeregisterStreamConsumer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/deregister-stream-consumer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-limits`.

- **AWS CLI**
- 
            
                    **To describe shard limits**The following `describe-limits`example displays the shard limits and usage for the current AWS account.`aws kinesis describe-limits`Output: `{ "ShardLimit": 500, "OpenShardCount": 29 }`For more information, see [Resharding a Stream](https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-resharding.html)in the*Amazon Kinesis Data Streams Developer Guide*.- 
                    For API details, see [DescribeLimits](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/describe-limits.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-stream-consumer`.

- **AWS CLI**
- 
            
                    **To describe a data stream consumer**The following `describe-stream-consumer`example returns the description of the specified consumer, registered with the specified data stream.`aws kinesis describe-stream-consumer \ --stream-arn``arn:aws:kinesis:us-west-2:012345678912:stream/samplestream`\ --consumer-name`KinesisConsumerApplication`Output: `{ "ConsumerDescription": { "ConsumerName": "KinesisConsumerApplication", "ConsumerARN": "arn:aws:kinesis:us-west-2:123456789012:stream/samplestream/consumer/KinesisConsumerApplication:1572383852", "ConsumerStatus": "ACTIVE", "ConsumerCreationTimestamp": 1572383852.0, "StreamARN": "arn:aws:kinesis:us-west-2:123456789012:stream/samplestream" } }`For more information, see [Reading Data from Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/building-consumers.html)in the*Amazon Kinesis Data Streams Developer Guide*.- 
                    For API details, see [DescribeStreamConsumer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/describe-stream-consumer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-stream-summary`.

- **AWS CLI**
- 
            
                    **To describe a data stream summary**The following `describe-stream-summary`example provides a summarized description (without the shard list) of the specified data stream.`aws kinesis describe-stream-summary \ --stream-name``samplestream`Output: `{ "StreamDescriptionSummary": { "StreamName": "samplestream", "StreamARN": "arn:aws:kinesis:us-west-2:123456789012:stream/samplestream", "StreamStatus": "ACTIVE", "RetentionPeriodHours": 48, "StreamCreationTimestamp": 1572297168.0, "EnhancedMonitoring": [ { "ShardLevelMetrics": [] } ], "EncryptionType": "NONE", "OpenShardCount": 3, "ConsumerCount": 0 } }`For more information, see [Creating and Managing Streams](https://docs.aws.amazon.com/streams/latest/dev/working-with-streams.html)in the*Amazon Kinesis Data Streams Developer Guide*.- 
                    For API details, see [DescribeStreamSummary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/describe-stream-summary.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-stream`.

- **AWS CLI**
- 
            
                    **To describe a data stream**The following `describe-stream`example returns the details of the specified data stream.`aws kinesis describe-stream \ --stream-name``samplestream`Output: `{ "StreamDescription": { "Shards": [ { "ShardId": "shardId-000000000000", "HashKeyRange": { "StartingHashKey": "0", "EndingHashKey": "113427455640312821154458202477256070484" }, "SequenceNumberRange": { "StartingSequenceNumber": "49600871682957036442365024926191073437251060580128653314" } }, { "ShardId": "shardId-000000000001", "HashKeyRange": { "StartingHashKey": "113427455640312821154458202477256070485", "EndingHashKey": "226854911280625642308916404954512140969" }, "SequenceNumberRange": { "StartingSequenceNumber": "49600871682979337187563555549332609155523708941634633746" } }, { "ShardId": "shardId-000000000002", "HashKeyRange": { "StartingHashKey": "226854911280625642308916404954512140970", "EndingHashKey": "340282366920938463463374607431768211455" }, "SequenceNumberRange": { "StartingSequenceNumber": "49600871683001637932762086172474144873796357303140614178" } } ], "StreamARN": "arn:aws:kinesis:us-west-2:123456789012:stream/samplestream", "StreamName": "samplestream", "StreamStatus": "ACTIVE", "RetentionPeriodHours": 24, "EnhancedMonitoring": [ { "ShardLevelMetrics": [] } ], "EncryptionType": "NONE", "KeyId": null, "StreamCreationTimestamp": 1572297168.0 } }`For more information, see [Creating and Managing Streams](https://docs.aws.amazon.com/streams/latest/dev/working-with-streams.html)in the*Amazon Kinesis Data Streams Developer Guide*.- 
                    For API details, see [DescribeStream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/describe-stream.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-enhanced-monitoring`.

- **AWS CLI**
- 
            
                    **To disable enhanced monitoring for shard-level metrics**The following `disable-enhanced-monitoring`example disables enhanced Kinesis data stream monitoring for shard-level metrics.`aws kinesis disable-enhanced-monitoring \ --stream-name``samplestream`--shard-level-metrics`ALL`Output: `{ "StreamName": "samplestream", "CurrentShardLevelMetrics": [ "IncomingBytes", "OutgoingRecords", "IteratorAgeMilliseconds", "IncomingRecords", "ReadProvisionedThroughputExceeded", "WriteProvisionedThroughputExceeded", "OutgoingBytes" ], "DesiredShardLevelMetrics": [] }`For more information, see [Monitoring Streams in Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/monitoring.html)in the*Amazon Kinesis Data Streams Developer Guide*.- 
                    For API details, see [DisableEnhancedMonitoring](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/disable-enhanced-monitoring.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-enhanced-monitoring`.

- **AWS CLI**
- 
            
                    **To enable enhanced monitoring for shard-level metrics**The following `enable-enhanced-monitoring`example enables enhanced Kinesis data stream monitoring for shard-level metrics.`aws kinesis enable-enhanced-monitoring \ --stream-name``samplestream`\ --shard-level-metrics`ALL`Output: `{ "StreamName": "samplestream", "CurrentShardLevelMetrics": [], "DesiredShardLevelMetrics": [ "IncomingBytes", "OutgoingRecords", "IteratorAgeMilliseconds", "IncomingRecords", "ReadProvisionedThroughputExceeded", "WriteProvisionedThroughputExceeded", "OutgoingBytes" ] }`For more information, see [Monitoring Streams in Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/monitoring.html)in the*Amazon Kinesis Data Streams Developer Guide*.- 
                    For API details, see [EnableEnhancedMonitoring](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/enable-enhanced-monitoring.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-records`.

- **AWS CLI**
- 
            
                    **To obtain records from a shard**The following `get-records`example gets data records from a Kinesis data stream's shard using the specified shard iterator.`aws kinesis get-records \ --shard-iterator``AAAAAAAAAAF7/0mWD7IuHj1yGv/TKuNgx2ukD5xipCY4cy4gU96orWwZwcSXh3K9tAmGYeOZyLZrvzzeOFVf9iN99hUPw/w/b0YWYeehfNvnf1DYt5XpDJghLKr3DzgznkTmMymDP3R+3wRKeuEw6/kdxY2yKJH0veaiekaVc4N2VwK/GvaGP2Hh9Fg7N++q0Adg6fIDQPt4p8RpavDbk+A4sL9SWGE1`Output: `{ "Records": [], "MillisBehindLatest": 80742000 }`For more information, see [Developing Consumers Using the Kinesis Data Streams API with the AWS SDK for Java](https://docs.aws.amazon.com/streams/latest/dev/developing-consumers-with-sdk.html)in the*Amazon Kinesis Data Streams Developer Guide*.- 
                    For API details, see [GetRecords](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/get-records.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-shard-iterator`.

- **AWS CLI**
- 
            
                    **To obtain a shard iterator**The following `get-shard-iterator`example uses the`AT_SEQUENCE_NUMBER`shard iterator type and generates a shard iterator to start reading data records exactly from the position denoted by the specified sequence number.`aws kinesis get-shard-iterator \ --stream-name``samplestream`\ --shard-id`shardId-000000000001`\ --shard-iterator-type`LATEST`Output: `{ "ShardIterator": "AAAAAAAAAAFEvJjIYI+3jw/4aqgH9FifJ+n48XWTh/IFIsbILP6o5eDueD39NXNBfpZ10WL5K6ADXk8w+5H+Qhd9cFA9k268CPXCz/kebq1TGYI7Vy+lUkA9BuN3xvATxMBGxRY3zYK05gqgvaIRn94O8SqeEqwhigwZxNWxID3Ej7YYYcxQi8Q/fIrCjGAy/n2r5Z9G864YpWDfN9upNNQAR/iiOWKs" }`For more information, see [Developing Consumers Using the Kinesis Data Streams API with the AWS SDK for Java](https://docs.aws.amazon.com/streams/latest/dev/developing-consumers-with-sdk.html)in the*Amazon Kinesis Data Streams Developer Guide*.- 
                    For API details, see [GetShardIterator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/get-shard-iterator.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `increase-stream-retention-period`.

- **AWS CLI**
- 
            
                    **To increase data stream retention period**The following `increase-stream-retention-period`example increases the retention period (the length of time data records are accessible after they are added to the stream) of the specified stream to 168 hours.`aws kinesis increase-stream-retention-period \ --stream-name``samplestream`\ --retention-period-hours`168`This command produces no output. For more information, see [Changing the Data Retention Period](https://docs.aws.amazon.com/streams/latest/dev/kinesis-extended-retention.html)in the*Amazon Kinesis Data Streams Developer Guide*.- 
                    For API details, see [IncreaseStreamRetentionPeriod](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/increase-stream-retention-period.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-shards`.

- **AWS CLI**
- 
            
                    **To list shards in a data stream**The following `list-shards`example lists all shards in the specified stream starting with the shard whose ID immediately follows the specified`exclusive-start-shard-id`of`shardId-000000000000`.`aws kinesis list-shards \ --stream-name``samplestream`\ --exclusive-start-shard-id`shardId-000000000000`Output: `{ "Shards": [ { "ShardId": "shardId-000000000001", "HashKeyRange": { "StartingHashKey": "113427455640312821154458202477256070485", "EndingHashKey": "226854911280625642308916404954512140969" }, "SequenceNumberRange": { "StartingSequenceNumber": "49600871682979337187563555549332609155523708941634633746" } }, { "ShardId": "shardId-000000000002", "HashKeyRange": { "StartingHashKey": "226854911280625642308916404954512140970", "EndingHashKey": "340282366920938463463374607431768211455" }, "SequenceNumberRange": { "StartingSequenceNumber": "49600871683001637932762086172474144873796357303140614178" } } ] }`For more information, see [Listing Shards](https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-list-shards.html)in the*Amazon Kinesis Data Streams Developer Guide*.- 
                    For API details, see [ListShards](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/list-shards.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-streams`.

- **AWS CLI**
- 
            
                    **To list data streams**The following `list-streams`example lists all active data streams in the current account and region.`aws kinesis list-streams`Output: `{ "StreamNames": [ "samplestream", "samplestream1" ] }`For more information, see [Listing Streams](https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-list-streams.html)in the*Amazon Kinesis Data Streams Developer Guide*.- 
                    For API details, see [ListStreams](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/list-streams.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-stream`.

- **AWS CLI**
- 
            
                    **To list tags for a data stream**The following `list-tags-for-stream`example lists the tags attached to the specified data stream.`aws kinesis list-tags-for-stream \ --stream-name``samplestream`Output: `{ "Tags": [ { "Key": "samplekey", "Value": "example" } ], "HasMoreTags": false }`For more information, see [Tagging Your Streams](https://docs.aws.amazon.com/streams/latest/dev/tagging.html)in the*Amazon Kinesis Data Streams Developer Guide*.- 
                    For API details, see [ListTagsForStream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/list-tags-for-stream.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `merge-shards`.

- **AWS CLI**
- 
            
                    **To merge shards**The following `merge-shards`example merges two adjacent shards with IDs of shardId-000000000000 and shardId-000000000001 in the specified data stream and combines them into a single shard.`aws kinesis merge-shards \ --stream-name``samplestream`\ --shard-to-merge`shardId-000000000000`\ --adjacent-shard-to-merge`shardId-000000000001`This command produces no output. For more information, see [Merging Two Shards](https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-resharding-merge.html)in the*Amazon Kinesis Data Streams Developer Guide*.- 
                    For API details, see [MergeShards](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/merge-shards.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-record`.

- **AWS CLI**
- 
            
                    **To write a record into a data stream**The following `put-record`example writes a single data record into the specified data stream using the specified partition key.`aws kinesis put-record \ --stream-name``samplestream`\ --data`sampledatarecord`\ --partition-key`samplepartitionkey`Output: `{ "ShardId": "shardId-000000000009", "SequenceNumber": "49600902273357540915989931256901506243878407835297513618", "EncryptionType": "KMS" }`For more information, see [Developing Producers Using the Amazon Kinesis Data Streams API with the AWS SDK for Java](https://docs.aws.amazon.com/streams/latest/dev/developing-producers-with-sdk.html)in the*Amazon Kinesis Data Streams Developer Guide*.- 
                    For API details, see [PutRecord](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/put-record.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-records`.

- **AWS CLI**
- 
            
                    **To write multiple records into a data stream**The following `put-records`example writes a data record using the specified partition key and another data record using a different partition key in a single call.`aws kinesis put-records \ --stream-name``samplestream`\ --records`Data=blob1,PartitionKey=partitionkey1``Data=blob2,PartitionKey=partitionkey2`Output: `{ "FailedRecordCount": 0, "Records": [ { "SequenceNumber": "49600883331171471519674795588238531498465399900093808706", "ShardId": "shardId-000000000004" }, { "SequenceNumber": "49600902273357540915989931256902715169698037101720764562", "ShardId": "shardId-000000000009" } ], "EncryptionType": "KMS" }`For more information, see [Developing Producers Using the Amazon Kinesis Data Streams API with the AWS SDK for Java](https://docs.aws.amazon.com/streams/latest/dev/developing-producers-with-sdk.html)in the*Amazon Kinesis Data Streams Developer Guide*.- 
                    For API details, see [PutRecords](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/put-records.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-stream-consumer`.

- **AWS CLI**
- 
            
                    **To register a data stream consumer**The following `register-stream-consumer`example registers a consumer called`KinesisConsumerApplication`with the specified data stream.`aws kinesis register-stream-consumer \ --stream-arn``arn:aws:kinesis:us-west-2:012345678912:stream/samplestream`\ --consumer-name`KinesisConsumerApplication`Output: `{ "Consumer": { "ConsumerName": "KinesisConsumerApplication", "ConsumerARN": "arn:aws:kinesis:us-west-2: 123456789012:stream/samplestream/consumer/KinesisConsumerApplication:1572383852", "ConsumerStatus": "CREATING", "ConsumerCreationTimestamp": 1572383852.0 } }`For more information, see [Developing Consumers with Enhanced Fan-Out Using the Kinesis Data Streams API](https://docs.aws.amazon.com/streams/latest/dev/building-enhanced-consumers-api.html)in the*Amazon Kinesis Data Streams Developer Guide*.- 
                    For API details, see [RegisterStreamConsumer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/register-stream-consumer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-tags-from-stream`.

- **AWS CLI**
- 
            
                    **To remove tags from a data stream**The following `remove-tags-from-stream`example removes the tag with the specified key from the specified data stream.`aws kinesis remove-tags-from-stream \ --stream-name``samplestream`\ --tag-keys`samplekey`This command produces no output. For more information, see [Tagging Your Streams](https://docs.aws.amazon.com/streams/latest/dev/tagging.html)in the*Amazon Kinesis Data Streams Developer Guide*.- 
                    For API details, see [RemoveTagsFromStream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/remove-tags-from-stream.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `split-shard`.

- **AWS CLI**
- 
            
                    **To split shards**The following `split-shard`example splits the specified shard into two new shards using a new starting hash key of 10.`aws kinesis split-shard \ --stream-name``samplestream`\ --shard-to-split`shardId-000000000000`\ --new-starting-hash-key`10`This command produces no output. For more information, see [Splitting a Shard](https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-resharding-split.html)in the*Amazon Kinesis Data Streams Developer Guide*.- 
                    For API details, see [SplitShard](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/split-shard.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-stream-encryption`.

- **AWS CLI**
- 
            
                    **To enable data stream encryption**The following `start-stream-encryption`example enables server-side encryption for the specified stream, using the specified AWS KMS key.`aws kinesis start-stream-encryption \ --encryption-type``KMS`\ --key-id`arn:aws:kms:us-west-2:012345678912:key/a3c4a7cd-728b-45dd-b334-4d3eb496e452`\ --stream-name`samplestream`This command produces no output. For more information, see [Data Protection in Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/server-side-encryption.html)in the*Amazon Kinesis Data Streams Developer Guide*.- 
                    For API details, see [StartStreamEncryption](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/start-stream-encryption.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-stream-encryption`.

- **AWS CLI**
- 
            
                    **To disable data stream encryption**The following `stop-stream-encryption`example disables server-side encryption for the specified stream, using the specified AWS KMS key.`aws kinesis start-stream-encryption \ --encryption-type``KMS`\ --key-id`arn:aws:kms:us-west-2:012345678912:key/a3c4a7cd-728b-45dd-b334-4d3eb496e452`\ --stream-name`samplestream`This command produces no output. For more information, see [Data Protection in Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/server-side-encryption.html)in the*Amazon Kinesis Data Streams Developer Guide*.- 
                    For API details, see [StopStreamEncryption](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/stop-stream-encryption.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-shard-count`.

- **AWS CLI**
- 
            
                    **To update the shard count in a data stream**The following `update-shard-count`example updates the shard count of the specified data stream to 6. This example uses uniform scaling, which creates shards of equal size.`aws kinesis update-shard-count \ --stream-name``samplestream`\ --scaling-type`UNIFORM_SCALING`\ --target-shard-count`6`Output: `{ "StreamName": "samplestream", "CurrentShardCount": 3, "TargetShardCount": 6 }`For more information, see [Resharding a Stream](https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-resharding.html)in the*Amazon Kinesis Data Streams Developer Guide*.- 
                    For API details, see [UpdateShardCount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/update-shard-count.html)in*AWS CLI Command Reference*.
 
-