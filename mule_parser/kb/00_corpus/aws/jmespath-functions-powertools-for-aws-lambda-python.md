# JMESPath Functions - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/utilities/jmespath_functions](https://docs.aws.amazon.com/powertools/python/latest/utilities/jmespath_functions)

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

All examples shared in this documentation are available within the project repository.

You might have events that contains encoded JSON payloads as string, base64, or even in compressed format. It is a common use case to decode and extract them partially or fully as part of your Lambda function invocation.

Powertools for AWS Lambda (Python) also have utilities like validation, idempotency, or feature flags where you might need to extract a portion of your data before using them.

Terminology

Envelope is the terminology we use for the JMESPath expression to extract your JSON object from your data input. We might use those two terms interchangeably.

Another common use case is to fetch deeply nested data, filter, flatten, and more.

1 2 3 4 5 6 7 8 9101112

fromaws_lambda_powertools.utilities.jmespath_utilsimportqueryfromaws_lambda_powertools.utilities.typingimportLambdaContextdefhandler(event:dict,context:LambdaContext)->dict:payload=query(data=event,envelope="powertools_json(body)")customer_id=payload.get("customerId")# now deserialized# also works for fetching and flattening deeply nested datasome_data=query(data=event,envelope="deeply_nested[*].some_data[]")return{"customer_id":customer_id,"message":"success","context":some_data,"statusCode":200}

We provide built-in envelopes for popular AWS Lambda event sources to easily decode and/or deserialize JSON objects.

1 2 3 4 5 6 7 8 9101112131415161718

from__future__importannotationsfromaws_lambda_powertoolsimportLoggerfromaws_lambda_powertools.utilities.jmespath_utilsimport(envelopes,query,)fromaws_lambda_powertools.utilities.typingimportLambdaContextlogger=Logger()defhandler(event:dict,context:LambdaContext)->dict:records:list=query(data=event,envelope=envelopes.SQS)forrecordinrecords:# records is a listlogger.info(record.get("customerId"))# now deserializedreturn{"message":"success","statusCode":200}

If you don't require SNS metadata, enable raw message delivery. It will reduce multiple payload layers and size, when using SNS in combination with other services (e.g., SQS, S3, etc).

You can use our built-in JMESPath functions within your envelope expression. They handle deserialization for common data formats found in AWS Lambda event sources such as JSON strings, base64, and uncompress gzip data.

Info

We use these everywhere in Powertools for AWS Lambda (Python) to easily decode and unwrap events from Amazon API Gateway, Amazon Kinesis, AWS CloudWatch Logs, etc.

importjsonfromdataclassesimportasdict,dataclass,field,is_dataclassfromuuidimportuuid4importpowertools_json_jmespath_schemaasschemasfromjmespath.exceptionsimportJMESPathTypeErrorfromaws_lambda_powertools.utilities.typingimportLambdaContextfromaws_lambda_powertools.utilities.validationimportSchemaValidationError,validate@dataclassclassOrder:user_id:intproduct_id:intquantity:intprice:floatcurrency:strorder_id:str=field(default_factory=lambda:f"{uuid4()}")classDataclassCustomEncoder(json.JSONEncoder):"""A custom JSON encoder to serialize dataclass obj"""defdefault(self,obj):# Only called for values that aren't JSON serializable# where `obj` will be an instance of Order in this examplereturnasdict(obj)ifis_dataclass(obj)elsesuper().default(obj)deflambda_handler(event,context:LambdaContext)->dict:try:# Validate order against our schemavalidate(event=event,schema=schemas.INPUT,envelope="powertools_json(payload)")# Deserialize JSON string order as dict# alternatively, query works here tooorder_payload:dict=json.loads(event.get("payload"))return{"order":json.dumps(Order(**order_payload),cls=DataclassCustomEncoder),"message":"order created","success":True,}exceptJMESPathTypeError:# The powertools_json() envelope function must match a valid pathreturnreturn_error_message("Invalid request.")exceptSchemaValidationErrorasexception:# SchemaValidationError indicates where a data mismatch isreturnreturn_error_message(str(exception))exceptjson.JSONDecodeError:returnreturn_error_message("Payload must be valid JSON (base64 encoded).")defreturn_error_message(message:str)->dict:return{"order":None,"message":message,"success":False}

