# Build Tools - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/build_recipes/build-tools](https://docs.aws.amazon.com/powertools/python/latest/build_recipes/build-tools)

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

This guide covers different build tools and dependency managers for packaging Lambda functions with Powertools for AWS Lambda (Python). Each tool has its strengths and is optimized for different use cases.

Requirements file security

For simplicity, examples in this guide use requirements.txt files with pinned versions. In production environments, you should use hash-checking for enhanced security by including --hash flags. Learn more about secure package installation in the pip documentation.

pip is Python's standard package installer - simple, reliable, and available everywhere. Perfect for straightforward Lambda functions where you need basic dependency management without complex workflows.

Cross-platform compatibility

Always use --platform manylinux2014_x86_64 and --only-binary=:all: flags when building on non-Linux systems to ensure Lambda compatibility. This forces pip to download Linux-compatible wheels instead of compiling from source.

fromaws_lambda_powertoolsimportLogger,Metrics,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.metricsimportMetricUnitlogger=Logger()tracer=Tracer()metrics=Metrics()app=APIGatewayRestResolver()@app.get("/hello")defhello():logger.info("Hello World API called")metrics.add_metric(name="HelloWorldInvocations",unit=MetricUnit.Count,value=1)return{"message":"Hello World from Powertools!"}@app.get("/health")defhealth_check():return{"status":"healthy","service":"powertools-pip-example"}@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handler@metrics.log_metrics(capture_cold_start_metric=True)deflambda_handler(event,context):returnapp.resolve(event,context)

fromaws_lambda_powertoolsimportLogger,Metrics,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.metricsimportMetricUnitlogger=Logger()tracer=Tracer()metrics=Metrics()app=APIGatewayRestResolver()@app.get("/hello")defhello():logger.info("Hello World API called")metrics.add_metric(name="HelloWorldInvocations",unit=MetricUnit.Count,value=1)return{"message":"Hello World from Powertools!"}@app.get("/health")defhealth_check():return{"status":"healthy","service":"powertools-pip-example"}@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handler@metrics.log_metrics(capture_cold_start_metric=True)deflambda_handler(event,context):returnapp.resolve(event,context)

uv is an extremely fast Python package manager written in Rust, designed as a drop-in replacement for pip and pip-tools. It offers 10-100x faster dependency resolution and installation, making it ideal for CI/CD pipelines and performance-critical builds. Learn more at docs.astral.sh/uv/.

Cross-platform compatibility

Use uv pip install with --platform manylinux2014_x86_64 and --only-binary=:all: flags when building on non-Linux systems. This ensures Lambda-compatible wheels are downloaded instead of compiling from source.

[project]name="lambda-powertools-uv"version="0.1.0"description="Lambda function with Powertools using uv"requires-python=">=3.10"dependencies=["aws-lambda-powertools[all]>=3.18.0","pydantic>=2.10.0","requests>=2.32.0",][project.optional-dependencies]dev=["pytest>=8.0.0","black>=24.0.0","mypy>=1.8.0",]

Poetry is a modern Python dependency manager that handles packaging, dependency resolution, and virtual environments. It uses lock files to ensure reproducible builds and provides excellent developer experience with semantic versioning.

Cross-platform compatibility

When building on non-Linux systems, use pip install with --platform manylinux2014_x86_64 and --only-binary=:all: flags after exporting requirements from Poetry. This ensures Lambda-compatible wheels are installed.

[tool.poetry]name="lambda-powertools-app"version="0.1.0"description="Lambda function with Powertools"[tool.poetry.dependencies]python="^3.10"aws-lambda-powertools={extras=["all"],version="^3.18.0"}pydantic="^2.10.0"requests="^2.32.0"[tool.poetry.group.dev.dependencies]pytest="^8.0.0"black="^24.0.0"mypy="^1.8.0"[tool.poetry.requires-plugins]poetry-plugin-export=">=1.8"[build-system]requires=["poetry-core"]build-backend="poetry.core.masonry.api"

