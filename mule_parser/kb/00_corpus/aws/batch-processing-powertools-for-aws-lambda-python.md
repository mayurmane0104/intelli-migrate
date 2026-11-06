# Batch Processing - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/utilities/batch](https://docs.aws.amazon.com/powertools/python/latest/utilities/batch)

---

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies.

If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Customize cookie preferences

We use cookies and similar tools (collectively, "cookies") for the following purposes.

Essential

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

Allowed

Performance

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Allowed

Functional

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Allowed

Advertising

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Allowed

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the AWS Cookie Notice.

Your privacy choices

We and our advertising partners (“we”) may use information we collect from or about you to show you ads on other websites and online services. Under certain laws, this activity is referred to as “cross-context behavioral advertising” or “targeted advertising.”

To opt out of our use of cookies or similar technologies to engage in these activities, select “Opt out of cross-context behavioral ads” and “Save preferences” below. If you clear your browser cookies or visit this site from a different device or browser, you will need to make your selection again. For more information about cookies and how we use them, read our Cookie Notice.

To opt out of the use of other identifiers, such as contact information, for these activities, fill out the form here.

For more information about how AWS handles your information, read the AWS Privacy Notice.

Unable to save cookie preferences

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

The batch processing utility handles partial failures when processing batches from Amazon SQS, Amazon Kinesis Data Streams, Amazon DynamoDB Streams, and Amazon MSK/self-managed Apache Kafka.

When using SQS, Kinesis Data Streams, DynamoDB Streams, or Amazon MSK/Apache Kafka as a Lambda event source, your Lambda functions are triggered with a batch of messages.

If your function fails to process any message from the batch, the entire batch returns to your queue or stream. This same batch is then retried until either condition happens first: a) your Lambda function returns a successful response, b) record reaches maximum retry attempts, or c) records expire.

This behavior changes when you enable Report Batch Item Failures feature in your Lambda function event source configuration:

SQS queues. Only messages reported as failure will return to the queue for a retry, while successful ones will be deleted.

Kinesis data streams and DynamoDB streams. Single reported failure will use its sequence number as the stream checkpoint. Multiple reported failures will use the lowest sequence number as checkpoint.

Kafka (MSK and self-managed). Failed records are identified by topic-partition and offset. Only failed records will be retried.

Warning: This utility lowers the chance of processing records more than once; it does not guarantee it

We recommend implementing processing logic in an idempotent manner wherever possible.

You can find more details on how Lambda works with either SQS, Kinesis, DynamoDB, or MSK/Kafka in the AWS Documentation.

For this feature to work, you need to (1) configure your Lambda function event source to use ReportBatchItemFailures, and (2) return a specific response to report which records failed to be processed.

You use your preferred deployment framework to set the correct configuration while this utility handles the correct response to be returned.

The remaining sections of the documentation will rely on these samples. For completeness, this demonstrates IAM permissions and Dead Letter Queue where batch records will be sent after 2 retries were attempted.

You do not need any additional IAM permissions to use this utility, except for what each event source requires.

AWSTemplateFormatVersion:"2010-09-09"Transform:AWS::Serverless-2016-10-31Description:partial batch response sampleGlobals:Function:Timeout:5MemorySize:256Runtime:python3.12Tracing:ActiveEnvironment:Variables:POWERTOOLS_LOG_LEVEL:INFOPOWERTOOLS_SERVICE_NAME:helloResources:HelloWorldFunction:Type:AWS::Serverless::FunctionProperties:Handler:app.lambda_handlerCodeUri:hello_worldPolicies:# Lambda Destinations require additional permissions# to send failure records to DLQ from Kinesis/DynamoDB-Version:"2012-10-17"Statement:Effect:"Allow"Action:-sqs:GetQueueAttributes-sqs:GetQueueUrl-sqs:SendMessageResource:!GetAttSampleDLQ.ArnEvents:KinesisStream:Type:KinesisProperties:Stream:!GetAttSampleStream.ArnBatchSize:100StartingPosition:LATESTMaximumRetryAttempts:2DestinationConfig:OnFailure:Destination:!GetAttSampleDLQ.ArnFunctionResponseTypes:-ReportBatchItemFailuresSampleDLQ:Type:AWS::SQS::QueueSampleStream:Type:AWS::Kinesis::StreamProperties:ShardCount:1StreamEncryption:EncryptionType:KMSKeyId:alias/aws/kinesis

