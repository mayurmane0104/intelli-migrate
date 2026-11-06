# aws_lambda_powertools.utilities.validation API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/validation/index.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/validation/index.html)

---

# Module `aws_lambda_powertools.utilities.validation`

Simple validator to enforce incoming/outgoing event conforms with JSON Schema

## Sub-modules

## Functions

- `def validate(event: Any,`
 schema: dict,
 formats: dict | None = None,
 handlers: dict | None = None,
 provider_options: dict | None = None,
 envelope: str | None = None,
 jmespath_options: dict | None = None) ‑> Any
- 
## Expand source code`def validate( event: Any, schema: dict, formats: dict | None = None, handlers: dict | None = None, provider_options: dict | None = None, envelope: str | None = None, jmespath_options: dict | None = None, ) -> Any: """Standalone function to validate event data using a JSON Schema Typically used when you need more control over the validation process. Parameters ---------- event : dict Lambda event to be validated schema : dict JSON Schema to validate incoming event envelope : dict JMESPath expression to filter data against jmespath_options : dict Alternative JMESPath options to be included when filtering expr formats: dict Custom formats containing a key (e.g. int64) and a value expressed as regex or callback returning bool handlers: Dict Custom methods to retrieve remote schemes, keyed off of URI scheme provider_options: Dict Arguments that will be passed directly to the underlying validate call Example ------- **Validate event** from aws_lambda_powertools.utilities.validation import validate def handler(event, context): validate(event=event, schema=json_schema_dict) return event **Unwrap event before validating against actual payload - using built-in envelopes** from aws_lambda_powertools.utilities.validation import validate, envelopes def handler(event, context): validate(event=event, schema=json_schema_dict, envelope=envelopes.API_GATEWAY_REST) return event **Unwrap event before validating against actual payload - using custom JMESPath expression** from aws_lambda_powertools.utilities.validation import validate def handler(event, context): validate(event=event, schema=json_schema_dict, envelope="payload[*].my_data") return event **Unwrap and deserialize JSON string event before validating against actual payload - using built-in functions** from aws_lambda_powertools.utilities.validation import validate def handler(event, context): validate(event=event, schema=json_schema_dict, envelope="Records[*].powertools_json(body)") return event **Unwrap, decode base64 and deserialize JSON string event before validating against actual payload - using built-in functions** from aws_lambda_powertools.utilities.validation import validate def handler(event, context): validate(event=event, schema=json_schema_dict, envelope="Records[*].kinesis.powertools_json(powertools_base64(data))") return event **Unwrap, decompress ZIP archive and deserialize JSON string event before validating against actual payload - using built-in functions** from aws_lambda_powertools.utilities.validation import validate def handler(event, context): validate(event=event, schema=json_schema_dict, envelope="awslogs.powertools_base64_gzip(data) | powertools_json(@).logEvents[*]") return event Returns ------- Dict The validated event. If the schema specifies a `default` value for fields that are omitted, those default values will be included in the response. Raises ------ SchemaValidationError When schema validation fails against data set InvalidSchemaFormatError When JSON schema provided is invalid InvalidEnvelopeExpressionError When JMESPath expression to unwrap event is invalid """ # noqa: E501 if envelope: event = jmespath_utils.query( data=event, envelope=envelope, jmespath_options=jmespath_options, ) return validate_data_against_schema( data=event, schema=schema, formats=formats, handlers=handlers, provider_options=provider_options, )`Standalone function to validate event data using a JSON Schema Typically used when you need more control over the validation process. ## Parameters- `event`- `dict`
- Lambda event to be validated
- `schema`- `dict`
- JSON Schema to validate incoming event
- `envelope`- `dict`
- JMESPath expression to filter data against
- `jmespath_options`- `dict`
- Alternative JMESPath options to be included when filtering expr
- `formats`- `dict`
- Custom formats containing a key (e.g. int64) and a value expressed as regex or callback returning bool
- `handlers`- `Dict`
- Custom methods to retrieve remote schemes, keyed off of URI scheme
- `provider_options`- `Dict`
- Arguments that will be passed directly to the underlying validate call
 ## Example**Validate event**`from aws_lambda_powertools.utilities.validation import validate def handler(event, context): validate(event=event, schema=json_schema_dict) return event`**Unwrap event before validating against actual payload - using built-in envelopes**`from aws_lambda_powertools.utilities.validation import validate, envelopes def handler(event, context): validate(event=event, schema=json_schema_dict, envelope=envelopes.API_GATEWAY_REST) return event`**Unwrap event before validating against actual payload - using custom JMESPath expression**`from aws_lambda_powertools.utilities.validation import validate def handler(event, context): validate(event=event, schema=json_schema_dict, envelope="payload[*].my_data") return event`**Unwrap and deserialize JSON string event before validating against actual payload - using built-in functions**`from aws_lambda_powertools.utilities.validation import validate def handler(event, context): validate(event=event, schema=json_schema_dict, envelope="Records[*].powertools_json(body)") return event`**Unwrap, decode base64 and deserialize JSON string event before validating against actual payload - using built-in functions**`from aws_lambda_powertools.utilities.validation import validate def handler(event, context): validate(event=event, schema=json_schema_dict, envelope="Records[*].kinesis.powertools_json(powertools_base64(data))") return event`**Unwrap, decompress ZIP archive and deserialize JSON string event before validating against actual payload - using built-in functions**`from aws_lambda_powertools.utilities.validation import validate def handler(event, context): validate(event=event, schema=json_schema_dict, envelope="awslogs.powertools_base64_gzip(data) | powertools_json(@).logEvents[*]") return event`## Returns- `Dict`
