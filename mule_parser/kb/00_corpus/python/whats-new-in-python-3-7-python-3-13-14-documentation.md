# What’s New In Python 3.7 — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/whatsnew/3.7.html](https://docs.python.org/3.13/whatsnew/3.7.html)

---

# What’s New In Python 3.7[¶](#what-s-new-in-python-3-7)

- Editor:
- Elvis Pranskevichus < - [elvis@magic.io](mailto:elvis%40magic.io)>

This article explains the new features in Python 3.7, compared to 3.6.
Python 3.7 was released on June 27, 2018.
For full details, see the [changelog](changelog.html#changelog).

## Summary – Release Highlights[¶](#summary-release-highlights)

New syntax features:

- [PEP 563](#whatsnew37-pep563), postponed evaluation of type annotations.

Backwards incompatible syntax changes:

New library modules:

New built-in features:

- [PEP 553](#whatsnew37-pep553), the new- `breakpoint()`

Python data model improvements:

- [PEP 562](#whatsnew37-pep562), customization of access to module attributes.
- [PEP 560](#whatsnew37-pep560), core support for typing module and generic types.
- the insertion-order preservation nature of - [dict](../library/stdtypes.html#typesmapping)objects- [has been declared](https://mail.python.org/pipermail/python-dev/2017-December/151283.html)to be an official part of the Python language spec.

Significant improvements in the standard library:

- The - `asyncio`- [usability and performance improvements](#whatsnew37-asyncio).
- The - `time`- [functions with nanosecond resolution](#whatsnew37-pep564).

CPython implementation improvements:

- Avoiding the use of ASCII as a default text encoding: 
- [PEP 552](#whatsnew37-pep552), deterministic .pycs
- [PEP 565](#whatsnew37-pep565), improved- `DeprecationWarning`

C API improvements:

- [PEP 539](#whatsnew37-pep539), new C API for thread-local storage

Documentation improvements:

- [PEP 545](#whatsnew37-pep545), Python documentation translations
- New documentation translations: - [Japanese](https://docs.python.org/ja/),- [French](https://docs.python.org/fr/), and- [Korean](https://docs.python.org/ko/).

This release features notable performance improvements in many areas.
The [Optimizations](#whatsnew37-perf) section lists them in detail.

For a list of changes that may affect compatibility with previous Python
releases please refer to the [Porting to Python 3.7](#porting-to-python-37) section.

## New Features[¶](#new-features)

### PEP 563: Postponed Evaluation of Annotations[¶](#pep-563-postponed-evaluation-of-annotations)

The advent of type hints in Python uncovered two glaring usability issues
with the functionality of annotations added in [ PEP 3107](https://peps.python.org/pep-3107/) and refined
further in 

[:](https://peps.python.org/pep-0526/)

**PEP 526**- annotations could only use names which were already available in the current scope, in other words they didn’t support forward references of any kind; and 
- annotating source code had adverse effects on startup time of Python programs. 

Both of these issues are fixed by postponing the evaluation of
annotations.  Instead of compiling code which executes expressions in
annotations at their definition time, the compiler stores the annotation
in a string form equivalent to the AST of the expression in question.
If needed, annotations can be resolved at runtime using
[ typing.get_type_hints()](../library/typing.html#typing.get_type_hints).  In the common case where this is not
required, the annotations are cheaper to store (since short strings
are interned by the interpreter) and make startup time faster.

Usability-wise, annotations now support forward references, making the following syntax valid:

```
class C:
    @classmethod
    def from_string(cls, source: str) -> C:
        ...
    def validate_b(self, obj: B) -> bool:
        ...
class B:
    ...
```
Since this change breaks compatibility, the new behavior needs to be enabled
on a per-module basis in Python 3.7 using a [ __future__](../library/__future__.html#module-__future__) import:

```
from __future__ import annotations
```
It will become the default in Python 3.10.

See also

- **PEP 563**
- PEP written and implemented by Łukasz Langa. 

### PEP 538: Legacy C Locale Coercion[¶](#pep-538-legacy-c-locale-coercion)

An ongoing challenge within the Python 3 series has been determining a sensible default strategy for handling the “7-bit ASCII” text encoding assumption currently implied by the use of the default C or POSIX locale on non-Windows platforms.

[ PEP 538](https://peps.python.org/pep-0538/) updates the default interpreter command line interface to
automatically coerce that locale to an available UTF-8 based locale as
described in the documentation of the new 

[environment variable. Automatically setting](../using/cmdline.html#envvar-PYTHONCOERCECLOCALE)

`PYTHONCOERCECLOCALE``LC_CTYPE` this way means that
both the core interpreter and locale-aware C extensions (such as
[) will assume the use of UTF-8 as the default text encoding, rather than ASCII.](../library/readline.html#module-readline)

`readline`The platform support definition in [ PEP 11](https://peps.python.org/pep-0011/) has also been updated to limit
full text handling support to suitably configured non-ASCII based locales.

As part of this change, the default error handler for [ stdin](../library/sys.html#sys.stdin) and

[is now](../library/sys.html#sys.stdout)

`stdout``surrogateescape` (rather than `strict`) when
using any of the defined coercion target locales (currently `C.UTF-8`,
`C.utf8`, and `UTF-8`).  The default error handler for [continues to be](../library/sys.html#sys.stderr)

`stderr``backslashreplace`, regardless of locale.Locale coercion is silent by default, but to assist in debugging potentially
locale related integration problems, explicit warnings (emitted directly on
[ stderr](../library/sys.html#sys.stderr)) can be requested by setting 

`PYTHONCOERCECLOCALE=warn`.
This setting will also cause the Python runtime to emit a warning if the
legacy C locale remains active when the core interpreter is initialized.While [ PEP 538](https://peps.python.org/pep-0538/)’s locale coercion has the benefit of also affecting extension
modules (such as GNU 

`readline`), as well as child processes (including those
running non-Python applications and older versions of Python), it has the
downside of requiring that a suitable target locale be present on the running
system. To better handle the case where no suitable target locale is available
(as occurs on RHEL/CentOS 7, for example), Python 3.7 also implements
[PEP 540: Forced UTF-8 Runtime Mode](#whatsnew37-pep540).

See also

- **PEP 538**
- PEP written and implemented by Nick Coghlan. 

### PEP 540: Forced UTF-8 Runtime Mode[¶](#pep-540-forced-utf-8-runtime-mode)

The new `-X``utf8` command line option and [ PYTHONUTF8](../using/cmdline.html#envvar-PYTHONUTF8)
environment variable can be used to enable the 

[Python UTF-8 Mode](../library/os.html#utf8-mode).

When in UTF-8 mode, CPython ignores the locale settings, and uses the
UTF-8 encoding by default.  The error handlers for [ sys.stdin](../library/sys.html#sys.stdin) and

[streams are set to](../library/sys.html#sys.stdout)

`sys.stdout``surrogateescape`.The forced UTF-8 mode can be used to change the text handling behavior in an embedded Python interpreter without changing the locale settings of an embedding application.

While [ PEP 540](https://peps.python.org/pep-0540/)’s UTF-8 mode has the benefit of working regardless of which
locales are available on the running system, it has the downside of having no
effect on extension modules (such as GNU 

`readline`), child processes running
non-Python applications, and child processes running older versions of Python.
To reduce the risk of corrupting text data when communicating with such
components, Python 3.7 also implements [PEP 540: Forced UTF-8 Runtime Mode](#whatsnew37-pep540)).

The UTF-8 mode is enabled by default when the locale is `C` or `POSIX`, and
the [ PEP 538](https://peps.python.org/pep-0538/) locale coercion feature fails to change it to a UTF-8 based
alternative (whether that failure is due to 

`PYTHONCOERCECLOCALE=0` being set,
`LC_ALL` being set, or the lack of a suitable target locale).See also

- **PEP 540**
- PEP written and implemented by Victor Stinner 

### PEP 553: Built-in `breakpoint()`[¶](#pep-553-built-in-breakpoint)

Python 3.7 includes the new built-in [ breakpoint()](../library/functions.html#breakpoint) function as
an easy and consistent way to enter the Python debugger.

Built-in `breakpoint()` calls [ sys.breakpointhook()](../library/sys.html#sys.breakpointhook).  By default, the
latter imports 

[and then calls](../library/pdb.html#module-pdb)

`pdb``pdb.set_trace()`, but by binding
`sys.breakpointhook()` to the function of your choosing, `breakpoint()` can
enter any debugger. Additionally, the environment variable
[can be set to the callable of your debugger of choice. Set](../using/cmdline.html#envvar-PYTHONBREAKPOINT)

`PYTHONBREAKPOINT``PYTHONBREAKPOINT=0` to completely disable built-in
`breakpoint()`.See also

- **PEP 553**
- PEP written and implemented by Barry Warsaw 

### PEP 539: New C API for Thread-Local Storage[¶](#pep-539-new-c-api-for-thread-local-storage)

While Python provides a C API for thread-local storage support; the existing
[Thread Local Storage (TLS) API](../c-api/init.html#thread-local-storage-api) has used
int to represent TLS keys across all platforms.  This has not
generally been a problem for officially support platforms, but that is neither
POSIX-compliant, nor portable in any practical sense.

[ PEP 539](https://peps.python.org/pep-0539/) changes this by providing a new 

[Thread Specific Storage (TSS) API](../c-api/init.html#thread-specific-storage-api)to CPython which supersedes use of the existing TLS API within the CPython interpreter, while deprecating the existing API. The TSS API uses a new type

[instead of int to represent TSS keys–an opaque type the definition of which may depend on the underlying TLS implementation. Therefore, this will allow to build CPython on platforms where the native TLS key is defined in a way that cannot be safely cast to int.](../c-api/init.html#c.Py_tss_t)

`Py_tss_t`Note that on platforms where the native TLS key is defined in a way that cannot be safely cast to int, all functions of the existing TLS API will be no-op and immediately return failure. This indicates clearly that the old API is not supported on platforms where it cannot be used reliably, and that no effort will be made to add such support.

See also

- **PEP 539**
- PEP written by Erik M. Bray; implementation by Masayuki Yamamoto. 

### PEP 562: Customization of Access to Module Attributes[¶](#pep-562-customization-of-access-to-module-attributes)

Python 3.7 allows defining [ __getattr__()](../reference/datamodel.html#module.__getattr__) on modules and will call
it whenever a module attribute is otherwise not found.  Defining

[on modules is now also allowed.](../reference/datamodel.html#module.__dir__)

`__dir__()`A typical example of where this may be useful is module attribute deprecation and lazy loading.

See also

- **PEP 562**- `__getattr__`and- `__dir__`
- PEP written and implemented by Ivan Levkivskyi 

### PEP 564: New Time Functions With Nanosecond Resolution[¶](#pep-564-new-time-functions-with-nanosecond-resolution)

The resolution of clocks in modern systems can exceed the limited precision
of a floating-point number returned by the [ time.time()](../library/time.html#time.time) function
and its variants.  To avoid loss of precision, 

[adds six new “nanosecond” variants of the existing timer functions to the](https://peps.python.org/pep-0564/)

**PEP 564**[module:](../library/time.html#module-time)

`time`The new functions return the number of nanoseconds as an integer value.

[ Measurements](https://peps.python.org/pep-0564/#annex-clocks-resolution-in-python)
show that on Linux and Windows the resolution of 

[is approximately 3 times better than that of](../library/time.html#time.time_ns)

`time.time_ns()`[.](../library/time.html#time.time)

`time.time()`See also

- **PEP 564**
- PEP written and implemented by Victor Stinner 

### PEP 565: Show DeprecationWarning in `__main__`[¶](#pep-565-show-deprecationwarning-in-main)

The default handling of [ DeprecationWarning](../library/exceptions.html#DeprecationWarning) has been changed such that
these warnings are once more shown by default, but only when the code
triggering them is running directly in the 

[module. As a result, developers of single file scripts and those using Python interactively should once again start seeing deprecation warnings for the APIs they use, but deprecation warnings triggered by imported application, library and framework modules will continue to be hidden by default.](../library/__main__.html#module-__main__)

`__main__`As a result of this change, the standard library now allows developers to choose between three different deprecation warning behaviours:

- `FutureWarning`
- `DeprecationWarning`- `__main__`
- `PendingDeprecationWarning`- `DeprecationWarning`- `FutureWarning`

Previously both [ DeprecationWarning](../library/exceptions.html#DeprecationWarning) and 

[were only visible when running tests, which meant that developers primarily writing single file scripts or using Python interactively could be surprised by breaking changes in the APIs they used.](../library/exceptions.html#PendingDeprecationWarning)

`PendingDeprecationWarning`See also

- **PEP 565**- `__main__`
- PEP written and implemented by Nick Coghlan 

### PEP 560: Core Support for `typing` module and Generic Types[¶](#pep-560-core-support-for-typing-module-and-generic-types)

Initially [ PEP 484](https://peps.python.org/pep-0484/) was designed in such way that it would not introduce 

*any*changes to the core CPython interpreter. Now type hints and the

[module are extensively used by the community, so this restriction is removed. The PEP introduces two special methods](../library/typing.html#module-typing)

`typing`[and](../reference/datamodel.html#object.__class_getitem__)

`__class_getitem__()`[, these methods are now used by most classes and special constructs in](../reference/datamodel.html#object.__mro_entries__)

`__mro_entries__()``typing`. As a result, the speed of various operations
with types increased up to 7 times, the generic types can be used without
metaclass conflicts, and several long standing bugs in `typing` module are
fixed.See also

- **PEP 560**
- PEP written and implemented by Ivan Levkivskyi 

### PEP 552: Hash-based .pyc Files[¶](#pep-552-hash-based-pyc-files)

Python has traditionally checked the up-to-dateness of bytecode cache files
(i.e., `.pyc` files) by comparing the source metadata (last-modified timestamp
and size) with source metadata saved in the cache file header when it was
generated. While effective, this invalidation method has its drawbacks.  When
filesystem timestamps are too coarse, Python can miss source updates, leading to
user confusion. Additionally, having a timestamp in the cache file is
problematic for [build reproducibility](https://reproducible-builds.org/) and
content-based build systems.

[ PEP 552](https://peps.python.org/pep-0552/) extends the pyc format to allow the hash of the source file to be
used for invalidation instead of the source timestamp. Such 

`.pyc` files are
called “hash-based”. By default, Python still uses timestamp-based invalidation
and does not generate hash-based `.pyc` files at runtime. Hash-based `.pyc`
files may be generated with [or](../library/py_compile.html#module-py_compile)

`py_compile`[.](../library/compileall.html#module-compileall)

`compileall`Hash-based `.pyc` files come in two variants: checked and unchecked. Python
validates checked hash-based `.pyc` files against the corresponding source
files at runtime but doesn’t do so for unchecked hash-based pycs. Unchecked
hash-based `.pyc` files are a useful performance optimization for environments
where a system external to Python (e.g., the build system) is responsible for
keeping `.pyc` files up-to-date.

See [Cached bytecode invalidation](../reference/import.html#pyc-invalidation) for more information.

See also

- **PEP 552**
- PEP written and implemented by Benjamin Peterson 

### PEP 545: Python Documentation Translations[¶](#pep-545-python-documentation-translations)

[ PEP 545](https://peps.python.org/pep-0545/) describes the process of creating and maintaining Python
documentation translations.

Three new translations have been added:

- Japanese: - [https://docs.python.org/ja/](https://docs.python.org/ja/)
- French: - [https://docs.python.org/fr/](https://docs.python.org/fr/)
- Korean: - [https://docs.python.org/ko/](https://docs.python.org/ko/)

See also

- **PEP 545**
- PEP written and implemented by Julien Palard, Inada Naoki, and Victor Stinner. 

### Python Development Mode (-X dev)[¶](#python-development-mode-x-dev)

The new `-X``dev` command line option or the new
[ PYTHONDEVMODE](../using/cmdline.html#envvar-PYTHONDEVMODE) environment variable can be used to enable

[Python Development Mode](../library/devmode.html#devmode). When in development mode, Python performs additional runtime checks that are too expensive to be enabled by default. See

[Python Development Mode](../library/devmode.html#devmode)documentation for the full description.

## Other Language Changes[¶](#other-language-changes)

- An - `await`- `async for`- [formatted string literals](../reference/lexical_analysis.html#f-strings)due to a problem with the implementation. In Python 3.7 this restriction was lifted.
- More than 255 arguments can now be passed to a function, and a function can now have more than 255 parameters. (Contributed by Serhiy Storchaka in - [bpo-12844](https://bugs.python.org/issue?@action=redirect&bpo=12844)and- [bpo-18896](https://bugs.python.org/issue?@action=redirect&bpo=18896).)
- `bytes.fromhex()`- `bytearray.fromhex()`- [bpo-28927](https://bugs.python.org/issue?@action=redirect&bpo=28927).)
- `str`- `bytes`- `bytearray`- `isascii()`- [bpo-32677](https://bugs.python.org/issue?@action=redirect&bpo=32677).)
- `ImportError`- `__file__`path when- `from ... import ...`fails. (Contributed by Matthias Bussonnier in- [bpo-29546](https://bugs.python.org/issue?@action=redirect&bpo=29546).)
- Circular imports involving absolute imports with binding a submodule to a name are now supported. (Contributed by Serhiy Storchaka in - [bpo-30024](https://bugs.python.org/issue?@action=redirect&bpo=30024).)
- `object.__format__(x, '')`is now equivalent to- `str(x)`rather than- `format(str(self), '')`. (Contributed by Serhiy Storchaka in- [bpo-28974](https://bugs.python.org/issue?@action=redirect&bpo=28974).)
- In order to better support dynamic creation of stack traces, - `types.TracebackType`- `tb_next`- [tracebacks](../reference/datamodel.html#traceback-objects)is now writable. (Contributed by Nathaniel J. Smith in- [bpo-30579](https://bugs.python.org/issue?@action=redirect&bpo=30579).)
- When using the - `-m`- `sys.path[0]`is now eagerly expanded to the full starting directory path, rather than being left as the empty directory (which allows imports from the- *current*working directory at the time when an import occurs) (Contributed by Nick Coghlan in- [bpo-33053](https://bugs.python.org/issue?@action=redirect&bpo=33053).)
- The new - `-X`- `importtime`option or the- `PYTHONPROFILEIMPORTTIME`- [bpo-31415](https://bugs.python.org/issue?@action=redirect&bpo=31415).)

## New Modules[¶](#new-modules)

### contextvars[¶](#contextvars)

The new [ contextvars](../library/contextvars.html#module-contextvars) module and a set of

[new C APIs](../c-api/contextvars.html#contextvarsobjects)introduce support for

*context variables*. Context variables are conceptually similar to thread-local variables. Unlike TLS, context variables support asynchronous code correctly.

The [ asyncio](../library/asyncio.html#module-asyncio) and 

[modules have been updated to use and support context variables out of the box. Particularly the active decimal context is now stored in a context variable, which allows decimal operations to work with the correct context in asynchronous code.](../library/decimal.html#module-decimal)

`decimal`See also

- **PEP 567**
- PEP written and implemented by Yury Selivanov 

### dataclasses[¶](#dataclasses)

The new [ dataclass()](../library/dataclasses.html#dataclasses.dataclass) decorator provides a way to declare

*data classes*. A data class describes its attributes using class variable annotations. Its constructor and other magic methods, such as

[,](../reference/datamodel.html#object.__repr__)

`__repr__()`[, and](../reference/datamodel.html#object.__eq__)

`__eq__()`[are generated automatically.](../reference/datamodel.html#object.__hash__)

`__hash__()`Example:

```
@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0
p = Point(1.5, 2.5)
print(p)   # produces "Point(x=1.5, y=2.5, z=0.0)"
```
See also

- **PEP 557**
- PEP written and implemented by Eric V. Smith 

### importlib.resources[¶](#importlib-resources)

The new [ importlib.resources](../library/importlib.resources.html#module-importlib.resources) module provides several new APIs and one
new ABC for access to, opening, and reading 

*resources*inside packages. Resources are roughly similar to files inside packages, but they needn’t be actual files on the physical file system. Module loaders can provide a

`get_resource_reader()` function which returns
a [instance to support this new API. Built-in file path loaders and zip file loaders both support this.](../library/importlib.html#importlib.abc.ResourceReader)

`importlib.abc.ResourceReader`Contributed by Barry Warsaw and Brett Cannon in [bpo-32248](https://bugs.python.org/issue?@action=redirect&bpo=32248).

See also

[importlib_resources](https://importlib-resources.readthedocs.io/en/latest/)
– a PyPI backport for earlier Python versions.

## Improved Modules[¶](#improved-modules)

### argparse[¶](#argparse)

The new [ ArgumentParser.parse_intermixed_args()](../library/argparse.html#argparse.ArgumentParser.parse_intermixed_args)
method allows intermixing options and positional arguments.
(Contributed by paul.j3 in 

[bpo-14191](https://bugs.python.org/issue?@action=redirect&bpo=14191).)

### asyncio[¶](#asyncio)

The [ asyncio](../library/asyncio.html#module-asyncio) module has received many new features, usability and

[performance improvements](#whatsnew37-asyncio-perf). Notable changes include:

- The new - [provisional](../glossary.html#term-provisional-API)- `asyncio.run()`- [bpo-32314](https://bugs.python.org/issue?@action=redirect&bpo=32314).)
- asyncio gained support for - `contextvars`- `loop.call_soon()`- `loop.call_soon_threadsafe()`- `loop.call_later()`- `loop.call_at()`- `Future.add_done_callback()`- *context*parameter.- `Tasks`- **PEP 567**- [bpo-32436](https://bugs.python.org/issue?@action=redirect&bpo=32436).)
- The new - `asyncio.create_task()`- `asyncio.get_event_loop().create_task()`. (Contributed by Andrew Svetlov in- [bpo-32311](https://bugs.python.org/issue?@action=redirect&bpo=32311).)
- The new - `loop.start_tls()`- [bpo-23749](https://bugs.python.org/issue?@action=redirect&bpo=23749).)
- The new - `loop.sock_recv_into()`- [bpo-31819](https://bugs.python.org/issue?@action=redirect&bpo=31819).)
- The new - `asyncio.current_task()`- `Task`- `asyncio.all_tasks()`- `Task`instances in a given loop. The- `Task.current_task()`and- `Task.all_tasks()`methods have been deprecated. (Contributed by Andrew Svetlov in- [bpo-32250](https://bugs.python.org/issue?@action=redirect&bpo=32250).)
- The new - *provisional*- `BufferedProtocol`- [bpo-32251](https://bugs.python.org/issue?@action=redirect&bpo=32251).)
- The new - `asyncio.get_running_loop()`- `RuntimeError`- `asyncio.get_event_loop()`- *create*a new event loop if none is running. (Contributed by Yury Selivanov in- [bpo-32269](https://bugs.python.org/issue?@action=redirect&bpo=32269).)
- The new - `StreamWriter.wait_closed()`- `StreamWriter.is_closing()`- [bpo-32391](https://bugs.python.org/issue?@action=redirect&bpo=32391).)
- The new - `loop.sock_sendfile()`- `os.sendfile`- [bpo-32410](https://bugs.python.org/issue?@action=redirect&bpo=32410).)
- The new - `Future.get_loop()`- `Task.get_loop()`methods return the instance of the loop on which a task or a future were created.- `Server.get_loop()`- `asyncio.Server`- [bpo-32415](https://bugs.python.org/issue?@action=redirect&bpo=32415)and Srinivas Reddy Thatiparthy in- [bpo-32418](https://bugs.python.org/issue?@action=redirect&bpo=32418).)
- It is now possible to control how instances of - `asyncio.Server`- *start_serving*keyword argument to- `loop.create_server()`- `loop.create_unix_server()`- `Server.start_serving()`- `Server.serve_forever()`- `Server.is_serving()`- `True`if the server is serving.- `Server`objects are now asynchronous context managers:- srv = await loop.create_server(...) async with srv: # some code # At this point, srv is closed and no longer accepts new connections. - (Contributed by Yury Selivanov in - [bpo-32662](https://bugs.python.org/issue?@action=redirect&bpo=32662).)
- Callback objects returned by - `loop.call_later()`- `when()`- [bpo-32741](https://bugs.python.org/issue?@action=redirect&bpo=32741).)
- The - `loop.create_datagram_endpoint()`- [bpo-31245](https://bugs.python.org/issue?@action=redirect&bpo=31245).)
- The - `asyncio.open_connection()`- `asyncio.start_server()`- `loop.create_connection()`- `loop.create_server()`- `loop.create_accepted_socket()`- *ssl_handshake_timeout*keyword argument. (Contributed by Neil Aspinall in- [bpo-29970](https://bugs.python.org/issue?@action=redirect&bpo=29970).)
- The new - `Handle.cancelled()`- `True`if the callback was cancelled. (Contributed by Marat Sharafutdinov in- [bpo-31943](https://bugs.python.org/issue?@action=redirect&bpo=31943).)
- The asyncio source has been converted to use the - `async`- `await`- [bpo-32193](https://bugs.python.org/issue?@action=redirect&bpo=32193).)
- The new - `ReadTransport.is_reading()`- `ReadTransport.resume_reading()`- `ReadTransport.pause_reading()`- [bpo-32356](https://bugs.python.org/issue?@action=redirect&bpo=32356).)
- Loop methods which accept socket paths now support passing - [path-like objects](../glossary.html#term-path-like-object). (Contributed by Yury Selivanov in- [bpo-32066](https://bugs.python.org/issue?@action=redirect&bpo=32066).)
- In - `asyncio`- `TCP_NODELAY`flag set by default. (Contributed by Yury Selivanov and Victor Stinner in- [bpo-27456](https://bugs.python.org/issue?@action=redirect&bpo=27456).)
- Exceptions occurring in cancelled tasks are no longer logged. (Contributed by Yury Selivanov in - [bpo-30508](https://bugs.python.org/issue?@action=redirect&bpo=30508).)
- New - `WindowsSelectorEventLoopPolicy`and- `WindowsProactorEventLoopPolicy`classes. (Contributed by Yury Selivanov in- [bpo-33792](https://bugs.python.org/issue?@action=redirect&bpo=33792).)

Several `asyncio` APIs have been
[deprecated](#whatsnew37-asyncio-deprecated).

### binascii[¶](#binascii)

The [ b2a_uu()](../library/binascii.html#binascii.b2a_uu) function now accepts an optional 

*backtick*keyword argument. When it’s true, zeros are represented by

`'`'`
instead of spaces.  (Contributed by Xiang Zhang in [bpo-30103](https://bugs.python.org/issue?@action=redirect&bpo=30103).)

### calendar[¶](#calendar)

The [ HTMLCalendar](../library/calendar.html#calendar.HTMLCalendar) class has new class attributes which ease
the customization of CSS classes in the produced HTML calendar.
(Contributed by Oz Tiram in 

[bpo-30095](https://bugs.python.org/issue?@action=redirect&bpo=30095).)

### collections[¶](#collections)

`collections.namedtuple()` now supports default values.
(Contributed by Raymond Hettinger in [bpo-32320](https://bugs.python.org/issue?@action=redirect&bpo=32320).)

### compileall[¶](#compileall)

[ compileall.compile_dir()](../library/compileall.html#compileall.compile_dir) learned the new 

*invalidation_mode*parameter, which can be used to enable

[hash-based .pyc invalidation](#whatsnew37-pep552). The invalidation mode can also be specified on the command line using the new

`--invalidation-mode` argument.
(Contributed by Benjamin Peterson in [bpo-31650](https://bugs.python.org/issue?@action=redirect&bpo=31650).)

### concurrent.futures[¶](#concurrent-futures)

[ ProcessPoolExecutor](../library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor) and

[now support the new](../library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor)

`ThreadPoolExecutor`*initializer*and

*initargs*constructor arguments. (Contributed by Antoine Pitrou in

[bpo-21423](https://bugs.python.org/issue?@action=redirect&bpo=21423).)

The [ ProcessPoolExecutor](../library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor)
can now take the multiprocessing context via the new 

*mp_context*argument. (Contributed by Thomas Moreau in

[bpo-31540](https://bugs.python.org/issue?@action=redirect&bpo=31540).)

### contextlib[¶](#contextlib)

The new [ nullcontext()](../library/contextlib.html#contextlib.nullcontext) is a simpler and faster no-op
context manager than 

[. (Contributed by Jesse-Bakker in](../library/contextlib.html#contextlib.ExitStack)

`ExitStack`[bpo-10049](https://bugs.python.org/issue?@action=redirect&bpo=10049).)

The new [ asynccontextmanager()](../library/contextlib.html#contextlib.asynccontextmanager),

[, and](../library/contextlib.html#contextlib.AbstractAsyncContextManager)

`AbstractAsyncContextManager`[have been added to complement their synchronous counterparts. (Contributed by Jelle Zijlstra in](../library/contextlib.html#contextlib.AsyncExitStack)

`AsyncExitStack`[bpo-29679](https://bugs.python.org/issue?@action=redirect&bpo=29679)and

[bpo-30241](https://bugs.python.org/issue?@action=redirect&bpo=30241), and by Alexander Mohr and Ilya Kulakov in

[bpo-29302](https://bugs.python.org/issue?@action=redirect&bpo=29302).)

### cProfile[¶](#cprofile)

The [ cProfile](../library/profile.html#module-cProfile) command line now accepts 

`-m module_name` as an
alternative to script path.  (Contributed by Sanyam Khurana in [bpo-21862](https://bugs.python.org/issue?@action=redirect&bpo=21862).)

### crypt[¶](#crypt)

The `crypt` module now supports the Blowfish hashing method.
(Contributed by Serhiy Storchaka in [bpo-31664](https://bugs.python.org/issue?@action=redirect&bpo=31664).)

The `mksalt()` function now allows specifying the number of rounds
for hashing.  (Contributed by Serhiy Storchaka in [bpo-31702](https://bugs.python.org/issue?@action=redirect&bpo=31702).)

### datetime[¶](#datetime)

The new [ datetime.fromisoformat()](../library/datetime.html#datetime.datetime.fromisoformat)
method constructs a 

[object from a string in one of the formats output by](../library/datetime.html#datetime.datetime)

`datetime`[. (Contributed by Paul Ganssle in](../library/datetime.html#datetime.datetime.isoformat)

`datetime.isoformat()`[bpo-15873](https://bugs.python.org/issue?@action=redirect&bpo=15873).)

The [ tzinfo](../library/datetime.html#datetime.tzinfo) class now supports sub-minute offsets.
(Contributed by Alexander Belopolsky in 

[bpo-5288](https://bugs.python.org/issue?@action=redirect&bpo=5288).)

### dbm[¶](#dbm)

[ dbm.dumb](../library/dbm.html#module-dbm.dumb) now supports reading read-only files and no longer writes the
index file when it is not changed.

### decimal[¶](#decimal)

The [ decimal](../library/decimal.html#module-decimal) module now uses 

[context variables](#whatsnew37-pep567)to store the decimal context. (Contributed by Yury Selivanov in

[bpo-32630](https://bugs.python.org/issue?@action=redirect&bpo=32630).)

### dis[¶](#dis)

The [ dis()](../library/dis.html#dis.dis) function is now able to
disassemble nested code objects (the code of comprehensions, generator
expressions and nested functions, and the code used for building nested
classes).  The maximum depth of disassembly recursion is controlled by
the new 

*depth*parameter. (Contributed by Serhiy Storchaka in

[bpo-11822](https://bugs.python.org/issue?@action=redirect&bpo=11822).)

### distutils[¶](#distutils)

`README.rst` is now included in the list of distutils standard READMEs and
therefore included in source distributions.
(Contributed by Ryan Gonzalez in [bpo-11913](https://bugs.python.org/issue?@action=redirect&bpo=11913).)

### enum[¶](#enum)

The [ Enum](../library/enum.html#enum.Enum) learned the new 

`_ignore_` class property,
which allows listing the names of properties which should not become
enum members.
(Contributed by Ethan Furman in [bpo-31801](https://bugs.python.org/issue?@action=redirect&bpo=31801).)

In Python 3.8, attempting to check for non-Enum objects in [ Enum](../library/enum.html#enum.Enum)
classes will raise a 

[(e.g.](../library/exceptions.html#TypeError)

`TypeError``1 in Color`); similarly,
attempting to check for non-Flag objects in a [member will raise](../library/enum.html#enum.Flag)

`Flag``TypeError` (e.g. `1 in Perm.RW`); currently, both operations
return [instead and are deprecated. (Contributed by Ethan Furman in](../library/constants.html#False)

`False`[bpo-33217](https://bugs.python.org/issue?@action=redirect&bpo=33217).)

### functools[¶](#functools)

[ functools.singledispatch()](../library/functools.html#functools.singledispatch) now supports registering implementations
using type annotations.
(Contributed by Łukasz Langa in 

[bpo-32227](https://bugs.python.org/issue?@action=redirect&bpo=32227).)

### gc[¶](#gc)

The new [ gc.freeze()](../library/gc.html#gc.freeze) function allows freezing all objects tracked
by the garbage collector and excluding them from future collections.
This can be used before a POSIX 

`fork()` call to make the GC copy-on-write
friendly or to speed up collection.  The new [functions reverses this operation. Additionally,](../library/gc.html#gc.unfreeze)

`gc.unfreeze()`[can be used to obtain the number of frozen objects. (Contributed by Li Zekun in](../library/gc.html#gc.get_freeze_count)

`gc.get_freeze_count()`[bpo-31558](https://bugs.python.org/issue?@action=redirect&bpo=31558).)

### hmac[¶](#hmac)

The [ hmac](../library/hmac.html#module-hmac) module now has an optimized one-shot 

[function, which is up to three times faster than](../library/hmac.html#hmac.digest)

`digest()`[. (Contributed by Christian Heimes in](../library/hmac.html#hmac.HMAC)

`HMAC()`[bpo-32433](https://bugs.python.org/issue?@action=redirect&bpo=32433).)

### http.client[¶](#http-client)

[ HTTPConnection](../library/http.client.html#http.client.HTTPConnection) and 

[now support the new](../library/http.client.html#http.client.HTTPSConnection)

`HTTPSConnection`*blocksize*argument for improved upload throughput. (Contributed by Nir Soffer in

[bpo-31945](https://bugs.python.org/issue?@action=redirect&bpo=31945).)

### http.server[¶](#http-server)

[ SimpleHTTPRequestHandler](../library/http.server.html#http.server.SimpleHTTPRequestHandler) now supports the HTTP

`If-Modified-Since` header.  The server returns the 304 response status if
the target file was not modified after the time specified in the header.
(Contributed by Pierre Quentel in [bpo-29654](https://bugs.python.org/issue?@action=redirect&bpo=29654).)

[ SimpleHTTPRequestHandler](../library/http.server.html#http.server.SimpleHTTPRequestHandler) accepts the new 

*directory*argument, in addition to the new

`--directory` command line argument.
With this parameter, the server serves the specified directory, by default it
uses the current working directory.
(Contributed by Stéphane Wirtel and Julien Palard in [bpo-28707](https://bugs.python.org/issue?@action=redirect&bpo=28707).)

The new [ ThreadingHTTPServer](../library/http.server.html#http.server.ThreadingHTTPServer) class
uses threads to handle requests using 

[. It is used when](../library/socketserver.html#socketserver.ThreadingMixIn)

`ThreadingMixIn``http.server` is run with `-m`.
(Contributed by Julien Palard in [bpo-31639](https://bugs.python.org/issue?@action=redirect&bpo=31639).)

### idlelib and IDLE[¶](#idlelib-and-idle)

Multiple fixes for autocompletion. (Contributed by Louie Lu in [bpo-15786](https://bugs.python.org/issue?@action=redirect&bpo=15786).)

Module Browser (on the File menu, formerly called Class Browser),
now displays nested functions and classes in addition to top-level
functions and classes.
(Contributed by Guilherme Polo, Cheryl Sabella, and Terry Jan Reedy
in [bpo-1612262](https://bugs.python.org/issue?@action=redirect&bpo=1612262).)

The Settings dialog (Options, Configure IDLE) has been partly rewritten to improve both appearance and function. (Contributed by Cheryl Sabella and Terry Jan Reedy in multiple issues.)

The font sample now includes a selection of non-Latin characters so that
users can better see the effect of selecting a particular font.
(Contributed by Terry Jan Reedy in [bpo-13802](https://bugs.python.org/issue?@action=redirect&bpo=13802).)
The sample can be edited to include other characters.
(Contributed by Serhiy Storchaka in [bpo-31860](https://bugs.python.org/issue?@action=redirect&bpo=31860).)

The IDLE features formerly implemented as extensions have been reimplemented
as normal features.  Their settings have been moved from the Extensions tab
to other dialog tabs.
(Contributed by Charles Wohlganger and Terry Jan Reedy in [bpo-27099](https://bugs.python.org/issue?@action=redirect&bpo=27099).)

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

New in 3.7.1:

Output over N lines (50 by default) is squeezed down to a button.
N can be changed in the PyShell section of the General page of the
Settings dialog.  Fewer, but possibly extra long, lines can be squeezed by
right clicking on the output.  Squeezed output can be expanded in place
by double-clicking the button or into the clipboard or a separate window
by right-clicking the button.  (Contributed by Tal Einat in [bpo-1529353](https://bugs.python.org/issue?@action=redirect&bpo=1529353).)

The changes above have been backported to 3.6 maintenance releases.

NEW in 3.7.4:

Add “Run Customized” to the Run menu to run a module with customized
settings. Any command line arguments entered are added to sys.argv.
They re-appear in the box for the next customized run.  One can also
suppress the normal Shell main module restart.  (Contributed by Cheryl
Sabella, Terry Jan Reedy, and others in [bpo-5680](https://bugs.python.org/issue?@action=redirect&bpo=5680) and [bpo-37627](https://bugs.python.org/issue?@action=redirect&bpo=37627).)

New in 3.7.5:

Add optional line numbers for IDLE editor windows. Windows
open without line numbers unless set otherwise in the General
tab of the configuration dialog.  Line numbers for an existing
window are shown and hidden in the Options menu.
(Contributed by Tal Einat and Saimadhav Heblikar in [bpo-17535](https://bugs.python.org/issue?@action=redirect&bpo=17535).)

### importlib[¶](#importlib)

The [ importlib.abc.ResourceReader](../library/importlib.html#importlib.abc.ResourceReader) ABC was introduced to
support the loading of resources from packages.  See also

[importlib.resources](#whatsnew37-importlib-resources). (Contributed by Barry Warsaw, Brett Cannon in

[bpo-32248](https://bugs.python.org/issue?@action=redirect&bpo=32248).)

[ importlib.reload()](../library/importlib.html#importlib.reload) now raises 

[if the module lacks a spec. (Contributed by Garvit Khatri in](../library/exceptions.html#ModuleNotFoundError)

`ModuleNotFoundError`[bpo-29851](https://bugs.python.org/issue?@action=redirect&bpo=29851).)

[ importlib.util.find_spec()](../library/importlib.html#importlib.util.find_spec) now raises 

[instead of](../library/exceptions.html#ModuleNotFoundError)

`ModuleNotFoundError`[if the specified parent module is not a package (i.e. lacks a](../library/exceptions.html#AttributeError)

`AttributeError``__path__` attribute).
(Contributed by Milan Oberkirch in [bpo-30436](https://bugs.python.org/issue?@action=redirect&bpo=30436).)

The new [ importlib.util.source_hash()](../library/importlib.html#importlib.util.source_hash) can be used to compute the hash of
the passed source.  A 

[hash-based .pyc file](#whatsnew37-pep552)embeds the value returned by this function.

### io[¶](#io)

The new [ TextIOWrapper.reconfigure()](../library/io.html#io.TextIOWrapper.reconfigure)
method can be used to reconfigure the text stream with the new settings.
(Contributed by Antoine Pitrou in 

[bpo-30526](https://bugs.python.org/issue?@action=redirect&bpo=30526)and INADA Naoki in

[bpo-15216](https://bugs.python.org/issue?@action=redirect&bpo=15216).)

### ipaddress[¶](#ipaddress)

The new `subnet_of()` and `supernet_of()` methods of
[ ipaddress.IPv6Network](../library/ipaddress.html#ipaddress.IPv6Network) and 

[can be used for network containment tests. (Contributed by Michel Albert and Cheryl Sabella in](../library/ipaddress.html#ipaddress.IPv4Network)

`ipaddress.IPv4Network`[bpo-20825](https://bugs.python.org/issue?@action=redirect&bpo=20825).)

### itertools[¶](#itertools)

[ itertools.islice()](../library/itertools.html#itertools.islice) now accepts

[as start, stop, and slice arguments. (Contributed by Will Roberts in](../reference/datamodel.html#object.__index__)

`integer-like objects`[bpo-30537](https://bugs.python.org/issue?@action=redirect&bpo=30537).)

### locale[¶](#locale)

The new *monetary* argument to [ locale.format_string()](../library/locale.html#locale.format_string) can be used
to make the conversion use monetary thousands separators and
grouping strings.  (Contributed by Garvit in 

[bpo-10379](https://bugs.python.org/issue?@action=redirect&bpo=10379).)

The [ locale.getpreferredencoding()](../library/locale.html#locale.getpreferredencoding) function now always returns 

`'UTF-8'`
on Android or when in the [forced UTF-8 mode](#whatsnew37-pep540).

### logging[¶](#logging)

[ Logger](../library/logging.html#logging.Logger) instances can now be pickled.
(Contributed by Vinay Sajip in 

[bpo-30520](https://bugs.python.org/issue?@action=redirect&bpo=30520).)

The new [ StreamHandler.setStream()](../library/logging.handlers.html#logging.StreamHandler.setStream)
method can be used to replace the logger stream after handler creation.
(Contributed by Vinay Sajip in 

[bpo-30522](https://bugs.python.org/issue?@action=redirect&bpo=30522).)

It is now possible to specify keyword arguments to handler constructors in
configuration passed to [ logging.config.fileConfig()](../library/logging.config.html#logging.config.fileConfig).
(Contributed by Preston Landers in 

[bpo-31080](https://bugs.python.org/issue?@action=redirect&bpo=31080).)

### math[¶](#math)

The new [ math.remainder()](../library/math.html#math.remainder) function implements the IEEE 754-style remainder
operation.  (Contributed by Mark Dickinson in 

[bpo-29962](https://bugs.python.org/issue?@action=redirect&bpo=29962).)

### mimetypes[¶](#mimetypes)

The MIME type of .bmp has been changed from `'image/x-ms-bmp'` to
`'image/bmp'`.
(Contributed by Nitish Chandra in [bpo-22589](https://bugs.python.org/issue?@action=redirect&bpo=22589).)

### msilib[¶](#msilib)

The new `Database.Close()` method can be used
to close the MSI database.
(Contributed by Berker Peksag in [bpo-20486](https://bugs.python.org/issue?@action=redirect&bpo=20486).)

### multiprocessing[¶](#multiprocessing)

The new [ Process.close()](../library/multiprocessing.html#multiprocessing.Process.close) method
explicitly closes the process object and releases all resources associated
with it.  

[is raised if the underlying process is still running. (Contributed by Antoine Pitrou in](../library/exceptions.html#ValueError)

`ValueError`[bpo-30596](https://bugs.python.org/issue?@action=redirect&bpo=30596).)

The new [ Process.kill()](../library/multiprocessing.html#multiprocessing.Process.kill) method can
be used to terminate the process using the 

[signal on Unix. (Contributed by Vitor Pereira in](../library/signal.html#signal.SIGKILL)

`SIGKILL`[bpo-30794](https://bugs.python.org/issue?@action=redirect&bpo=30794).)

Non-daemonic threads created by [ Process](../library/multiprocessing.html#multiprocessing.Process) are now
joined on process exit.
(Contributed by Antoine Pitrou in 

[bpo-18966](https://bugs.python.org/issue?@action=redirect&bpo=18966).)

### os[¶](#os)

[ os.fwalk()](../library/os.html#os.fwalk) now accepts the 

*path*argument as

[. (Contributed by Serhiy Storchaka in](../library/stdtypes.html#bytes)

`bytes`[bpo-28682](https://bugs.python.org/issue?@action=redirect&bpo=28682).)

[ os.scandir()](../library/os.html#os.scandir) gained support for 

[file descriptors](../library/os.html#path-fd). (Contributed by Serhiy Storchaka in

[bpo-25996](https://bugs.python.org/issue?@action=redirect&bpo=25996).)

The new [ register_at_fork()](../library/os.html#os.register_at_fork) function allows registering Python
callbacks to be executed at process fork.
(Contributed by Antoine Pitrou in 

[bpo-16500](https://bugs.python.org/issue?@action=redirect&bpo=16500).)

Added [ os.preadv()](../library/os.html#os.preadv) (combine the functionality of 

[and](../library/os.html#os.readv)

`os.readv()`[) and](../library/os.html#os.pread)

`os.pread()`[functions (combine the functionality of](../library/os.html#os.pwritev)

`os.pwritev()`[and](../library/os.html#os.writev)

`os.writev()`[). (Contributed by Pablo Galindo in](../library/os.html#os.pwrite)

`os.pwrite()`[bpo-31368](https://bugs.python.org/issue?@action=redirect&bpo=31368).)

The mode argument of [ os.makedirs()](../library/os.html#os.makedirs) no longer affects the file
permission bits of newly created intermediate-level directories.
(Contributed by Serhiy Storchaka in 

[bpo-19930](https://bugs.python.org/issue?@action=redirect&bpo=19930).)

[ os.dup2()](../library/os.html#os.dup2) now returns the new file descriptor.  Previously, 

`None`
was always returned.
(Contributed by Benjamin Peterson in [bpo-32441](https://bugs.python.org/issue?@action=redirect&bpo=32441).)

The structure returned by [ os.stat()](../library/os.html#os.stat) now contains the

[attribute on Solaris and its derivatives. (Contributed by Jesús Cea Avión in](../library/os.html#os.stat_result.st_fstype)

`st_fstype`[bpo-32659](https://bugs.python.org/issue?@action=redirect&bpo=32659).)

### pathlib[¶](#pathlib)

The new [ Path.is_mount()](../library/pathlib.html#pathlib.Path.is_mount) method is now available
on POSIX systems and can be used to determine whether a path is a mount point.
(Contributed by Cooper Ry Lees in 

[bpo-30897](https://bugs.python.org/issue?@action=redirect&bpo=30897).)

### pdb[¶](#pdb)

[ pdb.set_trace()](../library/pdb.html#pdb.set_trace) now takes an optional 

*header*keyword-only argument. If given, it is printed to the console just before debugging begins. (Contributed by Barry Warsaw in

[bpo-31389](https://bugs.python.org/issue?@action=redirect&bpo=31389).)

[ pdb](../library/pdb.html#module-pdb) command line now accepts 

`-m module_name` as an alternative to
script file.  (Contributed by Mario Corchero in [bpo-32206](https://bugs.python.org/issue?@action=redirect&bpo=32206).)

### py_compile[¶](#py-compile)

[ py_compile.compile()](../library/py_compile.html#py_compile.compile) – and by extension, 

[– now respects the](../library/compileall.html#module-compileall)

`compileall``SOURCE_DATE_EPOCH` environment variable by
unconditionally creating `.pyc` files for hash-based validation.
This allows for guaranteeing
[reproducible builds](https://reproducible-builds.org/)of

`.pyc`
files when they are created eagerly. (Contributed by Bernhard M. Wiedemann
in [bpo-29708](https://bugs.python.org/issue?@action=redirect&bpo=29708).)

### pydoc[¶](#pydoc)

The pydoc server can now bind to an arbitrary hostname specified by the
new `-n` command-line argument.
(Contributed by Feanil Patel in [bpo-31128](https://bugs.python.org/issue?@action=redirect&bpo=31128).)

### queue[¶](#queue)

The new [ SimpleQueue](../library/queue.html#queue.SimpleQueue) class is an unbounded FIFO queue.
(Contributed by Antoine Pitrou in 

[bpo-14976](https://bugs.python.org/issue?@action=redirect&bpo=14976).)

### re[¶](#re)

The flags [ re.ASCII](../library/re.html#re.ASCII), 

[and](../library/re.html#re.LOCALE)

`re.LOCALE`[can be set within the scope of a group. (Contributed by Serhiy Storchaka in](../library/re.html#re.UNICODE)

`re.UNICODE`[bpo-31690](https://bugs.python.org/issue?@action=redirect&bpo=31690).)

[ re.split()](../library/re.html#re.split) now supports splitting on a pattern like 

`r'\b'`,
`'^$'` or `(?=-)` that matches an empty string.
(Contributed by Serhiy Storchaka in [bpo-25054](https://bugs.python.org/issue?@action=redirect&bpo=25054).)

Regular expressions compiled with the [ re.LOCALE](../library/re.html#re.LOCALE) flag no longer
depend on the locale at compile time.  Locale settings are applied only
when the compiled regular expression is used.
(Contributed by Serhiy Storchaka in 

[bpo-30215](https://bugs.python.org/issue?@action=redirect&bpo=30215).)

[ FutureWarning](../library/exceptions.html#FutureWarning) is now emitted if a regular expression contains
character set constructs that will change semantically in the future,
such as nested sets and set operations.
(Contributed by Serhiy Storchaka in 

[bpo-30349](https://bugs.python.org/issue?@action=redirect&bpo=30349).)

Compiled regular expression and match objects can now be copied
using [ copy.copy()](../library/copy.html#copy.copy) and 

[. (Contributed by Serhiy Storchaka in](../library/copy.html#copy.deepcopy)

`copy.deepcopy()`[bpo-10076](https://bugs.python.org/issue?@action=redirect&bpo=10076).)

### signal[¶](#signal)

The new *warn_on_full_buffer* argument to the [ signal.set_wakeup_fd()](../library/signal.html#signal.set_wakeup_fd)
function makes it possible to specify whether Python prints a warning on
stderr when the wakeup buffer overflows.
(Contributed by Nathaniel J. Smith in 

[bpo-30050](https://bugs.python.org/issue?@action=redirect&bpo=30050).)

### socket[¶](#socket)

The new [ socket.getblocking()](../library/socket.html#socket.socket.getblocking) method
returns 

`True` if the socket is in blocking mode and `False` otherwise.
(Contributed by Yury Selivanov in [bpo-32373](https://bugs.python.org/issue?@action=redirect&bpo=32373).)

The new [ socket.close()](../library/socket.html#socket.close) function closes the passed socket file descriptor.
This function should be used instead of 

[for better compatibility across platforms. (Contributed by Christian Heimes in](../library/os.html#os.close)

`os.close()`[bpo-32454](https://bugs.python.org/issue?@action=redirect&bpo=32454).)

The [ socket](../library/socket.html#module-socket) module now exposes the 

[socket.TCP_CONGESTION](../library/socket.html#socket-unix-constants)(Linux 2.6.13),

[socket.TCP_USER_TIMEOUT](../library/socket.html#socket-unix-constants)(Linux 2.6.37), and

[socket.TCP_NOTSENT_LOWAT](../library/socket.html#socket-unix-constants)(Linux 3.12) constants. (Contributed by Omar Sandoval in

[bpo-26273](https://bugs.python.org/issue?@action=redirect&bpo=26273)and Nathaniel J. Smith in

[bpo-29728](https://bugs.python.org/issue?@action=redirect&bpo=29728).)

Support for [ socket.AF_VSOCK](../library/socket.html#socket.AF_VSOCK) sockets has been added to allow
communication between virtual machines and their hosts.
(Contributed by Cathy Avery in 

[bpo-27584](https://bugs.python.org/issue?@action=redirect&bpo=27584).)

Sockets now auto-detect family, type and protocol from file descriptor
by default.
(Contributed by Christian Heimes in [bpo-28134](https://bugs.python.org/issue?@action=redirect&bpo=28134).)

### socketserver[¶](#socketserver)

[ socketserver.ThreadingMixIn.server_close](../library/socketserver.html#socketserver.BaseServer.server_close) now waits until all non-daemon
threads complete. 

`socketserver.ForkingMixIn.server_close` now waits
until all child processes complete.Add a new [ socketserver.ForkingMixIn.block_on_close](../library/socketserver.html#socketserver.ThreadingMixIn.block_on_close) class attribute to

[and](../library/socketserver.html#socketserver.ForkingMixIn)

`socketserver.ForkingMixIn`[classes. Set the class attribute to](../library/socketserver.html#socketserver.ThreadingMixIn)

`socketserver.ThreadingMixIn``False` to get the pre-3.7 behaviour.### sqlite3[¶](#sqlite3)

[ sqlite3.Connection](../library/sqlite3.html#sqlite3.Connection) now exposes the 

[method when the underlying SQLite library is at version 3.6.11 or higher. (Contributed by Lele Gaifax in](../library/sqlite3.html#sqlite3.Connection.backup)

`backup()`[bpo-27645](https://bugs.python.org/issue?@action=redirect&bpo=27645).)

The *database* argument of [ sqlite3.connect()](../library/sqlite3.html#sqlite3.connect) now accepts any

[path-like object](../glossary.html#term-path-like-object), instead of just a string. (Contributed by Anders Lorentsen in

[bpo-31843](https://bugs.python.org/issue?@action=redirect&bpo=31843).)

### ssl[¶](#ssl)

The [ ssl](../library/ssl.html#module-ssl) module now uses OpenSSL’s builtin API instead of

`match_hostname()` to check a host name or an IP address.  Values
are validated during TLS handshake.  Any certificate validation error
including failing the host name check now raises
[and aborts the handshake with a proper TLS Alert message. The new exception contains additional information. Host name validation can be customized with](../library/ssl.html#ssl.SSLCertVerificationError)

`SSLCertVerificationError`[. (Contributed by Christian Heimes in](../library/ssl.html#ssl.SSLContext.hostname_checks_common_name)

`SSLContext.hostname_checks_common_name`[bpo-31399](https://bugs.python.org/issue?@action=redirect&bpo=31399).)

Note

The improved host name check requires a *libssl* implementation compatible
with OpenSSL 1.0.2 or 1.1.  Consequently, OpenSSL 0.9.8 and 1.0.1 are no
longer supported (see [Platform Support Removals](#platform-support-removals) for more details).
The ssl module is mostly compatible with LibreSSL 2.7.2 and newer.

The `ssl` module no longer sends IP addresses in SNI TLS extension.
(Contributed by Christian Heimes in [bpo-32185](https://bugs.python.org/issue?@action=redirect&bpo=32185).)

`match_hostname()` no longer supports partial wildcards like
`www*.example.org`.
(Contributed by Mandeep Singh in [bpo-23033](https://bugs.python.org/issue?@action=redirect&bpo=23033) and Christian Heimes in
[bpo-31399](https://bugs.python.org/issue?@action=redirect&bpo=31399).)

The default cipher suite selection of the `ssl` module now uses a blacklist
approach rather than a hard-coded whitelist.  Python no longer re-enables
ciphers that have been blocked by OpenSSL security updates.  Default cipher
suite selection can be configured at compile time.
(Contributed by Christian Heimes in [bpo-31429](https://bugs.python.org/issue?@action=redirect&bpo=31429).)

Validation of server certificates containing internationalized domain names
(IDNs) is now supported.  As part of this change, the
[ SSLSocket.server_hostname](../library/ssl.html#ssl.SSLSocket.server_hostname) attribute
now stores the expected hostname in A-label form (

`"xn--pythn-mua.org"`),
rather than the U-label form (`"pythön.org"`).  (Contributed by
Nathaniel J. Smith and Christian Heimes in [bpo-28414](https://bugs.python.org/issue?@action=redirect&bpo=28414).)

The `ssl` module has preliminary and experimental support for TLS 1.3 and
OpenSSL 1.1.1.  At the time of Python 3.7.0 release, OpenSSL 1.1.1 is still
under development and TLS 1.3 hasn’t been finalized yet.  The TLS 1.3
handshake and protocol behaves slightly differently than TLS 1.2 and earlier,
see [TLS 1.3](../library/ssl.html#ssl-tlsv1-3).
(Contributed by Christian Heimes in [bpo-32947](https://bugs.python.org/issue?@action=redirect&bpo=32947), [bpo-20995](https://bugs.python.org/issue?@action=redirect&bpo=20995),
[bpo-29136](https://bugs.python.org/issue?@action=redirect&bpo=29136), [bpo-30622](https://bugs.python.org/issue?@action=redirect&bpo=30622) and [bpo-33618](https://bugs.python.org/issue?@action=redirect&bpo=33618))

[ SSLSocket](../library/ssl.html#ssl.SSLSocket) and 

[no longer have a public constructor. Direct instantiation was never a documented and supported feature. Instances must be created with](../library/ssl.html#ssl.SSLObject)

`SSLObject`[methods](../library/ssl.html#ssl.SSLContext)

`SSLContext`[and](../library/ssl.html#ssl.SSLContext.wrap_socket)

`wrap_socket()`[. (Contributed by Christian Heimes in](../library/ssl.html#ssl.SSLContext.wrap_bio)

`wrap_bio()`[bpo-32951](https://bugs.python.org/issue?@action=redirect&bpo=32951))

OpenSSL 1.1 APIs for setting the minimum and maximum TLS protocol version are
available as [ SSLContext.minimum_version](../library/ssl.html#ssl.SSLContext.minimum_version)
and 

[. Supported protocols are indicated by several new flags, such as](../library/ssl.html#ssl.SSLContext.maximum_version)

`SSLContext.maximum_version`[. (Contributed by Christian Heimes in](../library/ssl.html#ssl.HAS_TLSv1_1)

`HAS_TLSv1_1`[bpo-32609](https://bugs.python.org/issue?@action=redirect&bpo=32609).)

Added [ ssl.SSLContext.post_handshake_auth](../library/ssl.html#ssl.SSLContext.post_handshake_auth) to enable and

[to initiate TLS 1.3 post-handshake authentication. (Contributed by Christian Heimes in](../library/ssl.html#ssl.SSLSocket.verify_client_post_handshake)

`ssl.SSLSocket.verify_client_post_handshake()`[gh-78851](https://github.com/python/cpython/issues/78851).)

### string[¶](#string)

[ string.Template](../library/string.html#string.Template) now lets you to optionally modify the regular
expression pattern for braced placeholders and non-braced placeholders
separately.  (Contributed by Barry Warsaw in 

[bpo-1198569](https://bugs.python.org/issue?@action=redirect&bpo=1198569).)

### subprocess[¶](#subprocess)

The [ subprocess.run()](../library/subprocess.html#subprocess.run) function accepts the new 

*capture_output*keyword argument. When true, stdout and stderr will be captured. This is equivalent to passing

[as](../library/subprocess.html#subprocess.PIPE)

`subprocess.PIPE`*stdout*and

*stderr*arguments. (Contributed by Bo Bayles in

[bpo-32102](https://bugs.python.org/issue?@action=redirect&bpo=32102).)

The `subprocess.run` function and the [ subprocess.Popen](../library/subprocess.html#subprocess.Popen) constructor
now accept the 

*text*keyword argument as an alias to

*universal_newlines*. (Contributed by Andrew Clegg in

[bpo-31756](https://bugs.python.org/issue?@action=redirect&bpo=31756).)

On Windows the default for *close_fds* was changed from `False` to
`True` when redirecting the standard handles.  It’s now possible to set
*close_fds* to true when redirecting the standard handles.  See
[ subprocess.Popen](../library/subprocess.html#subprocess.Popen).  This means that 

*close_fds*now defaults to

`True` on all supported platforms.
(Contributed by Segev Finer in [bpo-19764](https://bugs.python.org/issue?@action=redirect&bpo=19764).)

The subprocess module is now more graceful when handling
[ KeyboardInterrupt](../library/exceptions.html#KeyboardInterrupt) during 

[,](../library/subprocess.html#subprocess.call)

`subprocess.call()`[, or in a](../library/subprocess.html#subprocess.run)

`subprocess.run()`[context manager. It now waits a short amount of time for the child to exit, before continuing the handling of the](../library/subprocess.html#subprocess.Popen)

`Popen``KeyboardInterrupt`
exception.
(Contributed by Gregory P. Smith in [bpo-25942](https://bugs.python.org/issue?@action=redirect&bpo=25942).)

### sys[¶](#sys)

The new [ sys.breakpointhook()](../library/sys.html#sys.breakpointhook) hook function is called by the
built-in 

[. (Contributed by Barry Warsaw in](../library/functions.html#breakpoint)

`breakpoint()`[bpo-31353](https://bugs.python.org/issue?@action=redirect&bpo=31353).)

On Android, the new [ sys.getandroidapilevel()](../library/sys.html#sys.getandroidapilevel) returns the build-time
Android API version.
(Contributed by Victor Stinner in 

[bpo-28740](https://bugs.python.org/issue?@action=redirect&bpo=28740).)

The new [ sys.get_coroutine_origin_tracking_depth()](../library/sys.html#sys.get_coroutine_origin_tracking_depth) function returns
the current coroutine origin tracking depth, as set by
the new 

[.](../library/sys.html#sys.set_coroutine_origin_tracking_depth)

`sys.set_coroutine_origin_tracking_depth()`[has been converted to use this new API instead of the deprecated](../library/asyncio.html#module-asyncio)

`asyncio``sys.set_coroutine_wrapper()`.
(Contributed by Nathaniel J. Smith in [bpo-32591](https://bugs.python.org/issue?@action=redirect&bpo=32591).)

### time[¶](#time)

[ PEP 564](https://peps.python.org/pep-0564/) adds six new functions with nanosecond resolution to the

[module:](../library/time.html#module-time)

`time`New clock identifiers have been added:

- `time.CLOCK_BOOTTIME`- `time.CLOCK_MONOTONIC`
- `time.CLOCK_PROF`
- `time.CLOCK_UPTIME`

The new [ time.thread_time()](../library/time.html#time.thread_time) and 

[functions can be used to get per-thread CPU time measurements. (Contributed by Antoine Pitrou in](../library/time.html#time.thread_time_ns)

`time.thread_time_ns()`[bpo-32025](https://bugs.python.org/issue?@action=redirect&bpo=32025).)

The new [ time.pthread_getcpuclockid()](../library/time.html#time.pthread_getcpuclockid) function returns the clock ID
of the thread-specific CPU-time clock.

### tkinter[¶](#tkinter)

The new [ tkinter.ttk.Spinbox](../library/tkinter.ttk.html#tkinter.ttk.Spinbox) class is now available.
(Contributed by Alan Moore in 

[bpo-32585](https://bugs.python.org/issue?@action=redirect&bpo=32585).)

### tracemalloc[¶](#tracemalloc)

[ tracemalloc.Traceback](../library/tracemalloc.html#tracemalloc.Traceback) behaves more like regular tracebacks,
sorting the frames from oldest to most recent.

[now accepts negative](../library/tracemalloc.html#tracemalloc.Traceback.format)

`Traceback.format()`*limit*, truncating the result to the

`abs(limit)` oldest frames.  To get the old behaviour, use
the new *most_recent_first*argument to

`Traceback.format()`.
(Contributed by Jesse Bakker in [bpo-32121](https://bugs.python.org/issue?@action=redirect&bpo=32121).)

### types[¶](#types)

The new [ WrapperDescriptorType](../library/types.html#types.WrapperDescriptorType),

[,](../library/types.html#types.MethodWrapperType)

`MethodWrapperType`[, and](../library/types.html#types.MethodDescriptorType)

`MethodDescriptorType`[classes are now available. (Contributed by Manuel Krebber and Guido van Rossum in](../library/types.html#types.ClassMethodDescriptorType)

`ClassMethodDescriptorType`[bpo-29377](https://bugs.python.org/issue?@action=redirect&bpo=29377), and Serhiy Storchaka in

[bpo-32265](https://bugs.python.org/issue?@action=redirect&bpo=32265).)

The new [ types.resolve_bases()](../library/types.html#types.resolve_bases) function resolves MRO entries
dynamically as specified by 

[. (Contributed by Ivan Levkivskyi in](https://peps.python.org/pep-0560/)

**PEP 560**[bpo-32717](https://bugs.python.org/issue?@action=redirect&bpo=32717).)

### unicodedata[¶](#unicodedata)

The internal [ unicodedata](../library/unicodedata.html#module-unicodedata) database has been upgraded to use 

[Unicode 11](https://www.unicode.org/versions/Unicode11.0.0/). (Contributed by Benjamin Peterson.)

### unittest[¶](#unittest)

The new `-k` command-line option allows filtering tests by a name
substring or a Unix shell-like pattern.
For example, `python -m unittest -k foo` runs
`foo_tests.SomeTest.test_something`, `bar_tests.SomeTest.test_foo`,
but not `bar_tests.FooTest.test_something`.
(Contributed by Jonas Haag in [bpo-32071](https://bugs.python.org/issue?@action=redirect&bpo=32071).)

### unittest.mock[¶](#unittest-mock)

The [ sentinel](../library/unittest.mock.html#unittest.mock.sentinel) attributes now preserve their identity
when they are 

[or](../library/copy.html#module-copy)

`copied`[. (Contributed by Serhiy Storchaka in](../library/pickle.html#module-pickle)

`pickled`[bpo-20804](https://bugs.python.org/issue?@action=redirect&bpo=20804).)

The new [ seal()](../library/unittest.mock.html#unittest.mock.seal) function allows sealing

[instances, which will disallow further creation of attribute mocks. The seal is applied recursively to all attributes that are themselves mocks. (Contributed by Mario Corchero in](../library/unittest.mock.html#unittest.mock.Mock)

`Mock`[bpo-30541](https://bugs.python.org/issue?@action=redirect&bpo=30541).)

### urllib.parse[¶](#urllib-parse)

[ urllib.parse.quote()](../library/urllib.parse.html#urllib.parse.quote) has been updated from 

[to](https://datatracker.ietf.org/doc/html/rfc2396.html)

**RFC 2396**[, adding](https://datatracker.ietf.org/doc/html/rfc3986.html)

**RFC 3986**`~` to the set of characters that are never quoted by default.
(Contributed by Christian Theune and Ratnadeep Debnath in [bpo-16285](https://bugs.python.org/issue?@action=redirect&bpo=16285).)

### uu[¶](#uu)

The `uu.encode()` function now accepts an optional *backtick*
keyword argument.  When it’s true, zeros are represented by `'`'`
instead of spaces.  (Contributed by Xiang Zhang in [bpo-30103](https://bugs.python.org/issue?@action=redirect&bpo=30103).)

### uuid[¶](#uuid)

The new [ UUID.is_safe](../library/uuid.html#uuid.UUID.is_safe) attribute relays information
from the platform about whether generated UUIDs are generated with a
multiprocessing-safe method.
(Contributed by Barry Warsaw in 

[bpo-22807](https://bugs.python.org/issue?@action=redirect&bpo=22807).)

[ uuid.getnode()](../library/uuid.html#uuid.getnode) now prefers universally administered
MAC addresses over locally administered MAC addresses.
This makes a better guarantee for global uniqueness of UUIDs returned
from 

[. If only locally administered MAC addresses are available, the first such one found is returned. (Contributed by Barry Warsaw in](../library/uuid.html#uuid.uuid1)

`uuid.uuid1()`[bpo-32107](https://bugs.python.org/issue?@action=redirect&bpo=32107).)

### warnings[¶](#warnings)

The initialization of the default warnings filters has changed as follows:

- warnings enabled via command line options (including those for - `-b`- `-X`- `dev`option) are always passed to the warnings machinery via the- `sys.warnoptions`
- warnings filters enabled via the command line or the environment now have the following order of precedence: - the - `BytesWarning`filter for- `-b`- `-bb`)
- any filters specified with the - `-W`
- any filters specified with the - `PYTHONWARNINGS`
- any other CPython specific filters (e.g. the - `default`filter added for the new- `-X dev`mode)
- any implicit filters defined directly by the warnings machinery 
 
- in - [CPython debug builds](../using/configure.html#debug-build), all warnings are now displayed by default (the implicit filter list is empty)

(Contributed by Nick Coghlan and Victor Stinner in [bpo-20361](https://bugs.python.org/issue?@action=redirect&bpo=20361),
[bpo-32043](https://bugs.python.org/issue?@action=redirect&bpo=32043), and [bpo-32230](https://bugs.python.org/issue?@action=redirect&bpo=32230).)

Deprecation warnings are once again shown by default in single-file scripts and
at the interactive prompt.  See [PEP 565: Show DeprecationWarning in __main__](#whatsnew37-pep565) for details.
(Contributed by Nick Coghlan in [bpo-31975](https://bugs.python.org/issue?@action=redirect&bpo=31975).)

### xml[¶](#xml)

As mitigation against DTD and external entity retrieval, the
[ xml.dom.minidom](../library/xml.dom.minidom.html#module-xml.dom.minidom) and 

[modules no longer process external entities by default. (Contributed by Christian Heimes in](../library/xml.sax.html#module-xml.sax)

`xml.sax`[gh-61441](https://github.com/python/cpython/issues/61441).)

### xml.etree[¶](#xml-etree)

[ElementPath](../library/xml.etree.elementtree.html#elementtree-xpath) predicates in the `find()`
methods can now compare text of the current node with `[. = "text"]`,
not only text in children.  Predicates also allow adding spaces for
better readability.  (Contributed by Stefan Behnel in [bpo-31648](https://bugs.python.org/issue?@action=redirect&bpo=31648).)

### xmlrpc.server[¶](#xmlrpc-server)

`SimpleXMLRPCDispatcher.register_function()`
can now be used as a decorator.  (Contributed by Xiang Zhang in
[bpo-7769](https://bugs.python.org/issue?@action=redirect&bpo=7769).)

### zipapp[¶](#zipapp)

Function [ create_archive()](../library/zipapp.html#zipapp.create_archive) now accepts an optional 

*filter*argument to allow the user to select which files should be included in the archive. (Contributed by Irmen de Jong in

[bpo-31072](https://bugs.python.org/issue?@action=redirect&bpo=31072).)

Function [ create_archive()](../library/zipapp.html#zipapp.create_archive) now accepts an optional 

*compressed*argument to generate a compressed archive. A command line option

`--compress` has also been added to support compression.
(Contributed by Zhiming Wang in [bpo-31638](https://bugs.python.org/issue?@action=redirect&bpo=31638).)

### zipfile[¶](#zipfile)

[ ZipFile](../library/zipfile.html#zipfile.ZipFile) now accepts the new 

*compresslevel*parameter to control the compression level. (Contributed by Bo Bayles in

[bpo-21417](https://bugs.python.org/issue?@action=redirect&bpo=21417).)

Subdirectories in archives created by `ZipFile` are now stored in
alphabetical order.
(Contributed by Bernhard M. Wiedemann in [bpo-30693](https://bugs.python.org/issue?@action=redirect&bpo=30693).)

## C API Changes[¶](#c-api-changes)

A new API for thread-local storage has been implemented.  See
[PEP 539: New C API for Thread-Local Storage](#whatsnew37-pep539) for an overview and
[Thread Specific Storage (TSS) API](../c-api/init.html#thread-specific-storage-api) for a complete reference.
(Contributed by Masayuki Yamamoto in [bpo-25658](https://bugs.python.org/issue?@action=redirect&bpo=25658).)

The new [context variables](#whatsnew37-pep567) functionality
exposes a number of [new C APIs](../c-api/contextvars.html#contextvarsobjects).

The new [ PyImport_GetModule()](../c-api/import.html#c.PyImport_GetModule) function returns the previously
imported module with the given name.
(Contributed by Eric Snow in 

[bpo-28411](https://bugs.python.org/issue?@action=redirect&bpo=28411).)

The new [ Py_RETURN_RICHCOMPARE](../c-api/typeobj.html#c.Py_RETURN_RICHCOMPARE) macro eases writing rich
comparison functions.
(Contributed by Petr Victorin in 

[bpo-23699](https://bugs.python.org/issue?@action=redirect&bpo=23699).)

The new [ Py_UNREACHABLE](../c-api/intro.html#c.Py_UNREACHABLE) macro can be used to mark unreachable
code paths.
(Contributed by Barry Warsaw in 

[bpo-31338](https://bugs.python.org/issue?@action=redirect&bpo=31338).)

The [ tracemalloc](../library/tracemalloc.html#module-tracemalloc) now exposes a C API through the new

[and](../c-api/memory.html#c.PyTraceMalloc_Track)

`PyTraceMalloc_Track()`[functions. (Contributed by Victor Stinner in](../c-api/memory.html#c.PyTraceMalloc_Untrack)

`PyTraceMalloc_Untrack()`[bpo-30054](https://bugs.python.org/issue?@action=redirect&bpo=30054).)

The new [import__find__load__start](../howto/instrumentation.html#static-markers) and
[import__find__load__done](../howto/instrumentation.html#static-markers) static markers can be used
to trace module imports.
(Contributed by Christian Heimes in [bpo-31574](https://bugs.python.org/issue?@action=redirect&bpo=31574).)

The fields `name` and `doc` of structures
[ PyMemberDef](../c-api/structures.html#c.PyMemberDef), 

[,](../c-api/structures.html#c.PyGetSetDef)

`PyGetSetDef`[,](../c-api/tuple.html#c.PyStructSequence_Field)

`PyStructSequence_Field`[, and](../c-api/tuple.html#c.PyStructSequence_Desc)

`PyStructSequence_Desc``wrapperbase` are now of type `const char *` rather of
`char *`.  (Contributed by Serhiy Storchaka in [bpo-28761](https://bugs.python.org/issue?@action=redirect&bpo=28761).)

The result of [ PyUnicode_AsUTF8AndSize()](../c-api/unicode.html#c.PyUnicode_AsUTF8AndSize) and 

[is now of type](../c-api/unicode.html#c.PyUnicode_AsUTF8)

`PyUnicode_AsUTF8()``const char *` rather of `char *`. (Contributed by Serhiy
Storchaka in [bpo-28769](https://bugs.python.org/issue?@action=redirect&bpo=28769).)

The result of [ PyMapping_Keys()](../c-api/mapping.html#c.PyMapping_Keys), 

[and](../c-api/mapping.html#c.PyMapping_Values)

`PyMapping_Values()`[is now always a list, rather than a list or a tuple. (Contributed by Oren Milman in](../c-api/mapping.html#c.PyMapping_Items)

`PyMapping_Items()`[bpo-28280](https://bugs.python.org/issue?@action=redirect&bpo=28280).)

Added functions [ PySlice_Unpack()](../c-api/slice.html#c.PySlice_Unpack) and 

[. (Contributed by Serhiy Storchaka in](../c-api/slice.html#c.PySlice_AdjustIndices)

`PySlice_AdjustIndices()`[bpo-27867](https://bugs.python.org/issue?@action=redirect&bpo=27867).)

[ PyOS_AfterFork()](../c-api/sys.html#c.PyOS_AfterFork) is deprecated in favour of the new functions

[,](../c-api/sys.html#c.PyOS_BeforeFork)

`PyOS_BeforeFork()`[and](../c-api/sys.html#c.PyOS_AfterFork_Parent)

`PyOS_AfterFork_Parent()`[. (Contributed by Antoine Pitrou in](../c-api/sys.html#c.PyOS_AfterFork_Child)

`PyOS_AfterFork_Child()`[bpo-16500](https://bugs.python.org/issue?@action=redirect&bpo=16500).)

The `PyExc_RecursionErrorInst` singleton that was part of the public API
has been removed as its members being never cleared may cause a segfault
during finalization of the interpreter. Contributed by Xavier de Gaye in
[bpo-22898](https://bugs.python.org/issue?@action=redirect&bpo=22898) and [bpo-30697](https://bugs.python.org/issue?@action=redirect&bpo=30697).

Added C API support for timezones with timezone constructors
[ PyTimeZone_FromOffset()](../c-api/datetime.html#c.PyTimeZone_FromOffset) and 

[, and access to the UTC singleton with](../c-api/datetime.html#c.PyTimeZone_FromOffsetAndName)

`PyTimeZone_FromOffsetAndName()`[. Contributed by Paul Ganssle in](../c-api/datetime.html#c.PyDateTime_TimeZone_UTC)

`PyDateTime_TimeZone_UTC`[bpo-10381](https://bugs.python.org/issue?@action=redirect&bpo=10381).

The type of results of `PyThread_start_new_thread()` and
`PyThread_get_thread_ident()`, and the *id* parameter of
[ PyThreadState_SetAsyncExc()](../c-api/init.html#c.PyThreadState_SetAsyncExc) changed from long to
unsigned long.
(Contributed by Serhiy Storchaka in 

[bpo-6532](https://bugs.python.org/issue?@action=redirect&bpo=6532).)

[ PyUnicode_AsWideCharString()](../c-api/unicode.html#c.PyUnicode_AsWideCharString) now raises a 

[if the second argument is](../library/exceptions.html#ValueError)

`ValueError``NULL` and the wchar_t* string contains null
characters.  (Contributed by Serhiy Storchaka in [bpo-30708](https://bugs.python.org/issue?@action=redirect&bpo=30708).)

Changes to the startup sequence and the management of dynamic memory
allocators mean that the long documented requirement to call
[ Py_Initialize()](../c-api/init.html#c.Py_Initialize) before calling most C API functions is now
relied on more heavily, and failing to abide by it may lead to segfaults in
embedding applications. See the 

[Porting to Python 3.7](#porting-to-python-37)section in this document and the

[Before Python Initialization](../c-api/init.html#pre-init-safe)section in the C API documentation for more details.

The new [ PyInterpreterState_GetID()](../c-api/init.html#c.PyInterpreterState_GetID) returns the unique ID for a
given interpreter.
(Contributed by Eric Snow in 

[bpo-29102](https://bugs.python.org/issue?@action=redirect&bpo=29102).)

[ Py_DecodeLocale()](../c-api/sys.html#c.Py_DecodeLocale), 

[now use the UTF-8 encoding when the](../c-api/sys.html#c.Py_EncodeLocale)

`Py_EncodeLocale()`[UTF-8 mode](#whatsnew37-pep540)is enabled. (Contributed by Victor Stinner in

[bpo-29240](https://bugs.python.org/issue?@action=redirect&bpo=29240).)

[ PyUnicode_DecodeLocaleAndSize()](../c-api/unicode.html#c.PyUnicode_DecodeLocaleAndSize) and 

[now use the current locale encoding for](../c-api/unicode.html#c.PyUnicode_EncodeLocale)

`PyUnicode_EncodeLocale()``surrogateescape` error handler.
(Contributed by Victor Stinner in [bpo-29240](https://bugs.python.org/issue?@action=redirect&bpo=29240).)

The *start* and *end* parameters of [ PyUnicode_FindChar()](../c-api/unicode.html#c.PyUnicode_FindChar) are
now adjusted to behave like string slices.
(Contributed by Xiang Zhang in 

[bpo-28822](https://bugs.python.org/issue?@action=redirect&bpo=28822).)

## Build Changes[¶](#build-changes)

Support for building `--without-threads` has been removed.  The
[ threading](../library/threading.html#module-threading) module is now always available.
(Contributed by Antoine Pitrou in 

[bpo-31370](https://bugs.python.org/issue?@action=redirect&bpo=31370).).

A full copy of libffi is no longer bundled for use when building the
[ _ctypes](../library/ctypes.html#module-ctypes) module on non-OSX UNIX platforms.  An installed copy
of libffi is now required when building 

`_ctypes` on such platforms.
(Contributed by Zachary Ware in [bpo-27979](https://bugs.python.org/issue?@action=redirect&bpo=27979).)

The Windows build process no longer depends on Subversion to pull in external
sources, a Python script is used to download zipfiles from GitHub instead.
If Python 3.6 is not found on the system (via `py -3.6`), NuGet is used to
download a copy of 32-bit Python for this purpose.  (Contributed by Zachary
Ware in [bpo-30450](https://bugs.python.org/issue?@action=redirect&bpo=30450).)

The [ ssl](../library/ssl.html#module-ssl) module requires OpenSSL 1.0.2 or 1.1 compatible libssl.
OpenSSL 1.0.1 has reached end of lifetime on 2016-12-31 and is no longer
supported. LibreSSL is temporarily not supported as well. LibreSSL releases
up to version 2.6.4 are missing required OpenSSL 1.0.2 APIs.

## Optimizations[¶](#optimizations)

The overhead of calling many methods of various standard library classes
implemented in C has been significantly reduced by porting more code
to use the `METH_FASTCALL` convention.
(Contributed by Victor Stinner in [bpo-29300](https://bugs.python.org/issue?@action=redirect&bpo=29300), [bpo-29507](https://bugs.python.org/issue?@action=redirect&bpo=29507),
[bpo-29452](https://bugs.python.org/issue?@action=redirect&bpo=29452), and [bpo-29286](https://bugs.python.org/issue?@action=redirect&bpo=29286).)

Various optimizations have reduced Python startup time by 10% on Linux and
up to 30% on macOS.
(Contributed by Victor Stinner, INADA Naoki in [bpo-29585](https://bugs.python.org/issue?@action=redirect&bpo=29585), and
Ivan Levkivskyi in [bpo-31333](https://bugs.python.org/issue?@action=redirect&bpo=31333).)

Method calls are now up to 20% faster due to the bytecode changes which
avoid creating bound method instances.
(Contributed by Yury Selivanov and INADA Naoki in [bpo-26110](https://bugs.python.org/issue?@action=redirect&bpo=26110).)

The [ asyncio](../library/asyncio.html#module-asyncio) module received a number of notable optimizations for
commonly used functions:

- The - `asyncio.get_event_loop()`- [bpo-32296](https://bugs.python.org/issue?@action=redirect&bpo=32296).)
- `asyncio.Future`- [bpo-32348](https://bugs.python.org/issue?@action=redirect&bpo=32348).)
- `asyncio.gather()`- [bpo-32355](https://bugs.python.org/issue?@action=redirect&bpo=32355).)
- `asyncio.sleep()`- *delay*argument is zero or negative. (Contributed by Andrew Svetlov in- [bpo-32351](https://bugs.python.org/issue?@action=redirect&bpo=32351).)
- The performance overhead of asyncio debug mode has been reduced. (Contributed by Antoine Pitrou in - [bpo-31970](https://bugs.python.org/issue?@action=redirect&bpo=31970).)

As a result of [PEP 560 work](#whatsnew37-pep560), the import time
of [ typing](../library/typing.html#module-typing) has been reduced by a factor of 7, and many typing operations
are now faster.
(Contributed by Ivan Levkivskyi in 

[bpo-32226](https://bugs.python.org/issue?@action=redirect&bpo=32226).)

[ sorted()](../library/functions.html#sorted) and 

[have been optimized for common cases to be up to 40-75% faster. (Contributed by Elliot Gorokhovsky in](../library/stdtypes.html#list.sort)

`list.sort()`[bpo-28685](https://bugs.python.org/issue?@action=redirect&bpo=28685).)

[ dict.copy()](../library/stdtypes.html#dict.copy) is now up to 5.5 times faster.
(Contributed by Yury Selivanov in 

[bpo-31179](https://bugs.python.org/issue?@action=redirect&bpo=31179).)

[ hasattr()](../library/functions.html#hasattr) and 

[are now about 4 times faster when](../library/functions.html#getattr)

`getattr()`*name*is not found and

*obj*does not override

[or](../reference/datamodel.html#object.__getattr__)

`object.__getattr__()`[. (Contributed by INADA Naoki in](../reference/datamodel.html#object.__getattribute__)

`object.__getattribute__()`[bpo-32544](https://bugs.python.org/issue?@action=redirect&bpo=32544).)

Searching for certain Unicode characters (like Ukrainian capital “Є”)
in a string was up to 25 times slower than searching for other characters.
It is now only 3 times slower in the worst case.
(Contributed by Serhiy Storchaka in [bpo-24821](https://bugs.python.org/issue?@action=redirect&bpo=24821).)

The [ collections.namedtuple()](../library/collections.html#collections.namedtuple) factory has been reimplemented to
make the creation of named tuples 4 to 6 times faster.
(Contributed by Jelle Zijlstra with further improvements by INADA Naoki,
Serhiy Storchaka, and Raymond Hettinger in 

[bpo-28638](https://bugs.python.org/issue?@action=redirect&bpo=28638).)

[ datetime.date.fromordinal()](../library/datetime.html#datetime.date.fromordinal) and 

[are now up to 30% faster in the common case. (Contributed by Paul Ganssle in](../library/datetime.html#datetime.date.fromtimestamp)

`datetime.date.fromtimestamp()`[bpo-32403](https://bugs.python.org/issue?@action=redirect&bpo=32403).)

The [ os.fwalk()](../library/os.html#os.fwalk) function is now up to 2 times faster thanks to
the use of 

[. (Contributed by Serhiy Storchaka in](../library/os.html#os.scandir)

`os.scandir()`[bpo-25996](https://bugs.python.org/issue?@action=redirect&bpo=25996).)

The speed of the [ shutil.rmtree()](../library/shutil.html#shutil.rmtree) function has been improved by
20–40% thanks to the use of the 

[function. (Contributed by Serhiy Storchaka in](../library/os.html#os.scandir)

`os.scandir()`[bpo-28564](https://bugs.python.org/issue?@action=redirect&bpo=28564).)

Optimized case-insensitive matching and searching of [ regular
expressions](../library/re.html#module-re).  Searching some patterns can now be up to 20 times faster.
(Contributed by Serhiy Storchaka in 

[bpo-30285](https://bugs.python.org/issue?@action=redirect&bpo=30285).)

[ re.compile()](../library/re.html#re.compile) now converts 

`flags` parameter to int object if
it is `RegexFlag`.  It is now as fast as Python 3.5, and faster than
Python 3.6 by about 10% depending on the pattern.
(Contributed by INADA Naoki in [bpo-31671](https://bugs.python.org/issue?@action=redirect&bpo=31671).)

The [ modify()](../library/selectors.html#selectors.BaseSelector.modify) methods of classes

[,](../library/selectors.html#selectors.EpollSelector)

`selectors.EpollSelector`[and](../library/selectors.html#selectors.PollSelector)

`selectors.PollSelector`[may be around 10% faster under heavy loads. (Contributed by Giampaolo Rodola’ in](../library/selectors.html#selectors.DevpollSelector)

`selectors.DevpollSelector`[bpo-30014](https://bugs.python.org/issue?@action=redirect&bpo=30014))

Constant folding has been moved from the peephole optimizer to the new AST
optimizer, which is able perform optimizations more consistently.
(Contributed by Eugene Toder and INADA Naoki in [bpo-29469](https://bugs.python.org/issue?@action=redirect&bpo=29469) and
[bpo-11549](https://bugs.python.org/issue?@action=redirect&bpo=11549).)

Most functions and methods in [ abc](../library/abc.html#module-abc) have been rewritten in C.
This makes creation of abstract base classes, and calling 

[and](../library/functions.html#isinstance)

`isinstance()`[on them 1.5x faster. This also reduces Python start-up time by up to 10%. (Contributed by Ivan Levkivskyi and INADA Naoki in](../library/functions.html#issubclass)

`issubclass()`[bpo-31333](https://bugs.python.org/issue?@action=redirect&bpo=31333))

Significant speed improvements to alternate constructors for
[ datetime.date](../library/datetime.html#datetime.date) and 

[by using fast-path constructors when not constructing subclasses. (Contributed by Paul Ganssle in](../library/datetime.html#datetime.datetime)

`datetime.datetime`[bpo-32403](https://bugs.python.org/issue?@action=redirect&bpo=32403))

The speed of comparison of [ array.array](../library/array.html#array.array) instances has been
improved considerably in certain cases.  It is now from 10x to 70x faster
when comparing arrays holding values of the same integer type.
(Contributed by Adrian Wielgosik in 

[bpo-24700](https://bugs.python.org/issue?@action=redirect&bpo=24700).)

The [ math.erf()](../library/math.html#math.erf) and 

[functions now use the (faster) C library implementation on most platforms. (Contributed by Serhiy Storchaka in](../library/math.html#math.erfc)

`math.erfc()`[bpo-26121](https://bugs.python.org/issue?@action=redirect&bpo=26121).)

## Other CPython Implementation Changes[¶](#other-cpython-implementation-changes)

- Trace hooks may now opt out of receiving the - `line`and opt into receiving the- `opcode`events from the interpreter by setting the corresponding new- `f_trace_lines`- `f_trace_opcodes`- [bpo-31344](https://bugs.python.org/issue?@action=redirect&bpo=31344).)
- Fixed some consistency problems with namespace package module attributes. Namespace module objects now have an - `__file__`that is set to- `None`(previously unset), and their- `__spec__.origin`is also set to- `None`(previously the string- `"namespace"`). See- [bpo-32305](https://bugs.python.org/issue?@action=redirect&bpo=32305). Also, the namespace module object’s- `__spec__.loader`is set to the same value as- `__loader__`(previously, the former was set to- `None`). See- [bpo-32303](https://bugs.python.org/issue?@action=redirect&bpo=32303).
- The - `locals()`- [bpo-32690](https://bugs.python.org/issue?@action=redirect&bpo=32690).)
- The - `distutils`- `upload`command no longer tries to change CR end-of-line characters to CRLF. This fixes a corruption issue with sdists that ended with a byte equivalent to CR. (Contributed by Bo Bayles in- [bpo-32304](https://bugs.python.org/issue?@action=redirect&bpo=32304).)

## Deprecated Python Behavior[¶](#deprecated-python-behavior)

Yield expressions (both `yield` and `yield from` clauses) are now deprecated
in comprehensions and generator expressions (aside from the iterable expression
in the leftmost `for` clause). This ensures that comprehensions
always immediately return a container of the appropriate type (rather than
potentially returning a [generator iterator](../glossary.html#term-generator-iterator) object), while generator
expressions won’t attempt to interleave their implicit output with the output
from any explicit yield expressions.  In Python 3.7, such expressions emit
[ DeprecationWarning](../library/exceptions.html#DeprecationWarning) when compiled, in Python 3.8 this will be a

[. (Contributed by Serhiy Storchaka in](../library/exceptions.html#SyntaxError)

`SyntaxError`[bpo-10544](https://bugs.python.org/issue?@action=redirect&bpo=10544).)

Returning a subclass of [ complex](../library/functions.html#complex) from 

[is deprecated and will be an error in future Python versions. This makes](../reference/datamodel.html#object.__complex__)

`object.__complex__()``__complex__()` consistent with [and](../reference/datamodel.html#object.__int__)

`object.__int__()`[. (Contributed by Serhiy Storchaka in](../reference/datamodel.html#object.__float__)

`object.__float__()`[bpo-28894](https://bugs.python.org/issue?@action=redirect&bpo=28894).)

## Deprecated Python modules, functions and methods[¶](#deprecated-python-modules-functions-and-methods)

### aifc[¶](#aifc)

`aifc.openfp()` has been deprecated and will be removed in Python 3.9.
Use `aifc.open()` instead.
(Contributed by Brian Curtin in [bpo-31985](https://bugs.python.org/issue?@action=redirect&bpo=31985).)

### asyncio[¶](#whatsnew37-asyncio-deprecated)

Support for directly `await`-ing instances of [ asyncio.Lock](../library/asyncio-sync.html#asyncio.Lock) and
other asyncio synchronization primitives has been deprecated.  An
asynchronous context manager must be used in order to acquire and release
the synchronization resource.
(Contributed by Andrew Svetlov in 

[bpo-32253](https://bugs.python.org/issue?@action=redirect&bpo=32253).)

The `asyncio.Task.current_task()` and `asyncio.Task.all_tasks()`
methods have been deprecated.
(Contributed by Andrew Svetlov in [bpo-32250](https://bugs.python.org/issue?@action=redirect&bpo=32250).)

### collections[¶](#id3)

In Python 3.8, the abstract base classes in [ collections.abc](../library/collections.abc.html#module-collections.abc) will no
longer be exposed in the regular 

[module. This will help create a clearer distinction between the concrete classes and the abstract base classes. (Contributed by Serhiy Storchaka in](../library/collections.html#module-collections)

`collections`[bpo-25988](https://bugs.python.org/issue?@action=redirect&bpo=25988).)

### dbm[¶](#id4)

[ dbm.dumb](../library/dbm.html#module-dbm.dumb) now supports reading read-only files and no longer writes the
index file when it is not changed.  A deprecation warning is now emitted
if the index file is missing and recreated in the 

`'r'` and `'w'`
modes (this will be an error in future Python releases).
(Contributed by Serhiy Storchaka in [bpo-28847](https://bugs.python.org/issue?@action=redirect&bpo=28847).)

### enum[¶](#id5)

In Python 3.8, attempting to check for non-Enum objects in [ Enum](../library/enum.html#enum.Enum)
classes will raise a 

[(e.g.](../library/exceptions.html#TypeError)

`TypeError``1 in Color`); similarly,
attempting to check for non-Flag objects in a [member will raise](../library/enum.html#enum.Flag)

`Flag``TypeError` (e.g. `1 in Perm.RW`); currently, both operations
return [instead. (Contributed by Ethan Furman in](../library/constants.html#False)

`False`[bpo-33217](https://bugs.python.org/issue?@action=redirect&bpo=33217).)

### gettext[¶](#gettext)

Using non-integer value for selecting a plural form in [ gettext](../library/gettext.html#module-gettext) is
now deprecated.  It never correctly worked. (Contributed by Serhiy Storchaka
in 

[bpo-28692](https://bugs.python.org/issue?@action=redirect&bpo=28692).)

### importlib[¶](#id6)

Methods
`MetaPathFinder.find_module()`
(replaced by
[ MetaPathFinder.find_spec()](../library/importlib.html#importlib.abc.MetaPathFinder.find_spec))
and

`PathEntryFinder.find_loader()`
(replaced by
[) both deprecated in Python 3.4 now emit](../library/importlib.html#importlib.abc.PathEntryFinder.find_spec)

`PathEntryFinder.find_spec()`[. (Contributed by Matthias Bussonnier in](../library/exceptions.html#DeprecationWarning)

`DeprecationWarning`[bpo-29576](https://bugs.python.org/issue?@action=redirect&bpo=29576).)

The [ importlib.abc.ResourceLoader](../library/importlib.html#importlib.abc.ResourceLoader) ABC has been deprecated in
favour of 

[.](../library/importlib.html#importlib.abc.ResourceReader)

`importlib.abc.ResourceReader`### locale[¶](#id7)

`locale.format()` has been deprecated, use [ locale.format_string()](../library/locale.html#locale.format_string)
instead.  (Contributed by Garvit in 

[bpo-10379](https://bugs.python.org/issue?@action=redirect&bpo=10379).)

### macpath[¶](#macpath)

The `macpath` is now deprecated and will be removed in Python 3.8.
(Contributed by Chi Hsuan Yen in [bpo-9850](https://bugs.python.org/issue?@action=redirect&bpo=9850).)

### threading[¶](#threading)

`dummy_threading` and `_dummy_thread` have been deprecated.  It is
no longer possible to build Python with threading disabled.
Use [ threading](../library/threading.html#module-threading) instead.
(Contributed by Antoine Pitrou in 

[bpo-31370](https://bugs.python.org/issue?@action=redirect&bpo=31370).)

### socket[¶](#id8)

The silent argument value truncation in [ socket.htons()](../library/socket.html#socket.htons) and

[has been deprecated. In future versions of Python, if the passed argument is larger than 16 bits, an exception will be raised. (Contributed by Oren Milman in](../library/socket.html#socket.ntohs)

`socket.ntohs()`[bpo-28332](https://bugs.python.org/issue?@action=redirect&bpo=28332).)

### ssl[¶](#id9)

`ssl.wrap_socket()` is deprecated.  Use
[ ssl.SSLContext.wrap_socket()](../library/ssl.html#ssl.SSLContext.wrap_socket) instead.
(Contributed by Christian Heimes in 

[bpo-28124](https://bugs.python.org/issue?@action=redirect&bpo=28124).)

### sunau[¶](#sunau)

`sunau.openfp()` has been deprecated and will be removed in Python 3.9.
Use `sunau.open()` instead.
(Contributed by Brian Curtin in [bpo-31985](https://bugs.python.org/issue?@action=redirect&bpo=31985).)

### sys[¶](#id10)

Deprecated `sys.set_coroutine_wrapper()` and
`sys.get_coroutine_wrapper()`.

The undocumented `sys.callstats()` function has been deprecated and
will be removed in a future Python version.
(Contributed by Victor Stinner in [bpo-28799](https://bugs.python.org/issue?@action=redirect&bpo=28799).)

### wave[¶](#wave)

`wave.openfp()` has been deprecated and will be removed in Python 3.9.
Use [ wave.open()](../library/wave.html#wave.open) instead.
(Contributed by Brian Curtin in 

[bpo-31985](https://bugs.python.org/issue?@action=redirect&bpo=31985).)

## Deprecated functions and types of the C API[¶](#deprecated-functions-and-types-of-the-c-api)

Function [ PySlice_GetIndicesEx()](../c-api/slice.html#c.PySlice_GetIndicesEx) is deprecated and replaced with
a macro if 

`Py_LIMITED_API` is not set or set to a value in the range
between `0x03050400` and `0x03060000` (not inclusive), or is `0x03060100`
or higher.  (Contributed by Serhiy Storchaka in [bpo-27867](https://bugs.python.org/issue?@action=redirect&bpo=27867).)

[ PyOS_AfterFork()](../c-api/sys.html#c.PyOS_AfterFork) has been deprecated.  Use 

[,](../c-api/sys.html#c.PyOS_BeforeFork)

`PyOS_BeforeFork()`[or](../c-api/sys.html#c.PyOS_AfterFork_Parent)

`PyOS_AfterFork_Parent()`[instead. (Contributed by Antoine Pitrou in](../c-api/sys.html#c.PyOS_AfterFork_Child)

`PyOS_AfterFork_Child()`[bpo-16500](https://bugs.python.org/issue?@action=redirect&bpo=16500).)

## Platform Support Removals[¶](#platform-support-removals)

- FreeBSD 9 and older are no longer officially supported. 
- For full Unicode support, including within extension modules, *nix platforms are now expected to provide at least one of - `C.UTF-8`(full locale),- `C.utf8`(full locale) or- `UTF-8`(- `LC_CTYPE`-only locale) as an alternative to the legacy- `ASCII`-based- `C`locale.
- OpenSSL 0.9.8 and 1.0.1 are no longer supported, which means building CPython 3.7 with SSL/TLS support on older platforms still using these versions requires custom build options that link to a more recent version of OpenSSL. - Notably, this issue affects the Debian 8 (aka “jessie”) and Ubuntu 14.04 (aka “Trusty”) LTS Linux distributions, as they still use OpenSSL 1.0.1 by default. - Debian 9 (“stretch”) and Ubuntu 16.04 (“xenial”), as well as recent releases of other LTS Linux releases (e.g. RHEL/CentOS 7.5, SLES 12-SP3), use OpenSSL 1.0.2 or later, and remain supported in the default build configuration. - CPython’s own - [CI configuration file](https://github.com/python/cpython/blob/v3.7.13/.travis.yml)provides an example of using the SSL- [compatibility testing infrastructure](https://github.com/python/cpython/tree/3.13/Tools/ssl/multissltests.py)in CPython’s test suite to build and link against OpenSSL 1.1.0 rather than an outdated system provided OpenSSL.

## API and Feature Removals[¶](#api-and-feature-removals)

The following features and APIs have been removed from Python 3.7:

- The - `os.stat_float_times()`function has been removed. It was introduced in Python 2.3 for backward compatibility with Python 2.2, and was deprecated since Python 3.1.
- Unknown escapes consisting of - `'\'`and an ASCII letter in replacement templates for- `re.sub()`
- Removed support of the - *exclude*argument in- `tarfile.TarFile.add()`- *filter*argument instead.
- The - `ntpath.splitunc()`function was deprecated in Python 3.1, and has now been removed. Use- `splitdrive()`
- `collections.namedtuple()`- *verbose*parameter or- `_source`attribute which showed the generated source code for the named tuple class. This was part of an optimization designed to speed-up class creation. (Contributed by Jelle Zijlstra with further improvements by INADA Naoki, Serhiy Storchaka, and Raymond Hettinger in- [bpo-28638](https://bugs.python.org/issue?@action=redirect&bpo=28638).)
- Functions - `bool()`- `float()`- `list()`- `tuple()`- `int()`
- Removed previously deprecated in Python 2.4 classes - `Plist`,- `Dict`and- `_InternalDict`in the- `plistlib`- `readPlist()`and- `readPlistFromBytes()`are now normal dicts. You no longer can use attribute access to access items of these dictionaries.
- The - `asyncio.windows_utils.socketpair()`function has been removed. Use the- `socket.socketpair()`- `asyncio.windows_utils.socketpair`was just an alias to- `socket.socketpair`on Python 3.5 and newer.
- `asyncio`- `selectors`- `_overlapped`modules as- `asyncio.selectors`and- `asyncio._overlapped`. Replace- `from asyncio import selectors`with- `import selectors`.
- Direct instantiation of - `ssl.SSLSocket`- `ssl.SSLObject`- `ssl.wrap_socket()`or- `ssl.SSLContext`- [bpo-32951](https://bugs.python.org/issue?@action=redirect&bpo=32951).)
- The unused - `distutils`- `install_misc`command has been removed. (Contributed by Eric N. Vander Weele in- [bpo-29218](https://bugs.python.org/issue?@action=redirect&bpo=29218).)

## Module Removals[¶](#module-removals)

The `fpectl` module has been removed.  It was never enabled by
default, never worked correctly on x86-64, and it changed the Python
ABI in ways that caused unexpected breakage of C extensions.
(Contributed by Nathaniel J. Smith in [bpo-29137](https://bugs.python.org/issue?@action=redirect&bpo=29137).)

## Windows-only Changes[¶](#windows-only-changes)

The python launcher, (py.exe), can accept 32 & 64 bit specifiers **without**
having to specify a minor version as well. So `py -3-32` and `py -3-64`
become valid as well as `py -3.7-32`, also the -*m*-64 and -*m.n*-64 forms
are now accepted to force 64 bit python even if 32 bit would have otherwise
been used. If the specified version is not available py.exe will error exit.
(Contributed by Steve Barnes in [bpo-30291](https://bugs.python.org/issue?@action=redirect&bpo=30291).)

The launcher can be run as `py -0` to produce a list of the installed pythons,
*with default marked with an asterisk*. Running `py -0p` will include the paths.
If py is run with a version specifier that cannot be matched it will also print
the *short form* list of available specifiers.
(Contributed by Steve Barnes in [bpo-30362](https://bugs.python.org/issue?@action=redirect&bpo=30362).)

## Porting to Python 3.7[¶](#porting-to-python-3-7)

This section lists previously described changes and other bugfixes that may require changes to your code.

### Changes in Python Behavior[¶](#changes-in-python-behavior)

- `async`- `await`- `SyntaxError`- [bpo-30406](https://bugs.python.org/issue?@action=redirect&bpo=30406).)
- **PEP 479**- `StopIteration`- `RuntimeError`- [bpo-32670](https://bugs.python.org/issue?@action=redirect&bpo=32670).)
- `object.__aiter__()`- [bpo-31709](https://bugs.python.org/issue?@action=redirect&bpo=31709).)
- Due to an oversight, earlier Python versions erroneously accepted the following syntax: - f(1 for x in [1],) class C(1 for x in [1]): pass - Python 3.7 now correctly raises a - `SyntaxError`- [bpo-32012](https://bugs.python.org/issue?@action=redirect&bpo=32012)and- [bpo-32023](https://bugs.python.org/issue?@action=redirect&bpo=32023).)
- When using the - `-m`- `sys.path`- `os.getcwd()`or- `os.path.dirname(__main__.__file__)`, depending on why the code was checking for the empty string in the first place).

### Changes in the Python API[¶](#changes-in-the-python-api)

- `socketserver.ThreadingMixIn.server_close`- `socketserver.ThreadingMixIn.block_on_close`- `False`to get the pre-3.7 behaviour. (Contributed by Victor Stinner in- [bpo-31233](https://bugs.python.org/issue?@action=redirect&bpo=31233)and- [bpo-33540](https://bugs.python.org/issue?@action=redirect&bpo=33540).)
- `socketserver.ForkingMixIn.server_close`- `socketserver.ForkingMixIn.block_on_close`- `False`to get the pre-3.7 behaviour. (Contributed by Victor Stinner in- [bpo-31151](https://bugs.python.org/issue?@action=redirect&bpo=31151)and- [bpo-33540](https://bugs.python.org/issue?@action=redirect&bpo=33540).)
- The - `locale.localeconv()`- `LC_CTYPE`locale to the value of- `LC_NUMERIC`in some cases. (Contributed by Victor Stinner in- [bpo-31900](https://bugs.python.org/issue?@action=redirect&bpo=31900).)
- `pkgutil.walk_packages()`- `ValueError`- *path*is a string. Previously an empty list was returned. (Contributed by Sanyam Khurana in- [bpo-24744](https://bugs.python.org/issue?@action=redirect&bpo=24744).)
- A format string argument for - `string.Formatter.format()`- [positional-only](../glossary.html#positional-only-parameter). Passing it as a keyword argument was deprecated in Python 3.5. (Contributed by Serhiy Storchaka in- [bpo-29193](https://bugs.python.org/issue?@action=redirect&bpo=29193).)
- Attributes - `key`- `value`- `coded_value`- `http.cookies.Morsel`- `set()`- [bpo-29192](https://bugs.python.org/issue?@action=redirect&bpo=29192).)
- The - *mode*argument of- `os.makedirs()`- `makedirs()`. (Contributed by Serhiy Storchaka in- [bpo-19930](https://bugs.python.org/issue?@action=redirect&bpo=19930).)
- The - `struct.Struct.format`- `str`- `bytes`- [bpo-21071](https://bugs.python.org/issue?@action=redirect&bpo=21071).)
- `cgi.parse_multipart()`now accepts the- *encoding*and- *errors*arguments and returns the same results as- `FieldStorage`: for non-file fields, the value associated to a key is a list of strings, not bytes. (Contributed by Pierre Quentel in- [bpo-29979](https://bugs.python.org/issue?@action=redirect&bpo=29979).)
- Due to internal changes in - `socket`- `socket.fromshare()`- `socket.share`
- `repr`for- `BaseException`- [bpo-30399](https://bugs.python.org/issue?@action=redirect&bpo=30399).)
- `repr`for- `datetime.timedelta`- [bpo-30302](https://bugs.python.org/issue?@action=redirect&bpo=30302).)
- Because - `shutil.rmtree()`- `os.scandir()`- *onerror*is now called with the first argument- `os.scandir`instead of- `os.listdir`when listing the directory is failed.
- Support for nested sets and set operations in regular expressions as in - [Unicode Technical Standard #18](https://unicode.org/reports/tr18/)might be added in the future. This would change the syntax. To facilitate this future change a- `FutureWarning`- `'['`or containing literal character sequences- `'--'`,- `'&&'`,- `'~~'`, and- `'||'`. To avoid a warning, escape them with a backslash. (Contributed by Serhiy Storchaka in- [bpo-30349](https://bugs.python.org/issue?@action=redirect&bpo=30349).)
- The result of splitting a string on a - `regular expression`- `r'\s*'`will now split not only on whitespaces as it did previously, but also on empty strings before all non-whitespace characters and just before the end of the string. The previous behavior can be restored by changing the pattern to- `r'\s+'`. A- `FutureWarning`- For patterns that match both empty and non-empty strings, the result of searching for all matches may also be changed in other cases. For example in the string - `'a\n\n'`, the pattern- `r'(?m)^\s*?$'`will not only match empty strings at positions 2 and 3, but also the string- `'\n'`at positions 2–3. To match only blank lines, the pattern should be rewritten as- `r'(?m)^[^\S\n]*$'`.- `re.sub()`- `re.sub('x*', '-', 'abxd')`returns now- `'-a-b--d-'`instead of- `'-a-b-d-'`(the first minus between ‘b’ and ‘d’ replaces ‘x’, and the second minus replaces an empty string between ‘x’ and ‘d’).- (Contributed by Serhiy Storchaka in - [bpo-25054](https://bugs.python.org/issue?@action=redirect&bpo=25054)and- [bpo-32308](https://bugs.python.org/issue?@action=redirect&bpo=32308).)
- Change - `re.escape()`- `'_'`. (Contributed by Serhiy Storchaka in- [bpo-29995](https://bugs.python.org/issue?@action=redirect&bpo=29995).)
- `tracemalloc.Traceback`- `traceback`- [bpo-32121](https://bugs.python.org/issue?@action=redirect&bpo=32121).)
- On OSes that support - `socket.SOCK_NONBLOCK`- `socket.SOCK_CLOEXEC`- `socket.type`- `if sock.type == socket.SOCK_STREAM`work as expected on all platforms. (Contributed by Yury Selivanov in- [bpo-32331](https://bugs.python.org/issue?@action=redirect&bpo=32331).)
- On Windows the default for the - *close_fds*argument of- `subprocess.Popen`- `False`- `True`- `subprocess.Popen`with standard io redirection, you will have to pass- `close_fds=False`to preserve the previous behaviour, or use- `STARTUPINFO.lpAttributeList`
- `importlib.machinery.PathFinder.invalidate_caches()`- `importlib.invalidate_caches()`- `sys.path_importer_cache`- `None`. (Contributed by Brett Cannon in- [bpo-33169](https://bugs.python.org/issue?@action=redirect&bpo=33169).)
- In - `asyncio`- `loop.sock_recv()`- `loop.sock_sendall()`- `loop.sock_accept()`- `loop.getaddrinfo()`- `loop.getnameinfo()`- `asyncio.Future`- [bpo-32327](https://bugs.python.org/issue?@action=redirect&bpo=32327).)
- `asyncio.Server.sockets`- [bpo-32662](https://bugs.python.org/issue?@action=redirect&bpo=32662).)
- `Struct.format`- `str`- `bytes`- [bpo-21071](https://bugs.python.org/issue?@action=redirect&bpo=21071).)
- `argparse`- `required=True`to- `ArgumentParser.add_subparsers()`- [bpo-26510](https://bugs.python.org/issue?@action=redirect&bpo=26510).)
- `ast.literal_eval()`- [bpo-31778](https://bugs.python.org/issue?@action=redirect&bpo=31778).)
- `Calendar.itermonthdates`- `0001-01-01`through- `9999-12-31`range. To support applications that cannot tolerate such exceptions, the new- `Calendar.itermonthdays3`- `Calendar.itermonthdays4`- `datetime.date`- [bpo-28292](https://bugs.python.org/issue?@action=redirect&bpo=28292).)
- `collections.ChainMap`- [bpo-32792](https://bugs.python.org/issue?@action=redirect&bpo=32792).)
- The - `submit()`method of- `concurrent.futures.ThreadPoolExecutor`- `concurrent.futures.ProcessPoolExecutor`- `RuntimeError`- [bpo-33097](https://bugs.python.org/issue?@action=redirect&bpo=33097).)
- The - `configparser.ConfigParser`- `read_dict()`to process the default values, making its behavior consistent with the rest of the parser. Non-string keys and values in the defaults dictionary are now being implicitly converted to strings. (Contributed by James Tocknell in- [bpo-23835](https://bugs.python.org/issue?@action=redirect&bpo=23835).)
- Several undocumented internal imports were removed. One example is that - `os.errno`is no longer available; use- `import errno`directly instead. Note that such undocumented internal imports may be removed any time without notice, even in micro version releases.

### Changes in the C API[¶](#changes-in-the-c-api)

The function [ PySlice_GetIndicesEx()](../c-api/slice.html#c.PySlice_GetIndicesEx) is considered unsafe for
resizable sequences.  If the slice indices are not instances of 

[, but objects that implement the](../library/functions.html#int)

`int``__index__()` method, the sequence can be
resized after passing its length to `PySlice_GetIndicesEx()`.  This
can lead to returning indices out of the length of the sequence.  For
avoiding possible problems use new functions [and](../c-api/slice.html#c.PySlice_Unpack)

`PySlice_Unpack()`[. (Contributed by Serhiy Storchaka in](../c-api/slice.html#c.PySlice_AdjustIndices)

`PySlice_AdjustIndices()`[bpo-27867](https://bugs.python.org/issue?@action=redirect&bpo=27867).)

### CPython bytecode changes[¶](#cpython-bytecode-changes)

There are two new opcodes: [ LOAD_METHOD](../library/dis.html#opcode-LOAD_METHOD) and 

`CALL_METHOD`.
(Contributed by Yury Selivanov and INADA Naoki in [bpo-26110](https://bugs.python.org/issue?@action=redirect&bpo=26110).)

The `STORE_ANNOTATION` opcode has been removed.
(Contributed by Mark Shannon in [bpo-32550](https://bugs.python.org/issue?@action=redirect&bpo=32550).)

### Windows-only Changes[¶](#id12)

The file used to override [ sys.path](../library/sys.html#sys.path) is now called

`<python-executable>._pth` instead of `'sys.path'`.
See [Finding modules](../using/windows.html#windows-finding-modules)for more information. (Contributed by Steve Dower in

[bpo-28137](https://bugs.python.org/issue?@action=redirect&bpo=28137).)

### Other CPython implementation changes[¶](#id13)

In preparation for potential future changes to the public CPython runtime
initialization API (see [ PEP 432](https://peps.python.org/pep-0432/) for an initial, but somewhat outdated,
draft), CPython’s internal startup
and configuration management logic has been significantly refactored. While
these updates are intended to be entirely transparent to both embedding
applications and users of the regular CPython CLI, they’re being mentioned
here as the refactoring changes the internal order of various operations
during interpreter startup, and hence may uncover previously latent defects,
either in embedding applications, or in CPython itself.
(Initially contributed by Nick Coghlan and Eric Snow as part of

[bpo-22257](https://bugs.python.org/issue?@action=redirect&bpo=22257), and further updated by Nick, Eric, and Victor Stinner in a number of other issues). Some known details affected:

- `PySys_AddWarnOptionUnicode()`is not currently usable by embedding applications due to the requirement to create a Unicode object prior to calling- `Py_Initialize`. Use- `PySys_AddWarnOption()`instead.
- warnings filters added by an embedding application with - `PySys_AddWarnOption()`should now more consistently take precedence over the default filters set by the interpreter

Due to changes in the way the default warnings filters are configured,
setting [ Py_BytesWarningFlag](../c-api/init.html#c.Py_BytesWarningFlag) to a value greater than one is no longer
sufficient to both emit 

[messages and have them converted to exceptions. Instead, the flag must be set (to cause the warnings to be emitted in the first place), and an explicit](../library/exceptions.html#BytesWarning)

`BytesWarning``error::BytesWarning`
warnings filter added to convert them to exceptions.Due to a change in the way docstrings are handled by the compiler, the
implicit `return None` in a function body consisting solely of a docstring
is now marked as occurring on the same line as the docstring, not on the
function’s header line.

The current exception state has been moved from the frame object to the co-routine.
This simplified the interpreter and fixed a couple of obscure bugs caused by
having swap exception state when entering or exiting a generator.
(Contributed by Mark Shannon in [bpo-25612](https://bugs.python.org/issue?@action=redirect&bpo=25612).)

## Notable changes in Python 3.7.1[¶](#notable-changes-in-python-3-7-1)

Starting in 3.7.1, [ Py_Initialize()](../c-api/init.html#c.Py_Initialize) now consistently reads and respects
all of the same environment settings as 

[(in earlier Python versions, it respected an ill-defined subset of those environment variables, while in Python 3.7.0 it didn’t read any of them due to](../c-api/init.html#c.Py_Main)

`Py_Main()`[bpo-34247](https://bugs.python.org/issue?@action=redirect&bpo=34247)). If this behavior is unwanted, set

[to 1 before calling](../c-api/init.html#c.Py_IgnoreEnvironmentFlag)

`Py_IgnoreEnvironmentFlag``Py_Initialize()`.In 3.7.1 the C API for Context Variables
[was updated](../c-api/contextvars.html#contextvarsobjects-pointertype-change) to use
[ PyObject](../c-api/structures.html#c.PyObject) pointers.  See also 

[bpo-34762](https://bugs.python.org/issue?@action=redirect&bpo=34762).

In 3.7.1 the [ tokenize](../library/tokenize.html#module-tokenize) module now implicitly emits a 

`NEWLINE` token
when provided with input that does not have a trailing new line.  This behavior
now matches what the C tokenizer does internally.
(Contributed by Ammar Askar in [bpo-33899](https://bugs.python.org/issue?@action=redirect&bpo=33899).)

## Notable changes in Python 3.7.2[¶](#notable-changes-in-python-3-7-2)

In 3.7.2, [ venv](../library/venv.html#module-venv) on Windows no longer copies the original binaries, but
creates redirector scripts named 

`python.exe` and `pythonw.exe` instead.
This resolves a long standing issue where all virtual environments would have
to be upgraded or recreated with each Python update. However, note that this
release will still require recreation of virtual environments in order to get
the new scripts.## Notable changes in Python 3.7.6[¶](#notable-changes-in-python-3-7-6)

Due to significant security concerns, the *reuse_address* parameter of
[ asyncio.loop.create_datagram_endpoint()](../library/asyncio-eventloop.html#asyncio.loop.create_datagram_endpoint) is no longer supported. This is
because of the behavior of the socket option 

`SO_REUSEADDR` in UDP. For more
details, see the documentation for `loop.create_datagram_endpoint()`.
(Contributed by Kyle Stanley, Antoine Pitrou, and Yury Selivanov in
[bpo-37228](https://bugs.python.org/issue?@action=redirect&bpo=37228).)

## Notable changes in Python 3.7.10[¶](#notable-changes-in-python-3-7-10)

Earlier Python versions allowed using both `;` and `&` as
query parameter separators in [ urllib.parse.parse_qs()](../library/urllib.parse.html#urllib.parse.parse_qs) and

[. Due to security concerns, and to conform with newer W3C recommendations, this has been changed to allow only a single separator key, with](../library/urllib.parse.html#urllib.parse.parse_qsl)

`urllib.parse.parse_qsl()``&` as the default.  This change also affects
`cgi.parse()` and `cgi.parse_multipart()` as they use the affected
functions internally. For more details, please see their respective
documentation.
(Contributed by Adam Goldschmidt, Senthil Kumaran and Ken Jin in [bpo-42967](https://bugs.python.org/issue?@action=redirect&bpo=42967).)

## Notable changes in Python 3.7.11[¶](#notable-changes-in-python-3-7-11)

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

## Notable security feature in 3.7.14[¶](#notable-security-feature-in-3-7-14)

Converting between [ int](../library/functions.html#int) and 

[in bases other than 2 (binary), 4, 8 (octal), 16 (hexadecimal), or 32 such as base 10 (decimal) now raises a](../library/stdtypes.html#str)

`str`[if the number of digits in string form is above a limit to avoid potential denial of service attacks due to the algorithmic complexity. This is a mitigation for](../library/exceptions.html#ValueError)

`ValueError`[. This limit can be configured or disabled by environment variable, command line flag, or](https://www.cve.org/CVERecord?id=CVE-2020-10735)

**CVE 2020-10735**[APIs. See the](../library/sys.html#module-sys)

`sys`[integer string conversion length limitation](../library/stdtypes.html#int-max-str-digits)documentation. The default limit is 4300 digits in string form.