INPUT={"$schema":"http://json-schema.org/draft-07/schema","$id":"http://example.com/example.json","type":"object","title":"Sample order schema","description":"The root schema comprises the entire JSON document.","examples":[{"user_id":123,"product_id":1,"quantity":2,"price":10.40,"currency":"USD"}],"required":["user_id","product_id","quantity","price","currency"],"properties":{"user_id":{"$id":"#/properties/user_id","type":"integer","title":"The unique identifier of the user","examples":[123],"maxLength":10,},"product_id":{"$id":"#/properties/product_id","type":"integer","title":"The unique identifier of the product","examples":[1],"maxLength":10,},"quantity":{"$id":"#/properties/quantity","type":"integer","title":"The quantity of the product","examples":[2],"maxLength":10,},"price":{"$id":"#/properties/price","type":"number","title":"The individual price of the product","examples":[10.40],"maxLength":10,},"currency":{"$id":"#/properties/currency","type":"string","title":"The currency","examples":["The currency of the order"],"maxLength":100,},},}

importjsonfromuuidimportuuid4importrequestsfromaws_lambda_powertools.utilities.idempotencyimport(DynamoDBPersistenceLayer,IdempotencyConfig,idempotent,)persistence_layer=DynamoDBPersistenceLayer(table_name="IdempotencyTable")# Treat everything under the "body" key# in the event json object as our payloadconfig=IdempotencyConfig(event_key_jmespath="powertools_json(body)")classPaymentError(Exception):...@idempotent(config=config,persistence_store=persistence_layer)defhandler(event,context)->dict:body=json.loads(event["body"])try:payment:dict=create_subscription_payment(user=body["user"],product_id=body["product_id"])return{"payment_id":payment.get("id"),"message":"success","statusCode":200}exceptrequests.HTTPErrorase:raisePaymentError("Unable to create payment subscription")fromedefcreate_subscription_payment(user:str,product_id:str)->dict:payload={"user":user,"product_id":product_id}ret:requests.Response=requests.post(url="https://httpbin.org/anything",data=payload)ret.raise_for_status()return{"id":f"{uuid4()}","message":"paid"}

importbase64importbinasciiimportjsonfromdataclassesimportasdict,dataclass,field,is_dataclassfromuuidimportuuid4importpowertools_base64_jmespath_schemaasschemasfromjmespath.exceptionsimportJMESPathTypeErrorfromaws_lambda_powertools.utilities.typingimportLambdaContextfromaws_lambda_powertools.utilities.validationimportSchemaValidationError,validate@dataclassclassOrder:user_id:intproduct_id:intquantity:intprice:floatcurrency:strorder_id:str=field(default_factory=lambda:f"{uuid4()}")classDataclassCustomEncoder(json.JSONEncoder):"""A custom JSON encoder to serialize dataclass obj"""defdefault(self,obj):# Only called for values that aren't JSON serializable# where `obj` will be an instance of Todo in this examplereturnasdict(obj)ifis_dataclass(obj)elsesuper().default(obj)deflambda_handler(event,context:LambdaContext)->dict:# Try to validate the schematry:validate(event=event,schema=schemas.INPUT,envelope="powertools_json(powertools_base64(payload))")# alternatively, query works here toopayload_decoded=base64.b64decode(event["payload"]).decode()order_payload:dict=json.loads(payload_decoded)return{"order":json.dumps(Order(**order_payload),cls=DataclassCustomEncoder),"message":"order created","success":True,}exceptJMESPathTypeError:returnreturn_error_message("The powertools_json(powertools_base64()) envelope function must match a valid path.",)exceptbinascii.Error:returnreturn_error_message("Payload must be a valid base64 encoded string")exceptjson.JSONDecodeError:returnreturn_error_message("Payload must be valid JSON (base64 encoded).")exceptSchemaValidationErrorasexception:# SchemaValidationError indicates where a data mismatch isreturnreturn_error_message(str(exception))defreturn_error_message(message:str)->dict:return{"order":None,"message":message,"success":False}

