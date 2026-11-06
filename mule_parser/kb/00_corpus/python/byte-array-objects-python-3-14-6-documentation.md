# Byte Array Objects — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/bytearray.html](https://docs.python.org/c-api/bytearray.html)

---

# Byte Array Objects[¶](#byte-array-objects)

- 
[PyTypeObject](type.html#c.PyTypeObject)PyByteArray_Type[¶](#c.PyByteArray_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- This instance of - `PyTypeObject`- `bytearray`

## Type check macros[¶](#type-check-macros)

## Direct API functions[¶](#direct-api-functions)

- 
[PyObject](structures.html#c.PyObject)*PyByteArray_FromObject([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyByteArray_FromObject)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Safe for concurrent use on the same object](../library/threadsafety.html#threadsafety-level-shared).- Return a new bytearray object from any object, - *o*, that implements the- [buffer protocol](buffer.html#bufferobjects).- On failure, return - `NULL`with an exception set.- Note - If the object implements the buffer protocol, then the buffer must not be mutated while the bytearray object is being created. 

- 
[PyObject](structures.html#c.PyObject)*PyByteArray_FromStringAndSize(const char *string,[Py_ssize_t](intro.html#c.Py_ssize_t)len)[¶](#c.PyByteArray_FromStringAndSize)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Atomic](../library/threadsafety.html#threadsafety-level-atomic).- Create a new bytearray object from - *string*and its length,- *len*.- On failure, return - `NULL`with an exception set.

- 
[PyObject](structures.html#c.PyObject)*PyByteArray_Concat([PyObject](structures.html#c.PyObject)*a,[PyObject](structures.html#c.PyObject)*b)[¶](#c.PyByteArray_Concat)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Safe for concurrent use on the same object](../library/threadsafety.html#threadsafety-level-shared).- Concat bytearrays - *a*and- *b*and return a new bytearray with the result.- On failure, return - `NULL`with an exception set.- Note - If the object implements the buffer protocol, then the buffer must not be mutated while the bytearray object is being created. 

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyByteArray_Size([PyObject](structures.html#c.PyObject)*bytearray)[¶](#c.PyByteArray_Size)
- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Atomic](../library/threadsafety.html#threadsafety-level-atomic).- Return the size of - *bytearray*after checking for a- `NULL`pointer.

- 
char *PyByteArray_AsString([PyObject](structures.html#c.PyObject)*bytearray)[¶](#c.PyByteArray_AsString)
- *Part of the*- [Stable ABI](stable.html#stable).- *Thread safety:*- [Safe to call from multiple threads with external synchronization only](../library/threadsafety.html#threadsafety-level-compatible).- Return the contents of - *bytearray*as a char array after checking for a- `NULL`pointer. The returned array always has an extra null byte appended.- Note - It is not thread-safe to mutate the bytearray object while using the returned char array. 

- 
int PyByteArray_Resize([PyObject](structures.html#c.PyObject)*bytearray,[Py_ssize_t](intro.html#c.Py_ssize_t)len)[¶](#c.PyByteArray_Resize)
- *Part of the*- [Stable ABI](stable.html#stable).- Resize the internal buffer of - *bytearray*to- *len*. Failure is a- `-1`return with an exception set.- Changed in version 3.14: A negative - *len*will now result in an exception being set and -1 returned.

## Macros[¶](#macros)

These macros trade safety for speed and they don’t check pointers.

- 
char *PyByteArray_AS_STRING([PyObject](structures.html#c.PyObject)*bytearray)[¶](#c.PyByteArray_AS_STRING)
- *Thread safety:*- [Safe to call from multiple threads with external synchronization only](../library/threadsafety.html#threadsafety-level-compatible).- Similar to - `PyByteArray_AsString()`- Note - It is not thread-safe to mutate the bytearray object while using the returned char array. 

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyByteArray_GET_SIZE([PyObject](structures.html#c.PyObject)*bytearray)[¶](#c.PyByteArray_GET_SIZE)
- *Thread safety:*- [Atomic](../library/threadsafety.html#threadsafety-level-atomic).- Similar to - `PyByteArray_Size()`