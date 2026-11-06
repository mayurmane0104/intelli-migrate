# aws_lambda_powertools.utilities.serialization API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/serialization.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/serialization.html)

---

# Module `aws_lambda_powertools.utilities.serialization`

Standalone functions to serialize/deserialize common data structures

## Functions

- `def base64_decode(data: str) ‑> str`
- 
## Expand source code`def base64_decode(data: str) -> str: """Decodes a Base64-encoded string and returns the decoded value. Parameters ---------- data: str The Base64-encoded string to decode. Returns ------- str The decoded string value. """ return base64.b64decode(data).decode("utf-8")`Decodes a Base64-encoded string and returns the decoded value. ## Parameters- `data`- `str`
- The Base64-encoded string to decode.
 ## Returns- `str`
- The decoded string value.
 
- `def base64_encode(data: str) ‑> str`
- 
## Expand source code`def base64_encode(data: str) -> str: """Encode a string and returns Base64-encoded encoded value. Parameters ---------- data: str The string to encode. Returns ------- str The Base64-encoded encoded value. """ return base64.b64encode(data.encode()).decode("utf-8")`Encode a string and returns Base64-encoded encoded value. ## Parameters- `data`- `str`
- The string to encode.
 ## Returns- `str`
- The Base64-encoded encoded value.
 
- `def base64_from_json(data: Any, json_serializer: Callable[..., str] = <function dumps>) ‑> str`
- 
## Expand source code`def base64_from_json(data: Any, json_serializer: Callable[..., str] = json.dumps) -> str: """Encode JSON serializable data as base64 string Parameters ---------- data: Any JSON serializable (dict, list, boolean, etc.) json_serializer: Callable function to serialize `obj` to a JSON formatted `str`, by default json.dumps Returns ------- str: JSON string as base64 string """ return base64_from_str(data=json_serializer(data))`Encode JSON serializable data as base64 string ## Parameters- `data`- `Any`
- JSON serializable (dict, list, boolean, etc.)
- `json_serializer`- `Callable`
- function to serialize `obj`to a JSON formatted`str`, by default json.dumps
 ## Returns- `str:`
- JSON string as base64 string
 
- `def base64_from_str(data: str) ‑> str`
- 
## Expand source code`def base64_from_str(data: str) -> str: """Encode str as base64 string""" return base64.b64encode(data.encode()).decode("utf-8")`Encode str as base64 string