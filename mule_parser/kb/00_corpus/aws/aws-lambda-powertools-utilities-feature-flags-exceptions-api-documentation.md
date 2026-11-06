# aws_lambda_powertools.utilities.feature_flags.exceptions API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/feature_flags/exceptions.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/feature_flags/exceptions.html)

---

# Module `aws_lambda_powertools.utilities.feature_flags.exceptions`

## Classes

- `class ConfigurationStoreError (*args, **kwargs)`
- 
## Expand source code`class ConfigurationStoreError(Exception): """When a configuration store raises an exception on config retrieval or parsing"""`When a configuration store raises an exception on config retrieval or parsing ### Ancestors- builtins.Exception
- builtins.BaseException
 
- `class SchemaValidationError (*args, **kwargs)`
- 
## Expand source code`class SchemaValidationError(Exception): """When feature flag schema fails validation"""`When feature flag schema fails validation ### Ancestors- builtins.Exception
- builtins.BaseException
 
- `class StoreClientError (*args, **kwargs)`
- 
## Expand source code`class StoreClientError(Exception): """When a store raises an exception that should be propagated to the client For example, Access Denied errors when the client doesn't permissions to fetch config """`When a store raises an exception that should be propagated to the client For example, Access Denied errors when the client doesn't permissions to fetch config ### Ancestors- builtins.Exception
- builtins.BaseException