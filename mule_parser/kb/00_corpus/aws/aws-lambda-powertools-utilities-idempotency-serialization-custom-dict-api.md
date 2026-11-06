# aws_lambda_powertools.utilities.idempotency.serialization.custom_dict API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/idempotency/serialization/custom_dict.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/idempotency/serialization/custom_dict.html)

---

# Module `aws_lambda_powertools.utilities.idempotency.serialization.custom_dict`

## Classes

- `class CustomDictSerializer (to_dict: Callable[[Any], dict], from_dict: Callable[[dict], Any])`
- 
## Expand source code`class CustomDictSerializer(BaseIdempotencySerializer): def __init__(self, to_dict: Callable[[Any], dict], from_dict: Callable[[dict], Any]): """ Parameters ---------- to_dict: Callable[[Any], dict] A function capable of transforming the saved data object representation into a dictionary from_dict: Callable[[dict], Any] A function capable of transforming the saved dictionary into the original data object representation """ self.__to_dict: Callable[[Any], dict] = to_dict self.__from_dict: Callable[[dict], Any] = from_dict def to_dict(self, data: Any) -> dict: return self.__to_dict(data) def from_dict(self, data: dict) -> Any: return self.__from_dict(data)`Abstract Base Class for Idempotency serialization layer, supporting dict operations. ## Parameters- `to_dict`- `Callable[[Any], dict]`
- A function capable of transforming the saved data object representation into a dictionary
- `from_dict`- `Callable[[dict], Any]`
- A function capable of transforming the saved dictionary into the original data object representation
 ### Ancestors- [BaseIdempotencySerializer](base.html#aws_lambda_powertools.utilities.idempotency.serialization.base.BaseIdempotencySerializer)
- abc.ABC
 ### Methods- `def from_dict(self, data: dict) ‑> Any`
- 
## Expand source code`def from_dict(self, data: dict) -> Any: return self.__from_dict(data)`
- `def to_dict(self, data: Any) ‑> dict`
- 
## Expand source code`def to_dict(self, data: Any) -> dict: return self.__to_dict(data)`