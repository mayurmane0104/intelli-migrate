# aws_lambda_powertools.utilities.data_classes.appsync.scalar_types_utils API documentation

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/appsync/scalar_types_utils.html](https://docs.aws.amazon.com/powertools/python/latest/api/utilities/data_classes/appsync/scalar_types_utils.html)

---

# Module `aws_lambda_powertools.utilities.data_classes.appsync.scalar_types_utils`

## Functions

- `def aws_date(timezone_offset: int = 0) ‑> str`
- 
## Expand source code`def aws_date(timezone_offset: int = 0) -> str: """AWSDate - An extended ISO 8601 date string in the format YYYY-MM-DD. Parameters ---------- timezone_offset : int Timezone offset, defaults to 0 Returns ------- str Returns current time as AWSDate scalar string with optional timezone offset """ return _formatted_time(datetime.datetime.utcnow(), "%Y-%m-%d", timezone_offset)`AWSDate - An extended ISO 8601 date string in the format YYYY-MM-DD. ## Parameters- `timezone_offset`- `int`
- Timezone offset, defaults to 0
 ## Returns- `str`
- Returns current time as AWSDate scalar string with optional timezone offset
 
- `def aws_datetime(timezone_offset: int = 0) ‑> str`
- 
## Expand source code`def aws_datetime(timezone_offset: int = 0) -> str: """AWSDateTime - An extended ISO 8601 date and time string in the format YYYY-MM-DDThh:mm:ss.sssZ. Parameters ---------- timezone_offset : int Timezone offset, defaults to 0 Returns ------- str Returns current time as AWSDateTime scalar string with optional timezone offset """ return _formatted_time(datetime.datetime.utcnow(), "%Y-%m-%dT%H:%M:%S.%f", timezone_offset)`AWSDateTime - An extended ISO 8601 date and time string in the format YYYY-MM-DDThh:mm:ss.sssZ. ## Parameters- `timezone_offset`- `int`
- Timezone offset, defaults to 0
 ## Returns- `str`
- Returns current time as AWSDateTime scalar string with optional timezone offset
 
- `def aws_time(timezone_offset: int = 0) ‑> str`
- 
## Expand source code`def aws_time(timezone_offset: int = 0) -> str: """AWSTime - An extended ISO 8601 time string in the format hh:mm:ss.sss. Parameters ---------- timezone_offset : int Timezone offset, defaults to 0 Returns ------- str Returns current time as AWSTime scalar string with optional timezone offset """ return _formatted_time(datetime.datetime.utcnow(), "%H:%M:%S.%f", timezone_offset)`AWSTime - An extended ISO 8601 time string in the format hh:mm:ss.sss. ## Parameters- `timezone_offset`- `int`
- Timezone offset, defaults to 0
 ## Returns- `str`
- Returns current time as AWSTime scalar string with optional timezone offset
 
- `def aws_timestamp() ‑> int`
- 
## Expand source code`def aws_timestamp() -> int: """AWSTimestamp - An integer value representing the number of seconds before or after 1970-01-01-T00:00Z.""" return int(time.time())`AWSTimestamp - An integer value representing the number of seconds before or after 1970-01-01-T00:00Z. 
- `def make_id() ‑> str`
- 
## Expand source code`def make_id() -> str: """ID - A unique identifier for an object. This scalar is serialized like a String but isn't meant to be human-readable.""" return str(uuid.uuid4())`ID - A unique identifier for an object. This scalar is serialized like a String but isn't meant to be human-readable.