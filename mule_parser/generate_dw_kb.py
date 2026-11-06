import os

base_dir = r"c:\Users\TISSATECH\Documents\parsercopy\mule_parser\knowledge_base\corpus"
dw_dir = os.path.join(base_dir, "dataweave")
examples_dir = os.path.join(base_dir, "dataweave_examples")

# Create directories
os.makedirs(dw_dir, exist_ok=True)
os.makedirs(os.path.join(examples_dir, "simple"), exist_ok=True)
os.makedirs(os.path.join(examples_dir, "medium"), exist_ok=True)
os.makedirs(os.path.join(examples_dir, "advanced"), exist_ok=True)
os.makedirs(os.path.join(examples_dir, "expert"), exist_ok=True)

dw_files = {
    "basics.md": """# DataWeave Basics
## Syntax
DataWeave is a functional programming language designed for transforming data. It uses a JSON-like syntax.
## Execution Model
It streams data and evaluates lazily where possible.
## Python Equivalent
Python uses dictionaries, lists, and functions.
## TypeScript Equivalent
TypeScript uses objects, arrays, and arrow functions.
""",
    "arrays.md": """# DataWeave Arrays
## Syntax
DataWeave arrays support map, flatMap, flatten, first, last, tail, head.
## Execution Model
Operations are performed efficiently over sequences.
## Python Equivalent
`map` -> list comprehension or `map()`
`flatMap` -> nested list comprehension
`flatten` -> `itertools.chain.from_iterable`
`first` -> `arr[0]`
`last` -> `arr[-1]`
`tail` -> `arr[1:]`
`head` -> `arr[0]`
## TypeScript Equivalent
`map` -> `Array.prototype.map()`
`flatMap` -> `Array.prototype.flatMap()`
`flatten` -> `Array.prototype.flat()`
`first` -> `arr[0]`
`last` -> `arr[arr.length - 1]`
`tail` -> `arr.slice(1)`
`head` -> `arr[0]`
""",
    "objects.md": """# DataWeave Objects
## Syntax
Objects (key-value pairs) can be mapped using `mapObject`.
## Execution Model
Iterates over key-value-index triplets.
## Python Equivalent
Dictionary comprehensions: `{k: v for k, v in obj.items()}`
## TypeScript Equivalent
`Object.fromEntries(Object.entries(obj).map(([k, v]) => [k, v]))`
""",
    "filters.md": """# DataWeave Filters
## Syntax
Use `filter` to remove items from an array and `filterObject` for objects.
## Execution Model
Evaluates the condition for each element and returns matching ones.
## Python Equivalent
`[x for x in arr if condition]`
`{k: v for k, v in obj.items() if condition}`
## TypeScript Equivalent
`arr.filter(x => condition)`
`Object.fromEntries(Object.entries(obj).filter(([k, v]) => condition))`
""",
    "maps.md": """# DataWeave Maps
## Syntax
Use `map` for arrays and `mapObject` for objects.
## Execution Model
Transforms each element in the collection.
## Python Equivalent
`[f(x) for x in arr]`
`{k: f(v) for k, v in obj.items()}`
## TypeScript Equivalent
`arr.map(x => f(x))`
`Object.fromEntries(Object.entries(obj).map(([k, v]) => [k, f(v)]))`
""",
    "reduce.md": """# DataWeave Reduce
## Syntax
Use `reduce` to accumulate values in an array.
## Execution Model
Accumulates a value by iterating through the array.
## Python Equivalent
`functools.reduce(lambda acc, x: ..., arr, init)`
## TypeScript Equivalent
`arr.reduce((acc, x) => ..., init)`
""",
    "groupBy.md": """# DataWeave groupBy
## Syntax
Groups items in an array by a specific criteria.
## Execution Model
Creates an object where keys are the criteria and values are arrays of matching items.
## Python Equivalent
`itertools.groupby` (requires sorting first) or a custom dictionary loop.
## TypeScript Equivalent
`Object.groupBy(arr, x => x.key)` or custom reduce.
""",
    "distinctBy.md": """# DataWeave distinctBy
## Syntax
Returns unique items in an array based on a criteria.
## Execution Model
Filters out items that have duplicate criteria values.
## Python Equivalent
Using a dictionary or a set to keep track of seen keys.
## TypeScript Equivalent
Using `Set` or filtering with a tracker object.
""",
    "orderBy.md": """# DataWeave orderBy
## Syntax
Sorts an array based on a criteria.
## Execution Model
Sorts elements in ascending order by default.
## Python Equivalent
`sorted(arr, key=lambda x: ...)`
## TypeScript Equivalent
`arr.sort((a, b) => ...)`
""",
    "joins.md": """# DataWeave Joins
## Syntax
Join arrays of objects using `join`, `leftJoin`, `outerJoin`.
## Execution Model
Matches elements from left and right collections based on key functions.
## Python Equivalent
Using pandas `merge` or nested loops.
## TypeScript Equivalent
Nested loops or map with find.
""",
    "mergeWith.md": """# DataWeave mergeWith
## Syntax
Merges two objects.
## Execution Model
Right object overwrites matching keys in the left object.
## Python Equivalent
`{**obj1, **obj2}` or `obj1 | obj2`
## TypeScript Equivalent
`{...obj1, ...obj2}`
""",
    "csv.md": """# DataWeave CSV
## Syntax
Parsing and formatting CSV data.
## Execution Model
Streams rows as objects.
## Python Equivalent
`csv` module or `pandas.read_csv`.
## TypeScript Equivalent
`csv-parse` or similar libraries.
""",
    "xml.md": """# DataWeave XML
## Syntax
Parsing and formatting XML data.
## Execution Model
Maps nodes to objects/arrays.
## Python Equivalent
`xml.etree.ElementTree` or `lxml` or `xmltodict`.
## TypeScript Equivalent
`fast-xml-parser` or `xml2js`.
""",
    "json_format.md": """# DataWeave JSON
## Syntax
Parsing and formatting JSON data.
## Execution Model
Native tree representation in DataWeave.
## Python Equivalent
`json` module.
## TypeScript Equivalent
`JSON.parse()` and `JSON.stringify()`.
""",
    "functions.md": """# DataWeave Functions
## Syntax
Defining custom functions using `fun`.
## Execution Model
Supports first-class functions and closures.
## Python Equivalent
`def` keyword or `lambda`.
## TypeScript Equivalent
`function` keyword or arrow functions.
""",
    "modules.md": """# DataWeave Modules
## Syntax
Importing and exporting modules.
## Execution Model
Namespaces definitions for reuse.
## Python Equivalent
`import` and `from ... import ...`
## TypeScript Equivalent
`import` and `export` statements.
""",
    "advanced_patterns.md": """# DataWeave Advanced Patterns
## Syntax
Pattern matching, tail recursion, etc.
## Execution Model
Optimizes tail calls, matches based on types/values.
## Python Equivalent
`match` statement (Python 3.10+), loops instead of recursion.
## TypeScript Equivalent
`switch` statements, type guards, loops.
""",
    "streaming.md": """# DataWeave Streaming
## Syntax
Processing large payloads with streaming.
## Execution Model
Reads input progressively to save memory.
## Python Equivalent
Generators and `yield`.
## TypeScript Equivalent
Async generators and Node.js Streams.
"""
}