AWS SAM (Serverless Application Model) is AWS's framework for building serverless applications using CloudFormation templates. It provides local testing capabilities, built-in best practices, and seamless integration with AWS services, making it the go-to choice for AWS-native serverless development.

SAM automatically resolves multi-architecture compatibility issues by building functions inside Lambda-compatible containers (--use-container flag), ensuring dependencies are installed with the correct architecture and glibc versions for the Lambda runtime environment. This eliminates the common problem of architecture mismatches when building on macOS/Windows.

AWSTemplateFormatVersion:'2010-09-09'Transform:AWS::Serverless-2016-10-31Globals:Function:Runtime:python3.13Timeout:30MemorySize:512Environment:Variables:POWERTOOLS_SERVICE_NAME:!RefAWS::StackNamePOWERTOOLS_METRICS_NAMESPACE:MyAppPOWERTOOLS_LOG_LEVEL:INFOResources:# Single Lambda Function with all dependencies includedApiFunction:Type:AWS::Serverless::FunctionProperties:CodeUri:src/Handler:app_sam_no_layer.lambda_handlerEvents:ApiEvent:Type:ApiProperties:Path:/{proxy+}Method:ANYEnvironment:Variables:POWERTOOLS_SERVICE_NAME:api-serviceOutputs:ApiUrl:Description:API Gateway endpoint URLValue:!Sub"https://${ServerlessRestApi}.execute-api.${AWS::Region}.amazonaws.com/Prod/"

fromtypingimportOptionalfrompydanticimportBaseModelfromaws_lambda_powertoolsimportLogger,Metrics,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.metricsimportMetricUnitlogger=Logger()tracer=Tracer()metrics=Metrics()app=APIGatewayRestResolver()classUserModel(BaseModel):name:stremail:strage:Optional[int]=None@app.get("/health")defhealth_check():return{"status":"healthy","service":"powertools-sam"}@app.post("/users")defcreate_user(user:UserModel):logger.info("Creating user",extra={"user":user.model_dump()})metrics.add_metric(name="UserCreated",unit=MetricUnit.Count,value=1)return{"message":f"User {user.name} created successfully"}@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handler@metrics.log_metrics(capture_cold_start_metric=True)deflambda_handler(event,context):returnapp.resolve(event,context)

123456789

#!/bin/bashecho"🏗️ Building SAM application without layers..."# Build and deploy (SAM will handle dependency installation)
sambuild--use-container
samdeploy--guided
echo"✅ SAM application deployed successfully (no layers)"

fromtypingimportOptionalimportrequestsfrompydanticimportBaseModelfromaws_lambda_powertoolsimportLogger,Metrics,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.metricsimportMetricUnitlogger=Logger()tracer=Tracer()metrics=Metrics()app=APIGatewayRestResolver()classUserModel(BaseModel):name:stremail:strage:Optional[int]=None@app.get("/health")defhealth_check():return{"status":"healthy","service":"powertools-sam-layers"}@app.post("/users")defcreate_user(user:UserModel):logger.info("Creating user",extra={"user":user.model_dump()})metrics.add_metric(name="UserCreated",unit=MetricUnit.Count,value=1)return{"message":f"User {user.name} created successfully"}@app.get("/external")@tracer.capture_methoddeffetch_external_data():"""Example using requests from dependencies layer"""response=requests.get("https://httpbin.org/json")data=response.json()metrics.add_metric(name="ExternalApiCalled",unit=MetricUnit.Count,value=1)return{"external_data":data}@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handler@metrics.log_metrics(capture_cold_start_metric=True)deflambda_handler(event,context):returnapp.resolve(event,context)

