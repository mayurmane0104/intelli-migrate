# Feature flags - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/feature_flags/feature_flags](https://docs.aws.amazon.com/powertools/python/latest/api_doc/feature_flags/feature_flags)

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

def__init__(self,store:StoreProvider,logger:logging.Logger|Logger|None=None):"""Evaluates whether feature flags should be enabled based on a given context. It uses the provided store to fetch feature flag rules before evaluating them. Examples -------- ```python from aws_lambda_powertools.utilities.feature_flags import FeatureFlags, AppConfigStore app_config = AppConfigStore( environment="test", application="powertools", name="test_conf_name", max_age=300, envelope="features" ) feature_flags: FeatureFlags = FeatureFlags(store=app_config) ``` Parameters ---------- store: StoreProvider Store to use to fetch feature flag schema configuration. logger: A logging object Used to log messages. If None is supplied, one will be created. """self.store=storeself.logger=loggerorlogging.getLogger(__name__)self._exception_handlers:dict[Exception,Callable]={}

default value if feature flag doesn't exist in the schema,
or there has been an error when fetching the configuration from the store
Can be boolean or any JSON values for non-boolean features.

TYPE:JSONType

Example

1 2 3 4 5 6 7 8 9101112131415161718

fromaws_lambda_powertools.utilities.feature_flagsimportAppConfigStore,FeatureFlagsfromaws_lambda_powertools.utilities.typingimportLambdaContextapp_config=AppConfigStore(environment="dev",application="product-catalogue",name="features")feature_flags=FeatureFlags(store=app_config)deflambda_handler(event:dict,context:LambdaContext):# Get customer's tier from incoming requestctx={"tier":event.get("tier","standard")}# Evaluate whether customer's tier has access to premium features# based on `has_premium_features` ruleshas_premium_features:bool=feature_flags.evaluate(name="premium_features",context=ctx,default=False)ifhas_premium_features:# enable premium features...

RETURNS

DESCRIPTION

JSONType

whether feature should be enabled (bool flags) or JSON value when non-bool feature matches

RAISES

DESCRIPTION

SchemaValidationError

When schema doesn't conform with feature flag schema

Source code in aws_lambda_powertools/utilities/feature_flags/feature_flags.py

defevaluate(self,*,name:str,context:dict[str,Any]|None=None,default:JSONType)->JSONType:"""Evaluate whether a feature flag should be enabled according to stored schema and input context **Logic when evaluating a feature flag** 1. Feature exists and a rule matches, returns when_match value 2. Feature exists but has either no rules or no match, return feature default value 3. Feature doesn't exist in stored schema, encountered an error when fetching -> return default value provided ┌────────────────────────┐ ┌────────────────────────┐ ┌────────────────────────┐ │ Feature flags │──────▶ Get Configuration ├───────▶ Evaluate rules │ └────────────────────────┘ │ │ │ │ │┌──────────────────────┐│ │┌──────────────────────┐│ ││ Fetch schema ││ ││ Match rule ││ │└───────────┬──────────┘│ │└───────────┬──────────┘│ │ │ │ │ │ │ │┌───────────▼──────────┐│ │┌───────────▼──────────┐│ ││ Cache schema ││ ││ Match condition ││ │└───────────┬──────────┘│ │└───────────┬──────────┘│ │ │ │ │ │ │ │┌───────────▼──────────┐│ │┌───────────▼──────────┐│ ││ Validate schema ││ ││ Match action ││ │└──────────────────────┘│ │└──────────────────────┘│ └────────────────────────┘ └────────────────────────┘ Parameters ---------- name: str feature name to evaluate context: dict[str, Any] | None Attributes that should be evaluated against the stored schema. for example: `{"tenant_id": "X", "username": "Y", "region": "Z"}` default: JSONType default value if feature flag doesn't exist in the schema, or there has been an error when fetching the configuration from the store Can be boolean or any JSON values for non-boolean features. Example -------- ```python from aws_lambda_powertools.utilities.feature_flags import AppConfigStore, FeatureFlags from aws_lambda_powertools.utilities.typing import LambdaContext app_config = AppConfigStore(environment="dev", application="product-catalogue", name="features") feature_flags = FeatureFlags(store=app_config) def lambda_handler(event: dict, context: LambdaContext): # Get customer's tier from incoming request ctx = {"tier": event.get("tier", "standard")} # Evaluate whether customer's tier has access to premium features # based on `has_premium_features` rules has_premium_features: bool = feature_flags.evaluate(name="premium_features", context=ctx, default=False) if has_premium_features: # enable premium features ... ``` Returns ------ JSONType whether feature should be enabled (bool flags) or JSON value when non-bool feature matches Raises ------ SchemaValidationError When schema doesn't conform with feature flag schema """ifcontextisNone:context={}try:features=self.get_configuration()exceptConfigurationStoreErroraserr:self.logger.debug(f"Failed to fetch feature flags from store, returning default provided, reason={err}")returndefaultfeature=features.get(name)iffeatureisNone:self.logger.debug(f"Feature not found; returning default provided, name={name}, default={default}")returndefaultrules=feature.get(schema.RULES_KEY)feat_default=feature.get(schema.FEATURE_DEFAULT_VAL_KEY)# Maintenance: Revisit before going GA. We might to simplify customers on-boarding by not requiring it# for non-boolean flags. It'll need minor implementation changes, docs changes, and maybe refactor# get_enabled_features. We can minimize breaking change, despite Beta label, by having a new# method `get_matching_features` returning dict[feature_name, feature_value]boolean_feature=feature.get(schema.FEATURE_DEFAULT_VAL_TYPE_KEY,True,)# backwards compatibility, assume feature flagifnotrules:self.logger.debug(f"no rules found, returning feature default, name={name}, default={str(feat_default)}, boolean_feature={boolean_feature}",# noqa: E501)# Maintenance: Revisit before going GA. We might to simplify customers on-boarding by not requiring it# for non-boolean flags.returnbool(feat_default)ifboolean_featureelsefeat_defaultself.logger.debug(f"looking for rule match, name={name}, default={str(feat_default)}, boolean_feature={boolean_feature}",# noqa: E501)returnself._evaluate_rules(feature_name=name,context=context,feat_default=feat_default,rules=rules,boolean_feature=boolean_feature,)

