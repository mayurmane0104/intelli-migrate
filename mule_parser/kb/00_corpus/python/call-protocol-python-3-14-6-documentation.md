# Call Protocol — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/call.html](https://docs.python.org/c-api/call.html)

---

# Call Protocol[¶](#call-protocol)

CPython supports two different calling protocols:
*tp_call* and vectorcall.

## The *tp_call* Protocol[¶](#the-tp-call-protocol)

Instances of classes that set [ tp_call](typeobj.html#c.PyTypeObject.tp_call) are callable.
The signature of the slot is:

```
PyObject *tp_call(PyObject *callable, PyObject *args, PyObject *kwargs);
```
A call is made using a tuple for the positional arguments
and a dict for the keyword arguments, similarly to
`callable(*args, **kwargs)` in Python code.
*args* must be non-NULL (use an empty tuple if there are no arguments)
but *kwargs* may be *NULL* if there are no keyword arguments.

This convention is not only used by *tp_call*:
[ tp_new](typeobj.html#c.PyTypeObject.tp_new) and 

[also pass arguments this way.](typeobj.html#c.PyTypeObject.tp_init)

`tp_init`To call an object, use [ PyObject_Call()](#c.PyObject_Call) or another

[call API](#capi-call).

## The Vectorcall Protocol[¶](#the-vectorcall-protocol)

Added in version 3.9.

The vectorcall protocol was introduced in [ PEP 590](https://peps.python.org/pep-0590/) as an additional protocol
for making calls more efficient.

As rule of thumb, CPython will prefer the vectorcall for internal calls
if the callable supports it. However, this is not a hard rule.
Additionally, some third-party extensions use *tp_call* directly
(rather than using [ PyObject_Call()](#c.PyObject_Call)).
Therefore, a class supporting vectorcall must also implement

[. Moreover, the callable must behave the same regardless of which protocol is used. The recommended way to achieve this is by setting](typeobj.html#c.PyTypeObject.tp_call)

`tp_call``tp_call` to [. This bears repeating:](#c.PyVectorcall_Call)

`PyVectorcall_Call()`Warning

A class supporting vectorcall **must** also implement
[ tp_call](typeobj.html#c.PyTypeObject.tp_call) with the same semantics.

Changed in version 3.12: The [ Py_TPFLAGS_HAVE_VECTORCALL](typeobj.html#c.Py_TPFLAGS_HAVE_VECTORCALL) flag is now removed from a class
when the class’s 

[method is reassigned. (This internally sets](../reference/datamodel.html#object.__call__)

`__call__()`[only, and thus may make it behave differently than the vectorcall function.) In earlier Python versions, vectorcall should only be used with](typeobj.html#c.PyTypeObject.tp_call)

`tp_call`[or static types.](typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE)

`immutable`A class should not implement vectorcall if that would be slower
than *tp_call*. For example, if the callee needs to convert
the arguments to an args tuple and kwargs dict anyway, then there is no point
in implementing vectorcall.

Classes can implement the vectorcall protocol by enabling the
[ Py_TPFLAGS_HAVE_VECTORCALL](typeobj.html#c.Py_TPFLAGS_HAVE_VECTORCALL) flag and setting

[to the offset inside the object structure where a](typeobj.html#c.PyTypeObject.tp_vectorcall_offset)

`tp_vectorcall_offset`*vectorcallfunc*appears. This is a pointer to a function with the following signature:

- 
typedef [PyObject](structures.html#c.PyObject)*(*vectorcallfunc)([PyObject](structures.html#c.PyObject)*callable,[PyObject](structures.html#c.PyObject)*const *args, size_t nargsf,[PyObject](structures.html#c.PyObject)*kwnames)[¶](#c.vectorcallfunc)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.12.

- *callable*is the object being called.
- *args*is a C array consisting of the positional arguments followed by the
- values of the keyword arguments. This can be - *NULL*if there are no arguments.
 
- *nargsf*is the number of positional arguments plus possibly the
- `PY_VECTORCALL_ARGUMENTS_OFFSET`- *nargsf*, use- `PyVectorcall_NARGS()`
 
- *kwnames*is a tuple containing the names of the keyword arguments;
- in other words, the keys of the kwargs dict. These names must be strings (instances of - `str`or a subclass) and they must be unique. If there are no keyword arguments, then- *kwnames*can instead be- *NULL*.
 

- 
PY_VECTORCALL_ARGUMENTS_OFFSET[¶](#c.PY_VECTORCALL_ARGUMENTS_OFFSET)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.12.- If this flag is set in a vectorcall - *nargsf*argument, the callee is allowed to temporarily change- `args[-1]`. In other words,- *args*points to argument 1 (not 0) in the allocated vector. The callee must restore the value of- `args[-1]`before returning.- For - `PyObject_VectorcallMethod()`- `args[0]`may be changed.- Whenever they can do so cheaply (without additional allocation), callers are encouraged to use - `PY_VECTORCALL_ARGUMENTS_OFFSET`- *self*argument) very efficiently.- Added in version 3.8. 

To call an object that implements vectorcall, use a [call API](#capi-call)
function as with any other callable.
[ PyObject_Vectorcall()](#c.PyObject_Vectorcall) will usually be most efficient.

### Recursion Control[¶](#recursion-control)

When using *tp_call*, callees do not need to worry about
[recursion](exceptions.html#recursion): CPython uses
[ Py_EnterRecursiveCall()](exceptions.html#c.Py_EnterRecursiveCall) and 

[for calls made using](exceptions.html#c.Py_LeaveRecursiveCall)

`Py_LeaveRecursiveCall()`*tp_call*.

For efficiency, this is not the case for calls done using vectorcall:
the callee should use *Py_EnterRecursiveCall* and *Py_LeaveRecursiveCall*
if needed.

### Vectorcall Support API[¶](#vectorcall-support-api)

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)PyVectorcall_NARGS(size_t nargsf)[¶](#c.PyVectorcall_NARGS)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.12.- Given a vectorcall - *nargsf*argument, return the actual number of arguments. Currently equivalent to:- (Py_ssize_t)(nargsf & ~PY_VECTORCALL_ARGUMENTS_OFFSET) - However, the function - `PyVectorcall_NARGS`should be used to allow for future extensions.- Added in version 3.8. 

- 
[vectorcallfunc](#c.vectorcallfunc)PyVectorcall_Function([PyObject](structures.html#c.PyObject)*op)[¶](#c.PyVectorcall_Function)
- If - *op*does not support the vectorcall protocol (either because the type does not or because the specific instance does not), return- *NULL*. Otherwise, return the vectorcall function pointer stored in- *op*. This function never raises an exception.- This is mostly useful to check whether or not - *op*supports vectorcall, which can be done by checking- `PyVectorcall_Function(op) != NULL`.- Added in version 3.9. 

- 
[PyObject](structures.html#c.PyObject)*PyVectorcall_Call([PyObject](structures.html#c.PyObject)*callable,[PyObject](structures.html#c.PyObject)*tuple,[PyObject](structures.html#c.PyObject)*dict)[¶](#c.PyVectorcall_Call)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.12.- Call - *callable*’s- `vectorcallfunc`- This is a specialized function, intended to be put in the - `tp_call`- `tp_call`. It does not check the- `Py_TPFLAGS_HAVE_VECTORCALL`- `tp_call`.- Added in version 3.8. 

## Object Calling API[¶](#object-calling-api)

Various functions are available for calling a Python object.
Each converts its arguments to a convention supported by the called object –
either *tp_call* or vectorcall.
In order to do as little conversion as possible, pick one that best fits
the format of data you have available.

The following table summarizes the available functions; please see individual documentation for details.

| Function | callable | args | kwargs | 
|---|---|---|---|
| 
 | tuple | dict/ | |
| 
 | — | — | |
| 
 | 1 object | — | |
| 
 | tuple/ | — | |
| 
 | format | — | |
| obj +  | format | — | |
| 
 | variadic | — | |
| obj + name | variadic | — | |
| obj + name | — | — | |
| obj + name | 1 object | — | |
| 
 | vectorcall | vectorcall | |
| 
 | vectorcall | dict/ | |
| arg + name | vectorcall | vectorcall | 

- 
[PyObject](structures.html#c.PyObject)*PyObject_Call([PyObject](structures.html#c.PyObject)*callable,[PyObject](structures.html#c.PyObject)*args,[PyObject](structures.html#c.PyObject)*kwargs)[¶](#c.PyObject_Call)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Call a callable Python object - *callable*, with arguments given by the tuple- *args*, and named arguments given by the dictionary- *kwargs*.- *args*must not be- *NULL*; use an empty tuple if no arguments are needed. If no named arguments are needed,- *kwargs*can be- *NULL*.- Return the result of the call on success, or raise an exception and return - *NULL*on failure.- This is the equivalent of the Python expression: - `callable(*args, **kwargs)`.

- 
[PyObject](structures.html#c.PyObject)*PyObject_CallNoArgs([PyObject](structures.html#c.PyObject)*callable)[¶](#c.PyObject_CallNoArgs)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- Call a callable Python object - *callable*without any arguments. It is the most efficient way to call a callable Python object without any argument.- Return the result of the call on success, or raise an exception and return - *NULL*on failure.- Added in version 3.9. 

- 
[PyObject](structures.html#c.PyObject)*PyObject_CallOneArg([PyObject](structures.html#c.PyObject)*callable,[PyObject](structures.html#c.PyObject)*arg)[¶](#c.PyObject_CallOneArg)
- *Return value: New reference.*- Call a callable Python object - *callable*with exactly 1 positional argument- *arg*and no keyword arguments.- Return the result of the call on success, or raise an exception and return - *NULL*on failure.- Added in version 3.9. 

- 
[PyObject](structures.html#c.PyObject)*PyObject_CallObject([PyObject](structures.html#c.PyObject)*callable,[PyObject](structures.html#c.PyObject)*args)[¶](#c.PyObject_CallObject)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Call a callable Python object - *callable*, with arguments given by the tuple- *args*. If no arguments are needed, then- *args*can be- *NULL*.- Return the result of the call on success, or raise an exception and return - *NULL*on failure.- This is the equivalent of the Python expression: - `callable(*args)`.

- 
[PyObject](structures.html#c.PyObject)*PyObject_CallFunction([PyObject](structures.html#c.PyObject)*callable, const char *format, ...)[¶](#c.PyObject_CallFunction)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Call a callable Python object - *callable*, with a variable number of C arguments. The C arguments are described using a- `Py_BuildValue()`- *NULL*, indicating that no arguments are provided.- Return the result of the call on success, or raise an exception and return - *NULL*on failure.- This is the equivalent of the Python expression: - `callable(*args)`.- Note that if you only pass - [PyObject](structures.html#c.PyObject)* args,- `PyObject_CallFunctionObjArgs()`- Changed in version 3.4: The type of - *format*was changed from- `char *`.

- 
[PyObject](structures.html#c.PyObject)*PyObject_CallMethod([PyObject](structures.html#c.PyObject)*obj, const char *name, const char *format, ...)[¶](#c.PyObject_CallMethod)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Call the method named - *name*of object- *obj*with a variable number of C arguments. The C arguments are described by a- `Py_BuildValue()`- The format can be - *NULL*, indicating that no arguments are provided.- Return the result of the call on success, or raise an exception and return - *NULL*on failure.- This is the equivalent of the Python expression: - `obj.name(arg1, arg2, ...)`.- Note that if you only pass - [PyObject](structures.html#c.PyObject)* args,- `PyObject_CallMethodObjArgs()`- Changed in version 3.4: The types of - *name*and- *format*were changed from- `char *`.

- 
[PyObject](structures.html#c.PyObject)*PyObject_CallFunctionObjArgs([PyObject](structures.html#c.PyObject)*callable, ...)[¶](#c.PyObject_CallFunctionObjArgs)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Call a callable Python object - *callable*, with a variable number of- [PyObject](structures.html#c.PyObject)* arguments. The arguments are provided as a variable number of parameters followed by- *NULL*.- Return the result of the call on success, or raise an exception and return - *NULL*on failure.- This is the equivalent of the Python expression: - `callable(arg1, arg2, ...)`.

- 
[PyObject](structures.html#c.PyObject)*PyObject_CallMethodObjArgs([PyObject](structures.html#c.PyObject)*obj,[PyObject](structures.html#c.PyObject)*name, ...)[¶](#c.PyObject_CallMethodObjArgs)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Call a method of the Python object - *obj*, where the name of the method is given as a Python string object in- *name*. It is called with a variable number of- [PyObject](structures.html#c.PyObject)* arguments. The arguments are provided as a variable number of parameters followed by- *NULL*.- Return the result of the call on success, or raise an exception and return - *NULL*on failure.

- 
[PyObject](structures.html#c.PyObject)*PyObject_CallMethodNoArgs([PyObject](structures.html#c.PyObject)*obj,[PyObject](structures.html#c.PyObject)*name)[¶](#c.PyObject_CallMethodNoArgs)
- Call a method of the Python object - *obj*without arguments, where the name of the method is given as a Python string object in- *name*.- Return the result of the call on success, or raise an exception and return - *NULL*on failure.- Added in version 3.9. 

- 
[PyObject](structures.html#c.PyObject)*PyObject_CallMethodOneArg([PyObject](structures.html#c.PyObject)*obj,[PyObject](structures.html#c.PyObject)*name,[PyObject](structures.html#c.PyObject)*arg)[¶](#c.PyObject_CallMethodOneArg)
- Call a method of the Python object - *obj*with a single positional argument- *arg*, where the name of the method is given as a Python string object in- *name*.- Return the result of the call on success, or raise an exception and return - *NULL*on failure.- Added in version 3.9. 

- 
[PyObject](structures.html#c.PyObject)*PyObject_Vectorcall([PyObject](structures.html#c.PyObject)*callable,[PyObject](structures.html#c.PyObject)*const *args, size_t nargsf,[PyObject](structures.html#c.PyObject)*kwnames)[¶](#c.PyObject_Vectorcall)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.12.- Call a callable Python object - *callable*. The arguments are the same as for- `vectorcallfunc`- *callable*supports- [vectorcall](#vectorcall), this directly calls the vectorcall function stored in- *callable*.- Return the result of the call on success, or raise an exception and return - *NULL*on failure.- Added in version 3.8: as - `_PyObject_Vectorcall`- Changed in version 3.9: Renamed to the current name, without the leading underscore. The old provisional name is - [soft deprecated](../glossary.html#term-soft-deprecated).

- 
[PyObject](structures.html#c.PyObject)*PyObject_VectorcallDict([PyObject](structures.html#c.PyObject)*callable,[PyObject](structures.html#c.PyObject)*const *args, size_t nargsf,[PyObject](structures.html#c.PyObject)*kwdict)[¶](#c.PyObject_VectorcallDict)
- Call - *callable*with positional arguments passed exactly as in the- [vectorcall](#vectorcall)protocol, but with keyword arguments passed as a dictionary- *kwdict*. The- *args*array contains only the positional arguments.- Regardless of which protocol is used internally, a conversion of arguments needs to be done. Therefore, this function should only be used if the caller already has a dictionary ready to use for the keyword arguments, but not a tuple for the positional arguments. - Added in version 3.9. 

- 
[PyObject](structures.html#c.PyObject)*PyObject_VectorcallMethod([PyObject](structures.html#c.PyObject)*name,[PyObject](structures.html#c.PyObject)*const *args, size_t nargsf,[PyObject](structures.html#c.PyObject)*kwnames)[¶](#c.PyObject_VectorcallMethod)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.12.- Call a method using the vectorcall calling convention. The name of the method is given as a Python string - *name*. The object whose method is called is- *args[0]*, and the- *args*array starting at- *args[1]*represents the arguments of the call. There must be at least one positional argument.- *nargsf*is the number of positional arguments including- *args[0]*, plus- `PY_VECTORCALL_ARGUMENTS_OFFSET`- `args[0]`may temporarily be changed. Keyword arguments can be passed just like in- `PyObject_Vectorcall()`- If the object has the - `Py_TPFLAGS_METHOD_DESCRIPTOR`- *args*vector as arguments.- Return the result of the call on success, or raise an exception and return - *NULL*on failure.- Added in version 3.9. 

## Call Support API[¶](#call-support-api)

- 
int PyCallable_Check([PyObject](structures.html#c.PyObject)*o)[¶](#c.PyCallable_Check)
- *Part of the*- [Stable ABI](stable.html#stable).- Determine if the object - *o*is callable. Return- `1`if the object is callable and- `0`otherwise. This function always succeeds.