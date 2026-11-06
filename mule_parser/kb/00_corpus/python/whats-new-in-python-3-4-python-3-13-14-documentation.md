# What’s New In Python 3.4 — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/whatsnew/3.4.html](https://docs.python.org/3.13/whatsnew/3.4.html)

---

# What’s New In Python 3.4[¶](#what-s-new-in-python-3-4)

- Author:
- R. David Murray < - [rdmurray@bitdance.com](mailto:rdmurray%40bitdance.com)> (Editor)

This article explains the new features in Python 3.4, compared to 3.3.
Python 3.4 was released on March 16, 2014.  For full details, see the
[changelog](https://docs.python.org/3.4/whatsnew/changelog.html).

See also

[ PEP 429](https://peps.python.org/pep-0429/) – Python 3.4 Release Schedule

## Summary – Release Highlights[¶](#summary-release-highlights)

New syntax features:

- No new syntax features were added in Python 3.4. 

Other new features:

- [Newly created file descriptors are non-inheritable](#whatsnew-pep-446)(- **PEP 446**
- command line option for - [isolated mode](#whatsnew-isolated-mode)(- [bpo-16499](https://bugs.python.org/issue?@action=redirect&bpo=16499)).
- [improvements in the handling of codecs](#codec-handling-improvements)that are not text encodings (multiple issues).
- [A ModuleSpec Type](#whatsnew-pep-451)for the Import System (- **PEP 451**
- The - `marshal`- [more compact and efficient](#whatsnew-marshal-3)(- [bpo-16475](https://bugs.python.org/issue?@action=redirect&bpo=16475)).

New library modules:

- `asyncio`- [New provisional API for asynchronous IO](#whatsnew-asyncio)(- **PEP 3156**
- `selectors`- [High-level and efficient I/O multiplexing](#whatsnew-selectors), built upon the- `select`- **PEP 3156**
- `statistics`- [numerically stable statistics library](#whatsnew-statistics)(- **PEP 450**

Significantly improved library modules:

- New - `pickle`- [protocol 4](#whatsnew-protocol-4)(- **PEP 3154**
- `multiprocessing`- [an option to avoid using os.fork on Unix](#whatsnew-multiprocessing-no-fork)(- [bpo-8713](https://bugs.python.org/issue?@action=redirect&bpo=8713)).
- `email`- `contentmanager`- `Message`- `EmailMessage`- [simplify MIME handling](#whatsnew-email-contentmanager)(- [bpo-18891](https://bugs.python.org/issue?@action=redirect&bpo=18891)).
- The - `inspect`- `pydoc`- `help()`
- The - `ipaddress`

Security improvements:

- [Make newly created file descriptors non-inheritable](#whatsnew-pep-446)(- **PEP 446**
- New command line option for - [isolated mode](#whatsnew-isolated-mode), (- [bpo-16499](https://bugs.python.org/issue?@action=redirect&bpo=16499)).
- `multiprocessing`- [an option to avoid using os.fork on Unix](#whatsnew-multiprocessing-no-fork).- *spawn*and- *forkserver*are more secure because they avoid sharing data with child processes.
- `multiprocessing`
- A new - `hashlib.pbkdf2_hmac()`- [PKCS#5 password-based key derivation function 2](https://en.wikipedia.org/wiki/PBKDF2).
- [Retrieving certificates from the Windows system cert store support](#whatsnew34-win-cert-store)for- `ssl`
- The - `ssl.SSLContext`- [lot of improvements](#whatsnew34-sslcontext).
- All modules in the standard library that support SSL now support server certificate verification, including hostname matching ( - `ssl.match_hostname()`) and CRLs (Certificate Revocation lists, see- `ssl.SSLContext.load_verify_locations()`

CPython implementation improvements:

- Leveraging - **PEP 442**- [module globals are no longer set to None during finalization](#whatsnew-pep-442)(- [bpo-18214](https://bugs.python.org/issue?@action=redirect&bpo=18214)).

Please read on for a comprehensive list of user-facing changes, including many other smaller improvements, CPython optimizations, deprecations, and potential porting issues.

## New Features[¶](#new-features)

### PEP 453: Explicit Bootstrapping of PIP in Python Installations[¶](#pep-453-explicit-bootstrapping-of-pip-in-python-installations)

#### Bootstrapping pip By Default[¶](#bootstrapping-pip-by-default)

The new [ ensurepip](../library/ensurepip.html#module-ensurepip) module (defined in 

[) provides a standard cross-platform mechanism to bootstrap the pip installer into Python installations and virtual environments. The version of](https://peps.python.org/pep-0453/)

**PEP 453**`pip` included
with Python 3.4.0 is `pip` 1.5.4, and future 3.4.x maintenance releases
will update the bundled version to the latest version of `pip` that is
available at the time of creating the release candidate.By default, the commands `pipX` and `pipX.Y` will be installed on all
platforms (where X.Y stands for the version of the Python installation),
along with the `pip` Python package and its dependencies. On Windows and
in virtual environments on all platforms, the unversioned `pip` command
will also be installed. On other platforms, the system wide unversioned
`pip` command typically refers to the separately installed Python 2
version.

The `pyvenv` command line utility and the [ venv](../library/venv.html#module-venv)
module make use of the 

[module to make](../library/ensurepip.html#module-ensurepip)

`ensurepip``pip` readily
available in virtual environments. When using the command line utility,
`pip` is installed by default, while when using the `venv` module
[API](../library/venv.html#venv-api)installation of

`pip` must be requested explicitly.For CPython [source builds on POSIX systems](../using/unix.html#building-python-on-unix),
the `make install` and `make altinstall` commands bootstrap `pip` by
default.  This behaviour can be controlled through configure options, and
overridden through Makefile options.

On Windows and Mac OS X, the CPython installers now default to installing
`pip` along with CPython itself (users may opt out of installing it
during the installation process). Window users will need to opt in to the
automatic `PATH` modifications to have `pip` available from the command
line by default, otherwise it can still be accessed through the Python
launcher for Windows as `py -m pip`.

As [ discussed in the PEP](https://peps.python.org/pep-0453/#recommendations-for-downstream-distributors)
platform packagers may choose not to install
these commands by default, as long as, when invoked, they provide clear and
simple directions on how to install them on that platform (usually using
the system package manager).

Note

To avoid conflicts between parallel Python 2 and Python 3 installations,
only the versioned `pip3` and `pip3.4` commands are bootstrapped by
default when `ensurepip` is invoked directly - the `--default-pip`
option is needed to also request the unversioned `pip` command.
`pyvenv` and the Windows installer ensure that the unqualified `pip`
command is made available in those environments, and `pip` can always be
invoked via the `-m` switch rather than directly to avoid ambiguity on
systems with multiple Python installations.

#### Documentation Changes[¶](#documentation-changes)

As part of this change, the [Installing Python modules](../installing/index.html#installing-index) and
[Distributing Python Modules](../distributing/index.html#distributing-index) sections of the documentation have been
completely redesigned as short getting started and FAQ documents. Most
packaging documentation has now been moved out to the Python Packaging
Authority maintained [Python Packaging User Guide](https://packaging.python.org) and the documentation of the individual
projects.

However, as this migration is currently still incomplete, the legacy
versions of those guides remaining available as [Building C and C++ Extensions with setuptools](../extending/building.html#install-index)
and [Building C and C++ Extensions with setuptools](../extending/building.html#setuptools-index).

See also

- **PEP 453**
- PEP written by Donald Stufft and Nick Coghlan, implemented by Donald Stufft, Nick Coghlan, Martin von Löwis and Ned Deily. 

### PEP 446: Newly Created File Descriptors Are Non-Inheritable[¶](#pep-446-newly-created-file-descriptors-are-non-inheritable)

[ PEP 446](https://peps.python.org/pep-0446/) makes newly created file descriptors 

[non-inheritable](../library/os.html#fd-inheritance). In general, this is the behavior an application will want: when launching a new process, having currently open files also open in the new process can lead to all sorts of hard to find bugs, and potentially to security issues.

However, there are occasions when inheritance is desired. To support these cases, the following new functions and methods are available:

See also

- **PEP 446**
- PEP written and implemented by Victor Stinner. 

### Improvements to Codec Handling[¶](#improvements-to-codec-handling)

Since it was first introduced, the [ codecs](../library/codecs.html#module-codecs) module has always been
intended to operate as a type-neutral dynamic encoding and decoding
system. However, its close coupling with the Python text model, especially
the type restricted convenience methods on the builtin 

[,](../library/stdtypes.html#str)

`str`[and](../library/stdtypes.html#bytes)

`bytes`[types, has historically obscured that fact.](../library/stdtypes.html#bytearray)

`bytearray`As a key step in clarifying the situation, the [ codecs.encode()](../library/codecs.html#codecs.encode) and

[convenience functions are now properly documented in Python 2.7, 3.3 and 3.4. These functions have existed in the](../library/codecs.html#codecs.decode)

`codecs.decode()`[module (and have been covered by the regression test suite) since Python 2.4, but were previously only discoverable through runtime introspection.](../library/codecs.html#module-codecs)

`codecs`Unlike the convenience methods on [ str](../library/stdtypes.html#str), 

[and](../library/stdtypes.html#bytes)

`bytes`[, the](../library/stdtypes.html#bytearray)

`bytearray`[convenience functions support arbitrary codecs in both Python 2 and Python 3, rather than being limited to Unicode text encodings (in Python 3) or](../library/codecs.html#module-codecs)

`codecs``basestring` <-> `basestring` conversions (in
Python 2).In Python 3.4, the interpreter is able to identify the known non-text encodings provided in the standard library and direct users towards these general purpose convenience functions when appropriate:

```
>>> b"abcdef".decode("hex")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
LookupError: 'hex' is not a text encoding; use codecs.decode() to handle arbitrary codecs
>>> "hello".encode("rot13")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
LookupError: 'rot13' is not a text encoding; use codecs.encode() to handle arbitrary codecs
>>> open("foo.txt", encoding="hex")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
LookupError: 'hex' is not a text encoding; use codecs.open() to handle arbitrary codecs
```
In a related change, whenever it is feasible without breaking backwards compatibility, exceptions raised during encoding and decoding operations are wrapped in a chained exception of the same type that mentions the name of the codec responsible for producing the error:

```
>>> import codecs
>>> codecs.decode(b"abcdefgh", "hex")
Traceback (most recent call last):
  File "/usr/lib/python3.4/encodings/hex_codec.py", line 20, in hex_decode
    return (binascii.a2b_hex(input), len(input))
binascii.Error: Non-hexadecimal digit found
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
binascii.Error: decoding with 'hex' codec failed (Error: Non-hexadecimal digit found)
>>> codecs.encode("hello", "bz2")
Traceback (most recent call last):
  File "/usr/lib/python3.4/encodings/bz2_codec.py", line 17, in bz2_encode
    return (bz2.compress(input), len(input))
  File "/usr/lib/python3.4/bz2.py", line 498, in compress
    return comp.compress(data) + comp.flush()
TypeError: 'str' does not support the buffer interface
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: encoding with 'bz2' codec failed (TypeError: 'str' does not support the buffer interface)
```
Finally, as the examples above show, these improvements have permitted the restoration of the convenience aliases for the non-Unicode codecs that were themselves restored in Python 3.2. This means that encoding binary data to and from its hexadecimal representation (for example) can now be written as:

```
>>> from codecs import encode, decode
>>> encode(b"hello", "hex")
b'68656c6c6f'
>>> decode(b"68656c6c6f", "hex")
b'hello'
```
The binary and text transforms provided in the standard library are detailed
in [Binary Transforms](../library/codecs.html#binary-transforms) and [Text Transforms](../library/codecs.html#text-transforms).

(Contributed by Nick Coghlan in [bpo-7475](https://bugs.python.org/issue?@action=redirect&bpo=7475), [bpo-17827](https://bugs.python.org/issue?@action=redirect&bpo=17827),
[bpo-17828](https://bugs.python.org/issue?@action=redirect&bpo=17828) and [bpo-19619](https://bugs.python.org/issue?@action=redirect&bpo=19619).)

### PEP 451: A ModuleSpec Type for the Import System[¶](#pep-451-a-modulespec-type-for-the-import-system)

[ PEP 451](https://peps.python.org/pep-0451/) provides an encapsulation of the information about a module that the
import machinery will use to load it (that is, a module specification).  This
helps simplify both the import implementation and several import-related APIs.
The change is also a stepping stone for 

[several future import-related improvements](https://mail.python.org/pipermail/python-dev/2013-November/130111.html).

The public-facing changes from the PEP are entirely backward-compatible.
Furthermore, they should be transparent to everyone but importer authors.  Key
finder and loader methods have been deprecated, but they will continue working.
New importers should use the new methods described in the PEP.  Existing
importers should be updated to implement the new methods.  See the
[Deprecated](#deprecated-3-4) section for a list of methods that should be replaced and
their replacements.

### Other Language Changes[¶](#other-language-changes)

Some smaller changes made to the core Python language are:

- Unicode database updated to UCD version 6.3. 
- `min()`- `max()`- *default*keyword-only argument that can be used to specify the value they return if the iterable they are evaluating has no elements. (Contributed by Julian Berman in- [bpo-18111](https://bugs.python.org/issue?@action=redirect&bpo=18111).)
- Module objects are now - [weakly referenceable](../library/weakref.html#mod-weakref).
- Module - `__file__`attributes (and related values) should now always contain absolute paths by default, with the sole exception of- `__main__.__file__`when a script has been executed directly using a relative path. (Contributed by Brett Cannon in- [bpo-18416](https://bugs.python.org/issue?@action=redirect&bpo=18416).)
- All the UTF-* codecs (except UTF-7) now reject surrogates during both encoding and decoding unless the - `surrogatepass`error handler is used, with the exception of the UTF-16 decoder (which accepts valid surrogate pairs) and the UTF-16 encoder (which produces them while encoding non-BMP characters). (Contributed by Victor Stinner, Kang-Hao (Kenny) Lu and Serhiy Storchaka in- [bpo-12892](https://bugs.python.org/issue?@action=redirect&bpo=12892).)
- New German EBCDIC - [codec](../library/codecs.html#standard-encodings)- `cp273`. (Contributed by Michael Bierenfeld and Andrew Kuchling in- [bpo-1097797](https://bugs.python.org/issue?@action=redirect&bpo=1097797).)
- New Ukrainian - [codec](../library/codecs.html#standard-encodings)- `cp1125`. (Contributed by Serhiy Storchaka in- [bpo-19668](https://bugs.python.org/issue?@action=redirect&bpo=19668).)
- `bytes`- `bytearray`- [bpo-15958](https://bugs.python.org/issue?@action=redirect&bpo=15958).)
- The - `int`- `__index__`method for its- *base*argument. (Contributed by Mark Dickinson in- [bpo-16772](https://bugs.python.org/issue?@action=redirect&bpo=16772).)
- Frame objects now have a - `clear()`- [bpo-17934](https://bugs.python.org/issue?@action=redirect&bpo=17934).)
- `memoryview`- `Sequence`- `reversed()`- [bpo-18690](https://bugs.python.org/issue?@action=redirect&bpo=18690)and- [bpo-19078](https://bugs.python.org/issue?@action=redirect&bpo=19078).)
- Signatures reported by - `help()`- `inspect`- `pydoc`
- `__length_hint__()`- **PEP 424**- [bpo-16148](https://bugs.python.org/issue?@action=redirect&bpo=16148).)

## New Modules[¶](#new-modules)

### asyncio[¶](#asyncio)

The new [ asyncio](../library/asyncio.html#module-asyncio) module (defined in 

[) provides a standard pluggable event loop model for Python, providing solid asynchronous IO support in the standard library, and making it easier for other event loop implementations to interoperate with the standard library and each other.](https://peps.python.org/pep-3156/)

**PEP 3156**For Python 3.4, this module is considered a [provisional API](../glossary.html#term-provisional-API).

See also

- **PEP 3156**
- PEP written and implementation led by Guido van Rossum. 

### ensurepip[¶](#ensurepip)

The new [ ensurepip](../library/ensurepip.html#module-ensurepip) module is the primary infrastructure for the

[implementation. In the normal course of events end users will not need to interact with this module, but it can be used to manually bootstrap](https://peps.python.org/pep-0453/)

**PEP 453**`pip` if the automated bootstrapping into an installation or virtual
environment was declined.[ ensurepip](../library/ensurepip.html#module-ensurepip) includes a bundled copy of 

`pip`, up-to-date as of the first
release candidate of the release of CPython with which it ships (this applies
to both maintenance releases and feature releases).  `ensurepip` does not
access the internet.  If the installation has internet access, after
`ensurepip` is run the bundled `pip` can be used to upgrade `pip` to a
more recent release than the bundled one.  (Note that such an upgraded version
of `pip` is considered to be a separately installed package and will not be
removed if Python is uninstalled.)The module is named *ensure*pip because if called when `pip` is already
installed, it does nothing.  It also has an `--upgrade` option that will
cause it to install the bundled copy of `pip` if the existing installed
version of `pip` is older than the bundled copy.

### enum[¶](#enum)

The new [ enum](../library/enum.html#module-enum) module (defined in 

[) provides a standard implementation of enumeration types, allowing other modules (such as](https://peps.python.org/pep-0435/)

**PEP 435**[) to provide more informative error messages and better debugging support by replacing opaque integer constants with backwards compatible enumeration values.](../library/socket.html#module-socket)

`socket`See also

- **PEP 435**
- PEP written by Barry Warsaw, Eli Bendersky and Ethan Furman, implemented by Ethan Furman. 

### pathlib[¶](#pathlib)

The new [ pathlib](../library/pathlib.html#module-pathlib) module offers classes representing filesystem paths
with semantics appropriate for different operating systems.  Path classes are
divided between 

*pure paths*, which provide purely computational operations without I/O, and

*concrete paths*, which inherit from pure paths but also provide I/O operations.

For Python 3.4, this module is considered a [provisional API](../glossary.html#term-provisional-API).

See also

- **PEP 428**
- PEP written and implemented by Antoine Pitrou. 

### selectors[¶](#selectors)

The new [ selectors](../library/selectors.html#module-selectors) module (created as part of implementing 

[) allows high-level and efficient I/O multiplexing, built upon the](https://peps.python.org/pep-3156/)

**PEP 3156**[module primitives.](../library/select.html#module-select)

`select`### statistics[¶](#statistics)

The new [ statistics](../library/statistics.html#module-statistics) module (defined in 

[) offers some core statistics functionality directly in the standard library. This module supports calculation of the mean, median, mode, variance and standard deviation of a data series.](https://peps.python.org/pep-0450/)

**PEP 450**See also

- **PEP 450**
- PEP written and implemented by Steven D’Aprano 

### tracemalloc[¶](#tracemalloc)

The new [ tracemalloc](../library/tracemalloc.html#module-tracemalloc) module (defined in 

[) is a debug tool to trace memory blocks allocated by Python. It provides the following information:](https://peps.python.org/pep-0454/)

**PEP 454**- Trace where an object was allocated 
- Statistics on allocated memory blocks per filename and per line number: total size, number and average size of allocated memory blocks 
- Compute the differences between two snapshots to detect memory leaks 

See also

- **PEP 454**
- PEP written and implemented by Victor Stinner 

## Improved Modules[¶](#improved-modules)

### abc[¶](#abc)

New function [ abc.get_cache_token()](../library/abc.html#abc.get_cache_token) can be used to know when to invalidate
caches that are affected by changes in the object graph.  (Contributed
by Łukasz Langa in 

[bpo-16832](https://bugs.python.org/issue?@action=redirect&bpo=16832).)

New class [ ABC](../library/abc.html#abc.ABC) has 

[as its meta class. Using](../library/abc.html#abc.ABCMeta)

`ABCMeta``ABC` as a base class has essentially the same effect as specifying
`metaclass=abc.ABCMeta`, but is simpler to type and easier to read.
(Contributed by Bruno Dupuis in [bpo-16049](https://bugs.python.org/issue?@action=redirect&bpo=16049).)

### aifc[¶](#aifc)

The `getparams()` method now returns a namedtuple rather than a
plain tuple.  (Contributed by Claudiu Popa in [bpo-17818](https://bugs.python.org/issue?@action=redirect&bpo=17818).)

`aifc.open()` now supports the context management protocol: when used in a
[ with](../reference/compound_stmts.html#with) block, the 

`close()` method of the returned
object will be called automatically at the end of the block.  (Contributed by
Serhiy Storchacha in [bpo-16486](https://bugs.python.org/issue?@action=redirect&bpo=16486).)

The `writeframesraw()` and `writeframes()`
methods now accept any [bytes-like object](../glossary.html#term-bytes-like-object).  (Contributed by Serhiy
Storchaka in [bpo-8311](https://bugs.python.org/issue?@action=redirect&bpo=8311).)

### argparse[¶](#argparse)

The [ FileType](../library/argparse.html#argparse.FileType) class now accepts 

*encoding*and

*errors*arguments, which are passed through to

[. (Contributed by Lucas Maystre in](../library/functions.html#open)

`open()`[bpo-11175](https://bugs.python.org/issue?@action=redirect&bpo=11175).)

### audioop[¶](#audioop)

`audioop` now supports 24-bit samples.  (Contributed by Serhiy Storchaka
in [bpo-12866](https://bugs.python.org/issue?@action=redirect&bpo=12866).)

New `byteswap()` function converts big-endian samples to
little-endian and vice versa.  (Contributed by Serhiy Storchaka in
[bpo-19641](https://bugs.python.org/issue?@action=redirect&bpo=19641).)

All `audioop` functions now accept any [bytes-like object](../glossary.html#term-bytes-like-object).  Strings
are not accepted: they didn’t work before, now they raise an error right away.
(Contributed by Serhiy Storchaka in [bpo-16685](https://bugs.python.org/issue?@action=redirect&bpo=16685).)

### base64[¶](#base64)

The encoding and decoding functions in [ base64](../library/base64.html#module-base64) now accept any

[bytes-like object](../glossary.html#term-bytes-like-object)in cases where it previously required a

[or](../library/stdtypes.html#bytes)

`bytes`[instance. (Contributed by Nick Coghlan in](../library/stdtypes.html#bytearray)

`bytearray`[bpo-17839](https://bugs.python.org/issue?@action=redirect&bpo=17839).)

New functions [ a85encode()](../library/base64.html#base64.a85encode), 

[,](../library/base64.html#base64.a85decode)

`a85decode()`[, and](../library/base64.html#base64.b85encode)

`b85encode()`[provide the ability to encode and decode binary data from and to](../library/base64.html#base64.b85decode)

`b85decode()``Ascii85` and the git/mercurial
`Base85` formats, respectively.  The `a85` functions have options that can
be used to make them compatible with the variants of the `Ascii85` encoding,
including the Adobe variant.  (Contributed by Martin Morrison, the Mercurial
project, Serhiy Storchaka, and Antoine Pitrou in [bpo-17618](https://bugs.python.org/issue?@action=redirect&bpo=17618).)

### collections[¶](#collections)

The [ ChainMap.new_child()](../library/collections.html#collections.ChainMap.new_child) method now accepts an 

*m*argument specifying the child map to add to the chain. This allows an existing mapping and/or a custom mapping type to be used for the child. (Contributed by Vinay Sajip in

[bpo-16613](https://bugs.python.org/issue?@action=redirect&bpo=16613).)

### colorsys[¶](#colorsys)

The number of digits in the coefficients for the RGB — YIQ conversions have
been expanded so that they match the FCC NTSC versions.  The change in
results should be less than 1% and may better match results found elsewhere.
(Contributed by Brian Landers and Serhiy Storchaka in [bpo-14323](https://bugs.python.org/issue?@action=redirect&bpo=14323).)

### contextlib[¶](#contextlib)

The new [ contextlib.suppress](../library/contextlib.html#contextlib.suppress) context manager helps to clarify the
intent of code that deliberately suppresses exceptions from a single
statement.  (Contributed by Raymond Hettinger in 

[bpo-15806](https://bugs.python.org/issue?@action=redirect&bpo=15806)and Zero Piraeus in

[bpo-19266](https://bugs.python.org/issue?@action=redirect&bpo=19266).)

The new [ contextlib.redirect_stdout()](../library/contextlib.html#contextlib.redirect_stdout) context manager makes it easier
for utility scripts to handle inflexible APIs that write their output to

[and don’t provide any options to redirect it. Using the context manager, the](../library/sys.html#sys.stdout)

`sys.stdout``sys.stdout` output can be redirected to any
other stream or, in conjunction with [, to a string. The latter can be especially useful, for example, to capture output from a function that was written to implement a command line interface. It is recommended only for utility scripts because it affects the global state of](../library/io.html#io.StringIO)

`io.StringIO``sys.stdout`.  (Contributed by Raymond Hettinger
in [bpo-15805](https://bugs.python.org/issue?@action=redirect&bpo=15805).)

The [ contextlib](../library/contextlib.html#module-contextlib) documentation has also been updated to include a

[discussion](../library/contextlib.html#single-use-reusable-and-reentrant-cms)of the differences between single use, reusable and reentrant context managers.

### dbm[¶](#dbm)

[ dbm.open()](../library/dbm.html#dbm.open) objects now support the context management protocol.  When
used in a 

[statement, the](../reference/compound_stmts.html#with)

`with``close` method of the database
object will be called automatically at the end of the block.  (Contributed by
Claudiu Popa and Nick Coghlan in [bpo-19282](https://bugs.python.org/issue?@action=redirect&bpo=19282).)

### dis[¶](#dis)

Functions [ show_code()](../library/dis.html#dis.show_code), 

[,](../library/dis.html#dis.dis)

`dis()`[, and](../library/dis.html#dis.distb)

`distb()`[now accept a keyword-only](../library/dis.html#dis.disassemble)

`disassemble()`*file*argument that controls where they write their output.

The [ dis](../library/dis.html#module-dis) module is now built around an 

[class that provides object oriented access to the details of each individual bytecode operation.](../library/dis.html#dis.Instruction)

`Instruction`A new method, [ get_instructions()](../library/dis.html#dis.get_instructions), provides an iterator that emits
the Instruction stream for a given piece of Python code.  Thus it is now
possible to write a program that inspects and manipulates a bytecode
object in ways different from those provided by the 

[module itself. For example:](../library/dis.html#module-dis)

`dis````
>>> import dis
>>> for instr in dis.get_instructions(lambda x: x + 1):
...     print(instr.opname)
LOAD_FAST
LOAD_CONST
BINARY_ADD
RETURN_VALUE
```
The various display tools in the [ dis](../library/dis.html#module-dis) module have been rewritten to use
these new components.

In addition, a new application-friendly class [ Bytecode](../library/dis.html#dis.Bytecode) provides
an object-oriented API for inspecting bytecode in both in human-readable form
and for iterating over instructions.  The 

`Bytecode` constructor
takes the same arguments that [does (plus an optional](../library/dis.html#dis.get_instructions)

`get_instructions()`*current_offset*), and the resulting object can be iterated to produce

[objects. But it also has a](../library/dis.html#dis.Instruction)

`Instruction`[method, equivalent to calling](../library/dis.html#dis.Bytecode.dis)

`dis`[on the constructor argument, but returned as a multi-line string:](../library/dis.html#dis.dis)

`dis````
>>> bytecode = dis.Bytecode(lambda x: x + 1, current_offset=3)
>>> for instr in bytecode:
...     print('{} ({})'.format(instr.opname, instr.opcode))
LOAD_FAST (124)
LOAD_CONST (100)
BINARY_ADD (23)
RETURN_VALUE (83)
>>> bytecode.dis().splitlines()
['  1           0 LOAD_FAST                0 (x)',
 '      -->     3 LOAD_CONST               1 (1)',
 '              6 BINARY_ADD',
 '              7 RETURN_VALUE']
```
[ Bytecode](../library/dis.html#dis.Bytecode) also has a class method,

[, that provides the ability to manipulate a traceback (that is,](../library/dis.html#dis.Bytecode.from_traceback)

`from_traceback()``print(Bytecode.from_traceback(tb).dis())` is equivalent
to `distb(tb)`).(Contributed by Nick Coghlan, Ryan Kelly and Thomas Kluyver in [bpo-11816](https://bugs.python.org/issue?@action=redirect&bpo=11816)
and Claudiu Popa in [bpo-17916](https://bugs.python.org/issue?@action=redirect&bpo=17916).)

New function [ stack_effect()](../library/dis.html#dis.stack_effect) computes the effect on the Python stack
of a given opcode and argument, information that is not otherwise available.
(Contributed by Larry Hastings in 

[bpo-19722](https://bugs.python.org/issue?@action=redirect&bpo=19722).)

### doctest[¶](#doctest)

A new [option flag](../library/doctest.html#doctest-options), [ FAIL_FAST](../library/doctest.html#doctest.FAIL_FAST), halts
test running as soon as the first failure is detected.  (Contributed by R.
David Murray and Daniel Urban in 

[bpo-16522](https://bugs.python.org/issue?@action=redirect&bpo=16522).)

The [ doctest](../library/doctest.html#module-doctest) command line interface now uses 

[, and has two new options,](../library/argparse.html#module-argparse)

`argparse``-o` and `-f`.  `-o` allows [doctest options](../library/doctest.html#doctest-options)to be specified on the command line, and

`-f` is a
shorthand for `-o FAIL_FAST` (to parallel the similar option supported by the
[CLI). (Contributed by R. David Murray in](../library/unittest.html#module-unittest)

`unittest`[bpo-11390](https://bugs.python.org/issue?@action=redirect&bpo=11390).)

[ doctest](../library/doctest.html#module-doctest) will now find doctests in extension module 

`__doc__` strings.
(Contributed by Zachary Ware in [bpo-3158](https://bugs.python.org/issue?@action=redirect&bpo=3158).)

### email[¶](#email)

[ as_string()](../library/email.compat32-message.html#email.message.Message.as_string) now accepts a 

*policy*argument to override the default policy of the message when generating a string representation of it. This means that

`as_string` can now be used in more
circumstances, instead of having to create and use a [in order to pass formatting parameters to its](../library/email.generator.html#module-email.generator)

`generator``flatten` method.  (Contributed by
R. David Murray in [bpo-18600](https://bugs.python.org/issue?@action=redirect&bpo=18600).)

New method [ as_bytes()](../library/email.compat32-message.html#email.message.Message.as_bytes) added to produce a bytes
representation of the message in a fashion similar to how 

`as_string`
produces a string representation.  It does not accept the *maxheaderlen*argument, but does accept the

*unixfrom*and

*policy*arguments. The


`Message`[method calls it, meaning that](../library/email.compat32-message.html#email.message.Message.__bytes__)

`__bytes__()``bytes(mymsg)` will now produce the intuitive
result:  a bytes object containing the fully formatted message.  (Contributed
by R. David Murray in [bpo-18600](https://bugs.python.org/issue?@action=redirect&bpo=18600).)

The [ Message.set_param()](../library/email.compat32-message.html#email.message.Message.set_param) message now accepts a 

*replace*keyword argument. When specified, the associated header will be updated without changing its location in the list of headers. For backward compatibility, the default is

`False`.  (Contributed by R. David Murray in [bpo-18891](https://bugs.python.org/issue?@action=redirect&bpo=18891).)

A pair of new subclasses of [ Message](../library/email.compat32-message.html#email.message.Message) have been added
(

[and](../library/email.message.html#email.message.EmailMessage)

`EmailMessage`[), along with a new sub-module,](../library/email.message.html#email.message.MIMEPart)

`MIMEPart`[and a new](../library/email.contentmanager.html#module-email.contentmanager)

`contentmanager`[attribute](../library/email.policy.html#module-email.policy)

`policy`[. All documentation is currently in the new module, which is being added as part of email’s new](../library/email.policy.html#email.policy.EmailPolicy.content_manager)

`content_manager`[provisional API](../glossary.html#term-provisional-API). These classes provide a number of new methods that make extracting content from and inserting content into email messages much easier. For details, see the

`contentmanager` documentation and
the [email: Examples](../library/email.examples.html#email-examples). These API additions complete the bulk of the work that was planned as part of the email6 project. The currently provisional API is scheduled to become final in Python 3.5 (possibly with a few minor additions in the area of error handling). (Contributed by R. David Murray in

[bpo-18891](https://bugs.python.org/issue?@action=redirect&bpo=18891).)

### filecmp[¶](#filecmp)

A new [ clear_cache()](../library/filecmp.html#filecmp.clear_cache) function provides the ability to clear the

[comparison cache, which uses](../library/filecmp.html#module-filecmp)

`filecmp`[information to determine if the file has changed since the last compare. This can be used, for example, if the file might have been changed and re-checked in less time than the resolution of a particular filesystem’s file modification time field. (Contributed by Mark Levitt in](../library/os.html#os.stat)

`os.stat()`[bpo-18149](https://bugs.python.org/issue?@action=redirect&bpo=18149).)

New module attribute [ DEFAULT_IGNORES](../library/filecmp.html#filecmp.DEFAULT_IGNORES) provides the list of
directories that are used as the default value for the 

*ignore*parameter of the

[function. (Contributed by Eli Bendersky in](../library/filecmp.html#filecmp.dircmp)

`dircmp()`[bpo-15442](https://bugs.python.org/issue?@action=redirect&bpo=15442).)

### functools[¶](#functools)

The new [ partialmethod()](../library/functools.html#functools.partialmethod) descriptor brings partial argument
application to descriptors, just as 

[provides for normal callables. The new descriptor also makes it easier to get arbitrary callables (including](../library/functools.html#functools.partial)

`partial()``partial()` instances)
to behave like normal instance methods when included in a class definition.
(Contributed by Alon Horev and Nick Coghlan in [bpo-4331](https://bugs.python.org/issue?@action=redirect&bpo=4331).)

The new [ singledispatch()](../library/functools.html#functools.singledispatch) decorator brings support for
single-dispatch generic functions to the Python standard library. Where
object oriented programming focuses on grouping multiple operations on a
common set of data into a class, a generic function focuses on grouping
multiple implementations of an operation that allows it to work with

*different*kinds of data.

See also

- **PEP 443**
- PEP written and implemented by Łukasz Langa. 

[ total_ordering()](../library/functools.html#functools.total_ordering) now supports a return value of

[from the underlying comparison function. (Contributed by Katie Miller in](../library/constants.html#NotImplemented)

`NotImplemented`[bpo-10042](https://bugs.python.org/issue?@action=redirect&bpo=10042).)

A pure-python version of the [ partial()](../library/functools.html#functools.partial) function is now in the
stdlib; in CPython it is overridden by the C accelerated version, but it is
available for other implementations to use.  (Contributed by Brian Thorne in

[bpo-12428](https://bugs.python.org/issue?@action=redirect&bpo=12428).)

### gc[¶](#gc)

New function [ get_stats()](../library/gc.html#gc.get_stats) returns a list of three per-generation
dictionaries containing the collections statistics since interpreter startup.
(Contributed by Antoine Pitrou in 

[bpo-16351](https://bugs.python.org/issue?@action=redirect&bpo=16351).)

### glob[¶](#glob)

A new function [ escape()](../library/glob.html#glob.escape) provides a way to escape special characters
in a filename so that they do not become part of the globbing expansion but are
instead matched literally.  (Contributed by Serhiy Storchaka in 

[bpo-8402](https://bugs.python.org/issue?@action=redirect&bpo=8402).)

### hashlib[¶](#hashlib)

A new [ hashlib.pbkdf2_hmac()](../library/hashlib.html#hashlib.pbkdf2_hmac) function provides
the 

[PKCS#5 password-based key derivation function 2](https://en.wikipedia.org/wiki/PBKDF2). (Contributed by Christian Heimes in

[bpo-18582](https://bugs.python.org/issue?@action=redirect&bpo=18582).)

The [ name](../library/hashlib.html#hashlib.hash.name) attribute of 

[hash objects is now a formally supported interface. It has always existed in CPython’s](../library/hashlib.html#module-hashlib)

`hashlib``hashlib` (although it did not return lower case names for all supported
hashes), but it was not a public interface and so some other Python
implementations have not previously supported it.  (Contributed by Jason R.
Coombs in [bpo-18532](https://bugs.python.org/issue?@action=redirect&bpo=18532).)

### hmac[¶](#hmac)

[ hmac](../library/hmac.html#module-hmac) now accepts 

`bytearray` as well as `bytes` for the *key*argument to the

[function, and the](../library/hmac.html#hmac.new)

`new()`*msg*parameter to both the

`new()` function and the [method now accepts any type supported by the](../library/hmac.html#hmac.HMAC.update)

`update()`[module. (Contributed by Jonas Borgström in](../library/hashlib.html#module-hashlib)

`hashlib`[bpo-18240](https://bugs.python.org/issue?@action=redirect&bpo=18240).)

The *digestmod* argument to the [ hmac.new()](../library/hmac.html#hmac.new) function may now be any hash
digest name recognized by 

[. In addition, the current behavior in which the value of](../library/hashlib.html#module-hashlib)

`hashlib`*digestmod*defaults to

`MD5` is deprecated: in a
future version of Python there will be no default value.  (Contributed by
Christian Heimes in [bpo-17276](https://bugs.python.org/issue?@action=redirect&bpo=17276).)

With the addition of [ block_size](../library/hmac.html#hmac.HMAC.block_size) and 

[attributes (and the formal documentation of the](../library/hmac.html#hmac.HMAC.name)

`name`[attribute), the](../library/hmac.html#hmac.HMAC.digest_size)

`digest_size`[module now conforms fully to the](../library/hmac.html#module-hmac)

`hmac`[API. (Contributed by Christian Heimes in](https://peps.python.org/pep-0247/)

**PEP 247**[bpo-18775](https://bugs.python.org/issue?@action=redirect&bpo=18775).)

### html[¶](#html)

New function [ unescape()](../library/html.html#html.unescape) function converts HTML5 character references to
the corresponding Unicode characters.  (Contributed by Ezio Melotti in

[bpo-2927](https://bugs.python.org/issue?@action=redirect&bpo=2927).)

[ HTMLParser](../library/html.parser.html#html.parser.HTMLParser) accepts a new keyword argument

*convert_charrefs*that, when

`True`, automatically converts all character
references.  For backward-compatibility, its value defaults to `False`, but
it will change to `True` in a future version of Python, so you are invited to
set it explicitly and update your code to use this new feature.  (Contributed
by Ezio Melotti in [bpo-13633](https://bugs.python.org/issue?@action=redirect&bpo=13633).)

The *strict* argument of [ HTMLParser](../library/html.parser.html#html.parser.HTMLParser) is now deprecated.
(Contributed by Ezio Melotti in 

[bpo-15114](https://bugs.python.org/issue?@action=redirect&bpo=15114).)

### http[¶](#http)

[ send_error()](../library/http.server.html#http.server.BaseHTTPRequestHandler.send_error) now accepts an
optional additional 

*explain*parameter which can be used to provide an extended error description, overriding the hardcoded default if there is one. This extended error description will be formatted using the

[attribute and sent as the body of the error response. (Contributed by Karl Cow in](../library/http.server.html#http.server.BaseHTTPRequestHandler.error_message_format)

`error_message_format`[bpo-12921](https://bugs.python.org/issue?@action=redirect&bpo=12921).)

The `http.server`[command line interface](../library/http.server.html#http-server-cli) now has
a `-b/--bind` option that causes the server to listen on a specific address.
(Contributed by Malte Swart in [bpo-17764](https://bugs.python.org/issue?@action=redirect&bpo=17764).)

### idlelib and IDLE[¶](#idlelib-and-idle)

Since idlelib implements the IDLE shell and editor and is not intended for
import by other programs, it gets improvements with every release. See
`Lib/idlelib/NEWS.txt` for a cumulative list of changes since 3.3.0,
as well as changes made in future 3.4.x releases. This file is also available
from the IDLE  dialog.

### importlib[¶](#importlib)

The [ InspectLoader](../library/importlib.html#importlib.abc.InspectLoader) ABC defines a new method,

[that accepts source data and a path and returns a code object. The default implementation is equivalent to](../library/importlib.html#importlib.abc.InspectLoader.source_to_code)

`source_to_code()``compile(data, path, 'exec', dont_inherit=True)`.
(Contributed by Eric Snow and Brett Cannon in [bpo-15627](https://bugs.python.org/issue?@action=redirect&bpo=15627).)

[ InspectLoader](../library/importlib.html#importlib.abc.InspectLoader) also now has a default implementation
for the 

[method. However, it will normally be desirable to override the default implementation for performance reasons. (Contributed by Brett Cannon in](../library/importlib.html#importlib.abc.InspectLoader.get_code)

`get_code()`[bpo-18072](https://bugs.python.org/issue?@action=redirect&bpo=18072).)

The [ reload()](../library/importlib.html#importlib.reload) function has been moved from 

`imp` to
[as part of the](../library/importlib.html#module-importlib)

`importlib``imp` module deprecation.  (Contributed by
Berker Peksag in [bpo-18193](https://bugs.python.org/issue?@action=redirect&bpo=18193).)

[ importlib.util](../library/importlib.html#module-importlib.util) now has a 

[attribute providing access to the bytecode version number. This replaces the](../library/importlib.html#importlib.util.MAGIC_NUMBER)

`MAGIC_NUMBER``get_magic()` function in the deprecated `imp` module.
(Contributed by Brett Cannon in [bpo-18192](https://bugs.python.org/issue?@action=redirect&bpo=18192).)

New [ importlib.util](../library/importlib.html#module-importlib.util) functions 

[and](../library/importlib.html#importlib.util.cache_from_source)

`cache_from_source()`[replace the same-named functions in the deprecated](../library/importlib.html#importlib.util.source_from_cache)

`source_from_cache()``imp` module.  (Contributed by Brett Cannon in
[bpo-18194](https://bugs.python.org/issue?@action=redirect&bpo=18194).)

The [ importlib](../library/importlib.html#module-importlib) bootstrap 

[now conforms to the](../library/importlib.html#importlib.machinery.NamespaceLoader)

`NamespaceLoader`[ABC, which means that](../library/importlib.html#importlib.abc.InspectLoader)

`InspectLoader``runpy` and
`python -m` can now be used with namespace packages.  (Contributed
by Brett Cannon in [bpo-18058](https://bugs.python.org/issue?@action=redirect&bpo=18058).)

[ importlib.util](../library/importlib.html#module-importlib.util) has a new function 

[that decodes source from bytes using universal newline processing. This is useful for implementing](../library/importlib.html#importlib.util.decode_source)

`decode_source()`[methods.](../library/importlib.html#importlib.abc.InspectLoader.get_source)

`InspectLoader.get_source()`[ importlib.machinery.ExtensionFileLoader](../library/importlib.html#importlib.machinery.ExtensionFileLoader) now has a

[method. This was inadvertently omitted in the original implementation. (Contributed by Eric Snow in](../library/importlib.html#importlib.machinery.ExtensionFileLoader.get_filename)

`get_filename()`[bpo-19152](https://bugs.python.org/issue?@action=redirect&bpo=19152).)

### inspect[¶](#inspect)

The [ inspect](../library/inspect.html#module-inspect) module now offers a basic 

[command line interface](../library/inspect.html#inspect-module-cli)to quickly display source code and other information for modules, classes and functions. (Contributed by Claudiu Popa and Nick Coghlan in

[bpo-18626](https://bugs.python.org/issue?@action=redirect&bpo=18626).)

[ unwrap()](../library/inspect.html#inspect.unwrap) makes it easy to unravel wrapper function chains
created by 

[(and any other API that sets the](../library/functools.html#functools.wraps)

`functools.wraps()``__wrapped__` attribute on a wrapper function).  (Contributed by
Daniel Urban, Aaron Iles and Nick Coghlan in [bpo-13266](https://bugs.python.org/issue?@action=redirect&bpo=13266).)

As part of the implementation of the new [ enum](../library/enum.html#module-enum) module, the

[module now has substantially better support for custom](../library/inspect.html#module-inspect)

`inspect``__dir__` methods and dynamic class attributes provided through
metaclasses.  (Contributed by Ethan Furman in [bpo-18929](https://bugs.python.org/issue?@action=redirect&bpo=18929)and

[bpo-19030](https://bugs.python.org/issue?@action=redirect&bpo=19030).)

[ getfullargspec()](../library/inspect.html#inspect.getfullargspec) and 

`getargspec()`
now use the [API. This allows them to support a much broader range of callables, including those with](../library/inspect.html#inspect.signature)

`signature()``__signature__` attributes, those with metadata provided by argument
clinic, [objects and more. Note that, unlike](../library/functools.html#functools.partial)

`functools.partial()``signature()`, these functions still ignore `__wrapped__`
attributes, and report the already bound first argument for bound methods,
so it is still necessary to update your code to use
`signature()` directly if those features are desired.
(Contributed by Yury Selivanov in [bpo-17481](https://bugs.python.org/issue?@action=redirect&bpo=17481).)

[ signature()](../library/inspect.html#inspect.signature) now supports duck types of CPython functions,
which adds support for functions compiled with Cython.  (Contributed
by Stefan Behnel and Yury Selivanov in 

[bpo-17159](https://bugs.python.org/issue?@action=redirect&bpo=17159).)

### ipaddress[¶](#ipaddress)

[ ipaddress](../library/ipaddress.html#module-ipaddress) was added to the standard library in Python 3.3 as a

[provisional API](../glossary.html#term-provisional-API). With the release of Python 3.4, this qualification has been removed:

`ipaddress` is now considered a stable API, covered
by the normal standard library requirements to maintain backwards
compatibility.A new [ is_global](../library/ipaddress.html#ipaddress.IPv4Address.is_global) property is 

`True` if
an address is globally routeable.  (Contributed by Peter Moody in
[bpo-17400](https://bugs.python.org/issue?@action=redirect&bpo=17400).)

### logging[¶](#logging)

The [ TimedRotatingFileHandler](../library/logging.handlers.html#logging.handlers.TimedRotatingFileHandler) has a new 

*atTime*parameter that can be used to specify the time of day when rollover should happen. (Contributed by Ronald Oussoren in

[bpo-9556](https://bugs.python.org/issue?@action=redirect&bpo=9556).)

[ SocketHandler](../library/logging.handlers.html#logging.handlers.SocketHandler) and

[now support Unix domain sockets (by setting](../library/logging.handlers.html#logging.handlers.DatagramHandler)

`DatagramHandler`*port*to

`None`).  (Contributed by Vinay Sajip in commit
ce46195b56a9.)[ fileConfig()](../library/logging.config.html#logging.config.fileConfig) now accepts a

[subclass instance for the](../library/configparser.html#configparser.RawConfigParser)

`configparser.RawConfigParser`*fname*parameter. This facilitates using a configuration file when logging configuration is just a part of the overall application configuration, or where the application modifies the configuration before passing it to

`fileConfig()`.  (Contributed by Vinay Sajip in
[bpo-16110](https://bugs.python.org/issue?@action=redirect&bpo=16110).)

Logging configuration data received from a socket via the
[ logging.config.listen()](../library/logging.config.html#logging.config.listen) function can now be validated before being
processed by supplying a verification function as the argument to the new

*verify*keyword argument. (Contributed by Vinay Sajip in

[bpo-15452](https://bugs.python.org/issue?@action=redirect&bpo=15452).)

### marshal[¶](#marshal)

The default [ marshal](../library/marshal.html#module-marshal) version has been bumped to 3.  The code implementing
the new version restores the Python2 behavior of recording only one copy of
interned strings and preserving the interning on deserialization, and extends
this “one copy” ability to any object type (including handling recursive
references).  This reduces both the size of 

`.pyc` files and the amount of
memory a module occupies in memory when it is loaded from a `.pyc` (or
`.pyo`) file.  (Contributed by Kristján Valur Jónsson in [bpo-16475](https://bugs.python.org/issue?@action=redirect&bpo=16475), with additional speedups by Antoine Pitrou in

[bpo-19219](https://bugs.python.org/issue?@action=redirect&bpo=19219).)

### mmap[¶](#mmap)

mmap objects are now [weakly referenceable](../library/weakref.html#mod-weakref).
(Contributed by Valerie Lambert in [bpo-4885](https://bugs.python.org/issue?@action=redirect&bpo=4885).)

### multiprocessing[¶](#multiprocessing)

On Unix two new [start methods](../library/multiprocessing.html#multiprocessing-start-methods),
`spawn` and `forkserver`, have been added for starting processes using
[ multiprocessing](../library/multiprocessing.html#module-multiprocessing).  These make the mixing of processes with threads more
robust, and the 

`spawn` method matches the semantics that multiprocessing has
always used on Windows.  New function
[reports all start methods available on the platform,](../library/multiprocessing.html#multiprocessing.get_all_start_methods)

`get_all_start_methods()`[reports the current start method, and](../library/multiprocessing.html#multiprocessing.get_start_method)

`get_start_method()`[sets the start method. (Contributed by Richard Oudkerk in](../library/multiprocessing.html#multiprocessing.set_start_method)

`set_start_method()`[bpo-8713](https://bugs.python.org/issue?@action=redirect&bpo=8713).)

[ multiprocessing](../library/multiprocessing.html#module-multiprocessing) also now has the concept of a 

`context`, which
determines how child processes are created.  New function
[returns a context that uses a specified start method. It has the same API as the](../library/multiprocessing.html#multiprocessing.get_context)

`get_context()``multiprocessing` module itself,
so you can use it to create [s and other objects that will operate within that context. This allows a framework and an application or different parts of the same application to use multiprocessing without interfering with each other. (Contributed by Richard Oudkerk in](../library/multiprocessing.html#multiprocessing.pool.Pool)

`Pool`[bpo-18999](https://bugs.python.org/issue?@action=redirect&bpo=18999).)

Except when using the old *fork* start method, child processes no longer
inherit unneeded handles/file descriptors from their parents (part of
[bpo-8713](https://bugs.python.org/issue?@action=redirect&bpo=8713)).

[ multiprocessing](../library/multiprocessing.html#module-multiprocessing) now relies on 

[(which implements the](../library/runpy.html#module-runpy)

`runpy``-m` switch) to initialise `__main__` appropriately in child processes
when using the `spawn` or `forkserver` start methods. This resolves some
edge cases where combining multiprocessing, the `-m` command line switch,
and explicit relative imports could cause obscure failures in child
processes.  (Contributed by Nick Coghlan in [bpo-19946](https://bugs.python.org/issue?@action=redirect&bpo=19946).)

### operator[¶](#operator)

New function [ length_hint()](../library/operator.html#operator.length_hint) provides an implementation of the
specification for how the 

[special method should be used, as part of the](../reference/datamodel.html#object.__length_hint__)

`__length_hint__()`[formal specification of this language feature. (Contributed by Armin Ronacher in](https://peps.python.org/pep-0424/)

**PEP 424**[bpo-16148](https://bugs.python.org/issue?@action=redirect&bpo=16148).)

There is now a pure-python version of the [ operator](../library/operator.html#module-operator) module available for
reference and for use by alternate implementations of Python.  (Contributed by
Zachary Ware in 

[bpo-16694](https://bugs.python.org/issue?@action=redirect&bpo=16694).)

### os[¶](#os)

There are new functions to get and set the [inheritable flag](../library/os.html#fd-inheritance) of a file descriptor ([ os.get_inheritable()](../library/os.html#os.get_inheritable),

[) or a Windows handle (](../library/os.html#os.set_inheritable)

`os.set_inheritable()`[,](../library/os.html#os.get_handle_inheritable)

`os.get_handle_inheritable()`[).](../library/os.html#os.set_handle_inheritable)

`os.set_handle_inheritable()`New function [ cpu_count()](../library/os.html#os.cpu_count) reports the number of CPUs available on the
platform on which Python is running (or 

`None` if the count can’t be
determined).  The [function is now implemented in terms of this function). (Contributed by Trent Nelson, Yogesh Chaudhari, Victor Stinner, and Charles-François Natali in](../library/multiprocessing.html#multiprocessing.cpu_count)

`multiprocessing.cpu_count()`[bpo-17914](https://bugs.python.org/issue?@action=redirect&bpo=17914).)

[ os.path.samestat()](../library/os.path.html#os.path.samestat) is now available on the Windows platform (and the

[implementation is now shared between Unix and Windows). (Contributed by Brian Curtin in](../library/os.path.html#os.path.samefile)

`os.path.samefile()`[bpo-11939](https://bugs.python.org/issue?@action=redirect&bpo=11939).)

[ os.path.ismount()](../library/os.path.html#os.path.ismount) now recognizes volumes mounted below a drive
root on Windows.  (Contributed by Tim Golden in 

[bpo-9035](https://bugs.python.org/issue?@action=redirect&bpo=9035).)

[ os.open()](../library/os.html#os.open) supports two new flags on platforms that provide them,

[(un-opened file descriptor), and](../library/os.html#os.O_PATH)

`O_PATH`[(unnamed temporary file; as of 3.4.0 release available only on Linux systems with a kernel version of 3.11 or newer that have uapi headers). (Contributed by Christian Heimes in](../library/os.html#os.O_TMPFILE)

`O_TMPFILE`[bpo-18673](https://bugs.python.org/issue?@action=redirect&bpo=18673)and Benjamin Peterson, respectively.)

### pdb[¶](#pdb)

[ pdb](../library/pdb.html#module-pdb) has been enhanced to handle generators, 

[, and](../reference/simple_stmts.html#yield)

`yield``yield from` in a more useful fashion.  This is especially helpful when
debugging [based programs. (Contributed by Andrew Svetlov and Xavier de Gaye in](../library/asyncio.html#module-asyncio)

`asyncio`[bpo-16596](https://bugs.python.org/issue?@action=redirect&bpo=16596).)

The `print` command has been removed from [ pdb](../library/pdb.html#module-pdb), restoring access to the
Python 

[function from the pdb command line. Python2’s](../library/functions.html#print)

`print()``pdb` did
not have a `print` command; instead, entering `print` executed the
`print` statement.  In Python3 `print` was mistakenly made an alias for the
pdb [command.](../library/pdb.html#pdbcommand-p)

`p``p`, however, prints the `repr` of its argument,
not the `str` like the Python2 `print` command did.  Worse, the Python3
`pdb print` command shadowed the Python3 `print` function, making it
inaccessible at the `pdb` prompt.  (Contributed by Connor Osborn in
[bpo-18764](https://bugs.python.org/issue?@action=redirect&bpo=18764).)

### pickle[¶](#pickle)

[ pickle](../library/pickle.html#module-pickle) now supports (but does not use by default) a new pickle protocol,
protocol 4.  This new protocol addresses a number of issues that were present
in previous protocols, such as the serialization of nested classes, very large
strings and containers, and classes whose 

[method takes keyword-only arguments. It also provides some efficiency improvements.](../reference/datamodel.html#object.__new__)

`__new__()`See also

- **PEP 3154**
- PEP written by Antoine Pitrou and implemented by Alexandre Vassalotti. 

### plistlib[¶](#plistlib)

[ plistlib](../library/plistlib.html#module-plistlib) now has an API that is similar to the standard pattern for
stdlib serialization protocols, with new 

[,](../library/plistlib.html#plistlib.load)

`load()`[,](../library/plistlib.html#plistlib.dump)

`dump()`[, and](../library/plistlib.html#plistlib.loads)

`loads()`[functions. (The older API is now deprecated.) In addition to the already supported XML plist format (](../library/plistlib.html#plistlib.dumps)

`dumps()`[), it also now supports the binary plist format (](../library/plistlib.html#plistlib.FMT_XML)

`FMT_XML`[). (Contributed by Ronald Oussoren and others in](../library/plistlib.html#plistlib.FMT_BINARY)

`FMT_BINARY`[bpo-14455](https://bugs.python.org/issue?@action=redirect&bpo=14455).)

### poplib[¶](#poplib)

Two new methods have been added to [ poplib](../library/poplib.html#module-poplib): 

[, which returns the list of capabilities advertised by the POP server, and](../library/poplib.html#poplib.POP3.capa)

`capa()`[, which switches a clear-text POP3 session into an encrypted POP3 session if the POP server supports it. (Contributed by Lorenzo Catucci in](../library/poplib.html#poplib.POP3.stls)

`stls()`[bpo-4473](https://bugs.python.org/issue?@action=redirect&bpo=4473).)

### pprint[¶](#pprint)

The [ pprint](../library/pprint.html#module-pprint) module’s 

[class and its](../library/pprint.html#pprint.PrettyPrinter)

`PrettyPrinter`[, and](../library/pprint.html#pprint.pformat)

`pformat()`[functions have a new option,](../library/pprint.html#pprint.pprint)

`pprint()`*compact*, that controls how the output is formatted. Currently setting

*compact*to

`True` means that sequences will be printed with as many
sequence elements as will fit within *width*on each (indented) line. (Contributed by Serhiy Storchaka in

[bpo-19132](https://bugs.python.org/issue?@action=redirect&bpo=19132).)

Long strings are now wrapped using Python’s normal line continuation
syntax.  (Contributed by Antoine Pitrou in [bpo-17150](https://bugs.python.org/issue?@action=redirect&bpo=17150).)

### pty[¶](#pty)

[ pty.spawn()](../library/pty.html#pty.spawn) now returns the status value from 

[on the child process, instead of](../library/os.html#os.waitpid)

`os.waitpid()``None`.  (Contributed by Gregory P. Smith.)### pydoc[¶](#pydoc)

The [ pydoc](../library/pydoc.html#module-pydoc) module is now based directly on the 

[introspection API, allowing it to provide signature information for a wider variety of callable objects. This change also means that](../library/inspect.html#inspect.signature)

`inspect.signature()``__wrapped__`
attributes are now taken into account when displaying help information.
(Contributed by Larry Hastings in [bpo-19674](https://bugs.python.org/issue?@action=redirect&bpo=19674).)

The [ pydoc](../library/pydoc.html#module-pydoc) module no longer displays the 

`self` parameter for
already bound methods. Instead, it aims to always display the exact current
signature of the supplied callable.  (Contributed by Larry Hastings in
[bpo-20710](https://bugs.python.org/issue?@action=redirect&bpo=20710).)

In addition to the changes that have been made to [ pydoc](../library/pydoc.html#module-pydoc) directly,
its handling of custom 

`__dir__` methods and various descriptor
behaviours has also been improved substantially by the underlying changes in
the [module.](../library/inspect.html#module-inspect)

`inspect`As the [ help()](../library/functions.html#help) builtin is based on 

[, the above changes also affect the behaviour of](../library/pydoc.html#module-pydoc)

`pydoc``help()`.### re[¶](#re)

New [ fullmatch()](../library/re.html#re.fullmatch) function and 

[method anchor the pattern at both ends of the string to match. This provides a way to be explicit about the goal of the match, which avoids a class of subtle bugs where](../library/re.html#re.Pattern.fullmatch)

`Pattern.fullmatch()``$` characters get lost during code changes or the addition of alternatives
to an existing regular expression.  (Contributed by Matthew Barnett in
[bpo-16203](https://bugs.python.org/issue?@action=redirect&bpo=16203).)

The repr of [regex objects](../library/re.html#re-objects) now includes the pattern
and the flags; the repr of [match objects](../library/re.html#match-objects) now
includes the start, end, and the part of the string that matched.  (Contributed
by Hugo Lopes Tavares and Serhiy Storchaka in [bpo-13592](https://bugs.python.org/issue?@action=redirect&bpo=13592) and
[bpo-17087](https://bugs.python.org/issue?@action=redirect&bpo=17087).)

### resource[¶](#resource)

New [ prlimit()](../library/resource.html#resource.prlimit) function, available on Linux platforms with a
kernel version of 2.6.36 or later and glibc of 2.13 or later, provides the
ability to query or set the resource limits for processes other than the one
making the call.  (Contributed by Christian Heimes in 

[bpo-16595](https://bugs.python.org/issue?@action=redirect&bpo=16595).)

On Linux kernel version 2.6.36 or later, there are also some new
Linux specific constants: [ RLIMIT_MSGQUEUE](../library/resource.html#resource.RLIMIT_MSGQUEUE),

[,](../library/resource.html#resource.RLIMIT_NICE)

`RLIMIT_NICE`[,](../library/resource.html#resource.RLIMIT_RTPRIO)

`RLIMIT_RTPRIO`[, and](../library/resource.html#resource.RLIMIT_RTTIME)

`RLIMIT_RTTIME`[. (Contributed by Christian Heimes in](../library/resource.html#resource.RLIMIT_SIGPENDING)

`RLIMIT_SIGPENDING`[bpo-19324](https://bugs.python.org/issue?@action=redirect&bpo=19324).)

On FreeBSD version 9 and later, there some new FreeBSD specific constants:
[ RLIMIT_SBSIZE](../library/resource.html#resource.RLIMIT_SBSIZE), 

[, and](../library/resource.html#resource.RLIMIT_SWAP)

`RLIMIT_SWAP`[. (Contributed by Claudiu Popa in](../library/resource.html#resource.RLIMIT_NPTS)

`RLIMIT_NPTS`[bpo-19343](https://bugs.python.org/issue?@action=redirect&bpo=19343).)

### select[¶](#select)

[ epoll](../library/select.html#select.epoll) objects now support the context management protocol.
When used in a 

[statement, the](../reference/compound_stmts.html#with)

`with`[method will be called automatically at the end of the block. (Contributed by Serhiy Storchaka in](../library/select.html#select.epoll.close)

`close()`[bpo-16488](https://bugs.python.org/issue?@action=redirect&bpo=16488).)

[ devpoll](../library/select.html#select.devpoll) objects now have 

[and](../library/select.html#select.devpoll.fileno)

`fileno()`[methods, as well as a new attribute](../library/select.html#select.devpoll.close)

`close()`[. (Contributed by Victor Stinner in](../library/select.html#select.devpoll.closed)

`closed`[bpo-18794](https://bugs.python.org/issue?@action=redirect&bpo=18794).)

### shelve[¶](#shelve)

[ Shelf](../library/shelve.html#shelve.Shelf) instances may now be used in 

[statements, and will be automatically closed at the end of the](../reference/compound_stmts.html#with)

`with``with` block.
(Contributed by Filip Gruszczyński in [bpo-13896](https://bugs.python.org/issue?@action=redirect&bpo=13896).)

### shutil[¶](#shutil)

[ copyfile()](../library/shutil.html#shutil.copyfile) now raises a specific 

[subclass,](../library/shutil.html#shutil.Error)

`Error`[, when the source and destination are the same file, which allows an application to take appropriate action on this specific error. (Contributed by Atsuo Ishimoto and Hynek Schlawack in](../library/shutil.html#shutil.SameFileError)

`SameFileError`[bpo-1492704](https://bugs.python.org/issue?@action=redirect&bpo=1492704).)

### smtpd[¶](#smtpd)

The `SMTPServer` and `SMTPChannel` classes now
accept a *map* keyword argument which, if specified, is passed in to
`asynchat.async_chat` as its *map* argument.  This allows an application
to avoid affecting the global socket map.  (Contributed by Vinay Sajip in
[bpo-11959](https://bugs.python.org/issue?@action=redirect&bpo=11959).)

### smtplib[¶](#smtplib)

[ SMTPException](../library/smtplib.html#smtplib.SMTPException) is now a subclass of 

[, which allows both socket level errors and SMTP protocol level errors to be caught in one try/except statement by code that only cares whether or not an error occurred. (Contributed by Ned Jackson Lovely in](../library/exceptions.html#OSError)

`OSError`[bpo-2118](https://bugs.python.org/issue?@action=redirect&bpo=2118).)

### socket[¶](#socket)

The socket module now supports the [ CAN_BCM](../library/socket.html#socket.CAN_BCM) protocol on
platforms that support it.  (Contributed by Brian Thorne in 

[bpo-15359](https://bugs.python.org/issue?@action=redirect&bpo=15359).)

Socket objects have new methods to get or set their [inheritable flag](../library/os.html#fd-inheritance), [ get_inheritable()](../library/socket.html#socket.socket.get_inheritable) and

[.](../library/socket.html#socket.socket.set_inheritable)

`set_inheritable()`The `socket.AF_*` and `socket.SOCK_*` constants are now enumeration values
using the new [ enum](../library/enum.html#module-enum) module.  This allows meaningful names to be printed
during debugging, instead of integer “magic numbers”.

The [ AF_LINK](../library/socket.html#socket.AF_LINK) constant is now available on BSD and OSX.

[ inet_pton()](../library/socket.html#socket.inet_pton) and 

[are now supported on Windows. (Contributed by Atsuo Ishimoto in](../library/socket.html#socket.inet_ntop)

`inet_ntop()`[bpo-7171](https://bugs.python.org/issue?@action=redirect&bpo=7171).)

### sqlite3[¶](#sqlite3)

A new boolean parameter to the [ connect()](../library/sqlite3.html#sqlite3.connect) function, 

*uri*, can be used to indicate that the

*database*parameter is a

`uri` (see the [SQLite URI documentation](https://www.sqlite.org/uri.html)). (Contributed by poq in

[bpo-13773](https://bugs.python.org/issue?@action=redirect&bpo=13773).)

### ssl[¶](#ssl)

[ PROTOCOL_TLSv1_1](../library/ssl.html#ssl.PROTOCOL_TLSv1_1) and 

[(TLSv1.1 and TLSv1.2 support) have been added; support for these protocols is only available if Python is linked with OpenSSL 1.0.1 or later. (Contributed by Michele Orrù and Antoine Pitrou in](../library/ssl.html#ssl.PROTOCOL_TLSv1_2)

`PROTOCOL_TLSv1_2`[bpo-16692](https://bugs.python.org/issue?@action=redirect&bpo=16692).)

New function [ create_default_context()](../library/ssl.html#ssl.create_default_context) provides a standard way to
obtain an 

[whose settings are intended to be a reasonable balance between compatibility and security. These settings are more stringent than the defaults provided by the](../library/ssl.html#ssl.SSLContext)

`SSLContext``SSLContext`
constructor, and may be adjusted in the future, without prior deprecation, if
best-practice security requirements change.  The new recommended best
practice for using stdlib libraries that support SSL is to use
`create_default_context()` to obtain an `SSLContext`
object, modify it if needed, and then pass it as the *context*argument of the appropriate stdlib API. (Contributed by Christian Heimes in

[bpo-19689](https://bugs.python.org/issue?@action=redirect&bpo=19689).)

[ SSLContext](../library/ssl.html#ssl.SSLContext) method 

[accepts a new optional argument](../library/ssl.html#ssl.SSLContext.load_verify_locations)

`load_verify_locations()`*cadata*, which can be used to provide PEM or DER encoded certificates directly via strings or bytes, respectively. (Contributed by Christian Heimes in

[bpo-18138](https://bugs.python.org/issue?@action=redirect&bpo=18138).)

New function [ get_default_verify_paths()](../library/ssl.html#ssl.get_default_verify_paths) returns
a named tuple of the paths and environment variables that the

[method uses to set OpenSSL’s default](../library/ssl.html#ssl.SSLContext.set_default_verify_paths)

`set_default_verify_paths()``cafile` and `capath`.  This can be an aid in
debugging default verification issues.  (Contributed by Christian Heimes
in [bpo-18143](https://bugs.python.org/issue?@action=redirect&bpo=18143).)

[ SSLContext](../library/ssl.html#ssl.SSLContext) has a new method,

[, that reports the number of loaded](../library/ssl.html#ssl.SSLContext.cert_store_stats)

`cert_store_stats()``X.509` certs, `X.509 CA` certs, and certificate revocation lists
(`crl`s), as well as a [method that returns a list of the loaded](../library/ssl.html#ssl.SSLContext.get_ca_certs)

`get_ca_certs()``CA` certificates.  (Contributed by Christian
Heimes in [bpo-18147](https://bugs.python.org/issue?@action=redirect&bpo=18147).)

If OpenSSL 0.9.8 or later is available, [ SSLContext](../library/ssl.html#ssl.SSLContext) has a new
attribute 

[that can be used to control the certificate verification process by setting it to some combination of the new constants](../library/ssl.html#ssl.SSLContext.verify_flags)

`verify_flags`[,](../library/ssl.html#ssl.VERIFY_DEFAULT)

`VERIFY_DEFAULT`[,](../library/ssl.html#ssl.VERIFY_CRL_CHECK_LEAF)

`VERIFY_CRL_CHECK_LEAF`[, or](../library/ssl.html#ssl.VERIFY_CRL_CHECK_CHAIN)

`VERIFY_CRL_CHECK_CHAIN`[. OpenSSL does not do any CRL verification by default. (Contributed by Christien Heimes in](../library/ssl.html#ssl.VERIFY_X509_STRICT)

`VERIFY_X509_STRICT`[bpo-8813](https://bugs.python.org/issue?@action=redirect&bpo=8813).)

New [ SSLContext](../library/ssl.html#ssl.SSLContext) method 

[loads a set of default “certificate authority” (CA) certificates from default locations, which vary according to the platform. It can be used to load both TLS web server authentication certificates (](../library/ssl.html#ssl.SSLContext.load_default_certs)

`load_default_certs()``purpose=`[) for a client to use to verify a server, and certificates for a server to use in verifying client certificates (](../library/ssl.html#ssl.Purpose.SERVER_AUTH)

`SERVER_AUTH``purpose=`[). (Contributed by Christian Heimes in](../library/ssl.html#ssl.Purpose.CLIENT_AUTH)

`CLIENT_AUTH`[bpo-19292](https://bugs.python.org/issue?@action=redirect&bpo=19292).)

Two new windows-only functions, [ enum_certificates()](../library/ssl.html#ssl.enum_certificates) and

[provide the ability to retrieve certificates, certificate information, and CRLs from the Windows cert store. (Contributed by Christian Heimes in](../library/ssl.html#ssl.enum_crls)

`enum_crls()`[bpo-17134](https://bugs.python.org/issue?@action=redirect&bpo=17134).)

Support for server-side SNI (Server Name Indication) using the new
[ ssl.SSLContext.set_servername_callback()](../library/ssl.html#ssl.SSLContext.set_servername_callback) method.
(Contributed by Daniel Black in 

[bpo-8109](https://bugs.python.org/issue?@action=redirect&bpo=8109).)

The dictionary returned by [ SSLSocket.getpeercert()](../library/ssl.html#ssl.SSLSocket.getpeercert) contains additional

`X509v3` extension items: `crlDistributionPoints`, `calIssuers`, and
`OCSP` URIs.  (Contributed by Christian Heimes in [bpo-18379](https://bugs.python.org/issue?@action=redirect&bpo=18379).)

### stat[¶](#stat)

The [ stat](../library/stat.html#module-stat) module is now backed by a C implementation in 

`_stat`. A C
implementation is required as most of the values aren’t standardized and
are platform-dependent.  (Contributed by Christian Heimes in [bpo-11016](https://bugs.python.org/issue?@action=redirect&bpo=11016).)

The module supports new [ ST_MODE](../library/stat.html#stat.ST_MODE) flags, 

[,](../library/stat.html#stat.S_IFDOOR)

`S_IFDOOR`[, and](../library/stat.html#stat.S_IFPORT)

`S_IFPORT`[. (Contributed by Christian Hiemes in](../library/stat.html#stat.S_IFWHT)

`S_IFWHT`[bpo-11016](https://bugs.python.org/issue?@action=redirect&bpo=11016).)

### struct[¶](#struct)

New function [ iter_unpack](../library/struct.html#struct.iter_unpack) and a new

[method on compiled formats provide streamed unpacking of a buffer containing repeated instances of a given format of data. (Contributed by Antoine Pitrou in](../library/struct.html#struct.Struct.iter_unpack)

`struct.Struct.iter_unpack()`[bpo-17804](https://bugs.python.org/issue?@action=redirect&bpo=17804).)

### subprocess[¶](#subprocess)

[ check_output()](../library/subprocess.html#subprocess.check_output) now accepts an 

*input*argument that can be used to provide the contents of

`stdin` for the command that is run.
(Contributed by Zack Weinberg in [bpo-16624](https://bugs.python.org/issue?@action=redirect&bpo=16624).)

[ getoutput()](../library/subprocess.html#subprocess.getoutput) and 

[now work on Windows. This change was actually inadvertently made in 3.3.4. (Contributed by Tim Golden in](../library/subprocess.html#subprocess.getstatusoutput)

`getstatusoutput()`[bpo-10197](https://bugs.python.org/issue?@action=redirect&bpo=10197).)

### sunau[¶](#sunau)

The `getparams()` method now returns a namedtuple rather than a
plain tuple.  (Contributed by Claudiu Popa in [bpo-18901](https://bugs.python.org/issue?@action=redirect&bpo=18901).)

`sunau.open()` now supports the context management protocol: when used in a
[ with](../reference/compound_stmts.html#with) block, the 

`close` method of the returned object will be
called automatically at the end of the block.  (Contributed by Serhiy Storchaka
in [bpo-18878](https://bugs.python.org/issue?@action=redirect&bpo=18878).)

`AU_write.setsampwidth()` now supports 24 bit samples, thus adding
support for writing 24 sample using the module.  (Contributed by
Serhiy Storchaka in [bpo-19261](https://bugs.python.org/issue?@action=redirect&bpo=19261).)

The `writeframesraw()` and
`writeframes()` methods now accept any [bytes-like
object](../glossary.html#term-bytes-like-object).  (Contributed by Serhiy Storchaka in [bpo-8311](https://bugs.python.org/issue?@action=redirect&bpo=8311).)

### sys[¶](#sys)

New function [ sys.getallocatedblocks()](../library/sys.html#sys.getallocatedblocks) returns the current number of
blocks allocated by the interpreter.  (In CPython with the default

`--with-pymalloc` setting, this is allocations made through the
[API.) This can be useful for tracking memory leaks, especially if automated via a test suite. (Contributed by Antoine Pitrou in](../c-api/memory.html#c.PyObject_Malloc)

`PyObject_Malloc()`[bpo-13390](https://bugs.python.org/issue?@action=redirect&bpo=13390).)

When the Python interpreter starts in [interactive mode](../tutorial/interpreter.html#tut-interactive), it checks for an [ __interactivehook__](../library/sys.html#sys.__interactivehook__) attribute
on the 

[module. If the attribute exists, its value is called with no arguments just before interactive mode is started. The check is made after the](../library/sys.html#module-sys)

`sys`[file is read, so it can be set there. The](../using/cmdline.html#envvar-PYTHONSTARTUP)

`PYTHONSTARTUP`[module](../library/site.html#module-site)

`site`[sets it](../library/site.html#rlcompleter-config)to a function that enables tab completion and history saving (in

`~/.python-history`) if the platform
supports [. If you do not want this (new) behavior, you can override it in](../library/readline.html#module-readline)

`readline``PYTHONSTARTUP`, [, or](../library/site.html#module-sitecustomize)

`sitecustomize`[by deleting this attribute from](../library/site.html#module-usercustomize)

`usercustomize``sys` (or setting it
to some other callable).  (Contributed by Éric Araujo and Antoine Pitrou in
[bpo-5845](https://bugs.python.org/issue?@action=redirect&bpo=5845).)

### tarfile[¶](#tarfile)

The [ tarfile](../library/tarfile.html#module-tarfile) module now supports a simple 

[Command-Line Interface](../library/tarfile.html#tarfile-commandline)when called as a script directly or via

`-m`.  This can be used to create and
extract tarfile archives.  (Contributed by Berker Peksag in [bpo-13477](https://bugs.python.org/issue?@action=redirect&bpo=13477).)

### textwrap[¶](#textwrap)

The [ TextWrapper](../library/textwrap.html#textwrap.TextWrapper) class has two new attributes/constructor
arguments: 

[, which limits the number of lines in the output, and](../library/textwrap.html#textwrap.TextWrapper.max_lines)

`max_lines`[, which is a string that will appear at the end of the output if it has been truncated because of](../library/textwrap.html#textwrap.TextWrapper.placeholder)

`placeholder`*max_lines*. Building on these capabilities, a new convenience function

[collapses all of the whitespace in the input to single spaces and produces a single line of a given](../library/textwrap.html#textwrap.shorten)

`shorten()`*width*that ends with the

*placeholder*(by default,

`[...]`).  (Contributed by Antoine Pitrou and
Serhiy Storchaka in [bpo-18585](https://bugs.python.org/issue?@action=redirect&bpo=18585)and

[bpo-18725](https://bugs.python.org/issue?@action=redirect&bpo=18725).)

### threading[¶](#threading)

The [ Thread](../library/threading.html#threading.Thread) object representing the main thread can be
obtained from the new 

[function. In normal conditions this will be the thread from which the Python interpreter was started. (Contributed by Andrew Svetlov in](../library/threading.html#threading.main_thread)

`main_thread()`[bpo-18882](https://bugs.python.org/issue?@action=redirect&bpo=18882).)

### traceback[¶](#traceback)

A new [ traceback.clear_frames()](../library/traceback.html#traceback.clear_frames) function takes a traceback object
and clears the local variables in all of the frames it references,
reducing the amount of memory consumed.  (Contributed by Andrew Kuchling in

[bpo-1565525](https://bugs.python.org/issue?@action=redirect&bpo=1565525).)

### types[¶](#types)

A new [ DynamicClassAttribute()](../library/types.html#types.DynamicClassAttribute) descriptor provides a way to define
an attribute that acts normally when looked up through an instance object, but
which is routed to the 

*class*

`__getattr__` when looked up through the
class.  This allows one to have properties active on a class, and have virtual
attributes on the class with the same name (see [for an example). (Contributed by Ethan Furman in](../library/enum.html#module-enum)

`enum`[bpo-19030](https://bugs.python.org/issue?@action=redirect&bpo=19030).)

### urllib[¶](#urllib)

[ urllib.request](../library/urllib.request.html#module-urllib.request) now supports 

`data:` URLs via the
[class. (Contributed by Mathias Panzenböck in](../library/urllib.request.html#urllib.request.DataHandler)

`DataHandler`[bpo-16423](https://bugs.python.org/issue?@action=redirect&bpo=16423).)

The http method that will be used by a [ Request](../library/urllib.request.html#urllib.request.Request) class
can now be specified by setting a 

[class attribute on the subclass. (Contributed by Jason R Coombs in](../library/urllib.request.html#urllib.request.Request.method)

`method`[bpo-18978](https://bugs.python.org/issue?@action=redirect&bpo=18978).)

[ Request](../library/urllib.request.html#urllib.request.Request) objects are now reusable: if the

[or](../library/urllib.request.html#urllib.request.Request.full_url)

`full_url`[attributes are modified, all relevant internal properties are updated. This means, for example, that it is now possible to use the same](../library/urllib.request.html#urllib.request.Request.data)

`data``Request` object in more than one
[call with different](../library/urllib.request.html#urllib.request.OpenerDirector.open)

`OpenerDirector.open()`*data*arguments, or to modify a

`Request`‘s `url` rather than recomputing it
from scratch.  There is also a new
[method that can be used to remove headers from a](../library/urllib.request.html#urllib.request.Request.remove_header)

`remove_header()``Request`.  (Contributed by Alexey
Kachayev in [bpo-16464](https://bugs.python.org/issue?@action=redirect&bpo=16464), Daniel Wozniak in

[bpo-17485](https://bugs.python.org/issue?@action=redirect&bpo=17485), and Damien Brecht and Senthil Kumaran in

[bpo-17272](https://bugs.python.org/issue?@action=redirect&bpo=17272).)

[ HTTPError](../library/urllib.error.html#urllib.error.HTTPError) objects now have a

[attribute that provides access to the HTTP response headers associated with the error. (Contributed by Berker Peksag in](../library/urllib.error.html#urllib.error.HTTPError.headers)

`headers`[bpo-15701](https://bugs.python.org/issue?@action=redirect&bpo=15701).)

### unittest[¶](#unittest)

The [ TestCase](../library/unittest.html#unittest.TestCase) class has a new method,

[, that produces a context manager whose](../library/unittest.html#unittest.TestCase.subTest)

`subTest()`[block becomes a “sub-test”. This context manager allows a test method to dynamically generate subtests by, say, calling the](../reference/compound_stmts.html#with)

`with``subTest`
context manager inside a loop.  A single test method can thereby produce an
indefinite number of separately identified and separately counted tests, all of
which will run even if one or more of them fail.  For example:```
class NumbersTest(unittest.TestCase):
    def test_even(self):
        for i in range(6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)
```
will result in six subtests, each identified in the unittest verbose output
with a label consisting of the variable name `i` and a particular value for
that variable (`i=0`, `i=1`, etc).  See [Distinguishing test iterations using subtests](../library/unittest.html#subtests) for the full
version of this example.  (Contributed by Antoine Pitrou in [bpo-16997](https://bugs.python.org/issue?@action=redirect&bpo=16997).)

[ unittest.main()](../library/unittest.html#unittest.main) now accepts an iterable of test names for

*defaultTest*, where previously it only accepted a single test name as a string. (Contributed by Jyrki Pulliainen in

[bpo-15132](https://bugs.python.org/issue?@action=redirect&bpo=15132).)

If [ SkipTest](../library/unittest.html#unittest.SkipTest) is raised during test discovery (that is, at the
module level in the test file), it is now reported as a skip instead of an
error.  (Contributed by Zach Ware in 

[bpo-16935](https://bugs.python.org/issue?@action=redirect&bpo=16935).)

[ discover()](../library/unittest.html#unittest.TestLoader.discover) now sorts the discovered files to provide
consistent test ordering.  (Contributed by Martin Melin and Jeff Ramnani in

[bpo-16709](https://bugs.python.org/issue?@action=redirect&bpo=16709).)

[ TestSuite](../library/unittest.html#unittest.TestSuite) now drops references to tests as soon as the test
has been run, if the test is successful.  On Python interpreters that do
garbage collection, this allows the tests to be garbage collected if nothing
else is holding a reference to the test.  It is possible to override this
behavior by creating a 

`TestSuite` subclass that defines a
custom `_removeTestAtIndex` method.  (Contributed by Tom Wardill, Matt
McClure, and Andrew Svetlov in [bpo-11798](https://bugs.python.org/issue?@action=redirect&bpo=11798).)

A new test assertion context-manager, [ assertLogs()](../library/unittest.html#unittest.TestCase.assertLogs),
will ensure that a given block of code emits a log message using the

[module. By default the message can come from any logger and have a priority of](../library/logging.html#module-logging)

`logging``INFO` or higher, but both the logger name and an
alternative minimum logging level may be specified.  The object returned by the
context manager can be queried for the [s and/or formatted messages that were logged. (Contributed by Antoine Pitrou in](../library/logging.html#logging.LogRecord)

`LogRecord`[bpo-18937](https://bugs.python.org/issue?@action=redirect&bpo=18937).)

Test discovery now works with namespace packages (Contributed by Claudiu Popa
in [bpo-17457](https://bugs.python.org/issue?@action=redirect&bpo=17457).)

[ unittest.mock](../library/unittest.mock.html#module-unittest.mock) objects now inspect their specification signatures when
matching calls, which means an argument can now be matched by either position
or name, instead of only by position.  (Contributed by Antoine Pitrou in

[bpo-17015](https://bugs.python.org/issue?@action=redirect&bpo=17015).)

[ mock_open()](../library/unittest.mock.html#unittest.mock.mock_open) objects now have 

`readline` and `readlines`
methods.  (Contributed by Toshio Kuratomi in [bpo-17467](https://bugs.python.org/issue?@action=redirect&bpo=17467).)

### venv[¶](#venv)

[ venv](../library/venv.html#module-venv) now includes activation scripts for the 

`csh` and `fish`
shells.  (Contributed by Andrew Svetlov in [bpo-15417](https://bugs.python.org/issue?@action=redirect&bpo=15417).)

[ EnvBuilder](../library/venv.html#venv.EnvBuilder) and the 

[convenience function take a new keyword argument](../library/venv.html#venv.create)

`create()`*with_pip*, which defaults to

`False`, that
controls whether or not `EnvBuilder` ensures that `pip` is
installed in the virtual environment.  (Contributed by Nick Coghlan in
[bpo-19552](https://bugs.python.org/issue?@action=redirect&bpo=19552)as part of the

[implementation.)](https://peps.python.org/pep-0453/)

**PEP 453**### wave[¶](#wave)

The [ getparams()](../library/wave.html#wave.Wave_read.getparams) method now returns a namedtuple rather
than a plain tuple.  (Contributed by Claudiu Popa in 

[bpo-17487](https://bugs.python.org/issue?@action=redirect&bpo=17487).)

[ wave.open()](../library/wave.html#wave.open) now supports the context management protocol.  (Contributed
by Claudiu Popa in 

[bpo-17616](https://bugs.python.org/issue?@action=redirect&bpo=17616).)

[ wave](../library/wave.html#module-wave) can now 

[write output to unseekable files](../library/wave.html#wave-write-objects). (Contributed by David Jones, Guilherme Polo, and Serhiy Storchaka in

[bpo-5202](https://bugs.python.org/issue?@action=redirect&bpo=5202).)

The [ writeframesraw()](../library/wave.html#wave.Wave_write.writeframesraw) and

[methods now accept any](../library/wave.html#wave.Wave_write.writeframes)

`writeframes()`[bytes-like object](../glossary.html#term-bytes-like-object). (Contributed by Serhiy Storchaka in

[bpo-8311](https://bugs.python.org/issue?@action=redirect&bpo=8311).)

### weakref[¶](#weakref)

New [ WeakMethod](../library/weakref.html#weakref.WeakMethod) class simulates weak references to bound
methods.  (Contributed by Antoine Pitrou in 

[bpo-14631](https://bugs.python.org/issue?@action=redirect&bpo=14631).)

New [ finalize](../library/weakref.html#weakref.finalize) class makes it possible to register a callback
to be invoked when an object is garbage collected, without needing to
carefully manage the lifecycle of the weak reference itself.  (Contributed by
Richard Oudkerk in 

[bpo-15528](https://bugs.python.org/issue?@action=redirect&bpo=15528).)

The callback, if any, associated with a [ ref](../library/weakref.html#weakref.ref) is now
exposed via the 

[attribute. (Contributed by Mark Dickinson in](../library/weakref.html#weakref.ref.__callback__)

`__callback__`[bpo-17643](https://bugs.python.org/issue?@action=redirect&bpo=17643).)

### xml.etree[¶](#xml-etree)

A new parser, [ XMLPullParser](../library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLPullParser), allows a
non-blocking applications to parse XML documents.  An example can be
seen at 

[Pull API for non-blocking parsing](../library/xml.etree.elementtree.html#elementtree-pull-parsing). (Contributed by Antoine Pitrou in

[bpo-17741](https://bugs.python.org/issue?@action=redirect&bpo=17741).)

The `xml.etree.ElementTree`[ tostring()](../library/xml.etree.elementtree.html#xml.etree.ElementTree.tostring) and

[functions, and the](../library/xml.etree.elementtree.html#xml.etree.ElementTree.tostringlist)

`tostringlist()`

`ElementTree`[method, now have a](../library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree.write)

`write()`*short_empty_elements*

[keyword-only parameter](../glossary.html#keyword-only-parameter)providing control over whether elements with no content are written in abbreviated (

`<tag />`) or expanded (`<tag></tag>`) form.  (Contributed by
Ariel Poliak and Serhiy Storchaka in [bpo-14377](https://bugs.python.org/issue?@action=redirect&bpo=14377).)

### zipfile[¶](#zipfile)

The [ writepy()](../library/zipfile.html#zipfile.PyZipFile.writepy) method of the

[class has a new](../library/zipfile.html#zipfile.PyZipFile)

`PyZipFile`*filterfunc*option that can be used to control which directories and files are added to the archive. For example, this could be used to exclude test files from the archive. (Contributed by Christian Tismer in

[bpo-19274](https://bugs.python.org/issue?@action=redirect&bpo=19274).)

The *allowZip64* parameter to [ ZipFile](../library/zipfile.html#zipfile.ZipFile) and

[is now](../library/zipfile.html#zipfile.PyZipFile)

`PyZipFile``True` by default.  (Contributed by
William Mallard in [bpo-17201](https://bugs.python.org/issue?@action=redirect&bpo=17201).)

## CPython Implementation Changes[¶](#cpython-implementation-changes)

### PEP 445: Customization of CPython Memory Allocators[¶](#pep-445-customization-of-cpython-memory-allocators)

[ PEP 445](https://peps.python.org/pep-0445/) adds new C level interfaces to customize memory allocation in
the CPython interpreter.

See also

- **PEP 445**
- PEP written and implemented by Victor Stinner. 

### PEP 442: Safe Object Finalization[¶](#pep-442-safe-object-finalization)

[ PEP 442](https://peps.python.org/pep-0442/) removes the current limitations and quirks of object finalization
in CPython. With it, objects with 

[methods, as well as generators with](../reference/datamodel.html#object.__del__)

`__del__()`[clauses, can be finalized when they are part of a reference cycle.](../reference/compound_stmts.html#finally)

`finally`As part of this change, module globals are no longer forcibly set to
[ None](../library/constants.html#None) during interpreter shutdown in most cases, instead relying
on the normal operation of the cyclic garbage collector.  This avoids a
whole class of interpreter-shutdown-time errors, usually involving

`__del__` methods, that have plagued Python since the cyclic GC
was first introduced.See also

- **PEP 442**
- PEP written and implemented by Antoine Pitrou. 

### PEP 456: Secure and Interchangeable Hash Algorithm[¶](#pep-456-secure-and-interchangeable-hash-algorithm)

[ PEP 456](https://peps.python.org/pep-0456/) follows up on earlier security fix work done on Python’s hash
algorithm to address certain DOS attacks to which public facing APIs backed by
dictionary lookups may be subject.  (See 

[bpo-14621](https://bugs.python.org/issue?@action=redirect&bpo=14621)for the start of the current round of improvements.) The PEP unifies CPython’s hash code to make it easier for a packager to substitute a different hash algorithm, and switches Python’s default implementation to a SipHash implementation on platforms that have a 64 bit data type. Any performance differences in comparison with the older FNV algorithm are trivial.

The PEP adds additional fields to the [ sys.hash_info](../library/sys.html#sys.hash_info) named tuple to
describe the hash algorithm in use by the currently executing binary.  Otherwise,
the PEP does not alter any existing CPython APIs.

### PEP 436: Argument Clinic[¶](#pep-436-argument-clinic)

“Argument Clinic” ([ PEP 436](https://peps.python.org/pep-0436/)) is now part of the CPython build process
and can be used to simplify the process of defining and maintaining
accurate signatures for builtins and standard library extension modules
implemented in C.

Some standard library extension modules have been converted to use Argument
Clinic in Python 3.4, and [ pydoc](../library/pydoc.html#module-pydoc) and 

[have been updated accordingly.](../library/inspect.html#module-inspect)

`inspect`It is expected that signature metadata for programmatic introspection will be added to additional callables implemented in C as part of Python 3.4 maintenance releases.

Note

The Argument Clinic PEP is not fully up to date with the state of the implementation. This has been deemed acceptable by the release manager and core development team in this case, as Argument Clinic will not be made available as a public API for third party use in Python 3.4.

See also

- **PEP 436**
- PEP written and implemented by Larry Hastings. 

### Other Build and C API Changes[¶](#other-build-and-c-api-changes)

- The new - `PyType_GetSlot()`- [bpo-17162](https://bugs.python.org/issue?@action=redirect&bpo=17162).)
- The new - `Py_SetStandardStreamEncoding()`pre-initialization API allows applications embedding the CPython interpreter to reliably force a particular encoding and error handler for the standard streams. (Contributed by Bastien Montagne and Nick Coghlan in- [bpo-16129](https://bugs.python.org/issue?@action=redirect&bpo=16129).)
- Most Python C APIs that don’t mutate string arguments are now correctly marked as accepting - `const char *`rather than- `char *`. (Contributed by Serhiy Storchaka in- [bpo-1772673](https://bugs.python.org/issue?@action=redirect&bpo=1772673).)
- A new shell version of - `python-config`can be used even when a python interpreter is not available (for example, in cross compilation scenarios).
- `PyUnicode_FromFormat()`- `%s`,- `%A`,- `%U`,- `%V`,- `%S`, and- `%R`. (Contributed by Ysj Ray and Victor Stinner in- [bpo-7330](https://bugs.python.org/issue?@action=redirect&bpo=7330).)
- New function - `PyStructSequence_InitType2()`- `PyStructSequence_InitType()`- `0`on success and- `-1`on failure.
- The CPython source can now be compiled using the address sanity checking features of recent versions of GCC and clang: the false alarms in the small object allocator have been silenced. (Contributed by Dhiru Kholia in - [bpo-18596](https://bugs.python.org/issue?@action=redirect&bpo=18596).)
- The Windows build now uses - [Address Space Layout Randomization](https://en.wikipedia.org/wiki/Address_space_layout_randomization)and- [Data Execution Prevention](https://en.wikipedia.org/wiki/Data_Execution_Prevention). (Contributed by Christian Heimes in- [bpo-16632](https://bugs.python.org/issue?@action=redirect&bpo=16632).)
- New function - `PyObject_LengthHint()`- `operator.length_hint()`- [bpo-16148](https://bugs.python.org/issue?@action=redirect&bpo=16148).)

### Other Improvements[¶](#other-improvements)

- The - [python](../using/cmdline.html#using-on-cmdline)command has a new- [option](../using/cmdline.html#using-on-misc-options),- `-I`, which causes it to run in “isolated mode”, which means that- `sys.path`- `site-packages`directory, and all- `PYTHON*`environment variables are ignored (it implies both- `-s`and- `-E`). Other restrictions may also be applied in the future, with the goal being to isolate the execution of a script from the user’s environment. This is appropriate, for example, when Python is used to run a system script. On most POSIX systems it can and should be used in the- `#!`line of system scripts. (Contributed by Christian Heimes in- [bpo-16499](https://bugs.python.org/issue?@action=redirect&bpo=16499).)
- Tab-completion is now enabled by default in the interactive interpreter on systems that support - `readline`- `~/.python-history`. (Contributed by Antoine Pitrou and Éric Araujo in- [bpo-5845](https://bugs.python.org/issue?@action=redirect&bpo=5845).)
- Invoking the Python interpreter with - `--version`now outputs the version to standard output instead of standard error (- [bpo-18338](https://bugs.python.org/issue?@action=redirect&bpo=18338)). Similar changes were made to- `argparse`- [bpo-18920](https://bugs.python.org/issue?@action=redirect&bpo=18920)) and other modules that have script-like invocation capabilities (- [bpo-18922](https://bugs.python.org/issue?@action=redirect&bpo=18922)).
- The CPython Windows installer now adds - `.py`to the- `PATHEXT`variable when extensions are registered, allowing users to run a python script at the windows command prompt by just typing its name without the- `.py`extension. (Contributed by Paul Moore in- [bpo-18569](https://bugs.python.org/issue?@action=redirect&bpo=18569).)
- A new - `make`target- [coverage-report](https://devguide.python.org/coverage/#measuring-coverage-of-c-code-with-gcov-and-lcov)will build python, run the test suite, and generate an HTML coverage report for the C codebase using- `gcov`and- [lcov](https://github.com/linux-test-project/lcov).
- The - `-R`option to the- [python regression test suite](../library/test.html#regrtest)now also checks for memory allocation leaks, using- `sys.getallocatedblocks()`- [bpo-13390](https://bugs.python.org/issue?@action=redirect&bpo=13390).)
- `python -m`now works with namespace packages.
- The - `stat`
- Loading multiple python modules from a single OS module ( - `.so`,- `.dll`) now works correctly (previously it silently returned the first python module in the file). (Contributed by Václav Šmilauer in- [bpo-16421](https://bugs.python.org/issue?@action=redirect&bpo=16421).)
- A new opcode, - `LOAD_CLASSDEREF`, has been added to fix a bug in the loading of free variables in class bodies that could be triggered by certain uses of- [__prepare__](../reference/datamodel.html#prepare). (Contributed by Benjamin Peterson in- [bpo-17853](https://bugs.python.org/issue?@action=redirect&bpo=17853).)
- A number of MemoryError-related crashes were identified and fixed by Victor Stinner using his - **PEP 445**- `pyfailmalloc`tool (- [bpo-18408](https://bugs.python.org/issue?@action=redirect&bpo=18408),- [bpo-18520](https://bugs.python.org/issue?@action=redirect&bpo=18520)).
- The - `pyvenv`command now accepts a- `--copies`option to use copies rather than symlinks even on systems where symlinks are the default. (Contributed by Vinay Sajip in- [bpo-18807](https://bugs.python.org/issue?@action=redirect&bpo=18807).)
- The - `pyvenv`command also accepts a- `--without-pip`option to suppress the otherwise-automatic bootstrapping of pip into the virtual environment. (Contributed by Nick Coghlan in- [bpo-19552](https://bugs.python.org/issue?@action=redirect&bpo=19552)as part of the- **PEP 453**
- The encoding name is now optional in the value set for the - `PYTHONIOENCODING`- [bpo-18818](https://bugs.python.org/issue?@action=redirect&bpo=18818).)
- The - `bz2`- `lzma`- `gzip`- `open`functions now support- `x`(exclusive creation) mode. (Contributed by Tim Heaney and Vajrasky Kok in- [bpo-19201](https://bugs.python.org/issue?@action=redirect&bpo=19201),- [bpo-19222](https://bugs.python.org/issue?@action=redirect&bpo=19222), and- [bpo-19223](https://bugs.python.org/issue?@action=redirect&bpo=19223).)

### Significant Optimizations[¶](#significant-optimizations)

- The UTF-32 decoder is now 3x to 4x faster. (Contributed by Serhiy Storchaka in - [bpo-14625](https://bugs.python.org/issue?@action=redirect&bpo=14625).)
- The cost of hash collisions for sets is now reduced. Each hash table probe now checks a series of consecutive, adjacent key/hash pairs before continuing to make random probes through the hash table. This exploits cache locality to make collision resolution less expensive. The collision resolution scheme can be described as a hybrid of linear probing and open addressing. The number of additional linear probes defaults to nine. This can be changed at compile-time by defining LINEAR_PROBES to be any value. Set LINEAR_PROBES=0 to turn-off linear probing entirely. (Contributed by Raymond Hettinger in - [bpo-18771](https://bugs.python.org/issue?@action=redirect&bpo=18771).)
- The interpreter starts about 30% faster. A couple of measures lead to the speedup. The interpreter loads fewer modules on startup, e.g. the - `re`- `collections`- `locale`- [bpo-19219](https://bugs.python.org/issue?@action=redirect&bpo=19219),- [bpo-19218](https://bugs.python.org/issue?@action=redirect&bpo=19218),- [bpo-19209](https://bugs.python.org/issue?@action=redirect&bpo=19209),- [bpo-19205](https://bugs.python.org/issue?@action=redirect&bpo=19205)and- [bpo-9548](https://bugs.python.org/issue?@action=redirect&bpo=9548).)
- `bz2.BZ2File`- `lzma.LZMAFile`- [bpo-16034](https://bugs.python.org/issue?@action=redirect&bpo=16034).)
- `random.getrandbits()`- [bpo-16674](https://bugs.python.org/issue?@action=redirect&bpo=16674).)
- By taking advantage of the new storage format for strings, pickling of strings is now significantly faster. (Contributed by Victor Stinner and Antoine Pitrou in - [bpo-15596](https://bugs.python.org/issue?@action=redirect&bpo=15596).)
- A performance issue in - `io.FileIO.readall()`has been solved. This particularly affects Windows, and significantly speeds up the case of piping significant amounts of data through- `subprocess`- [bpo-15758](https://bugs.python.org/issue?@action=redirect&bpo=15758).)
- `html.escape()`- [bpo-18020](https://bugs.python.org/issue?@action=redirect&bpo=18020).)
- On Windows, the native - `VirtualAlloc`is now used instead of the CRT- `malloc`in- `obmalloc`. Artificial benchmarks show about a 3% memory savings.
- `os.urandom()`- [bpo-18756](https://bugs.python.org/issue?@action=redirect&bpo=18756).)

## Deprecated[¶](#deprecated)

This section covers various APIs and other features that have been deprecated
in Python 3.4, and will be removed in Python 3.5 or later.  In most (but not
all) cases, using the deprecated APIs will produce a [ DeprecationWarning](../library/exceptions.html#DeprecationWarning)
when the interpreter is run with deprecation warnings enabled (for example, by
using 

`-Wd`).### Deprecations in the Python API[¶](#deprecations-in-the-python-api)

- As mentioned in - [PEP 451: A ModuleSpec Type for the Import System](#whatsnew-pep-451), a number of- `importlib`- `importlib.find_loader()`is replaced by- `importlib.util.find_spec()`- `importlib.machinery.PathFinder.find_module()`is replaced by- `importlib.machinery.PathFinder.find_spec()`- `importlib.abc.MetaPathFinder.find_module()`is replaced by- `importlib.abc.MetaPathFinder.find_spec()`- `importlib.abc.PathEntryFinder.find_loader()`and- `find_module()`are replaced by- `importlib.abc.PathEntryFinder.find_spec()`- *xxx*Loader- `load_module`methods (- `importlib.abc.Loader.load_module()`,- `importlib.abc.InspectLoader.load_module()`,- `importlib.abc.FileLoader.load_module()`,- `importlib.abc.SourceLoader.load_module()`) should no longer be implemented, instead loaders should implement an- `exec_module`method (- `importlib.abc.Loader.exec_module()`- `importlib.abc.InspectLoader.exec_module()`- `importlib.abc.SourceLoader.exec_module()`- `importlib.abc.Loader.module_repr()`,- `importlib.util.module_for_loader()`,- `importlib.util.set_loader()`, and- `importlib.util.set_package()`are no longer needed because their functions are now handled automatically by the import system.
- The - `imp`module is pending deprecation. To keep compatibility with Python 2/3 code bases, the module’s removal is currently not scheduled.
- The - `formatter`module is pending deprecation and is slated for removal in Python 3.6.
- `MD5`as the default- *digestmod*for the- `hmac.new()`- *digestmod*argument.
- The internal - `Netrc`class in the- `ftplib`- `DeprecationWarning`
- The undocumented - *endtime*argument to- `subprocess.Popen.wait()`
- The - *strict*argument of- `HTMLParser`
- The - `plistlib`- `readPlist()`,- `writePlist()`,- `readPlistFromBytes()`, and- `writePlistToBytes()`functions are deprecated in favor of the corresponding new functions- `load()`- `dump()`- `loads()`- `dumps()`- `Data()`is deprecated in favor of just using the- `bytes`
- The - `sysconfig`- `SO`is deprecated, it has been replaced by- `EXT_SUFFIX`.
- The - `U`mode accepted by various- `open`functions is deprecated. In Python3 it does not do anything useful, and should be replaced by appropriate uses of- `io.TextIOWrapper`- *newline*argument.
- The - *parser*argument of- `xml.etree.ElementTree.iterparse()`- *html*argument of- `XMLParser()`- `XMLParser`should be passed by keyword.

### Deprecated Features[¶](#deprecated-features)

- Running - [IDLE — Python editor and shell](../library/idle.html#idle)with the- `-n`flag (no subprocess) is deprecated. However, the feature will not be removed until- [bpo-18823](https://bugs.python.org/issue?@action=redirect&bpo=18823)is resolved.
- The site module adding a “site-python” directory to sys.path, if it exists, is deprecated ( - [bpo-19375](https://bugs.python.org/issue?@action=redirect&bpo=19375)).

## Removed[¶](#removed)

### Operating Systems No Longer Supported[¶](#operating-systems-no-longer-supported)

Support for the following operating systems has been removed from the source and build tools:

### API and Feature Removals[¶](#api-and-feature-removals)

The following obsolete and previously deprecated APIs and features have been removed:

- The unmaintained - `Misc/TextMate`and- `Misc/vim`directories have been removed (see the- [devguide](https://devguide.python.org)for suggestions on what to use instead).
- The - `SO`makefile macro is removed (it was replaced by the- `SHLIB_SUFFIX`and- `EXT_SUFFIX`macros) (- [bpo-16754](https://bugs.python.org/issue?@action=redirect&bpo=16754)).
- The - `PyThreadState.tick_counter`field has been removed; its value has been meaningless since Python 3.2, when the “new GIL” was introduced (- [bpo-19199](https://bugs.python.org/issue?@action=redirect&bpo=19199)).
- `PyLoader`and- `PyPycLoader`have been removed from- `importlib`- [bpo-15641](https://bugs.python.org/issue?@action=redirect&bpo=15641).)
- The - *strict*argument to- `HTTPConnection`- `HTTPSConnection`
- The deprecated - `urllib.request.Request`- `add_data`,- `has_data`,- `get_data`,- `get_type`,- `get_host`,- `get_selector`,- `set_proxy`,- `get_origin_req_host`, and- `is_unverifiable`have been removed (use direct attribute access instead).
- Support for loading the deprecated - `TYPE_INT64`has been removed from- `marshal`- [bpo-15480](https://bugs.python.org/issue?@action=redirect&bpo=15480).)
- `inspect.Signature`
- `object.__format__()`- `TypeError`- `TypeError`if you are using an- `'s'`format code with objects that do not have a __format__ method that handles it. See- [bpo-7994](https://bugs.python.org/issue?@action=redirect&bpo=7994)for background.
- `difflib.SequenceMatcher.isbjunk()`and- `difflib.SequenceMatcher.isbpopular()`were deprecated in 3.2, and have now been removed: use- `x in sm.bjunk`and- `x in sm.bpopular`, where- *sm*is a- `SequenceMatcher`- [bpo-13248](https://bugs.python.org/issue?@action=redirect&bpo=13248)).

### Code Cleanups[¶](#code-cleanups)

- The unused and undocumented internal - `Scanner`class has been removed from the- `pydoc`
- The private and effectively unused - `_gestalt`module has been removed, along with the private- `platform`- `_mac_ver_lookup`,- `_mac_ver_gstalt`, and- `_bcd2str`, which would only have ever been called on badly broken OSX systems (see- [bpo-18393](https://bugs.python.org/issue?@action=redirect&bpo=18393)).
- The hardcoded copies of certain - `stat`- `tarfile`

## Porting to Python 3.4[¶](#porting-to-python-3-4)

This section lists previously described changes and other bugfixes that may require changes to your code.

### Changes in ‘python’ Command Behavior[¶](#changes-in-python-command-behavior)

- In a posix shell, setting the - `PATH`environment variable to an empty value is equivalent to not setting it at all. However, setting- `PYTHONPATH`- *not*equivalent to not setting it at all: setting- `PYTHONPATH`to an empty value was equivalent to setting it to- `.`, which leads to confusion when reasoning by analogy to how- `PATH`works. The behavior now conforms to the posix convention for- `PATH`.
- The [X refs, Y blocks] output of a debug ( - `--with-pydebug`) build of the CPython interpreter is now off by default. It can be re-enabled using the- `-X showrefcount`option. (Contributed by Ezio Melotti in- [bpo-17323](https://bugs.python.org/issue?@action=redirect&bpo=17323).)
- The python command and most stdlib scripts (as well as - `argparse`- `--version`information to- `stdout`instead of- `stderr`(for issue list see- [Other Improvements](#other-improvements-3-4)above).

### Changes in the Python API[¶](#changes-in-the-python-api)

- The ABCs defined in - `importlib.abc`- `NotImplementedError`- `super()`- `NotImplementedError`or the appropriate exception as needed.
- The module type now initializes the - `__package__`- `__loader__`- `None`by default. To determine if these attributes were set in a backwards-compatible fashion, use e.g.- `getattr(module, '__loader__', None) is not None`. (- [bpo-17115](https://bugs.python.org/issue?@action=redirect&bpo=17115).)
- `importlib.util.module_for_loader()`now sets- `__loader__`and- `__package__`unconditionally to properly support reloading. If this is not desired then you will need to set these attributes manually. You can use- `importlib.util.module_to_load()`for module management.
- Import now resets relevant attributes (e.g. - `__name__`,- `__loader__`,- `__package__`,- `__file__`,- `__cached__`) unconditionally when reloading. Note that this restores a pre-3.3 behavior in that it means a module is re-found when re-loaded (- [bpo-19413](https://bugs.python.org/issue?@action=redirect&bpo=19413)).
- Frozen packages no longer set - `__path__`to a list containing the package name, they now set it to an empty list. The previous behavior could cause the import system to do the wrong thing on submodule imports if there was also a directory with the same name as the frozen package. The correct way to determine if a module is a package or not is to use- `hasattr(module, '__path__')`(- [bpo-18065](https://bugs.python.org/issue?@action=redirect&bpo=18065)).
- Frozen modules no longer define a - `__file__`attribute. It’s semantically incorrect for frozen modules to set the attribute as they are not loaded from any explicit location. If you must know that a module comes from frozen code then you can see if the module’s- `__spec__.location`is set to- `'frozen'`, check if the loader is a subclass of- `importlib.machinery.FrozenImporter`- `imp.is_frozen()`.
- `py_compile.compile()`- `FileExistsError`
- `importlib.abc.SourceLoader.get_source()`- `ImportError`- `SyntaxError`- `UnicodeDecodeError`- `ImportError`is meant to be raised only when source code cannot be found but it should, it was felt to be over-reaching/overloading of that meaning when the source code is found but improperly structured. If you were catching ImportError before and wish to continue to ignore syntax or decoding issues, catch all three exceptions now.
- `functools.update_wrapper()`- `functools.wraps()`- `__wrapped__`attribute to the function being wrapped, even if that function also had its- `__wrapped__`attribute set. This means- `__wrapped__`attributes now correctly link a stack of decorated functions rather than every- `__wrapped__`attribute in the chain referring to the innermost function. Introspection libraries that assumed the previous behaviour was intentional can use- `inspect.unwrap()`- `__wrapped__`attribute.
- `inspect.getfullargspec()`- `inspect.signature()`- `inspect.getfullargspec()`will fail on non-Python callables may need to be adjusted accordingly.
- `importlib.machinery.PathFinder`- `sys.path_hooks`- `sys.path_importer_cache`- `''`, thus iterating through- `sys.path_importer_cache`based on- `sys.path`- `__file__`when imported in the current working directory will also now have an absolute path, including when using- `-m`with the interpreter (except for- `__main__.__file__`when a script has been executed directly using a relative path) (Contributed by Brett Cannon in- [bpo-18416](https://bugs.python.org/issue?@action=redirect&bpo=18416)). is specified on the command-line) (- [bpo-18416](https://bugs.python.org/issue?@action=redirect&bpo=18416)).
- The removal of the - *strict*argument to- `HTTPConnection`- `HTTPSConnection`
- Strings between - `from __future__ import ...`statements now- *always*raise a- `SyntaxError`- [bpo-17434](https://bugs.python.org/issue?@action=redirect&bpo=17434)).
- `ssl.SSLSocket.getpeercert()`- `ssl.SSLSocket.do_handshake()`- `OSError`- `ENOTCONN`when the- `SSLSocket`is not connected, instead of the previous behavior of raising an- `AttributeError`- `getpeercert()`will raise a- `ValueError`
- `base64.b32decode()`- `binascii.Error`- `TypeError`- `TypeError`was missed when the other- `TypeError`s were converted. (Contributed by Serhiy Storchaka in- [bpo-18011](https://bugs.python.org/issue?@action=redirect&bpo=18011).) Note: this change was also inadvertently applied in Python 3.3.3.
- The - `file`attribute is now automatically closed when the creating- `cgi.FieldStorage`instance is garbage collected. If you were pulling the file object out separately from the- `cgi.FieldStorage`instance and not keeping the instance alive, then you should either store the entire- `cgi.FieldStorage`instance or read the contents of the file before the- `cgi.FieldStorage`instance is garbage collected.
- Calling - `read`or- `write`on a closed SSL socket now raises an informative- `ValueError`- `AttributeError`- [bpo-9177](https://bugs.python.org/issue?@action=redirect&bpo=9177)).
- `slice.indices()`- `OverflowError`- `slice.indices()`now raises a- `ValueError`- [bpo-14794](https://bugs.python.org/issue?@action=redirect&bpo=14794)).
- The - `complex`- `cmath`- `float`- `__complex__`special method returned one. This now raises a- `TypeError`- [bpo-16290](https://bugs.python.org/issue?@action=redirect&bpo=16290).)
- The - `int`- `float`- *base*parameter. It is unlikely anyone was doing this, but if so, it will now raise a- `TypeError`- [bpo-16772](https://bugs.python.org/issue?@action=redirect&bpo=16772)).
- Defaults for keyword-only arguments are now evaluated - *after*defaults for regular keyword arguments, instead of before. Hopefully no one wrote any code that depends on the previous buggy behavior (- [bpo-16967](https://bugs.python.org/issue?@action=redirect&bpo=16967)).
- Stale thread states are now cleared after - `fork()`- [bpo-17094](https://bugs.python.org/issue?@action=redirect&bpo=17094).)
- Parameter names in - `__annotations__`dicts are now mangled properly, similarly to- `__kwdefaults__`- [bpo-20625](https://bugs.python.org/issue?@action=redirect&bpo=20625).)
- `hashlib.hash.name`- [bpo-18532](https://bugs.python.org/issue?@action=redirect&bpo=18532)).
- Because - `unittest.TestSuite`- `TestSuite`- `unittest`- `TestSuite`subclass that defines a- `_removeTestAtIndex`method that does nothing (see- `TestSuite.__iter__()`- [bpo-11798](https://bugs.python.org/issue?@action=redirect&bpo=11798)).
- `unittest`- `argparse`
- The - `re.split()`- `re.findall()`- `re.sub()`- `group()`- `groups()`- `match`objects now always return a- *bytes*object when the string to be matched is a- [bytes-like object](../glossary.html#term-bytes-like-object). Previously the return type matched the input type, so if your code was depending on the return value being, say, a- `bytearray`, you will need to change your code.
- `audioop`functions now raise an error immediately if passed string input, instead of failing randomly later on (- [bpo-16685](https://bugs.python.org/issue?@action=redirect&bpo=16685)).
- The new - *convert_charrefs*argument to- `HTMLParser`- `False`for backward compatibility, but will eventually be changed to default to- `True`. It is recommended that you add this keyword, with the appropriate value, to any- `HTMLParser`calls in your code (- [bpo-13633](https://bugs.python.org/issue?@action=redirect&bpo=13633)).
- Since the - *digestmod*argument to the- `hmac.new()`- `hmac.new()`should be changed to explicitly specify a- *digestmod*(- [bpo-17276](https://bugs.python.org/issue?@action=redirect&bpo=17276)).
- Calling - `sysconfig.get_config_var()`- `SO`key, or looking- `SO`up in the results of a call to- `sysconfig.get_config_vars()`- `EXT_SUFFIX`or- `SHLIB_SUFFIX`, depending on the context (- [bpo-19555](https://bugs.python.org/issue?@action=redirect&bpo=19555)).
- Any calls to - `open`functions that specify- `U`should be modified.- `U`is ineffective in Python3 and will eventually raise an error if used. Depending on the function, the equivalent of its old Python2 behavior can be achieved using either a- *newline*argument, or if necessary by wrapping the stream in- `TextIOWrapper`- *newline*argument (- [bpo-15204](https://bugs.python.org/issue?@action=redirect&bpo=15204)).
- If you use - `pyvenv`in a script and desire that pip- *not*be installed, you must add- `--without-pip`to your command invocation.
- The default behavior of - `json.dump()`- `json.dumps()`- [bpo-16333](https://bugs.python.org/issue?@action=redirect&bpo=16333)).
- `doctest`- `__doc__`strings, so if your doctest test discovery includes extension modules that have things that look like doctests in them you may see test failures you’ve never seen before when running your tests (- [bpo-3158](https://bugs.python.org/issue?@action=redirect&bpo=3158)).
- The - `collections.abc`- `collections`- `collections.abc`. If your program depended on the (undocumented) implicit import, you will need to add an explicit- `import collections.abc`(- [bpo-20784](https://bugs.python.org/issue?@action=redirect&bpo=20784)).

### Changes in the C API[¶](#changes-in-the-c-api)

- `PyEval_EvalFrameEx()`- `PyObject_Repr()`- `PyObject_Str()`- `PyErr_Fetch()`- `PyErr_Clear()`
- `PyErr_SetImportError()`- `TypeError`- **msg**argument is not set. Previously only- `NULL`was returned with no exception set.
- The result of the - `PyOS_ReadlineFunctionPointer`- `PyMem_RawMalloc()`- `PyMem_RawRealloc()`- `NULL`if an error occurred, instead of a string allocated by- `PyMem_Malloc()`- `PyMem_Realloc()`- [bpo-16742](https://bugs.python.org/issue?@action=redirect&bpo=16742))
- `PyThread_set_key_value()`- `NULL`pointer).
- The - `f_tstate`(thread state) field of the- `PyFrameObject`- [bpo-14432](https://bugs.python.org/issue?@action=redirect&bpo=14432)for the rationale.

## Changed in 3.4.3[¶](#changed-in-3-4-3)

### PEP 476: Enabling certificate verification by default for stdlib http clients[¶](#pep-476-enabling-certificate-verification-by-default-for-stdlib-http-clients)

[ http.client](../library/http.client.html#module-http.client) and modules which use it, such as 

[and](../library/urllib.request.html#module-urllib.request)

`urllib.request`[, will now verify that the server presents a certificate which is signed by a CA in the platform trust store and whose hostname matches the hostname being requested by default, significantly improving security for many applications.](../library/xmlrpc.client.html#module-xmlrpc.client)

`xmlrpc.client`For applications which require the old previous behavior, they can pass an alternate context:

```
import urllib.request
import ssl
# This disables all verification
context = ssl._create_unverified_context()
# This allows using a specific certificate for the host, which doesn't need
# to be in the trust store
context = ssl.create_default_context(cafile="/path/to/file.crt")
urllib.request.urlopen("https://invalid-cert", context=context)
```