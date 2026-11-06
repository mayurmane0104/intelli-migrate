# Feature flags - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/utilities/feature_flags](https://docs.aws.amazon.com/powertools/python/latest/utilities/feature_flags)

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

AWS AppConfig requires two API calls to fetch configuration for the first time. You can improve latency by consolidating your feature settings in a single Configuration.

When using the default store AppConfigStore, your Lambda function IAM Role must have appconfig:GetLatestConfiguration and appconfig:StartConfigurationSession IAM permissions before using this feature.

To get started, you'd need to initialize AppConfigStore and FeatureFlags. Then call FeatureFlagsevaluate method to fetch, validate, and evaluate your feature.

The evaluate method supports two optional parameters:

context: Value to be evaluated against each rule defined for the given feature

default: Sentinel value to use in case we experience any issues with our store, or feature doesn't exist

fromtypingimportAnyfromaws_lambda_powertools.utilities.feature_flagsimportAppConfigStore,FeatureFlagsfromaws_lambda_powertools.utilities.typingimportLambdaContextapp_config=AppConfigStore(environment="dev",application="product-catalogue",name="features")feature_flags=FeatureFlags(store=app_config)deflambda_handler(event:dict,context:LambdaContext):""" This feature flag is enabled under the following conditions: - The request payload contains a field 'tier' with the value 'premium'. Rule condition to be evaluated: "conditions": [ { "action": "EQUALS", "key": "tier", "value": "premium" } ] """# Get customer's tier from incoming requestctx={"tier":event.get("tier","standard")}# Evaluate whether customer's tier has access to premium features# based on `has_premium_features` ruleshas_premium_features:Any=feature_flags.evaluate(name="premium_features",context=ctx,default=False)ifhas_premium_features:# enable premium features...

We have a static flag named ten_percent_off_campaign. Meaning, there are no conditional rules, it's either ON or OFF for all customers.

In this case, we could omit the context parameter and simply evaluate whether we should apply the 10% discount.

1 2 3 4 5 6 7 8 9101112131415161718192021222324

fromtypingimportAnyfromaws_lambda_powertools.utilities.feature_flagsimportAppConfigStore,FeatureFlagsfromaws_lambda_powertools.utilities.typingimportLambdaContextapp_config=AppConfigStore(environment="dev",application="product-catalogue",name="features")feature_flags=FeatureFlags(store=app_config)deflambda_handler(event:dict,context:LambdaContext):""" This feature flag is enabled by default for all requests. """apply_discount:Any=feature_flags.evaluate(name="ten_percent_off_campaign",default=False)price:Any=event.get("price")ifapply_discount:# apply 10% discount to productprice=price*0.9return{"price":price}

from__future__importannotationsfromaws_lambda_powertools.event_handlerimportAPIGatewayRestResolverfromaws_lambda_powertools.utilities.feature_flagsimportAppConfigStore,FeatureFlagsfromaws_lambda_powertools.utilities.typingimportLambdaContextapp=APIGatewayRestResolver()app_config=AppConfigStore(environment="dev",application="product-catalogue",name="features")feature_flags=FeatureFlags(store=app_config)@app.get("/products")deflist_products():# getting fields from request# https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/api_gateway/#accessing-request-detailsjson_body=app.current_event.json_bodyheaders=app.current_event.headersctx={**headers,**json_body}# getting price from payloadprice:float=float(json_body.get("price"))percent_discount:int=0# all_features is evaluated to ["premium_features", "geo_customer_campaign", "ten_percent_off_campaign"]all_features:list[str]=feature_flags.get_enabled_features(context=ctx)if"geo_customer_campaign"inall_features:# apply 20% discounts for customers in NLpercent_discount+=20if"ten_percent_off_campaign"inall_features:# apply additional 10% for all customerspercent_discount+=10price=price*(100-percent_discount)/100return{"price":price}deflambda_handler(event:dict,context:LambdaContext):returnapp.resolve(event,context)

