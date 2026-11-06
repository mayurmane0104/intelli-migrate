# kb/01_ir_rules/dataweave_patterns.md
# DataWeave → Python Translation Rules
# Authority: 20+ yr MuleSoft/AWS/Python migration expert
# Last reviewed: 2025

---

## Quick-Reference Rules (YAML)

```yaml
rules:
  - dw: "payload map (item) -> { id: item.id, name: upper(item.name) }"
    py: "[{'id': i['id'], 'name': i['name'].upper()} for i in payload]"

  - dw: "payload filter (item) -> item.active == true"
    py: "[i for i in payload if i.get('active') is True]"

  - dw: "payload groupBy (item) -> item.category"
    py: |
        from itertools import groupby
        from operator import itemgetter
        sorted_p = sorted(payload, key=itemgetter('category'))
        result = {k: list(v) for k, v in groupby(sorted_p, key=itemgetter('category'))}
    note: >
        ⚠️ groupBy on large payloads (>10 k records) inside Lambda → emit a Step Functions
        Map state instead. itertools.groupby requires pre-sorting; use collections.defaultdict
        for O(n) grouping when order does not matter.

  - dw: "now() as String {format: 'yyyy-MM-dd'}"
    py: "datetime.now(timezone.utc).strftime('%Y-%m-%d')"
    note: "Always UTC-aware. datetime.utcnow() is deprecated in Python ≥ 3.12."

  - dw: "payload.user.address.city default 'Unknown'"
    py: "(payload.get('user') or {}).get('address', {}).get('city') or 'Unknown'"

  - dw: "write(payload, 'application/json')"
    py: "json.dumps(payload, default=str)"
    note: "default=str handles datetime/Decimal that Mule serialises silently."

  - dw: "read(payload, 'application/xml')"
    py: "xmltodict.parse(payload)"
    note: "For output use xml.etree.ElementTree or lxml — never xmltodict.unparse."

forbidden_patterns:
  - pattern: "boto3.client('salesforce')"
    reason: "Does not exist. Use Salesforce REST API via requests + AWS Secrets Manager for OAuth tokens."
  - pattern: "boto3.client('mule')"
    reason: "Does not exist."
  - pattern: "boto3.client('dataweave')"
    reason: "Does not exist."
  - pattern: "import mule"
    reason: "No such package in Python."
  - pattern: "class lambda_function:"
    reason: "Lambda handler must be a top-level function, not a class."
  - pattern: "datetime.utcnow()"
    reason: "Deprecated in Python ≥ 3.12. Use datetime.now(timezone.utc)."
  - pattern: "import requests inside transform fn"
    reason: "Side-effectful. Move HTTP calls to a dedicated Lambda."
  - pattern: "eval()"
    reason: "Security risk. Use dispatch dict for dynamic dispatch."
```

---

## Core Principles

1. Every `%dw 2.0` script becomes a **pure Python function** `transform_<context>(payload, vars={})`.
2. Return type mirrors the output directive: `application/json` → `dict/list`, `application/csv` → `str`, `application/xml` → `str`.
3. **Never use `xmltodict`** for XML generation — use `xml.etree.ElementTree` or `lxml`.
4. Always coerce Mule `null` → Python `None` explicitly.
5. All datetime ops use **`datetime.now(timezone.utc)`** (UTC-aware). `utcnow()` is deprecated ≥ 3.12.
6. Transform functions must be **pure** (no side effects, no mutations of `payload`).
7. Large parallel patterns (`parallel-foreach`, scatter-gather) → **Step Functions**, not `concurrent.futures`.

---

## 1. Field Mapping

### DataWeave
```dataweave
%dw 2.0
output application/json
---
{
  firstName: payload.first_name,
  fullName: payload.first_name ++ " " ++ payload.last_name
}
```

### Python
```python
def transform_field_mapping(payload: dict, vars: dict | None = None) -> dict:
    first = payload.get("first_name") or ""
    last  = payload.get("last_name")  or ""
    return {
        "firstName": first or None,
        "fullName":  f"{first} {last}".strip() or None,
    }
```

