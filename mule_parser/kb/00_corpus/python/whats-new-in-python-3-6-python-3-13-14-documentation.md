# What’s New In Python 3.6 — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/whatsnew/3.6.html](https://docs.python.org/3.13/whatsnew/3.6.html)

---

# What’s New In Python 3.6[¶](#what-s-new-in-python-3-6)

- Editors:
- Elvis Pranskevichus < - [elvis@magic.io](mailto:elvis%40magic.io)>, Yury Selivanov <- [yury@magic.io](mailto:yury%40magic.io)>

This article explains the new features in Python 3.6, compared to 3.5.
Python 3.6 was released on December 23, 2016.  See the
[changelog](https://docs.python.org/3.6/whatsnew/changelog.html) for a full
list of changes.

See also

[ PEP 494](https://peps.python.org/pep-0494/) - Python 3.6 Release Schedule

## Summary – Release highlights[¶](#summary-release-highlights)

New syntax features:

- [PEP 498](#whatsnew36-pep498), formatted string literals.
- [PEP 515](#whatsnew36-pep515), underscores in numeric literals.
- [PEP 526](#whatsnew36-pep526), syntax for variable annotations.
- [PEP 525](#whatsnew36-pep525), asynchronous generators.
- [PEP 530](#whatsnew36-pep530): asynchronous comprehensions.

New library modules:

CPython implementation improvements:

- The - [dict](../library/stdtypes.html#typesmapping)type has been reimplemented to use a- [more compact representation](#whatsnew36-compactdict)based on- [a proposal by Raymond Hettinger](https://mail.python.org/pipermail/python-dev/2012-December/123028.html)and similar to the- [PyPy dict implementation](https://morepypy.blogspot.com/2015/01/faster-more-memory-efficient-and-more.html). This resulted in dictionaries using 20% to 25% less memory when compared to Python 3.5.
- Customization of class creation has been simplified with the - [new protocol](#whatsnew36-pep487).
- The class attribute definition order is - [now preserved](#whatsnew36-pep520).
- The order of elements in - `**kwargs`now- [corresponds to the order](#whatsnew36-pep468)in which keyword arguments were passed to the function.
- DTrace and SystemTap - [probing support](#whatsnew36-tracing)has been added.
- The new - [PYTHONMALLOC](#whatsnew36-pythonmalloc)environment variable can now be used to debug the interpreter memory allocation and access errors.

Significant improvements in the standard library:

- The - `asyncio`- `asyncio`module is no longer provisional and its API is considered stable.
- A new - [file system path protocol](#whatsnew36-pep519)has been implemented to support- [path-like objects](../glossary.html#term-path-like-object). All standard library functions operating on paths have been updated to work with the new protocol.
- The - `datetime`- [Local Time Disambiguation](#whatsnew36-pep495).
- The - `typing`- [improvements](#whatsnew36-typing).
- The - `tracemalloc`- `ResourceWarning`- [PYTHONMALLOC section](#whatsnew36-pythonmalloc)for more information.

Security improvements:

- The new - `secrets`
- On Linux, - `os.urandom()`- **PEP 524**
- The default settings and feature set of the - `ssl`
- The - `hashlib`- `scrypt()`

Windows improvements:

- [PEP 528](#whatsnew36-pep528)and- [PEP 529](#whatsnew36-pep529), Windows filesystem and console encoding changed to UTF-8.
- The - `py.exe`launcher, when used interactively, no longer prefers Python 2 over Python 3 when the user doesn’t specify a version (via command line arguments or a config file). Handling of shebang lines remains unchanged - “python” refers to Python 2 in that case.
- `python.exe`and- `pythonw.exe`have been marked as long-path aware, which means that the 260 character path limit may no longer apply. See- [removing the MAX_PATH limitation](../using/windows.html#max-path)for details.
- A - `._pth`file can be added to force isolated mode and fully specify all search paths to avoid registry and environment lookup. See- [the documentation](../using/windows.html#windows-finding-modules)for more information.
- A - `python36.zip`file now works as a landmark to infer- `PYTHONHOME`- [the documentation](../using/windows.html#windows-finding-modules)for more information.

## New Features[¶](#new-features)

### PEP 498: Formatted string literals[¶](#pep-498-formatted-string-literals)

[ PEP 498](https://peps.python.org/pep-0498/) introduces a new kind of string literals: 

*f-strings*, or

[formatted string literals](../reference/lexical_analysis.html#f-strings).

Formatted string literals are prefixed with `'f'` and are similar to
the format strings accepted by [ str.format()](../library/stdtypes.html#str.format).  They contain replacement
fields surrounded by curly braces.  The replacement fields are expressions,
which are evaluated at run time, and then formatted using the

[protocol:](../library/functions.html#format)

`format()````
>>> name = "Fred"
>>> f"He said his name is {name}."
'He said his name is Fred.'
>>> width = 10
>>> precision = 4
>>> value = decimal.Decimal("12.34567")
>>> f"result: {value:{width}.{precision}}"  # nested fields
'result:      12.35'
```
See also

- **PEP 498**
- PEP written and implemented by Eric V. Smith. 

### PEP 526: Syntax for variable annotations[¶](#pep-526-syntax-for-variable-annotations)

[ PEP 484](https://peps.python.org/pep-0484/) introduced the standard for type annotations of function
parameters, a.k.a. type hints. This PEP adds syntax to Python for annotating
the types of variables including class variables and instance variables:

```
primes: List[int] = []
captain: str  # Note: no initial value!
class Starship:
    stats: Dict[str, int] = {}
```
Just as for function annotations, the Python interpreter does not attach any
particular meaning to variable annotations and only stores them in the
`__annotations__` attribute of a class or module.

In contrast to variable declarations in statically typed languages,
the goal of annotation syntax is to provide an easy way to specify structured
type metadata for third party tools and libraries via the abstract syntax tree
and the `__annotations__` attribute.

### PEP 515: Underscores in Numeric Literals[¶](#pep-515-underscores-in-numeric-literals)

[ PEP 515](https://peps.python.org/pep-0515/) adds the ability to use underscores in numeric literals for
improved readability.  For example:

```
>>> 1_000_000_000_000_000
1000000000000000
>>> 0x_FF_FF_FF_FF
4294967295
```
Single underscores are allowed between digits and after any base specifier. Leading, trailing, or multiple underscores in a row are not allowed.

The [string formatting](../library/string.html#formatspec) language also now has support
for the `'_'` option to signal the use of an underscore for a thousands
separator for floating-point presentation types and for integer
presentation type `'d'`.  For integer presentation types `'b'`,
`'o'`, `'x'`, and `'X'`, underscores will be inserted every 4
digits:

```
>>> '{:_}'.format(1000000)
'1_000_000'
>>> '{:_x}'.format(0xFFFFFFFF)
'ffff_ffff'
```
See also

- **PEP 515**
- PEP written by Georg Brandl and Serhiy Storchaka. 

### PEP 525: Asynchronous Generators[¶](#pep-525-asynchronous-generators)

[ PEP 492](https://peps.python.org/pep-0492/) introduced support for native coroutines and 

`async` / `await`
syntax to Python 3.5.  A notable limitation of the Python 3.5 implementation
is that it was not possible to use `await` and `yield` in the same
function body.  In Python 3.6 this restriction has been lifted, making it
possible to define *asynchronous generators*:

```
async def ticker(delay, to):
    """Yield numbers from 0 to *to* every *delay* seconds."""
    for i in range(to):
        yield i
        await asyncio.sleep(delay)
```
The new syntax allows for faster and more concise code.

See also

- **PEP 525**
- PEP written and implemented by Yury Selivanov. 

### PEP 530: Asynchronous Comprehensions[¶](#pep-530-asynchronous-comprehensions)

[ PEP 530](https://peps.python.org/pep-0530/) adds support for using 

`async for` in list, set, dict
comprehensions and generator expressions:```
result = [i async for i in aiter() if i % 2]
```
Additionally, `await` expressions are supported in all kinds
of comprehensions:

```
result = [await fun() for fun in funcs if await condition()]
```
See also

- **PEP 530**
- PEP written and implemented by Yury Selivanov. 

### PEP 487: Simpler customization of class creation[¶](#pep-487-simpler-customization-of-class-creation)

It is now possible to customize subclass creation without using a metaclass.
The new `__init_subclass__` classmethod will be called on the base class
whenever a new subclass is created:

```
class PluginBase:
    subclasses = []
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)
class Plugin1(PluginBase):
    pass
class Plugin2(PluginBase):
    pass
```
In order to allow zero-argument [ super()](../library/functions.html#super) calls to work correctly from

[implementations, custom metaclasses must ensure that the new](../reference/datamodel.html#object.__init_subclass__)

`__init_subclass__()``__classcell__` namespace entry is propagated to
`type.__new__` (as described in [Creating the class object](../reference/datamodel.html#class-object-creation)).

See also

- **PEP 487**
- PEP written and implemented by Martin Teichmann. 

### PEP 487: Descriptor Protocol Enhancements[¶](#pep-487-descriptor-protocol-enhancements)

[ PEP 487](https://peps.python.org/pep-0487/) extends the descriptor protocol to include the new optional

[method. Whenever a new class is defined, the new method will be called on all descriptors included in the definition, providing them with a reference to the class being defined and the name given to the descriptor within the class namespace. In other words, instances of descriptors can now know the attribute name of the descriptor in the owner class:](../reference/datamodel.html#object.__set_name__)

`__set_name__()````
class IntField:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f'expecting integer in {self.name}')
        instance.__dict__[self.name] = value
    # this is the new initializer:
    def __set_name__(self, owner, name):
        self.name = name
class Model:
    int_field = IntField()
```
See also

- **PEP 487**
- PEP written and implemented by Martin Teichmann. 

### PEP 519: Adding a file system path protocol[¶](#pep-519-adding-a-file-system-path-protocol)

File system paths have historically been represented as [ str](../library/stdtypes.html#str)
or 

[objects. This has led to people who write code which operate on file system paths to assume that such objects are only one of those two types (an](../library/stdtypes.html#bytes)

`bytes`[representing a file descriptor does not count as that is not a file path). Unfortunately that assumption prevents alternative object representations of file system paths like](../library/functions.html#int)

`int`[from working with pre-existing code, including Python’s standard library.](../library/pathlib.html#module-pathlib)

`pathlib`To fix this situation, a new interface represented by
[ os.PathLike](../library/os.html#os.PathLike) has been defined. By implementing the

[method, an object signals that it represents a path. An object can then provide a low-level representation of a file system path as a](../library/os.html#os.PathLike.__fspath__)

`__fspath__()`[or](../library/stdtypes.html#str)

`str`[object. This means an object is considered](../library/stdtypes.html#bytes)

`bytes`[path-like](../glossary.html#term-path-like-object)if it implements

`os.PathLike` or is a `str` or `bytes` object
which represents a file system path. Code can use [,](../library/os.html#os.fspath)

`os.fspath()`[, or](../library/os.html#os.fsdecode)

`os.fsdecode()`[to explicitly get a](../library/os.html#os.fsencode)

`os.fsencode()``str` and/or `bytes` representation of a path-like
object.The built-in [ open()](../library/functions.html#open) function has been updated to accept

[objects, as have all relevant functions in the](../library/os.html#os.PathLike)

`os.PathLike`[and](../library/os.html#module-os)

`os`[modules, and most other functions and classes in the standard library. The](../library/os.path.html#module-os.path)

`os.path`[class and relevant classes in](../library/os.html#os.DirEntry)

`os.DirEntry`[have also been updated to implement](../library/pathlib.html#module-pathlib)

`pathlib``os.PathLike`.The hope is that updating the fundamental functions for operating
on file system paths will lead to third-party code to implicitly
support all [path-like objects](../glossary.html#term-path-like-object) without any
code changes, or at least very minimal ones (e.g. calling
[ os.fspath()](../library/os.html#os.fspath) at the beginning of code before operating on a
path-like object).

Here are some examples of how the new interface allows for
[ pathlib.Path](../library/pathlib.html#pathlib.Path) to be used more easily and transparently with
pre-existing code:

```
>>> import pathlib
>>> with open(pathlib.Path("README")) as f:
...     contents = f.read()
...
>>> import os.path
>>> os.path.splitext(pathlib.Path("some_file.txt"))
('some_file', '.txt')
>>> os.path.join("/a/b", pathlib.Path("c"))
'/a/b/c'
>>> import os
>>> os.fspath(pathlib.Path("some_file.txt"))
'some_file.txt'
```
(Implemented by Brett Cannon, Ethan Furman, Dusty Phillips, and Jelle Zijlstra.)

See also

- **PEP 519**
- PEP written by Brett Cannon and Koos Zevenhoven. 

### PEP 495: Local Time Disambiguation[¶](#pep-495-local-time-disambiguation)

In most world locations, there have been and will be times when local clocks are moved back. In those times, intervals are introduced in which local clocks show the same time twice in the same day. In these situations, the information displayed on a local clock (or stored in a Python datetime instance) is insufficient to identify a particular moment in time.

[ PEP 495](https://peps.python.org/pep-0495/) adds the new 

*fold*attribute to instances of

[and](../library/datetime.html#datetime.datetime)

`datetime.datetime`[classes to differentiate between two moments in time for which local times are the same:](../library/datetime.html#datetime.time)

`datetime.time````
>>> u0 = datetime(2016, 11, 6, 4, tzinfo=timezone.utc)
>>> for i in range(4):
...     u = u0 + i*HOUR
...     t = u.astimezone(Eastern)
...     print(u.time(), 'UTC =', t.time(), t.tzname(), t.fold)
...
04:00:00 UTC = 00:00:00 EDT 0
05:00:00 UTC = 01:00:00 EDT 0
06:00:00 UTC = 01:00:00 EST 1
07:00:00 UTC = 02:00:00 EST 0
```
The values of the [ fold](../library/datetime.html#datetime.datetime.fold) attribute have the
value 

`0` for all instances except those that represent the second
(chronologically) moment in time in an ambiguous case.See also

- **PEP 495**
- PEP written by Alexander Belopolsky and Tim Peters, implementation by Alexander Belopolsky. 

### PEP 529: Change Windows filesystem encoding to UTF-8[¶](#pep-529-change-windows-filesystem-encoding-to-utf-8)

Representing filesystem paths is best performed with str (Unicode) rather than bytes. However, there are some situations where using bytes is sufficient and correct.

Prior to Python 3.6, data loss could result when using bytes paths on Windows.
With this change, using bytes to represent paths is now supported on Windows,
provided those bytes are encoded with the encoding returned by
[ sys.getfilesystemencoding()](../library/sys.html#sys.getfilesystemencoding), which now defaults to 

`'utf-8'`.Applications that do not use str to represent paths should use
[ os.fsencode()](../library/os.html#os.fsencode) and 

[to ensure their bytes are correctly encoded. To revert to the previous behaviour, set](../library/os.html#os.fsdecode)

`os.fsdecode()`[or call](../using/cmdline.html#envvar-PYTHONLEGACYWINDOWSFSENCODING)

`PYTHONLEGACYWINDOWSFSENCODING`[.](../library/sys.html#sys._enablelegacywindowsfsencoding)

`sys._enablelegacywindowsfsencoding()`See [ PEP 529](https://peps.python.org/pep-0529/) for more information and discussion of code modifications that
may be required.

### PEP 528: Change Windows console encoding to UTF-8[¶](#pep-528-change-windows-console-encoding-to-utf-8)

The default console on Windows will now accept all Unicode characters and
provide correctly read str objects to Python code. `sys.stdin`,
`sys.stdout` and `sys.stderr` now default to utf-8 encoding.

This change only applies when using an interactive console, and not when
redirecting files or pipes. To revert to the previous behaviour for interactive
console use, set [ PYTHONLEGACYWINDOWSSTDIO](../using/cmdline.html#envvar-PYTHONLEGACYWINDOWSSTDIO).

See also

- **PEP 528**
- PEP written and implemented by Steve Dower. 

### PEP 520: Preserving Class Attribute Definition Order[¶](#pep-520-preserving-class-attribute-definition-order)

Attributes in a class definition body have a natural ordering: the same
order in which the names appear in the source.  This order is now
preserved in the new class’s [ __dict__](../reference/datamodel.html#type.__dict__) attribute.

Also, the effective default class *execution* namespace (returned from
[type.__prepare__()](../reference/datamodel.html#prepare)) is now an insertion-order-preserving
mapping.

See also

- **PEP 520**
- PEP written and implemented by Eric Snow. 

### PEP 468: Preserving Keyword Argument Order[¶](#pep-468-preserving-keyword-argument-order)

`**kwargs` in a function signature is now guaranteed to be an
insertion-order-preserving mapping.

See also

- **PEP 468**
- PEP written and implemented by Eric Snow. 

### New [dict](../library/stdtypes.html#typesmapping) implementation[¶](#new-dict-implementation)

The [dict](../library/stdtypes.html#typesmapping) type now uses a “compact” representation
based on [a proposal by Raymond Hettinger](https://mail.python.org/pipermail/python-dev/2012-December/123028.html)
which was [first implemented by PyPy](https://morepypy.blogspot.com/2015/01/faster-more-memory-efficient-and-more.html).
The memory usage of the new [ dict()](../library/stdtypes.html#dict) is between 20% and 25% smaller
compared to Python 3.5.

The order-preserving aspect of this new implementation is considered an implementation detail and should not be relied upon (this may change in the future, but it is desired to have this new dict implementation in the language for a few releases before changing the language spec to mandate order-preserving semantics for all current and future Python implementations; this also helps preserve backwards-compatibility with older versions of the language where random iteration order is still in effect, e.g. Python 3.5).

(Contributed by INADA Naoki in [bpo-27350](https://bugs.python.org/issue?@action=redirect&bpo=27350). Idea
[originally suggested by Raymond Hettinger](https://mail.python.org/pipermail/python-dev/2012-December/123028.html).)

### PEP 523: Adding a frame evaluation API to CPython[¶](#pep-523-adding-a-frame-evaluation-api-to-cpython)

While Python provides extensive support to customize how code executes, one place it has not done so is in the evaluation of frame objects. If you wanted some way to intercept frame evaluation in Python there really wasn’t any way without directly manipulating function pointers for defined functions.

[ PEP 523](https://peps.python.org/pep-0523/) changes this by providing an API to make frame
evaluation pluggable at the C level. This will allow for tools such
as debuggers and JITs to intercept frame evaluation before the
execution of Python code begins. This enables the use of alternative
evaluation implementations for Python code, tracking frame
evaluation, etc.

This API is not part of the limited C API and is marked as private to signal that usage of this API is expected to be limited and only applicable to very select, low-level use-cases. Semantics of the API will change with Python as necessary.

See also

- **PEP 523**
- PEP written by Brett Cannon and Dino Viehland. 

### PYTHONMALLOC environment variable[¶](#pythonmalloc-environment-variable)

The new [ PYTHONMALLOC](../using/cmdline.html#envvar-PYTHONMALLOC) environment variable allows setting the Python
memory allocators and installing debug hooks.

It is now possible to install debug hooks on Python memory allocators on Python
compiled in release mode using `PYTHONMALLOC=debug`. Effects of debug hooks:

- Newly allocated memory is filled with the byte - `0xCB`
- Freed memory is filled with the byte - `0xDB`
- Detect violations of the Python memory allocator API. For example, - `PyObject_Free()`- `PyMem_Malloc()`
- Detect writes before the start of a buffer (buffer underflows) 
- Detect writes after the end of a buffer (buffer overflows) 
- Check that the - [GIL](../glossary.html#term-global-interpreter-lock)is held when allocator functions of- `PYMEM_DOMAIN_OBJ`- `PyObject_Malloc()`- `PYMEM_DOMAIN_MEM`- `PyMem_Malloc()`

Checking if the GIL is held is also a new feature of Python 3.6.

See the [ PyMem_SetupDebugHooks()](../c-api/memory.html#c.PyMem_SetupDebugHooks) function for debug hooks on Python
memory allocators.

It is now also possible to force the usage of the `malloc()` allocator of
the C library for all Python memory allocations using `PYTHONMALLOC=malloc`.
This is helpful when using external memory debuggers like Valgrind on
a Python compiled in release mode.

On error, the debug hooks on Python memory allocators now use the
[ tracemalloc](../library/tracemalloc.html#module-tracemalloc) module to get the traceback where a memory block was
allocated.

Example of fatal error on buffer overflow using
`python3.6 -X tracemalloc=5` (store 5 frames in traces):

```
Debug memory block at address p=0x7fbcd41666f8: API 'o'
    4 bytes originally requested
    The 7 pad bytes at p-7 are FORBIDDENBYTE, as expected.
    The 8 pad bytes at tail=0x7fbcd41666fc are not all FORBIDDENBYTE (0xfb):
        at tail+0: 0x02 *** OUCH
        at tail+1: 0xfb
        at tail+2: 0xfb
        at tail+3: 0xfb
        at tail+4: 0xfb
        at tail+5: 0xfb
        at tail+6: 0xfb
        at tail+7: 0xfb
    The block was made by call #1233329 to debug malloc/realloc.
    Data at p: 1a 2b 30 00
Memory block allocated at (most recent call first):
  File "test/test_bytes.py", line 323
  File "unittest/case.py", line 600
  File "unittest/case.py", line 648
  File "unittest/suite.py", line 122
  File "unittest/suite.py", line 84
Fatal Python error: bad trailing pad byte
Current thread 0x00007fbcdbd32700 (most recent call first):
  File "test/test_bytes.py", line 323 in test_hex
  File "unittest/case.py", line 600 in run
  File "unittest/case.py", line 648 in __call__
  File "unittest/suite.py", line 122 in run
  File "unittest/suite.py", line 84 in __call__
  File "unittest/suite.py", line 122 in run
  File "unittest/suite.py", line 84 in __call__
  ...
```
### DTrace and SystemTap probing support[¶](#dtrace-and-systemtap-probing-support)

Python can now be built `--with-dtrace` which enables static markers
for the following events in the interpreter:

- function call/return 
- garbage collection started/finished 
- line of code executed. 

This can be used to instrument running interpreters in production,
without the need to recompile specific [debug builds](../using/configure.html#debug-build) or
providing application-specific profiling/debugging code.

More details in [Instrumenting CPython with DTrace and SystemTap](../howto/instrumentation.html#instrumentation).

The current implementation is tested on Linux and macOS. Additional markers may be added in the future.

(Contributed by Łukasz Langa in [bpo-21590](https://bugs.python.org/issue?@action=redirect&bpo=21590), based on patches by
Jesús Cea Avión, David Malcolm, and Nikhil Benesch.)

## Other Language Changes[¶](#other-language-changes)

Some smaller changes made to the core Python language are:

- A - `global`or- `nonlocal`statement must now textually appear before the first use of the affected name in the same scope. Previously this was a- `SyntaxWarning`
- It is now possible to set a - [special method](../reference/datamodel.html#specialnames)to- `None`to indicate that the corresponding operation is not available. For example, if a class sets- `__iter__()`- `None`, the class is not iterable. (Contributed by Andrew Barnert and Ivan Levkivskyi in- [bpo-25958](https://bugs.python.org/issue?@action=redirect&bpo=25958).)
- Long sequences of repeated traceback lines are now abbreviated as - `"[Previous line repeated {count} more times]"`(see- [traceback](#whatsnew36-traceback)for an example). (Contributed by Emanuel Barry in- [bpo-26823](https://bugs.python.org/issue?@action=redirect&bpo=26823).)
- Import now raises the new exception - `ModuleNotFoundError`- `ImportError`- [bpo-15767](https://bugs.python.org/issue?@action=redirect&bpo=15767).)
- Class methods relying on zero-argument - `super()`will now work correctly when called from metaclass methods during class creation. (Contributed by Martin Teichmann in- [bpo-23722](https://bugs.python.org/issue?@action=redirect&bpo=23722).)

## New Modules[¶](#new-modules)

### secrets[¶](#secrets)

The main purpose of the new [ secrets](../library/secrets.html#module-secrets) module is to provide an obvious way
to reliably generate cryptographically strong pseudo-random values suitable
for managing secrets, such as account authentication, tokens, and similar.

Warning

Note that the pseudo-random generators in the [ random](../library/random.html#module-random) module
should 

*NOT*be used for security purposes. Use

[on Python 3.6+ and](../library/secrets.html#module-secrets)

`secrets`[on Python 3.5 and earlier.](../library/os.html#os.urandom)

`os.urandom()`See also

- **PEP 506**
- PEP written and implemented by Steven D’Aprano. 

## Improved Modules[¶](#improved-modules)

### array[¶](#array)

Exhausted iterators of [ array.array](../library/array.html#array.array) will now stay exhausted even
if the iterated array is extended.  This is consistent with the behavior
of other mutable sequences.

Contributed by Serhiy Storchaka in [bpo-26492](https://bugs.python.org/issue?@action=redirect&bpo=26492).

### ast[¶](#ast)

The new [ ast.Constant](../library/ast.html#ast.Constant) AST node has been added.  It can be used
by external AST optimizers for the purposes of constant folding.

Contributed by Victor Stinner in [bpo-26146](https://bugs.python.org/issue?@action=redirect&bpo=26146).

### asyncio[¶](#asyncio)

Starting with Python 3.6 the `asyncio` module is no longer provisional and its
API is considered stable.

Notable changes in the [ asyncio](../library/asyncio.html#module-asyncio) module since Python 3.5.0
(all backported to 3.5.x due to the provisional status):

- The - `get_event_loop()`- [bpo-28613](https://bugs.python.org/issue?@action=redirect&bpo=28613).)
- The - `ensure_future()`- `loop.run_until_complete()`- [awaitable objects](../glossary.html#term-awaitable). (Contributed by Yury Selivanov.)
- New - `run_coroutine_threadsafe()`
- New - `Transport.is_closing()`
- The - `loop.create_server()`
- New - `loop.create_future()`- [uvloop](https://github.com/MagicStack/uvloop), to provide a faster- `asyncio.Future`- [bpo-27041](https://bugs.python.org/issue?@action=redirect&bpo=27041).)
- New - `loop.get_exception_handler()`- [bpo-27040](https://bugs.python.org/issue?@action=redirect&bpo=27040).)
- New - `StreamReader.readuntil()`
- The performance of - `StreamReader.readexactly()`- [bpo-28370](https://bugs.python.org/issue?@action=redirect&bpo=28370).)
- The - `loop.getaddrinfo()`- `getaddrinfo`function if the address is already resolved. (Contributed by A. Jesse Jiryu Davis.)
- The - `loop.stop()`- [bpo-25593](https://bugs.python.org/issue?@action=redirect&bpo=25593).)
- `Future.set_exception`- `TypeError`- `StopIteration`- [bpo-26221](https://bugs.python.org/issue?@action=redirect&bpo=26221).)
- New - `loop.connect_accepted_socket()`- [bpo-27392](https://bugs.python.org/issue?@action=redirect&bpo=27392).)
- `TCP_NODELAY`flag is now set for all TCP transports by default. (Contributed by Yury Selivanov in- [bpo-27456](https://bugs.python.org/issue?@action=redirect&bpo=27456).)
- New - `loop.shutdown_asyncgens()`- [bpo-28003](https://bugs.python.org/issue?@action=redirect&bpo=28003).)
- `Future`- `Task`- [bpo-26081](https://bugs.python.org/issue?@action=redirect&bpo=26081)and- [bpo-28544](https://bugs.python.org/issue?@action=redirect&bpo=28544).)

### binascii[¶](#binascii)

The [ b2a_base64()](../library/binascii.html#binascii.b2a_base64) function now accepts an optional 

*newline*keyword argument to control whether the newline character is appended to the return value. (Contributed by Victor Stinner in

[bpo-25357](https://bugs.python.org/issue?@action=redirect&bpo=25357).)

### cmath[¶](#cmath)

The new [ cmath.tau](../library/cmath.html#cmath.tau) (

*τ*) constant has been added. (Contributed by Lisa Roach in

[bpo-12345](https://bugs.python.org/issue?@action=redirect&bpo=12345), see

[for details.)](https://peps.python.org/pep-0628/)

**PEP 628**New constants: [ cmath.inf](../library/cmath.html#cmath.inf) and 

[to match](../library/cmath.html#cmath.nan)

`cmath.nan`[and](../library/math.html#math.inf)

`math.inf`[, and also](../library/math.html#math.nan)

`math.nan`[and](../library/cmath.html#cmath.infj)

`cmath.infj`[to match the format used by complex repr. (Contributed by Mark Dickinson in](../library/cmath.html#cmath.nanj)

`cmath.nanj`[bpo-23229](https://bugs.python.org/issue?@action=redirect&bpo=23229).)

### collections[¶](#collections)

The new [ Collection](../library/collections.abc.html#collections.abc.Collection) abstract base class has been
added to represent sized iterable container classes.
(Contributed by Ivan Levkivskyi, docs by Neil Girdhar in 

[bpo-27598](https://bugs.python.org/issue?@action=redirect&bpo=27598).)

The new [ Reversible](../library/collections.abc.html#collections.abc.Reversible) abstract base class represents
iterable classes that also provide the 

[method. (Contributed by Ivan Levkivskyi in](../reference/datamodel.html#object.__reversed__)

`__reversed__()`[bpo-25987](https://bugs.python.org/issue?@action=redirect&bpo=25987).)

The new [ AsyncGenerator](../library/collections.abc.html#collections.abc.AsyncGenerator) abstract base class represents
asynchronous generators.
(Contributed by Yury Selivanov in 

[bpo-28720](https://bugs.python.org/issue?@action=redirect&bpo=28720).)

The [ namedtuple()](../library/collections.html#collections.namedtuple) function now accepts an optional
keyword argument 

*module*, which, when specified, is used for the

[attribute of the returned named tuple class. (Contributed by Raymond Hettinger in](../reference/datamodel.html#type.__module__)

`__module__`[bpo-17941](https://bugs.python.org/issue?@action=redirect&bpo=17941).)

The *verbose* and *rename* arguments for
[ namedtuple()](../library/collections.html#collections.namedtuple) are now keyword-only.
(Contributed by Raymond Hettinger in 

[bpo-25628](https://bugs.python.org/issue?@action=redirect&bpo=25628).)

Recursive [ collections.deque](../library/collections.html#collections.deque) instances can now be pickled.
(Contributed by Serhiy Storchaka in 

[bpo-26482](https://bugs.python.org/issue?@action=redirect&bpo=26482).)

### concurrent.futures[¶](#concurrent-futures)

The [ ThreadPoolExecutor](../library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor)
class constructor now accepts an optional 

*thread_name_prefix*argument to make it possible to customize the names of the threads created by the pool. (Contributed by Gregory P. Smith in

[bpo-27664](https://bugs.python.org/issue?@action=redirect&bpo=27664).)

### contextlib[¶](#contextlib)

The [ contextlib.AbstractContextManager](../library/contextlib.html#contextlib.AbstractContextManager) class has been added to
provide an abstract base class for context managers.  It provides a
sensible default implementation for 

`__enter__()` which returns
`self` and leaves `__exit__()` an abstract method.  A matching
class has been added to the [module as](../library/typing.html#module-typing)

`typing`[. (Contributed by Brett Cannon in](../library/typing.html#typing.ContextManager)

`typing.ContextManager`[bpo-25609](https://bugs.python.org/issue?@action=redirect&bpo=25609).)

### datetime[¶](#datetime)

The [ datetime](../library/datetime.html#datetime.datetime) and 

[classes have the new](../library/datetime.html#datetime.time)

`time`[attribute used to disambiguate local time when necessary. Many functions in the](../library/datetime.html#datetime.time.fold)

`fold`[have been updated to support local time disambiguation. See](../library/datetime.html#module-datetime)

`datetime`[Local Time Disambiguation](#whatsnew36-pep495)section for more information. (Contributed by Alexander Belopolsky in

[bpo-24773](https://bugs.python.org/issue?@action=redirect&bpo=24773).)

The [ datetime.strftime()](../library/datetime.html#datetime.datetime.strftime) and

[methods now support ISO 8601 date directives](../library/datetime.html#datetime.date.strftime)

`date.strftime()``%G`, `%u` and `%V`.
(Contributed by Ashley Anderson in [bpo-12006](https://bugs.python.org/issue?@action=redirect&bpo=12006).)

The [ datetime.isoformat()](../library/datetime.html#datetime.datetime.isoformat) function
now accepts an optional 

*timespec*argument that specifies the number of additional components of the time value to include. (Contributed by Alessandro Cucci and Alexander Belopolsky in

[bpo-19475](https://bugs.python.org/issue?@action=redirect&bpo=19475).)

The [ datetime.combine()](../library/datetime.html#datetime.datetime.combine) now
accepts an optional 

*tzinfo*argument. (Contributed by Alexander Belopolsky in

[bpo-27661](https://bugs.python.org/issue?@action=redirect&bpo=27661).)

### decimal[¶](#decimal)

New [ Decimal.as_integer_ratio()](../library/decimal.html#decimal.Decimal.as_integer_ratio)
method that returns a pair 

`(n, d)` of integers that represent the given
[instance as a fraction, in lowest terms and with a positive denominator:](../library/decimal.html#decimal.Decimal)

`Decimal````
>>> Decimal('-3.14').as_integer_ratio()
(-157, 50)
```
(Contributed by Stefan Krah amd Mark Dickinson in [bpo-25928](https://bugs.python.org/issue?@action=redirect&bpo=25928).)

### distutils[¶](#distutils)

The `default_format` attribute has been removed from
`distutils.command.sdist.sdist` and the `formats`
attribute defaults to `['gztar']`. Although not anticipated,
any code relying on the presence of `default_format` may
need to be adapted. See [bpo-27819](https://bugs.python.org/issue?@action=redirect&bpo=27819) for more details.

### email[¶](#email)

The new email API, enabled via the *policy* keyword to various constructors, is
no longer provisional.  The [ email](../library/email.html#module-email) documentation has been reorganized and
rewritten to focus on the new API, while retaining the old documentation for
the legacy API.  (Contributed by R. David Murray in 

[bpo-24277](https://bugs.python.org/issue?@action=redirect&bpo=24277).)

The [ email.mime](../library/email.mime.html#module-email.mime) classes now all accept an optional 

*policy*keyword. (Contributed by Berker Peksag in

[bpo-27331](https://bugs.python.org/issue?@action=redirect&bpo=27331).)

The [ DecodedGenerator](../library/email.generator.html#email.generator.DecodedGenerator) now supports the 

*policy*keyword.

There is a new [ policy](../library/email.policy.html#module-email.policy) attribute,

[, that controls what class is used by default when the parser creates new message objects. For the](../library/email.policy.html#email.policy.Policy.message_factory)

`message_factory`[policy this is](../library/email.policy.html#email.policy.compat32)

`email.policy.compat32`[, for the new policies it is](../library/email.compat32-message.html#email.message.Message)

`Message`[. (Contributed by R. David Murray in](../library/email.message.html#email.message.EmailMessage)

`EmailMessage`[bpo-20476](https://bugs.python.org/issue?@action=redirect&bpo=20476).)

### encodings[¶](#encodings)

On Windows, added the `'oem'` encoding to use `CP_OEMCP`, and the `'ansi'`
alias for the existing `'mbcs'` encoding, which uses the `CP_ACP` code page.
(Contributed by Steve Dower in [bpo-27959](https://bugs.python.org/issue?@action=redirect&bpo=27959).)

### enum[¶](#enum)

Two new enumeration base classes have been added to the [ enum](../library/enum.html#module-enum) module:

[and](../library/enum.html#enum.Flag)

`Flag`[. Both are used to define constants that can be combined using the bitwise operators. (Contributed by Ethan Furman in](../library/enum.html#enum.IntFlag)

`IntFlag`[bpo-23591](https://bugs.python.org/issue?@action=redirect&bpo=23591).)

Many standard library modules have been updated to use the
[ IntFlag](../library/enum.html#enum.IntFlag) class for their constants.

The new [ enum.auto](../library/enum.html#enum.auto) value can be used to assign values to enum
members automatically:

```
>>> from enum import Enum, auto
>>> class Color(Enum):
...     red = auto()
...     blue = auto()
...     green = auto()
...
>>> list(Color)
[<Color.red: 1>, <Color.blue: 2>, <Color.green: 3>]
```
### faulthandler[¶](#faulthandler)

On Windows, the [ faulthandler](../library/faulthandler.html#module-faulthandler) module now installs a handler for Windows
exceptions: see 

[. (Contributed by Victor Stinner in](../library/faulthandler.html#faulthandler.enable)

`faulthandler.enable()`[bpo-23848](https://bugs.python.org/issue?@action=redirect&bpo=23848).)

### fileinput[¶](#fileinput)

[ hook_encoded()](../library/fileinput.html#fileinput.hook_encoded) now supports the 

*errors*argument. (Contributed by Joseph Hackman in

[bpo-25788](https://bugs.python.org/issue?@action=redirect&bpo=25788).)

### hashlib[¶](#hashlib)

[ hashlib](../library/hashlib.html#module-hashlib) supports OpenSSL 1.1.0.  The minimum recommend version is 1.0.2.
(Contributed by Christian Heimes in 

[bpo-26470](https://bugs.python.org/issue?@action=redirect&bpo=26470).)

BLAKE2 hash functions were added to the module. [ blake2b()](../library/hashlib.html#hashlib.blake2b)
and 

[are always available and support the full feature set of BLAKE2. (Contributed by Christian Heimes in](../library/hashlib.html#hashlib.blake2s)

`blake2s()`[bpo-26798](https://bugs.python.org/issue?@action=redirect&bpo=26798)based on code by Dmitry Chestnykh and Samuel Neves. Documentation written by Dmitry Chestnykh.)

The SHA-3 hash functions [ sha3_224()](../library/hashlib.html#hashlib.sha3_224), 

[,](../library/hashlib.html#hashlib.sha3_256)

`sha3_256()`[,](../library/hashlib.html#hashlib.sha3_384)

`sha3_384()`[, and SHAKE hash functions](../library/hashlib.html#hashlib.sha3_512)

`sha3_512()`[and](../library/hashlib.html#hashlib.shake_128)

`shake_128()`[were added. (Contributed by Christian Heimes in](../library/hashlib.html#hashlib.shake_256)

`shake_256()`[bpo-16113](https://bugs.python.org/issue?@action=redirect&bpo=16113). Keccak Code Package by Guido Bertoni, Joan Daemen, Michaël Peeters, Gilles Van Assche, and Ronny Van Keer.)

The password-based key derivation function [ scrypt()](../library/hashlib.html#hashlib.scrypt) is now
available with OpenSSL 1.1.0 and newer.
(Contributed by Christian Heimes in 

[bpo-27928](https://bugs.python.org/issue?@action=redirect&bpo=27928).)

### http.client[¶](#http-client)

[ HTTPConnection.request()](../library/http.client.html#http.client.HTTPConnection.request) and

[both now support chunked encoding request bodies. (Contributed by Demian Brecht and Rolf Krahl in](../library/http.client.html#http.client.HTTPConnection.endheaders)

`endheaders()`[bpo-12319](https://bugs.python.org/issue?@action=redirect&bpo=12319).)

### idlelib and IDLE[¶](#idlelib-and-idle)

The idlelib package is being modernized and refactored to make IDLE look and work better and to make the code easier to understand, test, and improve. Part of making IDLE look better, especially on Linux and Mac, is using ttk widgets, mostly in the dialogs. As a result, IDLE no longer runs with tcl/tk 8.4. It now requires tcl/tk 8.5 or 8.6. We recommend running the latest release of either.

‘Modernizing’ includes renaming and consolidation of idlelib modules. The
renaming of files with partial uppercase names is similar to the renaming of,
for instance, Tkinter and TkFont to tkinter and tkinter.font in 3.0.  As a
result, imports of idlelib files that worked in 3.5 will usually not work in
3.6.  At least a module name change will be needed (see idlelib/README.txt),
sometimes more.  (Name changes contributed by Al Swiegart and Terry Reedy in
[bpo-24225](https://bugs.python.org/issue?@action=redirect&bpo=24225).  Most idlelib patches since have been and will be part of the
process.)

In compensation, the eventual result with be that some idlelib classes will be easier to use, with better APIs and docstrings explaining them. Additional useful information will be added to idlelib when available.

New in 3.6.2:

Multiple fixes for autocompletion. (Contributed by Louie Lu in [bpo-15786](https://bugs.python.org/issue?@action=redirect&bpo=15786).)

New in 3.6.3:

Module Browser (on the File menu, formerly called Class Browser),
now displays nested functions and classes in addition to top-level
functions and classes.
(Contributed by Guilherme Polo, Cheryl Sabella, and Terry Jan Reedy
in [bpo-1612262](https://bugs.python.org/issue?@action=redirect&bpo=1612262).)

The IDLE features formerly implemented as extensions have been reimplemented
as normal features.  Their settings have been moved from the Extensions tab
to other dialog tabs.
(Contributed by Charles Wohlganger and Terry Jan Reedy in [bpo-27099](https://bugs.python.org/issue?@action=redirect&bpo=27099).)

The Settings dialog (Options, Configure IDLE) has been partly rewritten to improve both appearance and function. (Contributed by Cheryl Sabella and Terry Jan Reedy in multiple issues.)

New in 3.6.4:

The font sample now includes a selection of non-Latin characters so that
users can better see the effect of selecting a particular font.
(Contributed by Terry Jan Reedy in [bpo-13802](https://bugs.python.org/issue?@action=redirect&bpo=13802).)
The sample can be edited to include other characters.
(Contributed by Serhiy Storchaka in [bpo-31860](https://bugs.python.org/issue?@action=redirect&bpo=31860).)

New in 3.6.6:

Editor code context option revised.  Box displays all context lines up to
maxlines.  Clicking on a context line jumps the editor to that line.  Context
colors for custom themes is added to Highlights tab of Settings dialog.
(Contributed by Cheryl Sabella and Terry Jan Reedy in [bpo-33642](https://bugs.python.org/issue?@action=redirect&bpo=33642),
[bpo-33768](https://bugs.python.org/issue?@action=redirect&bpo=33768), and [bpo-33679](https://bugs.python.org/issue?@action=redirect&bpo=33679).)

On Windows, a new API call tells Windows that tk scales for DPI. On Windows
8.1+ or 10, with DPI compatibility properties of the Python binary
unchanged, and a monitor resolution greater than 96 DPI, this should
make text and lines sharper.  It should otherwise have no effect.
(Contributed by Terry Jan Reedy in [bpo-33656](https://bugs.python.org/issue?@action=redirect&bpo=33656).)

New in 3.6.7:

Output over N lines (50 by default) is squeezed down to a button.
N can be changed in the PyShell section of the General page of the
Settings dialog.  Fewer, but possibly extra long, lines can be squeezed by
right clicking on the output.  Squeezed output can be expanded in place
by double-clicking the button or into the clipboard or a separate window
by right-clicking the button.  (Contributed by Tal Einat in [bpo-1529353](https://bugs.python.org/issue?@action=redirect&bpo=1529353).)

### importlib[¶](#importlib)

Import now raises the new exception [ ModuleNotFoundError](../library/exceptions.html#ModuleNotFoundError)
(subclass of 

[) when it cannot find a module. Code that current checks for](../library/exceptions.html#ImportError)

`ImportError``ImportError` (in try-except) will still work.
(Contributed by Eric Snow in [bpo-15767](https://bugs.python.org/issue?@action=redirect&bpo=15767).)

[ importlib.util.LazyLoader](../library/importlib.html#importlib.util.LazyLoader) now calls

[on the wrapped loader, removing the restriction that](../library/importlib.html#importlib.abc.Loader.create_module)

`create_module()`[and](../library/importlib.html#importlib.machinery.BuiltinImporter)

`importlib.machinery.BuiltinImporter`[couldn’t be used with](../library/importlib.html#importlib.machinery.ExtensionFileLoader)

`importlib.machinery.ExtensionFileLoader``importlib.util.LazyLoader`.[ importlib.util.cache_from_source()](../library/importlib.html#importlib.util.cache_from_source),

[, and](../library/importlib.html#importlib.util.source_from_cache)

`importlib.util.source_from_cache()`[now accept a](../library/importlib.html#importlib.util.spec_from_file_location)

`importlib.util.spec_from_file_location()`[path-like object](../glossary.html#term-path-like-object).

### inspect[¶](#inspect)

The [ inspect.signature()](../library/inspect.html#inspect.signature) function now reports the
implicit 

`.0` parameters generated by the compiler for comprehension and
generator expression scopes as if they were positional-only parameters called
`implicit0`. (Contributed by Jelle Zijlstra in [bpo-19611](https://bugs.python.org/issue?@action=redirect&bpo=19611).)

To reduce code churn when upgrading from Python 2.7 and the legacy
`inspect.getargspec()` API, the previously documented deprecation of
[ inspect.getfullargspec()](../library/inspect.html#inspect.getfullargspec) has been reversed. While this function is
convenient for single/source Python 2/3 code bases, the richer

[interface remains the recommended approach for new code. (Contributed by Nick Coghlan in](../library/inspect.html#inspect.signature)

`inspect.signature()`[bpo-27172](https://bugs.python.org/issue?@action=redirect&bpo=27172))

### json[¶](#json)

[ json.load()](../library/json.html#json.load) and 

[now support binary input. Encoded JSON should be represented using either UTF-8, UTF-16, or UTF-32. (Contributed by Serhiy Storchaka in](../library/json.html#json.loads)

`json.loads()`[bpo-17909](https://bugs.python.org/issue?@action=redirect&bpo=17909).)

### logging[¶](#logging)

The new [ WatchedFileHandler.reopenIfNeeded()](../library/logging.handlers.html#logging.handlers.WatchedFileHandler.reopenIfNeeded)
method has been added to add the ability to check if the log file needs to
be reopened.
(Contributed by Marian Horban in 

[bpo-24884](https://bugs.python.org/issue?@action=redirect&bpo=24884).)

### math[¶](#math)

The tau (*τ*) constant has been added to the [ math](../library/math.html#module-math) and 

[modules. (Contributed by Lisa Roach in](../library/cmath.html#module-cmath)

`cmath`[bpo-12345](https://bugs.python.org/issue?@action=redirect&bpo=12345), see

[for details.)](https://peps.python.org/pep-0628/)

**PEP 628**### multiprocessing[¶](#multiprocessing)

[Proxy Objects](../library/multiprocessing.html#multiprocessing-proxy-objects) returned by
[ multiprocessing.Manager()](../library/multiprocessing.html#multiprocessing.Manager) can now be nested.
(Contributed by Davin Potts in 

[bpo-6766](https://bugs.python.org/issue?@action=redirect&bpo=6766).)

### os[¶](#os)

See the summary of [PEP 519](#whatsnew36-pep519) for details on how the
[ os](../library/os.html#module-os) and 

[modules now support](../library/os.path.html#module-os.path)

`os.path`[path-like objects](../glossary.html#term-path-like-object).

[ scandir()](../library/os.html#os.scandir) now supports 

[paths on Windows.](../library/stdtypes.html#bytes)

`bytes`A new [ close()](../library/os.html#os.scandir.close) method allows explicitly closing a

[iterator. The](../library/os.html#os.scandir)

`scandir()``scandir()` iterator now
supports the [context manager](../glossary.html#term-context-manager)protocol. If a

`scandir()`
iterator is neither exhausted nor explicitly closed a [will be emitted in its destructor. (Contributed by Serhiy Storchaka in](../library/exceptions.html#ResourceWarning)

`ResourceWarning`[bpo-25994](https://bugs.python.org/issue?@action=redirect&bpo=25994).)

On Linux, [ os.urandom()](../library/os.html#os.urandom) now blocks until the system urandom entropy pool
is initialized to increase the security. See the 

[for the rationale.](https://peps.python.org/pep-0524/)

**PEP 524**The Linux `getrandom()` syscall (get random bytes) is now exposed as the new
[ os.getrandom()](../library/os.html#os.getrandom) function.
(Contributed by Victor Stinner, part of the 

[)](https://peps.python.org/pep-0524/)

**PEP 524**### pathlib[¶](#pathlib)

[ pathlib](../library/pathlib.html#module-pathlib) now supports 

[path-like objects](../glossary.html#term-path-like-object). (Contributed by Brett Cannon in

[bpo-27186](https://bugs.python.org/issue?@action=redirect&bpo=27186).)

See the summary of [PEP 519](#whatsnew36-pep519) for details.

### pdb[¶](#pdb)

The [ Pdb](../library/pdb.html#pdb.Pdb) class constructor has a new optional 

*readrc*argument to control whether

`.pdbrc` files should be read.### pickle[¶](#pickle)

Objects that need `__new__` called with keyword arguments can now be pickled
using [pickle protocols](../library/pickle.html#pickle-protocols) older than protocol version 4.
Protocol version 4 already supports this case.  (Contributed by Serhiy
Storchaka in [bpo-24164](https://bugs.python.org/issue?@action=redirect&bpo=24164).)

### pickletools[¶](#pickletools)

[ pickletools.dis()](../library/pickletools.html#pickletools.dis) now outputs the implicit memo index for the

`MEMOIZE` opcode.
(Contributed by Serhiy Storchaka in [bpo-25382](https://bugs.python.org/issue?@action=redirect&bpo=25382).)

### pydoc[¶](#pydoc)

The [ pydoc](../library/pydoc.html#module-pydoc) module has learned to respect the 

`MANPAGER`
environment variable.
(Contributed by Matthias Klose in [bpo-8637](https://bugs.python.org/issue?@action=redirect&bpo=8637).)

[ help()](../library/functions.html#help) and 

[can now list named tuple fields in the order they were defined rather than alphabetically. (Contributed by Raymond Hettinger in](../library/pydoc.html#module-pydoc)

`pydoc`[bpo-24879](https://bugs.python.org/issue?@action=redirect&bpo=24879).)

### random[¶](#random)

The new [ choices()](../library/random.html#random.choices) function returns a list of elements of
specified size from the given population with optional weights.
(Contributed by Raymond Hettinger in 

[bpo-18844](https://bugs.python.org/issue?@action=redirect&bpo=18844).)

### re[¶](#re)

Added support of modifier spans in regular expressions.  Examples:
`'(?i:p)ython'` matches `'python'` and `'Python'`, but not `'PYTHON'`;
`'(?i)g(?-i:v)r'` matches `'GvR'` and `'gvr'`, but not `'GVR'`.
(Contributed by Serhiy Storchaka in [bpo-433028](https://bugs.python.org/issue?@action=redirect&bpo=433028).)

Match object groups can be accessed by `__getitem__`, which is
equivalent to `group()`.  So `mo['name']` is now equivalent to
`mo.group('name')`.  (Contributed by Eric Smith in [bpo-24454](https://bugs.python.org/issue?@action=redirect&bpo=24454).)

[ Match](../library/re.html#re.Match) objects now support

[as group indices. (Contributed by Jeroen Demeyer and Xiang Zhang in](../reference/datamodel.html#object.__index__)

`index-like objects`[bpo-27177](https://bugs.python.org/issue?@action=redirect&bpo=27177).)

### readline[¶](#readline)

Added [ set_auto_history()](../library/readline.html#readline.set_auto_history) to enable or disable
automatic addition of input to the history list.  (Contributed by
Tyler Crompton in 

[bpo-26870](https://bugs.python.org/issue?@action=redirect&bpo=26870).)

### rlcompleter[¶](#rlcompleter)

Private and special attribute names now are omitted unless the prefix starts
with underscores.  A space or a colon is added after some completed keywords.
(Contributed by Serhiy Storchaka in [bpo-25011](https://bugs.python.org/issue?@action=redirect&bpo=25011) and [bpo-25209](https://bugs.python.org/issue?@action=redirect&bpo=25209).)

### shlex[¶](#shlex)

The [ shlex](../library/shlex.html#shlex.shlex) has much

[improved shell compatibility](../library/shlex.html#improved-shell-compatibility)through the new

*punctuation_chars*argument to control which characters are treated as punctuation. (Contributed by Vinay Sajip in

[bpo-1521950](https://bugs.python.org/issue?@action=redirect&bpo=1521950).)

### site[¶](#site)

When specifying paths to add to [ sys.path](../library/sys.html#sys.path) in a 

`.pth` file,
you may now specify file paths on top of directories (e.g. zip files).
(Contributed by Wolfgang Langner in [bpo-26587](https://bugs.python.org/issue?@action=redirect&bpo=26587)).

### sqlite3[¶](#sqlite3)

[ sqlite3.Cursor.lastrowid](../library/sqlite3.html#sqlite3.Cursor.lastrowid) now supports the 

`REPLACE` statement.
(Contributed by Alex LordThorsen in [bpo-16864](https://bugs.python.org/issue?@action=redirect&bpo=16864).)

### socket[¶](#socket)

The [ ioctl()](../library/socket.html#socket.socket.ioctl) function now supports the

[control code. (Contributed by Daniel Stokes in](../library/socket.html#socket.SIO_LOOPBACK_FAST_PATH)

`SIO_LOOPBACK_FAST_PATH`[bpo-26536](https://bugs.python.org/issue?@action=redirect&bpo=26536).)

The [ getsockopt()](../library/socket.html#socket.socket.getsockopt) constants 

`SO_DOMAIN`,
`SO_PROTOCOL`, `SO_PEERSEC`, and `SO_PASSSEC` are now supported.
(Contributed by Christian Heimes in [bpo-26907](https://bugs.python.org/issue?@action=redirect&bpo=26907).)

The [ setsockopt()](../library/socket.html#socket.socket.setsockopt) now supports the

`setsockopt(level, optname, None, optlen: int)` form.
(Contributed by Christian Heimes in [bpo-27744](https://bugs.python.org/issue?@action=redirect&bpo=27744).)

The socket module now supports the address family
[ AF_ALG](../library/socket.html#socket.AF_ALG) to interface with Linux Kernel crypto API. 

`ALG_*`,
`SOL_ALG` and [were added. (Contributed by Christian Heimes in](../library/socket.html#socket.socket.sendmsg_afalg)

`sendmsg_afalg()`[bpo-27744](https://bugs.python.org/issue?@action=redirect&bpo=27744)with support from Victor Stinner.)

New Linux constants `TCP_USER_TIMEOUT` and `TCP_CONGESTION` were added.
(Contributed by Omar Sandoval, [bpo-26273](https://bugs.python.org/issue?@action=redirect&bpo=26273)).

### socketserver[¶](#socketserver)

Servers based on the [ socketserver](../library/socketserver.html#module-socketserver) module, including those
defined in 

[,](../library/http.server.html#module-http.server)

`http.server`[and](../library/xmlrpc.server.html#module-xmlrpc.server)

`xmlrpc.server`[, now support the](../library/wsgiref.html#module-wsgiref.simple_server)

`wsgiref.simple_server`[context manager](../glossary.html#term-context-manager)protocol. (Contributed by Aviv Palivoda in

[bpo-26404](https://bugs.python.org/issue?@action=redirect&bpo=26404).)

The [ wfile](../library/socketserver.html#socketserver.DatagramRequestHandler.wfile) attribute of

[classes now implements the](../library/socketserver.html#socketserver.StreamRequestHandler)

`StreamRequestHandler`[writable interface. In particular, calling](../library/io.html#io.BufferedIOBase)

`io.BufferedIOBase`[is now guaranteed to send the data in full. (Contributed by Martin Panter in](../library/io.html#io.BufferedIOBase.write)

`write()`[bpo-26721](https://bugs.python.org/issue?@action=redirect&bpo=26721).)

### ssl[¶](#ssl)

[ ssl](../library/ssl.html#module-ssl) supports OpenSSL 1.1.0.  The minimum recommend version is 1.0.2.
(Contributed by Christian Heimes in 

[bpo-26470](https://bugs.python.org/issue?@action=redirect&bpo=26470).)

3DES has been removed from the default cipher suites and ChaCha20 Poly1305
cipher suites have been added.
(Contributed by Christian Heimes in [bpo-27850](https://bugs.python.org/issue?@action=redirect&bpo=27850) and [bpo-27766](https://bugs.python.org/issue?@action=redirect&bpo=27766).)

[ SSLContext](../library/ssl.html#ssl.SSLContext) has better default configuration for options
and ciphers.
(Contributed by Christian Heimes in 

[bpo-28043](https://bugs.python.org/issue?@action=redirect&bpo=28043).)

SSL session can be copied from one client-side connection to another
with the new [ SSLSession](../library/ssl.html#ssl.SSLSession) class.  TLS session resumption can
speed up the initial handshake, reduce latency and improve performance
(Contributed by Christian Heimes in 

[bpo-19500](https://bugs.python.org/issue?@action=redirect&bpo=19500)based on a draft by Alex Warhawk.)

The new [ get_ciphers()](../library/ssl.html#ssl.SSLContext.get_ciphers) method can be used to
get a list of enabled ciphers in order of cipher priority.

All constants and flags have been converted to [ IntEnum](../library/enum.html#enum.IntEnum) and

[. (Contributed by Christian Heimes in](../library/enum.html#enum.IntFlag)

`IntFlag`[bpo-28025](https://bugs.python.org/issue?@action=redirect&bpo=28025).)

Server and client-side specific TLS protocols for [ SSLContext](../library/ssl.html#ssl.SSLContext)
were added.
(Contributed by Christian Heimes in 

[bpo-28085](https://bugs.python.org/issue?@action=redirect&bpo=28085).)

Added [ ssl.SSLContext.post_handshake_auth](../library/ssl.html#ssl.SSLContext.post_handshake_auth) to enable and

[to initiate TLS 1.3 post-handshake authentication. (Contributed by Christian Heimes in](../library/ssl.html#ssl.SSLSocket.verify_client_post_handshake)

`ssl.SSLSocket.verify_client_post_handshake()`[gh-78851](https://github.com/python/cpython/issues/78851).)

### statistics[¶](#statistics)

A new [ harmonic_mean()](../library/statistics.html#statistics.harmonic_mean) function has been added.
(Contributed by Steven D’Aprano in 

[bpo-27181](https://bugs.python.org/issue?@action=redirect&bpo=27181).)

### struct[¶](#struct)

[ struct](../library/struct.html#module-struct) now supports IEEE 754 half-precision floats via the 

`'e'`
format specifier.
(Contributed by Eli Stevens, Mark Dickinson in [bpo-11734](https://bugs.python.org/issue?@action=redirect&bpo=11734).)

### subprocess[¶](#subprocess)

[ subprocess.Popen](../library/subprocess.html#subprocess.Popen) destructor now emits a 

[warning if the child process is still running. Use the context manager protocol (](../library/exceptions.html#ResourceWarning)

`ResourceWarning````
with
proc: ...
```
) or explicitly call the [method to read the exit status of the child process. (Contributed by Victor Stinner in](../library/subprocess.html#subprocess.Popen.wait)

`wait()`[bpo-26741](https://bugs.python.org/issue?@action=redirect&bpo=26741).)

The [ subprocess.Popen](../library/subprocess.html#subprocess.Popen) constructor and all functions that pass arguments
through to it now accept 

*encoding*and

*errors*arguments. Specifying either of these will enable text mode for the

*stdin*,

*stdout*and

*stderr*streams. (Contributed by Steve Dower in

[bpo-6135](https://bugs.python.org/issue?@action=redirect&bpo=6135).)

### sys[¶](#sys)

The new [ getfilesystemencodeerrors()](../library/sys.html#sys.getfilesystemencodeerrors) function returns the name of
the error mode used to convert between Unicode filenames and bytes filenames.
(Contributed by Steve Dower in 

[bpo-27781](https://bugs.python.org/issue?@action=redirect&bpo=27781).)

On Windows the return value of the [ getwindowsversion()](../library/sys.html#sys.getwindowsversion) function
now includes the 

*platform_version*field which contains the accurate major version, minor version and build number of the current operating system, rather than the version that is being emulated for the process (Contributed by Steve Dower in

[bpo-27932](https://bugs.python.org/issue?@action=redirect&bpo=27932).)

### telnetlib[¶](#telnetlib)

`telnetlib.Telnet` is now a context manager (contributed by
Stéphane Wirtel in [bpo-25485](https://bugs.python.org/issue?@action=redirect&bpo=25485)).

### time[¶](#time)

The [ struct_time](../library/time.html#time.struct_time) attributes 

`tm_gmtoff` and
`tm_zone` are now available on all platforms.### timeit[¶](#timeit)

The new [ Timer.autorange()](../library/timeit.html#timeit.Timer.autorange) convenience
method has been added to call 

[repeatedly so that the total run time is greater or equal to 200 milliseconds. (Contributed by Steven D’Aprano in](../library/timeit.html#timeit.Timer.timeit)

`Timer.timeit()`[bpo-6422](https://bugs.python.org/issue?@action=redirect&bpo=6422).)

[ timeit](../library/timeit.html#module-timeit) now warns when there is substantial (4x) variance
between best and worst times.
(Contributed by Serhiy Storchaka in 

[bpo-23552](https://bugs.python.org/issue?@action=redirect&bpo=23552).)

### tkinter[¶](#tkinter)

Added methods `Variable.trace_add()`,
`Variable.trace_remove()` and `trace_info()`
in the `tkinter.Variable` class.  They replace old methods
`trace_variable()`, `trace()`,
`trace_vdelete()` and
`trace_vinfo()` that use obsolete Tcl commands and might
not work in future versions of Tcl.
(Contributed by Serhiy Storchaka in [bpo-22115](https://bugs.python.org/issue?@action=redirect&bpo=22115)).

### traceback[¶](#traceback)

Both the traceback module and the interpreter’s builtin exception display now abbreviate long sequences of repeated lines in tracebacks as shown in the following example:

```
>>> def f(): f()
...
>>> f()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in f
  File "<stdin>", line 1, in f
  File "<stdin>", line 1, in f
  [Previous line repeated 995 more times]
RecursionError: maximum recursion depth exceeded
```
(Contributed by Emanuel Barry in [bpo-26823](https://bugs.python.org/issue?@action=redirect&bpo=26823).)

### tracemalloc[¶](#tracemalloc)

The [ tracemalloc](../library/tracemalloc.html#module-tracemalloc) module now supports tracing memory allocations in
multiple different address spaces.

The new [ DomainFilter](../library/tracemalloc.html#tracemalloc.DomainFilter) filter class has been added
to filter block traces by their address space (domain).

(Contributed by Victor Stinner in [bpo-26588](https://bugs.python.org/issue?@action=redirect&bpo=26588).)

### typing[¶](#typing)

Since the [ typing](../library/typing.html#module-typing) module is 

[provisional](../glossary.html#term-provisional-API), all changes introduced in Python 3.6 have also been backported to Python 3.5.x.

The [ typing](../library/typing.html#module-typing) module has a much improved support for generic type
aliases.  For example 

`Dict[str, Tuple[S, T]]` is now a valid
type annotation.
(Contributed by Guido van Rossum in [Github #195](https://github.com/python/typing/pull/195).)

The [ typing.ContextManager](../library/typing.html#typing.ContextManager) class has been added for
representing 

[. (Contributed by Brett Cannon in](../library/contextlib.html#contextlib.AbstractContextManager)

`contextlib.AbstractContextManager`[bpo-25609](https://bugs.python.org/issue?@action=redirect&bpo=25609).)

The [ typing.Collection](../library/typing.html#typing.Collection) class has been added for
representing 

[. (Contributed by Ivan Levkivskyi in](../library/collections.abc.html#collections.abc.Collection)

`collections.abc.Collection`[bpo-27598](https://bugs.python.org/issue?@action=redirect&bpo=27598).)

The [ typing.ClassVar](../library/typing.html#typing.ClassVar) type construct has been added to
mark class variables.  As introduced in 

[, a variable annotation wrapped in ClassVar indicates that a given attribute is intended to be used as a class variable and should not be set on instances of that class. (Contributed by Ivan Levkivskyi in](https://peps.python.org/pep-0526/)

**PEP 526**[Github #280](https://github.com/python/typing/pull/280).)

A new [ TYPE_CHECKING](../library/typing.html#typing.TYPE_CHECKING) constant that is assumed to be

`True` by the static type checkers, but is `False` at runtime.
(Contributed by Guido van Rossum in [Github #230](https://github.com/python/typing/issues/230).)

A new [ NewType()](../library/typing.html#typing.NewType) helper function has been added to create
lightweight distinct types for annotations:

```
from typing import NewType
UserId = NewType('UserId', int)
some_id = UserId(524313)
```
The static type checker will treat the new type as if it were a subclass
of the original type.  (Contributed by Ivan Levkivskyi in [Github #189](https://github.com/python/typing/issues/189).)

### unicodedata[¶](#unicodedata)

The [ unicodedata](../library/unicodedata.html#module-unicodedata) module now uses data from 

[Unicode 9.0.0](https://unicode.org/versions/Unicode9.0.0/). (Contributed by Benjamin Peterson.)

### unittest.mock[¶](#unittest-mock)

The [ Mock](../library/unittest.mock.html#unittest.mock.Mock) class has the following improvements:

- Two new methods, - `Mock.assert_called()`- `Mock.assert_called_once()`- [bpo-26323](https://bugs.python.org/issue?@action=redirect&bpo=26323).)
- The - `Mock.reset_mock()`- *return_value*and- *side_effect*. (Contributed by Kushal Das in- [bpo-21271](https://bugs.python.org/issue?@action=redirect&bpo=21271).)

### urllib.request[¶](#urllib-request)

If a HTTP request has a file or iterable body (other than a
bytes object) but no `Content-Length` header, rather than
throwing an error, [ AbstractHTTPHandler](../library/urllib.request.html#urllib.request.HTTPHandler)
now falls back to use chunked transfer encoding.
(Contributed by Demian Brecht and Rolf Krahl in 

[bpo-12319](https://bugs.python.org/issue?@action=redirect&bpo=12319).)

### urllib.robotparser[¶](#urllib-robotparser)

[ RobotFileParser](../library/urllib.robotparser.html#urllib.robotparser.RobotFileParser) now supports the 

`Crawl-delay` and
`Request-rate` extensions.
(Contributed by Nikolay Bogoychev in [bpo-16099](https://bugs.python.org/issue?@action=redirect&bpo=16099).)

### venv[¶](#venv)

[ venv](../library/venv.html#module-venv) accepts a new parameter 

`--prompt`. This parameter provides an
alternative prefix for the virtual environment. (Proposed by Łukasz Balcerzak
and ported to 3.6 by Stéphane Wirtel in [bpo-22829](https://bugs.python.org/issue?@action=redirect&bpo=22829).)

### warnings[¶](#warnings)

A new optional *source* parameter has been added to the
[ warnings.warn_explicit()](../library/warnings.html#warnings.warn_explicit) function: the destroyed object which emitted a

[. A](../library/exceptions.html#ResourceWarning)

`ResourceWarning`*source*attribute has also been added to

`warnings.WarningMessage` (contributed by Victor Stinner in
[bpo-26568](https://bugs.python.org/issue?@action=redirect&bpo=26568)and

[bpo-26567](https://bugs.python.org/issue?@action=redirect&bpo=26567)).

When a [ ResourceWarning](../library/exceptions.html#ResourceWarning) warning is logged, the 

[module is now used to try to retrieve the traceback where the destroyed object was allocated.](../library/tracemalloc.html#module-tracemalloc)

`tracemalloc`Example with the script `example.py`:

```
import warnings
def func():
    return open(__file__)
f = func()
f = None
```
Output of the command `python3.6 -Wd -X tracemalloc=5 example.py`:

```
example.py:7: ResourceWarning: unclosed file <_io.TextIOWrapper name='example.py' mode='r' encoding='UTF-8'>
  f = None
Object allocated at (most recent call first):
  File "example.py", lineno 4
    return open(__file__)
  File "example.py", lineno 6
    f = func()
```
The “Object allocated at” traceback is new and is only displayed if
[ tracemalloc](../library/tracemalloc.html#module-tracemalloc) is tracing Python memory allocations and if the

[module was already imported.](../library/warnings.html#module-warnings)

`warnings`### winreg[¶](#winreg)

Added the 64-bit integer type [ REG_QWORD](../library/winreg.html#winreg.REG_QWORD).
(Contributed by Clement Rouault in 

[bpo-23026](https://bugs.python.org/issue?@action=redirect&bpo=23026).)

### winsound[¶](#winsound)

Allowed keyword arguments to be passed to [ Beep](../library/winsound.html#winsound.Beep),

[, and](../library/winsound.html#winsound.MessageBeep)

`MessageBeep`[(](../library/winsound.html#winsound.PlaySound)

`PlaySound`[bpo-27982](https://bugs.python.org/issue?@action=redirect&bpo=27982)).

### xmlrpc.client[¶](#xmlrpc-client)

The [ xmlrpc.client](../library/xmlrpc.client.html#module-xmlrpc.client) module now supports unmarshalling
additional data types used by the Apache XML-RPC implementation
for numerics and 

`None`.
(Contributed by Serhiy Storchaka in [bpo-26885](https://bugs.python.org/issue?@action=redirect&bpo=26885).)

### zipfile[¶](#zipfile)

A new [ ZipInfo.from_file()](../library/zipfile.html#zipfile.ZipInfo.from_file) class method
allows making a 

[instance from a filesystem file. A new](../library/zipfile.html#zipfile.ZipInfo)

`ZipInfo`[method can be used to check if the](../library/zipfile.html#zipfile.ZipInfo.is_dir)

`ZipInfo.is_dir()``ZipInfo` instance represents a directory.
(Contributed by Thomas Kluyver in [bpo-26039](https://bugs.python.org/issue?@action=redirect&bpo=26039).)

The [ ZipFile.open()](../library/zipfile.html#zipfile.ZipFile.open) method can now be used to
write data into a ZIP file, as well as for extracting data.
(Contributed by Thomas Kluyver in 

[bpo-26039](https://bugs.python.org/issue?@action=redirect&bpo=26039).)

### zlib[¶](#zlib)

The [ compress()](../library/zlib.html#zlib.compress) and 

[functions now accept keyword arguments. (Contributed by Aviv Palivoda in](../library/zlib.html#zlib.decompress)

`decompress()`[bpo-26243](https://bugs.python.org/issue?@action=redirect&bpo=26243)and Xiang Zhang in

[bpo-16764](https://bugs.python.org/issue?@action=redirect&bpo=16764)respectively.)

## Optimizations[¶](#optimizations)

- The Python interpreter now uses a 16-bit wordcode instead of bytecode which made a number of opcode optimizations possible. (Contributed by Demur Rumed with input and reviews from Serhiy Storchaka and Victor Stinner in - [bpo-26647](https://bugs.python.org/issue?@action=redirect&bpo=26647)and- [bpo-28050](https://bugs.python.org/issue?@action=redirect&bpo=28050).)
- The - `asyncio.Future`- [bpo-26081](https://bugs.python.org/issue?@action=redirect&bpo=26081).)
- The - `asyncio.Task`- [bpo-28544](https://bugs.python.org/issue?@action=redirect&bpo=28544).)
- Various implementation improvements in the - `typing`
- The ASCII decoder is now up to 60 times as fast for error handlers - `surrogateescape`,- `ignore`and- `replace`(Contributed by Victor Stinner in- [bpo-24870](https://bugs.python.org/issue?@action=redirect&bpo=24870)).
- The ASCII and the Latin1 encoders are now up to 3 times as fast for the error handler - `surrogateescape`(Contributed by Victor Stinner in- [bpo-25227](https://bugs.python.org/issue?@action=redirect&bpo=25227)).
- The UTF-8 encoder is now up to 75 times as fast for error handlers - `ignore`,- `replace`,- `surrogateescape`,- `surrogatepass`(Contributed by Victor Stinner in- [bpo-25267](https://bugs.python.org/issue?@action=redirect&bpo=25267)).
- The UTF-8 decoder is now up to 15 times as fast for error handlers - `ignore`,- `replace`and- `surrogateescape`(Contributed by Victor Stinner in- [bpo-25301](https://bugs.python.org/issue?@action=redirect&bpo=25301)).
- `bytes % args`is now up to 2 times faster. (Contributed by Victor Stinner in- [bpo-25349](https://bugs.python.org/issue?@action=redirect&bpo=25349)).
- `bytearray % args`is now between 2.5 and 5 times faster. (Contributed by Victor Stinner in- [bpo-25399](https://bugs.python.org/issue?@action=redirect&bpo=25399)).
- Optimize - `bytes.fromhex()`- `bytearray.fromhex()`- [bpo-25401](https://bugs.python.org/issue?@action=redirect&bpo=25401)).
- Optimize - `bytes.replace(b'', b'.')`and- `bytearray.replace(b'', b'.')`: up to 80% faster. (Contributed by Josh Snider in- [bpo-26574](https://bugs.python.org/issue?@action=redirect&bpo=26574)).
- Allocator functions of the - `PyMem_Malloc()`- `PYMEM_DOMAIN_MEM`- [pymalloc memory allocator](../c-api/memory.html#pymalloc)instead of- `malloc()`function of the C library. The pymalloc allocator is optimized for objects smaller or equal to 512 bytes with a short lifetime, and use- `malloc()`for larger memory blocks. (Contributed by Victor Stinner in- [bpo-26249](https://bugs.python.org/issue?@action=redirect&bpo=26249)).
- `pickle.load()`- `pickle.loads()`- [bpo-27056](https://bugs.python.org/issue?@action=redirect&bpo=27056)).
- Passing - [keyword arguments](../glossary.html#term-keyword-argument)to a function has an overhead in comparison with passing- [positional arguments](../glossary.html#term-positional-argument). Now in extension functions implemented with using Argument Clinic this overhead is significantly decreased. (Contributed by Serhiy Storchaka in- [bpo-27574](https://bugs.python.org/issue?@action=redirect&bpo=27574)).
- Optimized - `glob()`- `iglob()`- `glob`- [bpo-25596](https://bugs.python.org/issue?@action=redirect&bpo=25596)).
- Optimized globbing in - `pathlib`- `os.scandir()`- [bpo-26032](https://bugs.python.org/issue?@action=redirect&bpo=26032)).
- `xml.etree.ElementTree`- [bpo-25638](https://bugs.python.org/issue?@action=redirect&bpo=25638),- [bpo-25873](https://bugs.python.org/issue?@action=redirect&bpo=25873), and- [bpo-25869](https://bugs.python.org/issue?@action=redirect&bpo=25869).)
- Creation of - `fractions.Fraction`- [bpo-25971](https://bugs.python.org/issue?@action=redirect&bpo=25971).)

## Build and C API Changes[¶](#build-and-c-api-changes)

- Python now requires some C99 support in the toolchain to build. Most notably, Python now uses standard integer types and macros in place of custom macros like - `PY_LONG_LONG`. For more information, see- **PEP 7**- [bpo-17884](https://bugs.python.org/issue?@action=redirect&bpo=17884).
- Cross-compiling CPython with the Android NDK and the Android API level set to 21 (Android 5.0 Lollipop) or greater runs successfully. While Android is not yet a supported platform, the Python test suite runs on the Android emulator with only about 16 tests failures. See the Android meta-issue - [bpo-26865](https://bugs.python.org/issue?@action=redirect&bpo=26865).
- The - `--enable-optimizations`configure flag has been added. Turning it on will activate expensive optimizations like PGO. (Original patch by Alecsandru Patrascu of Intel in- [bpo-26359](https://bugs.python.org/issue?@action=redirect&bpo=26359).)
- The - [GIL](../glossary.html#term-global-interpreter-lock)must now be held when allocator functions of- `PYMEM_DOMAIN_OBJ`- `PyObject_Malloc()`- `PYMEM_DOMAIN_MEM`- `PyMem_Malloc()`
- New - `Py_FinalizeEx()`- [bpo-5319](https://bugs.python.org/issue?@action=redirect&bpo=5319).)
- `PyArg_ParseTupleAndKeywords()`- [positional-only parameters](../glossary.html#positional-only-parameter). Positional-only parameters are defined by empty names. (Contributed by Serhiy Storchaka in- [bpo-26282](https://bugs.python.org/issue?@action=redirect&bpo=26282)).
- `PyTraceback_Print`method now abbreviates long sequences of repeated lines as- `"[Previous line repeated {count} more times]"`. (Contributed by Emanuel Barry in- [bpo-26823](https://bugs.python.org/issue?@action=redirect&bpo=26823).)
- The new - `PyErr_SetImportErrorSubclass()`- `ImportError`- [bpo-15767](https://bugs.python.org/issue?@action=redirect&bpo=15767).)
- The new - `PyErr_ResourceWarning()`- `ResourceWarning`- [bpo-26567](https://bugs.python.org/issue?@action=redirect&bpo=26567).)
- The new - `PyOS_FSPath()`- [path-like object](../glossary.html#term-path-like-object). (Contributed by Brett Cannon in- [bpo-27186](https://bugs.python.org/issue?@action=redirect&bpo=27186).)
- The - `PyUnicode_FSConverter()`- `PyUnicode_FSDecoder()`- [path-like objects](../glossary.html#term-path-like-object).

## Other Improvements[¶](#other-improvements)

- When - `--version`- `-V`- `sys.version`- $ ./python -VV Python 3.6.0b4+ (3.6:223967b49e49+, Nov 21 2016, 20:55:04) [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] 

## Deprecated[¶](#deprecated)

### New Keywords[¶](#new-keywords)

`async` and `await` are not recommended to be used as variable, class,
function or module names.  Introduced by [ PEP 492](https://peps.python.org/pep-0492/) in Python 3.5, they will
become proper keywords in Python 3.7.  Starting in Python 3.6, the use of

`async` or `await` as names will generate a [.](../library/exceptions.html#DeprecationWarning)

`DeprecationWarning`### Deprecated Python behavior[¶](#deprecated-python-behavior)

Raising the [ StopIteration](../library/exceptions.html#StopIteration) exception inside a generator will now
generate a 

[, and will trigger a](../library/exceptions.html#DeprecationWarning)

`DeprecationWarning`[in Python 3.7. See](../library/exceptions.html#RuntimeError)

`RuntimeError`[PEP 479: Change StopIteration handling inside generators](3.5.html#whatsnew-pep-479)for details.

The [ __aiter__()](../reference/datamodel.html#object.__aiter__) method is now expected to return an asynchronous
iterator directly instead of returning an awaitable as previously.
Doing the former will trigger a 

[. Backward compatibility will be removed in Python 3.7. (Contributed by Yury Selivanov in](../library/exceptions.html#DeprecationWarning)

`DeprecationWarning`[bpo-27243](https://bugs.python.org/issue?@action=redirect&bpo=27243).)

A backslash-character pair that is not a valid escape sequence now generates
a [ DeprecationWarning](../library/exceptions.html#DeprecationWarning).  Although this will eventually become a

[, that will not be for several Python releases. (Contributed by Emanuel Barry in](../library/exceptions.html#SyntaxError)

`SyntaxError`[bpo-27364](https://bugs.python.org/issue?@action=redirect&bpo=27364).)

When performing a relative import, falling back on `__name__` and
`__path__` from the calling module when `__spec__` or
`__package__` are not defined now raises an [ ImportWarning](../library/exceptions.html#ImportWarning).
(Contributed by Rose Ames in 

[bpo-25791](https://bugs.python.org/issue?@action=redirect&bpo=25791).)

### Deprecated Python modules, functions and methods[¶](#deprecated-python-modules-functions-and-methods)

#### asynchat[¶](#asynchat)

The `asynchat` has been deprecated in favor of [ asyncio](../library/asyncio.html#module-asyncio).
(Contributed by Mariatta in 

[bpo-25002](https://bugs.python.org/issue?@action=redirect&bpo=25002).)

#### asyncore[¶](#asyncore)

The `asyncore` has been deprecated in favor of [ asyncio](../library/asyncio.html#module-asyncio).
(Contributed by Mariatta in 

[bpo-25002](https://bugs.python.org/issue?@action=redirect&bpo=25002).)

#### dbm[¶](#dbm)

Unlike other [ dbm](../library/dbm.html#module-dbm) implementations, the 

[module creates databases with the](../library/dbm.html#module-dbm.dumb)

`dbm.dumb``'rw'` mode and allows modifying the database
opened with the `'r'` mode.  This behavior is now deprecated and will
be removed in 3.8.
(Contributed by Serhiy Storchaka in [bpo-21708](https://bugs.python.org/issue?@action=redirect&bpo=21708).)

#### distutils[¶](#id2)

The undocumented `extra_path` argument to the
`distutils.Distribution` constructor is now considered deprecated
and will raise a warning if set.   Support for this parameter will be
removed in a future Python release.  See [bpo-27919](https://bugs.python.org/issue?@action=redirect&bpo=27919) for details.

#### grp[¶](#grp)

The support of non-integer arguments in [ getgrgid()](../library/grp.html#grp.getgrgid) has been
deprecated.
(Contributed by Serhiy Storchaka in 

[bpo-26129](https://bugs.python.org/issue?@action=redirect&bpo=26129).)

#### importlib[¶](#id3)

The [ importlib.machinery.SourceFileLoader.load_module()](../library/importlib.html#importlib.machinery.SourceFileLoader.load_module) and

[methods are now deprecated. They were the only remaining implementations of](../library/importlib.html#importlib.machinery.SourcelessFileLoader.load_module)

`importlib.machinery.SourcelessFileLoader.load_module()`[in](../library/importlib.html#importlib.abc.Loader.load_module)

`importlib.abc.Loader.load_module()`[that had not been deprecated in previous versions of Python in favour of](../library/importlib.html#module-importlib)

`importlib`[.](../library/importlib.html#importlib.abc.Loader.exec_module)

`importlib.abc.Loader.exec_module()`The [ importlib.machinery.WindowsRegistryFinder](../library/importlib.html#importlib.machinery.WindowsRegistryFinder) class is now
deprecated. As of 3.6.0, it is still added to 

[by default (on Windows), but this may change in future releases.](../library/sys.html#sys.meta_path)

`sys.meta_path`#### os[¶](#id4)

Undocumented support of general [bytes-like objects](../glossary.html#term-bytes-like-object)
as paths in [ os](../library/os.html#module-os) functions, 

[and similar functions is now deprecated. (Contributed by Serhiy Storchaka in](../library/functions.html#compile)

`compile()`[bpo-25791](https://bugs.python.org/issue?@action=redirect&bpo=25791)and

[bpo-26754](https://bugs.python.org/issue?@action=redirect&bpo=26754).)

#### re[¶](#id5)

Support for inline flags `(?letters)` in the middle of the regular
expression has been deprecated and will be removed in a future Python
version.  Flags at the start of a regular expression are still allowed.
(Contributed by Serhiy Storchaka in [bpo-22493](https://bugs.python.org/issue?@action=redirect&bpo=22493).)

#### ssl[¶](#id6)

OpenSSL 0.9.8, 1.0.0 and 1.0.1 are deprecated and no longer supported.
In the future the [ ssl](../library/ssl.html#module-ssl) module will require at least OpenSSL 1.0.2 or
1.1.0.

SSL-related arguments like `certfile`, `keyfile` and `check_hostname`
in [ ftplib](../library/ftplib.html#module-ftplib), 

[,](../library/http.client.html#module-http.client)

`http.client`[,](../library/imaplib.html#module-imaplib)

`imaplib`[, and](../library/poplib.html#module-poplib)

`poplib`[have been deprecated in favor of](../library/smtplib.html#module-smtplib)

`smtplib``context`.
(Contributed by Christian Heimes in [bpo-28022](https://bugs.python.org/issue?@action=redirect&bpo=28022).)

A couple of protocols and functions of the [ ssl](../library/ssl.html#module-ssl) module are now
deprecated. Some features will no longer be available in future versions
of OpenSSL. Other features are deprecated in favor of a different API.
(Contributed by Christian Heimes in 

[bpo-28022](https://bugs.python.org/issue?@action=redirect&bpo=28022)and

[bpo-26470](https://bugs.python.org/issue?@action=redirect&bpo=26470).)

#### tkinter[¶](#id7)

The `tkinter.tix` module is now deprecated.  [ tkinter](../library/tkinter.html#module-tkinter) users
should use 

[instead.](../library/tkinter.ttk.html#module-tkinter.ttk)

`tkinter.ttk`#### venv[¶](#whatsnew36-venv)

The `pyvenv` script has been deprecated in favour of `python3 -m venv`.
This prevents confusion as to what Python interpreter `pyvenv` is
connected to and thus what Python interpreter will be used by the virtual
environment.  (Contributed by Brett Cannon in [bpo-25154](https://bugs.python.org/issue?@action=redirect&bpo=25154).)

### xml[¶](#xml)

- As mitigation against DTD and external entity retrieval, the - `xml.dom.minidom`- `xml.sax`- [gh-61441](https://github.com/python/cpython/issues/61441).)

### Deprecated functions and types of the C API[¶](#deprecated-functions-and-types-of-the-c-api)

Undocumented functions `PyUnicode_AsEncodedObject()`,
`PyUnicode_AsDecodedObject()`, `PyUnicode_AsEncodedUnicode()`
and `PyUnicode_AsDecodedUnicode()` are deprecated now.
Use the [generic codec based API](../c-api/codec.html#codec-registry) instead.

### Deprecated Build Options[¶](#deprecated-build-options)

The `--with-system-ffi` configure flag is now on by default on non-macOS
UNIX platforms.  It may be disabled by using `--without-system-ffi`, but
using the flag is deprecated and will not be accepted in Python 3.7.
macOS is unaffected by this change.  Note that many OS distributors already
use the `--with-system-ffi` flag when building their system Python.

## Removed[¶](#removed)

### API and Feature Removals[¶](#api-and-feature-removals)

- Unknown escapes consisting of - `'\'`and an ASCII letter in regular expressions will now cause an error. In replacement templates for- `re.sub()`- `re.LOCALE`
- `inspect.getmoduleinfo()`was removed (was deprecated since CPython 3.3).- `inspect.getmodulename()`- [bpo-13248](https://bugs.python.org/issue?@action=redirect&bpo=13248).)
- `traceback.Ignore`class and- `traceback.usage`,- `traceback.modname`,- `traceback.fullmodname`,- `traceback.find_lines_from_code`,- `traceback.find_lines`,- `traceback.find_strings`,- `traceback.find_executable_lines`methods were removed from the- `traceback`
- The - `tk_menuBar()`and- `tk_bindForTraversal()`dummy methods in- `tkinter`
- The - `open()`- `zipfile.ZipFile`- `'U'`mode (was deprecated since Python 3.4). Use- `io.TextIOWrapper`- [universal newlines](../glossary.html#term-universal-newlines)mode.
- The undocumented - `IN`,- `CDROM`,- `DLFCN`,- `TYPES`,- `CDIO`, and- `STROPTS`modules have been removed. They had been available in the platform specific- `Lib/plat-*/`directories, but were chronically out of date, inconsistently available across platforms, and unmaintained. The script that created these modules is still available in the source distribution at- [Tools/scripts/h2py.py](https://github.com/python/cpython/blob/v3.6.15/Tools/scripts/h2py.py).
- The deprecated - `asynchat.fifo`class has been removed.

## Porting to Python 3.6[¶](#porting-to-python-3-6)

This section lists previously described changes and other bugfixes that may require changes to your code.

### Changes in ‘python’ Command Behavior[¶](#changes-in-python-command-behavior)

- The output of a special Python build with defined - `COUNT_ALLOCS`,- `SHOW_ALLOC_COUNT`or- `SHOW_TRACK_COUNT`macros is now off by default. It can be re-enabled using the- `-X showalloccount`option. It now outputs to- `stderr`instead of- `stdout`. (Contributed by Serhiy Storchaka in- [bpo-23034](https://bugs.python.org/issue?@action=redirect&bpo=23034).)

### Changes in the Python API[¶](#changes-in-the-python-api)

- `open()`- `'U'`mode flag with- `'+'`. (Contributed by Jeff Balogh and John O’Connor in- [bpo-2091](https://bugs.python.org/issue?@action=redirect&bpo=2091).)
- `sqlite3`
- On Linux, - `os.urandom()`
- When - `importlib.abc.Loader.exec_module()`- `importlib.abc.Loader.create_module()`
- `PyErr_SetImportError()`- `TypeError`- **msg**argument is not set. Previously only- `NULL`was returned.
- The format of the - `co_lnotab`- `frame.f_lineno`- `PyFrame_GetLineNumber()`or- `PyCode_Addr2Line()`are not affected. Functions directly decoding- `co_lnotab`should be updated to use a signed 8-bit integer type for the line number delta, but this is only required to support applications using a negative line number delta. See- `Objects/lnotab_notes.txt`for the- `co_lnotab`format and how to decode it, and see the- **PEP 511**
- The functions in the - `compileall`- `1`or- `0`to represent success or failure, respectively. Thanks to booleans being a subclass of integers, this should only be an issue if you were doing identity checks for- `1`or- `0`. See- [bpo-25768](https://bugs.python.org/issue?@action=redirect&bpo=25768).
- Reading the - `port`attribute of- `urllib.parse.urlsplit()`- `urlparse()`- `ValueError`- `None`- [bpo-20059](https://bugs.python.org/issue?@action=redirect&bpo=20059).
- The - `imp`module now raises a- `DeprecationWarning`- `PendingDeprecationWarning`
- The following modules have had missing APIs added to their - `__all__`- `calendar`- `cgi`,- `csv`- `ElementTree`- `enum`- `fileinput`- `ftplib`- `logging`- `mailbox`- `mimetypes`- `optparse`- `plistlib`- `smtpd`,- `subprocess`- `tarfile`- `threading`- `wave`- `import *`is used. (Contributed by Joel Taddei and Jacek Kołodziej in- [bpo-23883](https://bugs.python.org/issue?@action=redirect&bpo=23883).)
- When performing a relative import, if - `__package__`does not compare equal to- `__spec__.parent`then- `ImportWarning`- [bpo-25791](https://bugs.python.org/issue?@action=redirect&bpo=25791).)
- When a relative import is performed and no parent package is known, then - `ImportError`- `SystemError`- [bpo-18018](https://bugs.python.org/issue?@action=redirect&bpo=18018).)
- Servers based on the - `socketserver`- `http.server`- `xmlrpc.server`- `wsgiref.simple_server`- `Exception`- `SystemExit`- `KeyboardInterrupt`- `handle_error()`- [bpo-23430](https://bugs.python.org/issue?@action=redirect&bpo=23430).)
- `spwd.getspnam()`now raises a- `PermissionError`- `KeyError`
- The - `socket.socket.close()`- `EBADF`) was reported by the underlying system call. (Contributed by Martin Panter in- [bpo-26685](https://bugs.python.org/issue?@action=redirect&bpo=26685).)
- The - *decode_data*argument for the- `smtpd.SMTPChannel`and- `smtpd.SMTPServer`constructors is now- `False`by default. This means that the argument passed to- `process_message()`is now a bytes object by default, and- `process_message()`will be passed keyword arguments. Code that has already been updated in accordance with the deprecation warning generated by 3.5 will not be affected.
- All optional arguments of the - `dump()`- `dumps()`- `load()`- `loads()`- `JSONEncoder`- `JSONDecoder`- `json`- [keyword-only](../glossary.html#keyword-only-parameter). (Contributed by Serhiy Storchaka in- [bpo-18726](https://bugs.python.org/issue?@action=redirect&bpo=18726).)
- Subclasses of - `type`- `type.__new__`may no longer use the one-argument form to get the type of an object.
- As part of - **PEP 487**- `type`- `metaclass`) is now consistently delegated to- `object.__init_subclass__()`- `type.__new__`- `type.__init__`- `object.__init_subclass__()`(which is called from- `type.__new__`) will reject them by default. Custom metaclasses accepting additional keyword arguments will need to adjust their calls to- `type.__new__`(whether direct or via- `super`
- In - `distutils.command.sdist.sdist`, the- `default_format`attribute has been removed and is no longer honored. Instead, the gzipped tarfile format is the default on all platforms and no platform-specific selection is made. In environments where distributions are built on Windows and zip distributions are required, configure the project with a- `setup.cfg`file containing the following:- [sdist] formats=zip - This behavior has also been backported to earlier Python versions by Setuptools 26.0.0. 
- In the - `urllib.request`- `http.client.HTTPConnection.request()`- [bpo-12319](https://bugs.python.org/issue?@action=redirect&bpo=12319).)
- The - `DictReader`- `OrderedDict`- [bpo-27842](https://bugs.python.org/issue?@action=redirect&bpo=27842).)
- The - `crypt.METHOD_CRYPT`will no longer be added to- `crypt.methods`if unsupported by the platform. (Contributed by Victor Stinner in- [bpo-25287](https://bugs.python.org/issue?@action=redirect&bpo=25287).)
- The - *verbose*and- *rename*arguments for- `namedtuple()`- [bpo-25628](https://bugs.python.org/issue?@action=redirect&bpo=25628).)
- On Linux, - `ctypes.util.find_library()`- `LD_LIBRARY_PATH`for shared libraries. (Contributed by Vinay Sajip in- [bpo-9998](https://bugs.python.org/issue?@action=redirect&bpo=9998).)
- The - `imaplib.IMAP4`- `']'`character in messages sent from the server to improve real-world compatibility. (Contributed by Lita Cho in- [bpo-21815](https://bugs.python.org/issue?@action=redirect&bpo=21815).)
- The - `mmap.mmap.write()`- [bpo-26335](https://bugs.python.org/issue?@action=redirect&bpo=26335).)
- The - `pkgutil.iter_modules()`- `pkgutil.walk_packages()`- `ModuleInfo`- [bpo-17211](https://bugs.python.org/issue?@action=redirect&bpo=17211).)
- `re.sub()`- [bpo-25953](https://bugs.python.org/issue?@action=redirect&bpo=25953).)
- `zipfile.ZipFile`- `NotImplementedError`- `RuntimeError`- `ZipFile`methods on a closed ZipFile or calling the- `write()`- `'r'`will raise a- `ValueError`- `RuntimeError`was raised in those scenarios.
- when custom metaclasses are combined with zero-argument - `super()`- `__class__`closure variable, the implicit- `__classcell__`namespace entry must now be passed up to- `type.__new__`for initialisation. Failing to do so will result in a- `DeprecationWarning`- `RuntimeError`
- With the introduction of - `ModuleNotFoundError`- `ImportError`- `__import__()`

### Changes in the C API[¶](#changes-in-the-c-api)

- The - `PyMem_Malloc()`- [pymalloc allocator](../c-api/memory.html#pymalloc)rather than the system- `malloc()`. Applications calling- `PyMem_Malloc()`without holding the GIL can now crash. Set the- `PYTHONMALLOC`- `debug`to validate the usage of memory allocators in your application. See- [bpo-26249](https://bugs.python.org/issue?@action=redirect&bpo=26249).
- `Py_Exit()`- [bpo-5319](https://bugs.python.org/issue?@action=redirect&bpo=5319).

### CPython bytecode changes[¶](#cpython-bytecode-changes)

There have been several major changes to the [bytecode](../glossary.html#term-bytecode) in Python 3.6.

- The Python interpreter now uses a 16-bit wordcode instead of bytecode. (Contributed by Demur Rumed with input and reviews from Serhiy Storchaka and Victor Stinner in - [bpo-26647](https://bugs.python.org/issue?@action=redirect&bpo=26647)and- [bpo-28050](https://bugs.python.org/issue?@action=redirect&bpo=28050).)
- The new - `FORMAT_VALUE`and- `BUILD_STRING`- [formatted string literal](#whatsnew36-pep498)implementation. (Contributed by Eric Smith in- [bpo-25483](https://bugs.python.org/issue?@action=redirect&bpo=25483)and Serhiy Storchaka in- [bpo-27078](https://bugs.python.org/issue?@action=redirect&bpo=27078).)
- The new - `BUILD_CONST_KEY_MAP`- [bpo-27140](https://bugs.python.org/issue?@action=redirect&bpo=27140).)
- The function call opcodes have been heavily reworked for better performance and simpler implementation. The - `MAKE_FUNCTION`- `CALL_FUNCTION`,- `CALL_FUNCTION_KW`and- `BUILD_MAP_UNPACK_WITH_CALL`opcodes have been modified, the new- `CALL_FUNCTION_EX`- `BUILD_TUPLE_UNPACK_WITH_CALL`have been added, and- `CALL_FUNCTION_VAR`,- `CALL_FUNCTION_VAR_KW`and- `MAKE_CLOSURE`opcodes have been removed. (Contributed by Demur Rumed in- [bpo-27095](https://bugs.python.org/issue?@action=redirect&bpo=27095), and Serhiy Storchaka in- [bpo-27213](https://bugs.python.org/issue?@action=redirect&bpo=27213),- [bpo-28257](https://bugs.python.org/issue?@action=redirect&bpo=28257).)
- The new - `SETUP_ANNOTATIONS`- `STORE_ANNOTATION`opcodes have been added to support the new- [variable annotation](../glossary.html#term-variable-annotation)syntax. (Contributed by Ivan Levkivskyi in- [bpo-27985](https://bugs.python.org/issue?@action=redirect&bpo=27985).)

## Notable changes in Python 3.6.2[¶](#notable-changes-in-python-3-6-2)

### New `make regen-all` build target[¶](#new-make-regen-all-build-target)

To simplify cross-compilation, and to ensure that CPython can reliably be compiled without requiring an existing version of Python to already be available, the autotools-based build system no longer attempts to implicitly recompile generated files based on file modification times.

Instead, a new `make regen-all` command has been added to force regeneration
of these files when desired (e.g. after an initial version of Python has
already been built based on the pregenerated versions).

More selective regeneration targets are also defined - see
[Makefile.pre.in](https://github.com/python/cpython/tree/3.13/Makefile.pre.in) for details.

(Contributed by Victor Stinner in [bpo-23404](https://bugs.python.org/issue?@action=redirect&bpo=23404).)

Added in version 3.6.2.

### Removal of `make touch` build target[¶](#removal-of-make-touch-build-target)

The `make touch` build target previously used to request implicit regeneration
of generated files by updating their modification times has been removed.

It has been replaced by the new `make regen-all` target.

(Contributed by Victor Stinner in [bpo-23404](https://bugs.python.org/issue?@action=redirect&bpo=23404).)

Changed in version 3.6.2.

## Notable changes in Python 3.6.4[¶](#notable-changes-in-python-3-6-4)

The `PyExc_RecursionErrorInst` singleton that was part of the public API
has been removed as its members being never cleared may cause a segfault
during finalization of the interpreter.
(Contributed by Xavier de Gaye in [bpo-22898](https://bugs.python.org/issue?@action=redirect&bpo=22898) and [bpo-30697](https://bugs.python.org/issue?@action=redirect&bpo=30697).)

## Notable changes in Python 3.6.5[¶](#notable-changes-in-python-3-6-5)

The [ locale.localeconv()](../library/locale.html#locale.localeconv) function now sets temporarily the 

`LC_CTYPE`
locale to the `LC_NUMERIC` locale in some cases.
(Contributed by Victor Stinner in [bpo-31900](https://bugs.python.org/issue?@action=redirect&bpo=31900).)

## Notable changes in Python 3.6.7[¶](#notable-changes-in-python-3-6-7)

[ xml.dom.minidom](../library/xml.dom.minidom.html#module-xml.dom.minidom) and 

[modules no longer process external entities by default. See also](../library/xml.sax.html#module-xml.sax)

`xml.sax`[gh-61441](https://github.com/python/cpython/issues/61441).

In 3.6.7 the [ tokenize](../library/tokenize.html#module-tokenize) module now implicitly emits a 

`NEWLINE` token
when provided with input that does not have a trailing new line.  This behavior
now matches what the C tokenizer does internally.
(Contributed by Ammar Askar in [bpo-33899](https://bugs.python.org/issue?@action=redirect&bpo=33899).)

## Notable changes in Python 3.6.10[¶](#notable-changes-in-python-3-6-10)

Due to significant security concerns, the *reuse_address* parameter of
[ asyncio.loop.create_datagram_endpoint()](../library/asyncio-eventloop.html#asyncio.loop.create_datagram_endpoint) is no longer supported. This is
because of the behavior of the socket option 

`SO_REUSEADDR` in UDP. For more
details, see the documentation for `loop.create_datagram_endpoint()`.
(Contributed by Kyle Stanley, Antoine Pitrou, and Yury Selivanov in
[bpo-37228](https://bugs.python.org/issue?@action=redirect&bpo=37228).)

## Notable changes in Python 3.6.13[¶](#notable-changes-in-python-3-6-13)

Earlier Python versions allowed using both `;` and `&` as
query parameter separators in [ urllib.parse.parse_qs()](../library/urllib.parse.html#urllib.parse.parse_qs) and

[. Due to security concerns, and to conform with newer W3C recommendations, this has been changed to allow only a single separator key, with](../library/urllib.parse.html#urllib.parse.parse_qsl)

`urllib.parse.parse_qsl()``&` as the default.  This change also affects
`cgi.parse()` and `cgi.parse_multipart()` as they use the affected
functions internally. For more details, please see their respective
documentation.
(Contributed by Adam Goldschmidt, Senthil Kumaran and Ken Jin in [bpo-42967](https://bugs.python.org/issue?@action=redirect&bpo=42967).)

## Notable changes in Python 3.6.14[¶](#notable-changes-in-python-3-6-14)

A security fix alters the [ ftplib.FTP](../library/ftplib.html#ftplib.FTP) behavior to not trust the
IPv4 address sent from the remote server when setting up a passive data
channel.  We reuse the ftp server IP address instead.  For unusual code
requiring the old behavior, set a 

`trust_server_pasv_ipv4_address`
attribute on your FTP instance to `True`.  (See [gh-87451](https://github.com/python/cpython/issues/87451))

The presence of newline or tab characters in parts of a URL allows for some
forms of attacks. Following the WHATWG specification that updates RFC 3986,
ASCII newline `\n`, `\r` and tab `\t` characters are stripped from the
URL by the parser [ urllib.parse()](../library/urllib.parse.html#module-urllib.parse) preventing such attacks. The removal
characters are controlled by a new module level variable

`urllib.parse._UNSAFE_URL_BYTES_TO_REMOVE`. (See [gh-88048](https://github.com/python/cpython/issues/88048))