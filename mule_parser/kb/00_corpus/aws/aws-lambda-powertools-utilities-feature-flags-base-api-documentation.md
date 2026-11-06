# aws_lambda_powertools.utilities.feature_flags.base API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/feature_flags/base.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/feature_flags/base.html)

---

# Module `aws_lambda_powertools.utilities.feature_flags.base`

## Classes

- `class BaseValidator`
- 
## Expand source code`class BaseValidator(ABC): @abstractmethod def validate(self): raise NotImplementedError() # pragma: no cover`Helper class that provides a standard way to create an ABC using inheritance. ### Ancestors- abc.ABC
 ### Subclasses### Methods- `def validate(self)`
- 
## Expand source code`@abstractmethod def validate(self): raise NotImplementedError() # pragma: no cover`
 
- `class StoreProvider`
- 
## Expand source code`class StoreProvider(ABC): @property @abstractmethod def get_raw_configuration(self) -> dict[str, Any]: """Get configuration from any store and return the parsed JSON dictionary""" raise NotImplementedError() # pragma: no cover @abstractmethod def get_configuration(self) -> dict[str, Any]: """Get configuration from any store and return the parsed JSON dictionary If envelope is set, it'll extract and return feature flags from configuration, otherwise it'll return the entire configuration fetched from the store. Raises ------ ConfigurationStoreError Any error that can occur during schema fetch or JSON parse Returns ------- dict[str, Any] parsed JSON dictionary **Example** ```python { "premium_features": { "default": False, "rules": { "customer tier equals premium": { "when_match": True, "conditions": [ { "action": "EQUALS", "key": "tier", "value": "premium", } ], } }, }, "feature_two": { "default": False } } ``` """ raise NotImplementedError() # pragma: no cover`Helper class that provides a standard way to create an ABC using inheritance. ### Ancestors- abc.ABC
 ### Subclasses### Instance variables- `prop get_raw_configuration : dict[str, Any]`
- 
## Expand source code`@property @abstractmethod def get_raw_configuration(self) -> dict[str, Any]: """Get configuration from any store and return the parsed JSON dictionary""" raise NotImplementedError() # pragma: no cover`Get configuration from any store and return the parsed JSON dictionary 
 ### Methods- `def get_configuration(self) ‑> dict[str, typing.Any]`
- 
## Expand source code`@abstractmethod def get_configuration(self) -> dict[str, Any]: """Get configuration from any store and return the parsed JSON dictionary If envelope is set, it'll extract and return feature flags from configuration, otherwise it'll return the entire configuration fetched from the store. Raises ------ ConfigurationStoreError Any error that can occur during schema fetch or JSON parse Returns ------- dict[str, Any] parsed JSON dictionary **Example** ```python { "premium_features": { "default": False, "rules": { "customer tier equals premium": { "when_match": True, "conditions": [ { "action": "EQUALS", "key": "tier", "value": "premium", } ], } }, }, "feature_two": { "default": False } } ``` """ raise NotImplementedError() # pragma: no cover`Get configuration from any store and return the parsed JSON dictionary If envelope is set, it'll extract and return feature flags from configuration, otherwise it'll return the entire configuration fetched from the store. ## Raises- `ConfigurationStoreError`
- Any error that can occur during schema fetch or JSON parse
 ## Returns- `dict[str, Any]`
- 
parsed JSON dictionary **Example**
 `{ "premium_features": { "default": False, "rules": { "customer tier equals premium": { "when_match": True, "conditions": [ { "action": "EQUALS", "key": "tier", "value": "premium", } ], } }, }, "feature_two": { "default": False } }`