AWSTemplateFormatVersion:'2010-09-09'Transform:AWS::Serverless-2016-10-31Description:partial batch response sampleGlobals:Function:Timeout:5MemorySize:256Runtime:python3.12Tracing:ActiveEnvironment:Variables:POWERTOOLS_LOG_LEVEL:INFOPOWERTOOLS_SERVICE_NAME:helloResources:HelloWorldFunction:Type:AWS::Serverless::FunctionProperties:Handler:app.lambda_handlerCodeUri:hello_worldPolicies:# Lambda Destinations require additional permissions# to send failure records from Kinesis/DynamoDB-Version:"2012-10-17"Statement:Effect:"Allow"Action:-sqs:GetQueueAttributes-sqs:GetQueueUrl-sqs:SendMessageResource:!GetAttSampleDLQ.ArnEvents:DynamoDBStream:Type:DynamoDBProperties:Stream:!GetAttSampleTable.StreamArnStartingPosition:LATESTMaximumRetryAttempts:2DestinationConfig:OnFailure:Destination:!GetAttSampleDLQ.ArnFunctionResponseTypes:-ReportBatchItemFailuresSampleDLQ:Type:AWS::SQS::QueueSampleTable:Type:AWS::DynamoDB::TableProperties:BillingMode:PAY_PER_REQUESTAttributeDefinitions:-AttributeName:pkAttributeType:S-AttributeName:skAttributeType:SKeySchema:-AttributeName:pkKeyType:HASH-AttributeName:skKeyType:RANGESSESpecification:SSEEnabled:trueStreamSpecification:StreamViewType:NEW_AND_OLD_IMAGES

AWSTemplateFormatVersion:"2010-09-09"Transform:AWS::Serverless-2016-10-31Description:Kafka/MSK partial batch response sampleGlobals:Function:Timeout:30MemorySize:256Runtime:python3.12Tracing:ActiveEnvironment:Variables:POWERTOOLS_LOG_LEVEL:INFOPOWERTOOLS_SERVICE_NAME:kafka-processorParameters:MSKClusterArn:Type:StringDescription:ARN of the MSK clusterKafkaTopic:Type:StringDescription:Name of the Kafka topic to consume fromDefault:mytopicResources:KafkaConsumerFunction:Type:AWS::Serverless::FunctionProperties:Handler:app.lambda_handlerCodeUri:hello_worldPolicies:# Permissions for MSK-Version:"2012-10-17"Statement:-Effect:"Allow"Action:-kafka:DescribeCluster-kafka:DescribeClusterV2-kafka:GetBootstrapBrokersResource:!RefMSKClusterArn-Effect:"Allow"Action:-kafka-cluster:Connect-kafka-cluster:DescribeGroup-kafka-cluster:AlterGroup-kafka-cluster:DescribeTopic-kafka-cluster:ReadData-kafka-cluster:DescribeClusterDynamicConfigurationResource:-!RefMSKClusterArn-!Sub"${MSKClusterArn}/*"# Lambda Destinations require additional permissions# to send failure records to DLQ-Version:"2012-10-17"Statement:Effect:"Allow"Action:-sqs:GetQueueAttributes-sqs:GetQueueUrl-sqs:SendMessageResource:!GetAttSampleDLQ.ArnEvents:MSKEvent:Type:MSKProperties:Stream:!RefMSKClusterArnTopics:-!RefKafkaTopicStartingPosition:LATESTBatchSize:100MaximumBatchingWindowInSeconds:5DestinationConfig:OnFailure:Destination:!GetAttSampleDLQ.ArnFunctionResponseTypes:-ReportBatchItemFailuresSampleDLQ:Type:AWS::SQS::QueueOutputs:KafkaConsumerFunctionArn:Description:"KafkaConsumerLambdaFunctionARN"Value:!GetAttKafkaConsumerFunction.ArnSampleDLQUrl:Description:"DeadLetterQueueURL"Value:!RefSampleDLQ

fromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.utilities.batchimport(BatchProcessor,EventType,process_partial_response,)fromaws_lambda_powertools.utilities.data_classes.sqs_eventimportSQSRecordfromaws_lambda_powertools.utilities.typingimportLambdaContextprocessor=BatchProcessor(event_type=EventType.SQS)tracer=Tracer()logger=Logger()@tracer.capture_methoddefrecord_handler(record:SQSRecord):payload:str=record.json_body# if json string data, otherwise record.body for strlogger.info(payload)@logger.inject_lambda_context@tracer.capture_lambda_handlerdeflambda_handler(event,context:LambdaContext):returnprocess_partial_response(event=event,record_handler=record_handler,processor=processor,context=context,)

When working with SQS FIFO queues, a batch may include messages from different group IDs.

By default, we will stop processing at the first failure and mark unprocessed messages as failed to preserve ordering. However, this behavior may not be optimal for customers who wish to proceed with processing messages from a different group ID.

Enable the skip_group_on_error option for seamless processing of messages from various group IDs. This setup ensures that messages from a failed group ID are sent back to SQS, enabling uninterrupted processing of messages from the subsequent group ID.

1 2 3 4 5 6 7 8 91011121314151617181920212223

fromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.utilities.batchimport(SqsFifoPartialProcessor,process_partial_response,)fromaws_lambda_powertools.utilities.data_classes.sqs_eventimportSQSRecordfromaws_lambda_powertools.utilities.typingimportLambdaContextprocessor=SqsFifoPartialProcessor()tracer=Tracer()logger=Logger()@tracer.capture_methoddefrecord_handler(record:SQSRecord):payload:str=record.json_body# if json string data, otherwise record.body for strlogger.info(payload)@logger.inject_lambda_context@tracer.capture_lambda_handlerdeflambda_handler(event,context:LambdaContext):returnprocess_partial_response(event=event,record_handler=record_handler,processor=processor,context=context)

importjsonfromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.utilities.batchimportSqsFifoPartialProcessorfromaws_lambda_powertools.utilities.data_classes.sqs_eventimportSQSRecordfromaws_lambda_powertools.utilities.typingimportLambdaContextprocessor=SqsFifoPartialProcessor()tracer=Tracer()logger=Logger()@tracer.capture_methoddefrecord_handler(record:SQSRecord):payload:str=record.bodyifpayload:item:dict=json.loads(payload)logger.info(item)@logger.inject_lambda_context@tracer.capture_lambda_handlerdeflambda_handler(event,context:LambdaContext):batch=event["Records"]withprocessor(records=batch,handler=record_handler):processor.process()# kick off processing, return List[Tuple]returnprocessor.response()

1 2 3 4 5 6 7 8 91011121314151617181920212223

fromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.utilities.batchimport(SqsFifoPartialProcessor,process_partial_response,)fromaws_lambda_powertools.utilities.data_classes.sqs_eventimportSQSRecordfromaws_lambda_powertools.utilities.typingimportLambdaContextprocessor=SqsFifoPartialProcessor(skip_group_on_error=True)tracer=Tracer()logger=Logger()@tracer.capture_methoddefrecord_handler(record:SQSRecord):payload:str=record.json_body# if json string data, otherwise record.body for strlogger.info(payload)@logger.inject_lambda_context@tracer.capture_lambda_handlerdeflambda_handler(event,context:LambdaContext):returnprocess_partial_response(event=event,record_handler=record_handler,processor=processor,context=context)

fromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.utilities.batchimport(BatchProcessor,EventType,process_partial_response,)fromaws_lambda_powertools.utilities.data_classes.kafka_eventimport(KafkaEventRecord,)fromaws_lambda_powertools.utilities.typingimportLambdaContextprocessor=BatchProcessor(event_type=EventType.Kafka)tracer=Tracer()logger=Logger()@tracer.capture_methoddefrecord_handler(record:KafkaEventRecord):logger.info(f"Processing record from topic: {record.topic}, partition: {record.partition}, offset: {record.offset}")payload:dict=record.json_valuelogger.info(payload)@logger.inject_lambda_context@tracer.capture_lambda_handlerdeflambda_handler(event,context:LambdaContext):returnprocess_partial_response(event=event,record_handler=record_handler,processor=processor,context=context)

The second record failed to be processed, therefore the processor added its topic-partition and offset in the response.

By default, we catch any exception raised by your record handler function. This allows us to (1) continue processing the batch, (2) collect each batch item that failed processing, and (3) return the appropriate response correctly without failing your Lambda function execution.

fromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.utilities.batchimport(BatchProcessor,EventType,process_partial_response,)fromaws_lambda_powertools.utilities.data_classes.sqs_eventimportSQSRecordfromaws_lambda_powertools.utilities.typingimportLambdaContextprocessor=BatchProcessor(event_type=EventType.SQS)tracer=Tracer()logger=Logger()classInvalidPayload(Exception):...@tracer.capture_methoddefrecord_handler(record:SQSRecord):payload:str=record.bodylogger.info(payload)ifnotpayload:raiseInvalidPayload("Payload does not contain minimum information to be processed.")@logger.inject_lambda_context@tracer.capture_lambda_handlerdeflambda_handler(event,context:LambdaContext):returnprocess_partial_response(event=event,record_handler=record_handler,processor=processor,context=context,)

You can use AsyncBatchProcessor class and async_process_partial_response function to process messages concurrently.

When is this useful?

Your use case might be able to process multiple records at the same time without conflicting with one another.

For example, imagine you need to process multiple loyalty points and incrementally save them in the database. While you await the database to confirm your records are saved, you could start processing another request concurrently.

The reason this is not the default behaviour is that not all use cases can handle concurrency safely (e.g., loyalty points must be updated in order).

importhttpx# external dependencyfromaws_lambda_powertools.utilities.batchimport(AsyncBatchProcessor,EventType,async_process_partial_response,)fromaws_lambda_powertools.utilities.data_classes.sqs_eventimportSQSRecordfromaws_lambda_powertools.utilities.typingimportLambdaContextprocessor=AsyncBatchProcessor(event_type=EventType.SQS)asyncdefasync_record_handler(record:SQSRecord):# Yield control back to the event loop to schedule other tasks# while you await from a response from httpbin.orgasyncwithhttpx.AsyncClient()asclient:ret=awaitclient.get("https://httpbin.org/get")returnret.status_codedeflambda_handler(event,context:LambdaContext):returnasync_process_partial_response(event=event,record_handler=async_record_handler,processor=processor,context=context,)

You can bring your own Pydantic models via model parameter when inheriting from SqsRecordModel, KinesisDataStreamRecord, or DynamoDBStreamRecordModel

Inheritance is importance because we need to access message IDs and sequence numbers from these records in the event of failure. Mypy is fully integrated with this utility, so it should identify whether you're passing the incorrect Model.

fromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.utilities.batchimport(BatchProcessor,EventType,process_partial_response,)fromaws_lambda_powertools.utilities.parserimportBaseModelfromaws_lambda_powertools.utilities.parser.modelsimportSqsRecordModelfromaws_lambda_powertools.utilities.parser.typesimportJsonfromaws_lambda_powertools.utilities.typingimportLambdaContextclassOrder(BaseModel):item:dictclassOrderSqsRecord(SqsRecordModel):# type: ignore[override]body:Json[Order]# deserialize order data from JSON stringprocessor=BatchProcessor(event_type=EventType.SQS,model=OrderSqsRecord)tracer=Tracer()logger=Logger()@tracer.capture_methoddefrecord_handler(record:OrderSqsRecord):logger.info(record.body.item)returnrecord.body.item@logger.inject_lambda_context@tracer.capture_lambda_handlerdeflambda_handler(event,context:LambdaContext):returnprocess_partial_response(event=event,record_handler=record_handler,processor=processor,context=context)

importjsonfromtypingimportDict,Optionalfromtyping_extensionsimportLiteralfromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.utilities.batchimport(BatchProcessor,EventType,process_partial_response,)fromaws_lambda_powertools.utilities.parserimportBaseModel,field_validatorfromaws_lambda_powertools.utilities.parser.modelsimport(DynamoDBStreamChangedRecordModel,DynamoDBStreamRecordModel,)fromaws_lambda_powertools.utilities.typingimportLambdaContextclassOrder(BaseModel):item:dictclassOrderDynamoDB(BaseModel):Message:Order# auto transform json string# so Pydantic can auto-initialize nested Order model@field_validator("Message",mode="before")deftransform_message_to_dict(cls,value:Dict[Literal["S"],str]):returnjson.loads(value["S"])classOrderDynamoDBChangeRecord(DynamoDBStreamChangedRecordModel):# type: ignore[override]NewImage:Optional[OrderDynamoDB]OldImage:Optional[OrderDynamoDB]classOrderDynamoDBRecord(DynamoDBStreamRecordModel):# type: ignore[override]dynamodb:OrderDynamoDBChangeRecordprocessor=BatchProcessor(event_type=EventType.DynamoDBStreams,model=OrderDynamoDBRecord)tracer=Tracer()logger=Logger()@tracer.capture_methoddefrecord_handler(record:OrderDynamoDBRecord):ifrecord.dynamodb.NewImageandrecord.dynamodb.NewImage.Message:logger.info(record.dynamodb.NewImage.Message.item)returnrecord.dynamodb.NewImage.Message.item@logger.inject_lambda_context@tracer.capture_lambda_handlerdeflambda_handler(event,context:LambdaContext):returnprocess_partial_response(event=event,record_handler=record_handler,processor=processor,context=context)

By default, the BatchProcessor will raise BatchProcessingError if all records in the batch fail to process, we do this to reflect the failure in your operational metrics.

When working with functions that handle batches with a small number of records, or when you use errors as a flow control mechanism, this behavior might not be desirable as your function might generate an unnaturally high number of errors. When this happens, the Lambda service will scale down the concurrency of your function, potentially impacting performance.

For these scenarios, you can set the raise_on_entire_batch_failure option to False.

fromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.utilities.batchimport(BatchProcessor,EventType,process_partial_response,)fromaws_lambda_powertools.utilities.data_classes.sqs_eventimportSQSRecordfromaws_lambda_powertools.utilities.typingimportLambdaContextprocessor=BatchProcessor(event_type=EventType.SQS,raise_on_entire_batch_failure=False)tracer=Tracer()logger=Logger()@tracer.capture_methoddefrecord_handler(record:SQSRecord):payload:str=record.json_body# if json string data, otherwise record.body for strlogger.info(payload)@logger.inject_lambda_context@tracer.capture_lambda_handlerdeflambda_handler(event,context:LambdaContext):returnprocess_partial_response(event=event,record_handler=record_handler,processor=processor,context=context,)

Use the context manager to access a list of all returned values from your record_handler function.

When successful. We include a tuple with 1/success, 2/ the result of record_handler, and 3/ the batch item

When failed. We include a tuple with 1/fail, 2/ exception as a string, and 3/ the batch item serialized as Event Source Data Class or Pydantic model.

