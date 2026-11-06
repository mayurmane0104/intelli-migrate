# tomllib — Parse TOML files — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/tomllib.html](https://docs.python.org/library/tomllib.html)

---

`tomllib` — Parse TOML files[¶](#module-tomllib)

Added in version 3.11.

**Source code:** [Lib/tomllib](https://github.com/python/cpython/tree/3.14/Lib/tomllib)

This module provides an interface for parsing TOML 1.0.0 (Tom’s Obvious Minimal
Language, [https://toml.io](https://toml.io/en/)). This module does not
support writing TOML.

Warning

Be cautious when parsing data from untrusted sources. A malicious TOML string may cause the decoder to consume considerable CPU and memory resources. Limiting the size of data to be parsed is recommended.

See also

The [Tomli-W package](https://pypi.org/project/tomli-w/)
is a TOML writer that can be used in conjunction with this module,
providing a write API familiar to users of the standard library
[ marshal](marshal.html#module-marshal) and 

[modules.](pickle.html#module-pickle)

`pickle`See also

The [TOML Kit package](https://pypi.org/project/tomlkit/)
is a style-preserving TOML library with both read and write capability.
It is a recommended replacement for this module for editing already
existing TOML files.

This module defines the following functions:

- 
tomllib.load(*fp*,*/*,***,*parse_float=float*)[¶](#tomllib.load)
- Read a TOML file. The first argument should be a readable and binary file object. Return a - `dict`- [conversion table](#toml-to-py-table).- *parse_float*will be called with the string of every TOML float to be decoded. By default, this is equivalent to- `float(num_str)`. This can be used to use another datatype or parser for TOML floats (e.g.- `decimal.Decimal`- `dict`- `list`- `ValueError`- A - `TOMLDecodeError`

- 
tomllib.loads(*s*,*/*,***,*parse_float=float*)[¶](#tomllib.loads)
- Load TOML from a - `str`- `dict`- [conversion table](#toml-to-py-table). The- *parse_float*argument has the same meaning as in- `load()`- A - `TOMLDecodeError`

The following exceptions are available:

- 
*exception*tomllib.TOMLDecodeError(*msg*,*doc*,*pos*)[¶](#tomllib.TOMLDecodeError)
- Subclass of - `ValueError`- 
msg[¶](#tomllib.TOMLDecodeError.msg)
- The unformatted error message. 
 - 
doc[¶](#tomllib.TOMLDecodeError.doc)
- The TOML document being parsed. 
 - 
pos[¶](#tomllib.TOMLDecodeError.pos)
- The index of - *doc*where parsing failed.
 - 
lineno[¶](#tomllib.TOMLDecodeError.lineno)
- The line corresponding to - *pos*.
 - 
colno[¶](#tomllib.TOMLDecodeError.colno)
- The column corresponding to - *pos*.
 - Changed in version 3.14: Added the - *msg*,- *doc*and- *pos*parameters. Added the- `msg`- `doc`- `pos`- `lineno`- `colno`- Deprecated since version 3.14: Passing free-form positional arguments is deprecated. 
- 
msg

## Examples[¶](#examples)

Parsing a TOML file:

```
import tomllib
with open("pyproject.toml", "rb") as f:
    data = tomllib.load(f)
```
Parsing a TOML string:

```
import tomllib
toml_str = """
python-version = "3.11.0"
python-implementation = "CPython"
"""
data = tomllib.loads(toml_str)
```
## Conversion Table[¶](#conversion-table)

| TOML | Python | 
|---|---|
| TOML document | dict | 
| string | str | 
| integer | int | 
| float | float (configurable with  | 
| boolean | bool | 
| offset date-time | datetime.datetime ( | 
| local date-time | datetime.datetime ( | 
| local date | datetime.date | 
| local time | datetime.time | 
| array | list | 
| table | dict | 
| inline table | dict | 
| array of tables | list of dicts |