# What’s New In Python 3.0 — Python 3.14.6 documentation

**Source:** [https://docs.python.org/whatsnew/3.0.html](https://docs.python.org/whatsnew/3.0.html)

---

# What’s New In Python 3.0[¶](#what-s-new-in-python-3-0)

- Author:
- Guido van Rossum 

This article explains the new features in Python 3.0, compared to 2.6.
Python 3.0, also known as “Python 3000” or “Py3K”, is the first ever
*intentionally backwards incompatible* Python release. Python 3.0 was released on December 3, 2008.
There are more changes than in a typical release, and more that are important for all
Python users. Nevertheless, after digesting the changes, you’ll find
that Python really hasn’t changed all that much – by and large, we’re
mostly fixing well-known annoyances and warts, and removing a lot of
old cruft.

This article doesn’t attempt to provide a complete specification of all new features, but instead tries to give a convenient overview. For full details, you should refer to the documentation for Python 3.0, and/or the many PEPs referenced in the text. If you want to understand the complete implementation and design rationale for a particular feature, PEPs usually have more details than the regular documentation; but note that PEPs usually are not kept up-to-date once a feature has been fully implemented.

Due to time constraints this document is not as complete as it should
have been.  As always for a new release, the `Misc/NEWS` file in the
source distribution contains a wealth of detailed information about
every small thing that was changed.

## Common Stumbling Blocks[¶](#common-stumbling-blocks)

This section lists those few changes that are most likely to trip you up if you’re used to Python 2.5.

### Print Is A Function[¶](#print-is-a-function)

The `print` statement has been replaced with a [ print()](../library/functions.html#print)
function, with keyword arguments to replace most of the special syntax
of the old 

`print` statement ([). Examples:](https://peps.python.org/pep-3105/)

**PEP 3105**```
Old: print "The answer is", 2*2
New: print("The answer is", 2*2)
Old: print x,           # Trailing comma suppresses newline
New: print(x, end=" ")  # Appends a space instead of a newline
Old: print              # Prints a newline
New: print()            # You must call the function!
Old: print >>sys.stderr, "fatal error"
New: print("fatal error", file=sys.stderr)
Old: print (x, y)       # prints repr((x, y))
New: print((x, y))      # Not the same as print(x, y)!
```
You can also customize the separator between items, e.g.:

```
print("There are <", 2**32, "> possibilities!", sep="")
```
which produces:

```
There are <4294967296> possibilities!
```
Note:

- The - `print()`- `print`statement. For example, in Python 2.x,- `print "A\n", "B"`would write- `"A\nB\n"`; but in Python 3.0,- `print("A\n", "B")`writes- `"A\n B\n"`.
- Initially, you’ll be finding yourself typing the old - `print x`a lot in interactive mode. Time to retrain your fingers to type- `print(x)`instead!
- When using the - `2to3`source-to-source conversion tool, all- `print`statements are automatically converted to- `print()`

### Views And Iterators Instead Of Lists[¶](#views-and-iterators-instead-of-lists)

Some well-known APIs no longer return lists:

- `dict`- `dict.keys()`- `dict.items()`- `dict.values()`- `k = d.keys(); k.sort()`. Use- `k = sorted(d)`instead (this works in Python 2.5 too and is just as efficient).
- Also, the - `dict.iterkeys()`,- `dict.iteritems()`and- `dict.itervalues()`methods are no longer supported.
- `map()`- `filter()`- `map()`in- `list()`- `list(map(...))`, but a better fix is often to use a list comprehension (especially when the original code uses- `lambda`- `map()`invoked for the side effects of the function; the correct transformation is to use a regular- `for`- If the input sequences are not of equal length, - `map()`- `map()`from Python 2.x, also wrap the sequences in- `itertools.zip_longest()`- `map(func, *sequences)`becomes- `list(map(func, itertools.zip_longest(*sequences)))`.
- `range()`- `xrange()`used to behave, except it works with values of arbitrary size. The latter no longer exists.
- `zip()`

### Ordering Comparisons[¶](#ordering-comparisons)

Python 3.0 has simplified the rules for ordering comparisons:

- The ordering comparison operators ( - `<`,- `<=`,- `>=`,- `>`) raise a TypeError exception when the operands don’t have a meaningful natural ordering. Thus, expressions like- `1 < ''`,- `0 > None`or- `len <= len`are no longer valid, and e.g.- `None < None`raises- `TypeError`- `False`. A corollary is that sorting a heterogeneous list no longer makes sense – all the elements must be comparable to each other. Note that this does not apply to the- `==`and- `!=`operators: objects of different incomparable types always compare unequal to each other.
- `sorted()`- `list.sort()`- *cmp*argument providing a comparison function. Use the- *key*argument instead. N.B. the- *key*and- *reverse*arguments are now “keyword-only”.
- The - `cmp()`function should be treated as gone, and the- `__cmp__()`special method is no longer supported. Use- `__lt__()`- `__eq__()`- `__hash__()`- `cmp()`functionality, you could use the expression- `(a > b) - (a < b)`as the equivalent for- `cmp(a, b)`.)

### Integers[¶](#integers)

- **PEP 237**- `long`renamed to- `int`- `int`; but it behaves mostly like the old- `long`type.
- **PEP 238**- `1/2`returns a float. Use- `1//2`to get the truncating behavior. (The latter syntax has existed for years, at least since Python 2.2.)
- The - `sys.maxint`constant was removed, since there is no longer a limit to the value of integers. However,- `sys.maxsize`- `sys.maxint`in previous releases on the same platform (assuming the same build options).
- The - `repr()`- `L`anymore, so code that unconditionally strips that character will chop off the last digit instead. (Use- `str()`
- Octal literals are no longer of the form - `0720`; use- `0o720`instead.

### Text Vs. Data Instead Of Unicode Vs. 8-bit[¶](#text-vs-data-instead-of-unicode-vs-8-bit)

Everything you thought you knew about binary data and Unicode has changed.

- Python 3.0 uses the concepts of - *text*and (binary)- *data*instead of Unicode strings and 8-bit strings. All text is Unicode; however- *encoded*Unicode is represented as binary data. The type used to hold text is- `str`- `bytes`- `TypeError`- `UnicodeDecodeError`
- As a consequence of this change in philosophy, pretty much all code that uses Unicode, encodings or binary data most likely has to change. The change is for the better, as in the 2.x world there were numerous bugs having to do with mixing encoded and unencoded text. To be prepared in Python 2.x, start using - `unicode`for all unencoded text, and- `str`- `2to3`tool will do most of the work for you.
- You can no longer use - `u"..."`literals for Unicode text. However, you must use- `b"..."`literals for binary data.
- As the - `str`- `bytes`- `str.encode()`- `str`to- `bytes`, and- `bytes.decode()`- `bytes`to- `str`. You can also use- `bytes(s, encoding=...)`and- `str(b, encoding=...)`, respectively.
- Like - `str`- `bytes`- *mutable*type to hold buffered binary data,- `bytearray`- `bytes`also accept- `bytearray`. The mutable API is based on- `collections.MutableSequence`
- All backslashes in raw string literals are interpreted literally. This means that - `'\U'`and- `'\u'`escapes in raw strings are not treated specially. For example,- `r'\u20ac'`is a string of 6 characters in Python 3.0, whereas in 2.6,- `ur'\u20ac'`was the single “euro” character. (Of course, this change only affects raw string literals; the euro character is- `'\u20ac'`in Python 3.0.)
- The built-in - `basestring`abstract type was removed. Use- `str`- `str`and- `bytes`- `2to3`tool (see below) replaces every occurrence of- `basestring`with- `str`.
- Files opened as text files (still the default mode for - `open()`- `b`in the mode argument) always use bytes in memory. This means that if a file is opened using an incorrect mode or encoding, I/O will likely fail loudly, instead of silently producing incorrect data. It also means that even Unix users will have to specify the correct mode (text or binary) when opening a file. There is a platform-dependent default encoding, which on Unixy platforms can be set with the- `LANG`environment variable (and sometimes also with some other platform-specific locale-related environment variables). In many cases, but not all, the system default is UTF-8; you should never count on this default. Any application reading or writing more than pure ASCII text should probably have a way to override the encoding. There is no longer any need for using the encoding-aware streams in the- `codecs`
- The initial values of - `sys.stdin`- `sys.stdout`- `sys.stderr`- `io.TextIOBase`- `io.TextIOBase.buffer`
- Filenames are passed to and returned from APIs as (Unicode) strings. This can present platform-specific problems because on some platforms filenames are arbitrary byte strings. (On the other hand, on Windows filenames are natively stored as Unicode.) As a work-around, most APIs (e.g. - `open()`- `os`- `bytes`- `bytes`return value. Thus,- `os.listdir()`- `bytes`instances if the argument is a- `bytes`instance, and- `os.getcwdb()`- `bytes`instance. Note that when- `os.listdir()`returns a list of strings, filenames that cannot be decoded properly are omitted rather than raising- `UnicodeError`
- Some system APIs like - `os.environ`- `sys.argv`- `LANG`variable and rerunning the program is probably the best approach.
- **PEP 3138**- `repr()`
- **PEP 3120**
- **PEP 3131**
- The - `StringIO`and- `cStringIO`modules are gone. Instead, import the- `io`- `io.StringIO`- `io.BytesIO`
- See also the - [Unicode HOWTO](../howto/unicode.html#unicode-howto), which was updated for Python 3.0.

## Overview Of Syntax Changes[¶](#overview-of-syntax-changes)

This section gives a brief overview of every *syntactic* change in
Python 3.0.

### New Syntax[¶](#new-syntax)

- **PEP 3107**- `__annotations__`
- **PEP 3102**- `*args`in the parameter list- *must*be specified using keyword syntax in the call. You can also use a bare- `*`in the parameter list to indicate that you don’t accept a variable-length argument list, but you do have keyword-only arguments.
- Keyword arguments are allowed after the list of base classes in a class definition. This is used by the new convention for specifying a metaclass (see next section), but can be used for other purposes as well, as long as the metaclass supports it. 
- **PEP 3104**- `nonlocal`- `nonlocal x`you can now assign directly to a variable in an outer (but non-global) scope.- `nonlocal`is a new reserved word.
- **PEP 3132**- `a, b, *rest = some_sequence`. And even- `*rest, a = stuff`. The- `rest`object is always a (possibly empty) list; the right-hand side may be any iterable. Example:- (a, *rest, b) = range(5) - This sets - *a*to- `0`,- *b*to- `4`, and- *rest*to- `[1, 2, 3]`.
- Dictionary comprehensions: - `{k: v for k, v in stuff}`means the same thing as- `dict(stuff)`but is more flexible. (This is- **PEP 274**
- Set literals, e.g. - `{1, 2}`. Note that- `{}`is an empty dictionary; use- `set()`for an empty set. Set comprehensions are also supported; e.g.,- `{x for x in stuff}`means the same thing as- `set(stuff)`but is more flexible.
- New octal literals, e.g. - `0o720`(already in 2.6). The old octal literals (- `0720`) are gone.
- New binary literals, e.g. - `0b1010`(already in 2.6), and there is a new corresponding built-in function,- `bin()`
- Bytes literals are introduced with a leading - `b`or- `B`, and there is a new corresponding built-in function,- `bytes()`

### Changed Syntax[¶](#changed-syntax)

- **PEP 3109**- **PEP 3134**- `raise`- `raise [`. See below.- *expr*[from- *expr*]]
- `as`and- `with`
- `True`,- `False`, and- `None`are reserved words. (2.6 partially enforced the restrictions on- `None`already.)
- Change from - `except`- *exc*,- *var*to- `except`- *exc*- `as`- *var*. See- **PEP 3110**
- **PEP 3115**- class C: __metaclass__ = M ... - you must now use: - class C(metaclass=M): ... - The module-global - `__metaclass__`variable is no longer supported. (It was a crutch to make it easier to default to new-style classes without deriving every class from- `object`
- List comprehensions no longer support the syntactic form - `[... for`. Use- *var*in- *item1*,- *item2*, ...]- `[... for`instead. Also note that list comprehensions have different semantics: they are closer to syntactic sugar for a generator expression inside a- *var*in (- *item1*,- *item2*, ...)]- `list()`
- The - *ellipsis*(- `...`) can be used as an atomic expression anywhere. (Previously it was only allowed in slices.) Also, it- *must*now be spelled as- `...`. (Previously it could also be spelled as- `. . .`, by a mere accident of the grammar.)

### Removed Syntax[¶](#removed-syntax)

- **PEP 3113**- `def foo(a, (b, c)): ...`. Use- `def foo(a, b_c): b, c = b_c`instead.
- Removed backticks (use - `repr()`
- Removed - `<>`(use- `!=`instead).
- Removed keyword: - `exec()`- `exec()`no longer takes a stream argument; instead of- `exec(f)`you can use- `exec(f.read())`.
- Integer literals no longer support a trailing - `l`or- `L`.
- String literals no longer support a leading - `u`or- `U`.
- The - `from`- *module*- `import`- `*`syntax is only allowed at the module level, no longer inside functions.
- The only acceptable syntax for relative imports is - `from .[`. All- *module*] import- *name*- `import`- `.`are interpreted as absolute imports. (- **PEP 328**
- Classic classes are gone. 

## Changes Already Present In Python 2.6[¶](#changes-already-present-in-python-2-6)

Since many users presumably make the jump straight from Python 2.5 to
Python 3.0, this section reminds the reader of new features that were
originally designed for Python 3.0 but that were back-ported to Python
2.6.  The corresponding sections in [What’s New in Python 2.6](2.6.html#whats-new-in-2-6) should be
consulted for longer descriptions.

- [PEP 343: The ‘with’ statement](2.6.html#pep-0343). The- `with`- `__future__`- [Writing Context Managers](2.6.html#new-26-context-managers)and- [The contextlib module](2.6.html#new-module-contextlib).
- [PEP 366: Explicit Relative Imports From a Main Module](2.6.html#pep-0366). This enhances the usefulness of the- `-m`
- [PEP 3101: Advanced String Formatting](2.6.html#pep-3101). Note: the 2.6 description mentions the- `format()`- `str`- `bytes`- `%`operator in Python 3.1.
- [PEP 3105: print As a Function](2.6.html#pep-3105). This is now a standard feature and no longer needs to be imported from- `__future__`
- [PEP 3110: Exception-Handling Changes](2.6.html#pep-3110). The- `except`- *exc*- `as`- *var*syntax is now standard and- `except`- *exc*,- *var*is no longer supported. (Of course, the- `as`- *var*part is still optional.)
- [PEP 3112: Byte Literals](2.6.html#pep-3112). The- `b"..."`string literal notation (and its variants like- `b'...'`,- `b"""..."""`, and- `br"..."`) now produces a literal of type- `bytes`
- [PEP 3116: New I/O Library](2.6.html#pep-3116). The- `io`- `open()`- `io.open()`- *encoding*,- *errors*,- *newline*and- *closefd*. Also note that an invalid- *mode*argument now raises- `ValueError`- `IOError`- `f.buffer`(but beware that the text object maintains a buffer of itself in order to speed up the encoding and decoding operations).
- [PEP 3118: Revised Buffer Protocol](2.6.html#pep-3118). The old builtin- `buffer()`is now really gone; the new builtin- `memoryview()`
- [PEP 3119: Abstract Base Classes](2.6.html#pep-3119). The- `abc`- `collections`- `dict`- `list`- `collections.MutableMapping`- `collections.MutableSequence`
- [PEP 3127: Integer Literal Support and Syntax](2.6.html#pep-3127). As mentioned above, the new octal literal notation is the only one supported, and binary literals have been added.
- [PEP 3141: A Type Hierarchy for Numbers](2.6.html#pep-3141). The- `numbers`- `fractions`- `numbers.Rational`

## Library Changes[¶](#library-changes)

Due to time constraints, this document does not exhaustively cover the
very extensive changes to the standard library.  [ PEP 3108](https://peps.python.org/pep-3108/) is the
reference for the major changes to the library.  Here’s a capsule
review:

- Many old modules were removed. Some, like - `gopherlib`(no longer used) and- `md5`(replaced by- `hashlib`- **PEP 4**- **PEP 11**- **PEP 3108**
- The - `bsddb3`package was removed because its presence in the core standard library has proved over time to be a particular burden for the core developers due to testing instability and Berkeley DB’s release schedule. However, the package is alive and well, externally maintained at- [https://www.jcea.es/programacion/pybsddb.htm](https://www.jcea.es/programacion/pybsddb.htm).
- Some modules were renamed because their old name disobeyed - **PEP 8**- Old Name - New Name - _winreg - winreg - ConfigParser - configparser - copy_reg - copyreg - Queue - queue - SocketServer - socketserver - markupbase - _markupbase - repr - reprlib - test.test_support - test.support 
- A common pattern in Python 2.x is to have one version of a module implemented in pure Python, with an optional accelerated version implemented as a C extension; for example, - `pickle`- `cPickle`. This places the burden of importing the accelerated version and falling back on the pure Python version on each user of these modules. In Python 3.0, the accelerated versions are considered implementation details of the pure Python versions. Users should always import the standard version, which attempts to import the accelerated version and falls back to the pure Python version. The- `pickle`/- `cPickle`pair received this treatment. The- `profile`- `StringIO`module has been turned into a class in the- `io`
- Some related modules have been grouped into packages, and usually the submodule names have been simplified. The resulting new packages are: - `dbm`- `anydbm`,- `dbhash`,- `dbm`,- `dumbdbm`,- `gdbm`,- `whichdb`).
- `html`- `HTMLParser`,- `htmlentitydefs`).
- `http`- `httplib`,- `BaseHTTPServer`,- `CGIHTTPServer`,- `SimpleHTTPServer`,- `Cookie`,- `cookielib`).
- `tkinter`- `Tkinter`-related modules except- `turtle`- `turtle`doesn’t really care about- `tkinter`. Also note that as of Python 2.6, the functionality of- `turtle`has been greatly enhanced.
- `urllib`- `urllib`,- `urllib2`,- `urlparse`,- `robotparse`).
- `xmlrpc`- `xmlrpclib`,- `DocXMLRPCServer`,- `SimpleXMLRPCServer`).
 

Some other changes to standard library modules, not covered by
[ PEP 3108](https://peps.python.org/pep-3108/):

- Killed - `sets`. Use the built-in- `set()`
- Cleanup of the - `sys`- `sys.exitfunc()`,- `sys.exc_clear()`,- `sys.exc_type`,- `sys.exc_value`,- `sys.exc_traceback`. (Note that- `sys.last_type`
- Cleanup of the - `array.array`- `read()`and- `write()`methods are gone; use- `fromfile()`- `tofile()`- `'c'`typecode for array is gone – use either- `'b'`for bytes or- `'u'`for Unicode characters.
- Cleanup of the - `operator`- `sequenceIncludes()`and- `isCallable()`.
- Cleanup of the - `thread`module:- `acquire_lock()`and- `release_lock()`are gone; use- `acquire()`- `release()`
- Cleanup of the - `random`- `jumpahead()`API.
- The - `new`module is gone.
- The functions - `os.tmpnam()`,- `os.tempnam()`and- `os.tmpfile()`have been removed in favor of the- `tempfile`
- The - `tokenize`- `tokenize.tokenize()`
- `string.letters`and its friends (- `string.lowercase`and- `string.uppercase`) are gone. Use- `string.ascii_letters`- `string.letters`and friends had locale-specific behavior, which is a bad idea for such attractively named global “constants”.)
- Renamed module - `__builtin__`to- `builtins`- `__builtins__`variable found in most global namespaces is unchanged. To modify a builtin, you should use- `builtins`, not- `__builtins__`!

**PEP 3101**[¶](#pep-3101-a-new-approach-to-string-formatting)

**PEP 3101**

- A new system for built-in string formatting operations replaces the - `%`string formatting operator. (However, the- `%`operator is still supported; it will be deprecated in Python 3.1 and removed from the language at some later time.) Read- **PEP 3101**

## Changes To Exceptions[¶](#changes-to-exceptions)

The APIs for raising and catching exception have been cleaned up and new powerful features added:

- **PEP 352**- `BaseException`- *requirement*to inherit from- `BaseException`is new. (Python 2.6 still allowed classic classes to be raised, and placed no restriction on what you can catch.) As a consequence, string exceptions are finally truly and utterly dead.
- Almost all exceptions should actually derive from - `Exception`- `BaseException`- `SystemExit`- `KeyboardInterrupt`- `except`- `Exception`.
- `StandardError`was removed.
- Exceptions no longer behave as sequences. Use the - `args`
- **PEP 3109**- `raise`instead of- *Exception*(- *args*)- `raise`. Additionally, you can no longer explicitly specify a traceback; instead, if you- *Exception*,- *args*- *have*to do this, you can assign directly to the- `__traceback__`
- **PEP 3110**- `except`instead of- *SomeException*as- *variable*- `except`. Moreover, the- *SomeException*,- *variable*- *variable*is explicitly deleted when the- `except`
- **PEP 3134**- `except`- `finally`- *secondary*exception. In this case, the original exception (that was being handled) is saved as the- `__context__`- raise SecondaryException() from primary_exception - (where - *primary_exception*is any expression that produces an exception object, probably an exception that was previously caught). In this case, the primary exception is stored on the- `__cause__`- `__cause__`and- `__context__`
- **PEP 3134**- `__traceback__`- `sys.exc_info()`
- A few exception messages are improved when Windows fails to load an extension module. For example, - `error code 193`is now- `%1 is not a valid Win32 application`. Strings now deal with non-English locales.

## Miscellaneous Other Changes[¶](#miscellaneous-other-changes)

### Operators And Special Methods[¶](#operators-and-special-methods)

- `!=`now returns the opposite of- `==`, unless- `==`returns- `NotImplemented`
- The concept of “unbound methods” has been removed from the language. When referencing a method as a class attribute, you now get a plain function object. 
- `__getslice__()`,- `__setslice__()`and- `__delslice__()`were killed. The syntax- `a[i:j]`now translates to- `a.__getitem__(slice(i, j))`(or- `__setitem__()`- `__delitem__()`
- **PEP 3114**- `next()`- `__next__()`
- The - `__oct__()`and- `__hex__()`special methods are removed –- `oct()`- `hex()`- `__index__()`
- Removed support for - `__members__`and- `__methods__`.
- The function attributes named - `func_X`have been renamed to use the- `__X__`form, freeing up these names in the function attribute namespace for user-defined attributes. To wit,- `func_closure`,- `func_code`,- `func_defaults`,- `func_dict`,- `func_doc`,- `func_globals`,- `func_name`were renamed to- `__closure__`- `__code__`- `__defaults__`- `__dict__`- `__doc__`- `__globals__`- `__name__`
- `__nonzero__()`is now- `__bool__()`

### Builtins[¶](#builtins)

- **PEP 3135**- `super()`- `super()`without arguments and (assuming this is in a regular instance method defined inside a- `class`- `super()`is unchanged.
- **PEP 3111**- `raw_input()`was renamed to- `input()`- `input()`function reads a line from- `sys.stdin`- `EOFError`- `input()`, use- `eval(input())`.
- A new built-in function - `next()`- `__next__()`
- The - `round()`- `round(2.5)`now returns- `2`rather than- `3`.)- `round(x[, n])`now delegates to- `x.__round__([n])`instead of always returning a float. It generally returns an integer when called with a single argument and a value of the same type as- `x`when called with two arguments.
- Moved - `intern()`to- `sys.intern()`
- Removed: - `apply()`. Instead of- `apply(f, args)`use- `f(*args)`.
- Removed - `callable()`- `callable(f)`you can use- `isinstance(f, collections.Callable)`. The- `operator.isCallable()`function is also gone.
- Removed - `coerce()`. This function no longer serves a purpose now that classic classes are gone.
- Removed - `execfile()`. Instead of- `execfile(fn)`use- `exec(open(fn).read())`.
- Removed the - `file`type. Use- `open()`- `io`
- Removed - `reduce()`. Use- `functools.reduce()`- `for`
- Removed - `reload()`. Use- `imp.reload()`.
- Removed. - `dict.has_key()`– use the- `in`

## Build and C API Changes[¶](#build-and-c-api-changes)

Due to time constraints, here is a *very* incomplete list of changes
to the C API.

- Support for several platforms was dropped, including but not limited to Mac OS 9, BeOS, RISCOS, Irix, and Tru64. 
- **PEP 3118**
- **PEP 3121**
- **PEP 3123**- `PyObject_HEAD`
- No more C API support for restricted execution. 
- `PyNumber_Coerce()`,- `PyNumber_CoerceEx()`,- `PyMember_Get()`, and- `PyMember_Set()`C APIs are removed.
- New C API - `PyImport_ImportModuleNoBlock()`- `PyImport_ImportModule()`
- Renamed the boolean conversion C-level slot and method: - `nb_nonzero`is now- `nb_bool`.
- Removed - `METH_OLDARGS`and- `WITH_CYCLE_GC`from the C API.

## Performance[¶](#performance)

The net result of the 3.0 generalizations is that Python 3.0 runs the pystone benchmark around 10% slower than Python 2.5. Most likely the biggest cause is the removal of special-casing for small integers. There’s room for improvement, but it will happen after 3.0 is released!

## Porting To Python 3.0[¶](#porting-to-python-3-0)

For porting existing Python 2.5 or 2.6 source code to Python 3.0, the best strategy is the following:

- (Prerequisite:) Start with excellent test coverage. 
- Port to Python 2.6. This should be no more work than the average port from Python 2.x to Python 2.(x+1). Make sure all your tests pass. 
- (Still using 2.6:) Turn on the - `-3`command line switch. This enables warnings about features that will be removed (or change) in 3.0. Run your test suite again, and fix code that you get warnings about until there are no warnings left, and all your tests still pass.
- Run the - `2to3`source-to-source translator over your source code tree. Run the result of the translation under Python 3.0. Manually fix up any remaining issues, fixing problems until all tests pass again.

It is not recommended to try to write source code that runs unchanged
under both Python 2.6 and 3.0; you’d have to use a very contorted
coding style, e.g. avoiding `print` statements, metaclasses,
and much more.  If you are maintaining a library that needs to support
both Python 2.6 and Python 3.0, the best approach is to modify step 3
above by editing the 2.6 version of the source code and running the
`2to3` translator again, rather than editing the 3.0 version of the
source code.

For porting C extensions to Python 3.0, please see [Porting Extension Modules to Python 3](../howto/cporting.html#cporting-howto).