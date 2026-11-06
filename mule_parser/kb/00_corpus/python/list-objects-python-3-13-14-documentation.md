# List Objects — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/list.html](https://docs.python.org/3.13/c-api/list.html)

---

# List Objects[¶](#list-objects)

- 
[PyTypeObject](type.html#c.PyTypeObject)PyList_Type[¶](#c.PyList_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- This instance of - `PyTypeObject`- `list`

- 
int PyList_Check([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyList_Check)
- Return true if - *p*is a list object or an instance of a subtype of the list type. This function always succeeds.

- 
int PyList_CheckExact([PyObject](structures.html#c.PyObject)*p)[¶](#c.PyList_CheckExact)
- Return true if - *p*is a list object, but not an instance of a subtype of the list type. This function always succeeds.

- 
[PyObject](structures.html#c.PyObject)*PyList_New([Py_ssize_t](intro.html#c.Py_ssize_t)len)[¶](#c.PyList_New)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a new list of length - *len*on success, or- `NULL`on failure.- Note - If - *len*is greater than zero, the returned list object’s items are set to- `NULL`. Thus you cannot use abstract API functions such as- `PySequence_SetItem()`- `PyList_SetItem()`- `PyList_SET_ITEM()`- `PyList_SetItem()`and- `PyList_SET_ITEM()`.

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyList_Size([PyObject](structures.html#c.PyObject)*list)[¶](#c.PyList_Size)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the length of the list object in - *list*; this is equivalent to- `len(list)`on a list object.

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyList_GET_SIZE([PyObject](structures.html#c.PyObject)*list)[¶](#c.PyList_GET_SIZE)
- Similar to - `PyList_Size()`

- 
[PyObject](structures.html#c.PyObject)*PyList_GetItemRef([PyObject](structures.html#c.PyObject)*list,[Py_ssize_t](intro.html#c.Py_ssize_t)index)[¶](#c.PyList_GetItemRef)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Return the object at position - *index*in the list pointed to by- *list*. The position must be non-negative; indexing from the end of the list is not supported. If- *index*is out of bounds (- `<0 or >=len(list)`), return- `NULL`and set an- `IndexError`- Added in version 3.13. 

- 
[PyObject](structures.html#c.PyObject)*PyList_GetItem([PyObject](structures.html#c.PyObject)*list,[Py_ssize_t](intro.html#c.Py_ssize_t)index)[¶](#c.PyList_GetItem)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Like - `PyList_GetItemRef()`- [borrowed reference](../glossary.html#term-borrowed-reference)instead of a- [strong reference](../glossary.html#term-strong-reference).

- 
[PyObject](structures.html#c.PyObject)*PyList_GET_ITEM([PyObject](structures.html#c.PyObject)*list,[Py_ssize_t](intro.html#c.Py_ssize_t)i)[¶](#c.PyList_GET_ITEM)
- *Return value: Borrowed reference.*- Similar to - `PyList_GetItem()`

- 
int PyList_SetItem([PyObject](structures.html#c.PyObject)*list,[Py_ssize_t](intro.html#c.Py_ssize_t)index,[PyObject](structures.html#c.PyObject)*item)[¶](#c.PyList_SetItem)
- *Part of the*- [Stable ABI](stable.html#stable).- Set the item at index - *index*in list to- *item*. Return- `0`on success. If- *index*is out of bounds, return- `-1`and set an- `IndexError`- Note - This function “steals” a reference to - *item*and discards a reference to an item already in the list at the affected position.

- 
void PyList_SET_ITEM([PyObject](structures.html#c.PyObject)*list,[Py_ssize_t](intro.html#c.Py_ssize_t)i,[PyObject](structures.html#c.PyObject)*o)[¶](#c.PyList_SET_ITEM)
- Macro form of - `PyList_SetItem()`- Bounds checking is performed as an assertion if Python is built in - [debug mode](../using/configure.html#debug-build)or- `with assertions`- Note - This macro “steals” a reference to - *item*, and, unlike- `PyList_SetItem()`- *not*discard a reference to any item that is being replaced; any reference in- *list*at position- *i*will be leaked.

- 
int PyList_Insert([PyObject](structures.html#c.PyObject)*list,[Py_ssize_t](intro.html#c.Py_ssize_t)index,[PyObject](structures.html#c.PyObject)*item)[¶](#c.PyList_Insert)
- *Part of the*- [Stable ABI](stable.html#stable).- Insert the item - *item*into list- *list*in front of index- *index*. Return- `0`if successful; return- `-1`and set an exception if unsuccessful. Analogous to- `list.insert(index, item)`.

- 
int PyList_Append([PyObject](structures.html#c.PyObject)*list,[PyObject](structures.html#c.PyObject)*item)[¶](#c.PyList_Append)
- *Part of the*- [Stable ABI](stable.html#stable).- Append the object - *item*at the end of list- *list*. Return- `0`if successful; return- `-1`and set an exception if unsuccessful. Analogous to- `list.append(item)`.

- 
[PyObject](structures.html#c.PyObject)*PyList_GetSlice([PyObject](structures.html#c.PyObject)*list,[Py_ssize_t](intro.html#c.Py_ssize_t)low,[Py_ssize_t](intro.html#c.Py_ssize_t)high)[¶](#c.PyList_GetSlice)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a list of the objects in - *list*containing the objects- *between*- *low*and- *high*. Return- `NULL`and set an exception if unsuccessful. Analogous to- `list[low:high]`. Indexing from the end of the list is not supported.

- 
int PyList_SetSlice([PyObject](structures.html#c.PyObject)*list,[Py_ssize_t](intro.html#c.Py_ssize_t)low,[Py_ssize_t](intro.html#c.Py_ssize_t)high,[PyObject](structures.html#c.PyObject)*itemlist)[¶](#c.PyList_SetSlice)
- *Part of the*- [Stable ABI](stable.html#stable).- Set the slice of - *list*between- *low*and- *high*to the contents of- *itemlist*. Analogous to- `list[low:high] = itemlist`. The- *itemlist*may be- `NULL`, indicating the assignment of an empty list (slice deletion). Return- `0`on success,- `-1`on failure. Indexing from the end of the list is not supported.

- 
int PyList_Extend([PyObject](structures.html#c.PyObject)*list,[PyObject](structures.html#c.PyObject)*iterable)[¶](#c.PyList_Extend)
- Extend - *list*with the contents of- *iterable*. This is the same as- `PyList_SetSlice(list, PY_SSIZE_T_MAX, PY_SSIZE_T_MAX, iterable)`and analogous to- `list.extend(iterable)`or- `list += iterable`.- Raise an exception and return - `-1`if- *list*is not a- `list`- Added in version 3.13. 

- 
int PyList_Clear([PyObject](structures.html#c.PyObject)*list)[¶](#c.PyList_Clear)
- Remove all items from - *list*. This is the same as- `PyList_SetSlice(list, 0, PY_SSIZE_T_MAX, NULL)`and analogous to- `list.clear()`or- `del list[:]`.- Raise an exception and return - `-1`if- *list*is not a- `list`- Added in version 3.13. 

- 
int PyList_Sort([PyObject](structures.html#c.PyObject)*list)[¶](#c.PyList_Sort)
- *Part of the*- [Stable ABI](stable.html#stable).- Sort the items of - *list*in place. Return- `0`on success,- `-1`on failure. This is equivalent to- `list.sort()`.

- 
int PyList_Reverse([PyObject](structures.html#c.PyObject)*list)[¶](#c.PyList_Reverse)
- *Part of the*- [Stable ABI](stable.html#stable).- Reverse the items of - *list*in place. Return- `0`on success,- `-1`on failure. This is the equivalent of- `list.reverse()`.

- 
[PyObject](structures.html#c.PyObject)*PyList_AsTuple([PyObject](structures.html#c.PyObject)*list)[¶](#c.PyList_AsTuple)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a new tuple object containing the contents of - *list*; equivalent to- `tuple(list)`.