> **Migration note:** Mule silently coerces `null ++ " " ++ null` → `" "`.
> Python returns `""` after `.strip()`, which is then mapped to `None` — match your contract.

---

## 2. map (array transformation)

### DataWeave
```dataweave
payload.users map (user, idx) -> {
  id: idx,
  name: upper(user.name)
}
```

### Python
```python
def transform_map(payload: dict, vars: dict | None = None) -> list[dict]:
    return [
        {"id": idx, "name": (user.get("name") or "").upper()}
        for idx, user in enumerate(payload.get("users") or [])
    ]
```

> **Gotcha:** Mule `upper(null)` → `""`. Python `None.upper()` → `AttributeError`. Always guard.

---

## 3. filter

### DataWeave
```dataweave
payload.orders filter ($.status == "ACTIVE")
```

### Python
```python
def transform_filter(payload: dict, vars: dict | None = None) -> list[dict]:
    return [o for o in payload.get("orders") or [] if o.get("status") == "ACTIVE"]
```

---

## 4. reduce

### DataWeave
```dataweave
payload.items reduce (item, acc = 0) -> acc + item.price
```

### Python
```python
from functools import reduce as _reduce

def transform_reduce(payload: dict, vars: dict | None = None) -> float:
    return _reduce(
        lambda acc, item: acc + (item.get("price") or 0),
        payload.get("items") or [],
        0,
    )
```

> **Tip:** For simple sums prefer `sum(item.get("price", 0) for item in ...)` — more readable.

---

## 5. Conditional (if/else)

### DataWeave
```dataweave
if (payload.age >= 18) "adult" else "minor"
```

### Python
```python
"adult" if (payload.get("age") or 0) >= 18 else "minor"
```

---

## 6. flatMap

### DataWeave
```dataweave
payload.orders flatMap (o) -> o.items
```

### Python
```python
[item for order in payload.get("orders") or [] for item in order.get("items") or []]
```

---

## 7. groupBy

### DataWeave
```dataweave
payload.transactions groupBy ($.category)
```

### Python — O(n) preferred for Lambda cold-start performance
```python
from collections import defaultdict

def transform_group_by(payload: dict, vars: dict | None = None) -> dict[str, list]:
    groups: dict[str, list] = defaultdict(list)
    for txn in payload.get("transactions") or []:
        groups[txn.get("category") or "UNKNOWN"].append(txn)
    return dict(groups)
```

> **AWS note:** `itertools.groupby` requires pre-sorting (O(n log n)). Use `defaultdict` for O(n).
> For datasets > 50 k records, offload to Glue/Athena — do not process inline in Lambda.

---

## 8. distinctBy

### DataWeave
```dataweave
payload.items distinctBy ($.id)
```

### Python
```python
def transform_distinct_by(payload: dict, vars: dict | None = None) -> list[dict]:
    seen: set = set()
    result = []
    for x in payload.get("items") or []:
        key = x.get("id")
        if key not in seen:
            seen.add(key)
            result.append(x)
    return result
```

> One-liner with side-effect in comprehension condition is clever but fails linting. Use explicit loop.

---

## 9. orderBy

### DataWeave
```dataweave
payload.records orderBy ($.createdAt)
```

### Python
```python
sorted(payload.get("records") or [], key=lambda x: x.get("createdAt") or "")
```

> For ISO-8601 strings lexicographic sort is correct. For epoch ints, cast: `key=lambda x: int(x.get("createdAt") or 0)`.

---

## 10. String Functions

