# Persistence - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/idempotency/persistence](https://docs.aws.amazon.com/powertools/python/latest/api_doc/idempotency/persistence)

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

defconfigure(self,config:IdempotencyConfig,function_name:str|None=None,key_prefix:str|None=None,)->None:""" Initialize the base persistence layer from the configuration settings Parameters ---------- config: IdempotencyConfig Idempotency configuration settings function_name: str, Optional The name of the function being decorated key_prefix: str | Optional Custom prefix for idempotency key: key_prefix#hash """self.function_name=(key_prefixorf"{os.getenv(constants.LAMBDA_FUNCTION_NAME_ENV,'test-func')}.{function_nameor''}")ifself.configured:# Prevent being reconfigured multiple timesreturnself.configured=Trueself.event_key_jmespath=config.event_key_jmespathifconfig.event_key_jmespath:self.event_key_compiled_jmespath=jmespath.compile(config.event_key_jmespath)self.jmespath_options=config.jmespath_optionsor{"custom_functions":PowertoolsFunctions()}ifconfig.payload_validation_jmespath:self.validation_key_jmespath=jmespath.compile(config.payload_validation_jmespath)self.payload_validation_enabled=Trueself.raise_on_no_idempotency_key=config.raise_on_no_idempotency_keyself.expires_after_seconds=config.expires_after_secondsself.use_local_cache=config.use_local_cacheifself.use_local_cache:self._cache=LRUDict(max_items=config.local_cache_max_items)self.hash_function=getattr(hashlib,config.hash_function)

defdelete_record(self,data:dict[str,Any],exception:Exception):""" Delete record from the persistence store Parameters ---------- data: dict[str, Any] Payload exception The exception raised by the function """idempotency_key=self._get_hashed_idempotency_key(data=data)ifidempotency_keyisNone:# If the idempotency key is None, no data will be saved in the Persistence Layer.# See: https://github.com/aws-powertools/powertools-lambda-python/issues/2465returnNonedata_record=DataRecord(idempotency_key=idempotency_key)logger.debug(f"Function raised an exception ({type(exception).__name__}). Clearing in progress record in persistence "f"store for idempotency key: {data_record.idempotency_key}",)self._delete_record(data_record=data_record)self._delete_from_cache(idempotency_key=data_record.idempotency_key)

defget_record(self,data:dict[str,Any])->DataRecord|None:""" Retrieve idempotency key for data provided, fetch from persistence store, and convert to DataRecord. Parameters ---------- data: dict[str, Any] Payload Returns ------- DataRecord DataRecord representation of existing record found in persistence store Raises ------ IdempotencyItemNotFoundError Exception raised if no record exists in persistence store with the idempotency key IdempotencyValidationError Payload doesn't match the stored record for the given idempotency key """idempotency_key=self._get_hashed_idempotency_key(data=data)ifidempotency_keyisNone:# If the idempotency key is None, no data will be saved in the Persistence Layer.# See: https://github.com/aws-powertools/powertools-lambda-python/issues/2465returnNonecached_record=self._retrieve_from_cache(idempotency_key=idempotency_key)ifcached_record:logger.debug(f"Idempotency record found in cache with idempotency key: {idempotency_key}")self._validate_payload(data_payload=data,stored_data_record=cached_record)returncached_recordrecord=self._get_record(idempotency_key=idempotency_key)self._validate_payload(data_payload=data,stored_data_record=record)self._save_to_cache(data_record=record)returnrecord

defsave_inprogress(self,data:dict[str,Any],remaining_time_in_millis:int|None=None)->None:""" Save record of function's execution being in progress Parameters ---------- data: dict[str, Any] Payload remaining_time_in_millis: int | None If expiry of in-progress invocations is enabled, this will contain the remaining time available in millis """idempotency_key=self._get_hashed_idempotency_key(data=data)ifidempotency_keyisNone:# If the idempotency key is None, no data will be saved in the Persistence Layer.# See: https://github.com/aws-powertools/powertools-lambda-python/issues/2465returnNonedata_record=DataRecord(idempotency_key=idempotency_key,status=STATUS_CONSTANTS["INPROGRESS"],expiry_timestamp=self._get_expiry_timestamp(),payload_hash=self._get_hashed_payload(data=data),)# When Lambda kills the container after timeout, the remaining_time_in_millis is 0, which is considered False.# Therefore, we need to check if remaining_time_in_millis is not None (>=0) to handle this case.# See: https://github.com/aws-powertools/powertools-lambda-python/issues/4759ifremaining_time_in_millisisnotNone:now=datetime.datetime.now()period=datetime.timedelta(milliseconds=remaining_time_in_millis)timestamp=(now+period).timestamp()data_record.in_progress_expiry_timestamp=int(timestamp*1000)else:warnings.warn("Couldn't determine the remaining time left. ""Did you call register_lambda_context on IdempotencyConfig?",stacklevel=2,)logger.debug(f"Saving in progress record for idempotency key: {data_record.idempotency_key}")ifself._retrieve_from_cache(idempotency_key=data_record.idempotency_key):raiseIdempotencyItemAlreadyExistsErrorself._put_record(data_record=data_record)

