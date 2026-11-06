# aws_lambda_powertools.utilities.parser.models.kafka API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/models/kafka.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/models/kafka.html)

---

# Module `aws_lambda_powertools.utilities.parser.models.kafka`

## Classes

- `class KafkaBaseEventModel (**data: Any)`
- 
## Expand source code`class KafkaBaseEventModel(BaseModel): bootstrapServers: List[str] records: Dict[str, List[KafkaRecordModel]] @field_validator("bootstrapServers", mode="before") def split_servers(cls, value): return None if not value else value.split(SERVERS_DELIMITER)`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
- The names of the class variables defined on the model.
- `__private_attributes__`
- Metadata about the private attributes of the model.
- `__signature__`
- The synthesized `__init__`[`Signature`][inspect.Signature] of the model.
- `__pydantic_complete__`
- Whether model building is completed, or if there are still undefined fields.
- `__pydantic_core_schema__`
- The core schema of the model.
- `__pydantic_custom_init__`
- Whether the model has a custom `__init__`function.
- `__pydantic_decorators__`
- Metadata containing the decorators defined on the model.
This replaces `Model.__validators__`and`Model.__root_validators__`from Pydantic V1.
- `__pydantic_generic_metadata__`
- Metadata for generic models; contains data used for a similar purpose to
**args**,**origin**,**parameters**in typing-module generics. May eventually be replaced by these.
- `__pydantic_parent_namespace__`
- Parent namespace of the model, used for automatic rebuilding of models.
- `__pydantic_post_init__`
- The name of the post-init method for the model, if defined.
- `__pydantic_root_model__`
- Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
- `__pydantic_serializer__`
- The `pydantic-core``SchemaSerializer`used to dump instances of the model.
- `__pydantic_validator__`
- The `pydantic-core``SchemaValidator`used to validate instances of the model.
- `__pydantic_fields__`
- A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
- `__pydantic_computed_fields__`
- A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
- `__pydantic_extra__`
- A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra] is set to`'allow'`.
- `__pydantic_fields_set__`
- The names of fields explicitly set during instantiation.
- `__pydantic_private__`
- Values of private attributes set on the model instance.
 Create a new model by parsing and validating input data from keyword arguments. Raises [ `ValidationError`][pydantic_core.ValidationError] if the input data cannot be validated to form a valid model.`self`is explicitly positional-only to allow`self`as a field name.### Ancestors- pydantic.main.BaseModel
 ### Subclasses### Class variables- `var bootstrapServers : List[str]`
- `var model_config`
- `var records : Dict[str, List[`- [KafkaRecordModel](#aws_lambda_powertools.utilities.parser.models.kafka.KafkaRecordModel)]]
 ### Static methods- `def split_servers(value)`
 
- `class KafkaMskEventModel (**data: Any)`
- 
## Expand source code`class KafkaMskEventModel(KafkaBaseEventModel): """Fully-managed AWS Apache Kafka event trigger Documentation: -------------- - https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html """ eventSource: Literal["aws:kafka"] eventSourceArn: str`Fully-managed AWS Apache Kafka event trigger Documentation: 
 Create a new model by parsing and validating input data from keyword arguments. Raises [ `ValidationError`][pydantic_core.ValidationError] if the input data cannot be validated to form a valid model.`self`is explicitly positional-only to allow`self`as a field name.### Ancestors- [KafkaBaseEventModel](#aws_lambda_powertools.utilities.parser.models.kafka.KafkaBaseEventModel)
- pydantic.main.BaseModel
 ### Class variables- `var eventSource : Literal['aws:kafka']`
- `var eventSourceArn : str`
- `var model_config`
 
- `class KafkaRecordModel (**data: Any)`
- 
## Expand source code`class KafkaRecordModel(BaseModel): topic: str partition: int offset: int timestamp: datetime timestampType: str key: bytes value: Union[str, Type[BaseModel]] headers: List[Dict[str, bytes]] # Added type ignore to keep compatibility between Pydantic v1 and v2 _decode_key = field_validator("key")(base64_decode) # type: ignore[type-var, unused-ignore] @field_validator("value", mode="before") def data_base64_decode(cls, value): as_bytes = base64_decode(value) return bytes_to_string(as_bytes) @field_validator("headers", mode="before") def decode_headers_list(cls, value): for header in value: for key, values in header.items(): header[key] = bytes(values) return value`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
- The names of the class variables defined on the model.
- `__private_attributes__`
- Metadata about the private attributes of the model.
- `__signature__`
- The synthesized `__init__`[`Signature`][inspect.Signature] of the model.
- `__pydantic_complete__`
- Whether model building is completed, or if there are still undefined fields.
- `__pydantic_core_schema__`
- The core schema of the model.
- `__pydantic_custom_init__`
- Whether the model has a custom `__init__`function.
- `__pydantic_decorators__`
- Metadata containing the decorators defined on the model.
This replaces `Model.__validators__`and`Model.__root_validators__`from Pydantic V1.
- `__pydantic_generic_metadata__`
- Metadata for generic models; contains data used for a similar purpose to
**args**,**origin**,**parameters**in typing-module generics. May eventually be replaced by these.
- `__pydantic_parent_namespace__`
- Parent namespace of the model, used for automatic rebuilding of models.
- `__pydantic_post_init__`
- The name of the post-init method for the model, if defined.
- `__pydantic_root_model__`
- Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
- `__pydantic_serializer__`
- The `pydantic-core``SchemaSerializer`used to dump instances of the model.
- `__pydantic_validator__`
- The `pydantic-core``SchemaValidator`used to validate instances of the model.
- `__pydantic_fields__`
- A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
- `__pydantic_computed_fields__`
- A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.
- `__pydantic_extra__`
- A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra] is set to`'allow'`.
- `__pydantic_fields_set__`
- The names of fields explicitly set during instantiation.
- `__pydantic_private__`
- Values of private attributes set on the model instance.
 Create a new model by parsing and validating input data from keyword arguments. Raises [ `ValidationError`][pydantic_core.ValidationError] if the input data cannot be validated to form a valid model.`self`is explicitly positional-only to allow`self`as a field name.### Ancestors- pydantic.main.BaseModel
 ### Class variables- `var headers : List[Dict[str, bytes]]`
- `var key : bytes`
- `var model_config`
- `var offset : int`
- `var partition : int`
- `var timestamp : datetime.datetime`
- `var timestampType : str`
- `var topic : str`
- `var value : str | Type[pydantic.main.BaseModel]`
 ### Static methods- `def data_base64_decode(value)`
- `def decode_headers_list(value)`
 
- `class KafkaSelfManagedEventModel (**data: Any)`
- 
## Expand source code`class KafkaSelfManagedEventModel(KafkaBaseEventModel): """Self-managed Apache Kafka event trigger Documentation: -------------- - https://docs.aws.amazon.com/lambda/latest/dg/with-kafka.html """ eventSource: Literal["SelfManagedKafka"]`Self-managed Apache Kafka event trigger Documentation: 
 Create a new model by parsing and validating input data from keyword arguments. Raises [ `ValidationError`][pydantic_core.ValidationError] if the input data cannot be validated to form a valid model.`self`is explicitly positional-only to allow`self`as a field name.### Ancestors- [KafkaBaseEventModel](#aws_lambda_powertools.utilities.parser.models.kafka.KafkaBaseEventModel)
- pydantic.main.BaseModel
 ### Class variables- `var eventSource : Literal['SelfManagedKafka']`
- `var model_config`