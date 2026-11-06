# Base - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/batch/base](https://docs.aws.amazon.com/powertools/python/latest/api_doc/batch/base)

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

def__init__(self,event_type:EventType,model:BatchTypeModels|None=None,raise_on_entire_batch_failure:bool=True,logger:logging.Logger|None=None,):"""Process batch and partially report failed items Parameters ---------- event_type: EventType Whether this is a SQS, DynamoDB Streams, or Kinesis Data Stream event model: BatchTypeModels | None Parser's data model using either SqsRecordModel, DynamoDBStreamRecordModel, KinesisDataStreamRecord raise_on_entire_batch_failure: bool Raise an exception when the entire batch has failed processing. When set to False, partial failures are reported in the response logger: logging.Logger | None Optional Logger instance to output warnings with tracebacks for failed records. Exceptions ---------- BatchProcessingError Raised when the entire batch has failed processing """self.event_type=event_typeself.model=modelself.raise_on_entire_batch_failure=raise_on_entire_batch_failureself.batch_response:PartialItemFailureResponse=copy.deepcopy(self.DEFAULT_RESPONSE)self._COLLECTOR_MAPPING={EventType.SQS:self._collect_sqs_failures,EventType.KinesisDataStreams:self._collect_kinesis_failures,EventType.DynamoDBStreams:self._collect_dynamodb_failures,EventType.Kafka:self._collect_kafka_failures,}self._DATA_CLASS_MAPPING={EventType.SQS:SQSRecord,EventType.KinesisDataStreams:KinesisStreamRecord,EventType.DynamoDBStreams:DynamoDBRecord,EventType.Kafka:KafkaEventRecord,}super().__init__(logger=logger)

def__init__(self,event_type:EventType,model:BatchTypeModels|None=None,raise_on_entire_batch_failure:bool=True,logger:logging.Logger|None=None,):"""Process batch and partially report failed items Parameters ---------- event_type: EventType Whether this is a SQS, DynamoDB Streams, or Kinesis Data Stream event model: BatchTypeModels | None Parser's data model using either SqsRecordModel, DynamoDBStreamRecordModel, KinesisDataStreamRecord raise_on_entire_batch_failure: bool Raise an exception when the entire batch has failed processing. When set to False, partial failures are reported in the response logger: logging.Logger | None Optional Logger instance to output warnings with tracebacks for failed records. Exceptions ---------- BatchProcessingError Raised when the entire batch has failed processing """self.event_type=event_typeself.model=modelself.raise_on_entire_batch_failure=raise_on_entire_batch_failureself.batch_response:PartialItemFailureResponse=copy.deepcopy(self.DEFAULT_RESPONSE)self._COLLECTOR_MAPPING={EventType.SQS:self._collect_sqs_failures,EventType.KinesisDataStreams:self._collect_kinesis_failures,EventType.DynamoDBStreams:self._collect_dynamodb_failures,EventType.Kafka:self._collect_kafka_failures,}self._DATA_CLASS_MAPPING={EventType.SQS:SQSRecord,EventType.KinesisDataStreams:KinesisStreamRecord,EventType.DynamoDBStreams:DynamoDBRecord,EventType.Kafka:KafkaEventRecord,}super().__init__(logger=logger)

We keep the outer function synchronous to prevent making Lambda handler async, so to not impact
customers' existing middlewares. Instead, we create an async closure to handle asynchrony.

We also handle edge cases like Lambda container thaw by getting an existing or creating an event loop.

