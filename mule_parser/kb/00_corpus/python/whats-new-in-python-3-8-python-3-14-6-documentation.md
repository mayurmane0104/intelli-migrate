# What’s New In Python 3.8 — Python 3.14.6 documentation

**Source:** [https://docs.python.org/whatsnew/3.8.html](https://docs.python.org/whatsnew/3.8.html)

---

# What’s New In Python 3.8[¶](#what-s-new-in-python-3-8)

- Editor:
- Raymond Hettinger 

This article explains the new features in Python 3.8, compared to 3.7.
Python 3.8 was released on October 14, 2019.
For full details, see the [changelog](changelog.html#changelog).

## Summary – Release highlights[¶](#summary-release-highlights)

## New Features[¶](#new-features)

### Assignment expressions[¶](#assignment-expressions)

There is new syntax `:=` that assigns values to variables as part of a larger
expression. It is affectionately known as “the walrus operator” due to
its resemblance to [the eyes and tusks of a walrus](https://en.wikipedia.org/wiki/Walrus#/media/File:Pacific_Walrus_-_Bull_(8247646168).jpg).

In this example, the assignment expression helps avoid calling
[ len()](../library/functions.html#len) twice:

```
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")
```
A similar benefit arises during regular expression matching where match objects are needed twice, once to test whether a match occurred and another to extract a subgroup:

```
discount = 0.0
if (mo := re.search(r'(\d+)% discount', advertisement)):
    discount = float(mo.group(1)) / 100.0
```
The operator is also useful with while-loops that compute a value to test loop termination and then need that same value again in the body of the loop:

```
# Loop over fixed length blocks
while (block := f.read(256)) != '':
    process(block)
```
Another motivating use case arises in list comprehensions where a value computed in a filtering condition is also needed in the expression body:

```
[clean_name.title() for name in names
 if (clean_name := normalize('NFC', name)) in allowed_names]
```
Try to limit use of the walrus operator to clean cases that reduce complexity and improve readability.

See [ PEP 572](https://peps.python.org/pep-0572/) for a full description.

(Contributed by Emily Morehouse in [bpo-35224](https://bugs.python.org/issue?@action=redirect&bpo=35224).)

### Positional-only parameters[¶](#positional-only-parameters)

There is a new function parameter syntax `/` to indicate that some
function parameters must be specified positionally and cannot be used as
keyword arguments.  This is the same notation shown by `help()` for C
functions annotated with Larry Hastings’
[Argument Clinic](https://devguide.python.org/development-tools/clinic/) tool.

In the following example, parameters *a* and *b* are positional-only,
while *c* or *d* can be positional or keyword, and *e* or *f* are
required to be keywords:

```
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
```
The following is a valid call:

```
f(10, 20, 30, d=40, e=50, f=60)
```
However, these are invalid calls:

```
f(10, b=20, c=30, d=40, e=50, f=60)   # b cannot be a keyword argument
f(10, 20, 30, 40, 50, f=60)           # e must be a keyword argument
```
One use case for this notation is that it allows pure Python functions
to fully emulate behaviors of existing C coded functions.  For example,
the built-in [ divmod()](../library/functions.html#divmod) function does not accept keyword arguments:

```
def divmod(a, b, /):
    "Emulate the built in divmod() function"
    return (a // b, a % b)
```
Another use case is to preclude keyword arguments when the parameter
name is not helpful.  For example, the builtin [ len()](../library/functions.html#len) function has
the signature 

`len(obj, /)`.  This precludes awkward calls such as:```
len(obj='hello')  # The "obj" keyword argument impairs readability
```
A further benefit of marking a parameter as positional-only is that it
allows the parameter name to be changed in the future without risk of
breaking client code.  For example, in the [ statistics](../library/statistics.html#module-statistics) module, the
parameter name 

*dist*may be changed in the future. This was made possible with the following function specification:

```
def quantiles(dist, /, *, n=4, method='exclusive')
    ...
```
Since the parameters to the left of `/` are not exposed as possible
keywords, the parameters names remain available for use in `**kwargs`:

```
>>> def f(a, b, /, **kwargs):
...     print(a, b, kwargs)
...
>>> f(10, 20, a=1, b=2, c=3)         # a and b are used in two ways
10 20 {'a': 1, 'b': 2, 'c': 3}
```
This greatly simplifies the implementation of functions and methods
that need to accept arbitrary keyword arguments.  For example, here
is an excerpt from code in the [ collections](../library/collections.html#module-collections) module:

```
class Counter(dict):
    def __init__(self, iterable=None, /, **kwds):
        # Note "iterable" is a possible keyword argument
```
See [ PEP 570](https://peps.python.org/pep-0570/) for a full description.

(Contributed by Pablo Galindo in [bpo-36540](https://bugs.python.org/issue?@action=redirect&bpo=36540).)

### Parallel filesystem cache for compiled bytecode files[¶](#parallel-filesystem-cache-for-compiled-bytecode-files)

The new [ PYTHONPYCACHEPREFIX](../using/cmdline.html#envvar-PYTHONPYCACHEPREFIX) setting (also available as


`-X``pycache_prefix`) configures the implicit bytecode
cache to use a separate parallel filesystem tree, rather than
the default `__pycache__` subdirectories within each source
directory.The location of the cache is reported in [ sys.pycache_prefix](../library/sys.html#sys.pycache_prefix)
(

[indicates the default location in](../library/constants.html#None)

`None``__pycache__`
subdirectories).(Contributed by Carl Meyer in [bpo-33499](https://bugs.python.org/issue?@action=redirect&bpo=33499).)

### Debug build uses the same ABI as release build[¶](#debug-build-uses-the-same-abi-as-release-build)

The ABI of Python [debug builds](../using/configure.html#debug-build)  is now compatible with
Python release builds. On Unix, when Python is built in debug mode, it is now
possible to load C extensions built in release mode and C extensions built
using the stable ABI. The inverse is not true, as debug builds expose
additional symbols not available in release builds.

Defining the `Py_DEBUG` macro no longer implies the `Py_TRACE_REFS` macro,
which introduces the only ABI incompatibility. The `Py_TRACE_REFS` macro,
which adds the [ sys.getobjects()](../library/sys.html#sys.getobjects) function and the 

[environment variable, can be set using the new](../using/cmdline.html#envvar-PYTHONDUMPREFS)

`PYTHONDUMPREFS`[build option. (Contributed by Victor Stinner in](../using/configure.html#cmdoption-with-trace-refs)

```
./configure
--with-trace-refs
```
[bpo-36465](https://bugs.python.org/issue?@action=redirect&bpo=36465).)

On Unix, C extensions are no longer linked to libpython except on Android
and Cygwin.
It is now possible
for a statically linked Python to load a C extension built using a shared
library Python.
(Contributed by Victor Stinner in [bpo-21536](https://bugs.python.org/issue?@action=redirect&bpo=21536).)

On Unix, when Python is built in debug mode, import now also looks for C
extensions compiled in release mode and for C extensions compiled with the
stable ABI.
(Contributed by Victor Stinner in [bpo-36722](https://bugs.python.org/issue?@action=redirect&bpo=36722).)

To embed Python into an application, a new `--embed` option must be passed to
`python3-config --libs --embed` to get `-lpython3.8` (link the application
to libpython). To support both 3.8 and older, try ```
python3-config --libs
--embed
```
 first and fallback to `python3-config --libs` (without `--embed`)
if the previous command fails.

Add a pkg-config `python-3.8-embed` module to embed Python into an
application: `pkg-config python-3.8-embed --libs` includes `-lpython3.8`.
To support both 3.8 and older, try `pkg-config python-X.Y-embed --libs` first
and fallback to `pkg-config python-X.Y --libs` (without `--embed`) if the
previous command fails (replace `X.Y` with the Python version).

On the other hand, `pkg-config python3.8 --libs` no longer contains
`-lpython3.8`. C extensions must not be linked to libpython (except on
Android and Cygwin, whose cases are handled by the script);
this change is backward incompatible on purpose.
(Contributed by Victor Stinner in [bpo-36721](https://bugs.python.org/issue?@action=redirect&bpo=36721).)

### f-strings support `=` for self-documenting expressions and debugging[¶](#f-strings-support-for-self-documenting-expressions-and-debugging)

Added an `=` specifier to [f-string](../glossary.html#term-f-string)s. An f-string such as
`f'{expr=}'` will expand to the text of the expression, an equal sign,
then the representation of the evaluated expression.  For example:

```
>>> import datetime as dt
>>> user = 'eric_idle'
>>> member_since = dt.date(1975, 7, 31)
>>> f'{user=} {member_since=}'
"user='eric_idle' member_since=datetime.date(1975, 7, 31)"
```
The usual [f-string format specifiers](../reference/lexical_analysis.html#f-strings) allow more
control over how the result of the expression is displayed:

```
>>> delta = dt.date.today() - member_since
>>> f'{user=!s}  {delta.days=:,d}'
'user=eric_idle  delta.days=16,075'
```
The `=` specifier will display the whole expression so that
calculations can be shown:

```
>>> print(f'{theta=}  {cos(radians(theta))=:.3f}')
theta=30  cos(radians(theta))=0.866
```
(Contributed by Eric V. Smith and Larry Hastings in [bpo-36817](https://bugs.python.org/issue?@action=redirect&bpo=36817).)

### PEP 578: Python Runtime Audit Hooks[¶](#pep-578-python-runtime-audit-hooks)

The PEP adds an Audit Hook and Verified Open Hook. Both are available from Python and native code, allowing applications and frameworks written in pure Python code to take advantage of extra notifications, while also allowing embedders or system administrators to deploy builds of Python where auditing is always enabled.

See [ PEP 578](https://peps.python.org/pep-0578/) for full details.

### PEP 587: Python Initialization Configuration[¶](#pep-587-python-initialization-configuration)

The [ PEP 587](https://peps.python.org/pep-0587/) adds a new C API to configure the Python Initialization
providing finer control on the whole configuration and better error reporting.

New structures:

New functions:

This PEP also adds `_PyRuntimeState.preconfig` ([ PyPreConfig](../c-api/init_config.html#c.PyPreConfig) type)
and 

`PyInterpreterState.config` ([type) fields to these internal structures.](../c-api/init_config.html#c.PyConfig)

`PyConfig``PyInterpreterState.config` becomes the new
reference configuration, replacing global configuration variables and
other private variables.See [Python Initialization Configuration](../c-api/init_config.html#init-config) for the
documentation.

See [ PEP 587](https://peps.python.org/pep-0587/) for a full description.

(Contributed by Victor Stinner in [bpo-36763](https://bugs.python.org/issue?@action=redirect&bpo=36763).)

### PEP 590: Vectorcall: a fast calling protocol for CPython[¶](#pep-590-vectorcall-a-fast-calling-protocol-for-cpython)

[The Vectorcall Protocol](../c-api/call.html#vectorcall) is added to the Python/C API.
It is meant to formalize existing optimizations which were already done
for various classes.
Any [static type](../c-api/typeobj.html#static-types) implementing a callable can use this
protocol.

This is currently provisional. The aim is to make it fully public in Python 3.9.

See [ PEP 590](https://peps.python.org/pep-0590/) for a full description.

(Contributed by Jeroen Demeyer, Mark Shannon and Petr Viktorin in [bpo-36974](https://bugs.python.org/issue?@action=redirect&bpo=36974).)

### Pickle protocol 5 with out-of-band data buffers[¶](#pickle-protocol-5-with-out-of-band-data-buffers)

When [ pickle](../library/pickle.html#module-pickle) is used to transfer large data between Python processes
in order to take advantage of multi-core or multi-machine processing,
it is important to optimize the transfer by reducing memory copies, and
possibly by applying custom techniques such as data-dependent compression.

The [ pickle](../library/pickle.html#module-pickle) protocol 5 introduces support for out-of-band buffers
where 

[-compatible data can be transmitted separately from the main pickle stream, at the discretion of the communication layer.](https://peps.python.org/pep-3118/)

**PEP 3118**See [ PEP 574](https://peps.python.org/pep-0574/) for a full description.

(Contributed by Antoine Pitrou in [bpo-36785](https://bugs.python.org/issue?@action=redirect&bpo=36785).)

## Other Language Changes[¶](#other-language-changes)

- A - `continue`- `finally`- [bpo-32489](https://bugs.python.org/issue?@action=redirect&bpo=32489).)
- The - `bool`- `int`- `fractions.Fraction`- `as_integer_ratio()`- `float`- `decimal.Decimal`- `numerator, denominator = x.as_integer_ratio()`and have it work across multiple numeric types. (Contributed by Lisa Roach in- [bpo-33073](https://bugs.python.org/issue?@action=redirect&bpo=33073)and Raymond Hettinger in- [bpo-37819](https://bugs.python.org/issue?@action=redirect&bpo=37819).)
- Constructors of - `int`- `float`- `complex`- `__index__()`- `__int__()`- `__float__()`- `__complex__()`- [bpo-20092](https://bugs.python.org/issue?@action=redirect&bpo=20092).)
- Added support of - `\N{`escapes in- *name*}- `regular expressions`- >>> notice = 'Copyright © 2019' >>> copyright_year_pattern = re.compile(r'\N{copyright sign}\s*(\d{4})') >>> int(copyright_year_pattern.search(notice).group(1)) 2019 - (Contributed by Jonathan Eunice and Serhiy Storchaka in - [bpo-30688](https://bugs.python.org/issue?@action=redirect&bpo=30688).)
- Dict and dictviews are now iterable in reversed insertion order using - `reversed()`- [bpo-33462](https://bugs.python.org/issue?@action=redirect&bpo=33462).)
- The syntax allowed for keyword names in function calls was further restricted. In particular, - `f((keyword)=arg)`is no longer allowed. It was never intended to permit more than a bare name on the left-hand side of a keyword argument assignment term. (Contributed by Benjamin Peterson in- [bpo-34641](https://bugs.python.org/issue?@action=redirect&bpo=34641).)
- Generalized iterable unpacking in - `yield`- `return`- *yield*and- *return*syntax into better agreement with normal assignment syntax:- >>> def parse(family): ... lastname, *members = family.split() ... return lastname.upper(), *members ... >>> parse('simpsons homer marge bart lisa maggie') ('SIMPSONS', 'homer', 'marge', 'bart', 'lisa', 'maggie') - (Contributed by David Cuthbert and Jordan Chapman in - [bpo-32117](https://bugs.python.org/issue?@action=redirect&bpo=32117).)
- When a comma is missed in code such as - `[(10, 20) (30, 40)]`, the compiler displays a- `SyntaxWarning`- `TypeError`- [bpo-15248](https://bugs.python.org/issue?@action=redirect&bpo=15248).)
- Arithmetic operations between subclasses of - `datetime.date`- `datetime.datetime`- `datetime.timedelta`- `datetime.timedelta`arithmetic, such as- `astimezone()`- [bpo-32417](https://bugs.python.org/issue?@action=redirect&bpo=32417).)
- When the Python interpreter is interrupted by Ctrl-C (SIGINT) and the resulting - `KeyboardInterrupt`- [bpo-1054041](https://bugs.python.org/issue?@action=redirect&bpo=1054041).)
- Some advanced styles of programming require updating the - `types.CodeType`- `replace()`method makes it possible to create a clone with a few altered parameters.- Here’s an example that alters the - `statistics.mean()`- *data*parameter from being used as a keyword argument:- >>> from statistics import mean >>> mean(data=[10, 20, 90]) 40 >>> mean.__code__ = mean.__code__.replace(co_posonlyargcount=1) >>> mean(data=[10, 20, 90]) Traceback (most recent call last): ... TypeError: mean() got some positional-only arguments passed as keyword arguments: 'data' - (Contributed by Victor Stinner in - [bpo-37032](https://bugs.python.org/issue?@action=redirect&bpo=37032).)
- For integers, the three-argument form of the - `pow()`- `-1`, and a suitable power of that inverse for other negative exponents. For example, to compute the- [modular multiplicative inverse](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse)of 38 modulo 137, write:- >>> pow(38, -1, 137) 119 >>> 119 * 38 % 137 1 - Modular inverses arise in the solution of - [linear Diophantine equations](https://en.wikipedia.org/wiki/Diophantine_equation). For example, to find integer solutions for- `4258𝑥 + 147𝑦 = 369`, first rewrite as- `4258𝑥 ≡ 369 (mod 147)`then solve:- >>> x = 369 * pow(4258, -1, 147) % 147 >>> y = (4258 * x - 369) // -147 >>> 4258 * x + 147 * y 369 - (Contributed by Mark Dickinson in - [bpo-36027](https://bugs.python.org/issue?@action=redirect&bpo=36027).)
- Dict comprehensions have been synced-up with dict literals so that the key is computed first and the value second: - >>> # Dict comprehension >>> cast = {input('role? '): input('actor? ') for i in range(2)} role? King Arthur actor? Chapman role? Black Knight actor? Cleese >>> # Dict literal >>> cast = {input('role? '): input('actor? ')} role? Sir Robin actor? Eric Idle - The guaranteed execution order is helpful with assignment expressions because variables assigned in the key expression will be available in the value expression: - >>> names = ['Martin von Löwis', 'Łukasz Langa', 'Walter Dörwald'] >>> {(n := normalize('NFC', name)).casefold() : n for name in names} {'martin von löwis': 'Martin von Löwis', 'łukasz langa': 'Łukasz Langa', 'walter dörwald': 'Walter Dörwald'} - (Contributed by Jörn Heissler in - [bpo-35224](https://bugs.python.org/issue?@action=redirect&bpo=35224).)
- The - `object.__reduce__()`- `(obj, state)`signature. This allows the direct control over the state-updating behavior of a specific object. If not- *None*, this callable will have priority over the object’s- `__setstate__()`- [bpo-35900](https://bugs.python.org/issue?@action=redirect&bpo=35900).)

## New Modules[¶](#new-modules)

- The new - `importlib.metadata`- >>> # Note following example requires that the popular "requests" >>> # package has been installed. >>> >>> from importlib.metadata import version, requires, files >>> version('requests') '2.22.0' >>> list(requires('requests')) ['chardet (<3.1.0,>=3.0.2)'] >>> list(files('requests'))[:5] [PackagePath('requests-2.22.0.dist-info/INSTALLER'), PackagePath('requests-2.22.0.dist-info/LICENSE'), PackagePath('requests-2.22.0.dist-info/METADATA'), PackagePath('requests-2.22.0.dist-info/RECORD'), PackagePath('requests-2.22.0.dist-info/WHEEL')] - (Contributed by Barry Warsaw and Jason R. Coombs in - [bpo-34632](https://bugs.python.org/issue?@action=redirect&bpo=34632).)

## Improved Modules[¶](#improved-modules)

### ast[¶](#ast)

AST nodes now have `end_lineno` and `end_col_offset` attributes,
which give the precise location of the end of the node.  (This only
applies to nodes that have `lineno` and `col_offset` attributes.)

New function [ ast.get_source_segment()](../library/ast.html#ast.get_source_segment) returns the source code
for a specific AST node.

(Contributed by Ivan Levkivskyi in [bpo-33416](https://bugs.python.org/issue?@action=redirect&bpo=33416).)

The [ ast.parse()](../library/ast.html#ast.parse) function has some new flags:

- `type_comments=True`causes it to return the text of- **PEP 484**- **PEP 526**
- `mode='func_type'`can be used to parse- **PEP 484**
- `feature_version=(3, N)`allows specifying an earlier Python 3 version. For example,- `feature_version=(3, 4)`will treat- `async`- `await`

(Contributed by Guido van Rossum in [bpo-35766](https://bugs.python.org/issue?@action=redirect&bpo=35766).)

### asyncio[¶](#asyncio)

[ asyncio.run()](../library/asyncio-runner.html#asyncio.run) has graduated from the provisional to stable API. This
function can be used to execute a 

[coroutine](../glossary.html#term-coroutine)and return the result while automatically managing the event loop. For example:

```
import asyncio
async def main():
    await asyncio.sleep(0)
    return 42
asyncio.run(main())
```
This is *roughly* equivalent to:

```
import asyncio
async def main():
    await asyncio.sleep(0)
    return 42
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
try:
    loop.run_until_complete(main())
finally:
    asyncio.set_event_loop(None)
    loop.close()
```
The actual implementation is significantly more complex. Thus,
[ asyncio.run()](../library/asyncio-runner.html#asyncio.run) should be the preferred way of running asyncio programs.

(Contributed by Yury Selivanov in [bpo-32314](https://bugs.python.org/issue?@action=redirect&bpo=32314).)

Running `python -m asyncio` launches a natively async REPL.  This allows rapid
experimentation with code that has a top-level [ await](../reference/expressions.html#await).  There is no
longer a need to directly call 

`asyncio.run()` which would spawn a new event
loop on every invocation:```
$ python -m asyncio
asyncio REPL 3.8.0
Use "await" directly instead of "asyncio.run()".
Type "help", "copyright", "credits" or "license" for more information.
>>> import asyncio
>>> await asyncio.sleep(10, result='hello')
hello
```
(Contributed by Yury Selivanov in [bpo-37028](https://bugs.python.org/issue?@action=redirect&bpo=37028).)

The exception [ asyncio.CancelledError](../library/asyncio-exceptions.html#asyncio.CancelledError) now inherits from

[rather than](../library/exceptions.html#BaseException)

`BaseException`[and no longer inherits from](../library/exceptions.html#Exception)

`Exception`[. (Contributed by Yury Selivanov in](../library/concurrent.futures.html#concurrent.futures.CancelledError)

`concurrent.futures.CancelledError`[bpo-32528](https://bugs.python.org/issue?@action=redirect&bpo=32528).)

On Windows, the default event loop is now [ ProactorEventLoop](../library/asyncio-eventloop.html#asyncio.ProactorEventLoop).
(Contributed by Victor Stinner in 

[bpo-34687](https://bugs.python.org/issue?@action=redirect&bpo=34687).)

[ ProactorEventLoop](../library/asyncio-eventloop.html#asyncio.ProactorEventLoop) now also supports UDP.
(Contributed by Adam Meily and Andrew Svetlov in 

[bpo-29883](https://bugs.python.org/issue?@action=redirect&bpo=29883).)

[ ProactorEventLoop](../library/asyncio-eventloop.html#asyncio.ProactorEventLoop) can now be interrupted by

[(“CTRL+C”). (Contributed by Vladimir Matveev in](../library/exceptions.html#KeyboardInterrupt)

`KeyboardInterrupt`[bpo-23057](https://bugs.python.org/issue?@action=redirect&bpo=23057).)

Added [ asyncio.Task.get_coro()](../library/asyncio-task.html#asyncio.Task.get_coro) for getting the wrapped coroutine
within an 

[. (Contributed by Alex Grönholm in](../library/asyncio-task.html#asyncio.Task)

`asyncio.Task`[bpo-36999](https://bugs.python.org/issue?@action=redirect&bpo=36999).)

Asyncio tasks can now be named, either by passing the `name` keyword
argument to [ asyncio.create_task()](../library/asyncio-task.html#asyncio.create_task) or
the 

[event loop method, or by calling the](../library/asyncio-eventloop.html#asyncio.loop.create_task)

`create_task()`[method on the task object. The task name is visible in the](../library/asyncio-task.html#asyncio.Task.set_name)

`set_name()``repr()` output of [and can also be retrieved using the](../library/asyncio-task.html#asyncio.Task)

`asyncio.Task`[method. (Contributed by Alex Grönholm in](../library/asyncio-task.html#asyncio.Task.get_name)

`get_name()`[bpo-34270](https://bugs.python.org/issue?@action=redirect&bpo=34270).)

Added support for
[Happy Eyeballs](https://en.wikipedia.org/wiki/Happy_Eyeballs) to
[ asyncio.loop.create_connection()](../library/asyncio-eventloop.html#asyncio.loop.create_connection). To specify the behavior, two new
parameters have been added: 

*happy_eyeballs_delay*and

*interleave*. The Happy Eyeballs algorithm improves responsiveness in applications that support IPv4 and IPv6 by attempting to simultaneously connect using both. (Contributed by twisteroid ambassador in

[bpo-33530](https://bugs.python.org/issue?@action=redirect&bpo=33530).)

### builtins[¶](#builtins)

The [ compile()](../library/functions.html#compile) built-in has been improved to accept the

`ast.PyCF_ALLOW_TOP_LEVEL_AWAIT` flag. With this new flag passed,
`compile()` will allow top-level `await`, `async for` and `async with`
constructs that are usually considered invalid syntax. Asynchronous code object
marked with the `CO_COROUTINE` flag may then be returned.
(Contributed by Matthias Bussonnier in [bpo-34616](https://bugs.python.org/issue?@action=redirect&bpo=34616))

### collections[¶](#collections)

The [ _asdict()](../library/collections.html#collections.somenamedtuple._asdict) method for

[now returns a](../library/collections.html#collections.namedtuple)

`collections.namedtuple()`[instead of a](../library/stdtypes.html#dict)

`dict`[. This works because regular dicts have guaranteed ordering since Python 3.7. If the extra features of](../library/collections.html#collections.OrderedDict)

`collections.OrderedDict``OrderedDict` are required, the suggested remediation is to cast the
result to the desired type: `OrderedDict(nt._asdict())`.
(Contributed by Raymond Hettinger in [bpo-35864](https://bugs.python.org/issue?@action=redirect&bpo=35864).)

### cProfile[¶](#cprofile)

The [ cProfile.Profile](../library/profile.html#profile.Profile) class can now be used as a context manager.
Profile a block of code by running:

```
import cProfile
with cProfile.Profile() as profiler:
      # code to be profiled
      ...
```
(Contributed by Scott Sanderson in [bpo-29235](https://bugs.python.org/issue?@action=redirect&bpo=29235).)

### csv[¶](#csv)

The [ csv.DictReader](../library/csv.html#csv.DictReader) now returns instances of 

[instead of a](../library/stdtypes.html#dict)

`dict`[. The tool is now faster and uses less memory while still preserving the field order. (Contributed by Michael Selik in](../library/collections.html#collections.OrderedDict)

`collections.OrderedDict`[bpo-34003](https://bugs.python.org/issue?@action=redirect&bpo=34003).)

### curses[¶](#curses)

Added a new variable holding structured version information for the
underlying ncurses library: [ ncurses_version](../library/curses.html#curses.ncurses_version).
(Contributed by Serhiy Storchaka in 

[bpo-31680](https://bugs.python.org/issue?@action=redirect&bpo=31680).)

### ctypes[¶](#ctypes)

On Windows, [ CDLL](../library/ctypes.html#ctypes.CDLL) and subclasses now accept a 

*winmode*parameter to specify flags for the underlying

`LoadLibraryEx` call. The default flags are
set to only load DLL dependencies from trusted locations, including the path
where the DLL is stored (if a full or partial path is used to load the initial
DLL) and paths added by [. (Contributed by Steve Dower in](../library/os.html#os.add_dll_directory)

`add_dll_directory()`[bpo-36085](https://bugs.python.org/issue?@action=redirect&bpo=36085).)

### datetime[¶](#datetime)

Added new alternate constructors [ datetime.date.fromisocalendar()](../library/datetime.html#datetime.date.fromisocalendar) and

[, which construct](../library/datetime.html#datetime.datetime.fromisocalendar)

`datetime.datetime.fromisocalendar()`[and](../library/datetime.html#datetime.date)

`date`[objects respectively from ISO year, week number, and weekday; these are the inverse of each class’s](../library/datetime.html#datetime.datetime)

`datetime``isocalendar` method.
(Contributed by Paul Ganssle in [bpo-36004](https://bugs.python.org/issue?@action=redirect&bpo=36004).)

### functools[¶](#functools)

[ functools.lru_cache()](../library/functools.html#functools.lru_cache) can now be used as a straight decorator rather
than as a function returning a decorator.  So both of these are now supported:

```
@lru_cache
def f(x):
    ...
@lru_cache(maxsize=256)
def f(x):
    ...
```
(Contributed by Raymond Hettinger in [bpo-36772](https://bugs.python.org/issue?@action=redirect&bpo=36772).)

Added a new [ functools.cached_property()](../library/functools.html#functools.cached_property) decorator, for computed properties
cached for the life of the instance.

```
import functools
import statistics
class Dataset:
   def __init__(self, sequence_of_numbers):
      self.data = sequence_of_numbers
   @functools.cached_property
   def variance(self):
      return statistics.variance(self.data)
```
(Contributed by Carl Meyer in [bpo-21145](https://bugs.python.org/issue?@action=redirect&bpo=21145))

Added a new [ functools.singledispatchmethod()](../library/functools.html#functools.singledispatchmethod) decorator that converts
methods into 

[generic functions](../glossary.html#term-generic-function)using

[single dispatch](../glossary.html#term-single-dispatch):

```
from functools import singledispatchmethod
from contextlib import suppress
class TaskManager:
    def __init__(self, tasks):
        self.tasks = list(tasks)
    @singledispatchmethod
    def discard(self, value):
        with suppress(ValueError):
            self.tasks.remove(value)
    @discard.register(list)
    def _(self, tasks):
        targets = set(tasks)
        self.tasks = [x for x in self.tasks if x not in targets]
```
(Contributed by Ethan Smith in [bpo-32380](https://bugs.python.org/issue?@action=redirect&bpo=32380))

### gc[¶](#gc)

[ get_objects()](../library/gc.html#gc.get_objects) can now receive an optional 

*generation*parameter indicating a generation to get objects from. (Contributed by Pablo Galindo in

[bpo-36016](https://bugs.python.org/issue?@action=redirect&bpo=36016).)

### gettext[¶](#gettext)

Added [ pgettext()](../library/gettext.html#gettext.pgettext) and its variants.
(Contributed by Franz Glasner, Éric Araujo, and Cheryl Sabella in 

[bpo-2504](https://bugs.python.org/issue?@action=redirect&bpo=2504).)

### gzip[¶](#gzip)

Added the *mtime* parameter to [ gzip.compress()](../library/gzip.html#gzip.compress) for reproducible output.
(Contributed by Guo Ci Teo in 

[bpo-34898](https://bugs.python.org/issue?@action=redirect&bpo=34898).)

A [ BadGzipFile](../library/gzip.html#gzip.BadGzipFile) exception is now raised instead of 

[for certain types of invalid or corrupt gzip files. (Contributed by Filip Gruszczyński, Michele Orrù, and Zackery Spytz in](../library/exceptions.html#OSError)

`OSError`[bpo-6584](https://bugs.python.org/issue?@action=redirect&bpo=6584).)

### IDLE and idlelib[¶](#idle-and-idlelib)

Output over N lines (50 by default) is squeezed down to a button.
N can be changed in the PyShell section of the General page of the
Settings dialog.  Fewer, but possibly extra long, lines can be squeezed by
right clicking on the output.  Squeezed output can be expanded in place
by double-clicking the button or into the clipboard or a separate window
by right-clicking the button.  (Contributed by Tal Einat in [bpo-1529353](https://bugs.python.org/issue?@action=redirect&bpo=1529353).)

Add “Run Customized” to the Run menu to run a module with customized
settings. Any command line arguments entered are added to sys.argv.
They also re-appear in the box for the next customized run.  One can also
suppress the normal Shell main module restart.  (Contributed by Cheryl
Sabella, Terry Jan Reedy, and others in [bpo-5680](https://bugs.python.org/issue?@action=redirect&bpo=5680) and [bpo-37627](https://bugs.python.org/issue?@action=redirect&bpo=37627).)

Added optional line numbers for IDLE editor windows. Windows
open without line numbers unless set otherwise in the General
tab of the configuration dialog.  Line numbers for an existing
window are shown and hidden in the Options menu.
(Contributed by Tal Einat and Saimadhav Heblikar in [bpo-17535](https://bugs.python.org/issue?@action=redirect&bpo=17535).)

OS native encoding is now used for converting between Python strings and Tcl
objects. This allows IDLE to work with emoji and other non-BMP characters.
These characters can be displayed or copied and pasted to or from the
clipboard.  Converting strings from Tcl to Python and back now never fails.
(Many people worked on this for eight years but the problem was finally
solved by Serhiy Storchaka in [bpo-13153](https://bugs.python.org/issue?@action=redirect&bpo=13153).)

New in 3.8.1:

Add option to toggle cursor blink off.  (Contributed by Zackery Spytz
in [bpo-4603](https://bugs.python.org/issue?@action=redirect&bpo=4603).)

Escape key now closes IDLE completion windows.  (Contributed by Johnny
Najera in [bpo-38944](https://bugs.python.org/issue?@action=redirect&bpo=38944).)

The changes above have been backported to 3.7 maintenance releases.

Add keywords to module name completion list.  (Contributed by Terry J.
Reedy in [bpo-37765](https://bugs.python.org/issue?@action=redirect&bpo=37765).)

### inspect[¶](#inspect)

The [ inspect.getdoc()](../library/inspect.html#inspect.getdoc) function can now find docstrings for 

`__slots__`
if that attribute is a [where the values are docstrings. This provides documentation options similar to what we already have for](../library/stdtypes.html#dict)

`dict`[,](../library/functions.html#property)

`property()`[, and](../library/functions.html#classmethod)

`classmethod()`[:](../library/functions.html#staticmethod)

`staticmethod()````
class AudioClip:
    __slots__ = {'bit_rate': 'expressed in kilohertz to one decimal place',
                 'duration': 'in seconds, rounded up to an integer'}
    def __init__(self, bit_rate, duration):
        self.bit_rate = round(bit_rate / 1000.0, 1)
        self.duration = ceil(duration)
```
(Contributed by Raymond Hettinger in [bpo-36326](https://bugs.python.org/issue?@action=redirect&bpo=36326).)

### io[¶](#io)

In development mode (`-X``env`) and in [debug build](../using/configure.html#debug-build), the
[ io.IOBase](../library/io.html#io.IOBase) finalizer now logs the exception if the 

`close()` method
fails. The exception is ignored silently by default in release build.
(Contributed by Victor Stinner in [bpo-18748](https://bugs.python.org/issue?@action=redirect&bpo=18748).)

### itertools[¶](#itertools)

The [ itertools.accumulate()](../library/itertools.html#itertools.accumulate) function added an option 

*initial*keyword argument to specify an initial value:

```
>>> from itertools import accumulate
>>> list(accumulate([10, 5, 30, 15], initial=1000))
[1000, 1010, 1015, 1045, 1060]
```
(Contributed by Lisa Roach in [bpo-34659](https://bugs.python.org/issue?@action=redirect&bpo=34659).)

### json.tool[¶](#json-tool)

Add option `--json-lines` to parse every input line as a separate JSON object.
(Contributed by Weipeng Hong in [bpo-31553](https://bugs.python.org/issue?@action=redirect&bpo=31553).)

### logging[¶](#logging)

Added a *force* keyword argument to [ logging.basicConfig()](../library/logging.html#logging.basicConfig).
When set to true, any existing handlers attached
to the root logger are removed and closed before carrying out the
configuration specified by the other arguments.

This solves a long-standing problem.  Once a logger or *basicConfig()* had
been called, subsequent calls to *basicConfig()* were silently ignored.
This made it difficult to update, experiment with, or teach the various
logging configuration options using the interactive prompt or a Jupyter
notebook.

(Suggested by Raymond Hettinger, implemented by Donghee Na, and
reviewed by Vinay Sajip in [bpo-33897](https://bugs.python.org/issue?@action=redirect&bpo=33897).)

### math[¶](#math)

Added new function [ math.dist()](../library/math.html#math.dist) for computing Euclidean distance
between two points.  (Contributed by Raymond Hettinger in 

[bpo-33089](https://bugs.python.org/issue?@action=redirect&bpo=33089).)

Expanded the [ math.hypot()](../library/math.html#math.hypot) function to handle multiple dimensions.
Formerly, it only supported the 2-D case.
(Contributed by Raymond Hettinger in 

[bpo-33089](https://bugs.python.org/issue?@action=redirect&bpo=33089).)

Added new function, [ math.prod()](../library/math.html#math.prod), as analogous function to 

[that returns the product of a ‘start’ value (default: 1) times an iterable of numbers:](../library/functions.html#sum)

`sum()````
>>> prior = 0.8
>>> likelihoods = [0.625, 0.84, 0.30]
>>> math.prod(likelihoods, start=prior)
0.126
```
(Contributed by Pablo Galindo in [bpo-35606](https://bugs.python.org/issue?@action=redirect&bpo=35606).)

Added two new combinatoric functions [ math.perm()](../library/math.html#math.perm) and 

[:](../library/math.html#math.comb)

`math.comb()````
>>> math.perm(10, 3)    # Permutations of 10 things taken 3 at a time
720
>>> math.comb(10, 3)    # Combinations of 10 things taken 3 at a time
120
```
(Contributed by Yash Aggarwal, Keller Fuchs, Serhiy Storchaka, and Raymond
Hettinger in [bpo-37128](https://bugs.python.org/issue?@action=redirect&bpo=37128), [bpo-37178](https://bugs.python.org/issue?@action=redirect&bpo=37178), and [bpo-35431](https://bugs.python.org/issue?@action=redirect&bpo=35431).)

Added a new function [ math.isqrt()](../library/math.html#math.isqrt) for computing accurate integer square
roots without conversion to floating point.  The new function supports
arbitrarily large integers.  It is faster than 

`floor(sqrt(n))` but slower
than [:](../library/math.html#math.sqrt)

`math.sqrt()````
>>> r = 650320427
>>> s = r ** 2
>>> isqrt(s - 1)         # correct
650320426
>>> floor(sqrt(s - 1))   # incorrect
650320427
```
(Contributed by Mark Dickinson in [bpo-36887](https://bugs.python.org/issue?@action=redirect&bpo=36887).)

The function [ math.factorial()](../library/math.html#math.factorial) no longer accepts arguments that are not
int-like. (Contributed by Pablo Galindo in 

[bpo-33083](https://bugs.python.org/issue?@action=redirect&bpo=33083).)

### mmap[¶](#mmap)

The [ mmap.mmap](../library/mmap.html#mmap.mmap) class now has an 

[method to access the](../library/mmap.html#mmap.mmap.madvise)

`madvise()``madvise()` system call.
(Contributed by Zackery Spytz in [bpo-32941](https://bugs.python.org/issue?@action=redirect&bpo=32941).)

### multiprocessing[¶](#multiprocessing)

Added new [ multiprocessing.shared_memory](../library/multiprocessing.shared_memory.html#module-multiprocessing.shared_memory) module.
(Contributed by Davin Potts in 

[bpo-35813](https://bugs.python.org/issue?@action=redirect&bpo=35813).)

On macOS, the *spawn* start method is now used by default.
(Contributed by Victor Stinner in [bpo-33725](https://bugs.python.org/issue?@action=redirect&bpo=33725).)

### os[¶](#os)

Added new function [ add_dll_directory()](../library/os.html#os.add_dll_directory) on Windows for providing
additional search paths for native dependencies when importing extension
modules or loading DLLs using 

[. (Contributed by Steve Dower in](../library/ctypes.html#module-ctypes)

`ctypes`[bpo-36085](https://bugs.python.org/issue?@action=redirect&bpo=36085).)

A new [ os.memfd_create()](../library/os.html#os.memfd_create) function was added to wrap the

`memfd_create()` syscall.
(Contributed by Zackery Spytz and Christian Heimes in [bpo-26836](https://bugs.python.org/issue?@action=redirect&bpo=26836).)

On Windows, much of the manual logic for handling reparse points (including
symlinks and directory junctions) has been delegated to the operating system.
Specifically, [ os.stat()](../library/os.html#os.stat) will now traverse anything supported by the
operating system, while 

[will only open reparse points that identify as “name surrogates” while others are opened as for](../library/os.html#os.lstat)

`os.lstat()``os.stat()`.
In all cases, [will only have](../library/os.html#os.stat_result.st_mode)

`os.stat_result.st_mode``S_IFLNK` set for
symbolic links and not other kinds of reparse points. To identify other kinds
of reparse point, check the new [attribute.](../library/os.html#os.stat_result.st_reparse_tag)

`os.stat_result.st_reparse_tag`On Windows, [ os.readlink()](../library/os.html#os.readlink) is now able to read directory junctions. Note
that 

[will return](../library/os.path.html#os.path.islink)

`islink()``False` for directory junctions,
and so code that checks `islink` first will continue to treat junctions as
directories, while code that handles errors from `os.readlink()` may now
treat junctions as links.(Contributed by Steve Dower in [bpo-37834](https://bugs.python.org/issue?@action=redirect&bpo=37834).)

### os.path[¶](#os-path)

[ os.path](../library/os.path.html#module-os.path) functions that return a boolean result like

[,](../library/os.path.html#os.path.exists)

`exists()`[,](../library/os.path.html#os.path.lexists)

`lexists()`[,](../library/os.path.html#os.path.isdir)

`isdir()`[,](../library/os.path.html#os.path.isfile)

`isfile()`[, and](../library/os.path.html#os.path.islink)

`islink()`[now return](../library/os.path.html#os.path.ismount)

`ismount()``False` instead of raising [or its subclasses](../library/exceptions.html#ValueError)

`ValueError`[and](../library/exceptions.html#UnicodeEncodeError)

`UnicodeEncodeError`[for paths that contain characters or bytes unrepresentable at the OS level. (Contributed by Serhiy Storchaka in](../library/exceptions.html#UnicodeDecodeError)

`UnicodeDecodeError`[bpo-33721](https://bugs.python.org/issue?@action=redirect&bpo=33721).)

[ expanduser()](../library/os.path.html#os.path.expanduser) on Windows now prefers the 

`USERPROFILE`
environment variable and does not use `HOME`, which is not normally set
for regular user accounts.
(Contributed by Anthony Sottile in [bpo-36264](https://bugs.python.org/issue?@action=redirect&bpo=36264).)

[ isdir()](../library/os.path.html#os.path.isdir) on Windows no longer returns 

`True` for a link to a
non-existent directory.[ realpath()](../library/os.path.html#os.path.realpath) on Windows now resolves reparse points, including
symlinks and directory junctions.

(Contributed by Steve Dower in [bpo-37834](https://bugs.python.org/issue?@action=redirect&bpo=37834).)

### pathlib[¶](#pathlib)

[ pathlib.Path](../library/pathlib.html#pathlib.Path) methods that return a boolean result like

[,](../library/pathlib.html#pathlib.Path.exists)

`exists()`[,](../library/pathlib.html#pathlib.Path.is_dir)

`is_dir()`[,](../library/pathlib.html#pathlib.Path.is_file)

`is_file()`[,](../library/pathlib.html#pathlib.Path.is_mount)

`is_mount()`[,](../library/pathlib.html#pathlib.Path.is_symlink)

`is_symlink()`[,](../library/pathlib.html#pathlib.Path.is_block_device)

`is_block_device()`[,](../library/pathlib.html#pathlib.Path.is_char_device)

`is_char_device()`[,](../library/pathlib.html#pathlib.Path.is_fifo)

`is_fifo()`[now return](../library/pathlib.html#pathlib.Path.is_socket)

`is_socket()``False` instead of raising
[or its subclass](../library/exceptions.html#ValueError)

`ValueError`[for paths that contain characters unrepresentable at the OS level. (Contributed by Serhiy Storchaka in](../library/exceptions.html#UnicodeEncodeError)

`UnicodeEncodeError`[bpo-33721](https://bugs.python.org/issue?@action=redirect&bpo=33721).)

Added `pathlib.Path.link_to()` which creates a hard link pointing
to a path.
(Contributed by Joannah Nanjekye in [bpo-26978](https://bugs.python.org/issue?@action=redirect&bpo=26978))
Note that `link_to` was deprecated in 3.10 and removed in 3.12 in
favor of a `hardlink_to` method added in 3.10 which matches the
semantics of the existing `symlink_to` method.

### pickle[¶](#pickle)

[ pickle](../library/pickle.html#module-pickle) extensions subclassing the C-optimized 

[can now override the pickling logic of functions and classes by defining the special](../library/pickle.html#pickle.Pickler)

`Pickler`[method. (Contributed by Pierre Glaser and Olivier Grisel in](../library/pickle.html#pickle.Pickler.reducer_override)

`reducer_override()`[bpo-35900](https://bugs.python.org/issue?@action=redirect&bpo=35900).)

### plistlib[¶](#plistlib)

Added new [ plistlib.UID](../library/plistlib.html#plistlib.UID) and enabled support for reading and writing
NSKeyedArchiver-encoded binary plists.
(Contributed by Jon Janzen in 

[bpo-26707](https://bugs.python.org/issue?@action=redirect&bpo=26707).)

### pprint[¶](#pprint)

The [ pprint](../library/pprint.html#module-pprint) module added a 

*sort_dicts*parameter to several functions. By default, those functions continue to sort dictionaries before rendering or printing. However, if

*sort_dicts*is set to false, the dictionaries retain the order that keys were inserted. This can be useful for comparison to JSON inputs during debugging.

In addition, there is a convenience new function, [ pprint.pp()](../library/pprint.html#pprint.pp) that is
like 

[but with](../library/pprint.html#pprint.pprint)

`pprint.pprint()`*sort_dicts*defaulting to

`False`:```
>>> from pprint import pprint, pp
>>> d = dict(source='input.txt', operation='filter', destination='output.txt')
>>> pp(d, width=40)                  # Original order
{'source': 'input.txt',
 'operation': 'filter',
 'destination': 'output.txt'}
>>> pprint(d, width=40)              # Keys sorted alphabetically
{'destination': 'output.txt',
 'operation': 'filter',
 'source': 'input.txt'}
```
(Contributed by Rémi Lapeyre in [bpo-30670](https://bugs.python.org/issue?@action=redirect&bpo=30670).)

### py_compile[¶](#py-compile)

[ py_compile.compile()](../library/py_compile.html#py_compile.compile) now supports silent mode.
(Contributed by Joannah Nanjekye in 

[bpo-22640](https://bugs.python.org/issue?@action=redirect&bpo=22640).)

### shlex[¶](#shlex)

The new [ shlex.join()](../library/shlex.html#shlex.join) function acts as the inverse of 

[. (Contributed by Bo Bayles in](../library/shlex.html#shlex.split)

`shlex.split()`[bpo-32102](https://bugs.python.org/issue?@action=redirect&bpo=32102).)

### shutil[¶](#shutil)

[ shutil.copytree()](../library/shutil.html#shutil.copytree) now accepts a new 

`dirs_exist_ok` keyword argument.
(Contributed by Josh Bronson in [bpo-20849](https://bugs.python.org/issue?@action=redirect&bpo=20849).)

[ shutil.make_archive()](../library/shutil.html#shutil.make_archive) now defaults to the modern pax (POSIX.1-2001)
format for new archives to improve portability and standards conformance,
inherited from the corresponding change to the 

[module. (Contributed by C.A.M. Gerlach in](../library/tarfile.html#module-tarfile)

`tarfile`[bpo-30661](https://bugs.python.org/issue?@action=redirect&bpo=30661).)

[ shutil.rmtree()](../library/shutil.html#shutil.rmtree) on Windows now removes directory junctions without
recursively removing their contents first.
(Contributed by Steve Dower in 

[bpo-37834](https://bugs.python.org/issue?@action=redirect&bpo=37834).)

### socket[¶](#socket)

Added [ create_server()](../library/socket.html#socket.create_server) and 

[convenience functions to automate the necessary tasks usually involved when creating a server socket, including accepting both IPv4 and IPv6 connections on the same socket. (Contributed by Giampaolo Rodolà in](../library/socket.html#socket.has_dualstack_ipv6)

`has_dualstack_ipv6()`[bpo-17561](https://bugs.python.org/issue?@action=redirect&bpo=17561).)

The [ socket.if_nameindex()](../library/socket.html#socket.if_nameindex), 

[, and](../library/socket.html#socket.if_nametoindex)

`socket.if_nametoindex()`[functions have been implemented on Windows. (Contributed by Zackery Spytz in](../library/socket.html#socket.if_indextoname)

`socket.if_indextoname()`[bpo-37007](https://bugs.python.org/issue?@action=redirect&bpo=37007).)

### ssl[¶](#ssl)

Added [ post_handshake_auth](../library/ssl.html#ssl.SSLContext.post_handshake_auth) to enable and

[to initiate TLS 1.3 post-handshake authentication. (Contributed by Christian Heimes in](../library/ssl.html#ssl.SSLSocket.verify_client_post_handshake)

`verify_client_post_handshake()`[bpo-34670](https://bugs.python.org/issue?@action=redirect&bpo=34670).)

### statistics[¶](#statistics)

Added [ statistics.fmean()](../library/statistics.html#statistics.fmean) as a faster, floating-point variant of

[. (Contributed by Raymond Hettinger and Steven D’Aprano in](../library/statistics.html#statistics.mean)

`statistics.mean()`[bpo-35904](https://bugs.python.org/issue?@action=redirect&bpo=35904).)

Added [ statistics.geometric_mean()](../library/statistics.html#statistics.geometric_mean)
(Contributed by Raymond Hettinger in 

[bpo-27181](https://bugs.python.org/issue?@action=redirect&bpo=27181).)

Added [ statistics.multimode()](../library/statistics.html#statistics.multimode) that returns a list of the most
common values. (Contributed by Raymond Hettinger in 

[bpo-35892](https://bugs.python.org/issue?@action=redirect&bpo=35892).)

Added [ statistics.quantiles()](../library/statistics.html#statistics.quantiles) that divides data or a distribution
in to equiprobable intervals (e.g. quartiles, deciles, or percentiles).
(Contributed by Raymond Hettinger in 

[bpo-36546](https://bugs.python.org/issue?@action=redirect&bpo=36546).)

Added [ statistics.NormalDist](../library/statistics.html#statistics.NormalDist), a tool for creating
and manipulating normal distributions of a random variable.
(Contributed by Raymond Hettinger in 

[bpo-36018](https://bugs.python.org/issue?@action=redirect&bpo=36018).)

```
>>> temperature_feb = NormalDist.from_samples([4, 12, -3, 2, 7, 14])
>>> temperature_feb.mean
6.0
>>> temperature_feb.stdev
6.356099432828281
>>> temperature_feb.cdf(3)            # Chance of being under 3 degrees
0.3184678262814532
>>> # Relative chance of being 7 degrees versus 10 degrees
>>> temperature_feb.pdf(7) / temperature_feb.pdf(10)
1.2039930378537762
>>> el_niño = NormalDist(4, 2.5)
>>> temperature_feb += el_niño        # Add in a climate effect
>>> temperature_feb
NormalDist(mu=10.0, sigma=6.830080526611674)
>>> temperature_feb * (9/5) + 32      # Convert to Fahrenheit
NormalDist(mu=50.0, sigma=12.294144947901014)
>>> temperature_feb.samples(3)        # Generate random samples
[7.672102882379219, 12.000027119750287, 4.647488369766392]
```
### sys[¶](#sys)

Add new [ sys.unraisablehook()](../library/sys.html#sys.unraisablehook) function which can be overridden to control
how “unraisable exceptions” are handled. It is called when an exception has
occurred but there is no way for Python to handle it. For example, when a
destructor raises an exception or during garbage collection
(

[). (Contributed by Victor Stinner in](../library/gc.html#gc.collect)

`gc.collect()`[bpo-36829](https://bugs.python.org/issue?@action=redirect&bpo=36829).)

### tarfile[¶](#tarfile)

The [ tarfile](../library/tarfile.html#module-tarfile) module now defaults to the modern pax (POSIX.1-2001)
format for new archives, instead of the previous GNU-specific one.
This improves cross-platform portability with a consistent encoding (UTF-8)
in a standardized and extensible format, and offers several other benefits.
(Contributed by C.A.M. Gerlach in 

[bpo-36268](https://bugs.python.org/issue?@action=redirect&bpo=36268).)

### threading[¶](#threading)

Add a new [ threading.excepthook()](../library/threading.html#threading.excepthook) function which handles uncaught

[exception. It can be overridden to control how uncaught](../library/threading.html#threading.Thread.run)

`threading.Thread.run()``threading.Thread.run()` exceptions are handled.
(Contributed by Victor Stinner in [bpo-1230540](https://bugs.python.org/issue?@action=redirect&bpo=1230540).)

Add a new [ threading.get_native_id()](../library/threading.html#threading.get_native_id) function and
a 

[attribute to the](../library/threading.html#threading.Thread.native_id)

`native_id`[class. These return the native integral Thread ID of the current thread assigned by the kernel. This feature is only available on certain platforms, see](../library/threading.html#threading.Thread)

`threading.Thread``get_native_id` for more information.
(Contributed by Jake Tesler in [bpo-36084](https://bugs.python.org/issue?@action=redirect&bpo=36084).)

### tokenize[¶](#tokenize)

The [ tokenize](../library/tokenize.html#module-tokenize) module now implicitly emits a 

`NEWLINE` token when
provided with input that does not have a trailing new line.  This behavior
now matches what the C tokenizer does internally.
(Contributed by Ammar Askar in [bpo-33899](https://bugs.python.org/issue?@action=redirect&bpo=33899).)

### tkinter[¶](#tkinter)

Added methods `selection_from()`,
`selection_present()`,
`selection_range()` and
`selection_to()`
in the `tkinter.Spinbox` class.
(Contributed by Juliette Monsel in [bpo-34829](https://bugs.python.org/issue?@action=redirect&bpo=34829).)

Added method `moveto()`
in the `tkinter.Canvas` class.
(Contributed by Juliette Monsel in [bpo-23831](https://bugs.python.org/issue?@action=redirect&bpo=23831).)

The `tkinter.PhotoImage` class now has
`transparency_get()` and
`transparency_set()` methods.  (Contributed by
Zackery Spytz in [bpo-25451](https://bugs.python.org/issue?@action=redirect&bpo=25451).)

### time[¶](#time)

Added new clock [ CLOCK_UPTIME_RAW](../library/time.html#time.CLOCK_UPTIME_RAW) for macOS 10.12.
(Contributed by Joannah Nanjekye in 

[bpo-35702](https://bugs.python.org/issue?@action=redirect&bpo=35702).)

### typing[¶](#typing)

The [ typing](../library/typing.html#module-typing) module incorporates several new features:

- A dictionary type with per-key types. See - **PEP 589**- `typing.TypedDict`- class Location(TypedDict, total=False): lat_long: tuple grid_square: str xy_coordinate: tuple 
- Literal types. See - **PEP 586**- `typing.Literal`- def get_status(port: int) -> Literal['connected', 'disconnected']: ... 
- “Final” variables, functions, methods and classes. See - **PEP 591**- `typing.Final`- `typing.final()`- pi: Final[float] = 3.1415926536 
- Protocol definitions. See - **PEP 544**- `typing.Protocol`- `typing.runtime_checkable()`- `typing.SupportsInt`- `Protocol`subclasses.
- New protocol class - `typing.SupportsIndex`
- New functions - `typing.get_origin()`- `typing.get_args()`

### unicodedata[¶](#unicodedata)

The [ unicodedata](../library/unicodedata.html#module-unicodedata) module has been upgraded to use the 

[Unicode 12.1.0](https://blog.unicode.org/2019/05/unicode-12-1-en.html)release.

New function [ is_normalized()](../library/unicodedata.html#unicodedata.is_normalized) can be used to verify a string
is in a specific normal form, often much faster than by actually normalizing
the string.  (Contributed by Max Belanger, David Euresti, and Greg Price in

[bpo-32285](https://bugs.python.org/issue?@action=redirect&bpo=32285)and

[bpo-37966](https://bugs.python.org/issue?@action=redirect&bpo=37966)).

### unittest[¶](#unittest)

Added [ AsyncMock](../library/unittest.mock.html#unittest.mock.AsyncMock) to support an asynchronous version of

[. Appropriate new assert functions for testing have been added as well. (Contributed by Lisa Roach in](../library/unittest.mock.html#unittest.mock.Mock)

`Mock`[bpo-26467](https://bugs.python.org/issue?@action=redirect&bpo=26467)).

Added [ addModuleCleanup()](../library/unittest.html#unittest.addModuleCleanup) and

[to unittest to support cleanups for](../library/unittest.html#unittest.TestCase.addClassCleanup)

`addClassCleanup()`[and](../library/unittest.html#unittest.setUpModule)

`setUpModule()`[. (Contributed by Lisa Roach in](../library/unittest.html#unittest.TestCase.setUpClass)

`setUpClass()`[bpo-24412](https://bugs.python.org/issue?@action=redirect&bpo=24412).)

Several mock assert functions now also print a list of actual calls upon
failure. (Contributed by Petter Strandmark in [bpo-35047](https://bugs.python.org/issue?@action=redirect&bpo=35047).)

[ unittest](../library/unittest.html#module-unittest) module gained support for coroutines to be used as test cases
with 

[. (Contributed by Andrew Svetlov in](../library/unittest.html#unittest.IsolatedAsyncioTestCase)

`unittest.IsolatedAsyncioTestCase`[bpo-32972](https://bugs.python.org/issue?@action=redirect&bpo=32972).)

Example:

```
import unittest
class TestRequest(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.connection = await AsyncConnection()
    async def test_get(self):
        response = await self.connection.get("https://example.com")
        self.assertEqual(response.status_code, 200)
    async def asyncTearDown(self):
        await self.connection.close()
if __name__ == "__main__":
    unittest.main()
```
### venv[¶](#venv)

[ venv](../library/venv.html#module-venv) now includes an 

`Activate.ps1` script on all platforms for
activating virtual environments under PowerShell Core 6.1.
(Contributed by Brett Cannon in [bpo-32718](https://bugs.python.org/issue?@action=redirect&bpo=32718).)

### weakref[¶](#weakref)

The proxy objects returned by [ weakref.proxy()](../library/weakref.html#weakref.proxy) now support the matrix
multiplication operators 

`@` and `@=` in addition to the other
numeric operators. (Contributed by Mark Dickinson in [bpo-36669](https://bugs.python.org/issue?@action=redirect&bpo=36669).)

### xml[¶](#xml)

As mitigation against DTD and external entity retrieval, the
[ xml.dom.minidom](../library/xml.dom.minidom.html#module-xml.dom.minidom) and 

[modules no longer process external entities by default. (Contributed by Christian Heimes in](../library/xml.sax.html#module-xml.sax)

`xml.sax`[bpo-17239](https://bugs.python.org/issue?@action=redirect&bpo=17239).)

The `.find*()` methods in the [ xml.etree.ElementTree](../library/xml.etree.elementtree.html#module-xml.etree.ElementTree) module
support wildcard searches like 

`{*}tag` which ignores the namespace
and `{namespace}*` which returns all tags in the given namespace.
(Contributed by Stefan Behnel in [bpo-28238](https://bugs.python.org/issue?@action=redirect&bpo=28238).)

The [ xml.etree.ElementTree](../library/xml.etree.elementtree.html#module-xml.etree.ElementTree) module provides a new function

[that implements C14N 2.0. (Contributed by Stefan Behnel in](../library/xml.etree.elementtree.html#xml.etree.ElementTree.canonicalize)

`canonicalize()`[bpo-13611](https://bugs.python.org/issue?@action=redirect&bpo=13611).)

The target object of [ xml.etree.ElementTree.XMLParser](../library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser) can
receive namespace declaration events through the new callback methods

`start_ns()` and `end_ns()`.  Additionally, the
[target can be configured to process events about comments and processing instructions to include them in the generated tree. (Contributed by Stefan Behnel in](../library/xml.etree.elementtree.html#xml.etree.ElementTree.TreeBuilder)

`xml.etree.ElementTree.TreeBuilder`[bpo-36676](https://bugs.python.org/issue?@action=redirect&bpo=36676)and

[bpo-36673](https://bugs.python.org/issue?@action=redirect&bpo=36673).)

### xmlrpc[¶](#xmlrpc)

[ xmlrpc.client.ServerProxy](../library/xmlrpc.client.html#xmlrpc.client.ServerProxy) now supports an optional 

*headers*keyword argument for a sequence of HTTP headers to be sent with each request. Among other things, this makes it possible to upgrade from default basic authentication to faster session authentication. (Contributed by Cédric Krier in

[bpo-35153](https://bugs.python.org/issue?@action=redirect&bpo=35153).)

## Optimizations[¶](#optimizations)

- The - `subprocess`- `os.posix_spawn()`- *close_fds*is false;
- *preexec_fn*,- *pass_fds*,- *cwd*and- *start_new_session*parameters are not set;
- the - *executable*path contains a directory.
 - (Contributed by Joannah Nanjekye and Victor Stinner in - [bpo-35537](https://bugs.python.org/issue?@action=redirect&bpo=35537).)
- `shutil.copyfile()`- `shutil.copy()`- `shutil.copy2()`- `shutil.copytree()`- `shutil.move()`- `outfd.write(infd.read())`”. On Windows- `shutil.copyfile()`uses a bigger default buffer size (1 MiB instead of 16 KiB) and a- `memoryview()`- `shutil.copyfileobj()`- [Platform-dependent efficient copy operations](../library/shutil.html#shutil-platform-dependent-efficient-copy-operations)section. (Contributed by Giampaolo Rodolà in- [bpo-33671](https://bugs.python.org/issue?@action=redirect&bpo=33671).)
- `shutil.copytree()`- `os.scandir()`- `os.stat()`- `os.stat()`syscalls is reduced by 38% making- `shutil.copytree()`especially faster on network filesystems. (Contributed by Giampaolo Rodolà in- [bpo-33695](https://bugs.python.org/issue?@action=redirect&bpo=33695).)
- The default protocol in the - `pickle`
- Removed one - `Py_ssize_t`- `PyGC_Head`. All GC tracked objects (e.g. tuple, list, dict) size is reduced 4 or 8 bytes. (Contributed by Inada Naoki in- [bpo-33597](https://bugs.python.org/issue?@action=redirect&bpo=33597).)
- `uuid.UUID`- `__slots__`to reduce its memory footprint. (Contributed by Wouter Bolsterlee and Tal Einat in- [bpo-30977](https://bugs.python.org/issue?@action=redirect&bpo=30977))
- Improved performance of - `operator.itemgetter()`- [bpo-35664](https://bugs.python.org/issue?@action=redirect&bpo=35664).)
- Sped-up field lookups in - `collections.namedtuple()`- [bpo-32492](https://bugs.python.org/issue?@action=redirect&bpo=32492).)
- The - `list`- `__len__`). This makes the created list 12% smaller on average. (Contributed by Raymond Hettinger and Pablo Galindo in- [bpo-33234](https://bugs.python.org/issue?@action=redirect&bpo=33234).)
- Doubled the speed of class variable writes. When a non-dunder attribute was updated, there was an unnecessary call to update slots. (Contributed by Stefan Behnel, Pablo Galindo Salgado, Raymond Hettinger, Neil Schemenauer, and Serhiy Storchaka in - [bpo-36012](https://bugs.python.org/issue?@action=redirect&bpo=36012).)
- Reduced an overhead of converting arguments passed to many builtin functions and methods. This sped up calling some simple builtin functions and methods up to 20–50%. (Contributed by Serhiy Storchaka in - [bpo-23867](https://bugs.python.org/issue?@action=redirect&bpo=23867),- [bpo-35582](https://bugs.python.org/issue?@action=redirect&bpo=35582)and- [bpo-36127](https://bugs.python.org/issue?@action=redirect&bpo=36127).)
- `LOAD_GLOBAL`instruction now uses new “per opcode cache” mechanism. It is about 40% faster now. (Contributed by Yury Selivanov and Inada Naoki in- [bpo-26219](https://bugs.python.org/issue?@action=redirect&bpo=26219).)

## Build and C API Changes[¶](#build-and-c-api-changes)

- Default - `sys.abiflags`- `m`flag for pymalloc became useless (builds with and without pymalloc are ABI compatible) and so has been removed. (Contributed by Victor Stinner in- [bpo-36707](https://bugs.python.org/issue?@action=redirect&bpo=36707).)- Example of changes: - Only - `python3.8`program is installed,- `python3.8m`program is gone.
- Only - `python3.8-config`script is installed,- `python3.8m-config`script is gone.
- The - `m`flag has been removed from the suffix of dynamic library filenames: extension modules in the standard library as well as those produced and installed by third-party packages, like those downloaded from PyPI. On Linux, for example, the Python 3.7 suffix- `.cpython-37m-x86_64-linux-gnu.so`became- `.cpython-38-x86_64-linux-gnu.so`in Python 3.8.
 
- The header files have been reorganized to better separate the different kinds of APIs: - `Include/*.h`should be the portable public stable C API.
- `Include/cpython/*.h`should be the unstable C API specific to CPython; public API, with some private API prefixed by- `_Py`or- `_PY`.
- `Include/internal/*.h`is the private internal C API very specific to CPython. This API comes with no backward compatibility warranty and should not be used outside CPython. It is only exposed for very specific needs like debuggers and profiles which has to access to CPython internals without calling functions. This API is now installed by- `make install`.
 - (Contributed by Victor Stinner in - [bpo-35134](https://bugs.python.org/issue?@action=redirect&bpo=35134)and- [bpo-35081](https://bugs.python.org/issue?@action=redirect&bpo=35081), work initiated by Eric Snow in Python 3.7.)
- Some macros have been converted to static inline functions: parameter types and return type are well defined, they don’t have issues specific to macros, variables have a local scopes. Examples: 
- `PyObject_INIT`,- `PyObject_INIT_VAR`
- Private functions: - `_PyObject_GC_TRACK()`,- `_PyObject_GC_UNTRACK()`,- `_Py_Dealloc()`
 - (Contributed by Victor Stinner in - [bpo-35059](https://bugs.python.org/issue?@action=redirect&bpo=35059).)
- The - `PyByteArray_Init()`and- `PyByteArray_Fini()`functions have been removed. They did nothing since Python 2.7.4 and Python 3.2.0, were excluded from the limited API (stable ABI), and were not documented. (Contributed by Victor Stinner in- [bpo-35713](https://bugs.python.org/issue?@action=redirect&bpo=35713).)
- The result of - `PyExceptionClass_Name()`- `const char *`rather of- `char *`. (Contributed by Serhiy Storchaka in- [bpo-33818](https://bugs.python.org/issue?@action=redirect&bpo=33818).)
- The duality of - `Modules/Setup.dist`and- `Modules/Setup`has been removed. Previously, when updating the CPython source tree, one had to manually copy- `Modules/Setup.dist`(inside the source tree) to- `Modules/Setup`(inside the build tree) in order to reflect any changes upstream. This was of a small benefit to packagers at the expense of a frequent annoyance to developers following CPython development, as forgetting to copy the file could produce build failures.- Now the build system always reads from - `Modules/Setup`inside the source tree. People who want to customize that file are encouraged to maintain their changes in a git fork of CPython or as patch files, as they would do for any other change to the source tree.- (Contributed by Antoine Pitrou in - [bpo-32430](https://bugs.python.org/issue?@action=redirect&bpo=32430).)
- Functions that convert Python number to C integer like - `PyLong_AsLong()`- `PyArg_ParseTuple()`- `'i'`will now use the- `__index__()`- `__int__()`- `__int__()`method but without the- `__index__()`method (like- `Decimal`- `Fraction`- `PyNumber_Check()`- `1`for objects implementing- `__index__()`.- `PyNumber_Long()`- `PyNumber_Float()`- `PyFloat_AsDouble()`- `__index__()`method if available. (Contributed by Serhiy Storchaka in- [bpo-36048](https://bugs.python.org/issue?@action=redirect&bpo=36048)and- [bpo-20092](https://bugs.python.org/issue?@action=redirect&bpo=20092).)
- Heap-allocated type objects will now increase their reference count in - `PyObject_Init()`- `PyObject_INIT`) instead of in- `PyType_GenericAlloc()`- [bpo-35810](https://bugs.python.org/issue?@action=redirect&bpo=35810).)
- The new function - `PyCode_NewWithPosOnlyArgs()`allows to create code objects like- `PyCode_New()`, but with an extra- *posonlyargcount*parameter for indicating the number of positional-only arguments. (Contributed by Pablo Galindo in- [bpo-37221](https://bugs.python.org/issue?@action=redirect&bpo=37221).)
- `Py_SetPath()`now sets- `sys.executable`- `Py_GetProgramFullPath()`- `Py_GetProgramName()`- [bpo-38234](https://bugs.python.org/issue?@action=redirect&bpo=38234).)

## Deprecated[¶](#deprecated)

- The distutils - `bdist_wininst`command is now deprecated, use- `bdist_wheel`(wheel packages) instead. (Contributed by Victor Stinner in- [bpo-37481](https://bugs.python.org/issue?@action=redirect&bpo=37481).)
- Deprecated methods - `getchildren()`and- `getiterator()`in the- `ElementTree`- `DeprecationWarning`- `PendingDeprecationWarning`- [bpo-29209](https://bugs.python.org/issue?@action=redirect&bpo=29209).)
- Passing an object that is not an instance of - `concurrent.futures.ThreadPoolExecutor`- `loop.set_default_executor()`- [bpo-34075](https://bugs.python.org/issue?@action=redirect&bpo=34075).)
- The - `__getitem__()`- `xml.dom.pulldom.DOMEventStream`- `wsgiref.util.FileWrapper`- `fileinput.FileInput`- Implementations of these methods have been ignoring their - *index*parameter, and returning the next item instead. (Contributed by Berker Peksag in- [bpo-9372](https://bugs.python.org/issue?@action=redirect&bpo=9372).)
- The - `typing.NamedTuple`- `_field_types`attribute in favor of the- `__annotations__`attribute which has the same information. (Contributed by Raymond Hettinger in- [bpo-36320](https://bugs.python.org/issue?@action=redirect&bpo=36320).)
- `ast`- `Num`,- `Str`,- `Bytes`,- `NameConstant`and- `Ellipsis`are considered deprecated and will be removed in future Python versions.- `Constant`- [bpo-32892](https://bugs.python.org/issue?@action=redirect&bpo=32892).)
- `ast.NodeVisitor`- `visit_Num()`,- `visit_Str()`,- `visit_Bytes()`,- `visit_NameConstant()`and- `visit_Ellipsis()`are deprecated now and will not be called in future Python versions. Add the- `visit_Constant()`- [bpo-36917](https://bugs.python.org/issue?@action=redirect&bpo=36917).)
- The - `@asyncio.coroutine`- [decorator](../glossary.html#term-decorator)is deprecated and will be removed in version 3.10. Instead of- `@asyncio.coroutine`, use- `async def`- [bpo-36921](https://bugs.python.org/issue?@action=redirect&bpo=36921).)
- In - `asyncio`- *loop*argument has been deprecated and will be removed in version 3.10 for the following:- `asyncio.sleep()`- `asyncio.gather()`- `asyncio.shield()`- `asyncio.wait_for()`- `asyncio.wait()`- `asyncio.as_completed()`- `asyncio.Task`- `asyncio.Lock`- `asyncio.Event`- `asyncio.Condition`- `asyncio.Semaphore`- `asyncio.BoundedSemaphore`- `asyncio.Queue`- `asyncio.create_subprocess_exec()`- `asyncio.create_subprocess_shell()`
- The explicit passing of coroutine objects to - `asyncio.wait()`- [bpo-34790](https://bugs.python.org/issue?@action=redirect&bpo=34790).)
- The following functions and methods are deprecated in the - `gettext`- `lgettext()`,- `ldgettext()`,- `lngettext()`and- `ldngettext()`. They return encoded bytes, and it’s possible that you will get unexpected Unicode-related exceptions if there are encoding problems with the translated strings. It’s much better to use alternatives which return Unicode strings in Python 3. These functions have been broken for a long time.- Function - `bind_textdomain_codeset()`, methods- `NullTranslations.output_charset()`and- `NullTranslations.set_output_charset()`, and the- *codeset*parameter of functions- `translation()`- `install()`- `l*gettext()`functions. (Contributed by Serhiy Storchaka in- [bpo-33710](https://bugs.python.org/issue?@action=redirect&bpo=33710).)
- The - `isAlive()`method of- `threading.Thread`- [bpo-35283](https://bugs.python.org/issue?@action=redirect&bpo=35283).)
- Many builtin and extension functions that take integer arguments will now emit a deprecation warning for - `Decimal`- `Fraction`- `__int__()`- `__index__()`- [bpo-36048](https://bugs.python.org/issue?@action=redirect&bpo=36048).)
- Deprecated passing the following arguments as keyword arguments: - *func*in- `functools.partialmethod()`- `weakref.finalize()`- `profile.Profile.runcall()`- `cProfile.Profile.runcall()`,- `bdb.Bdb.runcall()`- `trace.Trace.runfunc()`- `curses.wrapper()`
- *function*in- `unittest.TestCase.addCleanup()`
- *fn*in the- `submit()`- `concurrent.futures.ThreadPoolExecutor`- `concurrent.futures.ProcessPoolExecutor`
- *callback*in- `contextlib.ExitStack.callback()`- `contextlib.AsyncExitStack.callback()`and- `contextlib.AsyncExitStack.push_async_callback()`
- *c*and- *typeid*in the- `create()`method of- `multiprocessing.managers.Server`and- `multiprocessing.managers.SharedMemoryServer`.
- *obj*in- `weakref.finalize()`
 - In future releases of Python, they will be - [positional-only](../glossary.html#positional-only-parameter). (Contributed by Serhiy Storchaka in- [bpo-36492](https://bugs.python.org/issue?@action=redirect&bpo=36492).)

## API and Feature Removals[¶](#api-and-feature-removals)

The following features and APIs have been removed from Python 3.8:

- Starting with Python 3.3, importing ABCs from - `collections`- `collections.abc`- [gh-81134](https://github.com/python/cpython/issues/81134).)
- The - `macpath`module, deprecated in Python 3.7, has been removed. (Contributed by Victor Stinner in- [bpo-35471](https://bugs.python.org/issue?@action=redirect&bpo=35471).)
- The function - `platform.popen()`has been removed, after having been deprecated since Python 3.3: use- `os.popen()`- [bpo-35345](https://bugs.python.org/issue?@action=redirect&bpo=35345).)
- The function - `time.clock()`has been removed, after having been deprecated since Python 3.3: use- `time.perf_counter()`- `time.process_time()`- [bpo-36895](https://bugs.python.org/issue?@action=redirect&bpo=36895).)
- The - `pyvenv`script has been removed in favor of- `python3.8 -m venv`to help eliminate confusion as to what Python interpreter the- `pyvenv`script is tied to. (Contributed by Brett Cannon in- [bpo-25427](https://bugs.python.org/issue?@action=redirect&bpo=25427).)
- `parse_qs`,- `parse_qsl`, and- `escape`are removed from the- `cgi`module. They are deprecated in Python 3.2 or older. They should be imported from the- `urllib.parse`and- `html`modules instead.
- `filemode`function is removed from the- `tarfile`
- The - `XMLParser`- *html*argument. It never had an effect and was deprecated in Python 3.4. All other parameters are now- [keyword-only](../glossary.html#keyword-only-parameter). (Contributed by Serhiy Storchaka in- [bpo-29209](https://bugs.python.org/issue?@action=redirect&bpo=29209).)
- Removed the - `doctype()`method of- `XMLParser`- [bpo-29209](https://bugs.python.org/issue?@action=redirect&bpo=29209).)
- “unicode_internal” codec is removed. (Contributed by Inada Naoki in - [bpo-36297](https://bugs.python.org/issue?@action=redirect&bpo=36297).)
- The - `Cache`and- `Statement`objects of the- `sqlite3`- [bpo-30262](https://bugs.python.org/issue?@action=redirect&bpo=30262).)
- The - `bufsize`keyword argument of- `fileinput.input()`- `fileinput.FileInput()`- [bpo-36952](https://bugs.python.org/issue?@action=redirect&bpo=36952)(Contributed by Matthias Bussonnier.)
- The functions - `sys.set_coroutine_wrapper()`and- `sys.get_coroutine_wrapper()`deprecated in Python 3.7 have been removed;- [bpo-36933](https://bugs.python.org/issue?@action=redirect&bpo=36933)(Contributed by Matthias Bussonnier.)

## Porting to Python 3.8[¶](#porting-to-python-3-8)

This section lists previously described changes and other bugfixes that may require changes to your code.

### Changes in Python behavior[¶](#changes-in-python-behavior)

- Yield expressions (both - `yield`and- `yield from`clauses) are now disallowed in comprehensions and generator expressions (aside from the iterable expression in the leftmost- `for`clause). (Contributed by Serhiy Storchaka in- [bpo-10544](https://bugs.python.org/issue?@action=redirect&bpo=10544).)
- The compiler now produces a - `SyntaxWarning`- `is`and- `is not`) are used with certain types of literals (e.g. strings, numbers). These can often work by accident in CPython, but are not guaranteed by the language spec. The warning advises users to use equality tests (- `==`and- `!=`) instead. (Contributed by Serhiy Storchaka in- [bpo-34850](https://bugs.python.org/issue?@action=redirect&bpo=34850).)
- The CPython interpreter can swallow exceptions in some circumstances. In Python 3.8 this happens in fewer cases. In particular, exceptions raised when getting the attribute from the type dictionary are no longer ignored. (Contributed by Serhiy Storchaka in - [bpo-35459](https://bugs.python.org/issue?@action=redirect&bpo=35459).)
- Removed - `__str__`implementations from builtin types- `bool`- `int`- `float`- `complex`- `__str__()`from- `object`- `__repr__()`method in the subclass of these classes will affect their string representation. (Contributed by Serhiy Storchaka in- [bpo-36793](https://bugs.python.org/issue?@action=redirect&bpo=36793).)
- On AIX, - `sys.platform`- `'aix'`, instead of- `'aix3'`..- `'aix7'`. Since older Python versions include the version number, so it is recommended to always use- `sys.platform.startswith('aix')`. (Contributed by M. Felt in- [bpo-36588](https://bugs.python.org/issue?@action=redirect&bpo=36588).)
- `PyEval_AcquireLock()`and- `PyEval_AcquireThread()`now terminate the current thread if called while the interpreter is finalizing, making them consistent with- `PyEval_RestoreThread()`- `Py_END_ALLOW_THREADS()`- `PyGILState_Ensure()`- `_Py_IsFinalizing()`or- `sys.is_finalizing()`- [bpo-36475](https://bugs.python.org/issue?@action=redirect&bpo=36475).)

### Changes in the Python API[¶](#changes-in-the-python-api)

- The - `os.getcwdb()`- **PEP 529**- [bpo-37412](https://bugs.python.org/issue?@action=redirect&bpo=37412).)
- `subprocess.Popen`- `os.posix_spawn()`- `Popen`constructor using- `os.posix_spawn()`no longer raises an exception on errors like “missing program”. Instead the child process fails with a non-zero- `returncode`- [bpo-35537](https://bugs.python.org/issue?@action=redirect&bpo=35537).)
- The - *preexec_fn*argument of *- `subprocess.Popen`- `RuntimeError`- [bpo-34651](https://bugs.python.org/issue?@action=redirect&bpo=34651), modified by Christian Heimes in- [bpo-37951](https://bugs.python.org/issue?@action=redirect&bpo=37951).)
- The - `imaplib.IMAP4.logout()`- [bpo-36348](https://bugs.python.org/issue?@action=redirect&bpo=36348).)
- The function - `platform.popen()`has been removed, after having been deprecated since Python 3.3: use- `os.popen()`- [bpo-35345](https://bugs.python.org/issue?@action=redirect&bpo=35345).)
- The - `statistics.mode()`- [bpo-35892](https://bugs.python.org/issue?@action=redirect&bpo=35892).)
- The - `selection()`- `tkinter.ttk.Treeview`- `selection_set()`- [bpo-31508](https://bugs.python.org/issue?@action=redirect&bpo=31508).)
- The - `writexml()`- `toxml()`- `toprettyxml()`- `xml.dom.minidom`- `write()`- `xml.etree.ElementTree`- [bpo-34160](https://bugs.python.org/issue?@action=redirect&bpo=34160).)
- A - `dbm.dumb`- `'r'`is now read-only.- `dbm.dumb.open()`- `'r'`and- `'w'`no longer creates a database if it does not exist. (Contributed by Serhiy Storchaka in- [bpo-32749](https://bugs.python.org/issue?@action=redirect&bpo=32749).)
- The - `doctype()`method defined in a subclass of- `XMLParser`- `RuntimeWarning`- `DeprecationWarning`- `doctype()`- [bpo-29209](https://bugs.python.org/issue?@action=redirect&bpo=29209).)
- A - `RuntimeError`- `__classcell__`entry in the namespace passed to- `type.__new__`. A- `DeprecationWarning`- [bpo-23722](https://bugs.python.org/issue?@action=redirect&bpo=23722).)
- The - `cProfile.Profile`- [bpo-29235](https://bugs.python.org/issue?@action=redirect&bpo=29235).)
- `shutil.copyfile()`- `shutil.copy()`- `shutil.copy2()`- `shutil.copytree()`- `shutil.move()`- [Platform-dependent efficient copy operations](../library/shutil.html#shutil-platform-dependent-efficient-copy-operations)section).
- `shutil.copyfile()`
- The - `PyGC_Head`struct has changed completely. All code that touched the struct member should be rewritten. (See- [bpo-33597](https://bugs.python.org/issue?@action=redirect&bpo=33597).)
- The - `PyInterpreterState`- `PyInterpreterState`is still available as part of the public API (and stable ABI). The docs indicate that none of the struct’s fields are public, so we hope no one has been using them. However, if you do rely on one or more of those private fields and have no alternative then please open a BPO issue. We’ll work on helping you adjust (possibly including adding accessor functions to the public API). (See- [bpo-35886](https://bugs.python.org/issue?@action=redirect&bpo=35886).)
- The - `mmap.flush()`- `None`on success and raises an exception on error under all platforms. Previously, its behavior was platform-dependent: a nonzero value was returned on success; zero was returned on error under Windows. A zero value was returned on success; an exception was raised on error under Unix. (Contributed by Berker Peksag in- [bpo-2122](https://bugs.python.org/issue?@action=redirect&bpo=2122).)
- `xml.dom.minidom`- `xml.sax`- [bpo-17239](https://bugs.python.org/issue?@action=redirect&bpo=17239).)
- Deleting a key from a read-only - `dbm`- `dbm.dumb`- `dbm.gnu`- `dbm.ndbm`- `error`(- `dbm.dumb.error`- `dbm.gnu.error`- `dbm.ndbm.error`- `KeyError`- [bpo-33106](https://bugs.python.org/issue?@action=redirect&bpo=33106).)
- Simplified AST for literals. All constants will be represented as - `ast.Constant`- `Num`,- `Str`,- `Bytes`,- `NameConstant`and- `Ellipsis`will return an instance of- `Constant`. (Contributed by Serhiy Storchaka in- [bpo-32892](https://bugs.python.org/issue?@action=redirect&bpo=32892).)
- `expanduser()`- `USERPROFILE`environment variable and does not use- `HOME`, which is not normally set for regular user accounts. (Contributed by Anthony Sottile in- [bpo-36264](https://bugs.python.org/issue?@action=redirect&bpo=36264).)
- The exception - `asyncio.CancelledError`- `BaseException`- `Exception`- `concurrent.futures.CancelledError`- [bpo-32528](https://bugs.python.org/issue?@action=redirect&bpo=32528).)
- The function - `asyncio.wait_for()`- `asyncio.Task`- *timeout*, it was cancelled and immediately returned. (Contributed by Elvis Pranskevichus in- [bpo-32751](https://bugs.python.org/issue?@action=redirect&bpo=32751).)
- The function - `asyncio.BaseTransport.get_extra_info()`- *name*parameter. (Contributed by Yury Selivanov in- [bpo-37027](https://bugs.python.org/issue?@action=redirect&bpo=37027).)
- `asyncio.BufferedProtocol`

- DLL dependencies for extension modules and DLLs loaded with - `ctypes`- `add_dll_directory()`- `PATH`and the current working directory are no longer used, and modifications to these will no longer have any effect on normal DLL resolution. If your application relies on these mechanisms, you should check for- `add_dll_directory()`and if it exists, use it to add your DLLs directory while loading your library. Note that Windows 7 users will need to ensure that Windows Update KB2533623 has been installed (this is also verified by the installer). (Contributed by Steve Dower in- [bpo-36085](https://bugs.python.org/issue?@action=redirect&bpo=36085).)
- The header files and functions related to pgen have been removed after its replacement by a pure Python implementation. (Contributed by Pablo Galindo in - [bpo-36623](https://bugs.python.org/issue?@action=redirect&bpo=36623).)
- `types.CodeType`- *posonlyargcount*) to support positional-only arguments defined in- **PEP 570**- *argcount*) now represents the total number of positional arguments (including positional-only arguments). The new- `replace()`method of- `types.CodeType`can be used to make the code future-proof.
- The parameter - `digestmod`for- `hmac.new()`

### Changes in the C API[¶](#changes-in-the-c-api)

- The - `PyCompilerFlags`- *cf_feature_version*field. It should be initialized to- `PY_MINOR_VERSION`. The field is ignored by default, and is used if and only if- `PyCF_ONLY_AST`flag is set in- *cf_flags*. (Contributed by Guido van Rossum in- [bpo-35766](https://bugs.python.org/issue?@action=redirect&bpo=35766).)
- The - `PyEval_ReInitThreads()`function has been removed from the C API. It should not be called explicitly: use- `PyOS_AfterFork_Child()`- [bpo-36728](https://bugs.python.org/issue?@action=redirect&bpo=36728).)
- On Unix, C extensions are no longer linked to libpython except on Android and Cygwin. When Python is embedded, - `libpython`must not be loaded with- `RTLD_LOCAL`, but- `RTLD_GLOBAL`instead. Previously, using- `RTLD_LOCAL`, it was already not possible to load C extensions which were not linked to- `libpython`, like C extensions of the standard library built by the- `*shared*`section of- `Modules/Setup`. (Contributed by Victor Stinner in- [bpo-21536](https://bugs.python.org/issue?@action=redirect&bpo=21536).)
- Use of - `#`variants of formats in parsing or building value (e.g.- `PyArg_ParseTuple()`- `Py_BuildValue()`- `PyObject_CallFunction()`- `PY_SSIZE_T_CLEAN`defined raises- `DeprecationWarning`now. It will be removed in 3.10 or 4.0. Read- [Parsing arguments and building values](../c-api/arg.html#arg-parsing)for detail. (Contributed by Inada Naoki in- [bpo-36381](https://bugs.python.org/issue?@action=redirect&bpo=36381).)
- Instances of heap-allocated types (such as those created with - `PyType_FromSpec()`- `PyType_GenericAlloc()`- `PyObject_Init()`- `PyObject_INIT`. This makes types created through- `PyType_FromSpec()`behave like other classes in managed code.- [Statically allocated types](../c-api/typeobj.html#static-types)are not affected.- For the vast majority of cases, there should be no side effect. However, types that manually increase the reference count after allocating an instance (perhaps to work around the bug) may now become immortal. To avoid this, these classes need to call Py_DECREF on the type object during instance deallocation. - To correctly port these types into 3.8, please apply the following changes: - Remove - `Py_INCREF`- `PyObject_New`- `PyObject_NewVar`- `PyObject_GC_New()`- `PyObject_GC_NewVar()`- `PyObject_Init()`- `PyObject_INIT`.- Example: - static foo_struct * foo_new(PyObject *type) { foo_struct *foo = PyObject_GC_New(foo_struct, (PyTypeObject *) type); if (foo == NULL) return NULL; #if PY_VERSION_HEX < 0x03080000 // Workaround for Python issue 35810; no longer necessary in Python 3.8 PY_INCREF(type) #endif return foo; } 
- Ensure that all custom - `tp_dealloc`functions of heap-allocated types decrease the type’s reference count.- Example: - static void foo_dealloc(foo_struct *instance) { PyObject *type = Py_TYPE(instance); PyObject_GC_Del(instance); #if PY_VERSION_HEX >= 0x03080000 // This was not needed before Python 3.8 (Python issue 35810) Py_DECREF(type); #endif } 
 - (Contributed by Eddie Elizondo in - [bpo-35810](https://bugs.python.org/issue?@action=redirect&bpo=35810).)
- The - `Py_DEPRECATED()`- Example: - Py_DEPRECATED(3.8) PyAPI_FUNC(int) Py_OldFunction(void); - (Contributed by Zackery Spytz in - [bpo-33407](https://bugs.python.org/issue?@action=redirect&bpo=33407).)
- The interpreter does not pretend to support binary compatibility of extension types across feature releases, anymore. A - `PyTypeObject`- `tp_finalize`- `Py_TPFLAGS_HAVE_FINALIZE`- `tp_finalize`).- (Contributed by Antoine Pitrou in - [bpo-32388](https://bugs.python.org/issue?@action=redirect&bpo=32388).)
- The functions - `PyNode_AddChild()`and- `PyParser_AddToken()`now accept two additional- `int`arguments- *end_lineno*and- *end_col_offset*.
- The - `libpython38.a`file to allow MinGW tools to link directly against- `python38.dll`is no longer included in the regular Windows distribution. If you require this file, it may be generated with the- `gendef`and- `dlltool`tools, which are part of the MinGW binutils package:- gendef - python38.dll > tmp.def dlltool --dllname python38.dll --def tmp.def --output-lib libpython38.a - The location of an installed - `pythonXY.dll`will depend on the installation options and the version and language of Windows. See- [Using Python on Windows](../using/windows.html#using-on-windows)for more information. The resulting library should be placed in the same directory as- `pythonXY.lib`, which is generally the- `libs`directory under your Python installation.- (Contributed by Steve Dower in - [bpo-37351](https://bugs.python.org/issue?@action=redirect&bpo=37351).)

### CPython bytecode changes[¶](#cpython-bytecode-changes)

- The interpreter loop has been simplified by moving the logic of unrolling the stack of blocks into the compiler. The compiler emits now explicit instructions for adjusting the stack of values and calling the cleaning-up code for - `break`- `continue`- `return`- Removed opcodes - `BREAK_LOOP`,- `CONTINUE_LOOP`,- `SETUP_LOOP`and- `SETUP_EXCEPT`. Added new opcodes- `ROT_FOUR`,- `BEGIN_FINALLY`,- `CALL_FINALLY`and- `POP_FINALLY`. Changed the behavior of- `END_FINALLY`and- `WITH_CLEANUP_START`.- (Contributed by Mark Shannon, Antoine Pitrou and Serhiy Storchaka in - [bpo-17611](https://bugs.python.org/issue?@action=redirect&bpo=17611).)
- Added new opcode - `END_ASYNC_FOR`- `async for`- [bpo-33041](https://bugs.python.org/issue?@action=redirect&bpo=33041).)
- The - `MAP_ADD`- **PEP 572**- [bpo-35224](https://bugs.python.org/issue?@action=redirect&bpo=35224).)

### Demos and Tools[¶](#demos-and-tools)

Added a benchmark script for timing various ways to access variables:
`Tools/scripts/var_access_benchmark.py`.
(Contributed by Raymond Hettinger in [bpo-35884](https://bugs.python.org/issue?@action=redirect&bpo=35884).)

Here’s a summary of performance improvements since Python 3.3:

```
Python version                       3.3     3.4     3.5     3.6     3.7     3.8
--------------                       ---     ---     ---     ---     ---     ---
Variable and attribute read access:
    read_local                       4.0     7.1     7.1     5.4     5.1     3.9
    read_nonlocal                    5.3     7.1     8.1     5.8     5.4     4.4
    read_global                     13.3    15.5    19.0    14.3    13.6     7.6
    read_builtin                    20.0    21.1    21.6    18.5    19.0     7.5
    read_classvar_from_class        20.5    25.6    26.5    20.7    19.5    18.4
    read_classvar_from_instance     18.5    22.8    23.5    18.8    17.1    16.4
    read_instancevar                26.8    32.4    33.1    28.0    26.3    25.4
    read_instancevar_slots          23.7    27.8    31.3    20.8    20.8    20.2
    read_namedtuple                 68.5    73.8    57.5    45.0    46.8    18.4
    read_boundmethod                29.8    37.6    37.9    29.6    26.9    27.7
Variable and attribute write access:
    write_local                      4.6     8.7     9.3     5.5     5.3     4.3
    write_nonlocal                   7.3    10.5    11.1     5.6     5.5     4.7
    write_global                    15.9    19.7    21.2    18.0    18.0    15.8
    write_classvar                  81.9    92.9    96.0   104.6   102.1    39.2
    write_instancevar               36.4    44.6    45.8    40.0    38.9    35.5
    write_instancevar_slots         28.7    35.6    36.1    27.3    26.6    25.7
Data structure read access:
    read_list                       19.2    24.2    24.5    20.8    20.8    19.0
    read_deque                      19.9    24.7    25.5    20.2    20.6    19.8
    read_dict                       19.7    24.3    25.7    22.3    23.0    21.0
    read_strdict                    17.9    22.6    24.3    19.5    21.2    18.9
Data structure write access:
    write_list                      21.2    27.1    28.5    22.5    21.6    20.0
    write_deque                     23.8    28.7    30.1    22.7    21.8    23.5
    write_dict                      25.9    31.4    33.3    29.3    29.2    24.7
    write_strdict                   22.9    28.4    29.9    27.5    25.2    23.1
Stack (or queue) operations:
    list_append_pop                144.2    93.4   112.7    75.4    74.2    50.8
    deque_append_pop                30.4    43.5    57.0    49.4    49.2    42.5
    deque_append_popleft            30.8    43.7    57.3    49.7    49.7    42.8
Timing loop:
    loop_overhead                    0.3     0.5     0.6     0.4     0.3     0.3
```
The benchmarks were measured on an
[Intel® Core™ i7-4960HQ processor](https://ark.intel.com/content/www/us/en/ark/products/76088/intel-core-i7-4960hq-processor-6m-cache-up-to-3-80-ghz.html)
running the macOS 64-bit builds found at
[python.org](https://www.python.org/downloads/macos/).
The benchmark script displays timings in nanoseconds.

## Notable changes in Python 3.8.1[¶](#notable-changes-in-python-3-8-1)

Due to significant security concerns, the *reuse_address* parameter of
[ asyncio.loop.create_datagram_endpoint()](../library/asyncio-eventloop.html#asyncio.loop.create_datagram_endpoint) is no longer supported. This is
because of the behavior of the socket option 

`SO_REUSEADDR` in UDP. For more
details, see the documentation for `loop.create_datagram_endpoint()`.
(Contributed by Kyle Stanley, Antoine Pitrou, and Yury Selivanov in
[bpo-37228](https://bugs.python.org/issue?@action=redirect&bpo=37228).)

## Notable changes in Python 3.8.2[¶](#notable-changes-in-python-3-8-2)

Fixed a regression with the `ignore` callback of [ shutil.copytree()](../library/shutil.html#shutil.copytree).
The argument types are now str and List[str] again.
(Contributed by Manuel Barkhau and Giampaolo Rodola in 

[gh-83571](https://github.com/python/cpython/issues/83571).)

## Notable changes in Python 3.8.3[¶](#notable-changes-in-python-3-8-3)

The constant values of future flags in the [ __future__](../library/__future__.html#module-__future__) module
are updated in order to prevent collision with compiler flags. Previously

`PyCF_ALLOW_TOP_LEVEL_AWAIT` was clashing with `CO_FUTURE_DIVISION`.
(Contributed by Batuhan Taskaya in [gh-83743](https://github.com/python/cpython/issues/83743))

## Notable changes in Python 3.8.8[¶](#notable-changes-in-python-3-8-8)

Earlier Python versions allowed using both `;` and `&` as
query parameter separators in [ urllib.parse.parse_qs()](../library/urllib.parse.html#urllib.parse.parse_qs) and

[. Due to security concerns, and to conform with newer W3C recommendations, this has been changed to allow only a single separator key, with](../library/urllib.parse.html#urllib.parse.parse_qsl)

`urllib.parse.parse_qsl()``&` as the default.  This change also affects
`cgi.parse()` and `cgi.parse_multipart()` as they use the affected
functions internally. For more details, please see their respective
documentation.
(Contributed by Adam Goldschmidt, Senthil Kumaran and Ken Jin in [bpo-42967](https://bugs.python.org/issue?@action=redirect&bpo=42967).)

## Notable changes in Python 3.8.9[¶](#notable-changes-in-python-3-8-9)

A security fix alters the [ ftplib.FTP](../library/ftplib.html#ftplib.FTP) behavior to not trust the
IPv4 address sent from the remote server when setting up a passive data
channel.  We reuse the ftp server IP address instead.  For unusual code
requiring the old behavior, set a 

`trust_server_pasv_ipv4_address`
attribute on your FTP instance to `True`.  (See [gh-87451](https://github.com/python/cpython/issues/87451))

## Notable changes in Python 3.8.10[¶](#notable-changes-in-python-3-8-10)

### macOS 11.0 (Big Sur) and Apple Silicon Mac support[¶](#macos-11-0-big-sur-and-apple-silicon-mac-support)

As of 3.8.10, Python now supports building and running on macOS 11
(Big Sur) and on Apple Silicon Macs (based on the `ARM64` architecture).
A new universal build variant, `universal2`, is now available to natively
support both `ARM64` and `Intel 64` in one set of executables.
Note that support for “weaklinking”, building binaries targeted for newer
versions of macOS that will also run correctly on older versions by
testing at runtime for missing features, is not included in this backport
from Python 3.9; to support a range of macOS versions, continue to target
for and build on the oldest version in the range.

(Originally contributed by Ronald Oussoren and Lawrence D’Anna in [gh-85272](https://github.com/python/cpython/issues/85272),
with fixes by FX Coudert and Eli Rykoff, and backported to 3.8 by Maxime Bélanger
and Ned Deily)

## Notable changes in Python 3.8.10[¶](#id1)

### urllib.parse[¶](#urllib-parse)

The presence of newline or tab characters in parts of a URL allows for some
forms of attacks. Following the WHATWG specification that updates [ RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986.html),
ASCII newline 

`\n`, `\r` and tab `\t` characters are stripped from the
URL by the parser in [preventing such attacks. The removal characters are controlled by a new module level variable](../library/urllib.parse.html#module-urllib.parse)

`urllib.parse``urllib.parse._UNSAFE_URL_BYTES_TO_REMOVE`. (See [bpo-43882](https://bugs.python.org/issue?@action=redirect&bpo=43882))

## Notable changes in Python 3.8.12[¶](#notable-changes-in-python-3-8-12)

### Changes in the Python API[¶](#id2)

Starting with Python 3.8.12 the [ ipaddress](../library/ipaddress.html#module-ipaddress) module no longer accepts
any leading zeros in IPv4 address strings. Leading zeros are ambiguous and
interpreted as octal notation by some libraries. For example the legacy
function 

[treats leading zeros as octal notation. glibc implementation of modern](../library/socket.html#socket.inet_aton)

`socket.inet_aton()`[does not accept any leading zeros.](../library/socket.html#socket.inet_pton)

`inet_pton()`(Originally contributed by Christian Heimes in [bpo-36384](https://bugs.python.org/issue?@action=redirect&bpo=36384), and backported
to 3.8 by Achraf Merzouki.)

## Notable security feature in 3.8.14[¶](#notable-security-feature-in-3-8-14)

Converting between [ int](../library/functions.html#int) and 

[in bases other than 2 (binary), 4, 8 (octal), 16 (hexadecimal), or 32 such as base 10 (decimal) now raises a](../library/stdtypes.html#str)

`str`[if the number of digits in string form is above a limit to avoid potential denial of service attacks due to the algorithmic complexity. This is a mitigation for](../library/exceptions.html#ValueError)

`ValueError`[. This limit can be configured or disabled by environment variable, command line flag, or](https://www.cve.org/CVERecord?id=CVE-2020-10735)

**CVE 2020-10735**[APIs. See the](../library/sys.html#module-sys)

`sys`[integer string conversion length limitation](../library/stdtypes.html#int-max-str-digits)documentation. The default limit is 4300 digits in string form.

## Notable changes in 3.8.17[¶](#notable-changes-in-3-8-17)

### tarfile[¶](#id3)

- The extraction methods in - `tarfile`- `shutil.unpack_archive()`- *filter*argument that allows limiting tar features than may be surprising or dangerous, such as creating files outside the destination directory. See- [Extraction filters](../library/tarfile.html#tarfile-extraction-filter)for details. In Python 3.12, use without the- *filter*argument will show a- `DeprecationWarning`- `'data'`. (Contributed by Petr Viktorin in- **PEP 706**