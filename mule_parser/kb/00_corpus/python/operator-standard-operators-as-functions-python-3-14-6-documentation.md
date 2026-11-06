# operator — Standard operators as functions — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/operator.html](https://docs.python.org/library/operator.html)

---

`operator` — Standard operators as functions[¶](#module-operator)

**Source code:** [Lib/operator.py](https://github.com/python/cpython/tree/3.14/Lib/operator.py)

The `operator` module exports a set of efficient functions corresponding to
the intrinsic operators of Python.  For example, `operator.add(x, y)` is
equivalent to the expression `x+y`. Many function names are those used for
special methods, without the double underscores.  For backward compatibility,
many of these have a variant with the double underscores kept. The variants
without the double underscores are preferred for clarity.

The functions fall into categories that perform object comparisons, logical operations, mathematical operations and sequence operations.

The object comparison functions are useful for all objects, and are named after the rich comparison operators they support:

- 
operator.lt(*a*,*b*)[¶](#operator.lt)
- 
operator.le(*a*,*b*)[¶](#operator.le)
- 
operator.eq(*a*,*b*)[¶](#operator.eq)
- 
operator.ne(*a*,*b*)[¶](#operator.ne)
- 
operator.ge(*a*,*b*)[¶](#operator.ge)
- 
operator.gt(*a*,*b*)[¶](#operator.gt)
- 
operator.__lt__(*a*,*b*)[¶](#operator.__lt__)
- 
operator.__le__(*a*,*b*)[¶](#operator.__le__)
- 
operator.__eq__(*a*,*b*)[¶](#operator.__eq__)
- 
operator.__ne__(*a*,*b*)[¶](#operator.__ne__)
- 
operator.__ge__(*a*,*b*)[¶](#operator.__ge__)
- 
operator.__gt__(*a*,*b*)[¶](#operator.__gt__)
- Perform “rich comparisons” between - *a*and- *b*. Specifically,- `lt(a, b)`is equivalent to- `a < b`,- `le(a, b)`is equivalent to- `a <= b`,- `eq(a, b)`is equivalent to- `a == b`,- `ne(a, b)`is equivalent to- `a != b`,- `gt(a, b)`is equivalent to- `a > b`and- `ge(a, b)`is equivalent to- `a >= b`. Note that these functions can return any value, which may or may not be interpretable as a Boolean value. See- [Comparisons](../reference/expressions.html#comparisons)for more information about rich comparisons.

The logical operations are also generally applicable to all objects, and support truth tests, identity tests, and boolean operations:

- 
operator.not_(*obj*)[¶](#operator.not_)
- 
operator.__not__(*obj*)[¶](#operator.__not__)
- Return the outcome of - `not`- *obj*. (Note that there is no- `__not__()`method for object instances; only the interpreter core defines this operation. The result is affected by the- `__bool__()`- `__len__()`

- 
operator.truth(*obj*)[¶](#operator.truth)
- Return - `True`- *obj*is true, and- `False`- `bool`

- 
operator.is_(*a*,*b*)[¶](#operator.is_)
- Return - `a is b`. Tests object identity.

- 
operator.is_not(*a*,*b*)[¶](#operator.is_not)
- Return - `a is not b`. Tests object identity.

- 
operator.is_none(*a*)[¶](#operator.is_none)
- Return - `a is None`. Tests object identity.- Added in version 3.14. 

- 
operator.is_not_none(*a*)[¶](#operator.is_not_none)
- Return - `a is not None`. Tests object identity.- Added in version 3.14. 

The mathematical and bitwise operations are the most numerous:

- 
operator.index(*a*)[¶](#operator.index)
- 
operator.__index__(*a*)[¶](#operator.__index__)
- Return - *a*converted to an integer. Equivalent to- `a.__index__()`.- Changed in version 3.10: The result always has exact type - `int`- `int`.

- 
operator.inv(*obj*)[¶](#operator.inv)
- 
operator.invert(*obj*)[¶](#operator.invert)
- 
operator.__inv__(*obj*)[¶](#operator.__inv__)
- 
operator.__invert__(*obj*)[¶](#operator.__invert__)
- Return - `~obj`.

- 
operator.truediv(*a*,*b*)[¶](#operator.truediv)
- 
operator.__truediv__(*a*,*b*)[¶](#operator.__truediv__)
- Return - `a / b`where 2/3 is .66 rather than 0. This is also known as “true” division.

Operations which work with sequences (some of them with mappings too) include:

- 
operator.contains(*a*,*b*)[¶](#operator.contains)
- 
operator.__contains__(*a*,*b*)[¶](#operator.__contains__)
- Return the outcome of the test - `b in a`. Note the reversed operands.

- 
operator.countOf(*a*,*b*)[¶](#operator.countOf)
- Return the number of occurrences of - *b*in- *a*.

- 
operator.indexOf(*a*,*b*)[¶](#operator.indexOf)
- Return the index of the first of occurrence of - *b*in- *a*.

- 
operator.length_hint(*obj*,*default=0*)[¶](#operator.length_hint)
- Return an estimated length for the object - *obj*. First try to return its actual length, then an estimate using- `object.__length_hint__()`- Added in version 3.4. 

The following operation works with callables:

- 
operator.call(*obj*,*/*,**args*,***kwargs*)[¶](#operator.call)
- 
operator.__call__(*obj*,*/*,**args*,***kwargs*)[¶](#operator.__call__)
- Return - `obj(*args, **kwargs)`.- Added in version 3.11. 

The `operator` module also defines tools for generalized attribute and item
lookups.  These are useful for making fast field extractors as arguments for
[ map()](functions.html#map), 

[,](functions.html#sorted)

`sorted()`[, or other functions that expect a function argument.](itertools.html#itertools.groupby)

`itertools.groupby()`- 
operator.attrgetter(*attr*)[¶](#operator.attrgetter)
- 
operator.attrgetter(**attrs*)
- Return a callable object that fetches - *attr*from its operand. If more than one attribute is requested, returns a tuple of attributes. The attribute names can also contain dots. For example:- After - `f = attrgetter('name')`, the call- `f(b)`returns- `b.name`.
- After - `f = attrgetter('name', 'date')`, the call- `f(b)`returns- `(b.name, b.date)`.
- After - `f = attrgetter('name.first', 'name.last')`, the call- `f(b)`returns- `(b.name.first, b.name.last)`.
 - Equivalent to: - def attrgetter(*items): if any(not isinstance(item, str) for item in items): raise TypeError('attribute name must be a string') if len(items) == 1: attr = items[0] def g(obj): return resolve_attr(obj, attr) else: def g(obj): return tuple(resolve_attr(obj, attr) for attr in items) return g def resolve_attr(obj, attr): for name in attr.split("."): obj = getattr(obj, name) return obj 

- 
operator.itemgetter(*item*)[¶](#operator.itemgetter)
- 
operator.itemgetter(**items*)
- Return a callable object that fetches - *item*from its operand using the operand’s- `__getitem__()`- After - `f = itemgetter(2)`, the call- `f(r)`returns- `r[2]`.
- After - `g = itemgetter(2, 5, 3)`, the call- `g(r)`returns- `(r[2], r[5], r[3])`.
 - Equivalent to: - def itemgetter(*items): if len(items) == 1: item = items[0] def g(obj): return obj[item] else: def g(obj): return tuple(obj[item] for item in items) return g - The items can be any type accepted by the operand’s - `__getitem__()`- [hashable](../glossary.html#term-hashable)value. Lists, tuples, and strings accept an index or a slice:- >>> itemgetter(1)('ABCDEFG') 'B' >>> itemgetter(1, 3, 5)('ABCDEFG') ('B', 'D', 'F') >>> itemgetter(slice(2, None))('ABCDEFG') 'CDEFG' >>> soldier = dict(rank='captain', name='dotterbart') >>> itemgetter('rank')(soldier) 'captain' - Example of using - `itemgetter()`to retrieve specific fields from a tuple record:- >>> inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)] >>> getcount = itemgetter(1) >>> list(map(getcount, inventory)) [3, 2, 5, 1] >>> sorted(inventory, key=getcount) [('orange', 1), ('banana', 2), ('apple', 3), ('pear', 5)] 

- 
operator.methodcaller(*name*,*/*,**args*,***kwargs*)[¶](#operator.methodcaller)
- Return a callable object that calls the method - *name*on its operand. If additional arguments and/or keyword arguments are given, they will be given to the method as well. For example:- After - `f = methodcaller('name')`, the call- `f(b)`returns- `b.name()`.
- After - `f = methodcaller('name', 'foo', bar=1)`, the call- `f(b)`returns- `b.name('foo', bar=1)`.
 - Equivalent to: - def methodcaller(name, /, *args, **kwargs): def caller(obj): return getattr(obj, name)(*args, **kwargs) return caller 

## Mapping Operators to Functions[¶](#mapping-operators-to-functions)

This table shows how abstract operations correspond to operator symbols in the
Python syntax and the functions in the `operator` module.

| Operation | Syntax | Function | 
|---|---|---|
| Addition | 
 | 
 | 
| Concatenation | 
 | 
 | 
| Containment Test | 
 | 
 | 
| Division | 
 | 
 | 
| Division | 
 | 
 | 
| Bitwise And, or Intersection | 
 | 
 | 
| Bitwise Exclusive Or, or Symmetric Difference | 
 | 
 | 
| Bitwise Inversion, or Complement | 
 | 
 | 
| Bitwise Or, or Union | 
 | 
 | 
| Exponentiation | 
 | 
 | 
| Identity | 
 | 
 | 
| Identity | 
 | 
 | 
| Identity | 
 | 
 | 
| Identity | 
 | 
 | 
| Indexed Assignment | 
 | 
 | 
| Indexed Deletion | 
 | 
 | 
| Indexing | 
 | 
 | 
| Left Shift | 
 | 
 | 
| Modulo | 
 | 
 | 
| Multiplication | 
 | 
 | 
| Matrix Multiplication | 
 | 
 | 
| Negation (Arithmetic) | 
 | 
 | 
| Negation (Logical) | 
 | 
 | 
| Positive | 
 | 
 | 
| Right Shift | 
 | 
 | 
| Slice Assignment | 
 | 
 | 
| Slice Deletion | 
 | 
 | 
| Slicing | 
 | 
 | 
| String Formatting | 
 | 
 | 
| Subtraction | 
 | 
 | 
| Truth Test | 
 | 
 | 
| Ordering | 
 | 
 | 
| Ordering | 
 | 
 | 
| Equality | 
 | 
 | 
| Difference | 
 | 
 | 
| Ordering | 
 | 
 | 
| Ordering | 
 | 
 | 

## In-place Operators[¶](#in-place-operators)

Many operations have an “in-place” version.  Listed below are functions
providing a more primitive access to in-place operators than the usual syntax
does; for example, the [statement](../glossary.html#term-statement) `x += y` is equivalent to
`x = operator.iadd(x, y)`.  Another way to put it is to say that
`z = operator.iadd(x, y)` is equivalent to the compound statement
`z = x; z += y`.

In those examples, note that when an in-place method is called, the computation and assignment are performed in two separate steps. The in-place functions listed below only do the first step, calling the in-place method. The second step, assignment, is not handled.

For immutable targets such as strings, numbers, and tuples, the updated value is computed, but not assigned back to the input variable:

```
>>> a = 'hello'
>>> iadd(a, ' world')
'hello world'
>>> a
'hello'
```
For mutable targets such as lists and dictionaries, the in-place method will perform the update, so no subsequent assignment is necessary:

```
>>> s = ['h', 'e', 'l', 'l', 'o']
>>> iadd(s, [' ', 'w', 'o', 'r', 'l', 'd'])
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
>>> s
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
```
- 
operator.iconcat(*a*,*b*)[¶](#operator.iconcat)
- 
operator.__iconcat__(*a*,*b*)[¶](#operator.__iconcat__)
- `a = iconcat(a, b)`is equivalent to- `a += b`for- *a*and- *b*sequences.

- 
operator.ifloordiv(*a*,*b*)[¶](#operator.ifloordiv)
- 
operator.__ifloordiv__(*a*,*b*)[¶](#operator.__ifloordiv__)
- `a = ifloordiv(a, b)`is equivalent to- `a //= b`.