# Instance Method Objects — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/method.html](https://docs.python.org/3.13/c-api/method.html)

---

# Instance Method Objects[¶](#instance-method-objects)

An instance method is a wrapper for a [ PyCFunction](structures.html#c.PyCFunction) and the new way
to bind a 

`PyCFunction` to a class object. It replaces the former call
`PyMethod_New(func, NULL, class)`.- 
[PyTypeObject](type.html#c.PyTypeObject)PyInstanceMethod_Type[¶](#c.PyInstanceMethod_Type)
- This instance of - `PyTypeObject`

- 
int PyInstanceMethod_Check([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyInstanceMethod_Check)
- Return true if - *o*is an instance method object (has type- `PyInstanceMethod_Type`- `NULL`. This function always succeeds.

- 
[PyObject](structures.html#c.PyObject)*PyInstanceMethod_New([PyObject](structures.html#c.PyObject)*func)[¶](#c.PyInstanceMethod_New)
- *Return value: New reference.*- Return a new instance method object, with - *func*being any callable object.- *func*is the function that will be called when the instance method is called.

- 
[PyObject](structures.html#c.PyObject)*PyInstanceMethod_Function([PyObject](structures.html#c.PyObject)*im)[¶](#c.PyInstanceMethod_Function)
- *Return value: Borrowed reference.*- Return the function object associated with the instance method - *im*.

- 
[PyObject](structures.html#c.PyObject)*PyInstanceMethod_GET_FUNCTION([PyObject](structures.html#c.PyObject)*im)[¶](#c.PyInstanceMethod_GET_FUNCTION)
- *Return value: Borrowed reference.*- Macro version of - `PyInstanceMethod_Function()`

# Method Objects[¶](#method-objects)

Methods are bound function objects. Methods are always bound to an instance of a user-defined class. Unbound methods (methods bound to a class object) are no longer available.

- 
[PyTypeObject](type.html#c.PyTypeObject)PyMethod_Type[¶](#c.PyMethod_Type)
- This instance of - `PyTypeObject`- `types.MethodType`.

- 
int PyMethod_Check([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyMethod_Check)
- Return true if - *o*is a method object (has type- `PyMethod_Type`- `NULL`. This function always succeeds.

- 
[PyObject](structures.html#c.PyObject)*PyMethod_New([PyObject](structures.html#c.PyObject)*func,[PyObject](structures.html#c.PyObject)*self)[¶](#c.PyMethod_New)
- *Return value: New reference.*- Return a new method object, with - *func*being any callable object and- *self*the instance the method should be bound.- *func*is the function that will be called when the method is called.- *self*must not be- `NULL`.

- 
[PyObject](structures.html#c.PyObject)*PyMethod_Function([PyObject](structures.html#c.PyObject)*meth)[¶](#c.PyMethod_Function)
- *Return value: Borrowed reference.*- Return the function object associated with the method - *meth*.

- 
[PyObject](structures.html#c.PyObject)*PyMethod_GET_FUNCTION([PyObject](structures.html#c.PyObject)*meth)[¶](#c.PyMethod_GET_FUNCTION)
- *Return value: Borrowed reference.*- Macro version of - `PyMethod_Function()`

- 
[PyObject](structures.html#c.PyObject)*PyMethod_Self([PyObject](structures.html#c.PyObject)*meth)[¶](#c.PyMethod_Self)
- *Return value: Borrowed reference.*- Return the instance associated with the method - *meth*.

- 
[PyObject](structures.html#c.PyObject)*PyMethod_GET_SELF([PyObject](structures.html#c.PyObject)*meth)[¶](#c.PyMethod_GET_SELF)
- *Return value: Borrowed reference.*- Macro version of - `PyMethod_Self()`