# Generator Objects — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/gen.html](https://docs.python.org/3.13/c-api/gen.html)

---

# Generator Objects[¶](#generator-objects)

Generator objects are what Python uses to implement generator iterators. They
are normally created by iterating over a function that yields values, rather
than explicitly calling [ PyGen_New()](#c.PyGen_New) or 

[.](#c.PyGen_NewWithQualName)

`PyGen_NewWithQualName()`- 
type PyGenObject[¶](#c.PyGenObject)
- The C structure used for generator objects. 

- 
[PyTypeObject](type.html#c.PyTypeObject)PyGen_Type[¶](#c.PyGen_Type)
- The type object corresponding to generator objects. 

- 
int PyGen_Check([PyObject](structures.html#c.PyObject)*ob)[¶](#c.PyGen_Check)
- Return true if - *ob*is a generator object;- *ob*must not be- `NULL`. This function always succeeds.

- 
int PyGen_CheckExact([PyObject](structures.html#c.PyObject)*ob)[¶](#c.PyGen_CheckExact)
- Return true if - *ob*’s type is- `PyGen_Type`- *ob*must not be- `NULL`. This function always succeeds.

- 
[PyObject](structures.html#c.PyObject)*PyGen_New([PyFrameObject](frame.html#c.PyFrameObject)*frame)[¶](#c.PyGen_New)
- *Return value: New reference.*- Create and return a new generator object based on the - *frame*object. A reference to- *frame*is stolen by this function. The argument must not be- `NULL`.

- 
[PyObject](structures.html#c.PyObject)*PyGen_NewWithQualName([PyFrameObject](frame.html#c.PyFrameObject)*frame,[PyObject](structures.html#c.PyObject)*name,[PyObject](structures.html#c.PyObject)*qualname)[¶](#c.PyGen_NewWithQualName)
- *Return value: New reference.*- Create and return a new generator object based on the - *frame*object, with- `__name__`and- `__qualname__`set to- *name*and- *qualname*. A reference to- *frame*is stolen by this function. The- *frame*argument must not be- `NULL`.

- 
[PyCodeObject](code.html#c.PyCodeObject)*PyGen_GetCode([PyGenObject](#c.PyGenObject)*gen)[¶](#c.PyGen_GetCode)
- Return a new - [strong reference](../glossary.html#term-strong-reference)to the code object wrapped by- *gen*. This function always succeeds.

## Asynchronous Generator Objects[¶](#asynchronous-generator-objects)

See also

- 
[PyTypeObject](type.html#c.PyTypeObject)PyAsyncGen_Type[¶](#c.PyAsyncGen_Type)
- The type object corresponding to asynchronous generator objects. This is available as - `types.AsyncGeneratorType`- Added in version 3.6. 

- 
[PyObject](structures.html#c.PyObject)*PyAsyncGen_New([PyFrameObject](frame.html#c.PyFrameObject)*frame,[PyObject](structures.html#c.PyObject)*name,[PyObject](structures.html#c.PyObject)*qualname)[¶](#c.PyAsyncGen_New)
- Create a new asynchronous generator wrapping - *frame*, with- `__name__`and- `__qualname__`set to- *name*and- *qualname*.- *frame*is stolen by this function and must not be- `NULL`.- On success, this function returns a - [strong reference](../glossary.html#term-strong-reference)to the new asynchronous generator. On failure, this function returns- `NULL`with an exception set.- Added in version 3.6.