from__future__importannotationsimportjsonfromtypingimportAnyfrompydanticimportBaseModel,ValidationErrorfromaws_lambda_powertoolsimportLogger,Metrics,Tracerfromaws_lambda_powertools.utilities.batchimportBatchProcessor,EventType,process_partial_responsefromaws_lambda_powertools.utilities.typingimportLambdaContextlogger=Logger()tracer=Tracer()metrics=Metrics()# Initialize batch processor for SQSprocessor=BatchProcessor(event_type=EventType.SQS)classWorkerMessage(BaseModel):task_id:strtask_type:strpayload:dict@tracer.capture_methoddefrecord_handler(record):"""Process individual SQS record"""try:# Parse and validate messagemessage_data=json.loads(record.body)worker_message=WorkerMessage(**message_data)logger.info("Processing task",extra={"task_id":worker_message.task_id,"task_type":worker_message.task_type})# Simulate work based on task typeifworker_message.task_type=="email":# Process email tasklogger.info("Sending email",extra={"task_id":worker_message.task_id})elifworker_message.task_type=="report":# Process report tasklogger.info("Generating report",extra={"task_id":worker_message.task_id})else:logger.warning("Unknown task type",extra={"task_type":worker_message.task_type})metrics.add_metric(name="TaskProcessed",unit="Count",value=1)metrics.add_metadata(key="task_type",value=worker_message.task_type)return{"status":"success","task_id":worker_message.task_id}exceptValidationErrorase:logger.error("Invalid message format",extra={"error":str(e)})metrics.add_metric(name="TaskFailed",unit="Count",value=1)raiseexceptExceptionase:logger.error("Task processing failed",extra={"error":str(e)})metrics.add_metric(name="TaskFailed",unit="Count",value=1)raise@logger.inject_lambda_context@tracer.capture_lambda_handler@metrics.log_metricsdeflambda_handler(event:dict[str,Any],context:LambdaContext):"""Process SQS messages using BatchProcessor"""returnprocess_partial_response(event=event,record_handler=record_handler,processor=processor,context=context,)

#!/bin/bashecho"🏗️ Building SAM application with layers..."# Build Dependencies layer (Powertools uses public layer ARN)echo"Building Dependencies layer..."
mkdir-players/dependencies/python
pipinstallpydanticrequests-tlayers/dependencies/python/
# Optimize layers (remove unnecessary files)echo"Optimizing layers..."
findlayers/-name"*.pyc"-delete
findlayers/-name"__pycache__"-typed-execrm-rf{}+2>/dev/null||true
findlayers/-name"tests"-typed-execrm-rf{}+2>/dev/null||true
findlayers/-name"*.dist-info"-typed-execrm-rf{}+2>/dev/null||true# Build and deploy
sambuild--use-container
samdeploy--guided
echo"✅ SAM application with layers deployed successfully"# Show layer sizesecho""echo"📊 Layer sizes:"echo"Powertools: Using public layer ARN (no local build needed)"
du-shlayers/dependencies/

Configure different environments (dev, staging, prod) with environment-specific settings and layer references. This example demonstrates how to use parameters, mappings, and conditions to create flexible, multi-environment deployments.

The AWS CDK (Cloud Development Kit) allows you to define cloud infrastructure using familiar programming languages like Python, TypeScript, or Java. It provides type safety, IDE support, and the ability to create reusable constructs, making it perfect for complex infrastructure requirements and teams that prefer code over YAML.

CDK uses the concept of Apps, Stacks, and Constructs to organize infrastructure. A CDK app contains one or more stacks, and each stack contains constructs that represent AWS resources.

#!/usr/bin/env python3importaws_cdkascdkfromaws_cdkimport(Duration,Stack,)fromaws_cdkimport(aws_apigatewayasapigateway,)fromaws_cdkimport(aws_lambdaas_lambda,)fromaws_cdkimport(aws_logsaslogs,)fromconstructsimportConstructclassPowertoolsLambdaStack(Stack):def__init__(self,scope:Construct,construct_id:str,**kwargs)->None:super().__init__(scope,construct_id,**kwargs)# Use public Powertools layerpowertools_layer=_lambda.LayerVersion.from_layer_version_arn(self,"PowertoolsLayer",layer_version_arn="arn:aws:lambda:us-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36",)# Lambda Functionapi_function=_lambda.Function(self,"ApiFunction",runtime=_lambda.Runtime.PYTHON_3_13,handler="lambda_function.lambda_handler",code=_lambda.Code.from_asset("src"),layers=[powertools_layer],timeout=Duration.seconds(30),memory_size=512,environment={"POWERTOOLS_SERVICE_NAME":"api-service","POWERTOOLS_METRICS_NAMESPACE":"MyApp","POWERTOOLS_LOG_LEVEL":"INFO",},log_retention=logs.RetentionDays.ONE_WEEK,)# API Gatewayapi=apigateway.RestApi(self,"ApiGateway",rest_api_name="Powertools API",description="API powered by Lambda with Powertools",)# API Integrationintegration=apigateway.LambdaIntegration(api_function)api.root.add_proxy(default_integration=integration,any_method=True,)# Outputscdk.CfnOutput(self,"ApiUrl",value=api.url,description="API Gateway URL",)app=cdk.App()PowertoolsLambdaStack(app,"PowertoolsLambdaStack")app.synth()

