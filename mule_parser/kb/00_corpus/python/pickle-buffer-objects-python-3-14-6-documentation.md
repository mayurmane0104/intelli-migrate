# Pickle buffer objects — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/picklebuffer.html](https://docs.python.org/c-api/picklebuffer.html)

---

# Pickle buffer objects[¶](#pickle-buffer-objects)

Added in version 3.8.

A [ pickle.PickleBuffer](../library/pickle.html#pickle.PickleBuffer) object wraps a 

[buffer-providing object](buffer.html#bufferobjects)for out-of-band data transfer with the

[module.](../library/pickle.html#module-pickle)

`pickle`- 
[PyTypeObject](type.html#c.PyTypeObject)PyPickleBuffer_Type[¶](#c.PyPickleBuffer_Type)
- This instance of - `PyTypeObject`- `pickle.PickleBuffer`

- 
int PyPickleBuffer_Check([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyPickleBuffer_Check)
- Return true if - *op*is a pickle buffer instance. This function always succeeds.

- 
[PyObject](structures.html#c.PyObject)*PyPickleBuffer_FromObject([PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyPickleBuffer_FromObject)
- Create a pickle buffer from the object - *obj*.- This function will fail if - *obj*doesn’t support the- [buffer protocol](buffer.html#bufferobjects).- On success, return a new pickle buffer instance. On failure, set an exception and return - `NULL`.- Analogous to calling - `pickle.PickleBuffer`- *obj*in Python.

- 
const [Py_buffer](buffer.html#c.Py_buffer)*PyPickleBuffer_GetBuffer([PyObject](structures.html#c.PyObject)*picklebuf)[¶](#c.PyPickleBuffer_GetBuffer)
- Get a pointer to the underlying - `Py_buffer`- The returned pointer is valid as long as - *picklebuf*is alive and has not been released. The caller must not modify or free the returned- `Py_buffer`- `ValueError`- On success, return a pointer to the buffer view. On failure, set an exception and return - `NULL`.

- 
int PyPickleBuffer_Release([PyObject](structures.html#c.PyObject)*picklebuf)[¶](#c.PyPickleBuffer_Release)
- Release the underlying buffer held by the pickle buffer. - Return - `0`on success. On failure, set an exception and return- `-1`.- Analogous to calling - `pickle.PickleBuffer.release()`