If a Pydantic model fails validation early, we serialize its failure record as Event Source Data Class to be able to collect message ID/sequence numbers etc.

[("fail","<class 'Exception': Failed to process record",<aws_lambda_powertools.utilities.data_classes.sqs_event.SQSRecordobjectat0x103c590a0>),("success","success",{'messageId':'88891c36-32eb-4a25-9905-654a32916893','receiptHandle':'AQEBwJnKyrHigUMZj6rYigCgxlaS3SLy0a','body':'success','attributes':{'ApproximateReceiveCount':'1','SentTimestamp':'1545082649183','SenderId':'AIDAIENQZJOLO23YVJ4VO','ApproximateFirstReceiveTimestamp':'1545082649185'},'messageAttributes':{},'md5OfBody':'e4e68fb7bd0e697a0ae8f1bb342846b3','eventSource':'aws:sqs','eventSourceARN':'arn:aws:sqs:us-east-2:123456789012:my-queue','awsRegion':'us-east-1'})]

Sample exception could have raised from within record_handler function.

1 2 3 4 5 6 7 8 91011121314151617

[("fail","<class 'pydantic.error_wrappers.ValidationError'>:1 validation error for OrderSqs\nbody\n JSON object must be str, bytes or bytearray (type=type_error.json)",<aws_lambda_powertools.utilities.data_classes.sqs_event.SQSRecordobjectat0x103c590a0>),("success","success",{'messageId':'88891c36-32eb-4a25-9905-654a32916893','receiptHandle':'AQEBwJnKyrHigUMZj6rYigCgxlaS3SLy0a','body':'success','attributes':{'ApproximateReceiveCount':'1','SentTimestamp':'1545082649183','SenderId':'AIDAIENQZJOLO23YVJ4VO','ApproximateFirstReceiveTimestamp':'1545082649185'},'messageAttributes':{},'md5OfBody':'e4e68fb7bd0e697a0ae8f1bb342846b3','eventSource':'aws:sqs','eventSourceARN':'arn:aws:sqs:us-east-2:123456789012:my-queue','awsRegion':'us-east-1'}),("fail","<class 'Exception'>:Failed to process record.",OrderSqs(messageId='9d0bfba5-d213-4b64-89bd-f4fbd7e58358',receiptHandle='AQEBwJnKyrHigUMZj6rYigCgxlaS3SLy0a',body=Order(item={'type':'fail'}),attributes=SqsAttributesModel(ApproximateReceiveCount='1',ApproximateFirstReceiveTimestamp=datetime.datetime(2018,12,17,21,37,29,185000,tzinfo=datetime.timezone.utc),MessageDeduplicationId=None,MessageGroupId=None,SenderId='AIDAIENQZJOLO23YVJ4VO',SentTimestamp=datetime.datetime(2018,12,17,21,37,29,183000,tzinfo=datetime.timezone.utc),SequenceNumber=None,AWSTraceHeader=None),messageAttributes={},md5OfBody='e4e68fb7bd0e697a0ae8f1bb342846b3',md5OfMessageAttributes=None,eventSource='aws:sqs',eventSourceARN='arn:aws:sqs:us-east-2:123456789012:my-queue',awsRegion='us-east-1'))]

Sample when a model fails validation early.

Batch item (3rd item) is serialized to the respective Event Source Data Class event type.

Sample when model validated successfully but another exception was raised during processing.

Within your record_handler function, you might need access to the Lambda context to determine how much time you have left before your function times out.

We can automatically inject the Lambda context into your record_handler if your function signature has a parameter named lambda_context. When using a context manager, you also need to pass the Lambda context object like in the example below.

You might want to bring custom logic to the existing BatchProcessor to slightly override how we handle successes and failures.

For these scenarios, you can subclass BatchProcessor and quickly override success_handler and failure_handler methods:

success_handler() is called for each successfully processed record