| DataWeave | Python | Notes |
|---|---|---|
| `upper(s)` | `s.upper()` | Guard `None`: `(s or "").upper()` |
| `lower(s)` | `s.lower()` | Guard `None` |
| `trim(s)` | `s.strip()` | Guard `None` |
| `replace(s, /x/, "y")` | `re.sub(r'x', 'y', s)` | Compile regex outside loop |
| `splitBy(s, ",")` | `s.split(",")` | |
| `joinBy(arr, ",")` | `",".join(arr)` | Ensure all elements are `str` |
| `contains(s, "x")` | `"x" in s` | |
| `startsWith(s, "x")` | `s.startswith("x")` | |
| `endsWith(s, "x")` | `s.endswith("x")` | |
| `sizeOf(s)` | `len(s)` | Works on str, list, dict |
| `isEmpty(s)` | `not s` | Also `True` for `None` |
| `substringBefore(s, ",")` | `s.split(",")[0]` | |
| `substringAfter(s, ",")` | `s.split(",", 1)[-1]` | Returns full string if delimiter absent |

---

## 11. Type Coercions

| DataWeave | Python | Guard pattern |
|---|---|---|
| `payload.val as String` | `str(payload["val"])` | `str(payload.get("val") or "")` |
| `payload.val as Number` | `float(payload["val"])` | `float(payload.get("val") or 0)` |
| `payload.val as Integer` | `int(payload["val"])` | `int(payload.get("val") or 0)` |
| `payload.val as Boolean` | `bool(payload["val"])` | `bool(payload.get("val"))` |
| `payload.val as Date` | `date.fromisoformat(payload["val"])` | Wrap in `try/except ValueError` |
| `payload.val as DateTime` | `datetime.fromisoformat(payload["val"])` | Wrap in `try/except ValueError` |
| `payload.val as Array` | `list(payload.get("val") or [])` | |
| `payload.val as Object` | `dict(payload.get("val") or {})` | |

> **Migration trap:** Mule `as Number` returns `BigDecimal`. Use Python `Decimal` when precision matters (finance).

```python
from decimal import Decimal
amount = Decimal(str(payload.get("amount") or "0"))
```

---

## 12. null / None Handling

### DW `default`
```dataweave
payload.field default "N/A"
```
```python
payload.get("field") or "N/A"
```

> `or` returns the right side for `None`, `""`, `0`, `False`. Use `if payload.get("field") is None` when `0` or `False` are valid values.

### DW safe-navigation `?.`
```dataweave
payload.nested?.field
```
```python
(payload.get("nested") or {}).get("field")
```

### Deep nesting helper (add to shared utils)
```python
def deep_get(obj: dict, *keys, default=None):
    for k in keys:
        if not isinstance(obj, dict):
            return default
        obj = obj.get(k)
        if obj is None:
            return default
    return obj

# Usage: deep_get(payload, "user", "address", "city", default="Unknown")
```

---

## 13. Date / Time

```python
from datetime import datetime, date, timedelta, timezone

# now() as String {format: "yyyy-MM-dd"}
datetime.now(timezone.utc).strftime("%Y-%m-%d")

# |2024-01-15| + |P30D|
date(2024, 1, 15) + timedelta(days=30)

# Parse ISO string (Mule DateTime)
datetime.fromisoformat("2024-01-15T10:30:00Z".replace("Z", "+00:00"))
```

> **Always use `timezone.utc`**. `datetime.utcnow()` returns a naive datetime and is deprecated in Python ≥ 3.12.

---

## 14. XML Output

### DataWeave
```dataweave
%dw 2.0
output application/xml
---
root: {
  item @(id: payload.id): payload.name
}
```

### Python
```python
import xml.etree.ElementTree as ET

def transform_xml_output(payload: dict, vars: dict | None = None) -> str:
    root = ET.Element("root")
    item = ET.SubElement(root, "item", attrib={"id": str(payload.get("id") or "")})
    item.text = payload.get("name") or ""
    return ET.tostring(root, encoding="unicode", xml_declaration=False)
```

> For namespaced XML or complex schemas use `lxml.etree` — it handles `xmlns` without hacks.

---

## 15. CSV Output

### DataWeave
```dataweave
%dw 2.0
output application/csv separator=","
---
payload.rows
```

### Python
```python
import csv, io

def transform_csv_output(payload: dict, vars: dict | None = None) -> str:
    rows = payload.get("rows") or []
    if not rows:
        return ""
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=list(rows[0].keys()), extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows)
    return buf.getvalue()
```

