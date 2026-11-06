# Allocating objects on the heap — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/allocation.html](https://docs.python.org/3.13/c-api/allocation.html)

---

# Allocating objects on the heap[¶](#allocating-objects-on-the-heap)

- 
[PyObject](structures.html#c.PyObject)*_PyObject_New([PyTypeObject](type.html#c.PyTypeObject)*type)[¶](#c._PyObject_New)
- *Return value: New reference.*

- 
[PyVarObject](structures.html#c.PyVarObject)*_PyObject_NewVar([PyTypeObject](type.html#c.PyTypeObject)*type,[Py_ssize_t](intro.html#c.Py_ssize_t)size)[¶](#c._PyObject_NewVar)
- *Return value: New reference.*

- 
[PyObject](structures.html#c.PyObject)*PyObject_Init([PyObject](structures.html#c.PyObject)*op,[PyTypeObject](type.html#c.PyTypeObject)*type)[¶](#c.PyObject_Init)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Initialize a newly allocated object - *op*with its type and initial reference. Returns the initialized object. Other fields of the object are not affected.

- 
[PyVarObject](structures.html#c.PyVarObject)*PyObject_InitVar([PyVarObject](structures.html#c.PyVarObject)*op,[PyTypeObject](type.html#c.PyTypeObject)*type,[Py_ssize_t](intro.html#c.Py_ssize_t)size)[¶](#c.PyObject_InitVar)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable).- This does everything - `PyObject_Init()`

- 
PyObject_New(TYPE, typeobj)[¶](#c.PyObject_New)
- Allocate a new Python object using the C structure type - *TYPE*and the Python type object- *typeobj*(- `PyTypeObject*`). Fields not defined by the Python object header are not initialized. The caller will own the only reference to the object (i.e. its reference count will be one). The size of the memory allocation is determined from the- `tp_basicsize`- Note that this function is unsuitable if - *typeobj*has- `Py_TPFLAGS_HAVE_GC`- `PyObject_GC_New()`

- 
PyObject_NewVar(TYPE, typeobj, size)[¶](#c.PyObject_NewVar)
- Allocate a new Python object using the C structure type - *TYPE*and the Python type object- *typeobj*(- `PyTypeObject*`). Fields not defined by the Python object header are not initialized. The allocated memory allows for the- *TYPE*structure plus- *size*(- `Py_ssize_t`) fields of the size given by the- `tp_itemsize`- *typeobj*. This is useful for implementing objects like tuples, which are able to determine their size at construction time. Embedding the array of fields into the same allocation decreases the number of allocations, improving the memory management efficiency.- Note that this function is unsuitable if - *typeobj*has- `Py_TPFLAGS_HAVE_GC`- `PyObject_GC_NewVar()`

- 
[PyObject](structures.html#c.PyObject)_Py_NoneStruct[¶](#c._Py_NoneStruct)
- Object which is visible in Python as - `None`. This should only be accessed using the- `Py_None`

See also

- [Module Objects](module.html#moduleobjects)
- To allocate and create extension modules. 

## Soft-deprecated aliases[¶](#soft-deprecated-aliases)

[Soft deprecated](../glossary.html#term-soft-deprecated) since version 3.10.

These are aliases to existing functions and macros. They exist solely for backwards compatibility.