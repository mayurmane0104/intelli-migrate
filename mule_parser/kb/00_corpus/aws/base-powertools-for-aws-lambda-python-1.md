# Base - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/data_masking/base](https://docs.aws.amazon.com/powertools/python/latest/api_doc/data_masking/base)

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

Source code in aws_lambda_powertools/utilities/data_masking/base.py

102103104105106107108109110111

def__init__(self,provider:BaseProvider|None=None,raise_on_missing_field:bool=True,):self.provider=providerorBaseProvider()# NOTE: we depend on Provider to not confuse customers in passing the same 2 serializers in 2 placesself.json_serializer=self.provider.json_serializerself.json_deserializer=self.provider.json_deserializerself.raise_on_missing_field=raise_on_missing_field

defdecrypt(self,data,provider_options:dict|None=None,**encryption_context:str,)->Any:""" Decrypt data using the configured encryption provider. Parameters ---------- data : dict, Mapping, Sequence, or Number The data to encrypt. provider_options : dict, optional Provider-specific options for encryption. **encryption_context : str Additional key-value pairs for encryption context. Returns ------- str The encrypted data as a base64-encoded string. Example -------- encryption_provider = AWSEncryptionSDKProvider(keys=[KMS_KEY_ARN]) data_masker = DataMasking(provider=encryption_provider) encrypted = data_masker.decrypt(encrypted_data) """data=prepare_data(data)returnself._apply_action(data=data,fields=None,action=self.provider.decrypt,provider_options=provider_optionsor{},dynamic_mask=None,custom_mask=None,regex_pattern=None,mask_format=None,**encryption_context,)

defencrypt(self,data:dict|Mapping|Sequence|Number,provider_options:dict|None=None,**encryption_context:str,)->str:""" Encrypt data using the configured encryption provider. Parameters ---------- data : dict, Mapping, Sequence, or Number The data to encrypt. provider_options : dict, optional Provider-specific options for encryption. **encryption_context : str Additional key-value pairs for encryption context. Returns ------- str The encrypted data as a base64-encoded string. Example -------- encryption_provider = AWSEncryptionSDKProvider(keys=[KMS_KEY_ARN]) data_masker = DataMasking(provider=encryption_provider) encrypted = data_masker.encrypt({"secret": "value"}) """data=prepare_data(data)returnself._apply_action(data=data,fields=None,action=self.provider.encrypt,provider_options=provider_optionsor{},dynamic_mask=None,custom_mask=None,regex_pattern=None,mask_format=None,**encryption_context,)

deferase(self,data:Any,fields:list[str]|None=None,*,dynamic_mask:bool|None=None,custom_mask:str|None=None,regex_pattern:str|None=None,mask_format:str|None=None,masking_rules:dict|None=None,)->Any:""" Erase or mask sensitive data in the input. Parameters ---------- data : Any The data to be erased or masked. fields : list of str, optional List of field names to be erased or masked. dynamic_mask : bool, optional Whether to use dynamic masking. custom_mask : str, optional Custom mask to apply instead of the default. regex_pattern : str, optional Regular expression pattern for identifying data to mask. mask_format : str, optional Format string for the mask. masking_rules : dict, optional Dictionary of custom masking rules. Returns ------- Any The data with sensitive information erased or masked. """data=prepare_data(data)ifmasking_rules:returnself._apply_masking_rules(data=data,masking_rules=masking_rules)else:returnself._apply_action(data=data,fields=fields,action=self.provider.erase,dynamic_mask=dynamic_mask,custom_mask=custom_mask,regex_pattern=regex_pattern,mask_format=mask_format,)