Feature flags can also return enabled features based on time or datetime ranges.
This allows you to have features that are only enabled on certain days of the week, certain time
intervals or between certain calendar dates.

Use cases:

Enable maintenance mode during a weekend

Disable support/chat feature after working hours

Launch a new feature on a specific date and time

You can also have features enabled only at certain times of the day for premium tier customers

fromaws_lambda_powertools.utilities.feature_flagsimportAppConfigStore,FeatureFlagsfromaws_lambda_powertools.utilities.typingimportLambdaContextapp_config=AppConfigStore(environment="dev",application="product-catalogue",name="features")feature_flags=FeatureFlags(store=app_config)deflambda_handler(event:dict,context:LambdaContext):""" This feature flag is enabled under the following conditions: - The request payload contains a field 'tier' with the value 'premium'. - If the current day is either Saturday or Sunday in America/New_York timezone. Rule condition to be evaluated: "conditions": [ { "action": "EQUALS", "key": "tier", "value": "premium" }, { "action": "SCHEDULE_BETWEEN_DAYS_OF_WEEK", "key": "CURRENT_DAY_OF_WEEK", "value": { "DAYS": [ "SATURDAY", "SUNDAY" ], "TIMEZONE": "America/New_York" } } ] """# Get customer's tier from incoming requestctx={"tier":event.get("tier","standard")}# Checking if the weekend premum discount is enableweekend_premium_discount=feature_flags.evaluate(name="weekend_premium_discount",default=False,context=ctx)ifweekend_premium_discount:# Enable special discount on weekend for premium users:return{"message":"The weekend premium discount is enabled."}return{"message":"The weekend premium discount is not enabled."}

{"weekend_premium_discount":{"default":false,"rules":{"customer tier equals premium and its time for a discount":{"when_match":true,"conditions":[{"action":"EQUALS","key":"tier","value":"premium"},{"action":"SCHEDULE_BETWEEN_DAYS_OF_WEEK","key":"CURRENT_DAY_OF_WEEK","value":{"DAYS":["SATURDAY","SUNDAY"],"TIMEZONE":"America/New_York"}}]}}}}

You can also have features enabled only at certain times of the day.

fromaws_lambda_powertools.utilities.feature_flagsimportAppConfigStore,FeatureFlagsfromaws_lambda_powertools.utilities.typingimportLambdaContextapp_config=AppConfigStore(environment="dev",application="product-catalogue",name="features")feature_flags=FeatureFlags(store=app_config)deflambda_handler(event:dict,context:LambdaContext):""" This feature flag is enabled under the following conditions: - Every day between 17:00 to 19:00 in Europe/Copenhagen timezone Rule condition to be evaluated: "conditions": [ { "action": "SCHEDULE_BETWEEN_TIME_RANGE", "key": "CURRENT_TIME", "value": { "START": "17:00", "END": "19:00", "TIMEZONE": "Europe/Copenhagen" } } ] """# Checking if the happy hour discount is enableis_happy_hour=feature_flags.evaluate(name="happy_hour",default=False)ifis_happy_hour:# Enable special discount on happy hour:return{"message":"The happy hour discount is enabled."}return{"message":"The happy hour discount is not enabled."}

fromaws_lambda_powertools.utilities.feature_flagsimportAppConfigStore,FeatureFlagsfromaws_lambda_powertools.utilities.typingimportLambdaContextapp_config=AppConfigStore(environment="dev",application="product-catalogue",name="features")feature_flags=FeatureFlags(store=app_config)deflambda_handler(event:dict,context:LambdaContext):""" This feature flag is enabled under the following conditions: - Start date: December 25th, 2022 at 12:00:00 PM EST - End date: December 31st, 2022 at 11:59:59 PM EST - Timezone: America/New_York Rule condition to be evaluated: "conditions": [ { "action": "SCHEDULE_BETWEEN_DATETIME_RANGE", "key": "CURRENT_DATETIME", "value": { "START": "2022-12-25T12:00:00", "END": "2022-12-31T23:59:59", "TIMEZONE": "America/New_York" } } ] """# Checking if the Christmas discount is enablexmas_discount=feature_flags.evaluate(name="christmas_discount",default=False)ifxmas_discount:# Enable special discount on christmas:return{"message":"The Christmas discount is enabled."}return{"message":"The Christmas discount is not enabled."}