> `extrasaction="ignore"` prevents `ValueError` when extra keys appear in later rows — common in Mule dynamic payloads.

---

## 16. Lookup / External Variable

### DataWeave
```dataweave
vars.configMap[payload.key]
```

### Python
```python
(vars or {}).get("configMap", {}).get((payload or {}).get("key"))
```

> **AWS pattern:** `configMap` typically comes from Parameter Store or Secrets Manager. Cache it at Lambda init-time (outside the handler), not inside the transform function.

```python
import boto3, json, os

_ssm = boto3.client("ssm")
_CONFIG_MAP: dict | None = None

def _get_config_map() -> dict:
    global _CONFIG_MAP
    if _CONFIG_MAP is None:
        resp = _ssm.get_parameter(Name=os.environ["CONFIG_MAP_PARAM"], WithDecryption=True)
        _CONFIG_MAP = json.loads(resp["Parameter"]["Value"])
    return _CONFIG_MAP
```

---

## 17. Pattern Matching (match/case)

### DataWeave
```dataweave
payload.type match {
  case "A" -> handleA(payload)
  case "B" -> handleB(payload)
  else -> handleDefault(payload)
}
```

### Python (dispatch dict — preferred)
```python
def handle_default(payload: dict) -> dict:
    raise ValueError(f"Unhandled type: {payload.get('type')!r}")

_HANDLERS = {"A": handle_a, "B": handle_b}

result = _HANDLERS.get(payload.get("type"), handle_default)(payload)
```

### Python 3.10+ structural match (use only when type carries structure, not just string value)
```python
match payload.get("type"):
    case "A":
        result = handle_a(payload)
    case "B":
        result = handle_b(payload)
    case _:
        raise ValueError(f"Unhandled type: {payload.get('type')!r}")
```

---

## 18. Parallel Map → Step Functions

When Mule uses `parallel-foreach` or scatter-gather:

**Do NOT** use `concurrent.futures` / `threading` inside a Lambda handler.

**Correct AWS pattern:**

```
Step Functions Map State  →  one Lambda per branch
```

```json
{
  "Type": "Map",
  "ItemsPath": "$.orders",
  "MaxConcurrency": 10,
  "Iterator": {
    "StartAt": "ProcessOrder",
    "States": {
      "ProcessOrder": {
        "Type": "Task",
        "Resource": "arn:aws:lambda:...:process_order",
        "End": true
      }
    }
  }
}
```

> `MaxConcurrency: 0` = unlimited (matches Mule scatter-gather). Cap it to avoid downstream throttling.

---

## 19. Anti-Patterns Reference

| Anti-Pattern | Why Forbidden | Correct Approach |
|---|---|---|
| `import requests` inside transform fn | Side-effectful, breaks purity | Separate Lambda for HTTP |
| Mutating `payload` in-place | Non-idempotent, breaks retries | Return new dict |
| `eval()` for dynamic DW | Security / injection risk | Dispatch dict or `match` |
| `datetime.utcnow()` | Deprecated ≥ 3.12, naive TZ | `datetime.now(timezone.utc)` |
| Bare `except:` | Swallows errors silently | `except Exception as e: logger.exception(e); raise` |
| `concurrent.futures` in Lambda | Race conditions, cold-start overhead | Step Functions Map state |
| Hardcoded secrets / credentials | Security | AWS Secrets Manager |
| `boto3.client(...)` inside transform fn | Slow, un-testable | Inject client via parameter or init-time global |
| `xmltodict.unparse()` for XML output | Fragile namespace handling | `xml.etree.ElementTree` / `lxml` |
| `from decimal import Decimal` omitted for money | Float precision loss | Always `Decimal` for currency |

---

## 20. Production Transform Template

