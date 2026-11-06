# reprlib — Alternate repr() implementation — Python 3.14.6 documentation

**Source:** [https://docs.python.org/library/reprlib.html](https://docs.python.org/library/reprlib.html)

---

`reprlib` — Alternate `repr()`[¶](#module-reprlib)

`repr()`**Source code:** [Lib/reprlib.py](https://github.com/python/cpython/tree/3.14/Lib/reprlib.py)

The `reprlib` module provides a means for producing object representations
with limits on the size of the resulting strings. This is used in the Python
debugger and may be useful in other contexts as well.

This module provides a class, an instance, and a function:

- 
*class*reprlib.Repr(***,*maxlevel=6*,*maxtuple=6*,*maxlist=6*,*maxarray=5*,*maxdict=4*,*maxset=6*,*maxfrozenset=6*,*maxdeque=6*,*maxstring=30*,*maxlong=40*,*maxother=30*,*fillvalue='...'*,*indent=None*)[¶](#reprlib.Repr)
- Class which provides formatting services useful in implementing functions similar to the built-in - `repr()`- The keyword arguments of the constructor can be used as a shortcut to set the attributes of the - `Repr`instance. Which means that the following initialization:- aRepr = reprlib.Repr(maxlevel=3) - Is equivalent to: - aRepr = reprlib.Repr() aRepr.maxlevel = 3 - See section - [Repr Objects](#id1)for more information about- `Repr`attributes.- Changed in version 3.12: Allow attributes to be set via keyword arguments. 

- 
reprlib.aRepr[¶](#reprlib.aRepr)
- This is an instance of - `Repr`- `repr()`- `repr()`and the Python debugger.

- 
reprlib.repr(*obj*)[¶](#reprlib.repr)
- This is the - `repr()`- `aRepr`. It returns a string similar to that returned by the built-in function of the same name, but with limits on most sizes.

In addition to size-limiting tools, the module also provides a decorator for
detecting recursive calls to [ __repr__()](../reference/datamodel.html#object.__repr__) and substituting a
placeholder string instead.

- 
@reprlib.recursive_repr(*fillvalue='...'*)[¶](#reprlib.recursive_repr)
- Decorator for - `__repr__()`- *fillvalue*is returned, otherwise, the usual- `__repr__()`call is made. For example:- >>> from reprlib import recursive_repr >>> class MyList(list): ... @recursive_repr() ... def __repr__(self): ... return '<' + '|'.join(map(repr, self)) + '>' ... >>> m = MyList('abc') >>> m.append(m) >>> m.append('x') >>> print(m) <'a'|'b'|'c'|...|'x'> - Added in version 3.2. 

## Repr Objects[¶](#repr-objects)

[ Repr](#reprlib.Repr) instances provide several attributes which can be used to provide
size limits for the representations of different object types,  and methods
which format specific object types.

- 
Repr.fillvalue[¶](#reprlib.Repr.fillvalue)
- This string is displayed for recursive references. It defaults to - `...`.- Added in version 3.11. 

- 
Repr.maxlevel[¶](#reprlib.Repr.maxlevel)
- Depth limit on the creation of recursive representations. The default is - `6`.

- 
Repr.maxdict[¶](#reprlib.Repr.maxdict)
- 
Repr.maxlist[¶](#reprlib.Repr.maxlist)
- 
Repr.maxtuple[¶](#reprlib.Repr.maxtuple)
- 
Repr.maxset[¶](#reprlib.Repr.maxset)
- 
Repr.maxfrozenset[¶](#reprlib.Repr.maxfrozenset)
- 
Repr.maxdeque[¶](#reprlib.Repr.maxdeque)
- 
Repr.maxarray[¶](#reprlib.Repr.maxarray)
- Limits on the number of entries represented for the named object type. The default is - `4`for- `maxdict`- `5`for- `maxarray`- `6`for the others.

- 
Repr.maxlong[¶](#reprlib.Repr.maxlong)
- Maximum number of characters in the representation for an integer. Digits are dropped from the middle. The default is - `40`.

- 
Repr.maxstring[¶](#reprlib.Repr.maxstring)
- Limit on the number of characters in the representation of the string. Note that the “normal” representation of the string is used as the character source: if escape sequences are needed in the representation, these may be mangled when the representation is shortened. The default is - `30`.

- 
Repr.maxother[¶](#reprlib.Repr.maxother)
- This limit is used to control the size of object types for which no specific formatting method is available on the - `Repr`- `maxstring`- `20`.

- 
Repr.indent[¶](#reprlib.Repr.indent)
- If this attribute is set to - `None`(the default), the output is formatted with no line breaks or indentation, like the standard- `repr()`- >>> example = [ ... 1, 'spam', {'a': 2, 'b': 'spam eggs', 'c': {3: 4.5, 6: []}}, 'ham'] >>> import reprlib >>> aRepr = reprlib.Repr() >>> print(aRepr.repr(example)) [1, 'spam', {'a': 2, 'b': 'spam eggs', 'c': {3: 4.5, 6: []}}, 'ham'] - If - `indent`is set to a string, each recursion level is placed on its own line, indented by that string:- >>> aRepr.indent = '-->' >>> print(aRepr.repr(example)) [ -->1, -->'spam', -->{ -->-->'a': 2, -->-->'b': 'spam eggs', -->-->'c': { -->-->-->3: 4.5, -->-->-->6: [], -->-->}, -->}, -->'ham', ] - Setting - `indent`to a positive integer value behaves as if it was set to a string with that number of spaces:- >>> aRepr.indent = 4 >>> print(aRepr.repr(example)) [ 1, 'spam', { 'a': 2, 'b': 'spam eggs', 'c': { 3: 4.5, 6: [], }, }, 'ham', ] - Added in version 3.12. 

- 
Repr.repr(*obj*)[¶](#reprlib.Repr.repr)
- The equivalent to the built-in - `repr()`

- 
Repr.repr1(*obj*,*level*)[¶](#reprlib.Repr.repr1)
- Recursive implementation used by - `repr()`- *obj*to determine which formatting method to call, passing it- *obj*and- *level*. The type-specific methods should call- `repr1()`to perform recursive formatting, with- `level - 1`for the value of- *level*in the recursive call.

- 
Repr.repr_TYPE(*obj*,*level*)
- Formatting methods for specific types are implemented as methods with a name based on the type name. In the method name, - **TYPE**is replaced by- `'_'.join(type(obj).__name__.split())`. Dispatch to these methods is handled by- `repr1()`- `self.repr1(subobj, level - 1)`.

## Subclassing Repr Objects[¶](#subclassing-repr-objects)

The use of dynamic dispatching by [ Repr.repr1()](#reprlib.Repr.repr1) allows subclasses of

[to add support for additional built-in object types or to modify the handling of types already supported. This example shows how special support for file objects could be added:](#reprlib.Repr)

`Repr````
import reprlib
import sys
class MyRepr(reprlib.Repr):
    def repr_TextIOWrapper(self, obj, level):
        if obj.name in {'<stdin>', '<stdout>', '<stderr>'}:
            return obj.name
        return repr(obj)
aRepr = MyRepr()
print(aRepr.repr(sys.stdin))         # prints '<stdin>'
```
```
<stdin>
```