1 2 3 4 5 6 7 8 9101112131415161718192021

{"christmas_discount":{"default":false,"rules":{"enable discount during christmas":{"when_match":true,"conditions":[{"action":"SCHEDULE_BETWEEN_DATETIME_RANGE","key":"CURRENT_DATETIME","value":{"START":"2022-12-25T12:00:00","END":"2022-12-31T23:59:59","TIMEZONE":"America/New_York"}}]}}}}

How should I use timezones?

You can use any IANA time zone (as originally specified
in PEP 615) as part of your rules definition.
Powertools for AWS Lambda (Python) takes care of converting and calculate the correct timestamps for you.

When using SCHEDULE_BETWEEN_DATETIME_RANGE, use timestamps without timezone information, and
specify the timezone manually. This way, you'll avoid hitting problems with day light savings.

Feature flags can also be used to run experiments on a segment of users based on modulo range conditions on context variables.
This allows you to have features that are only enabled for a certain segment of users, comparing across multiple variants
of the same experiment.

Use cases:

Enable an experiment for a percentage of users

Scale up an experiment incrementally in production - canary release

Run multiple experiments or variants simultaneously by assigning a spectrum segment to each experiment variant.

The modulo range condition takes three values - BASE, START and END.

The condition evaluates START <= CONTEXT_VALUE % BASE <= END.

fromaws_lambda_powertools.utilities.feature_flagsimportAppConfigStore,FeatureFlagsfromaws_lambda_powertools.utilities.typingimportLambdaContextapp_config=AppConfigStore(environment="dev",application="product-catalogue",name="features")feature_flags=FeatureFlags(store=app_config)deflambda_handler(event:dict,context:LambdaContext):""" This feature flag is enabled under the following conditions: - The request payload contains a field 'tier' with the value 'standard'. - If the user_id belongs to the spectrum 0-19 modulo 100, (20% users) on whom we want to run the sale experiment. Rule condition to be evaluated: "conditions": [ { "action": "EQUALS", "key": "tier", "value": "standard" }, { "action": "MODULO_RANGE", "key": "user_id", "value": { "BASE": 100, "START": 0, "END": 19 } } ] """# Get customer's tier and identifier from incoming requestctx={"tier":event.get("tier","standard"),"user_id":event.get("user_id",0)}# Checking if the sale_experiment is enablesale_experiment=feature_flags.evaluate(name="sale_experiment",default=False,context=ctx)ifsale_experiment:# Enable special discount for sale experiment segment users:return{"message":"The sale experiment is enabled."}return{"message":"The sale experiment is not enabled."}

You might have a list of features to unlock for premium customers, unlock a specific set of features for admin users, etc.

Feature flags can return any JSON values when boolean_type parameter is set to false. These can be dictionaries, list, string, integers, etc.

1 2 3 4 5 6 7 8 9101112131415161718

fromtypingimportAnyfromaws_lambda_powertools.utilities.feature_flagsimportAppConfigStore,FeatureFlagsfromaws_lambda_powertools.utilities.typingimportLambdaContextapp_config=AppConfigStore(environment="dev",application="comments",name="config")feature_flags=FeatureFlags(store=app_config)deflambda_handler(event:dict,context:LambdaContext):# Get customer's tier from incoming requestctx={"tier":event.get("tier","standard")}# Evaluate `has_premium_features` based on customer's tierpremium_features:Any=feature_flags.evaluate(name="premium_features",context=ctx,default=[])return{"Premium features enabled":premium_features}

