# Object Protocol — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/object.html](https://docs.python.org/3.13/c-api/object.html)

---

# Object Protocol[¶](#object-protocol)

- 
[PyObject](structures.html#c.PyObject)*Py_GetConstant(unsigned int constant_id)[¶](#c.Py_GetConstant)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Get a - [strong reference](../glossary.html#term-strong-reference)to a constant.- Set an exception and return - `NULL`if- *constant_id*is invalid.- *constant_id*must be one of these constant identifiers:- Constant Identifier - Value - Returned object - 
Py_CONSTANT_NONE[¶](#c.Py_CONSTANT_NONE)
 - `0`- 
Py_CONSTANT_FALSE[¶](#c.Py_CONSTANT_FALSE)
 - `1`- 
Py_CONSTANT_TRUE[¶](#c.Py_CONSTANT_TRUE)
 - `2`- 
Py_CONSTANT_ELLIPSIS[¶](#c.Py_CONSTANT_ELLIPSIS)
 - `3`- 
Py_CONSTANT_NOT_IMPLEMENTED[¶](#c.Py_CONSTANT_NOT_IMPLEMENTED)
 - `4`- 
Py_CONSTANT_ZERO[¶](#c.Py_CONSTANT_ZERO)
 - `5`- `0`- 
Py_CONSTANT_ONE[¶](#c.Py_CONSTANT_ONE)
 - `6`- `1`- 
Py_CONSTANT_EMPTY_STR[¶](#c.Py_CONSTANT_EMPTY_STR)
 - `7`- `''`- 
Py_CONSTANT_EMPTY_BYTES[¶](#c.Py_CONSTANT_EMPTY_BYTES)
 - `8`- `b''`- 
Py_CONSTANT_EMPTY_TUPLE[¶](#c.Py_CONSTANT_EMPTY_TUPLE)
 - `9`- `()`- Numeric values are only given for projects which cannot use the constant identifiers. - Added in version 3.13. - **CPython implementation detail:**In CPython, all of these constants are- [immortal](../glossary.html#term-immortal).
- 
Py_CONSTANT_NONE

- 
[PyObject](structures.html#c.PyObject)*Py_GetConstantBorrowed(unsigned int constant_id)[¶](#c.Py_GetConstantBorrowed)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Similar to - `Py_GetConstant()`- [borrowed reference](../glossary.html#term-borrowed-reference).- This function is primarily intended for backwards compatibility: using - `Py_GetConstant()`- The reference is borrowed from the interpreter, and is valid until the interpreter finalization. - Added in version 3.13. 

- 
[PyObject](structures.html#c.PyObject)*Py_NotImplemented[¶](#c.Py_NotImplemented)
- The - `NotImplemented`singleton, used to signal that an operation is not implemented for the given type combination.

- 
Py_RETURN_NOTIMPLEMENTED[¶](#c.Py_RETURN_NOTIMPLEMENTED)
- Properly handle returning - `Py_NotImplemented`- [strong reference](../glossary.html#term-strong-reference)to- `NotImplemented`

- 
Py_PRINT_RAW[¶](#c.Py_PRINT_RAW)
- Flag to be used with multiple functions that print the object (like - `PyObject_Print()`- `PyFile_WriteObject()`- `str()`- `repr()`

- 
int PyObject_Print([PyObject](structures.html#c.PyObject)*o, FILE *fp, int flags)[¶](#c.PyObject_Print)
- Print an object - *o*, on file- *fp*. Returns- `-1`on error. The flags argument is used to enable certain printing options. The only option currently supported is- `Py_PRINT_RAW`- `str()`- `repr()`

- 
int PyObject_HasAttrWithError([PyObject](structures.html#c.PyObject)*o,[PyObject](structures.html#c.PyObject)*attr_name)[¶](#c.PyObject_HasAttrWithError)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Returns - `1`if- *o*has the attribute- *attr_name*, and- `0`otherwise. This is equivalent to the Python expression- `hasattr(o, attr_name)`. On failure, return- `-1`.- Added in version 3.13. 

- 
int PyObject_HasAttrStringWithError([PyObject](structures.html#c.PyObject)*o, const char *attr_name)[¶](#c.PyObject_HasAttrStringWithError)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- This is the same as - `PyObject_HasAttrWithError()`- *attr_name*is specified as a const char* UTF-8 encoded bytes string, rather than a- [PyObject](structures.html#c.PyObject)*.- Added in version 3.13. 

- 
int PyObject_HasAttr([PyObject](structures.html#c.PyObject)*o,[PyObject](structures.html#c.PyObject)*attr_name)[¶](#c.PyObject_HasAttr)
- *Part of the*- [Stable ABI](stable.html#stable).- Returns - `1`if- *o*has the attribute- *attr_name*, and- `0`otherwise. This function always succeeds.- Note - Exceptions that occur when this calls - `__getattr__()`- `__getattribute__()`- `sys.unraisablehook()`- `PyObject_HasAttrWithError()`- `PyObject_GetOptionalAttr()`- `PyObject_GetAttr()`

- 
int PyObject_HasAttrString([PyObject](structures.html#c.PyObject)*o, const char *attr_name)[¶](#c.PyObject_HasAttrString)
- *Part of the*- [Stable ABI](stable.html#stable).- This is the same as - `PyObject_HasAttr()`- *attr_name*is specified as a const char* UTF-8 encoded bytes string, rather than a- [PyObject](structures.html#c.PyObject)*.- Note - Exceptions that occur when this calls - `__getattr__()`- `__getattribute__()`- `str`- `PyObject_HasAttrStringWithError()`- `PyObject_GetOptionalAttrString()`- `PyObject_GetAttrString()`

- 
[PyObject](structures.html#c.PyObject)*PyObject_GetAttr([PyObject](structures.html#c.PyObject)*o,[PyObject](structures.html#c.PyObject)*attr_name)[¶](#c.PyObject_GetAttr)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Retrieve an attribute named - *attr_name*from object- *o*. Returns the attribute value on success, or- `NULL`on failure. This is the equivalent of the Python expression- `o.attr_name`.- If the missing attribute should not be treated as a failure, you can use - `PyObject_GetOptionalAttr()`

- 
[PyObject](structures.html#c.PyObject)*PyObject_GetAttrString([PyObject](structures.html#c.PyObject)*o, const char *attr_name)[¶](#c.PyObject_GetAttrString)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- This is the same as - `PyObject_GetAttr()`- *attr_name*is specified as a const char* UTF-8 encoded bytes string, rather than a- [PyObject](structures.html#c.PyObject)*.- If the missing attribute should not be treated as a failure, you can use - `PyObject_GetOptionalAttrString()`

- 
int PyObject_GetOptionalAttr([PyObject](structures.html#c.PyObject)*obj,[PyObject](structures.html#c.PyObject)*attr_name,[PyObject](structures.html#c.PyObject)**result);[¶](#c.PyObject_GetOptionalAttr)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Variant of - `PyObject_GetAttr()`- `AttributeError`- If the attribute is found, return - `1`and set- **result*to a new- [strong reference](../glossary.html#term-strong-reference)to the attribute. If the attribute is not found, return- `0`and set- **result*to- `NULL`; the- `AttributeError`- `AttributeError`is raised, return- `-1`and set- **result*to- `NULL`.- Added in version 3.13. 

- 
int PyObject_GetOptionalAttrString([PyObject](structures.html#c.PyObject)*obj, const char *attr_name,[PyObject](structures.html#c.PyObject)**result);[¶](#c.PyObject_GetOptionalAttrString)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- This is the same as - `PyObject_GetOptionalAttr()`- *attr_name*is specified as a const char* UTF-8 encoded bytes string, rather than a- [PyObject](structures.html#c.PyObject)*.- Added in version 3.13. 

- 
[PyObject](structures.html#c.PyObject)*PyObject_GenericGetAttr([PyObject](structures.html#c.PyObject)*o,[PyObject](structures.html#c.PyObject)*name)[¶](#c.PyObject_GenericGetAttr)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Generic attribute getter function that is meant to be put into a type object’s - `tp_getattro`slot. It looks for a descriptor in the dictionary of classes in the object’s MRO as well as an attribute in the object’s- `__dict__`- [Implementing Descriptors](../reference/datamodel.html#descriptors), data descriptors take preference over instance attributes, while non-data descriptors don’t. Otherwise, an- `AttributeError`

- 
int PyObject_SetAttr([PyObject](structures.html#c.PyObject)*o,[PyObject](structures.html#c.PyObject)*attr_name,[PyObject](structures.html#c.PyObject)*v)[¶](#c.PyObject_SetAttr)
- *Part of the*- [Stable ABI](stable.html#stable).- Set the value of the attribute named - *attr_name*, for object- *o*, to the value- *v*. Raise an exception and return- `-1`on failure; return- `0`on success. This is the equivalent of the Python statement- `o.attr_name = v`.- If - *v*is- `NULL`, the attribute is deleted. This behaviour is deprecated in favour of using- `PyObject_DelAttr()`

- 
int PyObject_SetAttrString([PyObject](structures.html#c.PyObject)*o, const char *attr_name,[PyObject](structures.html#c.PyObject)*v)[¶](#c.PyObject_SetAttrString)
- *Part of the*- [Stable ABI](stable.html#stable).- This is the same as - `PyObject_SetAttr()`- *attr_name*is specified as a const char* UTF-8 encoded bytes string, rather than a- [PyObject](structures.html#c.PyObject)*.- If - *v*is- `NULL`, the attribute is deleted, but this feature is deprecated in favour of using- `PyObject_DelAttrString()`- The number of different attribute names passed to this function should be kept small, usually by using a statically allocated string as - *attr_name*. For attribute names that aren’t known at compile time, prefer calling- `PyUnicode_FromString()`- `PyObject_SetAttr()`- `PyUnicode_InternFromString()`

- 
int PyObject_GenericSetAttr([PyObject](structures.html#c.PyObject)*o,[PyObject](structures.html#c.PyObject)*name,[PyObject](structures.html#c.PyObject)*value)[¶](#c.PyObject_GenericSetAttr)
- *Part of the*- [Stable ABI](stable.html#stable).- Generic attribute setter and deleter function that is meant to be put into a type object’s - `tp_setattro`- `__dict__`- `0`is returned, otherwise an- `AttributeError`- `-1`is returned.

- 
int PyObject_DelAttr([PyObject](structures.html#c.PyObject)*o,[PyObject](structures.html#c.PyObject)*attr_name)[¶](#c.PyObject_DelAttr)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Delete attribute named - *attr_name*, for object- *o*. Returns- `-1`on failure. This is the equivalent of the Python statement- `del o.attr_name`.

- 
int PyObject_DelAttrString([PyObject](structures.html#c.PyObject)*o, const char *attr_name)[¶](#c.PyObject_DelAttrString)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- This is the same as - `PyObject_DelAttr()`- *attr_name*is specified as a const char* UTF-8 encoded bytes string, rather than a- [PyObject](structures.html#c.PyObject)*.- The number of different attribute names passed to this function should be kept small, usually by using a statically allocated string as - *attr_name*. For attribute names that aren’t known at compile time, prefer calling- `PyUnicode_FromString()`- `PyObject_DelAttr()`- `PyUnicode_InternFromString()`

- 
[PyObject](structures.html#c.PyObject)*PyObject_GenericGetDict([PyObject](structures.html#c.PyObject)*o, void *context)[¶](#c.PyObject_GenericGetDict)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- A generic implementation for the getter of a - `__dict__`descriptor. It creates the dictionary if necessary.- This function may also be called to get the - `__dict__`- *o*. Pass- `NULL`for- *context*when calling it. Since this function may need to allocate memory for the dictionary, it may be more efficient to call- `PyObject_GetAttr()`- On failure, returns - `NULL`with an exception set.- Added in version 3.3. 

- 
int PyObject_GenericSetDict([PyObject](structures.html#c.PyObject)*o,[PyObject](structures.html#c.PyObject)*value, void *context)[¶](#c.PyObject_GenericSetDict)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- A generic implementation for the setter of a - `__dict__`descriptor. This implementation does not allow the dictionary to be deleted.- Added in version 3.3. 

- 
[PyObject](structures.html#c.PyObject)**_PyObject_GetDictPtr([PyObject](structures.html#c.PyObject)*obj)[¶](#c._PyObject_GetDictPtr)
- Return a pointer to - `__dict__`- *obj*. If there is no- `__dict__`, return- `NULL`without setting an exception.- This function may need to allocate memory for the dictionary, so it may be more efficient to call - `PyObject_GetAttr()`

- 
[PyObject](structures.html#c.PyObject)*PyObject_RichCompare([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2, int opid)[¶](#c.PyObject_RichCompare)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Compare the values of - *o1*and- *o2*using the operation specified by- *opid*, which must be one of- `Py_LT`- `Py_LE`- `Py_EQ`- `Py_NE`- `Py_GT`- `Py_GE`- `<`,- `<=`,- `==`,- `!=`,- `>`, or- `>=`respectively. This is the equivalent of the Python expression- `o1 op o2`, where- `op`is the operator corresponding to- *opid*. Returns the value of the comparison on success, or- `NULL`on failure.

- 
int PyObject_RichCompareBool([PyObject](structures.html#c.PyObject)*o1,[PyObject](structures.html#c.PyObject)*o2, int opid)[¶](#c.PyObject_RichCompareBool)
- *Part of the*- [Stable ABI](stable.html#stable).- Compare the values of - *o1*and- *o2*using the operation specified by- *opid*, like- `PyObject_RichCompare()`- `-1`on error,- `0`if the result is false,- `1`otherwise.

Note

If *o1* and *o2* are the same object, [ PyObject_RichCompareBool()](#c.PyObject_RichCompareBool)
will always return 

`1` for [and](typeobj.html#c.Py_EQ)

`Py_EQ``0` for [.](typeobj.html#c.Py_NE)

`Py_NE`- 
[PyObject](structures.html#c.PyObject)*PyObject_Format([PyObject](structures.html#c.PyObject)*obj,[PyObject](structures.html#c.PyObject)*format_spec)[¶](#c.PyObject_Format)
- *Part of the*- [Stable ABI](stable.html#stable).- Format - *obj*using- *format_spec*. This is equivalent to the Python expression- `format(obj, format_spec)`.- *format_spec*may be- `NULL`. In this case the call is equivalent to- `format(obj)`. Returns the formatted string on success,- `NULL`on failure.

- 
[PyObject](structures.html#c.PyObject)*PyObject_Repr([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyObject_Repr)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Compute a string representation of object - *o*. Returns the string representation on success,- `NULL`on failure. This is the equivalent of the Python expression- `repr(o)`. Called by the- `repr()`- If argument is - `NULL`, return the string- `'<NULL>'`.- Changed in version 3.4: This function now includes a debug assertion to help ensure that it does not silently discard an active exception. 

- 
[PyObject](structures.html#c.PyObject)*PyObject_ASCII([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyObject_ASCII)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- As - `PyObject_Repr()`- *o*, but escape the non-ASCII characters in the string returned by- `PyObject_Repr()`with- `\x`,- `\u`or- `\U`escapes. This generates a string similar to that returned by- `PyObject_Repr()`in Python 2. Called by the- `ascii()`- If argument is - `NULL`, return the string- `'<NULL>'`.

- 
[PyObject](structures.html#c.PyObject)*PyObject_Str([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyObject_Str)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Compute a string representation of object - *o*. Returns the string representation on success,- `NULL`on failure. This is the equivalent of the Python expression- `str(o)`. Called by the- `str()`- `print()`- If argument is - `NULL`, return the string- `'<NULL>'`.- Changed in version 3.4: This function now includes a debug assertion to help ensure that it does not silently discard an active exception. 

- 
[PyObject](structures.html#c.PyObject)*PyObject_Bytes([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyObject_Bytes)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Compute a bytes representation of object - *o*.- `NULL`is returned on failure and a bytes object on success. This is equivalent to the Python expression- `bytes(o)`, when- *o*is not an integer. Unlike- `bytes(o)`, a TypeError is raised when- *o*is an integer instead of a zero-initialized bytes object.- If argument is - `NULL`, return the- `bytes`- `b'<NULL>'`.

- 
int PyObject_IsSubclass([PyObject](structures.html#c.PyObject)*derived,[PyObject](structures.html#c.PyObject)*cls)[¶](#c.PyObject_IsSubclass)
- *Part of the*- [Stable ABI](stable.html#stable).- Return - `1`if the class- *derived*is identical to or derived from the class- *cls*, otherwise return- `0`. In case of an error, return- `-1`.- If - *cls*is a tuple, the check will be done against every entry in- *cls*. The result will be- `1`when at least one of the checks returns- `1`, otherwise it will be- `0`.- If - *cls*has a- `__subclasscheck__()`- **PEP 3119**- *derived*is a subclass of- *cls*if it is a direct or indirect subclass, i.e. contained in- `cls.__mro__`- Normally only class objects, i.e. instances of - `type`- `__bases__`

- 
int PyObject_IsInstance([PyObject](structures.html#c.PyObject)*inst,[PyObject](structures.html#c.PyObject)*cls)[¶](#c.PyObject_IsInstance)
- *Part of the*- [Stable ABI](stable.html#stable).- Return - `1`if- *inst*is an instance of the class- *cls*or a subclass of- *cls*, or- `0`if not. On error, returns- `-1`and sets an exception.- If - *cls*is a tuple, the check will be done against every entry in- *cls*. The result will be- `1`when at least one of the checks returns- `1`, otherwise it will be- `0`.- If - *cls*has a- `__instancecheck__()`- **PEP 3119**- *inst*is an instance of- *cls*if its class is a subclass of- *cls*.- An instance - *inst*can override what is considered its class by having a- `__class__`- An object - *cls*can override if it is considered a class, and what its base classes are, by having a- `__bases__`

- 
[Py_hash_t](hash.html#c.Py_hash_t)PyObject_Hash([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyObject_Hash)
- *Part of the*- [Stable ABI](stable.html#stable).- Compute and return the hash value of an object - *o*. On failure, return- `-1`. This is the equivalent of the Python expression- `hash(o)`.- Changed in version 3.2: The return type is now Py_hash_t. This is a signed integer the same size as - `Py_ssize_t`

- 
[Py_hash_t](hash.html#c.Py_hash_t)PyObject_HashNotImplemented([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyObject_HashNotImplemented)
- *Part of the*- [Stable ABI](stable.html#stable).- Set a - `TypeError`- `type(o)`is not- [hashable](../glossary.html#term-hashable)and return- `-1`. This function receives special treatment when stored in a- `tp_hash`slot, allowing a type to explicitly indicate to the interpreter that it is not hashable.

- 
int PyObject_IsTrue([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyObject_IsTrue)
- *Part of the*- [Stable ABI](stable.html#stable).- Returns - `1`if the object- *o*is considered to be true, and- `0`otherwise. This is equivalent to the Python expression- `not not o`. On failure, return- `-1`.

- 
int PyObject_Not([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyObject_Not)
- *Part of the*- [Stable ABI](stable.html#stable).- Returns - `0`if the object- *o*is considered to be true, and- `1`otherwise. This is equivalent to the Python expression- `not o`. On failure, return- `-1`.

- 
[PyObject](structures.html#c.PyObject)*PyObject_Type([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyObject_Type)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- When - *o*is non-- `NULL`, returns a type object corresponding to the object type of object- *o*. On failure, raises- `SystemError`- `NULL`. This is equivalent to the Python expression- `type(o)`. This function creates a new- [strong reference](../glossary.html#term-strong-reference)to the return value. There’s really no reason to use this function instead of the- `Py_TYPE()`- [PyTypeObject](type.html#c.PyTypeObject)*, except when a new strong reference is needed.

- 
int PyObject_TypeCheck([PyObject](structures.html#c.PyObject)*o,[PyTypeObject](type.html#c.PyTypeObject)*type)[¶](#c.PyObject_TypeCheck)
- Return non-zero if the object - *o*is of type- *type*or a subtype of- *type*, and- `0`otherwise. Both parameters must be non-- `NULL`.

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyObject_Size([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyObject_Size)
- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyObject_Length([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyObject_Length)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the length of object - *o*. If the object- *o*provides either the sequence and mapping protocols, the sequence length is returned. On error,- `-1`is returned. This is the equivalent to the Python expression- `len(o)`.

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyObject_LengthHint([PyObject](structures.html#c.PyObject)*o,[Py_ssize_t](intro.html#c.Py_ssize_t)defaultvalue)[¶](#c.PyObject_LengthHint)
- Return an estimated length for the object - *o*. First try to return its actual length, then an estimate using- `__length_hint__()`- `-1`. This is the equivalent to the Python expression- `operator.length_hint(o, defaultvalue)`.- Added in version 3.4. 

- 
[PyObject](structures.html#c.PyObject)*PyObject_GetItem([PyObject](structures.html#c.PyObject)*o,[PyObject](structures.html#c.PyObject)*key)[¶](#c.PyObject_GetItem)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return element of - *o*corresponding to the object- *key*or- `NULL`on failure. This is the equivalent of the Python expression- `o[key]`.

- 
int PyObject_SetItem([PyObject](structures.html#c.PyObject)*o,[PyObject](structures.html#c.PyObject)*key,[PyObject](structures.html#c.PyObject)*v)[¶](#c.PyObject_SetItem)
- *Part of the*- [Stable ABI](stable.html#stable).- Map the object - *key*to the value- *v*. Raise an exception and return- `-1`on failure; return- `0`on success. This is the equivalent of the Python statement- `o[key] = v`. This function- *does not*steal a reference to- *v*.

- 
int PyObject_DelItem([PyObject](structures.html#c.PyObject)*o,[PyObject](structures.html#c.PyObject)*key)[¶](#c.PyObject_DelItem)
- *Part of the*- [Stable ABI](stable.html#stable).- Remove the mapping for the object - *key*from the object- *o*. Return- `-1`on failure. This is equivalent to the Python statement- `del o[key]`.

- 
int PyObject_DelItemString([PyObject](structures.html#c.PyObject)*o, const char *key)[¶](#c.PyObject_DelItemString)
- *Part of the*- [Stable ABI](stable.html#stable).- This is the same as - `PyObject_DelItem()`- *key*is specified as a const char* UTF-8 encoded bytes string, rather than a- [PyObject](structures.html#c.PyObject)*.

- 
[PyObject](structures.html#c.PyObject)*PyObject_Dir([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyObject_Dir)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- This is equivalent to the Python expression - `dir(o)`, returning a (possibly empty) list of strings appropriate for the object argument, or- `NULL`if there was an error. If the argument is- `NULL`, this is like the Python- `dir()`, returning the names of the current locals; in this case, if no execution frame is active then- `NULL`is returned but- `PyErr_Occurred()`

- 
[PyObject](structures.html#c.PyObject)*PyObject_GetIter([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyObject_GetIter)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- This is equivalent to the Python expression - `iter(o)`. It returns a new iterator for the object argument, or the object itself if the object is already an iterator. Raises- `TypeError`- `NULL`if the object cannot be iterated.

- 
[PyObject](structures.html#c.PyObject)*PyObject_SelfIter([PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyObject_SelfIter)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- This is equivalent to the Python - `__iter__(self): return self`method. It is intended for- [iterator](../glossary.html#term-iterator)types, to be used in the- `PyTypeObject.tp_iter`

- 
[PyObject](structures.html#c.PyObject)*PyObject_GetAIter([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyObject_GetAIter)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- This is the equivalent to the Python expression - `aiter(o)`. Takes an- `AsyncIterable`object and returns an- `AsyncIterator`for it. This is typically a new iterator but if the argument is an- `AsyncIterator`, this returns itself. Raises- `TypeError`- `NULL`if the object cannot be iterated.- Added in version 3.10. 

- 
void *PyObject_GetTypeData([PyObject](structures.html#c.PyObject)*o,[PyTypeObject](type.html#c.PyTypeObject)*cls)[¶](#c.PyObject_GetTypeData)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.12.- Get a pointer to subclass-specific data reserved for - *cls*.- The object - *o*must be an instance of- *cls*, and- *cls*must have been created using negative- `PyType_Spec.basicsize`- On error, set an exception and return - `NULL`.- Added in version 3.12. 

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyType_GetTypeDataSize([PyTypeObject](type.html#c.PyTypeObject)*cls)[¶](#c.PyType_GetTypeDataSize)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.12.- Return the size of the instance memory space reserved for - *cls*, i.e. the size of the memory- `PyObject_GetTypeData()`- This may be larger than requested using - `-PyType_Spec.basicsize`- `memset()`).- The type - *cls*- **must**have been created using negative- `PyType_Spec.basicsize`- On error, set an exception and return a negative value. - Added in version 3.12. 

- 
void *PyObject_GetItemData([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyObject_GetItemData)
- Get a pointer to per-item data for a class with - `Py_TPFLAGS_ITEMS_AT_END`- On error, set an exception and return - `NULL`.- `TypeError`- *o*does not have- `Py_TPFLAGS_ITEMS_AT_END`- Added in version 3.12. 

- 
int PyObject_VisitManagedDict([PyObject](structures.html#c.PyObject)*obj,[visitproc](gcsupport.html#c.visitproc)visit, void *arg)[¶](#c.PyObject_VisitManagedDict)
- Visit the managed dictionary of - *obj*.- This function must only be called in a traverse function of the type which has the - `Py_TPFLAGS_MANAGED_DICT`- Added in version 3.13. 

- 
void PyObject_ClearManagedDict([PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyObject_ClearManagedDict)
- Clear the managed dictionary of - *obj*.- This function must only be called in a clear function of the type which has the - `Py_TPFLAGS_MANAGED_DICT`- Added in version 3.13.