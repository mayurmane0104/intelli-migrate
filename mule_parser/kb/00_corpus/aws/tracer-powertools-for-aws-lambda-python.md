# Tracer - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/core/tracer](https://docs.aws.amazon.com/powertools/python/latest/core/tracer)

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

This is not necessary if you're installing Powertools for AWS Lambda (Python) via Lambda Layer/SAR

Add aws-lambda-powertools[tracer] as a dependency in your preferred tool: e.g., requirements.txt, pyproject.toml. This will ensure you have the required dependencies before using Tracer.

Before your use this utility, your AWS Lambda function must have permissions to send traces to AWS X-Ray.

AWS Serverless Application Model (SAM) example

1 2 3 4 5 6 7 8 91011121314151617181920212223

AWSTemplateFormatVersion:"2010-09-09"Transform:AWS::Serverless-2016-10-31Description:Powertools for AWS Lambda (Python) versionGlobals:Function:Timeout:5Runtime:python3.12Tracing:ActiveEnvironment:Variables:POWERTOOLS_SERVICE_NAME:paymentLayers:# Find the latest Layer version in the official documentation# https://docs.aws.amazon.com/powertools/python/latest/#lambda-layer-!Subarn:aws:lambda:${AWS::Region}:017000801446:layer:AWSLambdaPowertoolsPythonV3-python312-x86_64:36Resources:CaptureLambdaHandlerExample:Type:AWS::Serverless::FunctionProperties:CodeUri:../srcHandler:capture_lambda_handler.handler

You can quickly start by initializing Tracer and use capture_lambda_handler decorator for your Lambda handler.

Tracing Lambda handler with capture_lambda_handler

1 2 3 4 5 6 7 8 9101112131415

fromaws_lambda_powertoolsimportTracerfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()# Sets service via POWERTOOLS_SERVICE_NAME env var# OR tracer = Tracer(service="example")defcollect_payment(charge_id:str)->str:returnf"dummy payment collected for charge: {charge_id}"@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->str:charge_id=event.get("charge_id","")returncollect_payment(charge_id=charge_id)

capture_lambda_handler performs these additional tasks to ease operations:

Creates a ColdStart annotation to easily filter traces that have had an initialization overhead

Creates a Service annotation if service parameter or POWERTOOLS_SERVICE_NAME is set

Captures any response, or full exceptions generated by the handler, and include as tracing metadata

Annotations are key-values associated with traces and indexed by AWS X-Ray. You can use them to filter traces and to create Trace Groups to slice and dice your transactions.

Adding annotations with put_annotation method

1 2 3 4 5 6 7 8 9101112131415

fromaws_lambda_powertoolsimportTracerfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()defcollect_payment(charge_id:str)->str:tracer.put_annotation(key="PaymentId",value=charge_id)returnf"dummy payment collected for charge: {charge_id}"@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->str:charge_id=event.get("charge_id","")returncollect_payment(charge_id=charge_id)

Metadata are key-values also associated with traces but not indexed by AWS X-Ray. You can use them to add additional context for an operation using any native object.

Adding arbitrary metadata with put_metadata method

1 2 3 4 5 6 7 8 9101112131415161718192021

fromaws_lambda_powertoolsimportTracerfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()defcollect_payment(charge_id:str)->str:returnf"dummy payment collected for charge: {charge_id}"@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->str:payment_context={"charge_id":event.get("charge_id",""),"merchant_id":event.get("merchant_id",""),"request_id":context.aws_request_id,}payment_context["receipt_id"]=collect_payment(charge_id=payment_context["charge_id"])tracer.put_metadata(key="payment_response",value=payment_context)returnpayment_context["receipt_id"]

The serialization is performed by aws-xray-sdk via jsonpickle module. This can cause
side effects for file-like objects like boto S3 StreamingBody, where its response will be read only once during serialization.

importcontextlibfromcollections.abcimportGeneratorfromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()@contextlib.contextmanager@tracer.capture_methoddefcollect_payment(charge_id:str)->Generator[str,None,None]:try:yieldf"dummy payment collected for charge: {charge_id}"finally:tracer.put_annotation(key="PaymentId",value=charge_id)@tracer.capture_lambda_handler@logger.inject_lambda_contextdeflambda_handler(event:dict,context:LambdaContext)->str:charge_id=event.get("charge_id","")withcollect_payment(charge_id=charge_id)asreceipt_id:logger.info(f"Processing payment collection for charge {charge_id} with receipt {receipt_id}")returnreceipt_id

1 2 3 4 5 6 7 8 91011121314151617

fromcollections.abcimportGeneratorfromaws_lambda_powertoolsimportTracerfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()@tracer.capture_methoddefcollect_payment(charge_id:str)->Generator[str,None,None]:yieldf"dummy payment collected for charge: {charge_id}"@tracer.capture_lambda_handlerdeflambda_handler(event:dict,context:LambdaContext)->str:charge_id=event.get("charge_id","")returnnext(collect_payment(charge_id=charge_id))

Tracer automatically patches all supported libraries by X-Ray during initialization, by default. Underneath, AWS X-Ray SDK checks whether a supported library has been imported before patching.