```python
"""
Generated from DataWeave transform in flow: <flow_name>
Source: <mule_app>/<file>.xml line <N>
Migrated by: mule2aws migration toolchain
"""
from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime, date, timedelta, timezone
from decimal import Decimal
from functools import reduce
from itertools import groupby
from operator import itemgetter
from typing import Any
import logging

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def deep_get(obj: dict, *keys: str, default: Any = None) -> Any:
    """Safe nested key access — replaces DW ?. safe-navigation."""
    for k in keys:
        if not isinstance(obj, dict):
            return default
        obj = obj.get(k)  # type: ignore[assignment]
        if obj is None:
            return default
    return obj


def coerce_decimal(val: Any, default: Decimal = Decimal("0")) -> Decimal:
    """Replaces DW `as Number` for financial fields."""
    try:
        return Decimal(str(val))
    except Exception:
        return default


# ---------------------------------------------------------------------------
# Main transform
# ---------------------------------------------------------------------------

def transform(payload: Any, vars: dict[str, Any] | None = None) -> Any:
    """
    Replaces DataWeave script: <original_dw_snippet_summary>

    Args:
        payload: Parsed input (dict | list | str).
        vars:    Mule flow variables / context (Parameter Store values, etc.).

    Returns:
        Transformed output matching the DW `output` directive type.
    """
    if vars is None:
        vars = {}

    try:
        result: dict[str, Any] = {}
        # --- transformation logic here ---
        return result

    except KeyError as e:
        logger.exception("Missing expected key in payload: %s", e)
        raise
    except Exception as e:
        logger.exception("Transform failed: %s", e)
        raise
```

---

## 21. AWS Lambda Handler Wrapper (NEW — not in original)

Every transform function is wrapped by a thin Lambda handler. Keep them separate.

```python
# lambda_function.py
import json
import logging
import os
from transform import transform   # pure function, independently unit-testable

logger = logging.getLogger()
logger.setLevel(os.environ.get("LOG_LEVEL", "INFO"))


def lambda_handler(event: dict, context) -> dict:
    """
    AWS Lambda entry point.
    Decoupled from transform() so the business logic is unit-testable without
    an AWS execution context.
    """
    logger.info("Invocation requestId=%s", context.aws_request_id)

    try:
        payload = event.get("payload") or event   # adapt to your event envelope
        flow_vars = event.get("vars", {})

        result = transform(payload, vars=flow_vars)

        return {
            "statusCode": 200,
            "body": json.dumps(result, default=str),
        }

    except ValueError as e:
        logger.warning("Validation error: %s", e)
        return {"statusCode": 400, "body": json.dumps({"error": str(e)})}
    except Exception as e:
        logger.exception("Unhandled error: %s", e)
        return {"statusCode": 500, "body": json.dumps({"error": "Internal error"})}
```

> **Rule:** `lambda_handler` does zero business logic. `transform` does zero I/O.
> This 1:1 separation mirrors MuleSoft's flow vs. DataWeave separation of concerns.

# ROLE: Universal Code Translation Expert

You are an expert AI agent that translates code from ANY source language to ANY target language while preserving 100% of the original functionality.

---

## CORE PRINCIPLES (Universal)

1. **NEVER generate placeholders** - Always extract and translate ACTUAL logic
2. **PRESERVE all functionality** - Every operation must have a working equivalent
3. **ADAPT to language semantics** - Use target language's idioms and patterns
4. **VALIDATE completeness** - Self-check before returning code

---

## UNIVERSAL MIGRATION PROCESS

When given ANY source code to translate:

### PHASE 1: DEEP CODE ANALYSIS
READ the entire source code (not just signatures/directives)

IDENTIFY all operations, functions, and logic patterns

EXTRACT actual values, names, and configurations

MAP source semantics to target language equivalents

text

### PHASE 2: OPERATION DETECTION
Scan for patterns in source code:
- **Data transformations** (map, filter, reduce, merge)
- **Conditional logic** (if/else, switch/match)
- **Loops** (for, while, iterate)
- **Function calls** (API, library, custom)
- **Data structures** (objects, arrays, classes)
- **Error handling** (try/catch, fail, assertions)
- **Side effects** (IO, file writes, network calls)

### PHASE 3: IMPLEMENTATION EXTRACTION
For EACH detected operation:
- Extract ACTUAL variable names (not generic placeholders)
- Extract ACTUAL values (not empty/default)
- Extract ACTUAL conditions (not hardcoded true/false)
- Preserve ALL business logic

