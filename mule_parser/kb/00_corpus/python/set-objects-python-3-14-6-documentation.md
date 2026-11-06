# Set Objects — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/set.html](https://docs.python.org/c-api/set.html)

---

# Set Objects[¶](#set-objects)

This section details the public API for [ set](../library/stdtypes.html#set) and 

[objects. Any functionality not listed below is best accessed using either the abstract object protocol (including](../library/stdtypes.html#frozenset)

`frozenset`[,](call.html#c.PyObject_CallMethod)

`PyObject_CallMethod()`[,](object.html#c.PyObject_RichCompareBool)

`PyObject_RichCompareBool()`[,](object.html#c.PyObject_Hash)

`PyObject_Hash()`[,](object.html#c.PyObject_Repr)

`PyObject_Repr()`[,](object.html#c.PyObject_IsTrue)

`PyObject_IsTrue()`[, and](object.html#c.PyObject_Print)

`PyObject_Print()`[) or the abstract number protocol (including](object.html#c.PyObject_GetIter)

`PyObject_GetIter()`[,](number.html#c.PyNumber_And)

`PyNumber_And()`[,](number.html#c.PyNumber_Subtract)

`PyNumber_Subtract()`[,](number.html#c.PyNumber_Or)

`PyNumber_Or()`[,](number.html#c.PyNumber_Xor)

`PyNumber_Xor()`[,](number.html#c.PyNumber_InPlaceAnd)

`PyNumber_InPlaceAnd()`[,](number.html#c.PyNumber_InPlaceSubtract)

`PyNumber_InPlaceSubtract()`[, and](number.html#c.PyNumber_InPlaceOr)

`PyNumber_InPlaceOr()`[).](number.html#c.PyNumber_InPlaceXor)

`PyNumber_InPlaceXor()`- 
type PySetObject[¶](#c.PySetObject)
- This subtype of - `PyObject`- `set`- `frozenset`- `PyDictObject`

- 
[PyTypeObject](type.html#c.PyTypeObject)PySet_Type[¶](#c.PySet_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- This is an instance of - `PyTypeObject`- `set`

- 
[PyTypeObject](type.html#c.PyTypeObject)PyFrozenSet_Type[¶](#c.PyFrozenSet_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- This is an instance of - `PyTypeObject`- `frozenset`

The following type check macros work on pointers to any Python object. Likewise, the constructor functions work with any iterable Python object.

- 
int PySet_Check([PyObject](structures.html#c.PyObject)*p)[¶](#c.PySet_Check)
- Return true if - *p*is a- `set`

- 
int PyFrozenSet_Check([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyFrozenSet_Check)
- Return true if - *p*is a- `frozenset`

- 
int PyAnySet_Check([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyAnySet_Check)
- Return true if - *p*is a- `set`- `frozenset`

- 
int PySet_CheckExact([PyObject](structures.html#c.PyObject)*p)[¶](#c.PySet_CheckExact)
- Return true if - *p*is a- `set`- Added in version 3.10. 

- 
int PyAnySet_CheckExact([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyAnySet_CheckExact)
- Return true if - *p*is a- `set`- `frozenset`

- 
int PyFrozenSet_CheckExact([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyFrozenSet_CheckExact)
- Return true if - *p*is a- `frozenset`

- 
[PyObject](structures.html#c.PyObject)*PySet_New([PyObject](structures.html#c.PyObject)*iterable)[¶](#c.PySet_New)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Safe for concurrent use on the same object](../library/threadsafety.html#threadsafety-level-shared).- Return a new - `set`- *iterable*. The- *iterable*may be- `NULL`to create a new empty set. Return the new set on success or- `NULL`on failure. Raise- `TypeError`- *iterable*is not actually iterable. The constructor is also useful for copying a set (- `c=set(s)`).- Note - The operation is atomic on - [free threading](../glossary.html#term-free-threaded-build)when- *iterable*is a- `set`- `frozenset`- `dict`

- 
[PyObject](structures.html#c.PyObject)*PyFrozenSet_New([PyObject](structures.html#c.PyObject)*iterable)[¶](#c.PyFrozenSet_New)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Safe for concurrent use on the same object](../library/threadsafety.html#threadsafety-level-shared).- Return a new - `frozenset`- *iterable*. The- *iterable*may be- `NULL`to create a new empty frozenset. Return the new set on success or- `NULL`on failure. Raise- `TypeError`- *iterable*is not actually iterable.- Note - The operation is atomic on - [free threading](../glossary.html#term-free-threaded-build)when- *iterable*is a- `set`- `frozenset`- `dict`

The following functions and macros are available for instances of [ set](../library/stdtypes.html#set)
or 

[or instances of their subtypes.](../library/stdtypes.html#frozenset)

`frozenset`- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PySet_Size([PyObject](structures.html#c.PyObject)*anyset)[¶](#c.PySet_Size)
- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Atomic](../library/threadsafety.html#threadsafety-level-atomic).- Return the length of a - `set`- `frozenset`- `len(anyset)`. Raises a- `SystemError`- *anyset*is not a- `set`,- `frozenset`, or an instance of a subtype.

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PySet_GET_SIZE([PyObject](structures.html#c.PyObject)*anyset)[¶](#c.PySet_GET_SIZE)
- *Thread safety:*- [Atomic](../library/threadsafety.html#threadsafety-level-atomic).- Macro form of - `PySet_Size()`

- 
int PySet_Contains([PyObject](structures.html#c.PyObject)*anyset,[PyObject](structures.html#c.PyObject)*key)[¶](#c.PySet_Contains)
- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Safe for concurrent use on the same object](../library/threadsafety.html#threadsafety-level-shared).- Return - `1`if found,- `0`if not found, and- `-1`if an error is encountered. Unlike the Python- `__contains__()`- `TypeError`- *key*is unhashable. Raise- `SystemError`- *anyset*is not a- `set`- `frozenset`

- 
int PySet_Add([PyObject](structures.html#c.PyObject)*set,[PyObject](structures.html#c.PyObject)*key)[¶](#c.PySet_Add)
- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Safe for concurrent use on the same object](../library/threadsafety.html#threadsafety-level-shared).- Add - *key*to a- `set`- `frozenset`- `PyTuple_SetItem()`- `0`on success or- `-1`on failure. Raise a- `TypeError`- *key*is unhashable. Raise a- `MemoryError`- `SystemError`- *set*is not an instance of- `set`or its subtype.

The following functions are available for instances of [ set](../library/stdtypes.html#set) or its
subtypes but not for instances of 

[or its subtypes.](../library/stdtypes.html#frozenset)

`frozenset`- 
int PySet_Discard([PyObject](structures.html#c.PyObject)*set,[PyObject](structures.html#c.PyObject)*key)[¶](#c.PySet_Discard)
- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Safe for concurrent use on the same object](../library/threadsafety.html#threadsafety-level-shared).- Return - `1`if found and removed,- `0`if not found (no action taken), and- `-1`if an error is encountered. Does not raise- `KeyError`- `TypeError`- *key*is unhashable. Unlike the Python- `discard()`- `SystemError`- *set*is not an instance of- `set`

- 
[PyObject](structures.html#c.PyObject)*PySet_Pop([PyObject](structures.html#c.PyObject)*set)[¶](#c.PySet_Pop)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Atomic](../library/threadsafety.html#threadsafety-level-atomic).- Return a new reference to an arbitrary object in the - *set*, and removes the object from the- *set*. Return- `NULL`on failure. Raise- `KeyError`- `SystemError`- *set*is not an instance of- `set`

- 
int PySet_Clear([PyObject](structures.html#c.PyObject)*set)[¶](#c.PySet_Clear)
- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Atomic](../library/threadsafety.html#threadsafety-level-atomic).- Empty an existing set of all elements. Return - `0`on success. Return- `-1`and raise- `SystemError`- *set*is not an instance of- `set`- Note - In the - [free-threaded build](../glossary.html#term-free-threaded-build), the set is emptied before its entries are cleared, so other threads will observe an empty set rather than intermediate states.

## Deprecated API[¶](#deprecated-api)

- 
PySet_MINSIZE[¶](#c.PySet_MINSIZE)
- A - [soft deprecated](../glossary.html#term-soft-deprecated)constant representing the size of an internal preallocated table inside- `PySetObject`- This is documented solely for completeness, as there are no guarantees that a given version of CPython uses preallocated tables with a fixed size. In code that does not deal with unstable set internals, - `PySet_MINSIZE`can be replaced with a small constant like- `8`.- If looking for the size of a set, use - `PySet_Size()`