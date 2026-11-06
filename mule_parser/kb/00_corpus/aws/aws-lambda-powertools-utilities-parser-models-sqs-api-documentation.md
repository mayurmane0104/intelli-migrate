# aws_lambda_powertools.utilities.parser.models.sqs API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/models/sqs.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/models/sqs.html)

---

# Module `aws_lambda_powertools.utilities.parser.models.sqs`

## Classes

- `class SqsAttributesModel (**data: Any)`
- 
## Expand source code`class SqsAttributesModel(BaseModel): ApproximateReceiveCount: str ApproximateFirstReceiveTimestamp: datetime MessageDeduplicationId: Optional[str] = None MessageGroupId: Optional[str] = None SenderId: str SentTimestamp: datetime SequenceNumber: Optional[str] = None AWSTraceHeader: Optional[str] = None DeadLetterQueueSourceArn: Optional[str] = None`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables- `var AWSTraceHeader : str | None`
- `var ApproximateFirstReceiveTimestamp : datetime.datetime`
- `var ApproximateReceiveCount : str`
- `var DeadLetterQueueSourceArn : str | None`
- `var MessageDeduplicationId : str | None`
- `var MessageGroupId : str | None`
- `var SenderId : str`
- `var SentTimestamp : datetime.datetime`
- `var SequenceNumber : str | None`
- `var model_config`
 
- `class SqsModel (**data: Any)`
- 
## Expand source code`class SqsModel(BaseModel): Records: Sequence[SqsRecordModel]`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Subclasses### Class variables- `var Records : Sequence[`- [SqsRecordModel](#aws_lambda_powertools.utilities.parser.models.sqs.SqsRecordModel)]
- `var model_config`
 
- `class SqsMsgAttributeModel (**data: Any)`
- 
## Expand source code`class SqsMsgAttributeModel(BaseModel): stringValue: Optional[str] = None binaryValue: Optional[str] = None stringListValues: List[str] = [] binaryListValues: List[str] = [] dataType: str # context on why it's commented: https://github.com/aws-powertools/powertools-lambda-python/pull/118 # Amazon SQS supports the logical data types String, Number, and Binary with optional custom data type # labels with the format .custom-data-type. # https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-metadata.html#sqs-message-attributes # @validator("dataType") # def valid_type(cls, v): # noqa: VNE001,ERA001 # noqa: ERA001 # pattern = re.compile("Number.*|String.*|Binary.*") # noqa: ERA001 # if not pattern.match(v): # noqa: ERA001 # raise TypeError("data type is invalid") # noqa: ERA001 # return v # noqa: ERA001 # # # validate that dataType and value are not None and match # @root_validator # def check_str_and_binary_values(cls, values): # noqa: ERA001 # binary_val, str_val = values.get("binaryValue", ""), values.get("stringValue", "") # noqa: ERA001 # data_type = values.get("dataType") # noqa: ERA001 # if not str_val and not binary_val: # noqa: ERA001 # raise TypeError("both binaryValue and stringValue are missing") # noqa: ERA001 # if data_type.startswith("Binary") and not binary_val: # noqa: ERA001 # raise TypeError("binaryValue is missing") # noqa: ERA001 # if (data_type.startswith("String") or data_type.startswith("Number")) and not str_val: # noqa: ERA001 # raise TypeError("stringValue is missing") # noqa: ERA001 # return values # noqa: ERA001`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables- `var binaryListValues : List[str]`
- `var binaryValue : str | None`
- `var dataType : str`
- `var model_config`
- `var stringListValues : List[str]`
- `var stringValue : str | None`
 
- `class SqsRecordModel (**data: Any)`
- 
## Expand source code`class SqsRecordModel(BaseModel): messageId: str receiptHandle: str body: Union[str, Type[BaseModel], BaseModel] attributes: SqsAttributesModel messageAttributes: Dict[str, SqsMsgAttributeModel] md5OfBody: str md5OfMessageAttributes: Optional[str] = None eventSource: Literal["aws:sqs"] eventSourceARN: str awsRegion: str`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Subclasses### Class variables- `var attributes :`- [SqsAttributesModel](#aws_lambda_powertools.utilities.parser.models.sqs.SqsAttributesModel)
- `var awsRegion : str`
- `var body : str | Type[pydantic.main.BaseModel] | pydantic.main.BaseModel`
- `var eventSource : Literal['aws:sqs']`
- `var eventSourceARN : str`
- `var md5OfBody : str`
- `var md5OfMessageAttributes : str | None`
- `var messageAttributes : Dict[str,`- [SqsMsgAttributeModel](#aws_lambda_powertools.utilities.parser.models.sqs.SqsMsgAttributeModel)]
- `var messageId : str`
- `var model_config`
- `var receiptHandle : str`