If you're looking to shave a few microseconds, or milliseconds depending on your function memory configuration, you can patch specific modules using patch_modules param:

Use capture_response=False parameter in both capture_lambda_handler and capture_method decorators to instruct Tracer not to serialize function responses as metadata.

Info: This is useful in three common scenarios

You might return sensitive information you don't want it to be added to your traces

You might manipulate streaming objects that can be read only once; this prevents subsequent calls from being empty

You might return more than 64K of data e.g., message too long error

1 2 3 4 5 6 7 8 9101112131415161718

fromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()logger=Logger()@tracer.capture_method(capture_response=False)defcollect_payment(charge_id:str)->str:tracer.put_annotation(key="PaymentId",value=charge_id)logger.debug("Returning sensitive information....")returnf"dummy payment collected for charge: {charge_id}"@tracer.capture_lambda_handler(capture_response=False)deflambda_handler(event:dict,context:LambdaContext)->str:charge_id=event.get("charge_id","")returncollect_payment(charge_id=charge_id)

importosimportboto3frombotocore.responseimportStreamingBodyfromaws_lambda_powertoolsimportLogger,Tracerfromaws_lambda_powertools.utilities.typingimportLambdaContextBUCKET=os.getenv("BUCKET_NAME","")REPORT_KEY=os.getenv("REPORT_KEY","")tracer=Tracer()logger=Logger()session=boto3.session.Session()s3=session.client("s3")@tracer.capture_method(capture_response=False)deffetch_payment_report(payment_id:str)->StreamingBody:ret=s3.get_object(Bucket=BUCKET,Key=f"{REPORT_KEY}/{payment_id}")logger.debug("Returning streaming body from S3 object....")returnret["Body"]@tracer.capture_lambda_handler(capture_response=False)deflambda_handler(event:dict,context:LambdaContext)->str:payment_id=event.get("payment_id","")report=fetch_payment_report(payment_id=payment_id)returnreport.read().decode()

Use capture_error=False parameter in both capture_lambda_handler and capture_method decorators to instruct Tracer not to serialize exceptions as metadata.

Info

Useful when returning sensitive information in exceptions/stack traces you don't control

Disabling exception auto-capture for tracing metadata

importosimportrequestsfromaws_lambda_powertoolsimportTracerfromaws_lambda_powertools.utilities.typingimportLambdaContexttracer=Tracer()ENDPOINT=os.getenv("PAYMENT_API","")classPaymentError(Exception):...@tracer.capture_method(capture_error=False)defcollect_payment(charge_id:str)->dict:try:ret=requests.post(url=f"{ENDPOINT}/collect",data={"charge_id":charge_id})ret.raise_for_status()returnret.json()exceptrequests.HTTPErrorase:raisePaymentError(f"Unable to collect payment for charge {charge_id}")frome@tracer.capture_lambda_handler(capture_error=False)deflambda_handler(event:dict,context:LambdaContext)->str:charge_id=event.get("charge_id","")ret=collect_payment(charge_id=charge_id)returnret.get("receipt_id","")

importosimportrequestsfromaws_lambda_powertoolsimportTracerfromaws_lambda_powertools.utilities.typingimportLambdaContextENDPOINT=os.getenv("PAYMENT_API","")IGNORE_URLS=["/collect","/refund"]tracer=Tracer()tracer.ignore_endpoint(hostname=ENDPOINT,urls=IGNORE_URLS)tracer.ignore_endpoint(hostname=f"*.{ENDPOINT}",urls=IGNORE_URLS)# `<stage>.ENDPOINT`classPaymentError(Exception):...@tracer.capture_method(capture_error=False)defcollect_payment(charge_id:str)->dict:try:ret=requests.post(url=f"{ENDPOINT}/collect",data={"charge_id":charge_id})ret.raise_for_status()returnret.json()exceptrequests.HTTPErrorase:raisePaymentError(f"Unable to collect payment for charge {charge_id}")frome@tracer.capture_lambda_handler(capture_error=False)deflambda_handler(event:dict,context:LambdaContext)->str:charge_id=event.get("charge_id","")ret=collect_payment(charge_id=charge_id)returnret.get("receipt_id","")

This snippet assumes you have aiohttp as a dependency

You can use aiohttp_trace_config function to create a valid aiohttp trace_config object. This is necessary since X-Ray utilizes aiohttp trace hooks to capture requests end-to-end.

Tracer keeps a copy of its configuration after the first initialization. This is useful for scenarios where you want to use Tracer in more than one location across your code base.

Warning: Import order matters when using Lambda Layers or multiple modules

Do not set auto_patch=False when reusing Tracer in Lambda Layers, or in multiple modules.

This can result in the first Tracer config being inherited by new instances, and their modules not being patched.

Tracer will automatically ignore imported modules that have been patched.

Tracer is disabled by default when not running in the AWS Lambda environment, including AWS SAM CLI and Chalice environments. This means no code changes or environment variables to be set.

Use annotations on key operations to slice and dice traces, create unique views, and create metrics from it via Trace Groups

Use a namespace when adding metadata to group data more easily

Annotations and metadata are added to the current subsegment opened. If you want them in a specific subsegment, use a context manager via the escape hatch mechanism