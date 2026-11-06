# aws_lambda_powertools.shared.user_agent API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/shared/user_agent.html](https://docs.aws.amazon.com/powertools/python/latest/api/shared/user_agent.html)

---

# Module `aws_lambda_powertools.shared.user_agent`

## Functions

- 
## Expand source code`def inject_user_agent(): if inject_header: # Some older botocore versions doesn't support register_initializer. In those cases, we disable the feature. if not hasattr(botocore, "register_initializer"): return # Customize botocore session to inject Powertools header # See: https://github.com/boto/botocore/pull/2682 botocore.register_initializer(_initializer_botocore_session)`
- 
## Expand source code`def register_feature_to_botocore_session(botocore_session, feature): """ Register the given feature string to the event system of the provided botocore session Please notice this function is for patching botocore session and is different from previous one which is for patching boto3 session Parameters ---------- botocore_session : botocore.session.Session The botocore session to which the feature will be registered. feature : str The feature string to be appended to the User-Agent header, e.g., "data-masking" in Powertools. Raises ------ AttributeError If the provided session does not have an event system. Examples -------- **register data-masking user-agent to botocore session** >>> from aws_lambda_powertools.shared.user_agent import ( >>> register_feature_to_botocore_session >>> ) >>> >>> session = botocore.session.Session() >>> register_feature_to_botocore_session(botocore_session=session, feature="data-masking") >>> key_provider = StrictAwsKmsMasterKeyProvider(key_ids=self.keys, botocore_session=session) """ try: botocore_session.register(TARGET_SDK_EVENT, _create_feature_function(feature)) except AttributeError as e: logger.debug(f"botocore session passed in doesn't have a event system:{e}")`Register the given feature string to the event system of the provided botocore session Please notice this function is for patching botocore session and is different from previous one which is for patching boto3 session ## Parameters- `botocore_session`- `botocore.session.Session`
- The botocore session to which the feature will be registered.
- `feature`- `str`
- The feature string to be appended to the User-Agent header, e.g., "data-masking" in Powertools.
 ## Raises- `AttributeError`
- If the provided session does not have an event system.
 ## Examples**register data-masking user-agent to botocore session**`>>> from aws_lambda_powertools.shared.user_agent import ( >>> register_feature_to_botocore_session >>> ) >>> >>> session = botocore.session.Session() >>> register_feature_to_botocore_session(botocore_session=session, feature="data-masking") >>> key_provider = StrictAwsKmsMasterKeyProvider(key_ids=self.keys, botocore_session=session)`
- 
## Expand source code`def register_feature_to_client(client, feature): """ Register the given feature string to the event system of the provided boto3 client and append the feature to the User-Agent header of the request Parameters ---------- client : boto3.session.Session.client The boto3 client to which the feature will be registered. feature : str The feature string to be appended to the User-Agent header, e.g., "streaming" in Powertools. Raises ------ AttributeError If the provided client does not have an event system. """ try: client.meta.events.register(TARGET_SDK_EVENT, _create_feature_function(feature)) except AttributeError as e: logger.debug(f"session passed in doesn't have a event system:{e}")`Register the given feature string to the event system of the provided boto3 client and append the feature to the User-Agent header of the request ## Parameters- `client`- `boto3.session.Session.client`
- The boto3 client to which the feature will be registered.
- `feature`- `str`
- The feature string to be appended to the User-Agent header, e.g., "streaming" in Powertools.
 ## Raises- `AttributeError`
- If the provided client does not have an event system.
 
- 
## Expand source code`def register_feature_to_resource(resource, feature): """ Register the given feature string to the event system of the provided boto3 resource and append the feature to the User-Agent header of the request Parameters ---------- resource : boto3.session.Session.resource The boto3 resource to which the feature will be registered. feature : str The feature string to be appended to the User-Agent header, e.g., "streaming" in Powertools. Raises ------ AttributeError If the provided resource does not have an event system. """ try: resource.meta.client.meta.events.register(TARGET_SDK_EVENT, _create_feature_function(feature)) except AttributeError as e: logger.debug(f"resource passed in doesn't have a event system:{e}")`Register the given feature string to the event system of the provided boto3 resource and append the feature to the User-Agent header of the request ## Parameters- `resource`- `boto3.session.Session.resource`
- The boto3 resource to which the feature will be registered.
- `feature`- `str`
- The feature string to be appended to the User-Agent header, e.g., "streaming" in Powertools.
 ## Raises- `AttributeError`
- If the provided resource does not have an event system.
 
- 
## Expand source code`def register_feature_to_session(session, feature): """ Register the given feature string to the event system of the provided boto3 session and append the feature to the User-Agent header of the request Parameters ---------- session : boto3.session.Session The boto3 session to which the feature will be registered. feature : str The feature string to be appended to the User-Agent header, e.g., "streaming" in Powertools. Raises ------ AttributeError If the provided session does not have an event system. """ try: session.events.register(TARGET_SDK_EVENT, _create_feature_function(feature)) except AttributeError as e: logger.debug(f"session passed in doesn't have a event system:{e}")`Register the given feature string to the event system of the provided boto3 session and append the feature to the User-Agent header of the request ## Parameters- `session`- `boto3.session.Session`
- The boto3 session to which the feature will be registered.
- `feature`- `str`
- The feature string to be appended to the User-Agent header, e.g., "streaming" in Powertools.
 ## Raises- `AttributeError`
- If the provided session does not have an event system.