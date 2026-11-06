# Function Objects — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/function.html](https://docs.python.org/3.13/c-api/function.html)

---

# Function Objects[¶](#function-objects)

There are a few functions specific to Python functions.

- 
type PyFunctionObject[¶](#c.PyFunctionObject)
- The C structure used for functions. 

- 
[PyTypeObject](type.html#c.PyTypeObject)PyFunction_Type[¶](#c.PyFunction_Type)
- This is an instance of - `PyTypeObject`- `types.FunctionType`.

- 
int PyFunction_Check([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyFunction_Check)
- Return true if - *o*is a function object (has type- `PyFunction_Type`- `NULL`. This function always succeeds.

- 
[PyObject](structures.html#c.PyObject)*PyFunction_New([PyObject](structures.html#c.PyObject)*code,[PyObject](structures.html#c.PyObject)*globals)[¶](#c.PyFunction_New)
- *Return value: New reference.*- Return a new function object associated with the code object - *code*.- *globals*must be a dictionary with the global variables accessible to the function.- The function’s docstring and name are retrieved from the code object. - `__module__`- *globals*. The argument defaults, annotations and closure are set to- `NULL`.- `__qualname__`- `co_qualname`

- 
[PyObject](structures.html#c.PyObject)*PyFunction_NewWithQualName([PyObject](structures.html#c.PyObject)*code,[PyObject](structures.html#c.PyObject)*globals,[PyObject](structures.html#c.PyObject)*qualname)[¶](#c.PyFunction_NewWithQualName)
- *Return value: New reference.*- As - `PyFunction_New()`- `__qualname__`- *qualname*should be a unicode object or- `NULL`; if- `NULL`, the- `__qualname__`attribute is set to the same value as the code object’s- `co_qualname`- Added in version 3.3. 

- 
[PyObject](structures.html#c.PyObject)*PyFunction_GetCode([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyFunction_GetCode)
- *Return value: Borrowed reference.*- Return the code object associated with the function object - *op*.

- 
[PyObject](structures.html#c.PyObject)*PyFunction_GetGlobals([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyFunction_GetGlobals)
- *Return value: Borrowed reference.*- Return the globals dictionary associated with the function object - *op*.

- 
[PyObject](structures.html#c.PyObject)*PyFunction_GetModule([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyFunction_GetModule)
- *Return value: Borrowed reference.*- Return a - [borrowed reference](../glossary.html#term-borrowed-reference)to the- `__module__`- [function object](../reference/datamodel.html#user-defined-funcs)- *op*. It can be- *NULL*.- This is normally a - `string`

- 
[PyObject](structures.html#c.PyObject)*PyFunction_GetDefaults([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyFunction_GetDefaults)
- *Return value: Borrowed reference.*- Return the argument default values of the function object - *op*. This can be a tuple of arguments or- `NULL`.

- 
int PyFunction_SetDefaults([PyObject](structures.html#c.PyObject)*op,[PyObject](structures.html#c.PyObject)*defaults)[¶](#c.PyFunction_SetDefaults)
- Set the argument default values for the function object - *op*.- *defaults*must be- `Py_None`or a tuple.- Raises - `SystemError`- `-1`on failure.

- 
void PyFunction_SetVectorcall([PyFunctionObject](#c.PyFunctionObject)*func,[vectorcallfunc](call.html#c.vectorcallfunc)vectorcall)[¶](#c.PyFunction_SetVectorcall)
- Set the vectorcall field of a given function object - *func*.- Warning: extensions using this API must preserve the behavior of the unaltered (default) vectorcall function! - Added in version 3.12. 

- 
[PyObject](structures.html#c.PyObject)*PyFunction_GetKwDefaults([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyFunction_GetKwDefaults)
- *Return value: Borrowed reference.*- Return the keyword-only argument default values of the function object - *op*. This can be a dictionary of arguments or- `NULL`.

- 
int PyFunction_SetKwDefaults([PyObject](structures.html#c.PyObject)*op,[PyObject](structures.html#c.PyObject)*defaults)[¶](#c.PyFunction_SetKwDefaults)
- Set the keyword-only argument default values of the function object - *op*.- *defaults*must be a dictionary of keyword-only arguments or- `Py_None`.- This function returns - `0`on success, and returns- `-1`with an exception set on failure.

- 
[PyObject](structures.html#c.PyObject)*PyFunction_GetClosure([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyFunction_GetClosure)
- *Return value: Borrowed reference.*- Return the closure associated with the function object - *op*. This can be- `NULL`or a tuple of cell objects.

- 
int PyFunction_SetClosure([PyObject](structures.html#c.PyObject)*op,[PyObject](structures.html#c.PyObject)*closure)[¶](#c.PyFunction_SetClosure)
- Set the closure associated with the function object - *op*.- *closure*must be- `Py_None`or a tuple of cell objects.- Raises - `SystemError`- `-1`on failure.

- 
[PyObject](structures.html#c.PyObject)*PyFunction_GetAnnotations([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyFunction_GetAnnotations)
- *Return value: Borrowed reference.*- Return the annotations of the function object - *op*. This can be a mutable dictionary or- `NULL`.

- 
int PyFunction_SetAnnotations([PyObject](structures.html#c.PyObject)*op,[PyObject](structures.html#c.PyObject)*annotations)[¶](#c.PyFunction_SetAnnotations)
- Set the annotations for the function object - *op*.- *annotations*must be a dictionary or- `Py_None`.- Raises - `SystemError`- `-1`on failure.

- 
[PyObject](structures.html#c.PyObject)*PyFunction_GET_CODE([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyFunction_GET_CODE)
- 
[PyObject](structures.html#c.PyObject)*PyFunction_GET_GLOBALS([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyFunction_GET_GLOBALS)
- 
[PyObject](structures.html#c.PyObject)*PyFunction_GET_MODULE([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyFunction_GET_MODULE)
- 
[PyObject](structures.html#c.PyObject)*PyFunction_GET_DEFAULTS([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyFunction_GET_DEFAULTS)
- 
[PyObject](structures.html#c.PyObject)*PyFunction_GET_KW_DEFAULTS([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyFunction_GET_KW_DEFAULTS)
- 
[PyObject](structures.html#c.PyObject)*PyFunction_GET_CLOSURE([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyFunction_GET_CLOSURE)
- 
[PyObject](structures.html#c.PyObject)*PyFunction_GET_ANNOTATIONS([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyFunction_GET_ANNOTATIONS)
- *Return value: Borrowed reference.*- These functions are similar to their - `PyFunction_Get*`counterparts, but do not do type checking. Passing anything other than an instance of- `PyFunction_Type`

- 
int PyFunction_AddWatcher([PyFunction_WatchCallback](#c.PyFunction_WatchCallback)callback)[¶](#c.PyFunction_AddWatcher)
- Register - *callback*as a function watcher for the current interpreter. Return an ID which may be passed to- `PyFunction_ClearWatcher()`- `-1`and set an exception.- Added in version 3.12. 

- 
int PyFunction_ClearWatcher(int watcher_id)[¶](#c.PyFunction_ClearWatcher)
- Clear watcher identified by - *watcher_id*previously returned from- `PyFunction_AddWatcher()`- `0`on success, or- `-1`and set an exception on error (e.g. if the given- *watcher_id*was never registered.)- Added in version 3.12. 

- 
type PyFunction_WatchEvent[¶](#c.PyFunction_WatchEvent)
- Enumeration of possible function watcher events: - `PyFunction_EVENT_CREATE`
- `PyFunction_EVENT_DESTROY`
- `PyFunction_EVENT_MODIFY_CODE`
- `PyFunction_EVENT_MODIFY_DEFAULTS`
- `PyFunction_EVENT_MODIFY_KWDEFAULTS`
 - Added in version 3.12. 

- 
typedef int (*PyFunction_WatchCallback)([PyFunction_WatchEvent](#c.PyFunction_WatchEvent)event,[PyFunctionObject](#c.PyFunctionObject)*func,[PyObject](structures.html#c.PyObject)*new_value)[¶](#c.PyFunction_WatchCallback)
- Type of a function watcher callback function. - If - *event*is- `PyFunction_EVENT_CREATE`or- `PyFunction_EVENT_DESTROY`then- *new_value*will be- `NULL`. Otherwise,- *new_value*will hold a- [borrowed reference](../glossary.html#term-borrowed-reference)to the new value that is about to be stored in- *func*for the attribute that is being modified.- The callback may inspect but must not modify - *func*; doing so could have unpredictable effects, including infinite recursion.- If - *event*is- `PyFunction_EVENT_CREATE`, then the callback is invoked after- *func*has been fully initialized. Otherwise, the callback is invoked before the modification to- *func*takes place, so the prior state of- *func*can be inspected. The runtime is permitted to optimize away the creation of function objects when possible. In such cases no event will be emitted. Although this creates the possibility of an observable difference of runtime behavior depending on optimization decisions, it does not change the semantics of the Python code being executed.- If - *event*is- `PyFunction_EVENT_DESTROY`, Taking a reference in the callback to the about-to-be-destroyed function will resurrect it, preventing it from being freed at this time. When the resurrected object is destroyed later, any watcher callbacks active at that time will be called again.- If the callback sets an exception, it must return - `-1`; this exception will be printed as an unraisable exception using- `PyErr_WriteUnraisable()`- `0`.- There may already be a pending exception set on entry to the callback. In this case, the callback should return - `0`with the same exception still set. This means the callback may not call any other API that can set an exception unless it saves and clears the exception state first, and restores it before returning.- Added in version 3.12.