# aws_lambda_powertools.utilities.idempotency.serialization.dataclass API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/idempotency/serialization/dataclass.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/idempotency/serialization/dataclass.html)

---

# Module `aws_lambda_powertools.utilities.idempotency.serialization.dataclass`

## Classes

- `class DataclassSerializer (model: type[DataClass])`
- 
## Expand source code`class DataclassSerializer(BaseIdempotencyModelSerializer): """ A serializer class for transforming data between dataclass objects and dictionaries. """ def __init__(self, model: type[DataClass]): """ Parameters ---------- model: type[DataClass] A dataclass type to be used for serialization and deserialization """ self.__model: type[DataClass] = model def to_dict(self, data: DataClass) -> dict: return asdict(data) def from_dict(self, data: dict) -> DataClass: return self.__model(**data) @classmethod def instantiate(cls, model_type: Any) -> BaseIdempotencySerializer: model_type = get_actual_type(model_type=model_type) if model_type is None: raise IdempotencyNoSerializationModelError("No serialization model was supplied") if not is_dataclass(model_type): raise IdempotencyModelTypeError("Model type is not inherited of dataclass type") return cls(model=model_type) # type: ignore[arg-type]`A serializer class for transforming data between dataclass objects and dictionaries. ## Parameters- `model`- `type[DataClass]`
- A dataclass type to be used for serialization and deserialization
 ### Ancestors### Methods- `def from_dict(self, data: dict) ‑> Any`
- 
## Expand source code`def from_dict(self, data: dict) -> DataClass: return self.__model(**data)`
- `def to_dict(self, data: DataClass) ‑> dict`
- 
## Expand source code`def to_dict(self, data: DataClass) -> dict: return asdict(data)`
 ### Inherited members