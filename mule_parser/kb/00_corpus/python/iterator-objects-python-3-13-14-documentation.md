# Iterator Objects — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/iterator.html](https://docs.python.org/3.13/c-api/iterator.html)

---

# Iterator Objects[¶](#iterator-objects)

Python provides two general-purpose iterator objects.  The first, a sequence
iterator, works with an arbitrary sequence supporting the [ __getitem__()](../reference/datamodel.html#object.__getitem__)
method.  The second works with a callable object and a sentinel value, calling
the callable for each item in the sequence, and ending the iteration when the
sentinel value is returned.

- 
[PyTypeObject](type.html#c.PyTypeObject)PySeqIter_Type[¶](#c.PySeqIter_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- Type object for iterator objects returned by - `PySeqIter_New()`- `iter()`

- 
int PySeqIter_Check([PyObject](structures.html#c.PyObject)*op)[¶](#c.PySeqIter_Check)
- Return true if the type of - *op*is- `PySeqIter_Type`

- 
[PyObject](structures.html#c.PyObject)*PySeqIter_New([PyObject](structures.html#c.PyObject)*seq)[¶](#c.PySeqIter_New)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return an iterator that works with a general sequence object, - *seq*. The iteration ends when the sequence raises- `IndexError`

- 
[PyTypeObject](type.html#c.PyTypeObject)PyCallIter_Type[¶](#c.PyCallIter_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- Type object for iterator objects returned by - `PyCallIter_New()`- `iter()`

- 
int PyCallIter_Check([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyCallIter_Check)
- Return true if the type of - *op*is- `PyCallIter_Type`

- 
[PyObject](structures.html#c.PyObject)*PyCallIter_New([PyObject](structures.html#c.PyObject)*callable,[PyObject](structures.html#c.PyObject)*sentinel)[¶](#c.PyCallIter_New)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a new iterator. The first parameter, - *callable*, can be any Python callable object that can be called with no parameters; each call to it should return the next item in the iteration. When- *callable*returns a value equal to- *sentinel*, the iteration will be terminated.

## Range Objects[¶](#range-objects)

- 
[PyTypeObject](type.html#c.PyTypeObject)PyRange_Type[¶](#c.PyRange_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- The type object for - `range`

## Builtin Iterator Types[¶](#builtin-iterator-types)

These are built-in iteration types that are included in Python’s C API, but provide no additional functions. They are here for completeness.

| C type | Python type | 
|---|---|
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | 

## Other Iterator Objects[¶](#other-iterator-objects)

- 
[PyTypeObject](type.html#c.PyTypeObject)PyByteArrayIter_Type[¶](#c.PyByteArrayIter_Type)
- *Part of the*- [Stable ABI](stable.html#stable).

- 
[PyTypeObject](type.html#c.PyTypeObject)PyBytesIter_Type[¶](#c.PyBytesIter_Type)
- *Part of the*- [Stable ABI](stable.html#stable).

- 
[PyTypeObject](type.html#c.PyTypeObject)PyListIter_Type[¶](#c.PyListIter_Type)
- *Part of the*- [Stable ABI](stable.html#stable).

- 
[PyTypeObject](type.html#c.PyTypeObject)PyListRevIter_Type[¶](#c.PyListRevIter_Type)
- *Part of the*- [Stable ABI](stable.html#stable).

- 
[PyTypeObject](type.html#c.PyTypeObject)PySetIter_Type[¶](#c.PySetIter_Type)
- *Part of the*- [Stable ABI](stable.html#stable).

- 
[PyTypeObject](type.html#c.PyTypeObject)PyTupleIter_Type[¶](#c.PyTupleIter_Type)
- *Part of the*- [Stable ABI](stable.html#stable).

- 
[PyTypeObject](type.html#c.PyTypeObject)PyRangeIter_Type[¶](#c.PyRangeIter_Type)
- *Part of the*- [Stable ABI](stable.html#stable).

- 
[PyTypeObject](type.html#c.PyTypeObject)PyLongRangeIter_Type[¶](#c.PyLongRangeIter_Type)
- *Part of the*- [Stable ABI](stable.html#stable).

- 
[PyTypeObject](type.html#c.PyTypeObject)PyDictIterKey_Type[¶](#c.PyDictIterKey_Type)
- *Part of the*- [Stable ABI](stable.html#stable).

- 
[PyTypeObject](type.html#c.PyTypeObject)PyDictRevIterKey_Type[¶](#c.PyDictRevIterKey_Type)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.8.

- 
[PyTypeObject](type.html#c.PyTypeObject)PyDictIterValue_Type[¶](#c.PyDictIterValue_Type)
- *Part of the*- [Stable ABI](stable.html#stable).

- 
[PyTypeObject](type.html#c.PyTypeObject)PyDictRevIterValue_Type[¶](#c.PyDictRevIterValue_Type)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.8.

- 
[PyTypeObject](type.html#c.PyTypeObject)PyDictIterItem_Type[¶](#c.PyDictIterItem_Type)
- *Part of the*- [Stable ABI](stable.html#stable).

- 
[PyTypeObject](type.html#c.PyTypeObject)PyDictRevIterItem_Type[¶](#c.PyDictRevIterItem_Type)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.8.

- 
[PyTypeObject](type.html#c.PyTypeObject)PyODictIter_Type[¶](#c.PyODictIter_Type)
- Type objects for iterators of various built-in objects. - Do not create instances of these directly; prefer calling - `PyObject_GetIter()`- Note that there is no guarantee that a given built-in type uses a given iterator type. For example, iterating over - `range`