- The validated event. If the schema specifies a `default`value for fields that are omitted, those default values will be included in the response.
 ## Raises- [SchemaValidationError](#aws_lambda_powertools.utilities.validation.SchemaValidationError)
- When schema validation fails against data set
- [InvalidSchemaFormatError](#aws_lambda_powertools.utilities.validation.InvalidSchemaFormatError)
- When JSON schema provided is invalid
- [InvalidEnvelopeExpressionError](#aws_lambda_powertools.utilities.validation.InvalidEnvelopeExpressionError)
- When JMESPath expression to unwrap event is invalid
 
- `def validator(handler: Callable,`
 event: dict | str,
 context: Any,
 inbound_schema: dict | None = None,
 inbound_formats: dict | None = None,
 inbound_handlers: dict | None = None,
 inbound_provider_options: dict | None = None,
 outbound_schema: dict | None = None,
 outbound_formats: dict | None = None,
 outbound_handlers: dict | None = None,
 outbound_provider_options: dict | None = None,
 envelope: str = '',
 jmespath_options: dict | None = None,
 **kwargs: Any) ‑> Any
- 
## Expand source code`@lambda_handler_decorator def validator( handler: Callable, event: dict | str, context: Any, inbound_schema: dict | None = None, inbound_formats: dict | None = None, inbound_handlers: dict | None = None, inbound_provider_options: dict | None = None, outbound_schema: dict | None = None, outbound_formats: dict | None = None, outbound_handlers: dict | None = None, outbound_provider_options: dict | None = None, envelope: str = "", jmespath_options: dict | None = None, **kwargs: Any, ) -> Any: """Lambda handler decorator to validate incoming/outbound data using a JSON Schema Parameters ---------- handler : Callable Method to annotate on event : dict Lambda event to be validated context : Any Lambda context object inbound_schema : dict JSON Schema to validate incoming event outbound_schema : dict JSON Schema to validate outbound event envelope : dict JMESPath expression to filter data against jmespath_options : dict Alternative JMESPath options to be included when filtering expr inbound_formats: dict Custom formats containing a key (e.g. int64) and a value expressed as regex or callback returning bool outbound_formats: dict Custom formats containing a key (e.g. int64) and a value expressed as regex or callback returning bool inbound_handlers: Dict Custom methods to retrieve remote schemes, keyed off of URI scheme outbound_handlers: Dict Custom methods to retrieve remote schemes, keyed off of URI scheme inbound_provider_options: Dict Arguments that will be passed directly to the underlying validation call, in this case fastjsonchema.validate. For all supported arguments see: https://horejsek.github.io/python-fastjsonschema/#fastjsonschema.validate outbound_provider_options: Dict Arguments that will be passed directly to the underlying validation call, in this case fastjsonchema.validate. For all supported arguments see: https://horejsek.github.io/python-fastjsonschema/#fastjsonschema.validate Example ------- **Validate incoming event** from aws_lambda_powertools.utilities.validation import validator @validator(inbound_schema=json_schema_dict) def handler(event, context): return event **Validate incoming and outgoing event** from aws_lambda_powertools.utilities.validation import validator @validator(inbound_schema=json_schema_dict, outbound_schema=response_json_schema_dict) def handler(event, context): return event **Unwrap event before validating against actual payload - using built-in envelopes** from aws_lambda_powertools.utilities.validation import validator, envelopes @validator(inbound_schema=json_schema_dict, envelope=envelopes.API_GATEWAY_REST) def handler(event, context): return event **Unwrap event before validating against actual payload - using custom JMESPath expression** from aws_lambda_powertools.utilities.validation import validator @validator(inbound_schema=json_schema_dict, envelope="payload[*].my_data") def handler(event, context): return event **Unwrap and deserialize JSON string event before validating against actual payload - using built-in functions** from aws_lambda_powertools.utilities.validation import validator @validator(inbound_schema=json_schema_dict, envelope="Records[*].powertools_json(body)") def handler(event, context): return event **Unwrap, decode base64 and deserialize JSON string event before validating against actual payload - using built-in functions** from aws_lambda_powertools.utilities.validation import validator @validator(inbound_schema=json_schema_dict, envelope="Records[*].kinesis.powertools_json(powertools_base64(data))") def handler(event, context): return event **Unwrap, decompress ZIP archive and deserialize JSON string event before validating against actual payload - using built-in functions** from aws_lambda_powertools.utilities.validation import validator @validator(inbound_schema=json_schema_dict, envelope="awslogs.powertools_base64_gzip(data) | powertools_json(@).logEvents[*]") def handler(event, context): return event Returns ------- Any Lambda handler response Raises ------ SchemaValidationError When schema validation fails against data set InvalidSchemaFormatError When JSON schema provided is invalid InvalidEnvelopeExpressionError When JMESPath expression to unwrap event is invalid """ # noqa: E501 if envelope: event = jmespath_utils.query( data=event, envelope=envelope, jmespath_options=jmespath_options, ) if inbound_schema: logger.debug("Validating inbound event") validate_data_against_schema( data=event, schema=inbound_schema, formats=inbound_formats, handlers=inbound_handlers, provider_options=inbound_provider_options, ) response = handler(event, context, **kwargs) if outbound_schema: logger.debug("Validating outbound event") validate_data_against_schema( data=response, schema=outbound_schema, formats=outbound_formats, handlers=outbound_handlers, provider_options=outbound_provider_options, ) return response`Lambda handler decorator to validate incoming/outbound data using a JSON Schema ## Parameters- `handler`- `Callable`
- Method to annotate on
- `event`- `dict`
- Lambda event to be validated
- `context`- `Any`
- Lambda context object
- `inbound_schema`- `dict`
- JSON Schema to validate incoming event
- `outbound_schema`- `dict`
- JSON Schema to validate outbound event
- `envelope`- `dict`
- JMESPath expression to filter data against
- `jmespath_options`- `dict`
- Alternative JMESPath options to be included when filtering expr
- `inbound_formats`- `dict`
- Custom formats containing a key (e.g. int64) and a value expressed as regex or callback returning bool
- `outbound_formats`- `dict`
- Custom formats containing a key (e.g. int64) and a value expressed as regex or callback returning bool
- `inbound_handlers`- `Dict`
- Custom methods to retrieve remote schemes, keyed off of URI scheme
- `outbound_handlers`- `Dict`
- Custom methods to retrieve remote schemes, keyed off of URI scheme
- `inbound_provider_options`- `Dict`
- Arguments that will be passed directly to the underlying validation call, in this case fastjsonchema.validate.
For all supported arguments see: [https://horejsek.github.io/python-fastjsonschema/#fastjsonschema.validate](https://horejsek.github.io/python-fastjsonschema/#fastjsonschema.validate)
- `outbound_provider_options`- `Dict`
- Arguments that will be passed directly to the underlying validation call, in this case fastjsonchema.validate.
For all supported arguments see: [https://horejsek.github.io/python-fastjsonschema/#fastjsonschema.validate](https://horejsek.github.io/python-fastjsonschema/#fastjsonschema.validate)
 ## Example**Validate incoming event**`from aws_lambda_powertools.utilities.validation import validator @validator(inbound_schema=json_schema_dict) def handler(event, context): return event`**Validate incoming and outgoing event**`from aws_lambda_powertools.utilities.validation import validator @validator(inbound_schema=json_schema_dict, outbound_schema=response_json_schema_dict) def handler(event, context): return event`**Unwrap event before validating against actual payload - using built-in envelopes**`from aws_lambda_powertools.utilities.validation import validator, envelopes @validator(inbound_schema=json_schema_dict, envelope=envelopes.API_GATEWAY_REST) def handler(event, context): return event`**Unwrap event before validating against actual payload - using custom JMESPath expression**`from aws_lambda_powertools.utilities.validation import validator @validator(inbound_schema=json_schema_dict, envelope="payload[*].my_data") def handler(event, context): return event`**Unwrap and deserialize JSON string event before validating against actual payload - using built-in functions**`from aws_lambda_powertools.utilities.validation import validator @validator(inbound_schema=json_schema_dict, envelope="Records[*].powertools_json(body)") def handler(event, context): return event`**Unwrap, decode base64 and deserialize JSON string event before validating against actual payload - using built-in functions**`from aws_lambda_powertools.utilities.validation import validator @validator(inbound_schema=json_schema_dict, envelope="Records[*].kinesis.powertools_json(powertools_base64(data))") def handler(event, context): return event`**Unwrap, decompress ZIP archive and deserialize JSON string event before validating against actual payload - using built-in functions**`from aws_lambda_powertools.utilities.validation import validator @validator(inbound_schema=json_schema_dict, envelope="awslogs.powertools_base64_gzip(data) | powertools_json(@).logEvents[*]") def handler(event, context): return event`## Returns- `Any`
- Lambda handler response
 ## Raises- [SchemaValidationError](#aws_lambda_powertools.utilities.validation.SchemaValidationError)
- When schema validation fails against data set
- [InvalidSchemaFormatError](#aws_lambda_powertools.utilities.validation.InvalidSchemaFormatError)
- When JSON schema provided is invalid
- [InvalidEnvelopeExpressionError](#aws_lambda_powertools.utilities.validation.InvalidEnvelopeExpressionError)
- When JMESPath expression to unwrap event is invalid
 

## Classes

- `class InvalidEnvelopeExpressionError (*args, **kwargs)`
- 
## Expand source code`class InvalidEnvelopeExpressionError(Exception): """When JMESPath fails to parse expression"""`When JMESPath fails to parse expression ### Ancestors- builtins.Exception
- builtins.BaseException
 
- `class InvalidSchemaFormatError (*args, **kwargs)`
- 
## Expand source code`class InvalidSchemaFormatError(Exception): """When JSON Schema is in invalid format"""`When JSON Schema is in invalid format ### Ancestors- builtins.Exception
- builtins.BaseException
 
- `class SchemaValidationError (message: str | None = None,`
 validation_message: str | None = None,
 name: str | None = None,
 path: list | None = None,
 value: Any | None = None,
 definition: Any | None = None,
 rule: str | None = None,
 rule_definition: Any | None = None)
- 
## Expand source code`class SchemaValidationError(Exception): """When serialization fail schema validation""" def __init__( self, message: str | None = None, validation_message: str | None = None, name: str | None = None, path: list | None = None, value: Any | None = None, definition: Any | None = None, rule: str | None = None, rule_definition: Any | None = None, ): """ Parameters ---------- message : str, optional Powertools for AWS Lambda (Python) formatted error message validation_message : str, optional Containing human-readable information what is wrong (e.g. `data.property[index] must be smaller than or equal to 42`) name : str, optional name of a path in the data structure (e.g. `data.property[index]`) path: list, optional `path` as an array in the data structure (e.g. `['data', 'property', 'index']`), value : Any, optional The invalid value definition : Any, optional The full rule `definition` (e.g. `42`) rule : str, optional `rule` which the `data` is breaking (e.g. `maximum`) rule_definition : Any, optional The specific rule `definition` (e.g. `42`) """ super().__init__(message) self.message = message self.validation_message = validation_message self.name = name self.path = path self.value = value self.definition = definition self.rule = rule self.rule_definition = rule_definition`When serialization fail schema validation ## Parameters- `message`- `str`, optional
- Powertools for AWS Lambda (Python) formatted error message
- `validation_message`- `str`, optional
- Containing human-readable information what is wrong
(e.g. `data.property[index] must be smaller than or equal to 42`)
- `name`- `str`, optional
- name of a path in the data structure
(e.g. `data.property[index]`)
- `path`- `list`, optional
- `path`as an array in the data structure (e.g.- `['data', 'property', 'index']`),
- `value`- `Any`, optional
- The invalid value
- `definition`- `Any`, optional
- The full rule `definition`(e.g.`42`)
- `rule`- `str`, optional
- `rule`which the- `data`is breaking (e.g.- `maximum`)
- `rule_definition`- `Any`, optional
- The specific rule `definition`(e.g.`42`)
 ### Ancestors- builtins.Exception
- builtins.BaseException