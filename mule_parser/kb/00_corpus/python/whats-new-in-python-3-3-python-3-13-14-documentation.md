# What’s New In Python 3.3 — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/whatsnew/3.3.html](https://docs.python.org/3.13/whatsnew/3.3.html)

---

# What’s New In Python 3.3[¶](#what-s-new-in-python-3-3)

This article explains the new features in Python 3.3, compared to 3.2.
Python 3.3 was released on September 29, 2012.  For full details,
see the [changelog](https://docs.python.org/3.3/whatsnew/changelog.html).

See also

[ PEP 398](https://peps.python.org/pep-0398/) - Python 3.3 Release Schedule

## Summary – Release highlights[¶](#summary-release-highlights)

New syntax features:

- New - `yield from`expression for- [generator delegation](#pep-380).
- The - `u'unicode'`syntax is accepted again for- `str`

New library modules:

- `faulthandler`
- `ipaddress`
- `lzma`
- `unittest.mock`
- `venv`- [virtual environments](#pep-405), as in the popular- `virtualenv`package)

New built-in features:

- Reworked - [I/O exception hierarchy](#pep-3151).

Implementation improvements:

- Rewritten - [import machinery](#importlib)based on- `importlib`
- More compact - [unicode strings](#pep-393).
- More compact - [attribute dictionaries](#pep-412).

Significantly Improved Library Modules:

- C Accelerator for the - [decimal](#new-decimal)module.
- Better unicode handling in the - [email](#new-email)module (- [provisional](../glossary.html#term-provisional-package)).

Security improvements:

- Hash randomization is switched on by default. 

Please read on for a comprehensive list of user-facing changes.

## PEP 405: Virtual Environments[¶](#pep-405-virtual-environments)

Virtual environments help create separate Python setups while sharing a
system-wide base install, for ease of maintenance.  Virtual environments
have their own set of private site packages (i.e. locally installed
libraries), and are optionally segregated from the system-wide site
packages.  Their concept and implementation are inspired by the popular
`virtualenv` third-party package, but benefit from tighter integration
with the interpreter core.

This PEP adds the [ venv](../library/venv.html#module-venv) module for programmatic access, and the

`pyvenv` script for command-line access and
administration.  The Python interpreter checks for a `pyvenv.cfg`,
file whose existence signals the base of a virtual environment’s directory
tree.See also

- **PEP 405**
- PEP written by Carl Meyer; implementation by Carl Meyer and Vinay Sajip 

## PEP 420: Implicit Namespace Packages[¶](#pep-420-implicit-namespace-packages)

Native support for package directories that don’t require `__init__.py`
marker files and can automatically span multiple path segments (inspired by
various third party approaches to namespace packages, as described in
[ PEP 420](https://peps.python.org/pep-0420/))

See also

- **PEP 420**
- PEP written by Eric V. Smith; implementation by Eric V. Smith and Barry Warsaw 

## PEP 3118: New memoryview implementation and buffer protocol documentation[¶](#pep-3118-new-memoryview-implementation-and-buffer-protocol-documentation)

The implementation of [ PEP 3118](https://peps.python.org/pep-3118/) has been significantly improved.

The new memoryview implementation comprehensively fixes all ownership and lifetime issues of dynamically allocated fields in the Py_buffer struct that led to multiple crash reports. Additionally, several functions that crashed or returned incorrect results for non-contiguous or multi-dimensional input have been fixed.

The memoryview object now has a PEP-3118 compliant getbufferproc() that checks the consumer’s request type. Many new features have been added, most of them work in full generality for non-contiguous arrays and arrays with suboffsets.

The documentation has been updated, clearly spelling out responsibilities for both exporters and consumers. Buffer request flags are grouped into basic and compound flags. The memory layout of non-contiguous and multi-dimensional NumPy-style arrays is explained.

### Features[¶](#features)

- All native single character format specifiers in struct module syntax (optionally prefixed with ‘@’) are now supported. 
- With some restrictions, the cast() method allows changing of format and shape of C-contiguous arrays. 
- Multi-dimensional list representations are supported for any array type. 
- Multi-dimensional comparisons are supported for any array type. 
- One-dimensional memoryviews of hashable (read-only) types with formats B, b or c are now hashable. (Contributed by Antoine Pitrou in - [bpo-13411](https://bugs.python.org/issue?@action=redirect&bpo=13411).)
- Arbitrary slicing of any 1-D arrays type is supported. For example, it is now possible to reverse a memoryview in - *O*(1) by using a negative step.

### API changes[¶](#api-changes)

- The maximum number of dimensions is officially limited to 64. 
- The representation of empty shape, strides and suboffsets is now an empty tuple instead of - `None`.
- Accessing a memoryview element with format ‘B’ (unsigned bytes) now returns an integer (in accordance with the struct module syntax). For returning a bytes object the view must be cast to ‘c’ first. 
- memoryview comparisons now use the logical structure of the operands and compare all array elements by value. All format strings in struct module syntax are supported. Views with unrecognised format strings are still permitted, but will always compare as unequal, regardless of view contents. 
- For further changes see - [Build and C API Changes](#build-and-c-api-changes)and- [Porting C code](#porting-c-code).

(Contributed by Stefan Krah in [bpo-10181](https://bugs.python.org/issue?@action=redirect&bpo=10181).)

See also

[ PEP 3118](https://peps.python.org/pep-3118/) - Revising the Buffer Protocol

## PEP 393: Flexible String Representation[¶](#pep-393-flexible-string-representation)

The Unicode string type is changed to support multiple internal representations, depending on the character with the largest Unicode ordinal (1, 2, or 4 bytes) in the represented string. This allows a space-efficient representation in common cases, but gives access to full UCS-4 on all systems. For compatibility with existing APIs, several representations may exist in parallel; over time, this compatibility should be phased out.

On the Python side, there should be no downside to this change.

On the C API side, [ PEP 393](https://peps.python.org/pep-0393/) is fully backward compatible.  The legacy API
should remain available at least five years.  Applications using the legacy
API will not fully benefit of the memory reduction, or - worse - may use
a bit more memory, because Python may have to maintain two versions of each
string (in the legacy format and in the new efficient storage).

### Functionality[¶](#functionality)

Changes introduced by [ PEP 393](https://peps.python.org/pep-0393/) are the following:

- Python now always supports the full range of Unicode code points, including non-BMP ones (i.e. from - `U+0000`to- `U+10FFFF`). The distinction between narrow and wide builds no longer exists and Python now behaves like a wide build, even under Windows.
- With the death of narrow builds, the problems specific to narrow builds have also been fixed, for example: - `len()`- `len('\U0010FFFF') == 1`;
- surrogate pairs are not recombined in string literals, so - `'\uDBFF\uDFFF' != '\U0010FFFF'`;
- indexing or slicing non-BMP characters returns the expected value, so - `'\U0010FFFF'[0]`now returns- `'\U0010FFFF'`and not- `'\uDBFF'`;
- all other functions in the standard library now correctly handle non-BMP code points. 
 
- The value of - `sys.maxunicode`- `1114111`(- `0x10FFFF`in hexadecimal). The- `PyUnicode_GetMax()`function still returns either- `0xFFFF`or- `0x10FFFF`for backward compatibility, and it should not be used with the new Unicode API (see- [bpo-13054](https://bugs.python.org/issue?@action=redirect&bpo=13054)).
- The - `./configure`flag- `--with-wide-unicode`has been removed.

### Performance and resource usage[¶](#performance-and-resource-usage)

The storage of Unicode strings now depends on the highest code point in the string:

- pure ASCII and Latin1 strings ( - `U+0000-U+00FF`) use 1 byte per code point;
- BMP strings ( - `U+0000-U+FFFF`) use 2 bytes per code point;
- non-BMP strings ( - `U+10000-U+10FFFF`) use 4 bytes per code point.

The net effect is that for most applications, memory usage of string storage should decrease significantly - especially compared to former wide unicode builds - as, in many cases, strings will be pure ASCII even in international contexts (because many strings store non-human language data, such as XML fragments, HTTP headers, JSON-encoded data, etc.). We also hope that it will, for the same reasons, increase CPU cache efficiency on non-trivial applications. The memory usage of Python 3.3 is two to three times smaller than Python 3.2, and a little bit better than Python 2.7, on a Django benchmark (see the PEP for details).

See also

- **PEP 393**
- PEP written by Martin von Löwis; implementation by Torsten Becker and Martin von Löwis. 

## PEP 397: Python Launcher for Windows[¶](#pep-397-python-launcher-for-windows)

The Python 3.3 Windows installer now includes a `py` launcher application
that can be used to launch Python applications in a version independent
fashion.

This launcher is invoked implicitly when double-clicking `*.py` files.
If only a single Python version is installed on the system, that version
will be used to run the file. If multiple versions are installed, the most
recent version is used by default, but this can be overridden by including
a Unix-style “shebang line” in the Python script.

The launcher can also be used explicitly from the command line as the `py`
application. Running `py` follows the same version selection rules as
implicitly launching scripts, but a more specific version can be selected
by passing appropriate arguments (such as `-3` to request Python 3 when
Python 2 is also installed, or `-2.6` to specifically request an earlier
Python version when a more recent version is installed).

In addition to the launcher, the Windows installer now includes an
option to add the newly installed Python to the system PATH.  (Contributed
by Brian Curtin in [bpo-3561](https://bugs.python.org/issue?@action=redirect&bpo=3561).)

See also

- **PEP 397**
- PEP written by Mark Hammond and Martin v. Löwis; implementation by Vinay Sajip. 

Launcher documentation: [Python Launcher for Windows](../using/windows.html#launcher)

Installer PATH modification: [Finding the Python executable](../using/windows.html#windows-path-mod)

## PEP 3151: Reworking the OS and IO exception hierarchy[¶](#pep-3151-reworking-the-os-and-io-exception-hierarchy)

The hierarchy of exceptions raised by operating system errors is now both simplified and finer-grained.

You don’t have to worry anymore about choosing the appropriate exception
type between [ OSError](../library/exceptions.html#OSError), 

[,](../library/exceptions.html#IOError)

`IOError`[,](../library/exceptions.html#EnvironmentError)

`EnvironmentError`[,](../library/exceptions.html#WindowsError)

`WindowsError``mmap.error`, [or](../library/socket.html#socket.error)

`socket.error`[. All these exception types are now only one:](../library/select.html#select.error)

`select.error``OSError`.  The other names are kept as aliases for compatibility
reasons.Also, it is now easier to catch a specific error condition.  Instead of
inspecting the `errno` attribute (or `args[0]`) for a particular
constant from the [ errno](../library/errno.html#module-errno) module, you can catch the adequate

[subclass. The available subclasses are the following:](../library/exceptions.html#OSError)

`OSError`And the [ ConnectionError](../library/exceptions.html#ConnectionError) itself has finer-grained subclasses:

Thanks to the new exceptions, common usages of the [ errno](../library/errno.html#module-errno) can now be
avoided.  For example, the following code written for Python 3.2:

```
from errno import ENOENT, EACCES, EPERM
try:
    with open("document.txt") as f:
        content = f.read()
except IOError as err:
    if err.errno == ENOENT:
        print("document.txt file is missing")
    elif err.errno in (EACCES, EPERM):
        print("You are not allowed to read document.txt")
    else:
        raise
```
can now be written without the [ errno](../library/errno.html#module-errno) import and without manual
inspection of exception attributes:

```
try:
    with open("document.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("document.txt file is missing")
except PermissionError:
    print("You are not allowed to read document.txt")
```
See also

- **PEP 3151**
- PEP written and implemented by Antoine Pitrou 

## PEP 380: Syntax for Delegating to a Subgenerator[¶](#pep-380-syntax-for-delegating-to-a-subgenerator)

PEP 380 adds the `yield from` expression, allowing a [generator](../glossary.html#term-generator) to
delegate
part of its operations to another generator. This allows a section of code
containing [ yield](../reference/simple_stmts.html#yield) to be factored out and placed in another generator.
Additionally, the subgenerator is allowed to return with a value, and the
value is made available to the delegating generator.

While designed primarily for use in delegating to a subgenerator, the ```
yield
from
```
 expression actually allows delegation to arbitrary subiterators.

For simple iterators, `yield from iterable` is essentially just a shortened
form of `for item in iterable: yield item`:

```
>>> def g(x):
...     yield from range(x, 0, -1)
...     yield from range(x)
...
>>> list(g(5))
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
```
However, unlike an ordinary loop, `yield from` allows subgenerators to
receive sent and thrown values directly from the calling scope, and
return a final value to the outer generator:

```
>>> def accumulate():
...     tally = 0
...     while 1:
...         next = yield
...         if next is None:
...             return tally
...         tally += next
...
>>> def gather_tallies(tallies):
...     while 1:
...         tally = yield from accumulate()
...         tallies.append(tally)
...
>>> tallies = []
>>> acc = gather_tallies(tallies)
>>> next(acc)  # Ensure the accumulator is ready to accept values
>>> for i in range(4):
...     acc.send(i)
...
>>> acc.send(None)  # Finish the first tally
>>> for i in range(5):
...     acc.send(i)
...
>>> acc.send(None)  # Finish the second tally
>>> tallies
[6, 10]
```
The main principle driving this change is to allow even generators that are
designed to be used with the `send` and `throw` methods to be split into
multiple subgenerators as easily as a single large function can be split into
multiple subfunctions.

See also

- **PEP 380**
- PEP written by Greg Ewing; implementation by Greg Ewing, integrated into 3.3 by Renaud Blanch, Ryan Kelly and Nick Coghlan; documentation by Zbigniew Jędrzejewski-Szmek and Nick Coghlan 

## PEP 409: Suppressing exception context[¶](#pep-409-suppressing-exception-context)

PEP 409 introduces new syntax that allows the display of the chained exception context to be disabled. This allows cleaner error messages in applications that convert between exception types:

```
>>> class D:
...     def __init__(self, extra):
...         self._extra_attributes = extra
...     def __getattr__(self, attr):
...         try:
...             return self._extra_attributes[attr]
...         except KeyError:
...             raise AttributeError(attr) from None
...
>>> D({}).x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 8, in __getattr__
AttributeError: x
```
Without the `from None` suffix to suppress the cause, the original
exception would be displayed by default:

```
>>> class C:
...     def __init__(self, extra):
...         self._extra_attributes = extra
...     def __getattr__(self, attr):
...         try:
...             return self._extra_attributes[attr]
...         except KeyError:
...             raise AttributeError(attr)
...
>>> C({}).x
Traceback (most recent call last):
  File "<stdin>", line 6, in __getattr__
KeyError: 'x'
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 8, in __getattr__
AttributeError: x
```
No debugging capability is lost, as the original exception context remains available if needed (for example, if an intervening library has incorrectly suppressed valuable underlying details):

```
>>> try:
...     D({}).x
... except AttributeError as exc:
...     print(repr(exc.__context__))
...
KeyError('x',)
```
See also

- **PEP 409**
- PEP written by Ethan Furman; implemented by Ethan Furman and Nick Coghlan. 

## PEP 414: Explicit Unicode literals[¶](#pep-414-explicit-unicode-literals)

To ease the transition from Python 2 for Unicode aware Python applications
that make heavy use of Unicode literals, Python 3.3 once again supports the
“`u`” prefix for string literals. This prefix has no semantic significance
in Python 3, it is provided solely to reduce the number of purely mechanical
changes in migrating to Python 3, making it easier for developers to focus on
the more significant semantic changes (such as the stricter default
separation of binary and text data).

See also

- **PEP 414**
- PEP written by Armin Ronacher. 

## PEP 3155: Qualified name for classes and functions[¶](#pep-3155-qualified-name-for-classes-and-functions)

Functions and class objects have a new [ __qualname__](../library/stdtypes.html#definition.__qualname__)
attribute representing
the “path” from the module top-level to their definition.  For global functions
and classes, this is the same as 

[. For other functions and classes, it provides better information about where they were actually defined, and how they might be accessible from the global scope.](../library/stdtypes.html#definition.__name__)

`__name__`Example with (non-bound) methods:

```
>>> class C:
...     def meth(self):
...         pass
...
>>> C.meth.__name__
'meth'
>>> C.meth.__qualname__
'C.meth'
```
Example with nested classes:

```
>>> class C:
...     class D:
...         def meth(self):
...             pass
...
>>> C.D.__name__
'D'
>>> C.D.__qualname__
'C.D'
>>> C.D.meth.__name__
'meth'
>>> C.D.meth.__qualname__
'C.D.meth'
```
Example with nested functions:

```
>>> def outer():
...     def inner():
...         pass
...     return inner
...
>>> outer().__name__
'inner'
>>> outer().__qualname__
'outer.<locals>.inner'
```
The string representation of those objects is also changed to include the new, more precise information:

```
>>> str(C.D)
"<class '__main__.C.D'>"
>>> str(C.D.meth)
'<function C.D.meth at 0x7f46b9fe31e0>'
```
See also

- **PEP 3155**
- PEP written and implemented by Antoine Pitrou. 

## PEP 412: Key-Sharing Dictionary[¶](#pep-412-key-sharing-dictionary)

Dictionaries used for the storage of objects’ attributes are now able to share part of their internal storage between each other (namely, the part which stores the keys and their respective hashes). This reduces the memory consumption of programs creating many instances of non-builtin types.

See also

- **PEP 412**
- PEP written and implemented by Mark Shannon. 

## PEP 362: Function Signature Object[¶](#pep-362-function-signature-object)

A new function [ inspect.signature()](../library/inspect.html#inspect.signature) makes introspection of python
callables easy and straightforward.  A broad range of callables is supported:
python functions, decorated or not, classes, and 

[objects. New classes](../library/functools.html#functools.partial)

`functools.partial()`[,](../library/inspect.html#inspect.Signature)

`inspect.Signature`[and](../library/inspect.html#inspect.Parameter)

`inspect.Parameter`[hold information about the call signatures, such as, annotations, default values, parameters kinds, and bound arguments, which considerably simplifies writing decorators and any code that validates or amends calling signatures or arguments.](../library/inspect.html#inspect.BoundArguments)

`inspect.BoundArguments`See also

- **PEP 362**
- PEP written by Brett Cannon, Yury Selivanov, Larry Hastings, Jiwon Seo; implemented by Yury Selivanov. 

## PEP 421: Adding sys.implementation[¶](#pep-421-adding-sys-implementation)

A new attribute on the [ sys](../library/sys.html#module-sys) module exposes details specific to the
implementation of the currently running interpreter.  The initial set of
attributes on 

[are](../library/sys.html#sys.implementation)

`sys.implementation``name`, `version`,
`hexversion`, and `cache_tag`.The intention of `sys.implementation` is to consolidate into one namespace
the implementation-specific data used by the standard library.  This allows
different Python implementations to share a single standard library code base
much more easily.  In its initial state, `sys.implementation` holds only a
small portion of the implementation-specific data.  Over time that ratio will
shift in order to make the standard library more portable.

One example of improved standard library portability is `cache_tag`.  As of
Python 3.3, `sys.implementation.cache_tag` is used by [ importlib](../library/importlib.html#module-importlib) to
support 

[compliance. Any Python implementation that uses](https://peps.python.org/pep-3147/)

**PEP 3147**`importlib` for its built-in import system may use `cache_tag` to control
the caching behavior for modules.### SimpleNamespace[¶](#simplenamespace)

The implementation of `sys.implementation` also introduces a new type to
Python: [ types.SimpleNamespace](../library/types.html#types.SimpleNamespace).  In contrast to a mapping-based
namespace, like 

[,](../library/stdtypes.html#dict)

`dict``SimpleNamespace` is attribute-based, like
[. However, unlike](../library/functions.html#object)

`object``object`, `SimpleNamespace` instances
are writable.  This means that you can add, remove, and modify the namespace
through normal attribute access.See also

- **PEP 421**
- PEP written and implemented by Eric Snow. 

## Using importlib as the Implementation of Import[¶](#using-importlib-as-the-implementation-of-import)

[bpo-2377](https://bugs.python.org/issue?@action=redirect&bpo=2377) - Replace __import__ w/ importlib.__import__
[bpo-13959](https://bugs.python.org/issue?@action=redirect&bpo=13959) - Re-implement parts of `imp` in pure Python
[bpo-14605](https://bugs.python.org/issue?@action=redirect&bpo=14605) - Make import machinery explicit
[bpo-14646](https://bugs.python.org/issue?@action=redirect&bpo=14646) - Require loaders set __loader__ and __package__

The [ __import__()](../library/functions.html#import__) function is now powered by 

[. This work leads to the completion of “phase 2” of](../library/importlib.html#importlib.__import__)

`importlib.__import__()`[. There are multiple benefits to this change. First, it has allowed for more of the machinery powering import to be exposed instead of being implicit and hidden within the C code. It also provides a single implementation for all Python VMs supporting Python 3.3 to use, helping to end any VM-specific deviations in import semantics. And finally it eases the maintenance of import, allowing for future growth to occur.](https://peps.python.org/pep-0302/)

**PEP 302**For the common user, there should be no visible change in semantics.  For
those whose code currently manipulates import or calls import
programmatically, the code changes that might possibly be required are covered
in the [Porting Python code](#porting-python-code) section of this document.

### New APIs[¶](#new-apis)

One of the large benefits of this work is the exposure of what goes into
making the import statement work. That means the various importers that were
once implicit are now fully exposed as part of the [ importlib](../library/importlib.html#module-importlib) package.

The abstract base classes defined in [ importlib.abc](../library/importlib.html#module-importlib.abc) have been expanded
to properly delineate between 

[meta path finders](../glossary.html#term-meta-path-finder)and

[path entry finders](../glossary.html#term-path-entry-finder)by introducing

[and](../library/importlib.html#importlib.abc.MetaPathFinder)

`importlib.abc.MetaPathFinder`[, respectively. The old ABC of](../library/importlib.html#importlib.abc.PathEntryFinder)

`importlib.abc.PathEntryFinder``importlib.abc.Finder` is now only provided for backwards-compatibility
and does not enforce any method requirements.In terms of finders, [ importlib.machinery.FileFinder](../library/importlib.html#importlib.machinery.FileFinder) exposes the
mechanism used to search for source and bytecode files of a module. Previously
this class was an implicit member of 

[.](../library/sys.html#sys.path_hooks)

`sys.path_hooks`For loaders, the new abstract base class [ importlib.abc.FileLoader](../library/importlib.html#importlib.abc.FileLoader) helps
write a loader that uses the file system as the storage mechanism for a module’s
code. The loader for source files
(

[), sourceless bytecode files (](../library/importlib.html#importlib.machinery.SourceFileLoader)

`importlib.machinery.SourceFileLoader`[), and extension modules (](../library/importlib.html#importlib.machinery.SourcelessFileLoader)

`importlib.machinery.SourcelessFileLoader`[) are now available for direct use.](../library/importlib.html#importlib.machinery.ExtensionFileLoader)

`importlib.machinery.ExtensionFileLoader`[ ImportError](../library/exceptions.html#ImportError) now has 

`name` and `path` attributes which are set when
there is relevant data to provide. The message for failed imports will also
provide the full name of the module now instead of just the tail end of the
module’s name.The [ importlib.invalidate_caches()](../library/importlib.html#importlib.invalidate_caches) function will now call the method with
the same name on all finders cached in 

[to help clean up any stored state as necessary.](../library/sys.html#sys.path_importer_cache)

`sys.path_importer_cache`### Visible Changes[¶](#visible-changes)

For potential required changes to code, see the [Porting Python code](#porting-python-code)
section.

Beyond the expanse of what [ importlib](../library/importlib.html#module-importlib) now exposes, there are other
visible changes to import. The biggest is that 

[and](../library/sys.html#sys.meta_path)

`sys.meta_path`[now store all of the meta path finders and path entry hooks used by import. Previously the finders were implicit and hidden within the C code of import instead of being directly exposed. This means that one can now easily remove or change the order of the various finders to fit one’s needs.](../library/sys.html#sys.path_hooks)

`sys.path_hooks`Another change is that all modules have a `__loader__` attribute, storing the
loader used to create the module. [ PEP 302](https://peps.python.org/pep-0302/) has been updated to make this
attribute mandatory for loaders to implement, so in the future once 3rd-party
loaders have been updated people will be able to rely on the existence of the
attribute. Until such time, though, import is setting the module post-load.

Loaders are also now expected to set the `__package__` attribute from
[ PEP 366](https://peps.python.org/pep-0366/). Once again, import itself is already setting this on all loaders
from 

[and import itself is setting the attribute post-load.](../library/importlib.html#module-importlib)

`importlib``None` is now inserted into [ sys.path_importer_cache](../library/sys.html#sys.path_importer_cache) when no finder
can be found on 

[. Since](../library/sys.html#sys.path_hooks)

`sys.path_hooks``imp.NullImporter` is not
directly exposed on `sys.path_hooks` it could no longer be relied upon to
always be available to use as a value representing no finder found.All other changes relate to semantic changes which should be taken into
consideration when updating code for Python 3.3, and thus should be read about
in the [Porting Python code](#porting-python-code) section of this document.

(Implementation by Brett Cannon)

## Other Language Changes[¶](#other-language-changes)

Some smaller changes made to the core Python language are:

- Added support for Unicode name aliases and named sequences. Both - `unicodedata.lookup()`- `'\N{...}'`now resolve name aliases, and- `unicodedata.lookup()`resolves named sequences too.- (Contributed by Ezio Melotti in - [bpo-12753](https://bugs.python.org/issue?@action=redirect&bpo=12753).)
- Unicode database updated to UCD version 6.1.0 
- Equality comparisons on - `range()`- [bpo-13201](https://bugs.python.org/issue?@action=redirect&bpo=13201))
- The - `count()`,- `find()`,- `rfind()`,- `index()`and- `rindex()`methods of- `bytes`- `bytearray`- (Contributed by Petri Lehtinen in - [bpo-12170](https://bugs.python.org/issue?@action=redirect&bpo=12170).)
- The - `rjust()`,- `ljust()`, and- `center()`methods of- `bytes`- `bytearray`- `bytearray`for the- `fill`argument. (Contributed by Petri Lehtinen in- [bpo-12380](https://bugs.python.org/issue?@action=redirect&bpo=12380).)
- New methods have been added to - `list`- `bytearray`- `copy()`and- `clear()`(- [bpo-10516](https://bugs.python.org/issue?@action=redirect&bpo=10516)). Consequently,- `MutableSequence`- `clear()`method (- [bpo-11388](https://bugs.python.org/issue?@action=redirect&bpo=11388)).
- Raw bytes literals can now be written - `rb"..."`as well as- `br"..."`.- (Contributed by Antoine Pitrou in - [bpo-13748](https://bugs.python.org/issue?@action=redirect&bpo=13748).)
- `dict.setdefault()`- (Contributed by Filip Gruszczyński in - [bpo-13521](https://bugs.python.org/issue?@action=redirect&bpo=13521).)
- The error messages produced when a function call does not match the function signature have been significantly improved. - (Contributed by Benjamin Peterson.) 

## A Finer-Grained Import Lock[¶](#a-finer-grained-import-lock)

Previous versions of CPython have always relied on a global import lock.
This led to unexpected annoyances, such as deadlocks when importing a module
would trigger code execution in a different thread as a side-effect.
Clumsy workarounds were sometimes employed, such as the
[ PyImport_ImportModuleNoBlock()](../c-api/import.html#c.PyImport_ImportModuleNoBlock) C API function.

In Python 3.3, importing a module takes a per-module lock. This correctly serializes importation of a given module from multiple threads (preventing the exposure of incompletely initialized modules), while eliminating the aforementioned annoyances.

(Contributed by Antoine Pitrou in [bpo-9260](https://bugs.python.org/issue?@action=redirect&bpo=9260).)

## Builtin functions and types[¶](#builtin-functions-and-types)

- `open()`- *opener*parameter: the underlying file descriptor for the file object is then obtained by calling- *opener*with (- *file*,- *flags*). It can be used to use custom flags like- `os.O_CLOEXEC`- `'x'`mode was added: open for exclusive creation, failing if the file already exists.
- `print()`- *flush*keyword argument. If the- *flush*keyword argument is true, the stream is forcibly flushed.
- `hash()`- `object.__hash__()`- `PYTHONHASHSEED`
- The - `str`- `casefold()`- `'ß'.casefold()`returns- `'ss'`.
- The sequence documentation has been substantially rewritten to better explain the binary/text sequence distinction and to provide specific documentation sections for the individual builtin sequence types ( - [bpo-4966](https://bugs.python.org/issue?@action=redirect&bpo=4966)).

## New Modules[¶](#new-modules)

### faulthandler[¶](#faulthandler)

This new debug module [ faulthandler](../library/faulthandler.html#module-faulthandler) contains functions to dump Python tracebacks explicitly,
on a fault (a crash like a segmentation fault), after a timeout, or on a user
signal. Call 

[to install fault handlers for the](../library/faulthandler.html#faulthandler.enable)

`faulthandler.enable()`[,](../library/signal.html#signal.SIGSEGV)

`SIGSEGV`[,](../library/signal.html#signal.SIGFPE)

`SIGFPE`[,](../library/signal.html#signal.SIGABRT)

`SIGABRT`[, and](../library/signal.html#signal.SIGBUS)

`SIGBUS`[signals. You can also enable them at startup by setting the](../library/signal.html#signal.SIGILL)

`SIGILL`[environment variable or by using](../using/cmdline.html#envvar-PYTHONFAULTHANDLER)

`PYTHONFAULTHANDLER`

`-X``faulthandler` command line option.Example of a segmentation fault on Linux:

```
$ python -q -X faulthandler
>>> import ctypes
>>> ctypes.string_at(0)
Fatal Python error: Segmentation fault
Current thread 0x00007fb899f39700:
  File "/home/python/cpython/Lib/ctypes/__init__.py", line 486 in string_at
  File "<stdin>", line 1 in <module>
Segmentation fault
```
### ipaddress[¶](#ipaddress)

The new [ ipaddress](../library/ipaddress.html#module-ipaddress) module provides tools for creating and manipulating
objects representing IPv4 and IPv6 addresses, networks and interfaces (i.e.
an IP address associated with a specific IP subnet).

(Contributed by Google and Peter Moody in [ PEP 3144](https://peps.python.org/pep-3144/).)

### lzma[¶](#lzma)

The newly added [ lzma](../library/lzma.html#module-lzma) module provides data compression and decompression
using the LZMA algorithm, including support for the 

`.xz` and `.lzma`
file formats.(Contributed by Nadeem Vawda and Per Øyvind Karlsen in [bpo-6715](https://bugs.python.org/issue?@action=redirect&bpo=6715).)

## Improved Modules[¶](#improved-modules)

### abc[¶](#abc)

Improved support for abstract base classes containing descriptors composed with
abstract methods. The recommended approach to declaring abstract descriptors is
now to provide `__isabstractmethod__` as a dynamically updated
property. The built-in descriptors have been updated accordingly.

- `abc.abstractproperty`- `property`- `abc.abstractmethod()`
- `abc.abstractclassmethod`- `classmethod`- `abc.abstractmethod()`
- `abc.abstractstaticmethod`- `staticmethod`- `abc.abstractmethod()`

(Contributed by Darren Dale in [bpo-11610](https://bugs.python.org/issue?@action=redirect&bpo=11610).)

[ abc.ABCMeta.register()](../library/abc.html#abc.ABCMeta.register) now returns the registered subclass, which means
it can now be used as a class decorator (

[bpo-10868](https://bugs.python.org/issue?@action=redirect&bpo=10868)).

### array[¶](#array)

The [ array](../library/array.html#module-array) module supports the long long type using 

`q` and
`Q` type codes.(Contributed by Oren Tirosh and Hirokazu Yamamoto in [bpo-1172711](https://bugs.python.org/issue?@action=redirect&bpo=1172711).)

### base64[¶](#base64)

ASCII-only Unicode strings are now accepted by the decoding functions of the
[ base64](../library/base64.html#module-base64) modern interface. For example, 

`base64.b64decode('YWJj')`
returns `b'abc'`.  (Contributed by Catalin Iacob in [bpo-13641](https://bugs.python.org/issue?@action=redirect&bpo=13641).)

### binascii[¶](#binascii)

In addition to the binary objects they normally accept, the `a2b_` functions
now all also accept ASCII-only strings as input.  (Contributed by Antoine
Pitrou in [bpo-13637](https://bugs.python.org/issue?@action=redirect&bpo=13637).)

### bz2[¶](#bz2)

The [ bz2](../library/bz2.html#module-bz2) module has been rewritten from scratch. In the process, several
new features have been added:

- New - `bz2.open()`
- `bz2.BZ2File`- *fileobj*argument.- (Contributed by Nadeem Vawda in - [bpo-5863](https://bugs.python.org/issue?@action=redirect&bpo=5863).)
- `bz2.BZ2File`- `bz2.decompress()`- **pbzip2**tool).- `bz2.BZ2File`can now also be used to create this type of file, using the- `'a'`(append) mode.- (Contributed by Nir Aides in - [bpo-1625](https://bugs.python.org/issue?@action=redirect&bpo=1625).)
- `bz2.BZ2File`- `io.BufferedIOBase`- `detach()`and- `truncate()`methods.

### codecs[¶](#codecs)

The [ mbcs](../library/codecs.html#module-encodings.mbcs) codec has been rewritten to handle correctly

`replace` and `ignore` error handlers on all Windows versions.  The
`mbcs` codec now supports all error handlers, instead of only
`replace` to encode and `ignore` to decode.A new Windows-only codec has been added: `cp65001` ([bpo-13216](https://bugs.python.org/issue?@action=redirect&bpo=13216)). It is the
Windows code page 65001 (Windows UTF-8, `CP_UTF8`).  For example, it is used
by `sys.stdout` if the console output code page is set to cp65001 (e.g., using
`chcp 65001` command).

Multibyte CJK decoders now resynchronize faster.  They only ignore the first
byte of an invalid byte sequence. For example, ```
b'\xff\n'.decode('gb2312',
'replace')
```
 now returns a `\n` after the replacement character.

Incremental CJK codec encoders are no longer reset at each call to their encode() methods. For example:

```
>>> import codecs
>>> encoder = codecs.getincrementalencoder('hz')('strict')
>>> b''.join(encoder.encode(x) for x in '\u52ff\u65bd\u65bc\u4eba\u3002 Bye.')
b'~{NpJ)l6HK!#~} Bye.'
```
This example gives `b'~{Np~}~{J)~}~{l6~}~{HK~}~{!#~} Bye.'` with older Python
versions.

The `unicode_internal` codec has been deprecated.

### collections[¶](#collections)

Addition of a new [ ChainMap](../library/collections.html#collections.ChainMap) class to allow treating a
number of mappings as a single unit.  (Written by Raymond Hettinger for

[bpo-11089](https://bugs.python.org/issue?@action=redirect&bpo=11089), made public in

[bpo-11297](https://bugs.python.org/issue?@action=redirect&bpo=11297).)

The abstract base classes have been moved in a new [ collections.abc](../library/collections.abc.html#module-collections.abc)
module, to better differentiate between the abstract and the concrete
collections classes.  Aliases for ABCs are still present in the

[module to preserve existing imports. (](../library/collections.html#module-collections)

`collections`[bpo-11085](https://bugs.python.org/issue?@action=redirect&bpo=11085))

The [ Counter](../library/collections.html#collections.Counter) class now supports the unary 

`+` and `-`
operators, as well as the in-place operators `+=`, `-=`, `|=`, and
`&=`.  (Contributed by Raymond Hettinger in [bpo-13121](https://bugs.python.org/issue?@action=redirect&bpo=13121).)

### contextlib[¶](#contextlib)

[ ExitStack](../library/contextlib.html#contextlib.ExitStack) now provides a solid foundation for
programmatic manipulation of context managers and similar cleanup
functionality. Unlike the previous 

`contextlib.nested` API (which was
deprecated and removed), the new API is designed to work correctly
regardless of whether context managers acquire their resources in
their `__init__` method (for example, file objects) or in their
`__enter__` method (for example, synchronisation objects from the
[module).](../library/threading.html#module-threading)

`threading`### crypt[¶](#crypt)

Addition of salt and modular crypt format (hashing method) and the `mksalt()`
function to the `crypt` module.

### curses[¶](#curses)

- If the - `curses`- `waddwstr()`), and bytes functions otherwise (e.g.- `waddstr()`).
- Use the locale encoding instead of - `utf-8`to encode Unicode strings.
- `curses.window`- `curses.window.encoding`
- The - `curses.window`- `get_wch()`
- The - `curses`- `unget_wch()`- `get_wch()`

(Contributed by Iñigo Serna in [bpo-6755](https://bugs.python.org/issue?@action=redirect&bpo=6755).)

### datetime[¶](#datetime)

- Equality comparisons between naive and aware - `datetime`- `False`- `TypeError`- [bpo-15006](https://bugs.python.org/issue?@action=redirect&bpo=15006)).
- New - `datetime.datetime.timestamp()`- `datetime`
- The - `datetime.datetime.strftime()`
- The - `datetime.datetime.astimezone()`

### decimal[¶](#decimal)

- [bpo-7652](https://bugs.python.org/issue?@action=redirect&bpo=7652)- integrate fast native decimal arithmetic.
- C-module and libmpdec written by Stefan Krah. 

The new C version of the decimal module integrates the high speed libmpdec library for arbitrary precision correctly rounded decimal floating-point arithmetic. libmpdec conforms to IBM’s General Decimal Arithmetic Specification.

Performance gains range from 10x for database applications to 100x for numerically intensive applications. These numbers are expected gains for standard precisions used in decimal floating-point arithmetic. Since the precision is user configurable, the exact figures may vary. For example, in integer bignum arithmetic the differences can be significantly higher.

The following table is meant as an illustration. Benchmarks are available
at [https://www.bytereef.org/mpdecimal/quickstart.html](https://www.bytereef.org/mpdecimal/quickstart.html).


decimal.py

_decimal

speedup

pi

42.02s

0.345s

120x

telco

172.19s

5.68s

30x

psycopg

3.57s

0.29s

12x


#### Features[¶](#id1)

- The - `FloatOperation`
- If Python is compiled without threads, the C version automatically disables the expensive thread local context machinery. In this case, the variable - `HAVE_THREADS`- `False`.

#### API changes[¶](#id2)

- The C module has the following context limits, depending on the machine architecture: 
- In the context templates ( - `DefaultContext`- `BasicContext`- `ExtendedContext`- `Emax`- `Emin`- `999999`.
- The - `Decimal`- `InvalidOperation`- `create_decimal()`
- The power function in decimal.py is always correctly rounded. In the C version, it is defined in terms of the correctly rounded - `exp()`- `ln()`
- In the C version, the context dictionary containing the signals is a - `MutableMapping`- `flags`- `traps`- `MutableMapping`that the context was initialized with. If a new signal dictionary is assigned,- `flags`and- `traps`are updated with the new values, but they do not reference the RHS dictionary.
- Pickling a - `Context`
- The order of arguments in the - `Context`- `repr()`
- The - `watchexp`parameter in the- `quantize()`

### email[¶](#email)

#### Policy Framework[¶](#policy-framework)

The email package now has a [ policy](../library/email.policy.html#module-email.policy) framework.  A

[is an object with several methods and properties that control how the email package behaves. The primary policy for Python 3.3 is the](../library/email.policy.html#email.policy.Policy)

`Policy`[policy, which provides backward compatibility with the email package in Python 3.2. A](../library/email.policy.html#email.policy.Compat32)

`Compat32``policy` can be
specified when an email message is parsed by a [, or when a](../library/email.parser.html#module-email.parser)

`parser`[object is created, or when an email is serialized using a](../library/email.compat32-message.html#email.message.Message)

`Message`[. Unless overridden, a policy passed to a](../library/email.generator.html#module-email.generator)

`generator``parser` is inherited by all the `Message` object and sub-objects
created by the `parser`.  By default a `generator` will use the policy of
the `Message` object it is serializing.  The default policy is
[.](../library/email.policy.html#email.policy.compat32)

`compat32`The minimum set of controls implemented by all `policy` objects are:

| max_line_length | The maximum length, excluding the linesep character(s),
individual lines may have when a  | 
| linesep | The character used to separate individual lines when a
 | 
| cte_type | 
 | 
| raise_on_defect | Causes a  | 

A new policy instance, with new settings, is created using the
[ clone()](../library/email.policy.html#email.policy.Policy.clone) method of policy objects.  

`clone` takes
any of the above controls as keyword arguments.  Any control not specified in
the call retains its default value.  Thus you can create a policy that uses
`\r\n` linesep characters like this:```
mypolicy = compat32.clone(linesep='\r\n')
```
Policies can be used to make the generation of messages in the format needed by
your application simpler.  Instead of having to remember to specify
`linesep='\r\n'` in all the places you call a `generator`, you can specify
it once, when you set the policy used by the `parser` or the `Message`,
whichever your program uses to create `Message` objects.  On the other hand,
if you need to generate messages in multiple forms, you can still specify the
parameters in the appropriate `generator` call.  Or you can have custom
policy instances for your different cases, and pass those in when you create
the `generator`.

#### Provisional Policy with New Header API[¶](#provisional-policy-with-new-header-api)

While the policy framework is worthwhile all by itself, the main motivation for
introducing it is to allow the creation of new policies that implement new
features for the email package in a way that maintains backward compatibility
for those who do not use the new policies.  Because the new policies introduce a
new API, we are releasing them in Python 3.3 as a [provisional policy](../glossary.html#term-provisional-package).  Backwards incompatible changes (up to and including
removal of the code) may occur if deemed necessary by the core developers.

The new policies are instances of [ EmailPolicy](../library/email.policy.html#email.policy.EmailPolicy),
and add the following additional controls:

| refold_source | Controls whether or not headers parsed by a
 .  It can be`generator``none`,`long`,
or`all`.  The default is`long`, which means that
source headers with a line longer than`max_line_length`get refolded.`none`means no
line get refolded, and`all`means that all lines
get refolded. | 
| header_factory | A callable that take a  | 

The `header_factory` is the key to the new features provided by the new
policies.  When one of the new policies is used, any header retrieved from
a `Message` object is an object produced by the `header_factory`, and any
time you set a header on a `Message` it becomes an object produced by
`header_factory`.  All such header objects have a `name` attribute equal
to the header name.  Address and Date headers have additional attributes
that give you access to the parsed data of the header.  This means you can now
do things like this:

```
>>> m = Message(policy=SMTP)
>>> m['To'] = 'Éric <foo@example.com>'
>>> m['to']
'Éric <foo@example.com>'
>>> m['to'].addresses
(Address(display_name='Éric', username='foo', domain='example.com'),)
>>> m['to'].addresses[0].username
'foo'
>>> m['to'].addresses[0].display_name
'Éric'
>>> m['Date'] = email.utils.localtime()
>>> m['Date'].datetime
datetime.datetime(2012, 5, 25, 21, 39, 24, 465484, tzinfo=datetime.timezone(datetime.timedelta(-1, 72000), 'EDT'))
>>> m['Date']
'Fri, 25 May 2012 21:44:27 -0400'
>>> print(m)
To: =?utf-8?q?=C3=89ric?= <foo@example.com>
Date: Fri, 25 May 2012 21:44:27 -0400
```
You will note that the unicode display name is automatically encoded as
`utf-8` when the message is serialized, but that when the header is accessed
directly, you get the unicode version.  This eliminates any need to deal with
the `email.header`[ decode_header()](../library/email.header.html#email.header.decode_header) or

[functions.](../library/email.header.html#email.header.make_header)

`make_header()`You can also create addresses from parts:

```
>>> m['cc'] = [Group('pals', [Address('Bob', 'bob', 'example.com'),
...                           Address('Sally', 'sally', 'example.com')]),
...            Address('Bonzo', addr_spec='bonz@laugh.com')]
>>> print(m)
To: =?utf-8?q?=C3=89ric?= <foo@example.com>
Date: Fri, 25 May 2012 21:44:27 -0400
cc: pals: Bob <bob@example.com>, Sally <sally@example.com>;, Bonzo <bonz@laugh.com>
```
Decoding to unicode is done automatically:

```
>>> m2 = message_from_string(str(m))
>>> m2['to']
'Éric <foo@example.com>'
```
When you parse a message, you can use the `addresses` and `groups`
attributes of the header objects to access the groups and individual
addresses:

```
>>> m2['cc'].addresses
(Address(display_name='Bob', username='bob', domain='example.com'), Address(display_name='Sally', username='sally', domain='example.com'), Address(display_name='Bonzo', username='bonz', domain='laugh.com'))
>>> m2['cc'].groups
(Group(display_name='pals', addresses=(Address(display_name='Bob', username='bob', domain='example.com'), Address(display_name='Sally', username='sally', domain='example.com')), Group(display_name=None, addresses=(Address(display_name='Bonzo', username='bonz', domain='laugh.com'),))
```
In summary, if you use one of the new policies, header manipulation works the way it ought to: your application works with unicode strings, and the email package transparently encodes and decodes the unicode to and from the RFC standard Content Transfer Encodings.

#### Other API Changes[¶](#other-api-changes)

New [ BytesHeaderParser](../library/email.parser.html#email.parser.BytesHeaderParser), added to the 

[module to complement](../library/email.parser.html#module-email.parser)

`parser`[and complete the Bytes API.](../library/email.parser.html#email.parser.HeaderParser)

`HeaderParser`New utility functions:

- `format_datetime()`- `datetime`
- `parsedate_to_datetime()`- `datetime`- `datetime`if the offset is- `-0000`.
- `localtime()`- `datetime`- `timezone`- `datetime`, converts it into an aware- `datetime`using the local- `timezone`.

### ftplib[¶](#ftplib)

- `ftplib.FTP`- `source_address`keyword argument to specify the- `(host, port)`to use as the source address in the bind call when creating the outgoing socket. (Contributed by Giampaolo Rodolà in- [bpo-8594](https://bugs.python.org/issue?@action=redirect&bpo=8594).)
- The - `FTP_TLS`- `ccc()`- [bpo-12139](https://bugs.python.org/issue?@action=redirect&bpo=12139).)
- Added - `ftplib.FTP.mlsd()`- `ftplib.FTP.nlst()`- `ftplib.FTP.dir()`- [bpo-11072](https://bugs.python.org/issue?@action=redirect&bpo=11072).)

### functools[¶](#functools)

The [ functools.lru_cache()](../library/functools.html#functools.lru_cache) decorator now accepts a 

`typed` keyword
argument (that defaults to `False` to ensure that it caches values of
different types that compare equal in separate cache slots.  (Contributed
by Raymond Hettinger in [bpo-13227](https://bugs.python.org/issue?@action=redirect&bpo=13227).)

### gc[¶](#gc)

It is now possible to register callbacks invoked by the garbage collector
before and after collection using the new [ callbacks](../library/gc.html#gc.callbacks) list.

### hmac[¶](#hmac)

A new [ compare_digest()](../library/hmac.html#hmac.compare_digest) function has been added to prevent side
channel attacks on digests through timing analysis.  (Contributed by Nick
Coghlan and Christian Heimes in 

[bpo-15061](https://bugs.python.org/issue?@action=redirect&bpo=15061).)

### http[¶](#http)

[ http.server.BaseHTTPRequestHandler](../library/http.server.html#http.server.BaseHTTPRequestHandler) now buffers the headers and writes
them all at once when 

[is called. A new method](../library/http.server.html#http.server.BaseHTTPRequestHandler.end_headers)

`end_headers()`[can be used to directly manage when the accumulated headers are sent. (Contributed by Andrew Schaaf in](../library/http.server.html#http.server.BaseHTTPRequestHandler.flush_headers)

`flush_headers()`[bpo-3709](https://bugs.python.org/issue?@action=redirect&bpo=3709).)

[ http.server](../library/http.server.html#module-http.server) now produces valid 

`HTML 4.01 strict` output.
(Contributed by Ezio Melotti in [bpo-13295](https://bugs.python.org/issue?@action=redirect&bpo=13295).)

[ http.client.HTTPResponse](../library/http.client.html#http.client.HTTPResponse) now has a

[method, which means it can be used as an](../library/http.client.html#http.client.HTTPResponse.readinto)

`readinto()`[class. (Contributed by John Kuhn in](../library/io.html#io.RawIOBase)

`io.RawIOBase`[bpo-13464](https://bugs.python.org/issue?@action=redirect&bpo=13464).)

### html[¶](#html)

[ html.parser.HTMLParser](../library/html.parser.html#html.parser.HTMLParser) is now able to parse broken markup without
raising errors, therefore the 

*strict*argument of the constructor and the

`HTMLParseError` exception are now deprecated.
The ability to parse broken markup is the result of a number of bug fixes that
are also available on the latest bug fix releases of Python 2.7/3.2.
(Contributed by Ezio Melotti in [bpo-15114](https://bugs.python.org/issue?@action=redirect&bpo=15114), and

[bpo-14538](https://bugs.python.org/issue?@action=redirect&bpo=14538),

[bpo-13993](https://bugs.python.org/issue?@action=redirect&bpo=13993),

[bpo-13960](https://bugs.python.org/issue?@action=redirect&bpo=13960),

[bpo-13358](https://bugs.python.org/issue?@action=redirect&bpo=13358),

[bpo-1745761](https://bugs.python.org/issue?@action=redirect&bpo=1745761),

[bpo-755670](https://bugs.python.org/issue?@action=redirect&bpo=755670),

[bpo-13357](https://bugs.python.org/issue?@action=redirect&bpo=13357),

[bpo-12629](https://bugs.python.org/issue?@action=redirect&bpo=12629),

[bpo-1200313](https://bugs.python.org/issue?@action=redirect&bpo=1200313),

[bpo-670664](https://bugs.python.org/issue?@action=redirect&bpo=670664),

[bpo-13273](https://bugs.python.org/issue?@action=redirect&bpo=13273),

[bpo-12888](https://bugs.python.org/issue?@action=redirect&bpo=12888),

[bpo-7311](https://bugs.python.org/issue?@action=redirect&bpo=7311).)

A new [ html5](../library/html.entities.html#html.entities.html5) dictionary that maps HTML5 named character
references to the equivalent Unicode character(s) (e.g. 

```
html5['gt;'] ==
'>'
```
) has been added to the [module. The dictionary is now also used by](../library/html.entities.html#module-html.entities)

`html.entities`[. (Contributed by Ezio Melotti in](../library/html.parser.html#html.parser.HTMLParser)

`HTMLParser`[bpo-11113](https://bugs.python.org/issue?@action=redirect&bpo=11113)and

[bpo-15156](https://bugs.python.org/issue?@action=redirect&bpo=15156).)

### imaplib[¶](#imaplib)

The [ IMAP4_SSL](../library/imaplib.html#imaplib.IMAP4_SSL) constructor now accepts an SSLContext
parameter to control parameters of the secure channel.

(Contributed by Sijin Joseph in [bpo-8808](https://bugs.python.org/issue?@action=redirect&bpo=8808).)

### inspect[¶](#inspect)

A new [ getclosurevars()](../library/inspect.html#inspect.getclosurevars) function has been added. This function
reports the current binding of all names referenced from the function body and
where those names were resolved, making it easier to verify correct internal
state when testing code that relies on stateful closures.

(Contributed by Meador Inge and Nick Coghlan in [bpo-13062](https://bugs.python.org/issue?@action=redirect&bpo=13062).)

A new [ getgeneratorlocals()](../library/inspect.html#inspect.getgeneratorlocals) function has been added. This
function reports the current binding of local variables in the generator’s
stack frame, making it easier to verify correct internal state when testing
generators.

(Contributed by Meador Inge in [bpo-15153](https://bugs.python.org/issue?@action=redirect&bpo=15153).)

### io[¶](#io)

The [ open()](../library/io.html#io.open) function has a new 

`'x'` mode that can be used to
exclusively create a new file, and raise a [if the file already exists. It is based on the C11 ‘x’ mode to fopen().](../library/exceptions.html#FileExistsError)

`FileExistsError`(Contributed by David Townshend in [bpo-12760](https://bugs.python.org/issue?@action=redirect&bpo=12760).)

The constructor of the [ TextIOWrapper](../library/io.html#io.TextIOWrapper) class has a new

*write_through*optional argument. If

*write_through*is

`True`, calls to
`write()` are guaranteed not to be buffered: any data
written on the `TextIOWrapper` object is immediately handled to its
underlying binary buffer.### itertools[¶](#itertools)

[ accumulate()](../library/itertools.html#itertools.accumulate) now takes an optional 

`func` argument for
providing a user-supplied binary function.### logging[¶](#logging)

The [ basicConfig()](../library/logging.html#logging.basicConfig) function now supports an optional 

`handlers`
argument taking an iterable of handlers to be added to the root logger.A class level attribute `append_nul` has
been added to [ SysLogHandler](../library/logging.handlers.html#logging.handlers.SysLogHandler) to allow control of the
appending of the 

`NUL` (`\000`) byte to syslog records, since for some
daemons it is required while for others it is passed through to the log.### math[¶](#math)

The [ math](../library/math.html#module-math) module has a new function, 

[, which returns the base-2 logarithm of](../library/math.html#math.log2)

`log2()`*x*.

(Written by Mark Dickinson in [bpo-11888](https://bugs.python.org/issue?@action=redirect&bpo=11888).)

### mmap[¶](#mmap)

The [ read()](../library/mmap.html#mmap.mmap.read) method is now more compatible with other file-like
objects: if the argument is omitted or specified as 

`None`, it returns the
bytes from the current file position to the end of the mapping.  (Contributed
by Petri Lehtinen in [bpo-12021](https://bugs.python.org/issue?@action=redirect&bpo=12021).)

### multiprocessing[¶](#multiprocessing)

The new [ multiprocessing.connection.wait()](../library/multiprocessing.html#multiprocessing.connection.wait) function allows polling
multiple objects (such as connections, sockets and pipes) with a timeout.
(Contributed by Richard Oudkerk in 

[bpo-12328](https://bugs.python.org/issue?@action=redirect&bpo=12328).)

[ multiprocessing.connection.Connection](../library/multiprocessing.html#multiprocessing.connection.Connection) objects can now be transferred
over multiprocessing connections.
(Contributed by Richard Oudkerk in 

[bpo-4892](https://bugs.python.org/issue?@action=redirect&bpo=4892).)

[ multiprocessing.Process](../library/multiprocessing.html#multiprocessing.Process) now accepts a 

`daemon` keyword argument
to override the default behavior of inheriting the `daemon` flag from
the parent process ([bpo-6064](https://bugs.python.org/issue?@action=redirect&bpo=6064)).

New attribute [ multiprocessing.Process.sentinel](../library/multiprocessing.html#multiprocessing.Process.sentinel) allows a
program to wait on multiple 

[objects at one time using the appropriate OS primitives (for example,](../library/multiprocessing.html#multiprocessing.Process)

`Process`[on posix systems).](../library/select.html#module-select)

`select`New methods [ multiprocessing.pool.Pool.starmap()](../library/multiprocessing.html#multiprocessing.pool.Pool.starmap) and

[provide](../library/multiprocessing.html#multiprocessing.pool.Pool.starmap_async)

`starmap_async()`[equivalents to the existing](../library/itertools.html#itertools.starmap)

`itertools.starmap()`[and](../library/multiprocessing.html#multiprocessing.pool.Pool.map)

`multiprocessing.pool.Pool.map()`[functions. (Contributed by Hynek Schlawack in](../library/multiprocessing.html#multiprocessing.pool.Pool.map_async)

`map_async()`[bpo-12708](https://bugs.python.org/issue?@action=redirect&bpo=12708).)

### nntplib[¶](#nntplib)

The `nntplib.NNTP` class now supports the context management protocol to
unconditionally consume [ socket.error](../library/socket.html#socket.error) exceptions and to close the NNTP
connection when done:

```
>>> from nntplib import NNTP
>>> with NNTP('news.gmane.org') as n:
...     n.group('gmane.comp.python.committers')
...
('211 1755 1 1755 gmane.comp.python.committers', 1755, 1, 1755, 'gmane.comp.python.committers')
>>>
```
(Contributed by Giampaolo Rodolà in [bpo-9795](https://bugs.python.org/issue?@action=redirect&bpo=9795).)

### os[¶](#os)

- The - `os`- `pipe2()`- `O_CLOEXEC`- `O_NONBLOCK`
- The - `os`- `sendfile()`- `sendfile()`can be used to efficiently copy data from a file on disk to a network socket, e.g. for downloading a file.- (Patch submitted by Ross Lagerwall and Giampaolo Rodolà in - [bpo-10882](https://bugs.python.org/issue?@action=redirect&bpo=10882).)
- To avoid race conditions like symlink attacks and issues with temporary files and directories, it is more reliable (and also faster) to manipulate file descriptors instead of file names. Python 3.3 enhances existing functions and introduces new functions to work on file descriptors ( - [bpo-4761](https://bugs.python.org/issue?@action=redirect&bpo=4761),- [bpo-10755](https://bugs.python.org/issue?@action=redirect&bpo=10755)and- [bpo-14626](https://bugs.python.org/issue?@action=redirect&bpo=14626)).- The - `os`- `fwalk()`- `walk()`
- The following functions get new optional - *dir_fd*(- [paths relative to directory descriptors](../library/os.html#dir-fd)) and/or- *follow_symlinks*(- [not following symlinks](../library/os.html#follow-symlinks)):- `access()`- `chflags()`- `chmod()`- `chown()`- `link()`- `lstat()`- `mkdir()`- `mkfifo()`- `mknod()`- `open()`- `readlink()`- `remove()`- `rename()`- `replace()`- `rmdir()`- `stat()`- `symlink()`- `unlink()`- `utime()`- `os.supports_dir_fd`- `os.supports_follow_symlinks`
- The following functions now support a file descriptor for their path argument: - `chdir()`- `chmod()`- `chown()`- `execve()`- `listdir()`- `pathconf()`- `exists()`- `stat()`- `statvfs()`- `utime()`- `os.supports_fd`
 
- `access()`- `effective_ids`keyword argument to turn on using the effective uid/gid rather than the real uid/gid in the access check. Platform support for this can be checked via the- `supports_effective_ids`
- The - `os`- `getpriority()`- `setpriority()`- `os.nice()`- (Patch submitted by Giampaolo Rodolà in - [bpo-10784](https://bugs.python.org/issue?@action=redirect&bpo=10784).)
- The new - `os.replace()`- `os.rename()`- [bpo-8828](https://bugs.python.org/issue?@action=redirect&bpo=8828).)
- The stat family of functions ( - `stat()`- `fstat()`- `lstat()`- `utime()`- [bpo-14127](https://bugs.python.org/issue?@action=redirect&bpo=14127).)
- The new - `os.get_terminal_size()`- `shutil.get_terminal_size()`- [bpo-13609](https://bugs.python.org/issue?@action=redirect&bpo=13609).)

- New functions to support Linux extended attributes ( - [bpo-12720](https://bugs.python.org/issue?@action=redirect&bpo=12720)):- `getxattr()`- `listxattr()`- `removexattr()`- `setxattr()`
- New interface to the scheduler. These functions control how a process is allocated CPU time by the operating system. New functions: - `sched_get_priority_max()`- `sched_get_priority_min()`- `sched_getaffinity()`- `sched_getparam()`- `sched_getscheduler()`- `sched_rr_get_interval()`- `sched_setaffinity()`- `sched_setparam()`- `sched_setscheduler()`- `sched_yield()`
- New functions to control the file system: - `posix_fadvise()`
- `posix_fallocate()`
- `sync()`
 
- Additional new posix functions: - `lockf()`
- `pread()`
- `pwrite()`
- `readv()`
- `truncate()`- *path*, so that it is at most- *length*bytes in size.
- `waitid()`
- `writev()`- *buffers*to a file descriptor, where- *buffers*is an arbitrary sequence of buffers.
- `getgrouplist()`- [bpo-9344](https://bugs.python.org/issue?@action=redirect&bpo=9344)): Return list of group ids that specified user belongs to.
 
- `times()`- `uname()`
- Some platforms now support additional constants for the - `lseek()`- `os.SEEK_HOLE`and- `os.SEEK_DATA`.
- New constants - `RTLD_LAZY`- `RTLD_NOW`- `RTLD_GLOBAL`- `RTLD_LOCAL`- `RTLD_NODELETE`- `RTLD_NOLOAD`- `RTLD_DEEPBIND`- `sys.setdlopenflags()`- `ctypes`- `DLFCN`. (Contributed by Victor Stinner in- [bpo-13226](https://bugs.python.org/issue?@action=redirect&bpo=13226).)
- `os.symlink()`- `target_is_directory`keyword argument on non-Windows platforms, to ease cross-platform support.

### pdb[¶](#pdb)

Tab-completion is now available not only for command names, but also their
arguments.  For example, for the `break` command, function and file names
are completed.

(Contributed by Georg Brandl in [bpo-14210](https://bugs.python.org/issue?@action=redirect&bpo=14210))

### pickle[¶](#pickle)

[ pickle.Pickler](../library/pickle.html#pickle.Pickler) objects now have an optional

[attribute allowing per-pickler reduction functions to be set.](../library/pickle.html#pickle.Pickler.dispatch_table)

`dispatch_table`(Contributed by Richard Oudkerk in [bpo-14166](https://bugs.python.org/issue?@action=redirect&bpo=14166).)

### pydoc[¶](#pydoc)

The Tk GUI and the `serve()` function have been removed from the
[ pydoc](../library/pydoc.html#module-pydoc) module: 

`pydoc -g` and `serve()` have been deprecated
in Python 3.2.### re[¶](#re)

[ str](../library/stdtypes.html#str) regular expressions now support 

`\u` and `\U` escapes.(Contributed by Serhiy Storchaka in [bpo-3665](https://bugs.python.org/issue?@action=redirect&bpo=3665).)

### sched[¶](#sched)

- `run()`- *blocking*parameter which when set to false makes the method execute the scheduled events due to expire soonest (if any) and then return immediately. This is useful in case you want to use the- `scheduler`- [bpo-13449](https://bugs.python.org/issue?@action=redirect&bpo=13449).)
- `scheduler`- [bpo-8684](https://bugs.python.org/issue?@action=redirect&bpo=8684).)
- *timefunc*and- *delayfunct*parameters of- `scheduler`- `time.time()`- `time.sleep()`- [bpo-13245](https://bugs.python.org/issue?@action=redirect&bpo=13245).)
- `enter()`- `enterabs()`- *argument*parameter is now optional. (Contributed by Chris Clark in- [bpo-13245](https://bugs.python.org/issue?@action=redirect&bpo=13245).)
- `enter()`- `enterabs()`- *kwargs*parameter. (Contributed by Chris Clark in- [bpo-13245](https://bugs.python.org/issue?@action=redirect&bpo=13245).)

### select[¶](#select)

Solaris and derivative platforms have a new class [ select.devpoll](../library/select.html#select.devpoll)
for high performance asynchronous sockets via 

`/dev/poll`.
(Contributed by Jesús Cea Avión in [bpo-6397](https://bugs.python.org/issue?@action=redirect&bpo=6397).)

### shlex[¶](#shlex)

The previously undocumented helper function `quote` from the
`pipes` modules has been moved to the [ shlex](../library/shlex.html#module-shlex) module and
documented.  

[properly escapes all characters in a string that might be otherwise given special meaning by the shell.](../library/shlex.html#shlex.quote)

`quote()`### shutil[¶](#shutil)

- New functions: - `disk_usage()`- [bpo-12442](https://bugs.python.org/issue?@action=redirect&bpo=12442).)
- `chown()`- [bpo-12191](https://bugs.python.org/issue?@action=redirect&bpo=12191).)
- `shutil.get_terminal_size()`- [bpo-13609](https://bugs.python.org/issue?@action=redirect&bpo=13609).)
 
- `copy2()`- `copystat()`- [bpo-14127](https://bugs.python.org/issue?@action=redirect&bpo=14127)and- [bpo-15238](https://bugs.python.org/issue?@action=redirect&bpo=15238).)
- Several functions now take an optional - `symlinks`argument: when that parameter is true, symlinks aren’t dereferenced and the operation instead acts on the symlink itself (or creates one, if relevant). (Contributed by Hynek Schlawack in- [bpo-12715](https://bugs.python.org/issue?@action=redirect&bpo=12715).)
- When copying files to a different file system, - `move()`- `mv`command does, recreating the symlink rather than copying the target file contents. (Contributed by Jonathan Niehof in- [bpo-9993](https://bugs.python.org/issue?@action=redirect&bpo=9993).)- `move()`now also returns the- `dst`argument as its result.
- `rmtree()`- `dir_fd`parameter in- `os.open()`- `os.unlink()`- [bpo-4489](https://bugs.python.org/issue?@action=redirect&bpo=4489).)

### signal[¶](#signal)

- The - `signal`- `pthread_sigmask()`- [bpo-8407](https://bugs.python.org/issue?@action=redirect&bpo=8407));
- `pthread_kill()`
- `sigpending()`
- `sigwait()`
- `sigwaitinfo()`
- `sigtimedwait()`- `sigwaitinfo()`
 
- The signal handler writes the signal number as a single byte instead of a nul byte into the wakeup file descriptor. So it is possible to wait more than one signal and know which signals were raised. 
- `signal.signal()`- `signal.siginterrupt()`

### smtpd[¶](#smtpd)

The `smtpd` module now supports [ RFC 5321](https://datatracker.ietf.org/doc/html/rfc5321.html) (extended SMTP) and 

[(size extension). Per the standard, these extensions are enabled if and only if the client initiates the session with an](https://datatracker.ietf.org/doc/html/rfc1870.html)

**RFC 1870**`EHLO` command.(Initial `ELHO` support by Alberto Trevino.  Size extension by Juhana
Jauhiainen.  Substantial additional work on the patch contributed by Michele
Orrù and Dan Boswell.  [bpo-8739](https://bugs.python.org/issue?@action=redirect&bpo=8739))

### smtplib[¶](#smtplib)

The [ SMTP](../library/smtplib.html#smtplib.SMTP), 

[, and](../library/smtplib.html#smtplib.SMTP_SSL)

`SMTP_SSL`[classes now accept a](../library/smtplib.html#smtplib.LMTP)

`LMTP``source_address` keyword argument
to specify the `(host, port)` to use as the source address in the bind call
when creating the outgoing socket.  (Contributed by Paulo Scardine in
[bpo-11281](https://bugs.python.org/issue?@action=redirect&bpo=11281).)

[ SMTP](../library/smtplib.html#smtplib.SMTP) now supports the context management protocol, allowing an

`SMTP` instance to be used in a `with` statement.  (Contributed
by Giampaolo Rodolà in [bpo-11289](https://bugs.python.org/issue?@action=redirect&bpo=11289).)

The [ SMTP_SSL](../library/smtplib.html#smtplib.SMTP_SSL) constructor and the 

[method now accept an SSLContext parameter to control parameters of the secure channel. (Contributed by Kasun Herath in](../library/smtplib.html#smtplib.SMTP.starttls)

`starttls()`[bpo-8809](https://bugs.python.org/issue?@action=redirect&bpo=8809).)

### socket[¶](#socket)

- The - `socket`- (Contributed by David Watson in - [bpo-6560](https://bugs.python.org/issue?@action=redirect&bpo=6560), based on an earlier patch by Heiko Wundram)
- The - `socket`- [https://en.wikipedia.org/wiki/Socketcan](https://en.wikipedia.org/wiki/Socketcan)), on Linux (- [https://lwn.net/Articles/253425](https://lwn.net/Articles/253425)).- (Contributed by Matthias Fuchs, updated by Tiago Gonçalves in - [bpo-10141](https://bugs.python.org/issue?@action=redirect&bpo=10141).)
- The - `socket`- [https://en.wikipedia.org/wiki/Reliable_Datagram_Sockets](https://en.wikipedia.org/wiki/Reliable_Datagram_Sockets)and- [https://oss.oracle.com/projects/rds](https://web.archive.org/web/20130115155505/https://oss.oracle.com/projects/rds/)).
- The - `socket`- `PF_SYSTEM`protocol family on OS X. (Contributed by Michael Goderbauer in- [bpo-13777](https://bugs.python.org/issue?@action=redirect&bpo=13777).)
- New function - `sethostname()`- [bpo-10866](https://bugs.python.org/issue?@action=redirect&bpo=10866).)

### socketserver[¶](#socketserver)

[ BaseServer](../library/socketserver.html#socketserver.BaseServer) now has an overridable method

[that is called by the](../library/socketserver.html#socketserver.BaseServer.service_actions)

`service_actions()`[method in the service loop.](../library/socketserver.html#socketserver.BaseServer.serve_forever)

`serve_forever()`[now uses this to clean up zombie child processes. (Contributed by Justin Warkentin in](../library/socketserver.html#socketserver.ForkingMixIn)

`ForkingMixIn`[bpo-11109](https://bugs.python.org/issue?@action=redirect&bpo=11109).)

### sqlite3[¶](#sqlite3)

New [ sqlite3.Connection](../library/sqlite3.html#sqlite3.Connection) method

[can be used to capture a trace of all sql commands processed by sqlite. (Contributed by Torsten Landschoff in](../library/sqlite3.html#sqlite3.Connection.set_trace_callback)

`set_trace_callback()`[bpo-11688](https://bugs.python.org/issue?@action=redirect&bpo=11688).)

### ssl[¶](#ssl)

- The - `ssl`- `RAND_bytes()`
- `RAND_pseudo_bytes()`: generate pseudo-random bytes.
 - (Contributed by Victor Stinner in - [bpo-12049](https://bugs.python.org/issue?@action=redirect&bpo=12049).)
- The - `ssl`- [bpo-11183](https://bugs.python.org/issue?@action=redirect&bpo=11183).)
- `load_cert_chain()`- *password*argument to be used if the private key is encrypted. (Contributed by Adam Simpkins in- [bpo-12803](https://bugs.python.org/issue?@action=redirect&bpo=12803).)
- Diffie-Hellman key exchange, both regular and Elliptic Curve-based, is now supported through the - `load_dh_params()`- `set_ecdh_curve()`- [bpo-13626](https://bugs.python.org/issue?@action=redirect&bpo=13626)and- [bpo-13627](https://bugs.python.org/issue?@action=redirect&bpo=13627).)
- SSL sockets have a new - `get_channel_binding()`- [bpo-12551](https://bugs.python.org/issue?@action=redirect&bpo=12551).)
- You can query the SSL compression algorithm used by an SSL socket, thanks to its new - `compression()`- `OP_NO_COMPRESSION`- [bpo-13634](https://bugs.python.org/issue?@action=redirect&bpo=13634).)
- Support has been added for the Next Protocol Negotiation extension using the - `ssl.SSLContext.set_npn_protocols()`- [bpo-14204](https://bugs.python.org/issue?@action=redirect&bpo=14204).)
- SSL errors can now be introspected more easily thanks to - `library`- `reason`- [bpo-14837](https://bugs.python.org/issue?@action=redirect&bpo=14837).)
- The - `get_server_certificate()`- [bpo-11811](https://bugs.python.org/issue?@action=redirect&bpo=11811).)
- New attribute - `OP_CIPHER_SERVER_PREFERENCE`- [bpo-13635](https://bugs.python.org/issue?@action=redirect&bpo=13635)).

### stat[¶](#stat)

The undocumented tarfile.filemode function has been moved to
[ stat.filemode()](../library/stat.html#stat.filemode). It can be used to convert a file’s mode to a string of
the form ‘-rwxrwxrwx’.

(Contributed by Giampaolo Rodolà in [bpo-14807](https://bugs.python.org/issue?@action=redirect&bpo=14807).)

### struct[¶](#struct)

The [ struct](../library/struct.html#module-struct) module now supports 

`ssize_t` and `size_t` via the
new codes `n` and `N`, respectively.  (Contributed by Antoine Pitrou
in [bpo-3163](https://bugs.python.org/issue?@action=redirect&bpo=3163).)

### subprocess[¶](#subprocess)

Command strings can now be bytes objects on posix platforms.  (Contributed by
Victor Stinner in [bpo-8513](https://bugs.python.org/issue?@action=redirect&bpo=8513).)

A new constant [ DEVNULL](../library/subprocess.html#subprocess.DEVNULL) allows suppressing output in a
platform-independent fashion.  (Contributed by Ross Lagerwall in

[bpo-5870](https://bugs.python.org/issue?@action=redirect&bpo=5870).)

### sys[¶](#sys)

The [ sys](../library/sys.html#module-sys) module has a new 


`thread_info`[named tuple](../glossary.html#term-named-tuple)holding information about the thread implementation (

[bpo-11223](https://bugs.python.org/issue?@action=redirect&bpo=11223)).

### tarfile[¶](#tarfile)

[ tarfile](../library/tarfile.html#module-tarfile) now supports 

`lzma` encoding via the [module. (Contributed by Lars Gustäbel in](../library/lzma.html#module-lzma)

`lzma`[bpo-5689](https://bugs.python.org/issue?@action=redirect&bpo=5689).)

### tempfile[¶](#tempfile)

[ tempfile.SpooledTemporaryFile](../library/tempfile.html#tempfile.SpooledTemporaryFile)'s 

`truncate()` method now accepts
a `size` parameter.  (Contributed by Ryan Kelly in [bpo-9957](https://bugs.python.org/issue?@action=redirect&bpo=9957).)

### textwrap[¶](#textwrap)

The [ textwrap](../library/textwrap.html#module-textwrap) module has a new 

[that makes it straightforward to add a common prefix to selected lines in a block of text (](../library/textwrap.html#textwrap.indent)

`indent()`[bpo-13857](https://bugs.python.org/issue?@action=redirect&bpo=13857)).

### threading[¶](#threading)

[ threading.Condition](../library/threading.html#threading.Condition), 

[,](../library/threading.html#threading.Semaphore)

`threading.Semaphore`[,](../library/threading.html#threading.BoundedSemaphore)

`threading.BoundedSemaphore`[, and](../library/threading.html#threading.Event)

`threading.Event`[, all of which used to be factory functions returning a class instance, are now classes and may be subclassed. (Contributed by Éric Araujo in](../library/threading.html#threading.Timer)

`threading.Timer`[bpo-10968](https://bugs.python.org/issue?@action=redirect&bpo=10968).)

The [ threading.Thread](../library/threading.html#threading.Thread) constructor now accepts a 

`daemon` keyword
argument to override the default behavior of inheriting the `daemon` flag
value from the parent thread ([bpo-6064](https://bugs.python.org/issue?@action=redirect&bpo=6064)).

The formerly private function `_thread.get_ident` is now available as the
public function [ threading.get_ident()](../library/threading.html#threading.get_ident).  This eliminates several cases of
direct access to the 

`_thread` module in the stdlib.  Third party code that
used `_thread.get_ident` should likewise be changed to use the new public
interface.### time[¶](#time)

The [ PEP 418](https://peps.python.org/pep-0418/) added new functions to the 

[module:](../library/time.html#module-time)

`time`- `get_clock_info()`
- `monotonic()`
- `perf_counter()`
- `process_time()`

Other new functions:

- `clock_getres()`- `clock_gettime()`- `clock_settime()`- `CLOCK_`constants. (Contributed by Victor Stinner in- *xxx*- [bpo-10278](https://bugs.python.org/issue?@action=redirect&bpo=10278).)

To improve cross platform consistency, [ sleep()](../library/time.html#time.sleep) now raises a

[when passed a negative sleep value. Previously this was an error on posix, but produced an infinite sleep on Windows.](../library/exceptions.html#ValueError)

`ValueError`### types[¶](#types)

Add a new [ types.MappingProxyType](../library/types.html#types.MappingProxyType) class: Read-only proxy of a mapping.
(

[bpo-14386](https://bugs.python.org/issue?@action=redirect&bpo=14386))

The new functions [ types.new_class()](../library/types.html#types.new_class) and 

[provide support for](../library/types.html#types.prepare_class)

`types.prepare_class()`[compliant dynamic type creation. (](https://peps.python.org/pep-3115/)

**PEP 3115**[bpo-14588](https://bugs.python.org/issue?@action=redirect&bpo=14588))

### unittest[¶](#unittest)

[ assertRaises()](../library/unittest.html#unittest.TestCase.assertRaises), 

[,](../library/unittest.html#unittest.TestCase.assertRaisesRegex)

`assertRaisesRegex()`[, and](../library/unittest.html#unittest.TestCase.assertWarns)

`assertWarns()`[now accept a keyword argument](../library/unittest.html#unittest.TestCase.assertWarnsRegex)

`assertWarnsRegex()`*msg*when used as context managers. (Contributed by Ezio Melotti and Winston Ewert in

[bpo-10775](https://bugs.python.org/issue?@action=redirect&bpo=10775).)

[ unittest.TestCase.run()](../library/unittest.html#unittest.TestCase.run) now returns the 

[object.](../library/unittest.html#unittest.TestResult)

`TestResult`### urllib[¶](#urllib)

The [ Request](../library/urllib.request.html#urllib.request.Request) class, now accepts a 

*method*argument used by

[to determine what HTTP method should be used. For example, this will send a](../library/urllib.request.html#urllib.request.Request.get_method)

`get_method()``'HEAD'` request:```
>>> urlopen(Request('https://www.python.org', method='HEAD'))
```
### webbrowser[¶](#webbrowser)

The [ webbrowser](../library/webbrowser.html#module-webbrowser) module supports more “browsers”: Google Chrome (named

**chrome**,

**chromium**,

**chrome-browser**or

**chromium-browser**depending on the version and operating system), and the generic launchers

**xdg-open**, from the FreeDesktop.org project, and

**gvfs-open**, which is the default URI handler for GNOME 3. (The former contributed by Arnaud Calmettes in

[bpo-13620](https://bugs.python.org/issue?@action=redirect&bpo=13620), the latter by Matthias Klose in

[bpo-14493](https://bugs.python.org/issue?@action=redirect&bpo=14493).)

### xml.etree.ElementTree[¶](#xml-etree-elementtree)

The [ xml.etree.ElementTree](../library/xml.etree.elementtree.html#module-xml.etree.ElementTree) module now imports its C accelerator by
default; there is no longer a need to explicitly import

`xml.etree.cElementTree` (this module stays for backwards compatibility,
but is now deprecated).  In addition,  the `iter` family of methods of
[has been optimized (rewritten in C). The module’s documentation has also been greatly improved with added examples and a more detailed reference.](../library/xml.etree.elementtree.html#xml.etree.ElementTree.Element)

`Element`### zlib[¶](#zlib)

New attribute [ zlib.Decompress.eof](../library/zlib.html#zlib.Decompress.eof) makes it possible to distinguish
between a properly formed compressed stream and an incomplete or truncated one.
(Contributed by Nadeem Vawda in 

[bpo-12646](https://bugs.python.org/issue?@action=redirect&bpo=12646).)

New attribute [ zlib.ZLIB_RUNTIME_VERSION](../library/zlib.html#zlib.ZLIB_RUNTIME_VERSION) reports the version string of
the underlying 

`zlib` library that is loaded at runtime.  (Contributed by
Torsten Landschoff in [bpo-12306](https://bugs.python.org/issue?@action=redirect&bpo=12306).)

## Optimizations[¶](#optimizations)

Major performance enhancements have been added:

- Thanks to - **PEP 393**- the memory footprint is divided by 2 to 4 depending on the text 
- encode an ASCII string to UTF-8 doesn’t need to encode characters anymore, the UTF-8 representation is shared with the ASCII representation 
- the UTF-8 encoder has been optimized 
- repeating a single ASCII letter and getting a substring of an ASCII string is 4 times faster 
 
- UTF-8 is now 2x to 4x faster. UTF-16 encoding is now up to 10x faster. - (Contributed by Serhiy Storchaka, - [bpo-14624](https://bugs.python.org/issue?@action=redirect&bpo=14624),- [bpo-14738](https://bugs.python.org/issue?@action=redirect&bpo=14738)and- [bpo-15026](https://bugs.python.org/issue?@action=redirect&bpo=15026).)

## Build and C API Changes[¶](#build-and-c-api-changes)

Changes to Python’s build process and to the C API include:

- New - **PEP 3118**
- **PEP 393**- High-level API: 
- Low-level API: 
- `PyASCIIObject`- `PyCompactUnicodeObject`
- `PyUnicode_DATA`- `PyUnicode_1BYTE_DATA`- `PyUnicode_2BYTE_DATA`- `PyUnicode_4BYTE_DATA`
- `PyUnicode_KIND`- `PyUnicode_Kind`enum:- `PyUnicode_WCHAR_KIND`,- `PyUnicode_1BYTE_KIND`- `PyUnicode_2BYTE_KIND`- `PyUnicode_4BYTE_KIND`
 
 
- `PyArg_ParseTuple`- `bytearray`- `c`format (- [bpo-12380](https://bugs.python.org/issue?@action=redirect&bpo=12380)).

## Deprecated[¶](#deprecated)

### Unsupported Operating Systems[¶](#unsupported-operating-systems)

OS/2 and VMS are no longer supported due to the lack of a maintainer.

Windows 2000 and Windows platforms which set `COMSPEC` to `command.com`
are no longer supported due to maintenance burden.

OSF support, which was deprecated in 3.2, has been completely removed.

### Deprecated Python modules, functions and methods[¶](#deprecated-python-modules-functions-and-methods)

- Passing a non-empty string to - `object.__format__()`is deprecated, and will produce a- `TypeError`- [bpo-9856](https://bugs.python.org/issue?@action=redirect&bpo=9856)).
- The - `unicode_internal`codec has been deprecated because of the- **PEP 393**- `utf-16-le`or- `utf-16-be`), or UTF-32 (- `utf-32-le`or- `utf-32-be`)
- `ftplib.FTP.nlst()`- `ftplib.FTP.dir()`- `ftplib.FTP.mlsd()`
- `platform.popen()`: use the- `subprocess`- [Replacing Older Functions with the subprocess Module](../library/subprocess.html#subprocess-replacements)section (- [bpo-11377](https://bugs.python.org/issue?@action=redirect&bpo=11377)).
- [bpo-13374](https://bugs.python.org/issue?@action=redirect&bpo=13374): The Windows bytes API has been deprecated in the- `os`
- [bpo-13988](https://bugs.python.org/issue?@action=redirect&bpo=13988): The- `xml.etree.cElementTree`module is deprecated. The accelerator is used automatically whenever available.
- The behaviour of - `time.clock()`depends on the platform: use the new- `time.perf_counter()`- `time.process_time()`
- The - `os.stat_float_times()`function is deprecated.
- `abc`- `abc.abstractproperty`- `property`- `abc.abstractmethod()`
- `abc.abstractclassmethod`- `classmethod`- `abc.abstractmethod()`
- `abc.abstractstaticmethod`- `staticmethod`- `abc.abstractmethod()`
 
- `importlib`- `importlib.abc.SourceLoader.path_mtime()`- `importlib.abc.SourceLoader.path_stats()`
 

### Deprecated functions and types of the C API[¶](#deprecated-functions-and-types-of-the-c-api)

The [ Py_UNICODE](../c-api/unicode.html#c.Py_UNICODE) has been deprecated by 

[and will be removed in Python 4. All functions using this type are deprecated:](https://peps.python.org/pep-0393/)

**PEP 393**Unicode functions and methods using [ Py_UNICODE](../c-api/unicode.html#c.Py_UNICODE) and

[Py_UNICODE](../c-api/unicode.html#c.Py_UNICODE)* types:

- `PyUnicode_FromUnicode`: use- `PyUnicode_FromWideChar()`- `PyUnicode_FromKindAndData()`
- `PyUnicode_AS_UNICODE`,- `PyUnicode_AsUnicode()`,- `PyUnicode_AsUnicodeAndSize()`: use- `PyUnicode_AsWideCharString()`
- `PyUnicode_AS_DATA`: use- `PyUnicode_DATA`- `PyUnicode_READ`- `PyUnicode_WRITE`
- `PyUnicode_GET_SIZE`,- `PyUnicode_GetSize()`: use- `PyUnicode_GET_LENGTH`- `PyUnicode_GetLength()`
- `PyUnicode_GET_DATA_SIZE`: use- `PyUnicode_GET_LENGTH(str) * PyUnicode_KIND(str)`(only work on ready strings)
- `PyUnicode_AsUnicodeCopy()`: use- `PyUnicode_AsUCS4Copy()`- `PyUnicode_AsWideCharString()`
- `PyUnicode_GetMax()`

Functions and macros manipulating Py_UNICODE* strings:

- `Py_UNICODE_strlen()`: use- `PyUnicode_GetLength()`- `PyUnicode_GET_LENGTH`
- `Py_UNICODE_strcat()`: use- `PyUnicode_CopyCharacters()`- `PyUnicode_FromFormat()`
- `Py_UNICODE_strcpy()`,- `Py_UNICODE_strncpy()`,- `Py_UNICODE_COPY()`: use- `PyUnicode_CopyCharacters()`- `PyUnicode_Substring()`
- `Py_UNICODE_strcmp()`: use- `PyUnicode_Compare()`
- `Py_UNICODE_strncmp()`: use- `PyUnicode_Tailmatch()`
- `Py_UNICODE_strchr()`,- `Py_UNICODE_strrchr()`: use- `PyUnicode_FindChar()`
- `Py_UNICODE_FILL()`: use- `PyUnicode_Fill()`
- `Py_UNICODE_MATCH`

Encoders:

- `PyUnicode_Encode()`: use- `PyUnicode_AsEncodedObject()`
- `PyUnicode_EncodeUTF7()`
- `PyUnicode_EncodeUTF8()`: use- `PyUnicode_AsUTF8()`- `PyUnicode_AsUTF8String()`
- `PyUnicode_EncodeUTF32()`
- `PyUnicode_EncodeUTF16()`
- `PyUnicode_EncodeUnicodeEscape()`use- `PyUnicode_AsUnicodeEscapeString()`
- `PyUnicode_EncodeRawUnicodeEscape()`use- `PyUnicode_AsRawUnicodeEscapeString()`
- `PyUnicode_EncodeLatin1()`: use- `PyUnicode_AsLatin1String()`
- `PyUnicode_EncodeASCII()`: use- `PyUnicode_AsASCIIString()`
- `PyUnicode_EncodeCharmap()`
- `PyUnicode_TranslateCharmap()`
- `PyUnicode_EncodeMBCS()`: use- `PyUnicode_AsMBCSString()`- `PyUnicode_EncodeCodePage()`- `CP_ACP`code_page)
- `PyUnicode_EncodeDecimal()`,- `PyUnicode_TransformDecimalToASCII()`

### Deprecated features[¶](#deprecated-features)

The [ array](../library/array.html#module-array) module’s 

`'u'` format code is now deprecated and will be
removed in Python 4 together with the rest of the ([) API.](../c-api/unicode.html#c.Py_UNICODE)

`Py_UNICODE`## Porting to Python 3.3[¶](#porting-to-python-3-3)

This section lists previously described changes and other bugfixes that may require changes to your code.

### Porting Python code[¶](#porting-python-code)

- Hash randomization is enabled by default. Set the - `PYTHONHASHSEED`- `0`to disable hash randomization. See also the- `object.__hash__()`
- [bpo-12326](https://bugs.python.org/issue?@action=redirect&bpo=12326): On Linux, sys.platform doesn’t contain the major version anymore. It is now always ‘linux’, instead of ‘linux2’ or ‘linux3’ depending on the Linux version used to build Python. Replace sys.platform == ‘linux2’ with sys.platform.startswith(‘linux’), or directly sys.platform == ‘linux’ if you don’t need to support older Python versions.
- [bpo-13847](https://bugs.python.org/issue?@action=redirect&bpo=13847),- [bpo-14180](https://bugs.python.org/issue?@action=redirect&bpo=14180):- `time`- `datetime`- `OverflowError`- `ValueError`- `OSError`- `gmtime()`or- `localtime()`failed.
- The default finders used by import now utilize a cache of what is contained within a specific directory. If you create a Python source file or sourceless bytecode file, make sure to call - `importlib.invalidate_caches()`
- `ImportError`
- The - *index*argument to- `__import__()`- **PEP 328**- `importlib.import_module()`- `__import__()`directly.
- `__import__()`- `__import__('sys', level=1)`is now an error.
- Because - `sys.meta_path`- `sys.path_hooks`- `list.insert()`- `list.append()`
- Because - `None`is now inserted into- `sys.path_importer_cache`- `None`- **and**- `imp.NullImporter`to be backwards-compatible. This will lead to extra overhead on older versions of Python that re-insert- `None`into- `sys.path_importer_cache`where it represents the use of implicit finders, but semantically it should not change anything.
- `importlib.abc.Finder`no longer specifies a- `find_module()`abstract method that must be implemented. If you were relying on subclasses to implement that method, make sure to check for the method’s existence first. You will probably want to check for- `find_loader()`first, though, in the case of working with- [path entry finders](../glossary.html#term-path-entry-finder).
- `pkgutil`- `importlib`- **PEP 302**- `pkgutil.iter_importers()`- `pkgutil.walk_packages()`- `iter_modules()`method.
- A longstanding RFC-compliance bug ( - [bpo-1079](https://bugs.python.org/issue?@action=redirect&bpo=1079)) in the parsing done by- `email.header.decode_header()`- `str(make_header(decode_header(h))`) will see no change, but code that looks at the individual tuples returned by decode_header will see that whitespace that precedes or follows- `ASCII`sections is now included in the- `ASCII`section. Code that builds headers using- `make_header`should also continue to work without change, since- `make_header`continues to add whitespace between- `ASCII`and non-- `ASCII`sections if it is not already present in the input strings.
- `email.utils.formataddr()`- `ASCII`display names. Any code that depended on the previous buggy behavior that preserved the non-- `ASCII`unicode in the formatted output string will need to be changed (- [bpo-1690608](https://bugs.python.org/issue?@action=redirect&bpo=1690608)).
- `poplib.POP3.quit()`- `poplib`methods. Code that assumes- `quit`does not raise- `poplib.error_proto`- `quit`are encountered by a particular application (- [bpo-11291](https://bugs.python.org/issue?@action=redirect&bpo=11291)).
- The - `strict`argument to- `email.parser.Parser`
- The deprecated method - `unittest.TestCase.assertSameElements`has been removed.
- The deprecated variable - `time.accept2dyear`has been removed.
- The deprecated - `Context._clamp`attribute has been removed from the- `decimal`- `clamp`- [bpo-8540](https://bugs.python.org/issue?@action=redirect&bpo=8540).)
- The undocumented internal helper class - `SSLFakeFile`has been removed from- `smtplib`- `socket.socket.makefile()`
- Passing a negative value to - `time.sleep()`
- The - `ast.__version__`constant has been removed. If you need to make decisions affected by the AST version, use- `sys.version_info`
- Code that used to work around the fact that the - `threading`
- The undocumented debugging machinery in the threading module has been removed, simplifying the code. This should have no effect on production code, but is mentioned here in case any application debug frameworks were interacting with it ( - [bpo-13550](https://bugs.python.org/issue?@action=redirect&bpo=13550)).

### Porting C code[¶](#porting-c-code)

- In the course of changes to the buffer API the undocumented - `smalltable`member of the- `Py_buffer`- `PyMemoryViewObject`has changed.- All extensions relying on the relevant parts in - `memoryobject.h`or- `object.h`must be rebuilt.
- Due to - [PEP 393](#pep-393), the- `Py_UNICODE`- **PEP 393**- [Unicode API](../c-api/unicode.html).- However, if you only have been using high-level functions such as - `PyUnicode_Concat()`- `PyUnicode_Join()`- `PyUnicode_FromFormat()`
- `PyImport_GetMagicNumber()`- `-1`upon failure.
- As a negative value for the - *level*argument to- `__import__()`- `PyImport_ImportModuleLevel()`- *level*used by- `PyImport_ImportModuleEx()`- `0`instead of- `-1`.

### Building C extensions[¶](#building-c-extensions)

- The range of possible file names for C extensions has been narrowed. Very rarely used spellings have been suppressed: under POSIX, files named - `xxxmodule.so`,- `xxxmodule.abi3.so`and- `xxxmodule.cpython-*.so`are no longer recognized as implementing the- `xxx`module. If you had been generating such files, you have to switch to the other spellings (i.e., remove the- `module`string from the file names).- (implemented in - [bpo-14040](https://bugs.python.org/issue?@action=redirect&bpo=14040).)

### Command Line Switch Changes[¶](#command-line-switch-changes)

- The -Q command-line flag and related artifacts have been removed. Code checking sys.flags.division_warning will need updating. - ( - [bpo-10998](https://bugs.python.org/issue?@action=redirect&bpo=10998), contributed by Éric Araujo.)
- When - **python**is started with- `-S`- `import site`will no longer add site-specific paths to the module search paths. In previous versions, it did.- ( - [bpo-11591](https://bugs.python.org/issue?@action=redirect&bpo=11591), contributed by Carl Meyer with editions by Éric Araujo.)