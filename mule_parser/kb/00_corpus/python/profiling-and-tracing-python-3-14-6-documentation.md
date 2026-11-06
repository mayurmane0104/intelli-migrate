# Profiling and tracing — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/profiling.html](https://docs.python.org/c-api/profiling.html)

---

# Profiling and tracing[¶](#profiling-and-tracing)

The Python interpreter provides some low-level support for attaching profiling and execution tracing facilities. These are used for profiling, debugging, and coverage analysis tools.

This C interface allows the profiling or tracing code to avoid the overhead of calling through Python-level callable objects, making a direct C function call instead. The essential attributes of the facility have not changed; the interface allows trace functions to be installed per-thread, and the basic events reported to the trace function are the same as had been reported to the Python-level trace functions in previous versions.

- 
typedef int (*Py_tracefunc)([PyObject](structures.html#c.PyObject)*obj,[PyFrameObject](frame.html#c.PyFrameObject)*frame, int what,[PyObject](structures.html#c.PyObject)*arg)[¶](#c.Py_tracefunc)
- The type of the trace function registered using - `PyEval_SetProfile()`- `PyEval_SetTrace()`- *obj*,- *frame*is the frame object to which the event pertains,- *what*is one of the constants- `PyTrace_CALL`- `PyTrace_EXCEPTION`- `PyTrace_LINE`- `PyTrace_RETURN`- `PyTrace_C_CALL`- `PyTrace_C_EXCEPTION`- `PyTrace_C_RETURN`- `PyTrace_OPCODE`- *arg*depends on the value of- *what*:- Value of - *what*- Meaning of - *arg*- Always - `Py_None`- Exception information as returned by - `sys.exc_info()`- Always - `Py_None`- Value being returned to the caller, or - `NULL`if caused by an exception.- Function object being called. - Function object being called. - Function object being called. - Always - `Py_None`

- 
int PyTrace_CALL[¶](#c.PyTrace_CALL)
- The value of the - *what*parameter to a- `Py_tracefunc`

- 
int PyTrace_EXCEPTION[¶](#c.PyTrace_EXCEPTION)
- The value of the - *what*parameter to a- `Py_tracefunc`- *what*when after any bytecode is processed after which the exception becomes set within the frame being executed. The effect of this is that as exception propagation causes the Python stack to unwind, the callback is called upon return to each frame as the exception propagates. Only trace functions receive these events; they are not needed by the profiler.

- 
int PyTrace_LINE[¶](#c.PyTrace_LINE)
- The value passed as the - *what*parameter to a- `Py_tracefunc`- `f_trace_lines`- *0*on that frame.

- 
int PyTrace_RETURN[¶](#c.PyTrace_RETURN)
- The value for the - *what*parameter to- `Py_tracefunc`

- 
int PyTrace_C_CALL[¶](#c.PyTrace_C_CALL)
- The value for the - *what*parameter to- `Py_tracefunc`

- 
int PyTrace_C_EXCEPTION[¶](#c.PyTrace_C_EXCEPTION)
- The value for the - *what*parameter to- `Py_tracefunc`

- 
int PyTrace_C_RETURN[¶](#c.PyTrace_C_RETURN)
- The value for the - *what*parameter to- `Py_tracefunc`

- 
int PyTrace_OPCODE[¶](#c.PyTrace_OPCODE)
- The value for the - *what*parameter to- `Py_tracefunc`- `f_trace_opcodes`- *1*on the frame.

- 
void PyEval_SetProfile([Py_tracefunc](#c.Py_tracefunc)func,[PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyEval_SetProfile)
- Set the profiler function to - *func*. The- *obj*parameter is passed to the function as its first parameter, and may be any Python object, or- `NULL`. If the profile function needs to maintain state, using a different value for- *obj*for each thread provides a convenient and thread-safe place to store it. The profile function is called for all monitored events except- `PyTrace_LINE`- `PyTrace_OPCODE`- `PyTrace_EXCEPTION`- See also the - `sys.setprofile()`- The caller must have an - [attached thread state](../glossary.html#term-attached-thread-state).

- 
void PyEval_SetProfileAllThreads([Py_tracefunc](#c.Py_tracefunc)func,[PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyEval_SetProfileAllThreads)
- Like - `PyEval_SetProfile()`- The caller must have an - [attached thread state](../glossary.html#term-attached-thread-state).- As - `PyEval_SetProfile()`

Added in version 3.12.

- 
void PyEval_SetTrace([Py_tracefunc](#c.Py_tracefunc)func,[PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyEval_SetTrace)
- Set the tracing function to - *func*. This is similar to- `PyEval_SetProfile()`- `PyEval_SetTrace()`- `PyTrace_C_CALL`- `PyTrace_C_EXCEPTION`- `PyTrace_C_RETURN`- *what*parameter.- See also the - `sys.settrace()`- The caller must have an - [attached thread state](../glossary.html#term-attached-thread-state).

- 
void PyEval_SetTraceAllThreads([Py_tracefunc](#c.Py_tracefunc)func,[PyObject](structures.html#c.PyObject)*obj)[¶](#c.PyEval_SetTraceAllThreads)
- Like - `PyEval_SetTrace()`- The caller must have an - [attached thread state](../glossary.html#term-attached-thread-state).- As - `PyEval_SetTrace()`

Added in version 3.12.

# Reference tracing[¶](#reference-tracing)

Added in version 3.13.

- 
typedef int (*PyRefTracer)([PyObject](structures.html#c.PyObject)*, int event, void *data)[¶](#c.PyRefTracer)
- The type of the trace function registered using - `PyRefTracer_SetTracer()`- **event**is set to- `PyRefTracer_CREATE`- **event**is set to- `PyRefTracer_DESTROY`- **data**argument is the opaque pointer that was provided when- `PyRefTracer_SetTracer()`was called.- If a new tracing function is registered replacing the current one, a call to the trace function will be made with the object set to - **NULL**and- **event**set to- `PyRefTracer_TRACKER_REMOVED`

Added in version 3.13.

- 
int PyRefTracer_CREATE[¶](#c.PyRefTracer_CREATE)
- The value for the - *event*parameter to- `PyRefTracer`

- 
int PyRefTracer_DESTROY[¶](#c.PyRefTracer_DESTROY)
- The value for the - *event*parameter to- `PyRefTracer`

- 
int PyRefTracer_TRACKER_REMOVED[¶](#c.PyRefTracer_TRACKER_REMOVED)
- The value for the - *event*parameter to- `PyRefTracer`- Added in version 3.14. 

- 
int PyRefTracer_SetTracer([PyRefTracer](#c.PyRefTracer)tracer, void *data)[¶](#c.PyRefTracer_SetTracer)
- Register a reference tracer function. The function will be called when a new Python object has been created or when an object is going to be destroyed. If - **data**is provided it must be an opaque pointer that will be provided when the tracer function is called. Return- `0`on success. Set an exception and return- `-1`on error.- Note that tracer functions - **must not**create Python objects inside or otherwise the call will be re-entrant. The tracer also- **must not**clear any existing exception or set an exception. A- [thread state](../glossary.html#term-thread-state)will be active every time the tracer function is called.- There must be an - [attached thread state](../glossary.html#term-attached-thread-state)when calling this function.- If another tracer function was already registered, the old function will be called with - **event**set to- `PyRefTracer_TRACKER_REMOVED`

Added in version 3.13.

- 
[PyRefTracer](#c.PyRefTracer)PyRefTracer_GetTracer(void **data)[¶](#c.PyRefTracer_GetTracer)
- Get the registered reference tracer function and the value of the opaque data pointer that was registered when - `PyRefTracer_SetTracer()`- **data**pointer to NULL.- There must be an - [attached thread state](../glossary.html#term-attached-thread-state)when calling this function.

Added in version 3.13.