defasync_process(self)->list[tuple]:""" Async call instance's handler for each record. Note ---- We keep the outer function synchronous to prevent making Lambda handler async, so to not impact customers' existing middlewares. Instead, we create an async closure to handle asynchrony. We also handle edge cases like Lambda container thaw by getting an existing or creating an event loop. See: https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html#runtimes-lifecycle-shutdown """asyncdefasync_process_closure():returnlist(awaitasyncio.gather(*[self._async_process_record(record)forrecordinself.records]))# WARNING# Do not use "asyncio.run(async_process())" due to Lambda container thaws/freeze, otherwise we might get "Event Loop is closed" # noqa: E501# Instead, get_event_loop() can also create one if a previous was erroneously closed# Mangum library does this as well. It's battle tested with other popular async-only frameworks like FastAPI# https://github.com/jordaneremieff/mangum/discussions/256#discussioncomment-2638946# https://github.com/jordaneremieff/mangum/blob/b85cd4a97f8ddd56094ccc540ca7156c76081745/mangum/protocols/http.py#L44# Let's prime the coroutine and decide# whether we create an event loop (Lambda) or schedule it as usual (non-Lambda)coro=async_process_closure()ifos.getenv(constants.LAMBDA_TASK_ROOT_ENV):# Python 3.14+ will raise RuntimeError if get_event_loop() is called when there's no running loop# We need to handle both cases: existing loop (container reuse) and no loop (cold start)try:loop=asyncio.get_event_loop()exceptRuntimeError:# No running loop, create a new oneloop=asyncio.new_event_loop()asyncio.set_event_loop(loop)task_instance=loop.create_task(coro)returnloop.run_until_complete(task_instance)# Non-Lambda environment, run coroutine as usualreturnasyncio.run(coro)

deffailure_handler(self,record,exception:ExceptionInfo)->FailureResponse:""" Keeps track of batch records that failed processing Parameters ---------- record: Any record that failed processing exception: ExceptionInfo Exception information containing type, value, and traceback (sys.exc_info()) Returns ------- FailureResponse "fail", exceptions args, original record """exception_string=f"{exception[0]}:{exception[1]}"entry=("fail",exception_string,record)logger.debug(f"Record processing exception: {exception_string}")ifself.loggerisnotNoneand_has_traceback(exception):self.logger.warning("Record processing exception; skipping this record",exc_info=exception,)self.exceptions.append(exception)self.fail_messages.append(record)returnentry

defsuccess_handler(self,record,result:Any)->SuccessResponse:""" Keeps track of batch records that were processed successfully Parameters ---------- record: Any record that succeeded processing result: Any result from record handler Returns ------- SuccessResponse "success", result, original record """entry=("success",result,record)self.success_messages.append(record)returnentry

def__init__(self,event_type:EventType,model:BatchTypeModels|None=None,raise_on_entire_batch_failure:bool=True,logger:logging.Logger|None=None,):"""Process batch and partially report failed items Parameters ---------- event_type: EventType Whether this is a SQS, DynamoDB Streams, or Kinesis Data Stream event model: BatchTypeModels | None Parser's data model using either SqsRecordModel, DynamoDBStreamRecordModel, KinesisDataStreamRecord raise_on_entire_batch_failure: bool Raise an exception when the entire batch has failed processing. When set to False, partial failures are reported in the response logger: logging.Logger | None Optional Logger instance to output warnings with tracebacks for failed records. Exceptions ---------- BatchProcessingError Raised when the entire batch has failed processing """self.event_type=event_typeself.model=modelself.raise_on_entire_batch_failure=raise_on_entire_batch_failureself.batch_response:PartialItemFailureResponse=copy.deepcopy(self.DEFAULT_RESPONSE)self._COLLECTOR_MAPPING={EventType.SQS:self._collect_sqs_failures,EventType.KinesisDataStreams:self._collect_kinesis_failures,EventType.DynamoDBStreams:self._collect_dynamodb_failures,EventType.Kafka:self._collect_kafka_failures,}self._DATA_CLASS_MAPPING={EventType.SQS:SQSRecord,EventType.KinesisDataStreams:KinesisStreamRecord,EventType.DynamoDBStreams:DynamoDBRecord,EventType.Kafka:KafkaEventRecord,}super().__init__(logger=logger)