fromaws_cdkimport(Duration,RemovalPolicy,Stack,)fromaws_cdkimport(aws_apigatewayasapigateway,)fromaws_cdkimport(aws_dynamodbasdynamodb,)fromaws_cdkimport(aws_lambdaas_lambda,)fromaws_cdkimport(aws_lambda_event_sourcesaslambda_event_sources,)fromaws_cdkimport(aws_sqsassqs,)fromconstructsimportConstructclassPowertoolsStack(Stack):def__init__(self,scope:Construct,construct_id:str,environment:str="dev",**kwargs)->None:super().__init__(scope,construct_id,**kwargs)self.deploy_environment=environment# Shared Powertools Layer (using public layer)self.powertools_layer=self._create_powertools_layer()# DynamoDB Tableself.table=self._create_dynamodb_table()# SQS Queueself.queue=self._create_sqs_queue()# Lambda Functionsself.api_function=self._create_api_function()self.worker_function=self._create_worker_function()# API Gatewayself.api=self._create_api_gateway()def_create_powertools_layer(self)->_lambda.ILayerVersion:return_lambda.LayerVersion.from_layer_version_arn(self,"PowertoolsLayer",layer_version_arn="arn:aws:lambda:us-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV3-python313-x86_64:36",)def_create_dynamodb_table(self)->dynamodb.Table:returndynamodb.Table(self,"DataTable",table_name=f"powertools-{self.deploy_environment}-data",partition_key=dynamodb.Attribute(name="pk",type=dynamodb.AttributeType.STRING),billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,removal_policy=RemovalPolicy.DESTROYifself.deploy_environment!="prod"elseRemovalPolicy.RETAIN,)def_create_sqs_queue(self)->sqs.Queue:returnsqs.Queue(self,"WorkerQueue",queue_name=f"powertools-{self.deploy_environment}-worker",visibility_timeout=Duration.seconds(180),)def_create_api_function(self)->_lambda.Function:function=_lambda.Function(self,"ApiFunction",runtime=_lambda.Runtime.PYTHON_3_13,handler="app.lambda_handler",code=_lambda.Code.from_asset("src/app"),layers=[self.powertools_layer],timeout=Duration.seconds(30),memory_size=512ifself.deploy_environment=="prod"else256,environment={"ENVIRONMENT":self.deploy_environment,"POWERTOOLS_SERVICE_NAME":f"app-{self.deploy_environment}","POWERTOOLS_METRICS_NAMESPACE":f"MyApp/{self.deploy_environment}","POWERTOOLS_LOG_LEVEL":"INFO"ifself.deploy_environment=="prod"else"DEBUG","TABLE_NAME":self.table.table_name,"QUEUE_URL":self.queue.queue_url,},)# Grant permissionsself.table.grant_read_write_data(function)self.queue.grant_send_messages(function)returnfunctiondef_create_worker_function(self)->_lambda.Function:function=_lambda.Function(self,"WorkerFunction",runtime=_lambda.Runtime.PYTHON_3_13,handler="worker.lambda_handler",code=_lambda.Code.from_asset("src/worker"),layers=[self.powertools_layer],timeout=Duration.seconds(120),memory_size=1024ifself.deploy_environment=="prod"else512,environment={"ENVIRONMENT":self.deploy_environment,"POWERTOOLS_SERVICE_NAME":f"worker-{self.deploy_environment}","POWERTOOLS_METRICS_NAMESPACE":f"MyApp/{self.deploy_environment}","POWERTOOLS_LOG_LEVEL":"INFO"ifself.deploy_environment=="prod"else"DEBUG","TABLE_NAME":self.table.table_name,},)# Add SQS event source with partial failure supportfunction.add_event_source(lambda_event_sources.SqsEventSource(self.queue,batch_size=10,report_batch_item_failures=True,),)# Grant permissionsself.table.grant_read_write_data(function)returnfunctiondef_create_api_gateway(self)->apigateway.RestApi:api=apigateway.RestApi(self,"ApiGateway",rest_api_name=f"Powertools API - {self.deploy_environment}",description=f"API for {self.deploy_environment} environment",)integration=apigateway.LambdaIntegration(self.api_function)api.root.add_proxy(default_integration=integration,any_method=True,)returnapi

