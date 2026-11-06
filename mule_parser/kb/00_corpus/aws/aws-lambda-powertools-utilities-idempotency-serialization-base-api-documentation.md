# aws_lambda_powertools.utilities.idempotency.serialization.base API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/idempotency/serialization/base.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/idempotency/serialization/base.html)

---

# Module `aws_lambda_powertools.utilities.idempotency.serialization.base`

Serialization for supporting idempotency

## Classes

- `class BaseIdempotencyModelSerializer`
- 
## Expand source code`class BaseIdempotencyModelSerializer(BaseIdempotencySerializer): """ Abstract Base Class for Idempotency serialization layer, for using a model as data object representation. """ @classmethod @abstractmethod def instantiate(cls, model_type: Any) -> BaseIdempotencySerializer: """ Creates an instance of a serializer based on a provided model type. In case the model_type is unknown, None will be sent as `model_type`. It's on the implementer to verify that: - None is handled correctly - A model type not matching the expected types is handled Parameters ---------- model_type: Any The model type to instantiate the class for Returns ------- BaseIdempotencySerializer Instance of the serializer class """ pass`Abstract Base Class for Idempotency serialization layer, for using a model as data object representation. ### Ancestors- [BaseIdempotencySerializer](#aws_lambda_powertools.utilities.idempotency.serialization.base.BaseIdempotencySerializer)
- abc.ABC
 ### Subclasses### Static methods- `def instantiate(model_type: Any) ‑>`- [BaseIdempotencySerializer](#aws_lambda_powertools.utilities.idempotency.serialization.base.BaseIdempotencySerializer)
- 
Creates an instance of a serializer based on a provided model type. In case the model_type is unknown, None will be sent as `model_type`. It's on the implementer to verify that: - None is handled correctly - A model type not matching the expected types is handled## Parameters- `model_type`- `Any`
- The model type to instantiate the class for
 ## Returns- [BaseIdempotencySerializer](#aws_lambda_powertools.utilities.idempotency.serialization.base.BaseIdempotencySerializer)
- Instance of the serializer class
 
 
- `class BaseIdempotencySerializer`
- 
## Expand source code`class BaseIdempotencySerializer(ABC): """ Abstract Base Class for Idempotency serialization layer, supporting dict operations. """ @abstractmethod def to_dict(self, data: Any) -> dict: raise NotImplementedError("Implementation of to_dict is required") @abstractmethod def from_dict(self, data: dict) -> Any: raise NotImplementedError("Implementation of from_dict is required")`Abstract Base Class for Idempotency serialization layer, supporting dict operations. ### Ancestors- abc.ABC
 ### Subclasses### Methods- `def from_dict(self, data: dict) ‑> Any`
- 
## Expand source code`@abstractmethod def from_dict(self, data: dict) -> Any: raise NotImplementedError("Implementation of from_dict is required")`
- `def to_dict(self, data: Any) ‑> dict`
- 
## Expand source code`@abstractmethod def to_dict(self, data: Any) -> dict: raise NotImplementedError("Implementation of to_dict is required")`