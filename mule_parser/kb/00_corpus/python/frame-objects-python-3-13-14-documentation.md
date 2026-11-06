# Frame objects — Python 3.13.14 documentation

**Source:** [https://docs.python.org/3.13/c-api/frame.html](https://docs.python.org/3.13/c-api/frame.html)

---

# Frame objects[¶](#frame-objects)

- 
type PyFrameObject[¶](#c.PyFrameObject)
- *Part of the*- [Limited API](stable.html#stable)(as an opaque struct).- The C structure of the objects used to describe frame objects. - There are no public members in this structure. - Changed in version 3.11: The members of this structure were removed from the public C API. Refer to the - [What’s New entry](../whatsnew/3.11.html#pyframeobject-3-11-hiding)for details.

The [ PyEval_GetFrame()](reflection.html#c.PyEval_GetFrame) and 

[functions can be used to get a frame object.](init.html#c.PyThreadState_GetFrame)

`PyThreadState_GetFrame()`See also [Reflection](reflection.html#reflection).

- 
[PyTypeObject](type.html#c.PyTypeObject)PyFrame_Type[¶](#c.PyFrame_Type)
- The type of frame objects. It is the same object as - `types.FrameType`- Changed in version 3.11: Previously, this type was only available after including - `<frameobject.h>`.

- 
[PyFrameObject](#c.PyFrameObject)*PyFrame_New([PyThreadState](init.html#c.PyThreadState)*tstate,[PyCodeObject](code.html#c.PyCodeObject)*code,[PyObject](structures.html#c.PyObject)*globals,[PyObject](structures.html#c.PyObject)*locals)[¶](#c.PyFrame_New)
- Create a new frame object. This function returns a - [strong reference](../glossary.html#term-strong-reference)to the new frame object on success, and returns- `NULL`with an exception set on failure.

- 
int PyFrame_Check([PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyFrame_Check)
- Return non-zero if - *obj*is a frame object.- Changed in version 3.11: Previously, this function was only available after including - `<frameobject.h>`.

- 
[PyFrameObject](#c.PyFrameObject)*PyFrame_GetBack([PyFrameObject](#c.PyFrameObject)*frame)[¶](#c.PyFrame_GetBack)
- *Return value: New reference.*- Get the - *frame*next outer frame.- Return a - [strong reference](../glossary.html#term-strong-reference), or- `NULL`if- *frame*has no outer frame. This raises no exceptions.- Added in version 3.9. 

- 
[PyObject](structures.html#c.PyObject)*PyFrame_GetBuiltins([PyFrameObject](#c.PyFrameObject)*frame)[¶](#c.PyFrame_GetBuiltins)
- *Return value: New reference.*- Get the - *frame*’s- `f_builtins`- Return a - [strong reference](../glossary.html#term-strong-reference). The result cannot be- `NULL`.- Added in version 3.11. 

- 
[PyCodeObject](code.html#c.PyCodeObject)*PyFrame_GetCode([PyFrameObject](#c.PyFrameObject)*frame)[¶](#c.PyFrame_GetCode)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- Get the - *frame*code.- Return a - [strong reference](../glossary.html#term-strong-reference).- The result (frame code) cannot be - `NULL`.- Added in version 3.9. 

- 
[PyObject](structures.html#c.PyObject)*PyFrame_GetGenerator([PyFrameObject](#c.PyFrameObject)*frame)[¶](#c.PyFrame_GetGenerator)
- *Return value: New reference.*- Get the generator, coroutine, or async generator that owns this frame, or - `NULL`if this frame is not owned by a generator. Does not raise an exception, even if the return value is- `NULL`.- Return a - [strong reference](../glossary.html#term-strong-reference), or- `NULL`.- Added in version 3.11. 

- 
[PyObject](structures.html#c.PyObject)*PyFrame_GetGlobals([PyFrameObject](#c.PyFrameObject)*frame)[¶](#c.PyFrame_GetGlobals)
- *Return value: New reference.*- Get the - *frame*’s- `f_globals`- Return a - [strong reference](../glossary.html#term-strong-reference). The result cannot be- `NULL`.- Added in version 3.11. 

- 
int PyFrame_GetLasti([PyFrameObject](#c.PyFrameObject)*frame)[¶](#c.PyFrame_GetLasti)
- Get the - *frame*’s- `f_lasti`- Returns -1 if - `frame.f_lasti`is- `None`.- Added in version 3.11. 

- 
[PyObject](structures.html#c.PyObject)*PyFrame_GetVar([PyFrameObject](#c.PyFrameObject)*frame,[PyObject](structures.html#c.PyObject)*name)[¶](#c.PyFrame_GetVar)
- *Return value: New reference.*- Get the variable - *name*of- *frame*.- Return a - [strong reference](../glossary.html#term-strong-reference)to the variable value on success.
- Raise - `NameError`- `NULL`if the variable does not exist.
- Raise an exception and return - `NULL`on error.
 - *name*type must be a- `str`- Added in version 3.12. 

- 
[PyObject](structures.html#c.PyObject)*PyFrame_GetVarString([PyFrameObject](#c.PyFrameObject)*frame, const char *name)[¶](#c.PyFrame_GetVarString)
- *Return value: New reference.*- Similar to - `PyFrame_GetVar()`- Added in version 3.12. 

- 
[PyObject](structures.html#c.PyObject)*PyFrame_GetLocals([PyFrameObject](#c.PyFrameObject)*frame)[¶](#c.PyFrame_GetLocals)
- *Return value: New reference.*- Get the - *frame*’s- `f_locals`- [optimized scope](../glossary.html#term-optimized-scope), this returns a write-through proxy object that allows modifying the locals. In all other cases (classes, modules,- `exec()`- `eval()`- `locals()`- Return a - [strong reference](../glossary.html#term-strong-reference).- Added in version 3.11. - Changed in version 3.13: As part of - **PEP 667**- `PyFrameLocalsProxy_Type`

- 
int PyFrame_GetLineNumber([PyFrameObject](#c.PyFrameObject)*frame)[¶](#c.PyFrame_GetLineNumber)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- Return the line number that - *frame*is currently executing.

## Frame locals proxies[¶](#frame-locals-proxies)

Added in version 3.13.

The [ f_locals](../reference/datamodel.html#frame.f_locals) attribute on a 

[frame object](../reference/datamodel.html#frame-objects)is an instance of a “frame-locals proxy”. The proxy object exposes a write-through view of the underlying locals dictionary for the frame. This ensures that the variables exposed by

`f_locals` are always up to date with
the live local variables in the frame itself.See [ PEP 667](https://peps.python.org/pep-0667/) for more information.

- 
[PyTypeObject](type.html#c.PyTypeObject)PyFrameLocalsProxy_Type[¶](#c.PyFrameLocalsProxy_Type)
- The type of frame - `locals()`

## Legacy local variable APIs[¶](#legacy-local-variable-apis)

These APIs are [soft deprecated](../glossary.html#term-soft-deprecated). As of Python 3.13, they do nothing.
They exist solely for backwards compatibility.

- 
void PyFrame_LocalsToFast([PyFrameObject](#c.PyFrameObject)*f, int clear)[¶](#c.PyFrame_LocalsToFast)
- Prior to Python 3.13, this function would copy the - `f_locals`- *f*to the internal “fast” array of local variables, allowing changes in frame objects to be visible to the interpreter. If- *clear*was true, this function would process variables that were unset in the locals dictionary.- [Soft deprecated](../glossary.html#term-soft-deprecated)since version 3.13: This function now does nothing.

- 
void PyFrame_FastToLocals([PyFrameObject](#c.PyFrameObject)*f)[¶](#c.PyFrame_FastToLocals)
- Prior to Python 3.13, this function would copy the internal “fast” array of local variables (which is used by the interpreter) to the - `f_locals`- *f*, allowing changes in local variables to be visible to frame objects.- [Soft deprecated](../glossary.html#term-soft-deprecated)since version 3.13: This function now does nothing.

- 
int PyFrame_FastToLocalsWithError([PyFrameObject](#c.PyFrameObject)*f)[¶](#c.PyFrame_FastToLocalsWithError)
- Prior to Python 3.13, this function was similar to - `PyFrame_FastToLocals()`- `0`on success, and- `-1`with an exception set on failure.- [Soft deprecated](../glossary.html#term-soft-deprecated)since version 3.13: This function now does nothing.

See also

## Internal frames[¶](#internal-frames)

Unless using [ PEP 523](https://peps.python.org/pep-0523/), you will not need this.

- 
struct _PyInterpreterFrame[¶](#c._PyInterpreterFrame)
- The interpreter’s internal frame representation. - Added in version 3.11. 

- 
[PyObject](structures.html#c.PyObject)*PyUnstable_InterpreterFrame_GetCode(struct[_PyInterpreterFrame](#c._PyInterpreterFrame)*frame);[¶](#c.PyUnstable_InterpreterFrame_GetCode)
- *This is*- [Unstable API](stable.html#unstable-c-api). It may change without warning in minor releases.- Return a - [strong reference](../glossary.html#term-strong-reference)to the code object for the frame.- Added in version 3.12. 

- 
int PyUnstable_InterpreterFrame_GetLasti(struct [_PyInterpreterFrame](#c._PyInterpreterFrame)*frame);[¶](#c.PyUnstable_InterpreterFrame_GetLasti)
- *This is*- [Unstable API](stable.html#unstable-c-api). It may change without warning in minor releases.- Return the byte offset into the last executed instruction. - Added in version 3.12. 

- 
int PyUnstable_InterpreterFrame_GetLine(struct [_PyInterpreterFrame](#c._PyInterpreterFrame)*frame);[¶](#c.PyUnstable_InterpreterFrame_GetLine)
- *This is*- [Unstable API](stable.html#unstable-c-api). It may change without warning in minor releases.- Return the currently executing line number, or -1 if there is no line number. - Added in version 3.12.