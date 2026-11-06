# aws_lambda_powertools.utilities.idempotency.serialization.pydantic API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/idempotency/serialization/pydantic.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/idempotency/serialization/pydantic.html)

---

# Module `aws_lambda_powertools.utilities.idempotency.serialization.pydantic`

## Classes

- `class PydanticSerializer (model: type[BaseModel])`
- 
## Expand source code`class PydanticSerializer(BaseIdempotencyModelSerializer): """Pydantic serializer for idempotency models""" def __init__(self, model: type[BaseModel]): """ Parameters ---------- model: Model Pydantic model to be used for serialization """ self.__model: type[BaseModel] = model def to_dict(self, data: BaseModel) -> dict: return data.model_dump() def from_dict(self, data: dict) -> BaseModel: return self.__model.model_validate(data) @classmethod def instantiate(cls, model_type: Any) -> BaseIdempotencySerializer: model_type = get_actual_type(model_type=model_type) if model_type is None: raise IdempotencyNoSerializationModelError("No serialization model was supplied") if not issubclass(model_type, BaseModel): raise IdempotencyModelTypeError("Model type is not inherited from pydantic BaseModel") return cls(model=model_type)`Pydantic serializer for idempotency models ## Parameters- `model`- `Model`
- Pydantic model to be used for serialization
 ### Ancestors### Methods- `def from_dict(self, data: dict) ‑> pydantic.main.BaseModel`
- 
## Expand source code`def from_dict(self, data: dict) -> BaseModel: return self.__model.model_validate(data)`
- `def to_dict(self, data: BaseModel) ‑> dict`
- 
## Expand source code`def to_dict(self, data: BaseModel) -> dict: return data.model_dump()`
 ### Inherited members