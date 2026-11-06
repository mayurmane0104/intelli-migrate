# Data Masking - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking)

---

# Data Masking

The data masking utility can encrypt, decrypt, or irreversibly erase sensitive information to protect data confidentiality.

## Key features[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#key-features)

- Encrypt, decrypt, or irreversibly erase data with ease
- Erase sensitive information in one or more fields within nested data
- Seamless integration with [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html)for industry and AWS security best practices

## Terminology[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#terminology)

**Erasing** replaces sensitive information **irreversibly** with a non-sensitive placeholder *( *****)*, or with a customized mask. This operation replaces data in-memory, making it a one-way action.

**Encrypting** transforms plaintext into ciphertext using an encryption algorithm and a cryptographic key. It allows you to encrypt any sensitive data, so only allowed personnel to decrypt it. Learn more about encryption [here](https://aws.amazon.com/blogs/security/importance-of-encryption-and-how-aws-can-help/).

**Decrypting** transforms ciphertext back into plaintext using a decryption algorithm and the correct decryption key.

**Encryption context** is a non-secret `key=value` data used for authentication like `tenant_id:<id>`. This adds extra security and confirms encrypted data relationship with a context.

** Encrypted message** is a portable data structure that includes encrypted data along with copies of the encrypted data key. It includes everything Encryption SDK needs to validate authenticity, integrity, and to decrypt with the right master key.

** Envelope encryption** uses two different keys to encrypt data safely: master and data key. The data key encrypts the plaintext, and the master key encrypts the data key. It simplifies key management 

*(you own the master key)*, isolates compromises to data key, and scales better with large data volumes.

*Envelope encryption visualized.*

## Getting started[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#getting-started)

## Tip

All examples shared in this documentation are available within the [project repository](https://github.com/aws-powertools/powertools-lambda-python/tree/develop/examples).

### Install[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#install)

Add `aws-lambda-powertools[datamasking]` as a dependency in your preferred tool: *e.g.*, *requirements.txt*, *pyproject.toml*. This will install the [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html).

AWS Encryption SDK contains non-Python dependencies. This means you should use [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-build.html#using-sam-cli-build-options-container) or [official build container images](https://gallery.ecr.aws/search?searchTerm=sam%2Fbuild-python&popularRegistries=amazon) when building your application for AWS Lambda. Local development should work as expected.

### Required resources[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#required-resources)

By default, we use Amazon Key Management Service (KMS) for encryption and decryption operations.

Before you start, you will need a KMS symmetric key to encrypt and decrypt your data. Your Lambda function will need read and write access to it.

**NOTE**. We recommend setting a minimum of 1024MB of memory *(CPU intensive)*, and separate Lambda functions for encrypt and decrypt. For more information, you can see the full reports of our [load tests](https://github.com/aws-powertools/powertools-lambda-python/pull/2197#issuecomment-1730571597) and [traces](https://github.com/aws-powertools/powertools-lambda-python/pull/2197#issuecomment-1732060923).

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 | 
 | 

### Erasing data[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#erasing-data)

Erasing will remove the original data and replace it with a `*****`. This means you cannot recover erased data, and the data type will change to `str` for all data unless the data to be erased is of an Iterable type (`list`, `tuple`, `set`), in which case the method will return a new object of the same type as the input data but with each element replaced by the string `*****`.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 | 
 | 

#### Custom masking[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#custom-masking)

The `erase` method also supports additional flags for more advanced and flexible masking:

(bool) Enables dynamic masking behavior when set to `True`, by maintaining the original length and structure of the text replacing with *.

Expression:

`data_masker.erase(data, fields=["address.zip"], dynamic_mask=True)`Field result:

`'street': '*** **** **'`

(str) Specifies a simple pattern for masking data. This pattern is applied directly to the input string, replacing all the original characters. For example, with a `custom_mask` of "XX-XX" applied to "12345", the result would be "XX-XX".

Expression:

`data_masker.erase(data, fields=["address.zip"], custom_mask="XX")`Field result:

`'zip': 'XX'`

(str) `regex_pattern` defines a regular expression pattern used to identify parts of the input string that should be masked. This allows for more complex and flexible masking rules. It's used in conjunction with `mask_format`.
`mask_format` specifies the format to use when replacing parts of the string matched by `regex_pattern`. It can include placeholders (like \1, \2) to refer to captured groups in the regex pattern, allowing some parts of the original string to be preserved.

Expression:

`data_masker.erase(data, fields=["email"], regex_pattern=r"(.)(.*)(@.*)", mask_format=r"\1****\3")`Field result:

`'email': 'j****@example.com'`

(dict) Allows you to apply different masking rules (flags) for each data field.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 | 
 | 

### Encrypting data[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#encrypting-data)

## About static typing and encryption

Encrypting data may lead to a different data type, as it always transforms into a string *( <ciphertext>)*.

To encrypt, you will need an [encryption provider](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#providers). Here, we will use `AWSEncryptionSDKProvider`.

Under the hood, we delegate a [number of operations](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#encrypt-operation-with-encryption-sdk-kms) to AWS Encryption SDK to authenticate, create a portable encryption message, and actual data encryption.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 | 
 | 

| 1 2 3 | 
 | 

### Decrypting data[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#decrypting-data)

## About static typing and decryption

Decrypting data may lead to a different data type, as encrypted data is always a string *( <ciphertext>)*.

To decrypt, you will need an [encryption provider](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#providers). Here, we will use `AWSEncryptionSDKProvider`.

Under the hood, we delegate a [number of operations](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#decrypt-operation-with-encryption-sdk-kms) to AWS Encryption SDK to verify authentication, integrity, and actual ciphertext decryption.

**NOTE**. Decryption only works with KMS Key ARN.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 | 
 | 

| 1 2 3 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 | 
 | 

### Encryption context for integrity and authenticity[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#encryption-context-for-integrity-and-authenticity)

For a stronger security posture, you can add metadata to each encryption operation, and verify them during decryption. This is known as additional authenticated data (AAD). These are non-sensitive data that can help protect authenticity and integrity of your encrypted data, and even help to prevent a [confused deputy](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html) situation.

## Important considerations you should know

- **Exact match verification on decrypt**. Be careful using random data like- `timestamps`as encryption context if you can't provide them on decrypt.
- **Only**. We will raise- `string`values are supported- `DataMaskingUnsupportedTypeError`for non-string values.
- **Use non-sensitive data only**. When using KMS, encryption context is available as plaintext in AWS CloudTrail, unless you- [intentionally disabled KMS events](https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html#filtering-kms-events).

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 | 
 | 

- They must match otherwise the operation will fail with `DataMaskingContextMismatchError`.

### Choosing parts of your data[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#choosing-parts-of-your-data)

## Current limitations

- The `fields`parameter is not yet supported in`encrypt`and`decrypt`operations.
- We support `JSON`data types only - see[data serialization for more details](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#data-serialization).

You can use the `fields` parameter with the dot notation `.` to choose one or more parts of your data to `erase`. This is useful when you want to keep data structure intact except the confidential fields.

When `fields` is present, `erase` behaves differently:

| Operation | Behavior | Example | Result | 
|---|---|---|---|
| `erase` | Replace data while keeping collections type intact. | `{"cards": ["a", "b"]}` | `{"cards": ["*****", "*****"]}` | 

Here are common scenarios to best visualize how to use `fields`.

You want to erase data in the `card_number` field.

Expression:

`data_masker.erase(data, fields=["card_number"])`

| 1 2 3 4 5 | 
 | 

| 1 2 3 4 5 | 
 | 

You want to erase data in the `postcode` field.

Expression:

`data_masker.erase(data, fields=["address.postcode"])`

| 1 2 3 4 5 6 7 8 | 
 | 

| 1 2 3 4 5 6 7 8 | 
 | 

You want to erase data in both `postcode` and `street` fields.

Expression:

`data_masker.erase(data, fields=["address.postcode", "address.street"])`

| 1 2 3 4 5 6 7 8 9 | 
 | 

| 1 2 3 4 5 6 7 8 9 | 
 | 

You want to erase data under `address` field.

Expression:

`data_masker.erase(data, fields=["address"])`

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 | 
 | 

| 1 2 3 4 5 6 7 8 9 | 
 | 

You want to erase data under `name` field.

Expression:

`data_masker.erase(data, fields=["category..name"])`

| 1 2 3 4 5 6 7 8 9 10 11 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 | 
 | 

You want to erase data under `street` field located at the any index of the address list.

Expression:

`data_masker.erase(data, fields=["address[*].street"])`

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 | 
 | 

You want to erase data by slicing a list.

Expression:

`data_masker.erase(data, fields=["address[-1].street"])`

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 | 
 | 

You want to erase data by finding for a field with conditional expression.

Expression:

`data_masker.erase(data, fields=["$.address[?(@.postcode > 12000)]"])`

`$`: Represents the root of the JSON structure.

`.address`: Selects the "address" property within the JSON structure.

`(@.postcode > 12000)`: Specifies the condition that elements should meet. It selects elements where the value of the`postcode`property is`greater than 12000`.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 | 
 | 

For comprehensive guidance on using JSONPath syntax, please refer to the official documentation available at [jsonpath-ng](https://github.com/h2non/jsonpath-ng#jsonpath-syntax)

#### JSON[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#json)

We also support data in JSON string format as input. We automatically deserialize it, then handle each field operation as expected.

Note that the return will be a deserialized JSON and your desired fields updated.

Expression: `data_masker.erase(data, fields=["card_number", "address.postcode"])`

| `1` | 
 | 

| 1 2 3 4 5 6 7 8 | 
 | 

## Advanced[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#advanced)

### Data serialization[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#data-serialization)

## Extended input support

We support `Pydantic models`, `Dataclasses`, and custom classes with `dict()` or `__dict__` for input.

These types are automatically converted into dictionaries before `masking` and `encrypting` operations. Please not that we **don't convert back** to the original type, and the returned object will be a dictionary.

Before we traverse the data structure, we perform two important operations on input data:

- If `JSON string`,**deserialize**using default or provided deserializer.
- If `dictionary or complex types`,**normalize**into`JSON`to prevent traversing unsupported data types.

For compatibility or performance, you can optionally pass your own JSON serializer and deserializer to replace `json.dumps` and `json.loads` respectively:

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 | 
 | 

### Using multiple keys[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#using-multiple-keys)

You can use multiple KMS keys from more than one AWS account for higher availability, when instantiating `AWSEncryptionSDKProvider`.

| using_multiple_keys.py | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 | 
 | 

### Providers[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#providers)

#### AWS Encryption SDK[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#aws-encryption-sdk)

You can modify the following values when initializing the `AWSEncryptionSDKProvider` to best accommodate your security and performance thresholds.

| Parameter | Default | Description | 
|---|---|---|
| local_cache_capacity | `100` | The maximum number of entries that can be retained in the local cryptographic materials cache | 
| max_cache_age_seconds | `300` | The maximum time (in seconds) that a cache entry may be kept in the cache | 
| max_messages_encrypted | `4294967296` | The maximum number of messages that may be encrypted under a cache entry | 
| max_bytes_encrypted | `9223372036854775807` | The maximum number of bytes that may be encrypted under a cache entry | 

If required, you can customize the default values when initializing the `AWSEncryptionSDKProvider` class.

| aws_encryption_provider_example.py | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 | 
 | 

##### Passing additional SDK arguments[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#passing-additional-sdk-arguments)

As an escape hatch mechanism, you can pass additional arguments to the `AWSEncryptionSDKProvider` via the `provider_options` parameter.

For example, the AWS Encryption SDK defaults to using the `AES_256_GCM_HKDF_SHA512_COMMIT_KEY_ECDSA_P384` algorithm for encrypting your Data Key. If you want, you have the flexibility to customize and choose a different encryption algorithm.

| changing_default_algorithm.py | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 | 
 | 

### Data masking request flow[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#data-masking-request-flow)

The following sequence diagrams explain how `DataMasking` behaves under different scenarios.

#### Erase operation[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#erase-operation)

Erasing operations occur in-memory and we cannot recover the original value.

*Simple masking operation*

#### Encrypt operation with Encryption SDK (KMS)[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#encrypt-operation-with-encryption-sdk-kms)

We call KMS to generate an unique data key that can be used for multiple `encrypt` operation in-memory. It improves performance, cost and prevent throttling.

To make this operation simpler to visualize, we keep caching details in a [separate sequence diagram](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#caching-encrypt-operations-with-encryption-sdk). Caching is enabled by default.

*Encrypting operation using envelope encryption.*

#### Encrypt operation with multiple KMS Keys[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#encrypt-operation-with-multiple-kms-keys)

When encrypting data with multiple KMS keys, the `aws_encryption_sdk` makes additional API calls to encrypt the data with each of the specified keys.

*Encrypting operation using envelope encryption.*

#### Decrypt operation with Encryption SDK (KMS)[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#decrypt-operation-with-encryption-sdk-kms)

We call KMS to decrypt the encrypted data key available in the encrypted message. If successful, we run authentication *(context)* and integrity checks (*algorithm, data key length, etc*) to confirm its proceedings.

Lastly, we decrypt the original encrypted data, throw away the decrypted data key for security reasons, and return the original plaintext data.

*Decrypting operation using envelope encryption.*

#### Caching encrypt operations with Encryption SDK[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#caching-encrypt-operations-with-encryption-sdk)

Without caching, every `encrypt()` operation would generate a new data key. It significantly increases latency and cost for ephemeral and short running environments like Lambda.

With caching, we balance ephemeral Lambda environment performance characteristics with [adjustable thresholds](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#aws-encryption-sdk) to meet your security needs.

Data key recycling

We request a new data key when a cached data key exceeds any of the following security thresholds:

- **Max age in seconds**
- **Max number of encrypted messages**
- **Max bytes encrypted**across all operations

*Caching data keys during encrypt operation.*

## Testing your code[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#testing-your-code)

### Testing erase operation[¶](https://docs.aws.amazon.com/powertools/python/latest/utilities/data_masking/#testing-erase-operation)

Testing your code with a simple erase operation

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 | 
 |