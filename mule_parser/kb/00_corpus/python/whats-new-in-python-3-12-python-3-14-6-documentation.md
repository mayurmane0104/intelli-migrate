# What’s New In Python 3.12 — Python 3.14.6 documentation

**Source:** [https://docs.python.org/whatsnew/3.12.html](https://docs.python.org/whatsnew/3.12.html)

---

# What’s New In Python 3.12[¶](#what-s-new-in-python-3-12)

- Editor:
- Adam Turner 

This article explains the new features in Python 3.12, compared to 3.11.
Python 3.12 was released on October 2, 2023.
For full details, see the [changelog](changelog.html#changelog).

See also

[ PEP 693](https://peps.python.org/pep-0693/) – Python 3.12 Release Schedule

## Summary – Release highlights[¶](#summary-release-highlights)

Python 3.12 is a stable release of the Python programming language,
with a mix of changes to the language and the standard library.
The library changes focus on cleaning up deprecated APIs, usability, and correctness.
Of note, the `distutils` package has been removed from the standard library.
Filesystem support in [ os](../library/os.html#module-os) and 

[has seen a number of improvements, and several modules have better performance.](../library/pathlib.html#module-pathlib)

`pathlib`The language changes focus on usability,
as [f-strings](../glossary.html#term-f-string) have had many limitations removed
and ‘Did you mean …’ suggestions continue to improve.
The new [type parameter syntax](#whatsnew312-pep695)
and [ type](../reference/simple_stmts.html#type) statement improve ergonomics for using 

[generic types](../glossary.html#term-generic-type)and

[type aliases](../glossary.html#term-type-alias)with static type checkers.

This article doesn’t attempt to provide a complete specification of all new features,
but instead gives a convenient overview.
For full details, you should refer to the documentation,
such as the  [Library Reference](../library/index.html#library-index)
and [Language Reference](../reference/index.html#reference-index).
If you want to understand the complete implementation and design rationale for a change,
refer to the PEP for a particular new feature;
but note that PEPs usually are not kept up-to-date
once a feature has been fully implemented.

New syntax features:

New grammar features:

Interpreter improvements:

- [PEP 669](#whatsnew312-pep669), low impact monitoring
- [Improved ‘Did you mean …’ suggestions](#improved-error-messages)for- `NameError`- `ImportError`- `SyntaxError`

Python data model improvements:

- [PEP 688](#whatsnew312-pep688), using the- [buffer protocol](../c-api/buffer.html#bufferobjects)from Python

Significant improvements in the standard library:

- The - `pathlib.Path`
- The - `os`
- A - [command-line interface](../library/sqlite3.html#sqlite3-cli)has been added to the- `sqlite3`
- `isinstance()`- `runtime-checkable protocols`
- The - `asyncio`
- A - [command-line interface](../library/uuid.html#uuid-cli)has been added to the- `uuid`
- Due to the changes in - [PEP 701](#whatsnew312-pep701), producing tokens via the- `tokenize`

Security improvements:

- Replace the builtin - `hashlib`- [HACL*](https://github.com/hacl-star/hacl-star/)project. These builtin implementations remain as fallbacks that are only used when OpenSSL does not provide them.

C API improvements:

CPython implementation improvements:

- [PEP 709](#whatsnew312-pep709), comprehension inlining
- [CPython support](../howto/perf_profiling.html#perf-profiling)for the Linux- `perf`profiler
- Implement stack overflow protection on supported platforms 

New typing features:

- [PEP 698](#whatsnew312-pep698),- `typing.override()`

Important deprecations, removals or restrictions:

- **PEP 623**- `wstr`from Unicode objects in Python’s C API, reducing the size of every- `str`
- **PEP 632**- `distutils`package. See- **the migration guide**- [Setuptools](https://setuptools.pypa.io/en/latest/deprecated/distutils-legacy.html)package continues to provide- `distutils`, if you still require it in Python 3.12 and beyond.
- [gh-95299](https://github.com/python/cpython/issues/95299): Do not pre-install- `setuptools`in virtual environments created with- `venv`- `distutils`,- `setuptools`,- `pkg_resources`, and- `easy_install`will no longer available by default; to access these run- `pip install setuptools`in the- [activated](../library/venv.html#venv-explanation)virtual environment.
- The - `asynchat`,- `asyncore`, and- `imp`modules have been removed, along with several- `unittest.TestCase`- [method aliases](#unittest-testcase-removed-aliases).

## New Features[¶](#new-features)

### PEP 695: Type Parameter Syntax[¶](#pep-695-type-parameter-syntax)

Generic classes and functions under [ PEP 484](https://peps.python.org/pep-0484/) were declared using a verbose syntax
that left the scope of type parameters unclear and required explicit declarations of
variance.

[ PEP 695](https://peps.python.org/pep-0695/) introduces a new, more compact and explicit way to create

[generic classes](../reference/compound_stmts.html#generic-classes)and

[functions](../reference/compound_stmts.html#generic-functions):

```
def max[T](args: Iterable[T]) -> T:
    ...
class list[T]:
    def __getitem__(self, index: int, /) -> T:
        ...
    def append(self, element: T) -> None:
        ...
```
In addition, the PEP introduces a new way to declare [type aliases](../library/typing.html#type-aliases)
using the [ type](../reference/simple_stmts.html#type) statement, which creates an instance of

[:](../library/typing.html#typing.TypeAliasType)

`TypeAliasType````
type Point = tuple[float, float]
```
Type aliases can also be [generic](../reference/compound_stmts.html#generic-type-aliases):

```
type Point[T] = tuple[T, T]
```
The new syntax allows declaring [ TypeVarTuple](../library/typing.html#typing.TypeVarTuple)
and 

[parameters, as well as](../library/typing.html#typing.ParamSpec)

`ParamSpec`[parameters with bounds or constraints:](../library/typing.html#typing.TypeVar)

`TypeVar````
type IntFunc[**P] = Callable[P, int]  # ParamSpec
type LabeledTuple[*Ts] = tuple[str, *Ts]  # TypeVarTuple
type HashableSequence[T: Hashable] = Sequence[T]  # TypeVar with bound
type IntOrStrSequence[T: (int, str)] = Sequence[T]  # TypeVar with constraints
```
The value of type aliases and the bound and constraints of type variables
created through this syntax are evaluated only on demand (see
[lazy evaluation](../reference/executionmodel.html#lazy-evaluation)). This means type aliases are able to
refer to other types defined later in the file.

Type parameters declared through a type parameter list are visible within the
scope of the declaration and any nested scopes, but not in the outer scope. For
example, they can be used in the type annotations for the methods of a generic
class or in the class body. However, they cannot be used in the module scope after
the class is defined. See [Type parameter lists](../reference/compound_stmts.html#type-params) for a detailed description of the
runtime semantics of type parameters.

In order to support these scoping semantics, a new kind of scope is introduced,
the [annotation scope](../reference/executionmodel.html#annotation-scopes). Annotation scopes behave for the
most part like function scopes, but interact differently with enclosing class scopes.
In Python 3.13, [annotations](../glossary.html#term-annotation) will also be evaluated in
annotation scopes.

See [ PEP 695](https://peps.python.org/pep-0695/) for more details.

(PEP written by Eric Traut. Implementation by Jelle Zijlstra, Eric Traut,
and others in [gh-103764](https://github.com/python/cpython/issues/103764).)

### PEP 701: Syntactic formalization of f-strings[¶](#pep-701-syntactic-formalization-of-f-strings)

[ PEP 701](https://peps.python.org/pep-0701/) lifts some restrictions on the usage of 

[f-strings](../glossary.html#term-f-string). Expression components inside f-strings can now be any valid Python expression, including strings reusing the same quote as the containing f-string, multi-line expressions, comments, backslashes, and unicode escape sequences. Let’s cover these in detail:

- Quote reuse: in Python 3.11, reusing the same quotes as the enclosing f-string raises a - `SyntaxError`- >>> songs = ['Take me back to Eden', 'Alkaline', 'Ascensionism'] >>> f"This is the playlist: {", ".join(songs)}" 'This is the playlist: Take me back to Eden, Alkaline, Ascensionism' - Note that before this change there was no explicit limit in how f-strings can be nested, but the fact that string quotes cannot be reused inside the expression component of f-strings made it impossible to nest f-strings arbitrarily. In fact, this is the most nested f-string that could be written: - >>> f"""{f'''{f'{f"{1+1}"}'}'''}""" '2' - As now f-strings can contain any valid Python expression inside expression components, it is now possible to nest f-strings arbitrarily: - >>> f"{f"{f"{f"{f"{f"{1+1}"}"}"}"}"}" '2' 
- Multi-line expressions and comments: In Python 3.11, f-string expressions must be defined in a single line, even if the expression within the f-string could normally span multiple lines (like literal lists being defined over multiple lines), making them harder to read. In Python 3.12 you can now define f-strings spanning multiple lines, and add inline comments: - `>>> f"This is the playlist: {", ".join([ ... 'Take me back to Eden', # My, my, those eyes like fire ... 'Alkaline', # Not acid nor alkaline ... 'Ascensionism' # Take to the broken skies at last ... ])}" 'This is the playlist: Take me back to Eden, Alkaline, Ascensionism'`
- Backslashes and unicode characters: before Python 3.12 f-string expressions couldn’t contain any - `\`character. This also affected unicode- [escape sequences](../reference/lexical_analysis.html#escape-sequences)(such as- `\N{snowman}`) as these contain the- `\N`part that previously could not be part of expression components of f-strings. Now, you can define expressions like this:- >>> print(f"This is the playlist: {"\n".join(songs)}") This is the playlist: Take me back to Eden Alkaline Ascensionism >>> print(f"This is the playlist: {"\N{BLACK HEART SUIT}".join(songs)}") This is the playlist: Take me back to Eden♥Alkaline♥Ascensionism 

See [ PEP 701](https://peps.python.org/pep-0701/) for more details.

As a positive side-effect of how this feature has been implemented (by parsing f-strings
with [ the PEG parser](https://peps.python.org/pep-0617/)), now error messages for f-strings are more precise
and include the exact location of the error. For example, in Python 3.11, the following
f-string raises a 

[:](../library/exceptions.html#SyntaxError)

`SyntaxError````
>>> my_string = f"{x z y}" + f"{1 + 1}"
  File "<stdin>", line 1
    (x z y)
     ^^^
SyntaxError: f-string: invalid syntax. Perhaps you forgot a comma?
```
but the error message doesn’t include the exact location of the error within the line and also has the expression artificially surrounded by parentheses. In Python 3.12, as f-strings are parsed with the PEG parser, error messages can be more precise and show the entire line:

```
>>> my_string = f"{x z y}" + f"{1 + 1}"
  File "<stdin>", line 1
    my_string = f"{x z y}" + f"{1 + 1}"
                   ^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
```
(Contributed by Pablo Galindo, Batuhan Taskaya, Lysandros Nikolaou, Cristián
Maureira-Fredes and Marta Gómez in [gh-102856](https://github.com/python/cpython/issues/102856). PEP written by Pablo Galindo,
Batuhan Taskaya, Lysandros Nikolaou and Marta Gómez).

### PEP 684: A Per-Interpreter GIL[¶](#pep-684-a-per-interpreter-gil)

[ PEP 684](https://peps.python.org/pep-0684/) introduces a per-interpreter 

[GIL](../glossary.html#term-global-interpreter-lock), so that sub-interpreters may now be created with a unique GIL per interpreter. This allows Python programs to take full advantage of multiple CPU cores. This is currently only available through the C-API, though a Python API is

[.](https://peps.python.org/pep-0554/)

**anticipated for 3.13**Use the new [ Py_NewInterpreterFromConfig()](../c-api/subinterpreters.html#c.Py_NewInterpreterFromConfig) function to
create an interpreter with its own GIL:

```
PyInterpreterConfig config = {
    .check_multi_interp_extensions = 1,
    .gil = PyInterpreterConfig_OWN_GIL,
};
PyThreadState *tstate = NULL;
PyStatus status = Py_NewInterpreterFromConfig(&tstate, &config);
if (PyStatus_Exception(status)) {
    return -1;
}
/* The new interpreter is now active in the current thread. */
```
For further examples how to use the C-API for sub-interpreters with a
per-interpreter GIL, see `Modules/_xxsubinterpretersmodule.c`.

(Contributed by Eric Snow in [gh-104210](https://github.com/python/cpython/issues/104210), etc.)

### PEP 669: Low impact monitoring for CPython[¶](#pep-669-low-impact-monitoring-for-cpython)

[ PEP 669](https://peps.python.org/pep-0669/) defines a new 

[for profilers, debuggers, and other tools to monitor events in CPython. It covers a wide range of events, including calls, returns, lines, exceptions, jumps, and more. This means that you only pay for what you use, providing support for near-zero overhead debuggers and coverage tools. See](../library/sys.monitoring.html#module-sys.monitoring)

`API``sys.monitoring` for details.(Contributed by Mark Shannon in [gh-103082](https://github.com/python/cpython/issues/103082).)

### PEP 688: Making the buffer protocol accessible in Python[¶](#pep-688-making-the-buffer-protocol-accessible-in-python)

[ PEP 688](https://peps.python.org/pep-0688/) introduces a way to use the 

[buffer protocol](../c-api/buffer.html#bufferobjects)from Python code. Classes that implement the

[method are now usable as buffer types.](../reference/datamodel.html#object.__buffer__)

`__buffer__()`The new [ collections.abc.Buffer](../library/collections.abc.html#collections.abc.Buffer) ABC provides a standard
way to represent buffer objects, for example in type annotations.
The new 

[enum represents the flags that can be used to customize buffer creation. (Contributed by Jelle Zijlstra in](../library/inspect.html#inspect.BufferFlags)

`inspect.BufferFlags`[gh-102500](https://github.com/python/cpython/issues/102500).)

### PEP 709: Comprehension inlining[¶](#pep-709-comprehension-inlining)

Dictionary, list, and set comprehensions are now inlined, rather than creating a
new single-use function object for each execution of the comprehension. This
speeds up execution of a comprehension by up to two times.
See [ PEP 709](https://peps.python.org/pep-0709/) for further details.

Comprehension iteration variables remain isolated and don’t overwrite a variable of the same name in the outer scope, nor are they visible after the comprehension. Inlining does result in a few visible behavior changes:

- There is no longer a separate frame for the comprehension in tracebacks, and tracing/profiling no longer shows the comprehension as a function call. 
- The - `symtable`
- Calling - `locals()`- `.0`variable for the comprehension “argument”.
- A comprehension iterating directly over - `locals()`(e.g.- `[k for k in locals()]`) may see “RuntimeError: dictionary changed size during iteration” when run under tracing (e.g. code coverage measurement). This is the same behavior already seen in e.g.- `for k in locals():`. To avoid the error, first create a list of keys to iterate over:- `keys = list(locals()); [k for k in keys]`.

(Contributed by Carl Meyer and Vladimir Matveev in [ PEP 709](https://peps.python.org/pep-0709/).)

### Improved Error Messages[¶](#improved-error-messages)

- Modules from the standard library are now potentially suggested as part of the error messages displayed by the interpreter when a - `NameError`- [gh-98254](https://github.com/python/cpython/issues/98254).)- >>> sys.version_info Traceback (most recent call last): File "<stdin>", line 1, in <module> NameError: name 'sys' is not defined. Did you forget to import 'sys'? 
- Improve the error suggestion for - `NameError`- `NameError`is raised in a method and the instance has an attribute that’s exactly equal to the name in the exception, the suggestion will include- `self.<NAME>`instead of the closest match in the method scope. (Contributed by Pablo Galindo in- [gh-99139](https://github.com/python/cpython/issues/99139).)- >>> class A: ... def __init__(self): ... self.blech = 1 ... ... def foo(self): ... somethin = blech ... >>> A().foo() Traceback (most recent call last): File "<stdin>", line 1 somethin = blech ^^^^^ NameError: name 'blech' is not defined. Did you mean: 'self.blech'? 
- Improve the - `SyntaxError`- `import x from y`instead of- `from y import x`. (Contributed by Pablo Galindo in- [gh-98931](https://github.com/python/cpython/issues/98931).)- >>> import a.y.z from b.y.z Traceback (most recent call last): File "<stdin>", line 1 import a.y.z from b.y.z ^^^^^^^^^^^^^^^^^^^^^^^ SyntaxError: Did you mean to use 'from ... import ...' instead? 
- `ImportError`- `from <module> import <name>`statements now include suggestions for the value of- `<name>`based on the available names in- `<module>`. (Contributed by Pablo Galindo in- [gh-91058](https://github.com/python/cpython/issues/91058).)- >>> from collections import chainmap Traceback (most recent call last): File "<stdin>", line 1, in <module> ImportError: cannot import name 'chainmap' from 'collections'. Did you mean: 'ChainMap'? 

## Other Language Changes[¶](#other-language-changes)

- The parser now raises - `SyntaxError`- [gh-96670](https://github.com/python/cpython/issues/96670).)
- A backslash-character pair that is not a valid escape sequence now generates a - `SyntaxWarning`- `DeprecationWarning`- `re.compile("\d+\.\d+")`now emits a- `SyntaxWarning`(- `"\d"`is an invalid escape sequence, use raw strings for regular expression:- `re.compile(r"\d+\.\d+")`). In a future Python version,- `SyntaxError`- `SyntaxWarning`. (Contributed by Victor Stinner in- [gh-98401](https://github.com/python/cpython/issues/98401).)
- Octal escapes with value larger than - `0o377`(ex:- `"\477"`), deprecated in Python 3.11, now produce a- `SyntaxWarning`- `DeprecationWarning`- `SyntaxError`- [gh-98401](https://github.com/python/cpython/issues/98401).)
- Variables used in the target part of comprehensions that are not stored to can now be used in assignment expressions ( - `:=`). For example, in- `[(b := 1) for a, b.prop in some_iter]`, the assignment to- `b`is now allowed. Note that assigning to variables stored to in the target part of comprehensions (like- `a`) is still disallowed, as per- **PEP 572**- [gh-100581](https://github.com/python/cpython/issues/100581).)
- Exceptions raised in a class or type’s - `__set_name__`method are no longer wrapped by a- `RuntimeError`- **PEP 678**- [gh-77757](https://github.com/python/cpython/issues/77757).)
- When a - `try-except*`construct handles the entire- `ExceptionGroup`- `ExceptionGroup`. Also changed in version 3.11.4. (Contributed by Irit Katriel in- [gh-103590](https://github.com/python/cpython/issues/103590).)
- The Garbage Collector now runs only on the eval breaker mechanism of the Python bytecode evaluation loop instead of object allocations. The GC can also run when - `PyErr_CheckSignals()`- [gh-97922](https://github.com/python/cpython/issues/97922).)
- All builtin and extension callables expecting boolean parameters now accept arguments of any type instead of just - `bool`- `int`- [gh-60203](https://github.com/python/cpython/issues/60203).)
- `memoryview`- [gh-90751](https://github.com/python/cpython/issues/90751).)
- `slice`- [gh-101264](https://github.com/python/cpython/issues/101264).)
- `sum()`- [gh-100425](https://github.com/python/cpython/issues/100425).)
- `ast.parse()`- `SyntaxError`- `ValueError`- [gh-96670](https://github.com/python/cpython/issues/96670).)
- The extraction methods in - `tarfile`- `shutil.unpack_archive()`- *filter*argument that allows limiting tar features than may be surprising or dangerous, such as creating files outside the destination directory. See- [tarfile extraction filters](../library/tarfile.html#tarfile-extraction-filter)for details. In Python 3.14, the default will switch to- `'data'`. (Contributed by Petr Viktorin in- **PEP 706**
- `types.MappingProxyType`- [gh-87995](https://github.com/python/cpython/issues/87995).)
- Add - [support for the perf profiler](../howto/perf_profiling.html#perf-profiling)through the new environment variable- `PYTHONPERFSUPPORT`- `-X perf`- `sys.activate_stack_trampoline()`- `sys.deactivate_stack_trampoline()`- `sys.is_stack_trampoline_active()`- [gh-96123](https://github.com/python/cpython/issues/96123).)

## New Modules[¶](#new-modules)

- None. 

## Improved Modules[¶](#improved-modules)

### array[¶](#array)

- The - `array.array`- [generic type](../glossary.html#term-generic-type). (Contributed by Jelle Zijlstra in- [gh-98658](https://github.com/python/cpython/issues/98658).)

### asyncio[¶](#asyncio)

- The performance of writing to sockets in - `asyncio`- `asyncio`now avoids unnecessary copying when writing to sockets and uses- `sendmsg()`- [gh-91166](https://github.com/python/cpython/issues/91166).)
- Add - `asyncio.eager_task_factory()`- `asyncio.create_eager_task_factory()`- [gh-102853](https://github.com/python/cpython/issues/102853),- [gh-104140](https://github.com/python/cpython/issues/104140), and- [gh-104138](https://github.com/python/cpython/issues/104138))
- On Linux, - `asyncio`- `asyncio.PidfdChildWatcher`by default if- `os.pidfd_open()`- `asyncio.ThreadedChildWatcher`. (Contributed by Kumar Aditya in- [gh-98024](https://github.com/python/cpython/issues/98024).)
- The event loop now uses the best available child watcher for each platform ( - `asyncio.PidfdChildWatcher`if supported and- `asyncio.ThreadedChildWatcher`otherwise), so manually configuring a child watcher is not recommended. (Contributed by Kumar Aditya in- [gh-94597](https://github.com/python/cpython/issues/94597).)
- Add - *loop_factory*parameter to- `asyncio.run()`- [gh-99388](https://github.com/python/cpython/issues/99388).)
- Add C implementation of - `asyncio.current_task()`- [gh-100344](https://github.com/python/cpython/issues/100344).)
- `asyncio.iscoroutine()`- `False`for generators as- `asyncio`- [gh-102748](https://github.com/python/cpython/issues/102748).)
- `asyncio.wait()`- `asyncio.as_completed()`- [gh-78530](https://github.com/python/cpython/issues/78530).)

### calendar[¶](#calendar)

- Add enums - `calendar.Month`- `calendar.Day`- [gh-103636](https://github.com/python/cpython/issues/103636).)

### csv[¶](#csv)

- Add - `csv.QUOTE_NOTNULL`- `csv.QUOTE_STRINGS`- `None`and empty strings by- `reader`- `writer`

### dis[¶](#dis)

- Pseudo instruction opcodes (which are used by the compiler but do not appear in executable bytecode) are now exposed in the - `dis`- `HAVE_ARGUMENT`- `dis.hasarg`- [gh-94216](https://github.com/python/cpython/issues/94216).)
- Add the - `dis.hasexc`- [gh-94216](https://github.com/python/cpython/issues/94216).)

### fractions[¶](#fractions)

- Objects of type - `fractions.Fraction`- [gh-100161](https://github.com/python/cpython/issues/100161).)

### importlib.resources[¶](#importlib-resources)

- `importlib.resources.as_file()`- [gh-97930](https://github.com/python/cpython/issues/97930).)
- Rename first parameter of - `importlib.resources.files()`- *anchor*. (Contributed by Jason R. Coombs in- [gh-100598](https://github.com/python/cpython/issues/100598).)

### inspect[¶](#inspect)

- Add - `inspect.markcoroutinefunction()`- [coroutine](../glossary.html#term-coroutine)for use with- `inspect.iscoroutinefunction()`- [gh-99247](https://github.com/python/cpython/issues/99247).)
- Add - `inspect.getasyncgenstate()`- `inspect.getasyncgenlocals()`- [gh-79940](https://github.com/python/cpython/issues/79940).)
- The performance of - `inspect.getattr_static()`- [gh-103193](https://github.com/python/cpython/issues/103193).)

### itertools[¶](#itertools)

- Add - `itertools.batched()`- [gh-98363](https://github.com/python/cpython/issues/98363).)

### math[¶](#math)

- Add - `math.sumprod()`- [gh-100485](https://github.com/python/cpython/issues/100485).)
- Extend - `math.nextafter()`- *steps*argument for moving up or down multiple steps at a time. (Contributed by Matthias Goergens, Mark Dickinson, and Raymond Hettinger in- [gh-94906](https://github.com/python/cpython/issues/94906).)

### os[¶](#os)

- Add - `os.PIDFD_NONBLOCK`- `os.pidfd_open()`- [gh-93312](https://github.com/python/cpython/issues/93312).)
- `os.DirEntry`- `os.DirEntry.is_junction()`- [gh-99547](https://github.com/python/cpython/issues/99547).)
- Add - `os.listdrives()`- `os.listvolumes()`- `os.listmounts()`- [gh-102519](https://github.com/python/cpython/issues/102519).)
- `os.stat()`- `os.lstat()`- `st_birthtime`field will now be filled with the creation time of the file, and- `st_ctime`is deprecated but still contains the creation time (but in the future will return the last metadata change, for consistency with other platforms).- `st_dev`may be up to 64 bits and- `st_ino`up to 128 bits depending on your file system, and- `st_rdev`is always set to zero rather than incorrect values. Both functions may be significantly faster on newer releases of Windows. (Contributed by Steve Dower in- [gh-99726](https://github.com/python/cpython/issues/99726).)

### os.path[¶](#os-path)

- Add - `os.path.isjunction()`- [gh-99547](https://github.com/python/cpython/issues/99547).)
- Add - `os.path.splitroot()`- `(drive, root, tail)`. (Contributed by Barney Gale in- [gh-101000](https://github.com/python/cpython/issues/101000).)

### pathlib[¶](#pathlib)

- Add support for subclassing - `pathlib.PurePath`- `pathlib.Path`- `pathlib.PurePath.with_segments()`
- Add - `pathlib.Path.walk()`- `os.walk()`- [gh-90385](https://github.com/python/cpython/issues/90385).)
- Add - *walk_up*optional parameter to- `pathlib.PurePath.relative_to()`- `..`entries in the result; this behavior is more consistent with- `os.path.relpath()`- [gh-84538](https://github.com/python/cpython/issues/84538).)
- Add - `pathlib.Path.is_junction()`- `os.path.isjunction()`- [gh-99547](https://github.com/python/cpython/issues/99547).)
- Add - *case_sensitive*optional parameter to- `pathlib.Path.glob()`- `pathlib.Path.rglob()`- `pathlib.PurePath.match()`

### platform[¶](#platform)

- Add support for detecting Windows 11 and Windows Server releases past 2012. Previously, lookups on Windows Server platforms newer than Windows Server 2012 and on Windows 11 would return - `Windows-10`. (Contributed by Steve Dower in- [gh-89545](https://github.com/python/cpython/issues/89545).)

### pdb[¶](#pdb)

- Add convenience variables to hold values temporarily for debug session and provide quick access to values like the current frame or the return value. (Contributed by Tian Gao in - [gh-103693](https://github.com/python/cpython/issues/103693).)

### random[¶](#random)

- Add - `random.binomialvariate()`- [gh-81620](https://github.com/python/cpython/issues/81620).)
- Add a default of - `lambd=1.0`to- `random.expovariate()`- [gh-100234](https://github.com/python/cpython/issues/100234).)

### shutil[¶](#shutil)

- `shutil.make_archive()`- *root_dir*argument to custom archivers which support it. In this case it no longer temporarily changes the current working directory of the process to- *root_dir*to perform archiving. (Contributed by Serhiy Storchaka in- [gh-74696](https://github.com/python/cpython/issues/74696).)
- `shutil.rmtree()`- *onexc*which is an error handler like- *onerror*but which expects an exception instance rather than a- *(typ, val, tb)*triplet.- *onerror*is deprecated. (Contributed by Irit Katriel in- [gh-102828](https://github.com/python/cpython/issues/102828).)
- `shutil.which()`- *PATHEXT*environment variable to find matches within- *PATH*on Windows even when the given- *cmd*includes a directory component. (Contributed by Charles Machalow in- [gh-103179](https://github.com/python/cpython/issues/103179).)- `shutil.which()`- `NeedCurrentDirectoryForExePathW`when querying for executables on Windows to determine if the current working directory should be prepended to the search path. (Contributed by Charles Machalow in- [gh-103179](https://github.com/python/cpython/issues/103179).)- `shutil.which()`- *cmd*with a component from- `PATHEXT`prior to a direct match elsewhere in the search path on Windows. (Contributed by Charles Machalow in- [gh-103179](https://github.com/python/cpython/issues/103179).)

### sqlite3[¶](#sqlite3)

- Add a - [command-line interface](../library/sqlite3.html#sqlite3-cli). (Contributed by Erlend E. Aasland in- [gh-77617](https://github.com/python/cpython/issues/77617).)
- Add the - `sqlite3.Connection.autocommit`- `sqlite3.Connection`- *autocommit*parameter to- `sqlite3.connect()`- **PEP 249**- [transaction handling](../library/sqlite3.html#sqlite3-transaction-control-autocommit). (Contributed by Erlend E. Aasland in- [gh-83638](https://github.com/python/cpython/issues/83638).)
- Add - *entrypoint*keyword-only parameter to- `sqlite3.Connection.load_extension()`- [gh-103015](https://github.com/python/cpython/issues/103015).)
- Add - `sqlite3.Connection.getconfig()`- `sqlite3.Connection.setconfig()`- `sqlite3.Connection`- [gh-103489](https://github.com/python/cpython/issues/103489).)

### statistics[¶](#statistics)

- Extend - `statistics.correlation()`- `ranked`method for computing the Spearman correlation of ranked data. (Contributed by Raymond Hettinger in- [gh-95861](https://github.com/python/cpython/issues/95861).)

### sys[¶](#sys)

- Add the - `sys.monitoring`- [PEP 669](#whatsnew312-pep669)monitoring API. (Contributed by Mark Shannon in- [gh-103082](https://github.com/python/cpython/issues/103082).)
- Add - `sys.activate_stack_trampoline()`- `sys.deactivate_stack_trampoline()`- `sys.is_stack_trampoline_active()`- [gh-96123](https://github.com/python/cpython/issues/96123).)
- Add - `sys.last_exc`- `sys.last_type`- `sys.last_value`- `sys.last_traceback`- [gh-102778](https://github.com/python/cpython/issues/102778).)
- `sys._current_exceptions()`- `(typ, exc, tb)`tuple. (Contributed by Irit Katriel in- [gh-103176](https://github.com/python/cpython/issues/103176).)
- `sys.setrecursionlimit()`- `sys.getrecursionlimit()`

### tempfile[¶](#tempfile)

- The - `tempfile.NamedTemporaryFile`- *delete_on_close*(Contributed by Evgeny Zorin in- [gh-58451](https://github.com/python/cpython/issues/58451).)
- `tempfile.mkdtemp()`- *dir*parameter is a relative path.

### threading[¶](#threading)

- Add - `threading.settrace_all_threads()`- `threading.setprofile_all_threads()`- [gh-93503](https://github.com/python/cpython/issues/93503).)

### tkinter[¶](#tkinter)

- `tkinter.Canvas.coords()`now flattens its arguments. It now accepts not only coordinates as separate arguments (- `x1, y1, x2, y2, ...`) and a sequence of coordinates (- `[x1, y1, x2, y2, ...]`), but also coordinates grouped in pairs (- `(x1, y1), (x2, y2), ...`and- `[(x1, y1), (x2, y2), ...]`), like- `create_*()`methods. (Contributed by Serhiy Storchaka in- [gh-94473](https://github.com/python/cpython/issues/94473).)

### tokenize[¶](#tokenize)

- The - `tokenize`- **PEP 701**- [gh-102856](https://github.com/python/cpython/issues/102856).) See- [Porting to Python 3.12](#whatsnew312-porting-to-python312)for more information on the changes to the- `tokenize`module.

### types[¶](#types)

- Add - `types.get_original_bases()`- [User-defined generic types](../library/typing.html#user-defined-generics)when subclassed. (Contributed by James Hilton-Balfe and Alex Waygood in- [gh-101827](https://github.com/python/cpython/issues/101827).)

### typing[¶](#typing)

- `isinstance()`- `runtime-checkable protocols`- `inspect.getattr_static()`- `hasattr()`- `__getattr__()`- `isinstance()`checks against runtime-checkable protocols. However, it may also mean that some objects which used to be considered instances of a runtime-checkable protocol may no longer be considered instances of that protocol on Python 3.12+, and vice versa. Most users are unlikely to be affected by this change. (Contributed by Alex Waygood in- [gh-102433](https://github.com/python/cpython/issues/102433).)
- The members of a runtime-checkable protocol are now considered “frozen” at runtime as soon as the class has been created. Monkey-patching attributes onto a runtime-checkable protocol will still work, but will have no impact on - `isinstance()`- >>> from typing import Protocol, runtime_checkable >>> @runtime_checkable ... class HasX(Protocol): ... x = 1 ... >>> class Foo: ... ... >>> f = Foo() >>> isinstance(f, HasX) False >>> f.x = 1 >>> isinstance(f, HasX) True >>> HasX.y = 2 >>> isinstance(f, HasX) # unchanged, even though HasX now also has a "y" attribute True - This change was made in order to speed up - `isinstance()`checks against runtime-checkable protocols.
- The performance profile of - `isinstance()`- `runtime-checkable protocols`- `isinstance()`checks against protocols with only a few members should be at least 2x faster than in 3.11, and some may be 20x faster or more. However,- `isinstance()`checks against protocols with many members may be slower than in Python 3.11. (Contributed by Alex Waygood in- [gh-74690](https://github.com/python/cpython/issues/74690)and- [gh-103193](https://github.com/python/cpython/issues/103193).)
- All - `typing.TypedDict`- `typing.NamedTuple`- `__orig_bases__`attribute. (Contributed by Adrian Garcia Badaracco in- [gh-103699](https://github.com/python/cpython/issues/103699).)
- Add - `frozen_default`parameter to- `typing.dataclass_transform()`- [gh-99957](https://github.com/python/cpython/issues/99957).)

### unicodedata[¶](#unicodedata)

- The Unicode database has been updated to version 15.0.0. (Contributed by Benjamin Peterson in - [gh-96734](https://github.com/python/cpython/issues/96734)).

### unittest[¶](#unittest)

Add a `--durations` command line option, showing the N slowest test cases:

```
python3 -m unittest --durations=3 lib.tests.test_threading
.....
Slowest test durations
----------------------------------------------------------------------
1.210s     test_timeout (Lib.test.test_threading.BarrierTests)
1.003s     test_default_timeout (Lib.test.test_threading.BarrierTests)
0.518s     test_timeout (Lib.test.test_threading.EventTests)
(0.000 durations hidden.  Use -v to show these durations.)
----------------------------------------------------------------------
Ran 158 tests in 9.869s
OK (skipped=3)
```
(Contributed by Giampaolo Rodola in [gh-48330](https://github.com/python/cpython/issues/48330))

### uuid[¶](#uuid)

- Add a - [command-line interface](../library/uuid.html#uuid-cli). (Contributed by Adam Chhina in- [gh-88597](https://github.com/python/cpython/issues/88597).)

## Optimizations[¶](#optimizations)

- Remove - `wstr`and- `wstr_length`members from Unicode objects. It reduces object size by 8 or 16 bytes on 64bit platform. (- **PEP 623**- [gh-92536](https://github.com/python/cpython/issues/92536).)
- Add experimental support for using the BOLT binary optimizer in the build process, which improves performance by 1-5%. (Contributed by Kevin Modzelewski in - [gh-90536](https://github.com/python/cpython/issues/90536)and tuned by Donghee Na in- [gh-101525](https://github.com/python/cpython/issues/101525))
- Speed up the regular expression substitution (functions - `re.sub()`- `re.subn()`- `re.Pattern`methods) for replacement strings containing group references by 2–3 times. (Contributed by Serhiy Storchaka in- [gh-91524](https://github.com/python/cpython/issues/91524).)
- Speed up - `asyncio.Task`- [gh-103793](https://github.com/python/cpython/issues/103793).)
- The - `tokenize.tokenize()`- `tokenize.generate_tokens()`- **PEP 701**- `tokenize`- [gh-102856](https://github.com/python/cpython/issues/102856).)
- Speed up - `super()`- `LOAD_SUPER_ATTR`- [gh-103497](https://github.com/python/cpython/issues/103497).)

## CPython bytecode changes[¶](#cpython-bytecode-changes)

- Remove the - `LOAD_METHOD`instruction. It has been merged into- `LOAD_ATTR`- `LOAD_ATTR`will now behave like the old- `LOAD_METHOD`instruction if the low bit of its oparg is set. (Contributed by Ken Jin in- [gh-93429](https://github.com/python/cpython/issues/93429).)
- Remove the - `JUMP_IF_FALSE_OR_POP`and- `JUMP_IF_TRUE_OR_POP`instructions. (Contributed by Irit Katriel in- [gh-102859](https://github.com/python/cpython/issues/102859).)
- Remove the - `PRECALL`instruction. (Contributed by Mark Shannon in- [gh-92925](https://github.com/python/cpython/issues/92925).)
- Add the - `BINARY_SLICE`- `STORE_SLICE`- [gh-94163](https://github.com/python/cpython/issues/94163).)
- Add the - `CALL_INTRINSIC_1`- [gh-99005](https://github.com/python/cpython/issues/99005).)
- Add the - `CALL_INTRINSIC_2`- [gh-101799](https://github.com/python/cpython/issues/101799).)
- Add the - `CLEANUP_THROW`- [gh-90997](https://github.com/python/cpython/issues/90997).)
- Add the - `END_SEND`instruction. (Contributed by Mark Shannon in- [gh-103082](https://github.com/python/cpython/issues/103082).)
- Add the - `LOAD_FAST_AND_CLEAR`- **PEP 709**- [gh-101441](https://github.com/python/cpython/issues/101441).)
- Add the - `LOAD_FAST_CHECK`- [gh-93143](https://github.com/python/cpython/issues/93143).)
- Add the - `LOAD_FROM_DICT_OR_DEREF`- `LOAD_FROM_DICT_OR_GLOBALS`- `LOAD_LOCALS`- **PEP 695**- `LOAD_CLASSDEREF`opcode, which can be replaced with- `LOAD_LOCALS`plus- `LOAD_FROM_DICT_OR_DEREF`. (Contributed by Jelle Zijlstra in- [gh-103764](https://github.com/python/cpython/issues/103764).)
- Add the - `LOAD_SUPER_ATTR`- [gh-103497](https://github.com/python/cpython/issues/103497).)
- Add the - `RETURN_CONST`instruction. (Contributed by Wenyang Wang in- [gh-101632](https://github.com/python/cpython/issues/101632).)

## Demos and Tools[¶](#demos-and-tools)

- Remove the - `Tools/demo/`directory which contained old demo scripts. A copy can be found in the- [old-demos project](https://github.com/gvanrossum/old-demos). (Contributed by Victor Stinner in- [gh-97681](https://github.com/python/cpython/issues/97681).)
- Remove outdated example scripts of the - `Tools/scripts/`directory. A copy can be found in the- [old-demos project](https://github.com/gvanrossum/old-demos). (Contributed by Victor Stinner in- [gh-97669](https://github.com/python/cpython/issues/97669).)

## Deprecated[¶](#deprecated)

- `argparse`- *type*,- *choices*, and- *metavar*parameters of- `argparse.BooleanOptionalAction`are deprecated and will be removed in 3.14. (Contributed by Nikita Sobolev in- [gh-92248](https://github.com/python/cpython/issues/92248).)
- `ast`- `ast`features have been deprecated in documentation since Python 3.8, now cause a- `DeprecationWarning`- `ast.Num`
- `ast.Str`
- `ast.Bytes`
- `ast.NameConstant`
- `ast.Ellipsis`
 - Use - `ast.Constant`- [gh-90953](https://github.com/python/cpython/issues/90953).)
- 
- The child watcher classes - `asyncio.MultiLoopChildWatcher`,- `asyncio.FastChildWatcher`,- `asyncio.AbstractChildWatcher`and- `asyncio.SafeChildWatcher`are deprecated and will be removed in Python 3.14. (Contributed by Kumar Aditya in- [gh-94597](https://github.com/python/cpython/issues/94597).)
- `asyncio.set_child_watcher()`,- `asyncio.get_child_watcher()`,- `asyncio.AbstractEventLoopPolicy.set_child_watcher()`and- `asyncio.AbstractEventLoopPolicy.get_child_watcher()`are deprecated and will be removed in Python 3.14. (Contributed by Kumar Aditya in- [gh-94597](https://github.com/python/cpython/issues/94597).)
- The - `get_event_loop()`- `DeprecationWarning`- [gh-100160](https://github.com/python/cpython/issues/100160).)
 
- `calendar`- `calendar.January`and- `calendar.February`constants are deprecated and replaced by- `calendar.JANUARY`- `calendar.FEBRUARY`- [gh-103636](https://github.com/python/cpython/issues/103636).)
- `collections.abc`- `collections.abc.ByteString`- Use - `isinstance(obj, collections.abc.Buffer)`to test if- `obj`implements the- [buffer protocol](../c-api/buffer.html#bufferobjects)at runtime. For use in type annotations, either use- `Buffer`- `bytes | bytearray | memoryview`).- `ByteString`was originally intended to be an abstract class that would serve as a supertype of both- `bytes`- `bytearray`- `ByteString`never actually told you anything useful about the object. Other common buffer types such as- `memoryview`- `ByteString`(either at runtime or by static type checkers).- See - **PEP 688**- [gh-91896](https://github.com/python/cpython/issues/91896).)
- `datetime`- `datetime.datetime`- `utcnow()`- `utcfromtimestamp()`- `now()`- `fromtimestamp()`- *tz*parameter set to- `datetime.UTC`- [gh-103857](https://github.com/python/cpython/issues/103857).)
- `email`- *isdst*parameter in- `email.utils.localtime()`- [gh-72346](https://github.com/python/cpython/issues/72346).)
- `importlib.abc`- `importlib.abc.ResourceReader`
- `importlib.abc.Traversable`
- `importlib.abc.TraversableResources`
 - Use - `importlib.resources.abc`- (Contributed by Jason R. Coombs and Hugo van Kemenade in - [gh-93963](https://github.com/python/cpython/issues/93963).)
- `itertools`- [gh-101588](https://github.com/python/cpython/issues/101588).)
- `multiprocessing`- `multiprocessing`start method will change to a safer one on Linux, BSDs, and other non-macOS POSIX platforms where- `'fork'`is currently the default (- [gh-84559](https://github.com/python/cpython/issues/84559)). Adding a runtime warning about this was deemed too disruptive as the majority of code is not expected to care. Use the- `get_context()`- `set_start_method()`- *requires*- `'fork'`. See- [contexts and start methods](../library/multiprocessing.html#multiprocessing-start-methods).
- `pkgutil`- `pkgutil.find_loader()`and- `pkgutil.get_loader()`are deprecated and will be removed in Python 3.14; use- `importlib.util.find_spec()`- [gh-97850](https://github.com/python/cpython/issues/97850).)
- `pty`- `master_open()`and- `slave_open()`functions that have been deprecated since Python 2 but only gained a proper- `DeprecationWarning`- [gh-85984](https://github.com/python/cpython/issues/85984).)
- `os`- The - `st_ctime`fields return by- `os.stat()`- `os.lstat()`- `st_birthtime`field. (Contributed by Steve Dower in- [gh-99726](https://github.com/python/cpython/issues/99726).)
- On POSIX platforms, - `os.fork()`- `DeprecationWarning`- *appeared*to work. We added the warning to raise awareness as issues encountered by code doing this are becoming more frequent. See the- `os.fork()`documentation for more details along with- [this discussion on fork being incompatible with threads](https://discuss.python.org/t/concerns-regarding-deprecation-of-fork-with-alive-threads/33555)for- *why*we’re now surfacing this longstanding platform compatibility problem to developers.
 - When this warning appears due to usage of - `multiprocessing`- `concurrent.futures`- `multiprocessing`start method such as- `"spawn"`or- `"forkserver"`.
- `shutil`- *onerror*argument of- `shutil.rmtree()`- *onexc*instead. (Contributed by Irit Katriel in- [gh-102828](https://github.com/python/cpython/issues/102828).)
- 
- [default adapters and converters](../library/sqlite3.html#sqlite3-default-converters)are now deprecated. Instead, use the- [Adapter and converter recipes](../library/sqlite3.html#sqlite3-adapter-converter-recipes)and tailor them to your needs. (Contributed by Erlend E. Aasland in- [gh-90016](https://github.com/python/cpython/issues/90016).)
- In - `execute()`- `DeprecationWarning`- [named placeholders](../library/sqlite3.html#sqlite3-placeholders)are used together with parameters supplied as a- [sequence](../glossary.html#term-sequence)instead of as a- `dict`- `ProgrammingError`- [gh-101698](https://github.com/python/cpython/issues/101698).)
 
- `sys`- `sys.last_type`- `sys.last_value`- `sys.last_traceback`- `sys.last_exc`- [gh-102778](https://github.com/python/cpython/issues/102778).)
- `tarfile`- *filter*is deprecated until Python 3.14, when- `'data'`filter will become the default. See- [Extraction filters](../library/tarfile.html#tarfile-extraction-filter)for details.
- 
- `typing.Hashable`- `typing.Sized`- `collections.abc.Hashable`- `collections.abc.Sized`- [gh-94309](https://github.com/python/cpython/issues/94309).)
- `typing.ByteString`- `DeprecationWarning`- [gh-91896](https://github.com/python/cpython/issues/91896).)
 
- `xml.etree.ElementTree`- `DeprecationWarning`- `xml.etree.ElementTree.Element`- `FutureWarning`- [gh-83122](https://github.com/python/cpython/issues/83122).)
- The 3-arg signatures (type, value, traceback) of - `coroutine throw()`- `generator throw()`- `async generator throw()`- [gh-89874](https://github.com/python/cpython/issues/89874).)
- `DeprecationWarning`- `__package__`- `__spec__.parent`- `ImportWarning`- [gh-65961](https://github.com/python/cpython/issues/65961).)
- Setting - `__package__`- `__cached__`- [gh-65961](https://github.com/python/cpython/issues/65961).)
- The bitwise inversion operator ( - `~`) on bool is deprecated. It will throw an error in Python 3.16. Use- `not`for logical negation of bools instead. In the rare case that you really need the bitwise inversion of the underlying- `int`, convert to int explicitly:- `~int(x)`. (Contributed by Tim Hoffmann in- [gh-103487](https://github.com/python/cpython/issues/103487).)
- Accessing - `co_lnotab`- **PEP 626**- `DeprecationWarning`- [gh-101866](https://github.com/python/cpython/issues/101866).)

### Pending removal in Python 3.13[¶](#pending-removal-in-python-3-13)

Modules (see [ PEP 594](https://peps.python.org/pep-0594/)):

- `aifc`
- `audioop`
- `cgi`
- `cgitb`
- `chunk`
- `crypt`
- `imghdr`
- `mailcap`
- `msilib`
- `nis`
- `nntplib`
- `ossaudiodev`
- `pipes`
- `sndhdr`
- `spwd`
- `sunau`
- `telnetlib`
- `uu`
- `xdrlib`

Other modules:

- `lib2to3`, and the- **2to3**program (- [gh-84540](https://github.com/python/cpython/issues/84540))

APIs:

- `configparser.LegacyInterpolation`(- [gh-90765](https://github.com/python/cpython/issues/90765))
- `locale.resetlocale()`(- [gh-90817](https://github.com/python/cpython/issues/90817))
- `turtle.RawTurtle.settiltangle()`(- [gh-50096](https://github.com/python/cpython/issues/50096))
- `unittest.findTestCases()`(- [gh-50096](https://github.com/python/cpython/issues/50096))
- `unittest.getTestCaseNames()`(- [gh-50096](https://github.com/python/cpython/issues/50096))
- `unittest.makeSuite()`(- [gh-50096](https://github.com/python/cpython/issues/50096))
- `unittest.TestProgram.usageExit()`(- [gh-67048](https://github.com/python/cpython/issues/67048))
- `webbrowser.MacOSX`(- [gh-86421](https://github.com/python/cpython/issues/86421))
- `classmethod`- [gh-89519](https://github.com/python/cpython/issues/89519))

### Pending removal in Python 3.14[¶](#pending-removal-in-python-3-14)

- `argparse`- *type*,- *choices*, and- *metavar*parameters of- `argparse.BooleanOptionalAction`are deprecated and will be removed in 3.14. (Contributed by Nikita Sobolev in- [gh-92248](https://github.com/python/cpython/issues/92248).)
- `ast`- `DeprecationWarning`- `ast.Num`
- `ast.Str`
- `ast.Bytes`
- `ast.NameConstant`
- `ast.Ellipsis`
 - Use - `ast.Constant`- [gh-90953](https://github.com/python/cpython/issues/90953).)
- 
- The child watcher classes - `asyncio.MultiLoopChildWatcher`,- `asyncio.FastChildWatcher`,- `asyncio.AbstractChildWatcher`and- `asyncio.SafeChildWatcher`are deprecated and will be removed in Python 3.14. (Contributed by Kumar Aditya in- [gh-94597](https://github.com/python/cpython/issues/94597).)
- `asyncio.set_child_watcher()`,- `asyncio.get_child_watcher()`,- `asyncio.AbstractEventLoopPolicy.set_child_watcher()`and- `asyncio.AbstractEventLoopPolicy.get_child_watcher()`are deprecated and will be removed in Python 3.14. (Contributed by Kumar Aditya in- [gh-94597](https://github.com/python/cpython/issues/94597).)
- The - `get_event_loop()`- `DeprecationWarning`- [gh-100160](https://github.com/python/cpython/issues/100160).)
 
- `email`- *isdst*parameter in- `email.utils.localtime()`- [gh-72346](https://github.com/python/cpython/issues/72346).)
- `importlib.abc`- `importlib.abc.ResourceReader`
- `importlib.abc.Traversable`
- `importlib.abc.TraversableResources`
 - Use - `importlib.resources.abc`- (Contributed by Jason R. Coombs and Hugo van Kemenade in - [gh-93963](https://github.com/python/cpython/issues/93963).)
- `itertools`- [gh-101588](https://github.com/python/cpython/issues/101588).)
- `multiprocessing`- `'fork'`is currently the default (- [gh-84559](https://github.com/python/cpython/issues/84559)). Adding a runtime warning about this was deemed too disruptive as the majority of code is not expected to care. Use the- `get_context()`- `set_start_method()`- *requires*- `'fork'`. See- [Contexts and start methods](../library/multiprocessing.html#multiprocessing-start-methods).
- `pathlib`- `is_relative_to()`- `relative_to()`
- `pkgutil`- `pkgutil.find_loader()`and- `pkgutil.get_loader()`now raise- `DeprecationWarning`- `importlib.util.find_spec()`- [gh-97850](https://github.com/python/cpython/issues/97850).)
- `pty`- `master_open()`: use- `pty.openpty()`
- `slave_open()`: use- `pty.openpty()`
 
- 
- `version`and- `version_info`.
- `execute()`- `executemany()`- [named placeholders](../library/sqlite3.html#sqlite3-placeholders)are used and- *parameters*is a sequence instead of a- `dict`
 
- `urllib`- `urllib.parse.Quoter`is deprecated: it was not intended to be a public API. (Contributed by Gregory P. Smith in- [gh-88168](https://github.com/python/cpython/issues/88168).)

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

## Removed[¶](#removed)

### asynchat and asyncore[¶](#asynchat-and-asyncore)

### configparser[¶](#configparser)

- Several names deprecated in the - `configparser`- [gh-89336](https://github.com/python/cpython/issues/89336):- `configparser.ParsingError`- `filename`attribute or argument. Use the- `source`attribute and argument instead.
- `configparser`- `SafeConfigParser`class. Use the shorter- `ConfigParser`
- `configparser.ConfigParser`- `readfp`method. Use- `read_file()`
 

### distutils[¶](#distutils)

### ensurepip[¶](#ensurepip)

- Remove the bundled setuptools wheel from - `ensurepip`- `venv`- `pip (>= 22.1)`does not require setuptools to be installed in the environment.- `setuptools`-based (and- `distutils`-based) packages can still be used with- `pip install`, since pip will provide- `setuptools`in the build environment it uses for building a package.- `easy_install`,- `pkg_resources`,- `setuptools`and- `distutils`are no longer provided by default in environments created with- `venv`or bootstrapped with- `ensurepip`, since they are part of the- `setuptools`package. For projects relying on these at runtime, the- `setuptools`project should be declared as a dependency and installed separately (typically, using pip).- (Contributed by Pradyun Gedam in - [gh-95299](https://github.com/python/cpython/issues/95299).)

### enum[¶](#enum)

### ftplib[¶](#ftplib)

### gzip[¶](#gzip)

- Remove the - `filename`attribute of- `gzip`- `gzip.GzipFile`- `name`- `filename`attribute added- `'.gz'`file extension if it was not present. (Contributed by Victor Stinner in- [gh-94196](https://github.com/python/cpython/issues/94196).)

### hashlib[¶](#hashlib)

- Remove the pure Python implementation of - `hashlib`- `hashlib.pbkdf2_hmac()`- **PEP 644**- `pbkdf2_hmac()`which is faster. (Contributed by Victor Stinner in- [gh-94199](https://github.com/python/cpython/issues/94199).)

### importlib[¶](#importlib)

- Many previously deprecated cleanups in - `importlib`- References to, and support for - `module_repr()`has been removed. (Contributed by Barry Warsaw in- [gh-97850](https://github.com/python/cpython/issues/97850).)
- `importlib.util.set_package`,- `importlib.util.set_loader`and- `importlib.util.module_for_loader`have all been removed. (Contributed by Brett Cannon and Nikita Sobolev in- [gh-65961](https://github.com/python/cpython/issues/65961)and- [gh-97850](https://github.com/python/cpython/issues/97850).)
- Support for - `find_loader()`and- `find_module()`APIs have been removed. (Contributed by Barry Warsaw in- [gh-98040](https://github.com/python/cpython/issues/98040).)
- `importlib.abc.Finder`,- `pkgutil.ImpImporter`, and- `pkgutil.ImpLoader`have been removed. (Contributed by Barry Warsaw in- [gh-98040](https://github.com/python/cpython/issues/98040).)
 

### imp[¶](#imp)

- The - `imp`module has been removed. (Contributed by Barry Warsaw in- [gh-98040](https://github.com/python/cpython/issues/98040).)- To migrate, consult the following correspondence table: - imp - importlib - `imp.NullImporter`- Insert - `None`into- `sys.path_importer_cache`- `imp.cache_from_source()`- `imp.find_module()`- `imp.get_magic()`- `imp.get_suffixes()`- `importlib.machinery.SOURCE_SUFFIXES`- `importlib.machinery.EXTENSION_SUFFIXES`- `importlib.machinery.BYTECODE_SUFFIXES`- `imp.get_tag()`- `imp.load_module()`- `imp.new_module(name)`- `types.ModuleType(name)`- `imp.reload()`- `imp.source_from_cache()`- `imp.load_source()`- *See below*- Replace - `imp.load_source()`with:- import importlib.util import importlib.machinery def load_source(modname, filename): loader = importlib.machinery.SourceFileLoader(modname, filename) spec = importlib.util.spec_from_file_location(modname, filename, loader=loader) module = importlib.util.module_from_spec(spec) # The module is always executed and not cached in sys.modules. # Uncomment the following line to cache the module. # sys.modules[module.__name__] = module loader.exec_module(module) return module 
- Remove - `imp`functions and attributes with no replacements:- Undocumented functions: - `imp.init_builtin()`
- `imp.load_compiled()`
- `imp.load_dynamic()`
- `imp.load_package()`
 
- `imp.lock_held()`,- `imp.acquire_lock()`,- `imp.release_lock()`: the locking scheme has changed in Python 3.3 to per-module locks.
- `imp.find_module()`constants:- `SEARCH_ERROR`,- `PY_SOURCE`,- `PY_COMPILED`,- `C_EXTENSION`,- `PY_RESOURCE`,- `PKG_DIRECTORY`,- `C_BUILTIN`,- `PY_FROZEN`,- `PY_CODERESOURCE`,- `IMP_HOOK`.
 

### io[¶](#io)

### locale[¶](#locale)

- Remove - `locale`- `locale.format()`function, deprecated in Python 3.7: use- `locale.format_string()`- [gh-94226](https://github.com/python/cpython/issues/94226).)

### smtpd[¶](#smtpd)

### sqlite3[¶](#id2)

- The following undocumented - `sqlite3`- `sqlite3.enable_shared_cache()`
- `sqlite3.OptimizedUnicode`
 - If a shared cache must be used, open the database in URI mode using the - `cache=shared`query parameter.- The - `sqlite3.OptimizedUnicode`text factory has been an alias for- `str`- `OptimizedUnicode`can either use- `str`explicitly, or rely on the default value which is also- `str`.- (Contributed by Erlend E. Aasland in - [gh-92548](https://github.com/python/cpython/issues/92548).)

### ssl[¶](#ssl)

- Remove - `ssl`- `ssl.RAND_pseudo_bytes()`function, deprecated in Python 3.6: use- `os.urandom()`- `ssl.RAND_bytes()`- [gh-94199](https://github.com/python/cpython/issues/94199).)
- Remove the - `ssl.match_hostname()`function. It was deprecated in Python 3.7. OpenSSL performs hostname matching since Python 3.7, Python no longer uses the- `ssl.match_hostname()`function. (Contributed by Victor Stinner in- [gh-94199](https://github.com/python/cpython/issues/94199).)
- Remove the - `ssl.wrap_socket()`function, deprecated in Python 3.7: instead, create a- `ssl.SSLContext`- `ssl.SSLContext.wrap_socket`- `ssl.wrap_socket()`is broken and insecure. The function neither sends a SNI TLS extension nor validates the server hostname. Code is subject to- **CWE 295**- [gh-94199](https://github.com/python/cpython/issues/94199).)

### unittest[¶](#id3)

- Remove many long-deprecated - `unittest`- A number of - `TestCase`- Deprecated alias - Method Name - Deprecated in - `failUnless`- 3.1 - `failIf`- 3.1 - `failUnlessEqual`- 3.1 - `failIfEqual`- 3.1 - `failUnlessAlmostEqual`- 3.1 - `failIfAlmostEqual`- 3.1 - `failUnlessRaises`- 3.1 - `assert_`- 3.2 - `assertEquals`- 3.2 - `assertNotEquals`- 3.2 - `assertAlmostEquals`- 3.2 - `assertNotAlmostEquals`- 3.2 - `assertRegexpMatches`- 3.2 - `assertRaisesRegexp`- 3.2 - `assertNotRegexpMatches`- 3.5 - You can use - [https://github.com/isidentical/teyit](https://github.com/isidentical/teyit)to automatically modernise your unit tests.
- Undocumented and broken - `TestCase`- `assertDictContainsSubset`(deprecated in Python 3.2).
- Undocumented - `TestLoader.loadTestsFromModule`- *use_load_tests*(deprecated and ignored since Python 3.5).
- An alias of the - `TextTestResult`- `_TextTestResult`(deprecated in Python 3.2).
 - (Contributed by Serhiy Storchaka in - [gh-89325](https://github.com/python/cpython/issues/89325).)

### webbrowser[¶](#webbrowser)

- Remove support for obsolete browsers from - `webbrowser`- [gh-102871](https://github.com/python/cpython/issues/102871)).

### xml.etree.ElementTree[¶](#xml-etree-elementtree)

- Remove the - `ElementTree.Element.copy()`method of the pure Python implementation, deprecated in Python 3.10, use the- `copy.copy()`- `xml.etree.ElementTree`- `copy()`method, only a- `__copy__()`method. (Contributed by Victor Stinner in- [gh-94383](https://github.com/python/cpython/issues/94383).)

### zipimport[¶](#zipimport)

### Others[¶](#others)

- Remove the - `suspicious`rule from the documentation- `Makefile`and- `Doc/tools/rstlint.py`, both in favor of- [sphinx-lint](https://github.com/sphinx-contrib/sphinx-lint). (Contributed by Julien Palard in- [gh-98179](https://github.com/python/cpython/issues/98179).)
- Remove the - *keyfile*and- *certfile*parameters from the- `ftplib`- `imaplib`- `poplib`- `smtplib`- *key_file*,- *cert_file*and- *check_hostname*parameters from the- `http.client`- *context*parameter (- *ssl_context*in- `imaplib`) instead. (Contributed by Victor Stinner in- [gh-94172](https://github.com/python/cpython/issues/94172).)
- Remove - `Jython`compatibility hacks from several stdlib modules and tests. (Contributed by Nikita Sobolev in- [gh-99482](https://github.com/python/cpython/issues/99482).)
- Remove - `_use_broken_old_ctypes_structure_semantics_`flag from- `ctypes`- [gh-99285](https://github.com/python/cpython/issues/99285).)

## Porting to Python 3.12[¶](#porting-to-python-3-12)

This section lists previously described changes and other bugfixes that may require changes to your code.

### Changes in the Python API[¶](#changes-in-the-python-api)

- More strict rules are now applied for numerical group references and group names in regular expressions. Only sequence of ASCII digits is now accepted as a numerical reference. The group name in bytes patterns and replacement strings can now only contain ASCII letters and digits and underscore. (Contributed by Serhiy Storchaka in - [gh-91760](https://github.com/python/cpython/issues/91760).)
- Remove - `randrange()`functionality deprecated since Python 3.10. Formerly,- `randrange(10.0)`losslessly converted to- `randrange(10)`. Now, it raises a- `TypeError`- `randrange(10.5)`or- `randrange('10')`has been changed from- `ValueError`- `TypeError`. This also prevents bugs where- `randrange(1e25)`would silently select from a larger range than- `randrange(10**25)`. (Originally suggested by Serhiy Storchaka- [gh-86388](https://github.com/python/cpython/issues/86388).)
- `argparse.ArgumentParser`- `fromfile_prefix_chars`option) from default text encoding (e.g.- `locale.getpreferredencoding(False)`- [filesystem encoding and error handler](../glossary.html#term-filesystem-encoding-and-error-handler). Argument files should be encoded in UTF-8 instead of ANSI Codepage on Windows.
- Remove the - `asyncore`-based- `smtpd`module deprecated in Python 3.4.7 and 3.5.4. A recommended replacement is the- `asyncio`- [aiosmtpd](https://pypi.org/project/aiosmtpd/)PyPI module.
- `shlex.split()`- `None`for- *s*argument now raises an exception, rather than reading- `sys.stdin`- [gh-94352](https://github.com/python/cpython/issues/94352).)
- The - `os`- `bytearray`- `memoryview`- `bytes`- [gh-98393](https://github.com/python/cpython/issues/98393).)
- `syslog.openlog()`- `syslog.closelog()`- `syslog.syslog()`- `syslog.openlog()`has already been called in the main interpreter. These new restrictions do not apply to the main interpreter, so only a very small set of users might be affected. This change helps with interpreter isolation. Furthermore,- `syslog`- [gh-99127](https://github.com/python/cpython/issues/99127).)
- The undocumented locking behavior of - `cached_property()`
- `sys._current_exceptions()`- `(typ, exc, tb)`tuple. (Contributed by Irit Katriel in- [gh-103176](https://github.com/python/cpython/issues/103176).)
- When extracting tar files using - `tarfile`- `shutil.unpack_archive()`- *filter*argument to limit features that may be surprising or dangerous. See- [Extraction filters](../library/tarfile.html#tarfile-extraction-filter)for details.
- The output of the - `tokenize.tokenize()`- `tokenize.generate_tokens()`- **PEP 701**- `STRING`tokens are not emitted any more for f-strings and the tokens described in- **PEP 701**- `FSTRING_START`,- `FSTRING_MIDDLE`and- `FSTRING_END`are now emitted for f-string “string” parts in addition to the appropriate tokens for the tokenization in the expression components. For example for the f-string- `f"start {1+1} end"`the old version of the tokenizer emitted:- 1,0-1,18: STRING 'f"start {1+1} end"' - while the new version emits: - 1,0-1,2: FSTRING_START 'f"' 1,2-1,8: FSTRING_MIDDLE 'start ' 1,8-1,9: OP '{' 1,9-1,10: NUMBER '1' 1,10-1,11: OP '+' 1,11-1,12: NUMBER '1' 1,12-1,13: OP '}' 1,13-1,17: FSTRING_MIDDLE ' end' 1,17-1,18: FSTRING_END '"' - Additionally, there may be some minor behavioral changes as a consequence of the changes required to support - **PEP 701**- The - `type`attribute of the tokens emitted when tokenizing some invalid Python characters such as- `!`has changed from- `ERRORTOKEN`to- `OP`.
- Incomplete single-line strings now also raise - `tokenize.TokenError`
- Some incomplete or invalid Python code now raises - `tokenize.TokenError`- `ERRORTOKEN`tokens when tokenizing it.
- Mixing tabs and spaces as indentation in the same file is not supported anymore and will raise a - `TabError`
 
- The - `threading`- `_thread`module to have an- `_is_main_interpreter`attribute. It is a function with no arguments that returns- `True`if the current interpreter is the main interpreter.- Any library or application that provides a custom - `_thread`module should provide- `_is_main_interpreter()`. (See- [gh-112826](https://github.com/python/cpython/issues/112826).)

## Build Changes[¶](#build-changes)

- Python no longer uses - `setup.py`to build shared C extension modules. Build parameters like headers and libraries are detected in- `configure`script. Extensions are built by- `Makefile`. Most extensions use- `pkg-config`and fall back to manual detection. (Contributed by Christian Heimes in- [gh-93939](https://github.com/python/cpython/issues/93939).)
- `va_start()`with two parameters, like- `va_start(args, format),`is now required to build Python.- `va_start()`is no longer called with a single parameter. (Contributed by Kumar Aditya in- [gh-93207](https://github.com/python/cpython/issues/93207).)
- CPython now uses the ThinLTO option as the default link time optimization policy if the Clang compiler accepts the flag. (Contributed by Donghee Na in - [gh-89536](https://github.com/python/cpython/issues/89536).)
- Add - `COMPILEALL_OPTS`variable in- `Makefile`to override- `compileall`- `-j0`) in- `make install`. Also merged the 3- `compileall`commands into a single command to build .pyc files for all optimization levels (0, 1, 2) at once. (Contributed by Victor Stinner in- [gh-99289](https://github.com/python/cpython/issues/99289).)
- Add platform triplets for 64-bit LoongArch: - loongarch64-linux-gnusf 
- loongarch64-linux-gnuf32 
- loongarch64-linux-gnu 
 - (Contributed by Zhang Na in - [gh-90656](https://github.com/python/cpython/issues/90656).)
- `PYTHON_FOR_REGEN`now require Python 3.10 or newer.
- Autoconf 2.71 and aclocal 1.16.4 is now required to regenerate - `configure`. (Contributed by Christian Heimes in- [gh-89886](https://github.com/python/cpython/issues/89886).)
- Windows builds and macOS installers from python.org now use OpenSSL 3.0. 

## C API Changes[¶](#c-api-changes)

### New Features[¶](#id4)

- **PEP 697**- [Unstable C API tier](../c-api/stable.html#unstable-c-api), intended for low-level tools like debuggers and JIT compilers. This API may change in each minor release of CPython without deprecation warnings. Its contents are marked by the- `PyUnstable_`prefix in names.- Code object constructors: - `PyUnstable_Code_New()`(renamed from- `PyCode_New`)
- `PyUnstable_Code_NewWithPosOnlyArgs()`(renamed from- `PyCode_NewWithPosOnlyArgs`)
 - Extra storage for code objects ( - **PEP 523**- `PyUnstable_Eval_RequestCodeExtraIndex()`(renamed from- `_PyEval_RequestCodeExtraIndex`)
- `PyUnstable_Code_GetExtra()`(renamed from- `_PyCode_GetExtra`)
- `PyUnstable_Code_SetExtra()`(renamed from- `_PyCode_SetExtra`)
 - The original names will continue to be available until the respective API changes. - (Contributed by Petr Viktorin in - [gh-101101](https://github.com/python/cpython/issues/101101).)
- **PEP 697**- `PyType_Spec.basicsize`
- `PyObject_GetTypeData()`- `PyType_GetTypeDataSize()`
- `Py_TPFLAGS_ITEMS_AT_END`- `PyObject_GetItemData()`- `PyType_Type`
- `Py_RELATIVE_OFFSET`- `members`
 - (Contributed by Petr Viktorin in - [gh-103509](https://github.com/python/cpython/issues/103509).)
- Add the new - [limited C API](../c-api/stable.html#limited-c-api)function- `PyType_FromMetaclass()`- `PyType_FromModuleAndSpec()`- [gh-93012](https://github.com/python/cpython/issues/93012).)
- API for creating objects that can be called using - [the vectorcall protocol](../c-api/call.html#vectorcall)was added to the- [Limited API](../c-api/stable.html#stable):- The - `Py_TPFLAGS_HAVE_VECTORCALL`- `__call__()`- `Py_TPFLAGS_IMMUTABLETYPE`- `tp_call`- `Py_TPFLAGS_HAVE_VECTORCALL`flag. (Contributed by Petr Viktorin in- [gh-93274](https://github.com/python/cpython/issues/93274).)- The - `Py_TPFLAGS_MANAGED_DICT`- `Py_TPFLAGS_MANAGED_WEAKREF`- `__dict__`
- API for performing calls using - [the vectorcall protocol](../c-api/call.html#vectorcall)was added to the- [Limited API](../c-api/stable.html#stable):- This means that both the incoming and outgoing ends of the vector call protocol are now available in the - [Limited API](../c-api/stable.html#stable). (Contributed by Wenzel Jakob in- [gh-98586](https://github.com/python/cpython/issues/98586).)
- Add two new public functions, - `PyEval_SetProfileAllThreads()`- `PyEval_SetTraceAllThreads()`- [gh-93503](https://github.com/python/cpython/issues/93503).)
- Add new function - `PyFunction_SetVectorcall()`- `PyFunctionObject`- [gh-92257](https://github.com/python/cpython/issues/92257).)
- The C API now permits registering callbacks via - `PyDict_AddWatcher()`- `PyDict_Watch()`- [gh-91052](https://github.com/python/cpython/issues/91052).)
- Add - `PyType_AddWatcher()`- `PyType_Watch()`- [gh-91051](https://github.com/python/cpython/issues/91051).)
- Add - `PyCode_AddWatcher()`- `PyCode_ClearWatcher()`- [gh-91054](https://github.com/python/cpython/issues/91054).)
- Add - `PyFrame_GetVar()`- `PyFrame_GetVarString()`- [gh-91248](https://github.com/python/cpython/issues/91248).)
- Add - `PyErr_GetRaisedException()`- `PyErr_SetRaisedException()`- `PyErr_Fetch()`- `PyErr_Restore()`- [gh-101578](https://github.com/python/cpython/issues/101578).)
- Add - `_PyErr_ChainExceptions1`, which takes an exception instance, to replace the legacy-API- `_PyErr_ChainExceptions`, which is now deprecated. (Contributed by Mark Shannon in- [gh-101578](https://github.com/python/cpython/issues/101578).)
- Add - `PyException_GetArgs()`- `PyException_SetArgs()`- `args`- [gh-101578](https://github.com/python/cpython/issues/101578).)
- Add - `PyErr_DisplayException()`- `PyErr_Display()`. (Contributed by Irit Katriel in- [gh-102755](https://github.com/python/cpython/issues/102755)).

- **PEP 683**- *Immortal Objects*, which allows objects to bypass reference counts, and related changes to the C-API:- `_Py_IMMORTAL_REFCNT`: The reference count that defines an object
- as immortal. 
 
- `_Py_IsImmortal`Checks if an object has the immortal reference count.
- `PyObject_HEAD_INIT`This will now initialize reference count to
- `_Py_IMMORTAL_REFCNT`when used with- `Py_BUILD_CORE`.
 
- `SSTATE_INTERNED_IMMORTAL`An identifier for interned unicode objects
- that are immortal. 
 
- `SSTATE_INTERNED_IMMORTAL_STATIC`An identifier for interned unicode
- objects that are immortal and static 
 
- `sys.getunicodeinternedsize`This returns the total number of unicode
- objects that have been interned. This is now needed for - `refleak.py`to correctly track reference counts and allocated blocks
 
 - (Contributed by Eddie Elizondo in - [gh-84436](https://github.com/python/cpython/issues/84436).)
- **PEP 684**- `Py_NewInterpreterFromConfig()`- `PyInterpreterConfig`- [PEP 684: A Per-Interpreter GIL](#whatsnew312-pep684)for more info.) (Contributed by Eric Snow in- [gh-104110](https://github.com/python/cpython/issues/104110).)
- In the limited C API version 3.12, - `Py_INCREF()`- `Py_DECREF()`- [gh-105387](https://github.com/python/cpython/issues/105387).)

### Porting to Python 3.12[¶](#id5)

- Legacy Unicode APIs based on - `Py_UNICODE*`representation has been removed. Please migrate to APIs based on UTF-8 or- `wchar_t*`.
- Argument parsing functions like - `PyArg_ParseTuple()`- `Py_UNICODE*`based format (e.g.- `u`,- `Z`) anymore. Please migrate to other formats for Unicode like- `s`,- `z`,- `es`, and- `U`.
- `tp_weaklist`for all static builtin types is always- `NULL`. This is an internal-only field on- `PyTypeObject`but we’re pointing out the change in case someone happens to be accessing the field directly anyway. To avoid breakage, consider using the existing public C-API instead, or, if necessary, the (internal-only)- `_PyObject_GET_WEAKREFS_LISTPTR()`macro.
- This internal-only - `PyTypeObject.tp_subclasses`- To get a list of subclasses, call the Python method - `__subclasses__()`- `PyObject_CallMethod()`
- Add support of more formatting options (left aligning, octals, uppercase hexadecimals, - `intmax_t`,- `ptrdiff_t`,- `wchar_t`C strings, variable width and precision) in- `PyUnicode_FromFormat()`- `PyUnicode_FromFormatV()`- [gh-98836](https://github.com/python/cpython/issues/98836).)
- An unrecognized format character in - `PyUnicode_FromFormat()`- `PyUnicode_FromFormatV()`- `SystemError`- [gh-95781](https://github.com/python/cpython/issues/95781).)
- Fix wrong sign placement in - `PyUnicode_FromFormat()`- `PyUnicode_FromFormatV()`- [gh-95504](https://github.com/python/cpython/issues/95504).)
- Extension classes wanting to add a - `__dict__`- `Py_TPFLAGS_MANAGED_DICT`- `Py_TPFLAGS_MANAGED_WEAKREF`- `tp_dictoffset`and- `tp_weaklistoffset`, respectively. The use of- `tp_dictoffset`and- `tp_weaklistoffset`is still supported, but does not fully support multiple inheritance (- [gh-95589](https://github.com/python/cpython/issues/95589)), and performance may be worse. Classes declaring- `Py_TPFLAGS_MANAGED_DICT`must call- `_PyObject_VisitManagedDict()`and- `_PyObject_ClearManagedDict()`to traverse and clear their instance’s dictionaries. To clear weakrefs, call- `PyObject_ClearWeakRefs()`
- The - `PyUnicode_FSDecoder()`- `bytearray`- `memoryview`- `bytes`- [gh-98393](https://github.com/python/cpython/issues/98393).)
- The - `Py_CLEAR`- `Py_SETREF`- `Py_XSETREF`- [gh-98724](https://github.com/python/cpython/issues/98724).)
- The interpreter’s error indicator is now always normalized. This means that - `PyErr_SetObject()`- `PyErr_SetString()`- [gh-101578](https://github.com/python/cpython/issues/101578).)
- `_Py_RefTotal`is no longer authoritative and only kept around for ABI compatibility. Note that it is an internal global and only available on debug builds. If you happen to be using it then you’ll need to start using- `_Py_GetGlobalRefTotal()`.
- The following functions now select an appropriate metaclass for the newly created type: - Creating classes whose metaclass overrides - `tp_new`- `tp_new`of the metaclass, possibly allowing incomplete initialization.- Note that - `PyType_FromMetaclass()`- `tp_new`(- `__new__()`- Since - `tp_new`overrides almost everything- `PyType_From*`functions do, the two are incompatible with each other. The existing behavior – ignoring the metaclass for several steps of type creation – is unsafe in general, since (meta)classes assume that- `tp_new`was called. There is no simple general workaround. One of the following may work for you:- If you control the metaclass, avoid using - `tp_new`in it:- If initialization can be skipped, it can be done in - `tp_init`
- If the metaclass doesn’t need to be instantiated from Python, set its - `tp_new`to- `NULL`using the- `Py_TPFLAGS_DISALLOW_INSTANTIATION`- `PyType_From*`functions.
 
- Avoid - `PyType_From*`functions: if you don’t need C-specific features (slots or setting the instance size), create types by- [calling](../c-api/call.html#call)the metaclass.
- If you - *know*the- `tp_new`can be skipped safely, filter the deprecation warning out using- `warnings.catch_warnings()`
 
- `PyOS_InputHook`- `PyOS_ReadlineFunctionPointer`- [subinterpreters](../c-api/subinterpreters.html#sub-interpreter-support). This is because clients generally rely on process-wide global state (since these callbacks have no way of recovering extension module state).- This also avoids situations where extensions may find themselves running in a subinterpreter that they don’t support (or haven’t yet been loaded in). See - [gh-104668](https://github.com/python/cpython/issues/104668)for more info.
- `PyLongObject`- `PyLongObject`are private, they are used by some extension modules. The internal fields should no longer be accessed directly, instead the API functions beginning- `PyLong_...`should be used instead. Two new- *unstable*API functions are provided for efficient access to the value of- `PyLongObject`s which fit into a single machine word:
- Custom allocators, set via - `PyMem_SetAllocator()`- `@ericsnowcurrently`.

### Deprecated[¶](#id6)

- In accordance with - **PEP 699**- `ma_version_tag`field in- `PyDictObject`- [gh-101193](https://github.com/python/cpython/issues/101193). PEP by Ken Jin.)
- Deprecate global configuration variable: 
- `Py_HashRandomizationFlag`- `PyConfig.use_hash_seed`- `PyConfig.hash_seed`
- `Py_LegacyWindowsFSEncodingFlag`- `PyPreConfig.legacy_windows_fs_encoding`
- `Py_LegacyWindowsStdioFlag`- `PyConfig.legacy_windows_stdio`
- `Py_FileSystemDefaultEncoding`: use- `PyConfig.filesystem_encoding`
- `Py_HasFileSystemDefaultEncoding`: use- `PyConfig.filesystem_encoding`
- `Py_FileSystemDefaultEncodeErrors`: use- `PyConfig.filesystem_errors`
- `Py_UTF8Mode`: use- `PyPreConfig.utf8_mode`- `Py_PreInitialize()`
 - The - `Py_InitializeFromConfig()`- `PyConfig`- [gh-77782](https://github.com/python/cpython/issues/77782).)
- Creating - `immutable types`- [gh-95388](https://github.com/python/cpython/issues/95388))
- The - `structmember.h`header is deprecated, though it continues to be available and there are no plans to remove it.- Its contents are now available just by including - `Python.h`, with a- `Py`prefix added if it was missing:
- Type macros like - `Py_T_INT`- `Py_T_DOUBLE`- `T_INT`,- `T_DOUBLE`, etc.)
- The flags - `Py_READONLY`- `READONLY`) and- `Py_AUDIT_READ`
 - Several items are not exposed from - `Python.h`:- `T_OBJECT`- `Py_T_OBJECT_EX`
- `T_NONE`
- The macro - `WRITE_RESTRICTED`which does nothing.
- The macros - `RESTRICTED`and- `READ_RESTRICTED`, equivalents of- `Py_AUDIT_READ`
- In some configurations, - `<stddef.h>`is not included from- `Python.h`. It should be included manually when using- `offsetof()`.
 - The deprecated header continues to provide its original contents under the original names. Your old code can stay unchanged, unless the extra include and non-namespaced macros bother you greatly. - (Contributed in - [gh-47146](https://github.com/python/cpython/issues/47146)by Petr Viktorin, based on earlier work by Alexander Belopolsky and Matthias Braun.)
- `PyErr_Fetch()`- `PyErr_Restore()`- `PyErr_GetRaisedException()`- `PyErr_SetRaisedException()`- [gh-101578](https://github.com/python/cpython/issues/101578).)
- `PyErr_Display()`is deprecated. Use- `PyErr_DisplayException()`- [gh-102755](https://github.com/python/cpython/issues/102755)).
- `_PyErr_ChainExceptions`is deprecated. Use- `_PyErr_ChainExceptions1`instead. (Contributed by Irit Katriel in- [gh-102192](https://github.com/python/cpython/issues/102192).)
- Using - `PyType_FromSpec()`- `PyType_FromSpecWithBases()`- `PyType_FromModuleAndSpec()`- `tp_new`

#### Pending removal in Python 3.14[¶](#id7)

- The - `ma_version_tag`field in- `PyDictObject`- **PEP 699**- [gh-101193](https://github.com/python/cpython/issues/101193)).
- Creating - `immutable types`- [gh-95388](https://github.com/python/cpython/issues/95388)).

#### Pending removal in Python 3.15[¶](#id8)

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

#### Pending removal in Python 3.16[¶](#id9)

- The bundled copy of - `libmpdec`.

#### Pending removal in future versions[¶](#id10)

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
 

### Removed[¶](#id11)

- Remove the - `token.h`header file. There was never any public tokenizer C API. The- `token.h`header file was only designed to be used by Python internals. (Contributed by Victor Stinner in- [gh-92651](https://github.com/python/cpython/issues/92651).)
- Legacy Unicode APIs have been removed. See - **PEP 623**- `PyUnicode_WCHAR_KIND`
- `PyUnicode_AS_UNICODE()`
- `PyUnicode_AsUnicode()`
- `PyUnicode_AsUnicodeAndSize()`
- `PyUnicode_AS_DATA()`
- `PyUnicode_FromUnicode()`
- `PyUnicode_GET_SIZE()`
- `PyUnicode_GetSize()`
- `PyUnicode_GET_DATA_SIZE()`
 
- Remove the - `PyUnicode_InternImmortal()`function macro. (Contributed by Victor Stinner in- [gh-85858](https://github.com/python/cpython/issues/85858).)