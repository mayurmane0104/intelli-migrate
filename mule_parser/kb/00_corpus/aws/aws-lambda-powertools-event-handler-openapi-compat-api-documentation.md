# aws_lambda_powertools.event_handler.openapi.compat API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/event_handler/openapi/compat.html](https://docs.aws.amazon.com/powertools/python/latest/api/event_handler/openapi/compat.html)

---

# Module `aws_lambda_powertools.event_handler.openapi.compat`

## Functions

- `def copy_field_info(*, field_info: FieldInfo, annotation: Any) ‑> pydantic.fields.FieldInfo`
- 
## Expand source code`def copy_field_info(*, field_info: FieldInfo, annotation: Any) -> FieldInfo: return type(field_info).from_annotation(annotation)`
- `def create_body_model(*,`
 fields: Sequence[- [ModelField](#aws_lambda_powertools.event_handler.openapi.compat.ModelField)],
 model_name: str) ‑> type[pydantic.main.BaseModel]
- 
## Expand source code`def create_body_model(*, fields: Sequence[ModelField], model_name: str) -> type[BaseModel]: field_params = {f.name: (f.field_info.annotation, f.field_info) for f in fields} model: type[BaseModel] = create_model(model_name, **field_params) return model`
- `def field_annotation_is_complex(annotation: type[Any] | None) ‑> bool`
- 
## Expand source code`def field_annotation_is_complex(annotation: type[Any] | None) -> bool: origin = get_origin(annotation) if origin is Union or origin is UnionType: return any(field_annotation_is_complex(arg) for arg in get_args(annotation)) return ( _annotation_is_complex(annotation) or _annotation_is_complex(origin) or hasattr(origin, "__pydantic_core_schema__") or hasattr(origin, "__get_pydantic_core_schema__") )`
- `def field_annotation_is_scalar(annotation: Any) ‑> bool`
- 
## Expand source code`def field_annotation_is_scalar(annotation: Any) -> bool: return annotation is Ellipsis or not field_annotation_is_complex(annotation)`
- `def field_annotation_is_scalar_sequence(annotation: type[Any] | None) ‑> bool`
- 
## Expand source code`def field_annotation_is_scalar_sequence(annotation: type[Any] | None) -> bool: origin = get_origin(annotation) if origin is Union or origin is UnionType: at_least_one_scalar_sequence = False for arg in get_args(annotation): if field_annotation_is_scalar_sequence(arg): at_least_one_scalar_sequence = True continue elif not field_annotation_is_scalar(arg): return False return at_least_one_scalar_sequence return field_annotation_is_sequence(annotation) and all( field_annotation_is_scalar(sub_annotation) for sub_annotation in get_args(annotation) )`
- `def field_annotation_is_sequence(annotation: type[Any] | None) ‑> bool`
- 
## Expand source code`def field_annotation_is_sequence(annotation: type[Any] | None) -> bool: return _annotation_is_sequence(annotation) or _annotation_is_sequence(get_origin(annotation))`
- `def get_annotation_from_field_info(annotation: Any, field_info: FieldInfo, field_name: str) ‑> Any`
- 
## Expand source code`def get_annotation_from_field_info(annotation: Any, field_info: FieldInfo, field_name: str) -> Any: return annotation`
- `def get_compat_model_name_map(fields: list[`- [ModelField](#aws_lambda_powertools.event_handler.openapi.compat.ModelField)]) ‑> ModelNameMap
- 
## Expand source code`def get_compat_model_name_map(fields: list[ModelField]) -> ModelNameMap: return {}`
- `def get_definitions(*,`
 fields: list[- [ModelField](#aws_lambda_powertools.event_handler.openapi.compat.ModelField)],
 schema_generator: GenerateJsonSchema,
 model_name_map: ModelNameMap) ‑> tuple[dict[tuple[- [ModelField](#aws_lambda_powertools.event_handler.openapi.compat.ModelField), Literal['validation', 'serialization']], dict[str, Any]], dict[str, dict[str, Any]]]
- 
## Expand source code`def get_definitions( *, fields: list[ModelField], schema_generator: GenerateJsonSchema, model_name_map: ModelNameMap, ) -> tuple[ dict[ tuple[ModelField, Literal["validation", "serialization"]], dict[str, Any], ], dict[str, dict[str, Any]], ]: inputs = [(field, field.mode, field._type_adapter.core_schema) for field in fields] field_mapping, definitions = schema_generator.generate_definitions(inputs=inputs) return field_mapping, definitions`
- `def get_missing_field_error(loc: tuple[str, ...]) ‑> dict[str, typing.Any]`
- 
## Expand source code`def get_missing_field_error(loc: tuple[str, ...]) -> dict[str, Any]: error = ValidationError.from_exception_data( "Field required", [{"type": "missing", "loc": loc, "input": {}}] ).errors()[0] error["input"] = None return error`
- `def get_schema_from_model_field(*,`
 field:- [ModelField](#aws_lambda_powertools.event_handler.openapi.compat.ModelField),
 model_name_map: ModelNameMap,
 field_mapping: "dict[tuple[- [ModelField](#aws_lambda_powertools.event_handler.openapi.compat.ModelField), Literal['validation', 'serialization']], JsonSchemaValue]") ‑> dict[str, Any]
- 
## Expand source code`def get_schema_from_model_field( *, field: ModelField, model_name_map: ModelNameMap, field_mapping: dict[ tuple[ModelField, Literal["validation", "serialization"]], JsonSchemaValue, ], ) -> dict[str, Any]: json_schema = field_mapping[(field, field.mode)] if "$ref" not in json_schema: # MAINTENANCE: remove when deprecating Pydantic v1 # Ref: https://github.com/pydantic/pydantic/blob/d61792cc42c80b13b23e3ffa74bc37ec7c77f7d1/pydantic/schema.py#L207 json_schema["title"] = field.field_info.title or field.alias.title().replace("_", " ") return json_schema`
- `def is_bytes_field(field:`- [ModelField](#aws_lambda_powertools.event_handler.openapi.compat.ModelField)) ‑> bool
- 
## Expand source code`def is_bytes_field(field: ModelField) -> bool: return is_bytes_or_nonable_bytes_annotation(field.type_)`
- `def is_bytes_or_nonable_bytes_annotation(annotation: Any) ‑> bool`
- 
## Expand source code`def is_bytes_or_nonable_bytes_annotation(annotation: Any) -> bool: if lenient_issubclass(annotation, bytes): return True origin = get_origin(annotation) if origin is Union or origin is UnionType: for arg in get_args(annotation): if lenient_issubclass(arg, bytes): return True return False`
- `def is_bytes_sequence_annotation(annotation: Any) ‑> bool`
- 
## Expand source code`def is_bytes_sequence_annotation(annotation: Any) -> bool: origin = get_origin(annotation) if origin is Union or origin is UnionType: at_least_one = False for arg in get_args(annotation): if is_bytes_sequence_annotation(arg): at_least_one = True break return at_least_one return field_annotation_is_sequence(annotation) and all( is_bytes_or_nonable_bytes_annotation(sub_annotation) for sub_annotation in get_args(annotation) )`
- `def is_bytes_sequence_field(field:`- [ModelField](#aws_lambda_powertools.event_handler.openapi.compat.ModelField)) ‑> bool
- 
## Expand source code`def is_bytes_sequence_field(field: ModelField) -> bool: return is_bytes_sequence_annotation(field.type_)`
- `def is_scalar_field(field:`- [ModelField](#aws_lambda_powertools.event_handler.openapi.compat.ModelField)) ‑> bool
- 
## Expand source code`def is_scalar_field(field: ModelField) -> bool: from aws_lambda_powertools.event_handler.openapi.params import Body return field_annotation_is_scalar(field.field_info.annotation) and not isinstance(field.field_info, Body)`
- `def is_scalar_sequence_field(field:`- [ModelField](#aws_lambda_powertools.event_handler.openapi.compat.ModelField)) ‑> bool
- 
## Expand source code`def is_scalar_sequence_field(field: ModelField) -> bool: return field_annotation_is_scalar_sequence(field.field_info.annotation)`
- `def is_sequence_field(field:`- [ModelField](#aws_lambda_powertools.event_handler.openapi.compat.ModelField)) ‑> bool
- 
## Expand source code`def is_sequence_field(field: ModelField) -> bool: return field_annotation_is_sequence(field.field_info.annotation)`
- `def model_json(model: BaseModel, **kwargs: Any) ‑> Any`
- 
## Expand source code`def model_json(model: BaseModel, **kwargs: Any) -> Any: return model.model_dump_json(**kwargs)`
- `def model_rebuild(model: type[BaseModel]) ‑> None`
- 
## Expand source code`def model_rebuild(model: type[BaseModel]) -> None: model.model_rebuild()`
- `def serialize_sequence_value(*,`
 field:- [ModelField](#aws_lambda_powertools.event_handler.openapi.compat.ModelField),
 value: Any) ‑> Sequence[Any]
- 
## Expand source code`def serialize_sequence_value(*, field: ModelField, value: Any) -> Sequence[Any]: origin_type = get_origin(field.field_info.annotation) or field.field_info.annotation if not issubclass(origin_type, sequence_types): # type: ignore[arg-type] raise AssertionError(f"Expected sequence type, got {origin_type}") return sequence_annotation_to_type[origin_type](value) # type: ignore[no-any-return]`
- `def value_is_sequence(value: Any) ‑> bool`
- 
## Expand source code`def value_is_sequence(value: Any) -> bool: return isinstance(value, sequence_types) and not isinstance(value, (str, bytes)) # type: ignore[arg-type]`

## Classes

- `class ErrorWrapper (*args, **kwargs)`
- 
## Expand source code`class ErrorWrapper(Exception): pass`Common base class for all non-exit exceptions. ### Ancestors- builtins.Exception
- builtins.BaseException
 
- `class ModelField (field_info: FieldInfo,`
 name: str,
 mode: "Literal['validation', 'serialization']" = 'validation')
- 
## Expand source code`@dataclass class ModelField: field_info: FieldInfo name: str mode: Literal["validation", "serialization"] = "validation" @property def alias(self) -> str: value = self.field_info.alias return value if value is not None else self.name @property def required(self) -> bool: return self.field_info.is_required() @property def default(self) -> Any: return self.get_default() @property def type_(self) -> Any: return self.field_info.annotation def __post_init__(self) -> None: self._type_adapter: TypeAdapter[Any] = TypeAdapter( Annotated[self.field_info.annotation, self.field_info], ) def get_default(self) -> Any: if self.field_info.is_required(): return Undefined return self.field_info.get_default(call_default_factory=True) def serialize( self, value: Any, *, mode: Literal["json", "python"] = "json", include: IncEx | None = None, exclude: IncEx | None = None, by_alias: bool = True, exclude_unset: bool = False, exclude_defaults: bool = False, exclude_none: bool = False, ) -> Any: return self._type_adapter.dump_python( value, mode=mode, include=include, exclude=exclude, by_alias=by_alias, exclude_unset=exclude_unset, exclude_defaults=exclude_defaults, exclude_none=exclude_none, ) def validate( self, value: Any, values: dict[str, Any] = {}, *, loc: tuple[int | str, ...] = () ) -> tuple[Any, list[dict[str, Any]] | None]: try: return (self._type_adapter.validate_python(value, from_attributes=True), None) except ValidationError as exc: return None, _regenerate_error_with_loc(errors=exc.errors(), loc_prefix=loc) def __hash__(self) -> int: # Each ModelField is unique for our purposes return id(self)`ModelField(field_info: 'FieldInfo', name: 'str', mode: "Literal['validation', 'serialization']" = 'validation') ### Class variables- `var field_info : pydantic.fields.FieldInfo`
- `var mode : Literal['validation', 'serialization']`
- `var name : str`
 ### Instance variables- `prop alias : str`
- 
## Expand source code`@property def alias(self) -> str: value = self.field_info.alias return value if value is not None else self.name`
- `prop default : Any`
- 
## Expand source code`@property def default(self) -> Any: return self.get_default()`
- `prop required : bool`
- 
## Expand source code`@property def required(self) -> bool: return self.field_info.is_required()`
- `prop type_ : Any`
- 
## Expand source code`@property def type_(self) -> Any: return self.field_info.annotation`
 ### Methods- `def get_default(self) ‑> Any`
- 
## Expand source code`def get_default(self) -> Any: if self.field_info.is_required(): return Undefined return self.field_info.get_default(call_default_factory=True)`
- `def serialize(self,`
 value: Any,
 *,
 mode: "Literal['json', 'python']" = 'json',
 include: IncEx | None = None,
 exclude: IncEx | None = None,
 by_alias: bool = True,
 exclude_unset: bool = False,
 exclude_defaults: bool = False,
 exclude_none: bool = False) ‑> Any
- 
## Expand source code`def serialize( self, value: Any, *, mode: Literal["json", "python"] = "json", include: IncEx | None = None, exclude: IncEx | None = None, by_alias: bool = True, exclude_unset: bool = False, exclude_defaults: bool = False, exclude_none: bool = False, ) -> Any: return self._type_adapter.dump_python( value, mode=mode, include=include, exclude=exclude, by_alias=by_alias, exclude_unset=exclude_unset, exclude_defaults=exclude_defaults, exclude_none=exclude_none, )`
- `def validate(self, value: Any, values: dict[str, Any] = {}, *, loc: tuple[int | str, ...] = ()) ‑> tuple[typing.Any, list[dict[str, typing.Any]] | None]`
- 
## Expand source code`def validate( self, value: Any, values: dict[str, Any] = {}, *, loc: tuple[int | str, ...] = () ) -> tuple[Any, list[dict[str, Any]] | None]: try: return (self._type_adapter.validate_python(value, from_attributes=True), None) except ValidationError as exc: return None, _regenerate_error_with_loc(errors=exc.errors(), loc_prefix=loc)`
 
- `class RequestErrorModel (**data: Any)`
- 
Usage docs: [https://docs.pydantic.dev/2.10/concepts/models/](https://docs.pydantic.dev/2.10/concepts/models/)A base class for creating Pydantic models. ## Attributes- `__class_vars__`
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