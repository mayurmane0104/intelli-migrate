# Mapping Protocol — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/mapping.html](https://docs.python.org/3.13/c-api/mapping.html)

---

# Mapping Protocol[¶](#mapping-protocol)

See also [ PyObject_GetItem()](object.html#c.PyObject_GetItem), 

[and](object.html#c.PyObject_SetItem)

`PyObject_SetItem()`[.](object.html#c.PyObject_DelItem)

`PyObject_DelItem()`- 
int PyMapping_Check([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyMapping_Check)
- *Part of the*- [Stable ABI](stable.html#stable).- Return - `1`if the object provides the mapping protocol or supports slicing, and- `0`otherwise. Note that it returns- `1`for Python classes with a- `__getitem__()`

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyMapping_Size([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyMapping_Size)
- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyMapping_Length([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyMapping_Length)
- *Part of the*- [Stable ABI](stable.html#stable).- Returns the number of keys in object - *o*on success, and- `-1`on failure. This is equivalent to the Python expression- `len(o)`.

- 
[PyObject](structures.html#c.PyObject)*PyMapping_GetItemString([PyObject](structures.html#c.PyObject)*o, const char *key)[¶](#c.PyMapping_GetItemString)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- This is the same as - `PyObject_GetItem()`- *key*is specified as a const char* UTF-8 encoded bytes string, rather than a- [PyObject](structures.html#c.PyObject)*.

- 
int PyMapping_GetOptionalItem([PyObject](structures.html#c.PyObject)*obj,[PyObject](structures.html#c.PyObject)*key,[PyObject](structures.html#c.PyObject)**result)[¶](#c.PyMapping_GetOptionalItem)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Variant of - `PyObject_GetItem()`- `KeyError`- If the key is found, return - `1`and set- **result*to a new- [strong reference](../glossary.html#term-strong-reference)to the corresponding value. If the key is not found, return- `0`and set- **result*to- `NULL`; the- `KeyError`- `KeyError`is raised, return- `-1`and set- **result*to- `NULL`.- Added in version 3.13. 

- 
int PyMapping_GetOptionalItemString([PyObject](structures.html#c.PyObject)*obj, const char *key,[PyObject](structures.html#c.PyObject)**result)[¶](#c.PyMapping_GetOptionalItemString)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- This is the same as - `PyMapping_GetOptionalItem()`- *key*is specified as a const char* UTF-8 encoded bytes string, rather than a- [PyObject](structures.html#c.PyObject)*.- Added in version 3.13. 

- 
int PyMapping_SetItemString([PyObject](structures.html#c.PyObject)*o, const char *key,[PyObject](structures.html#c.PyObject)*v)[¶](#c.PyMapping_SetItemString)
- *Part of the*- [Stable ABI](stable.html#stable).- This is the same as - `PyObject_SetItem()`- *key*is specified as a const char* UTF-8 encoded bytes string, rather than a- [PyObject](structures.html#c.PyObject)*.

- 
int PyMapping_DelItem([PyObject](structures.html#c.PyObject)*o,[PyObject](structures.html#c.PyObject)*key)[¶](#c.PyMapping_DelItem)
- This is an alias of - `PyObject_DelItem()`

- 
int PyMapping_DelItemString([PyObject](structures.html#c.PyObject)*o, const char *key)[¶](#c.PyMapping_DelItemString)
- This is the same as - `PyObject_DelItem()`- *key*is specified as a const char* UTF-8 encoded bytes string, rather than a- [PyObject](structures.html#c.PyObject)*.

- 
int PyMapping_HasKeyWithError([PyObject](structures.html#c.PyObject)*o,[PyObject](structures.html#c.PyObject)*key)[¶](#c.PyMapping_HasKeyWithError)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Return - `1`if the mapping object has the key- *key*and- `0`otherwise. This is equivalent to the Python expression- `key in o`. On failure, return- `-1`.- Added in version 3.13. 

- 
int PyMapping_HasKeyStringWithError([PyObject](structures.html#c.PyObject)*o, const char *key)[¶](#c.PyMapping_HasKeyStringWithError)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- This is the same as - `PyMapping_HasKeyWithError()`- *key*is specified as a const char* UTF-8 encoded bytes string, rather than a- [PyObject](structures.html#c.PyObject)*.- Added in version 3.13. 

- 
int PyMapping_HasKey([PyObject](structures.html#c.PyObject)*o,[PyObject](structures.html#c.PyObject)*key)[¶](#c.PyMapping_HasKey)
- *Part of the*- [Stable ABI](stable.html#stable).- Return - `1`if the mapping object has the key- *key*and- `0`otherwise. This is equivalent to the Python expression- `key in o`. This function always succeeds.- Note - Exceptions which occur when this calls the - `__getitem__()`- `PyMapping_HasKeyWithError()`- `PyMapping_GetOptionalItem()`- `PyObject_GetItem()`

- 
int PyMapping_HasKeyString([PyObject](structures.html#c.PyObject)*o, const char *key)[¶](#c.PyMapping_HasKeyString)
- *Part of the*- [Stable ABI](stable.html#stable).- This is the same as - `PyMapping_HasKey()`- *key*is specified as a const char* UTF-8 encoded bytes string, rather than a- [PyObject](structures.html#c.PyObject)*.- Note - Exceptions that occur when this calls the - `__getitem__()`- `str`- `PyMapping_HasKeyStringWithError()`- `PyMapping_GetOptionalItemString()`- `PyMapping_GetItemString()`

- 
[PyObject](structures.html#c.PyObject)*PyMapping_Keys([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyMapping_Keys)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- On success, return a list of the keys in object - *o*. On failure, return- `NULL`.- Changed in version 3.7: Previously, the function returned a list or a tuple. 

- 
[PyObject](structures.html#c.PyObject)*PyMapping_Values([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyMapping_Values)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- On success, return a list of the values in object - *o*. On failure, return- `NULL`.- Changed in version 3.7: Previously, the function returned a list or a tuple. 

- 
[PyObject](structures.html#c.PyObject)*PyMapping_Items([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyMapping_Items)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- On success, return a list of the items in object - *o*, where each item is a tuple containing a key-value pair. On failure, return- `NULL`.- Changed in version 3.7: Previously, the function returned a list or a tuple.