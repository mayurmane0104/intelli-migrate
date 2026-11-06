# aws_lambda_powertools.utilities.idempotency.serialization.functions API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/idempotency/serialization/functions.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/idempotency/serialization/functions.html)

---

# Module `aws_lambda_powertools.utilities.idempotency.serialization.functions`

## Functions

- `def get_actual_type(model_type: Any) ‑> Any`
- 
## Expand source code`def get_actual_type(model_type: Any) -> Any: """ Extract the actual type from a potentially Optional or Union type. This function handles types that may be wrapped in Optional or Union, including the Python 3.10+ Union syntax (Type | None). Parameters ---------- model_type: Any The type to analyze. Can be a simple type, Optional[Type], BaseModel, dataclass Returns ------- The actual type without Optional or Union wrappers. Raises: IdempotencyModelTypeError: If the type specification is invalid (e.g., Union with multiple non-None types). """ # Get the origin of the type (e.g., Union, Optional) origin = get_origin(model_type) # Check if type is Union, Optional, or UnionType (Python 3.10+) if origin in (Union, Optional) or (sys.version_info >= (3, 10) and origin in (Union, UnionType)): # Get type arguments args = get_args(model_type) # Filter out NoneType actual_type = _extract_non_none_types(args) # Ensure only one non-None type exists if len(actual_type) != 1: raise IdempotencyModelTypeError( "Invalid type: expected a single type, optionally wrapped in Optional or Union with None.", ) return actual_type[0] # If not a Union/Optional type, return original type return model_type`Extract the actual type from a potentially Optional or Union type. This function handles types that may be wrapped in Optional or Union, including the Python 3.10+ Union syntax (Type | None). Parameters 
 - `model_type`- `Any`
- The type to analyze. Can be a simple type, Optional[Type], BaseModel, dataclass
 ## ReturnsThe actual type without Optional or Union wrappers. ## Raises- `IdempotencyModelTypeError`
- If the type specification is invalid (e.g., Union with multiple non-None types).