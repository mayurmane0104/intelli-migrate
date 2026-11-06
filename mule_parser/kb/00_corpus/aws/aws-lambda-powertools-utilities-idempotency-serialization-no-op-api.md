# aws_lambda_powertools.utilities.idempotency.serialization.no_op API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/idempotency/serialization/no_op.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/idempotency/serialization/no_op.html)

---

# Module `aws_lambda_powertools.utilities.idempotency.serialization.no_op`

## Classes

- `class NoOpSerializer`
- 
## Expand source code`class NoOpSerializer(BaseIdempotencySerializer): def __init__(self): """ Parameters ---------- Default serializer, does not transform data """ def to_dict(self, data: dict) -> dict: return data def from_dict(self, data: dict) -> dict: return data`Abstract Base Class for Idempotency serialization layer, supporting dict operations. ## ParametersDefault serializer, does not transform data ### Ancestors- [BaseIdempotencySerializer](base.html#aws_lambda_powertools.utilities.idempotency.serialization.base.BaseIdempotencySerializer)
- abc.ABC
 ### Methods- `def from_dict(self, data: dict) ‑> dict`
- 
## Expand source code`def from_dict(self, data: dict) -> dict: return data`
- `def to_dict(self, data: dict) ‑> dict`
- 
## Expand source code`def to_dict(self, data: dict) -> dict: return data`