# aws_lambda_powertools.utilities.parser.models.kinesis API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/models/kinesis.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/models/kinesis.html)

---

# Module `aws_lambda_powertools.utilities.parser.models.kinesis`

## Functions

- `def extract_cloudwatch_logs_from_event(event:`- [KinesisDataStreamModel](#aws_lambda_powertools.utilities.parser.models.kinesis.KinesisDataStreamModel)) ‑> List[- [CloudWatchLogsDecode](cloudwatch.html#aws_lambda_powertools.utilities.parser.models.cloudwatch.CloudWatchLogsDecode)]
- 
## Expand source code`def extract_cloudwatch_logs_from_event(event: KinesisDataStreamModel) -> List[CloudWatchLogsDecode]: return [CloudWatchLogsDecode(**record.decompress_zlib_record_data_as_json()) for record in event.Records]`
- `def extract_cloudwatch_logs_from_record(record:`- [KinesisDataStreamRecord](#aws_lambda_powertools.utilities.parser.models.kinesis.KinesisDataStreamRecord)) ‑>- [CloudWatchLogsDecode](cloudwatch.html#aws_lambda_powertools.utilities.parser.models.cloudwatch.CloudWatchLogsDecode)
- 
## Expand source code`def extract_cloudwatch_logs_from_record(record: KinesisDataStreamRecord) -> CloudWatchLogsDecode: return CloudWatchLogsDecode(**record.decompress_zlib_record_data_as_json())`

## Classes

- `class KinesisDataStreamModel (**data: Any)`
- 
## Expand source code`class KinesisDataStreamModel(BaseModel): Records: List[KinesisDataStreamRecord]`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables- `var Records : List[`- [KinesisDataStreamRecord](#aws_lambda_powertools.utilities.parser.models.kinesis.KinesisDataStreamRecord)]
- `var model_config`
 
- `class KinesisDataStreamRecord (**data: Any)`
- 
## Expand source code`class KinesisDataStreamRecord(BaseModel): eventSource: Literal["aws:kinesis"] eventVersion: str eventID: str eventName: Literal["aws:kinesis:record"] invokeIdentityArn: str awsRegion: str eventSourceARN: str kinesis: KinesisDataStreamRecordPayload def decompress_zlib_record_data_as_json(self) -> Dict: """Decompress Kinesis Record bytes data zlib compressed to JSON""" if not isinstance(self.kinesis.data, bytes): raise ValueError("We can only decompress bytes data, not custom models.") return json.loads(zlib.decompress(self.kinesis.data, zlib.MAX_WBITS | 32))`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables- `var awsRegion : str`
- `var eventID : str`
- `var eventName : Literal['aws:kinesis:record']`
- `var eventSource : Literal['aws:kinesis']`
- `var eventSourceARN : str`
- `var eventVersion : str`
- `var invokeIdentityArn : str`
- `var kinesis :`- [KinesisDataStreamRecordPayload](#aws_lambda_powertools.utilities.parser.models.kinesis.KinesisDataStreamRecordPayload)
- `var model_config`
 ### Methods- `def decompress_zlib_record_data_as_json(self) ‑> Dict`
- 
## Expand source code`def decompress_zlib_record_data_as_json(self) -> Dict: """Decompress Kinesis Record bytes data zlib compressed to JSON""" if not isinstance(self.kinesis.data, bytes): raise ValueError("We can only decompress bytes data, not custom models.") return json.loads(zlib.decompress(self.kinesis.data, zlib.MAX_WBITS | 32))`Decompress Kinesis Record bytes data zlib compressed to JSON 
 
- `class KinesisDataStreamRecordPayload (**data: Any)`
- 
## Expand source code`class KinesisDataStreamRecordPayload(BaseModel): kinesisSchemaVersion: str partitionKey: str sequenceNumber: str data: Union[bytes, Type[BaseModel], BaseModel] # base64 encoded str is parsed into bytes approximateArrivalTimestamp: float @field_validator("data", mode="before") def data_base64_decode(cls, value): return base64_decode(value)`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables- `var approximateArrivalTimestamp : float`
- `var data : bytes | Type[pydantic.main.BaseModel] | pydantic.main.BaseModel`
- `var kinesisSchemaVersion : str`
- `var model_config`
- `var partitionKey : str`
- `var sequenceNumber : str`
 ### Static methods- `def data_base64_decode(value)`