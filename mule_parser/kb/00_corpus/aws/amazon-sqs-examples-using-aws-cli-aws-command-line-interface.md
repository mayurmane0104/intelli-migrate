# Amazon SQS examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_sqs_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_sqs_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon SQS.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `add-permission`.

- **AWS CLI**
- 
            
                    **To add a permission to a queue**This example enables the specified AWS account to send messages to the specified queue. Command: `aws sqs add-permission --queue-url``https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue`--label`SendMessagesFromMyQueue`--aws-account-ids`12345EXAMPLE`--actions`SendMessage`Output: `None.`- 
                    For API details, see [AddPermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/add-permission.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-message-move-task`.

- **AWS CLI**
- 
            
                    **To cancel a message move task**The following `cancel-message-move-task`example cancels the specified message move task.`aws sqs cancel-message-move-task \ --task-handle``AQEB6nR4...HzlvZQ==`Output: `{ "ApproximateNumberOfMessagesMoved": 102 }`For more information, see [Amazon SQS API permissions: Actions and resource reference](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-api-permissions-reference.html)in the*Developer Guide*.- 
                    For API details, see [CancelMessageMoveTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/cancel-message-move-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `change-message-visibility-batch`.

- **AWS CLI**
- 
            
                    **To change multiple messages' timeout visibilities as a batch**This example changes the 2 specified messages' timeout visibilities to 10 hours (10 hours * 60 minutes * 60 seconds). Command: `aws sqs change-message-visibility-batch --queue-url``https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue`--entries`file://change-message-visibility-batch.json`Input file (change-message-visibility-batch.json): `[ { "Id": "FirstMessage", "ReceiptHandle": "AQEBhz2q...Jf3kaw==", "VisibilityTimeout": 36000 }, { "Id": "SecondMessage", "ReceiptHandle": "AQEBkTUH...HifSnw==", "VisibilityTimeout": 36000 } ]`Output: `{ "Successful": [ { "Id": "SecondMessage" }, { "Id": "FirstMessage" } ] }`- 
                    For API details, see [ChangeMessageVisibilityBatch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/change-message-visibility-batch.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `change-message-visibility`.

- **AWS CLI**
- 
            
                    **To change a message's timeout visibility**This example changes the specified message's timeout visibility to 10 hours (10 hours * 60 minutes * 60 seconds). Command: `aws sqs change-message-visibility --queue-url``https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue`--receipt-handle`AQEBTpyI...t6HyQg==`--visibility-timeout`36000`Output: `None.`- 
                    For API details, see [ChangeMessageVisibility](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/change-message-visibility.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-queue`.

- **AWS CLI**
- 
            
                    **To create a queue**This example creates a queue with the specified name, sets the message retention period to 3 days (3 days * 24 hours * 60 minutes * 60 seconds), and sets the queue's dead letter queue to the specified queue with a maximum receive count of 1,000 messages. Command: `aws sqs create-queue --queue-name``MyQueue`--attributes`file://create-queue.json`Input file (create-queue.json): `{ "RedrivePolicy": "{\"deadLetterTargetArn\":\"arn:aws:sqs:us-east-1:80398EXAMPLE:MyDeadLetterQueue\",\"maxReceiveCount\":\"1000\"}", "MessageRetentionPeriod": "259200" }`Output: `{ "QueueUrl": "https://queue.amazonaws.com/80398EXAMPLE/MyQueue" }`- 
                    For API details, see [CreateQueue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/create-queue.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-message-batch`.

- **AWS CLI**
- 
            
                    **To delete multiple messages as a batch**This example deletes the specified messages. Command: `aws sqs delete-message-batch --queue-url``https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue`--entries`file://delete-message-batch.json`Input file (delete-message-batch.json): `[ { "Id": "FirstMessage", "ReceiptHandle": "AQEB1mgl...Z4GuLw==" }, { "Id": "SecondMessage", "ReceiptHandle": "AQEBLsYM...VQubAA==" } ]`Output: `{ "Successful": [ { "Id": "FirstMessage" }, { "Id": "SecondMessage" } ] }`- 
                    For API details, see [DeleteMessageBatch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/delete-message-batch.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-message`.

- **AWS CLI**
- 
            
                    **To delete a message**This example deletes the specified message. Command: `aws sqs delete-message --queue-url``https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue`--receipt-handle`AQEBRXTo...q2doVA==`Output: `None.`- 
                    For API details, see [DeleteMessage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/delete-message.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-queue`.

- **AWS CLI**
- 
            
                    **To delete a queue**This example deletes the specified queue. Command: `aws sqs delete-queue --queue-url``https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyNewerQueue`Output: `None.`- 
                    For API details, see [DeleteQueue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/delete-queue.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-queue-attributes`.

- **AWS CLI**
- 
            
                    **To get a queue's attributes**This example gets all of the specified queue's attributes. Command: `aws sqs get-queue-attributes --queue-url``https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue`--attribute-names`All`Output: `{ "Attributes": { "ApproximateNumberOfMessagesNotVisible": "0", "RedrivePolicy": "{\"deadLetterTargetArn\":\"arn:aws:sqs:us-east-1:80398EXAMPLE:MyDeadLetterQueue\",\"maxReceiveCount\":1000}", "MessageRetentionPeriod": "345600", "ApproximateNumberOfMessagesDelayed": "0", "MaximumMessageSize": "262144", "CreatedTimestamp": "1442426968", "ApproximateNumberOfMessages": "0", "ReceiveMessageWaitTimeSeconds": "0", "DelaySeconds": "0", "VisibilityTimeout": "30", "LastModifiedTimestamp": "1442426968", "QueueArn": "arn:aws:sqs:us-east-1:80398EXAMPLE:MyNewQueue" } }`This example gets only the specified queue's maximum message size and visibility timeout attributes. Command: `aws sqs get-queue-attributes --queue-url``https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyNewQueue`--attribute-names`MaximumMessageSize``VisibilityTimeout`Output: `{ "Attributes": { "VisibilityTimeout": "30", "MaximumMessageSize": "262144" } }`- 
                    For API details, see [GetQueueAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/get-queue-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-queue-url`.

- **AWS CLI**
- 
            
                    **To get a queue URL**This example gets the specified queue's URL. Command: `aws sqs get-queue-url --queue-name``MyQueue`Output: `{ "QueueUrl": "https://queue.amazonaws.com/80398EXAMPLE/MyQueue" }`- 
                    For API details, see [GetQueueUrl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/get-queue-url.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-dead-letter-source-queues`.

- **AWS CLI**
- 
            
                    **To list dead letter source queues**This example lists the queues that are associated with the specified dead letter source queue. Command: `aws sqs list-dead-letter-source-queues --queue-url``https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyDeadLetterQueue`Output: `{ "queueUrls": [ "https://queue.amazonaws.com/80398EXAMPLE/MyQueue", "https://queue.amazonaws.com/80398EXAMPLE/MyOtherQueue" ] }`- 
                    For API details, see [ListDeadLetterSourceQueues](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/list-dead-letter-source-queues.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-message-move-tasks`.

- **AWS CLI**
- 
            
                    **To list the message move tasks**The following `list-message-move-tasks`example lists the 2 most recent message move tasks in the specified queue.`aws sqs list-message-move-tasks \ --source-arn``arn:aws:sqs:us-west-2:80398EXAMPLE:MyQueue`\ --max-results`2`Output: `{ "Results": [ { "TaskHandle": "AQEB6nR4...HzlvZQ==", "Status": "RUNNING", "SourceArn": "arn:aws:sqs:us-west-2:80398EXAMPLE:MyQueue1", "DestinationArn": "arn:aws:sqs:us-west-2:80398EXAMPLE:MyQueue2", "MaxNumberOfMessagesPerSecond": 50, "ApproximateNumberOfMessagesMoved": 203, "ApproximateNumberOfMessagesToMove": 30, "StartedTimestamp": 1442428276921 }, { "Status": "COMPLETED", "SourceArn": "arn:aws:sqs:us-west-2:80398EXAMPLE:MyQueue1", "DestinationArn": "arn:aws:sqs:us-west-2:80398EXAMPLE:MyQueue2", "ApproximateNumberOfMessagesMoved": 29, "ApproximateNumberOfMessagesToMove": 0, "StartedTimestamp": 1342428272093 } ] }`For more information, see [Amazon SQS API permissions: Actions and resource reference](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-api-permissions-reference.html)in the*Developer Guide*.- 
                    For API details, see [ListMessageMoveTasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/list-message-move-tasks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-queue-tags`.

- **AWS CLI**
- 
            
                    **To list all cost allocation tags for a queue**The following `list-queue-tags`example displays all of the cost allocation tags associated with the specified queue.`aws sqs list-queue-tags \ --queue-url``https://sqs.us-west-2.amazonaws.com/123456789012/MyQueue`Output: `{ "Tags": { "Team": "Alpha" } }`For more information, see [Listing Cost Allocation Tags](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-tags.html)in the*Amazon Simple Queue Service Developer Guide*.- 
                    For API details, see [ListQueueTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/list-queue-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-queues`.

- **AWS CLI**
- 
            
                    **To list queues**This example lists all queues. Command: `aws sqs list-queues`Output: `{ "QueueUrls": [ "https://queue.amazonaws.com/80398EXAMPLE/MyDeadLetterQueue", "https://queue.amazonaws.com/80398EXAMPLE/MyQueue", "https://queue.amazonaws.com/80398EXAMPLE/MyOtherQueue", "https://queue.amazonaws.com/80398EXAMPLE/TestQueue1", "https://queue.amazonaws.com/80398EXAMPLE/TestQueue2" ] }`This example lists only queues that start with "My". Command: `aws sqs list-queues --queue-name-prefix``My`Output: `{ "QueueUrls": [ "https://queue.amazonaws.com/80398EXAMPLE/MyDeadLetterQueue", "https://queue.amazonaws.com/80398EXAMPLE/MyQueue", "https://queue.amazonaws.com/80398EXAMPLE/MyOtherQueue" ] }`- 
                    For API details, see [ListQueues](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/list-queues.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `purge-queue`.

- **AWS CLI**
- 
            
                    **To purge a queue**This example deletes all messages in the specified queue. Command: `aws sqs purge-queue --queue-url``https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyNewQueue`Output: `None.`- 
                    For API details, see [PurgeQueue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/purge-queue.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `receive-message`.

- **AWS CLI**
- 
            
                    **To receive a message**This example receives up to 10 available messages, returning all available attributes. Command: `aws sqs receive-message --queue-url``https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue`--attribute-names`All`--message-attribute-names`All`--max-number-of-messages`10`Output: `{ "Messages": [ { "Body": "My first message.", "ReceiptHandle": "AQEBzbVv...fqNzFw==", "MD5OfBody": "1000f835...a35411fa", "MD5OfMessageAttributes": "9424c491...26bc3ae7", "MessageId": "d6790f8d-d575-4f01-bc51-40122EXAMPLE", "Attributes": { "ApproximateFirstReceiveTimestamp": "1442428276921", "SenderId": "AIDAIAZKMSNQ7TEXAMPLE", "ApproximateReceiveCount": "5", "SentTimestamp": "1442428276921" }, "MessageAttributes": { "PostalCode": { "DataType": "String", "StringValue": "ABC123" }, "City": { "DataType": "String", "StringValue": "Any City" } } } ] }`This example receives the next available message, returning only the SenderId and SentTimestamp attributes as well as the PostalCode message attribute. Command: `aws sqs receive-message --queue-url``https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue`--attribute-names`SenderId``SentTimestamp`--message-attribute-names`PostalCode`Output: `{ "Messages": [ { "Body": "My first message.", "ReceiptHandle": "AQEB6nR4...HzlvZQ==", "MD5OfBody": "1000f835...a35411fa", "MD5OfMessageAttributes": "b8e89563...e088e74f", "MessageId": "d6790f8d-d575-4f01-bc51-40122EXAMPLE", "Attributes": { "SenderId": "AIDAIAZKMSNQ7TEXAMPLE", "SentTimestamp": "1442428276921" }, "MessageAttributes": { "PostalCode": { "DataType": "String", "StringValue": "ABC123" } } } ] }`- 
                    For API details, see [ReceiveMessage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/receive-message.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-permission`.

- **AWS CLI**
- 
            
                    **To remove a permission**This example removes the permission with the specified label from the specified queue. Command: `aws sqs remove-permission --queue-url``https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue`--label`SendMessagesFromMyQueue`Output: `None.`- 
                    For API details, see [RemovePermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/remove-permission.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `send-message-batch`.

- **AWS CLI**
- 
            
                    **To send multiple messages as a batch**This example sends 2 messages with the specified message bodies, delay periods, and message attributes, to the specified queue. Command: `aws sqs send-message-batch --queue-url``https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue`--entries`file://send-message-batch.json`Input file (send-message-batch.json): `[ { "Id": "FuelReport-0001-2015-09-16T140731Z", "MessageBody": "Fuel report for account 0001 on 2015-09-16 at 02:07:31 PM.", "DelaySeconds": 10, "MessageAttributes": { "SellerName": { "DataType": "String", "StringValue": "Example Store" }, "City": { "DataType": "String", "StringValue": "Any City" }, "Region": { "DataType": "String", "StringValue": "WA" }, "PostalCode": { "DataType": "String", "StringValue": "99065" }, "PricePerGallon": { "DataType": "Number", "StringValue": "1.99" } } }, { "Id": "FuelReport-0002-2015-09-16T140930Z", "MessageBody": "Fuel report for account 0002 on 2015-09-16 at 02:09:30 PM.", "DelaySeconds": 10, "MessageAttributes": { "SellerName": { "DataType": "String", "StringValue": "Example Fuels" }, "City": { "DataType": "String", "StringValue": "North Town" }, "Region": { "DataType": "String", "StringValue": "WA" }, "PostalCode": { "DataType": "String", "StringValue": "99123" }, "PricePerGallon": { "DataType": "Number", "StringValue": "1.87" } } } ]`Output: `{ "Successful": [ { "MD5OfMessageBody": "203c4a38...7943237e", "MD5OfMessageAttributes": "10809b55...baf283ef", "Id": "FuelReport-0001-2015-09-16T140731Z", "MessageId": "d175070c-d6b8-4101-861d-adeb3EXAMPLE" }, { "MD5OfMessageBody": "2cf0159a...c1980595", "MD5OfMessageAttributes": "55623928...ae354a25", "Id": "FuelReport-0002-2015-09-16T140930Z", "MessageId": "f9b7d55d-0570-413e-b9c5-a9264EXAMPLE" } ] }`- 
                    For API details, see [SendMessageBatch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/send-message-batch.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `send-message`.

- **AWS CLI**
- 
            
                    **To send a message**This example sends a message with the specified message body, delay period, and message attributes, to the specified queue. Command: `aws sqs send-message --queue-url``https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyQueue`--message-body`"Information about the largest city in Any Region."`--delay-seconds`10`--message-attributes`file://send-message.json`Input file (send-message.json): `{ "City": { "DataType": "String", "StringValue": "Any City" }, "Greeting": { "DataType": "Binary", "BinaryValue": "Hello, World!" }, "Population": { "DataType": "Number", "StringValue": "1250800" } }`Output: `{ "MD5OfMessageBody": "51b0a325...39163aa0", "MD5OfMessageAttributes": "00484c68...59e48f06", "MessageId": "da68f62c-0c07-4bee-bf5f-7e856EXAMPLE" }`- 
                    For API details, see [SendMessage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/send-message.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-queue-attributes`.

- **AWS CLI**
- 
            
                    **To set queue attributes**This example sets the specified queue to a delivery delay of 10 seconds, a maximum message size of 128 KB (128 KB * 1,024 bytes), a message retention period of 3 days (3 days * 24 hours * 60 minutes * 60 seconds), a receive message wait time of 20 seconds, and a default visibility timeout of 60 seconds. This example also associates the specified dead letter queue with a maximum receive count of 1,000 messages. Command: `aws sqs set-queue-attributes --queue-url``https://sqs.us-east-1.amazonaws.com/80398EXAMPLE/MyNewQueue`--attributes`file://set-queue-attributes.json`Input file (set-queue-attributes.json): `{ "DelaySeconds": "10", "MaximumMessageSize": "131072", "MessageRetentionPeriod": "259200", "ReceiveMessageWaitTimeSeconds": "20", "RedrivePolicy": "{\"deadLetterTargetArn\":\"arn:aws:sqs:us-east-1:80398EXAMPLE:MyDeadLetterQueue\",\"maxReceiveCount\":\"1000\"}", "VisibilityTimeout": "60" }`Output: `None.`- 
                    For API details, see [SetQueueAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/set-queue-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-message-move-task`.

- **AWS CLI**
- 
            
                    *Example 1: *To start a message move task**The following `start-message-move-task`example starts a message move task to redrive messages from the specified dead-letter queue to the source queue.`aws sqs start-message-move-task \ --source-arn``arn:aws:sqs:us-west-2:80398EXAMPLE:MyQueue`Output: `{ "TaskHandle": "AQEB6nR4...HzlvZQ==" }`For more information, see [This is the topic title](https://link.to.the/topic/page)in the*Name of your guide*.*Example 2: *To start a message move task with a maximum rate**The following `start-message-move-task`example starts a message move task to redrive messages from the specified dead-letter queue to the specified destination queue at a maximum rate of 50 messages per second.`aws sqs start-message-move-task \ --source-arn``arn:aws:sqs:us-west-2:80398EXAMPLE:MyQueue1`\ --destination-arn`arn:aws:sqs:us-west-2:80398EXAMPLE:MyQueue2`\ --max-number-of-messages-per-second`50`Output: `{ "TaskHandle": "AQEB6nR4...HzlvZQ==" }`For more information, see [Amazon SQS API permissions: Actions and resource reference](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-api-permissions-reference.html)in the*Developer Guide*.- 
                    For API details, see [StartMessageMoveTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/start-message-move-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-queue`.

- **AWS CLI**
- 
            
                    **To add cost allocation tags to a queue**The following `tag-queue`example adds a cost allocation tag to the specified Amazon SQS queue.`aws sqs tag-queue \ --queue-url``https://sqs.us-west-2.amazonaws.com/123456789012/MyQueue`\ --tags`Priority=Highest`This command produces no output. For more information, see [Adding Cost Allocation Tags](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-tags.html)in the*Amazon Simple Queue Service Developer Guide*.- 
                    For API details, see [TagQueue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/tag-queue.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-queue`.

- **AWS CLI**
- 
            
                    **To remove cost allocation tags from a queue**The following `untag-queue`example removes a cost allocation tag from the specified Amazon SQS queue.`aws sqs untag-queue \ --queue-url``https://sqs.us-west-2.amazonaws.com/123456789012/MyQueue`\ --tag-keys`"Priority"`This command produces no output. For more information, see [Adding Cost Allocation Tags](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-tags.html)in the*Amazon Simple Queue Service Developer Guide*.- 
                    For API details, see [UntagQueue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/untag-queue.html)in*AWS CLI Command Reference*.
 
-