defsave_success(self,data:dict[str,Any],result:dict)->None:""" Save record of function's execution completing successfully Parameters ---------- data: dict[str, Any] Payload result: dict The response from function """idempotency_key=self._get_hashed_idempotency_key(data=data)ifidempotency_keyisNone:# If the idempotency key is None, no data will be saved in the Persistence Layer.# See: https://github.com/aws-powertools/powertools-lambda-python/issues/2465returnNoneresponse_data=json.dumps(result,cls=Encoder,sort_keys=True)data_record=DataRecord(idempotency_key=idempotency_key,status=STATUS_CONSTANTS["COMPLETED"],expiry_timestamp=self._get_expiry_timestamp(),response_data=response_data,payload_hash=self._get_hashed_payload(data=data),)logger.debug(f"Function successfully executed. Saving record to persistence store with "f"idempotency key: {data_record.idempotency_key}",)self._update_record(data_record=data_record)self._save_to_cache(data_record=data_record)

def__init__(self,idempotency_key:str,status:str="",expiry_timestamp:int|None=None,in_progress_expiry_timestamp:int|None=None,response_data:str="",payload_hash:str="",sort_key:str|None=None,)->None:""" Parameters ---------- idempotency_key: str hashed representation of the idempotent data status: str, optional status of the idempotent record expiry_timestamp: int, optional time before the record should expire, in seconds in_progress_expiry_timestamp: int, optional time before the record should expire while in the INPROGRESS state, in seconds payload_hash: str, optional hashed representation of payload response_data: str, optional response data from previous executions using the record sort_key: str, optional sort key when using composite key """self.idempotency_key=idempotency_keyself.payload_hash=payload_hashself.expiry_timestamp=expiry_timestampself.in_progress_expiry_timestamp=in_progress_expiry_timestampself._status=statusself.response_data=response_dataself.sort_key=sort_key

defget_expiration_datetime(self)->datetime.datetime|None:""" Converts the expiry timestamp to a datetime object. This method checks if an expiry timestamp exists and converts it to a datetime object. If no timestamp is present, it returns None. Returns: ------- datetime.datetime | None A datetime object representing the expiration time, or None if no expiry timestamp is set. Note: ---- The returned datetime object is timezone-naive and assumes the timestamp is in the system's local timezone. Lambda default timezone is UTC. """ifself.expiry_timestamp:returndatetime.datetime.fromtimestamp(int(self.expiry_timestamp))returnNone

Source code in aws_lambda_powertools/utilities/idempotency/persistence/datarecord.py

89909192939495969798

defresponse_json_as_dict(self)->dict|None:""" Get response data deserialized to python dict Returns ------- dict | None previous response data deserialized """returnjson.loads(self.response_data)ifself.response_dataelseNone

def__init__(self,table_name:str,key_attr:str="id",static_pk_value:str|None=None,sort_key_attr:str|None=None,expiry_attr:str="expiration",in_progress_expiry_attr:str="in_progress_expiration",status_attr:str="status",data_attr:str="data",validation_key_attr:str="validation",boto_config:Config|None=None,boto3_session:boto3.session.Session|None=None,boto3_client:DynamoDBClient|None=None,):""" Initialize the DynamoDB client Parameters ---------- table_name: str Name of the table to use for storing execution records key_attr: str, optional DynamoDB attribute name for partition key, by default "id" static_pk_value: str, optional DynamoDB attribute value for partition key, by default "idempotency#<function-name>". This will be used if the sort_key_attr is set. sort_key_attr: str, optional DynamoDB attribute name for the sort key expiry_attr: str, optional DynamoDB attribute name for expiry timestamp, by default "expiration" in_progress_expiry_attr: str, optional DynamoDB attribute name for in-progress expiry timestamp, by default "in_progress_expiration" status_attr: str, optional DynamoDB attribute name for status, by default "status" data_attr: str, optional DynamoDB attribute name for response data, by default "data" validation_key_attr: str, optional DynamoDB attribute name for hashed representation of the parts of the event used for validation boto_config: botocore.config.Config, optional Botocore configuration to pass during client initialization boto3_session : boto3.session.Session, optional Boto3 session to use for AWS API communication boto3_client : DynamoDBClient, optional Boto3 DynamoDB Client to use, boto3_session and boto_config will be ignored if both are provided Example -------- **Create a DynamoDB persistence layer with custom settings** >>> from aws_lambda_powertools.utilities.idempotency import ( >>> idempotent, DynamoDBPersistenceLayer >>> ) >>> >>> persistence_store = DynamoDBPersistenceLayer(table_name="idempotency_store") >>> >>> @idempotent(persistence_store=persistence_store) >>> def handler(event, context): >>> return {"StatusCode": 200} """ifboto3_clientisNone:boto3_session=boto3_sessionorboto3.session.Session()boto3_client=boto3_session.client("dynamodb",config=boto_config)self.client=boto3_clientuser_agent.register_feature_to_client(client=self.client,feature="idempotency")ifsort_key_attr==key_attr:raiseValueError(f"key_attr [{key_attr}] and sort_key_attr [{sort_key_attr}] cannot be the same!")ifstatic_pk_valueisNone:static_pk_value=f"idempotency#{os.getenv(constants.LAMBDA_FUNCTION_NAME_ENV,'')}"self.table_name=table_nameself.key_attr=key_attrself.static_pk_value=static_pk_valueself.sort_key_attr=sort_key_attrself.expiry_attr=expiry_attrself.in_progress_expiry_attr=in_progress_expiry_attrself.status_attr=status_attrself.data_attr=data_attrself.validation_key_attr=validation_key_attr# Use DynamoDB's ReturnValuesOnConditionCheckFailure to optimize put and get operations and optimize costs.# This feature is supported in boto3 versions 1.26.164 and later.self.return_value_on_condition=({"ReturnValuesOnConditionCheckFailure":"ALL_OLD"}ifself.boto3_supports_condition_check_failure(boto3.__version__)else{})self._deserializer=TypeDeserializer()super().__init__()

