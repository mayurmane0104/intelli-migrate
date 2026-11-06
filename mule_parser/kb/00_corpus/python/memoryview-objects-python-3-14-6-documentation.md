# MemoryView objects — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/memoryview.html](https://docs.python.org/c-api/memoryview.html)

---

# MemoryView objects[¶](#index-0)

A [ memoryview](../library/stdtypes.html#memoryview) object exposes the C level 

[buffer interface](buffer.html#bufferobjects)as a Python object which can then be passed around like any other object.

- 
[PyTypeObject](type.html#c.PyTypeObject)PyMemoryView_Type[¶](#c.PyMemoryView_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- This instance of - `PyTypeObject`- `memoryview`

- 
[PyObject](structures.html#c.PyObject)*PyMemoryView_FromObject([PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyMemoryView_FromObject)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Create a memoryview object from an object that provides the buffer interface. If - *obj*supports writable buffer exports, the memoryview object will be read/write, otherwise it may be either read-only or read/write at the discretion of the exporter.

- 
PyBUF_READ[¶](#c.PyBUF_READ)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.11.- Flag to request a readonly buffer. 

- 
PyBUF_WRITE[¶](#c.PyBUF_WRITE)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.11.- Flag to request a writable buffer. 

- 
[PyObject](structures.html#c.PyObject)*PyMemoryView_FromMemory(char *mem,[Py_ssize_t](intro.html#c.Py_ssize_t)size, int flags)[¶](#c.PyMemoryView_FromMemory)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Create a memoryview object using - *mem*as the underlying buffer.- *flags*can be one of- `PyBUF_READ`- `PyBUF_WRITE`- Added in version 3.3. 

- 
[PyObject](structures.html#c.PyObject)*PyMemoryView_FromBuffer(const[Py_buffer](buffer.html#c.Py_buffer)*view)[¶](#c.PyMemoryView_FromBuffer)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.11.- Create a memoryview object wrapping the given buffer structure - *view*. For simple byte buffers,- `PyMemoryView_FromMemory()`

- 
[PyObject](structures.html#c.PyObject)*PyMemoryView_GetContiguous([PyObject](structures.html#c.PyObject)*obj, int buffertype, char order)[¶](#c.PyMemoryView_GetContiguous)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Create a memoryview object to a - [contiguous](../glossary.html#term-contiguous)chunk of memory (in either ‘C’ or ‘F’ortran- *order*) from an object that defines the buffer interface. If memory is contiguous, the memoryview object points to the original memory. Otherwise, a copy is made and the memoryview points to a new bytes object.- *buffertype*can be one of- `PyBUF_READ`- `PyBUF_WRITE`

- 
int PyMemoryView_Check([PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyMemoryView_Check)
- Return true if the object - *obj*is a memoryview object. It is not currently allowed to create subclasses of- `memoryview`

- 
[Py_buffer](buffer.html#c.Py_buffer)*PyMemoryView_GET_BUFFER([PyObject](structures.html#c.PyObject)*mview)[¶](#c.PyMemoryView_GET_BUFFER)
- Return a pointer to the memoryview’s private copy of the exporter’s buffer. - *mview*- **must**be a memoryview instance; this macro doesn’t check its type, you must do it yourself or you will risk crashes.

- 
[PyObject](structures.html#c.PyObject)*PyMemoryView_GET_BASE([PyObject](structures.html#c.PyObject)*mview)[¶](#c.PyMemoryView_GET_BASE)
- Return either a pointer to the exporting object that the memoryview is based on or - `NULL`if the memoryview has been created by one of the functions- `PyMemoryView_FromMemory()`- `PyMemoryView_FromBuffer()`- *mview*- **must**be a memoryview instance.