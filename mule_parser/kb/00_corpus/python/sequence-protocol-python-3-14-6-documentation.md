# Sequence Protocol — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/sequence.html](https://docs.python.org/c-api/sequence.html)

---

# Sequence Protocol[¶](#sequence-protocol)

- 
int PySequence_Check([PyObject](structures.html#c.PyObject)*o)[¶](#c.PySequence_Check)
- *Part of the*- [Stable ABI](stable.html#stable).- Return - `1`if the object provides the sequence protocol, and- `0`otherwise. Note that it returns- `1`for Python classes with a- `__getitem__()`- `dict`

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PySequence_Size([PyObject](structures.html#c.PyObject)*o)[¶](#c.PySequence_Size)
- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PySequence_Length([PyObject](structures.html#c.PyObject)*o)[¶](#c.PySequence_Length)
- *Part of the*- [Stable ABI](stable.html#stable).- Returns the number of objects in sequence - *o*on success, and- `-1`on failure. This is equivalent to the Python expression- `len(o)`.

- 
[PyObject](structures.html#c.PyObject)*PySequence_Concat([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2)[¶](#c.PySequence_Concat)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return the concatenation of - *o1*and- *o2*on success, and- `NULL`on failure. This is the equivalent of the Python expression- `o1 + o2`.

- 
[PyObject](structures.html#c.PyObject)*PySequence_Repeat([PyObject](structures.html#c.PyObject)*o,[Py_ssize_t](intro.html#c.Py_ssize_t)count)[¶](#c.PySequence_Repeat)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return the result of repeating sequence object - *o*- *count*times, or- `NULL`on failure. This is the equivalent of the Python expression- `o * count`.

- 
[PyObject](structures.html#c.PyObject)*PySequence_InPlaceConcat([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2)[¶](#c.PySequence_InPlaceConcat)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return the concatenation of - *o1*and- *o2*on success, and- `NULL`on failure. The operation is done- *in-place*when- *o1*supports it. This is the equivalent of the Python expression- `o1 += o2`.

- 
[PyObject](structures.html#c.PyObject)*PySequence_InPlaceRepeat([PyObject](structures.html#c.PyObject)*o,[Py_ssize_t](intro.html#c.Py_ssize_t)count)[¶](#c.PySequence_InPlaceRepeat)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return the result of repeating sequence object - *o*- *count*times, or- `NULL`on failure. The operation is done- *in-place*when- *o*supports it. This is the equivalent of the Python expression- `o *= count`.

- 
[PyObject](structures.html#c.PyObject)*PySequence_GetItem([PyObject](structures.html#c.PyObject)*o,[Py_ssize_t](intro.html#c.Py_ssize_t)i)[¶](#c.PySequence_GetItem)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return the - *i*th element of- *o*, or- `NULL`on failure. This is the equivalent of the Python expression- `o[i]`.

- 
[PyObject](structures.html#c.PyObject)*PySequence_GetSlice([PyObject](structures.html#c.PyObject)*o,[Py_ssize_t](intro.html#c.Py_ssize_t)i1,[Py_ssize_t](intro.html#c.Py_ssize_t)i2)[¶](#c.PySequence_GetSlice)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return the slice of sequence object - *o*between- *i1*and- *i2*, or- `NULL`on failure. This is the equivalent of the Python expression- `o[i1:i2]`.

- 
int PySequence_SetItem([PyObject](structures.html#c.PyObject)*o,[Py_ssize_t](intro.html#c.Py_ssize_t)i,[PyObject](structures.html#c.PyObject)*v)[¶](#c.PySequence_SetItem)
- *Part of the*- [Stable ABI](stable.html#stable).- Assign object - *v*to the- *i*th element of- *o*. Raise an exception and return- `-1`on failure; return- `0`on success. This is the equivalent of the Python statement- `o[i] = v`. This function- *does not*steal a reference to- *v*.- If - *v*is- `NULL`, the element is deleted, but this feature is deprecated in favour of using- `PySequence_DelItem()`

- 
int PySequence_DelItem([PyObject](structures.html#c.PyObject)*o,[Py_ssize_t](intro.html#c.Py_ssize_t)i)[¶](#c.PySequence_DelItem)
- *Part of the*- [Stable ABI](stable.html#stable).- Delete the - *i*th element of object- *o*. Returns- `-1`on failure. This is the equivalent of the Python statement- `del o[i]`.

- 
int PySequence_SetSlice([PyObject](structures.html#c.PyObject)*o,[Py_ssize_t](intro.html#c.Py_ssize_t)i1,[Py_ssize_t](intro.html#c.Py_ssize_t)i2,[PyObject](structures.html#c.PyObject)*v)[¶](#c.PySequence_SetSlice)
- *Part of the*- [Stable ABI](stable.html#stable).- Assign the sequence object - *v*to the slice in sequence object- *o*from- *i1*to- *i2*. This is the equivalent of the Python statement- `o[i1:i2] = v`.

- 
int PySequence_DelSlice([PyObject](structures.html#c.PyObject)*o,[Py_ssize_t](intro.html#c.Py_ssize_t)i1,[Py_ssize_t](intro.html#c.Py_ssize_t)i2)[¶](#c.PySequence_DelSlice)
- *Part of the*- [Stable ABI](stable.html#stable).- Delete the slice in sequence object - *o*from- *i1*to- *i2*. Returns- `-1`on failure. This is the equivalent of the Python statement- `del o[i1:i2]`.

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PySequence_Count([PyObject](structures.html#c.PyObject)*o,[PyObject](structures.html#c.PyObject)*value)[¶](#c.PySequence_Count)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the number of occurrences of - *value*in- *o*, that is, return the number of keys for which- `o[key] == value`. On failure, return- `-1`. This is equivalent to the Python expression- `o.count(value)`.

- 
int PySequence_Contains([PyObject](structures.html#c.PyObject)*o,[PyObject](structures.html#c.PyObject)*value)[¶](#c.PySequence_Contains)
- *Part of the*- [Stable ABI](stable.html#stable).- Determine if - *o*contains- *value*. If an item in- *o*is equal to- *value*, return- `1`, otherwise return- `0`. On error, return- `-1`. This is equivalent to the Python expression- `value in o`.

- 
int PySequence_In([PyObject](structures.html#c.PyObject)*o,[PyObject](structures.html#c.PyObject)*value)[¶](#c.PySequence_In)
- *Part of the*- [Stable ABI](stable.html#stable).- Alias for - `PySequence_Contains()`- [Soft deprecated](../glossary.html#term-soft-deprecated)since version 3.14: The function should no longer be used to write new code.

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PySequence_Index([PyObject](structures.html#c.PyObject)*o,[PyObject](structures.html#c.PyObject)*value)[¶](#c.PySequence_Index)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the first index - *i*for which- `o[i] == value`. On error, return- `-1`. This is equivalent to the Python expression- `o.index(value)`.

- 
[PyObject](structures.html#c.PyObject)*PySequence_List([PyObject](structures.html#c.PyObject)*o)[¶](#c.PySequence_List)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a list object with the same contents as the sequence or iterable - *o*, or- `NULL`on failure. The returned list is guaranteed to be new. This is equivalent to the Python expression- `list(o)`.

- 
[PyObject](structures.html#c.PyObject)*PySequence_Tuple([PyObject](structures.html#c.PyObject)*o)[¶](#c.PySequence_Tuple)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a tuple object with the same contents as the sequence or iterable - *o*, or- `NULL`on failure. If- *o*is a tuple, a new reference will be returned, otherwise a tuple will be constructed with the appropriate contents. This is equivalent to the Python expression- `tuple(o)`.

- 
[PyObject](structures.html#c.PyObject)*PySequence_Fast([PyObject](structures.html#c.PyObject)*o, const char *m)[¶](#c.PySequence_Fast)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return the sequence or iterable - *o*as an object usable by the other- `PySequence_Fast*`family of functions. If the object is not a sequence or iterable, raises- `TypeError`- *m*as the message text. Returns- `NULL`on failure.- The - `PySequence_Fast*`functions are thus named because they assume- *o*is a- `PyTupleObject`- `PyListObject`- *o*directly.- As a CPython implementation detail, if - *o*is already a sequence or list, it will be returned.

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PySequence_Fast_GET_SIZE([PyObject](structures.html#c.PyObject)*o)[¶](#c.PySequence_Fast_GET_SIZE)
- Returns the length of - *o*, assuming that- *o*was returned by- `PySequence_Fast()`- *o*is not- `NULL`. The size can also be retrieved by calling- `PySequence_Size()`- *o*, but- `PySequence_Fast_GET_SIZE()`- *o*is a list or tuple.

- 
[PyObject](structures.html#c.PyObject)*PySequence_Fast_GET_ITEM([PyObject](structures.html#c.PyObject)*o,[Py_ssize_t](intro.html#c.Py_ssize_t)i)[¶](#c.PySequence_Fast_GET_ITEM)
- *Return value: Borrowed reference.*- Return the - *i*th element of- *o*, assuming that- *o*was returned by- `PySequence_Fast()`- *o*is not- `NULL`, and that- *i*is within bounds.

- 
[PyObject](structures.html#c.PyObject)**PySequence_Fast_ITEMS([PyObject](structures.html#c.PyObject)*o)[¶](#c.PySequence_Fast_ITEMS)
- Return the underlying array of PyObject pointers. Assumes that - *o*was returned by- `PySequence_Fast()`- *o*is not- `NULL`.- Note, if a list gets resized, the reallocation may relocate the items array. So, only use the underlying array pointer in contexts where the sequence cannot change. 

- 
[PyObject](structures.html#c.PyObject)*PySequence_ITEM([PyObject](structures.html#c.PyObject)*o,[Py_ssize_t](intro.html#c.Py_ssize_t)i)[¶](#c.PySequence_ITEM)
- *Return value: New reference.*- Return the - *i*th element of- *o*or- `NULL`on failure. Faster form of- `PySequence_GetItem()`- `PySequence_Check()`- *o*is true and without adjustment for negative indices.