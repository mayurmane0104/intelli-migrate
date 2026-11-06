# aws_lambda_powertools.utilities.parser.models.vpc_latticev2 API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/models/vpc_latticev2.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/parser/models/vpc_latticev2.html)

---

# Module `aws_lambda_powertools.utilities.parser.models.vpc_latticev2`

## Classes

- `class VpcLatticeV2Model (**data: Any)`
- 
## Expand source code`class VpcLatticeV2Model(BaseModel): version: str path: str method: str headers: Dict[str, str] query_string_parameters: Optional[Dict[str, str]] = Field(None, alias="queryStringParameters") body: Optional[Union[str, Type[BaseModel]]] = None is_base64_encoded: Optional[bool] = Field(None, alias="isBase64Encoded") request_context: VpcLatticeV2RequestContext = Field(..., alias="requestContext")`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables- `var body : str | Type[pydantic.main.BaseModel] | None`
- `var headers : Dict[str, str]`
- `var is_base64_encoded : bool | None`
- `var method : str`
- `var model_config`
- `var path : str`
- `var query_string_parameters : Dict[str, str] | None`
- `var request_context :`- [VpcLatticeV2RequestContext](#aws_lambda_powertools.utilities.parser.models.vpc_latticev2.VpcLatticeV2RequestContext)
- `var version : str`
 
- `class VpcLatticeV2RequestContext (**data: Any)`
- 
## Expand source code`class VpcLatticeV2RequestContext(BaseModel): service_network_arn: str = Field(alias="serviceNetworkArn") service_arn: str = Field(alias="serviceArn") target_group_arn: str = Field(alias="targetGroupArn") identity: VpcLatticeV2RequestContextIdentity region: str time_epoch: float = Field(alias="timeEpoch") time_epoch_as_datetime: datetime = Field(alias="timeEpoch") @field_validator("time_epoch_as_datetime", mode="before") def time_epoch_convert_to_miliseconds(cls, value: int): return round(int(value) / 1000)`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables- `var identity :`- [VpcLatticeV2RequestContextIdentity](#aws_lambda_powertools.utilities.parser.models.vpc_latticev2.VpcLatticeV2RequestContextIdentity)
- `var model_config`
- `var region : str`
- `var service_arn : str`
- `var service_network_arn : str`
- `var target_group_arn : str`
- `var time_epoch : float`
- `var time_epoch_as_datetime : datetime.datetime`
 ### Static methods- `def time_epoch_convert_to_miliseconds(value: int)`
 
- `class VpcLatticeV2RequestContextIdentity (**data: Any)`
- 
## Expand source code`class VpcLatticeV2RequestContextIdentity(BaseModel): source_vpc_arn: Optional[str] = Field(None, alias="sourceVpcArn") get_type: Optional[str] = Field(None, alias="type") principal: Optional[str] = Field(None, alias="principal") principal_org_id: Optional[str] = Field(None, alias="principalOrgID") session_name: Optional[str] = Field(None, alias="sessionName") x509_subject_cn: Optional[str] = Field(None, alias="X509SubjectCn") x509_issuer_ou: Optional[str] = Field(None, alias="X509IssuerOu") x509_san_dns: Optional[str] = Field(None, alias="x509SanDns") x509_san_uri: Optional[str] = Field(None, alias="X509SanUri") x509_san_name_cn: Optional[str] = Field(None, alias="X509SanNameCn")`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables- `var get_type : str | None`
- `var model_config`
- `var principal : str | None`
- `var principal_org_id : str | None`
- `var session_name : str | None`
- `var source_vpc_arn : str | None`
- `var x509_issuer_ou : str | None`
- `var x509_san_dns : str | None`
- `var x509_san_name_cn : str | None`
- `var x509_san_uri : str | None`
- `var x509_subject_cn : str | None`