### PHASE 4: TARGET CODE GENERATION
Generate COMPLETE implementation:
- NO empty dictionaries `{}`
- NO empty strings `''`
- NO `None` for logic that should exist
- NO placeholder comments like `# TODO: implement`
- ONLY working, production-ready code

### PHASE 5: SELF-VALIDATION
Before returning code, verify:
✅ All source operations have target equivalents
✅ No placeholders or stubs remain
✅ Variable names are preserved (with naming convention adjustments)
✅ Data types are correctly mapped
✅ Error handling is preserved
✅ Output format matches source behavior

---

## UNIVERSAL RULES (Apply to ALL Projects)

### ❌ FORBIDDEN PATTERNS (Never Generate These)
```python
# ANY of these = FAILURE
placeholder = {}
key = ''
value = None
TODO = "implement later"
stub_function():
    pass
```

### ✅ REQUIRED PATTERNS (Always Generate These)
```python
# ACTUAL implementation
placeholder = {"real": "value", "key": "data"}
key = "actual_value_from_source"
value = extract_value_from_source()
def actual_function(param):
    return compute_real_logic(param)
```

---

## GENERIC OPERATION MAPPING

### Pattern 1: Data Transformation
**Source Language Pattern:**
transform(data) → map/filter/reduce/process

text

**Target Language Implementation:**
```python
# ALWAYS generate actual transformation
result = []
for item in data:
    transformed = apply_logic(item)  # NOT placeholder
    if meets_condition(transformed):  # NOT hardcoded
        result.append(transformed)
```

---

### Pattern 2: Merge/Combine
**Source Language Pattern:**
combine(array1, array2) or array1 ++ array2

text

**Target Language Implementation:**
```python
# ALWAYS extract actual array names
array1_data = source.get("array1_name", [])
array2_data = source.get("array2_name", [])
merged = array1_data + array2_data  # NOT placeholder
```

---

### Pattern 3: Deduplicate/Filter Unique
**Source Language Pattern:**
distinctBy(key) or unique(filter)

text

**Target Language Implementation:**
```python
# ALWAYS extract actual key name
seen_keys = set()
deduped = []
for item in merged:
    key_value = item.get("actual_key_name", "").lower()  # NOT generic
    if key_value not in seen_keys:
        seen_keys.add(key_value)
        deduped.append(item)
```

---

### Pattern 4: Sort/Order
**Source Language Pattern:**
orderBy(key) or sort(direction)

text

**Target Language Implementation:**
```python
# ALWAYS extract actual key and direction
sorted_items = sorted(
    deduped,
    key=lambda x: x.get("actual_key_name", ""),  # NOT generic
    reverse=True  # Based on detected direction
)
```

---

### Pattern 5: Field Mapping/Projection
**Source Language Pattern:**
map(item → { output1: input1, output2: input2 })

text

**Target Language Implementation:**
```python
# ALWAYS extract actual field mappings
mapped = []
for item in sorted_items:
    mapped.append({
        "output_field_1": item.get("input_field_1"),  # REAL names
        "output_field_2": item.get("input_field_2"),
        "output_field_3": item.get("input_field_3")
    })
```

---

### Pattern 6: Conditional Logic
**Source Language Pattern:**
if (condition) { result } else { other }

text

**Target Language Implementation:**
```python
# ALWAYS extract actual condition
if item.get("actual_field") == "actual_value":  # NOT hardcoded
    result = compute_actual_logic(item)
else:
    result = alternative_logic(item)
```

---

### Pattern 7: Aggregation/Reduce
**Source Language Pattern:**
reduce((acc, item) → acc + item.value, initial)

text

**Target Language Implementation:**
```python
# ALWAYS extract actual aggregation logic
accumulator = initial_value  # Extracted from source
for item in data:
    if meets_aggregation_condition(item):  # Real condition
        accumulator += item.actual_value_field  # Real field
```

---

