# What’s New In Python 3.5 — Python 3.14.6 documentation

**Source:** [https://docs.python.org/whatsnew/3.5.html](https://docs.python.org/whatsnew/3.5.html)

---

# What’s New In Python 3.5[¶](#what-s-new-in-python-3-5)

- Editors:
- Elvis Pranskevichus < - [elvis@magic.io](mailto:elvis%40magic.io)>, Yury Selivanov <- [yury@magic.io](mailto:yury%40magic.io)>

This article explains the new features in Python 3.5, compared to 3.4.
Python 3.5 was released on September 13, 2015.  See the
[changelog](https://docs.python.org/3.5/whatsnew/changelog.html) for a full
list of changes.

See also

[ PEP 478](https://peps.python.org/pep-0478/) - Python 3.5 Release Schedule

## Summary – Release highlights[¶](#summary-release-highlights)

New syntax features:

- [PEP 492](#whatsnew-pep-492), coroutines with async and await syntax.
- [PEP 465](#whatsnew-pep-465), a new matrix multiplication operator:- `a @ b`.
- [PEP 448](#whatsnew-pep-448), additional unpacking generalizations.

New library modules:

New built-in features:

- `bytes % args`,- `bytearray % args`:- [PEP 461](#whatsnew-pep-461)– Adding- `%`formatting to bytes and bytearray.
- New - `bytes.hex()`- `bytearray.hex()`- `memoryview.hex()`- [bpo-9951](https://bugs.python.org/issue?@action=redirect&bpo=9951).)
- `memoryview`- [bpo-23632](https://bugs.python.org/issue?@action=redirect&bpo=23632).)
- Generators have a new - `gi_yieldfrom`attribute, which returns the object being iterated by- `yield from`expressions. (Contributed by Benno Leslie and Yury Selivanov in- [bpo-24450](https://bugs.python.org/issue?@action=redirect&bpo=24450).)
- A new - `RecursionError`- [bpo-19235](https://bugs.python.org/issue?@action=redirect&bpo=19235).)

CPython implementation improvements:

- When the - `LC_TYPE`locale is the POSIX locale (- `C`locale),- `sys.stdin`- `sys.stdout`- `surrogateescape`error handler, instead of the- `strict`error handler. (Contributed by Victor Stinner in- [bpo-19977](https://bugs.python.org/issue?@action=redirect&bpo=19977).)
- `.pyo`files are no longer used and have been replaced by a more flexible scheme that includes the optimization level explicitly in- `.pyc`name. (See- [PEP 488 overview](#whatsnew-pep-488).)
- Builtin and extension modules are now initialized in a multi-phase process, which is similar to how Python modules are loaded. (See - [PEP 489 overview](#whatsnew-pep-489).)

Significant improvements in the standard library:

- `collections.OrderedDict`- [implemented in C](#whatsnew-ordereddict), which makes it 4 to 100 times faster.
- The - `ssl`- [support for Memory BIO](#whatsnew-sslmemorybio), which decouples SSL protocol handling from network IO.
- The new - `os.scandir()`- [better and significantly faster way](#whatsnew-pep-471)of directory traversal.
- `functools.lru_cache()`- [reimplemented in C](#whatsnew-lrucache), yielding much better performance.
- The new - `subprocess.run()`- [streamlined way to run subprocesses](#whatsnew-subprocess).
- The - `traceback`- [enhanced](#whatsnew-traceback)for improved performance and developer convenience.

Security improvements:

- SSLv3 is now disabled throughout the standard library. It can still be enabled by instantiating a - `ssl.SSLContext`- [bpo-22638](https://bugs.python.org/issue?@action=redirect&bpo=22638)for more details; this change was backported to CPython 3.4 and 2.7.)
- HTTP cookie parsing is now stricter, in order to protect against potential injection attacks. (Contributed by Antoine Pitrou in - [bpo-22796](https://bugs.python.org/issue?@action=redirect&bpo=22796).)

Windows improvements:

- A new installer for Windows has replaced the old MSI. See - [Using Python on Windows](../using/windows.html#using-on-windows)for more information.
- Windows builds now use Microsoft Visual C++ 14.0, and extension modules should use the same. 

Please read on for a comprehensive list of user-facing changes, including many other smaller improvements, CPython optimizations, deprecations, and potential porting issues.

## New Features[¶](#new-features)

### PEP 492 - Coroutines with async and await syntax[¶](#pep-492-coroutines-with-async-and-await-syntax)

[ PEP 492](https://peps.python.org/pep-0492/) greatly improves support for asynchronous programming in Python
by adding 

[awaitable objects](../glossary.html#term-awaitable),

[coroutine functions](../glossary.html#term-coroutine-function),

[asynchronous iteration](../glossary.html#term-asynchronous-iterable), and

[asynchronous context managers](../glossary.html#term-asynchronous-context-manager).

Coroutine functions are declared using the new [ async def](../reference/compound_stmts.html#async-def) syntax:

```
>>> async def coro():
...     return 'spam'
```
Inside a coroutine function, the new [ await](../reference/expressions.html#await) expression can be used
to suspend coroutine execution until the result is available.  Any object
can be 

*awaited*, as long as it implements the

[awaitable](../glossary.html#term-awaitable)protocol by defining the

[method.](../reference/datamodel.html#object.__await__)

`__await__()`PEP 492 also adds [ async for](../reference/compound_stmts.html#async-for) statement for convenient iteration
over asynchronous iterables.

An example of a rudimentary HTTP client written using the new syntax:

```
import asyncio
async def http_get(domain):
    reader, writer = await asyncio.open_connection(domain, 80)
    writer.write(b'\r\n'.join([
        b'GET / HTTP/1.1',
        b'Host: %b' % domain.encode('latin-1'),
        b'Connection: close',
        b'', b''
    ]))
    async for line in reader:
        print('>>>', line)
    writer.close()
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(http_get('example.com'))
finally:
    loop.close()
```
Similarly to asynchronous iteration, there is a new syntax for asynchronous context managers. The following script:

```
import asyncio
async def coro(name, lock):
    print('coro {}: waiting for lock'.format(name))
    async with lock:
        print('coro {}: holding the lock'.format(name))
        await asyncio.sleep(1)
        print('coro {}: releasing the lock'.format(name))
loop = asyncio.get_event_loop()
lock = asyncio.Lock()
coros = asyncio.gather(coro(1, lock), coro(2, lock))
try:
    loop.run_until_complete(coros)
finally:
    loop.close()
```
will output:

```
coro 2: waiting for lock
coro 2: holding the lock
coro 1: waiting for lock
coro 2: releasing the lock
coro 1: holding the lock
coro 1: releasing the lock
```
Note that both [ async for](../reference/compound_stmts.html#async-for) and 

[can only be used inside a coroutine function declared with](../reference/compound_stmts.html#async-with)

`async with`[.](../reference/compound_stmts.html#async-def)

`async def`Coroutine functions are intended to be run inside a compatible event loop,
such as the [asyncio loop](../library/asyncio-eventloop.html#asyncio-event-loop).

Note

Changed in version 3.5.2: Starting with CPython 3.5.2, `__aiter__` can directly return
[asynchronous iterators](../glossary.html#term-asynchronous-iterator).  Returning
an [awaitable](../glossary.html#term-awaitable) object will result in a
[ PendingDeprecationWarning](../library/exceptions.html#PendingDeprecationWarning).

See more details in the [Asynchronous Iterators](../reference/datamodel.html#async-iterators) documentation
section.

See also

- **PEP 492**
- PEP written and implemented by Yury Selivanov. 

### PEP 465 - A dedicated infix operator for matrix multiplication[¶](#pep-465-a-dedicated-infix-operator-for-matrix-multiplication)

[ PEP 465](https://peps.python.org/pep-0465/) adds the 

`@` infix operator for matrix multiplication.
Currently, no builtin Python types implement the new operator, however, it
can be implemented by defining [,](../reference/datamodel.html#object.__matmul__)

`__matmul__()`[, and](../reference/datamodel.html#object.__rmatmul__)

`__rmatmul__()`[for regular, reflected, and in-place matrix multiplication. The semantics of these methods is similar to that of methods defining other infix arithmetic operators.](../reference/datamodel.html#object.__imatmul__)

`__imatmul__()`Matrix multiplication is a notably common operation in many fields of
mathematics, science, engineering, and the addition of `@` allows writing
cleaner code:

```
S = (H @ beta - r).T @ inv(H @ V @ H.T) @ (H @ beta - r)
```
instead of:

```
S = dot((dot(H, beta) - r).T,
        dot(inv(dot(dot(H, V), H.T)), dot(H, beta) - r))
```
NumPy 1.10 has support for the new operator:

```
>>> import numpy
>>> x = numpy.ones(3)
>>> x
array([ 1., 1., 1.])
>>> m = numpy.eye(3)
>>> m
array([[ 1., 0., 0.],
       [ 0., 1., 0.],
       [ 0., 0., 1.]])
>>> x @ m
array([ 1., 1., 1.])
```
See also

- **PEP 465**
- PEP written by Nathaniel J. Smith; implemented by Benjamin Peterson. 

### PEP 448 - Additional Unpacking Generalizations[¶](#pep-448-additional-unpacking-generalizations)

[ PEP 448](https://peps.python.org/pep-0448/) extends the allowed uses of the 

`*` iterable unpacking
operator and `**` dictionary unpacking operator.  It is now possible
to use an arbitrary number of unpackings in [function calls](../reference/expressions.html#calls):

```
>>> print(*[1], *[2], 3, *[4, 5])
1 2 3 4 5
>>> def fn(a, b, c, d):
...     print(a, b, c, d)
...
>>> fn(**{'a': 1, 'c': 3}, **{'b': 2, 'd': 4})
1 2 3 4
```
Similarly, tuple, list, set, and dictionary displays allow multiple
unpackings (see [Expression lists](../reference/expressions.html#exprlists) and [Dictionary displays](../reference/expressions.html#dict)):

```
>>> *range(4), 4
(0, 1, 2, 3, 4)
>>> [*range(4), 4]
[0, 1, 2, 3, 4]
>>> {*range(4), 4, *(5, 6, 7)}
{0, 1, 2, 3, 4, 5, 6, 7}
>>> {'x': 1, **{'y': 2}}
{'x': 1, 'y': 2}
```
See also

- **PEP 448**
- PEP written by Joshua Landau; implemented by Neil Girdhar, Thomas Wouters, and Joshua Landau. 

### PEP 461 - percent formatting support for bytes and bytearray[¶](#pep-461-percent-formatting-support-for-bytes-and-bytearray)

[ PEP 461](https://peps.python.org/pep-0461/) adds support for the 

`%`
[interpolation operator](../library/stdtypes.html#bytes-formatting)to

[and](../library/stdtypes.html#bytes)

`bytes`[.](../library/stdtypes.html#bytearray)

`bytearray`While interpolation is usually thought of as a string operation, there are
cases where interpolation on `bytes` or `bytearrays` makes sense, and the
work needed to make up for this missing functionality detracts from the
overall readability of the code.  This issue is particularly important when
dealing with wire format protocols, which are often a mixture of binary
and ASCII compatible text.

Examples:

```
>>> b'Hello %b!' % b'World'
b'Hello World!'
>>> b'x=%i y=%f' % (1, 2.5)
b'x=1 y=2.500000'
```
Unicode is not allowed for `%b`, but it is accepted by `%a` (equivalent of
`repr(obj).encode('ascii', 'backslashreplace')`):

```
>>> b'Hello %b!' % 'World'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: %b requires bytes, or an object that implements __bytes__, not 'str'
>>> b'price: %a' % '10€'
b"price: '10\\u20ac'"
```
Note that `%s` and `%r` conversion types, although supported, should
only be used in codebases that need compatibility with Python 2.

See also

- **PEP 461**
- PEP written by Ethan Furman; implemented by Neil Schemenauer and Ethan Furman. 

### PEP 484 - Type Hints[¶](#pep-484-type-hints)

Function annotation syntax has been a Python feature since version 3.0
([ PEP 3107](https://peps.python.org/pep-3107/)), however the semantics of annotations has been left undefined.

Experience has shown that the majority of function annotation uses were to provide type hints to function parameters and return values. It became evident that it would be beneficial for Python users, if the standard library included the base definitions and tools for type annotations.

[ PEP 484](https://peps.python.org/pep-0484/) introduces a 

[provisional module](../glossary.html#term-provisional-API)to provide these standard definitions and tools, along with some conventions for situations where annotations are not available.

For example, here is a simple function whose argument and return type are declared in the annotations:

```
def greeting(name: str) -> str:
    return 'Hello ' + name
```
While these annotations are available at runtime through the usual
[ __annotations__](../reference/datamodel.html#object.__annotations__) attribute, 

*no automatic type checking happens at runtime*. Instead, it is assumed that a separate off-line type checker (e.g.

[mypy](https://mypy-lang.org)) will be used for on-demand source code analysis.

The type system supports unions, generic types, and a special type
named [ Any](../library/typing.html#typing.Any) which is consistent with (i.e. assignable to
and from) all types.

### PEP 471 - os.scandir() function – a better and faster directory iterator[¶](#pep-471-os-scandir-function-a-better-and-faster-directory-iterator)

[ PEP 471](https://peps.python.org/pep-0471/) adds a new directory iteration function, 

[, to the standard library. Additionally,](../library/os.html#os.scandir)

`os.scandir()`[is now implemented using](../library/os.html#os.walk)

`os.walk()``scandir`, which makes it 3 to 5 times faster
on POSIX systems and 7 to 20 times faster on Windows systems.  This is
largely achieved by greatly reducing the number of calls to [required to walk a directory tree.](../library/os.html#os.stat)

`os.stat()`Additionally, `scandir` returns an iterator, as opposed to returning
a list of file names, which improves memory efficiency when iterating
over very large directories.

The following example shows a simple use of [ os.scandir()](../library/os.html#os.scandir) to display all
the files (excluding directories) in the given 

*path*that don’t start with

`'.'`. The [call will generally not make an additional system call:](../library/os.html#os.DirEntry.is_file)

`entry.is_file()````
for entry in os.scandir(path):
    if not entry.name.startswith('.') and entry.is_file():
        print(entry.name)
```
See also

- **PEP 471**
- PEP written and implemented by Ben Hoyt with the help of Victor Stinner. 

### PEP 475: Retry system calls failing with EINTR[¶](#pep-475-retry-system-calls-failing-with-eintr)

An [ errno.EINTR](../library/errno.html#errno.EINTR) error code is returned whenever a system call, that
is waiting for I/O, is interrupted by a signal.  Previously, Python would
raise 

[in such cases. This meant that, when writing a Python application, the developer had two choices:](../library/exceptions.html#InterruptedError)

`InterruptedError`- Ignore the - `InterruptedError`.
- Handle the - `InterruptedError`and attempt to restart the interrupted system call at every call site.

The first option makes an application fail intermittently. The second option adds a large amount of boilerplate that makes the code nearly unreadable. Compare:

```
print("Hello World")
```
and:

```
while True:
    try:
        print("Hello World")
        break
    except InterruptedError:
        continue
```
[ PEP 475](https://peps.python.org/pep-0475/) implements automatic retry of system calls on

`EINTR`.  This removes the burden of dealing with `EINTR`
or [in user code in most situations and makes Python programs, including the standard library, more robust. Note that the system call is only retried if the signal handler does not raise an exception.](../library/exceptions.html#InterruptedError)

`InterruptedError`Below is a list of functions which are now retried when interrupted by a signal:

- functions of the - `faulthandler`
- `os`- `fchdir()`- `fchmod()`- `fchown()`- `fdatasync()`- `fstat()`- `fstatvfs()`- `fsync()`- `ftruncate()`- `mkfifo()`- `mknod()`- `open()`- `posix_fadvise()`- `posix_fallocate()`- `pread()`- `pwrite()`- `read()`- `readv()`- `sendfile()`- `wait3()`- `wait4()`- `wait()`- `waitid()`- `waitpid()`- `write()`- `writev()`
- special cases: - `os.close()`- `os.dup2()`- `EINTR`
- `select`- `devpoll.poll()`- `epoll.poll()`- `kqueue.control()`- `poll.poll()`- `select()`
- methods of the - `socket`- `accept()`- `connect()`- `recv()`- `recvfrom()`- `recvmsg()`- `send()`- `sendall()`- `sendmsg()`- `sendto()`

See also

- **PEP 475**
- PEP and implementation written by Charles-François Natali and Victor Stinner, with the help of Antoine Pitrou (the French connection). 

### PEP 479: Change StopIteration handling inside generators[¶](#pep-479-change-stopiteration-handling-inside-generators)

The interaction of generators and [ StopIteration](../library/exceptions.html#StopIteration) in Python 3.4 and
earlier was sometimes surprising, and could conceal obscure bugs.  Previously,

`StopIteration` raised accidentally inside a generator function was
interpreted as the end of the iteration by the loop construct driving the
generator.[ PEP 479](https://peps.python.org/pep-0479/) changes the behavior of generators: when a 

`StopIteration`
exception is raised inside a generator, it is replaced with a
[before it exits the generator frame. The main goal of this change is to ease debugging in the situation where an unguarded](../library/exceptions.html#RuntimeError)

`RuntimeError`[call raises](../library/functions.html#next)

`next()``StopIteration` and causes the iteration controlled
by the generator to terminate silently. This is particularly pernicious in
combination with the `yield from` construct.This is a backwards incompatible change, so to enable the new behavior,
a [__future__](../glossary.html#term-__future__) import is necessary:

```
>>> from __future__ import generator_stop
>>> def gen():
...     next(iter([]))
...     yield
...
>>> next(gen())
Traceback (most recent call last):
  File "<stdin>", line 2, in gen
StopIteration
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: generator raised StopIteration
```
Without a `__future__` import, a [ PendingDeprecationWarning](../library/exceptions.html#PendingDeprecationWarning) will be
raised whenever a 

[exception is raised inside a generator.](../library/exceptions.html#StopIteration)

`StopIteration`See also

- **PEP 479**
- PEP written by Chris Angelico and Guido van Rossum. Implemented by Chris Angelico, Yury Selivanov and Nick Coghlan. 

### PEP 485: A function for testing approximate equality[¶](#pep-485-a-function-for-testing-approximate-equality)

[ PEP 485](https://peps.python.org/pep-0485/) adds the 

[and](../library/math.html#math.isclose)

`math.isclose()`[functions which tell whether two values are approximately equal or “close” to each other. Whether or not two values are considered close is determined according to given absolute and relative tolerances. Relative tolerance is the maximum allowed difference between](../library/cmath.html#cmath.isclose)

`cmath.isclose()``isclose`
arguments, relative to the larger absolute value:```
>>> import math
>>> a = 5.0
>>> b = 4.99998
>>> math.isclose(a, b, rel_tol=1e-5)
True
>>> math.isclose(a, b, rel_tol=1e-6)
False
```
It is also possible to compare two values using absolute tolerance, which must be a non-negative value:

```
>>> import math
>>> a = 5.0
>>> b = 4.99998
>>> math.isclose(a, b, abs_tol=0.00003)
True
>>> math.isclose(a, b, abs_tol=0.00001)
False
```
See also

- **PEP 485**
- PEP written by Christopher Barker; implemented by Chris Barker and Tal Einat. 

### PEP 486: Make the Python Launcher aware of virtual environments[¶](#pep-486-make-the-python-launcher-aware-of-virtual-environments)

[ PEP 486](https://peps.python.org/pep-0486/) makes the Windows launcher (see 

[) aware of an active virtual environment. When the default interpreter would be used and the](https://peps.python.org/pep-0397/)

**PEP 397**`VIRTUAL_ENV` environment variable is set, the interpreter in the virtual
environment will be used.See also

- **PEP 486**
- PEP written and implemented by Paul Moore. 

### PEP 488: Elimination of PYO files[¶](#pep-488-elimination-of-pyo-files)

[ PEP 488](https://peps.python.org/pep-0488/) does away with the concept of 

`.pyo` files. This means that
`.pyc` files represent both unoptimized and optimized bytecode. To prevent the
need to constantly regenerate bytecode files, `.pyc` files now have an
optional `opt-` tag in their name when the bytecode is optimized. This has the
side-effect of no more bytecode file name clashes when running under either
[or](../using/cmdline.html#cmdoption-O)

`-O`[. Consequently, bytecode files generated from](../using/cmdline.html#cmdoption-OO)

`-OO``-O`, and `-OO` may now exist simultaneously.
[has an updated API to help with this change.](../library/importlib.html#importlib.util.cache_from_source)

`importlib.util.cache_from_source()`See also

- **PEP 488**
- PEP written and implemented by Brett Cannon. 

### PEP 489: Multi-phase extension module initialization[¶](#pep-489-multi-phase-extension-module-initialization)

[ PEP 489](https://peps.python.org/pep-0489/) updates extension module initialization to take advantage of the
two step module loading mechanism introduced by 

[in Python 3.4.](https://peps.python.org/pep-0451/)

**PEP 451**This change brings the import semantics of extension modules that opt-in to using the new mechanism much closer to those of Python source and bytecode modules, including the ability to use any valid identifier as a module name, rather than being restricted to ASCII.

See also

- **PEP 489**
- PEP written by Petr Viktorin, Stefan Behnel, and Nick Coghlan; implemented by Petr Viktorin. 

## Other Language Changes[¶](#other-language-changes)

Some smaller changes made to the core Python language are:

- Added the - `"namereplace"`error handlers. The- `"backslashreplace"`error handlers now work with decoding and translating. (Contributed by Serhiy Storchaka in- [bpo-19676](https://bugs.python.org/issue?@action=redirect&bpo=19676)and- [bpo-22286](https://bugs.python.org/issue?@action=redirect&bpo=22286).)
- The - `-b`- `bytes`- `int`- [bpo-23681](https://bugs.python.org/issue?@action=redirect&bpo=23681).)
- New Kazakh - `kz1048`and Tajik- `koi8_t`- [codecs](../library/codecs.html#standard-encodings). (Contributed by Serhiy Storchaka in- [bpo-22682](https://bugs.python.org/issue?@action=redirect&bpo=22682)and- [bpo-22681](https://bugs.python.org/issue?@action=redirect&bpo=22681).)
- Property docstrings are now writable. This is especially useful for - `collections.namedtuple()`- [bpo-24064](https://bugs.python.org/issue?@action=redirect&bpo=24064).)
- Circular imports involving relative imports are now supported. (Contributed by Brett Cannon and Antoine Pitrou in - [bpo-17636](https://bugs.python.org/issue?@action=redirect&bpo=17636).)

## New Modules[¶](#new-modules)

### typing[¶](#typing)

The new `typing`[provisional](../glossary.html#term-provisional-API) module
provides standard definitions and tools for function type annotations.
See [Type Hints](#whatsnew-pep-484) for more information.

### zipapp[¶](#zipapp)

The new [ zipapp](../library/zipapp.html#module-zipapp) module (specified in 

[) provides an API and command line tool for creating executable Python Zip Applications, which were introduced in Python 2.6 in](https://peps.python.org/pep-0441/)

**PEP 441**[bpo-1739468](https://bugs.python.org/issue?@action=redirect&bpo=1739468), but which were not well publicized, either at the time or since.

With the new module, bundling your application is as simple as putting all
the files, including a `__main__.py` file, into a directory `myapp`
and running:

```
$ python -m zipapp myapp
$ python myapp.pyz
```
The module implementation has been contributed by Paul Moore in
[bpo-23491](https://bugs.python.org/issue?@action=redirect&bpo=23491).

See also

[ PEP 441](https://peps.python.org/pep-0441/) – Improving Python ZIP Application Support

## Improved Modules[¶](#improved-modules)

### argparse[¶](#argparse)

The [ ArgumentParser](../library/argparse.html#argparse.ArgumentParser) class now allows disabling

[abbreviated usage](../library/argparse.html#prefix-matching)of long options by setting

[allow_abbrev](../library/argparse.html#allow-abbrev)to

`False`.  (Contributed by Jonathan Paugh,
Steven Bethard, paul j3 and Daniel Eriksson in [bpo-14910](https://bugs.python.org/issue?@action=redirect&bpo=14910).)

### asyncio[¶](#asyncio)

Since the [ asyncio](../library/asyncio.html#module-asyncio) module is 

[provisional](../glossary.html#term-provisional-API), all changes introduced in Python 3.5 have also been backported to Python 3.4.x.

Notable changes in the [ asyncio](../library/asyncio.html#module-asyncio) module since Python 3.4.0:

- New debugging APIs: - `loop.set_debug()`- `loop.get_debug()`
- The proactor event loop now supports SSL. (Contributed by Antoine Pitrou and Victor Stinner in - [bpo-22560](https://bugs.python.org/issue?@action=redirect&bpo=22560).)
- A new - `loop.is_closed()`- [bpo-21326](https://bugs.python.org/issue?@action=redirect&bpo=21326).)
- A new - `loop.create_task()`- `Task`- `create_task`method is also used by all asyncio functions that wrap coroutines into tasks, such as- `asyncio.wait()`- `asyncio.gather()`
- A new - `transport.get_write_buffer_limits()`- *high-*and- *low-*water limits of the flow control. (Contributed by Victor Stinner.)
- The - `async()`function is deprecated in favor of- `ensure_future()`
- New - `loop.set_task_factory()`- `loop.get_task_factory()`- `loop.create_task()`
- New - `Queue.join()`- `Queue.task_done()`
- The - `JoinableQueue`class was removed, in favor of the- `asyncio.Queue`

Updates in 3.5.1:

- The - `ensure_future()`- `loop.run_until_complete()`- [awaitable objects](../glossary.html#term-awaitable). (Contributed by Yury Selivanov.)
- New - `run_coroutine_threadsafe()`
- New - `Transport.is_closing()`
- The - `loop.create_server()`

Updates in 3.5.2:

- New - `loop.create_future()`- [uvloop](https://github.com/MagicStack/uvloop), to provide a faster- `asyncio.Future`
- New - `loop.get_exception_handler()`
- New - `StreamReader.readuntil()`
- The - `loop.create_connection()`- `loop.create_server()`- `getaddrinfo`function if the address is already resolved. (Contributed by A. Jesse Jiryu Davis.)
- The - `loop.sock_connect(sock, address)`- *address*to be resolved prior to the call. (Contributed by A. Jesse Jiryu Davis.)

### bz2[¶](#bz2)

The [ BZ2Decompressor.decompress](../library/bz2.html#bz2.BZ2Decompressor.decompress)
method now accepts an optional 

*max_length*argument to limit the maximum size of decompressed data. (Contributed by Nikolaus Rath in

[bpo-15955](https://bugs.python.org/issue?@action=redirect&bpo=15955).)

### cgi[¶](#cgi)

The `FieldStorage` class now supports the [context manager](../glossary.html#term-context-manager)
protocol.  (Contributed by Berker Peksag in [bpo-20289](https://bugs.python.org/issue?@action=redirect&bpo=20289).)

### cmath[¶](#cmath)

A new function [ isclose()](../library/cmath.html#cmath.isclose) provides a way to test for approximate
equality.  (Contributed by Chris Barker and Tal Einat in 

[bpo-24270](https://bugs.python.org/issue?@action=redirect&bpo=24270).)

### code[¶](#code)

The [ InteractiveInterpreter.showtraceback()](../library/code.html#code.InteractiveInterpreter.showtraceback)
method now prints the full chained traceback, just like the interactive
interpreter.  (Contributed by Claudiu Popa in 

[bpo-17442](https://bugs.python.org/issue?@action=redirect&bpo=17442).)

### collections[¶](#collections)

The [ OrderedDict](../library/collections.html#collections.OrderedDict) class is now implemented in C, which
makes it 4 to 100 times faster.  (Contributed by Eric Snow in 

[bpo-16991](https://bugs.python.org/issue?@action=redirect&bpo=16991).)

`OrderedDict.items()`, `OrderedDict.keys()`,
and `OrderedDict.values()` views now support [ reversed()](../library/functions.html#reversed) iteration.
(Contributed by Serhiy Storchaka in 

[bpo-19505](https://bugs.python.org/issue?@action=redirect&bpo=19505).)

The [ deque](../library/collections.html#collections.deque) class now defines

[,](../library/collections.html#collections.deque.index)

`index()`[, and](../library/collections.html#collections.deque.insert)

`insert()`[, and supports the](../library/collections.html#collections.deque.copy)

`copy()``+` and `*` operators.
This allows deques to be recognized as a [and improves their substitutability for lists. (Contributed by Raymond Hettinger in](../library/collections.abc.html#collections.abc.MutableSequence)

`MutableSequence`[bpo-23704](https://bugs.python.org/issue?@action=redirect&bpo=23704).)

Docstrings produced by [ namedtuple()](../library/collections.html#collections.namedtuple) can now be updated:

```
Point = namedtuple('Point', ['x', 'y'])
Point.__doc__ += ': Cartesian coordinate'
Point.x.__doc__ = 'abscissa'
Point.y.__doc__ = 'ordinate'
```
(Contributed by Berker Peksag in [bpo-24064](https://bugs.python.org/issue?@action=redirect&bpo=24064).)

The [ UserString](../library/collections.html#collections.UserString) class now implements the

[,](../library/pickle.html#object.__getnewargs__)

`__getnewargs__()`[,](../reference/datamodel.html#object.__rmod__)

`__rmod__()`[,](../library/stdtypes.html#str.casefold)

`casefold()`[,](../library/stdtypes.html#str.format_map)

`format_map()`[, and](../library/stdtypes.html#str.isprintable)

`isprintable()`[methods to match the corresponding methods of](../library/stdtypes.html#str.maketrans)

`maketrans()`[. (Contributed by Joe Jevnik in](../library/stdtypes.html#str)

`str`[bpo-22189](https://bugs.python.org/issue?@action=redirect&bpo=22189).)

### collections.abc[¶](#collections-abc)

The `Sequence.index()` method now
accepts *start* and *stop* arguments to match the corresponding methods
of [ tuple](../library/stdtypes.html#tuple), 

[, etc. (Contributed by Devin Jeanpierre in](../library/stdtypes.html#list)

`list`[bpo-23086](https://bugs.python.org/issue?@action=redirect&bpo=23086).)

A new [ Generator](../library/collections.abc.html#collections.abc.Generator) abstract base class. (Contributed
by Stefan Behnel in 

[bpo-24018](https://bugs.python.org/issue?@action=redirect&bpo=24018).)

New [ Awaitable](../library/collections.abc.html#collections.abc.Awaitable), 

[,](../library/collections.abc.html#collections.abc.Coroutine)

`Coroutine`[, and](../library/collections.abc.html#collections.abc.AsyncIterator)

`AsyncIterator`[abstract base classes. (Contributed by Yury Selivanov in](../library/collections.abc.html#collections.abc.AsyncIterable)

`AsyncIterable`[bpo-24184](https://bugs.python.org/issue?@action=redirect&bpo=24184).)

For earlier Python versions, a backport of the new ABCs is available in an
external [PyPI package](https://pypi.org/project/backports_abc/).

### compileall[¶](#compileall)

A new [ compileall](../library/compileall.html#module-compileall) option, 

`-j `*N*, allows running *N*workers simultaneously to perform parallel bytecode compilation. The

[function has a corresponding](../library/compileall.html#compileall.compile_dir)

`compile_dir()``workers`
parameter.  (Contributed by Claudiu Popa in [bpo-16104](https://bugs.python.org/issue?@action=redirect&bpo=16104).)

Another new option, `-r`, allows controlling the maximum recursion
level for subdirectories.  (Contributed by Claudiu Popa in [bpo-19628](https://bugs.python.org/issue?@action=redirect&bpo=19628).)

The `-q` command line option can now be specified more than once, in
which case all output, including errors, will be suppressed.  The corresponding
`quiet` parameter in [ compile_dir()](../library/compileall.html#compileall.compile_dir),

[, and](../library/compileall.html#compileall.compile_file)

`compile_file()`[can now accept an integer value indicating the level of output suppression. (Contributed by Thomas Kluyver in](../library/compileall.html#compileall.compile_path)

`compile_path()`[bpo-21338](https://bugs.python.org/issue?@action=redirect&bpo=21338).)

### concurrent.futures[¶](#concurrent-futures)

The [ Executor.map()](../library/concurrent.futures.html#concurrent.futures.Executor.map) method now accepts a

*chunksize*argument to allow batching of tasks to improve performance when

[is used. (Contributed by Dan O’Reilly in](../library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor)

`ProcessPoolExecutor()`[bpo-11271](https://bugs.python.org/issue?@action=redirect&bpo=11271).)

The number of workers in the [ ThreadPoolExecutor](../library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor)
constructor is optional now.  The default value is 5 times the number of CPUs.
(Contributed by Claudiu Popa in 

[bpo-21527](https://bugs.python.org/issue?@action=redirect&bpo=21527).)

### configparser[¶](#configparser)

[ configparser](../library/configparser.html#module-configparser) now provides a way to customize the conversion
of values by specifying a dictionary of converters in the

[constructor, or by defining them as methods in](../library/configparser.html#configparser.ConfigParser)

`ConfigParser``ConfigParser` subclasses.  Converters defined in
a parser instance are inherited by its section proxies.Example:

```
>>> import configparser
>>> conv = {}
>>> conv['list'] = lambda v: [e.strip() for e in v.split() if e.strip()]
>>> cfg = configparser.ConfigParser(converters=conv)
>>> cfg.read_string("""
... [s]
... list = a b c d e f g
... """)
>>> cfg.get('s', 'list')
'a b c d e f g'
>>> cfg.getlist('s', 'list')
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> section = cfg['s']
>>> section.getlist('list')
['a', 'b', 'c', 'd', 'e', 'f', 'g']
```
(Contributed by Łukasz Langa in [bpo-18159](https://bugs.python.org/issue?@action=redirect&bpo=18159).)

### contextlib[¶](#contextlib)

The new `redirect_stderr()`[context manager](../glossary.html#term-context-manager) (similar to
[ redirect_stdout()](../library/contextlib.html#contextlib.redirect_stdout)) makes it easier for utility scripts to
handle inflexible APIs that write their output to 

[and don’t provide any options to redirect it:](../library/sys.html#sys.stderr)

`sys.stderr````
>>> import contextlib, io, logging
>>> f = io.StringIO()
>>> with contextlib.redirect_stderr(f):
...     logging.warning('warning')
...
>>> f.getvalue()
'WARNING:root:warning\n'
```
(Contributed by Berker Peksag in [bpo-22389](https://bugs.python.org/issue?@action=redirect&bpo=22389).)

### csv[¶](#csv)

The [ writerow()](../library/csv.html#csv.csvwriter.writerow) method now supports arbitrary iterables,
not just sequences.  (Contributed by Serhiy Storchaka in 

[bpo-23171](https://bugs.python.org/issue?@action=redirect&bpo=23171).)

### curses[¶](#curses)

The new [ update_lines_cols()](../library/curses.html#curses.update_lines_cols) function updates the 

[and](../library/curses.html#curses.LINES)

`LINES`[module variables. This is useful for detecting manual screen resizing. (Contributed by Arnon Yaari in](../library/curses.html#curses.COLS)

`COLS`[bpo-4254](https://bugs.python.org/issue?@action=redirect&bpo=4254).)

### dbm[¶](#dbm)

[ dumb.open](../library/dbm.html#dbm.dumb.open) always creates a new database when the flag
has the value 

`"n"`.  (Contributed by Claudiu Popa in [bpo-18039](https://bugs.python.org/issue?@action=redirect&bpo=18039).)

### difflib[¶](#difflib)

The charset of HTML documents generated by
[ HtmlDiff.make_file()](../library/difflib.html#difflib.HtmlDiff.make_file)
can now be customized by using a new 

*charset*keyword-only argument. The default charset of HTML document changed from

`"ISO-8859-1"`
to `"utf-8"`.
(Contributed by Berker Peksag in [bpo-2052](https://bugs.python.org/issue?@action=redirect&bpo=2052).)

The [ diff_bytes()](../library/difflib.html#difflib.diff_bytes) function can now compare lists of byte
strings.  This fixes a regression from Python 2.
(Contributed by Terry J. Reedy and Greg Ward in 

[bpo-17445](https://bugs.python.org/issue?@action=redirect&bpo=17445).)

### distutils[¶](#distutils)

Both the `build` and `build_ext` commands now accept a `-j` option to
enable parallel building of extension modules.
(Contributed by Antoine Pitrou in [bpo-5309](https://bugs.python.org/issue?@action=redirect&bpo=5309).)

The `distutils` module now supports `xz` compression, and can be
enabled by passing `xztar` as an argument to `bdist --format`.
(Contributed by Serhiy Storchaka in [bpo-16314](https://bugs.python.org/issue?@action=redirect&bpo=16314).)

### doctest[¶](#doctest)

The [ DocTestSuite()](../library/doctest.html#doctest.DocTestSuite) function returns an empty

[if](../library/unittest.html#unittest.TestSuite)

`unittest.TestSuite`*module*contains no docstrings, instead of raising

[. (Contributed by Glenn Jones in](../library/exceptions.html#ValueError)

`ValueError`[bpo-15916](https://bugs.python.org/issue?@action=redirect&bpo=15916).)

### email[¶](#email)

A new policy option [ Policy.mangle_from_](../library/email.policy.html#email.policy.Policy.mangle_from_)
controls whether or not lines that start with 

`"From "` in email bodies are
prefixed with a `">"` character by generators.  The default is `True` for
[and](../library/email.policy.html#email.policy.compat32)

`compat32``False` for all other policies.
(Contributed by Milan Oberkirch in [bpo-20098](https://bugs.python.org/issue?@action=redirect&bpo=20098).)

A new
[ Message.get_content_disposition()](../library/email.compat32-message.html#email.message.Message.get_content_disposition)
method provides easy access to a canonical value for the

*Content-Disposition*header. (Contributed by Abhilash Raj in

[bpo-21083](https://bugs.python.org/issue?@action=redirect&bpo=21083).)

A new policy option [ EmailPolicy.utf8](../library/email.policy.html#email.policy.EmailPolicy.utf8)
can be set to 

`True` to encode email headers using the UTF-8 charset instead
of using encoded words.  This allows `Messages` to be formatted according to
[and used with an SMTP server that supports the](https://datatracker.ietf.org/doc/html/rfc6532.html)

**RFC 6532**

**RFC 6531**`SMTPUTF8` extension.  (Contributed by R. David Murray in
[bpo-24211](https://bugs.python.org/issue?@action=redirect&bpo=24211).)

The [ mime.text.MIMEText](../library/email.mime.html#email.mime.text.MIMEText) constructor now
accepts a 

[instance. (Contributed by Claude Paroz and Berker Peksag in](../library/email.charset.html#email.charset.Charset)

`charset.Charset`[bpo-16324](https://bugs.python.org/issue?@action=redirect&bpo=16324).)

### enum[¶](#enum)

The [ Enum](../library/enum.html#enum.Enum) callable has a new parameter 

*start*to specify the initial number of enum values if only

*names*are provided:

```
>>> Animal = enum.Enum('Animal', 'cat dog', start=10)
>>> Animal.cat
<Animal.cat: 10>
>>> Animal.dog
<Animal.dog: 11>
```
(Contributed by Ethan Furman in [bpo-21706](https://bugs.python.org/issue?@action=redirect&bpo=21706).)

### faulthandler[¶](#faulthandler)

The [ enable()](../library/faulthandler.html#faulthandler.enable), 

[,](../library/faulthandler.html#faulthandler.register)

`register()`[and](../library/faulthandler.html#faulthandler.dump_traceback)

`dump_traceback()`[functions now accept file descriptors in addition to file-like objects. (Contributed by Wei Wu in](../library/faulthandler.html#faulthandler.dump_traceback_later)

`dump_traceback_later()`[bpo-23566](https://bugs.python.org/issue?@action=redirect&bpo=23566).)

### functools[¶](#functools)

Most of the [ lru_cache()](../library/functools.html#functools.lru_cache) machinery is now implemented in C, making
it significantly faster.  (Contributed by Matt Joiner, Alexey Kachayev, and
Serhiy Storchaka in 

[bpo-14373](https://bugs.python.org/issue?@action=redirect&bpo=14373).)

### glob[¶](#glob)

The [ iglob()](../library/glob.html#glob.iglob) and 

[functions now support recursive search in subdirectories, using the](../library/glob.html#glob.glob)

`glob()``"**"` pattern.
(Contributed by Serhiy Storchaka in [bpo-13968](https://bugs.python.org/issue?@action=redirect&bpo=13968).)

### gzip[¶](#gzip)

The *mode* argument of the [ GzipFile](../library/gzip.html#gzip.GzipFile) constructor now
accepts 

`"x"` to request exclusive creation.
(Contributed by Tim Heaney in [bpo-19222](https://bugs.python.org/issue?@action=redirect&bpo=19222).)

### heapq[¶](#heapq)

Element comparison in [ merge()](../library/heapq.html#heapq.merge) can now be customized by
passing a 

[key function](../glossary.html#term-key-function)in a new optional

*key*keyword argument, and a new optional

*reverse*keyword argument can be used to reverse element comparison:

```
>>> import heapq
>>> a = ['9', '777', '55555']
>>> b = ['88', '6666']
>>> list(heapq.merge(a, b, key=len))
['9', '88', '777', '6666', '55555']
>>> list(heapq.merge(reversed(a), reversed(b), key=len, reverse=True))
['55555', '6666', '777', '88', '9']
```
(Contributed by Raymond Hettinger in [bpo-13742](https://bugs.python.org/issue?@action=redirect&bpo=13742).)

### http[¶](#http)

A new [ HTTPStatus](../library/http.html#http.HTTPStatus) enum that defines a set of
HTTP status codes, reason phrases and long descriptions written in English.
(Contributed by Demian Brecht in 

[bpo-21793](https://bugs.python.org/issue?@action=redirect&bpo=21793).)

### http.client[¶](#http-client)

[ HTTPConnection.getresponse()](../library/http.client.html#http.client.HTTPConnection.getresponse)
now raises a 

[exception when a remote server connection is closed unexpectedly. Additionally, if a](../library/http.client.html#http.client.RemoteDisconnected)

`RemoteDisconnected`[(of which](../library/exceptions.html#ConnectionError)

`ConnectionError``RemoteDisconnected`
is a subclass) is raised, the client socket is now closed automatically,
and will reconnect on the next request:```
import http.client
conn = http.client.HTTPConnection('www.python.org')
for retries in range(3):
    try:
        conn.request('GET', '/')
        resp = conn.getresponse()
    except http.client.RemoteDisconnected:
        pass
```
(Contributed by Martin Panter in [bpo-3566](https://bugs.python.org/issue?@action=redirect&bpo=3566).)

### idlelib and IDLE[¶](#idlelib-and-idle)

Since idlelib implements the IDLE shell and editor and is not intended for
import by other programs, it gets improvements with every release.  See
`Lib/idlelib/NEWS.txt` for a cumulative list of changes since 3.4.0,
as well as changes made in future 3.5.x releases. This file is also available
from the IDLE  dialog.

### imaplib[¶](#imaplib)

The [ IMAP4](../library/imaplib.html#imaplib.IMAP4) class now supports the 

[context manager](../glossary.html#term-context-manager)protocol. When used in a

[statement, the IMAP4](../reference/compound_stmts.html#with)

`with``LOGOUT`
command will be called automatically at the end of the block.
(Contributed by Tarek Ziadé and Serhiy Storchaka in [bpo-4972](https://bugs.python.org/issue?@action=redirect&bpo=4972).)

The [ imaplib](../library/imaplib.html#module-imaplib) module now supports 

[(ENABLE Extension) and](https://datatracker.ietf.org/doc/html/rfc5161.html)

**RFC 5161**[(UTF-8 Support) via the](https://datatracker.ietf.org/doc/html/rfc6855.html)

**RFC 6855**[method. A new](../library/imaplib.html#imaplib.IMAP4.enable)

`IMAP4.enable()`[attribute tracks whether or not](../library/imaplib.html#imaplib.IMAP4.utf8_enabled)

`IMAP4.utf8_enabled`[support is enabled. (Contributed by Milan Oberkirch, R. David Murray, and Maciej Szulik in](https://datatracker.ietf.org/doc/html/rfc6855.html)

**RFC 6855**[bpo-21800](https://bugs.python.org/issue?@action=redirect&bpo=21800).)

The [ imaplib](../library/imaplib.html#module-imaplib) module now automatically encodes non-ASCII string usernames
and passwords using UTF-8, as recommended by the RFCs.  (Contributed by Milan
Oberkirch in 

[bpo-21800](https://bugs.python.org/issue?@action=redirect&bpo=21800).)

### imghdr[¶](#imghdr)

The `what()` function now recognizes the
[OpenEXR](https://www.openexr.com) format
(contributed by Martin Vignali and Claudiu Popa in [bpo-20295](https://bugs.python.org/issue?@action=redirect&bpo=20295)),
and the [WebP](https://en.wikipedia.org/wiki/WebP) format
(contributed by Fabrice Aneche and Claudiu Popa in [bpo-20197](https://bugs.python.org/issue?@action=redirect&bpo=20197).)

### importlib[¶](#importlib)

The [ util.LazyLoader](../library/importlib.html#importlib.util.LazyLoader) class allows for
lazy loading of modules in applications where startup time is important.
(Contributed by Brett Cannon in 

[bpo-17621](https://bugs.python.org/issue?@action=redirect&bpo=17621).)

The [ abc.InspectLoader.source_to_code()](../library/importlib.html#importlib.abc.InspectLoader.source_to_code)
method is now a static method.  This makes it easier to initialize a module
object with code compiled from a string by running

`exec(code, module.__dict__)`.
(Contributed by Brett Cannon in [bpo-21156](https://bugs.python.org/issue?@action=redirect&bpo=21156).)

The new [ util.module_from_spec()](../library/importlib.html#importlib.util.module_from_spec)
function is now the preferred way to create a new module.  As opposed to
creating a 

[instance directly, this new function will set the various import-controlled attributes based on the passed-in spec object. (Contributed by Brett Cannon in](../library/types.html#types.ModuleType)

`types.ModuleType`[bpo-20383](https://bugs.python.org/issue?@action=redirect&bpo=20383).)

### inspect[¶](#inspect)

Both the [ Signature](../library/inspect.html#inspect.Signature) and 

[classes are now picklable and hashable. (Contributed by Yury Selivanov in](../library/inspect.html#inspect.Parameter)

`Parameter`[bpo-20726](https://bugs.python.org/issue?@action=redirect&bpo=20726)and

[bpo-20334](https://bugs.python.org/issue?@action=redirect&bpo=20334).)

A new
[ BoundArguments.apply_defaults()](../library/inspect.html#inspect.BoundArguments.apply_defaults)
method provides a way to set default values for missing arguments:

```
>>> def foo(a, b='ham', *args): pass
>>> ba = inspect.signature(foo).bind('spam')
>>> ba.apply_defaults()
>>> ba.arguments
OrderedDict([('a', 'spam'), ('b', 'ham'), ('args', ())])
```
(Contributed by Yury Selivanov in [bpo-24190](https://bugs.python.org/issue?@action=redirect&bpo=24190).)

A new class method
[ Signature.from_callable()](../library/inspect.html#inspect.Signature.from_callable) makes
subclassing of 

[easier. (Contributed by Yury Selivanov and Eric Snow in](../library/inspect.html#inspect.Signature)

`Signature`[bpo-17373](https://bugs.python.org/issue?@action=redirect&bpo=17373).)

The [ signature()](../library/inspect.html#inspect.signature) function now accepts a 

*follow_wrapped*optional keyword argument, which, when set to

`False`, disables automatic
following of `__wrapped__` links.
(Contributed by Yury Selivanov in [bpo-20691](https://bugs.python.org/issue?@action=redirect&bpo=20691).)

A set of new functions to inspect
[coroutine functions](../glossary.html#term-coroutine-function) and
[coroutine objects](../glossary.html#term-coroutine) has been added:
[ iscoroutine()](../library/inspect.html#inspect.iscoroutine), 

[,](../library/inspect.html#inspect.iscoroutinefunction)

`iscoroutinefunction()`[,](../library/inspect.html#inspect.isawaitable)

`isawaitable()`[, and](../library/inspect.html#inspect.getcoroutinelocals)

`getcoroutinelocals()`[. (Contributed by Yury Selivanov in](../library/inspect.html#inspect.getcoroutinestate)

`getcoroutinestate()`[bpo-24017](https://bugs.python.org/issue?@action=redirect&bpo=24017)and

[bpo-24400](https://bugs.python.org/issue?@action=redirect&bpo=24400).)

The [ stack()](../library/inspect.html#inspect.stack), 

[,](../library/inspect.html#inspect.trace)

`trace()`[, and](../library/inspect.html#inspect.getouterframes)

`getouterframes()`[functions now return a list of named tuples. (Contributed by Daniel Shahaf in](../library/inspect.html#inspect.getinnerframes)

`getinnerframes()`[bpo-16808](https://bugs.python.org/issue?@action=redirect&bpo=16808).)

### io[¶](#io)

A new [ BufferedIOBase.readinto1()](../library/io.html#io.BufferedIOBase.readinto1)
method, that uses at most one call to the underlying raw stream’s

[or](../library/io.html#io.RawIOBase.read)

`RawIOBase.read()`[methods. (Contributed by Nikolaus Rath in](../library/io.html#io.RawIOBase.readinto)

`RawIOBase.readinto()`[bpo-20578](https://bugs.python.org/issue?@action=redirect&bpo=20578).)

### ipaddress[¶](#ipaddress)

Both the [ IPv4Network](../library/ipaddress.html#ipaddress.IPv4Network) and 

[classes now accept an](../library/ipaddress.html#ipaddress.IPv6Network)

`IPv6Network``(address, netmask)` tuple argument, so as to easily construct
network objects from existing addresses:```
>>> import ipaddress
>>> ipaddress.IPv4Network(('127.0.0.0', 8))
IPv4Network('127.0.0.0/8')
>>> ipaddress.IPv4Network(('127.0.0.0', '255.0.0.0'))
IPv4Network('127.0.0.0/8')
```
(Contributed by Peter Moody and Antoine Pitrou in [bpo-16531](https://bugs.python.org/issue?@action=redirect&bpo=16531).)

A new [ reverse_pointer](../library/ipaddress.html#ipaddress.IPv4Address.reverse_pointer) attribute for the

[and](../library/ipaddress.html#ipaddress.IPv4Address)

`IPv4Address`[classes returns the name of the reverse DNS PTR record:](../library/ipaddress.html#ipaddress.IPv6Address)

`IPv6Address````
>>> import ipaddress
>>> addr = ipaddress.IPv4Address('127.0.0.1')
>>> addr.reverse_pointer
'1.0.0.127.in-addr.arpa'
>>> addr6 = ipaddress.IPv6Address('::1')
>>> addr6.reverse_pointer
'1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa'
```
(Contributed by Leon Weber in [bpo-20480](https://bugs.python.org/issue?@action=redirect&bpo=20480).)

### json[¶](#json)

The [ json.tool](../library/json.html#module-json.tool) command line interface now preserves the order of keys in
JSON objects passed in input.  The new 

`--sort-keys` option can be used
to sort the keys alphabetically. (Contributed by Berker Peksag
in [bpo-21650](https://bugs.python.org/issue?@action=redirect&bpo=21650).)

JSON decoder now raises [ JSONDecodeError](../library/json.html#json.JSONDecodeError) instead of

[to provide better context information about the error. (Contributed by Serhiy Storchaka in](../library/exceptions.html#ValueError)

`ValueError`[bpo-19361](https://bugs.python.org/issue?@action=redirect&bpo=19361).)

### linecache[¶](#linecache)

A new [ lazycache()](../library/linecache.html#linecache.lazycache) function can be used to capture information
about a non-file-based module to permit getting its lines later via

[. This avoids doing I/O until a line is actually needed, without having to carry the module globals around indefinitely. (Contributed by Robert Collins in](../library/linecache.html#linecache.getline)

`getline()`[bpo-17911](https://bugs.python.org/issue?@action=redirect&bpo=17911).)

### locale[¶](#locale)

A new [ delocalize()](../library/locale.html#locale.delocalize) function can be used to convert a string into
a normalized number string, taking the 

`LC_NUMERIC` settings into account:```
>>> import locale
>>> locale.setlocale(locale.LC_NUMERIC, 'de_DE.UTF-8')
'de_DE.UTF-8'
>>> locale.delocalize('1.234,56')
'1234.56'
>>> locale.setlocale(locale.LC_NUMERIC, 'en_US.UTF-8')
'en_US.UTF-8'
>>> locale.delocalize('1,234.56')
'1234.56'
```
(Contributed by Cédric Krier in [bpo-13918](https://bugs.python.org/issue?@action=redirect&bpo=13918).)

### logging[¶](#logging)

All logging methods (`Logger`[ log()](../library/logging.html#logging.Logger.log),

[,](../library/logging.html#logging.Logger.exception)

`exception()`[,](../library/logging.html#logging.Logger.critical)

`critical()`[, etc.), now accept exception instances as an](../library/logging.html#logging.Logger.debug)

`debug()`*exc_info*argument, in addition to boolean values and exception tuples:

```
>>> import logging
>>> try:
...     1/0
... except ZeroDivisionError as ex:
...     logging.error('exception', exc_info=ex)
ERROR:root:exception
```
(Contributed by Yury Selivanov in [bpo-20537](https://bugs.python.org/issue?@action=redirect&bpo=20537).)

The [ handlers.HTTPHandler](../library/logging.handlers.html#logging.handlers.HTTPHandler) class now
accepts an optional 

[instance to configure SSL settings used in an HTTP connection. (Contributed by Alex Gaynor in](../library/ssl.html#ssl.SSLContext)

`ssl.SSLContext`[bpo-22788](https://bugs.python.org/issue?@action=redirect&bpo=22788).)

The [ handlers.QueueListener](../library/logging.handlers.html#logging.handlers.QueueListener) class now
takes a 

*respect_handler_level*keyword argument which, if set to

`True`,
will pass messages to handlers taking handler levels into account.
(Contributed by Vinay Sajip.)### lzma[¶](#lzma)

The [ LZMADecompressor.decompress()](../library/lzma.html#lzma.LZMADecompressor.decompress)
method now accepts an optional 

*max_length*argument to limit the maximum size of decompressed data. (Contributed by Martin Panter in

[bpo-15955](https://bugs.python.org/issue?@action=redirect&bpo=15955).)

### math[¶](#math)

Two new constants have been added to the [ math](../library/math.html#module-math) module: 

[and](../library/math.html#math.inf)

`inf`[. (Contributed by Mark Dickinson in](../library/math.html#math.nan)

`nan`[bpo-23185](https://bugs.python.org/issue?@action=redirect&bpo=23185).)

A new function [ isclose()](../library/math.html#math.isclose) provides a way to test for approximate
equality. (Contributed by Chris Barker and Tal Einat in 

[bpo-24270](https://bugs.python.org/issue?@action=redirect&bpo=24270).)

A new [ gcd()](../library/math.html#math.gcd) function has been added.  The 

`fractions.gcd()`
function is now deprecated. (Contributed by Mark Dickinson and Serhiy
Storchaka in [bpo-22486](https://bugs.python.org/issue?@action=redirect&bpo=22486).)

### multiprocessing[¶](#multiprocessing)

[ sharedctypes.synchronized()](../library/multiprocessing.html#multiprocessing.sharedctypes.synchronized)
objects now support the 

[context manager](../glossary.html#term-context-manager)protocol. (Contributed by Charles-François Natali in

[bpo-21565](https://bugs.python.org/issue?@action=redirect&bpo=21565).)

### operator[¶](#operator)

[ attrgetter()](../library/operator.html#operator.attrgetter), 

[, and](../library/operator.html#operator.itemgetter)

`itemgetter()`[objects now support pickling. (Contributed by Josh Rosenberg and Serhiy Storchaka in](../library/operator.html#operator.methodcaller)

`methodcaller()`[bpo-22955](https://bugs.python.org/issue?@action=redirect&bpo=22955).)

New [ matmul()](../library/operator.html#operator.matmul) and 

[functions to perform matrix multiplication. (Contributed by Benjamin Peterson in](../library/operator.html#operator.imatmul)

`imatmul()`[bpo-21176](https://bugs.python.org/issue?@action=redirect&bpo=21176).)

### os[¶](#os)

The new [ scandir()](../library/os.html#os.scandir) function returning an iterator of

[objects has been added. If possible,](../library/os.html#os.DirEntry)

`DirEntry``scandir()`
extracts file attributes while scanning a directory, removing the need to
perform subsequent system calls to determine file type or attributes, which may
significantly improve performance.  (Contributed by Ben Hoyt with the help
of Victor Stinner in [bpo-22524](https://bugs.python.org/issue?@action=redirect&bpo=22524).)

On Windows, a new
[ stat_result.st_file_attributes](../library/os.html#os.stat_result.st_file_attributes)
attribute is now available.  It corresponds to the 

`dwFileAttributes` member
of the `BY_HANDLE_FILE_INFORMATION` structure returned by
`GetFileInformationByHandle()`.  (Contributed by Ben Hoyt in [bpo-21719](https://bugs.python.org/issue?@action=redirect&bpo=21719).)

The [ urandom()](../library/os.html#os.urandom) function now uses the 

`getrandom()` syscall on Linux 3.17
or newer, and `getentropy()` on OpenBSD 5.6 and newer, removing the need to
use `/dev/urandom` and avoiding failures due to potential file descriptor
exhaustion.  (Contributed by Victor Stinner in [bpo-22181](https://bugs.python.org/issue?@action=redirect&bpo=22181).)

New [ get_blocking()](../library/os.html#os.get_blocking) and 

[functions allow getting and setting a file descriptor’s blocking mode (](../library/os.html#os.set_blocking)

`set_blocking()`[.) (Contributed by Victor Stinner in](../library/os.html#os.O_NONBLOCK)

`O_NONBLOCK`[bpo-22054](https://bugs.python.org/issue?@action=redirect&bpo=22054).)

The [ truncate()](../library/os.html#os.truncate) and 

[functions are now supported on Windows. (Contributed by Steve Dower in](../library/os.html#os.ftruncate)

`ftruncate()`[bpo-23668](https://bugs.python.org/issue?@action=redirect&bpo=23668).)

There is a new [ os.path.commonpath()](../library/os.path.html#os.path.commonpath) function returning the longest
common sub-path of each passed pathname.  Unlike the

[function, it always returns a valid path:](../library/os.path.html#os.path.commonprefix)

`os.path.commonprefix()````
>>> os.path.commonprefix(['/usr/lib', '/usr/local/lib'])
'/usr/l'
>>> os.path.commonpath(['/usr/lib', '/usr/local/lib'])
'/usr'
```
(Contributed by Rafik Draoui and Serhiy Storchaka in [bpo-10395](https://bugs.python.org/issue?@action=redirect&bpo=10395).)

### pathlib[¶](#pathlib)

The new [ Path.samefile()](../library/pathlib.html#pathlib.Path.samefile) method can be used
to check whether the path points to the same file as another path, which can
be either another 

[object, or a string:](../library/pathlib.html#pathlib.Path)

`Path````
>>> import pathlib
>>> p1 = pathlib.Path('/etc/hosts')
>>> p2 = pathlib.Path('/etc/../etc/hosts')
>>> p1.samefile(p2)
True
```
(Contributed by Vajrasky Kok and Antoine Pitrou in [bpo-19775](https://bugs.python.org/issue?@action=redirect&bpo=19775).)

The [ Path.mkdir()](../library/pathlib.html#pathlib.Path.mkdir) method now accepts a new optional

*exist_ok*argument to match

`mkdir -p` and [functionality. (Contributed by Berker Peksag in](../library/os.html#os.makedirs)

`os.makedirs()`[bpo-21539](https://bugs.python.org/issue?@action=redirect&bpo=21539).)

There is a new [ Path.expanduser()](../library/pathlib.html#pathlib.Path.expanduser) method to
expand 

`~` and `~user` prefixes.  (Contributed by Serhiy Storchaka and
Claudiu Popa in [bpo-19776](https://bugs.python.org/issue?@action=redirect&bpo=19776).)

A new [ Path.home()](../library/pathlib.html#pathlib.Path.home) class method can be used to get
a 

[instance representing the user’s home directory. (Contributed by Victor Salgado and Mayank Tripathi in](../library/pathlib.html#pathlib.Path)

`Path`[bpo-19777](https://bugs.python.org/issue?@action=redirect&bpo=19777).)

New [ Path.write_text()](../library/pathlib.html#pathlib.Path.write_text),

[,](../library/pathlib.html#pathlib.Path.read_text)

`Path.read_text()`[,](../library/pathlib.html#pathlib.Path.write_bytes)

`Path.write_bytes()`[methods to simplify read/write operations on files.](../library/pathlib.html#pathlib.Path.read_bytes)

`Path.read_bytes()`The following code snippet will create or rewrite existing file
`~/spam42`:

```
>>> import pathlib
>>> p = pathlib.Path('~/spam42')
>>> p.expanduser().write_text('ham')
3
```
(Contributed by Christopher Welborn in [bpo-20218](https://bugs.python.org/issue?@action=redirect&bpo=20218).)

### pickle[¶](#pickle)

Nested objects, such as unbound methods or nested classes, can now be pickled
using [pickle protocols](../library/pickle.html#pickle-protocols) older than protocol version 4.
Protocol version 4 already supports these cases.  (Contributed by Serhiy
Storchaka in [bpo-23611](https://bugs.python.org/issue?@action=redirect&bpo=23611).)

### poplib[¶](#poplib)

A new [ POP3.utf8()](../library/poplib.html#poplib.POP3.utf8) command enables 

[(Internationalized Email) support, if a POP server supports it. (Contributed by Milan OberKirch in](https://datatracker.ietf.org/doc/html/rfc6856.html)

**RFC 6856**[bpo-21804](https://bugs.python.org/issue?@action=redirect&bpo=21804).)

### re[¶](#re)

References and conditional references to groups with fixed length are now allowed in lookbehind assertions:

```
>>> import re
>>> pat = re.compile(r'(a|b).(?<=\1)c')
>>> pat.match('aac')
<_sre.SRE_Match object; span=(0, 3), match='aac'>
>>> pat.match('bbc')
<_sre.SRE_Match object; span=(0, 3), match='bbc'>
```
(Contributed by Serhiy Storchaka in [bpo-9179](https://bugs.python.org/issue?@action=redirect&bpo=9179).)

The number of capturing groups in regular expressions is no longer limited to
100.  (Contributed by Serhiy Storchaka in [bpo-22437](https://bugs.python.org/issue?@action=redirect&bpo=22437).)

The [ sub()](../library/re.html#re.sub) and 

[functions now replace unmatched groups with empty strings instead of raising an exception. (Contributed by Serhiy Storchaka in](../library/re.html#re.subn)

`subn()`[bpo-1519638](https://bugs.python.org/issue?@action=redirect&bpo=1519638).)

The [ re.error](../library/re.html#re.PatternError) exceptions have new attributes,

[,](../library/re.html#re.PatternError.msg)

`msg`[,](../library/re.html#re.PatternError.pattern)

`pattern`[,](../library/re.html#re.PatternError.pos)

`pos`[, and](../library/re.html#re.PatternError.lineno)

`lineno`[, that provide better context information about the error:](../library/re.html#re.PatternError.colno)

`colno````
>>> re.compile("""
...     (?x)
...     .++
... """)
Traceback (most recent call last):
   ...
sre_constants.error: multiple repeat at position 16 (line 3, column 7)
```
(Contributed by Serhiy Storchaka in [bpo-22578](https://bugs.python.org/issue?@action=redirect&bpo=22578).)

### readline[¶](#readline)

A new [ append_history_file()](../library/readline.html#readline.append_history_file) function can be used to append
the specified number of trailing elements in history to the given file.
(Contributed by Bruno Cauet in 

[bpo-22940](https://bugs.python.org/issue?@action=redirect&bpo=22940).)

### selectors[¶](#selectors)

The new [ DevpollSelector](../library/selectors.html#selectors.DevpollSelector) supports efficient

`/dev/poll` polling on Solaris.
(Contributed by Giampaolo Rodola’ in [bpo-18931](https://bugs.python.org/issue?@action=redirect&bpo=18931).)

### shutil[¶](#shutil)

The [ move()](../library/shutil.html#shutil.move) function now accepts a 

*copy_function*argument, allowing, for example, the

[function to be used instead of the default](../library/shutil.html#shutil.copy)

`copy()`[if there is a need to ignore file metadata when moving. (Contributed by Claudiu Popa in](../library/shutil.html#shutil.copy2)

`copy2()`[bpo-19840](https://bugs.python.org/issue?@action=redirect&bpo=19840).)

The [ make_archive()](../library/shutil.html#shutil.make_archive) function now supports the 

*xztar*format. (Contributed by Serhiy Storchaka in

[bpo-5411](https://bugs.python.org/issue?@action=redirect&bpo=5411).)

### signal[¶](#signal)

On Windows, the [ set_wakeup_fd()](../library/signal.html#signal.set_wakeup_fd) function now also supports
socket handles.  (Contributed by Victor Stinner in 

[bpo-22018](https://bugs.python.org/issue?@action=redirect&bpo=22018).)

Various `SIG*` constants in the [ signal](../library/signal.html#module-signal) module have been converted into

[. This allows meaningful names to be printed during debugging, instead of integer “magic numbers”. (Contributed by Giampaolo Rodola’ in](../library/enum.html#module-enum)

`Enums`[bpo-21076](https://bugs.python.org/issue?@action=redirect&bpo=21076).)

### smtpd[¶](#smtpd)

Both the `SMTPServer` and `SMTPChannel` classes now
accept a *decode_data* keyword argument to determine if the `DATA` portion of
the SMTP transaction is decoded using the `"utf-8"` codec or is instead
provided to the
`SMTPServer.process_message()`
method as a byte string.  The default is `True` for backward compatibility
reasons, but will change to `False` in Python 3.6.  If *decode_data* is set
to `False`, the `process_message` method must be prepared to accept keyword
arguments.
(Contributed by Maciej Szulik in [bpo-19662](https://bugs.python.org/issue?@action=redirect&bpo=19662).)

The `SMTPServer` class now advertises the `8BITMIME` extension
([ RFC 6152](https://datatracker.ietf.org/doc/html/rfc6152.html)) if 

*decode_data*has been set

`True`.  If the client
specifies `BODY=8BITMIME` on the `MAIL` command, it is passed to
`SMTPServer.process_message()`
via the *mail_options*keyword. (Contributed by Milan Oberkirch and R. David Murray in

[bpo-21795](https://bugs.python.org/issue?@action=redirect&bpo=21795).)

The `SMTPServer` class now also supports the `SMTPUTF8`
extension ([ RFC 6531](https://datatracker.ietf.org/doc/html/rfc6531.html): Internationalized Email).  If the client specified

`SMTPUTF8 BODY=8BITMIME` on the `MAIL` command, they are passed to
`SMTPServer.process_message()`
via the *mail_options*keyword. It is the responsibility of the

`process_message` method to correctly handle the `SMTPUTF8` data.
(Contributed by Milan Oberkirch in [bpo-21725](https://bugs.python.org/issue?@action=redirect&bpo=21725).)

It is now possible to provide, directly or via name resolution, IPv6
addresses in the `SMTPServer` constructor, and have it
successfully connect.  (Contributed by Milan Oberkirch in [bpo-14758](https://bugs.python.org/issue?@action=redirect&bpo=14758).)

### smtplib[¶](#smtplib)

A new [ SMTP.auth()](../library/smtplib.html#smtplib.SMTP.auth) method provides a convenient way to
implement custom authentication mechanisms. (Contributed by Milan
Oberkirch in 

[bpo-15014](https://bugs.python.org/issue?@action=redirect&bpo=15014).)

The [ SMTP.set_debuglevel()](../library/smtplib.html#smtplib.SMTP.set_debuglevel) method now
accepts an additional debuglevel (2), which enables timestamps in debug
messages. (Contributed by Gavin Chappell and Maciej Szulik in 

[bpo-16914](https://bugs.python.org/issue?@action=redirect&bpo=16914).)

Both the [ SMTP.sendmail()](../library/smtplib.html#smtplib.SMTP.sendmail) and

[methods now support](../library/smtplib.html#smtplib.SMTP.send_message)

`SMTP.send_message()`[(SMTPUTF8). (Contributed by Milan Oberkirch and R. David Murray in](https://datatracker.ietf.org/doc/html/rfc6531.html)

**RFC 6531**[bpo-22027](https://bugs.python.org/issue?@action=redirect&bpo=22027).)

### sndhdr[¶](#sndhdr)

The `what()` and `whathdr()` functions  now return
a [ namedtuple()](../library/collections.html#collections.namedtuple).  (Contributed by Claudiu Popa in

[bpo-18615](https://bugs.python.org/issue?@action=redirect&bpo=18615).)

### socket[¶](#socket)

Functions with timeouts now use a monotonic clock, instead of a system clock.
(Contributed by Victor Stinner in [bpo-22043](https://bugs.python.org/issue?@action=redirect&bpo=22043).)

A new [ socket.sendfile()](../library/socket.html#socket.socket.sendfile) method allows
sending a file over a socket by using the high-performance 

[function on UNIX, resulting in uploads being from 2 to 3 times faster than when using plain](../library/os.html#os.sendfile)

`os.sendfile()`[. (Contributed by Giampaolo Rodola’ in](../library/socket.html#socket.socket.send)

`socket.send()`[bpo-17552](https://bugs.python.org/issue?@action=redirect&bpo=17552).)

The [ socket.sendall()](../library/socket.html#socket.socket.sendall) method no longer resets the
socket timeout every time bytes are received or sent.  The socket timeout is
now the maximum total duration to send all data.
(Contributed by Victor Stinner in 

[bpo-23853](https://bugs.python.org/issue?@action=redirect&bpo=23853).)

The *backlog* argument of the [ socket.listen()](../library/socket.html#socket.socket.listen)
method is now optional.  By default it is set to

[or to](../library/socket.html#socket.SOMAXCONN)

`SOMAXCONN``128`, whichever is less.
(Contributed by Charles-François Natali in [bpo-21455](https://bugs.python.org/issue?@action=redirect&bpo=21455).)

### ssl[¶](#ssl)

#### Memory BIO Support[¶](#memory-bio-support)

(Contributed by Geert Jansen in [bpo-21965](https://bugs.python.org/issue?@action=redirect&bpo=21965).)

The new [ SSLObject](../library/ssl.html#ssl.SSLObject) class has been added to provide SSL protocol
support for cases when the network I/O capabilities of 

[are not necessary or are suboptimal.](../library/ssl.html#ssl.SSLSocket)

`SSLSocket``SSLObject` represents
an SSL protocol instance, but does not implement any network I/O methods, and
instead provides a memory buffer interface.  The new [class can be used to pass data between Python and an SSL protocol instance.](../library/ssl.html#ssl.MemoryBIO)

`MemoryBIO`The memory BIO SSL support is primarily intended to be used in frameworks
implementing asynchronous I/O for which [ SSLSocket](../library/ssl.html#ssl.SSLSocket)’s readiness
model (“select/poll”) is inefficient.

A new [ SSLContext.wrap_bio()](../library/ssl.html#ssl.SSLContext.wrap_bio) method can be used
to create a new 

`SSLObject` instance.#### Application-Layer Protocol Negotiation Support[¶](#application-layer-protocol-negotiation-support)

(Contributed by Benjamin Peterson in [bpo-20188](https://bugs.python.org/issue?@action=redirect&bpo=20188).)

Where OpenSSL support is present, the [ ssl](../library/ssl.html#module-ssl) module now implements
the 

*Application-Layer Protocol Negotiation*TLS extension as described in

[.](https://datatracker.ietf.org/doc/html/rfc7301.html)

**RFC 7301**The new [ SSLContext.set_alpn_protocols()](../library/ssl.html#ssl.SSLContext.set_alpn_protocols)
can be used to specify which protocols a socket should advertise during
the TLS handshake.

The new
[ SSLSocket.selected_alpn_protocol()](../library/ssl.html#ssl.SSLSocket.selected_alpn_protocol)
returns the protocol that was selected during the TLS handshake.
The 

[flag indicates whether ALPN support is present.](../library/ssl.html#ssl.HAS_ALPN)

`HAS_ALPN`#### Other Changes[¶](#other-changes)

There is a new [ SSLSocket.version()](../library/ssl.html#ssl.SSLSocket.version) method to
query the actual protocol version in use.
(Contributed by Antoine Pitrou in 

[bpo-20421](https://bugs.python.org/issue?@action=redirect&bpo=20421).)

The [ SSLSocket](../library/ssl.html#ssl.SSLSocket) class now implements
a 

`SSLSocket.sendfile()` method.
(Contributed by Giampaolo Rodola’ in [bpo-17552](https://bugs.python.org/issue?@action=redirect&bpo=17552).)

The `SSLSocket.send()` method now raises either
the [ ssl.SSLWantReadError](../library/ssl.html#ssl.SSLWantReadError) or 

[exception on a non-blocking socket if the operation would block. Previously, it would return](../library/ssl.html#ssl.SSLWantWriteError)

`ssl.SSLWantWriteError``0`.  (Contributed by Nikolaus Rath in [bpo-20951](https://bugs.python.org/issue?@action=redirect&bpo=20951).)

The [ cert_time_to_seconds()](../library/ssl.html#ssl.cert_time_to_seconds) function now interprets the input time
as UTC and not as local time, per 

[. Additionally, the return value is always an](https://datatracker.ietf.org/doc/html/rfc5280.html)

**RFC 5280**[. (Contributed by Akira Li in](../library/functions.html#int)

`int`[bpo-19940](https://bugs.python.org/issue?@action=redirect&bpo=19940).)

New `SSLObject.shared_ciphers()` and
[ SSLSocket.shared_ciphers()](../library/ssl.html#ssl.SSLSocket.shared_ciphers) methods return
the list of ciphers sent by the client during the handshake.
(Contributed by Benjamin Peterson in 

[bpo-23186](https://bugs.python.org/issue?@action=redirect&bpo=23186).)

The [ SSLSocket.do_handshake()](../library/ssl.html#ssl.SSLSocket.do_handshake),

[,](../library/ssl.html#ssl.SSLSocket.read)

`SSLSocket.read()``SSLSocket.shutdown()`, and
[methods of the](../library/ssl.html#ssl.SSLSocket.write)

`SSLSocket.write()`[class no longer reset the socket timeout every time bytes are received or sent. The socket timeout is now the maximum total duration of the method. (Contributed by Victor Stinner in](../library/ssl.html#ssl.SSLSocket)

`SSLSocket`[bpo-23853](https://bugs.python.org/issue?@action=redirect&bpo=23853).)

The `match_hostname()` function now supports matching of IP addresses.
(Contributed by Antoine Pitrou in [bpo-23239](https://bugs.python.org/issue?@action=redirect&bpo=23239).)

### sqlite3[¶](#sqlite3)

The [ Row](../library/sqlite3.html#sqlite3.Row) class now fully supports the sequence protocol,
in particular 

[iteration and slice indexing. (Contributed by Claudiu Popa in](../library/functions.html#reversed)

`reversed()`[bpo-10203](https://bugs.python.org/issue?@action=redirect&bpo=10203); by Lucas Sinclair, Jessica McKellar, and Serhiy Storchaka in

[bpo-13583](https://bugs.python.org/issue?@action=redirect&bpo=13583).)

### subprocess[¶](#subprocess)

The new [ run()](../library/subprocess.html#subprocess.run) function has been added.
It runs the specified command and returns a

[object, which describes a finished process. The new API is more consistent and is the recommended approach to invoking subprocesses in Python code that does not need to maintain compatibility with earlier Python versions. (Contributed by Thomas Kluyver in](../library/subprocess.html#subprocess.CompletedProcess)

`CompletedProcess`[bpo-23342](https://bugs.python.org/issue?@action=redirect&bpo=23342).)

Examples:

```
>>> subprocess.run(["ls", "-l"])  # doesn't capture output
CompletedProcess(args=['ls', '-l'], returncode=0)
>>> subprocess.run("exit 1", shell=True, check=True)
Traceback (most recent call last):
  ...
subprocess.CalledProcessError: Command 'exit 1' returned non-zero exit status 1
>>> subprocess.run(["ls", "-l", "/dev/null"], stdout=subprocess.PIPE)
CompletedProcess(args=['ls', '-l', '/dev/null'], returncode=0,
stdout=b'crw-rw-rw- 1 root root 1, 3 Jan 23 16:23 /dev/null\n')
```
### sys[¶](#sys)

A new `set_coroutine_wrapper()` function allows setting a global
hook that will be called whenever a [coroutine object](../glossary.html#term-coroutine)
is created by an [ async def](../reference/compound_stmts.html#async-def) function.  A corresponding

`get_coroutine_wrapper()` can be used to obtain a currently set
wrapper.  Both functions are [provisional](../glossary.html#term-provisional-API), and are intended for debugging purposes only. (Contributed by Yury Selivanov in

[bpo-24017](https://bugs.python.org/issue?@action=redirect&bpo=24017).)

A new [ is_finalizing()](../library/sys.html#sys.is_finalizing) function can be used to check if the Python
interpreter is 

[shutting down](../glossary.html#term-interpreter-shutdown). (Contributed by Antoine Pitrou in

[bpo-22696](https://bugs.python.org/issue?@action=redirect&bpo=22696).)

### sysconfig[¶](#sysconfig)

The name of the user scripts directory on Windows now includes the first
two components of the Python version. (Contributed by Paul Moore
in [bpo-23437](https://bugs.python.org/issue?@action=redirect&bpo=23437).)

### tarfile[¶](#tarfile)

The *mode* argument of the [ open()](../library/tarfile.html#tarfile.open) function now accepts 

`"x"`
to request exclusive creation.  (Contributed by Berker Peksag in [bpo-21717](https://bugs.python.org/issue?@action=redirect&bpo=21717).)

The [ TarFile.extractall()](../library/tarfile.html#tarfile.TarFile.extractall) and

[methods now take a keyword argument](../library/tarfile.html#tarfile.TarFile.extract)

`TarFile.extract()`*numeric_owner*. If set to

`True`, the extracted files and
directories will be owned by the numeric `uid` and `gid` from the tarfile.
If set to `False` (the default, and the behavior in versions prior to 3.5),
they will be owned by the named user and group in the tarfile.
(Contributed by Michael Vogt and Eric Smith in [bpo-23193](https://bugs.python.org/issue?@action=redirect&bpo=23193).)

The [ TarFile.list()](../library/tarfile.html#tarfile.TarFile.list) now accepts an optional

*members*keyword argument that can be set to a subset of the list returned by

[. (Contributed by Serhiy Storchaka in](../library/tarfile.html#tarfile.TarFile.getmembers)

`TarFile.getmembers()`[bpo-21549](https://bugs.python.org/issue?@action=redirect&bpo=21549).)

### threading[¶](#threading)

Both the [ Lock.acquire()](../library/threading.html#threading.Lock.acquire) and

[methods now use a monotonic clock for timeout management. (Contributed by Victor Stinner in](../library/threading.html#threading.RLock.acquire)

`RLock.acquire()`[bpo-22043](https://bugs.python.org/issue?@action=redirect&bpo=22043).)

### time[¶](#time)

The [ monotonic()](../library/time.html#time.monotonic) function is now always available.
(Contributed by Victor Stinner in 

[bpo-22043](https://bugs.python.org/issue?@action=redirect&bpo=22043).)

### timeit[¶](#timeit)

A new command line option `-u` or `--unit=` can be used to specify the time
unit for the timer output.  Supported options are *U*`usec`, `msec`,
or `sec`.  (Contributed by Julian Gindi in [bpo-18983](https://bugs.python.org/issue?@action=redirect&bpo=18983).)

The [ timeit()](../library/timeit.html#timeit.timeit) function has a new 

*globals*parameter for specifying the namespace in which the code will be running. (Contributed by Ben Roberts in

[bpo-2527](https://bugs.python.org/issue?@action=redirect&bpo=2527).)

### tkinter[¶](#tkinter)

The `tkinter._fix` module used for setting up the Tcl/Tk environment
on Windows has been replaced by a private function in the `_tkinter`
module which makes no permanent changes to environment variables.
(Contributed by Zachary Ware in [bpo-20035](https://bugs.python.org/issue?@action=redirect&bpo=20035).)

### traceback[¶](#traceback)

New [ walk_stack()](../library/traceback.html#traceback.walk_stack) and 

[functions to conveniently traverse frame and](../library/traceback.html#traceback.walk_tb)

`walk_tb()`[traceback objects](../reference/datamodel.html#traceback-objects). (Contributed by Robert Collins in

[bpo-17911](https://bugs.python.org/issue?@action=redirect&bpo=17911).)

New lightweight classes: [ TracebackException](../library/traceback.html#traceback.TracebackException),

[, and](../library/traceback.html#traceback.StackSummary)

`StackSummary`[. (Contributed by Robert Collins in](../library/traceback.html#traceback.FrameSummary)

`FrameSummary`[bpo-17911](https://bugs.python.org/issue?@action=redirect&bpo=17911).)

Both the [ print_tb()](../library/traceback.html#traceback.print_tb) and 

[functions now support negative values for the](../library/traceback.html#traceback.print_stack)

`print_stack()`*limit*argument. (Contributed by Dmitry Kazakov in

[bpo-22619](https://bugs.python.org/issue?@action=redirect&bpo=22619).)

### types[¶](#types)

A new [ coroutine()](../library/types.html#types.coroutine) function to transform

[generator](../glossary.html#term-generator-iterator)and

[objects into](../library/collections.abc.html#collections.abc.Generator)

`generator-like`[awaitables](../glossary.html#term-awaitable). (Contributed by Yury Selivanov in

[bpo-24017](https://bugs.python.org/issue?@action=redirect&bpo=24017).)

A new type called [ CoroutineType](../library/types.html#types.CoroutineType), which is used for

[coroutine](../glossary.html#term-coroutine)objects created by

[functions. (Contributed by Yury Selivanov in](../reference/compound_stmts.html#async-def)

`async def`[bpo-24400](https://bugs.python.org/issue?@action=redirect&bpo=24400).)

### unicodedata[¶](#unicodedata)

The [ unicodedata](../library/unicodedata.html#module-unicodedata) module now uses data from 

[Unicode 8.0.0](https://unicode.org/versions/Unicode8.0.0/).

### unittest[¶](#unittest)

The [ TestLoader.loadTestsFromModule()](../library/unittest.html#unittest.TestLoader.loadTestsFromModule)
method now accepts a keyword-only argument 

*pattern*which is passed to

`load_tests` as the third argument.  Found packages are now checked for
`load_tests` regardless of whether their path matches *pattern*, because it is impossible for a package name to match the default pattern. (Contributed by Robert Collins and Barry A. Warsaw in

[bpo-16662](https://bugs.python.org/issue?@action=redirect&bpo=16662).)

Unittest discovery errors now are exposed in the
[ TestLoader.errors](../library/unittest.html#unittest.TestLoader.errors) attribute of the

[instance. (Contributed by Robert Collins in](../library/unittest.html#unittest.TestLoader)

`TestLoader`[bpo-19746](https://bugs.python.org/issue?@action=redirect&bpo=19746).)

A new command line option `--locals` to show local variables in
tracebacks.  (Contributed by Robert Collins in [bpo-22936](https://bugs.python.org/issue?@action=redirect&bpo=22936).)

### unittest.mock[¶](#unittest-mock)

The [ Mock](../library/unittest.mock.html#unittest.mock.Mock) class has the following improvements:

- The class constructor has a new - *unsafe*parameter, which causes mock objects to raise- `AttributeError`- `"assert"`. (Contributed by Kushal Das in- [bpo-21238](https://bugs.python.org/issue?@action=redirect&bpo=21238).)
- A new - `Mock.assert_not_called()`- [bpo-21262](https://bugs.python.org/issue?@action=redirect&bpo=21262).)

The [ MagicMock](../library/unittest.mock.html#unittest.mock.MagicMock) class now supports

[,](../reference/datamodel.html#object.__truediv__)

`__truediv__()`[and](../reference/datamodel.html#object.__divmod__)

`__divmod__()`[operators. (Contributed by Johannes Baiter in](../reference/datamodel.html#object.__matmul__)

`__matmul__()`[bpo-20968](https://bugs.python.org/issue?@action=redirect&bpo=20968), and Håkan Lövdahl in

[bpo-23581](https://bugs.python.org/issue?@action=redirect&bpo=23581)and

[bpo-23568](https://bugs.python.org/issue?@action=redirect&bpo=23568).)

It is no longer necessary to explicitly pass `create=True` to the
[ patch()](../library/unittest.mock.html#unittest.mock.patch) function when patching builtin names.
(Contributed by Kushal Das in 

[bpo-17660](https://bugs.python.org/issue?@action=redirect&bpo=17660).)

### urllib[¶](#urllib)

A new
[ request.HTTPPasswordMgrWithPriorAuth](../library/urllib.request.html#urllib.request.HTTPPasswordMgrWithPriorAuth)
class allows HTTP Basic Authentication credentials to be managed so as to
eliminate unnecessary 

`401` response handling, or to unconditionally send
credentials on the first request in order to communicate with servers that
return a `404` response instead of a `401` if the `Authorization` header
is not sent. (Contributed by Matej Cepl in [bpo-19494](https://bugs.python.org/issue?@action=redirect&bpo=19494)and Akshit Khurana in

[bpo-7159](https://bugs.python.org/issue?@action=redirect&bpo=7159).)

A new *quote_via* argument for the
[ parse.urlencode()](../library/urllib.parse.html#urllib.parse.urlencode)
function provides a way to control the encoding of query parts if needed.
(Contributed by Samwyse and Arnon Yaari in 

[bpo-13866](https://bugs.python.org/issue?@action=redirect&bpo=13866).)

The [ request.urlopen()](../library/urllib.request.html#urllib.request.urlopen) function accepts an

[object as a](../library/ssl.html#ssl.SSLContext)

`ssl.SSLContext`*context*argument, which will be used for the HTTPS connection. (Contributed by Alex Gaynor in

[bpo-22366](https://bugs.python.org/issue?@action=redirect&bpo=22366).)

The [ parse.urljoin()](../library/urllib.parse.html#urllib.parse.urljoin) was updated to use the

[semantics for the resolution of relative URLs, rather than](https://datatracker.ietf.org/doc/html/rfc3986.html)

**RFC 3986**[and](https://datatracker.ietf.org/doc/html/rfc1808.html)

**RFC 1808**[. (Contributed by Demian Brecht and Senthil Kumaran in](https://datatracker.ietf.org/doc/html/rfc2396.html)

**RFC 2396**[bpo-22118](https://bugs.python.org/issue?@action=redirect&bpo=22118).)

### wsgiref[¶](#wsgiref)

The *headers* argument of the [ headers.Headers](../library/wsgiref.html#wsgiref.headers.Headers)
class constructor is now optional.
(Contributed by Pablo Torres Navarrete and SilentGhost in 

[bpo-5800](https://bugs.python.org/issue?@action=redirect&bpo=5800).)

### xmlrpc[¶](#xmlrpc)

The [ client.ServerProxy](../library/xmlrpc.client.html#xmlrpc.client.ServerProxy) class now supports
the 

[context manager](../glossary.html#term-context-manager)protocol. (Contributed by Claudiu Popa in

[bpo-20627](https://bugs.python.org/issue?@action=redirect&bpo=20627).)

The [ client.ServerProxy](../library/xmlrpc.client.html#xmlrpc.client.ServerProxy) constructor now accepts
an optional 

[instance. (Contributed by Alex Gaynor in](../library/ssl.html#ssl.SSLContext)

`ssl.SSLContext`[bpo-22960](https://bugs.python.org/issue?@action=redirect&bpo=22960).)

### xml.sax[¶](#xml-sax)

SAX parsers now support a character stream of the
[ xmlreader.InputSource](../library/xml.sax.reader.html#xml.sax.xmlreader.InputSource) object.
(Contributed by Serhiy Storchaka in 

[bpo-2175](https://bugs.python.org/issue?@action=redirect&bpo=2175).)

[ parseString()](../library/xml.sax.html#xml.sax.parseString) now accepts a 

[instance. (Contributed by Serhiy Storchaka in](../library/stdtypes.html#str)

`str`[bpo-10590](https://bugs.python.org/issue?@action=redirect&bpo=10590).)

### zipfile[¶](#zipfile)

ZIP output can now be written to unseekable streams.
(Contributed by Serhiy Storchaka in [bpo-23252](https://bugs.python.org/issue?@action=redirect&bpo=23252).)

The *mode* argument of [ ZipFile.open()](../library/zipfile.html#zipfile.ZipFile.open) method now
accepts 

`"x"` to request exclusive creation.
(Contributed by Serhiy Storchaka in [bpo-21717](https://bugs.python.org/issue?@action=redirect&bpo=21717).)

## Other module-level changes[¶](#other-module-level-changes)

Many functions in the [ mmap](../library/mmap.html#module-mmap), 

`ossaudiodev`, [,](../library/socket.html#module-socket)

`socket`[, and](../library/ssl.html#module-ssl)

`ssl`[modules now accept writable](../library/codecs.html#module-codecs)

`codecs`[bytes-like objects](../glossary.html#term-bytes-like-object). (Contributed by Serhiy Storchaka in

[bpo-23001](https://bugs.python.org/issue?@action=redirect&bpo=23001).)

## Optimizations[¶](#optimizations)

The [ os.walk()](../library/os.html#os.walk) function has been sped up by 3 to 5 times on POSIX systems,
and by 7 to 20 times on Windows.  This was done using the new 

[function, which exposes file information from the underlying](../library/os.html#os.scandir)

`os.scandir()``readdir` or
`FindFirstFile`/`FindNextFile` system calls.  (Contributed by
Ben Hoyt with help from Victor Stinner in [bpo-23605](https://bugs.python.org/issue?@action=redirect&bpo=23605).)

Construction of `bytes(int)` (filled by zero bytes) is faster and uses less
memory for large objects. `calloc()` is used instead of `malloc()` to
allocate memory for these objects.
(Contributed by Victor Stinner in [bpo-21233](https://bugs.python.org/issue?@action=redirect&bpo=21233).)

Some operations on `ipaddress`[ IPv4Network](../library/ipaddress.html#ipaddress.IPv4Network) and

[have been massively sped up, such as](../library/ipaddress.html#ipaddress.IPv6Network)

`IPv6Network`[,](../library/ipaddress.html#ipaddress.IPv4Network.subnets)

`subnets()`[,](../library/ipaddress.html#ipaddress.IPv4Network.supernet)

`supernet()`[,](../library/ipaddress.html#ipaddress.summarize_address_range)

`summarize_address_range()`[. The speed up can range from 3 to 15 times. (Contributed by Antoine Pitrou, Michel Albert, and Markus in](../library/ipaddress.html#ipaddress.collapse_addresses)

`collapse_addresses()`[bpo-21486](https://bugs.python.org/issue?@action=redirect&bpo=21486),

[bpo-21487](https://bugs.python.org/issue?@action=redirect&bpo=21487),

[bpo-20826](https://bugs.python.org/issue?@action=redirect&bpo=20826),

[bpo-23266](https://bugs.python.org/issue?@action=redirect&bpo=23266).)

Pickling of [ ipaddress](../library/ipaddress.html#module-ipaddress) objects was optimized to produce significantly
smaller output.  (Contributed by Serhiy Storchaka in 

[bpo-23133](https://bugs.python.org/issue?@action=redirect&bpo=23133).)

Many operations on [ io.BytesIO](../library/io.html#io.BytesIO) are now 50% to 100% faster.
(Contributed by Serhiy Storchaka in 

[bpo-15381](https://bugs.python.org/issue?@action=redirect&bpo=15381)and David Wilson in

[bpo-22003](https://bugs.python.org/issue?@action=redirect&bpo=22003).)

The [ marshal.dumps()](../library/marshal.html#marshal.dumps) function is now faster: 65–85% with versions 3
and 4, 20–25% with versions 0 to 2 on typical data, and up to 5 times in
best cases.
(Contributed by Serhiy Storchaka in 

[bpo-20416](https://bugs.python.org/issue?@action=redirect&bpo=20416)and

[bpo-23344](https://bugs.python.org/issue?@action=redirect&bpo=23344).)

The UTF-32 encoder is now 3 to 7 times faster.
(Contributed by Serhiy Storchaka in [bpo-15027](https://bugs.python.org/issue?@action=redirect&bpo=15027).)

Regular expressions are now parsed up to 10% faster.
(Contributed by Serhiy Storchaka in [bpo-19380](https://bugs.python.org/issue?@action=redirect&bpo=19380).)

The [ json.dumps()](../library/json.html#json.dumps) function was optimized to run with

`ensure_ascii=False` as fast as with `ensure_ascii=True`.
(Contributed by Naoki Inada in [bpo-23206](https://bugs.python.org/issue?@action=redirect&bpo=23206).)

The [ PyObject_IsInstance()](../c-api/object.html#c.PyObject_IsInstance) and 

[functions have been sped up in the common case that the second argument has](../c-api/object.html#c.PyObject_IsSubclass)

`PyObject_IsSubclass()`[as its metaclass. (Contributed Georg Brandl by in](../library/functions.html#type)

`type`[bpo-22540](https://bugs.python.org/issue?@action=redirect&bpo=22540).)

Method caching was slightly improved, yielding up to 5% performance
improvement in some benchmarks.
(Contributed by Antoine Pitrou in [bpo-22847](https://bugs.python.org/issue?@action=redirect&bpo=22847).)

Objects from the [ random](../library/random.html#module-random) module now use 50% less memory on 64-bit
builds.  (Contributed by Serhiy Storchaka in 

[bpo-23488](https://bugs.python.org/issue?@action=redirect&bpo=23488).)

The [ property()](../library/functions.html#property) getter calls are up to 25% faster.
(Contributed by Joe Jevnik in 

[bpo-23910](https://bugs.python.org/issue?@action=redirect&bpo=23910).)

Instantiation of [ fractions.Fraction](../library/fractions.html#fractions.Fraction) is now up to 30% faster.
(Contributed by Stefan Behnel in 

[bpo-22464](https://bugs.python.org/issue?@action=redirect&bpo=22464).)

String methods [ find()](../library/stdtypes.html#str.find), 

[,](../library/stdtypes.html#str.rfind)

`rfind()`[,](../library/stdtypes.html#str.split)

`split()`[and the](../library/stdtypes.html#str.partition)

`partition()`[string operator are now significantly faster for searching 1-character substrings. (Contributed by Serhiy Storchaka in](../reference/expressions.html#in)

`in`[bpo-23573](https://bugs.python.org/issue?@action=redirect&bpo=23573).)

## Build and C API Changes[¶](#build-and-c-api-changes)

New `calloc` functions were added:

(Contributed by Victor Stinner in [bpo-21233](https://bugs.python.org/issue?@action=redirect&bpo=21233).)

New encoding/decoding helper functions:

- `Py_DecodeLocale()`- `_Py_char2wchar()`),
- `Py_EncodeLocale()`- `_Py_wchar2char()`).

(Contributed by Victor Stinner in [bpo-18395](https://bugs.python.org/issue?@action=redirect&bpo=18395).)

A new [ PyCodec_NameReplaceErrors()](../c-api/codec.html#c.PyCodec_NameReplaceErrors) function to replace the unicode
encode error with 

`\N{...}` escapes.
(Contributed by Serhiy Storchaka in [bpo-19676](https://bugs.python.org/issue?@action=redirect&bpo=19676).)

A new [ PyErr_FormatV()](../c-api/exceptions.html#c.PyErr_FormatV) function similar to 

[, but accepts a](../c-api/exceptions.html#c.PyErr_Format)

`PyErr_Format()``va_list` argument.
(Contributed by Antoine Pitrou in [bpo-18711](https://bugs.python.org/issue?@action=redirect&bpo=18711).)

A new [ PyExc_RecursionError](../c-api/exceptions.html#c.PyExc_RecursionError) exception.
(Contributed by Georg Brandl in 

[bpo-19235](https://bugs.python.org/issue?@action=redirect&bpo=19235).)

New [ PyModule_FromDefAndSpec()](../c-api/module.html#c.PyModule_FromDefAndSpec), 

[, and](../c-api/module.html#c.PyModule_FromDefAndSpec2)

`PyModule_FromDefAndSpec2()`[functions introduced by](../c-api/module.html#c.PyModule_ExecDef)

`PyModule_ExecDef()`[– multi-phase extension module initialization. (Contributed by Petr Viktorin in](https://peps.python.org/pep-0489/)

**PEP 489**[bpo-24268](https://bugs.python.org/issue?@action=redirect&bpo=24268).)

New [ PyNumber_MatrixMultiply()](../c-api/number.html#c.PyNumber_MatrixMultiply) and

[functions to perform matrix multiplication. (Contributed by Benjamin Peterson in](../c-api/number.html#c.PyNumber_InPlaceMatrixMultiply)

`PyNumber_InPlaceMatrixMultiply()`[bpo-21176](https://bugs.python.org/issue?@action=redirect&bpo=21176). See also

[for details.)](https://peps.python.org/pep-0465/)

**PEP 465**The [ PyTypeObject.tp_finalize](../c-api/typeobj.html#c.PyTypeObject.tp_finalize) slot is now part of the stable ABI.

Windows builds now require Microsoft Visual C++ 14.0, which
is available as part of [Visual Studio 2015](https://visualstudio.microsoft.com/en/vs/older-downloads/#visual-studio-2015-and-other-products).

Extension modules now include a platform information tag in their filename on some platforms (the tag is optional, and CPython will import extensions without it, although if the tag is present and mismatched, the extension won’t be loaded):

- On Linux, extension module filenames end with - `.cpython-<major><minor>m-<architecture>-<os>.pyd`:- `<major>`is the major number of the Python version; for Python 3.5 this is- `3`.
- `<minor>`is the minor number of the Python version; for Python 3.5 this is- `5`.
- `<architecture>`is the hardware architecture the extension module was built to run on. It’s most commonly either- `i386`for 32-bit Intel platforms or- `x86_64`for 64-bit Intel (and AMD) platforms.
- `<os>`is always- `linux-gnu`, except for extensions built to talk to the 32-bit ABI on 64-bit platforms, in which case it is- `linux-gnu32`(and- `<architecture>`will be- `x86_64`).
 
- On Windows, extension module filenames end with - `<debug>.cp<major><minor>-<platform>.pyd`:- `<major>`is the major number of the Python version; for Python 3.5 this is- `3`.
- `<minor>`is the minor number of the Python version; for Python 3.5 this is- `5`.
- `<platform>`is the platform the extension module was built for, either- `win32`for Win32,- `win_amd64`for Win64,- `win_ia64`for Windows Itanium 64, and- `win_arm`for Windows on ARM.
- If built in debug mode, - `<debug>`will be- `_d`, otherwise it will be blank.
 
- On OS X platforms, extension module filenames now end with - `-darwin.so`.
- On all other platforms, extension module filenames are the same as they were with Python 3.4. 

## Deprecated[¶](#deprecated)

### New Keywords[¶](#new-keywords)

`async` and `await` are not recommended to be used as variable, class,
function or module names.  Introduced by [ PEP 492](https://peps.python.org/pep-0492/) in Python 3.5, they will
become proper keywords in Python 3.7.

### Deprecated Python Behavior[¶](#deprecated-python-behavior)

Raising the [ StopIteration](../library/exceptions.html#StopIteration) exception inside a generator will now generate a silent

[, which will become a non-silent deprecation warning in Python 3.6 and will trigger a](../library/exceptions.html#PendingDeprecationWarning)

`PendingDeprecationWarning`[in Python 3.7. See](../library/exceptions.html#RuntimeError)

`RuntimeError`[PEP 479: Change StopIteration handling inside generators](#whatsnew-pep-479)for details.

### Unsupported Operating Systems[¶](#unsupported-operating-systems)

Windows XP is no longer supported by Microsoft, thus, per [ PEP 11](https://peps.python.org/pep-0011/), CPython
3.5 is no longer officially supported on this OS.

### Deprecated Python modules, functions and methods[¶](#deprecated-python-modules-functions-and-methods)

The `formatter` module has now graduated to full deprecation and is still
slated for removal in Python 3.6.

The `asyncio.async()` function is deprecated in favor of
[ ensure_future()](../library/asyncio-future.html#asyncio.ensure_future).

The `smtpd` module has in the past always decoded the DATA portion of
email messages using the `utf-8` codec.  This can now be controlled by the
new *decode_data* keyword to `SMTPServer`.  The default value is
`True`, but this default is deprecated.  Specify the *decode_data* keyword
with an appropriate value to avoid the deprecation warning.

Directly assigning values to the [ key](../library/http.cookies.html#http.cookies.Morsel.key),

[and](../library/http.cookies.html#http.cookies.Morsel.value)

`value`[of](../library/http.cookies.html#http.cookies.Morsel.coded_value)

`coded_value`[objects is deprecated. Use the](../library/http.cookies.html#http.cookies.Morsel)

`http.cookies.Morsel`[method instead. In addition, the undocumented](../library/http.cookies.html#http.cookies.Morsel.set)

`set()`*LegalChars*parameter of

`set()` is deprecated, and is now ignored.Passing a format string as keyword argument *format_string* to the
[ format()](../library/string.html#string.Formatter.format) method of the 

[class has been deprecated. (Contributed by Serhiy Storchaka in](../library/string.html#string.Formatter)

`string.Formatter`[bpo-23671](https://bugs.python.org/issue?@action=redirect&bpo=23671).)

The `platform.dist()` and `platform.linux_distribution()` functions
are now deprecated.  Linux distributions use too many different ways of
describing themselves, so the functionality is left to a package.
(Contributed by Vajrasky Kok and Berker Peksag in [bpo-1322](https://bugs.python.org/issue?@action=redirect&bpo=1322).)

The previously undocumented `from_function` and `from_builtin` methods of
[ inspect.Signature](../library/inspect.html#inspect.Signature) are deprecated.  Use the new

[method instead. (Contributed by Yury Selivanov in](../library/inspect.html#inspect.Signature.from_callable)

`Signature.from_callable()`[bpo-24248](https://bugs.python.org/issue?@action=redirect&bpo=24248).)

The `inspect.getargspec()` function is deprecated and scheduled to be
removed in Python 3.6.  (See [bpo-20438](https://bugs.python.org/issue?@action=redirect&bpo=20438) for details.)

The `inspect`[ getfullargspec()](../library/inspect.html#inspect.getfullargspec),

[, and](../library/inspect.html#inspect.getcallargs)

`getcallargs()``formatargspec()` functions are
deprecated in favor of the [API. (Contributed by Yury Selivanov in](../library/inspect.html#inspect.signature)

`inspect.signature()`[bpo-20438](https://bugs.python.org/issue?@action=redirect&bpo=20438).)

[ getargvalues()](../library/inspect.html#inspect.getargvalues) and 

[functions were inadvertently marked as deprecated with the release of Python 3.5.0.](../library/inspect.html#inspect.formatargvalues)

`formatargvalues()`Use of [ re.LOCALE](../library/re.html#re.LOCALE) flag with str patterns or 

[is now deprecated. (Contributed by Serhiy Storchaka in](../library/re.html#re.ASCII)

`re.ASCII`[bpo-22407](https://bugs.python.org/issue?@action=redirect&bpo=22407).)

Use of unrecognized special sequences consisting of `'\'` and an ASCII letter
in regular expression patterns and replacement patterns now raises a
deprecation warning and will be forbidden in Python 3.6.
(Contributed by Serhiy Storchaka in [bpo-23622](https://bugs.python.org/issue?@action=redirect&bpo=23622).)

The undocumented and unofficial *use_load_tests* default argument of the
[ unittest.TestLoader.loadTestsFromModule()](../library/unittest.html#unittest.TestLoader.loadTestsFromModule) method now is
deprecated and ignored.
(Contributed by Robert Collins and Barry A. Warsaw in 

[bpo-16662](https://bugs.python.org/issue?@action=redirect&bpo=16662).)

## Removed[¶](#removed)

### API and Feature Removals[¶](#api-and-feature-removals)

The following obsolete and previously deprecated APIs and features have been removed:

- The - `__version__`attribute has been dropped from the email package. The email code hasn’t been shipped separately from the stdlib for a long time, and the- `__version__`string was not updated in the last few releases.
- The internal - `Netrc`class in the- `ftplib`- [bpo-6623](https://bugs.python.org/issue?@action=redirect&bpo=6623).)
- The concept of - `.pyo`files has been removed.
- The JoinableQueue class in the provisional - `asyncio`- [bpo-23464](https://bugs.python.org/issue?@action=redirect&bpo=23464).)

## Porting to Python 3.5[¶](#porting-to-python-3-5)

This section lists previously described changes and other bugfixes that may require changes to your code.

### Changes in Python behavior[¶](#changes-in-python-behavior)

- Due to an oversight, earlier Python versions erroneously accepted the following syntax: - f(1 for x in [1], *args) f(1 for x in [1], **kwargs) - Python 3.5 now correctly raises a - `SyntaxError`

### Changes in the Python API[¶](#changes-in-the-python-api)

- **PEP 475**- `InterruptedError`
- Before Python 3.5, a - `datetime.time`- [bpo-13936](https://bugs.python.org/issue?@action=redirect&bpo=13936)for full details.
- The - `ssl.SSLSocket.send()`method now raises either- `ssl.SSLWantReadError`- `ssl.SSLWantWriteError`- `0`. (Contributed by Nikolaus Rath in- [bpo-20951](https://bugs.python.org/issue?@action=redirect&bpo=20951).)
- The - `__name__`attribute of generators is now set from the function name, instead of being set from the code name. Use- `gen.gi_code.co_name`to retrieve the code name. Generators also have a new- `__qualname__`attribute, the qualified name, which is now used for the representation of a generator (- `repr(gen)`). (Contributed by Victor Stinner in- [bpo-21205](https://bugs.python.org/issue?@action=redirect&bpo=21205).)
- The deprecated “strict” mode and argument of - `HTMLParser`- `HTMLParser.error()`, and the- `HTMLParserError`exception have been removed. (Contributed by Ezio Melotti in- [bpo-15114](https://bugs.python.org/issue?@action=redirect&bpo=15114).) The- *convert_charrefs*argument of- `HTMLParser`is now- `True`by default. (Contributed by Berker Peksag in- [bpo-21047](https://bugs.python.org/issue?@action=redirect&bpo=21047).)
- Although it is not formally part of the API, it is worth noting for porting purposes (ie: fixing tests) that error messages that were previously of the form “‘sometype’ does not support the buffer protocol” are now of the form “a - [bytes-like object](../glossary.html#term-bytes-like-object)is required, not ‘sometype’”. (Contributed by Ezio Melotti in- [bpo-16518](https://bugs.python.org/issue?@action=redirect&bpo=16518).)
- If the current directory is set to a directory that no longer exists then - `FileNotFoundError`- `find_spec()`- `None`- **without**caching- `None`in- `sys.path_importer_cache`- [bpo-22834](https://bugs.python.org/issue?@action=redirect&bpo=22834)).
- HTTP status code and messages from - `http.client`- `http.server`- `HTTPStatus`- `http.client`and- `http.server`remain available for backwards compatibility. (Contributed by Demian Brecht in- [bpo-21793](https://bugs.python.org/issue?@action=redirect&bpo=21793).)
- When an import loader defines - `exec_module()`- `create_module()`- `DeprecationWarning`- `importlib.abc.Loader`- `create_module()`to return- `None`. (Contributed by Brett Cannon in- [bpo-23014](https://bugs.python.org/issue?@action=redirect&bpo=23014).)
- The - `re.split()`- `"x*"`pattern worked the same as- `"x+"`, and the- `"\b"`pattern never worked. Now- `re.split()`raises a warning if the pattern could match an empty string. For compatibility, use patterns that never match an empty string (e.g.- `"x+"`instead of- `"x*"`). Patterns that could only match an empty string (such as- `"\b"`) now raise an error. (Contributed by Serhiy Storchaka in- [bpo-22818](https://bugs.python.org/issue?@action=redirect&bpo=22818).)
- The - `http.cookies.Morsel`- `key`- `value`- `copy()`- `Morsel`instance rather than a- `dict`- `update()`- *LegalChars*parameter of- `set()`- [bpo-2211](https://bugs.python.org/issue?@action=redirect&bpo=2211).)
- **PEP 488**- `.pyo`files from Python and introduced the optional- `opt-`tag in- `.pyc`file names. The- `importlib.util.cache_from_source()`- *optimization*parameter to help control the- `opt-`tag. Because of this, the- *debug_override*parameter of the function is now deprecated.- `.pyo`files are also no longer supported as a file argument to the Python interpreter and thus serve no purpose when distributed on their own (i.e. sourceless code distribution). Due to the fact that the magic number for bytecode has changed in Python 3.5, all old- `.pyo`files from previous versions of Python are invalid regardless of this PEP.
- The - `socket`- `CAN_RAW_FD_FRAMES`
- The - `ssl.cert_time_to_seconds()`- **RFC 5280**- `int`- [bpo-19940](https://bugs.python.org/issue?@action=redirect&bpo=19940).)
- The - `pygettext.py`Tool now uses the standard +NNNN format for timezones in the POT-Creation-Date header.
- The - `smtplib`- `sys.stderr`- `stderr`variable for debug output. If your (test) program depends on patching the module-level variable to capture the debug output, you will need to update it to capture sys.stderr instead.
- The - `str.startswith()`- `str.endswith()`- `True`when finding the empty string and the indexes are completely out of range. (Contributed by Serhiy Storchaka in- [bpo-24284](https://bugs.python.org/issue?@action=redirect&bpo=24284).)
- The - `inspect.getdoc()`- `pydoc`- `help()`- [bpo-15582](https://bugs.python.org/issue?@action=redirect&bpo=15582).)
- Nested - `functools.partial()`- `functools.partial()`object or you can create a subclass of- `functools.partial()`. (Contributed by Alexander Belopolsky in- [bpo-7830](https://bugs.python.org/issue?@action=redirect&bpo=7830).)

### Changes in the C API[¶](#changes-in-the-c-api)

- The undocumented - `format`member of the (non-public)- `PyMemoryViewObject`structure has been removed. All extensions relying on the relevant parts in- `memoryobject.h`must be rebuilt.
- The - `PyMemAllocator`structure was renamed to- `PyMemAllocatorEx`- `calloc`field was added.
- Removed non-documented macro - `PyObject_REPR()`which leaked references. Use format character- `%R`in- `PyUnicode_FromFormat()`- `repr()`- [bpo-22453](https://bugs.python.org/issue?@action=redirect&bpo=22453).)
- Because the lack of the - `__module__`- `__module__`attribute. This will be an- `AttributeError`- [bpo-20204](https://bugs.python.org/issue?@action=redirect&bpo=20204).)
- As part of the - **PEP 492**- `tp_reserved`slot of- `PyTypeObject`- `tp_as_async`- [Coroutine Objects](../c-api/coro.html#coro-objects)for new types, structures and functions.

## Notable changes in Python 3.5.4[¶](#notable-changes-in-python-3-5-4)

### New `make regen-all` build target[¶](#new-make-regen-all-build-target)

To simplify cross-compilation, and to ensure that CPython can reliably be compiled without requiring an existing version of Python to already be available, the autotools-based build system no longer attempts to implicitly recompile generated files based on file modification times.

Instead, a new `make regen-all` command has been added to force regeneration
of these files when desired (e.g. after an initial version of Python has
already been built based on the pregenerated versions).

More selective regeneration targets are also defined - see
[Makefile.pre.in](https://github.com/python/cpython/tree/3.14/Makefile.pre.in) for details.

(Contributed by Victor Stinner in [bpo-23404](https://bugs.python.org/issue?@action=redirect&bpo=23404).)

Added in version 3.5.4.

### Removal of `make touch` build target[¶](#removal-of-make-touch-build-target)

The `make touch` build target previously used to request implicit regeneration
of generated files by updating their modification times has been removed.

It has been replaced by the new `make regen-all` target.

(Contributed by Victor Stinner in [bpo-23404](https://bugs.python.org/issue?@action=redirect&bpo=23404).)

Changed in version 3.5.4.