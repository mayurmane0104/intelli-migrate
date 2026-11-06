# AppConfig - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/feature_flags/appconfig](https://docs.aws.amazon.com/powertools/python/latest/api_doc/feature_flags/appconfig)

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

def__init__(self,environment:str,application:str,name:str,max_age:int=5,sdk_config:Config|None=None,envelope:str|None="",jmespath_options:dict|None=None,logger:logging.Logger|Logger|None=None,boto_config:Config|None=None,boto3_session:boto3.session.Session|None=None,boto3_client:AppConfigDataClient|None=None,):"""This class fetches JSON schemas from AWS AppConfig Parameters ---------- environment: str Appconfig environment, e.g. 'dev/test' etc. application: str AppConfig application name, e.g. 'powertools' name: str AppConfig configuration name e.g. `my_conf` max_age: int cache expiration time in seconds, or how often to call AppConfig to fetch latest configuration sdk_config: Config | None Botocore Config object to pass during client initialization envelope : str | None JMESPath expression to pluck feature flags data from config jmespath_options : dict | None Alternative JMESPath options to be included when filtering expr logger: A logging object Used to log messages. If None is supplied, one will be created. boto_config: botocore.config.Config, optional Botocore configuration to pass during client initialization boto3_session : boto3.Session, optional Boto3 session to use for AWS API communication boto3_client : AppConfigDataClient, optional Boto3 AppConfigDataClient Client to use, boto3_session and boto_config will be ignored if both are provided """super().__init__()self.logger=loggerorlogging.getLogger(__name__)self.environment=environmentself.application=applicationself.name=nameself.cache_seconds=max_ageself.config=sdk_configorboto_configself.envelope=envelopeself.jmespath_options=jmespath_optionsself._conf_store=AppConfigProvider(environment=environment,application=application,config=sdk_configorboto_config,boto3_client=boto3_client,boto3_session=boto3_session,)# Override the user agent to use "feature_flags" instead of "parameters"self._register_feature_flags_user_agent()

Fetch feature schema configuration from AWS AppConfig

If envelope is set, it'll extract and return feature flags from configuration,
otherwise it'll return the entire configuration fetched from AWS AppConfig.

defget_configuration(self)->dict[str,Any]:"""Fetch feature schema configuration from AWS AppConfig If envelope is set, it'll extract and return feature flags from configuration, otherwise it'll return the entire configuration fetched from AWS AppConfig. Raises ------ ConfigurationStoreError Any validation error or AppConfig error that can occur Returns ------- dict[str, Any] parsed JSON dictionary """config=self.get_raw_configurationifself.envelope:self.logger.debug("Envelope enabled; extracting data from config",extra={"envelope":self.envelope})config=jmespath_utils.query(data=config,envelope=self.envelope,jmespath_options=self.jmespath_options,)returnconfig