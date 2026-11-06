# Context Variables Objects — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/contextvars.html](https://docs.python.org/3.13/c-api/contextvars.html)

---

# Context Variables Objects[¶](#context-variables-objects)

Added in version 3.7.

Changed in version 3.7.1:

Note

In Python 3.7.1 the signatures of all context variables
C APIs were **changed** to use [ PyObject](structures.html#c.PyObject) pointers instead
of 

[,](#c.PyContext)

`PyContext`[, and](#c.PyContextVar)

`PyContextVar`[, e.g.:](#c.PyContextToken)

`PyContextToken````
// in 3.7.0:
PyContext *PyContext_New(void);
// in 3.7.1+:
PyObject *PyContext_New(void);
```
See [bpo-34762](https://bugs.python.org/issue?@action=redirect&bpo=34762) for more details.

This section details the public C API for the [ contextvars](../library/contextvars.html#module-contextvars) module.

- 
type PyContext[¶](#c.PyContext)
- The C structure used to represent a - `contextvars.Context`

- 
type PyContextVar[¶](#c.PyContextVar)
- The C structure used to represent a - `contextvars.ContextVar`

- 
type PyContextToken[¶](#c.PyContextToken)
- The C structure used to represent a - `contextvars.Token`

- 
[PyTypeObject](type.html#c.PyTypeObject)PyContext_Type[¶](#c.PyContext_Type)
- The type object representing the - *context*type.

- 
[PyTypeObject](type.html#c.PyTypeObject)PyContextVar_Type[¶](#c.PyContextVar_Type)
- The type object representing the - *context variable*type.

- 
[PyTypeObject](type.html#c.PyTypeObject)PyContextToken_Type[¶](#c.PyContextToken_Type)
- The type object representing the - *context variable token*type.

Type-check macros:

- 
int PyContext_CheckExact([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyContext_CheckExact)
- Return true if - *o*is of type- `PyContext_Type`- *o*must not be- `NULL`. This function always succeeds.

- 
int PyContextVar_CheckExact([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyContextVar_CheckExact)
- Return true if - *o*is of type- `PyContextVar_Type`- *o*must not be- `NULL`. This function always succeeds.

- 
int PyContextToken_CheckExact([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyContextToken_CheckExact)
- Return true if - *o*is of type- `PyContextToken_Type`- *o*must not be- `NULL`. This function always succeeds.

Context object management functions:

- 
[PyObject](structures.html#c.PyObject)*PyContext_New(void)[¶](#c.PyContext_New)
- *Return value: New reference.*- Create a new empty context object. Returns - `NULL`if an error has occurred.

- 
[PyObject](structures.html#c.PyObject)*PyContext_Copy([PyObject](structures.html#c.PyObject)*ctx)[¶](#c.PyContext_Copy)
- *Return value: New reference.*- Create a shallow copy of the passed - *ctx*context object. Returns- `NULL`if an error has occurred.

- 
[PyObject](structures.html#c.PyObject)*PyContext_CopyCurrent(void)[¶](#c.PyContext_CopyCurrent)
- *Return value: New reference.*- Create a shallow copy of the current thread context. Returns - `NULL`if an error has occurred.

- 
int PyContext_Enter([PyObject](structures.html#c.PyObject)*ctx)[¶](#c.PyContext_Enter)
- Set - *ctx*as the current context for the current thread. Returns- `0`on success, and- `-1`on error.

- 
int PyContext_Exit([PyObject](structures.html#c.PyObject)*ctx)[¶](#c.PyContext_Exit)
- Deactivate the - *ctx*context and restore the previous context as the current context for the current thread. Returns- `0`on success, and- `-1`on error.

Context variable functions:

- 
[PyObject](structures.html#c.PyObject)*PyContextVar_New(const char *name,[PyObject](structures.html#c.PyObject)*def)[¶](#c.PyContextVar_New)
- *Return value: New reference.*- Create a new - `ContextVar`object. The- *name*parameter is used for introspection and debug purposes. The- *def*parameter specifies a default value for the context variable, or- `NULL`for no default. If an error has occurred, this function returns- `NULL`.

- 
int PyContextVar_Get([PyObject](structures.html#c.PyObject)*var,[PyObject](structures.html#c.PyObject)*default_value,[PyObject](structures.html#c.PyObject)**value)[¶](#c.PyContextVar_Get)
- Get the value of a context variable. Returns - `-1`if an error has occurred during lookup, and- `0`if no error occurred, whether or not a value was found.- If the context variable was found, - *value*will be a pointer to it. If the context variable was- *not*found,- *value*will point to:- *default_value*, if not- `NULL`;
- the default value of - *var*, if not- `NULL`;
- `NULL`
 - Except for - `NULL`, the function returns a new reference.

- 
[PyObject](structures.html#c.PyObject)*PyContextVar_Set([PyObject](structures.html#c.PyObject)*var,[PyObject](structures.html#c.PyObject)*value)[¶](#c.PyContextVar_Set)
- *Return value: New reference.*- Set the value of - *var*to- *value*in the current context. Returns a new token object for this change, or- `NULL`if an error has occurred.

- 
int PyContextVar_Reset([PyObject](structures.html#c.PyObject)*var,[PyObject](structures.html#c.PyObject)*token)[¶](#c.PyContextVar_Reset)
- Reset the state of the - *var*context variable to that it was in before- `PyContextVar_Set()`- *token*was called. This function returns- `0`on success and- `-1`on error.