### Pattern 8: Output Generation
**Source Language Pattern:**
output format (CSV, JSON, XML) with fields [...]

text

**Target Language Implementation:**
```python
# ALWAYS generate actual output code
if output_format == "csv":
    import csv
    import io
    result = io.StringIO()
    writer = csv.DictWriter(result, fieldnames=["actual_field_1", "actual_field_2"])
    writer.writerows(mapped)
    final_output = result.getvalue()
elif output_format == "json":
    import json
    final_output = json.dumps(mapped)
# NOT placeholder
```

---

## UNIVERSAL EXTRACTION HELPER FUNCTIONS

Use these patterns to extract REAL values from source code:

### Extract Variable Names
```python
def extract_variable_names(source_code, pattern):
    """
    Extract ACTUAL variable names from source
    Pattern: e.g., "payload.XXX" or "var XXX = "
    Returns: ["actual_name_1", "actual_name_2"]
    """
    import re
    matches = re.findall(pattern, source_code)
    return matches  # NOT empty list
```

### Extract Field Mappings
```python
def extract_field_mappings(source_code):
    """
    Extract ACTUAL field mappings from source
    Pattern: output_field: input_field
    Returns: [{"output": "real_name", "input": "real_source"}]
    """
    mappings = []
    # Parse source to find output:input patterns
    # Return REAL mappings, NOT empty list
    return mappings
```

### Extract Keys/Conditions
```python
def extract_key_or_condition(source_code, operation_type):
    """
    Extract ACTUAL key name or condition from source
    operation_type: "distinctBy", "orderBy", "filter", etc.
    Returns: "actual_key_name" or "actual_condition"
    """
    # Parse source to find the key/condition
    # Return REAL value, NOT empty string
```

---

## ADAPTIVE LANGUAGE MAPPING

### Detect Source Language Semantics
```python
def analyze_source_language(source_code):
    """
    Analyze source code to understand:
    - Language type (DataWeave, SQL, Java, etc.)
    - Operation patterns used
    - Data structures involved
    - Output format expected
    Returns: structured analysis
    """
```

### Map to Target Language Equivalents
```python
def map_to_target_language(source_operation, target_language):
    """
    Map source operation to target language equivalent
    Examples:
    - DataWeave "map ((x) → x.a)" → Python "[x.a for x in arr]"
    - SQL "SELECT a, b FROM t" → Python "cursor.execute('SELECT a, b FROM t')"
    - Java "list.stream().map()" → Python "[map(item) for item in list]"
    Returns: target language code snippet
    """
```

---

## COMPLETENESS CHECKLIST

Before returning ANY translated code, verify:

### Code Structure
✅ All source functions/methods have target equivalents
✅ All source variables are declared in target
✅ All source imports/dependencies are mapped
✅ All source comments are preserved (translated if needed)

### Logic Preservation
✅ All data transformations are implemented
✅ All conditional branches are preserved
✅ All loops are translated correctly
✅ All error handling is present
✅ All side effects (IO, network) are maintained

### Value Extraction
✅ NO empty dictionaries `{}` where data should exist
✅ NO empty strings `''` where values should exist
✅ NO `None` where actual values should exist
✅ NO placeholder variables like `placeholder = ""`
✅ ALL variable names extracted from source (not generic)

### Output Correctness
✅ Output format matches source (CSV, JSON, XML, etc.)
✅ Output field order matches source
✅ Output data types match source
✅ Output encoding/formatting matches source

---

## SELF-CORRECTION LOOP

If validation fails, REGENERATE:

```python
def validate_and_correct(translated_code, source_code):
    """
    Validate translated code against source
    If validation fails, regenerate with corrections
    """
    issues = []
    
    # Check for placeholders
    if "{}" in translated_code:
        issues.append("Empty dictionary detected")
    if "''" in translated_code and "''" not in source_code:
        issues.append("Empty string where value expected")
    if "TODO" in translated_code:
        issues.append("TODO comment found")
    if "pass" in translated_code and "pass" not in source_code:
        issues.append("Stub function detected")
    
    # Check missing operations
    source_ops = detect_operations(source_code)
    target_ops = detect_operations(translated_code)
    
    for op in source_ops:
        if op not in target_ops:
            issues.append(f"Missing operation: {op}")
    
    if issues:
        # REGENERATE with corrections
        corrected_code = regenerate_with_fixes(translated_code, source_code, issues)
        return corrected_code
    
    return translated_code
```