INPUT={"$schema":"http://json-schema.org/draft-07/schema","$id":"http://example.com/example.json","type":"object","title":"Sample order schema","description":"The root schema comprises the entire JSON document.","examples":[{"user_id":123,"product_id":1,"quantity":2,"price":10.40,"currency":"USD"}],"required":["user_id","product_id","quantity","price","currency"],"properties":{"user_id":{"$id":"#/properties/user_id","type":"integer","title":"The unique identifier of the user","examples":[123],"maxLength":10,},"product_id":{"$id":"#/properties/product_id","type":"integer","title":"The unique identifier of the product","examples":[1],"maxLength":10,},"quantity":{"$id":"#/properties/quantity","type":"integer","title":"The quantity of the product","examples":[2],"maxLength":10,},"price":{"$id":"#/properties/price","type":"number","title":"The individual price of the product","examples":[10.40],"maxLength":10,},"currency":{"$id":"#/properties/currency","type":"string","title":"The currency","examples":["The currency of the order"],"maxLength":100,},},}

Use powertools_base64_gzip function to decompress and decode base64 data.

This sample will decompress and decode base64 data from Cloudwatch Logs, then use JMESPath pipeline expression to pass the result for decoding its JSON string.

importbase64importbinasciiimportgzipimportjsonimportpowertools_base64_gzip_jmespath_schemaasschemasfromjmespath.exceptionsimportJMESPathTypeErrorfromaws_lambda_powertools.utilities.typingimportLambdaContextfromaws_lambda_powertools.utilities.validationimportSchemaValidationError,validatedeflambda_handler(event,context:LambdaContext)->dict:try:validate(event=event,schema=schemas.INPUT,envelope="powertools_base64_gzip(payload) | powertools_json(@)")# Alternatively, query works here tooencoded_payload=base64.b64decode(event["payload"])uncompressed_payload=gzip.decompress(encoded_payload).decode()log:dict=json.loads(uncompressed_payload)return{"message":"Logs processed","log_group":log.get("logGroup"),"owner":log.get("owner"),"success":True,}exceptJMESPathTypeError:returnreturn_error_message("The powertools_base64_gzip() envelope function must match a valid path.")exceptbinascii.Error:returnreturn_error_message("Payload must be a valid base64 encoded string")exceptjson.JSONDecodeError:returnreturn_error_message("Payload must be valid JSON (base64 encoded).")exceptSchemaValidationErrorasexception:# SchemaValidationError indicates where a data mismatch isreturnreturn_error_message(str(exception))defreturn_error_message(message:str)->dict:return{"message":message,"success":False}

This should only be used for advanced use cases where you have special formats not covered by the built-in functions.

For special binary formats that you want to decode before applying JSON Schema validation, you can bring your own JMESPath function and any additional option via jmespath_options param. To keep Powertools for AWS Lambda (Python) built-in functions, you can subclass from PowertoolsFunctions.

Here is an example of how to decompress messages using zlib:

importbase64importbinasciiimportzlibfromjmespath.exceptionsimportJMESPathTypeErrorfromjmespath.functionsimportsignaturefromaws_lambda_powertools.utilities.jmespath_utilsimport(PowertoolsFunctions,query,)classCustomFunctions(PowertoolsFunctions):# only decode if value is a string# see supported data types: https://jmespath.org/specification.html#built-in-functions@signature({"types":["string"]})def_func_decode_zlib_compression(self,payload:str):decoded:bytes=base64.b64decode(payload)returnzlib.decompress(decoded)custom_jmespath_options={"custom_functions":CustomFunctions()}deflambda_handler(event,context)->dict:try:logs=[]logs.append(query(data=event,# NOTE: Use the prefix `_func_` before the name of the functionenvelope="Records[*].decode_zlib_compression(log)",jmespath_options=custom_jmespath_options,),)return{"logs":logs,"message":"Extracted messages","success":True}exceptJMESPathTypeError:returnreturn_error_message("The envelope function must match a valid path.")exceptzlib.error:returnreturn_error_message("Log must be a valid zlib compressed message")exceptbinascii.Error:returnreturn_error_message("Log must be a valid base64 encoded string")defreturn_error_message(message:str)->dict:return{"logs":None,"message":message,"success":False}