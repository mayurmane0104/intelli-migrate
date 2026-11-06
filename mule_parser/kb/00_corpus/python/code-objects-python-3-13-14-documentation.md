# Code Objects — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/code.html](https://docs.python.org/3.13/c-api/code.html)

---

# Code Objects[¶](#code-objects)

Code objects are a low-level detail of the CPython implementation. Each one represents a chunk of executable code that hasn’t yet been bound into a function.

- 
type PyCodeObject[¶](#c.PyCodeObject)
- The C structure of the objects used to describe code objects. The fields of this type are subject to change at any time. 

- 
[PyTypeObject](type.html#c.PyTypeObject)PyCode_Type[¶](#c.PyCode_Type)
- This is an instance of - `PyTypeObject`- [code object](../reference/datamodel.html#code-objects).

- 
int PyCode_Check([PyObject](structures.html#c.PyObject)*co)[¶](#c.PyCode_Check)
- Return true if - *co*is a- [code object](../reference/datamodel.html#code-objects). This function always succeeds.

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyCode_GetNumFree([PyCodeObject](#c.PyCodeObject)*co)[¶](#c.PyCode_GetNumFree)
- Return the number of - [free (closure) variables](../glossary.html#term-closure-variable)in a code object.

- 
int PyUnstable_Code_GetFirstFree([PyCodeObject](#c.PyCodeObject)*co)[¶](#c.PyUnstable_Code_GetFirstFree)
- *This is*- [Unstable API](stable.html#unstable-c-api). It may change without warning in minor releases.- Return the position of the first - [free (closure) variable](../glossary.html#term-closure-variable)in a code object.- Changed in version 3.13: Renamed from - `PyCode_GetFirstFree`as part of- [Unstable C API](stable.html#unstable-c-api). The old name is deprecated, but will remain available until the signature changes again.

- 
[PyCodeObject](#c.PyCodeObject)*PyUnstable_Code_New(int argcount, int kwonlyargcount, int nlocals, int stacksize, int flags,[PyObject](structures.html#c.PyObject)*code,[PyObject](structures.html#c.PyObject)*consts,[PyObject](structures.html#c.PyObject)*names,[PyObject](structures.html#c.PyObject)*varnames,[PyObject](structures.html#c.PyObject)*freevars,[PyObject](structures.html#c.PyObject)*cellvars,[PyObject](structures.html#c.PyObject)*filename,[PyObject](structures.html#c.PyObject)*name,[PyObject](structures.html#c.PyObject)*qualname, int firstlineno,[PyObject](structures.html#c.PyObject)*linetable,[PyObject](structures.html#c.PyObject)*exceptiontable)[¶](#c.PyUnstable_Code_New)
- *This is*- [Unstable API](stable.html#unstable-c-api). It may change without warning in minor releases.- Return a new code object. If you need a dummy code object to create a frame, use - `PyCode_NewEmpty()`- Since the definition of the bytecode changes often, calling - `PyUnstable_Code_New()`- The many arguments of this function are inter-dependent in complex ways, meaning that subtle changes to values are likely to result in incorrect execution or VM crashes. Use this function only with extreme care. - Changed in version 3.11: Added - `qualname`and- `exceptiontable`parameters.- Changed in version 3.12: Renamed from - `PyCode_New`as part of- [Unstable C API](stable.html#unstable-c-api). The old name is deprecated, but will remain available until the signature changes again.

- 
[PyCodeObject](#c.PyCodeObject)*PyUnstable_Code_NewWithPosOnlyArgs(int argcount, int posonlyargcount, int kwonlyargcount, int nlocals, int stacksize, int flags,[PyObject](structures.html#c.PyObject)*code,[PyObject](structures.html#c.PyObject)*consts,[PyObject](structures.html#c.PyObject)*names,[PyObject](structures.html#c.PyObject)*varnames,[PyObject](structures.html#c.PyObject)*freevars,[PyObject](structures.html#c.PyObject)*cellvars,[PyObject](structures.html#c.PyObject)*filename,[PyObject](structures.html#c.PyObject)*name,[PyObject](structures.html#c.PyObject)*qualname, int firstlineno,[PyObject](structures.html#c.PyObject)*linetable,[PyObject](structures.html#c.PyObject)*exceptiontable)[¶](#c.PyUnstable_Code_NewWithPosOnlyArgs)
- *This is*- [Unstable API](stable.html#unstable-c-api). It may change without warning in minor releases.- Similar to - `PyUnstable_Code_New()`- `PyUnstable_Code_New`also apply to this function.- Added in version 3.8: as - `PyCode_NewWithPosOnlyArgs`- Changed in version 3.11: Added - `qualname`and- `exceptiontable`parameters.- Changed in version 3.12: Renamed to - `PyUnstable_Code_NewWithPosOnlyArgs`. The old name is deprecated, but will remain available until the signature changes again.

- 
[PyCodeObject](#c.PyCodeObject)*PyCode_NewEmpty(const char *filename, const char *funcname, int firstlineno)[¶](#c.PyCode_NewEmpty)
- *Return value: New reference.*- Return a new empty code object with the specified filename, function name, and first line number. The resulting code object will raise an - `Exception`if executed.

- 
int PyCode_Addr2Line([PyCodeObject](#c.PyCodeObject)*co, int byte_offset)[¶](#c.PyCode_Addr2Line)
- Return the line number of the instruction that occurs on or before - `byte_offset`and ends after it. If you just need the line number of a frame, use- `PyFrame_GetLineNumber()`- For efficiently iterating over the line numbers in a code object, use - **the API described in PEP 626**

- 
int PyCode_Addr2Location([PyObject](structures.html#c.PyObject)*co, int byte_offset, int *start_line, int *start_column, int *end_line, int *end_column)[¶](#c.PyCode_Addr2Location)
- Sets the passed - `int`pointers to the source code line and column numbers for the instruction at- `byte_offset`. Sets the value to- `0`when information is not available for any particular element.- Returns - `1`if the function succeeds and 0 otherwise.- Added in version 3.11. 

- 
[PyObject](structures.html#c.PyObject)*PyCode_GetCode([PyCodeObject](#c.PyCodeObject)*co)[¶](#c.PyCode_GetCode)
- Equivalent to the Python code - `getattr(co, 'co_code')`. Returns a strong reference to a- `PyBytesObject`- `NULL`is returned and an exception is raised.- This - `PyBytesObject`may be created on-demand by the interpreter and does not necessarily represent the bytecode actually executed by CPython. The primary use case for this function is debuggers and profilers.- Added in version 3.11. 

- 
[PyObject](structures.html#c.PyObject)*PyCode_GetVarnames([PyCodeObject](#c.PyCodeObject)*co)[¶](#c.PyCode_GetVarnames)
- Equivalent to the Python code - `getattr(co, 'co_varnames')`. Returns a new reference to a- `PyTupleObject`- `NULL`is returned and an exception is raised.- Added in version 3.11. 

- 
[PyObject](structures.html#c.PyObject)*PyCode_GetCellvars([PyCodeObject](#c.PyCodeObject)*co)[¶](#c.PyCode_GetCellvars)
- Equivalent to the Python code - `getattr(co, 'co_cellvars')`. Returns a new reference to a- `PyTupleObject`- `NULL`is returned and an exception is raised.- Added in version 3.11. 

- 
[PyObject](structures.html#c.PyObject)*PyCode_GetFreevars([PyCodeObject](#c.PyCodeObject)*co)[¶](#c.PyCode_GetFreevars)
- Equivalent to the Python code - `getattr(co, 'co_freevars')`. Returns a new reference to a- `PyTupleObject`- [free (closure) variables](../glossary.html#term-closure-variable). On error,- `NULL`is returned and an exception is raised.- Added in version 3.11. 

- 
int PyCode_AddWatcher([PyCode_WatchCallback](#c.PyCode_WatchCallback)callback)[¶](#c.PyCode_AddWatcher)
- Register - *callback*as a code object watcher for the current interpreter. Return an ID which may be passed to- `PyCode_ClearWatcher()`- `-1`and set an exception.- Added in version 3.12. 

- 
int PyCode_ClearWatcher(int watcher_id)[¶](#c.PyCode_ClearWatcher)
- Clear watcher identified by - *watcher_id*previously returned from- `PyCode_AddWatcher()`- `0`on success, or- `-1`and set an exception on error (e.g. if the given- *watcher_id*was never registered.)- Added in version 3.12. 

- 
type PyCodeEvent[¶](#c.PyCodeEvent)
- Enumeration of possible code object watcher events: - - `PY_CODE_EVENT_CREATE`-- `PY_CODE_EVENT_DESTROY`- Added in version 3.12. 

- 
typedef int (*PyCode_WatchCallback)([PyCodeEvent](#c.PyCodeEvent)event,[PyCodeObject](#c.PyCodeObject)*co)[¶](#c.PyCode_WatchCallback)
- Type of a code object watcher callback function. - If - *event*is- `PY_CODE_EVENT_CREATE`, then the callback is invoked after- *co*has been fully initialized. Otherwise, the callback is invoked before the destruction of- *co*takes place, so the prior state of- *co*can be inspected.- If - *event*is- `PY_CODE_EVENT_DESTROY`, taking a reference in the callback to the about-to-be-destroyed code object will resurrect it and prevent it from being freed at this time. When the resurrected object is destroyed later, any watcher callbacks active at that time will be called again.- Users of this API should not rely on internal runtime implementation details. Such details may include, but are not limited to, the exact order and timing of creation and destruction of code objects. While changes in these details may result in differences observable by watchers (including whether a callback is invoked or not), it does not change the semantics of the Python code being executed. - If the callback sets an exception, it must return - `-1`; this exception will be printed as an unraisable exception using- `PyErr_WriteUnraisable()`- `0`.- There may already be a pending exception set on entry to the callback. In this case, the callback should return - `0`with the same exception still set. This means the callback may not call any other API that can set an exception unless it saves and clears the exception state first, and restores it before returning.- Added in version 3.12. 

# Code Object Flags[¶](#code-object-flags)

Code objects contain a bit-field of flags, which can be retrieved as the
[ co_flags](../reference/datamodel.html#codeobject.co_flags) Python attribute (for example using

[), and set using a](object.html#c.PyObject_GetAttrString)

`PyObject_GetAttrString()`*flags*argument to

[and similar functions.](#c.PyUnstable_Code_New)

`PyUnstable_Code_New()`Flags whose names start with `CO_FUTURE_` correspond to features normally
selectable by [future statements](../reference/simple_stmts.html#future). These flags can be used in
[ PyCompilerFlags.cf_flags](veryhigh.html#c.PyCompilerFlags.cf_flags).
Note that many 

`CO_FUTURE_` flags are mandatory in current versions of
Python, and setting them has no effect.The following flags are available. For their meaning, see the linked documentation of their Python equivalents.

| Flag | Meaning | 
|---|---|
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | |
| 
 | no effect ( | 
| 
 | no effect ( | 
| 
 | no effect ( | 
| 
 | no effect ( | 
| 
 | no effect ( | 
| 
 | no effect ( | 
| 
 | 

# Extra information[¶](#extra-information)

To support low-level extensions to frame evaluation, such as external just-in-time compilers, it is possible to attach arbitrary extra data to code objects.

These functions are part of the unstable C API tier: this functionality is a CPython implementation detail, and the API may change without deprecation warnings.

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyUnstable_Eval_RequestCodeExtraIndex([freefunc](typeobj.html#c.freefunc)free)[¶](#c.PyUnstable_Eval_RequestCodeExtraIndex)
- *This is*- [Unstable API](stable.html#unstable-c-api). It may change without warning in minor releases.- Return a new opaque index value used to adding data to code objects. - You generally call this function once (per interpreter) and use the result with - `PyCode_GetExtra`and- `PyCode_SetExtra`to manipulate data on individual code objects.- If - *free*is not- `NULL`: when a code object is deallocated,- *free*will be called on non-- `NULL`data stored under the new index. Use- `Py_DecRef()`- `PyObject`- Added in version 3.6: as - `_PyEval_RequestCodeExtraIndex`- Changed in version 3.12: Renamed to - `PyUnstable_Eval_RequestCodeExtraIndex`. The old private name is deprecated, but will be available until the API changes.

- 
int PyUnstable_Code_GetExtra([PyObject](structures.html#c.PyObject)*code,[Py_ssize_t](intro.html#c.Py_ssize_t)index, void **extra)[¶](#c.PyUnstable_Code_GetExtra)
- *This is*- [Unstable API](stable.html#unstable-c-api). It may change without warning in minor releases.- Set - *extra*to the extra data stored under the given index. Return 0 on success. Set an exception and return -1 on failure.- If no data was set under the index, set - *extra*to- `NULL`and return 0 without setting an exception.- Added in version 3.6: as - `_PyCode_GetExtra`- Changed in version 3.12: Renamed to - `PyUnstable_Code_GetExtra`. The old private name is deprecated, but will be available until the API changes.

- 
int PyUnstable_Code_SetExtra([PyObject](structures.html#c.PyObject)*code,[Py_ssize_t](intro.html#c.Py_ssize_t)index, void *extra)[¶](#c.PyUnstable_Code_SetExtra)
- *This is*- [Unstable API](stable.html#unstable-c-api). It may change without warning in minor releases.- Set the extra data stored under the given index to - *extra*. Return 0 on success. Set an exception and return -1 on failure.- Added in version 3.6: as - `_PyCode_SetExtra`- Changed in version 3.12: Renamed to - `PyUnstable_Code_SetExtra`. The old private name is deprecated, but will be available until the API changes.