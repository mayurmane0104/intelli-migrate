# Provider - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api_doc/data_masking/provider](https://docs.aws.amazon.com/powertools/python/latest/api_doc/data_masking/provider)

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

fromaws_lambda_powertools.utilities._data_masking.providerimportBaseProviderfromaws_lambda_powertools.utilities.data_maskingimportDataMaskingclassMyCustomProvider(BaseProvider):defencrypt(self,data)->str:# Implementation logic for data encryptiondefdecrypt(self,data)->Any:# Implementation logic for data decryptiondeferase(self,data)->Any|Iterable:# Implementation logic for data maskingpassdeflambda_handler(event,context):provider=MyCustomProvider(["secret-key"])data_masker=DataMasking(provider=provider)data={"project":"powertools","sensitive":"password"}encrypted=data_masker.encrypt(data)returnencrypted

Abstract method for decrypting data. Subclasses must implement this method.

Source code in aws_lambda_powertools/utilities/data_masking/provider/base.py

6970717273

defdecrypt(self,data,provider_options:dict|None=None,**encryption_context:str)->Any:""" Abstract method for decrypting data. Subclasses must implement this method. """raiseNotImplementedError("Subclasses must implement decrypt()")

Abstract method for encrypting data. Subclasses must implement this method.

Source code in aws_lambda_powertools/utilities/data_masking/provider/base.py

6364656667

defencrypt(self,data,provider_options:dict|None=None,**encryption_context:str)->str:""" Abstract method for encrypting data. Subclasses must implement this method. """raiseNotImplementedError("Subclasses must implement encrypt()")

fromaws_lambda_powertools.utilities._data_masking.providerimportBaseProviderfromaws_lambda_powertools.utilities.data_maskingimportDataMaskingclassMyCustomProvider(BaseProvider):defencrypt(self,data)->str:# Implementation logic for data encryptiondefdecrypt(self,data)->Any:# Implementation logic for data decryptiondeferase(self,data)->Any|Iterable:# Implementation logic for data maskingpassdeflambda_handler(event,context):provider=MyCustomProvider(["secret-key"])data_masker=DataMasking(provider=provider)data={"project":"powertools","sensitive":"password"}encrypted=data_masker.encrypt(data)returnencrypted

Abstract method for decrypting data. Subclasses must implement this method.

Source code in aws_lambda_powertools/utilities/data_masking/provider/base.py

6970717273

defdecrypt(self,data,provider_options:dict|None=None,**encryption_context:str)->Any:""" Abstract method for decrypting data. Subclasses must implement this method. """raiseNotImplementedError("Subclasses must implement decrypt()")

Abstract method for encrypting data. Subclasses must implement this method.

Source code in aws_lambda_powertools/utilities/data_masking/provider/base.py

6364656667

defencrypt(self,data,provider_options:dict|None=None,**encryption_context:str)->str:""" Abstract method for encrypting data. Subclasses must implement this method. """raiseNotImplementedError("Subclasses must implement encrypt()")

The KMSKeyProvider is responsible for assembling an AWS Key Management Service (KMS)
client, a caching mechanism, and a keyring for secure key management and data encryption.

defdecrypt(self,data:str,provider_options:dict|None=None,**encryption_context:str)->Any:""" Decrypt data using AWSEncryptionSDKProvider. Parameters ------- data: str The encrypted data, as a base64-encoded string provider_options Additional options for the aws_encryption_sdk.EncryptionSDKClient Returns ------- ciphertext: bytes The decrypted data in bytes """provider_options=provider_optionsor{}self._validate_encryption_context(encryption_context)try:ciphertext_decoded=base64_decode(data)exceptError:raiseDataMaskingDecryptValueError("Data decryption failed. Please ensure that you are attempting to decrypt data that was previously encrypted.",# noqa E501)try:ciphertext,decryptor_header=self.client.decrypt(source=ciphertext_decoded,key_provider=self.key_provider,**provider_options,)exceptDecryptKeyError:raiseDataMaskingDecryptKeyError("Failed to decrypt data - Please ensure you are using a valid Symmetric AWS KMS Key ARN, not KMS Key ID or alias.",# noqa E501)except(TypeError,NotSupportedError):raiseDataMaskingDecryptValueError("Data decryption failed. Please ensure that you are attempting to decrypt data that was previously encrypted.",# noqa E501)self._compare_encryption_context(decryptor_header.encryption_context,encryption_context)decoded_ciphertext=bytes_to_string(ciphertext)returnself.json_deserializer(decoded_ciphertext)

defencrypt(self,data:Any,provider_options:dict|None=None,**encryption_context:str)->str:""" Encrypt data using the AWSEncryptionSDKProvider. Parameters ------- data: Any The data to be encrypted. provider_options: dict Additional options for the aws_encryption_sdk.EncryptionSDKClient **encryption_context: str Additional keyword arguments collected into a dictionary. Returns ------- ciphertext: str The encrypted data, as a base64-encoded string. """provider_options=provider_optionsor{}self._validate_encryption_context(encryption_context)data_encoded=self.json_serializer(data).encode("utf-8")try:ciphertext,_=self.client.encrypt(source=data_encoded,materials_manager=self.cache_cmm,encryption_context=encryption_context,**provider_options,)exceptGenerateKeyError:raiseDataMaskingEncryptKeyError("Failed to encrypt data. Please ensure you are using a valid Symmetric AWS KMS Key ARN, not KMS Key ID or alias.",# noqa E501)returnbytes_to_base64_string(ciphertext)