# aws_lambda_powertools.event_handler.openapi.models API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/event_handler/openapi/models.html](https://docs.aws.amazon.com/powertools/python/latest/api/event_handler/openapi/models.html)

---

# Module `aws_lambda_powertools.event_handler.openapi.models`

## Global variables

- `var MODEL_CONFIG_IGNORE`
- 
The code defines Pydantic models for the various OpenAPI objects like OpenAPI, PathItem, Operation, Parameter etc. These models can be used to parse OpenAPI JSON/YAML files into Python objects, or generate OpenAPI from Python data. 

## Classes

- `class APIKey (**data: Any)`
- 
## Expand source code`class APIKey(SecurityBase): type_: SecuritySchemeType = Field(default=SecuritySchemeType.apiKey, alias="type") in_: APIKeyIn = Field(alias="in") name: str`This class serves as a Pydantic proxy model to add OpenAPI extensions. OpenAPI extensions are arbitrary fields, so we remove openapi_extensions when dumping and add only the provided value in the schema. Create a new model by parsing and validating input data from keyword arguments. Raises [ `ValidationError`][pydantic_core.ValidationError] if the input data cannot be validated to form a valid model.`self`is explicitly positional-only to allow`self`as a field name.### Ancestors- [SecurityBase](#aws_lambda_powertools.event_handler.openapi.models.SecurityBase)
- [OpenAPIExtensions](#aws_lambda_powertools.event_handler.openapi.models.OpenAPIExtensions)
- pydantic.main.BaseModel
 ### Class variables- `var in_ :`- [APIKeyIn](#aws_lambda_powertools.event_handler.openapi.models.APIKeyIn)
- `var model_config`
- `var name : str`
- `var type_ :`- [SecuritySchemeType](#aws_lambda_powertools.event_handler.openapi.models.SecuritySchemeType)
 
- `class APIKeyIn (*args, **kwds)`
- 
## Expand source code`class APIKeyIn(Enum): query = "query" header = "header" cookie = "cookie"`Create a collection of name/value pairs. Example enumeration: `>>> class Color(Enum): ... RED = 1 ... BLUE = 2 ... GREEN = 3`Access them by: - attribute access:
 Color.RED - value lookup:
 Color(1) - name lookup:
 Color['RED'] Enumerations can be iterated over, and know how many members they have: `>>> len(Color) 3``>>> list(Color) [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]`Methods can be added to enumerations, and members can have their own attributes – see the documentation for details. ### Ancestors- enum.Enum
 ### Class variables
- `var header`
- `var query`
 
- `class Components (**data: Any)`
- 
## Expand source code`class Components(BaseModel): schemas: Optional[Dict[str, Union[Schema, Reference]]] = None responses: Optional[Dict[str, Union[Response, Reference]]] = None parameters: Optional[Dict[str, Union[Parameter, Reference]]] = None examples: Optional[Dict[str, Union[Example, Reference]]] = None requestBodies: Optional[Dict[str, Union[RequestBody, Reference]]] = None headers: Optional[Dict[str, Union[Header, Reference]]] = None securitySchemes: Optional[Dict[str, Union[SecurityScheme, Reference]]] = None links: Optional[Dict[str, Union[Link, Reference]]] = None # Using Any for Specification Extensions callbacks: Optional[Dict[str, Union[Dict[str, PathItem], Reference, Any]]] = None pathItems: Optional[Dict[str, Union[PathItem, Reference]]] = None model_config = MODEL_CONFIG_ALLOW`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables- `var callbacks : Dict[str, Dict[str,`- [PathItem](#aws_lambda_powertools.event_handler.openapi.models.PathItem)] |- [Reference](#aws_lambda_powertools.event_handler.openapi.models.Reference)| Any] | None
- `var examples : Dict[str,`- [Example](#aws_lambda_powertools.event_handler.openapi.models.Example)|- [Reference](#aws_lambda_powertools.event_handler.openapi.models.Reference)] | None
- `var headers : Dict[str,`- [Header](#aws_lambda_powertools.event_handler.openapi.models.Header)|- [Reference](#aws_lambda_powertools.event_handler.openapi.models.Reference)] | None
- `var links : Dict[str,`- [Link](#aws_lambda_powertools.event_handler.openapi.models.Link)|- [Reference](#aws_lambda_powertools.event_handler.openapi.models.Reference)] | None
- `var model_config`
- `var parameters : Dict[str,`- [Parameter](#aws_lambda_powertools.event_handler.openapi.models.Parameter)|- [Reference](#aws_lambda_powertools.event_handler.openapi.models.Reference)] | None
- `var pathItems : Dict[str,`- [PathItem](#aws_lambda_powertools.event_handler.openapi.models.PathItem)|- [Reference](#aws_lambda_powertools.event_handler.openapi.models.Reference)] | None
- `var requestBodies : Dict[str,`- [RequestBody](#aws_lambda_powertools.event_handler.openapi.models.RequestBody)|- [Reference](#aws_lambda_powertools.event_handler.openapi.models.Reference)] | None
- `var responses : Dict[str,`- [Response](#aws_lambda_powertools.event_handler.openapi.models.Response)|- [Reference](#aws_lambda_powertools.event_handler.openapi.models.Reference)] | None
- `var schemas : Dict[str,`- [Schema](#aws_lambda_powertools.event_handler.openapi.models.Schema)|- [Reference](#aws_lambda_powertools.event_handler.openapi.models.Reference)] | None
- `var securitySchemes : Dict[str,`- [APIKey](#aws_lambda_powertools.event_handler.openapi.models.APIKey)|- [HTTPBase](#aws_lambda_powertools.event_handler.openapi.models.HTTPBase)|- [OAuth2](#aws_lambda_powertools.event_handler.openapi.models.OAuth2)|- [OpenIdConnect](#aws_lambda_powertools.event_handler.openapi.models.OpenIdConnect)|- [HTTPBearer](#aws_lambda_powertools.event_handler.openapi.models.HTTPBearer)|- [MutualTLS](#aws_lambda_powertools.event_handler.openapi.models.MutualTLS)|- [Reference](#aws_lambda_powertools.event_handler.openapi.models.Reference)] | None
 
- `class Contact (**data: Any)`
- 
## Expand source code`class Contact(BaseModel): name: Optional[str] = None url: Optional[AnyUrl] = None email: Optional[str] = None model_config = MODEL_CONFIG_ALLOW`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables- `var email : str | None`
- `var model_config`
- `var name : str | None`
- `var url : pydantic.networks.AnyUrl | None`
 
- `class Discriminator (**data: Any)`
- 
## Expand source code`class Discriminator(BaseModel): propertyName: str mapping: Optional[Dict[str, str]] = None`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables- `var mapping : Dict[str, str] | None`
- `var model_config`
- `var propertyName : str`
 
- `class Encoding (**data: Any)`
- 
## Expand source code`class Encoding(BaseModel): contentType: Optional[str] = None headers: Optional[Dict[str, Union["Header", Reference]]] = None style: Optional[str] = None explode: Optional[bool] = None allowReserved: Optional[bool] = None model_config = MODEL_CONFIG_ALLOW`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables
- `class Example (**data: Any)`
- 
## Expand source code`class Example(BaseModel): summary: Optional[str] = None description: Optional[str] = None value: Optional[Any] = None externalValue: Optional[AnyUrl] = None model_config = MODEL_CONFIG_ALLOW`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables- `var description : str | None`
- `var externalValue : pydantic.networks.AnyUrl | None`
- `var model_config`
- `var summary : str | None`
- `var value : Any | None`
 
- `class ExternalDocumentation (**data: Any)`
- 
## Expand source code`class ExternalDocumentation(BaseModel): description: Optional[str] = None url: AnyUrl model_config = MODEL_CONFIG_ALLOW`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables- `var description : str | None`
- `var model_config`
- `var url : pydantic.networks.AnyUrl`
 
- `class HTTPBase (**data: Any)`
- 
## Expand source code`class HTTPBase(SecurityBase): type_: SecuritySchemeType = Field(default=SecuritySchemeType.http, alias="type") scheme: str`This class serves as a Pydantic proxy model to add OpenAPI extensions. OpenAPI extensions are arbitrary fields, so we remove openapi_extensions when dumping and add only the provided value in the schema. Create a new model by parsing and validating input data from keyword arguments. Raises [ `ValidationError`][pydantic_core.ValidationError] if the input data cannot be validated to form a valid model.`self`is explicitly positional-only to allow`self`as a field name.### Ancestors- [SecurityBase](#aws_lambda_powertools.event_handler.openapi.models.SecurityBase)
- [OpenAPIExtensions](#aws_lambda_powertools.event_handler.openapi.models.OpenAPIExtensions)
- pydantic.main.BaseModel
 ### Subclasses### Class variables- `var model_config`
- `var scheme : str`
- `var type_ :`- [SecuritySchemeType](#aws_lambda_powertools.event_handler.openapi.models.SecuritySchemeType)
 
- `class HTTPBearer (**data: Any)`
- 
## Expand source code`class HTTPBearer(HTTPBase): # type: ignore[override] scheme: Literal["bearer"] = "bearer" bearerFormat: Optional[str] = None`This class serves as a Pydantic proxy model to add OpenAPI extensions. OpenAPI extensions are arbitrary fields, so we remove openapi_extensions when dumping and add only the provided value in the schema. Create a new model by parsing and validating input data from keyword arguments. Raises [ `ValidationError`][pydantic_core.ValidationError] if the input data cannot be validated to form a valid model.`self`is explicitly positional-only to allow`self`as a field name.### Ancestors- [HTTPBase](#aws_lambda_powertools.event_handler.openapi.models.HTTPBase)
- [SecurityBase](#aws_lambda_powertools.event_handler.openapi.models.SecurityBase)
- [OpenAPIExtensions](#aws_lambda_powertools.event_handler.openapi.models.OpenAPIExtensions)
- pydantic.main.BaseModel
 ### Class variables- `var bearerFormat : str | None`
- `var model_config`
- `var scheme : Literal['bearer']`
 
- `class Header (**data: Any)`
- 
## Expand source code`class Header(ParameterBase): pass`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 Create a new model by parsing and validating input data from keyword arguments. Raises [ `ValidationError`][pydantic_core.ValidationError] if the input data cannot be validated to form a valid model.`self`is explicitly positional-only to allow`self`as a field name.### Ancestors- [ParameterBase](#aws_lambda_powertools.event_handler.openapi.models.ParameterBase)
- pydantic.main.BaseModel
 ### Class variables- `var model_config`
 
- `class Info (**data: Any)`
- 
## Expand source code`class Info(BaseModel): title: str description: Optional[str] = None termsOfService: Optional[str] = None contact: Optional[Contact] = None license: Optional[License] = None # noqa: A003 version: str summary: Optional[str] = None model_config = MODEL_CONFIG_IGNORE`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables
- `class License (**data: Any)`
- 
## Expand source code`class License(BaseModel): name: str identifier: Optional[str] = None url: Optional[AnyUrl] = None model_config = MODEL_CONFIG_ALLOW`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables- `var identifier : str | None`
- `var model_config`
- `var name : str`
- `var url : pydantic.networks.AnyUrl | None`
 
- `class Link (**data: Any)`
- 
## Expand source code`class Link(BaseModel): operationRef: Optional[str] = None operationId: Optional[str] = None parameters: Optional[Dict[str, Union[Any, str]]] = None requestBody: Optional[Union[Any, str]] = None description: Optional[str] = None server: Optional[Server] = None model_config = MODEL_CONFIG_ALLOW`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables- `var description : str | None`
- `var model_config`
- `var operationId : str | None`
- `var operationRef : str | None`
- `var parameters : Dict[str, Any | str] | None`
- `var requestBody : Any | str | None`
- `var server :`- [Server](#aws_lambda_powertools.event_handler.openapi.models.Server)| None
 
- `class MediaType (**data: Any)`
- 
## Expand source code`class MediaType(BaseModel): schema_: Optional[Union[Schema, Reference]] = Field(default=None, alias="schema") examples: Optional[Dict[str, Union[Example, Reference]]] = None encoding: Optional[Dict[str, Encoding]] = None model_config = MODEL_CONFIG_ALLOW`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables
- `class MutualTLS (**data: Any)`
- 
## Expand source code`class MutualTLS(SecurityBase): type_: SecuritySchemeType = Field(default=SecuritySchemeType.mutualTLS, alias="type")`This class serves as a Pydantic proxy model to add OpenAPI extensions. OpenAPI extensions are arbitrary fields, so we remove openapi_extensions when dumping and add only the provided value in the schema. Create a new model by parsing and validating input data from keyword arguments. Raises [ `ValidationError`][pydantic_core.ValidationError] if the input data cannot be validated to form a valid model.`self`is explicitly positional-only to allow`self`as a field name.### Ancestors- [SecurityBase](#aws_lambda_powertools.event_handler.openapi.models.SecurityBase)
- [OpenAPIExtensions](#aws_lambda_powertools.event_handler.openapi.models.OpenAPIExtensions)
- pydantic.main.BaseModel
 ### Class variables- `var model_config`
- `var type_ :`- [SecuritySchemeType](#aws_lambda_powertools.event_handler.openapi.models.SecuritySchemeType)
 
- `class OAuth2 (**data: Any)`
- 
## Expand source code`class OAuth2(SecurityBase): type_: SecuritySchemeType = Field(default=SecuritySchemeType.oauth2, alias="type") flows: OAuthFlows`This class serves as a Pydantic proxy model to add OpenAPI extensions. OpenAPI extensions are arbitrary fields, so we remove openapi_extensions when dumping and add only the provided value in the schema. Create a new model by parsing and validating input data from keyword arguments. Raises [ `ValidationError`][pydantic_core.ValidationError] if the input data cannot be validated to form a valid model.`self`is explicitly positional-only to allow`self`as a field name.### Ancestors- [SecurityBase](#aws_lambda_powertools.event_handler.openapi.models.SecurityBase)
- [OpenAPIExtensions](#aws_lambda_powertools.event_handler.openapi.models.OpenAPIExtensions)
- pydantic.main.BaseModel
 ### Class variables- `var flows :`- [OAuthFlows](#aws_lambda_powertools.event_handler.openapi.models.OAuthFlows)
- `var model_config`
- `var type_ :`- [SecuritySchemeType](#aws_lambda_powertools.event_handler.openapi.models.SecuritySchemeType)
 
- `class OAuthFlow (**data: Any)`
- 
## Expand source code`class OAuthFlow(BaseModel): refreshUrl: Optional[str] = None scopes: Dict[str, str] = {} model_config = MODEL_CONFIG_ALLOW`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Subclasses### Class variables- `var model_config`
- `var refreshUrl : str | None`
- `var scopes : Dict[str, str]`
 
- `class OAuthFlowAuthorizationCode (**data: Any)`
- 
## Expand source code`class OAuthFlowAuthorizationCode(OAuthFlow): authorizationUrl: str tokenUrl: str`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 Create a new model by parsing and validating input data from keyword arguments. Raises [ `ValidationError`][pydantic_core.ValidationError] if the input data cannot be validated to form a valid model.`self`is explicitly positional-only to allow`self`as a field name.### Ancestors- [OAuthFlow](#aws_lambda_powertools.event_handler.openapi.models.OAuthFlow)
- pydantic.main.BaseModel
 ### Class variables
- `var model_config`
- `var tokenUrl : str`
 
- `class OAuthFlowClientCredentials (**data: Any)`
- 
## Expand source code`class OAuthFlowClientCredentials(OAuthFlow): tokenUrl: str`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 Create a new model by parsing and validating input data from keyword arguments. Raises [ `ValidationError`][pydantic_core.ValidationError] if the input data cannot be validated to form a valid model.`self`is explicitly positional-only to allow`self`as a field name.### Ancestors- [OAuthFlow](#aws_lambda_powertools.event_handler.openapi.models.OAuthFlow)
- pydantic.main.BaseModel
 ### Class variables- `var model_config`
- `var tokenUrl : str`
 
- `class OAuthFlowImplicit (**data: Any)`
- 
## Expand source code`class OAuthFlowImplicit(OAuthFlow): authorizationUrl: str`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 Create a new model by parsing and validating input data from keyword arguments. Raises [ `ValidationError`][pydantic_core.ValidationError] if the input data cannot be validated to form a valid model.`self`is explicitly positional-only to allow`self`as a field name.### Ancestors- [OAuthFlow](#aws_lambda_powertools.event_handler.openapi.models.OAuthFlow)
- pydantic.main.BaseModel
 ### Class variables
- `var model_config`
 
- `class OAuthFlowPassword (**data: Any)`
- 
## Expand source code`class OAuthFlowPassword(OAuthFlow): tokenUrl: str`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 Create a new model by parsing and validating input data from keyword arguments. Raises [ `ValidationError`][pydantic_core.ValidationError] if the input data cannot be validated to form a valid model.`self`is explicitly positional-only to allow`self`as a field name.### Ancestors- [OAuthFlow](#aws_lambda_powertools.event_handler.openapi.models.OAuthFlow)
- pydantic.main.BaseModel
 ### Class variables- `var model_config`
- `var tokenUrl : str`
 
- `class OAuthFlows (**data: Any)`
- 
## Expand source code`class OAuthFlows(BaseModel): implicit: Optional[OAuthFlowImplicit] = None password: Optional[OAuthFlowPassword] = None clientCredentials: Optional[OAuthFlowClientCredentials] = None authorizationCode: Optional[OAuthFlowAuthorizationCode] = None model_config = MODEL_CONFIG_ALLOW`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables
- `var clientCredentials :`- [OAuthFlowClientCredentials](#aws_lambda_powertools.event_handler.openapi.models.OAuthFlowClientCredentials)| None
- `var implicit :`- [OAuthFlowImplicit](#aws_lambda_powertools.event_handler.openapi.models.OAuthFlowImplicit)| None
- `var model_config`
- `var password :`- [OAuthFlowPassword](#aws_lambda_powertools.event_handler.openapi.models.OAuthFlowPassword)| None
 
- `class OpenAPI (**data: Any)`
- 
## Expand source code`class OpenAPI(OpenAPIExtensions): openapi: str info: Info jsonSchemaDialect: Optional[str] = None servers: Optional[List[Server]] = None # Using Any for Specification Extensions paths: Optional[Dict[str, Union[PathItem, Any]]] = None webhooks: Optional[Dict[str, Union[PathItem, Reference]]] = None components: Optional[Components] = None security: Optional[List[Dict[str, List[str]]]] = None tags: Optional[List[Tag]] = None externalDocs: Optional[ExternalDocumentation] = None model_config = MODEL_CONFIG_ALLOW`This class serves as a Pydantic proxy model to add OpenAPI extensions. OpenAPI extensions are arbitrary fields, so we remove openapi_extensions when dumping and add only the provided value in the schema. Create a new model by parsing and validating input data from keyword arguments. Raises [ `ValidationError`][pydantic_core.ValidationError] if the input data cannot be validated to form a valid model.`self`is explicitly positional-only to allow`self`as a field name.### Ancestors- [OpenAPIExtensions](#aws_lambda_powertools.event_handler.openapi.models.OpenAPIExtensions)
- pydantic.main.BaseModel
 ### Class variables- `var components :`- [Components](#aws_lambda_powertools.event_handler.openapi.models.Components)| None
- `var externalDocs :`- [ExternalDocumentation](#aws_lambda_powertools.event_handler.openapi.models.ExternalDocumentation)| None
- `var info :`- [Info](#aws_lambda_powertools.event_handler.openapi.models.Info)
- `var jsonSchemaDialect : str | None`
- `var model_config`
- `var openapi : str`
- `var paths : Dict[str,`- [PathItem](#aws_lambda_powertools.event_handler.openapi.models.PathItem)| Any] | None
- `var security : List[Dict[str, List[str]]] | None`
- `var servers : List[`- [Server](#aws_lambda_powertools.event_handler.openapi.models.Server)] | None
- `var webhooks : Dict[str,`- [PathItem](#aws_lambda_powertools.event_handler.openapi.models.PathItem)|- [Reference](#aws_lambda_powertools.event_handler.openapi.models.Reference)] | None
 
- `class OpenAPIExtensions (**data: Any)`
- 
## Expand source code`class OpenAPIExtensions(BaseModel): """ This class serves as a Pydantic proxy model to add OpenAPI extensions. OpenAPI extensions are arbitrary fields, so we remove openapi_extensions when dumping and add only the provided value in the schema. """ openapi_extensions: Optional[Dict[str, Any]] = None # If the 'openapi_extensions' field is present in the 'values' dictionary, # And if the extension starts with x- (must respect the RFC) # update the 'values' dictionary with the contents of 'openapi_extensions', # and then remove the 'openapi_extensions' field from the 'values' dictionary model_config = {"extra": "allow"} @model_validator(mode="before") def serialize_openapi_extension_v2(self): if isinstance(self, dict) and self.get("openapi_extensions"): openapi_extension_value = self.get("openapi_extensions") for extension_key in openapi_extension_value: if not str(extension_key).startswith("x-"): raise SchemaValidationError("An OpenAPI extension key must start with x-") self.update(openapi_extension_value) self.pop("openapi_extensions", None) return self`This class serves as a Pydantic proxy model to add OpenAPI extensions. OpenAPI extensions are arbitrary fields, so we remove openapi_extensions when dumping and add only the provided value in the schema. Create a new model by parsing and validating input data from keyword arguments. Raises [ `ValidationError`][pydantic_core.ValidationError] if the input data cannot be validated to form a valid model.`self`is explicitly positional-only to allow`self`as a field name.### Ancestors- pydantic.main.BaseModel
 ### Subclasses### Class variables- `var model_config`
- `var openapi_extensions : Dict[str, Any] | None`
 ### Methods- `def serialize_openapi_extension_v2(self)`
- 
## Expand source code`@model_validator(mode="before") def serialize_openapi_extension_v2(self): if isinstance(self, dict) and self.get("openapi_extensions"): openapi_extension_value = self.get("openapi_extensions") for extension_key in openapi_extension_value: if not str(extension_key).startswith("x-"): raise SchemaValidationError("An OpenAPI extension key must start with x-") self.update(openapi_extension_value) self.pop("openapi_extensions", None) return self`
 
- `class OpenIdConnect (**data: Any)`
- 
## Expand source code`class OpenIdConnect(SecurityBase): type_: SecuritySchemeType = Field( default=SecuritySchemeType.openIdConnect, alias="type", ) openIdConnectUrl: str`This class serves as a Pydantic proxy model to add OpenAPI extensions. OpenAPI extensions are arbitrary fields, so we remove openapi_extensions when dumping and add only the provided value in the schema. Create a new model by parsing and validating input data from keyword arguments. Raises [ `ValidationError`][pydantic_core.ValidationError] if the input data cannot be validated to form a valid model.`self`is explicitly positional-only to allow`self`as a field name.### Ancestors- [SecurityBase](#aws_lambda_powertools.event_handler.openapi.models.SecurityBase)
- [OpenAPIExtensions](#aws_lambda_powertools.event_handler.openapi.models.OpenAPIExtensions)
- pydantic.main.BaseModel
 ### Class variables- `var model_config`
- `var openIdConnectUrl : str`
- `var type_ :`- [SecuritySchemeType](#aws_lambda_powertools.event_handler.openapi.models.SecuritySchemeType)
 
- `class Operation (**data: Any)`
- 
## Expand source code`class Operation(OpenAPIExtensions): tags: Optional[List[str]] = None summary: Optional[str] = None description: Optional[str] = None externalDocs: Optional[ExternalDocumentation] = None operationId: Optional[str] = None parameters: Optional[List[Union[Parameter, Reference]]] = None requestBody: Optional[Union[RequestBody, Reference]] = None # Using Any for Specification Extensions responses: Optional[Dict[int, Union[Response, Any]]] = None callbacks: Optional[Dict[str, Union[Dict[str, "PathItem"], Reference]]] = None deprecated: Optional[bool] = None security: Optional[List[Dict[str, List[str]]]] = None servers: Optional[List[Server]] = None model_config = MODEL_CONFIG_ALLOW`This class serves as a Pydantic proxy model to add OpenAPI extensions. OpenAPI extensions are arbitrary fields, so we remove openapi_extensions when dumping and add only the provided value in the schema. Create a new model by parsing and validating input data from keyword arguments. Raises [ `ValidationError`][pydantic_core.ValidationError] if the input data cannot be validated to form a valid model.`self`is explicitly positional-only to allow`self`as a field name.### Ancestors- [OpenAPIExtensions](#aws_lambda_powertools.event_handler.openapi.models.OpenAPIExtensions)
- pydantic.main.BaseModel
 ### Class variables- `var callbacks : Dict[str, Dict[str,`- [PathItem](#aws_lambda_powertools.event_handler.openapi.models.PathItem)] |- [Reference](#aws_lambda_powertools.event_handler.openapi.models.Reference)] | None
- `var deprecated : bool | None`
- `var description : str | None`
- `var externalDocs :`- [ExternalDocumentation](#aws_lambda_powertools.event_handler.openapi.models.ExternalDocumentation)| None
- `var model_config`
- `var operationId : str | None`
- `var parameters : List[`- [Parameter](#aws_lambda_powertools.event_handler.openapi.models.Parameter)|- [Reference](#aws_lambda_powertools.event_handler.openapi.models.Reference)] | None
- `var requestBody :`- [RequestBody](#aws_lambda_powertools.event_handler.openapi.models.RequestBody)|- [Reference](#aws_lambda_powertools.event_handler.openapi.models.Reference)| None
- `var responses : Dict[int,`- [Response](#aws_lambda_powertools.event_handler.openapi.models.Response)| Any] | None
- `var security : List[Dict[str, List[str]]] | None`
- `var servers : List[`- [Server](#aws_lambda_powertools.event_handler.openapi.models.Server)] | None
- `var summary : str | None`
 
- `class Parameter (**data: Any)`
- 
## Expand source code`class Parameter(ParameterBase): name: str in_: ParameterInType = Field(alias="in")`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 Create a new model by parsing and validating input data from keyword arguments. Raises [ `ValidationError`][pydantic_core.ValidationError] if the input data cannot be validated to form a valid model.`self`is explicitly positional-only to allow`self`as a field name.### Ancestors- [ParameterBase](#aws_lambda_powertools.event_handler.openapi.models.ParameterBase)
- pydantic.main.BaseModel
 ### Class variables- `var in_ :`- [ParameterInType](#aws_lambda_powertools.event_handler.openapi.models.ParameterInType)
- `var model_config`
- `var name : str`
 
- `class ParameterBase (**data: Any)`
- 
## Expand source code`class ParameterBase(BaseModel): description: Optional[str] = None required: Optional[bool] = None deprecated: Optional[bool] = None # Serialization rules for simple scenarios style: Optional[str] = None explode: Optional[bool] = None allowReserved: Optional[bool] = None schema_: Optional[Union[Schema, Reference]] = Field(default=None, alias="schema") examples: Optional[Dict[str, Union[Example, Reference]]] = None # Serialization rules for more complex scenarios content: Optional[Dict[str, MediaType]] = None model_config = MODEL_CONFIG_ALLOW`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Subclasses### Class variables- `var allowReserved : bool | None`
- `var content : Dict[str,`- [MediaType](#aws_lambda_powertools.event_handler.openapi.models.MediaType)] | None
- `var deprecated : bool | None`
- `var description : str | None`
- `var examples : Dict[str,`- [Example](#aws_lambda_powertools.event_handler.openapi.models.Example)|- [Reference](#aws_lambda_powertools.event_handler.openapi.models.Reference)] | None
- `var explode : bool | None`
- `var model_config`
- `var required : bool | None`
- `var schema_ :`- [Schema](#aws_lambda_powertools.event_handler.openapi.models.Schema)|- [Reference](#aws_lambda_powertools.event_handler.openapi.models.Reference)| None
- `var style : str | None`
 
- `class ParameterInType (*args, **kwds)`
- 
## Expand source code`class ParameterInType(Enum): query = "query" header = "header" path = "path" cookie = "cookie"`Create a collection of name/value pairs. Example enumeration: `>>> class Color(Enum): ... RED = 1 ... BLUE = 2 ... GREEN = 3`Access them by: - attribute access:
 Color.RED - value lookup:
 Color(1) - name lookup:
 Color['RED'] Enumerations can be iterated over, and know how many members they have: `>>> len(Color) 3``>>> list(Color) [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]`Methods can be added to enumerations, and members can have their own attributes – see the documentation for details. ### Ancestors- enum.Enum
 ### Class variables
- `var header`
- `var path`
- `var query`
 
- `class PathItem (**data: Any)`
- 
## Expand source code`class PathItem(BaseModel): ref: Optional[str] = Field(default=None, alias="$ref") summary: Optional[str] = None description: Optional[str] = None get: Optional[Operation] = None put: Optional[Operation] = None post: Optional[Operation] = None delete: Optional[Operation] = None options: Optional[Operation] = None head: Optional[Operation] = None patch: Optional[Operation] = None trace: Optional[Operation] = None servers: Optional[List[Server]] = None parameters: Optional[List[Union[Parameter, Reference]]] = None model_config = MODEL_CONFIG_ALLOW`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables- `var delete :`- [Operation](#aws_lambda_powertools.event_handler.openapi.models.Operation)| None
- `var description : str | None`
- `var get :`- [Operation](#aws_lambda_powertools.event_handler.openapi.models.Operation)| None
- `var head :`- [Operation](#aws_lambda_powertools.event_handler.openapi.models.Operation)| None
- `var model_config`
- `var options :`- [Operation](#aws_lambda_powertools.event_handler.openapi.models.Operation)| None
- `var parameters : List[`- [Parameter](#aws_lambda_powertools.event_handler.openapi.models.Parameter)|- [Reference](#aws_lambda_powertools.event_handler.openapi.models.Reference)] | None
- `var patch :`- [Operation](#aws_lambda_powertools.event_handler.openapi.models.Operation)| None
- `var post :`- [Operation](#aws_lambda_powertools.event_handler.openapi.models.Operation)| None
- `var put :`- [Operation](#aws_lambda_powertools.event_handler.openapi.models.Operation)| None
- `var ref : str | None`
- `var servers : List[`- [Server](#aws_lambda_powertools.event_handler.openapi.models.Server)] | None
- `var summary : str | None`
- `var trace :`- [Operation](#aws_lambda_powertools.event_handler.openapi.models.Operation)| None
 
- `class Reference (**data: Any)`
- 
## Expand source code`class Reference(BaseModel): ref: str = Field(alias="$ref")`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
- `var ref : str`
 
- `class RequestBody (**data: Any)`
- 
## Expand source code`class RequestBody(BaseModel): description: Optional[str] = None content: Dict[str, MediaType] required: Optional[bool] = None model_config = MODEL_CONFIG_ALLOW`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables- `var content : Dict[str,`- [MediaType](#aws_lambda_powertools.event_handler.openapi.models.MediaType)]
- `var description : str | None`
- `var model_config`
- `var required : bool | None`
 
- `class Response (**data: Any)`
- 
## Expand source code`class Response(BaseModel): description: str headers: Optional[Dict[str, Union[Header, Reference]]] = None content: Optional[Dict[str, MediaType]] = None links: Optional[Dict[str, Union[Link, Reference]]] = None model_config = MODEL_CONFIG_ALLOW`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables
- `class Schema (**data: Any)`
- 
## Expand source code`class Schema(BaseModel): # Ref: JSON Schema 2020-12: https://json-schema.org/draft/2020-12/json-schema-core.html#name-the-json-schema-core-vocabu # Core Vocabulary schema_: Optional[str] = Field(default=None, alias="$schema") vocabulary: Optional[str] = Field(default=None, alias="$vocabulary") id: Optional[str] = Field(default=None, alias="$id") # noqa: A003 anchor: Optional[str] = Field(default=None, alias="$anchor") dynamicAnchor: Optional[str] = Field(default=None, alias="$dynamicAnchor") ref: Optional[str] = Field(default=None, alias="$ref") dynamicRef: Optional[str] = Field(default=None, alias="$dynamicRef") defs: Optional[Dict[str, "SchemaOrBool"]] = Field(default=None, alias="$defs") comment: Optional[str] = Field(default=None, alias="$comment") # Ref: JSON Schema 2020-12: https://json-schema.org/draft/2020-12/json-schema-core.html#name-a-vocabulary-for-applying-s # A Vocabulary for Applying Subschemas allOf: Optional[List["SchemaOrBool"]] = None anyOf: Optional[List["SchemaOrBool"]] = None oneOf: Optional[List["SchemaOrBool"]] = None not_: Optional["SchemaOrBool"] = Field(default=None, alias="not") if_: Optional["SchemaOrBool"] = Field(default=None, alias="if") then: Optional["SchemaOrBool"] = None else_: Optional["SchemaOrBool"] = Field(default=None, alias="else") dependentSchemas: Optional[Dict[str, "SchemaOrBool"]] = None prefixItems: Optional[List["SchemaOrBool"]] = None # MAINTENANCE: uncomment and remove below when deprecating Pydantic v1 # MAINTENANCE: It generates a list of schemas for tuples, before prefixItems was available # MAINTENANCE: items: Optional["SchemaOrBool"] = None items: Optional[Union["SchemaOrBool", List["SchemaOrBool"]]] = None contains: Optional["SchemaOrBool"] = None properties: Optional[Dict[str, "SchemaOrBool"]] = None patternProperties: Optional[Dict[str, "SchemaOrBool"]] = None additionalProperties: Optional["SchemaOrBool"] = None propertyNames: Optional["SchemaOrBool"] = None unevaluatedItems: Optional["SchemaOrBool"] = None unevaluatedProperties: Optional["SchemaOrBool"] = None # Ref: JSON Schema Validation 2020-12: https://json-schema.org/draft/2020-12/json-schema-validation.html#name-a-vocabulary-for-structural # A Vocabulary for Structural Validation type: Optional[str] = None # noqa: A003 enum: Optional[List[Any]] = None const: Optional[Any] = None multipleOf: Optional[float] = Field(default=None, gt=0) maximum: Optional[float] = None exclusiveMaximum: Optional[float] = None minimum: Optional[float] = None exclusiveMinimum: Optional[float] = None maxLength: Optional[int] = Field(default=None, ge=0) minLength: Optional[int] = Field(default=None, ge=0) pattern: Optional[str] = None maxItems: Optional[int] = Field(default=None, ge=0) minItems: Optional[int] = Field(default=None, ge=0) uniqueItems: Optional[bool] = None maxContains: Optional[int] = Field(default=None, ge=0) minContains: Optional[int] = Field(default=None, ge=0) maxProperties: Optional[int] = Field(default=None, ge=0) minProperties: Optional[int] = Field(default=None, ge=0) required: Optional[List[str]] = None dependentRequired: Optional[Dict[str, Set[str]]] = None # Ref: JSON Schema Validation 2020-12: https://json-schema.org/draft/2020-12/json-schema-validation.html#name-vocabularies-for-semantic-c # Vocabularies for Semantic Content With "format" format: Optional[str] = None # noqa: A003 # Ref: JSON Schema Validation 2020-12: https://json-schema.org/draft/2020-12/json-schema-validation.html#name-a-vocabulary-for-the-conten # A Vocabulary for the Contents of String-Encoded Data contentEncoding: Optional[str] = None contentMediaType: Optional[str] = None contentSchema: Optional["SchemaOrBool"] = None # Ref: JSON Schema Validation 2020-12: https://json-schema.org/draft/2020-12/json-schema-validation.html#name-a-vocabulary-for-basic-meta # A Vocabulary for Basic Meta-Data Annotations title: Optional[str] = None description: Optional[str] = None default: Optional[Any] = None deprecated: Optional[bool] = None readOnly: Optional[bool] = None writeOnly: Optional[bool] = None examples: Optional[List[Any]] = None # Ref: OpenAPI 3.0.0: https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.0.md#schema-object # Schema Object discriminator: Optional[Discriminator] = None xml: Optional[XML] = None externalDocs: Optional[ExternalDocumentation] = None model_config = MODEL_CONFIG_ALLOW`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables- `var additionalProperties :`- [Schema](#aws_lambda_powertools.event_handler.openapi.models.Schema)| bool | None
- `var allOf : List[`- [Schema](#aws_lambda_powertools.event_handler.openapi.models.Schema)| bool] | None
- `var anchor : str | None`
- `var anyOf : List[`- [Schema](#aws_lambda_powertools.event_handler.openapi.models.Schema)| bool] | None
- `var comment : str | None`
- `var const : Any | None`
- `var contains :`- [Schema](#aws_lambda_powertools.event_handler.openapi.models.Schema)| bool | None
- `var contentEncoding : str | None`
- `var contentMediaType : str | None`
- `var contentSchema :`- [Schema](#aws_lambda_powertools.event_handler.openapi.models.Schema)| bool | None
- `var default : Any | None`
- `var defs : Dict[str,`- [Schema](#aws_lambda_powertools.event_handler.openapi.models.Schema)| bool] | None
- `var dependentRequired : Dict[str, Set[str]] | None`
- `var dependentSchemas : Dict[str,`- [Schema](#aws_lambda_powertools.event_handler.openapi.models.Schema)| bool] | None
- `var deprecated : bool | None`
- `var description : str | None`
- `var discriminator :`- [Discriminator](#aws_lambda_powertools.event_handler.openapi.models.Discriminator)| None
- `var dynamicAnchor : str | None`
- `var dynamicRef : str | None`
- `var else_ :`- [Schema](#aws_lambda_powertools.event_handler.openapi.models.Schema)| bool | None
- `var enum : List[Any] | None`
- `var examples : List[Any] | None`
- `var exclusiveMaximum : float | None`
- `var exclusiveMinimum : float | None`
- `var externalDocs :`- [ExternalDocumentation](#aws_lambda_powertools.event_handler.openapi.models.ExternalDocumentation)| None
- `var format : str | None`
- `var id : str | None`
- `var if_ :`- [Schema](#aws_lambda_powertools.event_handler.openapi.models.Schema)| bool | None
- `var items :`- [Schema](#aws_lambda_powertools.event_handler.openapi.models.Schema)| bool | List[- [Schema](#aws_lambda_powertools.event_handler.openapi.models.Schema)| bool] | None
- `var maxContains : int | None`
- `var maxItems : int | None`
- `var maxLength : int | None`
- `var maxProperties : int | None`
- `var maximum : float | None`
- `var minContains : int | None`
- `var minItems : int | None`
- `var minLength : int | None`
- `var minProperties : int | None`
- `var minimum : float | None`
- `var model_config`
- `var multipleOf : float | None`
- `var not_ :`- [Schema](#aws_lambda_powertools.event_handler.openapi.models.Schema)| bool | None
- `var oneOf : List[`- [Schema](#aws_lambda_powertools.event_handler.openapi.models.Schema)| bool] | None
- `var pattern : str | None`
- `var patternProperties : Dict[str,`- [Schema](#aws_lambda_powertools.event_handler.openapi.models.Schema)| bool] | None
- `var prefixItems : List[`- [Schema](#aws_lambda_powertools.event_handler.openapi.models.Schema)| bool] | None
- `var properties : Dict[str,`- [Schema](#aws_lambda_powertools.event_handler.openapi.models.Schema)| bool] | None
- `var propertyNames :`- [Schema](#aws_lambda_powertools.event_handler.openapi.models.Schema)| bool | None
- `var readOnly : bool | None`
- `var ref : str | None`
- `var required : List[str] | None`
- `var schema_ : str | None`
- `var then :`- [Schema](#aws_lambda_powertools.event_handler.openapi.models.Schema)| bool | None
- `var title : str | None`
- `var type : str | None`
- `var unevaluatedItems :`- [Schema](#aws_lambda_powertools.event_handler.openapi.models.Schema)| bool | None
- `var unevaluatedProperties :`- [Schema](#aws_lambda_powertools.event_handler.openapi.models.Schema)| bool | None
- `var uniqueItems : bool | None`
- `var vocabulary : str | None`
- `var writeOnly : bool | None`
- `var xml :`- [XML](#aws_lambda_powertools.event_handler.openapi.models.XML)| None
 
- `class SecurityBase (**data: Any)`
- 
## Expand source code`class SecurityBase(OpenAPIExtensions): type_: SecuritySchemeType = Field(alias="type") description: Optional[str] = None model_config = {"extra": "allow", "populate_by_name": True}`This class serves as a Pydantic proxy model to add OpenAPI extensions. OpenAPI extensions are arbitrary fields, so we remove openapi_extensions when dumping and add only the provided value in the schema. Create a new model by parsing and validating input data from keyword arguments. Raises [ `ValidationError`][pydantic_core.ValidationError] if the input data cannot be validated to form a valid model.`self`is explicitly positional-only to allow`self`as a field name.### Ancestors- [OpenAPIExtensions](#aws_lambda_powertools.event_handler.openapi.models.OpenAPIExtensions)
- pydantic.main.BaseModel
 ### Subclasses### Class variables- `var description : str | None`
- `var model_config`
- `var type_ :`- [SecuritySchemeType](#aws_lambda_powertools.event_handler.openapi.models.SecuritySchemeType)
 
- `class SecuritySchemeType (*args, **kwds)`
- 
## Expand source code`class SecuritySchemeType(Enum): apiKey = "apiKey" http = "http" oauth2 = "oauth2" openIdConnect = "openIdConnect" mutualTLS = "mutualTLS"`Create a collection of name/value pairs. Example enumeration: `>>> class Color(Enum): ... RED = 1 ... BLUE = 2 ... GREEN = 3`Access them by: - attribute access:
 Color.RED - value lookup:
 Color(1) - name lookup:
 Color['RED'] Enumerations can be iterated over, and know how many members they have: `>>> len(Color) 3``>>> list(Color) [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]`Methods can be added to enumerations, and members can have their own attributes – see the documentation for details. ### Ancestors- enum.Enum
 ### Class variables- `var apiKey`
- `var http`
- `var mutualTLS`
- `var oauth2`
- `var openIdConnect`
 
- `class Server (**data: Any)`
- 
## Expand source code`class Server(OpenAPIExtensions): url: Union[AnyUrl, str] description: Optional[str] = None variables: Optional[Dict[str, ServerVariable]] = None model_config = MODEL_CONFIG_ALLOW`This class serves as a Pydantic proxy model to add OpenAPI extensions. OpenAPI extensions are arbitrary fields, so we remove openapi_extensions when dumping and add only the provided value in the schema. Create a new model by parsing and validating input data from keyword arguments. Raises [ `ValidationError`][pydantic_core.ValidationError] if the input data cannot be validated to form a valid model.`self`is explicitly positional-only to allow`self`as a field name.### Ancestors- [OpenAPIExtensions](#aws_lambda_powertools.event_handler.openapi.models.OpenAPIExtensions)
- pydantic.main.BaseModel
 ### Class variables- `var description : str | None`
- `var model_config`
- `var url : pydantic.networks.AnyUrl | str`
- `var variables : Dict[str,`- [ServerVariable](#aws_lambda_powertools.event_handler.openapi.models.ServerVariable)] | None
 
- `class ServerVariable (**data: Any)`
- 
## Expand source code`class ServerVariable(BaseModel): enum: Annotated[Optional[List[str]], Field(min_length=1)] = None default: str description: Optional[str] = None model_config = MODEL_CONFIG_ALLOW`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables- `var default : str`
- `var description : str | None`
- `var enum : List[str] | None`
- `var model_config`
 
- `class Tag (**data: Any)`
- 
## Expand source code`class Tag(BaseModel): name: str description: Optional[str] = None externalDocs: Optional[ExternalDocumentation] = None model_config = MODEL_CONFIG_ALLOW`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables- `var description : str | None`
- `var externalDocs :`- [ExternalDocumentation](#aws_lambda_powertools.event_handler.openapi.models.ExternalDocumentation)| None
- `var model_config`
- `var name : str`
 
- `class XML (**data: Any)`
- 
## Expand source code`class XML(BaseModel): name: Optional[str] = None namespace: Optional[str] = None prefix: Optional[str] = None attribute: Optional[bool] = None wrapped: Optional[bool] = None model_config = MODEL_CONFIG_ALLOW`Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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
 ### Class variables- `var attribute : bool | None`
- `var model_config`
- `var name : str | None`
- `var namespace : str | None`
- `var prefix : str | None`
- `var wrapped : bool | None`