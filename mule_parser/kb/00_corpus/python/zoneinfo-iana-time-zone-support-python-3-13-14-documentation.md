# zoneinfo — IANA time zone support — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/library/zoneinfo.html](https://docs.python.org/3.13/library/zoneinfo.html)

---

`zoneinfo` — IANA time zone support[¶](#module-zoneinfo)

Added in version 3.9.

**Source code:** [Lib/zoneinfo](https://github.com/python/cpython/tree/3.13/Lib/zoneinfo)

The `zoneinfo` module provides a concrete time zone implementation to
support the IANA time zone database as originally specified in [ PEP 615](https://peps.python.org/pep-0615/). By
default, 

`zoneinfo` uses the system’s time zone data if available; if no
system time zone data is available, the library will fall back to using the
first-party [tzdata](https://pypi.org/project/tzdata/)package available on PyPI.

See also

[Availability](intro.html#availability): not WASI.

This module does not work or is not available on WebAssembly. See
[WebAssembly platforms](intro.html#wasm-availability) for more information.

## Using `ZoneInfo`[¶](#using-zoneinfo)

[ ZoneInfo](#zoneinfo.ZoneInfo) is a concrete implementation of the 

[abstract base class, and is intended to be attached to](datetime.html#datetime.tzinfo)

`datetime.tzinfo``tzinfo`, either via
the constructor, the [method or](datetime.html#datetime.datetime.replace)

`datetime.replace`[:](datetime.html#datetime.datetime.astimezone)

`datetime.astimezone````
>>> from zoneinfo import ZoneInfo
>>> import datetime as dt
>>> when = dt.datetime(2020, 10, 31, 12, tzinfo=ZoneInfo("America/Los_Angeles"))
>>> print(when)
2020-10-31 12:00:00-07:00
>>> when.tzname()
'PDT'
```
Datetimes constructed in this way are compatible with datetime arithmetic and handle daylight saving time transitions with no further intervention:

```
>>> when_add = when + dt.timedelta(days=1)
>>> print(when_add)
2020-11-01 12:00:00-08:00
>>> when_add.tzname()
'PST'
```
These time zones also support the [ fold](datetime.html#datetime.datetime.fold) attribute
introduced in 

[. During offset transitions which induce ambiguous times (such as a daylight saving time to standard time transition), the offset from](https://peps.python.org/pep-0495/)

**PEP 495***before*the transition is used when

`fold=0`, and the offset *after*the transition is used when

`fold=1`, for example:```
>>> when = dt.datetime(2020, 11, 1, 1, tzinfo=ZoneInfo("America/Los_Angeles"))
>>> print(when)
2020-11-01 01:00:00-07:00
>>> print(when.replace(fold=1))
2020-11-01 01:00:00-08:00
```
When converting from another time zone, the fold will be set to the correct value:

```
>>> LOS_ANGELES = ZoneInfo("America/Los_Angeles")
>>> when_utc = dt.datetime(2020, 11, 1, 8, tzinfo=dt.timezone.utc)
>>> # Before the PDT -> PST transition
>>> print(when_utc.astimezone(LOS_ANGELES))
2020-11-01 01:00:00-07:00
>>> # After the PDT -> PST transition
>>> print((when_utc + dt.timedelta(hours=1)).astimezone(LOS_ANGELES))
2020-11-01 01:00:00-08:00
```
## Data sources[¶](#data-sources)

The `zoneinfo` module does not directly provide time zone data, and instead
pulls time zone information from the system time zone database or the
first-party PyPI package [tzdata](https://pypi.org/project/tzdata/), if available. Some systems, including
notably Windows systems, do not have an IANA database available, and so for
projects targeting cross-platform compatibility that require time zone data, it
is recommended to declare a dependency on tzdata. If neither system data nor
tzdata are available, all calls to [ ZoneInfo](#zoneinfo.ZoneInfo) will raise

[.](#zoneinfo.ZoneInfoNotFoundError)

`ZoneInfoNotFoundError`### Configuring the data sources[¶](#configuring-the-data-sources)

When `ZoneInfo(key)` is called, the constructor first searches the
directories specified in [ TZPATH](#zoneinfo.TZPATH) for a file matching 

`key`, and on
failure looks for a match in the tzdata package. This behavior can be
configured in three ways:- The default - `TZPATH`- [compile time](#zoneinfo-data-compile-time-config).
- `TZPATH`- [an environment variable](#zoneinfo-data-environment-var).
- At - [runtime](#zoneinfo-data-runtime-config), the search path can be manipulated using the- `reset_tzpath()`

#### Compile-time configuration[¶](#compile-time-configuration)

The default [ TZPATH](#zoneinfo.TZPATH) includes several common deployment locations for the
time zone database (except on Windows, where there are no “well-known”
locations for time zone data). On POSIX systems, downstream distributors and
those building Python from source who know where their system
time zone data is deployed may change the default time zone path by specifying
the compile-time option 

`TZPATH` (or, more likely, the [), which should be a string delimited by](../using/configure.html#cmdoption-with-tzpath)

```
configure
flag --with-tzpath
```
[.](os.html#os.pathsep)

`os.pathsep`On all platforms, the configured value is available as the `TZPATH` key in
[ sysconfig.get_config_var()](sysconfig.html#sysconfig.get_config_var).

#### Environment configuration[¶](#environment-configuration)

When initializing [ TZPATH](#zoneinfo.TZPATH) (either at import time or whenever

[is called with no arguments), the](#zoneinfo.reset_tzpath)

`reset_tzpath()``zoneinfo` module will
use the environment variable `PYTHONTZPATH`, if it exists, to set the search
path.- 
PYTHONTZPATH[¶](#envvar-PYTHONTZPATH)
- This is an - `os.pathsep`- `PYTHONTZPATH`will not be used, but otherwise the behavior when a relative path is specified is implementation-defined; CPython will raise- `InvalidTZPathWarning`

To set the system to ignore the system data and use the tzdata package
instead, set `PYTHONTZPATH=""`.

#### Runtime configuration[¶](#runtime-configuration)

The TZ search path can also be configured at runtime using the
[ reset_tzpath()](#zoneinfo.reset_tzpath) function. This is generally not an advisable operation,
though it is reasonable to use it in test functions that require the use of a
specific time zone path (or require disabling access to the system time zones).

## The `ZoneInfo` class[¶](#the-zoneinfo-class)

- 
*class*zoneinfo.ZoneInfo(*key*)[¶](#zoneinfo.ZoneInfo)
- A concrete - `datetime.tzinfo`- `key`. Calls to the primary constructor will always return objects that compare identically; put another way, barring cache invalidation via- `ZoneInfo.clear_cache()`- `key`, the following assertion will always be true:- a = ZoneInfo(key) b = ZoneInfo(key) assert a is b - `key`must be in the form of a relative, normalized POSIX path, with no up-level references. The constructor will raise- `ValueError`- If no file matching - `key`is found, the constructor will raise- `ZoneInfoNotFoundError`

The `ZoneInfo` class has two alternate constructors:

- 
*classmethod*ZoneInfo.from_file(*file_obj*,*/*,*key=None*)[¶](#zoneinfo.ZoneInfo.from_file)
- Constructs a - `ZoneInfo`object from a file-like object returning bytes (e.g. a file opened in binary mode or an- `io.BytesIO`- The - `key`parameter sets the name of the zone for the purposes of- `__str__()`- `__repr__()`- Objects created via this constructor cannot be pickled (see - [pickling](#pickling)).- `ValueError`- *file_obj*is not a valid TZif file.

- 
*classmethod*ZoneInfo.no_cache(*key*)[¶](#zoneinfo.ZoneInfo.no_cache)
- An alternate constructor that bypasses the constructor’s cache. It is identical to the primary constructor, but returns a new object on each call. This is most likely to be useful for testing or demonstration purposes, but it can also be used to create a system with a different cache invalidation strategy. - Objects created via this constructor will also bypass the cache of a deserializing process when unpickled. - Caution - Using this constructor may change the semantics of your datetimes in surprising ways, only use it if you know that you need to. 

The following class methods are also available:

- 
*classmethod*ZoneInfo.clear_cache(***,*only_keys=None*)[¶](#zoneinfo.ZoneInfo.clear_cache)
- A method for invalidating the cache on the - `ZoneInfo`class. If no arguments are passed, all caches are invalidated and the next call to the primary constructor for each key will return a new instance.- If an iterable of key names is passed to the - `only_keys`parameter, only the specified keys will be removed from the cache. Keys passed to- `only_keys`but not found in the cache are ignored.- Warning - Invoking this function may change the semantics of datetimes using - `ZoneInfo`in surprising ways; this modifies module state and thus may have wide-ranging effects. Only use it if you know that you need to.

The class has one attribute:

- 
ZoneInfo.key[¶](#zoneinfo.ZoneInfo.key)
- This is a read-only - [attribute](../glossary.html#term-attribute)that returns the value of- `key`passed to the constructor, which should be a lookup key in the IANA time zone database (e.g.- `America/New_York`,- `Europe/Paris`or- `Asia/Tokyo`).- For zones constructed from file without specifying a - `key`parameter, this will be set to- `None`.- Note - Although it is a somewhat common practice to expose these to end users, these values are designed to be primary keys for representing the relevant zones and not necessarily user-facing elements. Projects like CLDR (the Unicode Common Locale Data Repository) can be used to get more user-friendly strings from these keys. 

### String representations[¶](#string-representations)

The string representation returned when calling [ str](stdtypes.html#str) on a

[object defaults to using the](#zoneinfo.ZoneInfo)

`ZoneInfo`[attribute (see the note on usage in the attribute documentation):](#zoneinfo.ZoneInfo.key)

`ZoneInfo.key````
>>> zone = ZoneInfo("Pacific/Kwajalein")
>>> str(zone)
'Pacific/Kwajalein'
>>> when = dt.datetime(2020, 4, 1, 3, 15, tzinfo=zone)
>>> f"{when.isoformat()} [{when.tzinfo}]"
'2020-04-01T03:15:00+12:00 [Pacific/Kwajalein]'
```
For objects constructed from a file without specifying a `key` parameter,
`str` falls back to calling [ repr()](functions.html#repr). 

`ZoneInfo`’s `repr` is
implementation-defined and not necessarily stable between versions, but it is
guaranteed not to be a valid `ZoneInfo` key.### Pickle serialization[¶](#pickle-serialization)

Rather than serializing all transition data, `ZoneInfo` objects are
serialized by key, and `ZoneInfo` objects constructed from files (even those
with a value for `key` specified) cannot be pickled.

The behavior of a `ZoneInfo` file depends on how it was constructed:

- `ZoneInfo(key)`: When constructed with the primary constructor, a- `ZoneInfo`object is serialized by key, and when deserialized, the deserializing process uses the primary and thus it is expected that these are the same object as other references to the same time zone. For example, if- `europe_berlin_pkl`is a string containing a pickle constructed from- `ZoneInfo("Europe/Berlin")`, one would expect the following behavior:- >>> a = ZoneInfo("Europe/Berlin") >>> b = pickle.loads(europe_berlin_pkl) >>> a is b True 
- `ZoneInfo.no_cache(key)`: When constructed from the cache-bypassing constructor, the- `ZoneInfo`object is also serialized by key, but when deserialized, the deserializing process uses the cache bypassing constructor. If- `europe_berlin_pkl_nc`is a string containing a pickle constructed from- `ZoneInfo.no_cache("Europe/Berlin")`, one would expect the following behavior:- >>> a = ZoneInfo("Europe/Berlin") >>> b = pickle.loads(europe_berlin_pkl_nc) >>> a is b False 
- `ZoneInfo.from_file(file_obj, /, key=None)`: When constructed from a file, the- `ZoneInfo`object raises an exception on pickling. If an end user wants to pickle a- `ZoneInfo`constructed from a file, it is recommended that they use a wrapper type or a custom serialization function: either serializing by key or storing the contents of the file object and serializing that.

This method of serialization requires that the time zone data for the required
key be available on both the serializing and deserializing side, similar to the
way that references to classes and functions are expected to exist in both the
serializing and deserializing environments. It also means that no guarantees
are made about the consistency of results when unpickling a `ZoneInfo`
pickled in an environment with a different version of the time zone data.

## Functions[¶](#functions)

- 
zoneinfo.available_timezones()[¶](#zoneinfo.available_timezones)
- Get a set containing all the valid keys for IANA time zones available anywhere on the time zone path. This is recalculated on every call to the function. - This function only includes canonical zone names and does not include “special” zones such as those under the - `posix/`and- `right/`directories, or the- `posixrules`zone.- Caution - This function may open a large number of files, as the best way to determine if a file on the time zone path is a valid time zone is to read the “magic string” at the beginning. - Note - These values are not designed to be exposed to end-users; for user facing elements, applications should use something like CLDR (the Unicode Common Locale Data Repository) to get more user-friendly strings. See also the cautionary note on - `ZoneInfo.key`

- 
zoneinfo.reset_tzpath(*to=None*)[¶](#zoneinfo.reset_tzpath)
- Sets or resets the time zone search path ( - `TZPATH`- `TZPATH`is set to the default value.- Calling - `reset_tzpath`will not invalidate the- `ZoneInfo`- `ZoneInfo`constructor will only use the new- `TZPATH`in the case of a cache miss.- The - `to`parameter must be a- [sequence](../glossary.html#term-sequence)of strings or- `os.PathLike`- `ValueError`

## Globals[¶](#globals)

- 
zoneinfo.TZPATH[¶](#zoneinfo.TZPATH)
- A read-only sequence representing the time zone search path – when constructing a - `ZoneInfo`from a key, the key is joined to each entry in the- `TZPATH`, and the first file found is used.- `TZPATH`may contain only absolute paths, never relative paths, regardless of how it is configured.- The object that - `zoneinfo.TZPATH`points to may change in response to a call to- `reset_tzpath()`- `zoneinfo.TZPATH`rather than importing- `TZPATH`from- `zoneinfo`or assigning a long-lived variable to- `zoneinfo.TZPATH`.- For more information on configuring the time zone search path, see - [Configuring the data sources](#zoneinfo-data-configuration).

## Exceptions and warnings[¶](#exceptions-and-warnings)

- 
*exception*zoneinfo.ZoneInfoNotFoundError[¶](#zoneinfo.ZoneInfoNotFoundError)
- Raised when construction of a - `ZoneInfo`- `KeyError`

- 
*exception*zoneinfo.InvalidTZPathWarning[¶](#zoneinfo.InvalidTZPathWarning)
- Raised when - `PYTHONTZPATH`