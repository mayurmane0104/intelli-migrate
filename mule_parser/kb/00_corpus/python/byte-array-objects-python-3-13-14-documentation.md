# Byte Array Objects — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/bytearray.html](https://docs.python.org/3.13/c-api/bytearray.html)

---

# Byte Array Objects[¶](#byte-array-objects)

- 
[PyTypeObject](type.html#c.PyTypeObject)PyByteArray_Type[¶](#c.PyByteArray_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- This instance of - `PyTypeObject`- `bytearray`

## Type check macros[¶](#type-check-macros)

## Direct API functions[¶](#direct-api-functions)

- 
[PyObject](structures.html#c.PyObject)*PyByteArray_FromObject([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyByteArray_FromObject)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return a new bytearray object from any object, - *o*, that implements the- [buffer protocol](buffer.html#bufferobjects).- On failure, return - `NULL`with an exception set.

- 
[PyObject](structures.html#c.PyObject)*PyByteArray_FromStringAndSize(const char *string,[Py_ssize_t](intro.html#c.Py_ssize_t)len)[¶](#c.PyByteArray_FromStringAndSize)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Create a new bytearray object from - *string*and its length,- *len*.- On failure, return - `NULL`with an exception set.

- 
[PyObject](structures.html#c.PyObject)*PyByteArray_Concat([PyObject](structures.html#c.PyObject)*a,[PyObject](structures.html#c.PyObject)*b)[¶](#c.PyByteArray_Concat)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Concat bytearrays - *a*and- *b*and return a new bytearray with the result.- On failure, return - `NULL`with an exception set.

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyByteArray_Size([PyObject](structures.html#c.PyObject)*bytearray)[¶](#c.PyByteArray_Size)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the size of - *bytearray*after checking for a- `NULL`pointer.

- 
char *PyByteArray_AsString([PyObject](structures.html#c.PyObject)*bytearray)[¶](#c.PyByteArray_AsString)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the contents of - *bytearray*as a char array after checking for a- `NULL`pointer. The returned array always has an extra null byte appended.

- 
int PyByteArray_Resize([PyObject](structures.html#c.PyObject)*bytearray,[Py_ssize_t](intro.html#c.Py_ssize_t)len)[¶](#c.PyByteArray_Resize)
- *Part of the*- [Stable ABI](stable.html#stable).- Resize the internal buffer of - *bytearray*to- *len*.

## Macros[¶](#macros)

These macros trade safety for speed and they don’t check pointers.

- 
char *PyByteArray_AS_STRING([PyObject](structures.html#c.PyObject)*bytearray)[¶](#c.PyByteArray_AS_STRING)
- Similar to - `PyByteArray_AsString()`

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyByteArray_GET_SIZE([PyObject](structures.html#c.PyObject)*bytearray)[¶](#c.PyByteArray_GET_SIZE)
- Similar to - `PyByteArray_Size()`