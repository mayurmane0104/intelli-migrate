# 3. Data model — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/reference/datamodel.html](https://docs.python.org/3.13/reference/datamodel.html)

---

# 3. Data model[¶](#data-model)

## 3.1. Objects, values and types[¶](#objects-values-and-types)

*Objects* are Python’s abstraction for data.  All data in a Python program
is represented by objects or by relations between objects. Even code is
represented by objects.

Every object has an identity, a type and a value.  An object’s *identity* never
changes once it has been created; you may think of it as the object’s address in
memory.  The [ is](expressions.html#is) operator compares the identity of two objects; the

[function returns an integer representing its identity.](../library/functions.html#id)

`id()`**CPython implementation detail:** For CPython, `id(x)` is the memory address where `x` is stored.

An object’s type determines the operations that the object supports (e.g., “does
it have a length?”) and also defines the possible values for objects of that
type.  The [ type()](../library/functions.html#type) function returns an object’s type (which is an object
itself).  Like its identity, an object’s 

*type*is also unchangeable.

[[1]](#id19)

The *value* of some objects can change.  Objects whose value can
change are said to be *mutable*; objects whose value is unchangeable once they
are created are called *immutable*. (The value of an immutable container object
that contains a reference to a mutable object can change when the latter’s value
is changed; however the container is still considered immutable, because the
collection of objects it contains cannot be changed.  So, immutability is not
strictly the same as having an unchangeable value, it is more subtle.) An
object’s mutability is determined by its type; for instance, numbers, strings
and tuples are immutable, while dictionaries and lists are mutable.

Objects are never explicitly destroyed; however, when they become unreachable they may be garbage-collected. An implementation is allowed to postpone garbage collection or omit it altogether — it is a matter of implementation quality how garbage collection is implemented, as long as no objects are collected that are still reachable.

**CPython implementation detail:** CPython currently uses a reference-counting scheme with (optional) delayed
detection of cyclically linked garbage, which collects most objects as soon
as they become unreachable, but is not guaranteed to collect garbage
containing circular references.  See the documentation of the [ gc](../library/gc.html#module-gc)
module for information on controlling the collection of cyclic garbage.
Other implementations act differently and CPython may change.
Do not depend on immediate finalization of objects when they become
unreachable (so you should always close files explicitly).

Note that the use of the implementation’s tracing or debugging facilities may
keep objects alive that would normally be collectable. Also note that catching
an exception with a [ try](compound_stmts.html#try)…

[statement may keep objects alive.](compound_stmts.html#except)

`except`Some objects contain references to “external” resources such as open files or
windows.  It is understood that these resources are freed when the object is
garbage-collected, but since garbage collection is not guaranteed to happen,
such objects also provide an explicit way to release the external resource,
usually a `close()` method. Programs are strongly recommended to explicitly
close such objects.  The [ try](compound_stmts.html#try)…

[statement and the](compound_stmts.html#finally)

`finally`[statement provide convenient ways to do this.](compound_stmts.html#with)

`with`Some objects contain references to other objects; these are called *containers*.
Examples of containers are tuples, lists and dictionaries.  The references are
part of a container’s value.  In most cases, when we talk about the value of a
container, we imply the values, not the identities of the contained objects;
however, when we talk about the mutability of a container, only the identities
of the immediately contained objects are implied.  So, if an immutable container
(like a tuple) contains a reference to a mutable object, its value changes if
that mutable object is changed.

Types affect almost all aspects of object behavior.  Even the importance of
object identity is affected in some sense: for immutable types, operations that
compute new values may actually return a reference to any existing object with
the same type and value, while for mutable objects this is not allowed.
For example, after `a = 1; b = 1`, *a* and *b* may or may not refer to
the same object with the value one, depending on the implementation.
This is because [ int](../library/functions.html#int) is an immutable type, so the reference to 

`1`
can be reused. This behaviour depends on the implementation used, so should
not be relied upon, but is something to be aware of when making use of object
identity tests.
However, after `c = []; d = []`, *c*and

*d*are guaranteed to refer to two different, unique, newly created empty lists. (Note that

`e = f = []` assigns
the *same*object to both

*e*and

*f*.)

## 3.2. The standard type hierarchy[¶](#the-standard-type-hierarchy)

Below is a list of the types that are built into Python. Extension modules (written in C, Java, or other languages, depending on the implementation) can define additional types. Future versions of Python may add types to the type hierarchy (e.g., rational numbers, efficiently stored arrays of integers, etc.), although such additions will often be provided via the standard library instead.

Some of the type descriptions below contain a paragraph listing ‘special attributes.’ These are attributes that provide access to the implementation and are not intended for general use. Their definition may change in the future.

### 3.2.1. None[¶](#none)

This type has a single value.  There is a single object with this value. This
object is accessed through the built-in name `None`. It is used to signify the
absence of a value in many situations, e.g., it is returned from functions that
don’t explicitly return anything. Its truth value is false.

### 3.2.2. NotImplemented[¶](#notimplemented)

This type has a single value.  There is a single object with this value. This
object is accessed through the built-in name [ NotImplemented](../library/constants.html#NotImplemented). Numeric methods
and rich comparison methods should return this value if they do not implement the
operation for the operands provided.  (The interpreter will then try the
reflected operation, or some other fallback, depending on the operator.)  It
should not be evaluated in a boolean context.

See
[Implementing the arithmetic operations](../library/numbers.html#implementing-the-arithmetic-operations)
for more details.

Changed in version 3.9: Evaluating [ NotImplemented](../library/constants.html#NotImplemented) in a boolean context is deprecated. While
it currently evaluates as true, it will emit a 

[. It will raise a](../library/exceptions.html#DeprecationWarning)

`DeprecationWarning`[in a future version of Python.](../library/exceptions.html#TypeError)

`TypeError`### 3.2.3. Ellipsis[¶](#ellipsis)

This type has a single value.  There is a single object with this value. This
object is accessed through the literal `...` or the built-in name
`Ellipsis`.  Its truth value is true.

### 3.2.4. `numbers.Number`[¶](#numbers-number)

`numbers.Number`These are created by numeric literals and returned as results by arithmetic operators and arithmetic built-in functions. Numeric objects are immutable; once created their value never changes. Python numbers are of course strongly related to mathematical numbers, but subject to the limitations of numerical representation in computers.

The string representations of the numeric classes, computed by
[ __repr__()](#object.__repr__) and 

[, have the following properties:](#object.__str__)

`__str__()`- They are valid numeric literals which, when passed to their class constructor, produce an object having the value of the original numeric. 
- The representation is in base 10, when possible. 
- Leading zeros, possibly excepting a single zero before a decimal point, are not shown. 
- Trailing zeros, possibly excepting a single zero after a decimal point, are not shown. 
- A sign is shown only when the number is negative. 

Python distinguishes between integers, floating-point numbers, and complex numbers:

#### 3.2.4.1. `numbers.Integral`[¶](#numbers-integral)

`numbers.Integral`These represent elements from the mathematical set of integers (positive and negative).

Note

The rules for integer representation are intended to give the most meaningful interpretation of shift and mask operations involving negative integers.

There are two types of integers:

- Integers (`int`
- These represent numbers in an unlimited range, subject to available (virtual) memory only. For the purpose of shift and mask operations, a binary representation is assumed, and negative numbers are represented in a variant of 2’s complement which gives the illusion of an infinite string of sign bits extending to the left. 
- Booleans (`bool`
- These represent the truth values False and True. The two objects representing the values - `False`and- `True`are the only Boolean objects. The Boolean type is a subtype of the integer type, and Boolean values behave like the values 0 and 1, respectively, in almost all contexts, the exception being that when converted to a string, the strings- `"False"`or- `"True"`are returned, respectively.

#### 3.2.4.2. `numbers.Real``float`[¶](#numbers-real-float)

`numbers.Real``float`These represent machine-level double precision floating-point numbers. You are at the mercy of the underlying machine architecture (and C or Java implementation) for the accepted range and handling of overflow. Python does not support single-precision floating-point numbers; the savings in processor and memory usage that are usually the reason for using these are dwarfed by the overhead of using objects in Python, so there is no reason to complicate the language with two kinds of floating-point numbers.

#### 3.2.4.3. `numbers.Complex``complex`[¶](#numbers-complex-complex)

`numbers.Complex``complex`These represent complex numbers as a pair of machine-level double precision
floating-point numbers.  The same caveats apply as for floating-point numbers.
The real and imaginary parts of a complex number `z` can be retrieved through
the read-only attributes `z.real` and `z.imag`.

### 3.2.5. Sequences[¶](#sequences)

These represent finite ordered sets indexed by non-negative numbers. The
built-in function [ len()](../library/functions.html#len) returns the number of items of a sequence. When
the length of a sequence is 

*n*, the index set contains the numbers 0, 1, …,

*n*-1. Item

*i*of sequence

*a*is selected by

`a[i]`. Some sequences,
including built-in sequences, interpret negative subscripts by adding the
sequence length. For example, `a[-2]` equals `a[n-2]`, the second to last
item of sequence a with length `n`.Sequences also support slicing: `a[i:j]` selects all items with index *k* such
that *i* `<=` *k* `<` *j*.  When used as an expression, a slice is a
sequence of the same type. The comment above about negative indexes also applies
to negative slice positions.

Some sequences also support “extended slicing” with a third “step” parameter:
`a[i:j:k]` selects all items of *a* with index *x* where `x = i + n*k`, *n*
`>=` `0` and *i* `<=` *x* `<` *j*.

Sequences are distinguished according to their mutability:

#### 3.2.5.1. Immutable sequences[¶](#immutable-sequences)

An object of an immutable sequence type cannot change once it is created. (If the object contains references to other objects, these other objects may be mutable and may be changed; however, the collection of objects directly referenced by an immutable object cannot change.)

The following types are immutable sequences:

- Strings
- A string is a sequence of values that represent Unicode code points. All the code points in the range - `U+0000 - U+10FFFF`can be represented in a string. Python doesn’t have a char type; instead, every code point in the string is represented as a string object with length- `1`. The built-in function- `ord()`- `0 - 10FFFF`;- `chr()`- `0 - 10FFFF`to the corresponding length- `1`string object.- `str.encode()`- `str`- `bytes`- `bytes.decode()`
- Tuples
- The items of a tuple are arbitrary Python objects. Tuples of two or more items are formed by comma-separated lists of expressions. A tuple of one item (a ‘singleton’) can be formed by affixing a comma to an expression (an expression by itself does not create a tuple, since parentheses must be usable for grouping of expressions). An empty tuple can be formed by an empty pair of parentheses. 
- Bytes
- A bytes object is an immutable array. The items are 8-bit bytes, represented by integers in the range 0 <= x < 256. Bytes literals (like - `b'abc'`) and the built-in- `bytes()`- `decode()`

#### 3.2.5.2. Mutable sequences[¶](#mutable-sequences)

Mutable sequences can be changed after they are created.  The subscription and
slicing notations can be used as the target of assignment and [ del](simple_stmts.html#del)
(delete) statements.

Note

The [ collections](../library/collections.html#module-collections) and 

[module provide additional examples of mutable sequence types.](../library/array.html#module-array)

`array`There are currently two intrinsic mutable sequence types:

- Lists
- The items of a list are arbitrary Python objects. Lists are formed by placing a comma-separated list of expressions in square brackets. (Note that there are no special cases needed to form lists of length 0 or 1.) 
- Byte Arrays
- A bytearray object is a mutable array. They are created by the built-in - `bytearray()`- `bytes`

### 3.2.6. Set types[¶](#set-types)

These represent unordered, finite sets of unique, immutable objects. As such,
they cannot be indexed by any subscript. However, they can be iterated over, and
the built-in function [ len()](../library/functions.html#len) returns the number of items in a set. Common
uses for sets are fast membership testing, removing duplicates from a sequence,
and computing mathematical operations such as intersection, union, difference,
and symmetric difference.

For set elements, the same immutability rules apply as for dictionary keys. Note
that numeric types obey the normal rules for numeric comparison: if two numbers
compare equal (e.g., `1` and `1.0`), only one of them can be contained in a
set.

There are currently two intrinsic set types:

- Sets
- These represent a mutable set. They are created by the built-in - `set()`- `add()`
- Frozen sets
- These represent an immutable set. They are created by the built-in - `frozenset()`- [hashable](../glossary.html#term-hashable), it can be used again as an element of another set, or as a dictionary key.

### 3.2.7. Mappings[¶](#mappings)

These represent finite sets of objects indexed by arbitrary index sets. The
subscript notation `a[k]` selects the item indexed by `k` from the mapping
`a`; this can be used in expressions and as the target of assignments or
[ del](simple_stmts.html#del) statements. The built-in function 

[returns the number of items in a mapping.](../library/functions.html#len)

`len()`There is currently a single intrinsic mapping type:

#### 3.2.7.1. Dictionaries[¶](#dictionaries)

These represent finite sets of objects indexed by nearly arbitrary values.  The
only types of values not acceptable as keys are values containing lists or
dictionaries or other mutable types that are compared by value rather than by
object identity, the reason being that the efficient implementation of
dictionaries requires a key’s hash value to remain constant. Numeric types used
for keys obey the normal rules for numeric comparison: if two numbers compare
equal (e.g., `1` and `1.0`) then they can be used interchangeably to index
the same dictionary entry.

Dictionaries preserve insertion order, meaning that keys will be produced in the same order they were added sequentially over the dictionary. Replacing an existing key does not change the order, however removing a key and re-inserting it will add it to the end instead of keeping its old place.

Dictionaries are mutable; they can be created by the `{}` notation (see
section [Dictionary displays](expressions.html#dict)).

The extension modules [ dbm.ndbm](../library/dbm.html#module-dbm.ndbm) and 

[provide additional examples of mapping types, as does the](../library/dbm.html#module-dbm.gnu)

`dbm.gnu`[module.](../library/collections.html#module-collections)

`collections`Changed in version 3.7: Dictionaries did not preserve insertion order in versions of Python before 3.6. In CPython 3.6, insertion order was preserved, but it was considered an implementation detail at that time rather than a language guarantee.

### 3.2.8. Callable types[¶](#callable-types)

These are the types to which the function call operation (see section
[Calls](expressions.html#calls)) can be applied:

#### 3.2.8.1. User-defined functions[¶](#user-defined-functions)

A user-defined function object is created by a function definition (see
section [Function definitions](compound_stmts.html#function)).  It should be called with an argument list
containing the same number of items as the function’s formal parameter
list.

##### 3.2.8.1.1. Special read-only attributes[¶](#special-read-only-attributes)

| Attribute | Meaning | 
|---|---|
| 
 | A reference to the  Added in version 3.10. | 
| 
 | A reference to the  [global variables](executionmodel.html#naming)– the global namespace of the module
in which the function was defined. | 
| 
 | 
 attribute of the function’s`co_freevars`.`code object`A cell object has the attribute  | 

##### 3.2.8.1.2. Special writable attributes[¶](#special-writable-attributes)

Most of these attributes check the type of the assigned value:

| Attribute | Meaning | 
|---|---|
| 
 | The function’s documentation string, or  | 
| 
 | The function’s name.
See also:  | 
| 
 | The function’s  Added in version 3.3. | 
| 
 | The name of the module the function was defined in,
or  | 
| 
 | A  [parameter](../glossary.html#term-parameter)values
for those parameters that have defaults,
or`None`if no parameters have a default value. | 
| 
 | The  | 
| 
 | The namespace supporting arbitrary function attributes.
See also:  | 
| 
 | A  [parameters](../glossary.html#term-parameter).
The keys of the dictionary are the parameter names,
and`'return'`for the return annotation, if provided.
See also:[Annotations Best Practices](../howto/annotations.html#annotations-howto). | 
| 
 | A  [parameters](../glossary.html#term-parameter). | 
| 
 | A  [type parameters](compound_stmts.html#type-params)of
a[generic function](compound_stmts.html#generic-functions).Added in version 3.12. | 

Function objects also support getting and setting arbitrary attributes, which can be used, for example, to attach metadata to functions. Regular attribute dot-notation is used to get and set such attributes.

**CPython implementation detail:** CPython’s current implementation only supports function attributes
on user-defined functions. Function attributes on
[built-in functions](#builtin-functions) may be supported in the
future.

Additional information about a function’s definition can be retrieved from its
[code object](#code-objects)
(accessible via the [ __code__](#function.__code__) attribute).

#### 3.2.8.2. Instance methods[¶](#instance-methods)

An instance method object combines a class, a class instance and any callable object (normally a user-defined function).

Special read-only attributes:

| 
 | Refers to the class instance object to which the method is
 | 
| 
 | Refers to the original  | 
| 
 | The method’s documentation
(same as  if the original function had a docstring, else`string``None`. | 
| 
 | The name of the method
(same as  | 
| 
 | The name of the module the method was defined in, or  | 

Methods also support accessing (but not setting) the arbitrary function
attributes on the underlying [function object](#user-defined-funcs).

User-defined method objects may be created when getting an attribute of a
class (perhaps via an instance of that class), if that attribute is a
user-defined [function object](#user-defined-funcs) or a
[ classmethod](../library/functions.html#classmethod) object.

When an instance method object is created by retrieving a user-defined
[function object](#user-defined-funcs) from a class via one of its
instances, its [ __self__](#method.__self__) attribute is the instance, and the
method object is said to be 

*bound*. The new method’s

[attribute is the original function object.](#method.__func__)

`__func__`When an instance method object is created by retrieving a [ classmethod](../library/functions.html#classmethod)
object from a class or instance, its 

[attribute is the class itself, and its](#method.__self__)

`__self__`[attribute is the function object underlying the class method.](#method.__func__)

`__func__`When an instance method object is called, the underlying function
([ __func__](#method.__func__)) is called, inserting the class instance
(

[) in front of the argument list. For instance, when](#method.__self__)

`__self__``C` is a class which contains a definition for a function
`f()`, and `x` is an instance of `C`, calling `x.f(1)` is
equivalent to calling `C.f(x, 1)`.When an instance method object is derived from a [ classmethod](../library/functions.html#classmethod) object, the
“class instance” stored in 

[will actually be the class itself, so that calling either](#method.__self__)

`__self__``x.f(1)` or `C.f(1)` is equivalent to
calling `f(C,1)` where `f` is the underlying function.It is important to note that user-defined functions
which are attributes of a class instance are not converted to bound
methods; this *only* happens when the function is an attribute of the
class.

#### 3.2.8.3. Generator functions[¶](#generator-functions)

A function or method which uses the [ yield](simple_stmts.html#yield) statement (see section

[The yield statement](simple_stmts.html#yield)) is called a

*generator function*. Such a function, when called, always returns an

[iterator](../glossary.html#term-iterator)object which can be used to execute the body of the function: calling the iterator’s

[method will cause the function to execute until it provides a value using the](../library/stdtypes.html#iterator.__next__)

`iterator.__next__()``yield` statement.  When the
function executes a [statement or falls off the end, a](simple_stmts.html#return)

`return`[exception is raised and the iterator will have reached the end of the set of values to be returned.](../library/exceptions.html#StopIteration)

`StopIteration`#### 3.2.8.4. Coroutine functions[¶](#coroutine-functions)

A function or method which is defined using [ async def](compound_stmts.html#async-def) is called
a 

*coroutine function*. Such a function, when called, returns a

[coroutine](../glossary.html#term-coroutine)object. It may contain

[expressions, as well as](expressions.html#await)

`await`[and](compound_stmts.html#async-with)

`async with`[statements. See also the](compound_stmts.html#async-for)

`async for`[Coroutine Objects](#coroutine-objects)section.

#### 3.2.8.5. Asynchronous generator functions[¶](#asynchronous-generator-functions)

A function or method which is defined using [ async def](compound_stmts.html#async-def) and
which uses the 

[statement is called a](simple_stmts.html#yield)

`yield`*asynchronous generator function*. Such a function, when called, returns an

[asynchronous iterator](../glossary.html#term-asynchronous-iterator)object which can be used in an

[statement to execute the body of the function.](compound_stmts.html#async-for)

`async for`Calling the asynchronous iterator’s
[ aiterator.__anext__](#object.__anext__) method
will return an 

[awaitable](../glossary.html#term-awaitable)which when awaited will execute until it provides a value using the

[expression. When the function executes an empty](simple_stmts.html#yield)

`yield`[statement or falls off the end, a](simple_stmts.html#return)

`return`[exception is raised and the asynchronous iterator will have reached the end of the set of values to be yielded.](../library/exceptions.html#StopAsyncIteration)

`StopAsyncIteration`#### 3.2.8.6. Built-in functions[¶](#built-in-functions)

A built-in function object is a wrapper around a C function.  Examples of
built-in functions are [ len()](../library/functions.html#len) and 

[(](../library/math.html#math.sin)

`math.sin()`[is a standard built-in module). The number and type of the arguments are determined by the C function. Special read-only attributes:](../library/math.html#module-math)

`math`- `__doc__`is the function’s documentation string, or- `None`if unavailable. See- `function.__doc__`
- `__name__`is the function’s name. See- `function.__name__`
- `__self__`is set to- `None`(but see the next item).
- `__module__`is the name of the module the function was defined in or- `None`if unavailable. See- `function.__module__`

#### 3.2.8.7. Built-in methods[¶](#built-in-methods)

This is really a different disguise of a built-in function, this time containing
an object passed to the C function as an implicit extra argument.  An example of
a built-in method is `alist.append()`, assuming *alist* is a list object. In
this case, the special read-only attribute `__self__` is set to the object
denoted by *alist*. (The attribute has the same semantics as it does with
[ other instance methods](#method.__self__).)

#### 3.2.8.8. Classes[¶](#classes)

Classes are callable.  These objects normally act as factories for new
instances of themselves, but variations are possible for class types that
override [ __new__()](#object.__new__).  The arguments of the call are passed to

`__new__()` and, in the typical case, to [to initialize the new instance.](#object.__init__)

`__init__()`#### 3.2.8.9. Class Instances[¶](#class-instances)

Instances of arbitrary classes can be made callable by defining a
[ __call__()](#object.__call__) method in their class.

### 3.2.9. Modules[¶](#modules)

Modules are a basic organizational unit of Python code, and are created by
the [import system](import.html#importsystem) as invoked either by the
[ import](simple_stmts.html#import) statement, or by calling
functions such as 

[and built-in](../library/importlib.html#importlib.import_module)

`importlib.import_module()`[. A module object has a namespace implemented by a](../library/functions.html#import__)

`__import__()`[object (this is the dictionary referenced by the](../library/stdtypes.html#dict)

`dictionary`[attribute of functions defined in the module). Attribute references are translated to lookups in this dictionary, e.g.,](#function.__globals__)

`__globals__``m.x` is equivalent to
`m.__dict__["x"]`. A module object does not contain the code object used
to initialize the module (since it isn’t needed once the initialization is
done).Attribute assignment updates the module’s namespace dictionary, e.g.,
`m.x = 1` is equivalent to `m.__dict__["x"] = 1`.

#### 3.2.9.2. Other writable attributes on module objects[¶](#other-writable-attributes-on-module-objects)

As well as the import-related attributes listed above, module objects also have the following writable attributes:

- 
module.__doc__[¶](#module.__doc__)
- The module’s documentation string, or - `None`if unavailable. See also:- `__doc__ attributes`

- 
module.__annotations__[¶](#module.__annotations__)
- A dictionary containing - [variable annotations](../glossary.html#term-variable-annotation)collected during module body execution. For best practices on working with- `__annotations__`- [Annotations Best Practices](../howto/annotations.html#annotations-howto).

#### 3.2.9.3. Module dictionaries[¶](#module-dictionaries)

Module objects also have the following special read-only attribute:

- 
module.__dict__[¶](#module.__dict__)
- The module’s namespace as a dictionary object. Uniquely among the attributes listed here, - `__dict__`cannot be accessed as a global variable from within a module; it can only be accessed as an attribute on module objects.- **CPython implementation detail:**Because of the way CPython clears module dictionaries, the module dictionary will be cleared when the module falls out of scope even if the dictionary still has live references. To avoid this, copy the dictionary or keep the module around while using its dictionary directly.

### 3.2.10. Custom classes[¶](#custom-classes)

Custom class types are typically created by class definitions (see section
[Class definitions](compound_stmts.html#class)).  A class has a namespace implemented by a dictionary object.
Class attribute references are translated to lookups in this dictionary, e.g.,
`C.x` is translated to `C.__dict__["x"]` (although there are a number of
hooks which allow for other means of locating attributes). When the attribute
name is not found there, the attribute search continues in the base classes.
This search of the base classes uses the C3 method resolution order which
behaves correctly even in the presence of ‘diamond’ inheritance structures
where there are multiple inheritance paths leading back to a common ancestor.
Additional details on the C3 MRO used by Python can be found at
[The Python 2.3 Method Resolution Order](../howto/mro.html#python-2-3-mro).

When a class attribute reference (for class `C`, say) would yield a
class method object, it is transformed into an instance method object whose
[ __self__](#method.__self__) attribute is 

`C`.
When it would yield a [object, it is transformed into the object wrapped by the static method object. See section](../library/functions.html#staticmethod)

`staticmethod`[Implementing Descriptors](#descriptors)for another way in which attributes retrieved from a class may differ from those actually contained in its

[.](#object.__dict__)

`__dict__`Class attribute assignments update the class’s dictionary, never the dictionary of a base class.

A class object can be called (see above) to yield a class instance (see below).

#### 3.2.10.1. Special attributes[¶](#special-attributes)

| Attribute | Meaning | 
|---|---|
| 
 | The class’s name.
See also:  | 
| 
 | The class’s  | 
| 
 | The name of the module in which the class was defined. | 
| 
 | A  .`__dict__ attributes` | 
| 
 | A  `class X(A, B, C)`,`X.__bases__`will be exactly equal to`(A, B, C)`. | 
| 
 | 
 | 
| 
 | The class’s documentation string, or  | 
| 
 | A dictionary containing
 Caution Accessing the  | 
| 
 | A  [type parameters](compound_stmts.html#type-params)of
a[generic class](compound_stmts.html#generic-classes).Added in version 3.12. | 
| 
 | A  `self.X`from any function in its body.Added in version 3.13. | 
| 
 | The line number of the first line of the class definition,
including decorators.
Setting the  `__firstlineno__`item from the type’s dictionary.Added in version 3.13. | 
| 
 | The  | 

#### 3.2.10.2. Special methods[¶](#special-methods)

In addition to the special attributes described above, all Python classes also have the following two methods available:

- 
type.mro()[¶](#type.mro)
- This method can be overridden by a metaclass to customize the method resolution order for its instances. It is called at class instantiation, and its result is stored in - `__mro__`

- 
type.__subclasses__()[¶](#type.__subclasses__)
- Each class keeps a list of weak references to its immediate subclasses. This method returns a list of all those references still alive. The list is in definition order. Example: - >>> class A: pass >>> class B(A): pass >>> A.__subclasses__() [<class 'B'>] 

### 3.2.11. Class instances[¶](#id4)

A class instance is created by calling a class object (see above).  A class
instance has a namespace implemented as a dictionary which is the first place
in which attribute references are searched.  When an attribute is not found
there, and the instance’s class has an attribute by that name, the search
continues with the class attributes.  If a class attribute is found that is a
user-defined function object, it is transformed into an instance method
object whose [ __self__](#method.__self__) attribute is the instance.  Static method and
class method objects are also transformed; see above under “Classes”.  See
section 

[Implementing Descriptors](#descriptors)for another way in which attributes of a class retrieved via its instances may differ from the objects actually stored in the class’s

[. If no class attribute is found, and the object’s class has a](#object.__dict__)

`__dict__`[method, that is called to satisfy the lookup.](#object.__getattr__)

`__getattr__()`Attribute assignments and deletions update the instance’s dictionary, never a
class’s dictionary.  If the class has a [ __setattr__()](#object.__setattr__) or

[method, this is called instead of updating the instance dictionary directly.](#object.__delattr__)

`__delattr__()`Class instances can pretend to be numbers, sequences, or mappings if they have
methods with certain special names.  See section [Special method names](#specialnames).

#### 3.2.11.1. Special attributes[¶](#id5)

- 
object.__class__[¶](#object.__class__)
- The class to which a class instance belongs. 

### 3.2.12. I/O objects (also known as file objects)[¶](#i-o-objects-also-known-as-file-objects)

A [file object](../glossary.html#term-file-object) represents an open file.  Various shortcuts are
available to create file objects: the [ open()](../library/functions.html#open) built-in function, and
also 

[,](../library/os.html#os.popen)

`os.popen()`[, and the](../library/os.html#os.fdopen)

`os.fdopen()`[method of socket objects (and perhaps by other functions or methods provided by extension modules).](../library/socket.html#socket.socket.makefile)

`makefile()`File objects implement common methods, listed below, to simplify usage in
generic code. They are expected to be [With Statement Context Managers](#context-managers).

The objects `sys.stdin`, `sys.stdout` and `sys.stderr` are
initialized to file objects corresponding to the interpreter’s standard
input, output and error streams; they are all open in text mode and
therefore follow the interface defined by the [ io.TextIOBase](../library/io.html#io.TextIOBase)
abstract class.

- 
file.read(*size=-1*,*/*)[¶](#file.read)
- Retrieve up to - *size*data from the file. As a convenience if- *size*is unspecified or -1 retrieve all data available.

- 
file.write(*data*,*/*)[¶](#file.write)
- Store - *data*to the file.

- 
file.close()[¶](#file.close)
- Flush any buffers and close the underlying file. 

### 3.2.13. Internal types[¶](#internal-types)

A few types used internally by the interpreter are exposed to the user. Their definitions may change with future versions of the interpreter, but they are mentioned here for completeness.

#### 3.2.13.1. Code objects[¶](#code-objects)

Code objects represent *byte-compiled* executable Python code, or [bytecode](../glossary.html#term-bytecode).
The difference between a code object and a function object is that the function
object contains an explicit reference to the function’s globals (the module in
which it was defined), while a code object contains no context; also the default
argument values are stored in the function object, not in the code object
(because they represent values calculated at run-time).  Unlike function
objects, code objects are immutable and contain no references (directly or
indirectly) to mutable objects.

##### 3.2.13.1.1. Special read-only attributes[¶](#index-60)

| 
 | The function name | 
| 
 | The fully qualified function name Added in version 3.11. | 
| 
 | The total number of positional  | 
| 
 | The number of positional-only  | 
| 
 | The number of keyword-only  | 
| 
 | The number of  | 
| 
 | A  | 
| 
 | A  [local variables](executionmodel.html#naming)that are referenced from at least one[nested scope](../glossary.html#term-nested-scope)inside the function | 
| 
 | A  [free (closure) variables](../glossary.html#term-closure-variable)that a[nested scope](../glossary.html#term-nested-scope)references in an outer scope. See also.`function.__closure__`Note: references to global and builtin names are  | 
| 
 | A string representing the sequence of  | 
| 
 | A  [bytecode](../glossary.html#term-bytecode)in
the function | 
| 
 | A  [bytecode](../glossary.html#term-bytecode)in
the function | 
| 
 | The name of the file from which the code was compiled | 
| 
 | The line number of the first line of the function | 
| 
 | A string encoding the mapping from  Deprecated since version 3.12: This attribute of code objects is deprecated, and may be removed in Python 3.15. | 
| 
 | The required stack size of the code object | 
| 
 | An  | 

The following flag bits are defined for [ co_flags](#codeobject.co_flags):
bit 

`0x04` is set if
the function uses the `*arguments` syntax to accept an arbitrary number of
positional arguments; bit `0x08` is set if the function uses the
`**keywords` syntax to accept arbitrary keyword arguments; bit `0x20` is set
if the function is a generator. See [Code Objects Bit Flags](../library/inspect.html#inspect-module-co-flags)for details on the semantics of each flags that might be present.

Future feature declarations (for example, `from __future__ import division`) also use bits
in [ co_flags](#codeobject.co_flags) to indicate whether a code object was compiled with a
particular feature enabled. See 

[.](../library/__future__.html#future__._Feature.compiler_flag)

`compiler_flag`Other bits in [ co_flags](#codeobject.co_flags) are reserved for internal use.

If a code object represents a function, the first item in
[ co_consts](#codeobject.co_consts) is
the documentation string of the function, or 

`None` if undefined.##### 3.2.13.1.2. Methods on code objects[¶](#methods-on-code-objects)

- 
codeobject.co_positions()[¶](#codeobject.co_positions)
- Returns an iterable over the source code positions of each - [bytecode](../glossary.html#term-bytecode)instruction in the code object.- The iterator returns - `tuple`- `(start_line, end_line, start_column, end_column)`. The- *i-th*tuple corresponds to the position of the source code that compiled to the- *i-th*code unit. Column information is 0-indexed utf-8 byte offsets on the given source line.- This positional information can be missing. A non-exhaustive lists of cases where this may happen: - Running the interpreter with - `-X`- `no_debug_ranges`.
- Loading a pyc file compiled while using - `-X`- `no_debug_ranges`.
- Position tuples corresponding to artificial instructions. 
- Line and column numbers that can’t be represented due to implementation specific limitations. 
 - When this occurs, some or all of the tuple elements can be - `None`- Added in version 3.11. - Note - This feature requires storing column positions in code objects which may result in a small increase of disk usage of compiled Python files or interpreter memory usage. To avoid storing the extra information and/or deactivate printing the extra traceback information, the - `-X`- `no_debug_ranges`command line flag or the- `PYTHONNODEBUGRANGES`

- 
codeobject.co_lines()[¶](#codeobject.co_lines)
- Returns an iterator that yields information about successive ranges of - [bytecode](../glossary.html#term-bytecode)s. Each item yielded is a- `(start, end, lineno)`- `tuple`- `start`(an- `int`- [bytecode](../glossary.html#term-bytecode)range
- `end`(an- `int`- [bytecode](../glossary.html#term-bytecode)range
- `lineno`is an- `int`- [bytecode](../glossary.html#term-bytecode)range, or- `None`if the bytecodes in the given range have no line number
 - The items yielded will have the following properties: - The first range yielded will have a - `start`of 0.
- The - `(start, end)`ranges will be non-decreasing and consecutive. That is, for any pair of- `tuple`- `start`of the second will be equal to the- `end`of the first.
- No range will be backwards: - `end >= start`for all triples.
- The last - `tuple`- `end`equal to the size of the- [bytecode](../glossary.html#term-bytecode).
 - Zero-width ranges, where - `start == end`, are allowed. Zero-width ranges are used for lines that are present in the source code, but have been eliminated by the- [bytecode](../glossary.html#term-bytecode)compiler.- Added in version 3.10. - See also - **PEP 626**
- The PEP that introduced the - `co_lines()`method.
 

- 
codeobject.replace(***kwargs*)[¶](#codeobject.replace)
- Return a copy of the code object with new values for the specified fields. - Code objects are also supported by the generic function - `copy.replace()`- Added in version 3.8. 

#### 3.2.13.2. Frame objects[¶](#frame-objects)

Frame objects represent execution frames.  They may occur in
[traceback objects](#traceback-objects),
and are also passed to registered trace functions.

##### 3.2.13.2.1. Special read-only attributes[¶](#index-66)

| 
 | Points to the previous stack frame (towards the caller),
or  | 
| 
 | The  | 
| 
 | The mapping used by the frame to look up
 Changed in version 3.13: Return a proxy for optimized scopes. | 
| 
 | The dictionary used by the frame to look up
 | 
| 
 | The dictionary used by the frame to look up
 | 
| 
 | The “precise instruction” of the frame object
(this is an index into the  | 

##### 3.2.13.2.2. Special writable attributes[¶](#index-67)

| 
 | If not  | 
| 
 | Set this attribute to  | 
| 
 | Set this attribute to  | 
| 
 | The current line number of the frame – writing to this from within a trace function jumps to the given line (only for the bottom-most frame). A debugger can implement a Jump command (aka Set Next Statement) by writing to this attribute. | 

##### 3.2.13.2.3. Frame object methods[¶](#frame-object-methods)

Frame objects support one method:

- 
frame.clear()[¶](#frame.clear)
- This method clears all references to - [local variables](executionmodel.html#naming)held by the frame. Also, if the frame belonged to a- [generator](../glossary.html#term-generator), the generator is finalized. This helps break reference cycles involving frame objects (for example when catching an- [exception](../library/exceptions.html#bltin-exceptions)and storing its- [traceback](#traceback-objects)for later use).- `RuntimeError`- Added in version 3.4. - Changed in version 3.13: Attempting to clear a suspended frame raises - `RuntimeError`

#### 3.2.13.3. Traceback objects[¶](#traceback-objects)

Traceback objects represent the stack trace of an [exception](../tutorial/errors.html#tut-errors).
A traceback object
is implicitly created when an exception occurs, and may also be explicitly
created by calling [ types.TracebackType](../library/types.html#types.TracebackType).

Changed in version 3.7: Traceback objects can now be explicitly instantiated from Python code.

For implicitly created tracebacks, when the search for an exception handler
unwinds the execution stack, at each unwound level a traceback object is
inserted in front of the current traceback.  When an exception handler is
entered, the stack trace is made available to the program. (See section
[The try statement](compound_stmts.html#try).) It is accessible as the third item of the
tuple returned by [ sys.exc_info()](../library/sys.html#sys.exc_info), and as the

[attribute of the caught exception.](../library/exceptions.html#BaseException.__traceback__)

`__traceback__`When the program contains no suitable
handler, the stack trace is written (nicely formatted) to the standard error
stream; if the interpreter is interactive, it is also made available to the user
as [ sys.last_traceback](../library/sys.html#sys.last_traceback).

For explicitly created tracebacks, it is up to the creator of the traceback
to determine how the [ tb_next](#traceback.tb_next) attributes should be linked to
form a full stack trace.

Special read-only attributes:

| 
 | Points to the execution  Accessing this attribute raises an
 | 
| 
 | Gives the line number where the exception occurred | 
| 
 | Indicates the “precise instruction”. | 

The line number and last instruction in the traceback may differ from the
line number of its [frame object](#frame-objects) if the exception
occurred in a
[ try](compound_stmts.html#try) statement with no matching except clause or with a

[clause.](compound_stmts.html#finally)

`finally`- 
traceback.tb_next[¶](#traceback.tb_next)
- The special writable attribute - `tb_next`is the next level in the stack trace (towards the frame where the exception occurred), or- `None`if there is no next level.- Changed in version 3.7: This attribute is now writable 

#### 3.2.13.4. Slice objects[¶](#slice-objects)

Slice objects are used to represent slices for
[ __getitem__()](#object.__getitem__)
methods.  They are also created by the built-in 

[function.](../library/functions.html#slice)

`slice()`Special read-only attributes: [ start](../library/functions.html#slice.start) is the lower bound;

[is the upper bound;](../library/functions.html#slice.stop)

`stop`[is the step value; each is](../library/functions.html#slice.step)

`step``None` if omitted.  These attributes can have any type.Slice objects support one method:

- 
slice.indices(*self*,*length*)[¶](#slice.indices)
- This method takes a single integer argument - *length*and computes information about the slice that the slice object would describe if applied to a sequence of- *length*items. It returns a tuple of three integers; respectively these are the- *start*and- *stop*indices and the- *step*or stride length of the slice. Missing or out-of-bounds indices are handled in a manner consistent with regular slices.

#### 3.2.13.5. Static method objects[¶](#static-method-objects)

Static method objects provide a way of defeating the transformation of function
objects to method objects described above. A static method object is a wrapper
around any other object, usually a user-defined method object. When a static
method object is retrieved from a class or a class instance, the object actually
returned is the wrapped object, which is not subject to any further
transformation. Static method objects are also callable. Static method
objects are created by the built-in [ staticmethod()](../library/functions.html#staticmethod) constructor.

#### 3.2.13.6. Class method objects[¶](#class-method-objects)

A class method object, like a static method object, is a wrapper around another
object that alters the way in which that object is retrieved from classes and
class instances. The behaviour of class method objects upon such retrieval is
described above, under [“instance methods”](#instance-methods). Class method objects are created
by the built-in [ classmethod()](../library/functions.html#classmethod) constructor.

## 3.3. Special method names[¶](#special-method-names)

A class can implement certain operations that are invoked by special syntax
(such as arithmetic operations or subscripting and slicing) by defining methods
with special names. This is Python’s approach to *operator overloading*,
allowing classes to define their own behavior with respect to language
operators.  For instance, if a class defines a method named
[ __getitem__()](#object.__getitem__),
and 

`x` is an instance of this class, then `x[i]` is roughly equivalent
to `type(x).__getitem__(x, i)`.  Except where mentioned, attempts to execute an
operation raise an exception when no appropriate method is defined (typically
[or](../library/exceptions.html#AttributeError)

`AttributeError`[).](../library/exceptions.html#TypeError)

`TypeError`Setting a special method to `None` indicates that the corresponding
operation is not available.  For example, if a class sets
[ __iter__()](#object.__iter__) to 

`None`, the class is not iterable, so calling
[on its instances will raise a](../library/functions.html#iter)

`iter()`[(without falling back to](../library/exceptions.html#TypeError)

`TypeError`[).](#object.__getitem__)

`__getitem__()`[[2]](#id20)

When implementing a class that emulates any built-in type, it is important that
the emulation only be implemented to the degree that it makes sense for the
object being modelled.  For example, some sequences may work well with retrieval
of individual elements, but extracting a slice may not make sense.
(One example of this is the [NodeList](../library/xml.dom.html#dom-nodelist-objects) interface
in the W3C’s Document Object Model.)

### 3.3.1. Basic customization[¶](#basic-customization)

- 
object.__new__(*cls*[,*...*])[¶](#object.__new__)
- Called to create a new instance of class - *cls*.- `__new__()`is a static method (special-cased so you need not declare it as such) that takes the class of which an instance was requested as its first argument. The remaining arguments are those passed to the object constructor expression (the call to the class). The return value of- `__new__()`should be the new object instance (usually an instance of- *cls*).- Typical implementations create a new instance of the class by invoking the superclass’s - `__new__()`method using- `super().__new__(cls[, ...])`with appropriate arguments and then modifying the newly created instance as necessary before returning it.- If - `__new__()`is invoked during object construction and it returns an instance of- *cls*, then the new instance’s- `__init__()`- `__init__(self[, ...])`, where- *self*is the new instance and the remaining arguments are the same as were passed to the object constructor.- If - `__new__()`does not return an instance of- *cls*, then the new instance’s- `__init__()`- `__new__()`is intended mainly to allow subclasses of immutable types (like int, str, or tuple) to customize instance creation. It is also commonly overridden in custom metaclasses in order to customize class creation.

- 
object.__init__(*self*[,*...*])[¶](#object.__init__)
- Called after the instance has been created (by - `__new__()`- `__init__()`method, the derived class’s- `__init__()`method, if any, must explicitly call it to ensure proper initialization of the base class part of the instance; for example:- `super().__init__([args...])`.- Because - `__new__()`- `__init__()`work together in constructing objects (- `__new__()`to create it, and- `__init__()`to customize it), no non-- `None`value may be returned by- `__init__()`; doing so will cause a- `TypeError`

- 
object.__del__(*self*)[¶](#object.__del__)
- Called when the instance is about to be destroyed. This is also called a finalizer or (improperly) a destructor. If a base class has a - `__del__()`method, the derived class’s- `__del__()`method, if any, must explicitly call it to ensure proper deletion of the base class part of the instance.- It is possible (though not recommended!) for the - `__del__()`method to postpone destruction of the instance by creating a new reference to it. This is called object- *resurrection*. It is implementation-dependent whether- `__del__()`is called a second time when a resurrected object is about to be destroyed; the current- [CPython](../glossary.html#term-CPython)implementation only calls it once.- It is not guaranteed that - `__del__()`methods are called for objects that still exist when the interpreter exits.- `weakref.finalize`- Note - `del x`doesn’t directly call- `x.__del__()`— the former decrements the reference count for- `x`by one, and the latter is only called when- `x`’s reference count reaches zero.- **CPython implementation detail:**It is possible for a reference cycle to prevent the reference count of an object from going to zero. In this case, the cycle will be later detected and deleted by the- [cyclic garbage collector](../glossary.html#term-garbage-collection). A common cause of reference cycles is when an exception has been caught in a local variable. The frame’s locals then reference the exception, which references its own traceback, which references the locals of all frames caught in the traceback.- See also - Documentation for the - `gc`- Warning - Due to the precarious circumstances under which - `__del__()`methods are invoked, exceptions that occur during their execution are ignored, and a warning is printed to- `sys.stderr`instead. In particular:- `__del__()`can be invoked when arbitrary code is being executed, including from any arbitrary thread. If- `__del__()`needs to take a lock or invoke any other blocking resource, it may deadlock as the resource may already be taken by the code that gets interrupted to execute- `__del__()`.
- `__del__()`can be executed during interpreter shutdown. As a consequence, the global variables it needs to access (including other modules) may already have been deleted or set to- `None`. Python guarantees that globals whose name begins with a single underscore are deleted from their module before other globals are deleted; if no other references to such globals exist, this may help in assuring that imported modules are still available at the time when the- `__del__()`method is called.
 

- 
object.__repr__(*self*)[¶](#object.__repr__)
- Called by the - `repr()`- `<...some useful description...>`should be returned. The return value must be a string object. If a class defines- `__repr__()`but not- `__str__()`- `__repr__()`is also used when an “informal” string representation of instances of that class is required.- This is typically used for debugging, so it is important that the representation is information-rich and unambiguous. A default implementation is provided by the - `object`

- 
object.__str__(*self*)[¶](#object.__str__)
- Called by - `str(object)`- `__format__()`- `print()`- [str](../library/stdtypes.html#textseq)object.- This method differs from - `object.__repr__()`- `__str__()`return a valid Python expression: a more convenient or concise representation can be used.- The default implementation defined by the built-in type - `object`- `object.__repr__()`

- 
object.__bytes__(*self*)[¶](#object.__bytes__)
- Called by - [bytes](../library/functions.html#func-bytes)to compute a byte-string representation of an object. This should return a- `bytes`- `object`

- 
object.__format__(*self*,*format_spec*)[¶](#object.__format__)
- Called by the - `format()`- [formatted string literals](lexical_analysis.html#f-strings)and the- `str.format()`- *format_spec*argument is a string that contains a description of the formatting options desired. The interpretation of the- *format_spec*argument is up to the type implementing- `__format__()`, however most classes will either delegate formatting to one of the built-in types, or use a similar formatting option syntax.- See - [Format specification mini-language](../library/string.html#formatspec)for a description of the standard formatting syntax.- The return value must be a string object. - The default implementation by the - `object`- *format_spec*string. It delegates to- `__str__()`- Changed in version 3.4: The __format__ method of - `object`itself raises a- `TypeError`- Changed in version 3.7: - `object.__format__(x, '')`is now equivalent to- `str(x)`rather than- `format(str(x), '')`.

- 
object.__lt__(*self*,*other*)[¶](#object.__lt__)
- 
object.__le__(*self*,*other*)[¶](#object.__le__)
- 
object.__eq__(*self*,*other*)[¶](#object.__eq__)
- 
object.__ne__(*self*,*other*)[¶](#object.__ne__)
- 
object.__gt__(*self*,*other*)[¶](#object.__gt__)
- 
object.__ge__(*self*,*other*)[¶](#object.__ge__)
- These are the so-called “rich comparison” methods. The correspondence between operator symbols and method names is as follows: - `x<y`calls- `x.__lt__(y)`,- `x<=y`calls- `x.__le__(y)`,- `x==y`calls- `x.__eq__(y)`,- `x!=y`calls- `x.__ne__(y)`,- `x>y`calls- `x.__gt__(y)`, and- `x>=y`calls- `x.__ge__(y)`.- A rich comparison method may return the singleton - `NotImplemented`- `False`and- `True`are returned for a successful comparison. However, these methods can return any value, so if the comparison operator is used in a Boolean context (e.g., in the condition of an- `if`statement), Python will call- `bool()`- By default, - `object`implements- `__eq__()`by using- `is`, returning- `NotImplemented`- `True if x is y else NotImplemented`. For- `__ne__()`, by default it delegates to- `__eq__()`and inverts the result unless it is- `NotImplemented`. There are no other implied relationships among the comparison operators or default implementations; for example, the truth of- `(x<y or x==y)`does not imply- `x<=y`. To automatically generate ordering operations from a single root operation, see- `functools.total_ordering()`- By default, the - `object`- [Value comparisons](expressions.html#expressions-value-comparisons): equality compares according to object identity, and order comparisons raise- `TypeError`- `NotImplemented`- See the paragraph on - `__hash__()`- [hashable](../glossary.html#term-hashable)objects which support custom comparison operations and are usable as dictionary keys.- There are no swapped-argument versions of these methods (to be used when the left argument does not support the operation but the right argument does); rather, - `__lt__()`and- `__gt__()`are each other’s reflection,- `__le__()`and- `__ge__()`are each other’s reflection, and- `__eq__()`and- `__ne__()`are their own reflection. If the operands are of different types, and the right operand’s type is a direct or indirect subclass of the left operand’s type, the reflected method of the right operand has priority, otherwise the left operand’s method has priority. Virtual subclassing is not considered.- When no appropriate method returns any value other than - `NotImplemented`- `==`and- `!=`operators will fall back to- `is`and- `is not`, respectively.

- 
object.__hash__(*self*)[¶](#object.__hash__)
- Called by built-in function - `hash()`- `set`- `frozenset`- `dict`- `__hash__()`method should return an integer. The only required property is that objects which compare equal have the same hash value; it is advised to mix together the hash values of the components of the object that also play a part in comparison of objects by packing them into a tuple and hashing the tuple. Example:- def __hash__(self): return hash((self.name, self.nick, self.color)) - Note - `hash()`- `__hash__()`method to the size of a- `Py_ssize_t`- `__hash__()`must interoperate on builds of different bit sizes, be sure to check the width on all supported builds. An easy way to do this is with- `python -c "import sys; print(sys.hash_info.width)"`.- If a class does not define an - `__eq__()`- `__hash__()`operation either; if it defines- `__eq__()`but not- `__hash__()`, its instances will not be usable as items in hashable collections. If a class defines mutable objects and implements an- `__eq__()`method, it should not implement- `__hash__()`, since the implementation of- [hashable](../glossary.html#term-hashable)collections requires that a key’s hash value is immutable (if the object’s hash value changes, it will be in the wrong hash bucket).- User-defined classes have - `__eq__()`- `__hash__()`methods by default (inherited from the- `object`- `x.__hash__()`returns an appropriate value such that- `x == y`implies both that- `x is y`and- `hash(x) == hash(y)`.- A class that overrides - `__eq__()`- `__hash__()`will have its- `__hash__()`implicitly set to- `None`. When the- `__hash__()`method of a class is- `None`, instances of the class will raise an appropriate- `TypeError`- `isinstance(obj, collections.abc.Hashable)`.- If a class that overrides - `__eq__()`- `__hash__()`from a parent class, the interpreter must be told this explicitly by setting- `__hash__ = <ParentClass>.__hash__`.- If a class that does not override - `__eq__()`- `__hash__ = None`in the class definition. A class which defines its own- `__hash__()`that explicitly raises a- `TypeError`- `isinstance(obj, collections.abc.Hashable)`call.- Note - By default, the - `__hash__()`values of str and bytes objects are “salted” with an unpredictable random value. Although they remain constant within an individual Python process, they are not predictable between repeated invocations of Python.- This is intended to provide protection against a denial-of-service caused by carefully chosen inputs that exploit the worst case performance of a dict insertion, - *O*(- *n*- 2) complexity. See- [https://ocert.org/advisories/ocert-2011-003.html](https://ocert.org/advisories/ocert-2011-003.html)for details.- Changing hash values affects the iteration order of sets. Python has never made guarantees about this ordering (and it typically varies between 32-bit and 64-bit builds). - See also - `PYTHONHASHSEED`- Changed in version 3.3: Hash randomization is enabled by default. 

- 
object.__bool__(*self*)[¶](#object.__bool__)
- Called to implement truth value testing and the built-in operation - `bool()`; should return- `False`or- `True`. When this method is not defined,- `__len__()`- `__len__()`nor- `__bool__()`(which is true of the- `object`

### 3.3.2. Customizing attribute access[¶](#customizing-attribute-access)

The following methods can be defined to customize the meaning of attribute
access (use of, assignment to, or deletion of `x.name`) for class instances.

- 
object.__getattr__(*self*,*name*)[¶](#object.__getattr__)
- Called when the default attribute access fails with an - `AttributeError`- `__getattribute__()`- `AttributeError`because- *name*is not an instance attribute or an attribute in the class tree for- `self`; or- `__get__()`- *name*property raises- `AttributeError`). This method should either return the (computed) attribute value or raise an- `AttributeError`exception. The- `object`- Note that if the attribute is found through the normal mechanism, - `__getattr__()`is not called. (This is an intentional asymmetry between- `__getattr__()`and- `__setattr__()`- `__getattr__()`would have no way to access other attributes of the instance. Note that at least for instance variables, you can take total control by not inserting any values in the instance attribute dictionary (but instead inserting them in another object). See the- `__getattribute__()`

- 
object.__getattribute__(*self*,*name*)[¶](#object.__getattribute__)
- Called unconditionally to implement attribute accesses for instances of the class. If the class also defines - `__getattr__()`- `__getattribute__()`either calls it explicitly or raises an- `AttributeError`- `AttributeError`exception. In order to avoid infinite recursion in this method, its implementation should always call the base class method with the same name to access any attributes it needs, for example,- `object.__getattribute__(self, name)`.- Note - This method may still be bypassed when looking up special methods as the result of implicit invocation via language syntax or - [built-in functions](#builtin-functions). See- [Special method lookup](#special-lookup).- For certain sensitive attribute accesses, raises an - [auditing event](../library/sys.html#auditing)- `object.__getattr__`with arguments- `obj`and- `name`.

- 
object.__setattr__(*self*,*name*,*value*)[¶](#object.__setattr__)
- Called when an attribute assignment is attempted. This is called instead of the normal mechanism (i.e. store the value in the instance dictionary). - *name*is the attribute name,- *value*is the value to be assigned to it.- If - `__setattr__()`wants to assign to an instance attribute, it should call the base class method with the same name, for example,- `object.__setattr__(self, name, value)`.- For certain sensitive attribute assignments, raises an - [auditing event](../library/sys.html#auditing)- `object.__setattr__`with arguments- `obj`,- `name`,- `value`.

- 
object.__delattr__(*self*,*name*)[¶](#object.__delattr__)
- Like - `__setattr__()`- `del obj.name`is meaningful for the object.- For certain sensitive attribute deletions, raises an - [auditing event](../library/sys.html#auditing)- `object.__delattr__`with arguments- `obj`and- `name`.

- 
object.__dir__(*self*)[¶](#object.__dir__)
- Called when - `dir()`- `dir()`converts the returned iterable to a list and sorts it.

#### 3.3.2.1. Customizing module attribute access[¶](#customizing-module-attribute-access)

Special names `__getattr__` and `__dir__` can be also used to customize
access to module attributes. The `__getattr__` function at the module level
should accept one argument which is the name of an attribute and return the
computed value or raise an [ AttributeError](../library/exceptions.html#AttributeError). If an attribute is
not found on a module object through the normal lookup, i.e.

[, then](#object.__getattribute__)

`object.__getattribute__()``__getattr__` is searched in
the module `__dict__` before raising an `AttributeError`. If found,
it is called with the attribute name and the result is returned.The `__dir__` function should accept no arguments, and return an iterable of
strings that represents the names accessible on module. If present, this
function overrides the standard [ dir()](../library/functions.html#dir) search on a module.

- 
module.__class__[¶](#module.__class__)

For a more fine grained customization of the module behavior (setting
attributes, properties, etc.), one can set the `__class__` attribute of
a module object to a subclass of [ types.ModuleType](../library/types.html#types.ModuleType). For example:

```
import sys
from types import ModuleType
class VerboseModule(ModuleType):
    def __repr__(self):
        return f'Verbose {self.__name__}'
    def __setattr__(self, attr, value):
        print(f'Setting {attr}...')
        super().__setattr__(attr, value)
sys.modules[__name__].__class__ = VerboseModule
```
Note

Defining module `__getattr__` and setting module `__class__` only
affect lookups made using the attribute access syntax – directly accessing
the module globals (whether by code within the module, or via a reference
to the module’s globals dictionary) is unaffected.

Changed in version 3.5: `__class__` module attribute is now writable.

Added in version 3.7: `__getattr__` and `__dir__` module attributes.

See also

- **PEP 562**
- Describes the - `__getattr__`and- `__dir__`functions on modules.

#### 3.3.2.2. Implementing Descriptors[¶](#implementing-descriptors)

The following methods only apply when an instance of the class containing the
method (a so-called *descriptor* class) appears in an *owner* class (the
descriptor must be in either the owner’s class dictionary or in the class
dictionary for one of its parents).  In the examples below, “the attribute”
refers to the attribute whose name is the key of the property in the owner
class’ [ __dict__](#object.__dict__).  The 

[class itself does not implement any of these protocols.](../library/functions.html#object)

`object`- 
object.__get__(*self*,*instance*,*owner=None*)[¶](#object.__get__)
- Called to get the attribute of the owner class (class attribute access) or of an instance of that class (instance attribute access). The optional - *owner*argument is the owner class, while- *instance*is the instance that the attribute was accessed through, or- `None`when the attribute is accessed through the- *owner*.- This method should return the computed attribute value or raise an - `AttributeError`- **PEP 252**- `__get__()`is callable with one or two arguments. Python’s own built-in descriptors support this specification; however, it is likely that some third-party tools have descriptors that require both arguments. Python’s own- `__getattribute__()`

- 
object.__set__(*self*,*instance*,*value*)[¶](#object.__set__)
- Called to set the attribute on an instance - *instance*of the owner class to a new value,- *value*.- Note, adding - `__set__()`or- `__delete__()`- [Invoking Descriptors](#descriptor-invocation)for more details.

- 
object.__delete__(*self*,*instance*)[¶](#object.__delete__)
- Called to delete the attribute on an instance - *instance*of the owner class.

Instances of descriptors may also have the `__objclass__` attribute
present:

- 
object.__objclass__[¶](#object.__objclass__)
- The attribute - `__objclass__`is interpreted by the- `inspect`

#### 3.3.2.3. Invoking Descriptors[¶](#invoking-descriptors)

In general, a descriptor is an object attribute with “binding behavior”, one
whose attribute access has been overridden by methods in the descriptor
protocol:  [ __get__()](#object.__get__), 

[, and](#object.__set__)

`__set__()`[. If any of those methods are defined for an object, it is said to be a descriptor.](#object.__delete__)

`__delete__()`The default behavior for attribute access is to get, set, or delete the
attribute from an object’s dictionary. For instance, `a.x` has a lookup chain
starting with `a.__dict__['x']`, then `type(a).__dict__['x']`, and
continuing through the base classes of `type(a)` excluding metaclasses.

However, if the looked-up value is an object defining one of the descriptor methods, then Python may override the default behavior and invoke the descriptor method instead. Where this occurs in the precedence chain depends on which descriptor methods were defined and how they were called.

The starting point for descriptor invocation is a binding, `a.x`. How the
arguments are assembled depends on `a`:

- Direct Call
- The simplest and least common call is when user code directly invokes a descriptor method: - `x.__get__(a)`.
- Instance Binding
- If binding to an object instance, - `a.x`is transformed into the call:- `type(a).__dict__['x'].__get__(a, type(a))`.
- Class Binding
- If binding to a class, - `A.x`is transformed into the call:- `A.__dict__['x'].__get__(None, A)`.
- Super Binding
- A dotted lookup such as - `super(A, a).x`searches- `a.__class__.__mro__`for a base class- `B`following- `A`and then returns- `B.__dict__['x'].__get__(a, A)`. If not a descriptor,- `x`is returned unchanged.

For instance bindings, the precedence of descriptor invocation depends on
which descriptor methods are defined.  A descriptor can define any combination
of [ __get__()](#object.__get__), 

[and](#object.__set__)

`__set__()`[. If it does not define](#object.__delete__)

`__delete__()``__get__()`, then accessing the attribute will return the descriptor
object itself unless there is a value in the object’s instance dictionary.  If
the descriptor defines `__set__()` and/or `__delete__()`, it is a data
descriptor; if it defines neither, it is a non-data descriptor.  Normally, data
descriptors define both `__get__()` and `__set__()`, while non-data
descriptors have just the `__get__()` method.  Data descriptors with
`__get__()` and `__set__()` (and/or `__delete__()`) defined
always override a redefinition in an
instance dictionary.  In contrast, non-data descriptors can be overridden by
instances.Python methods (including those decorated with
[ @staticmethod](../library/functions.html#staticmethod) and 

[) are implemented as non-data descriptors. Accordingly, instances can redefine and override methods. This allows individual instances to acquire behaviors that differ from other instances of the same class.](../library/functions.html#classmethod)

`@classmethod`The [ property()](../library/functions.html#property) function is implemented as a data descriptor. Accordingly,
instances cannot override the behavior of a property.

#### 3.3.2.4. __slots__[¶](#slots)

*__slots__* allow us to explicitly declare data members (like
properties) and deny the creation of [ __dict__](#object.__dict__) and 

*__weakref__*(unless explicitly declared in

*__slots__*or available in a parent.)

The space saved over using [ __dict__](#object.__dict__) can be significant.
Attribute lookup speed can be significantly improved as well.

- 
object.__slots__[¶](#object.__slots__)
- This class variable can be assigned a string, iterable, or sequence of strings with variable names used by instances. - *__slots__*reserves space for the declared variables and prevents the automatic creation of- `__dict__`- *__weakref__*for each instance.

Notes on using *__slots__*:

- When inheriting from a class without - *__slots__*, the- `__dict__`- *__weakref__*attribute of the instances will always be accessible.
- Without a - `__dict__`- *__slots__*definition. Attempts to assign to an unlisted variable name raises- `AttributeError`- `'__dict__'`to the sequence of strings in the- *__slots__*declaration.
- Without a - *__weakref__*variable for each instance, classes defining- *__slots__*do not support- `weak references`- `'__weakref__'`to the sequence of strings in the- *__slots__*declaration.
- *__slots__*are implemented at the class level by creating- [descriptors](#descriptors)for each variable name. As a result, class attributes cannot be used to set default values for instance variables defined by- *__slots__*; otherwise, the class attribute would overwrite the descriptor assignment.
- The action of a - *__slots__*declaration is not limited to the class where it is defined.- *__slots__*declared in parents are available in child classes. However, instances of a child subclass will get a- `__dict__`- *__weakref__*unless the subclass also defines- *__slots__*(which should only contain names of any- *additional*slots).
- If a class defines a slot also defined in a base class, the instance variable defined by the base class slot is inaccessible (except by retrieving its descriptor directly from the base class). This renders the meaning of the program undefined. In the future, a check may be added to prevent this. 
- `TypeError`- *__slots__*are defined for a class derived from a- `"variable-length" built-in type`- `int`- `bytes`- `tuple`
- Any non-string - [iterable](../glossary.html#term-iterable)may be assigned to- *__slots__*.
- If a - `dictionary`- *__slots__*, the dictionary keys will be used as the slot names. The values of the dictionary can be used to provide per-attribute docstrings that will be recognised by- `inspect.getdoc()`- `help()`
- `__class__`- *__slots__*.
- [Multiple inheritance](../tutorial/classes.html#tut-multiple)with multiple slotted parent classes can be used, but only one parent is allowed to have attributes created by slots (the other bases must have empty slot layouts) - violations raise- `TypeError`
- If an - [iterator](../glossary.html#term-iterator)is used for- *__slots__*then a- [descriptor](../glossary.html#term-descriptor)is created for each of the iterator’s values. However, the- *__slots__*attribute will be an empty iterator.

### 3.3.3. Customizing class creation[¶](#customizing-class-creation)

Whenever a class inherits from another class, [ __init_subclass__()](#object.__init_subclass__) is
called on the parent class. This way, it is possible to write classes which
change the behavior of subclasses. This is closely related to class
decorators, but where class decorators only affect the specific class they’re
applied to, 

`__init_subclass__` solely applies to future subclasses of the
class defining the method.- 
*classmethod*object.__init_subclass__(*cls*)[¶](#object.__init_subclass__)
- This method is called whenever the containing class is subclassed. - *cls*is then the new subclass. If defined as a normal instance method, this method is implicitly converted to a class method.- Keyword arguments which are given to a new class are passed to the parent class’s - `__init_subclass__`. For compatibility with other classes using- `__init_subclass__`, one should take out the needed keyword arguments and pass the others over to the base class, as in:- class Philosopher: def __init_subclass__(cls, /, default_name, **kwargs): super().__init_subclass__(**kwargs) cls.default_name = default_name class AustralianPhilosopher(Philosopher, default_name="Bruce"): pass - The default implementation - `object.__init_subclass__`does nothing, but raises an error if it is called with any arguments.- Note - The metaclass hint - `metaclass`is consumed by the rest of the type machinery, and is never passed to- `__init_subclass__`implementations. The actual metaclass (rather than the explicit hint) can be accessed as- `type(cls)`.- Added in version 3.6. 

When a class is created, `type.__new__()` scans the class variables
and makes callbacks to those with a [ __set_name__()](#object.__set_name__) hook.

- 
object.__set_name__(*self*,*owner*,*name*)[¶](#object.__set_name__)
- Automatically called at the time the owning class - *owner*is created. The object has been assigned to- *name*in that class:- class A: x = C() # Automatically calls: x.__set_name__(A, 'x') - If the class variable is assigned after the class is created, - `__set_name__()`will not be called automatically. If needed,- `__set_name__()`can be called directly:- class A: pass c = C() A.x = c # The hook is not called c.__set_name__(A, 'x') # Manually invoke the hook - See - [Creating the class object](#class-object-creation)for more details.- Added in version 3.6. 

#### 3.3.3.1. Metaclasses[¶](#metaclasses)

By default, classes are constructed using [ type()](../library/functions.html#type). The class body is
executed in a new namespace and the class name is bound locally to the
result of 

`type(name, bases, namespace)`.The class creation process can be customized by passing the `metaclass`
keyword argument in the class definition line, or by inheriting from an
existing class that included such an argument. In the following example,
both `MyClass` and `MySubclass` are instances of `Meta`:

```
class Meta(type):
    pass
class MyClass(metaclass=Meta):
    pass
class MySubclass(MyClass):
    pass
```
Any other keyword arguments that are specified in the class definition are passed through to all metaclass operations described below.

When a class definition is executed, the following steps occur:

- MRO entries are resolved; 
- the appropriate metaclass is determined; 
- the class namespace is prepared; 
- the class body is executed; 
- the class object is created. 

#### 3.3.3.2. Resolving MRO entries[¶](#resolving-mro-entries)

- 
object.__mro_entries__(*self*,*bases*)[¶](#object.__mro_entries__)
- If a base that appears in a class definition is not an instance of - `type`- `__mro_entries__()`method is searched on the base. If an- `__mro_entries__()`method is found, the base is substituted with the result of a call to- `__mro_entries__()`when creating the class. The method is called with the original bases tuple passed to the- *bases*parameter, and must return a tuple of classes that will be used instead of the base. The returned tuple may be empty: in these cases, the original base is ignored.

See also

- `types.resolve_bases()`
- Dynamically resolve bases that are not instances of - `type`
- `types.get_original_bases()`
- Retrieve a class’s “original bases” prior to modifications by - `__mro_entries__()`
- **PEP 560**
- Core support for typing module and generic types. 

#### 3.3.3.3. Determining the appropriate metaclass[¶](#determining-the-appropriate-metaclass)

The appropriate metaclass for a class definition is determined as follows:

- if no bases and no explicit metaclass are given, then - `type()`
- if an explicit metaclass is given and it is - *not*an instance of- `type()`
- if an instance of - `type()`

The most derived metaclass is selected from the explicitly specified
metaclass (if any) and the metaclasses (i.e. `type(cls)`) of all specified
base classes. The most derived metaclass is one which is a subtype of *all*
of these candidate metaclasses. If none of the candidate metaclasses meets
that criterion, then the class definition will fail with `TypeError`.

#### 3.3.3.4. Preparing the class namespace[¶](#preparing-the-class-namespace)

Once the appropriate metaclass has been identified, then the class namespace
is prepared. If the metaclass has a `__prepare__` attribute, it is called
as `namespace = metaclass.__prepare__(name, bases, **kwds)` (where the
additional keyword arguments, if any, come from the class definition). The
`__prepare__` method should be implemented as a
[ classmethod](../library/functions.html#classmethod). The
namespace returned by 

`__prepare__` is passed in to `__new__`, but when
the final class object is created the namespace is copied into a new `dict`.If the metaclass has no `__prepare__` attribute, then the class namespace
is initialised as an empty ordered mapping.

See also

- **PEP 3115**
- Introduced the - `__prepare__`namespace hook

#### 3.3.3.5. Executing the class body[¶](#executing-the-class-body)

The class body is executed (approximately) as
`exec(body, globals(), namespace)`. The key difference from a normal
call to [ exec()](../library/functions.html#exec) is that lexical scoping allows the class body (including
any methods) to reference names from the current and outer scopes when the
class definition occurs inside a function.

However, even when the class definition occurs inside the function, methods
defined inside the class still cannot see names defined at the class scope.
Class variables must be accessed through the first parameter of instance or
class methods, or through the implicit lexically scoped `__class__` reference
described in the next section.

#### 3.3.3.6. Creating the class object[¶](#creating-the-class-object)

Once the class namespace has been populated by executing the class body,
the class object is created by calling
`metaclass(name, bases, namespace, **kwds)` (the additional keywords
passed here are the same as those passed to `__prepare__`).

This class object is the one that will be referenced by the zero-argument
form of [ super()](../library/functions.html#super). 

`__class__` is an implicit closure reference
created by the compiler if any methods in a class body refer to either
`__class__` or `super`. This allows the zero argument form of
`super()` to correctly identify the class being defined based on
lexical scoping, while the class or instance that was used to make the
current call is identified based on the first argument passed to the method.**CPython implementation detail:** In CPython 3.6 and later, the `__class__` cell is passed to the metaclass
as a `__classcell__` entry in the class namespace. If present, this must
be propagated up to the `type.__new__` call in order for the class to be
initialised correctly.
Failing to do so will result in a [ RuntimeError](../library/exceptions.html#RuntimeError) in Python 3.8.

When using the default metaclass [ type](../library/functions.html#type), or any metaclass that ultimately
calls 

`type.__new__`, the following additional customization steps are
invoked after creating the class object:- The - `type.__new__`method collects all of the attributes in the class namespace that define a- `__set_name__()`
- Those - `__set_name__`methods are called with the class being defined and the assigned name of that particular attribute;
- The - `__init_subclass__()`

After the class object is created, it is passed to the class decorators included in the class definition (if any) and the resulting object is bound in the local namespace as the defined class.

When a new class is created by `type.__new__`, the object provided as the
namespace parameter is copied to a new ordered mapping and the original
object is discarded. The new copy is wrapped in a read-only proxy, which
becomes the [ __dict__](#type.__dict__) attribute of the class object.

See also

- **PEP 3135**
- Describes the implicit - `__class__`closure reference

#### 3.3.3.7. Uses for metaclasses[¶](#uses-for-metaclasses)

The potential uses for metaclasses are boundless. Some ideas that have been explored include enum, logging, interface checking, automatic delegation, automatic property creation, proxies, frameworks, and automatic resource locking/synchronization.

### 3.3.4. Customizing instance and subclass checks[¶](#customizing-instance-and-subclass-checks)

The following methods are used to override the default behavior of the
[ isinstance()](../library/functions.html#isinstance) and 

[built-in functions.](../library/functions.html#issubclass)

`issubclass()`In particular, the metaclass [ abc.ABCMeta](../library/abc.html#abc.ABCMeta) implements these methods in
order to allow the addition of Abstract Base Classes (ABCs) as “virtual base
classes” to any class or type (including built-in types), including other
ABCs.

- 
type.__instancecheck__(*self*,*instance*)[¶](#type.__instancecheck__)
- Return true if - *instance*should be considered a (direct or indirect) instance of- *class*. If defined, called to implement- `isinstance(instance, class)`.

- 
type.__subclasscheck__(*self*,*subclass*)[¶](#type.__subclasscheck__)
- Return true if - *subclass*should be considered a (direct or indirect) subclass of- *class*. If defined, called to implement- `issubclass(subclass, class)`.

Note that these methods are looked up on the type (metaclass) of a class. They cannot be defined as class methods in the actual class. This is consistent with the lookup of special methods that are called on instances, only in this case the instance is itself a class.

See also

- **PEP 3119**
- Includes the specification for customizing - `isinstance()`- `issubclass()`- `__instancecheck__()`- `__subclasscheck__()`- `abc`

### 3.3.5. Emulating generic types[¶](#emulating-generic-types)

When using [type annotations](../glossary.html#term-annotation), it is often useful to
*parameterize* a [generic type](../glossary.html#term-generic-type) using Python’s square-brackets notation.
For example, the annotation `list[int]` might be used to signify a
[ list](../library/stdtypes.html#list) in which all the elements are of type 

[.](../library/functions.html#int)

`int`See also

- **PEP 484**
- Introducing Python’s framework for type annotations 
- [Generic Alias Types](../library/stdtypes.html#types-genericalias)
- Documentation for objects representing parameterized generic classes 
- [Generics](../library/typing.html#generics),- [user-defined generics](../library/typing.html#user-defined-generics)and- `typing.Generic`
- Documentation on how to implement generic classes that can be parameterized at runtime and understood by static type-checkers. 

A class can *generally* only be parameterized if it defines the special
class method `__class_getitem__()`.

- 
*classmethod*object.__class_getitem__(*cls*,*key*)[¶](#object.__class_getitem__)
- Return an object representing the specialization of a generic class by type arguments found in - *key*.- When defined on a class, - `__class_getitem__()`is automatically a class method. As such, there is no need for it to be decorated with- `@classmethod`

#### 3.3.5.1. The purpose of *__class_getitem__*[¶](#the-purpose-of-class-getitem)

The purpose of [ __class_getitem__()](#object.__class_getitem__) is to allow runtime
parameterization of standard-library generic classes in order to more easily
apply 

[type hints](../glossary.html#term-type-hint)to these classes.

To implement custom generic classes that can be parameterized at runtime and
understood by static type-checkers, users should either inherit from a standard
library class that already implements [ __class_getitem__()](#object.__class_getitem__), or
inherit from 

[, which has its own implementation of](../library/typing.html#typing.Generic)

`typing.Generic``__class_getitem__()`.Custom implementations of [ __class_getitem__()](#object.__class_getitem__) on classes defined
outside of the standard library may not be understood by third-party
type-checkers such as mypy. Using 

`__class_getitem__()` on any class for
purposes other than type hinting is discouraged.#### 3.3.5.2. *__class_getitem__* versus *__getitem__*[¶](#class-getitem-versus-getitem)

Usually, the [subscription](expressions.html#subscriptions) of an object using square
brackets will call the [ __getitem__()](#object.__getitem__) instance method defined on
the object’s class. However, if the object being subscribed is itself a class,
the class method 

[may be called instead.](#object.__class_getitem__)

`__class_getitem__()``__class_getitem__()` should return a [GenericAlias](../library/stdtypes.html#types-genericalias)object if it is properly defined.

Presented with the [expression](../glossary.html#term-expression) `obj[x]`, the Python interpreter
follows something like the following process to decide whether
[ __getitem__()](#object.__getitem__) or 

[should be called:](#object.__class_getitem__)

`__class_getitem__()````
from inspect import isclass
def subscribe(obj, x):
    """Return the result of the expression 'obj[x]'"""
    class_of_obj = type(obj)
    # If the class of obj defines __getitem__,
    # call class_of_obj.__getitem__(obj, x)
    if hasattr(class_of_obj, '__getitem__'):
        return class_of_obj.__getitem__(obj, x)
    # Else, if obj is a class and defines __class_getitem__,
    # call obj.__class_getitem__(x)
    elif isclass(obj) and hasattr(obj, '__class_getitem__'):
        return obj.__class_getitem__(x)
    # Else, raise an exception
    else:
        raise TypeError(
            f"'{class_of_obj.__name__}' object is not subscriptable"
        )
```
In Python, all classes are themselves instances of other classes. The class of
a class is known as that class’s [metaclass](../glossary.html#term-metaclass), and most classes have the
[ type](../library/functions.html#type) class as their metaclass. 

`type` does not define
[, meaning that expressions such as](#object.__getitem__)

`__getitem__()``list[int]`,
`dict[str, float]` and `tuple[str, bytes]` all result in
[being called:](#object.__class_getitem__)

`__class_getitem__()````
>>> # list has class "type" as its metaclass, like most classes:
>>> type(list)
<class 'type'>
>>> type(dict) == type(list) == type(tuple) == type(str) == type(bytes)
True
>>> # "list[int]" calls "list.__class_getitem__(int)"
>>> list[int]
list[int]
>>> # list.__class_getitem__ returns a GenericAlias object:
>>> type(list[int])
<class 'types.GenericAlias'>
```
However, if a class has a custom metaclass that defines
[ __getitem__()](#object.__getitem__), subscribing the class may result in different
behaviour. An example of this can be found in the 

[module:](../library/enum.html#module-enum)

`enum````
>>> from enum import Enum
>>> class Menu(Enum):
...     """A breakfast menu"""
...     SPAM = 'spam'
...     BACON = 'bacon'
...
>>> # Enum classes have a custom metaclass:
>>> type(Menu)
<class 'enum.EnumMeta'>
>>> # EnumMeta defines __getitem__,
>>> # so __class_getitem__ is not called,
>>> # and the result is not a GenericAlias object:
>>> Menu['SPAM']
<Menu.SPAM: 'spam'>
>>> type(Menu['SPAM'])
<enum 'Menu'>
```
See also

- **PEP 560**
- Introducing - `__class_getitem__()`- [subscription](expressions.html#subscriptions)results in- `__class_getitem__()`being called instead of- `__getitem__()`

### 3.3.6. Emulating callable objects[¶](#emulating-callable-objects)

### 3.3.7. Emulating container types[¶](#emulating-container-types)

The following methods can be defined to implement container objects. None of them
are provided by the [ object](../library/functions.html#object) class itself. Containers usually are

[sequences](../glossary.html#term-sequence)(such as

[or](../library/stdtypes.html#list)

`lists`[) or](../library/stdtypes.html#tuple)

`tuples`[mappings](../glossary.html#term-mapping)(like

[dictionaries](../glossary.html#term-dictionary)), but can represent other containers as well. The first set of methods is used either to emulate a sequence or to emulate a mapping; the difference is that for a sequence, the allowable keys should be the integers

*k*for which

```
0 <= k <
N
```
 where *N*is the length of the sequence, or

[objects, which define a range of items. It is also recommended that mappings provide the methods](../library/functions.html#slice)

`slice``keys()`, `values()`, `items()`, `get()`, `clear()`,
`setdefault()`, `pop()`, `popitem()`, `copy()`, and
`update()` behaving similar to those for Python’s standard [objects. The](../library/stdtypes.html#dict)

`dictionary`[module provides a](../library/collections.abc.html#module-collections.abc)

`collections.abc`

`MutableMapping`[abstract base class](../glossary.html#term-abstract-base-class)to help create those methods from a base set of

[,](#object.__getitem__)

`__getitem__()`[,](#object.__setitem__)

`__setitem__()`[, and](#object.__delitem__)

`__delitem__()``keys()`.Mutable sequences should provide methods
[ append()](../library/stdtypes.html#sequence.append), 

[,](../library/stdtypes.html#sequence.clear)

`clear()`[,](../library/stdtypes.html#sequence.count)

`count()`[,](../library/stdtypes.html#sequence.extend)

`extend()`[,](../library/stdtypes.html#sequence.index)

`index()`[,](../library/stdtypes.html#sequence.insert)

`insert()`[,](../library/stdtypes.html#sequence.pop)

`pop()`[, and](../library/stdtypes.html#sequence.remove)

`remove()`[, like Python standard](../library/stdtypes.html#sequence.reverse)

`reverse()`[objects. Finally, sequence types should implement addition (meaning concatenation) and multiplication (meaning repetition) by defining the methods](../library/stdtypes.html#list)

`list`[,](#object.__add__)

`__add__()`[,](#object.__radd__)

`__radd__()`[,](#object.__iadd__)

`__iadd__()`[,](#object.__mul__)

`__mul__()`[and](#object.__rmul__)

`__rmul__()`[described below; they should not define other numerical operators.](#object.__imul__)

`__imul__()`It is recommended that both mappings and sequences implement the
[ __contains__()](#object.__contains__) method to allow efficient use of the 

`in`
operator; for
mappings, `in` should search the mapping’s keys; for sequences, it should
search through the values.  It is further recommended that both mappings and
sequences implement the [method to allow efficient iteration through the container; for mappings,](#object.__iter__)

`__iter__()``__iter__()` should iterate
through the object’s keys; for sequences, it should iterate through the values.- 
object.__len__(*self*)[¶](#object.__len__)
- Called to implement the built-in function - `len()`- `>=`0. Also, an object that doesn’t define a- `__bool__()`- `__len__()`method returns zero is considered to be false in a Boolean context.- **CPython implementation detail:**In CPython, the length is required to be at most- `sys.maxsize`- `sys.maxsize`some features (such as- `len()`- `OverflowError`- `OverflowError`by truth value testing, an object must define a- `__bool__()`

- 
object.__length_hint__(*self*)[¶](#object.__length_hint__)
- Called to implement - `operator.length_hint()`- `>=`0. The return value may also be- `NotImplemented`- `__length_hint__`method didn’t exist at all. This method is purely an optimization and is never required for correctness.- Added in version 3.4. 

Note

Slicing is done exclusively with the following three methods. A call like

```
a[1:2] = b
```
is translated to

```
a[slice(1, 2, None)] = b
```
and so forth.  Missing slice items are always filled in with `None`.

- 
object.__getitem__(*self*,*key*)[¶](#object.__getitem__)
- Called to implement evaluation of - `self[key]`. For- [sequence](../glossary.html#term-sequence)types, the accepted keys should be integers. Optionally, they may support- `slice`- *key*is of an inappropriate type,- `TypeError`- *key*is a value outside the set of indexes for the sequence (after any special interpretation of negative values),- `IndexError`- [mapping](../glossary.html#term-mapping)types, if- *key*is missing (not in the container),- `KeyError`- Note - `for`- `IndexError`- Note - When - [subscripting](expressions.html#subscriptions)a- *class*, the special class method- `__class_getitem__()`- `__getitem__()`. See- [__class_getitem__ versus __getitem__](#classgetitem-versus-getitem)for more details.

- 
object.__setitem__(*self*,*key*,*value*)[¶](#object.__setitem__)
- Called to implement assignment to - `self[key]`. Same note as for- `__getitem__()`- *key*values as for the- `__getitem__()`method.

- 
object.__delitem__(*self*,*key*)[¶](#object.__delitem__)
- Called to implement deletion of - `self[key]`. Same note as for- `__getitem__()`- *key*values as for the- `__getitem__()`method.

- 
object.__missing__(*self*,*key*)[¶](#object.__missing__)
- Called by - `dict`- `__getitem__()`- `self[key]`for dict subclasses when key is not in the dictionary.

- 
object.__iter__(*self*)[¶](#object.__iter__)
- This method is called when an - [iterator](../glossary.html#term-iterator)is required for a container. This method should return a new iterator object that can iterate over all the objects in the container. For mappings, it should iterate over the keys of the container.

- 
object.__reversed__(*self*)[¶](#object.__reversed__)
- Called (if present) by the - `reversed()`- If the - `__reversed__()`method is not provided, the- `reversed()`- `__len__()`- `__getitem__()`- `__reversed__()`if they can provide an implementation that is more efficient than the one provided by- `reversed()`.

The membership test operators ([ in](expressions.html#in) and 

[) are normally implemented as an iteration through a container. However, container objects can supply the following special method with a more efficient implementation, which also does not require the object be iterable.](expressions.html#not-in)

`not in`- 
object.__contains__(*self*,*item*)[¶](#object.__contains__)
- Called to implement membership test operators. Should return true if - *item*is in- *self*, false otherwise. For mapping objects, this should consider the keys of the mapping rather than the values or the key-item pairs.- For objects that don’t define - `__contains__()`, the membership test first tries iteration via- `__iter__()`- `__getitem__()`- [this section in the language reference](expressions.html#membership-test-details).

### 3.3.8. Emulating numeric types[¶](#emulating-numeric-types)

The following methods can be defined to emulate numeric objects. Methods corresponding to operations that are not supported by the particular kind of number implemented (e.g., bitwise operations for non-integral numbers) should be left undefined.

- 
object.__add__(*self*,*other*)[¶](#object.__add__)
- 
object.__sub__(*self*,*other*)[¶](#object.__sub__)
- 
object.__mul__(*self*,*other*)[¶](#object.__mul__)
- 
object.__matmul__(*self*,*other*)[¶](#object.__matmul__)
- 
object.__truediv__(*self*,*other*)[¶](#object.__truediv__)
- 
object.__floordiv__(*self*,*other*)[¶](#object.__floordiv__)
- 
object.__mod__(*self*,*other*)[¶](#object.__mod__)
- 
object.__divmod__(*self*,*other*)[¶](#object.__divmod__)
- 
object.__pow__(*self*,*other*[,*modulo*])[¶](#object.__pow__)
- 
object.__lshift__(*self*,*other*)[¶](#object.__lshift__)
- 
object.__rshift__(*self*,*other*)[¶](#object.__rshift__)
- 
object.__and__(*self*,*other*)[¶](#object.__and__)
- 
object.__xor__(*self*,*other*)[¶](#object.__xor__)
- 
object.__or__(*self*,*other*)[¶](#object.__or__)
- These methods are called to implement the binary arithmetic operations ( - `+`,- `-`,- `*`,- `@`,- `/`,- `//`,- `%`,- `divmod()`- `pow()`- `**`,- `<<`,- `>>`,- `&`,- `^`,- `|`). For instance, to evaluate the expression- `x + y`, where- *x*is an instance of a class that has an- `__add__()`method,- `type(x).__add__(x, y)`is called. The- `__divmod__()`method should be the equivalent to using- `__floordiv__()`and- `__mod__()`; it should not be related to- `__truediv__()`. Note that- `__pow__()`should be defined to accept an optional third argument if the ternary version of the built-in- `pow()`function is to be supported.- If one of those methods does not support the operation with the supplied arguments, it should return - `NotImplemented`

- 
object.__radd__(*self*,*other*)[¶](#object.__radd__)
- 
object.__rsub__(*self*,*other*)[¶](#object.__rsub__)
- 
object.__rmul__(*self*,*other*)[¶](#object.__rmul__)
- 
object.__rmatmul__(*self*,*other*)[¶](#object.__rmatmul__)
- 
object.__rtruediv__(*self*,*other*)[¶](#object.__rtruediv__)
- 
object.__rfloordiv__(*self*,*other*)[¶](#object.__rfloordiv__)
- 
object.__rmod__(*self*,*other*)[¶](#object.__rmod__)
- 
object.__rdivmod__(*self*,*other*)[¶](#object.__rdivmod__)
- 
object.__rpow__(*self*,*other*[,*modulo*])[¶](#object.__rpow__)
- 
object.__rlshift__(*self*,*other*)[¶](#object.__rlshift__)
- 
object.__rrshift__(*self*,*other*)[¶](#object.__rrshift__)
- 
object.__rand__(*self*,*other*)[¶](#object.__rand__)
- 
object.__rxor__(*self*,*other*)[¶](#object.__rxor__)
- 
object.__ror__(*self*,*other*)[¶](#object.__ror__)
- These methods are called to implement the binary arithmetic operations ( - `+`,- `-`,- `*`,- `@`,- `/`,- `//`,- `%`,- `divmod()`- `pow()`- `**`,- `<<`,- `>>`,- `&`,- `^`,- `|`) with reflected (swapped) operands. These functions are only called if the left operand does not support the corresponding operation- [[3]](#id21)and the operands are of different types.- [[4]](#id22)For instance, to evaluate the expression- `x - y`, where- *y*is an instance of a class that has an- `__rsub__()`method,- `type(y).__rsub__(y, x)`is called if- `type(x).__sub__(x, y)`returns- `NotImplemented`- Note that ternary - `pow()`- `__rpow__()`(the coercion rules would become too complicated).- Note - If the right operand’s type is a subclass of the left operand’s type and that subclass provides a different implementation of the reflected method for the operation, this method will be called before the left operand’s non-reflected method. This behavior allows subclasses to override their ancestors’ operations. 

- 
object.__iadd__(*self*,*other*)[¶](#object.__iadd__)
- 
object.__isub__(*self*,*other*)[¶](#object.__isub__)
- 
object.__imul__(*self*,*other*)[¶](#object.__imul__)
- 
object.__imatmul__(*self*,*other*)[¶](#object.__imatmul__)
- 
object.__itruediv__(*self*,*other*)[¶](#object.__itruediv__)
- 
object.__ifloordiv__(*self*,*other*)[¶](#object.__ifloordiv__)
- 
object.__imod__(*self*,*other*)[¶](#object.__imod__)
- 
object.__ipow__(*self*,*other*[,*modulo*])[¶](#object.__ipow__)
- 
object.__ilshift__(*self*,*other*)[¶](#object.__ilshift__)
- 
object.__irshift__(*self*,*other*)[¶](#object.__irshift__)
- 
object.__iand__(*self*,*other*)[¶](#object.__iand__)
- 
object.__ixor__(*self*,*other*)[¶](#object.__ixor__)
- 
object.__ior__(*self*,*other*)[¶](#object.__ior__)
- These methods are called to implement the augmented arithmetic assignments ( - `+=`,- `-=`,- `*=`,- `@=`,- `/=`,- `//=`,- `%=`,- `**=`,- `<<=`,- `>>=`,- `&=`,- `^=`,- `|=`). These methods should attempt to do the operation in-place (modifying- *self*) and return the result (which could be, but does not have to be,- *self*). If a specific method is not defined, or if that method returns- `NotImplemented`- *x*is an instance of a class with an- `__iadd__()`method,- `x += y`is equivalent to- `x = x.__iadd__(y)`. If- `__iadd__()`does not exist, or if- `x.__iadd__(y)`returns- `NotImplemented`,- `x.__add__(y)`and- `y.__radd__(x)`are considered, as with the evaluation of- `x + y`. In certain situations, augmented assignment can result in unexpected errors (see- [Why does a_tuple[i] += [‘item’] raise an exception when the addition works?](../faq/programming.html#faq-augmented-assignment-tuple-error)), but this behavior is in fact part of the data model.

- 
object.__neg__(*self*)[¶](#object.__neg__)
- 
object.__pos__(*self*)[¶](#object.__pos__)
- 
object.__abs__(*self*)[¶](#object.__abs__)
- 
object.__invert__(*self*)[¶](#object.__invert__)
- Called to implement the unary arithmetic operations ( - `-`,- `+`,- `abs()`- `~`).

- 
object.__complex__(*self*)[¶](#object.__complex__)
- 
object.__int__(*self*)[¶](#object.__int__)
- 
object.__float__(*self*)[¶](#object.__float__)
- Called to implement the built-in functions - `complex()`- `int()`- `float()`

- 
object.__index__(*self*)[¶](#object.__index__)
- Called to implement - `operator.index()`- `bin()`- `hex()`- `oct()`- If - `__int__()`- `__float__()`- `__complex__()`- `int()`- `float()`- `complex()`- `__index__()`.

- 
object.__round__(*self*[,*ndigits*])[¶](#object.__round__)
- 
object.__trunc__(*self*)[¶](#object.__trunc__)
- 
object.__floor__(*self*)[¶](#object.__floor__)
- 
object.__ceil__(*self*)[¶](#object.__ceil__)
- Called to implement the built-in function - `round()`- `math`- `trunc()`- `floor()`- `ceil()`- *ndigits*is passed to- `__round__()`all these methods should return the value of the object truncated to an- `Integral`- `int`- The built-in function - `int()`- `__trunc__()`if neither- `__int__()`- `__index__()`- Changed in version 3.11: The delegation of - `int()`- `__trunc__()`is deprecated.

### 3.3.9. With Statement Context Managers[¶](#with-statement-context-managers)

A *context manager* is an object that defines the runtime context to be
established when executing a [ with](compound_stmts.html#with) statement. The context manager
handles the entry into, and the exit from, the desired runtime context for the
execution of the block of code.  Context managers are normally invoked using the

`with` statement (described in section [The with statement](compound_stmts.html#with)), but can also be used by directly invoking their methods.

Typical uses of context managers include saving and restoring various kinds of global state, locking and unlocking resources, closing opened files, etc.

For more information on context managers, see [Context Manager Types](../library/stdtypes.html#typecontextmanager).
The [ object](../library/functions.html#object) class itself does not provide the context manager methods.

- 
object.__enter__(*self*)[¶](#object.__enter__)
- Enter the runtime context related to this object. The - `with`- `as`clause of the statement, if any.

- 
object.__exit__(*self*,*exc_type*,*exc_value*,*traceback*)[¶](#object.__exit__)
- Exit the runtime context related to this object. The parameters describe the exception that caused the context to be exited. If the context was exited without an exception, all three arguments will be - `None`- If an exception is supplied, and the method wishes to suppress the exception (i.e., prevent it from being propagated), it should return a true value. Otherwise, the exception will be processed normally upon exit from this method. - Note that - `__exit__()`methods should not reraise the passed-in exception; this is the caller’s responsibility.

### 3.3.10. Customizing positional arguments in class pattern matching[¶](#customizing-positional-arguments-in-class-pattern-matching)

When using a class name in a pattern, positional arguments in the pattern are not
allowed by default, i.e. `case MyClass(x, y)` is typically invalid without special
support in `MyClass`. To be able to use that kind of pattern, the class needs to
define a *__match_args__* attribute.

- 
object.__match_args__[¶](#object.__match_args__)
- This class variable can be assigned a tuple of strings. When this class is used in a class pattern with positional arguments, each positional argument will be converted into a keyword argument, using the corresponding value in - *__match_args__*as the keyword. The absence of this attribute is equivalent to setting it to- `()`.

For example, if `MyClass.__match_args__` is `("left", "center", "right")` that means
that `case MyClass(x, y)` is equivalent to `case MyClass(left=x, center=y)`. Note
that the number of arguments in the pattern must be smaller than or equal to the number
of elements in *__match_args__*; if it is larger, the pattern match attempt will raise
a [ TypeError](../library/exceptions.html#TypeError).

Added in version 3.10.

See also

- **PEP 634**
- The specification for the Python - `match`statement.

### 3.3.11. Emulating buffer types[¶](#emulating-buffer-types)

The [buffer protocol](../c-api/buffer.html#bufferobjects) provides a way for Python
objects to expose efficient access to a low-level memory array. This protocol
is implemented by builtin types such as [ bytes](../library/stdtypes.html#bytes) and 

[, and third-party libraries may define additional buffer types.](../library/stdtypes.html#memoryview)

`memoryview`While buffer types are usually implemented in C, it is also possible to implement the protocol in Python.

- 
object.__buffer__(*self*,*flags*)[¶](#object.__buffer__)
- Called when a buffer is requested from - *self*(for example, by the- `memoryview`- *flags*argument is an integer representing the kind of buffer requested, affecting for example whether the returned buffer is read-only or writable.- `inspect.BufferFlags`- `memoryview`object.

- 
object.__release_buffer__(*self*,*buffer*)[¶](#object.__release_buffer__)
- Called when a buffer is no longer needed. The - *buffer*argument is a- `memoryview`- `__buffer__()`- `None`. Buffer objects that do not need to perform any cleanup are not required to implement this method.

Added in version 3.12.

See also

- **PEP 688**
- Introduces the Python - `__buffer__`and- `__release_buffer__`methods.
- `collections.abc.Buffer`
- ABC for buffer types. 

### 3.3.12. Special method lookup[¶](#special-method-lookup)

For custom classes, implicit invocations of special methods are only guaranteed to work correctly if defined on an object’s type, not in the object’s instance dictionary. That behaviour is the reason why the following code raises an exception:

```
>>> class C:
...     pass
...
>>> c = C()
>>> c.__len__ = lambda: 5
>>> len(c)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'C' has no len()
```
The rationale behind this behaviour lies with a number of special methods such
as [ __hash__()](#object.__hash__) and 

[that are implemented by all objects, including type objects. If the implicit lookup of these methods used the conventional lookup process, they would fail when invoked on the type object itself:](#object.__repr__)

`__repr__()````
>>> 1 .__hash__() == hash(1)
True
>>> int.__hash__() == hash(int)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: descriptor '__hash__' of 'int' object needs an argument
```
Incorrectly attempting to invoke an unbound method of a class in this way is sometimes referred to as ‘metaclass confusion’, and is avoided by bypassing the instance when looking up special methods:

```
>>> type(1).__hash__(1) == hash(1)
True
>>> type(int).__hash__(int) == hash(int)
True
```
In addition to bypassing any instance attributes in the interest of
correctness, implicit special method lookup generally also bypasses the
[ __getattribute__()](#object.__getattribute__) method even of the object’s metaclass:

```
>>> class Meta(type):
...     def __getattribute__(*args):
...         print("Metaclass getattribute invoked")
...         return type.__getattribute__(*args)
...
>>> class C(object, metaclass=Meta):
...     def __len__(self):
...         return 10
...     def __getattribute__(*args):
...         print("Class getattribute invoked")
...         return object.__getattribute__(*args)
...
>>> c = C()
>>> c.__len__()                 # Explicit lookup via instance
Class getattribute invoked
10
>>> type(c).__len__(c)          # Explicit lookup via type
Metaclass getattribute invoked
10
>>> len(c)                      # Implicit lookup
10
```
Bypassing the [ __getattribute__()](#object.__getattribute__) machinery in this fashion
provides significant scope for speed optimisations within the
interpreter, at the cost of some flexibility in the handling of
special methods (the special method 

*must*be set on the class object itself in order to be consistently invoked by the interpreter).

## 3.4. Coroutines[¶](#coroutines)

### 3.4.1. Awaitable Objects[¶](#awaitable-objects)

An [awaitable](../glossary.html#term-awaitable) object generally implements an [ __await__()](#object.__await__) method.

[Coroutine objects](../glossary.html#term-coroutine)returned from

[functions are awaitable.](compound_stmts.html#async-def)

`async def`Note

The [generator iterator](../glossary.html#term-generator-iterator) objects returned from generators
decorated with [ types.coroutine()](../library/types.html#types.coroutine)
are also awaitable, but they do not implement 

[.](#object.__await__)

`__await__()`- 
object.__await__(*self*)[¶](#object.__await__)
- Must return an - [iterator](../glossary.html#term-iterator). Should be used to implement- [awaitable](../glossary.html#term-awaitable)objects. For instance,- `asyncio.Future`- `await`- `object`

Added in version 3.5.

See also

[ PEP 492](https://peps.python.org/pep-0492/) for additional information about awaitable objects.

### 3.4.2. Coroutine Objects[¶](#coroutine-objects)

[Coroutine objects](../glossary.html#term-coroutine) are [awaitable](../glossary.html#term-awaitable) objects.
A coroutine’s execution can be controlled by calling [ __await__()](#object.__await__) and
iterating over the result.  When the coroutine has finished executing and
returns, the iterator raises 

[, and the exception’s](../library/exceptions.html#StopIteration)

`StopIteration`[attribute holds the return value. If the coroutine raises an exception, it is propagated by the iterator. Coroutines should not directly raise unhandled](../library/exceptions.html#StopIteration.value)

`value``StopIteration` exceptions.Coroutines also have the methods listed below, which are analogous to
those of generators (see [Generator-iterator methods](expressions.html#generator-methods)).  However, unlike
generators, coroutines do not directly support iteration.

Coroutines are [generic](../library/typing.html#generics) over the types of their yield, send,
and return values, respectively.

Changed in version 3.5.2: It is a [ RuntimeError](../library/exceptions.html#RuntimeError) to await on a coroutine more than once.

- 
coroutine.send(*value*)[¶](#coroutine.send)
- Starts or resumes execution of the coroutine. If - *value*is- `None`, this is equivalent to advancing the iterator returned by- `__await__()`- *value*is not- `None`, this method delegates to the- `send()`- `StopIteration`- `__await__()`return value, described above.

- 
coroutine.throw(*value*)[¶](#coroutine.throw)
- 
coroutine.throw(*type*[,*value*[,*traceback*]])
- Raises the specified exception in the coroutine. This method delegates to the - `throw()`- `StopIteration`- `__await__()`- Changed in version 3.12: The second signature (type[, value[, traceback]]) is deprecated and may be removed in a future version of Python. 

- 
coroutine.close()[¶](#coroutine.close)
- Causes the coroutine to clean itself up and exit. If the coroutine is suspended, this method first delegates to the - `close()`- `GeneratorExit`- Coroutine objects are automatically closed using the above process when they are about to be destroyed. 

### 3.4.3. Asynchronous Iterators[¶](#asynchronous-iterators)

An *asynchronous iterator* can call asynchronous code in
its `__anext__` method.

Asynchronous iterators can be used in an [ async for](compound_stmts.html#async-for) statement.

The [ object](../library/functions.html#object) class itself does not provide these methods.

- 
object.__aiter__(*self*)[¶](#object.__aiter__)
- Must return an - *asynchronous iterator*object.

- 
object.__anext__(*self*)[¶](#object.__anext__)
- Must return an - *awaitable*resulting in a next value of the iterator. Should raise a- `StopAsyncIteration`

An example of an asynchronous iterable object:

```
class Reader:
    async def readline(self):
        ...
    def __aiter__(self):
        return self
    async def __anext__(self):
        val = await self.readline()
        if val == b'':
            raise StopAsyncIteration
        return val
```
Added in version 3.5.

Changed in version 3.7: Prior to Python 3.7, [ __aiter__()](#object.__aiter__) could return an 

*awaitable*that would resolve to an

[asynchronous iterator](../glossary.html#term-asynchronous-iterator).

Starting with Python 3.7, [ __aiter__()](#object.__aiter__) must return an
asynchronous iterator object.  Returning anything else
will result in a 

[error.](../library/exceptions.html#TypeError)

`TypeError`### 3.4.4. Asynchronous Context Managers[¶](#asynchronous-context-managers)

An *asynchronous context manager* is a *context manager* that is able to
suspend execution in its `__aenter__` and `__aexit__` methods.

Asynchronous context managers can be used in an [ async with](compound_stmts.html#async-with) statement.

The [ object](../library/functions.html#object) class itself does not provide these methods.

- 
object.__aenter__(*self*)[¶](#object.__aenter__)
- Semantically similar to - `__enter__()`- *awaitable*.

- 
object.__aexit__(*self*,*exc_type*,*exc_value*,*traceback*)[¶](#object.__aexit__)
- Semantically similar to - `__exit__()`- *awaitable*.

An example of an asynchronous context manager class:

```
class AsyncContextManager:
    async def __aenter__(self):
        await log('entering context')
    async def __aexit__(self, exc_type, exc, tb):
        await log('exiting context')
```
Added in version 3.5.

Footnotes