failure_handler() is called for each failed record

Note

These functions have a common record argument. For backward compatibility reasons, their type is not the same:

success_handler: record type is dict[str, Any], the raw record data.

failure_handler: record type can be an Event Source Data Class or your Pydantic model. During Pydantic validation errors, we fall back and serialize record to Event Source Data Class to not break the processing pipeline.

Let's suppose you'd like to add metrics to track successes and failures of your batch records.

Extending failure handling mechanism in BatchProcessor

You can create your own partial batch processor from scratch by inheriting the BasePartialProcessor class, and implementing _prepare(), _clean(), _process_record() and _async_process_record().

Visual representation to bring your own processor

_process_record() – handles all processing logic for each individual message of a batch, including calling the record_handler (self.handler)

_prepare() – called once as part of the processor initialization

_clean() – teardown logic called once after _process_record completes

_async_process_record() – If you need to implement asynchronous logic, use this method, otherwise define it in your class with empty logic

response() - called upon completion of processing

You can utilize this class to instantiate a new processor and then pass it to the process_partial_response function.

importcopyimportosimportsysfromrandomimportrandintfromtypingimportAnyimportboto3fromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.utilities.batchimport(BasePartialProcessor,process_partial_response,)fromaws_lambda_powertools.utilities.batch.typesimportPartialItemFailureResponsetable_name=os.getenv("TABLE_NAME","table_store_batch")logger=Logger()classMyPartialProcessor(BasePartialProcessor):DEFAULT_RESPONSE:PartialItemFailureResponse={"batchItemFailures":[]}""" Process a record and stores successful results at a Amazon DynamoDB Table Parameters ---------- table_name: str DynamoDB table name to write results to """def__init__(self,table_name:str):self.table_name=table_nameself.batch_response:PartialItemFailureResponse=copy.deepcopy(self.DEFAULT_RESPONSE)super().__init__()def_prepare(self):# It's called once, *before* processing# Creates table resource and clean previous resultsself.ddb_table=boto3.resource("dynamodb").Table(self.table_name)self.success_messages.clear()defresponse(self)->PartialItemFailureResponse:returnself.batch_responsedef_clean(self):# It's called once, *after* closing processing all records (closing the context manager)# Here we're sending, at once, all successful messages to a ddb tablewithself.ddb_table.batch_writer()asbatch:forresultinself.success_messages:batch.put_item(Item=result)def_process_record(self,record):# It handles how your record is processed# Here we're keeping the status of each run# where self.handler is the record_handler function passed as an argumenttry:result=self.handler(record)# record_handler passed to decorator/context managerreturnself.success_handler(record,result)exceptExceptionasexc:logger.error(exc)returnself.failure_handler(record,sys.exc_info())defsuccess_handler(self,record,result:Any):entry=("success",result,record)self.success_messages.append(record)returnentryasyncdef_async_process_record(self,record:dict):raiseNotImplementedError()processor=MyPartialProcessor(table_name)defrecord_handler(record):returnrandint(0,100)deflambda_handler(event,context):returnprocess_partial_response(event=event,record_handler=record_handler,processor=processor,context=context)

Tracer response auto-capture for large batch sizes¶

When using Tracer to capture responses for each batch record processing, you might exceed 64K of tracing data depending on what you return from your record_handler function, or how big is your batch size.

As there is no external calls, you can unit test your code with BatchProcessor quite easily.

Example:

Given a SQS batch where the first batch record succeeds and the second fails processing, we should have a single item reported in the function response.

Use context manager when you want access to the processed messages or handle BatchProcessingError exception when all records within the batch fail to be processed.

fromsentry_sdkimportcapture_exceptionfromaws_lambda_powertools.utilities.batchimportBatchProcessor,FailureResponseclassMyProcessor(BatchProcessor):deffailure_handler(self,record,exception)->FailureResponse:capture_exception()# send exception to Sentryreturnsuper().failure_handler(record,exception)