By default, we cache configuration retrieved from the Store for 5 seconds for performance and reliability reasons.

You can override max_age parameter when instantiating the store.

1 2 3 4 5 6 7 8 9101112131415161718192021222324

fromtypingimportAnyfromaws_lambda_powertools.utilities.feature_flagsimportAppConfigStore,FeatureFlagsfromaws_lambda_powertools.utilities.typingimportLambdaContextapp_config=AppConfigStore(environment="dev",application="product-catalogue",name="features",max_age=300)feature_flags=FeatureFlags(store=app_config)deflambda_handler(event:dict,context:LambdaContext):""" This feature flag is enabled by default for all requests. """apply_discount:Any=feature_flags.evaluate(name="ten_percent_off_campaign",default=False)price:Any=event.get("price")ifapply_discount:# apply 10% discount to productprice=price*0.9return{"price":price}

If you need more control and want to provide context such as user group, permissions, location, etc., you need to add rules to your feature flag configuration.

You can have multiple rules with different names. The rule engine will return the first result when_match of the matching rule configuration, or default value when none of the rules apply.

The action configuration can have the following values, where the expressions a is the key and b is the value above:

Action

Equivalent expression

EQUALS

lambda a, b: a == b

NOT_EQUALS

lambda a, b: a != b

KEY_GREATER_THAN_VALUE

lambda a, b: a > b

KEY_GREATER_THAN_OR_EQUAL_VALUE

lambda a, b: a >= b

KEY_LESS_THAN_VALUE

lambda a, b: a < b

KEY_LESS_THAN_OR_EQUAL_VALUE

lambda a, b: a <= b

STARTSWITH

lambda a, b: a.startswith(b)

ENDSWITH

lambda a, b: a.endswith(b)

KEY_IN_VALUE

lambda a, b: a in b

KEY_NOT_IN_VALUE

lambda a, b: a not in b

ANY_IN_VALUE

lambda a, b: any of a is in b

ALL_IN_VALUE

lambda a, b: all of a is in b

NONE_IN_VALUE

lambda a, b: none of a is in b

VALUE_IN_KEY

lambda a, b: b in a

VALUE_NOT_IN_KEY

lambda a, b: b not in a

SCHEDULE_BETWEEN_TIME_RANGE

lambda a, b: b.start <= time(a) <= b.end

SCHEDULE_BETWEEN_DATETIME_RANGE

lambda a, b: b.start <= datetime(a) <= b.end

SCHEDULE_BETWEEN_DAYS_OF_WEEK

lambda a, b: day_of_week(a) in b

MODULO_RANGE

lambda a, b: b.start <= a % b.base <= b.end

Info

The key and value will be compared to the input from the context parameter.

Time based keys

For time based keys, we provide a list of predefined keys. These will automatically get converted to the corresponding timestamp on each invocation of your Lambda function.

fromtypingimportAnyfrombotocore.configimportConfigfromjmespath.functionsimportFunctions,signaturefromaws_lambda_powertools.utilities.feature_flagsimportAppConfigStore,FeatureFlagsfromaws_lambda_powertools.utilities.typingimportLambdaContextboto_config=Config(read_timeout=10,retries={"total_max_attempts":2})# Custom JMESPath functionsclassCustomFunctions(Functions):@signature({"types":["object"]})def_func_special_decoder(self,features):# You can add some logic herereturnfeaturescustom_jmespath_options={"custom_functions":CustomFunctions()}app_config=AppConfigStore(environment="dev",application="product-catalogue",name="features",max_age=120,envelope="special_decoder(features)",# using a custom function defined in CustomFunctions Classboto_config=boto_config,jmespath_options=custom_jmespath_options,)feature_flags=FeatureFlags(store=app_config)deflambda_handler(event:dict,context:LambdaContext):apply_discount:Any=feature_flags.evaluate(name="ten_percent_off_campaign",default=False)price:Any=event.get("price")ifapply_discount:# apply 10% discount to productprice=price*0.9return{"price":price}

