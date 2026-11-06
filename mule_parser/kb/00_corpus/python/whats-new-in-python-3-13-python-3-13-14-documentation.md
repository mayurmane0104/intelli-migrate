# What’s New In Python 3.13 — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/whatsnew/3.13.html](https://docs.python.org/3.13/whatsnew/3.13.html)

---

# What’s New In Python 3.13[¶](#what-s-new-in-python-3-13)

- Editors:
- Adam Turner and Thomas Wouters 

This article explains the new features in Python 3.13, compared to 3.12.
Python 3.13 was released on October 7, 2024.
For full details, see the [changelog](changelog.html#changelog).

See also

[ PEP 719](https://peps.python.org/pep-0719/) – Python 3.13 Release Schedule

## Summary – Release Highlights[¶](#summary-release-highlights)

Python 3.13 is the latest stable release of the Python programming
language, with a mix of changes to the language, the implementation
and the standard library.
The biggest changes include a new [interactive interpreter](#whatsnew313-better-interactive-interpreter),
experimental support for running in a [free-threaded mode](#whatsnew313-free-threaded-cpython) ([ PEP 703](https://peps.python.org/pep-0703/)),
and a 

[Just-In-Time compiler](#whatsnew313-jit-compiler)(

[).](https://peps.python.org/pep-0744/)

**PEP 744**Error messages continue to improve, with tracebacks now highlighted in color
by default. The [ locals()](../library/functions.html#locals) builtin now has 

[defined semantics](#whatsnew313-locals-semantics)for changing the returned mapping, and type parameters now support default values.

The library changes contain removal of deprecated APIs and modules,
as well as the usual improvements in user-friendliness and correctness.
Several legacy standard library modules have now [been removed](#whatsnew313-pep594) following their deprecation in Python 3.11 ([ PEP 594](https://peps.python.org/pep-0594/)).

This article doesn’t attempt to provide a complete specification
of all new features, but instead gives a convenient overview.
For full details refer to the documentation,
such as the [Library Reference](../library/index.html#library-index)
and [Language Reference](../reference/index.html#reference-index).
To understand the complete implementation and design rationale for a change,
refer to the PEP for a particular new feature;
but note that PEPs usually are not kept up-to-date
once a feature has been fully implemented.
See [Porting to Python 3.13](#porting-to-python-3-13) for guidance on upgrading from
earlier versions of Python.

Interpreter improvements:

- A greatly improved - [interactive interpreter](#whatsnew313-better-interactive-interpreter)and- [improved error messages](#whatsnew313-improved-error-messages).
- **PEP 667**- `locals()`- [defined semantics](#whatsnew313-locals-semantics)when mutating the returned mapping. Python debuggers and similar tools may now more reliably update local variables in optimized scopes even during concurrent code execution.
- **PEP 703**- [global interpreter lock](../glossary.html#term-global-interpreter-lock)disabled. See- [Free-threaded CPython](#whatsnew313-free-threaded-cpython)for more details.
- **PEP 744**- [JIT compiler](#whatsnew313-jit-compiler)was added. It is currently disabled by default (though we may turn it on later). Performance improvements are modest – we expect to improve this over the next few releases.
- Color support in the new - [interactive interpreter](#whatsnew313-better-interactive-interpreter), as well as in- [tracebacks](#whatsnew313-improved-error-messages)and- [doctest](#whatsnew313-doctest)output. This can be disabled through the- `PYTHON_COLORS`- `NO_COLOR`

Python data model improvements:

- `__static_attributes__`- `self.X`in any function in a class body.
- `__firstlineno__`

Significant improvements in the standard library:

- Add a new - `PythonFinalizationError`- [finalization](../glossary.html#term-interpreter-shutdown).
- The - `argparse`
- The new functions - `base64.z85encode()`- `base64.z85decode()`- [Z85 data](https://rfc.zeromq.org/spec/32/).
- The - `copy`- `copy.replace()`- `__replace__()`
- The new - `dbm.sqlite3`- `dbm`
- The - `os`- [suite of new functions](../library/os.html#os-timerfd)for working with Linux’s timer notification file descriptors.
- The - `random`- [command-line interface](../library/random.html#random-cli).

Security improvements:

- `ssl.create_default_context()`- `ssl.VERIFY_X509_PARTIAL_CHAIN`- `ssl.VERIFY_X509_STRICT`

C API improvements:

- The - `Py_mod_gil`- [GIL](../glossary.html#term-GIL)disabled.
- The - [PyTime C API](../c-api/time.html)has been added, providing access to system clocks.
- `PyMutex`
- There is a new - [suite of functions](../c-api/monitoring.html#c-api-monitoring)for generating- **PEP 669**

New typing features:

- **PEP 696**- `typing.TypeVar`- `typing.ParamSpec`- `typing.TypeVarTuple`
- **PEP 702**- `warnings.deprecated()`
- **PEP 705**- `typing.ReadOnly`- `typing.TypedDict`
- **PEP 742**- `typing.TypeIs`- `typing.TypeGuard`

Platform support:

- **PEP 730**- [officially supported platform](#whatsnew313-platform-support), at- **tier 3**
- **PEP 738**- [officially supported platform](#whatsnew313-platform-support), at- **tier 3**
- `wasm32-wasi`is now supported as a- **tier 2**
- `wasm32-emscripten`is no longer an officially supported platform.

Important removals:

- [PEP 594](#whatsnew313-pep594): The remaining 19 “dead batteries” (legacy stdlib modules) have been removed from the standard library:- `aifc`,- `audioop`,- `cgi`,- `cgitb`,- `chunk`,- `crypt`,- `imghdr`,- `mailcap`,- `msilib`,- `nis`,- `nntplib`,- `ossaudiodev`,- `pipes`,- `sndhdr`,- `spwd`,- `sunau`,- `telnetlib`,- `uu`and- `xdrlib`.
- Remove the - **2to3**tool and- `lib2to3`module (deprecated in Python 3.11).
- Remove the - `tkinter.tix`module (deprecated in Python 3.6).
- Remove the - `locale.resetlocale()`function.
- Remove the - `typing.io`and- `typing.re`namespaces.
- Remove chained - `classmethod`

Release schedule changes:

[ PEP 602](https://peps.python.org/pep-0602/) (“Annual Release Cycle for Python”) has been updated
to extend the full support (‘bugfix’) period for new releases to two years.
This updated policy means that:

- Python 3.9–3.12 have one and a half years of full support, followed by three and a half years of security fixes. 
- Python 3.13 and later have two years of full support, followed by three years of security fixes. 

## New Features[¶](#new-features)

### A better interactive interpreter[¶](#a-better-interactive-interpreter)

Python now uses a new [interactive](../glossary.html#term-interactive) shell by default, based on code
from the [PyPy project](https://pypy.org/).
When the user starts the [REPL](../glossary.html#term-REPL) from an interactive terminal,
the following new features are now supported:

- Multiline editing with history preservation. 
- Direct support for REPL-specific commands like - `help`,- `exit`, and- `quit`, without the need to call them as functions.
- Prompts and tracebacks with - [color enabled by default](../using/cmdline.html#using-on-controlling-color).
- Interactive help browsing using - `F1`with a separate command history.
- History browsing using - `F2`that skips output as well as the- [>>>](../glossary.html#term-0)and- […](../glossary.html#term-...)prompts.
- “Paste mode” with - `F3`that makes pasting larger blocks of code easier (press- `F3`again to return to the regular prompt).

To disable the new interactive shell,
set the [ PYTHON_BASIC_REPL](../using/cmdline.html#envvar-PYTHON_BASIC_REPL) environment variable.
For more on interactive mode, see 

[Interactive Mode](../tutorial/appendix.html#tut-interac).

(Contributed by Pablo Galindo Salgado, Łukasz Langa, and
Lysandros Nikolaou in [gh-111201](https://github.com/python/cpython/issues/111201) based on code from the PyPy project.
Windows support contributed by Dino Viehland and Anthony Shaw.)

### Improved error messages[¶](#improved-error-messages)

- The interpreter now uses color by default when displaying tracebacks in the terminal. This feature - [can be controlled](../using/cmdline.html#using-on-controlling-color)via the new- `PYTHON_COLORS`- `NO_COLOR`- `FORCE_COLOR`- [gh-112730](https://github.com/python/cpython/issues/112730).)

- A common mistake is to write a script with the same name as a standard library module. When this results in errors, we now display a more helpful error message: - $ python random.py Traceback (most recent call last): File "/home/me/random.py", line 1, in <module> import random File "/home/me/random.py", line 3, in <module> print(random.randint(5)) ^^^^^^^^^^^^^^ AttributeError: module 'random' has no attribute 'randint' (consider renaming '/home/me/random.py' since it has the same name as the standard library module named 'random' and prevents importing that standard library module) - Similarly, if a script has the same name as a third-party module that it attempts to import and this results in errors, we also display a more helpful error message: - $ python numpy.py Traceback (most recent call last): File "/home/me/numpy.py", line 1, in <module> import numpy as np File "/home/me/numpy.py", line 3, in <module> np.array([1, 2, 3]) ^^^^^^^^ AttributeError: module 'numpy' has no attribute 'array' (consider renaming '/home/me/numpy.py' if it has the same name as a library you intended to import) - (Contributed by Shantanu Jain in - [gh-95754](https://github.com/python/cpython/issues/95754).)
- The error message now tries to suggest the correct keyword argument when an incorrect keyword argument is passed to a function. - >>> "Better error messages!".split(max_split=1) Traceback (most recent call last): File "<python-input-0>", line 1, in <module> "Better error messages!".split(max_split=1) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^ TypeError: split() got an unexpected keyword argument 'max_split'. Did you mean 'maxsplit'? - (Contributed by Pablo Galindo Salgado and Shantanu Jain in - [gh-107944](https://github.com/python/cpython/issues/107944).)

### Free-threaded CPython[¶](#free-threaded-cpython)

CPython now has experimental support for running in a free-threaded mode,
with the [global interpreter lock](../glossary.html#term-global-interpreter-lock) (GIL) disabled.
This is an experimental feature and therefore is not enabled by default.
The free-threaded mode requires a different executable,
usually called `python3.13t` or `python3.13t.exe`.
Pre-built binaries marked as *free-threaded* can be installed as part of
the official [Windows](../using/windows.html#install-freethreaded-windows)
and [macOS](../using/mac.html#install-freethreaded-macos) installers,
or CPython can be built from source with the [ --disable-gil](../using/configure.html#cmdoption-disable-gil) option.

Free-threaded execution allows for full utilization of the available
processing power by running threads in parallel on available CPU cores.
While not all software will benefit from this automatically, programs
designed with threading in mind will run faster on multi-core hardware.
**The free-threaded mode is experimental** and work is ongoing to improve it:
expect some bugs and a substantial single-threaded performance hit.
Free-threaded builds of CPython support optionally running with the GIL
enabled at runtime using the environment variable [ PYTHON_GIL](../using/cmdline.html#envvar-PYTHON_GIL) or
the command-line option 

[.](../using/cmdline.html#cmdoption-X)

`-X gil=1`To check if the current interpreter supports free-threading, [ python -VV](../using/cmdline.html#cmdoption-V)
and 

[contain “experimental free-threading build”. The new](../library/sys.html#sys.version)

`sys.version``sys._is_gil_enabled()` function can be used to check whether
the GIL is actually disabled in the running process.C-API extension modules need to be built specifically for the free-threaded
build. Extensions that support running with the [GIL](../glossary.html#term-GIL) disabled should
use the [ Py_mod_gil](../c-api/module.html#c.Py_mod_gil) slot. Extensions using single-phase init should
use 

[to indicate whether they support running with the GIL disabled. Importing C extensions that don’t use these mechanisms will cause the GIL to be enabled, unless the GIL was explicitly disabled with the](../c-api/module.html#c.PyUnstable_Module_SetGIL)

`PyUnstable_Module_SetGIL()`[environment variable or the](../using/cmdline.html#envvar-PYTHON_GIL)

`PYTHON_GIL`[option. pip 24.1 or newer is required to install packages with C extensions in the free-threaded build.](../using/cmdline.html#cmdoption-X)

`-X gil=0`This work was made possible thanks to many individuals and organizations, including the large community of contributors to Python and third-party projects to test and enable free-threading support. Notable contributors include: Sam Gross, Ken Jin, Donghee Na, Itamar Oren, Matt Page, Brett Simmers, Dino Viehland, Carl Meyer, Nathan Goldbaum, Ralf Gommers, Lysandros Nikolaou, and many others. Many of these contributors are employed by Meta, which has provided significant engineering resources to support this project.

See also

[ PEP 703](https://peps.python.org/pep-0703/) “Making the Global Interpreter Lock Optional in CPython”
contains rationale and information surrounding this work.

[Porting Extension Modules to Support Free-Threading](https://py-free-threading.github.io/porting/): A community-maintained
porting guide for extension authors.

### An experimental just-in-time (JIT) compiler[¶](#an-experimental-just-in-time-jit-compiler)

When CPython is configured and built using
the `--enable-experimental-jit` option,
a just-in-time (JIT) compiler is added which may speed up some Python programs.
On Windows, use `PCbuild/build.bat --experimental-jit` to enable the JIT
or `--experimental-jit-interpreter` to enable the Tier 2 interpreter.
Build requirements and further supporting information [are contained at](https://github.com/python/cpython/blob/main/Tools/jit/README.md)
`Tools/jit/README.md`.

The `--enable-experimental-jit` option takes these (optional) values,
defaulting to `yes` if `--enable-experimental-jit` is present
without the optional value.

- `no`: Disable the entire Tier 2 and JIT pipeline.
- `yes`: Enable the JIT. To disable the JIT at runtime, pass the environment variable- `PYTHON_JIT=0`
- `yes-off`: Build the JIT but disable it by default. To enable the JIT at runtime, pass the environment variable- `PYTHON_JIT=1`
- `interpreter`: Enable the Tier 2 interpreter but disable the JIT. The interpreter can be disabled by running with- `PYTHON_JIT=0`

The internal architecture is roughly as follows:

- We start with specialized - *Tier 1 bytecode*. See- [What’s new in 3.11](3.11.html#whatsnew311-pep659)for details.
- When the Tier 1 bytecode gets hot enough, it gets translated to a new purely internal intermediate representation (IR), called the - *Tier 2 IR*, and sometimes referred to as micro-ops (“uops”).
- The Tier 2 IR uses the same stack-based virtual machine as Tier 1, but the instruction format is better suited to translation to machine code. 
- We have several optimization passes for Tier 2 IR, which are applied before it is interpreted or translated to machine code. 
- There is a Tier 2 interpreter, but it is mostly intended for debugging the earlier stages of the optimization pipeline. The Tier 2 interpreter can be enabled by configuring Python with - `--enable-experimental-jit=interpreter`.
- When the JIT is enabled, the optimized Tier 2 IR is translated to machine code, which is then executed. 
- The machine code translation process uses a technique called - *copy-and-patch*. It has no runtime dependencies, but there is a new build-time dependency on LLVM.

See also

(JIT by Brandt Bucher, inspired by a paper by Haoran Xu and Fredrik Kjolstad. Tier 2 IR by Mark Shannon and Guido van Rossum. Tier 2 optimizer by Ken Jin.)

### Defined mutation semantics for `locals()`[¶](#defined-mutation-semantics-for-locals)

`locals()`Historically, the expected result of mutating the return value of
[ locals()](../library/functions.html#locals) has been left to individual Python implementations to define.
Starting from Python 3.13, 

[standardises the historical behavior of CPython for most code execution scopes, but changes](https://peps.python.org/pep-0667/)

**PEP 667**[optimized scopes](../glossary.html#term-optimized-scope)(functions, generators, coroutines, comprehensions, and generator expressions) to explicitly return independent snapshots of the currently assigned local variables, including locally referenced nonlocal variables captured in closures.

This change to the semantics of [ locals()](../library/functions.html#locals) in optimized scopes also
affects the default behavior of code execution functions that implicitly
target 

`locals()` if no explicit namespace is provided
(such as [and](../library/functions.html#exec)

`exec()`[). In previous versions, whether or not changes could be accessed by calling](../library/functions.html#eval)

`eval()``locals()` after calling the code execution function was
implementation-dependent. In CPython specifically, such code would typically
appear to work as desired, but could sometimes fail in optimized scopes based
on other code (including debuggers and code execution tracing tools)
potentially resetting the shared snapshot in that scope.
Now, the code will always run against an independent snapshot of
the local variables in optimized scopes, and hence the changes will never
be visible in subsequent calls to `locals()`.
To access the changes made in these cases, an explicit namespace reference
must now be passed to the relevant function.
Alternatively, it may make sense to update affected code to use a higher level
code execution API that returns the resulting code execution namespace
(e.g. [when executing Python files from disk).](../library/runpy.html#runpy.run_path)

`runpy.run_path()`To ensure debuggers and similar tools can reliably update local variables in
scopes affected by this change, [ FrameType.f_locals](../reference/datamodel.html#frame.f_locals) now
returns a write-through proxy to the frame’s local and locally referenced
nonlocal variables in these scopes, rather than returning an inconsistently
updated shared 

`dict` instance with undefined runtime semantics.See [ PEP 667](https://peps.python.org/pep-0667/) for more details, including related C API changes
and deprecations. Porting notes are also provided below for the affected

[Python APIs](#pep667-porting-notes-py)and

[C APIs](#pep667-porting-notes-c).

(PEP and implementation contributed by Mark Shannon and Tian Gao in
[gh-74929](https://github.com/python/cpython/issues/74929). Documentation updates provided by Guido van Rossum and
Alyssa Coghlan.)

### Support for mobile platforms[¶](#support-for-mobile-platforms)

[ PEP 730](https://peps.python.org/pep-0730/): iOS is now a 

[supported platform, with the](https://peps.python.org/pep-0011/)

**PEP 11**`arm64-apple-ios` and `arm64-apple-ios-simulator` targets at tier 3
(iPhone and iPad devices released after 2013 and the Xcode iOS simulator
running on Apple silicon hardware, respectively).
`x86_64-apple-ios-simulator`
(the Xcode iOS simulator running on older `x86_64` hardware)
is not a tier 3 supported platform, but will have best-effort support.
(PEP written and implementation contributed by Russell Keith-Magee in
[gh-114099](https://github.com/python/cpython/issues/114099).)

[ PEP 738](https://peps.python.org/pep-0738/): Android is now a 

[supported platform, with the](https://peps.python.org/pep-0011/)

**PEP 11**`aarch64-linux-android` and `x86_64-linux-android` targets at tier 3.
The 32-bit targets `arm-linux-androideabi` and `i686-linux-android`
are not tier 3 supported platforms, but will have best-effort support.
(PEP written and implementation contributed by Malcolm Smith in
[gh-116622](https://github.com/python/cpython/issues/116622).)

## Other Language Changes[¶](#other-language-changes)

- The compiler now strips common leading whitespace from every line in a docstring. This reduces the size of the - [bytecode cache](../glossary.html#term-bytecode)(such as- `.pyc`files), with reductions in file size of around 5%, for example in- `sqlalchemy.orm.session`from SQLAlchemy 2.0. This change affects tools that use docstrings, such as- `doctest`- >>> def spam(): ... """ ... This is a docstring with ... leading whitespace. ... ... It even has multiple paragraphs! ... """ ... >>> spam.__doc__ '\nThis is a docstring with\n leading whitespace.\n\nIt even has multiple paragraphs!\n' - (Contributed by Inada Naoki in - [gh-81283](https://github.com/python/cpython/issues/81283).)
- [Annotation scopes](../reference/executionmodel.html#annotation-scopes)within class scopes can now contain lambdas and comprehensions. Comprehensions that are located within class scopes are not inlined into their parent scope.- class C[T]: type Alias = lambda: T 
- [Future statements](../reference/simple_stmts.html#future)are no longer triggered by relative imports of the- `__future__`- `from .__future__ import ...`are now simply standard relative imports, with no special features activated. (Contributed by Jeremiah Gabriel Pascual in- [gh-118216](https://github.com/python/cpython/issues/118216).)
- `global`- `except`- `else`- `SyntaxError`- [gh-111123](https://github.com/python/cpython/issues/111123).)
- Add - `PYTHON_FROZEN_MODULES`- `-X frozen_modules`- [gh-111374](https://github.com/python/cpython/issues/111374).)
- Add - [support for the perf profiler](../howto/perf_profiling.html#perf-profiling)working without- [frame pointers](https://en.wikipedia.org/wiki/Call_stack)through the new environment variable- `PYTHON_PERF_JIT_SUPPORT`- `-X perf_jit`- [gh-118518](https://github.com/python/cpython/issues/118518).)
- The location of a - `.python_history`file can be changed via the new- `PYTHON_HISTORY`- [gh-73965](https://github.com/python/cpython/issues/73965).)
- Classes have a new - `__static_attributes__`- `self.<name>`from any function in its body. (Contributed by Irit Katriel in- [gh-115775](https://github.com/python/cpython/issues/115775).)
- The compiler now creates a - `__firstlineno__`attribute on classes with the line number of the first line of the class definition. (Contributed by Serhiy Storchaka in- [gh-118465](https://github.com/python/cpython/issues/118465).)
- The - `exec()`- `eval()`- *globals*and- *locals*arguments as keywords. (Contributed by Raphael Gaschignard in- [gh-105879](https://github.com/python/cpython/issues/105879))
- The - `compile()`- `ast.PyCF_OPTIMIZED_AST`, which is similar to- `ast.PyCF_ONLY_AST`except that the returned AST is optimized according to the value of the- *optimize*argument. (Contributed by Irit Katriel in- [gh-108113](https://github.com/python/cpython/issues/108113)).
- Add a - `__name__`- `property`- [gh-101860](https://github.com/python/cpython/issues/101860).)
- Add - `PythonFinalizationError`- `RuntimeError`- [finalization](../glossary.html#term-interpreter-shutdown). The following callables now raise- `PythonFinalizationError`, instead of- `RuntimeError`:- (Contributed by Victor Stinner in - [gh-114570](https://github.com/python/cpython/issues/114570).)
- Allow the - *count*argument of- `str.replace()`- [gh-106487](https://github.com/python/cpython/issues/106487).)
- Many functions now emit a warning if a boolean value is passed as a file descriptor argument. This can help catch some errors earlier. (Contributed by Serhiy Storchaka in - [gh-82626](https://github.com/python/cpython/issues/82626).)
- Added - `name`and- `mode`attributes for compressed and archived file-like objects in the- `bz2`- `lzma`- `tarfile`- `zipfile`- [gh-115961](https://github.com/python/cpython/issues/115961).)

## New Modules[¶](#new-modules)

- `dbm.sqlite3`- `dbm`- [gh-100414](https://github.com/python/cpython/issues/100414).)

## Improved Modules[¶](#improved-modules)

### argparse[¶](#argparse)

- Add the - *deprecated*parameter to the- `add_argument()`- `add_parser()`methods, to enable deprecating command-line options, positional arguments, and subcommands. (Contributed by Serhiy Storchaka in- [gh-83648](https://github.com/python/cpython/issues/83648).)

### array[¶](#array)

- Add the - `'w'`type code (- `Py_UCS4`) for Unicode characters. It should be used instead of the deprecated- `'u'`type code. (Contributed by Inada Naoki in- [gh-80480](https://github.com/python/cpython/issues/80480).)
- Register - `array.array`- `MutableSequence`- `clear()`- [gh-114894](https://github.com/python/cpython/issues/114894).)

### ast[¶](#ast)

- The constructors of node types in the - `ast`- If an optional field on an AST node is not included as an argument when constructing an instance, the field will now be set to - `None`. Similarly, if a list field is omitted, that field will now be set to an empty list, and if an- `expr_context`field is omitted, it defaults to- `Load()`- In all other cases, where a required argument is omitted, the node constructor will emit a - `DeprecationWarning`- These changes do not apply to user-defined subclasses of - `ast.AST`- `AST._field_types`- (Contributed by Jelle Zijlstra in - [gh-105858](https://github.com/python/cpython/issues/105858),- [gh-117486](https://github.com/python/cpython/issues/117486), and- [gh-118851](https://github.com/python/cpython/issues/118851).)
- `ast.parse()`- *optimize*which is passed on to- `compile()`- [gh-108113](https://github.com/python/cpython/issues/108113).)

### asyncio[¶](#asyncio)

- `asyncio.as_completed()`- [asynchronous iterator](../glossary.html#term-asynchronous-iterator)and a plain- [iterator](../glossary.html#term-iterator)of- [awaitables](../glossary.html#term-awaitable). The awaitables yielded by asynchronous iteration include original task or future objects that were passed in, making it easier to associate results with the tasks being completed. (Contributed by Justin Arthur in- [gh-77714](https://github.com/python/cpython/issues/77714).)
- `asyncio.loop.create_unix_server()`- [gh-111246](https://github.com/python/cpython/issues/111246).)
- `DatagramTransport.sendto()`- [gh-115199](https://github.com/python/cpython/issues/115199).)
- Add - `Queue.shutdown`- `QueueShutDown`- [gh-104228](https://github.com/python/cpython/issues/104228).)
- Add the - `Server.close_clients()`- `Server.abort_clients()`- [gh-113538](https://github.com/python/cpython/issues/113538).)
- Accept a tuple of separators in - `StreamReader.readuntil()`- [gh-81322](https://github.com/python/cpython/issues/81322).)
- Improve the behavior of - `TaskGroup`- In the case where a task group is cancelled externally and also must raise an - `ExceptionGroup`- `cancel()`- `CancelledError`- `await`- An added benefit of these changes is that task groups now preserve the cancellation count ( - `cancelling()`- In order to handle some corner cases, - `uncancel()`- `_must_cancel`flag when the cancellation count reaches zero.- (Inspired by an issue reported by Arthur Tacca in - [gh-116720](https://github.com/python/cpython/issues/116720).)
- When - `TaskGroup.create_task()`- `TaskGroup`- `RuntimeWarning`- [gh-115957](https://github.com/python/cpython/issues/115957).)
- The function and methods named - `create_task`have received a new- `**kwargs`argument that is passed through to the task constructor. This change was accidentally added in 3.13.3, and broke the API contract for custom task factories. Several third-party task factories implemented workarounds for this. In 3.13.4 and later releases the old factory contract is honored once again (until 3.14). To keep the workarounds working, the extra- `**kwargs`argument still allows passing additional keyword arguments to- `Task`- This affects the following function and methods: - `asyncio.create_task()`- `asyncio.loop.create_task()`- `asyncio.TaskGroup.create_task()`- [gh-128307](https://github.com/python/cpython/issues/128307).)

### base64[¶](#base64)

- Add - `z85encode()`- `z85decode()`- `bytes`- [Z85 data](https://rfc.zeromq.org/spec/32/)and decoding Z85-encoded data to- `bytes`. (Contributed by Matan Perelman in- [gh-75299](https://github.com/python/cpython/issues/75299).)

### compileall[¶](#compileall)

- The default number of worker threads and processes is now selected using - `os.process_cpu_count()`- `os.cpu_count()`- [gh-109649](https://github.com/python/cpython/issues/109649).)

### concurrent.futures[¶](#concurrent-futures)

- The default number of worker threads and processes is now selected using - `os.process_cpu_count()`- `os.cpu_count()`- [gh-109649](https://github.com/python/cpython/issues/109649).)

### configparser[¶](#configparser)

- `ConfigParser`- *allow_unnamed_section*parameter. (Contributed by Pedro Sousa Lacerda in- [gh-66449](https://github.com/python/cpython/issues/66449).)

### copy[¶](#copy)

- The new - `replace()`- `replace protocol`- `replace()`function and implement the replace protocol:- Any user-defined class can also support - `copy.replace()`- `__replace__()`- [gh-108751](https://github.com/python/cpython/issues/108751).)

### ctypes[¶](#ctypes)

- As a consequence of necessary internal refactoring, initialization of internal metaclasses now happens in - `__init__`rather than in- `__new__`. This affects projects that subclass these internal metaclasses to provide custom initialization. Generally:- Custom logic that was done in - `__new__`after calling- `super().__new__`should be moved to- `__init__`.
- To create a class, call the metaclass, not only the metaclass’s - `__new__`method.
 - See - [gh-124520](https://github.com/python/cpython/issues/124520)for discussion and links to changes in some affected projects.
- `ctypes.Structure`- `_align_`- [gh-112433](https://github.com/python/cpython/issues/112433))

### dbm[¶](#dbm)

- Add - `dbm.sqlite3`- `dbm`backend. (Contributed by Raymond Hettinger and Erlend E. Aasland in- [gh-100414](https://github.com/python/cpython/issues/100414).)
- Allow removing all items from the database through the new - `clear()`methods of the GDBM and NDBM database objects. (Contributed by Donghee Na in- [gh-107122](https://github.com/python/cpython/issues/107122).)

### dis[¶](#dis)

- Change the output of - `dis`- `-O`- *show_offsets*argument. (Contributed by Irit Katriel in- [gh-112137](https://github.com/python/cpython/issues/112137).)
- `get_instructions()`- `Instruction`- *cache_info*field. The- *show_caches*argument to- `get_instructions()`is deprecated and no longer has any effect. (Contributed by Irit Katriel in- [gh-112962](https://github.com/python/cpython/issues/112962).)

### doctest[¶](#doctest)

- `doctest`- `PYTHON_COLORS`- `NO_COLOR`- `FORCE_COLOR`- [Controlling color](../using/cmdline.html#using-on-controlling-color). (Contributed by Hugo van Kemenade in- [gh-117225](https://github.com/python/cpython/issues/117225).)
- The - `DocTestRunner.run()`- `DocTestRunner.skips`- `TestResults.skipped`- [gh-108794](https://github.com/python/cpython/issues/108794).)

### email[¶](#email)

- Headers with embedded newlines are now quoted on output. The - `generator`- `verify_generated_headers`- [gh-121650](https://github.com/python/cpython/issues/121650).)
- `getaddresses()`- `parseaddr()`- `('', '')`pairs in more situations where invalid email addresses are encountered instead of potentially inaccurate values. The two functions have a new optional- *strict*parameter (default- `True`). To get the old behavior (accepting malformed input), use- `strict=False`.- `getattr(email.utils, 'supports_strict_parsing', False)`can be used to check if the- *strict*parameter is available. (Contributed by Thomas Dwyer and Victor Stinner for- [gh-102988](https://github.com/python/cpython/issues/102988)to improve the- **CVE 2023-27043**

### enum[¶](#enum)

### fractions[¶](#fractions)

- `Fraction`- [format specification mini-language](../library/string.html#formatspec)rules for fill, alignment, sign handling, minimum width, and grouping. (Contributed by Mark Dickinson in- [gh-111320](https://github.com/python/cpython/issues/111320).)

### glob[¶](#glob)

- Add - `translate()`- [gh-72904](https://github.com/python/cpython/issues/72904).)

### importlib[¶](#importlib)

- The following functions in - `importlib.resources`- *encoding*and- *errors*arguments in the text-reading functions are now keyword-only):- These functions are no longer deprecated and are not scheduled for removal. (Contributed by Petr Viktorin in - [gh-116608](https://github.com/python/cpython/issues/116608).)
- `contents()`- `Traversable`- [gh-116608](https://github.com/python/cpython/issues/116608).)

### io[¶](#io)

- The - `IOBase`- `close()`- `sys.unraisablehook`- [Python Development Mode](../library/devmode.html#devmode)or when using a- [Python debug build](../using/configure.html#debug-build). (Contributed by Victor Stinner in- [gh-62948](https://github.com/python/cpython/issues/62948).)

### ipaddress[¶](#ipaddress)

- Add the - `IPv4Address.ipv6_mapped`- [gh-109466](https://github.com/python/cpython/issues/109466).)
- Fix - `is_global`and- `is_private`behavior in- `IPv4Address`- `IPv6Address`- `IPv4Network`- `IPv6Network`- [gh-113171](https://github.com/python/cpython/issues/113171).)

### itertools[¶](#itertools)

- `batched()`- *strict*parameter, which raises a- `ValueError`- [gh-113202](https://github.com/python/cpython/issues/113202).)

### marshal[¶](#marshal)

- Add the - *allow_code*parameter in module functions. Passing- `allow_code=False`prevents serialization and de-serialization of code objects which are incompatible between Python versions. (Contributed by Serhiy Storchaka in- [gh-113626](https://github.com/python/cpython/issues/113626).)

### math[¶](#math)

- The new function - `fma()`- `x * y + z`with only a single round, and so avoids any intermediate loss of precision. It wraps the- `fma()`function provided by C99, and follows the specification of the IEEE 754 “fusedMultiplyAdd” operation for special cases. (Contributed by Mark Dickinson and Victor Stinner in- [gh-73468](https://github.com/python/cpython/issues/73468).)

### mimetypes[¶](#mimetypes)

- Add the - `guess_file_type()`- `guess_type()`- [soft deprecated](../glossary.html#term-soft-deprecated). (Contributed by Serhiy Storchaka in- [gh-66543](https://github.com/python/cpython/issues/66543).)

### mmap[¶](#mmap)

- `mmap`- [gh-118209](https://github.com/python/cpython/issues/118209).)
- `mmap`- `seekable()`- `seek()`- [gh-111835](https://github.com/python/cpython/issues/111835).)
- The new UNIX-only - *trackfd*parameter for- `mmap`- *fileno*will not be duplicated. (Contributed by Zackery Spytz and Petr Viktorin in- [gh-78502](https://github.com/python/cpython/issues/78502).)

### multiprocessing[¶](#multiprocessing)

- The default number of worker threads and processes is now selected using - `os.process_cpu_count()`- `os.cpu_count()`- [gh-109649](https://github.com/python/cpython/issues/109649).)

### os[¶](#os)

- Add - `process_cpu_count()`- [gh-109649](https://github.com/python/cpython/issues/109649).)
- `cpu_count()`- `process_cpu_count()`- `PYTHON_CPU_COUNT`- `-X cpu_count`- [gh-109595](https://github.com/python/cpython/issues/109595).)
- Add a - [low level interface](../library/os.html#os-timerfd)to Linux’s- [timer file descriptors](https://manpages.debian.org/timerfd_create(2))- `timerfd_create()`- `timerfd_settime()`- `timerfd_settime_ns()`- `timerfd_gettime()`- `timerfd_gettime_ns()`- `TFD_NONBLOCK`- `TFD_CLOEXEC`- `TFD_TIMER_ABSTIME`- `TFD_TIMER_CANCEL_ON_SET`- [gh-108277](https://github.com/python/cpython/issues/108277).)
- `lchmod()`- *follow_symlinks*argument of- `chmod()`- *follow_symlinks*in- `lchmod()`is- `False`on Windows. (Contributed by Serhiy Storchaka in- [gh-59616](https://github.com/python/cpython/issues/59616).)
- `fchmod()`- `chmod()`- [gh-113191](https://github.com/python/cpython/issues/113191).)
- On Windows, - `mkdir()`- `makedirs()`- *mode*value of- `0o700`to apply access control to the new directory. This implicitly affects- `tempfile.mkdtemp()`- **CVE 2024-4030**- *mode*continue to be ignored. (Contributed by Steve Dower in- [gh-118486](https://github.com/python/cpython/issues/118486).)
- `posix_spawn()`- `None`for the- *env*argument, which makes the newly spawned process use the current process environment. (Contributed by Jakub Kulik in- [gh-113119](https://github.com/python/cpython/issues/113119).)
- `posix_spawn()`- `POSIX_SPAWN_CLOSEFROM`- *file_actions*parameter on platforms that support- `posix_spawn_file_actions_addclosefrom_np()`. (Contributed by Jakub Kulik in- [gh-113117](https://github.com/python/cpython/issues/113117).)

### os.path[¶](#os-path)

- Add - `isreserved()`- [gh-88569](https://github.com/python/cpython/issues/88569).)
- On Windows, - `isabs()`- `\`or- `/`) to be absolute. (Contributed by Barney Gale and Jon Foster in- [gh-44626](https://github.com/python/cpython/issues/44626).)
- `realpath()`- [gh-82367](https://github.com/python/cpython/issues/82367).)

### pathlib[¶](#pathlib)

- Add - `UnsupportedOperation`- `NotImplementedError`- [gh-89812](https://github.com/python/cpython/issues/89812).)
- Add a new constructor for creating - `Path`- `file:///`),- `Path.from_uri()`- [gh-107465](https://github.com/python/cpython/issues/107465).)
- Add - `PurePath.full_match()`- `**`”. (Contributed by Barney Gale in- [gh-73435](https://github.com/python/cpython/issues/73435).)
- Add the - `PurePath.parser`- `os.path`- `posixpath`or- `ntpath`.
- Add - *recurse_symlinks*keyword-only argument to- `Path.glob()`- `rglob()`- [gh-77609](https://github.com/python/cpython/issues/77609).)
- `Path.glob()`- `rglob()`- `**`”. Previously, only directories were returned. (Contributed by Barney Gale in- [gh-70303](https://github.com/python/cpython/issues/70303).)
- Add the - *follow_symlinks*keyword-only argument to- `Path.is_file`- `Path.is_dir`- `Path.owner()`- `Path.group()`- [gh-105793](https://github.com/python/cpython/issues/105793)and Kamil Turek in- [gh-107962](https://github.com/python/cpython/issues/107962).)

### pdb[¶](#pdb)

- `breakpoint()`- `set_trace()`- `breakpoint()`is positioned at the end of the context. (Contributed by Tian Gao in- [gh-118579](https://github.com/python/cpython/issues/118579).)
- `sys.path[0]`is no longer replaced by the directory of the script being debugged when- `sys.flags.safe_path`- [gh-111762](https://github.com/python/cpython/issues/111762).)
- `zipapp`- [gh-118501](https://github.com/python/cpython/issues/118501).)
- Add ability to move between chained exceptions during post-mortem debugging in - `pm()`- `exceptions [exc_number]`- [gh-106676](https://github.com/python/cpython/issues/106676).)
- Expressions and statements whose prefix is a pdb command are now correctly identified and executed. (Contributed by Tian Gao in - [gh-108464](https://github.com/python/cpython/issues/108464).)

### queue[¶](#queue)

- Add - `Queue.shutdown`- `ShutDown`- [gh-104750](https://github.com/python/cpython/issues/104750).)

### random[¶](#random)

- Add a - [command-line interface](../library/random.html#random-cli). (Contributed by Hugo van Kemenade in- [gh-118131](https://github.com/python/cpython/issues/118131).)

### re[¶](#re)

- Rename - `re.error`to- `PatternError`- `re.error`is kept for backward compatibility.

### shutil[¶](#shutil)

### site[¶](#site)

- `.pth`files are now decoded using UTF-8 first, and then with the- [locale encoding](../glossary.html#term-locale-encoding)if UTF-8 decoding fails. (Contributed by Inada Naoki in- [gh-117802](https://github.com/python/cpython/issues/117802).)

### sqlite3[¶](#sqlite3)

- A - `ResourceWarning`- `Connection`- `closed`- [gh-105539](https://github.com/python/cpython/issues/105539).)
- Add the - *filter*keyword-only parameter to- `Connection.iterdump()`- [gh-91602](https://github.com/python/cpython/issues/91602).)

### ssl[¶](#ssl)

- The - `create_default_context()`- `VERIFY_X509_PARTIAL_CHAIN`- `VERIFY_X509_STRICT`- Note - `VERIFY_X509_STRICT`- **RFC 5280**- import ssl ctx = ssl.create_default_context() ctx.verify_flags &= ~ssl.VERIFY_X509_STRICT - (Contributed by William Woodruff in - [gh-112389](https://github.com/python/cpython/issues/112389).)

### statistics[¶](#statistics)

- Add - `kde()`- [gh-115863](https://github.com/python/cpython/issues/115863).)
- Add - `kde_random()`- `kde()`- [gh-115863](https://github.com/python/cpython/issues/115863).)

### subprocess[¶](#subprocess)

- The - `subprocess`- `posix_spawn()`- Notably, when - *close_fds*is- `True`(the default),- `posix_spawn()`- `posix_spawn_file_actions_addclosefrom_np()`, which includes recent versions of Linux, FreeBSD, and Solaris. On Linux, this should perform similarly to the existing Linux- `vfork()`based code.- A private control knob - `subprocess._USE_POSIX_SPAWN`can be set to- `False`if you need to force- `subprocess`- `posix_spawn()`- [issue tracker](../bugs.html#using-the-tracker)if you set this so that we can improve our API selection logic for everyone. (Contributed by Jakub Kulik in- [gh-113117](https://github.com/python/cpython/issues/113117).)

### sys[¶](#sys)

- Add the - `_is_interned()`- [gh-78573](https://github.com/python/cpython/issues/78573).)

### tempfile[¶](#tempfile)

- On Windows, the default mode - `0o700`used by- `tempfile.mkdtemp()`- `os.mkdir()`- **CVE 2024-4030**- [gh-118486](https://github.com/python/cpython/issues/118486).)

### time[¶](#time)

- On Windows, - `monotonic()`- `QueryPerformanceCounter()`clock for a resolution of 1 microsecond, instead of the- `GetTickCount64()`clock which has a resolution of 15.6 milliseconds. (Contributed by Victor Stinner in- [gh-88494](https://github.com/python/cpython/issues/88494).)
- On Windows, - `time()`- `GetSystemTimePreciseAsFileTime()`clock for a resolution of 1 microsecond, instead of the- `GetSystemTimeAsFileTime()`clock which has a resolution of 15.6 milliseconds. (Contributed by Victor Stinner in- [gh-63207](https://github.com/python/cpython/issues/63207).)

### tkinter[¶](#tkinter)

- Add - `tkinter`- `tk_busy_hold()`,- `tk_busy_configure()`,- `tk_busy_cget()`,- `tk_busy_forget()`,- `tk_busy_current()`, and- `tk_busy_status()`. (Contributed by Miguel, klappnase and Serhiy Storchaka in- [gh-72684](https://github.com/python/cpython/issues/72684).)
- The - `tkinter`- `wm_attributes()`now accepts the attribute name without the minus prefix to get window attributes, for example- `w.wm_attributes('alpha')`and allows specifying attributes and values to set as keyword arguments, for example- `w.wm_attributes(alpha=0.5)`. (Contributed by Serhiy Storchaka in- [gh-43457](https://github.com/python/cpython/issues/43457).)
- `wm_attributes()`can now return attributes as a- `dict`- *return_python_dict*. (Contributed by Serhiy Storchaka in- [gh-43457](https://github.com/python/cpython/issues/43457).)
- `Text.count()`can now return a simple- `int`- *return_ints*is used. Otherwise, the single count is returned as a 1-tuple or- `None`. (Contributed by Serhiy Storchaka in- [gh-97928](https://github.com/python/cpython/issues/97928).)
- Support the “vsapi” element type in the - `element_create()`- `tkinter.ttk.Style`- [gh-68166](https://github.com/python/cpython/issues/68166).)
- Add the - `after_info()`method for Tkinter widgets. (Contributed by Cheryl Sabella in- [gh-77020](https://github.com/python/cpython/issues/77020).)
- Add a new - `copy_replace()`method to- `PhotoImage`to copy a region from one image to another, possibly with pixel zooming, subsampling, or both. (Contributed by Serhiy Storchaka in- [gh-118225](https://github.com/python/cpython/issues/118225).)
- Add - *from_coords*parameter to the- `PhotoImage`methods- `copy()`,- `zoom()`and- `subsample()`. Add- *zoom*and- *subsample*parameters to the- `PhotoImage`method- `copy()`. (Contributed by Serhiy Storchaka in- [gh-118225](https://github.com/python/cpython/issues/118225).)
- Add the - `PhotoImage`methods- `read()`to read an image from a file and- `data()`to get the image data. Add- *background*and- *grayscale*parameters to the- `write()`method. (Contributed by Serhiy Storchaka in- [gh-118271](https://github.com/python/cpython/issues/118271).)

### traceback[¶](#traceback)

- Add the - `exc_type_str`- `TracebackException`- *exc_type*. Deprecate the- `exc_type`- *save_exc_type*(default- `True`) to indicate whether- `exc_type`should be saved. (Contributed by Irit Katriel in- [gh-112332](https://github.com/python/cpython/issues/112332).)
- Add a new - *show_group*keyword-only parameter to- `TracebackException.format_exception_only()`- `BaseExceptionGroup`- [gh-105292](https://github.com/python/cpython/issues/105292).)

### types[¶](#types)

- `SimpleNamespace`- [gh-108191](https://github.com/python/cpython/issues/108191).)

### typing[¶](#typing)

- **PEP 705**- `ReadOnly`- `TypedDict`
- **PEP 742**- `TypeIs`
- Add - `NoDefault`- `typing`- [gh-116126](https://github.com/python/cpython/issues/116126).)
- Add - `get_protocol_members()`- `typing.Protocol`- [gh-104873](https://github.com/python/cpython/issues/104873).)
- Add - `is_protocol()`- `Protocol`- [gh-104873](https://github.com/python/cpython/issues/104873).)
- `ClassVar`- `Final`- [gh-89547](https://github.com/python/cpython/issues/89547).)

### unicodedata[¶](#unicodedata)

- Update the Unicode database to - [version 15.1.0](https://www.unicode.org/versions/Unicode15.1.0/). (Contributed by James Gerity in- [gh-109559](https://github.com/python/cpython/issues/109559).)

### venv[¶](#venv)

- Add support for creating source control management (SCM) ignore files in a virtual environment’s directory. By default, Git is supported. This is implemented as opt-in via the API, which can be extended to support other SCMs ( - `EnvBuilder`- `create()`- `--without-scm-ignore-files`. (Contributed by Brett Cannon in- [gh-108125](https://github.com/python/cpython/issues/108125).)

### warnings[¶](#warnings)

- **PEP 702**- `warnings.deprecated()`- [static type checker](../glossary.html#term-static-type-checker)and to warn on usage of deprecated classes and functions. A- `DeprecationWarning`- [gh-104003](https://github.com/python/cpython/issues/104003).)

### xml[¶](#xml)

- Allow controlling Expat >=2.6.0 reparse deferral ( - **CVE 2023-52425**
- `xml.sax.expatreader.ExpatParser.flush()`
 - (Contributed by Sebastian Pipping in - [gh-115623](https://github.com/python/cpython/issues/115623).)
- Add the - `close()`method for the iterator returned by- `iterparse()`- [gh-69893](https://github.com/python/cpython/issues/69893).)

### zipimport[¶](#zipimport)

## Optimizations[¶](#optimizations)

- Several standard library modules have had their import times significantly improved. For example, the import time of the - `typing`- `re`- `contextlib`- `email.utils`- `enum`- `functools`- `importlib.metadata`- `threading`- [gh-109653](https://github.com/python/cpython/issues/109653).)
- `textwrap.indent()`- [gh-107369](https://github.com/python/cpython/issues/107369).)
- The - `subprocess`- `posix_spawn()`- *close_fds*is- `True`(the default) on many modern platforms. This should provide a notable performance increase when launching processes on FreeBSD and Solaris. See the- [subprocess](#whatsnew313-subprocess)section above for details. (Contributed by Jakub Kulik in- [gh-113117](https://github.com/python/cpython/issues/113117).)

## Removed Modules And APIs[¶](#removed-modules-and-apis)

### PEP 594: Remove “dead batteries” from the standard library[¶](#pep-594-remove-dead-batteries-from-the-standard-library)

[ PEP 594](https://peps.python.org/pep-0594/) proposed removing 19 modules from the standard library,
colloquially referred to as ‘dead batteries’ due to their
historic, obsolete, or insecure status.
All of the following modules were deprecated in Python 3.11,
and are now removed:

- `aifc`- [standard-aifc](https://pypi.org/project/standard-aifc/): Use the redistribution of- `aifc`library from PyPI.
 
- `audioop`- [audioop-lts](https://pypi.org/project/audioop-lts/): Use- `audioop-lts`library from PyPI.
 
- `chunk`- [standard-chunk](https://pypi.org/project/standard-chunk/): Use the redistribution of- `chunk`library from PyPI.
 
- `cgi`and- `cgitb`- `cgi.FieldStorage`can typically be replaced with- `urllib.parse.parse_qsl()`- `GET`and- `HEAD`requests, and the- `email.message`- [multipart](https://pypi.org/project/multipart/)library for- `POST`and- `PUT`requests.
- `cgi.parse()`can be replaced by calling- `urllib.parse.parse_qs()`- `multipart/form-data`, which should be replaced as described below for- `cgi.parse_multipart()`.
- `cgi.parse_header()`can be replaced with the functionality in the- `email`- `email.message.EmailMessage`- from email.message import EmailMessage msg = EmailMessage() msg['content-type'] = 'application/json; charset="utf8"' main, params = msg.get_content_type(), msg['content-type'].params 
- `cgi.parse_multipart()`can be replaced with the functionality in the- `email`- [multipart](https://pypi.org/project/multipart/)library. For example, the- `email.message.EmailMessage`- `email.message.Message`
- [standard-cgi](https://pypi.org/project/standard-cgi/): and- [standard-cgitb](https://pypi.org/project/standard-cgitb/): Use the redistribution of- `cgi`and- `cgitb`library from PyPI.
 
- `crypt`and the private- `_crypt`extension. The- `hashlib`- [bcrypt](https://pypi.org/project/bcrypt/): Modern password hashing for your software and your servers.
- [argon2-cffi](https://pypi.org/project/argon2-cffi/): The secure Argon2 password hashing algorithm.
- [legacycrypt](https://pypi.org/project/legacycrypt/):- `ctypes`
- [crypt_r](https://pypi.org/project/crypt_r/): Fork of the- `crypt`module, wrapper to the- [crypt_r(3)](https://manpages.debian.org/crypt_r(3))
- [standard-crypt](https://pypi.org/project/standard-crypt/)and- [deprecated-crypt-alternative](https://pypi.org/project/deprecated-crypt-alternative/): Use the redistribution of- `crypt`and reimplementation of- `_crypt`libraries from PyPI.
 
- `imghdr`: The- [filetype](https://pypi.org/project/filetype/),- [puremagic](https://pypi.org/project/puremagic/), or- [python-magic](https://pypi.org/project/python-magic/)libraries should be used as replacements. For example, the- `puremagic.what()`function can be used to replace the- `imghdr.what()`function for all file formats that were supported by- `imghdr`.- [standard-imghdr](https://pypi.org/project/standard-imghdr/): Use the redistribution of- `imghdr`library from PyPI.
 
- `mailcap`: Use the- `mimetypes`- [standard-mailcap](https://pypi.org/project/standard-mailcap/): Use the redistribution of- `mailcap`library from PyPI.
 
- `msilib`
- `nis`
- `nntplib`: Use the- [pynntp](https://pypi.org/project/pynntp/)library from PyPI instead.- [standard-nntplib](https://pypi.org/project/standard-nntplib/): Use the redistribution of- `nntplib`library from PyPI.
 
- `ossaudiodev`: For audio playback, use the- [pygame](https://pypi.org/project/pygame/)library from PyPI instead.
- `pipes`: Use the- `subprocess`- `shlex.quote()`- `pipes.quote`function.- [standard-pipes](https://pypi.org/project/standard-pipes/): Use the redistribution of- `pipes`library from PyPI.
 
- `sndhdr`: The- [filetype](https://pypi.org/project/filetype/),- [puremagic](https://pypi.org/project/puremagic/), or- [python-magic](https://pypi.org/project/python-magic/)libraries should be used as replacements.- [standard-sndhdr](https://pypi.org/project/standard-sndhdr/): Use the redistribution of- `sndhdr`library from PyPI.
 
- `spwd`: Use the- [python-pam](https://pypi.org/project/python-pam/)library from PyPI instead.
- `sunau`- [standard-sunau](https://pypi.org/project/standard-sunau/): Use the redistribution of- `sunau`library from PyPI.
 
- `telnetlib`, Use the- [telnetlib3](https://pypi.org/project/telnetlib3/)or- [Exscript](https://pypi.org/project/Exscript/)libraries from PyPI instead.- [standard-telnetlib](https://pypi.org/project/standard-telnetlib/): Use the redistribution of- `telnetlib`library from PyPI.
 
- `uu`: Use the- `base64`- [standard-uu](https://pypi.org/project/standard-uu/): Use the redistribution of- `uu`library from PyPI.
 
- `xdrlib`- [standard-xdrlib](https://pypi.org/project/standard-xdrlib/): Use the redistribution of- `xdrlib`library from PyPI.
 

(Contributed by Victor Stinner and Zachary Ware in [gh-104773](https://github.com/python/cpython/issues/104773) and [gh-104780](https://github.com/python/cpython/issues/104780).)

### 2to3[¶](#to3)

- Remove the - **2to3**program and the- `lib2to3`module, previously deprecated in Python 3.11. (Contributed by Victor Stinner in- [gh-104780](https://github.com/python/cpython/issues/104780).)

### builtins[¶](#builtins)

- Remove support for chained - `classmethod`- [gh-63272](https://github.com/python/cpython/issues/63272)). These can no longer be used to wrap other descriptors, such as- `property`- `classmethod`, consider using the- `__wrapped__`attribute that was added in Python 3.10. (Contributed by Raymond Hettinger in- [gh-89519](https://github.com/python/cpython/issues/89519).)
- Raise a - `RuntimeError`- `frame.clear()`- [gh-79932](https://github.com/python/cpython/issues/79932).)

### configparser[¶](#id3)

- Remove the undocumented - `LegacyInterpolation`class, deprecated in the docstring since Python 3.2, and at runtime since Python 3.11. (Contributed by Hugo van Kemenade in- [gh-104886](https://github.com/python/cpython/issues/104886).)

### importlib.metadata[¶](#importlib-metadata)

- Remove deprecated subscript ( - `__getitem__()`- [EntryPoint](../library/importlib.metadata.html#entry-points)objects. (Contributed by Jason R. Coombs in- [gh-113175](https://github.com/python/cpython/issues/113175).)

### locale[¶](#locale)

- Remove the - `locale.resetlocale()`function, deprecated in Python 3.11. Use- `locale.setlocale(locale.LC_ALL, "")`instead. (Contributed by Victor Stinner in- [gh-104783](https://github.com/python/cpython/issues/104783).)

### opcode[¶](#opcode)

- Move - `opcode.ENABLE_SPECIALIZATION`to- `_opcode.ENABLE_SPECIALIZATION`. This field was added in 3.12, it was never documented, and is not intended for external use. (Contributed by Irit Katriel in- [gh-105481](https://github.com/python/cpython/issues/105481).)
- Remove - `opcode.is_pseudo()`,- `opcode.MIN_PSEUDO_OPCODE`, and- `opcode.MAX_PSEUDO_OPCODE`, which were added in Python 3.12, but were neither documented nor exposed through- `dis`- [gh-105481](https://github.com/python/cpython/issues/105481).)

### optparse[¶](#optparse)

- This module is no longer considered - [soft deprecated](../glossary.html#term-soft-deprecated). While- `argparse`- `argparse`works that mean the lower level- `optparse`module may provide a better foundation for- *writing*argument processing libraries, and for implementing command line applications which adhere more strictly than- `argparse`does to various Unix command line processing conventions that originate in the behaviour of the C- `getopt()`function . (Contributed by Alyssa Coghlan and Serhiy Storchaka in- [gh-126180](https://github.com/python/cpython/issues/126180).)

### pathlib[¶](#id4)

### re[¶](#id5)

- Remove the undocumented, deprecated, and broken - `re.template()`function and- `re.TEMPLATE`/- `re.T`flag. (Contributed by Serhiy Storchaka and Nikita Sobolev in- [gh-105687](https://github.com/python/cpython/issues/105687).)

### tkinter.tix[¶](#tkinter-tix)

- Remove the - `tkinter.tix`module, deprecated in Python 3.6. The third-party Tix library which the module wrapped is unmaintained. (Contributed by Zachary Ware in- [gh-75552](https://github.com/python/cpython/issues/75552).)

### turtle[¶](#turtle)

- Remove the - `RawTurtle.settiltangle()`method, deprecated in the documentation since Python 3.1 and at runtime since Python 3.11. (Contributed by Hugo van Kemenade in- [gh-104876](https://github.com/python/cpython/issues/104876).)

### typing[¶](#id6)

- Remove the - `typing.io`and- `typing.re`namespaces, deprecated since Python 3.8. The items in those namespaces can be imported directly from the- `typing`- [gh-92871](https://github.com/python/cpython/issues/92871).)
- Remove the keyword-argument method of creating - `TypedDict`- [gh-104786](https://github.com/python/cpython/issues/104786).)

### unittest[¶](#unittest)

- Remove the following - `unittest`- `unittest.findTestCases()`
- `unittest.makeSuite()`
- `unittest.getTestCaseNames()`
 - Use - `TestLoader`- (Contributed by Hugo van Kemenade in - [gh-104835](https://github.com/python/cpython/issues/104835).)
- Remove the untested and undocumented - `TestProgram.usageExit()`method, deprecated in Python 3.11. (Contributed by Hugo van Kemenade in- [gh-104992](https://github.com/python/cpython/issues/104992).)

### urllib[¶](#urllib)

- Remove the - *cafile*,- *capath*, and- *cadefault*parameters of the- `urllib.request.urlopen()`- *context*parameter instead with an- `SSLContext`- `ssl.SSLContext.load_cert_chain()`- `ssl.create_default_context()`- [gh-105382](https://github.com/python/cpython/issues/105382).)

### webbrowser[¶](#webbrowser)

- Remove the untested and undocumented - `MacOSX`class, deprecated in Python 3.11. Use the- `MacOSXOSAScript`class (introduced in Python 3.2) instead. (Contributed by Hugo van Kemenade in- [gh-104804](https://github.com/python/cpython/issues/104804).)
- Remove the deprecated - `MacOSXOSAScript._name`attribute. Use the- `MacOSXOSAScript.name`- [gh-105546](https://github.com/python/cpython/issues/105546).)

## New Deprecations[¶](#new-deprecations)

- 
- Deprecate the undocumented - `SetPointerType()`function, to be removed in Python 3.15. (Contributed by Victor Stinner in- [gh-105733](https://github.com/python/cpython/issues/105733).)
- [Soft-deprecate](../glossary.html#term-soft-deprecated)the- `ARRAY()`- `type * length`multiplication. (Contributed by Victor Stinner in- [gh-105733](https://github.com/python/cpython/issues/105733).)
 
- `dis`
- 
- Deprecate non-integer numbers as arguments to functions and methods that consider plural forms in the - `gettext`module, even if no translation was found. (Contributed by Serhiy Storchaka in- [gh-88434](https://github.com/python/cpython/issues/88434).)
 
- `glob`- Deprecate the undocumented - `glob0()`and- `glob1()`functions. Use- `glob()`- [path-like object](../glossary.html#term-path-like-object)specifying the root directory to the- *root_dir*parameter instead. (Contributed by Barney Gale in- [gh-117337](https://github.com/python/cpython/issues/117337).)
 
- 
- Deprecate - `CGIHTTPRequestHandler`- [gh-109096](https://github.com/python/cpython/issues/109096).)
- Deprecate the - `--cgi`flag to the- **python -m http.server**command-line interface, to be removed in Python 3.15. (Contributed by Gregory P. Smith in- [gh-109096](https://github.com/python/cpython/issues/109096).)
 
- 
- [Soft-deprecate](../glossary.html#term-soft-deprecated)file path arguments to- `guess_type()`- `guess_file_type()`- [gh-66543](https://github.com/python/cpython/issues/66543).)
 
- `re`- Deprecate passing the optional - *maxsplit*,- *count*, or- *flags*arguments as positional arguments to the module-level- `split()`- `sub()`- `subn()`- [keyword-only](../glossary.html#keyword-only-parameter)in a future version of Python. (Contributed by Serhiy Storchaka in- [gh-56166](https://github.com/python/cpython/issues/56166).)
 
- 
- Deprecate - `PurePath.is_reserved()`- `os.path.isreserved()`- [gh-88569](https://github.com/python/cpython/issues/88569).)
 
- 
- Deprecate - `java_ver()`- [gh-116349](https://github.com/python/cpython/issues/116349).)
 
- 
- Deprecate the undocumented - `ispackage()`function. (Contributed by Zackery Spytz in- [gh-64020](https://github.com/python/cpython/issues/64020).)
 
- 
- Deprecate passing more than one positional argument to the - `connect()`- `Connection`- [gh-107948](https://github.com/python/cpython/issues/107948).)
- Deprecate passing name, number of arguments, and the callable as keyword arguments for - `Connection.create_function()`- `Connection.create_aggregate()`- [gh-108278](https://github.com/python/cpython/issues/108278).)
- Deprecate passing the callback callable by keyword for the - `set_authorizer()`- `set_progress_handler()`- `set_trace_callback()`- `Connection`- [gh-108278](https://github.com/python/cpython/issues/108278).)
 
- `sys`- Deprecate the - `_enablelegacywindowsfsencoding()`- `PYTHONLEGACYWINDOWSFSENCODING`- [gh-73427](https://github.com/python/cpython/issues/73427).)
 
- 
- Deprecate the undocumented and unused - `TarFile.tarfile`attribute, to be removed in Python 3.16. (Contributed in- [gh-115256](https://github.com/python/cpython/issues/115256).)
 
- 
- Deprecate the - `TracebackException.exc_type`- `TracebackException.exc_type_str`- [gh-112332](https://github.com/python/cpython/issues/112332).)
 
- 
- Deprecate the undocumented keyword argument syntax for creating - `NamedTuple`- `Point = NamedTuple("Point", x=int, y=int)`), to be removed in Python 3.15. Use the class-based syntax or the functional syntax instead. (Contributed by Alex Waygood in- [gh-105566](https://github.com/python/cpython/issues/105566).)
- Deprecate omitting the - *fields*parameter when creating a- `NamedTuple`- `typing.TypedDict`- `None`to the- *fields*parameter of both types. Python 3.15 will require a valid sequence for the- *fields*parameter. To create a NamedTuple class with zero fields, use- `class NT(NamedTuple): pass`or- `NT = NamedTuple("NT", ())`. To create a TypedDict class with zero fields, use- `class TD(TypedDict): pass`or- `TD = TypedDict("TD", {})`. (Contributed by Alex Waygood in- [gh-105566](https://github.com/python/cpython/issues/105566)and- [gh-105570](https://github.com/python/cpython/issues/105570).)
- Deprecate the - `typing.no_type_check_decorator()`- `typing`- [gh-106309](https://github.com/python/cpython/issues/106309).)
- Deprecate - `typing.AnyStr`- `typing.__all__`, and a- `DeprecationWarning`- [type parameter syntax](../reference/compound_stmts.html#type-params)instead. (Contributed by Michael The in- [gh-107116](https://github.com/python/cpython/issues/107116).)
 
- `wave`- Deprecate the - `getmark()`- `setmark()`, and- `getmarkers()`- `Wave_read`- `Wave_write`- [gh-105096](https://github.com/python/cpython/issues/105096).)
 

### Pending Removal in Python 3.14[¶](#pending-removal-in-python-3-14)

- `argparse`- *type*,- *choices*, and- *metavar*parameters of- `argparse.BooleanOptionalAction`are deprecated and will be removed in 3.14. (Contributed by Nikita Sobolev in- [gh-92248](https://github.com/python/cpython/issues/92248).)
- `ast`- `DeprecationWarning`- `ast.Num`
- `ast.Str`
- `ast.Bytes`
- `ast.NameConstant`
- `ast.Ellipsis`
 - Use - `ast.Constant`- [gh-90953](https://github.com/python/cpython/issues/90953).)
- 
- The child watcher classes - `MultiLoopChildWatcher`- `FastChildWatcher`- `AbstractChildWatcher`- `SafeChildWatcher`- [gh-94597](https://github.com/python/cpython/issues/94597).)
- `asyncio.set_child_watcher()`- `asyncio.get_child_watcher()`- `asyncio.AbstractEventLoopPolicy.set_child_watcher()`- `asyncio.AbstractEventLoopPolicy.get_child_watcher()`- [gh-94597](https://github.com/python/cpython/issues/94597).)
- The - `get_event_loop()`- `DeprecationWarning`- [gh-100160](https://github.com/python/cpython/issues/100160).)
 
- `builtins`- `bool(NotImplemented)`now emits a- `DeprecationWarning`- `TypeError`- [gh-118767](https://github.com/python/cpython/issues/118767).)
- `email`- *isdst*parameter in- `email.utils.localtime()`- [gh-72346](https://github.com/python/cpython/issues/72346).)
- `importlib.abc`- `importlib.abc.ResourceReader`
- `importlib.abc.Traversable`
- `importlib.abc.TraversableResources`
 - Use - `importlib.resources.abc`- (Contributed by Jason R. Coombs and Hugo van Kemenade in - [gh-93963](https://github.com/python/cpython/issues/93963).)
- `itertools`- [gh-101588](https://github.com/python/cpython/issues/101588).)
- `multiprocessing`- `'fork'`is currently the default (- [gh-84559](https://github.com/python/cpython/issues/84559)). Adding a runtime warning about this was deemed too disruptive as the majority of code is not expected to care. Use the- `get_context()`- `set_start_method()`- *requires*- `'fork'`. See- [Contexts and start methods](../library/multiprocessing.html#multiprocessing-start-methods).
- `pathlib`- `is_relative_to()`- `relative_to()`
- `pkgutil`- `find_loader()`- `get_loader()`- `DeprecationWarning`- `importlib.util.find_spec()`- [gh-97850](https://github.com/python/cpython/issues/97850).)
- `pty`- `master_open()`: use- `pty.openpty()`
- `slave_open()`: use- `pty.openpty()`
 
- 
- `version`- `version_info`
- `execute()`- `executemany()`- [named placeholders](../library/sqlite3.html#sqlite3-placeholders)are used and- *parameters*is a sequence instead of a- `dict`
 
- `urllib`- `urllib.parse.Quoter`is deprecated: it was not intended to be a public API. (Contributed by Gregory P. Smith in- [gh-88168](https://github.com/python/cpython/issues/88168).)

### Pending Removal in Python 3.15[¶](#pending-removal-in-python-3-15)

- The import system: - Setting - `__cached__`- `__spec__.cached`- `__cached__`will cease to be set or take into consideration by the import system or standard library. (- [gh-97879](https://github.com/python/cpython/issues/97879))
- Setting - `__package__`- `__spec__.parent`- `__package__`will cease to be set or take into consideration by the import system or standard library. (- [gh-97879](https://github.com/python/cpython/issues/97879))
 
- 
- The undocumented - `ctypes.SetPointerType()`function has been deprecated since Python 3.13.
 
- 
- The obsolete and rarely used - `CGIHTTPRequestHandler`- *Anything*is better than CGI to interface a web server with a request handler.
- The - `--cgi`flag to the- **python -m http.server**command-line interface has been deprecated since Python 3.13.
 
- 
- `load_module()`method: use- `exec_module()`instead.
 
- 
- `PurePath.is_reserved()`- `os.path.isreserved()`
 
- 
- `java_ver()`
 
- 
- The - *check_home*argument of- `sysconfig.is_python_build()`
 
- 
- `RLock()`
 
- 
- `types.CodeType`- `co_lnotab`- **PEP 626**- `DeprecationWarning`- [gh-101866](https://github.com/python/cpython/issues/101866).)
 
- 
- The undocumented keyword argument syntax for creating - `NamedTuple`- `Point = NamedTuple("Point", x=int, y=int)`) has been deprecated since Python 3.13. Use the class-based syntax or the functional syntax instead.
- When using the functional syntax of - `TypedDict`- *fields*parameter (- `TD = TypedDict("TD")`) or passing- `None`(- `TD = TypedDict("TD", None)`) has been deprecated since Python 3.13. Use- `class TD(TypedDict): pass`or- `TD = TypedDict("TD", {})`to create a TypedDict with zero field.
- The - `typing.no_type_check_decorator()`- `typing`
 
- `wave`- The - `getmark()`- `setmark()`, and- `getmarkers()`- `Wave_read`- `Wave_write`
 

### Pending removal in Python 3.16[¶](#pending-removal-in-python-3-16)

- The import system: - Setting - `__loader__`- `__spec__.loader`- `__loader__`will cease to be set or taken into consideration by the import system or the standard library.
 
- 
- The - `'u'`format code (- `wchar_t`) has been deprecated in documentation since Python 3.3 and at runtime since Python 3.13. Use the- `'w'`format code (- `Py_UCS4`
 
- 
- `asyncio.iscoroutinefunction()`is deprecated and will be removed in Python 3.16, use- `inspect.iscoroutinefunction()`- [gh-122875](https://github.com/python/cpython/issues/122875).)
 
- 
- Bitwise inversion on boolean types, - `~True`or- `~False`has been deprecated since Python 3.12, as it produces surprising and unintuitive results (- `-2`and- `-1`). Use- `not x`instead for the logical negation of a Boolean. In the rare case that you need the bitwise inversion of the underlying integer, convert to- `int`explicitly (- `~int(x)`).
 
- 
- The - `ExecError`exception has been deprecated since Python 3.14. It has not been used by any function in- `shutil`since Python 3.4, and is now an alias of- `RuntimeError`
 
- 
- The - `Class.get_methods`
 
- `sys`- The - `_enablelegacywindowsfsencoding()`- `PYTHONLEGACYWINDOWSFSENCODING`
 
- 
- The undocumented and unused - `TarFile.tarfile`attribute has been deprecated since Python 3.13.
 

### Pending removal in Python 3.17[¶](#pending-removal-in-python-3-17)

- 
- `collections.abc.ByteString`- Use - `isinstance(obj, collections.abc.Buffer)`to test if- `obj`implements the- [buffer protocol](../c-api/buffer.html#bufferobjects)at runtime. For use in type annotations, either use- `Buffer`- `bytes | bytearray | memoryview`).- `ByteString`was originally intended to be an abstract class that would serve as a supertype of both- `bytes`- `bytearray`- `ByteString`never actually told you anything useful about the object. Other common buffer types such as- `memoryview`- `ByteString`(either at runtime or by static type checkers).- See - **PEP 688**- [gh-91896](https://github.com/python/cpython/issues/91896).)
 
- 
- Before Python 3.14, old-style unions were implemented using the private class - `typing._UnionGenericAlias`. This class is no longer needed for the implementation, but it has been retained for backward compatibility, with removal scheduled for Python 3.17. Users should use documented introspection helpers like- `typing.get_origin()`- `typing.get_args()`
- `typing.ByteString`- Use - `isinstance(obj, collections.abc.Buffer)`to test if- `obj`implements the- [buffer protocol](../c-api/buffer.html#bufferobjects)at runtime. For use in type annotations, either use- `Buffer`- `bytes | bytearray | memoryview`).- `ByteString`was originally intended to be an abstract class that would serve as a supertype of both- `bytes`- `bytearray`- `ByteString`never actually told you anything useful about the object. Other common buffer types such as- `memoryview`- `ByteString`(either at runtime or by static type checkers).- See - **PEP 688**- [gh-91896](https://github.com/python/cpython/issues/91896).)
 

### Pending removal in Python 3.18[¶](#pending-removal-in-python-3-18)

### Pending Removal in Future Versions[¶](#pending-removal-in-future-versions)

The following APIs will be removed in the future, although there is currently no date scheduled for their removal.

- `argparse`
- 
- Generators: - `throw(type, exc, tb)`and- `athrow(type, exc, tb)`signature is deprecated: use- `throw(exc)`and- `athrow(exc)`instead, the single argument signature.
- Currently Python accepts numeric literals immediately followed by keywords, for example - `0in x`,- `1or x`,- `0if 1else 2`. It allows confusing and ambiguous expressions like- `[0x1for x in y]`(which can be interpreted as- `[0x1 for x in y]`or- `[0x1f or x in y]`). A syntax warning is raised if the numeric literal is immediately followed by one of keywords- `and`- `else`- `for`- `if`- `in`- `is`- `or`- [gh-87999](https://github.com/python/cpython/issues/87999))
- Support for - `__index__()`and- `__int__()`method returning non-int type: these methods will be required to return an instance of a strict subclass of- `int`
- Support for - `__float__()`method returning a strict subclass of- `float`- `float`.
- Support for - `__complex__()`method returning a strict subclass of- `complex`- `complex`.
- Delegation of - `int()`to- `__trunc__()`method.
- Passing a complex number as the - *real*or- *imag*argument in the- `complex()`- [gh-109218](https://github.com/python/cpython/issues/109218).)
 
- `calendar`- `calendar.January`and- `calendar.February`constants are deprecated and replaced by- `calendar.JANUARY`- `calendar.FEBRUARY`- [gh-103636](https://github.com/python/cpython/issues/103636).)
- `codeobject.co_lnotab`- `codeobject.co_lines()`
- 
- `utcnow()`- `datetime.datetime.now(tz=datetime.UTC)`.
- `utcfromtimestamp()`- `datetime.datetime.fromtimestamp(timestamp, tz=datetime.UTC)`.
 
- `gettext`
- 
- `cache_from_source()`- *debug_override*parameter is deprecated: use the- *optimization*parameter instead.
 
- 
- `EntryPoints`tuple interface.
- Implicit - `None`on return values.
 
- `logging`- `warn()`method has been deprecated since Python 3.3, use- `warning()`
- `mailbox`
- `os`- `os.register_at_fork()`
- `pydoc.ErrorDuringImport`: A tuple value for- *exc_info*parameter is deprecated, use an exception instance.
- `re`- [gh-91760](https://github.com/python/cpython/issues/91760).)
- `sre_compile`,- `sre_constants`and- `sre_parse`modules.
- `shutil`- `rmtree()`- *onerror*parameter is deprecated in Python 3.12; use the- *onexc*parameter instead.
- `ssl`- `ssl.SSLContext`
- `ssl.SSLContext`- `set_npn_protocols()`- `selected_npn_protocol()`are deprecated: use ALPN instead.
- `ssl.OP_NO_SSL*`options
- `ssl.OP_NO_TLS*`options
- `ssl.PROTOCOL_SSLv3`
- `ssl.PROTOCOL_TLS`
- `ssl.PROTOCOL_TLSv1`
- `ssl.PROTOCOL_TLSv1_1`
- `ssl.PROTOCOL_TLSv1_2`
- `ssl.TLSVersion.SSLv3`
- `ssl.TLSVersion.TLSv1`
- `ssl.TLSVersion.TLSv1_1`
 
- `threading`- `threading.Condition.notifyAll()`: use- `notify_all()`
- `threading.Event.isSet()`: use- `is_set()`
- `threading.Thread.isDaemon()`,- `threading.Thread.setDaemon()`- `threading.Thread.daemon`
- `threading.Thread.getName()`,- `threading.Thread.setName()`- `threading.Thread.name`
- `threading.currentThread()`: use- `threading.current_thread()`
- `threading.activeCount()`: use- `threading.active_count()`
 
- `unittest.IsolatedAsyncioTestCase`- `None`from a test case.
- `urllib.parse`- `urlparse()`- `splitattr()`
- `splithost()`
- `splitnport()`
- `splitpasswd()`
- `splitport()`
- `splitquery()`
- `splittag()`
- `splittype()`
- `splituser()`
- `splitvalue()`
- `to_bytes()`
 
- `urllib.request`- `URLopener`- `FancyURLopener`- `urlopen()`
- `wsgiref`- `SimpleHandler.stdout.write()`should not do partial writes.
- `xml.etree.ElementTree`- `Element`- `True`. Prefer explicit- `len(elem)`or- `elem is not None`tests instead.
- `zipimport.zipimporter.load_module()`- `exec_module()`

## CPython Bytecode Changes[¶](#cpython-bytecode-changes)

- The oparg of - `YIELD_VALUE`- `1`if the yield is part of a yield-from or await, and- `0`otherwise. The oparg of- `RESUME`- [gh-111354](https://github.com/python/cpython/issues/111354).)

## C API Changes[¶](#c-api-changes)

### New Features[¶](#id7)

- Add the - [PyMonitoring C API](../c-api/monitoring.html#c-api-monitoring)for generating- **PEP 669**- (Contributed by Irit Katriel in - [gh-111997](https://github.com/python/cpython/issues/111997)).
- Add - `PyMutex`- `PyMutex_Lock()`- `PyMutex_Unlock()`- `PyMutex_Lock()`will release the- [GIL](../glossary.html#term-GIL)(if currently held) if the operation needs to block. (Contributed by Sam Gross in- [gh-108724](https://github.com/python/cpython/issues/108724).)
- Add the - [PyTime C API](../c-api/time.html#c-api-time)to provide access to system clocks:
- `PyTime_MIN`- `PyTime_MAX`
 - (Contributed by Victor Stinner and Petr Viktorin in - [gh-110850](https://github.com/python/cpython/issues/110850).)
- Add the - `PyDict_ContainsString()`- `PyDict_Contains()`- *key*is specified as a const char* UTF-8 encoded bytes string, rather than a- [PyObject](../c-api/structures.html#c.PyObject)*. (Contributed by Victor Stinner in- [gh-108314](https://github.com/python/cpython/issues/108314).)
- Add the - `PyDict_GetItemRef()`- `PyDict_GetItemStringRef()`- `PyDict_GetItemWithError()`- [strong reference](../glossary.html#term-strong-reference)instead of a- [borrowed reference](../glossary.html#term-borrowed-reference). Moreover, these functions return- `-1`on error, removing the need to check- `PyErr_Occurred()`. (Contributed by Victor Stinner in- [gh-106004](https://github.com/python/cpython/issues/106004).)
- Add the - `PyDict_SetDefaultRef()`- `PyDict_SetDefault()`- [strong reference](../glossary.html#term-strong-reference)instead of a- [borrowed reference](../glossary.html#term-borrowed-reference). This function returns- `-1`on error,- `0`on insertion, and- `1`if the key was already present in the dictionary. (Contributed by Sam Gross in- [gh-112066](https://github.com/python/cpython/issues/112066).)
- Add the - `PyDict_Pop()`- `PyDict_PopString()`- `dict.pop()`- `KeyError`- [gh-111262](https://github.com/python/cpython/issues/111262).)
- Add the - `PyMapping_GetOptionalItem()`- `PyMapping_GetOptionalItemString()`- `PyObject_GetItem()`- `PyMapping_GetItemString()`- `KeyError`- [gh-106307](https://github.com/python/cpython/issues/106307).)
- Add the - `PyObject_GetOptionalAttr()`- `PyObject_GetOptionalAttrString()`- `PyObject_GetAttr()`- `PyObject_GetAttrString()`- `AttributeError`- [gh-106521](https://github.com/python/cpython/issues/106521).)
- Add the - `PyErr_FormatUnraisable()`- `PyErr_WriteUnraisable()`- [gh-108082](https://github.com/python/cpython/issues/108082).)
- Add new functions that return a - [strong reference](../glossary.html#term-strong-reference)instead of a- [borrowed reference](../glossary.html#term-borrowed-reference)for frame locals, globals, and builtins, as part of- [PEP 667](#whatsnew313-locals-semantics):- (Contributed by Mark Shannon and Tian Gao in - [gh-74929](https://github.com/python/cpython/issues/74929).)
- Add the - `Py_GetConstant()`- `Py_GetConstantBorrowed()`- [strong](../glossary.html#term-strong-reference)or- [borrowed](../glossary.html#term-borrowed-reference)references to constants. For example,- `Py_GetConstant(Py_CONSTANT_ZERO)`returns a strong reference to the constant zero. (Contributed by Victor Stinner in- [gh-115754](https://github.com/python/cpython/issues/115754).)
- Add the - `PyImport_AddModuleRef()`- `PyImport_AddModule()`- [strong reference](../glossary.html#term-strong-reference)instead of a- [borrowed reference](../glossary.html#term-borrowed-reference). (Contributed by Victor Stinner in- [gh-105922](https://github.com/python/cpython/issues/105922).)
- Add the - `Py_IsFinalizing()`- [shutting down](../glossary.html#term-interpreter-shutdown). (Contributed by Victor Stinner in- [gh-108014](https://github.com/python/cpython/issues/108014).)
- Add the - `PyList_GetItemRef()`- `PyList_GetItem()`- [strong reference](../glossary.html#term-strong-reference)instead of a- [borrowed reference](../glossary.html#term-borrowed-reference). (Contributed by Sam Gross in- [gh-114329](https://github.com/python/cpython/issues/114329).)
- Add the - `PyList_Extend()`- `PyList_Clear()`- `list.extend()`- `list.clear()`- [gh-111138](https://github.com/python/cpython/issues/111138).)
- Add the - `PyLong_AsInt()`- `PyLong_AsLong()`- [gh-108014](https://github.com/python/cpython/issues/108014).)
- Add the - `PyLong_AsNativeBytes()`- `PyLong_FromNativeBytes()`- `PyLong_FromUnsignedNativeBytes()`- `int`- [gh-111140](https://github.com/python/cpython/issues/111140).)
- Add - `PyModule_Add()`- `PyModule_AddObjectRef()`- `PyModule_AddObject()`- [gh-86493](https://github.com/python/cpython/issues/86493).)
- Add the - `PyObject_GenericHash()`- [gh-113024](https://github.com/python/cpython/issues/113024).)
- Add the - `Py_HashPointer()`- [gh-111545](https://github.com/python/cpython/issues/111545).)
- Add the - `PyObject_VisitManagedDict()`- `PyObject_ClearManagedDict()`- `Py_TPFLAGS_MANAGED_DICT`- [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/)can be used to use these functions with Python 3.11 and 3.12. (Contributed by Victor Stinner in- [gh-107073](https://github.com/python/cpython/issues/107073).)
- Add the - `PyRefTracer_SetTracer()`- `PyRefTracer_GetTracer()`- `tracemalloc`- [gh-93502](https://github.com/python/cpython/issues/93502).)
- Add the - `PySys_AuditTuple()`- `PySys_Audit()`- `tuple`- [gh-85283](https://github.com/python/cpython/issues/85283).)
- Add the - `PyThreadState_GetUnchecked()`- `PyThreadState_Get()`- `NULL`. The caller is responsible for checking if the result is- `NULL`. (Contributed by Victor Stinner in- [gh-108867](https://github.com/python/cpython/issues/108867).)
- Add the - `PyType_GetFullyQualifiedName()`- `type.__module__`- `'builtins'`or- `'__main__'`. (Contributed by Victor Stinner in- [gh-111696](https://github.com/python/cpython/issues/111696).)
- Add the - `PyType_GetModuleName()`- `type.__module__`- [gh-111696](https://github.com/python/cpython/issues/111696).)
- Add the - `PyUnicode_EqualToUTF8AndSize()`- `PyUnicode_EqualToUTF8()`- `1`if they are equal or- `0`otherwise. These functions do not raise exceptions. (Contributed by Serhiy Storchaka in- [gh-110289](https://github.com/python/cpython/issues/110289).)
- Add the - `PyWeakref_GetRef()`- `PyWeakref_GetObject()`- [strong reference](../glossary.html#term-strong-reference)or- `NULL`if the referent is no longer live. (Contributed by Victor Stinner in- [gh-105927](https://github.com/python/cpython/issues/105927).)
- Add fixed variants of functions which silently ignore errors: 
- `PyObject_HasAttrStringWithError()`- `PyObject_HasAttrString()`
- `PyMapping_HasKeyStringWithError()`- `PyMapping_HasKeyString()`
 - The new functions return - `-1`for errors and the standard- `1`for true and- `0`for false.- (Contributed by Serhiy Storchaka in - [gh-108511](https://github.com/python/cpython/issues/108511).)

### Changed C APIs[¶](#changed-c-apis)

- The - *keywords*parameter of- `PyArg_ParseTupleAndKeywords()`- `PyArg_VaParseTupleAndKeywords()`- `PY_CXX_CONST`- [gh-65210](https://github.com/python/cpython/issues/65210).)
- `PyArg_ParseTupleAndKeywords()`- [gh-110815](https://github.com/python/cpython/issues/110815).)
- The - `PyCode_GetFirstFree()`function is now unstable API and is now named- `PyUnstable_Code_GetFirstFree()`- [gh-115781](https://github.com/python/cpython/issues/115781).)
- The - `PyDict_GetItem()`- `PyDict_GetItemString()`- `PyMapping_HasKey()`- `PyMapping_HasKeyString()`- `PyObject_HasAttr()`- `PyObject_HasAttrString()`- `PySys_GetObject()`- `sys.unraisablehook()`- [gh-106672](https://github.com/python/cpython/issues/106672).)
- Add support for the - `%T`,- `%#T`,- `%N`and- `%#N`formats to- `PyUnicode_FromFormat()`- `%T`: Get the fully qualified name of an object type
- `%#T`: As above, but use a colon as the separator
- `%N`: Get the fully qualified name of a type
- `%#N`: As above, but use a colon as the separator
 - See - **PEP 737**- [gh-111696](https://github.com/python/cpython/issues/111696).)
- You no longer have to define the - `PY_SSIZE_T_CLEAN`macro before including- `Python.h`when using- `#`formats in- [format codes](../c-api/arg.html#arg-parsing-string-and-buffers). APIs accepting the format codes always use- `Py_ssize_t`for- `#`formats. (Contributed by Inada Naoki in- [gh-104922](https://github.com/python/cpython/issues/104922).)
- If Python is built in - [debug mode](../using/configure.html#debug-build)or- `with assertions`- `PyTuple_SET_ITEM()`- `PyList_SET_ITEM()`- [gh-106168](https://github.com/python/cpython/issues/106168).)

### Limited C API Changes[¶](#limited-c-api-changes)

- The following functions are now included in the Limited C API: 
- Python built with - `--with-trace-refs`- [Limited API](../c-api/stable.html#limited-c-api). (Contributed by Victor Stinner in- [gh-108634](https://github.com/python/cpython/issues/108634).)

### Removed C APIs[¶](#removed-c-apis)

- Remove several functions, macros, variables, etc with names prefixed by - `_Py`or- `_PY`(which are considered private). If your project is affected by one of these removals and you believe that the removed API should remain available, please- [open a new issue](../bugs.html#using-the-tracker)to request a public C API and add- `cc: @vstinner`to the issue to notify Victor Stinner. (Contributed by Victor Stinner in- [gh-106320](https://github.com/python/cpython/issues/106320).)
- Remove old buffer protocols deprecated in Python 3.0. Use - [Buffer Protocol](../c-api/buffer.html#bufferobjects)instead.- `PyObject_CheckReadBuffer()`: Use- `PyObject_CheckBuffer()`- `PyObject_CheckBuffer()`doesn’t guarantee that- `PyObject_GetBuffer()`- `PyObject_GetBuffer()`.
- `PyObject_AsCharBuffer()`,- `PyObject_AsReadBuffer()`: Use- `PyObject_GetBuffer()`- `PyBuffer_Release()`- Py_buffer view; if (PyObject_GetBuffer(obj, &view, PyBUF_SIMPLE) < 0) { return NULL; } // Use `view.buf` and `view.len` to read from the buffer. // You may need to cast buf as `(const char*)view.buf`. PyBuffer_Release(&view); 
- `PyObject_AsWriteBuffer()`: Use- `PyObject_GetBuffer()`- `PyBuffer_Release()`- Py_buffer view; if (PyObject_GetBuffer(obj, &view, PyBUF_WRITABLE) < 0) { return NULL; } // Use `view.buf` and `view.len` to write to the buffer. PyBuffer_Release(&view); 
 - (Contributed by Inada Naoki in - [gh-85275](https://github.com/python/cpython/issues/85275).)
- Remove various functions deprecated in Python 3.9: - `PyEval_CallObject()`,- `PyEval_CallObjectWithKeywords()`: Use- `PyObject_CallNoArgs()`- `PyObject_Call()`- Warning - In - `PyObject_Call()`- `tuple`- `NULL`, and keyword arguments must be a- `dict`- `NULL`, whereas the removed functions checked argument types and accepted- `NULL`positional and keyword arguments. To replace- `PyEval_CallObjectWithKeywords(func, NULL, kwargs)`with- `PyObject_Call()`, pass an empty tuple as positional arguments using- `PyTuple_New(0)`
- `PyEval_CallFunction()`: Use- `PyObject_CallFunction()`
- `PyEval_CallMethod()`: Use- `PyObject_CallMethod()`
- `PyCFunction_Call()`: Use- `PyObject_Call()`
 - (Contributed by Victor Stinner in - [gh-105107](https://github.com/python/cpython/issues/105107).)
- Remove the following old functions to configure the Python initialization, deprecated in Python 3.11: - `PySys_AddWarnOptionUnicode()`: Use- `PyConfig.warnoptions`
- `PySys_AddWarnOption()`: Use- `PyConfig.warnoptions`
- `PySys_AddXOption()`: Use- `PyConfig.xoptions`
- `PySys_HasWarnOptions()`: Use- `PyConfig.xoptions`
- `PySys_SetPath()`: Set- `PyConfig.module_search_paths`
- `Py_SetPath()`: Set- `PyConfig.module_search_paths`
- `Py_SetStandardStreamEncoding()`: Set- `PyConfig.stdio_encoding`- `PyConfig.legacy_windows_stdio`
- `_Py_SetProgramFullPath()`: Set- `PyConfig.executable`
 - Use the new - `PyConfig`- [Python Initialization Configuration](../c-api/init_config.html#init-config)instead (- **PEP 587**- [gh-105145](https://github.com/python/cpython/issues/105145).)
- Remove - `PyEval_AcquireLock()`and- `PyEval_ReleaseLock()`functions, deprecated in Python 3.2. They didn’t update the current thread state. They can be replaced with:
- low-level - `PyEval_AcquireThread()`- `PyEval_RestoreThread()`
 - (Contributed by Victor Stinner in - [gh-105182](https://github.com/python/cpython/issues/105182).)
- Remove the - `PyEval_ThreadsInitialized()`function, deprecated in Python 3.9. Since Python 3.7,- `Py_Initialize()`always creates the GIL: calling- `PyEval_InitThreads()`does nothing and- `PyEval_ThreadsInitialized()`always returns non-zero. (Contributed by Victor Stinner in- [gh-105182](https://github.com/python/cpython/issues/105182).)
- Remove the - `_PyInterpreterState_Get()`alias to- `PyInterpreterState_Get()`- [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/)can be used to get- `PyInterpreterState_Get()`on Python 3.8 and older. (Contributed by Victor Stinner in- [gh-106320](https://github.com/python/cpython/issues/106320).)
- Remove the private - `_PyObject_FastCall()`function: use- `PyObject_Vectorcall()`which is available since Python 3.8 (- **PEP 590**- [gh-106023](https://github.com/python/cpython/issues/106023).)
- Remove the - `cpython/pytime.h`header file, which only contained private functions. (Contributed by Victor Stinner in- [gh-106316](https://github.com/python/cpython/issues/106316).)
- Remove the undocumented - `PY_TIMEOUT_MAX`constant from the limited C API. (Contributed by Victor Stinner in- [gh-110014](https://github.com/python/cpython/issues/110014).)
- Remove the old trashcan macros - `Py_TRASHCAN_SAFE_BEGIN`and- `Py_TRASHCAN_SAFE_END`. Replace both with the new macros- `Py_TRASHCAN_BEGIN`and- `Py_TRASHCAN_END`. (Contributed by Irit Katriel in- [gh-105111](https://github.com/python/cpython/issues/105111).)

### Deprecated C APIs[¶](#deprecated-c-apis)

- Deprecate old Python initialization functions: - `PySys_ResetWarnOptions()`- `sys.warnoptions`- `warnings.filters`instead.
- `Py_GetExecPrefix()`- `sys.exec_prefix`
- `Py_GetPath()`- `sys.path`
- `Py_GetPrefix()`- `sys.prefix`
- `Py_GetProgramFullPath()`- `sys.executable`
- `Py_GetProgramName()`- `sys.executable`
- `Py_GetPythonHome()`- `PyConfig.home`- `PYTHONHOME`
 - (Contributed by Victor Stinner in - [gh-105145](https://github.com/python/cpython/issues/105145).)
- [Soft deprecate](../glossary.html#term-soft-deprecated)the- `PyEval_GetBuiltins()`- `PyEval_GetGlobals()`- `PyEval_GetLocals()`- [borrowed reference](../glossary.html#term-borrowed-reference). (Soft deprecated as part of- **PEP 667**
- Deprecate the - `PyImport_ImportModuleNoBlock()`- `PyImport_ImportModule()`- [gh-105396](https://github.com/python/cpython/issues/105396).)
- [Soft deprecate](../glossary.html#term-soft-deprecated)the- `PyModule_AddObject()`- `PyModule_Add()`- `PyModule_AddObjectRef()`- [gh-86493](https://github.com/python/cpython/issues/86493).)
- Deprecate the old - `Py_UNICODE`and- `PY_UNICODE_TYPE`types and the- `Py_UNICODE_WIDE`define. Use the- `wchar_t`type directly instead. Since Python 3.3,- `Py_UNICODE`and- `PY_UNICODE_TYPE`are just aliases to- `wchar_t`. (Contributed by Victor Stinner in- [gh-105156](https://github.com/python/cpython/issues/105156).)
- Deprecate the - `PyWeakref_GetObject()`- `PyWeakref_GET_OBJECT()`- [borrowed reference](../glossary.html#term-borrowed-reference). Replace them with the new- `PyWeakref_GetRef()`- [strong reference](../glossary.html#term-strong-reference). The- [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/)can be used to get- `PyWeakref_GetRef()`on Python 3.12 and older. (Contributed by Victor Stinner in- [gh-105927](https://github.com/python/cpython/issues/105927).)

#### Pending Removal in Python 3.14[¶](#id8)

- The - `ma_version_tag`field in- `PyDictObject`- **PEP 699**- [gh-101193](https://github.com/python/cpython/issues/101193)).
- Creating - `immutable types`- [gh-95388](https://github.com/python/cpython/issues/95388)).
- Functions to configure Python’s initialization, deprecated in Python 3.11: - `PySys_SetArgvEx()`: Set- `PyConfig.argv`
- `PySys_SetArgv()`: Set- `PyConfig.argv`
- `Py_SetProgramName()`: Set- `PyConfig.program_name`
- `Py_SetPythonHome()`: Set- `PyConfig.home`
 - The - `Py_InitializeFromConfig()`- `PyConfig`
- Global configuration variables: - `Py_DebugFlag`- `PyConfig.parser_debug`
- `Py_VerboseFlag`- `PyConfig.verbose`
- `Py_QuietFlag`- `PyConfig.quiet`
- `Py_InteractiveFlag`- `PyConfig.interactive`
- `Py_InspectFlag`- `PyConfig.inspect`
- `Py_OptimizeFlag`- `PyConfig.optimization_level`
- `Py_NoSiteFlag`- `PyConfig.site_import`
- `Py_BytesWarningFlag`- `PyConfig.bytes_warning`
- `Py_FrozenFlag`- `PyConfig.pathconfig_warnings`
- `Py_IgnoreEnvironmentFlag`- `PyConfig.use_environment`
- `Py_DontWriteBytecodeFlag`- `PyConfig.write_bytecode`
- `Py_NoUserSiteDirectory`- `PyConfig.user_site_directory`
- `Py_UnbufferedStdioFlag`- `PyConfig.buffered_stdio`
- `Py_HashRandomizationFlag`- `PyConfig.use_hash_seed`- `PyConfig.hash_seed`
- `Py_IsolatedFlag`- `PyConfig.isolated`
- `Py_LegacyWindowsFSEncodingFlag`- `PyPreConfig.legacy_windows_fs_encoding`
- `Py_LegacyWindowsStdioFlag`- `PyConfig.legacy_windows_stdio`
- `Py_FileSystemDefaultEncoding`: Use- `PyConfig.filesystem_encoding`
- `Py_HasFileSystemDefaultEncoding`: Use- `PyConfig.filesystem_encoding`
- `Py_FileSystemDefaultEncodeErrors`: Use- `PyConfig.filesystem_errors`
- `Py_UTF8Mode`: Use- `PyPreConfig.utf8_mode`- `Py_PreInitialize()`
 - The - `Py_InitializeFromConfig()`- `PyConfig`

#### Pending Removal in Python 3.15[¶](#id9)

- The - `PyImport_ImportModuleNoBlock()`- `PyImport_ImportModule()`
- `PyWeakref_GetObject()`- `PyWeakref_GET_OBJECT()`- `PyWeakref_GetRef()`
- `Py_UNICODE`- `Py_UNICODE_WIDE`macro: Use- `wchar_t`instead.
- Python initialization functions: - `PySys_ResetWarnOptions()`- `sys.warnoptions`- `warnings.filters`instead.
- `Py_GetExecPrefix()`- `sys.base_exec_prefix`- `sys.exec_prefix`
- `Py_GetPath()`- `sys.path`
- `Py_GetPrefix()`- `sys.base_prefix`- `sys.prefix`
- `Py_GetProgramFullPath()`- `sys.executable`
- `Py_GetProgramName()`- `sys.executable`
- `Py_GetPythonHome()`- `PyConfig.home`- `PYTHONHOME`
 

#### Pending removal in Python 3.16[¶](#id10)

- The bundled copy of - `libmpdec`.

#### Pending Removal in Future Versions[¶](#id11)

The following APIs are deprecated and will be removed, although there is currently no date scheduled for their removal.

- `Py_TPFLAGS_HAVE_FINALIZE`
- `PyErr_Fetch()`- `PyErr_GetRaisedException()`
- `PyErr_NormalizeException()`- `PyErr_GetRaisedException()`
- `PyErr_Restore()`- `PyErr_SetRaisedException()`
- `PyModule_GetFilename()`- `PyModule_GetFilenameObject()`
- `PyOS_AfterFork()`- `PyOS_AfterFork_Child()`
- `PySlice_GetIndicesEx()`- `PySlice_Unpack()`- `PySlice_AdjustIndices()`
- `PyUnicode_AsDecodedObject()`: Use- `PyCodec_Decode()`
- `PyUnicode_AsDecodedUnicode()`: Use- `PyCodec_Decode()`
- `PyUnicode_AsEncodedObject()`: Use- `PyCodec_Encode()`
- `PyUnicode_AsEncodedUnicode()`: Use- `PyCodec_Encode()`
- `PyUnicode_READY()`
- `PyErr_Display()`: Use- `PyErr_DisplayException()`
- `_PyErr_ChainExceptions()`: Use- `_PyErr_ChainExceptions1()`instead.
- `PyBytesObject.ob_shash`member: call- `PyObject_Hash()`
- `PyDictObject.ma_version_tag`member.
- Thread Local Storage (TLS) API: - `PyThread_create_key()`- `PyThread_tss_alloc()`
- `PyThread_delete_key()`- `PyThread_tss_free()`
- `PyThread_set_key_value()`- `PyThread_tss_set()`
- `PyThread_get_key_value()`- `PyThread_tss_get()`
- `PyThread_delete_key_value()`- `PyThread_tss_delete()`
- `PyThread_ReInitTLS()`
 

## Build Changes[¶](#build-changes)

- `arm64-apple-ios`and- `arm64-apple-ios-simulator`are both now- **PEP 11**- [PEP 730](#whatsnew313-platform-support)written and implementation contributed by Russell Keith-Magee in- [gh-114099](https://github.com/python/cpython/issues/114099).)
- `aarch64-linux-android`and- `x86_64-linux-android`are both now- **PEP 11**- [PEP 738](#whatsnew313-platform-support)written and implementation contributed by Malcolm Smith in- [gh-116622](https://github.com/python/cpython/issues/116622).)
- `wasm32-wasi`is now a- **PEP 11**- [gh-115192](https://github.com/python/cpython/issues/115192).)
- `wasm32-emscripten`is no longer a- **PEP 11**- [gh-115192](https://github.com/python/cpython/issues/115192).)
- Building CPython now requires a compiler with support for the C11 atomic library, GCC built-in atomic functions, or MSVC interlocked intrinsics. 
- Autoconf 2.71 and aclocal 1.16.5 are now required to regenerate the - `configure`script. (Contributed by Christian Heimes in- [gh-89886](https://github.com/python/cpython/issues/89886)and by Victor Stinner in- [gh-112090](https://github.com/python/cpython/issues/112090).)
- SQLite 3.15.2 or newer is required to build the - `sqlite3`- [gh-105875](https://github.com/python/cpython/issues/105875).)
- CPython now bundles the - [mimalloc library](https://github.com/microsoft/mimalloc/)by default. It is licensed under the MIT license; see- [mimalloc license](../license.html#mimalloc-license). The bundled mimalloc has custom changes, see- [gh-113141](https://github.com/python/cpython/issues/113141)for details. (Contributed by Dino Viehland in- [gh-109914](https://github.com/python/cpython/issues/109914).)
- The - `configure`option- `--with-system-libmpdec`- `yes`. The bundled copy of- `libmpdec`will be removed in Python 3.16.
- Python built with - `configure`- `--with-trace-refs`- [debug build](../using/configure.html#debug-build). (Contributed by Victor Stinner in- [gh-108634](https://github.com/python/cpython/issues/108634).)
- On POSIX systems, the pkg-config ( - `.pc`) filenames now include the ABI flags. For example, the free-threaded build generates- `python-3.13t.pc`and the debug build generates- `python-3.13d.pc`.
- The - `errno`,- `fcntl`,- `grp`,- `md5`,- `pwd`,- `resource`,- `termios`,- `winsound`,- `_ctypes_test`,- `_multiprocessing.posixshmem`,- `_scproxy`,- `_stat`,- `_statistics`,- `_testconsole`,- `_testimportmultiple`and- `_uuid`C extensions are now built with the- [limited C API](../c-api/stable.html#limited-c-api). (Contributed by Victor Stinner in- [gh-85283](https://github.com/python/cpython/issues/85283).)

## Porting to Python 3.13[¶](#porting-to-python-3-13)

This section lists previously described changes and other bugfixes that may require changes to your code.

### Changes in the Python API[¶](#changes-in-the-python-api)

- [PEP 667](#whatsnew313-locals-semantics)introduces several changes to the semantics of- `locals()`- `f_locals`- Calling - `locals()`- [optimized scope](../glossary.html#term-optimized-scope)now produces an independent snapshot on each call, and hence no longer implicitly updates previously returned references. Obtaining the legacy CPython behavior now requires explicit calls to update the initially returned dictionary with the results of subsequent calls to- `locals()`. Code execution functions that implicitly target- `locals()`(such as- `exec`and- `eval`) must be passed an explicit namespace to access their results in an optimized scope. (Changed as part of- **PEP 667**
- Calling - `locals()`- `exec`or- `eval`) once more behaves as if the comprehension were running as an independent nested function (i.e. the local variables from the containing scope are not included). In Python 3.12, this had changed to include the local variables from the containing scope when implementing- **PEP 709**- **PEP 667**
- Accessing - `FrameType.f_locals`- [optimized scope](../glossary.html#term-optimized-scope)now returns a write-through proxy rather than a snapshot that gets updated at ill-specified times. If a snapshot is desired, it must be created explicitly with- `dict`or the proxy’s- `.copy()`method. (Changed as part of- **PEP 667**
 
- `functools.partial`- `FutureWarning`- `staticmethod()`- [gh-121027](https://github.com/python/cpython/issues/121027).)
- An - `OSError`- `getpass.getuser()`- `ImportError`- `KeyError`
- The value of the - `mode`attribute of- `gzip.GzipFile`- `'rb'`or- `'wb'`) instead of an integer (- `1`or- `2`). The value of the- `mode`attribute of the readable file-like object returned by- `zipfile.ZipFile.open()`- `'rb'`instead of- `'r'`. (Contributed by Serhiy Storchaka in- [gh-115961](https://github.com/python/cpython/issues/115961).)
- `mailbox.Maildir`- `.`). (Contributed by Zackery Spytz in- [gh-65559](https://github.com/python/cpython/issues/65559).)
- `pathlib.Path.glob()`- `rglob()`- `**`” is given, rather than directories only. Add a trailing slash to keep the previous behavior and only match directories.
- The - `threading`- `_thread`module to have an- `_is_main_interpreter()`function. This function takes no arguments and returns- `True`if the current interpreter is the main interpreter.- Any library or application that provides a custom - `_thread`module must provide- `_is_main_interpreter()`, just like the module’s other “private” attributes. (- [gh-112826](https://github.com/python/cpython/issues/112826).)

### Changes in the C API[¶](#changes-in-the-c-api)

- `Python.h`no longer includes the- `<ieeefp.h>`standard header. It was included for the- `finite()`function which is now provided by the- `<math.h>`header. It should now be included explicitly if needed. Remove also the- `HAVE_IEEEFP_H`macro. (Contributed by Victor Stinner in- [gh-108765](https://github.com/python/cpython/issues/108765).)
- `Python.h`no longer includes these standard header files:- `<time.h>`,- `<sys/select.h>`and- `<sys/time.h>`. If needed, they should now be included explicitly. For example,- `<time.h>`provides the- `clock()`and- `gmtime()`functions,- `<sys/select.h>`provides the- `select()`function, and- `<sys/time.h>`provides the- `futimes()`,- `gettimeofday()`and- `setitimer()`functions. (Contributed by Victor Stinner in- [gh-108765](https://github.com/python/cpython/issues/108765).)
- On Windows, - `Python.h`no longer includes the- `<stddef.h>`standard header file. If needed, it should now be included explicitly. For example, it provides- `offsetof()`function, and- `size_t`and- `ptrdiff_t`types. Including- `<stddef.h>`explicitly was already needed by all other platforms, the- `HAVE_STDDEF_H`macro is only defined on Windows. (Contributed by Victor Stinner in- [gh-108765](https://github.com/python/cpython/issues/108765).)
- If the - `Py_LIMITED_API`- `Py_BUILD_CORE`,- `Py_BUILD_CORE_BUILTIN`and- `Py_BUILD_CORE_MODULE`macros are now undefined by- `<Python.h>`. (Contributed by Victor Stinner in- [gh-85283](https://github.com/python/cpython/issues/85283).)
- The old trashcan macros - `Py_TRASHCAN_SAFE_BEGIN`and- `Py_TRASHCAN_SAFE_END`were removed. They should be replaced by the new macros- `Py_TRASHCAN_BEGIN`and- `Py_TRASHCAN_END`.- A - `tp_dealloc`function that has the old macros, such as:- static void mytype_dealloc(mytype *p) { PyObject_GC_UnTrack(p); Py_TRASHCAN_SAFE_BEGIN(p); ... Py_TRASHCAN_SAFE_END } - should migrate to the new macros as follows: - static void mytype_dealloc(mytype *p) { PyObject_GC_UnTrack(p); Py_TRASHCAN_BEGIN(p, mytype_dealloc) ... Py_TRASHCAN_END } - Note that - `Py_TRASHCAN_BEGIN`has a second argument which should be the deallocation function it is in. The new macros were added in Python 3.8 and the old macros were deprecated in Python 3.11. (Contributed by Irit Katriel in- [gh-105111](https://github.com/python/cpython/issues/105111).)

- [PEP 667](#whatsnew313-locals-semantics)introduces several changes to frame-related functions:- The effects of mutating the dictionary returned from - `PyEval_GetLocals()`- [optimized scope](../glossary.html#term-optimized-scope)have changed. New dict entries added this way will now- *only*be visible to subsequent- `PyEval_GetLocals()`calls in that frame, as- `PyFrame_GetLocals()`- `locals()`- `FrameType.f_locals`- `PyEval_GetLocals()`in that frame. The recommended code update depends on how the function was being used, so refer to the deprecation notice on the function for details.
- Calling - `PyFrame_GetLocals()`- [optimized scope](../glossary.html#term-optimized-scope)now returns a write-through proxy rather than a snapshot that gets updated at ill-specified times. If a snapshot is desired, it must be created explicitly (e.g. with- `PyDict_Copy()`- `PyEval_GetFrameLocals()`
- `PyFrame_FastToLocals()`and- `PyFrame_FastToLocalsWithError()`no longer have any effect. Calling these functions has been redundant since Python 3.11, when- `PyFrame_GetLocals()`
- `PyFrame_LocalsToFast()`no longer has any effect. Calling this function is redundant now that- `PyFrame_GetLocals()`- [optimized scopes](../glossary.html#term-optimized-scope).
 
- Python 3.13 removed many private functions. Some of them can be replaced using these alternatives: - `_PyDict_Pop()`:- `PyDict_Pop()`- `PyDict_PopString()`
- `_PyDict_GetItemWithError()`:- `PyDict_GetItemRef()`
- `_PyErr_WriteUnraisableMsg()`:- `PyErr_FormatUnraisable()`
- `_PyEval_SetTrace()`:- `PyEval_SetTrace()`- `PyEval_SetTraceAllThreads()`
- `_PyList_Extend()`:- `PyList_Extend()`
- `_PyLong_AsInt()`:- `PyLong_AsInt()`
- `_PyMem_RawStrdup()`:- `strdup()`;
- `_PyMem_Strdup()`:- `strdup()`;
- `_PyObject_ClearManagedDict()`:- `PyObject_ClearManagedDict()`
- `_PyObject_VisitManagedDict()`:- `PyObject_VisitManagedDict()`
- `_PyThreadState_UncheckedGet()`:- `PyThreadState_GetUnchecked()`
- `_PyTime_AsSecondsDouble()`:- `PyTime_AsSecondsDouble()`
- `_PyTime_GetMonotonicClock()`:- `PyTime_Monotonic()`- `PyTime_MonotonicRaw()`
- `_PyTime_GetPerfCounter()`:- `PyTime_PerfCounter()`- `PyTime_PerfCounterRaw()`
- `_PyTime_GetSystemClock()`:- `PyTime_Time()`- `PyTime_TimeRaw()`
- `_PyTime_MAX`:- `PyTime_MAX`
- `_PyTime_MIN`:- `PyTime_MIN`
- `_PyTime_t`:- `PyTime_t`
- `_Py_HashPointer()`:- `Py_HashPointer()`
- `_Py_IsFinalizing()`:- `Py_IsFinalizing()`
 - The - [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/)can be used to get most of these new functions on Python 3.12 and older.

## Regression Test Changes[¶](#regression-test-changes)

- Python built with - `configure`- `--with-pydebug`- `-X presite=package.module`- `site.py`is executed. (Contributed by Łukasz Langa in- [gh-110769](https://github.com/python/cpython/issues/110769).)

## Notable changes in 3.13.1[¶](#notable-changes-in-3-13-1)

### sys[¶](#id12)

- The previously undocumented special function - `sys.getobjects()`

## Notable changes in 3.13.4[¶](#notable-changes-in-3-13-4)

### os.path[¶](#id13)

- The - *strict*parameter to- `os.path.realpath()`- `os.path.ALLOW_MISSING`- `FileNotFoundError`- **CVE 2025-4517**

### tarfile[¶](#tarfile)

- `data_filter()`- [gh-127987](https://github.com/python/cpython/issues/127987)and- **CVE 2025-4138**
- `extractall()`- [gh-127987](https://github.com/python/cpython/issues/127987)and- **CVE 2024-12718**
- `extract()`- `extractall()`- `LinkFallbackError`- **CVE 2025-4330**- **CVE 2024-12718**
- `extract()`- `extractall()`- `errorlevel()`- [gh-112887](https://github.com/python/cpython/issues/112887)and- **CVE 2025-4435**