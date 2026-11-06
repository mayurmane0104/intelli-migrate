# plistlib — Generate and parse Apple .plist files — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/plistlib.html](https://docs.python.org/library/plistlib.html)

---

`plistlib` — Generate and parse Apple `.plist` files[¶](#module-plistlib)

**Source code:** [Lib/plistlib.py](https://github.com/python/cpython/tree/3.14/Lib/plistlib.py)

This module provides an interface for reading and writing the “property list” files used by Apple, primarily on macOS and iOS. This module supports both binary and XML plist files.

The property list (`.plist`) file format is a simple serialization supporting
basic object types, like dictionaries, lists, numbers and strings.  Usually the
top level object is a dictionary.

To write out and to parse a plist file, use the [ dump()](#plistlib.dump) and

[functions.](#plistlib.load)

`load()`To work with plist data in bytes or string objects, use [ dumps()](#plistlib.dumps)
and 

[.](#plistlib.loads)

`loads()`Values can be strings, integers, floats, booleans, tuples, lists, dictionaries
(but only with string keys), [ bytes](stdtypes.html#bytes), 

[or](stdtypes.html#bytearray)

`bytearray`[objects.](datetime.html#datetime.datetime)

`datetime.datetime`Changed in version 3.4: New API, old API deprecated. Support for binary format plists added.

Changed in version 3.8: Support added for reading and writing [ UID](#plistlib.UID) tokens in binary plists as used
by NSKeyedArchiver and NSKeyedUnarchiver.

Changed in version 3.9: Old API removed.

See also

- [PList manual page](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/)
- Apple’s documentation of the file format. 

This module defines the following functions:

- 
plistlib.load(*fp*,***,*fmt=None*,*dict_type=dict*,*aware_datetime=False*)[¶](#plistlib.load)
- Read a plist file. - *fp*should be a readable and binary file object. Return the unpacked root object (which usually is a dictionary).- The - *fmt*is the format of the file and the following values are valid:- `None`
- `FMT_XML`
- `FMT_BINARY`
 - The - *dict_type*is the type used for dictionaries that are read from the plist file.- When - *aware_datetime*is true, fields with type- `datetime.datetime`will be created as- [aware object](datetime.html#datetime-naive-aware), with- `tzinfo`as- `datetime.UTC`- XML data for the - `FMT_XML`- `xml.parsers.expat`- The parser raises - `InvalidFileException`- Added in version 3.4. - Changed in version 3.13: The keyword-only parameter - *aware_datetime*has been added.

- 
plistlib.loads(*data*,***,*fmt=None*,*dict_type=dict*,*aware_datetime=False*)[¶](#plistlib.loads)
- Load a plist from a bytes or string object. See - `load()`- Added in version 3.4. - Changed in version 3.13: - *data*can be a string when- *fmt*equals- `FMT_XML`

- 
plistlib.dump(*value*,*fp*,***,*fmt=FMT_XML*,*sort_keys=True*,*skipkeys=False*,*aware_datetime=False*)[¶](#plistlib.dump)
- Write - *value*to a plist file.- *fp*should be a writable, binary file object.- The - *fmt*argument specifies the format of the plist file and can be one of the following values:- `FMT_XML`
- `FMT_BINARY`
 - When - *sort_keys*is true (the default) the keys for dictionaries will be written to the plist in sorted order, otherwise they will be written in the iteration order of the dictionary.- When - *skipkeys*is false (the default) the function raises- `TypeError`- When - *aware_datetime*is true and any field with type- `datetime.datetime`is set as an- [aware object](datetime.html#datetime-naive-aware), it will convert to UTC timezone before writing it.- A - `TypeError`- An - `OverflowError`- Added in version 3.4. - Changed in version 3.13: The keyword-only parameter - *aware_datetime*has been added.

- 
plistlib.dumps(*value*,***,*fmt=FMT_XML*,*sort_keys=True*,*skipkeys=False*,*aware_datetime=False*)[¶](#plistlib.dumps)
- Return - *value*as a plist-formatted bytes object. See the documentation for- `dump()`- Added in version 3.4. 

The following classes are available:

- 
*class*plistlib.UID(*data*)[¶](#plistlib.UID)
- Wraps an - `int`- 
data[¶](#plistlib.UID.data)
- Int value of the UID. It must be in the range - `0 <= data < 2**64`.
 - Added in version 3.8. 
- 
data

The following constants are available:

- 
plistlib.FMT_XML[¶](#plistlib.FMT_XML)
- The XML format for plist files. - Added in version 3.4. 

- 
plistlib.FMT_BINARY[¶](#plistlib.FMT_BINARY)
- The binary format for plist files - Added in version 3.4. 

The module defines the following exceptions:

- 
*exception*plistlib.InvalidFileException[¶](#plistlib.InvalidFileException)
- Raised when a file cannot be parsed. - Added in version 3.4. 

## Examples[¶](#examples)

Generating a plist:

```
import datetime as dt
import plistlib
pl = dict(
    aString = "Doodah",
    aList = ["A", "B", 12, 32.1, [1, 2, 3]],
    aFloat = 0.1,
    anInt = 728,
    aDict = dict(
        anotherString = "<hello & hi there!>",
        aThirdString = "M\xe4ssig, Ma\xdf",
        aTrueValue = True,
        aFalseValue = False,
    ),
    someData = b"<binary gunk>",
    someMoreData = b"<lots of binary gunk>" * 10,
    aDate = dt.datetime.now()
)
print(plistlib.dumps(pl).decode())
```
Parsing a plist:

```
import plistlib
plist = b"""<plist version="1.0">
<dict>
    <key>foo</key>
    <string>bar</string>
</dict>
</plist>"""
pl = plistlib.loads(plist)
print(pl["foo"])
```