example_files = {
    "simple/field_rename.md": """# Field Rename
## DataWeave
```dataweave
%dw 2.0
output application/json
---
{
    newName: payload.oldName
}
```
## Python
```python
def transform(payload):
    return {"newName": payload.get("oldName")}
```
## TypeScript
```typescript
function transform(payload: any) {
    return { newName: payload.oldName };
}
```""",
    "simple/type_coercion.md": """# Type Coercion
## DataWeave
```dataweave
%dw 2.0
output application/json
---
{
    count: payload.count as Number
}
```
## Python
```python
def transform(payload):
    return {"count": float(payload.get("count", 0))}
```
## TypeScript
```typescript
function transform(payload: any) {
    return { count: Number(payload.count) };
}
```""",
    "simple/null_default.md": """# Null Default
## DataWeave
```dataweave
%dw 2.0
output application/json
---
{
    value: payload.value default "fallback"
}
```
## Python
```python
def transform(payload):
    return {"value": payload.get("value") or "fallback"}
```
## TypeScript
```typescript
function transform(payload: any) {
    return { value: payload.value ?? "fallback" };
}
```""",
    "simple/string_operations.md": """# String Operations
## DataWeave
```dataweave
%dw 2.0
output application/json
---
{
    upper: upper(payload.text),
    lower: lower(payload.text)
}
```
## Python
```python
def transform(payload):
    text = payload.get("text", "")
    return {
        "upper": text.upper(),
        "lower": text.lower()
    }
```
## TypeScript
```typescript
function transform(payload: any) {
    const text = payload.text || "";
    return {
        upper: text.toUpperCase(),
        lower: text.toLowerCase()
    };
}
```""",
    "simple/conditional.md": """# Conditional
## DataWeave
```dataweave
%dw 2.0
output application/json
---
{
    status: if (payload.code == 200) "OK" else "ERROR"
}
```
## Python
```python
def transform(payload):
    return {"status": "OK" if payload.get("code") == 200 else "ERROR"}
```
## TypeScript
```typescript
function transform(payload: any) {
    return { status: payload.code === 200 ? "OK" : "ERROR" };
}
```""",
    "medium/array_map.md": """# Array Map
## DataWeave
```dataweave
%dw 2.0
output application/json
---
payload map (item, index) -> {
    id: item.id,
    index: index
}
```
## Python
```python
def transform(payload):
    return [{"id": item.get("id"), "index": idx} for idx, item in enumerate(payload)]
```
## TypeScript
```typescript
function transform(payload: any[]) {
    return payload.map((item, index) => ({ id: item.id, index }));
}
```""",
    "medium/filter_array.md": """# Filter Array
## DataWeave
```dataweave
%dw 2.0
output application/json
---
payload filter ((item, index) -> item.isActive == true)
```
## Python
```python
def transform(payload):
    return [item for item in payload if item.get("isActive") is True]
```
## TypeScript
```typescript
function transform(payload: any[]) {
    return payload.filter(item => item.isActive === true);
}
```""",
    "medium/groupBy_example.md": """# Group By Example
## DataWeave
```dataweave
%dw 2.0
output application/json
---
payload groupBy ((item, index) -> item.category)
```
## Python
```python
from collections import defaultdict

def transform(payload):
    grouped = defaultdict(list)
    for item in payload:
        grouped[item.get("category")].append(item)
    return dict(grouped)
```
## TypeScript
```typescript
function transform(payload: any[]) {
    return payload.reduce((acc, item) => {
        const key = item.category;
        if (!acc[key]) acc[key] = [];
        acc[key].push(item);
        return acc;
    }, {} as Record<string, any[]>);
}
```""",
    "medium/distinctBy_example.md": """# Distinct By Example
## DataWeave
```dataweave
%dw 2.0
output application/json
---
payload distinctBy ((item, index) -> item.id)
```
## Python
```python
def transform(payload):
    seen = set()
    result = []
    for item in payload:
        if item.get("id") not in seen:
            seen.add(item.get("id"))
            result.append(item)
    return result
```
## TypeScript
```typescript
function transform(payload: any[]) {
    const seen = new Set();
    return payload.filter(item => {
        if (!seen.has(item.id)) {
            seen.add(item.id);
            return true;
        }
        return false;
    });
}
```""",
    "medium/reduce_sum.md": """# Reduce Sum
## DataWeave
```dataweave
%dw 2.0
output application/json
---
payload reduce ((item, acc = 0) -> acc + item.amount)
```
## Python
```python
import functools

def transform(payload):
    return functools.reduce(lambda acc, item: acc + item.get("amount", 0), payload, 0)
```
## TypeScript
```typescript
function transform(payload: any[]) {
    return payload.reduce((acc, item) => acc + (item.amount || 0), 0);
}
```""",
    "advanced/nested_transform.md": """# Nested Transform
## DataWeave
```dataweave
%dw 2.0
output application/json
---
payload map ((user) -> {
    userId: user.id,
    address: user.address mapObject ((value, key) -> {
        (upper(key)): value
    })
})
```
## Python
```python
def transform(payload):
    return [
        {
            "userId": user.get("id"),
            "address": {str(k).upper(): v for k, v in user.get("address", {}).items()}
        }
        for user in payload
    ]
```
## TypeScript
```typescript
function transform(payload: any[]) {
    return payload.map(user => ({
        userId: user.id,
        address: Object.fromEntries(
            Object.entries(user.address || {}).map(([k, v]) => [k.toUpperCase(), v])
        )
    }));
}
```""",
    "advanced/innerjoin_example.md": """# Inner Join Example
## DataWeave
```dataweave
%dw 2.0
import * from dw::core::Arrays
output application/json
---
join(payload.users, payload.orders, (user) -> user.id, (order) -> order.userId)
```
## Python
```python
def transform(payload):
    users = {u["id"]: u for u in payload.get("users", [])}
    result = []
    for order in payload.get("orders", []):
        user = users.get(order.get("userId"))
        if user:
            result.append({"l": user, "r": order})
    return result
```
## TypeScript
```typescript
function transform(payload: any) {
    const usersMap = new Map(payload.users?.map((u: any) => [u.id, u]) || []);
    const result: any[] = [];
    for (const order of payload.orders || []) {
        const user = usersMap.get(order.userId);
        if (user) {
            result.push({ l: user, r: order });
        }
    }
    return result;
}
```""",
    "advanced/csv_to_json.md": """# CSV to JSON
## DataWeave
```dataweave
%dw 2.0
output application/json
---
payload map ((row) -> {
    id: row.ID as Number,
    name: row.Name
})
```
## Python
```python
def transform(payload):
    # Assuming payload is a list of dicts from csv.DictReader
    return [
        {
            "id": int(row.get("ID", 0)),
            "name": row.get("Name")
        }
        for row in payload
    ]
```
## TypeScript
```typescript
function transform(payload: any[]) {
    return payload.map(row => ({
        id: Number(row.ID),
        name: row.Name
    }));
}
```""",
    "expert/multi_source_merge.md": """# Multi-Source Merge
## DataWeave
```dataweave
%dw 2.0
output application/json
var dbData = payload.dbResult
var apiData = payload.apiResult
---
dbData map ((dbRow) -> 
    dbRow ++ (apiData filter ($.id == dbRow.id))[0] default {}
)
```
## Python
```python
def transform(payload):
    db_data = payload.get("dbResult", [])
    api_data = payload.get("apiResult", [])
    
    api_map = {item.get("id"): item for item in api_data if "id" in item}
    
    result = []
    for db_row in db_data:
        merged = dict(db_row)
        merged.update(api_map.get(db_row.get("id"), {}))
        result.append(merged)
        
    return result
```
## TypeScript
```typescript
function transform(payload: any) {
    const dbData = payload.dbResult || [];
    const apiData = payload.apiResult || [];
    
    const apiMap = new Map(apiData.map((item: any) => [item.id, item]));
    
    return dbData.map((dbRow: any) => ({
        ...dbRow,
        ...(apiMap.get(dbRow.id) || {})
    }));
}
```"""
}

for name, content in dw_files.items():
    path = os.path.join(dw_dir, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {path}")

for name, content in example_files.items():
    path = os.path.join(examples_dir, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {path}")

print("Knowledge base created successfully.")
