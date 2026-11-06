# Objects for Type Hinting — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/typehints.html](https://docs.python.org/3.13/c-api/typehints.html)

---

# Objects for Type Hinting[¶](#objects-for-type-hinting)

Various built-in types for type hinting are provided.  Currently,
two types exist – [GenericAlias](../library/stdtypes.html#types-genericalias) and
[Union](../library/stdtypes.html#types-union).  Only `GenericAlias` is exposed to C.

- 
[PyObject](structures.html#c.PyObject)*Py_GenericAlias([PyObject](structures.html#c.PyObject)*origin,[PyObject](structures.html#c.PyObject)*args)[¶](#c.Py_GenericAlias)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.9.- Create a - [GenericAlias](../library/stdtypes.html#types-genericalias)object. Equivalent to calling the Python class- `types.GenericAlias`- *origin*and- *args*arguments set the- `GenericAlias`‘s- `__origin__`and- `__args__`attributes respectively.- *origin*should be a- [PyTypeObject](type.html#c.PyTypeObject)*, and- *args*can be a- [PyTupleObject](tuple.html#c.PyTupleObject)* or any- `PyObject*`. If- *args*passed is not a tuple, a 1-tuple is automatically constructed and- `__args__`is set to- `(args,)`. Minimal checking is done for the arguments, so the function will succeed even if- *origin*is not a type. The- `GenericAlias`‘s- `__parameters__`attribute is constructed lazily from- `__args__`. On failure, an exception is raised and- `NULL`is returned.- Here’s an example of how to make an extension type generic: - ... static PyMethodDef my_obj_methods[] = { // Other methods. ... {"__class_getitem__", Py_GenericAlias, METH_O|METH_CLASS, "my_obj is generic over its contained type"} ... } - See also - The data model method - `__class_getitem__()`- Added in version 3.9. 

- 
[PyTypeObject](type.html#c.PyTypeObject)Py_GenericAliasType[¶](#c.Py_GenericAliasType)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.9.- The C type of the object returned by - `Py_GenericAlias()`- `types.GenericAlias`- Added in version 3.9.