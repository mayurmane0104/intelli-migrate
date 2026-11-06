# Reflection — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/reflection.html](https://docs.python.org/c-api/reflection.html)

---

# Reflection[¶](#reflection)

- 
[PyObject](structures.html#c.PyObject)*PyEval_GetBuiltins(void)[¶](#c.PyEval_GetBuiltins)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Deprecated since version 3.13: Use - `PyEval_GetFrameBuiltins()`- Return a dictionary of the builtins in the current execution frame, or the interpreter of the thread state if no frame is currently executing. 

- 
[PyObject](structures.html#c.PyObject)*PyEval_GetLocals(void)[¶](#c.PyEval_GetLocals)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Deprecated since version 3.13: Use either - `PyEval_GetFrameLocals()`- `locals()`- `PyFrame_GetLocals()`- `PyEval_GetFrame()`- `f_locals`- Return a mapping providing access to the local variables in the current execution frame, or - `NULL`if no frame is currently executing.- Refer to - `locals()`- As this function returns a - [borrowed reference](../glossary.html#term-borrowed-reference), the dictionary returned for- [optimized scopes](../glossary.html#term-optimized-scope)is cached on the frame object and will remain alive as long as the frame object does. Unlike- `PyEval_GetFrameLocals()`- `locals()`- Changed in version 3.13: As part of - **PEP 667**- `PyFrame_GetLocals()`- `locals()`- `FrameType.f_locals`- [What’s New entry](../whatsnew/3.13.html#whatsnew313-locals-semantics)for additional details.

- 
[PyObject](structures.html#c.PyObject)*PyEval_GetGlobals(void)[¶](#c.PyEval_GetGlobals)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Deprecated since version 3.13: Use - `PyEval_GetFrameGlobals()`- Return a dictionary of the global variables in the current execution frame, or - `NULL`if no frame is currently executing.

- 
[PyFrameObject](frame.html#c.PyFrameObject)*PyEval_GetFrame(void)[¶](#c.PyEval_GetFrame)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Return the - [attached thread state](../glossary.html#term-attached-thread-state)’s frame, which is- `NULL`if no frame is currently executing.- See also - `PyThreadState_GetFrame()`

- 
[PyObject](structures.html#c.PyObject)*PyEval_GetFrameBuiltins(void)[¶](#c.PyEval_GetFrameBuiltins)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Return a dictionary of the builtins in the current execution frame, or the interpreter of the thread state if no frame is currently executing. - Added in version 3.13. 

- 
[PyObject](structures.html#c.PyObject)*PyEval_GetFrameLocals(void)[¶](#c.PyEval_GetFrameLocals)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Return a dictionary of the local variables in the current execution frame, or - `NULL`if no frame is currently executing. Equivalent to calling- `locals()`- To access - `f_locals`- [optimized scopes](../glossary.html#term-optimized-scope), call- `PyFrame_GetLocals()`- `PyEval_GetFrame()`- Added in version 3.13. 

- 
[PyObject](structures.html#c.PyObject)*PyEval_GetFrameGlobals(void)[¶](#c.PyEval_GetFrameGlobals)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Return a dictionary of the global variables in the current execution frame, or - `NULL`if no frame is currently executing. Equivalent to calling- `globals()`- Added in version 3.13. 

- 
const char *PyEval_GetFuncName([PyObject](structures.html#c.PyObject)*func)[¶](#c.PyEval_GetFuncName)
- *Part of the*- [Stable ABI](stable.html#stable).- Return the name of - *func*if it is a function, class or instance object, else the name of- *func*s type.

- 
const char *PyEval_GetFuncDesc([PyObject](structures.html#c.PyObject)*func)[¶](#c.PyEval_GetFuncDesc)
- *Part of the*- [Stable ABI](stable.html#stable).- Return a description string, depending on the type of - *func*. Return values include “()” for functions and methods, “ constructor”, “ instance”, and “ object”. Concatenated with the result of- `PyEval_GetFuncName()`- *func*.