# Coroutine Objects — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/coro.html](https://docs.python.org/3.13/c-api/coro.html)

---

# Coroutine Objects[¶](#coroutine-objects)

Added in version 3.5.

Coroutine objects are what functions declared with an `async` keyword
return.

- 
type PyCoroObject[¶](#c.PyCoroObject)
- The C structure used for coroutine objects. 

- 
[PyTypeObject](type.html#c.PyTypeObject)PyCoro_Type[¶](#c.PyCoro_Type)
- The type object corresponding to coroutine objects. 

- 
int PyCoro_CheckExact([PyObject](structures.html#c.PyObject)*ob)[¶](#c.PyCoro_CheckExact)
- Return true if - *ob*’s type is- `PyCoro_Type`- *ob*must not be- `NULL`. This function always succeeds.

- 
[PyObject](structures.html#c.PyObject)*PyCoro_New([PyFrameObject](frame.html#c.PyFrameObject)*frame,[PyObject](structures.html#c.PyObject)*name,[PyObject](structures.html#c.PyObject)*qualname)[¶](#c.PyCoro_New)
- *Return value: New reference.*- Create and return a new coroutine object based on the - *frame*object, with- `__name__`and- `__qualname__`set to- *name*and- *qualname*. A reference to- *frame*is stolen by this function. The- *frame*argument must not be- `NULL`.