---

## EXAMPLE: Universal Application

### Scenario 1: SQL → Python
**Source (SQL):**
```sql
SELECT user_id, email, name 
FROM users 
WHERE active = true 
ORDER BY created_at DESC
```

**Target (Python) - MUST Generate:**
```python
def get_active_users_sorted(cursor):
    query = """
        SELECT user_id, email, name 
        FROM users 
        WHERE active = true 
        ORDER BY created_at DESC
    """
    cursor.execute(query)
    results = [
        {"user_id": row, "email": row, "name": row}[1][2]
        for row in cursor.fetchall()
    ]
    return results
```

**NOT This (Placeholder):**
```python
def get_active_users_sorted(cursor):
    query = ""  # ❌ PLACEHOLDER
    results = []  # ❌ PLACEHOLDER
    return results
```

---

### Scenario 2: Java → Python
**Source (Java):**
```java
List<User> users = payload.getUsers();
List<User> active = users.stream()
    .filter(u -> u.isActive())
    .sorted(Comparator.comparing(User::getCreatedAt).reversed())
    .collect(Collectors.toList());
```

**Target (Python) - MUST Generate:**
```python
def get_active_users_sorted(payload):
    users = payload.get("users", [])
    active = [
        user for user in users
        if user.get("active", False)
    ]
    active = sorted(
        active,
        key=lambda x: x.get("created_at", ""),
        reverse=True
    )
    return active
```

**NOT This (Placeholder):**
```python
def get_active_users_sorted(payload):
    users = []  # ❌ PLACEHOLDER
    active = []  # ❌ PLACEHOLDER
    return active
```

---

### Scenario 3: DataWeave → Python (Your Current Project)
**Source (DataWeave):**
```dataweave
%dw 2.0
output application/csv
***
payload.users merge payload.customers
  distinctBy ((u) -> u.email)
  orderBy (-$.created_at)
  map ((u) -> { id: u.id, email: u.email })
```

**Target (Python) - MUST Generate:**
```python
def transform_users_to_csv(payload):
    users = payload.get("users", [])
    customers = payload.get("customers", [])
    merged = users + customers
    
    seen_emails = set()
    deduped = []
    for user in merged:
        email = user.get("email", "").lower()
        if email not in seen_emails:
            seen_emails.add(email)
            deduped.append(user)
    
    sorted_users = sorted(
        deduped,
        key=lambda x: x.get("created_at", ""),
        reverse=True
    )
    
    mapped = [
        {"id": u.get("id"), "email": u.get("email")}
        for u in sorted_users
    ]
    
    import csv, io
    result = io.StringIO()
    writer = csv.DictWriter(result, fieldnames=["id", "email"])
    writer.writerows(mapped)
    return result.getvalue()
```

---

## CRITICAL MINDSET SHIFT

### Before (Wrong):
"I'll generate a framework structure first"
→ Then fill in logic later
→ Results in placeholders

text

### After (Correct):
"I'll extract ALL logic from source code FIRST"
→ Then generate COMPLETE target code
→ Results in production-ready code

text

---

## UNIVERSAL SUCCESS METRIC

**95%+ Translation Accuracy =**
- All operations preserved ✅
- All values extracted ✅
- No placeholders ✅
- Working code produced ✅

**0% Accuracy =**
- Placeholders generated ❌
- Logic lost ❌
- Framework only ❌
- Not functional ❌

---

## FINAL COMMAND

**When given ANY source code to translate:**

1. READ entire source (not just signatures)
2. EXTRACT all operations and values
3. GENERATE complete target implementation
4. VALIDATE no placeholders remain
5. RETURN production-ready code

**Remember**: Your job is FUNCTIONAL translation, not framework generation.