@staticmethoddefboto3_supports_condition_check_failure(boto3_version:str)->bool:""" Check if the installed boto3 version supports condition check failure. Params ------ boto3_version: str The boto3 version Returns ------- bool True if the boto3 version supports condition check failure, False otherwise. """# Only supported in boto3 1.26.164 and abovemajor,minor,*patch=map(int,boto3_version.split("."))return(major,minor,*patch)>=(1,26,164)

def__init__(self,url:str="",host:str="",port:int=6379,username:str="",password:str="",# nosec - password for Cache connectiondb_index:int=0,mode:Literal["standalone","cluster"]="standalone",ssl:bool=True,client:RedisClientProtocol|None=None,in_progress_expiry_attr:str="in_progress_expiration",expiry_attr:str="expiration",status_attr:str="status",data_attr:str="data",validation_key_attr:str="validation",):""" Initialize the Cache Persistence Layer Parameters ---------- host: str, optional Cache host port: int, optional: default 6379 Cache port username: str, optional Cache username password: str, optional Cache password url: str, optional Cache connection string, using url will override the host/port in the previous parameters db_index: int, optional: default 0 Cache db index mode: str, Literal["standalone","cluster"] set Cache client mode, choose from standalone/cluster ssl: bool, optional: default True set whether to use ssl for Cache connection client: CacheClientProtocol, optional Bring your own Cache client that follows CacheClientProtocol. If provided, all other connection configuration options will be ignored expiry_attr: str, optional Cache json attribute name for expiry timestamp, by default "expiration" in_progress_expiry_attr: str, optional Cache json attribute name for in-progress expiry timestamp, by default "in_progress_expiration" status_attr: str, optional Cache json attribute name for status, by default "status" data_attr: str, optional Cache json attribute name for response data, by default "data" validation_key_attr: str, optional Cache json attribute name for hashed representation of the parts of the event used for validation Examples -------- ```python from redis import Redis from aws_lambda_powertools.utilities.idempotency import ( idempotent, ) from aws_lambda_powertools.utilities.idempotency.persistence.cache import ( CachePersistenceLayer, ) client = redis.Redis( host="localhost", port="6379", decode_responses=True, ) persistence_layer = CachePersistenceLayer(client=client) @idempotent(persistence_store=persistence_layer) def lambda_handler(event: dict, context: LambdaContext): print("expensive operation") return { "payment_id": 12345, "message": "success", "statusCode": 200, } ``` """# Initialize Cache client with cache config if no client is passed inifclientisNone:self.client=RedisConnection(host=host,port=port,username=username,password=password,db_index=db_index,url=url,mode=mode,ssl=ssl,)._init_client()else:self.client=clientself.in_progress_expiry_attr=in_progress_expiry_attrself.expiry_attr=expiry_attrself.status_attr=status_attrself.data_attr=data_attrself.validation_key_attr=validation_key_attrself._json_serializer=json.dumpsself._json_deserializer=json.loadssuper().__init__()self._orphan_lock_timeout=min(10,self.expires_after_seconds)

Protocol class defining the interface for a Cache client.

This protocol outlines the expected behavior of a Cache client, allowing for
standardization among different implementations and allowing customers to extend it
in their own implementation.

METHOD

DESCRIPTION

- get

Retrieves the value associated with the given key.

- set

) -> bool | None:

Sets the value for the specified key with optional parameters.

- delete

Deletes one or more keys.

Note

The ex parameter represents the expiration time in seconds.

The px parameter represents the expiration time in milliseconds.

The nx parameter, if True, sets the value only if the key does not exist.

RAISES

DESCRIPTION

- NotImplementedError: If any of the methods are not implemented by the concrete class.