#!/usr/bin/env python3importaws_cdkascdkfromstacks.powertools_cdk_stackimportPowertoolsStackapp=cdk.App()# Get environment from context or default to devenvironment=app.node.try_get_context("environment")or"dev"# Create stack for the specified environmentPowertoolsStack(app,f"PowertoolsStack-{environment}",environment=environment,env=cdk.Environment(account=app.node.try_get_context("account"),region=app.node.try_get_context("region")or"us-east-1",),)app.synth()

importosimportboto3fromaws_lambda_powertoolsimportLogger,Metrics,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.metricsimportMetricUnitlogger=Logger()tracer=Tracer()metrics=Metrics()app=APIGatewayRestResolver()# Initialize AWS clientsdynamodb=boto3.resource("dynamodb")sqs=boto3.client("sqs")table=dynamodb.Table(os.environ["TABLE_NAME"])queue_url=os.environ["QUEUE_URL"]@app.get("/health")defhealth_check():return{"status":"healthy","service":"powertools-cdk-api"}@app.post("/tasks")@tracer.capture_methoddefcreate_task():task_data=app.current_event.json_body# Store in DynamoDBtable.put_item(Item={"pk":task_data["task_id"],"task_type":task_data["task_type"],"status":"pending"})# Send to SQS for processingsqs.send_message(QueueUrl=queue_url,MessageBody=app.current_event.body)metrics.add_metric(name="TaskCreated",unit=MetricUnit.Count,value=1)logger.info("Task created",extra={"task_id":task_data["task_id"]})return{"message":"Task created successfully","task_id":task_data["task_id"]}@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handler@metrics.log_metrics(capture_cold_start_metric=True)deflambda_handler(event,context):returnapp.resolve(event,context)

from__future__importannotationsimportjsonimportosfromtypingimportAnyimportboto3fromaws_lambda_powertoolsimportLogger,Metrics,Tracerfromaws_lambda_powertools.utilities.batchimportBatchProcessor,EventType,process_partial_responsefromaws_lambda_powertools.utilities.typingimportLambdaContextlogger=Logger()tracer=Tracer()metrics=Metrics()# Initialize batch processor for SQSprocessor=BatchProcessor(event_type=EventType.SQS)# Initialize AWS clientsdynamodb=boto3.resource("dynamodb")table=dynamodb.Table(os.environ["TABLE_NAME"])@tracer.capture_methoddefrecord_handler(record):"""Process individual SQS record"""try:# Parse messagemessage_data=json.loads(record.body)task_id=message_data["task_id"]task_type=message_data["task_type"]logger.info("Processing task",extra={"task_id":task_id,"task_type":task_type})# Update task status in DynamoDBtable.update_item(Key={"pk":task_id},UpdateExpression="SET #status = :status",ExpressionAttributeNames={"#status":"status"},ExpressionAttributeValues={":status":"processing"},)# Simulate work based on task typeiftask_type=="email":logger.info("Sending email",extra={"task_id":task_id})eliftask_type=="report":logger.info("Generating report",extra={"task_id":task_id})else:logger.warning("Unknown task type",extra={"task_type":task_type})# Mark as completedtable.update_item(Key={"pk":task_id},UpdateExpression="SET #status = :status",ExpressionAttributeNames={"#status":"status"},ExpressionAttributeValues={":status":"completed"},)metrics.add_metric(name="TaskProcessed",unit="Count",value=1)metrics.add_metadata(key="task_type",value=task_type)return{"status":"success","task_id":task_id}exceptExceptionase:logger.error("Task processing failed",extra={"error":str(e)})metrics.add_metric(name="TaskFailed",unit="Count",value=1)raise@logger.inject_lambda_context@tracer.capture_lambda_handler@metrics.log_metricsdeflambda_handler(event:dict[str,Any],context:LambdaContext):"""Process SQS messages using BatchProcessor"""returnprocess_partial_response(event=event,record_handler=record_handler,processor=processor,context=context,)