The boto_config , boto3_session, and boto3_client parameters enable you to pass in a custom botocore config object, boto3 session, or a boto3 client when constructing the AppConfig store provider.

You can create your own custom FeatureFlags store provider by inheriting the StoreProvider class, and implementing both get_raw_configuration() and get_configuration() methods to retrieve the configuration from your custom store.

get_raw_configuration() – get the raw configuration from the store provider and return the parsed JSON dictionary

get_configuration() – get the configuration from the store provider, parsing it as a JSON dictionary. If an envelope is set, extract the envelope data

Here are an example of implementing a custom store provider using Amazon S3, a popular object storage.

Note

This is just one example of how you can create your own store provider. Before creating a custom store provider, carefully evaluate your requirements and consider factors such as performance, scalability, and ease of maintenance.

1 2 3 4 5 6 7 8 910111213141516171819202122

fromtypingimportAnyfromcustom_s3_store_providerimportS3StoreProviderfromaws_lambda_powertools.utilities.feature_flagsimportFeatureFlagsfromaws_lambda_powertools.utilities.typingimportLambdaContexts3_config_store=S3StoreProvider("your-bucket-name","working_with_own_s3_store_provider_features.json")feature_flags=FeatureFlags(store=s3_config_store)deflambda_handler(event:dict,context:LambdaContext):apply_discount:Any=feature_flags.evaluate(name="ten_percent_off_campaign",default=False)price:Any=event.get("price")ifapply_discount:# apply 10% discount to productprice=price*0.9return{"price":price}

importjsonfromtypingimportAny,Dictimportboto3frombotocore.exceptionsimportClientErrorfromaws_lambda_powertools.utilities.feature_flags.baseimportStoreProviderfromaws_lambda_powertools.utilities.feature_flags.exceptionsimport(ConfigurationStoreError,)classS3StoreProvider(StoreProvider):def__init__(self,bucket_name:str,object_key:str):# Initialize the client to your custom store providersuper().__init__()self.bucket_name=bucket_nameself.object_key=object_keyself.client=boto3.client("s3")def_get_s3_object(self)->Dict[str,Any]:# Retrieve the object contenttry:response=self.client.get_object(Bucket=self.bucket_name,Key=self.object_key)returnjson.loads(response["Body"].read().decode())exceptClientErrorasexc:raiseConfigurationStoreError("Unable to get S3 Store Provider configuration file")fromexcdefget_configuration(self)->Dict[str,Any]:returnself._get_s3_object()@propertydefget_raw_configuration(self)->Dict[str,Any]:returnself._get_s3_object()

fromaws_lambda_powertools.utilities.feature_flagsimport(AppConfigStore,FeatureFlags,RuleAction,)definit_feature_flags(mocker,mock_schema,envelope="")->FeatureFlags:"""Mock AppConfig Store get_configuration method to use mock schema instead"""method_to_mock="aws_lambda_powertools.utilities.feature_flags.AppConfigStore.get_configuration"mocked_get_conf=mocker.patch(method_to_mock)mocked_get_conf.return_value=mock_schemaapp_conf_store=AppConfigStore(environment="test_env",application="test_app",name="test_conf_name",envelope=envelope,)returnFeatureFlags(store=app_conf_store)deftest_flags_condition_match(mocker):# GIVENexpected_value=Truemocked_app_config_schema={"my_feature":{"default":False,"rules":{"tenant id equals 12345":{"when_match":expected_value,"conditions":[{"action":RuleAction.EQUALS.value,"key":"tenant_id","value":"12345",},],},},},}# WHENctx={"tenant_id":"12345","username":"a"}feature_flags=init_feature_flags(mocker=mocker,mock_schema=mocked_app_config_schema)flag=feature_flags.evaluate(name="my_feature",context=ctx,default=False)# THENassertflag==expected_value