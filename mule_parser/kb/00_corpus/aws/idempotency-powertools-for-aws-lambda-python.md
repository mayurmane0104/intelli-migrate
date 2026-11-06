# Idempotency - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/utilities/idempotency](https://docs.aws.amazon.com/powertools/python/latest/utilities/idempotency)

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

The property of idempotency means that an operation does not cause additional side effects if it is called more than once with the same input parameters.

Idempotency key By default, this is a combination of (a) Lambda function name, (b) fully qualified name of your function, and (c) a hash of the entire payload or part(s) of the payload you specify. However, you can customize the key generation by using (a) a custom prefix name, while still incorporating (c) a hash of the entire payload or part(s) of the payload you specify.

Idempotent request is an operation with the same input previously processed that is not expired in your persistent storage or in-memory cache.

Persistence layer is a storage we use to create, read, expire, and delete idempotency records.

Idempotency record is the data representation of an idempotent request saved in the persistent layer and in its various status. We use it to coordinate whether (a) a request is idempotent, (b) it's not expired, (c) JSON response to return, and more.

We combine the Lambda function name and the fully qualified name for classes/functions to
prevent accidental reuse for similar code sharing input/output.

terraform{required_providers{aws={source="hashicorp/aws"version="~> 4.0"}}}provider"aws"{region="us-east-1" # Replace with your desired AWS region}resource"aws_dynamodb_table""IdempotencyTable"{name="IdempotencyTable"billing_mode="PAY_PER_REQUEST"hash_key="id"attribute{name="id"type="S"}ttl{attribute_name="expiration"enabled=true}}resource"aws_lambda_function""IdempotencyFunction"{function_name="IdempotencyFunction"role=aws_iam_role.IdempotencyFunctionRole.arnruntime="python3.12"handler="app.lambda_handler"filename="lambda.zip"}resource"aws_iam_role""IdempotencyFunctionRole"{name="IdempotencyFunctionRole"assume_role_policy=jsonencode({Version="2012-10-17"Statement=[{Sid=""Effect="Allow"Principal={Service="lambda.amazonaws.com"}Action="sts:AssumeRole"},]})}resource"aws_iam_policy""LambdaDynamoDBPolicy"{name="LambdaDynamoDBPolicy"description="IAM policy for Lambda function to access DynamoDB"policy=jsonencode({Version="2012-10-17"Statement=[{Sid="AllowDynamodbReadWrite"Effect="Allow"Action=["dynamodb:PutItem","dynamodb:GetItem","dynamodb:UpdateItem","dynamodb:DeleteItem",]Resource=aws_dynamodb_table.IdempotencyTable.arn},]})}resource"aws_iam_role_policy_attachment""IdempotencyFunctionRoleAttachment"{role=aws_iam_role.IdempotencyFunctionRole.namepolicy_arn=aws_iam_policy.LambdaDynamoDBPolicy.arn}

DynamoDB restricts item sizes to 400KB. This means that if your annotated function's response must be smaller than 400KB, otherwise your function will fail. Consider Redis as an alternative.

Expect 2 WCU per non-idempotent call. During the first invocation, we use PutItem for locking and UpdateItem for completion. Consider reviewing DynamoDB pricing documentation to estimate cost.

Old boto3 versions can increase costs. For cost optimization, we use a conditional PutItem to always lock a new idempotency record. If locking fails, it means we already have an idempotency record saving us an additional GetItem call. However, this is only supported in boto3 1.26.194 and higher (June 30th 2023).

For simple use cases, you can use the idempotent decorator on your Lambda handler function.

It will treat the entire event as an idempotency key. That is, the same event will return the previously stored result within a configurable time window(1 hour, by default).

For full flexibility, you can use the idempotent_function decorator for any synchronous Python function.

When using this decorator, you must call your decorated function using keyword arguments.

You can use data_keyword_argument to tell us the argument to extract an idempotency key. We support JSON serializable data, Dataclasses, Pydantic Models, and Event Source Data Classes

importosfromdataclassesimportdataclassfromaws_lambda_powertools.utilities.idempotencyimport(DynamoDBPersistenceLayer,IdempotencyConfig,idempotent_function,)fromaws_lambda_powertools.utilities.typingimportLambdaContexttable=os.getenv("IDEMPOTENCY_TABLE","")dynamodb=DynamoDBPersistenceLayer(table_name=table)config=IdempotencyConfig(event_key_jmespath="order_id")# see Choosing a payload subset section@dataclassclassOrderItem:sku:strdescription:str@dataclassclassOrder:item:OrderItemorder_id:int@idempotent_function(data_keyword_argument="order",config=config,persistence_store=dynamodb)defprocess_order(order:Order):returnf"processed order {order.order_id}"deflambda_handler(event:dict,context:LambdaContext):# see Lambda timeouts sectionconfig.register_lambda_context(context)order_item=OrderItem(sku="fake",description="sample")order=Order(item=order_item,order_id=1)# `order` parameter must be called as a keyword argument to workprocess_order(order=order)

importosfromaws_lambda_powertools.utilities.idempotencyimport(DynamoDBPersistenceLayer,IdempotencyConfig,idempotent_function,)fromaws_lambda_powertools.utilities.parserimportBaseModelfromaws_lambda_powertools.utilities.typingimportLambdaContexttable=os.getenv("IDEMPOTENCY_TABLE","")dynamodb=DynamoDBPersistenceLayer(table_name=table)config=IdempotencyConfig(event_key_jmespath="order_id")# see Choosing a payload subset sectionclassOrderItem(BaseModel):sku:strdescription:strclassOrder(BaseModel):item:OrderItemorder_id:int@idempotent_function(data_keyword_argument="order",config=config,persistence_store=dynamodb)defprocess_order(order:Order):returnf"processed order {order.order_id}"deflambda_handler(event:dict,context:LambdaContext):config.register_lambda_context(context)# see Lambda timeouts sectionorder_item=OrderItem(sku="fake",description="sample")order=Order(item=order_item,order_id=1)# `order` parameter must be called as a keyword argument to workprocess_order(order=order)

By default, idempotent_function serializes, stores, and returns your annotated function's result as a JSON object. You can change this behavior using output_serializer parameter.

The output serializer supports any JSON serializable data, Python Dataclasses and Pydantic Models.

Info

When using the output_serializer parameter, the data will continue to be stored in your persistent storage as a JSON string.

Function returns must be annotated with a single type, optionally wrapped in Optional or Union with None.

Use PydanticSerializer to automatically serialize what's retrieved from the persistent storage based on the return type annotated.

importosfromaws_lambda_powertools.utilities.idempotencyimport(DynamoDBPersistenceLayer,IdempotencyConfig,idempotent_function,)fromaws_lambda_powertools.utilities.idempotency.serialization.pydanticimportPydanticSerializerfromaws_lambda_powertools.utilities.parserimportBaseModelfromaws_lambda_powertools.utilities.typingimportLambdaContexttable=os.getenv("IDEMPOTENCY_TABLE","")dynamodb=DynamoDBPersistenceLayer(table_name=table)config=IdempotencyConfig(event_key_jmespath="order_id")# see Choosing a payload subset sectionclassOrderItem(BaseModel):sku:strdescription:strclassOrder(BaseModel):item:OrderItemorder_id:intclassOrderOutput(BaseModel):order_id:int@idempotent_function(data_keyword_argument="order",config=config,persistence_store=dynamodb,output_serializer=PydanticSerializer,)# order output is inferred from return typedefprocess_order(order:Order)->OrderOutput:returnOrderOutput(order_id=order.order_id)deflambda_handler(event:dict,context:LambdaContext):config.register_lambda_context(context)# see Lambda timeouts sectionorder_item=OrderItem(sku="fake",description="sample")order=Order(item=order_item,order_id=1)# `order` parameter must be called as a keyword argument to workprocess_order(order=order)

Alternatively, you can provide an explicit model as an input to PydanticSerializer.

importosfromaws_lambda_powertools.utilities.idempotencyimport(DynamoDBPersistenceLayer,IdempotencyConfig,idempotent_function,)fromaws_lambda_powertools.utilities.idempotency.serialization.pydanticimportPydanticSerializerfromaws_lambda_powertools.utilities.parserimportBaseModelfromaws_lambda_powertools.utilities.typingimportLambdaContexttable=os.getenv("IDEMPOTENCY_TABLE","")dynamodb=DynamoDBPersistenceLayer(table_name=table)config=IdempotencyConfig(event_key_jmespath="order_id")# see Choosing a payload subset sectionclassOrderItem(BaseModel):sku:strdescription:strclassOrder(BaseModel):item:OrderItemorder_id:intclassOrderOutput(BaseModel):order_id:int@idempotent_function(data_keyword_argument="order",config=config,persistence_store=dynamodb,output_serializer=PydanticSerializer(model=OrderOutput),)defprocess_order(order:Order):returnOrderOutput(order_id=order.order_id)deflambda_handler(event:dict,context:LambdaContext):config.register_lambda_context(context)# see Lambda timeouts sectionorder_item=OrderItem(sku="fake",description="sample")order=Order(item=order_item,order_id=1)# `order` parameter must be called as a keyword argument to workprocess_order(order=order)

Use DataclassSerializer to automatically serialize what's retrieved from the persistent storage based on the return type annotated.

importosfromdataclassesimportdataclassfromaws_lambda_powertools.utilities.idempotencyimport(DynamoDBPersistenceLayer,IdempotencyConfig,idempotent_function,)fromaws_lambda_powertools.utilities.idempotency.serialization.dataclassimportDataclassSerializerfromaws_lambda_powertools.utilities.typingimportLambdaContexttable=os.getenv("IDEMPOTENCY_TABLE","")dynamodb=DynamoDBPersistenceLayer(table_name=table)config=IdempotencyConfig(event_key_jmespath="order_id")# see Choosing a payload subset section@dataclassclassOrderItem:sku:strdescription:str@dataclassclassOrder:item:OrderItemorder_id:int@dataclassclassOrderOutput:order_id:int@idempotent_function(data_keyword_argument="order",config=config,persistence_store=dynamodb,output_serializer=DataclassSerializer,)# order output is inferred from return typedefprocess_order(order:Order)->OrderOutput:returnOrderOutput(order_id=order.order_id)deflambda_handler(event:dict,context:LambdaContext):config.register_lambda_context(context)# see Lambda timeouts sectionorder_item=OrderItem(sku="fake",description="sample")order=Order(item=order_item,order_id=1)# `order` parameter must be called as a keyword argument to workprocess_order(order=order)

We'll use OrderOutput to instantiate a new object using the data retrieved from persistent storage as input.

This ensures the return of the function is not impacted when @idempotent_function is used.

Alternatively, you can provide an explicit model as an input to DataclassSerializer.

importosfromdataclassesimportdataclassfromaws_lambda_powertools.utilities.idempotencyimport(DynamoDBPersistenceLayer,IdempotencyConfig,idempotent_function,)fromaws_lambda_powertools.utilities.idempotency.serialization.dataclassimportDataclassSerializerfromaws_lambda_powertools.utilities.typingimportLambdaContexttable=os.getenv("IDEMPOTENCY_TABLE","")dynamodb=DynamoDBPersistenceLayer(table_name=table)config=IdempotencyConfig(event_key_jmespath="order_id")# see Choosing a payload subset section@dataclassclassOrderItem:sku:strdescription:str@dataclassclassOrder:item:OrderItemorder_id:int@dataclassclassOrderOutput:order_id:int@idempotent_function(data_keyword_argument="order",config=config,persistence_store=dynamodb,output_serializer=DataclassSerializer(model=OrderOutput),)defprocess_order(order:Order):returnOrderOutput(order_id=order.order_id)deflambda_handler(event:dict,context:LambdaContext):config.register_lambda_context(context)# see Lambda timeouts sectionorder_item=OrderItem(sku="fake",description="sample")order=Order(item=order_item,order_id=1)# `order` parameter must be called as a keyword argument to workprocess_order(order=order)

Use CustomDictSerializer to have full control over the serialization process for any type. It expects two functions:

to_dict. Function to convert any type to a JSON serializable dictionary before it saves into the persistent storage.

from_dict. Function to convert from a dictionary retrieved from persistent storage and serialize in its original form.

importosfromtypingimportDict,Typefromaws_lambda_powertools.utilities.idempotencyimport(DynamoDBPersistenceLayer,IdempotencyConfig,idempotent_function,)fromaws_lambda_powertools.utilities.idempotency.serialization.custom_dictimportCustomDictSerializerfromaws_lambda_powertools.utilities.typingimportLambdaContexttable=os.getenv("IDEMPOTENCY_TABLE","")dynamodb=DynamoDBPersistenceLayer(table_name=table)config=IdempotencyConfig(event_key_jmespath="order_id")# see Choosing a payload subset sectionclassOrderItem:def__init__(self,sku:str,description:str):self.sku=skuself.description=descriptionclassOrder:def__init__(self,item:OrderItem,order_id:int):self.item=itemself.order_id=order_idclassOrderOutput:def__init__(self,order_id:int):self.order_id=order_iddeforder_to_dict(x:Type[OrderOutput])->Dict:returndict(x.__dict__)defdict_to_order(x:Dict)->OrderOutput:returnOrderOutput(**x)order_output_serializer=CustomDictSerializer(to_dict=order_to_dict,from_dict=dict_to_order,)@idempotent_function(data_keyword_argument="order",config=config,persistence_store=dynamodb,output_serializer=order_output_serializer,)defprocess_order(order:Order)->OrderOutput:returnOrderOutput(order_id=order.order_id)deflambda_handler(event:dict,context:LambdaContext):config.register_lambda_context(context)# see Lambda timeouts sectionorder_item=OrderItem(sku="fake",description="sample")order=Order(item=order_item,order_id=1)# `order` parameter must be called as a keyword argument to workprocess_order(order=order)

This function does the following

1. Receives the return from process_order 2. Converts to dictionary before it can be saved into the persistent storage.

This function does the following

1. Receives the dictionary saved into the persistent storage 1 Serializes to OrderOutput before @idempotent returns back to the caller.

This serializer receives both functions so it knows who to call when to serialize to and from dictionary.

In-memory cache is local to each Lambda execution environment.

You can enable caching with the use_local_cache parameter in IdempotencyConfig. When enabled, you can adjust cache capacity (256) with local_cache_max_items.

By default, caching is disabled since we don't know how big your response could be in relation to your configured memory size.

1 2 3 4 5 6 7 8 9101112131415161718192021

importosfromaws_lambda_powertools.utilities.idempotencyimport(DynamoDBPersistenceLayer,IdempotencyConfig,idempotent,)fromaws_lambda_powertools.utilities.typingimportLambdaContexttable=os.getenv("IDEMPOTENCY_TABLE","")persistence_layer=DynamoDBPersistenceLayer(table_name=table)config=IdempotencyConfig(event_key_jmespath="powertools_json(body)",# by default, it holds 256 items in a Least-Recently-Used (LRU) manneruse_local_cache=True,)@idempotent(config=config,persistence_store=persistence_layer)deflambda_handler(event,context:LambdaContext):returnevent

When dealing with a more elaborate payload, where parts of the payload always change, you should use event_key_jmespath parameter.

Use event_key_jmespath parameter in IdempotencyConfig to select one or more payload parts as your idempotency key.

Example scenario

In this example, we have a Lambda handler that creates a payment for a user subscribing to a product. We want to ensure that we don't accidentally charge our customer by subscribing them more than once.

Imagine the function runs successfully, but the client never receives the response due to a connection issue. It is safe to immediately retry in this instance, as the idempotent decorator will return a previously saved response.

We want to use user_id and product_id fields as our idempotency key. If we were to treat the entire request as our idempotency key, a simple HTTP header change would cause our function to run again.

Deserializing JSON strings in payloads for increased accuracy.

The payload extracted by the event_key_jmespath is treated as a string by default.
This means there could be differences in whitespace even when the JSON payload itself is identical.

To alter this behaviour, we can use the JMESPath built-in functionpowertools_json() to treat the payload as a JSON object (dict) rather than a string.

importjsonimportosfromdataclassesimportdataclass,fieldfromuuidimportuuid4fromaws_lambda_powertools.utilities.idempotencyimport(DynamoDBPersistenceLayer,IdempotencyConfig,idempotent,)fromaws_lambda_powertools.utilities.typingimportLambdaContexttable=os.getenv("IDEMPOTENCY_TABLE","")persistence_layer=DynamoDBPersistenceLayer(table_name=table)# Deserialize JSON string under the "body" key# then extract "user" and "product_id" dataconfig=IdempotencyConfig(event_key_jmespath='powertools_json(body).["user_id", "product_id"]')@dataclassclassPayment:user_id:strproduct_id:strpayment_id:str=field(default_factory=lambda:f"{uuid4()}")classPaymentError(Exception):...@idempotent(config=config,persistence_store=persistence_layer)deflambda_handler(event:dict,context:LambdaContext):try:payment_info:str=event.get("body","")payment:Payment=create_subscription_payment(json.loads(payment_info))return{"payment_id":payment.payment_id,"message":"success","statusCode":200,}exceptExceptionasexc:raisePaymentError(f"Error creating payment {str(exc)}")defcreate_subscription_payment(event:dict)->Payment:returnPayment(**event)

By default, we expire idempotency records after an hour (3600 seconds). After that, a transaction with the same payload will not be considered idempotent.

You can change this expiration window with the expires_after_seconds parameter. There is no limit on how long this expiration window can be set to.

Idempotency record expiration vs DynamoDB time-to-live (TTL)

DynamoDB TTL is a feature to remove items after a certain period of time, it may occur within 48 hours of expiration.

We don't rely on DynamoDB or any persistence storage layer to determine whether a record is expired to avoid eventual inconsistency states.

Instead, Idempotency records saved in the storage layer contain timestamps that can be verified upon retrieval and double checked within Idempotency feature.

Why?

A record might still be valid (COMPLETE) when we retrieved, but in some rare cases it might expire a second later. A record could also be cached in memory. You might also want to have idempotent transactions that should expire in seconds.

Warning: Changing the idempotency key generation will invalidate existing idempotency records

Use key_prefix parameter in the @idempotent or @idempotent_function decorators to define a custom prefix for your Idempotency Key. This allows you to decouple idempotency key name from function names. It can be useful during application refactoring, for example.

importosfromdataclassesimportdataclassfromaws_lambda_powertools.utilities.idempotencyimport(DynamoDBPersistenceLayer,IdempotencyConfig,idempotent_function,)fromaws_lambda_powertools.utilities.typingimportLambdaContexttable=os.getenv("IDEMPOTENCY_TABLE","")dynamodb=DynamoDBPersistenceLayer(table_name=table)config=IdempotencyConfig(event_key_jmespath="order_id")# see Choosing a payload subset section@dataclassclassOrderItem:sku:strdescription:str@dataclassclassOrder:item:OrderItemorder_id:int@idempotent_function(data_keyword_argument="order",config=config,persistence_store=dynamodb,key_prefix="my_custom_prefix",)defprocess_order(order:Order):returnf"processed order {order.order_id}"deflambda_handler(event:dict,context:LambdaContext):# see Lambda timeouts sectionconfig.register_lambda_context(context)order_item=OrderItem(sku="fake",description="sample")order=Order(item=order_item,order_id=1)# `order` parameter must be called as a keyword argument to workprocess_order(order=order)

The Idempotency record will be something like my_custom_prefix#c4ca4238a0b923820dcc509a6f75849b

By default, we protect against concurrent executions with the same payload using a locking mechanism. However, if your Lambda function times out before completing the first invocation it will only accept the same request when the idempotency record expire.

To prevent extended failures, use register_lambda_context function from your idempotency config to calculate and include the remaining invocation time in your idempotency record.

If a second invocation happens after this timestamp, and the record is marked as INPROGRESS, we will run the invocation again as if it was in the EXPIRED state.

This means that if an invocation expired during execution, it will be quickly executed again on the next retry.

importosimportrequestsfromaws_lambda_powertools.utilities.idempotencyimport(DynamoDBPersistenceLayer,IdempotencyConfig,idempotent_function,)fromaws_lambda_powertools.utilities.idempotency.exceptionsimportIdempotencyPersistenceLayerErrorfromaws_lambda_powertools.utilities.typingimportLambdaContexttable=os.getenv("IDEMPOTENCY_TABLE","")persistence_layer=DynamoDBPersistenceLayer(table_name=table)config=IdempotencyConfig()@idempotent_function(data_keyword_argument="data",config=config,persistence_store=persistence_layer)defcall_external_service(data:dict):# Any exception raised will lead to idempotency record to be deletedresult:requests.Response=requests.post("https://jsonplaceholder.typicode.com/comments/",json=data,)returnresult.json()deflambda_handler(event:dict,context:LambdaContext):try:call_external_service(data=event)exceptIdempotencyPersistenceLayerErrorase:# No idempotency, but you can decide to error differently.raiseRuntimeError(f"Oops, can't talk to persistence layer. Permissions? error: {e}")# This exception will not impact the idempotency of 'call_external_service'# because it happens in isolation, or outside their scope.raiseSyntaxError("Oops, this shouldn't be here.")

Use sort_key_attr parameter when your table is configured with a composite primary key (hash+range key).

When enabled, we will save the idempotency key in the sort key instead. By default, the primary key will now be set to idempotency#{LAMBDA_FUNCTION_NAME}.

You can optionally set a static value for the partition key using the static_pk_value parameter.

The CachePersistenceLayer enables you to use Valkey, Redis OSS, or any Redis-compatible cache as the persistence layer for idempotency state.

We recommend using valkey-glide for Valkey or redis for Redis. However, any Redis OSS-compatible client should work.

For simple setups, initialize CachePersistenceLayer with your Cache endpoint and port to connect. Note that for security, we enforce SSL connections by default; to disable it, set ssl=False.

importosfromtypingimportAny,Dictfromaws_lambda_powertools.utilities.batchimportBatchProcessor,EventType,process_partial_responsefromaws_lambda_powertools.utilities.data_classes.sqs_eventimportSQSRecordfromaws_lambda_powertools.utilities.idempotencyimport(DynamoDBPersistenceLayer,IdempotencyConfig,idempotent_function,)fromaws_lambda_powertools.utilities.typingimportLambdaContextprocessor=BatchProcessor(event_type=EventType.SQS)table=os.getenv("IDEMPOTENCY_TABLE","")dynamodb=DynamoDBPersistenceLayer(table_name=table)config=IdempotencyConfig(event_key_jmespath="messageId")@idempotent_function(data_keyword_argument="record",config=config,persistence_store=dynamodb)defrecord_handler(record:SQSRecord):return{"message":record.body}deflambda_handler(event:Dict[str,Any],context:LambdaContext):config.register_lambda_context(context)# see Lambda timeouts sectionreturnprocess_partial_response(event=event,context=context,processor=processor,record_handler=record_handler,)

You can override and further extend idempotency behavior via IdempotencyConfig with the following options:

Parameter

Default

Description

event_key_jmespath

""

JMESPath expression to extract the idempotency key from the event record using built-in functions

payload_validation_jmespath

""

JMESPath expression to validate that the specified fields haven't changed across requests for the same idempotency key e.g., payload tampering.

raise_on_no_idempotency_key

False

Raise exception if no idempotency key was found in the request

expires_after_seconds

3600

The number of seconds to wait before a record is expired, allowing a new transaction with the same idempotency key

use_local_cache

False

Whether to cache idempotency results in-memory to save on persistence storage latency and costs

local_cache_max_items

256

Max number of items to store in local cache

hash_function

md5

Function to use for calculating hashes, as provided by hashlib in the standard library.

response_hook

None

Function to use for processing the stored Idempotent response. This function hook is called when an existing idempotent response is found. See Manipulating The Idempotent Response

Handling concurrent executions with the same payload¶

This utility will raise an IdempotencyAlreadyInProgressError exception if you receive multiple invocations with the same payload while the first invocation hasn't completed yet.

Info

If you receive IdempotencyAlreadyInProgressError, you can safely retry the operation.

This is a locking mechanism for correctness. Since we don't know the result from the first invocation yet, we can't safely allow another concurrent execution.

Question: What if your function is invoked with the same payload except some outer parameters have changed?

Example: A payment transaction for a given productID was requested twice for the same customer, however the amount to be paid has changed in the second transaction.

By default, we will return the same result as it returned before, however in this instance it may be misleading; we provide a fail fast payload validation to address this edge case.

With payload_validation_jmespath, you can provide an additional JMESPath expression to specify which part of the event body should be validated against previous idempotent invocations

importosfromdataclassesimportdataclass,fieldfromuuidimportuuid4fromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.utilities.idempotencyimport(DynamoDBPersistenceLayer,IdempotencyConfig,idempotent,)fromaws_lambda_powertools.utilities.idempotency.exceptionsimportIdempotencyValidationErrorfromaws_lambda_powertools.utilities.typingimportLambdaContextlogger=Logger()table=os.getenv("IDEMPOTENCY_TABLE","")persistence_layer=DynamoDBPersistenceLayer(table_name=table)config=IdempotencyConfig(event_key_jmespath='["user_id", "product_id"]',payload_validation_jmespath="amount",)@dataclassclassPayment:user_id:strproduct_id:strcharge_type:stramount:intpayment_id:str=field(default_factory=lambda:f"{uuid4()}")classPaymentError(Exception):...@idempotent(config=config,persistence_store=persistence_layer)deflambda_handler(event:dict,context:LambdaContext):try:payment:Payment=create_subscription_payment(event)return{"payment_id":payment.payment_id,"message":"success","statusCode":200,}exceptIdempotencyValidationError:logger.exception("Payload tampering detected",payment=payment,failure_type="validation")return{"message":"Unable to process payment at this time. Try again later.","statusCode":500,}exceptExceptionasexc:raisePaymentError(f"Error creating payment {str(exc)}")defcreate_subscription_payment(event:dict)->Payment:returnPayment(**event)

In this example, the user_id and product_id keys are used as the payload to generate the idempotency key, as per event_key_jmespath parameter.

Note

If we try to send the same request but with a different amount, we will raise IdempotencyValidationError.

Without payload validation, we would have returned the same result as we did for the initial request. Since we're also returning an amount in the response, this could be quite confusing for the client.

By using payload_validation_jmespath="amount", we prevent this potentially confusing behavior and instead raise an Exception.

If you want to enforce that an idempotency key is required, you can set raise_on_no_idempotency_key to True.

This means that we will raise IdempotencyKeyError if the evaluation of event_key_jmespath is None.

Warning

To prevent errors, transactions will not be treated as idempotent if raise_on_no_idempotency_key is set to False and the evaluation of event_key_jmespath is None. Therefore, no data will be fetched, stored, or deleted in the idempotency storage layer.

The boto_config and boto3_session parameters enable you to pass in a custom botocore config object or a custom boto3 session when constructing the persistence store.

This utility provides an abstract base class (ABC), so that you can implement your choice of persistent storage layer.

You can create your own persistent store from scratch by inheriting the BasePersistenceLayer class, and implementing _get_record(), _put_record(), _update_record() and _delete_record().

_get_record() – Retrieves an item from the persistence store using an idempotency key and returns it as a DataRecord instance.

_put_record() – Adds a DataRecord to the persistence store if it doesn't already exist with that key. Raises an ItemAlreadyExists exception if a non-expired entry already exists.

_update_record() – Updates an item in the persistence store.

_delete_record() – Removes an item from the persistence store.

importdatetimeimportloggingfromtypingimportAny,Dict,Optionalimportboto3frombotocore.configimportConfigfromaws_lambda_powertools.utilities.idempotencyimportBasePersistenceLayerfromaws_lambda_powertools.utilities.idempotency.exceptionsimport(IdempotencyItemAlreadyExistsError,IdempotencyItemNotFoundError,)fromaws_lambda_powertools.utilities.idempotency.persistence.baseimportDataRecordlogger=logging.getLogger(__name__)classMyOwnPersistenceLayer(BasePersistenceLayer):def__init__(self,table_name:str,key_attr:str="id",expiry_attr:str="expiration",status_attr:str="status",data_attr:str="data",validation_key_attr:str="validation",boto_config:Optional[Config]=None,boto3_session:Optional[boto3.session.Session]=None,):boto3_session=boto3_sessionorboto3.session.Session()self._ddb_resource=boto3_session.resource("dynamodb",config=boto_config)self.table_name=table_nameself.table=self._ddb_resource.Table(self.table_name)self.key_attr=key_attrself.expiry_attr=expiry_attrself.status_attr=status_attrself.data_attr=data_attrself.validation_key_attr=validation_key_attrsuper().__init__()def_item_to_data_record(self,item:Dict[str,Any])->DataRecord:""" Translate raw item records from DynamoDB to DataRecord Parameters ---------- item: Dict[str, Union[str, int]] Item format from dynamodb response Returns ------- DataRecord representation of item """returnDataRecord(idempotency_key=item[self.key_attr],status=item[self.status_attr],expiry_timestamp=item[self.expiry_attr],response_data=item.get(self.data_attr,""),payload_hash=item.get(self.validation_key_attr,""),)def_get_record(self,idempotency_key)->DataRecord:response=self.table.get_item(Key={self.key_attr:idempotency_key},ConsistentRead=True)try:item=response["Item"]exceptKeyError:raiseIdempotencyItemNotFoundErrorreturnself._item_to_data_record(item)def_put_record(self,data_record:DataRecord)->None:item={self.key_attr:data_record.idempotency_key,self.expiry_attr:data_record.expiry_timestamp,self.status_attr:data_record.status,}ifself.payload_validation_enabled:item[self.validation_key_attr]=data_record.payload_hashnow=datetime.datetime.now()try:logger.debug(f"Putting record for idempotency key: {data_record.idempotency_key}")self.table.put_item(Item=item,ConditionExpression=f"attribute_not_exists({self.key_attr}) OR {self.expiry_attr} < :now",ExpressionAttributeValues={":now":int(now.timestamp())},)exceptself._ddb_resource.meta.client.exceptions.ConditionalCheckFailedException:logger.debug(f"Failed to put record for already existing idempotency key: {data_record.idempotency_key}")raiseIdempotencyItemAlreadyExistsErrordef_update_record(self,data_record:DataRecord):logger.debug(f"Updating record for idempotency key: {data_record.idempotency_key}")update_expression="SET #response_data = :response_data, #expiry = :expiry, #status = :status"expression_attr_values={":expiry":data_record.expiry_timestamp,":response_data":data_record.response_data,":status":data_record.status,}expression_attr_names={"#response_data":self.data_attr,"#expiry":self.expiry_attr,"#status":self.status_attr,}ifself.payload_validation_enabled:update_expression+=", #validation_key = :validation_key"expression_attr_values[":validation_key"]=data_record.payload_hashexpression_attr_names["#validation_key"]=self.validation_key_attrself.table.update_item(Key={self.key_attr:data_record.idempotency_key},UpdateExpression=update_expression,ExpressionAttributeValues=expression_attr_values,ExpressionAttributeNames=expression_attr_names,)def_delete_record(self,data_record:DataRecord)->None:logger.debug(f"Deleting record for idempotency key: {data_record.idempotency_key}")self.table.delete_item(Key={self.key_attr:data_record.idempotency_key},)

Danger

Pay attention to the documentation for each - you may need to perform additional checks inside these methods to ensure the idempotency guarantees remain intact.

For example, the _put_record method needs to raise an exception if a non-expired record already exists in the data store with a matching key.

You can set up a response_hook in the IdempotentConfig class to manipulate the returned data when an operation is idempotent. The hook function will be called with the current deserialized response object and the Idempotency record.

importosimportuuidfromtypingimportDictfromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.utilities.idempotencyimport(DynamoDBPersistenceLayer,IdempotencyConfig,idempotent_function,)fromaws_lambda_powertools.utilities.idempotency.persistence.datarecordimport(DataRecord,)fromaws_lambda_powertools.utilities.typingimportLambdaContextlogger=Logger()defmy_response_hook(response:Dict,idempotent_data:DataRecord)->Dict:# Return inserted Header data into the Idempotent Responseresponse["x-idempotent-key"]=idempotent_data.idempotency_key# expiry_timestamp can be None so include if setexpiry_timestamp=idempotent_data.get_expiration_datetime()ifexpiry_timestamp:response["x-idempotent-expiration"]=expiry_timestamp.isoformat()# Must return the response herereturnresponsetable=os.getenv("IDEMPOTENCY_TABLE","")dynamodb=DynamoDBPersistenceLayer(table_name=table)config=IdempotencyConfig(response_hook=my_response_hook)@idempotent_function(data_keyword_argument="order",config=config,persistence_store=dynamodb)defprocess_order(order:dict)->dict:# create the order_idorder_id=str(uuid.uuid4())# create your logic to save the order# append the order_id createdorder["order_id"]=order_id# return the orderreturn{"order":order}deflambda_handler(event:dict,context:LambdaContext):config.register_lambda_context(context)# see Lambda timeouts sectiontry:logger.info(f"Processing order id {event.get('order_id')}")returnprocess_order(order=event.get("order"))exceptExceptionaserr:return{"status_code":400,"error":f"Error processing {str(err)}"}

When using response hooks to manipulate returned data from idempotent operations, it's important to follow best practices to avoid introducing complexity or issues. Keep these guidelines in mind:

Response hook works exclusively when operations are idempotent. The hook will not be called when an operation is not idempotent, or when the idempotent logic fails.

Catch and Handle Exceptions. Your response hook code should catch and handle any exceptions that may arise from your logic. Unhandled exceptions will cause the Lambda function to fail unexpectedly.

Keep Hook Logic Simple Response hooks should consist of minimal and straightforward logic for manipulating response data. Avoid complex conditional branching and aim for hooks that are easy to reason about.

The idempotency utility can be used with the validator decorator. Ensure that idempotency is the innermost decorator.

Warning

If you use an envelope with the validator, the event received by the idempotency utility will be the unwrapped
event - not the "raw" event Lambda was invoked with.

Make sure to account for this behavior, if you set the event_key_jmespath.

Tip: JMESPath Powertools for AWS Lambda (Python) functions are also available

Built-in functions known in the validation utility like powertools_json, powertools_base64, powertools_base64_gzip are also available to use in this utility.

On subsequent executions with the same payload, Lambda optimistically tries to save the record in DynamoDB. If the record already exists, DynamoDB returns the item.

Explore how to handle conditional write errors in high-concurrency scenarios with DynamoDB in this blog post.

When testing your code, you may wish to disable the idempotency logic altogether and focus on testing your business logic. To do this, you can set the environment variable POWERTOOLS_IDEMPOTENCY_DISABLED
with a truthy value. If you prefer setting this for specific tests, and are using Pytest, you can use monkeypatch fixture:

fromdataclassesimportdataclassimportapp_test_disabling_idempotency_utilityimportpytest@dataclassclassLambdaContext:function_name:str="test"memory_limit_in_mb:int=128invoked_function_arn:str="arn:aws:lambda:eu-west-1:809313241:function:test"aws_request_id:str="52fdfc07-2182-154f-163f-5f0f9a621d72"defget_remaining_time_in_millis(self)->int:return5@pytest.fixturedeflambda_context()->LambdaContext:returnLambdaContext()deftest_idempotent_lambda_handler(monkeypatch,lambda_context:LambdaContext):# Set POWERTOOLS_IDEMPOTENCY_DISABLED before calling decorated functionsmonkeypatch.setenv("POWERTOOLS_IDEMPOTENCY_DISABLED",1)result=app_test_disabling_idempotency_utility.lambda_handler({},lambda_context)assertresult

To test with DynamoDB Local, you can replace the DynamoDB client used by the persistence layer with one you create inside your tests. This allows you to set the endpoint_url.

fromdataclassesimportdataclassimportapp_test_dynamodb_localimportboto3importpytest@dataclassclassLambdaContext:function_name:str="test"memory_limit_in_mb:int=128invoked_function_arn:str="arn:aws:lambda:eu-west-1:809313241:function:test"aws_request_id:str="52fdfc07-2182-154f-163f-5f0f9a621d72"defget_remaining_time_in_millis(self)->int:return5@pytest.fixturedeflambda_context()->LambdaContext:returnLambdaContext()deftest_idempotent_lambda(lambda_context):# Configure the boto3 to use the endpoint for the DynamoDB Local instancedynamodb_local_client=boto3.client("dynamodb",endpoint_url="http://localhost:8000")app_test_dynamodb_local.persistence_layer.client=dynamodb_local_client# If desired, you can use a different DynamoDB Local table name than what your code already uses# app.persistence_layer.table_name = "another table name" # noqa: ERA001result=app_test_dynamodb_local.handler({"testkey":"testvalue"},lambda_context)assertresult["payment_id"]==12345

The idempotency utility lazily creates the dynamodb Table which it uses to access DynamoDB.
This means it is possible to pass a mocked Table resource, or stub various methods.

To test locally, you can either utilize fakeredis-py for a simulated Redis environment or refer to the MockRedis class used in our tests to mock Redis operations.

importtimeastfromtypingimportDict# Mock redis class that includes all operations we used in IdempotencyclassMockRedis:def__init__(self,decode_responses,cache:Dict,**kwargs):self.cache=cacheor{}self.expire_dict:Dict={}self.decode_responses=decode_responsesself.acl:Dict={}self.username=""defhset(self,name,mapping):self.expire_dict.pop(name,{})self.cache[name]=mappingdeffrom_url(self,url:str):passdefexpire(self,name,time):self.expire_dict[name]=t.time()+time# return {} if no matchdefhgetall(self,name):ifself.expire_dict.get(name,t.time()+1)<t.time():self.cache.pop(name,{})returnself.cache.get(name,{})defget_connection_kwargs(self):return{"decode_responses":self.decode_responses}defauth(self,username,**kwargs):self.username=usernamedefdelete(self,name):self.cache.pop(name,{})

If you want to set up a real Redis client for integration testing, you can reference the code provided below.

fromdataclassesimportdataclassimportpytestimportredisfromaws_lambda_powertools.utilities.idempotencyimport(idempotent,)fromaws_lambda_powertools.utilities.idempotency.persistence.redisimport(RedisCachePersistenceLayer,)fromaws_lambda_powertools.utilities.typingimportLambdaContext@pytest.fixturedeflambda_context():@dataclassclassLambdaContext:function_name:str="test"memory_limit_in_mb:int=128invoked_function_arn:str="arn:aws:lambda:eu-west-1:809313241:function:test"aws_request_id:str="52fdfc07-2182-154f-163f-5f0f9a621d72"defget_remaining_time_in_millis(self)->int:return1000returnLambdaContext()@pytest.fixturedefpersistence_store_standalone_redis():# init a Real Redis client and connect to the Port set in the Makefileredis_client=redis.Redis(host="localhost",port="63005",decode_responses=True,)# return a persistence layer with real RedisreturnRedisCachePersistenceLayer(client=redis_client)deftest_idempotent_lambda(lambda_context,persistence_store_standalone_redis):# Establish persistence layer using the real redis clientpersistence_layer=persistence_store_standalone_redis# setup idempotent with redis persistence layer@idempotent(persistence_store=persistence_layer)deflambda_handler(event:dict,context:LambdaContext):print("expensive operation")return{"payment_id":12345,"message":"success","statusCode":200,}# Inovke the sim lambda handlerresult=lambda_handler({"testkey":"testvalue"},lambda_context)assertresult["payment_id"]==12345