1 2 3 4 5 6 7 8 91011121314

#!/bin/bash# Deploy to different environmentsenvironments=("dev""staging""prod")forenvin"${environments[@]}";doecho"🚀 Deploying to $env environment..."cdkdeployPowertoolsStack-$env\--contextenvironment=$env\--require-approvalnever
echo"✅ $env deployment completed"done

Pants is a powerful build system designed for large codebases and monorepos. It provides incremental builds, dependency inference, and advanced caching mechanisms. Ideal for organizations with complex Python projects that need fine-grained build control and optimization.

from__future__importannotationsfromtypingimportAnyimportrequestsfrompydanticimportBaseModelfromaws_lambda_powertoolsimportLogger,Metrics,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.utilities.typingimportLambdaContextlogger=Logger()tracer=Tracer()metrics=Metrics()app=APIGatewayRestResolver()classTodoItem(BaseModel):id:inttitle:strcompleted:bool=Falseuser_id:int|None=None@app.get("/todos")@tracer.capture_methoddefget_todos()->TodoItem:"""Fetch todos from external API"""logger.info("Fetching todos from external API")response=requests.get("https://jsonplaceholder.typicode.com/todos")response.raise_for_status()returnresponse.json()[0]@logger.inject_lambda_context@tracer.capture_lambda_handler@metrics.log_metricsdeflambda_handler(event:dict[str,Any],context:LambdaContext):returnapp.resolve(event,context)

1 2 3 4 5 6 7 8 910111213141516171819202122

#!/bin/bash# Build the PEX binary
pantspackage:lambda_function
# The PEX file is created in dist/# Rename it to a more descriptive name
mvdist/lambda_function.pexlambda-pants.pex
# For Lambda deployment, we need to extract the PEX
mkdir-pbuild/
cdbuild/
# Extract PEX contents
python../lambda-pants.pex--pex-root.--pex-path.-c"import sys; sys.exit(0)"# Create deployment zip
zip-r../lambda-pants.zip.
cd..
echo"✅ Pants deployment package created: lambda-pants.zip"echo"✅ Pants PEX binary created: lambda-pants.pex"

Pants excels at managing complex projects with multiple Lambda functions that share dependencies. This approach provides significant benefits for monorepo architectures and microservices.

fromaws_lambda_powertoolsimportLogger,Metrics,Tracerfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.loggingimportcorrelation_pathsfromaws_lambda_powertools.metricsimportMetricUnitlogger=Logger()tracer=Tracer()metrics=Metrics()app=APIGatewayRestResolver()@app.get("/health")defhealth_check():return{"status":"healthy","service":"powertools-pants-api"}@app.get("/metrics")defget_metrics():metrics.add_metric(name="MetricsEndpointCalled",unit=MetricUnit.Count,value=1)return{"message":"Metrics recorded"}@app.post("/tasks")defcreate_task():task_data=app.current_event.json_bodylogger.info("Task created",extra={"task":task_data})metrics.add_metric(name="TaskCreated",unit=MetricUnit.Count,value=1)return{"message":"Task created successfully","task_id":task_data.get("id")}@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)@tracer.capture_lambda_handler@metrics.log_metrics(capture_cold_start_metric=True)deflambda_handler(event,context):returnapp.resolve(event,context)