# aws_lambda_powertools.utilities.data_masking.provider.kms API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_masking/provider/kms/index.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_masking/provider/kms/index.html)

---

# Module `aws_lambda_powertools.utilities.data_masking.provider.kms`

## Sub-modules

## Classes

- `class AWSEncryptionSDKProvider (keys: list[str],`
 key_provider=None,
 local_cache_capacity: int = 100,
 max_cache_age_seconds: float = 300.0,
 max_messages_encrypted: int = 4294967296,
 max_bytes_encrypted: int = 9223372036854775807,
 json_serializer: Callable[..., str] = functools.partial(<function dumps>, ensure_ascii=False),
 json_deserializer: Callable[[str], Any] = <function loads>)
- 
## Expand source code`class AWSEncryptionSDKProvider(BaseProvider): """ The AWSEncryptionSDKProvider is used as a provider for the DataMasking class. Usage ------- ``` from aws_lambda_powertools.utilities.data_masking import DataMasking from aws_lambda_powertools.utilities.data_masking.providers.kms.aws_encryption_sdk import ( AWSEncryptionSDKProvider, ) def lambda_handler(event, context): provider = AWSEncryptionSDKProvider(["arn:aws:kms:us-east-1:0123456789012:key/key-id"]) data_masker = DataMasking(provider=provider) data = { "project": "powertools", "sensitive": "password" } encrypted = data_masker.encrypt(data) return encrypted ``` """ def __init__( self, keys: list[str], key_provider=None, local_cache_capacity: int = CACHE_CAPACITY, max_cache_age_seconds: float = MAX_CACHE_AGE_SECONDS, max_messages_encrypted: int = MAX_MESSAGES_ENCRYPTED, max_bytes_encrypted: int = MAX_BYTES_ENCRYPTED, json_serializer: Callable[..., str] = functools.partial(json.dumps, ensure_ascii=False), json_deserializer: Callable[[str], Any] = json.loads, ): super().__init__(json_serializer=json_serializer, json_deserializer=json_deserializer) self._key_provider = key_provider or KMSKeyProvider( keys=keys, local_cache_capacity=local_cache_capacity, max_cache_age_seconds=max_cache_age_seconds, max_messages_encrypted=max_messages_encrypted, max_bytes_encrypted=max_bytes_encrypted, json_serializer=json_serializer, json_deserializer=json_deserializer, ) def encrypt(self, data: Any, provider_options: dict | None = None, **encryption_context: str) -> str: return self._key_provider.encrypt(data=data, provider_options=provider_options, **encryption_context) def decrypt(self, data: str, provider_options: dict | None = None, **encryption_context: str) -> Any: return self._key_provider.decrypt(data=data, provider_options=provider_options, **encryption_context)`The AWSEncryptionSDKProvider is used as a provider for the DataMasking class. ## Usage`from aws_lambda_powertools.utilities.data_masking import DataMasking from aws_lambda_powertools.utilities.data_masking.providers.kms.aws_encryption_sdk import ( AWSEncryptionSDKProvider, ) def lambda_handler(event, context): provider = AWSEncryptionSDKProvider(["arn:aws:kms:us-east-1:0123456789012:key/key-id"]) data_masker = DataMasking(provider=provider) data = { "project": "powertools", "sensitive": "password" } encrypted = data_masker.encrypt(data) return encrypted`### Ancestors### Inherited members