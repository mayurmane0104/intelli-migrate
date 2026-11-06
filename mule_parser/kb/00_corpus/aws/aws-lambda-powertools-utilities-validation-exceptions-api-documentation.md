# aws_lambda_powertools.utilities.validation.exceptions API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/validation/exceptions.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/validation/exceptions.html)

---

# Module `aws_lambda_powertools.utilities.validation.exceptions`

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