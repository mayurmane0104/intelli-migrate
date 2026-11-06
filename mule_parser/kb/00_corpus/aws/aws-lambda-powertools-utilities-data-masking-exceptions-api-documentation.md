# aws_lambda_powertools.utilities.data_masking.exceptions API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_masking/exceptions.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_masking/exceptions.html)

---

# Module `aws_lambda_powertools.utilities.data_masking.exceptions`

## Classes

- `class DataMaskingContextMismatchError (*args, **kwargs)`
- 
## Expand source code`class DataMaskingContextMismatchError(Exception): """ Decrypting with the incorrect encryption context. """`Decrypting with the incorrect encryption context. ### Ancestors- builtins.Exception
- builtins.BaseException
 
- `class DataMaskingDecryptKeyError (*args, **kwargs)`
- 
## Expand source code`class DataMaskingDecryptKeyError(Exception): """ Decrypting with an invalid AWS KMS Key ARN. """`Decrypting with an invalid AWS KMS Key ARN. ### Ancestors- builtins.Exception
- builtins.BaseException
 
- `class DataMaskingDecryptValueError (*args, **kwargs)`
- 
## Expand source code`class DataMaskingDecryptValueError(Exception): """ Decrypting an invalid field. """`Decrypting an invalid field. ### Ancestors- builtins.Exception
- builtins.BaseException
 
- `class DataMaskingEncryptKeyError (*args, **kwargs)`
- 
## Expand source code`class DataMaskingEncryptKeyError(Exception): """ Encrypting with an invalid AWS KMS Key ARN. """`Encrypting with an invalid AWS KMS Key ARN. ### Ancestors- builtins.Exception
- builtins.BaseException
 
- `class DataMaskingFieldNotFoundError (*args, **kwargs)`
- 
## Expand source code`class DataMaskingFieldNotFoundError(Exception): """ Field not found. """`Field not found. ### Ancestors- builtins.Exception
- builtins.BaseException
 
- `class DataMaskingUnsupportedTypeError (*args, **kwargs)`
- 
## Expand source code`class DataMaskingUnsupportedTypeError(Exception): """ UnsupportedType Error """`UnsupportedType Error ### Ancestors- builtins.Exception
- builtins.BaseException