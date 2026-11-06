# Allocating objects on the heap — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/allocation.html](https://docs.python.org/c-api/allocation.html)

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
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Initialize a newly allocated object - *op*with its type and initial reference. Returns the initialized object. Other fields of the object are not initialized. Despite its name, this function is unrelated to the object’s- `__init__()`- `tp_init`- **not**call the object’s- `__init__()`method.- In general, consider this function to be a low-level routine. Use - `tp_alloc`- `tp_alloc`for your type, prefer- `PyType_GenericAlloc()`- `PyObject_New()`- Note - This function only initializes the object’s memory corresponding to the initial - `PyObject`

- 
[PyVarObject](structures.html#c.PyVarObject)*PyObject_InitVar([PyVarObject](structures.html#c.PyVarObject)*op,[PyTypeObject](type.html#c.PyTypeObject)*type,[Py_ssize_t](intro.html#c.Py_ssize_t)size)[¶](#c.PyObject_InitVar)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable).- This does everything - `PyObject_Init()`- Note - This function only initializes some of the object’s memory. It does not zero the rest. 

- 
PyObject_New(TYPE, typeobj)[¶](#c.PyObject_New)
- Allocates a new Python object using the C structure type - *TYPE*and the Python type object- *typeobj*(- `PyTypeObject*`) by calling- `PyObject_Malloc()`- `PyObject_Init()`- Avoid calling this directly to allocate memory for an object; call the type’s - `tp_alloc`- When populating a type’s - `tp_alloc`- `PyType_GenericAlloc()`- This macro does not call - `tp_alloc`- `tp_new`- `__new__()`- `tp_init`- `__init__()`- This cannot be used for objects with - `Py_TPFLAGS_HAVE_GC`- `tp_flags`- `PyObject_GC_New`- Memory allocated by this macro must be freed with - `PyObject_Free()`- `tp_free`- Note - The returned memory is not guaranteed to have been completely zeroed before it was initialized. - Note - This macro does not construct a fully initialized object of the given type; it merely allocates memory and prepares it for further initialization by - `tp_init`- *typeobj*instead. For example:- PyObject *foo = PyObject_CallNoArgs((PyObject *)&PyFoo_Type); 

- 
PyObject_NewVar(TYPE, typeobj, size)[¶](#c.PyObject_NewVar)
- Like - `PyObject_New`- It allocates enough memory for the - *TYPE*structure plus- *size*(- `Py_ssize_t`) fields of the size given by the- `tp_itemsize`- *typeobj*.
- The memory is initialized like - `PyObject_InitVar()`
 - This is useful for implementing objects like tuples, which are able to determine their size at construction time. Embedding the array of fields into the same allocation decreases the number of allocations, improving the memory management efficiency. - Avoid calling this directly to allocate memory for an object; call the type’s - `tp_alloc`- When populating a type’s - `tp_alloc`- `PyType_GenericAlloc()`- This cannot be used for objects with - `Py_TPFLAGS_HAVE_GC`- `tp_flags`- `PyObject_GC_NewVar`- Memory allocated by this function must be freed with - `PyObject_Free()`- `tp_free`- Note - The returned memory is not guaranteed to have been completely zeroed before it was initialized. - Note - This macro does not construct a fully initialized object of the given type; it merely allocates memory and prepares it for further initialization by - `tp_init`- *typeobj*instead. For example:- PyObject *list_instance = PyObject_CallNoArgs((PyObject *)&PyList_Type); 

- 
[PyObject](structures.html#c.PyObject)_Py_NoneStruct[¶](#c._Py_NoneStruct)
- Object which is visible in Python as - `None`. This should only be accessed using the- `Py_None`

See also

- [Module Objects](module.html#moduleobjects)
- To allocate and create extension modules. 

## Soft-deprecated aliases[¶](#soft-deprecated-aliases)

[Soft deprecated](../glossary.html#term-soft-deprecated) since version 3.10.

These are aliases to existing functions and macros. They exist solely for backwards compatibility.