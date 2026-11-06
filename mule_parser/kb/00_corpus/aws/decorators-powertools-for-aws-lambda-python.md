# Decorators - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/batch/decorators](https://docs.aws.amazon.com/powertools/python/latest/api_doc/batch/decorators)

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

@lambda_handler_decorator@deprecated("`async_batch_processor` decorator is deprecated; use `async_process_partial_response` function instead.",category=None,)defasync_batch_processor(handler:Callable,event:dict,context:LambdaContext,record_handler:Callable[...,Awaitable[Any]],processor:AsyncBatchProcessor,):""" Middleware to handle batch event processing Notes ----- Consider using async_process_partial_response function for an easier experience. Parameters ---------- handler: Callable Lambda's handler event: dict Lambda's Event context: LambdaContext Lambda's Context record_handler: Callable[..., Awaitable[Any]] Callable to process each record from the batch processor: AsyncBatchProcessor Batch Processor to handle partial failure cases Example -------- >>> from aws_lambda_powertools.utilities.batch import async_batch_processor, AsyncBatchProcessor >>> from aws_lambda_powertools.utilities.data_classes.sqs_event import SQSRecord >>> >>> processor = AsyncBatchProcessor(event_type=EventType.SQS) >>> >>> async def async_record_handler(record: SQSRecord): >>> payload: str = record.body >>> return payload >>> >>> @async_batch_processor(record_handler=async_record_handler, processor=processor) >>> def lambda_handler(event, context): >>> return processor.response() Limitations ----------- * Sync batch processors. Use `batch_processor` instead. """warnings.warn("The `async_batch_processor` decorator is deprecated in V3 ""and will be removed in the next major version. Use `async_process_partial_response` function instead.",category=PowertoolsDeprecationWarning,stacklevel=2,)records=event["Records"]withprocessor(records,record_handler,lambda_context=context):processor.async_process()returnhandler(event,context)

@lambda_handler_decorator@deprecated("`batch_processor` decorator is deprecated; use `process_partial_response` function instead.",category=None,)defbatch_processor(handler:Callable,event:dict,context:LambdaContext,record_handler:Callable,processor:BatchProcessor,):""" Middleware to handle batch event processing Notes ----- Consider using process_partial_response function for an easier experience. Parameters ---------- handler: Callable Lambda's handler event: dict Lambda's Event context: LambdaContext Lambda's Context record_handler: Callable Callable or corutine to process each record from the batch processor: BatchProcessor Batch Processor to handle partial failure cases Example -------- **Processes Lambda's event with a BatchProcessor** >>> from aws_lambda_powertools.utilities.batch import batch_processor, BatchProcessor, EventType >>> from aws_lambda_powertools.utilities.data_classes.sqs_event import SQSRecord >>> >>> processor = BatchProcessor(EventType.SQS) >>> >>> def record_handler(record): >>> return record["body"] >>> >>> @batch_processor(record_handler=record_handler, processor=BatchProcessor()) >>> def handler(event, context): >>> return processor.response() Limitations ----------- * Async batch processors. Use `async_batch_processor` instead. """warnings.warn("The `batch_processor` decorator is deprecated in V3 ""and will be removed in the next major version. Use `process_partial_response` function instead.",category=PowertoolsDeprecationWarning,stacklevel=2,)records=event["Records"]withprocessor(records,record_handler,lambda_context=context):processor.process()returnhandler(event,context)

Source code in aws_lambda_powertools/utilities/batch/sqs_fifo_partial_processor.py

697071727374757677787980818283848586878889909192

def__init__(self,model:BatchSqsTypeModel|None=None,skip_group_on_error:bool=False,logger:logging.Logger|None=None,):""" Initialize the SqsFifoProcessor. Parameters ---------- model: BatchSqsTypeModel | None An optional model for batch processing. skip_group_on_error: bool Determines whether to exclusively skip messages from the MessageGroupID that encountered processing failures Default is False. logger: logging.Logger | None Optional Logger instance to output warnings with tracebacks for failed records. """self._skip_group_on_error:bool=skip_group_on_errorself._current_group_id=Noneself._failed_group_ids:set[str]=set()super().__init__(EventType.SQS,model,logger=logger)