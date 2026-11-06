# What’s new in Python 3.14 — Python 3.14.6 documentation

**Source:** [https://docs.python.org/3/whatsnew/3.14.html](https://docs.python.org/3/whatsnew/3.14.html)

---

# What’s new in Python 3.14[¶](#what-s-new-in-python-3-14)

- Editors:
- Adam Turner and Hugo van Kemenade 

This article explains the new features in Python 3.14, compared to 3.13.
Python 3.14 was released on 7 October 2025.
For full details, see the [changelog](changelog.html#changelog).

See also

[ PEP 745](https://peps.python.org/pep-0745/) – Python 3.14 release schedule

## Summary – Release highlights[¶](#summary-release-highlights)

Python 3.14 is the latest stable release of the Python programming
language, with a mix of changes to the language, the implementation,
and the standard library.
The biggest changes include [template string literals](#whatsnew314-template-string-literals),
[deferred evaluation of annotations](#whatsnew314-deferred-annotations),
and support for [subinterpreters](#whatsnew314-multiple-interpreters) in
the standard library.

The library changes include significantly improved capabilities for
[introspection in asyncio](#whatsnew314-asyncio-introspection),
[support for Zstandard](#whatsnew314-zstandard) via a new
[ compression.zstd](../library/compression.zstd.html#module-compression.zstd) module, syntax highlighting in the REPL,
as well as the usual deprecations and removals,
and improvements in user-friendliness and correctness.

This article doesn’t attempt to provide a complete specification
of all new features, but instead gives a convenient overview.
For full details refer to the documentation,
such as the [Library Reference](../library/index.html#library-index)
and [Language Reference](../reference/index.html#reference-index).
To understand the complete implementation and design rationale for a change,
refer to the PEP for a particular new feature;
but note that PEPs usually are not kept up-to-date
once a feature has been fully implemented.
See [Porting to Python 3.14](#porting-to-python-3-14) for guidance on upgrading from
earlier versions of Python.

Interpreter improvements:

Significant improvements in the standard library:

- [Syntax highlighting in the default interactive shell](#whatsnew314-pyrepl-highlighting), and color output in several standard library CLIs

C API improvements:

Platform support:

- **PEP 776**- [officially supported platform](#whatsnew314-build-changes), at- **tier 3**

Release changes:

## New features[¶](#new-features)

**PEP 649****PEP 749**[¶](#pep-649-pep-749-deferred-evaluation-of-annotations)

**PEP 649**

**PEP 749**

The [annotations](../glossary.html#term-annotation) on functions, classes, and modules are no
longer evaluated eagerly. Instead, annotations are stored in special-purpose
[annotate functions](../glossary.html#term-annotate-function) and evaluated only when
necessary (except if `from __future__ import annotations` is used).

This change is designed to improve performance and usability of annotations in Python in most circumstances. The runtime cost for defining annotations is minimized, but it remains possible to introspect annotations at runtime. It is no longer necessary to enclose annotations in strings if they contain forward references.

The new [ annotationlib](../library/annotationlib.html#module-annotationlib) module provides tools for inspecting deferred
annotations. Annotations may be evaluated in the 

[format (which evaluates annotations to runtime values, similar to the behavior in earlier Python versions), the](../library/annotationlib.html#annotationlib.Format.VALUE)

`VALUE`[format (which replaces undefined names with special markers), and the](../library/annotationlib.html#annotationlib.Format.FORWARDREF)

`FORWARDREF`[format (which returns annotations as strings).](../library/annotationlib.html#annotationlib.Format.STRING)

`STRING`This example shows how these formats behave:

```
>>> from annotationlib import get_annotations, Format
>>> def func(arg: Undefined):
...     pass
>>> get_annotations(func, format=Format.VALUE)
Traceback (most recent call last):
  ...
NameError: name 'Undefined' is not defined
>>> get_annotations(func, format=Format.FORWARDREF)
{'arg': ForwardRef('Undefined', owner=<function func at 0x...>)}
>>> get_annotations(func, format=Format.STRING)
{'arg': 'Undefined'}
```
The [porting](#whatsnew314-porting-annotations) section contains guidance
on changes that may be needed due to these changes, though in the majority of
cases, code will continue working as-is.

(Contributed by Jelle Zijlstra in [ PEP 749](https://peps.python.org/pep-0749/) and 

[gh-119180](https://github.com/python/cpython/issues/119180);

[was written by Larry Hastings.)](https://peps.python.org/pep-0649/)

**PEP 649****PEP 734**[¶](#pep-734-multiple-interpreters-in-the-standard-library)

**PEP 734**

The CPython runtime supports running multiple copies of Python in the
same process simultaneously and has done so for over 20 years.
Each of these separate copies is called an ‘interpreter’.
However, the feature had been available only through
the [C-API](../c-api/subinterpreters.html#sub-interpreter-support).

That limitation is removed in Python 3.14,
with the new [ concurrent.interpreters](../library/concurrent.interpreters.html#module-concurrent.interpreters) module.

There are at least two notable reasons why using multiple interpreters has significant benefits:

- they support a new (to Python), human-friendly concurrency model 
- true multi-core parallelism 

For some use cases, concurrency in software improves efficiency and
can simplify design, at a high level.
At the same time, implementing and maintaining all but the simplest concurrency
is often a struggle for the human brain.
That especially applies to plain threads (for example, [ threading](../library/threading.html#module-threading)),
where all memory is shared between all threads.

With multiple isolated interpreters, you can take advantage of a class of concurrency models, like Communicating Sequential Processes (CSP) or the actor model, that have found success in other programming languages, like Smalltalk, Erlang, Haskell, and Go. Think of multiple interpreters as threads but with opt-in sharing.

Regarding multi-core parallelism: as of Python 3.12, interpreters
are now sufficiently isolated from one another to be used in parallel
(see [ PEP 684](https://peps.python.org/pep-0684/)). This unlocks a variety of CPU-intensive use cases
for Python that were limited by the 

[GIL](../glossary.html#term-GIL).

Using multiple interpreters is similar in many ways to
[ multiprocessing](../library/multiprocessing.html#module-multiprocessing), in that they both provide isolated logical
“processes” that can run in parallel, with no sharing by default.
However, when using multiple interpreters, an application will use
fewer system resources and will operate more efficiently (since it
stays within the same process). Think of multiple interpreters as
having the isolation of processes with the efficiency of threads.

While the feature has been around for decades, multiple interpreters have not been used widely, due to low awareness and the lack of a standard library module. Consequently, they currently have several notable limitations, which are expected to improve significantly now that the feature is going mainstream.

Current limitations:

- starting each interpreter has not been optimized yet 
- each interpreter uses more memory than necessary (work continues on extensive internal sharing between interpreters) 
- there aren’t many options - *yet*for truly sharing objects or other data between interpreters (other than- `memoryview`
- many third-party extension modules on PyPI are not yet compatible with multiple interpreters (all standard library extension modules - *are*compatible)
- the approach to writing applications that use multiple isolated interpreters is mostly unfamiliar to Python users, for now 

The impact of these limitations will depend on future CPython improvements, how interpreters are used, and what the community solves through PyPI packages. Depending on the use case, the limitations may not have much impact, so try it out!

Furthermore, future CPython releases will reduce or eliminate overhead
and provide utilities that are less appropriate on PyPI. In the
meantime, most of the limitations can also be addressed through
extension modules, meaning PyPI packages can fill any gap for 3.14, and
even back to 3.12 where interpreters were finally properly isolated and
stopped sharing the [GIL](../glossary.html#term-GIL). Likewise, libraries on PyPI are expected
to emerge for high-level abstractions on top of interpreters.

Regarding extension modules, work is in progress to update some PyPI
projects, as well as tools like Cython, pybind11, nanobind, and PyO3.
The steps for isolating an extension module are found at
[Isolating Extension Modules](../howto/isolating-extensions.html#isolating-extensions-howto).
Isolating a module has a lot of overlap with what is required to support
[free-threading](#whatsnew314-free-threaded-cpython), so the ongoing
work in the community in that area will help accelerate support
for multiple interpreters.

Also added in 3.14: [concurrent.futures.InterpreterPoolExecutor](#whatsnew314-concurrent-futures-interp-pool).

(Contributed by Eric Snow in [gh-134939](https://github.com/python/cpython/issues/134939).)

See also

**PEP 750**[¶](#pep-750-template-string-literals)

**PEP 750**

Template strings are a new mechanism for custom string processing.
They share the familiar syntax of f-strings but, unlike f-strings,
return an object representing the static and interpolated parts of
the string, instead of a simple [ str](../library/stdtypes.html#str).

To write a t-string, use a `'t'` prefix instead of an `'f'`:

```
>>> variety = 'Stilton'
>>> template = t'Try some {variety} cheese!'
>>> type(template)
<class 'string.templatelib.Template'>
```
[ Template](../library/string.templatelib.html#string.templatelib.Template) objects provide access to the static
and interpolated (in curly braces) parts of a string 

*before*they are combined. Iterate over

`Template` instances to access their parts in order:```
>>> list(template)
['Try some ', Interpolation('Stilton', 'variety', None, ''), ' cheese!']
```
It’s easy to write (or call) code to process `Template` instances.
For example, here’s a function that renders static parts lowercase and
[ Interpolation](../library/string.templatelib.html#string.templatelib.Interpolation) instances uppercase:

```
from string.templatelib import Interpolation
def lower_upper(template):
    """Render static parts lowercase and interpolations uppercase."""
    parts = []
    for part in template:
        if isinstance(part, Interpolation):
            parts.append(str(part.value).upper())
        else:
            parts.append(part.lower())
    return ''.join(parts)
name = 'Wenslydale'
template = t'Mister {name}'
assert lower_upper(template) == 'mister WENSLYDALE'
```
Because `Template` instances distinguish between static strings and
interpolations at runtime, they can be useful for sanitising user input.
Writing a `html()` function that escapes user input in HTML is an exercise
left to the reader!
Template processing code can provide improved flexibility.
For instance, a more advanced `html()` function could accept
a `dict` of HTML attributes directly in the template:

```
attributes = {'src': 'limburger.jpg', 'alt': 'lovely cheese'}
template = t'<img {attributes}>'
assert html(template) == '<img src="limburger.jpg" alt="lovely cheese" />'
```
Of course, template processing code does not need to return a string-like result.
An even *more* advanced `html()` could return a custom type representing
a DOM-like structure.

With t-strings in place, developers can write systems that sanitise SQL, make safe shell operations, improve logging, tackle modern ideas in web development (HTML, CSS, and so on), and implement lightweight custom business DSLs.

(Contributed by Jim Baker, Guido van Rossum, Paul Everitt, Koudai Aono,
Lysandros Nikolaou, Dave Peck, Adam Turner, Jelle Zijlstra, Bénédikt Tran,
and Pablo Galindo Salgado in [gh-132661](https://github.com/python/cpython/issues/132661).)

See also

**PEP 768**[¶](#pep-768-safe-external-debugger-interface)

**PEP 768**

Python 3.14 introduces a zero-overhead debugging interface that allows debuggers and profilers to safely attach to running Python processes without stopping or restarting them. This is a significant enhancement to Python’s debugging capabilities, meaning that unsafe alternatives are no longer required.

The new interface provides safe execution points for attaching debugger code without modifying the interpreter’s normal execution path or adding any overhead at runtime. Due to this, tools can now inspect and interact with Python applications in real-time, which is a crucial capability for high-availability systems and production environments.

For convenience, this interface is implemented in the [ sys.remote_exec()](../library/sys.html#sys.remote_exec)
function. For example:

```
import sys
from tempfile import NamedTemporaryFile
with NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
    script_path = f.name
    f.write(f'import my_debugger; my_debugger.connect({os.getpid()})')
# Execute in process with PID 1234
print('Behold! An offering:')
sys.remote_exec(1234, script_path)
```
This function allows sending Python code to be executed in a target process at the next safe execution point. However, tool authors can also implement the protocol directly as described in the PEP, which details the underlying mechanisms used to safely attach to running processes.

The debugging interface has been carefully designed with security in mind and includes several mechanisms to control access:

- A - `PYTHON_DISABLE_REMOTE_DEBUG`
- A - `-X disable-remote-debug`
- A - `--without-remote-debug`

(Contributed by Pablo Galindo Salgado, Matt Wozniski, and Ivona Stojanovic
in [gh-131591](https://github.com/python/cpython/issues/131591).)

See also

### A new type of interpreter[¶](#a-new-type-of-interpreter)

A new type of interpreter has been added to CPython.
It uses tail calls between small C functions that implement individual
Python opcodes, rather than one large C `case` statement.
For certain newer compilers, this interpreter provides
significantly better performance. Preliminary benchmarks suggest a geometric
mean of 3-5% faster on the standard `pyperformance` benchmark suite,
depending on platform and architecture.
The baseline is Python 3.14 built with Clang 19, without this new interpreter.

This interpreter currently only works with Clang 19 and newer on x86-64 and AArch64 architectures. However, a future release of GCC is expected to support this as well.

This feature is opt-in for now. Enabling profile-guided optimization is highly
recommended when using the new interpreter as it is the only configuration
that has been tested and validated for improved performance.
For further information, see [ --with-tail-call-interp](../using/configure.html#cmdoption-with-tail-call-interp).

Note

This is not to be confused with [tail call optimization](https://en.wikipedia.org/wiki/Tail_call) of Python
functions, which is currently not implemented in CPython.

This new interpreter type is an internal implementation detail of the CPython interpreter. It doesn’t change the visible behavior of Python programs at all. It can improve their performance, but doesn’t change anything else.

(Contributed by Ken Jin in [gh-128563](https://github.com/python/cpython/issues/128563), with ideas on how to implement this
in CPython by Mark Shannon, Garrett Gu, Haoran Xu, and Josh Haberman.)

### Free-threaded mode improvements[¶](#free-threaded-mode-improvements)

CPython’s free-threaded mode ([ PEP 703](https://peps.python.org/pep-0703/)), initially added in 3.13,
has been significantly improved in Python 3.14.
The implementation described in PEP 703 has been finished, including C API
changes, and temporary workarounds in the interpreter were replaced with
more permanent solutions.
The specializing adaptive interpreter (

[) is now enabled in free-threaded mode, which along with many other optimizations greatly improves its performance. The performance penalty on single-threaded code in free-threaded mode is now roughly 5-10%, depending on the platform and C compiler used.](https://peps.python.org/pep-0659/)

**PEP 659**From Python 3.14, when compiling extension modules for the free-threaded build of
CPython on Windows, the preprocessor variable `Py_GIL_DISABLED` now needs to
be specified by the build backend, as it will no longer be determined
automatically by the C compiler. For a running interpreter, the setting that
was used at compile time can be found using [ sysconfig.get_config_var()](../library/sysconfig.html#sysconfig.get_config_var).

The new [ -X context_aware_warnings](../using/cmdline.html#cmdoption-X) flag controls if

[concurrent safe warnings control](#whatsnew314-concurrent-warnings-control)is enabled. The flag defaults to true for the free-threaded build and false for the GIL-enabled build.

A new [ thread_inherit_context](../library/sys.html#sys.flags.thread_inherit_context) flag has been added,
which if enabled means that threads created with 

[start with a copy of the](../library/threading.html#threading.Thread)

`threading.Thread`[of the caller of](../library/contextvars.html#contextvars.Context)

`Context()`[. Most significantly, this makes the warning filtering context established by](../library/threading.html#threading.Thread.start)

`start()`[be “inherited” by threads (or asyncio tasks) started within that context. It also affects other modules that use context variables, such as the](../library/warnings.html#warnings.catch_warnings)

`catch_warnings`[context manager. This flag defaults to true for the free-threaded build and false for the GIL-enabled build.](../library/decimal.html#module-decimal)

`decimal`(Contributed by Sam Gross, Matt Page, Neil Schemenauer, Thomas Wouters, Donghee Na, Kirill Podoprigora, Ken Jin, Itamar Oren, Brett Simmers, Dino Viehland, Nathan Goldbaum, Ralf Gommers, Lysandros Nikolaou, Kumar Aditya, Edgar Margffoy, and many others. Some of these contributors are employed by Meta, which has continued to provide significant engineering resources to support this project.)

### Improved error messages[¶](#improved-error-messages)

- The interpreter now provides helpful suggestions when it detects typos in Python keywords. When a word that closely resembles a Python keyword is encountered, the interpreter will suggest the correct keyword in the error message. This feature helps programmers quickly identify and fix common typing mistakes. For example: - >>> whille True: ... pass Traceback (most recent call last): File "<stdin>", line 1 whille True: ^^^^^^ SyntaxError: invalid syntax. Did you mean 'while'? - While the feature focuses on the most common cases, some variations of misspellings may still result in regular syntax errors. (Contributed by Pablo Galindo in - [gh-132449](https://github.com/python/cpython/issues/132449).)
- `elif`- `else`- [gh-129902](https://github.com/python/cpython/issues/129902).)- >>> if who == "me": ... print("It's me!") ... else: ... print("It's not me!") ... elif who is None: ... print("Who is it?") File "<stdin>", line 5 elif who is None: ^^^^ SyntaxError: 'elif' block follows an 'else' block 
- If a statement is passed to the - [Conditional expressions](../reference/expressions.html#if-expr)after- `else`- `pass`- `break`- `continue`- `if`- `expression`- [gh-129515](https://github.com/python/cpython/issues/129515).)- >>> x = 1 if True else pass Traceback (most recent call last): File "<string>", line 1 x = 1 if True else pass ^^^^ SyntaxError: expected expression after 'else', but statement is given >>> x = continue if True else break Traceback (most recent call last): File "<string>", line 1 x = continue if True else break ^^^^^^^^ SyntaxError: expected expression before 'if', but statement is given 
- When incorrectly closed strings are detected, the error message suggests that the string may be intended to be part of the string. (Contributed by Pablo Galindo in - [gh-88535](https://github.com/python/cpython/issues/88535).)- >>> "The interesting object "The important object" is very important" Traceback (most recent call last): SyntaxError: invalid syntax. Is this intended to be part of the string? 
- When strings have incompatible prefixes, the error now shows which prefixes are incompatible. (Contributed by Nikita Sobolev in - [gh-133197](https://github.com/python/cpython/issues/133197).)- >>> ub'abc' File "<python-input-0>", line 1 ub'abc' ^^ SyntaxError: 'u' and 'b' prefixes are incompatible 
- Improved error messages when using - `as`with incompatible targets in:- Imports: - `import ... as ...`
- From imports: - `from ... import ... as ...`
- Except handlers: - `except ... as ...`
- Pattern-match cases: - `case ... as ...`
 - (Contributed by Nikita Sobolev in - [gh-123539](https://github.com/python/cpython/issues/123539),- [gh-123562](https://github.com/python/cpython/issues/123562), and- [gh-123440](https://github.com/python/cpython/issues/123440).)
- Improved error message when trying to add an instance of an unhashable type to a - `dict`- `set`- [gh-132828](https://github.com/python/cpython/issues/132828).)- >>> s = set() >>> s.add({'pages': 12, 'grade': 'A'}) Traceback (most recent call last): File "<python-input-1>", line 1, in <module> s.add({'pages': 12, 'grade': 'A'}) ~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ TypeError: cannot use 'dict' as a set element (unhashable type: 'dict') >>> d = {} >>> l = [1, 2, 3] >>> d[l] = 12 Traceback (most recent call last): File "<python-input-4>", line 1, in <module> d[l] = 12 ~^^^ TypeError: cannot use 'list' as a dict key (unhashable type: 'list') 
- Improved error message when an object supporting the synchronous context manager protocol is entered using - `async with`- `with`- [gh-128398](https://github.com/python/cpython/issues/128398).)

**PEP 784**[¶](#pep-784-zstandard-support-in-the-standard-library)

**PEP 784**

The new `compression` package contains modules `compression.lzma`,
`compression.bz2`, `compression.gzip` and `compression.zlib`
which re-export the [ lzma](../library/lzma.html#module-lzma), 

[,](../library/bz2.html#module-bz2)

`bz2`[and](../library/gzip.html#module-gzip)

`gzip`[modules respectively. The new import names under](../library/zlib.html#module-zlib)

`zlib``compression` are the
preferred names for importing these compression modules from Python 3.14. However,
the existing modules names have not been deprecated. Any deprecation or removal
of the existing compression modules will occur no sooner than five years after
the release of 3.14.The new `compression.zstd` module provides compression and decompression
APIs for the Zstandard format via bindings to [Meta’s zstd library](https://facebook.github.io/zstd/). Zstandard is a widely adopted, highly
efficient, and fast compression format. In addition to the APIs introduced in
`compression.zstd`, support for reading and writing Zstandard compressed
archives has been added to the [ tarfile](../library/tarfile.html#module-tarfile), 

[, and](../library/zipfile.html#module-zipfile)

`zipfile`[modules.](../library/shutil.html#module-shutil)

`shutil`Here’s an example of using the new module to compress some data:

```
from compression import zstd
import math
data = str(math.pi).encode() * 20
compressed = zstd.compress(data)
ratio = len(compressed) / len(data)
print(f"Achieved compression ratio of {ratio}")
```
As can be seen, the API is similar to the APIs of the `lzma` and
`bz2` modules.

(Contributed by Emma Harper Smith, Adam Turner, Gregory P. Smith, Tomas Roun,
Victor Stinner, and Rogdham in [gh-132983](https://github.com/python/cpython/issues/132983).)

See also

### Asyncio introspection capabilities[¶](#asyncio-introspection-capabilities)

Added a new command-line interface to inspect running Python processes
using asynchronous tasks, available via `python -m asyncio ps PID`
or `python -m asyncio pstree PID`.

The `ps` subcommand inspects the given process ID (PID) and displays
information about currently running asyncio tasks.
It outputs a task table: a flat listing of all tasks, their names,
their coroutine stacks, and which tasks are awaiting them.

The `pstree` subcommand fetches the same information, but instead renders a
visual async call tree, showing coroutine relationships in a hierarchical format.
This command is particularly useful for debugging long-running or stuck
asynchronous programs.
It can help developers quickly identify where a program is blocked,
what tasks are pending, and how coroutines are chained together.

For example given this code:

```
import asyncio
async def play_track(track):
    await asyncio.sleep(5)
    print(f'🎵 Finished: {track}')
async def play_album(name, tracks):
    async with asyncio.TaskGroup() as tg:
        for track in tracks:
            tg.create_task(play_track(track), name=track)
async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(
          play_album('Sundowning', ['TNDNBTG', 'Levitate']),
          name='Sundowning')
        tg.create_task(
          play_album('TMBTE', ['DYWTYLM', 'Aqua Regia']),
          name='TMBTE')
if __name__ == '__main__':
    asyncio.run(main())
```
Executing the new tool on the running process will yield a table like this:

```
python -m asyncio ps 12345
tid        task id              task name            coroutine stack                                    awaiter chain                                      awaiter name    awaiter id
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1935500    0x7fc930c18050       Task-1               TaskGroup._aexit -> TaskGroup.__aexit__ -> main                                                                       0x0
1935500    0x7fc930c18230       Sundowning           TaskGroup._aexit -> TaskGroup.__aexit__ -> album   TaskGroup._aexit -> TaskGroup.__aexit__ -> main    Task-1          0x7fc930c18050
1935500    0x7fc93173fa50       TMBTE                TaskGroup._aexit -> TaskGroup.__aexit__ -> album   TaskGroup._aexit -> TaskGroup.__aexit__ -> main    Task-1          0x7fc930c18050
1935500    0x7fc93173fdf0       TNDNBTG              sleep -> play                                      TaskGroup._aexit -> TaskGroup.__aexit__ -> album   Sundowning      0x7fc930c18230
1935500    0x7fc930d32510       Levitate             sleep -> play                                      TaskGroup._aexit -> TaskGroup.__aexit__ -> album   Sundowning      0x7fc930c18230
1935500    0x7fc930d32890       DYWTYLM              sleep -> play                                      TaskGroup._aexit -> TaskGroup.__aexit__ -> album   TMBTE           0x7fc93173fa50
1935500    0x7fc93161ec30       Aqua Regia           sleep -> play                                      TaskGroup._aexit -> TaskGroup.__aexit__ -> album   TMBTE           0x7fc93173fa50
```
or a tree like this:

```
python -m asyncio pstree 12345
└── (T) Task-1
    └──  main example.py:13
        └──  TaskGroup.__aexit__ Lib/asyncio/taskgroups.py:72
            └──  TaskGroup._aexit Lib/asyncio/taskgroups.py:121
                ├── (T) Sundowning
                │   └──  album example.py:8
                │       └──  TaskGroup.__aexit__ Lib/asyncio/taskgroups.py:72
                │           └──  TaskGroup._aexit Lib/asyncio/taskgroups.py:121
                │               ├── (T) TNDNBTG
                │               │   └──  play example.py:4
                │               │       └──  sleep Lib/asyncio/tasks.py:702
                │               └── (T) Levitate
                │                   └──  play example.py:4
                │                       └──  sleep Lib/asyncio/tasks.py:702
                └── (T) TMBTE
                    └──  album example.py:8
                        └──  TaskGroup.__aexit__ Lib/asyncio/taskgroups.py:72
                            └──  TaskGroup._aexit Lib/asyncio/taskgroups.py:121
                                ├── (T) DYWTYLM
                                │   └──  play example.py:4
                                │       └──  sleep Lib/asyncio/tasks.py:702
                                └── (T) Aqua Regia
                                    └──  play example.py:4
                                        └──  sleep Lib/asyncio/tasks.py:702
```
If a cycle is detected in the async await graph (which could indicate a programming issue), the tool raises an error and lists the cycle paths that prevent tree construction:

```
python -m asyncio pstree 12345
ERROR: await-graph contains cycles - cannot print a tree!
cycle: Task-2 → Task-3 → Task-2
```
(Contributed by Pablo Galindo, Łukasz Langa, Yury Selivanov, and Marta
Gomez Macias in [gh-91048](https://github.com/python/cpython/issues/91048).)

### Concurrent safe warnings control[¶](#concurrent-safe-warnings-control)

The [ warnings.catch_warnings](../library/warnings.html#warnings.catch_warnings) context manager will now optionally
use a context variable for warning filters. This is enabled by setting
the 

[flag, either with the](../library/sys.html#sys.flags.context_aware_warnings)

`context_aware_warnings``-X`
command-line option or an environment variable. This gives predictable
warnings control when using `catch_warnings` combined with
multiple threads or asynchronous tasks. The flag defaults to true for the
free-threaded build and false for the GIL-enabled build.(Contributed by Neil Schemenauer and Kumar Aditya in [gh-130010](https://github.com/python/cpython/issues/130010).)

## Other language changes[¶](#other-language-changes)

- All Windows code pages are now supported as ‘cpXXX’ codecs on Windows. (Contributed by Serhiy Storchaka in - [gh-123803](https://github.com/python/cpython/issues/123803).)
- Implement mixed-mode arithmetic rules combining real and complex numbers as specified by the C standard since C99. (Contributed by Sergey B Kirpichev in - [gh-69639](https://github.com/python/cpython/issues/69639).)
- More syntax errors are now detected regardless of optimisation and the - `-O`- `__debug__`, incorrect use of- `await`- `python -O -c 'assert (__debug__ := 1)'`or- `python -O -c 'assert await 1'`now produce- `SyntaxError`- [gh-122245](https://github.com/python/cpython/issues/122245)&- [gh-121637](https://github.com/python/cpython/issues/121637).)
- When subclassing a pure C type, the C slots for the new type are no longer replaced with a wrapped version on class creation if they are not explicitly overridden in the subclass. (Contributed by Tomasz Pytel in - [gh-132284](https://github.com/python/cpython/issues/132284).)

### Built-ins[¶](#built-ins)

- The - `bytes.fromhex()`- `bytearray.fromhex()`- `bytes`- [bytes-like objects](../glossary.html#term-bytes-like-object). (Contributed by Daniel Pope in- [gh-129349](https://github.com/python/cpython/issues/129349).)
- Add class methods - `float.from_number()`- `complex.from_number()`- `float`- `complex`- `TypeError`- [gh-84978](https://github.com/python/cpython/issues/84978).)
- Support underscore and comma as thousands separators in the fractional part for floating-point presentation types of the new-style string formatting (with - `format()`- [f-strings](../reference/lexical_analysis.html#f-strings)). (Contributed by Sergey B Kirpichev in- [gh-87790](https://github.com/python/cpython/issues/87790).)
- The - `int()`- `__trunc__()`- `int()`must implement either- `__int__()`- `__index__()`- [gh-119743](https://github.com/python/cpython/issues/119743).)
- The - `map()`- *strict*flag like- `zip()`- [gh-119793](https://github.com/python/cpython/issues/119793).)
- The - `memoryview`- [generic type](../glossary.html#term-generic-type). (Contributed by Brian Schubert in- [gh-126012](https://github.com/python/cpython/issues/126012).)
- Using - `NotImplemented`- `TypeError`- `DeprecationWarning`- [gh-118767](https://github.com/python/cpython/issues/118767).)
- Three-argument - `pow()`- `__rpow__()`- `pow()`and the binary power operator. (Contributed by Serhiy Storchaka in- [gh-130104](https://github.com/python/cpython/issues/130104).)
- `super`- `copyable`- `pickleable`- [gh-125767](https://github.com/python/cpython/issues/125767).)

### Command line and environment[¶](#command-line-and-environment)

- The import time flag can now track modules that are already loaded (‘cached’), via the new - `-X importtime=2`- `self`and- `cumulative`times are replaced by the string- `cached`.- Values above - `2`for- `-X importtime`are now reserved for future use.- (Contributed by Noah Kim and Adam Turner in - [gh-118655](https://github.com/python/cpython/issues/118655).)
- The command-line option - `-c`- `textwrap.dedent()`- [gh-103998](https://github.com/python/cpython/issues/103998).)
- `-J`is no longer a reserved flag for- [Jython](https://www.jython.org/), and now has no special meaning. (Contributed by Adam Turner in- [gh-133336](https://github.com/python/cpython/issues/133336).)

### PEP 758: Allow `except` and `except*` expressions without brackets[¶](#pep-758-allow-except-and-except-expressions-without-brackets)

The [ except](../reference/compound_stmts.html#except) and 

[expressions now allow brackets to be omitted when there are multiple exception types and the](../reference/compound_stmts.html#except-star)

`except*``as` clause is not used.
For example:```
try:
    connect_to_server()
except TimeoutError, ConnectionRefusedError:
    print('The network has ceased to be!')
```
(Contributed by Pablo Galindo and Brett Cannon in [ PEP 758](https://peps.python.org/pep-0758/) and 

[gh-131831](https://github.com/python/cpython/issues/131831).)

### PEP 765: Control flow in `finally`[¶](#pep-765-control-flow-in-finally-blocks)

`finally`The compiler now emits a [ SyntaxWarning](../library/exceptions.html#SyntaxWarning) when a 

[,](../reference/simple_stmts.html#return)

`return`[, or](../reference/simple_stmts.html#break)

`break`[statement have the effect of leaving a](../reference/simple_stmts.html#continue)

`continue`[block. This change is specified in](../reference/compound_stmts.html#finally)

`finally`[.](https://peps.python.org/pep-0765/)

**PEP 765**In situations where this change is inconvenient (such as those where the
warnings are redundant due to code linting), the [warning filter](../library/warnings.html#warning-filter) can be used to turn off all syntax warnings by adding
`ignore::SyntaxWarning` as a filter. This can be specified in combination
with a filter that converts other warnings to errors (for example, passing
`-Werror -Wignore::SyntaxWarning` as CLI options, or setting
`PYTHONWARNINGS=error,ignore::SyntaxWarning`).

Note that applying such a filter at runtime using the [ warnings](../library/warnings.html#module-warnings) module
will only suppress the warning in code that is compiled 

*after*the filter is adjusted. Code that is compiled prior to the filter adjustment (for example, when a module is imported) will still emit the syntax warning.

(Contributed by Irit Katriel in [gh-130080](https://github.com/python/cpython/issues/130080).)

### Garbage collection[¶](#garbage-collection)

**From Python 3.14.5 onwards:**

The garbage collector (GC) has changed in Python 3.14.5.

Python 3.14.0-3.14.4 shipped with a new incremental GC.
However, due to a number of [reports](https://github.com/python/cpython/issues/142516)
of significant memory pressure in production environments,
it has been reverted back to the generational GC from 3.13.
This is the GC now used in Python 3.14.5 and later.

**Previously in Python 3.14.0-3.14.4:**

The cycle garbage collector is now incremental. This means that maximum pause times are reduced by an order of magnitude or more for larger heaps.

There are now only two generations: young and old.
When [ gc.collect()](../library/gc.html#gc.collect) is not called directly, the
GC is invoked a little less frequently. When invoked, it
collects the young generation and an increment of the
old generation, instead of collecting one or more generations.

The behavior of `gc.collect()` changes slightly:

- `gc.collect(1)`: Performs an increment of garbage collection, rather than collecting generation 1.
- Other calls to - `gc.collect()`are unchanged.

(Contributed by Mark Shannon in [gh-108362](https://github.com/python/cpython/issues/108362).)

### Default interactive shell[¶](#default-interactive-shell)

- The default - [interactive](../glossary.html#term-interactive)shell now highlights Python syntax. The feature is enabled by default, save if- `PYTHON_BASIC_REPL`- [Controlling color](../using/cmdline.html#using-on-controlling-color)for details.- The default color theme for syntax highlighting strives for good contrast and exclusively uses the 4-bit VGA standard ANSI color codes for maximum compatibility. The theme can be customized using an experimental API - `_colorize.set_theme()`. This can be called interactively or in the- `PYTHONSTARTUP`- (Contributed by Łukasz Langa in - [gh-131507](https://github.com/python/cpython/issues/131507).)
- The default - [interactive](../glossary.html#term-interactive)shell now supports import auto-completion. This means that typing- `import co`and pressing- `<Tab>`will suggest modules starting with- `co`. Similarly, typing- `from concurrent import i`will suggest submodules of- `concurrent`starting with- `i`. Note that autocompletion of module attributes is not currently supported. (Contributed by Tomas Roun in- [gh-69605](https://github.com/python/cpython/issues/69605).)

## New modules[¶](#new-modules)

- `annotationlib`- [annotations](../glossary.html#term-annotation). See- [PEP 749](#whatsnew314-deferred-annotations)for more details. (Contributed by Jelle Zijlstra in- [gh-119180](https://github.com/python/cpython/issues/119180).)
- `compression`- `compression.zstd`- [PEP 784](#whatsnew314-zstandard)for more details. (Contributed by Emma Harper Smith, Adam Turner, Gregory P. Smith, Tomas Roun, Victor Stinner, and Rogdham in- [gh-132983](https://github.com/python/cpython/issues/132983).)
- `concurrent.interpreters`- [PEP 734](#whatsnew314-multiple-interpreters)for more details. (Contributed by Eric Snow in- [gh-134939](https://github.com/python/cpython/issues/134939).)
- `string.templatelib`- [PEP 750](#whatsnew314-template-string-literals)for more details. (Contributed by Jim Baker, Guido van Rossum, Paul Everitt, Koudai Aono, Lysandros Nikolaou, Dave Peck, Adam Turner, Jelle Zijlstra, Bénédikt Tran, and Pablo Galindo Salgado in- [gh-132661](https://github.com/python/cpython/issues/132661).)

## Improved modules[¶](#improved-modules)

### argparse[¶](#argparse)

- The default value of the - [program name](../library/argparse.html#prog)for- `argparse.ArgumentParser`- `__main__`module code. (Contributed by Serhiy Storchaka and Alyssa Coghlan in- [gh-66436](https://github.com/python/cpython/issues/66436).)
- Introduced the optional - *suggest_on_error*parameter to- `argparse.ArgumentParser`- [gh-124456](https://github.com/python/cpython/issues/124456).)
- Enable color for help text, which can be disabled with the optional - *color*parameter to- `argparse.ArgumentParser`- [environment variables](../using/cmdline.html#using-on-controlling-color). (Contributed by Hugo van Kemenade in- [gh-130645](https://github.com/python/cpython/issues/130645).)

### ast[¶](#ast)

- Add - `compare()`- [gh-60191](https://github.com/python/cpython/issues/60191).)
- Add support for - `copy.replace()`- [gh-121141](https://github.com/python/cpython/issues/121141).)
- Docstrings are now removed from an optimized AST in optimization level 2. (Contributed by Irit Katriel in - [gh-123958](https://github.com/python/cpython/issues/123958).)
- The - `repr()`- [gh-116022](https://github.com/python/cpython/issues/116022).)
- When called with an AST as input, the - `parse()`- [gh-130139](https://github.com/python/cpython/issues/130139).)
- Add new options to the command-line interface: - `--feature-version`- `--optimize`- `--show-empty`- [gh-133367](https://github.com/python/cpython/issues/133367).)

### asyncio[¶](#asyncio)

- The function and methods named - `create_task()`now take an arbitrary list of keyword arguments. All keyword arguments are passed to the- `Task`- `set_task_factory()`- `name`and- `context`keyword arguments are no longer special; the name should now be set using the- `name`keyword argument of the factory, and- `context`may be- `None`.- This affects the following function and methods: - `asyncio.create_task()`- `asyncio.loop.create_task()`- `asyncio.TaskGroup.create_task()`- (Contributed by Thomas Grainger in - [gh-128307](https://github.com/python/cpython/issues/128307).)
- There are two new utility functions for introspecting and printing a program’s call graph: - `capture_call_graph()`- `print_call_graph()`- [Asyncio introspection capabilities](#whatsnew314-asyncio-introspection)for more details. (Contributed by Yury Selivanov, Pablo Galindo Salgado, and Łukasz Langa in- [gh-91048](https://github.com/python/cpython/issues/91048).)

### calendar[¶](#calendar)

- By default, today’s date is highlighted in color in - `calendar`- [command-line](../library/calendar.html#calendar-cli)text output. This can be controlled by- [environment variables](../using/cmdline.html#using-on-controlling-color). (Contributed by Hugo van Kemenade in- [gh-128317](https://github.com/python/cpython/issues/128317).)

### concurrent.futures[¶](#concurrent-futures)

- Add a new executor class, - `InterpreterPoolExecutor`- This is separate from the new - `interpreters`- [PEP 734](#whatsnew314-multiple-interpreters). (Contributed by Eric Snow in- [gh-124548](https://github.com/python/cpython/issues/124548).)

- On Unix platforms other than macOS, - [‘forkserver’](../library/multiprocessing.html#multiprocessing-start-method-forkserver)is now the default- [start method](../library/multiprocessing.html#multiprocessing-start-methods)for- `ProcessPoolExecutor`- [‘fork’](../library/multiprocessing.html#multiprocessing-start-method-fork)). This change does not affect Windows or macOS, where- [‘spawn’](../library/multiprocessing.html#multiprocessing-start-method-spawn)remains the default start method.- If the threading incompatible - *fork*method is required, you must explicitly request it by supplying a multiprocessing context- *mp_context*to- `ProcessPoolExecutor`- See - [forkserver restrictions](../library/multiprocessing.html#multiprocessing-programming-forkserver)for information and differences with the- *fork*method and how this change may affect existing code with mutable global shared variables and/or shared objects that can not be automatically- `pickled`- (Contributed by Gregory P. Smith in - [gh-84559](https://github.com/python/cpython/issues/84559).)
- Add two new methods to - `ProcessPoolExecutor`- `terminate_workers()`- `kill_workers()`- [gh-130849](https://github.com/python/cpython/issues/130849).)
- Add the optional - *buffersize*parameter to- `Executor.map`- *iterables*pauses until a result is yielded from the buffer. (Contributed by Enzo Bonnal and Josh Rosenberg in- [gh-74028](https://github.com/python/cpython/issues/74028).)

### configparser[¶](#configparser)

- `configparser`will no longer write config files it cannot read, to improve security. Attempting to- `write()`- `InvalidWriteError`- [gh-129270](https://github.com/python/cpython/issues/129270).)

### contextvars[¶](#contextvars)

- Support the - [context manager](../glossary.html#term-context-manager)protocol for- `Token`- [gh-129889](https://github.com/python/cpython/issues/129889).)

### ctypes[¶](#ctypes)

- The layout of - [bit fields](../library/ctypes.html#ctypes-bit-fields-in-structures-unions)in- `Structure`- `Union`- [gh-97702](https://github.com/python/cpython/issues/97702).)
- The - `Structure._layout_`- [gh-97702](https://github.com/python/cpython/issues/97702).)
- The class of - `Structure`- `Union`- `CField`- [gh-128715](https://github.com/python/cpython/issues/128715).)
- On Windows, the - `COMError`- [gh-126686](https://github.com/python/cpython/issues/126686).)
- On Windows, the - `CopyComPointer()`- [gh-127275](https://github.com/python/cpython/issues/127275).)
- Add - `memoryview_at()`- `memoryview`- `ctypes.string_at()`- [gh-112018](https://github.com/python/cpython/issues/112018).)
- Complex types, - `c_float_complex`- `c_double_complex`- `c_longdouble_complex`- `libffi`library support complex C types. (Contributed by Sergey B Kirpichev in- [gh-61103](https://github.com/python/cpython/issues/61103).)
- Add - `ctypes.util.dllist()`- [gh-119349](https://github.com/python/cpython/issues/119349).)
- Move - `ctypes.POINTER()`- `_pointer_type_cache`) to the- `_CData.__pointer_type__`- `ctypes`types. This will stop the cache from growing without limits in some situations. (Contributed by Sergey Miryanov in- [gh-100926](https://github.com/python/cpython/issues/100926).)
- The - `py_object`- [generic type](../glossary.html#term-generic-type). (Contributed by Brian Schubert in- [gh-132168](https://github.com/python/cpython/issues/132168).)
- `ctypes`now supports- [free-threading builds](../glossary.html#term-free-threading). (Contributed by Kumar Aditya and Peter Bierma in- [gh-127945](https://github.com/python/cpython/issues/127945).)

### curses[¶](#curses)

- Add the - `assume_default_colors()`- `use_default_colors()`- `0`. (Contributed by Serhiy Storchaka in- [gh-133139](https://github.com/python/cpython/issues/133139).)

### datetime[¶](#datetime)

- Add the - `strptime()`- `datetime.date`- `datetime.time`- [gh-41431](https://github.com/python/cpython/issues/41431).)

### decimal[¶](#decimal)

- Add - `Decimal.from_number()`- `Decimal`- [gh-121798](https://github.com/python/cpython/issues/121798).)
- Expose - `IEEEContext()`- [gh-53032](https://github.com/python/cpython/issues/53032).)

### difflib[¶](#difflib)

### dis[¶](#dis)

- Add support for rendering full source location information of - `instructions`- *show_positions*keyword argument:- This feature is also exposed via - `dis --show-positions`- [gh-123165](https://github.com/python/cpython/issues/123165).)
- Add the - `dis --specialized`- [gh-127413](https://github.com/python/cpython/issues/127413).)

### errno[¶](#errno)

### faulthandler[¶](#faulthandler)

- Add support for printing the C stack trace on systems that - [support it](../library/faulthandler.html#c-stack-compatibility)via the new- `dump_c_stack()`- *c_stack*argument in- `faulthandler.enable()`- [gh-127604](https://github.com/python/cpython/issues/127604).)

### fnmatch[¶](#fnmatch)

- Add - `filterfalse()`- [gh-74598](https://github.com/python/cpython/issues/74598).)

### fractions[¶](#fractions)

- A - `Fraction`- `as_integer_ratio()`method. (Contributed by Serhiy Storchaka in- [gh-82017](https://github.com/python/cpython/issues/82017).)
- Add - `Fraction.from_number()`- `Fraction`- [gh-121797](https://github.com/python/cpython/issues/121797).)

### functools[¶](#functools)

- Add the - `Placeholder`- `partial()`- `partialmethod()`- [partial object](../library/functools.html#partial-objects). (Contributed by Dominykas Grigonis in- [gh-119127](https://github.com/python/cpython/issues/119127).)
- Allow the - *initial*parameter of- `reduce()`- [gh-125916](https://github.com/python/cpython/issues/125916).)

### getopt[¶](#getopt)

### getpass[¶](#getpass)

### graphlib[¶](#graphlib)

- Allow - `TopologicalSorter.prepare()`- [gh-130914](https://github.com/python/cpython/issues/130914).)

### heapq[¶](#heapq)

- The - `heapq`module has improved support for working with max-heaps, via the following new functions:

### hmac[¶](#hmac)

### http[¶](#http)

- Directory lists and error pages generated by the - `http.server`- [gh-123430](https://github.com/python/cpython/issues/123430).)
- The - `http.server`- `http.server.HTTPSServer`- `python -m http.server`) through the following options:- `--tls-cert <path>`
- `--tls-key <path>`
- `--tls-password-file <path>`
 - (Contributed by Semyon Moroz in - [gh-85162](https://github.com/python/cpython/issues/85162).)

### imaplib[¶](#imaplib)

- Add - `IMAP4.idle()`- `IDLE`command as defined in- **RFC 2177**- [gh-55454](https://github.com/python/cpython/issues/55454).)

### inspect[¶](#inspect)

- `signature()`- *annotation_format*to control the- `annotationlib.Format`- [gh-101552](https://github.com/python/cpython/issues/101552).)
- `Signature.format()`- *unquote_annotations*. If true, string- [annotations](../glossary.html#term-annotation)are displayed without surrounding quotes. (Contributed by Jelle Zijlstra in- [gh-101552](https://github.com/python/cpython/issues/101552).)
- Add function - `ispackage()`- [package](../glossary.html#term-package)or not. (Contributed by Zhikang Yan in- [gh-125634](https://github.com/python/cpython/issues/125634).)

### io[¶](#io)

- Reading text from a non-blocking stream with - `read`may now raise a- `BlockingIOError`- [gh-109523](https://github.com/python/cpython/issues/109523).)
- Add the - `Reader`- `Writer`- `typing.IO`- `typing.TextIO`- `typing.BinaryIO`- [gh-127648](https://github.com/python/cpython/issues/127648).)

### json[¶](#json)

- Add exception notes for JSON serialization errors that allow identifying the source of the error. (Contributed by Serhiy Storchaka in - [gh-122163](https://github.com/python/cpython/issues/122163).)
- Allow using the - `json`- `-m`- **python -m json**. This is now preferred to- **python -m json.tool**, which is- [soft deprecated](../glossary.html#term-soft-deprecated). See the- [JSON command-line interface](../library/json.html#json-commandline)documentation. (Contributed by Trey Hunner in- [gh-122873](https://github.com/python/cpython/issues/122873).)
- By default, the output of the - [JSON command-line interface](../library/json.html#json-commandline)is highlighted in color. This can be controlled by- [environment variables](../using/cmdline.html#using-on-controlling-color). (Contributed by Tomas Roun in- [gh-131952](https://github.com/python/cpython/issues/131952).)

### linecache[¶](#linecache)

### logging.handlers[¶](#logging-handlers)

- `QueueListener`- [context manager](../glossary.html#term-context-manager)protocol. (Contributed by Charles Machalow in- [gh-132106](https://github.com/python/cpython/issues/132106).)
- `QueueListener.start`- `RuntimeError`- [gh-132106](https://github.com/python/cpython/issues/132106).)

### math[¶](#math)

- Added more detailed error messages for domain errors in the module. (Contributed by Charlie Zhao and Sergey B Kirpichev in - [gh-101410](https://github.com/python/cpython/issues/101410).)

### mimetypes[¶](#mimetypes)

- Add a public - [command-line](../library/mimetypes.html#mimetypes-cli)for the module, invoked via- **python -m mimetypes**. (Contributed by Oleg Iarygin and Hugo van Kemenade in- [gh-93096](https://github.com/python/cpython/issues/93096).)
- Add several new MIME types based on RFCs and common usage: - Microsoft and - **RFC 8081**- Embedded OpenType: - `application/vnd.ms-fontobject`
- OpenType Layout (OTF) - `font/otf`
- TrueType: - `font/ttf`
- WOFF 1.0 - `font/woff`
- WOFF 2.0 - `font/woff2`
 - **RFC 9559**- audio with no video: - `audio/matroska`(- `.mka`)
- video: - `video/matroska`(- `.mkv`)
- stereoscopic video: - `video/matroska-3d`(- `.mk3d`)
 - Images with RFCs - **RFC 1494**- `.g3`)
- **RFC 3362**- `.t38`)
- **RFC 3745**- `.jp2`), extension (- `.jpx`) and compound (- `.jpm`)
- **RFC 3950**- `.tfx`)
- **RFC 4047**- `.fits`)
- **RFC 7903**- `.emf`) and Windows Metafile (- `.wmf`)
 - Other MIME type additions and changes - **RFC 2361**- `.avi`to- `video/vnd.avi`and for- `.wav`to- `audio/vnd.wave`
- **RFC 4337**- `audio/mp4`(- `.m4a`)
- **RFC 5334**- `.oga`,- `.ogg`and- `.ogx`)
- **RFC 6713**- `application/gzip`(- `.gz`)
- **RFC 9639**- `audio/flac`(- `.flac`)
- **RFC 9512**- `application/yaml`MIME type for YAML files (- `.yaml`and- `.yml`)
- Add 7z - `application/x-7z-compressed`(- `.7z`)
- Add Android Package - `application/vnd.android.package-archive`(- `.apk`) when not strict
- Add deb - `application/x-debian-package`(- `.deb`)
- Add glTF binary - `model/gltf-binary`(- `.glb`)
- Add glTF JSON/ASCII - `model/gltf+json`(- `.gltf`)
- Add M4V - `video/x-m4v`(- `.m4v`)
- Add PHP - `application/x-httpd-php`(- `.php`)
- Add RAR - `application/vnd.rar`(- `.rar`)
- Add RPM - `application/x-rpm`(- `.rpm`)
- Add STL - `model/stl`(- `.stl`)
- Add Windows Media Video - `video/x-ms-wmv`(- `.wmv`)
- De facto: Add WebM - `audio/webm`(- `.weba`)
- [ECMA-376](https://ecma-international.org/publications-and-standards/standards/ecma-376/): Add- `.docx`,- `.pptx`and- `.xlsx`types
- [OASIS](https://docs.oasis-open.org/office/v1.2/cs01/OpenDocument-v1.2-cs01-part1.html#Appendix_C): Add OpenDocument- `.odg`,- `.odp`,- `.ods`and- `.odt`types
- [W3C](https://www.w3.org/TR/epub-33/#app-media-type): Add EPUB- `application/epub+zip`(- `.epub`)
 - (Contributed by Sahil Prajapati and Hugo van Kemenade in - [gh-84852](https://github.com/python/cpython/issues/84852), by Sasha “Nelie” Chernykh and Hugo van Kemenade in- [gh-132056](https://github.com/python/cpython/issues/132056), and by Hugo van Kemenade in- [gh-89416](https://github.com/python/cpython/issues/89416),- [gh-85957](https://github.com/python/cpython/issues/85957), and- [gh-129965](https://github.com/python/cpython/issues/129965).)

### multiprocessing[¶](#multiprocessing)

- On Unix platforms other than macOS, - [‘forkserver’](../library/multiprocessing.html#multiprocessing-start-method-forkserver)is now the default- [start method](../library/multiprocessing.html#multiprocessing-start-methods)(replacing- [‘fork’](../library/multiprocessing.html#multiprocessing-start-method-fork)). This change does not affect Windows or macOS, where- [‘spawn’](../library/multiprocessing.html#multiprocessing-start-method-spawn)remains the default start method.- If the threading incompatible - *fork*method is required, you must explicitly request it via a context from- `get_context()`- `set_start_method()`- See - [forkserver restrictions](../library/multiprocessing.html#multiprocessing-programming-forkserver)for information and differences with the- *fork*method and how this change may affect existing code with mutable global shared variables and/or shared objects that can not be automatically- `pickled`- (Contributed by Gregory P. Smith in - [gh-84559](https://github.com/python/cpython/issues/84559).)
- `multiprocessing`- `'forkserver'`start method now authenticates its control socket to avoid solely relying on filesystem permissions to restrict what other processes could cause the forkserver to spawn workers and run code. (Contributed by Gregory P. Smith for- [gh-97514](https://github.com/python/cpython/issues/97514).)
- The - [multiprocessing proxy objects](../library/multiprocessing.html#multiprocessing-proxy-objects)for- *list*and- *dict*types gain previously overlooked missing methods:- `clear()`and- `copy()`for proxies of- `list`
- `fromkeys()`- `reversed(d)`,- `d | {}`,- `{} | d`,- `d |= {'b': 2}`for proxies of- `dict`
 - (Contributed by Roy Hyunjin Han for - [gh-103134](https://github.com/python/cpython/issues/103134).)
- Add support for shared - `set`- `SyncManager.set()`- `set()`- `Manager()`- [gh-129949](https://github.com/python/cpython/issues/129949).)
- Add the - `interrupt()`- `multiprocessing.Process`- `SIGINT`- `finally`- [gh-131913](https://github.com/python/cpython/issues/131913).)

### operator[¶](#operator)

- Add - `is_none()`- `is_not_none()`- `operator.is_none(obj)`is equivalent to- `obj is None`and- `operator.is_not_none(obj)`is equivalent to- `obj is not None`. (Contributed by Raymond Hettinger and Nico Mexis in- [gh-115808](https://github.com/python/cpython/issues/115808).)

### os[¶](#os)

- Add the - `reload_environ()`- `os.environ`- `os.environb`- `os.putenv()`- `os.unsetenv()`- [gh-120057](https://github.com/python/cpython/issues/120057).)
- Add the - `SCHED_DEADLINE`- `SCHED_NORMAL`- `os`module. (Contributed by James Roy in- [gh-127688](https://github.com/python/cpython/issues/127688).)
- Add the - `readinto()`- [buffer object](../c-api/buffer.html#bufferobjects)from a file descriptor. (Contributed by Cody Maloney in- [gh-129205](https://github.com/python/cpython/issues/129205).)

### os.path[¶](#os-path)

- The - *strict*parameter to- `realpath()`- `ALLOW_MISSING`- `FileNotFoundError`- **CVE 2025-4517**

### pathlib[¶](#pathlib)

- Add methods to - `pathlib.Path`- `copy()`
- `copy_into()`- *into*a destination directory.
- `move()`
- `move_into()`- *into*a destination directory.
 - (Contributed by Barney Gale in - [gh-73991](https://github.com/python/cpython/issues/73991).)
- Add the - `info`- `pathlib.types.PathInfo`- `stat()`- `iterdir()`- [gh-125413](https://github.com/python/cpython/issues/125413).)

### pdb[¶](#pdb)

- The - `pdb`- `-p PID`- python -m pdb -p 1234 - This will connect to the Python process with the given PID and allow you to debug it interactively. Notice that due to how the Python interpreter works attaching to a remote process that is blocked in a system call or waiting for I/O will only work once the next bytecode instruction is executed or when the process receives a signal. - This feature uses - [PEP 768](#whatsnew314-remote-debugging)and the new- `sys.remote_exec()`- (Contributed by Matt Wozniski and Pablo Galindo in - [gh-131591](https://github.com/python/cpython/issues/131591).)
- Hardcoded breakpoints ( - `breakpoint()`- `set_trace()`- `Pdb`- `set_trace()`- `display`- `commands`- [gh-121450](https://github.com/python/cpython/issues/121450).)
- Add a new argument - *mode*to- `pdb.Pdb`- `restart`command when- `pdb`- `inline`mode. (Contributed by Tian Gao in- [gh-123757](https://github.com/python/cpython/issues/123757).)
- A confirmation prompt will be shown when the user tries to quit - `pdb`- `inline`mode.- `y`,- `Y`,- `<Enter>`or- `EOF`will confirm the quit and call- `sys.exit()`- `bdb.BdbQuit`- [gh-124704](https://github.com/python/cpython/issues/124704).)
- Inline breakpoints like - `breakpoint()`- `pdb.set_trace()`- `skip`pattern (if any). (Contributed by Tian Gao in- [gh-130493](https://github.com/python/cpython/issues/130493).)
- `<tab>`at the beginning of the line in- `pdb`- `\t`character. (Contributed by Tian Gao in- [gh-130471](https://github.com/python/cpython/issues/130471).)
- Auto-indent is introduced in - `pdb`- [gh-133350](https://github.com/python/cpython/issues/133350).)
- `$_asynctask`is added to access the current asyncio task if applicable. (Contributed by Tian Gao in- [gh-124367](https://github.com/python/cpython/issues/124367).)
- `pdb.set_trace_async()`- `await`- [gh-132576](https://github.com/python/cpython/issues/132576).)
- Source code displayed in - `pdb`- [interactive](../glossary.html#term-interactive)shell, in addition to the newly added- `colorize`argument of- `pdb.Pdb`- [gh-133355](https://github.com/python/cpython/issues/133355).)

### pickle[¶](#pickle)

- Set the default protocol version on the - `pickle`- [pickle protocols](../library/pickle.html#pickle-protocols).
- Add exception notes for pickle serialization errors that allow identifying the source of the error. (Contributed by Serhiy Storchaka in - [gh-122213](https://github.com/python/cpython/issues/122213).)

### platform[¶](#platform)

- Add - `invalidate_caches()`- `platform`module. (Contributed by Bénédikt Tran in- [gh-122549](https://github.com/python/cpython/issues/122549).)

### pydoc[¶](#pydoc)

- [Annotations](../glossary.html#term-annotation)in help output are now usually displayed in a format closer to that in the original source. (Contributed by Jelle Zijlstra in- [gh-101552](https://github.com/python/cpython/issues/101552).)

### re[¶](#re)

- Support - `\z`as a synonym for- `\Z`in- `regular expressions`- `\Z`, which has subtly different behavior. (Contributed by Serhiy Storchaka in- [gh-133306](https://github.com/python/cpython/issues/133306).)
- `\B`in- `regular expression`- `\b`. (Contributed by Serhiy Storchaka in- [gh-124130](https://github.com/python/cpython/issues/124130).)

### socket[¶](#socket)

- Improve and fix support for Bluetooth sockets. - Fix support of Bluetooth sockets on NetBSD and DragonFly BSD. (Contributed by Serhiy Storchaka in - [gh-132429](https://github.com/python/cpython/issues/132429).)
- Fix support for - `BTPROTO_HCI`- [gh-111178](https://github.com/python/cpython/issues/111178).)
- Add support for - `BTPROTO_SCO`- [gh-85302](https://github.com/python/cpython/issues/85302).)
- Add support for - *cid*and- *bdaddr_type*in the address for- `BTPROTO_L2CAP`- [gh-132429](https://github.com/python/cpython/issues/132429).)
- Add support for - *channel*in the address for- `BTPROTO_HCI`- [gh-70145](https://github.com/python/cpython/issues/70145).)
- Accept an integer as the address for - `BTPROTO_HCI`- [gh-132099](https://github.com/python/cpython/issues/132099).)
- Return - *cid*in- `getsockname()`- `BTPROTO_L2CAP`- [gh-132429](https://github.com/python/cpython/issues/132429).)
- Add many new constants. (Contributed by Serhiy Storchaka in - [gh-132734](https://github.com/python/cpython/issues/132734).)
 

### ssl[¶](#ssl)

### struct[¶](#struct)

### symtable[¶](#symtable)

### sys[¶](#sys)

- The previously undocumented special function - `sys.getobjects()`- [gh-125286](https://github.com/python/cpython/issues/125286).)
- Add - `sys._is_immortal()`- [immortal](../glossary.html#term-immortal). (Contributed by Peter Bierma in- [gh-128509](https://github.com/python/cpython/issues/128509).)
- On FreeBSD, - `sys.platform`- `'freebsd'`, instead of- `'freebsd13'`or- `'freebsd14'`. (Contributed by Michael Osipov in- [gh-129393](https://github.com/python/cpython/issues/129393).)
- Raise - `DeprecationWarning`- `sys._clear_type_cache()`
- Add - `sys.remote_exec()`- [PEP 768](#whatsnew314-remote-debugging)for details. (Contributed by Pablo Galindo Salgado, Matt Wozniski, and Ivona Stojanovic in- [gh-131591](https://github.com/python/cpython/issues/131591).)
- Add the - `sys._jit`- [gh-133231](https://github.com/python/cpython/issues/133231).)

### sys.monitoring[¶](#sys-monitoring)

- Add two new monitoring events, - `BRANCH_LEFT`- `BRANCH_RIGHT`- `BRANCH`event. (Contributed by Mark Shannon in- [gh-122548](https://github.com/python/cpython/issues/122548).)

### sysconfig[¶](#sysconfig)

- Add - `ABIFLAGS`key to- `get_config_vars()`- [gh-131799](https://github.com/python/cpython/issues/131799).)

### tarfile[¶](#tarfile)

- `data_filter()`- [gh-127987](https://github.com/python/cpython/issues/127987)and- **CVE 2025-4138**
- `extractall()`- [gh-127987](https://github.com/python/cpython/issues/127987)and- **CVE 2024-12718**
- `extract()`- `extractall()`- `LinkFallbackError`- **CVE 2025-4330**- **CVE 2024-12718**
- `extract()`- `extractall()`- `errorlevel()`- [gh-112887](https://github.com/python/cpython/issues/112887)and- **CVE 2025-4435**

### threading[¶](#threading)

- `threading.Thread.start()`- `threading.Thread.name`- [gh-59705](https://github.com/python/cpython/issues/59705).)

### tkinter[¶](#tkinter)

### turtle[¶](#turtle)

- Add context managers for - `turtle.fill()`- `turtle.poly()`- `turtle.no_animation()`- [gh-126350](https://github.com/python/cpython/issues/126350).)

### types[¶](#types)

- `types.UnionType`- `typing.Union`- [below](#whatsnew314-typing-union)for more details. (Contributed by Jelle Zijlstra in- [gh-105499](https://github.com/python/cpython/issues/105499).)

### typing[¶](#typing)

- The - `types.UnionType`- `typing.Union`- `Union[int, str]`) and new-style unions (- `int | str`) now create instances of the same runtime type. This unifies the behavior between the two syntaxes, but leads to some differences in behavior that may affect users who introspect types at runtime:- Both syntaxes for creating a union now produce the same string representation in - `repr()`- `repr(Union[int, str])`is now- `"int | str"`instead of- `"typing.Union[int, str]"`.
- Unions created using the old syntax are no longer cached. Previously, running - `Union[int, str]`multiple times would return the same object (- `Union[int, str] is Union[int, str]`would be- `True`), but now it will return two different objects. Use- `==`to compare unions for equality, not- `is`. New-style unions have never been cached this way. This change could increase memory usage for some programs that use a large number of unions created by subscripting- `typing.Union`. However, several factors offset this cost: unions used in annotations are no longer evaluated by default in Python 3.14 because of- **PEP 649**- `types.UnionType`- `Union[]`was on prior Python versions; and removing the cache also saves some space. It is therefore unlikely that this change will cause a significant increase in memory usage for most users.
- Previously, old-style unions were implemented using the private class - `typing._UnionGenericAlias`. This class is no longer needed for the implementation, but it has been retained for backward compatibility, with removal scheduled for Python 3.17. Users should use documented introspection helpers like- `get_origin()`- `typing.get_args()`
- It is now possible to use - `typing.Union`- `isinstance()`- `isinstance(int | str, typing.Union)`will return- `True`; previously this raised- `TypeError`
- The - `__args__`attribute of- `typing.Union`
- It is no longer possible to set any attributes on - `Union`
 - (Contributed by Jelle Zijlstra in - [gh-105499](https://github.com/python/cpython/issues/105499).)
- `TypeAliasType`

### unicodedata[¶](#unicodedata)

- The Unicode database has been updated to Unicode 16.0.0. 

### unittest[¶](#unittest)

- `unittest`- [environment variables](../using/cmdline.html#using-on-controlling-color). (Contributed by Hugo van Kemenade in- [gh-127221](https://github.com/python/cpython/issues/127221).)
- unittest discovery supports - [namespace package](../glossary.html#term-namespace-package)as start directory again. It was removed in Python 3.11. (Contributed by Jacob Walls in- [gh-80958](https://github.com/python/cpython/issues/80958).)
- A number of new methods were added in the - `TestCase`- `assertHasAttr()`- `assertNotHasAttr()`
- `assertIsSubclass()`- `assertNotIsSubclass()`
- `assertStartsWith()`- `assertNotStartsWith()`- `assertEndsWith()`- `assertNotEndsWith()`
 - (Contributed by Serhiy Storchaka in - [gh-71339](https://github.com/python/cpython/issues/71339).)

### urllib[¶](#urllib)

- Upgrade HTTP digest authentication algorithm for - `urllib.request`- **RFC 7616**- [gh-128193](https://github.com/python/cpython/issues/128193).)
- Improve ergonomics and standards compliance when parsing and emitting - `file:`URLs.- In - `url2pathname()`- Accept a complete URL when the new - *require_scheme*argument is set to true.
- Discard URL authority if it matches the local hostname. 
- Discard URL authority if it resolves to a local IP address when the new - *resolve_host*argument is set to true.
- Discard URL query and fragment components. 
- Raise - `URLError`
 - In - `pathname2url()`- Return a complete URL when the new - *add_scheme*argument is set to true.
- Include an empty URL authority when a path begins with a slash. For example, the path - `/etc/hosts`is converted to the URL- `///etc/hosts`.
 - On Windows, drive letters are no longer converted to uppercase, and - `:`characters not following a drive letter no longer cause an- `OSError`- (Contributed by Barney Gale in - [gh-125866](https://github.com/python/cpython/issues/125866).)

### uuid[¶](#uuid)

- Add support for UUID versions 6, 7, and 8 via - `uuid6()`- `uuid7()`- `uuid8()`- **RFC 9562**- [gh-89083](https://github.com/python/cpython/issues/89083).)
- `NIL`- `MAX`- **RFC 9562**- [gh-128427](https://github.com/python/cpython/issues/128427).)
- Allow generating multiple UUIDs simultaneously on the command-line via - `python -m uuid --count`- [gh-131236](https://github.com/python/cpython/issues/131236).)

### webbrowser[¶](#webbrowser)

- Names in the - `BROWSER`environment variable can now refer to already registered browsers for the- `webbrowser`- This makes it possible to set - `BROWSER`to the value of one of the supported browsers on macOS.

### zipfile[¶](#zipfile)

- Added - `ZipInfo._for_archive`- `ZipInfo`- `ZipFile.writestr`- [gh-123424](https://github.com/python/cpython/issues/123424).)
- `ZipFile.writestr()`- `SOURCE_DATE_EPOCH`environment variable in order to better support reproducible builds. (Contributed by Jiahao Li in- [gh-91279](https://github.com/python/cpython/issues/91279).)

## Optimizations[¶](#optimizations)

- The import time for several standard library modules has been improved, including - `annotationlib`- `ast`- `asyncio`- `base64`- `cmd`- `csv`- `gettext`- `importlib.util`- `locale`- `mimetypes`- `optparse`- `pickle`- `pprint`- `pstats`- `shlex`- `socket`- `string`- `subprocess`- `threading`- `tomllib`- `types`- `zipfile`- (Contributed by Adam Turner, Bénédikt Tran, Chris Markiewicz, Eli Schwartz, Hugo van Kemenade, Jelle Zijlstra, and others in - [gh-118761](https://github.com/python/cpython/issues/118761).)
- The interpreter now avoids some reference count modifications internally when it’s safe to do so. This can lead to different values being returned from - `sys.getrefcount()`- `Py_REFCNT()`- [below](#whatsnew314-refcount)for details.

### asyncio[¶](#id2)

- Standard benchmark results have improved by 10-20% following the implementation of a new per-thread doubly linked list for - `native tasks`- [python -m asyncio pstree](#whatsnew314-asyncio-introspection)to introspect the call graph of asyncio tasks running in all threads. (Contributed by Kumar Aditya in- [gh-107803](https://github.com/python/cpython/issues/107803).)
- The module now has first class support for - [free-threading builds](../glossary.html#term-free-threading). This enables parallel execution of multiple event loops across different threads, scaling linearly with the number of threads. (Contributed by Kumar Aditya in- [gh-128002](https://github.com/python/cpython/issues/128002).)

### base64[¶](#base64)

- `b16decode()`- [gh-118761](https://github.com/python/cpython/issues/118761).)

### bdb[¶](#bdb)

- The basic debugger now has a - `sys.monitoring`- `'monitoring'`to the- `Bdb`- *backend*parameter. (Contributed by Tian Gao in- [gh-124533](https://github.com/python/cpython/issues/124533).)

### difflib[¶](#id3)

- The - `IS_LINE_JUNK()`- [gh-130167](https://github.com/python/cpython/issues/130167).)

### gc[¶](#gc)

- **From Python 3.14.5 onwards:**- Python 3.14.0-3.14.4 shipped with a new incremental garbage collector. However, due to a number of - [reports](https://github.com/python/cpython/issues/142516)of significant memory pressure in production environments, it has been reverted back to the generational GC from 3.13. This is the GC now used in Python 3.14.5 and later.
- **Previously in Python 3.14.0-3.14.4:**- The new - [incremental garbage collector](#whatsnew314-incremental-gc)means that maximum pause times are reduced by an order of magnitude or more for larger heaps.- Because of this optimization, the meaning of the results of - `get_threshold()`- `set_threshold()`- `get_count()`- `get_stats()`- For backwards compatibility, - `get_threshold()`
- `set_threshold()`
- `get_count()`- `get_stats()`
 - In summary, code that attempted to manipulate the behavior of the cycle GC may not work exactly as intended, but it is very unlikely to be harmful. All other code will work just fine. - (Contributed by Mark Shannon in - [gh-108362](https://github.com/python/cpython/issues/108362).)

### io[¶](#id4)

### pathlib[¶](#id5)

- `Path.read_bytes`- [gh-120754](https://github.com/python/cpython/issues/120754).)

### pdb[¶](#id6)

- `pdb`- `sys.settrace()`- `sys.monitoring`- [pdb CLI](../library/pdb.html#pdb-cli)or- `breakpoint()`- `sys.monitoring`backend. Explicitly instantiating- `pdb.Pdb`- `sys.settrace()`backend by default, which is configurable. (Contributed by Tian Gao in- [gh-124533](https://github.com/python/cpython/issues/124533).)

### textwrap[¶](#textwrap)

- Optimize the - `dedent()`

### uuid[¶](#id7)

### zlib[¶](#zlib)

- On Windows, - [zlib-ng](https://github.com/zlib-ng/zlib-ng)is now used as the implementation of the- `zlib`- `zlib-ng`and the previously-used- `zlib`implementation. This should result in better performance at all compression levels.- It is worth noting that - `zlib.Z_BEST_SPEED`(- `1`) may result in significantly less compression than the previous implementation, whilst also significantly reducing the time taken to compress.- (Contributed by Steve Dower in - [gh-91349](https://github.com/python/cpython/issues/91349).)

## Removed[¶](#removed)

### argparse[¶](#id8)

- Remove the - *type*,- *choices*, and- *metavar*parameters of- `BooleanOptionalAction`. These have been deprecated since Python 3.12. (Contributed by Nikita Sobolev in- [gh-118805](https://github.com/python/cpython/issues/118805).)
- Calling - `add_argument_group()`- `ValueError`- `add_argument_group()`or- `add_mutually_exclusive_group()`- `ValueError`s. This ‘nesting’ was never supported, often failed to work correctly, and was unintentionally exposed through inheritance. This functionality has been deprecated since Python 3.11. (Contributed by Savannah Ostrowski in- [gh-127186](https://github.com/python/cpython/issues/127186).)

### ast[¶](#id9)

- Remove the following classes, which have been deprecated aliases of - `Constant`- `Bytes`
- `Ellipsis`
- `NameConstant`
- `Num`
- `Str`
 - As a consequence of these removals, user-defined - `visit_Num`,- `visit_Str`,- `visit_Bytes`,- `visit_NameConstant`and- `visit_Ellipsis`methods on custom- `NodeVisitor`- `NodeVisitor`subclass is visiting an AST. Define a- `visit_Constant`method instead.- (Contributed by Alex Waygood in - [gh-119562](https://github.com/python/cpython/issues/119562).)
- Remove the following deprecated properties on - `ast.Constant`- `Constant.n`
- `Constant.s`
 - Use - `Constant.value`instead. (Contributed by Alex Waygood in- [gh-119562](https://github.com/python/cpython/issues/119562).)

### asyncio[¶](#id10)

- Remove the following classes, methods, and functions, which have been deprecated since Python 3.12: - `AbstractChildWatcher`
- `FastChildWatcher`
- `MultiLoopChildWatcher`
- `PidfdChildWatcher`
- `SafeChildWatcher`
- `ThreadedChildWatcher`
- `AbstractEventLoopPolicy.get_child_watcher()`
- `AbstractEventLoopPolicy.set_child_watcher()`
- `get_child_watcher()`
- `set_child_watcher()`
 - (Contributed by Kumar Aditya in - [gh-120804](https://github.com/python/cpython/issues/120804).)
- `asyncio.get_event_loop()`- `RuntimeError`- (Contributed by Kumar Aditya in - [gh-126353](https://github.com/python/cpython/issues/126353).)- There’s a few patterns that use - `asyncio.get_event_loop()`- `asyncio.run()`- If you’re running an async function, simply use - `asyncio.run()`- Before: - async def main(): ... loop = asyncio.get_event_loop() try: loop.run_until_complete(main()) finally: loop.close() - After: - async def main(): ... asyncio.run(main()) - If you need to start something, for example, a server listening on a socket and then run forever, use - `asyncio.run()`- `asyncio.Event`- Before: - def start_server(loop): ... loop = asyncio.get_event_loop() try: start_server(loop) loop.run_forever() finally: loop.close() - After: - def start_server(loop): ... async def main(): start_server(asyncio.get_running_loop()) await asyncio.Event().wait() asyncio.run(main()) - If you need to run something in an event loop, then run some blocking code around it, use - `asyncio.Runner`- Before: - async def operation_one(): ... def blocking_code(): ... async def operation_two(): ... loop = asyncio.get_event_loop() try: loop.run_until_complete(operation_one()) blocking_code() loop.run_until_complete(operation_two()) finally: loop.close() - After: - async def operation_one(): ... def blocking_code(): ... async def operation_two(): ... with asyncio.Runner() as runner: runner.run(operation_one()) blocking_code() runner.run(operation_two()) 

### email[¶](#email)

- Remove - `email.utils.localtime()`- *isdst*parameter, which was deprecated in and has been ignored since Python 3.12. (Contributed by Hugo van Kemenade in- [gh-118798](https://github.com/python/cpython/issues/118798).)

### importlib.abc[¶](#importlib-abc)

- Remove deprecated - `importlib.abc`- `ResourceReader`(use- `TraversableResources`
- `Traversable`(use- `Traversable`
- `TraversableResources`(use- `TraversableResources`
 - (Contributed by Jason R. Coombs and Hugo van Kemenade in - [gh-93963](https://github.com/python/cpython/issues/93963).)

### itertools[¶](#itertools)

- Remove support for copy, deepcopy, and pickle operations from - `itertools`- `DeprecationWarning`- [gh-101588](https://github.com/python/cpython/issues/101588).)

### pathlib[¶](#id11)

- Remove support for passing additional keyword arguments to - `Path`- [gh-74033](https://github.com/python/cpython/issues/74033).)
- Remove support for passing additional positional arguments to - `PurePath.relative_to()`- `is_relative_to()`- *other*. (Contributed by Barney Gale in- [gh-78707](https://github.com/python/cpython/issues/78707).)

### pkgutil[¶](#pkgutil)

- Remove the - `get_loader()`and- `find_loader()`functions, which have been deprecated since Python 3.12. (Contributed by Bénédikt Tran in- [gh-97850](https://github.com/python/cpython/issues/97850).)

### pty[¶](#pty)

- Remove the - `master_open()`and- `slave_open()`functions, which have been deprecated since Python 3.12. Use- `pty.openpty()`- [gh-118824](https://github.com/python/cpython/issues/118824).)

### sqlite3[¶](#sqlite3)

- Remove - `version`and- `version_info`from the- `sqlite3`- `sqlite_version`- `sqlite_version_info`- [gh-118924](https://github.com/python/cpython/issues/118924).)
- Using a sequence of parameters with named placeholders now raises a - `ProgrammingError`- [gh-118928](https://github.com/python/cpython/issues/118928)and- [gh-101693](https://github.com/python/cpython/issues/101693).)

### urllib[¶](#id12)

- Remove the - `Quoter`class from- `urllib.parse`- [gh-118827](https://github.com/python/cpython/issues/118827).)
- Remove the - `URLopener`and- `FancyURLopener`classes from- `urllib.request`- `myopener.open()`can be replaced with- `urlopen()`- `myopener.retrieve()`can be replaced with- `urlretrieve()`- `build_opener()`- [gh-84850](https://github.com/python/cpython/issues/84850).)

## Deprecated[¶](#deprecated)

### New deprecations[¶](#new-deprecations)

- Passing a complex number as the - *real*or- *imag*argument in the- `complex()`- [gh-109218](https://github.com/python/cpython/issues/109218).)
- 
- Passing the undocumented keyword argument - *prefix_chars*to the- `add_argument_group()`- [gh-125563](https://github.com/python/cpython/issues/125563).)
- Deprecated the - `argparse.FileType`- [gh-58032](https://github.com/python/cpython/issues/58032).)
 
- 
- The - `asyncio.iscoroutinefunction()`is now deprecated and will be removed in Python 3.16; use- `inspect.iscoroutinefunction()`- [gh-122875](https://github.com/python/cpython/issues/122875).)
- The - `asyncio`- Users should use - `asyncio.run()`- `asyncio.Runner`- *loop_factory*argument to use the desired event loop implementation.- For example, to use - `asyncio.SelectorEventLoop`- import asyncio async def main(): ... asyncio.run(main(), loop_factory=asyncio.SelectorEventLoop) - (Contributed by Kumar Aditya in - [gh-127949](https://github.com/python/cpython/issues/127949).)
 
- `codecs`- `codecs.open()`- `open()`- [gh-133036](https://github.com/python/cpython/issues/133036).)
- 
- On non-Windows platforms, setting - `Structure._pack_`- `Structure._layout_`- `'ms'`, and will be removed in Python 3.19. (Contributed by Petr Viktorin in- [gh-131747](https://github.com/python/cpython/issues/131747).)
- Calling - `ctypes.POINTER()`- [incomplete types](../library/ctypes.html#ctypes-incomplete-types)for self-referential structures. Also, the internal- `ctypes._pointer_type_cache`is deprecated. See- `ctypes.POINTER()`for updated implementation details. (Contributed by Sergey Myrianov in- [gh-100926](https://github.com/python/cpython/issues/100926).)
 
- `functools`- `functools.reduce()`- *function*or- *sequence*as keyword arguments is now deprecated; the parameters will be made positional-only in Python 3.16. (Contributed by Kirill Podoprigora in- [gh-121676](https://github.com/python/cpython/issues/121676).)
- `logging`- *strm*argument is now deprecated and scheduled for removal in Python 3.16. Define handlers with the- *stream*argument instead. (Contributed by Mariusz Felisiak in- [gh-115032](https://github.com/python/cpython/issues/115032).)
- `mimetypes`- `mimetypes.MimeTypes.add_type()`- `ValueError`- [gh-75223](https://github.com/python/cpython/issues/75223).)
- `nturl2path`: This module is now deprecated. Call- `urllib.request.url2pathname()`- `pathname2url()`- [gh-125866](https://github.com/python/cpython/issues/125866).)
- `os`- `os.popen()`- `os.spawn*`- [soft deprecated](../glossary.html#term-soft-deprecated). They should no longer be used to write new code. The- `subprocess`- [gh-120743](https://github.com/python/cpython/issues/120743).)
- `pathlib`- `pathlib.PurePath.as_uri()`is now deprecated and scheduled for removal in Python 3.19. Use- `pathlib.Path.as_uri()`- [gh-123599](https://github.com/python/cpython/issues/123599).)
- `pdb`- `pdb.Pdb.curframe_locals`attribute is now a deprecated read-only property, which will be removed in a future version of Python. The low overhead dynamic frame locals access added in Python 3.13 by- **PEP 667**- `pdb.Pdb.curframe.f_locals`directly in Python 3.13 and later versions. (Contributed by Tian Gao in- [gh-124369](https://github.com/python/cpython/issues/124369)and- [gh-125951](https://github.com/python/cpython/issues/125951).)
- `symtable`- `symtable.Class.get_methods()`- [gh-119698](https://github.com/python/cpython/issues/119698).)
- `tkinter`- `tkinter.Variable`methods- `trace_variable()`,- `trace_vdelete()`and- `trace_vinfo()`are now deprecated. Use- `trace_add()`,- `trace_remove()`and- `trace_info()`instead. (Contributed by Serhiy Storchaka in- [gh-120220](https://github.com/python/cpython/issues/120220).)
- `urllib.parse`- `0`and- `[]`) except empty strings, bytes-like objects and- `None`in- `parse_qsl()`- `parse_qs()`- [gh-116897](https://github.com/python/cpython/issues/116897).)

### Pending removal in Python 3.15[¶](#pending-removal-in-python-3-15)

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
 
- 
- `load_module()`- `exec_module()`- [gh-125746](https://github.com/python/cpython/issues/125746).)
 

### Pending removal in Python 3.16[¶](#pending-removal-in-python-3-16)

- The import system: - Setting - `__loader__`- `__spec__.loader`- `__loader__`will cease to be set or taken into consideration by the import system or the standard library.
 
- 
- The - `'u'`format code (- `wchar_t`) has been deprecated in documentation since Python 3.3 and at runtime since Python 3.13. Use the- `'w'`format code (- `Py_UCS4`
 
- 
- `asyncio.iscoroutinefunction()`is deprecated and will be removed in Python 3.16; use- `inspect.iscoroutinefunction()`- [gh-122875](https://github.com/python/cpython/issues/122875).)
- `asyncio`- Users should use - `asyncio.run()`- `asyncio.Runner`- *loop_factory*to use the desired event loop implementation.- For example, to use - `asyncio.SelectorEventLoop`- import asyncio async def main(): ... asyncio.run(main(), loop_factory=asyncio.SelectorEventLoop) - (Contributed by Kumar Aditya in - [gh-127949](https://github.com/python/cpython/issues/127949).)
 
- 
- Bitwise inversion on boolean types, - `~True`or- `~False`has been deprecated since Python 3.12, as it produces surprising and unintuitive results (- `-2`and- `-1`). Use- `not x`instead for the logical negation of a Boolean. In the rare case that you need the bitwise inversion of the underlying integer, convert to- `int`explicitly (- `~int(x)`).
 
- 
- Calling the Python implementation of - `functools.reduce()`- *function*or- *sequence*as keyword arguments has been deprecated since Python 3.14.
 
- 
Support for custom logging handlers with the *strm*argument is deprecated and scheduled for removal in Python 3.16. Define handlers with the*stream*argument instead. (Contributed by Mariusz Felisiak in[gh-115032](https://github.com/python/cpython/issues/115032).)
- 
- Valid extensions start with a ‘.’ or are empty for - `mimetypes.MimeTypes.add_type()`- `ValueError`- [gh-75223](https://github.com/python/cpython/issues/75223).)
 
- 
- The - `ExecError`exception has been deprecated since Python 3.14. It has not been used by any function in- `shutil`since Python 3.4, and is now an alias of- `RuntimeError`
 
- 
- The - `Class.get_methods`
 
- `sys`- The - `_enablelegacywindowsfsencoding()`- `PYTHONLEGACYWINDOWSFSENCODING`
 
- 
- The - `sysconfig.expand_makefile_vars()`function has been deprecated since Python 3.14. Use the- `vars`argument of- `sysconfig.get_paths()`
 
- 
- The undocumented and unused - `TarFile.tarfile`attribute has been deprecated since Python 3.13.
 

### Pending removal in Python 3.17[¶](#pending-removal-in-python-3-17)

- 
- `collections.abc.ByteString`- Use - `isinstance(obj, collections.abc.Buffer)`to test if- `obj`implements the- [buffer protocol](../c-api/buffer.html#bufferobjects)at runtime. For use in type annotations, either use- `Buffer`- `bytes | bytearray | memoryview`).- `ByteString`was originally intended to be an abstract class that would serve as a supertype of both- `bytes`- `bytearray`- `ByteString`never actually told you anything useful about the object. Other common buffer types such as- `memoryview`- `ByteString`(either at runtime or by static type checkers).- See - **PEP 688**- [gh-91896](https://github.com/python/cpython/issues/91896).)
 
- 
- Before Python 3.14, old-style unions were implemented using the private class - `typing._UnionGenericAlias`. This class is no longer needed for the implementation, but it has been retained for backward compatibility, with removal scheduled for Python 3.17. Users should use documented introspection helpers like- `typing.get_origin()`- `typing.get_args()`
- `typing.ByteString`- Use - `isinstance(obj, collections.abc.Buffer)`to test if- `obj`implements the- [buffer protocol](../c-api/buffer.html#bufferobjects)at runtime. For use in type annotations, either use- `Buffer`- `bytes | bytearray | memoryview`).- `ByteString`was originally intended to be an abstract class that would serve as a supertype of both- `bytes`- `bytearray`- `ByteString`never actually told you anything useful about the object. Other common buffer types such as- `memoryview`- `ByteString`(either at runtime or by static type checkers).- See - **PEP 688**- [gh-91896](https://github.com/python/cpython/issues/91896).)
 

### Pending removal in Python 3.18[¶](#pending-removal-in-python-3-18)

### Pending removal in Python 3.19[¶](#pending-removal-in-python-3-19)

### Pending removal in future versions[¶](#pending-removal-in-future-versions)

The following APIs will be removed in the future, although there is currently no date scheduled for their removal.

- 
- Nesting argument groups and nesting mutually exclusive groups are deprecated. 
- Passing the undocumented keyword argument - *prefix_chars*to- `add_argument_group()`
- The - `argparse.FileType`
 
- 
- Generators: - `throw(type, exc, tb)`and- `athrow(type, exc, tb)`signature is deprecated: use- `throw(exc)`and- `athrow(exc)`instead, the single argument signature.
- Currently Python accepts numeric literals immediately followed by keywords, for example - `0in x`,- `1or x`,- `0if 1else 2`. It allows confusing and ambiguous expressions like- `[0x1for x in y]`(which can be interpreted as- `[0x1 for x in y]`or- `[0x1f or x in y]`). A syntax warning is raised if the numeric literal is immediately followed by one of keywords- `and`- `else`- `for`- `if`- `in`- `is`- `or`- [gh-87999](https://github.com/python/cpython/issues/87999))
- Support for - `__index__()`and- `__int__()`method returning non-int type: these methods will be required to return an instance of a strict subclass of- `int`
- Support for - `__float__()`method returning a strict subclass of- `float`- `float`.
- Support for - `__complex__()`method returning a strict subclass of- `complex`- `complex`.
- Passing a complex number as the - *real*or- *imag*argument in the- `complex()`- [gh-109218](https://github.com/python/cpython/issues/109218).)
 
- `calendar`- `calendar.January`and- `calendar.February`constants are deprecated and replaced by- `calendar.JANUARY`- `calendar.FEBRUARY`- [gh-103636](https://github.com/python/cpython/issues/103636).)
- `codecs`- `open()`- `codecs.open()`- [gh-133038](https://github.com/python/cpython/issues/133038))
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
 
- The internal class - `typing._UnionGenericAlias`is no longer used to implement- `typing.Union`- [gh-105499](https://github.com/python/cpython/issues/105499).)
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
 
- `wsgiref`- `SimpleHandler.stdout.write()`should not do partial writes.
- `xml.etree.ElementTree`- `Element`- `True`. Prefer explicit- `len(elem)`or- `elem is not None`tests instead.
- `sys._clear_type_cache()`- `sys._clear_internal_caches()`

## CPython bytecode changes[¶](#cpython-bytecode-changes)

- Replaced the opcode - `BINARY_SUBSCR`by the- `BINARY_OP`- `NB_SUBSCR`oparg. (Contributed by Irit Katriel in- [gh-100239](https://github.com/python/cpython/issues/100239).)
- Add the - `BUILD_INTERPOLATION`- `BUILD_TEMPLATE`- `Interpolation`- `Template`- [gh-132661](https://github.com/python/cpython/issues/132661); see also- [PEP 750: Template strings](#whatsnew314-template-string-literals)).
- Remove the - `BUILD_CONST_KEY_MAP`opcode. Use- `BUILD_MAP`- [gh-122160](https://github.com/python/cpython/issues/122160).)
- Replace the - `LOAD_ASSERTION_ERROR`opcode with- `LOAD_COMMON_CONSTANT`- `NotImplementedError`
- Add the - `LOAD_FAST_BORROW`- `LOAD_FAST_BORROW_LOAD_FAST_BORROW`- [gh-130704](https://github.com/python/cpython/issues/130704).)
- Add the - `LOAD_SMALL_INT`- `oparg`to the stack. The- `RETURN_CONST`opcode is removed as it is no longer used. (Contributed by Mark Shannon in- [gh-125837](https://github.com/python/cpython/issues/125837).)
- Add the new - `LOAD_SPECIAL`- `with`- `async with`- `BEFORE_WITH`and- `BEFORE_ASYNC_WITH`instructions. (Contributed by Mark Shannon in- [gh-120507](https://github.com/python/cpython/issues/120507).)
- Add the - `POP_ITER`- [gh-132554](https://github.com/python/cpython/issues/132554).)

### Pseudo-instructions[¶](#pseudo-instructions)

- Add the - `ANNOTATIONS_PLACEHOLDER`pseudo instruction to support partially executed module-level annotations with- [deferred evaluation of annotations](#whatsnew314-deferred-annotations). (Contributed by Jelle Zijlstra in- [gh-130907](https://github.com/python/cpython/issues/130907).)
- Add the - `BINARY_OP_EXTEND`pseudo instruction, which executes a pair of functions (guard and specialization functions) accessed from the inline cache. (Contributed by Irit Katriel in- [gh-100239](https://github.com/python/cpython/issues/100239).)
- Add three specializations for - `CALL_KW`- `CALL_KW_PY`for calls to Python functions,- `CALL_KW_BOUND_METHOD`for calls to bound methods, and- `CALL_KW_NON_PY`for all other calls. (Contributed by Mark Shannon in- [gh-118093](https://github.com/python/cpython/issues/118093).)
- Add the - `JUMP_IF_TRUE`- `JUMP_IF_FALSE`- `COPY 1`,- `TO_BOOL`,- `POP_JUMP_IF_TRUE/FALSE`. (Contributed by Irit Katriel in- [gh-124285](https://github.com/python/cpython/issues/124285).)
- Add the - `LOAD_CONST_MORTAL`pseudo instruction. (Contributed by Mark Shannon in- [gh-128685](https://github.com/python/cpython/issues/128685).)
- Add the - `LOAD_CONST_IMMORTAL`- `LOAD_CONST`, but is more efficient for immortal objects. (Contributed by Mark Shannon in- [gh-125837](https://github.com/python/cpython/issues/125837).)
- Add the - `NOT_TAKEN`- `sys.monitoring`- `BRANCH_LEFT`- [gh-122548](https://github.com/python/cpython/issues/122548).)

## C API changes[¶](#c-api-changes)

### Python configuration C API[¶](#python-configuration-c-api)

Add a [PyInitConfig C API](../c-api/init_config.html#pyinitconfig-api) to configure the Python
initialization without relying on C structures and the ability to make
ABI-compatible changes in the future.

Complete the **PEP 587**[PyConfig C API](../c-api/init_config.html#pyconfig-api) by adding
[ PyInitConfig_AddModule()](../c-api/init_config.html#c.PyInitConfig_AddModule) which can be used to add a built-in extension
module; a feature previously referred to as the “inittab”.

Add [ PyConfig_Get()](../c-api/init_config.html#c.PyConfig_Get) and 

[functions to get and set the current runtime configuration.](../c-api/init_config.html#c.PyConfig_Set)

`PyConfig_Set()`[ PEP 587](https://peps.python.org/pep-0587/) ‘Python Initialization Configuration’ unified all the ways
to configure Python’s initialization. This PEP also unifies the configuration
of Python’s preinitialization and initialization in a single API.
Moreover, this PEP only provides a single choice to embed Python,
instead of having two ‘Python’ and ‘Isolated’ choices (PEP 587),
to further simplify the API.

The lower level PEP 587 PyConfig API remains available for use cases with an intentionally higher level of coupling to CPython implementation details (such as emulating the full functionality of CPython’s CLI, including its configuration mechanisms).

(Contributed by Victor Stinner in [gh-107954](https://github.com/python/cpython/issues/107954).)

### New features in the C API[¶](#new-features-in-the-c-api)

- Add - `Py_PACK_VERSION()`- `Py_PACK_FULL_VERSION()`- `Py_Version`- `PY_VERSION_HEX`- [gh-128629](https://github.com/python/cpython/issues/128629).)
- Add - `PyBytes_Join(sep, iterable)`- `sep.join(iterable)`in Python. (Contributed by Victor Stinner in- [gh-121645](https://github.com/python/cpython/issues/121645).)
- Add functions to manipulate the configuration of the current runtime Python interpreter ( - [PEP 741: Python configuration C API](#whatsnew314-capi-config)):- (Contributed by Victor Stinner in - [gh-107954](https://github.com/python/cpython/issues/107954).)
- Add functions to configure Python initialization ( - [PEP 741: Python configuration C API](#whatsnew314-capi-config)):- (Contributed by Victor Stinner in - [gh-107954](https://github.com/python/cpython/issues/107954).)
- Add - `Py_fopen()`- `fopen()`function, instead accepting a Python object for the- *path*parameter and setting an exception on error. The corresponding new- `Py_fclose()`- [gh-127350](https://github.com/python/cpython/issues/127350).)
- Add - `Py_HashBuffer()`- [gh-122854](https://github.com/python/cpython/issues/122854).)
- Add - `PyImport_ImportModuleAttr()`- `PyImport_ImportModuleAttrString()`- [gh-128911](https://github.com/python/cpython/issues/128911).)
- Add - `PyIter_NextItem()`- `PyIter_Next()`- [gh-105201](https://github.com/python/cpython/issues/105201).)
- Add - `PyLong_GetSign()`- `int`- [gh-116560](https://github.com/python/cpython/issues/116560).)
- Add - `PyLong_IsPositive()`- `PyLong_IsNegative()`- `PyLong_IsZero()`- `PyLongObject`- [gh-126061](https://github.com/python/cpython/issues/126061).)
- Add new functions to convert C - `<stdint.h>`numbers to/from Python- `int`- (Contributed by Victor Stinner in - [gh-120389](https://github.com/python/cpython/issues/120389).)
- Add a new import and export API for Python - `int`- **PEP 757**- (Contributed by Sergey B Kirpichev and Victor Stinner in - [gh-102471](https://github.com/python/cpython/issues/102471).)
- Add - `PyMonitoring_FireBranchLeftEvent()`- `PyMonitoring_FireBranchRightEvent()`- `BRANCH_LEFT`- `BRANCH_RIGHT`- [gh-122548](https://github.com/python/cpython/issues/122548).)
- Add - `PyType_Freeze()`- [gh-121654](https://github.com/python/cpython/issues/121654).)
- Add - `PyType_GetBaseByToken()`- `Py_tp_token`- **PEP 630**- [gh-124153](https://github.com/python/cpython/issues/124153).)
- Add a new - `PyUnicode_Equal()`- [gh-124502](https://github.com/python/cpython/issues/124502).)
- Add a new - `PyUnicodeWriter`- `str`- (Contributed by Victor Stinner in - [gh-119182](https://github.com/python/cpython/issues/119182).)
- The - `k`and- `K`formats in- `PyArg_ParseTuple()`- `__index__()`- [gh-112068](https://github.com/python/cpython/issues/112068).)
- Add support for a new - `p`format unit in- `Py_BuildValue()`- `bool`- [bpo-45325](https://bugs.python.org/issue?@action=redirect&bpo=45325).)
- Add - `PyUnstable_IsImmortal()`- [immortal](../glossary.html#term-immortal), for debugging purposes. (Contributed by Peter Bierma in- [gh-128509](https://github.com/python/cpython/issues/128509).)
- Add - `PyUnstable_Object_EnableDeferredRefcount()`- **PEP 703**
- Add - `PyUnstable_Object_IsUniquelyReferenced()`- `Py_REFCNT(op) == 1`on- [free threaded](../glossary.html#term-free-threading)builds. (Contributed by Peter Bierma in- [gh-133140](https://github.com/python/cpython/issues/133140).)
- Add - `PyUnstable_Object_IsUniqueReferencedTemporary()`- `Py_REFCNT()`- `1`for Python objects passed as arguments to C API functions. (Contributed by Sam Gross in- [gh-133164](https://github.com/python/cpython/issues/133164).)

### Limited C API changes[¶](#limited-c-api-changes)

- In the limited C API version 3.14 and newer, - `Py_TYPE()`- `Py_REFCNT()`- [gh-120600](https://github.com/python/cpython/issues/120600)and- [gh-124127](https://github.com/python/cpython/issues/124127).)
- Remove the - `PySequence_Fast_GET_SIZE`- `PySequence_Fast_GET_ITEM`- `PySequence_Fast_ITEMS`- [gh-91417](https://github.com/python/cpython/issues/91417).)

### Removed C APIs[¶](#removed-c-apis)

- Creating - `immutable types`- `TypeError`- [gh-119775](https://github.com/python/cpython/issues/119775).)
- Remove - `PyDictObject.ma_version_tag`member, which was deprecated in Python 3.12. Use the- `PyDict_AddWatcher()`- [gh-124296](https://github.com/python/cpython/issues/124296).)
- Remove the private - `_Py_InitializeMain()`function. It was a- [provisional API](../glossary.html#term-provisional-API)added to Python 3.8 by- **PEP 587**- [gh-129033](https://github.com/python/cpython/issues/129033).)
- Remove the undocumented APIs - `Py_C_RECURSION_LIMIT`and- `PyThreadState.c_recursion_remaining`. These were added in 3.13 and have been removed without deprecation. Use- `Py_EnterRecursiveCall()`- [gh-133079](https://github.com/python/cpython/issues/133079), see also- [gh-130396](https://github.com/python/cpython/issues/130396).)

### Deprecated C APIs[¶](#deprecated-c-apis)

- The - `Py_HUGE_VAL`macro is now- [soft deprecated](../glossary.html#term-soft-deprecated). Use- `Py_INFINITY`instead. (Contributed by Sergey B Kirpichev in- [gh-120026](https://github.com/python/cpython/issues/120026).)
- The - `Py_IS_NAN`,- `Py_IS_INFINITY`, and- `Py_IS_FINITE`macros are now- [soft deprecated](../glossary.html#term-soft-deprecated). Use- `isnan`,- `isinf`and- `isfinite`instead, available from- `math.h`since C99. (Contributed by Sergey B Kirpichev in- [gh-119613](https://github.com/python/cpython/issues/119613).)
- Non-tuple sequences are now deprecated as argument for the - `(items)`format unit in- `PyArg_ParseTuple()`- [argument parsing](../c-api/arg.html#arg-parsing)functions if- *items*contains format units which store a- [borrowed buffer](../c-api/arg.html#c-arg-borrowed-buffer)or a- [borrowed reference](../glossary.html#term-borrowed-reference). (Contributed by Serhiy Storchaka in- [gh-50333](https://github.com/python/cpython/issues/50333).)
- The - `_PyMonitoring_FireBranchEvent`function is now deprecated and should be replaced with calls to- `PyMonitoring_FireBranchLeftEvent()`- `PyMonitoring_FireBranchRightEvent()`
- The previously undocumented function - `PySequence_In()`- [soft deprecated](../glossary.html#term-soft-deprecated). Use- `PySequence_Contains()`- [gh-127896](https://github.com/python/cpython/issues/127896).)

#### Pending removal in Python 3.15[¶](#id13)

- The - `PyImport_ImportModuleNoBlock()`- `PyImport_ImportModule()`
- `PyWeakref_GetObject()`- `PyWeakref_GET_OBJECT()`- `PyWeakref_GetRef()`- [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/)can be used to get- `PyWeakref_GetRef()`on Python 3.12 and older.
- `Py_UNICODE`- `Py_UNICODE_WIDE`macro: Use- `wchar_t`instead.
- `PyUnicode_AsDecodedObject()`: Use- `PyCodec_Decode()`
- `PyUnicode_AsDecodedUnicode()`: Use- `PyCodec_Decode()`- `str`- `bytes`
- `PyUnicode_AsEncodedObject()`: Use- `PyCodec_Encode()`
- `PyUnicode_AsEncodedUnicode()`: Use- `PyCodec_Encode()`- `bytes`- `str`
- Python initialization functions, deprecated in Python 3.13: - `Py_GetPath()`- `PyConfig_Get("module_search_paths")`- `sys.path`
- `Py_GetPrefix()`- `PyConfig_Get("base_prefix")`- `sys.base_prefix`- `PyConfig_Get("prefix")`(- `sys.prefix`- [virtual environments](../library/venv.html#venv-def)need to be handled.
- `Py_GetExecPrefix()`- `PyConfig_Get("base_exec_prefix")`- `sys.base_exec_prefix`- `PyConfig_Get("exec_prefix")`(- `sys.exec_prefix`- [virtual environments](../library/venv.html#venv-def)need to be handled.
- `Py_GetProgramFullPath()`- `PyConfig_Get("executable")`- `sys.executable`
- `Py_GetProgramName()`- `PyConfig_Get("executable")`- `sys.executable`
- `Py_GetPythonHome()`- `PyConfig_Get("home")`- `PYTHONHOME`
 - The - [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/)can be used to get- `PyConfig_Get()`
- Functions to configure Python’s initialization, deprecated in Python 3.11: - `PySys_SetArgvEx()`: Set- `PyConfig.argv`
- `PySys_SetArgv()`: Set- `PyConfig.argv`
- `Py_SetProgramName()`: Set- `PyConfig.program_name`
- `Py_SetPythonHome()`: Set- `PyConfig.home`
- `PySys_ResetWarnOptions()`- `sys.warnoptions`- `warnings.filters`instead.
 - The - `Py_InitializeFromConfig()`- `PyConfig`
- Global configuration variables: - `Py_DebugFlag`- `PyConfig.parser_debug`- `PyConfig_Get("parser_debug")`
- `Py_VerboseFlag`- `PyConfig.verbose`- `PyConfig_Get("verbose")`
- `Py_QuietFlag`- `PyConfig.quiet`- `PyConfig_Get("quiet")`
- `Py_InteractiveFlag`- `PyConfig.interactive`- `PyConfig_Get("interactive")`
- `Py_InspectFlag`- `PyConfig.inspect`- `PyConfig_Get("inspect")`
- `Py_OptimizeFlag`- `PyConfig.optimization_level`- `PyConfig_Get("optimization_level")`
- `Py_NoSiteFlag`- `PyConfig.site_import`- `PyConfig_Get("site_import")`
- `Py_BytesWarningFlag`- `PyConfig.bytes_warning`- `PyConfig_Get("bytes_warning")`
- `Py_FrozenFlag`- `PyConfig.pathconfig_warnings`- `PyConfig_Get("pathconfig_warnings")`
- `Py_IgnoreEnvironmentFlag`- `PyConfig.use_environment`- `PyConfig_Get("use_environment")`
- `Py_DontWriteBytecodeFlag`- `PyConfig.write_bytecode`- `PyConfig_Get("write_bytecode")`
- `Py_NoUserSiteDirectory`- `PyConfig.user_site_directory`- `PyConfig_Get("user_site_directory")`
- `Py_UnbufferedStdioFlag`- `PyConfig.buffered_stdio`- `PyConfig_Get("buffered_stdio")`
- `Py_HashRandomizationFlag`- `PyConfig.use_hash_seed`- `PyConfig.hash_seed`- `PyConfig_Get("hash_seed")`
- `Py_IsolatedFlag`- `PyConfig.isolated`- `PyConfig_Get("isolated")`
- `Py_LegacyWindowsFSEncodingFlag`- `PyPreConfig.legacy_windows_fs_encoding`- `PyConfig_Get("legacy_windows_fs_encoding")`
- `Py_LegacyWindowsStdioFlag`- `PyConfig.legacy_windows_stdio`- `PyConfig_Get("legacy_windows_stdio")`
- `Py_FileSystemDefaultEncoding`,- `Py_HasFileSystemDefaultEncoding`: Use- `PyConfig.filesystem_encoding`- `PyConfig_Get("filesystem_encoding")`
- `Py_FileSystemDefaultEncodeErrors`: Use- `PyConfig.filesystem_errors`- `PyConfig_Get("filesystem_errors")`
- `Py_UTF8Mode`: Use- `PyPreConfig.utf8_mode`- `PyConfig_Get("utf8_mode")`- `Py_PreInitialize()`
 - The - `Py_InitializeFromConfig()`- `PyConfig`- `PyConfig_Get()`

#### Pending removal in Python 3.16[¶](#id14)

- The bundled copy of - `libmpdec`.

#### Pending removal in Python 3.18[¶](#id15)

- The following private functions are deprecated and planned for removal in Python 3.18: - `_PyBytes_Join()`: use- `PyBytes_Join()`
- `_PyDict_GetItemStringWithError()`: use- `PyDict_GetItemStringRef()`
- `_PyDict_Pop()`: use- `PyDict_Pop()`
- `_PyLong_Sign()`: use- `PyLong_GetSign()`
- `_PyLong_FromDigits()`and- `_PyLong_New()`: use- `PyLongWriter_Create()`
- `_PyThreadState_UncheckedGet()`: use- `PyThreadState_GetUnchecked()`
- `_PyUnicode_AsString()`: use- `PyUnicode_AsUTF8()`
- `_PyUnicodeWriter_Init()`: replace- `_PyUnicodeWriter_Init(&writer)`with- `writer = PyUnicodeWriter_Create(0)`
- `_PyUnicodeWriter_Finish()`: replace- `_PyUnicodeWriter_Finish(&writer)`with- `PyUnicodeWriter_Finish(writer)`
- `_PyUnicodeWriter_Dealloc()`: replace- `_PyUnicodeWriter_Dealloc(&writer)`with- `PyUnicodeWriter_Discard(writer)`
- `_PyUnicodeWriter_WriteChar()`: replace- `_PyUnicodeWriter_WriteChar(&writer, ch)`with- `PyUnicodeWriter_WriteChar(writer, ch)`
- `_PyUnicodeWriter_WriteStr()`: replace- `_PyUnicodeWriter_WriteStr(&writer, str)`with- `PyUnicodeWriter_WriteStr(writer, str)`
- `_PyUnicodeWriter_WriteSubstring()`: replace- `_PyUnicodeWriter_WriteSubstring(&writer, str, start, end)`with- `PyUnicodeWriter_WriteSubstring(writer, str, start, end)`
- `_PyUnicodeWriter_WriteASCIIString()`: replace- `_PyUnicodeWriter_WriteASCIIString(&writer, str)`with- `PyUnicodeWriter_WriteASCII(writer, str)`
- `_PyUnicodeWriter_WriteLatin1String()`: replace- `_PyUnicodeWriter_WriteLatin1String(&writer, str)`with- `PyUnicodeWriter_WriteUTF8(writer, str)`
- `_PyUnicodeWriter_Prepare()`: (no replacement).
- `_PyUnicodeWriter_PrepareKind()`: (no replacement).
- `_Py_HashPointer()`: use- `Py_HashPointer()`
- `_Py_fopen_obj()`: use- `Py_fopen()`
 - The - [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/)can be used to get these new public functions on Python 3.13 and older. (Contributed by Victor Stinner in- [gh-128863](https://github.com/python/cpython/issues/128863).)

#### Pending removal in future versions[¶](#id16)

The following APIs are deprecated and will be removed, although there is currently no date scheduled for their removal.

- `Py_TPFLAGS_HAVE_FINALIZE`
- `PyErr_Fetch()`- `PyErr_GetRaisedException()`
- `PyErr_NormalizeException()`- `PyErr_GetRaisedException()`
- `PyErr_Restore()`- `PyErr_SetRaisedException()`
- `PyModule_GetFilename()`- `PyModule_GetFilenameObject()`
- `PyOS_AfterFork()`- `PyOS_AfterFork_Child()`
- `PySlice_GetIndicesEx()`- `PySlice_Unpack()`- `PySlice_AdjustIndices()`
- `PyUnicode_READY()`
- `PyErr_Display()`: Use- `PyErr_DisplayException()`
- `_PyErr_ChainExceptions()`: Use- `_PyErr_ChainExceptions1()`instead.
- `PyBytesObject.ob_shash`member: call- `PyObject_Hash()`
- Thread Local Storage (TLS) API: - `PyThread_create_key()`- `PyThread_tss_alloc()`
- `PyThread_delete_key()`- `PyThread_tss_free()`
- `PyThread_set_key_value()`- `PyThread_tss_set()`
- `PyThread_get_key_value()`- `PyThread_tss_get()`
- `PyThread_delete_key_value()`- `PyThread_tss_delete()`
- `PyThread_ReInitTLS()`
 

## Build changes[¶](#build-changes)

- **PEP 776**- **tier 3**- [Emscripten libc](https://emscripten.org/docs/porting/emscripten-runtime-environment.html)were fixed. Emscripten now includes support for- `ctypes`- `termios`- `fcntl`- [default interactive shell](../tutorial/interpreter.html#tut-interactive). (Contributed by R. Hood Chatham in- [gh-127146](https://github.com/python/cpython/issues/127146),- [gh-127683](https://github.com/python/cpython/issues/127683), and- [gh-136931](https://github.com/python/cpython/issues/136931).)
- Official Android binary releases are now provided on - [python.org](https://www.python.org/downloads/android/).
- GNU Autoconf 2.72 is now required to generate - `configure`. (Contributed by Erlend Aasland in- [gh-115765](https://github.com/python/cpython/issues/115765).)
- `wasm32-unknown-emscripten`is now a- **PEP 11**- [gh-127146](https://github.com/python/cpython/issues/127146),- [gh-127683](https://github.com/python/cpython/issues/127683), and- [gh-136931](https://github.com/python/cpython/issues/136931).)
- `#pragma`-based linking with- `python3*.lib`can now be switched off with- [Py_NO_LINK_LIB](../extending/windows.html#c.Py_NO_LINK_LIB). (Contributed by Jean-Christophe Fillion-Robin in- [gh-82909](https://github.com/python/cpython/issues/82909).)
- CPython now enables a set of recommended compiler options by default for improved security. Use the - `--disable-safety`- `configure`option to disable them, or the- `--enable-slower-safety`
- The - `WITH_FREELISTS`macro and- `--without-freelists`- `configure`option have been removed.
- The new - `configure`option- `--with-tail-call-interp`- [A new type of interpreter](#whatsnew314-tail-call-interpreter)for further details.
- To disable the new remote debugging support, use the - `--without-remote-debug`- `configure`option. This may be useful for security reasons.
- iOS and macOS apps can now be configured to redirect - `stdout`and- `stderr`content to the system log. (Contributed by Russell Keith-Magee in- [gh-127592](https://github.com/python/cpython/issues/127592).)
- The iOS testbed is now able to stream test output while the test is running. The testbed can also be used to run the test suite of projects other than CPython itself. (Contributed by Russell Keith-Magee in - [gh-127592](https://github.com/python/cpython/issues/127592).)

`build-details.json`[¶](#build-details-json)

Installations of Python now contain a new file, `build-details.json`.
This is a static JSON document containing build details for CPython,
to allow for introspection without needing to run code.
This is helpful for use-cases such as Python launchers, cross-compilation,
and so on.

`build-details.json` must be installed in the platform-independent
standard library directory. This corresponds to the [‘stdlib’](../library/sysconfig.html#installation-paths) [ sysconfig](../library/sysconfig.html#module-sysconfig) installation path,
which can be found by running 

`sysconfig.get_path('stdlib')`.See also

[ PEP 739](https://peps.python.org/pep-0739/) – 

`build-details.json` 1.0 – a static description file
for Python build details### Discontinuation of PGP signatures[¶](#discontinuation-of-pgp-signatures)

PGP (Pretty Good Privacy) signatures will not be provided
for releases of Python 3.14 or future versions.
To verify CPython artifacts, users must use [Sigstore verification materials](https://www.python.org/downloads/metadata/sigstore/).
Releases have been signed using [Sigstore](https://www.sigstore.dev/) since Python 3.11.

This change in release process was specified in [ PEP 761](https://peps.python.org/pep-0761/).

### Free-threaded Python is officially supported[¶](#free-threaded-python-is-officially-supported)

The free-threaded build of Python is now supported and no longer experimental.
This is the start of [phase II](https://discuss.python.org/t/37075) where
free-threaded Python is officially supported but still optional.

The free-threading team are confident that the project is on the right path, and appreciate the continued dedication from everyone working to make free-threading ready for broader adoption across the Python community.

With these recommendations and the acceptance of this PEP, the Python developer community should broadly advertise that free-threading is a supported Python build option now and into the future, and that it will not be removed without a proper deprecation schedule.

Any decision to transition to [phase III](https://discuss.python.org/t/37075),
with free-threading as the default or sole build of Python is still undecided,
and dependent on many factors both within CPython itself and the community.
This decision is for the future.

### Binary releases for the experimental just-in-time compiler[¶](#binary-releases-for-the-experimental-just-in-time-compiler)

The official macOS and Windows release binaries now include an *experimental*
just-in-time (JIT) compiler. Although it is **not** recommended for production
use, it can be tested by setting [ PYTHON_JIT=1](../using/cmdline.html#envvar-PYTHON_JIT) as an
environment variable. Downstream source builds and redistributors can use the

[configuration option for similar behavior.](../using/configure.html#cmdoption-enable-experimental-jit)

`--enable-experimental-jit=yes-off`The JIT is at an early stage and still in active development. As such, the
typical performance impact of enabling it can range from 10% slower to 20%
faster, depending on workload. To aid in testing and evaluation, a set of
introspection functions has been provided in the [ sys._jit](../library/sys.html#sys._jit) namespace.

[can be used to determine if the current executable supports JIT compilation, while](../library/sys.html#sys._jit.is_available)

`sys._jit.is_available()`[can be used to tell if JIT compilation has been enabled for the current process.](../library/sys.html#sys._jit.is_enabled)

`sys._jit.is_enabled()`Currently, the most significant missing functionality is that native debuggers
and profilers like `gdb` and `perf` are unable to unwind through JIT frames
(Python debuggers and profilers, like [ pdb](../library/pdb.html#module-pdb) or 

[, continue to work without modification). Free-threaded builds do not support JIT compilation.](../library/profile.html#module-profile)

`profile`Please report any bugs or major performance regressions that you encounter!

See also

## Porting to Python 3.14[¶](#porting-to-python-3-14)

This section lists previously described changes and other bugfixes that may require changes to your code.

### Changes in the Python API[¶](#changes-in-the-python-api)

- On Unix platforms other than macOS, - *forkserver*is now the default- [start method](../library/multiprocessing.html#multiprocessing-start-methods)for- `multiprocessing`- `ProcessPoolExecutor`- *fork*.- If you encounter - `NameError`- `multiprocessing`- `concurrent.futures`- [forkserver restrictions](../library/multiprocessing.html#multiprocessing-programming-forkserver).- This change does not affect Windows or macOS, where - [‘spawn’](../library/multiprocessing.html#multiprocessing-start-method-spawn)remains the default start method.
- `functools.partial`- `staticmethod()`- [gh-121027](https://github.com/python/cpython/issues/121027).)
- The - [garbage collector is now incremental](#whatsnew314-incremental-gc), which means that the behavior of- `gc.collect()`- `gc.collect(1)`: Performs an increment of garbage collection, rather than collecting generation 1.
- Other calls to - `gc.collect()`are unchanged.
 
- The - `locale.nl_langinfo()`- `LC_CTYPE`locale in some cases. This temporary change affects other threads. (Contributed by Serhiy Storchaka in- [gh-69998](https://github.com/python/cpython/issues/69998).)
- `types.UnionType`- `typing.Union`- [above](#whatsnew314-typing-union)for more details. (Contributed by Jelle Zijlstra in- [gh-105499](https://github.com/python/cpython/issues/105499).)
- The runtime behavior of annotations has changed in various ways; see - [above](#whatsnew314-deferred-annotations)for details. While most code that interacts with annotations should continue to work, some undocumented details may behave differently.
- As part of making the - `mimetypes`- `1`on failure instead of- `0`and- `2`on incorrect command-line parameters instead of- `1`. Error messages are now printed to stderr.
- The - `\B`pattern in regular expression now matches the empty string when given as the entire pattern, which may cause behavioural changes.
- On FreeBSD, - `sys.platform`

### Changes in annotations (**PEP 649****PEP 749**[¶](#changes-in-annotations-pep-649-and-pep-749)

**PEP 649**

**PEP 749**

This section contains guidance on changes that may be needed to annotations
or Python code that interacts with or introspects annotations,
due to the changes related to [deferred evaluation of annotations](#whatsnew314-deferred-annotations).

In the majority of cases, working code from older versions of Python will not require any changes.

#### Implications for annotated code[¶](#implications-for-annotated-code)

If you define annotations in your code (for example, for use with a static type checker), then this change probably does not affect you: you can keep writing annotations the same way you did with previous versions of Python.

You will likely be able to remove quoted strings in annotations, which are frequently
used for forward references. Similarly, if you use `from __future__ import annotations`
to avoid having to write strings in annotations, you may well be able to
remove that import once you support only Python 3.14 and newer.
However, if you rely on third-party libraries that read annotations,
those libraries may need changes to support unquoted annotations before they
work as expected.

#### Implications for readers of `__annotations__`[¶](#implications-for-readers-of-annotations)

If your code reads the [ __annotations__](../reference/datamodel.html#object.__annotations__) attribute on objects,
you may want to make changes in order to support code that relies on
deferred evaluation of annotations.
For example, you may want to use 

[with the](../library/annotationlib.html#annotationlib.get_annotations)

`annotationlib.get_annotations()`[format, as the](../library/annotationlib.html#annotationlib.Format.FORWARDREF)

`FORWARDREF`[module now does.](../library/dataclasses.html#module-dataclasses)

`dataclasses`The external [typing_extensions](https://pypi.org/project/typing_extensions/) package provides partial backports
of some of the functionality of the [ annotationlib](../library/annotationlib.html#module-annotationlib) module,
such as the 

[enum and the](../library/annotationlib.html#annotationlib.Format)

`Format`[function. These can be used to write cross-version code that takes advantage of the new behavior in Python 3.14.](../library/annotationlib.html#annotationlib.get_annotations)

`get_annotations()``from __future__ import annotations`[¶](#from-future-import-annotations)

In Python 3.7, [ PEP 563](https://peps.python.org/pep-0563/) introduced the 

`from __future__ import annotations`
[future statement](../reference/simple_stmts.html#future), which turns all annotations into strings.

However, this statement is now deprecated and it is expected to be removed in a future version of Python. This removal will not happen until after Python 3.13 reaches its end of life in 2029, being the last version of Python without support for deferred evaluation of annotations.

In Python 3.14, the behavior of code using `from __future__ import annotations`
is unchanged.

### Changes in the C API[¶](#changes-in-the-c-api)

- `Py_Finalize()`- `Py_Finalize()`and is then reused after a call to- `Py_Initialize()`- `Py_Initialize()`from accessing uninitialized memory. To fix, use an address sanitizer to identify any use-after-free coming from an interned string and deallocate it during module shutdown. (Contributed by Eddie Elizondo in- [gh-113601](https://github.com/python/cpython/issues/113601).)
- The - [Unicode Exception Objects](../c-api/exceptions.html#unicodeexceptions)C API now raises a- `TypeError`- `UnicodeError`- [gh-127691](https://github.com/python/cpython/issues/127691).)

- The interpreter internally avoids some reference count modifications when loading objects onto the operands stack by - [borrowing](../glossary.html#term-borrowed-reference)references when possible. This can lead to smaller reference count values compared to previous Python versions. C API extensions that checked- `Py_REFCNT()`- `1`to determine if an function argument is not referenced by any other code should instead use- `PyUnstable_Object_IsUniqueReferencedTemporary()`
- Private functions promoted to public C APIs: - `_PyBytes_Join()`:- `PyBytes_Join()`
- `_PyLong_IsNegative()`:- `PyLong_IsNegative()`
- `_PyLong_IsPositive()`:- `PyLong_IsPositive()`
- `_PyLong_IsZero()`:- `PyLong_IsZero()`
- `_PyLong_Sign()`:- `PyLong_GetSign()`
- `_PyUnicodeWriter_Dealloc()`:- `PyUnicodeWriter_Discard()`
- `_PyUnicodeWriter_Finish()`:- `PyUnicodeWriter_Finish()`
- `_PyUnicodeWriter_Init()`: use- `PyUnicodeWriter_Create()`
- `_PyUnicodeWriter_Prepare()`: (no replacement)
- `_PyUnicodeWriter_PrepareKind()`: (no replacement)
- `_PyUnicodeWriter_WriteChar()`:- `PyUnicodeWriter_WriteChar()`
- `_PyUnicodeWriter_WriteStr()`:- `PyUnicodeWriter_WriteStr()`
- `_PyUnicodeWriter_WriteSubstring()`:- `PyUnicodeWriter_WriteSubstring()`
- `_PyUnicode_EQ()`:- `PyUnicode_Equal()`
- `_PyUnicode_Equal()`:- `PyUnicode_Equal()`
- `_Py_GetConfig()`:- `PyConfig_Get()`- `PyConfig_GetInt()`
- `_Py_HashBytes()`:- `Py_HashBuffer()`
- `_Py_fopen_obj()`:- `Py_fopen()`
- `PyMutex_IsLocked()`:- `PyMutex_IsLocked()`
 - The - [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/)can be used to get most of these new functions on Python 3.13 and older.

## Notable changes in 3.14.1[¶](#notable-changes-in-3-14-1)

- Add - `PyUnstable_ThreadState_SetStackProtection()`- `PyUnstable_ThreadState_ResetStackProtection()`- [gh-139653](https://github.com/python/cpython/issues/139653).)

## Notable changes in 3.14.5[¶](#notable-changes-in-3-14-5)

### gc[¶](#id19)

- The incremental garbage collector shipped in Python 3.14.0-3.14.4 has been reverted back to the generational garbage collector from 3.13, due to a number of - [reports](https://github.com/python/cpython/issues/142516)of significant memory pressure in production environments. See- [Garbage collection](#whatsnew314-incremental-gc)for details.