defget_configuration(self)->dict:"""Get validated feature flag schema from configured store. Largely used to aid testing, since it's called by `evaluate` and `get_enabled_features` methods. Raises ------ ConfigurationStoreError Any propagated error from store SchemaValidationError When schema doesn't conform with feature flag schema Returns ------ dict[str, dict] parsed JSON dictionary Example ------- ```python { "premium_features": { "default": False, "rules": { "customer tier equals premium": { "when_match": True, "conditions": [ { "action": "EQUALS", "key": "tier", "value": "premium", } ], } }, }, "feature_two": { "default": False } } ``` """# parse result conf as JSON, keep in cache for max age defined in storeself.logger.debug(f"Fetching schema from registered store, store={self.store}")config:dict=self.store.get_configuration()validator=schema.SchemaValidator(schema=config,logger=self.logger)validator.validate()returnconfig

defget_enabled_features(self,*,context:dict[str,Any]|None=None)->list[str]:"""Get all enabled feature flags while also taking into account context (when a feature has defined rules) Parameters ---------- context: dict[str, Any] | None dict of attributes that you would like to match the rules against, can be `{'tenant_id: 'X', 'username':' 'Y', 'region': 'Z'}` etc. Returns ---------- list[str] list of all feature names that either matches context or have True as default Example ------- ```python ["premium_features", "my_feature_two", "always_true_feature"] ``` Raises ------ SchemaValidationError When schema doesn't conform with feature flag schema """ifcontextisNone:context={}features_enabled:list[str]=[]try:features:dict[str,Any]=self.get_configuration()exceptConfigurationStoreErroraserr:self.logger.debug(f"Failed to fetch feature flags from store, returning empty list, reason={err}")returnfeatures_enabledself.logger.debug("Evaluating all features")forname,featureinfeatures.items():rules=feature.get(schema.RULES_KEY,{})feature_default_value=feature.get(schema.FEATURE_DEFAULT_VAL_KEY)boolean_feature=feature.get(schema.FEATURE_DEFAULT_VAL_TYPE_KEY,True,)# backwards compatibility, assume feature flagiffeature_default_valueandnotrules:self.logger.debug(f"feature is enabled by default and has no defined rules, name={name}")features_enabled.append(name)elifself._evaluate_rules(feature_name=name,context=context,feat_default=feature_default_value,rules=rules,boolean_feature=boolean_feature,):self.logger.debug(f"feature's calculated value is True, name={name}")features_enabled.append(name)returnfeatures_enabled

Registers function to handle unexpected validation exceptions when evaluating flags.

It does not override the function of a default flag value in case of network and IAM permissions.
For example, you won't be able to catch ConfigurationStoreError exception.

feature_flags=FeatureFlags(store=app_config)@feature_flags.validation_exception_handler(Exception)# any exceptiondefcatch_exception(exc):raiseTypeError("re-raised")fromexc

Source code in aws_lambda_powertools/utilities/feature_flags/feature_flags.py

defvalidation_exception_handler(self,exc_class:Exception|list[Exception]):"""Registers function to handle unexpected validation exceptions when evaluating flags. It does not override the function of a default flag value in case of network and IAM permissions. For example, you won't be able to catch ConfigurationStoreError exception. Parameters ---------- exc_class : Exception | list[Exception] One or more exceptions to catch Example ------- ```python feature_flags = FeatureFlags(store=app_config) @feature_flags.validation_exception_handler(Exception) # any exception def catch_exception(exc): raise TypeError("re-raised") from exc ``` """defregister_exception_handler(func:Callable[P,T])->Callable[P,T]:ifisinstance(exc_class,list):forexpinexc_class:self._exception_handlers[exp]=funcelse:self._exception_handlers[exc_class]=funcreturnfuncreturnregister_exception_handler