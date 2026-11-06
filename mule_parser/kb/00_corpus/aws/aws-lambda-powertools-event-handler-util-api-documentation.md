# aws_lambda_powertools.event_handler.util API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/event_handler/util.html](https://docs.aws.amazon.com/powertools/python/latest/api/event_handler/util.html)

---

# Module `aws_lambda_powertools.event_handler.util`

## Functions

- `def extract_origin_header(resolved_headers: Mapping[str, Any])`
- 
## Expand source code`def extract_origin_header(resolved_headers: Mapping[str, Any]): """ Extracts the 'origin' or 'Origin' header from the provided resolver headers. The 'origin' or 'Origin' header can be either a single header or a multi-header. Args: resolved_headers (Mapping): A dictionary containing the headers. Returns: str | None: The value(s) of the origin header or None. """ resolved_header = resolved_headers.get("origin") if isinstance(resolved_header, list): return resolved_header[0] return resolved_header`Extracts the 'origin' or 'Origin' header from the provided resolver headers. The 'origin' or 'Origin' header can be either a single header or a multi-header. ## Args- `resolved_headers`- `Mapping`
- A dictionary containing the headers.
 ## Returns- `str | None`
- The value(s) of the origin header or None.