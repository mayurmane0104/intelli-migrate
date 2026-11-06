# Bytes Objects — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/bytes.html](https://docs.python.org/c-api/bytes.html)

---

# Bytes Objects[¶](#bytes-objects)

These functions raise [ TypeError](../library/exceptions.html#TypeError) when expecting a bytes parameter and
called with a non-bytes parameter.

- 
[PyTypeObject](type.html#c.PyTypeObject)PyBytes_Type[¶](#c.PyBytes_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- This instance of - `PyTypeObject`- `bytes`

- 
int PyBytes_Check([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyBytes_Check)
- Return true if the object - *o*is a bytes object or an instance of a subtype of the bytes type. This function always succeeds.

- 
int PyBytes_CheckExact([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyBytes_CheckExact)
- Return true if the object - *o*is a bytes object, but not an instance of a subtype of the bytes type. This function always succeeds.

- 
[PyObject](structures.html#c.PyObject)*PyBytes_FromString(const char *v)[¶](#c.PyBytes_FromString)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Atomic](../library/threadsafety.html#threadsafety-level-atomic).- Return a new bytes object with a copy of the string - *v*as value on success, and- `NULL`on failure. The parameter- *v*must not be- `NULL`; it will not be checked.

- 
[PyObject](structures.html#c.PyObject)*PyBytes_FromStringAndSize(const char *v,[Py_ssize_t](intro.html#c.Py_ssize_t)len)[¶](#c.PyBytes_FromStringAndSize)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Atomic](../library/threadsafety.html#threadsafety-level-atomic).- Return a new bytes object with a copy of the string - *v*as value and length- *len*on success, and- `NULL`on failure. If- *v*is- `NULL`, the contents of the bytes object are uninitialized.

- 
[PyObject](structures.html#c.PyObject)*PyBytes_FromFormat(const char *format, ...)[¶](#c.PyBytes_FromFormat)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Atomic](../library/threadsafety.html#threadsafety-level-atomic).- Take a C - `printf()`-style- *format*string and a variable number of arguments, calculate the size of the resulting Python bytes object and return a bytes object with the values formatted into it. The variable arguments must be C types and must correspond exactly to the format characters in the- *format*string. The following format characters are allowed:- Format Characters - Type - Comment - `%%`- *n/a*- The literal % character. - `%c`- int - A single byte, represented as a C int. - `%d`- int - Equivalent to - `printf("%d")`.- [[1]](#id9)- `%u`- unsigned int - Equivalent to - `printf("%u")`.- [[1]](#id9)- `%ld`- long - Equivalent to - `printf("%ld")`.- [[1]](#id9)- `%lu`- unsigned long - Equivalent to - `printf("%lu")`.- [[1]](#id9)- `%zd`- Equivalent to - `printf("%zd")`.- [[1]](#id9)- `%zu`- size_t - Equivalent to - `printf("%zu")`.- [[1]](#id9)- `%i`- int - Equivalent to - `printf("%i")`.- [[1]](#id9)- `%x`- int - Equivalent to - `printf("%x")`.- [[1]](#id9)- `%s`- const char* - A null-terminated C character array. - `%p`- const void* - The hex representation of a C pointer. Mostly equivalent to - `printf("%p")`except that it is guaranteed to start with the literal- `0x`regardless of what the platform’s- `printf`yields.- An unrecognized format character causes all the rest of the format string to be copied as-is to the result object, and any extra arguments discarded. 

- 
[PyObject](structures.html#c.PyObject)*PyBytes_FromFormatV(const char *format, va_list vargs)[¶](#c.PyBytes_FromFormatV)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Atomic](../library/threadsafety.html#threadsafety-level-atomic).- Identical to - `PyBytes_FromFormat()`

- 
[PyObject](structures.html#c.PyObject)*PyBytes_FromObject([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyBytes_FromObject)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Safe for concurrent use on the same object](../library/threadsafety.html#threadsafety-level-shared).- Return the bytes representation of object - *o*that implements the buffer protocol.- Note - If the object implements the buffer protocol, then the buffer must not be mutated while the bytes object is being created. 

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyBytes_Size([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyBytes_Size)
- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Atomic](../library/threadsafety.html#threadsafety-level-atomic).- Return the length of the bytes in bytes object - *o*.

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyBytes_GET_SIZE([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyBytes_GET_SIZE)
- *Thread safety:*- [Atomic](../library/threadsafety.html#threadsafety-level-atomic).- Similar to - `PyBytes_Size()`

- 
char *PyBytes_AsString([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyBytes_AsString)
- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Safe to call from multiple threads with external synchronization only](../library/threadsafety.html#threadsafety-level-compatible).- Return a pointer to the contents of - *o*. The pointer refers to the internal buffer of- *o*, which consists of- `len(o) + 1`bytes. The last byte in the buffer is always null, regardless of whether there are any other null bytes. The data must not be modified in any way, unless the object was just created using- `PyBytes_FromStringAndSize(NULL, size)`. It must not be deallocated. If- *o*is not a bytes object at all,- `PyBytes_AsString()`- `NULL`and raises- `TypeError`

- 
char *PyBytes_AS_STRING([PyObject](structures.html#c.PyObject)*string)[¶](#c.PyBytes_AS_STRING)
- *Thread safety:*- [Safe to call from multiple threads with external synchronization only](../library/threadsafety.html#threadsafety-level-compatible).- Similar to - `PyBytes_AsString()`

- 
int PyBytes_AsStringAndSize([PyObject](structures.html#c.PyObject)*obj, char **buffer,[Py_ssize_t](intro.html#c.Py_ssize_t)*length)[¶](#c.PyBytes_AsStringAndSize)
- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Safe to call from multiple threads with external synchronization only](../library/threadsafety.html#threadsafety-level-compatible).- Return the null-terminated contents of the object - *obj*through the output variables- *buffer*and- *length*. Returns- `0`on success.- If - *length*is- `NULL`, the bytes object may not contain embedded null bytes; if it does, the function returns- `-1`and a- `ValueError`- The buffer refers to an internal buffer of - *obj*, which includes an additional null byte at the end (not counted in- *length*). The data must not be modified in any way, unless the object was just created using- `PyBytes_FromStringAndSize(NULL, size)`. It must not be deallocated. If- *obj*is not a bytes object at all,- `PyBytes_AsStringAndSize()`- `-1`and raises- `TypeError`- Changed in version 3.5: Previously, - `TypeError`

- 
void PyBytes_Concat([PyObject](structures.html#c.PyObject)**bytes,[PyObject](structures.html#c.PyObject)*newpart)[¶](#c.PyBytes_Concat)
- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Safe for concurrent use on the same object](../library/threadsafety.html#threadsafety-level-shared).- Create a new bytes object in - **bytes*containing the contents of- *newpart*appended to- *bytes*; the caller will own the new reference. The reference to the old value of- *bytes*will be stolen. If the new object cannot be created, the old reference to- *bytes*will still be discarded and the value of- **bytes*will be set to- `NULL`; the appropriate exception will be set.- Note - If - *newpart*implements the buffer protocol, then the buffer must not be mutated while the new bytes object is being created.

- 
void PyBytes_ConcatAndDel([PyObject](structures.html#c.PyObject)**bytes,[PyObject](structures.html#c.PyObject)*newpart)[¶](#c.PyBytes_ConcatAndDel)
- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Safe for concurrent use on the same object](../library/threadsafety.html#threadsafety-level-shared).- Create a new bytes object in - **bytes*containing the contents of- *newpart*appended to- *bytes*. This version releases the- [strong reference](../glossary.html#term-strong-reference)to- *newpart*(i.e. decrements its reference count).- Note - If - *newpart*implements the buffer protocol, then the buffer must not be mutated while the new bytes object is being created.

- 
[PyObject](structures.html#c.PyObject)*PyBytes_Join([PyObject](structures.html#c.PyObject)*sep,[PyObject](structures.html#c.PyObject)*iterable)[¶](#c.PyBytes_Join)
- *Thread safety:*- [Safe for concurrent use on the same object](../library/threadsafety.html#threadsafety-level-shared).- Similar to - `sep.join(iterable)`in Python.- *sep*must be Python- `bytes`- `PyUnicode_Join()`- `NULL`separator and treats it as a space, whereas- `PyBytes_Join()`- `NULL`separator.)- *iterable*must be an iterable object yielding objects that implement the- [buffer protocol](buffer.html#bufferobjects).- On success, return a new - `bytes`- `NULL`.- Added in version 3.14. - Note - If - *iterable*objects implement the buffer protocol, then the buffers must not be mutated while the new bytes object is being created.

- 
int _PyBytes_Resize([PyObject](structures.html#c.PyObject)**bytes,[Py_ssize_t](intro.html#c.Py_ssize_t)newsize)[¶](#c._PyBytes_Resize)
- *Thread safety:*- [Safe to call without external synchronization on distinct objects](../library/threadsafety.html#threadsafety-level-distinct).- Resize a bytes object. - *newsize*will be the new length of the bytes object. You can think of it as creating a new bytes object and destroying the old one, only more efficiently. Pass the address of an existing bytes object as an lvalue (it may be written into), and the new size desired. On success,- **bytes*holds the resized bytes object and- `0`is returned; the address in- **bytes*may differ from its input value. If the reallocation fails, the original bytes object at- **bytes*is deallocated,- **bytes*is set to- `NULL`,- `MemoryError`- `-1`is returned.

- 
[PyObject](structures.html#c.PyObject)*PyBytes_Repr([PyObject](structures.html#c.PyObject)*bytes, int smartquotes)[¶](#c.PyBytes_Repr)
- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Atomic](../library/threadsafety.html#threadsafety-level-atomic).- Get the string representation of - *bytes*. This function is currently used to implement- `bytes.__repr__()`in Python.- This function does not do type checking; it is undefined behavior to pass - *bytes*as a non-bytes object or- `NULL`.- If - *smartquotes*is true, the representation will use a double-quoted string instead of single-quoted string when single-quotes are present in- *bytes*. For example, the byte string- `'Python'`would be represented as- `b"'Python'"`when- *smartquotes*is true, or- `b'\'Python\''`when it is false.- On success, this function returns a - [strong reference](../glossary.html#term-strong-reference)to a- `str`- `NULL`with an exception set.

- 
[PyObject](structures.html#c.PyObject)*PyBytes_DecodeEscape(const char *s,[Py_ssize_t](intro.html#c.Py_ssize_t)len, const char *errors,[Py_ssize_t](intro.html#c.Py_ssize_t)unicode, const char *recode_encoding)[¶](#c.PyBytes_DecodeEscape)
- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Atomic](../library/threadsafety.html#threadsafety-level-atomic).- Unescape a backslash-escaped string - *s*.- *s*must not be- `NULL`.- *len*must be the size of- *s*.- *errors*must be one of- `"strict"`,- `"replace"`, or- `"ignore"`. If- *errors*is- `NULL`, then- `"strict"`is used by default.- On success, this function returns a - [strong reference](../glossary.html#term-strong-reference)to a Python- `bytes`- `NULL`with an exception set.- Changed in version 3.9: - *unicode*and- *recode_encoding*are now unused.