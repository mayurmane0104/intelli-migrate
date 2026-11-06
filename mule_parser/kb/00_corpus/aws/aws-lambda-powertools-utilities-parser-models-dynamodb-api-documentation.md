# aws_lambda_powertools.utilities.parser.models.dynamodb API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/models/dynamodb.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/models/dynamodb.html)

---

# Module `aws_lambda_powertools.utilities.parser.models.dynamodb`

## Classes

- `class DynamoDBStreamChangedRecordModel (**data: Any)`
- 
## Expand source code`class DynamoDBStreamChangedRecordModel(BaseModel): ApproximateCreationDateTime: Optional[datetime] = None Keys: Dict[str, Any] NewImage: Optional[Union[Dict[str, Any], Type[BaseModel], BaseModel]] = None OldImage: Optional[Union[Dict[str, Any], Type[BaseModel], BaseModel]] = None SequenceNumber: str SizeBytes: int StreamViewType: Literal["NEW_AND_OLD_IMAGES", "KEYS_ONLY", "NEW_IMAGE", "OLD_IMAGE"] # context on why it's commented: https://github.com/aws-powertools/powertools-lambda-python/pull/118 # since both images are optional, they can both be None. However, at least one must # exist in a legal model of NEW_AND_OLD_IMAGES type # @root_validator # def check_one_image_exists(cls, values): # noqa: ERA001 # new_img, old_img = values.get("NewImage"), values.get("OldImage") # noqa: ERA001 # stream_type = values.get("StreamViewType") # noqa: ERA001 # if stream_type == "NEW_AND_OLD_IMAGES" and not new_img and not old_img: # noqa: ERA001 # raise TypeError("DynamoDB streams model failed validation, missing both new & old stream images") # noqa: ERA001,E501 # return values # noqa: ERA001 @field_validator("Keys", "NewImage", "OldImage", mode="before") def deserialize_field(cls, value): return {k: _DESERIALIZER.deserialize(v) for k, v in value.items()}`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables- `var ApproximateCreationDateTime : datetime.datetime | None`
- `var Keys : Dict[str, Any]`
- `var NewImage : Dict[str, Any] | Type[pydantic.main.BaseModel] | pydantic.main.BaseModel | None`
- `var OldImage : Dict[str, Any] | Type[pydantic.main.BaseModel] | pydantic.main.BaseModel | None`
- `var SequenceNumber : str`
- `var SizeBytes : int`
- `var StreamViewType : Literal['NEW_AND_OLD_IMAGES', 'KEYS_ONLY', 'NEW_IMAGE', 'OLD_IMAGE']`
- `var model_config`
 ### Static methods- `def deserialize_field(value)`
 
- `class DynamoDBStreamModel (**data: Any)`
- 
## Expand source code`class DynamoDBStreamModel(BaseModel): Records: List[DynamoDBStreamRecordModel]`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables- `var Records : List[`- [DynamoDBStreamRecordModel](#aws_lambda_powertools.utilities.parser.models.dynamodb.DynamoDBStreamRecordModel)]
- `var model_config`
 
- `class DynamoDBStreamRecordModel (**data: Any)`
- 
## Expand source code`class DynamoDBStreamRecordModel(BaseModel): eventID: str eventName: Literal["INSERT", "MODIFY", "REMOVE"] eventVersion: float eventSource: Literal["aws:dynamodb"] awsRegion: str eventSourceARN: str dynamodb: DynamoDBStreamChangedRecordModel userIdentity: Optional[UserIdentity] = None`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
- `var dynamodb :`- [DynamoDBStreamChangedRecordModel](#aws_lambda_powertools.utilities.parser.models.dynamodb.DynamoDBStreamChangedRecordModel)
- `var eventID : str`
- `var eventName : Literal['INSERT', 'MODIFY', 'REMOVE']`
- `var eventSource : Literal['aws:dynamodb']`
- `var eventSourceARN : str`
- `var eventVersion : float`
- `var model_config`
- `var userIdentity :`- [UserIdentity](#aws_lambda_powertools.utilities.parser.models.dynamodb.UserIdentity)| None
 
- `class UserIdentity (**data: Any)`
- 
## Expand source code`class UserIdentity(BaseModel): type: Literal["Service"] # noqa: VNE003, A003 principalId: Literal["dynamodb.amazonaws.com"]`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables- `var model_config`
- `var principalId : Literal['dynamodb.amazonaws.com']`
- `var type : Literal['Service']`