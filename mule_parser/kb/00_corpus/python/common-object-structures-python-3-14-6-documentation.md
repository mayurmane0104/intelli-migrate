# Common Object Structures — Python 3.14.6 documentation

**Source:** [https://docs.python.org/c-api/structures.html](https://docs.python.org/c-api/structures.html)

---

# Common Object Structures[¶](#common-object-structures)

There are a large number of structures which are used in the definition of object types for Python. This section describes these structures and how they are used.

## Base object types and macros[¶](#base-object-types-and-macros)

All Python objects ultimately share a small number of fields at the beginning
of the object’s representation in memory.  These are represented by the
[ PyObject](#c.PyObject) and 

[types, which are defined, in turn, by the expansions of some macros also used, whether directly or indirectly, in the definition of all other Python objects. Additional macros can be found under](#c.PyVarObject)

`PyVarObject`[reference counting](refcounting.html#countingrefs).

- 
type PyObject[¶](#c.PyObject)
- *Part of the*- [Limited API](stable.html#stable). (Only some members are part of the stable ABI.)- All object types are extensions of this type. This is a type which contains the information Python needs to treat a pointer to an object as an object. In a normal “release” build, it contains only the object’s reference count and a pointer to the corresponding type object. Nothing is actually declared to be a - `PyObject`- [PyObject](#c.PyObject)*.- The members must not be accessed directly; instead use macros such as - `Py_REFCNT`- `Py_TYPE`- 
[Py_ssize_t](intro.html#c.Py_ssize_t)ob_refcnt[¶](#c.PyObject.ob_refcnt)
- *Part of the*- [Stable ABI](stable.html#stable).- The object’s reference count, as returned by - `Py_REFCNT`- `Py_REFCNT`,- `Py_INCREF()`- `Py_DecRef()`- The field type may be different from - `Py_ssize_t`, depending on build configuration and platform.
 - 
[PyTypeObject](type.html#c.PyTypeObject)*ob_type[¶](#c.PyObject.ob_type)
- *Part of the*- [Stable ABI](stable.html#stable).- The object’s type. Do not use this field directly; use - `Py_TYPE`- `Py_SET_TYPE()`
 
- 

- 
type PyVarObject[¶](#c.PyVarObject)
- *Part of the*- [Limited API](stable.html#stable). (Only some members are part of the stable ABI.)- An extension of - `PyObject`- `ob_size`- *length*.- As with - `PyObject`, the members must not be accessed directly; instead use macros such as- `Py_SIZE`- `Py_REFCNT`- `Py_TYPE`- 
[Py_ssize_t](intro.html#c.Py_ssize_t)ob_size[¶](#c.PyVarObject.ob_size)
- *Part of the*- [Stable ABI](stable.html#stable).- A size field, whose contents should be considered an object’s internal implementation detail. - Do not use this field directly; use - `Py_SIZE`- Object creation functions such as - `PyObject_NewVar()`- `ob_size`using- `Py_SET_SIZE`- To get an object’s publicly exposed length, as returned by the Python function - `len()`- `PyObject_Length()`
 
- 

- 
PyObject_HEAD[¶](#c.PyObject_HEAD)
- This is a macro used when declaring new types which represent objects without a varying length. The PyObject_HEAD macro expands to: - PyObject ob_base; - See documentation of - `PyObject`

- 
PyObject_VAR_HEAD[¶](#c.PyObject_VAR_HEAD)
- This is a macro used when declaring new types which represent objects with a length that varies from instance to instance. The PyObject_VAR_HEAD macro expands to: - PyVarObject ob_base; - See documentation of - `PyVarObject`

- 
[PyTypeObject](type.html#c.PyTypeObject)PyBaseObject_Type[¶](#c.PyBaseObject_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- The base class of all other objects, the same as - `object`

- 
int Py_Is([PyObject](#c.PyObject)*x,[PyObject](#c.PyObject)*y)[¶](#c.Py_Is)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- Test if the - *x*object is the- *y*object, the same as- `x is y`in Python.- Added in version 3.10. 

- 
int Py_IsNone([PyObject](#c.PyObject)*x)[¶](#c.Py_IsNone)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- Test if an object is the - `None`singleton, the same as- `x is None`in Python.- Added in version 3.10. 

- 
int Py_IsTrue([PyObject](#c.PyObject)*x)[¶](#c.Py_IsTrue)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- Test if an object is the - `True`singleton, the same as- `x is True`in Python.- Added in version 3.10. 

- 
int Py_IsFalse([PyObject](#c.PyObject)*x)[¶](#c.Py_IsFalse)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- Test if an object is the - `False`singleton, the same as- `x is False`in Python.- Added in version 3.10. 

- 
[PyTypeObject](type.html#c.PyTypeObject)*Py_TYPE([PyObject](#c.PyObject)*o)[¶](#c.Py_TYPE)
- *Return value: Borrowed reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.14.- Get the type of the Python object - *o*.- The returned reference is - [borrowed](../glossary.html#term-borrowed-reference)from- *o*. Do not release it with- `Py_DECREF()`

- 
int Py_IS_TYPE([PyObject](#c.PyObject)*o,[PyTypeObject](type.html#c.PyTypeObject)*type)[¶](#c.Py_IS_TYPE)
- Return non-zero if the object - *o*type is- *type*. Return zero otherwise. Equivalent to:- `Py_TYPE(o) == type`.- Added in version 3.9. 

- 
void Py_SET_TYPE([PyObject](#c.PyObject)*o,[PyTypeObject](type.html#c.PyTypeObject)*type)[¶](#c.Py_SET_TYPE)
- Set the type of object - *o*to- *type*, without any checking or reference counting.- This is a very low-level operation. Consider instead setting the Python attribute - `__class__`- `PyObject_SetAttrString()`- Note that assigning an incompatible type can lead to undefined behavior. - If - *type*is a- [heap type](typeobj.html#heap-types), the caller must create a new reference to it. Similarly, if the old type of- *o*is a heap type, the caller must release a reference to that type.- Added in version 3.9. 

- 
[Py_ssize_t](intro.html#c.Py_ssize_t)Py_SIZE([PyVarObject](#c.PyVarObject)*o)[¶](#c.Py_SIZE)
- Get the - `ob_size`- *o*.- Changed in version 3.11: - `Py_SIZE()`- [PyVarObject](#c.PyVarObject)*.

- 
void Py_SET_SIZE([PyVarObject](#c.PyVarObject)*o,[Py_ssize_t](intro.html#c.Py_ssize_t)size)[¶](#c.Py_SET_SIZE)
- Set the - `ob_size`- *o*to- *size*.- Added in version 3.9. 

- 
PyObject_HEAD_INIT(type)[¶](#c.PyObject_HEAD_INIT)
- This is a macro which expands to initialization values for a new - `PyObject`- _PyObject_EXTRA_INIT 1, type, 

- 
PyVarObject_HEAD_INIT(type, size)[¶](#c.PyVarObject_HEAD_INIT)
- This is a macro which expands to initialization values for a new - `PyVarObject`- `ob_size`- _PyObject_EXTRA_INIT 1, type, size, 

## Implementing functions and methods[¶](#implementing-functions-and-methods)

- 
type PyCFunction[¶](#c.PyCFunction)
- *Part of the*- [Stable ABI](stable.html#stable).- Type of the functions used to implement most Python callables in C. Functions of this type take two - [PyObject](#c.PyObject)* parameters and return one such value. If the return value is- `NULL`, an exception shall have been set. If not- `NULL`, the return value is interpreted as the return value of the function as exposed in Python. The function must return a new reference.- The function signature is: - PyObject *PyCFunction(PyObject *self, PyObject *args); 

- 
type PyCFunctionWithKeywords[¶](#c.PyCFunctionWithKeywords)
- *Part of the*- [Stable ABI](stable.html#stable).- Type of the functions used to implement Python callables in C with signature - [METH_VARARGS | METH_KEYWORDS](#meth-varargs-meth-keywords). The function signature is:- PyObject *PyCFunctionWithKeywords(PyObject *self, PyObject *args, PyObject *kwargs); 

- 
type PyCFunctionFast[¶](#c.PyCFunctionFast)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Type of the functions used to implement Python callables in C with signature - `METH_FASTCALL`- PyObject *PyCFunctionFast(PyObject *self, PyObject *const *args, Py_ssize_t nargs); 

- 
type PyCFunctionFastWithKeywords[¶](#c.PyCFunctionFastWithKeywords)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.13.- Type of the functions used to implement Python callables in C with signature - [METH_FASTCALL | METH_KEYWORDS](#meth-fastcall-meth-keywords). The function signature is:- PyObject *PyCFunctionFastWithKeywords(PyObject *self, PyObject *const *args, Py_ssize_t nargs, PyObject *kwnames); 

- 
type PyCMethod[¶](#c.PyCMethod)
- Type of the functions used to implement Python callables in C with signature - [METH_METHOD | METH_FASTCALL | METH_KEYWORDS](#meth-method-meth-fastcall-meth-keywords). The function signature is:- PyObject *PyCMethod(PyObject *self, PyTypeObject *defining_class, PyObject *const *args, Py_ssize_t nargs, PyObject *kwnames) - Added in version 3.9. 

- 
type PyMethodDef[¶](#c.PyMethodDef)
- *Part of the*- [Stable ABI](stable.html#stable)(including all members).- Structure used to describe a method of an extension type. This structure has four fields: - 
const char *ml_name[¶](#c.PyMethodDef.ml_name)
- Name of the method. 
 - 
[PyCFunction](#c.PyCFunction)ml_meth[¶](#c.PyMethodDef.ml_meth)
- Pointer to the C implementation. 
 - 
int ml_flags[¶](#c.PyMethodDef.ml_flags)
- Flags bits indicating how the call should be constructed. 
 - 
const char *ml_doc[¶](#c.PyMethodDef.ml_doc)
- Points to the contents of the docstring. 
 
- 
const char *ml_name

The [ ml_meth](#c.PyMethodDef.ml_meth) is a C function pointer.
The functions may be of different
types, but they always return 

[PyObject](#c.PyObject)*. If the function is not of the

[, the compiler will require a cast in the method table. Even though](#c.PyCFunction)

`PyCFunction``PyCFunction` defines the first parameter as
PyObject*, it is common that the method implementation uses the
specific C type of the *self*object.

The [ ml_flags](#c.PyMethodDef.ml_flags) field is a bitfield which can include
the following flags.
The individual flags indicate either a calling convention or a binding
convention.

There are these calling conventions:

- 
METH_VARARGS[¶](#c.METH_VARARGS)
- *Part of the*- [Stable ABI](stable.html#stable).- This is the typical calling convention, where the methods have the type - `PyCFunction`- [PyObject](#c.PyObject)* values. The first one is the- *self*object for methods; for module functions, it is the module object. The second parameter (often called- *args*) is a tuple object representing all arguments. This parameter is typically processed using- `PyArg_ParseTuple()`- `PyArg_UnpackTuple()`

- 
METH_KEYWORDS[¶](#c.METH_KEYWORDS)
- Can only be used in certain combinations with other flags: - [METH_VARARGS | METH_KEYWORDS](#meth-varargs-meth-keywords),- [METH_FASTCALL | METH_KEYWORDS](#meth-fastcall-meth-keywords)and- [METH_METHOD | METH_FASTCALL | METH_KEYWORDS](#meth-method-meth-fastcall-meth-keywords).

- [METH_VARARGS](#c.METH_VARARGS)|- [METH_KEYWORDS](#c.METH_KEYWORDS)
- Methods with these flags must be of type - `PyCFunctionWithKeywords`- *self*,- *args*,- *kwargs*where- *kwargs*is a dictionary of all the keyword arguments or possibly- `NULL`if there are no keyword arguments. The parameters are typically processed using- `PyArg_ParseTupleAndKeywords()`

- 
METH_FASTCALL[¶](#c.METH_FASTCALL)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.10.- Fast calling convention supporting only positional arguments. The methods have the type - `PyCFunctionFast`- *self*, the second parameter is a C array of- [PyObject](#c.PyObject)* values indicating the arguments and the third parameter is the number of arguments (the length of the array).- Added in version 3.7. - Changed in version 3.10: - `METH_FASTCALL`is now part of the- [stable ABI](stable.html#stable-abi).

- [METH_FASTCALL](#c.METH_FASTCALL)|- [METH_KEYWORDS](#c.METH_KEYWORDS)
- Extension of - `METH_FASTCALL`- `PyCFunctionFastWithKeywords`- [vectorcall protocol](call.html#vectorcall): there is an additional fourth- [PyObject](#c.PyObject)* parameter which is a tuple representing the names of the keyword arguments (which are guaranteed to be strings) or possibly- `NULL`if there are no keywords. The values of the keyword arguments are stored in the- *args*array, after the positional arguments.- Added in version 3.7. 

- 
METH_METHOD[¶](#c.METH_METHOD)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.7.- Can only be used in the combination with other flags: - [METH_METHOD | METH_FASTCALL | METH_KEYWORDS](#meth-method-meth-fastcall-meth-keywords).

- [METH_METHOD](#c.METH_METHOD)|- [METH_FASTCALL](#c.METH_FASTCALL)|- [METH_KEYWORDS](#c.METH_KEYWORDS)
- Extension of - [METH_FASTCALL | METH_KEYWORDS](#meth-fastcall-meth-keywords)supporting the- *defining class*, that is, the class that contains the method in question. The defining class might be a superclass of- `Py_TYPE(self)`.- The method needs to be of type - `PyCMethod`- `METH_FASTCALL | METH_KEYWORDS`with- `defining_class`argument added after- `self`.- Added in version 3.9. 

- 
METH_NOARGS[¶](#c.METH_NOARGS)
- *Part of the*- [Stable ABI](stable.html#stable).- Methods without parameters don’t need to check whether arguments are given if they are listed with the - `METH_NOARGS`- `PyCFunction`- *self*and will hold a reference to the module or object instance. In all cases the second parameter will be- `NULL`.- The function must have 2 parameters. Since the second parameter is unused, - `Py_UNUSED`

- 
METH_O[¶](#c.METH_O)
- *Part of the*- [Stable ABI](stable.html#stable).- Methods with a single object argument can be listed with the - `METH_O`- `PyArg_ParseTuple()`- `"O"`argument. They have the type- `PyCFunction`- *self*parameter, and a- [PyObject](#c.PyObject)* parameter representing the single argument.

These two constants are not used to indicate the calling convention but the binding when used with methods of classes. These may not be used for functions defined for modules. At most one of these flags may be set for any given method.

- 
METH_CLASS[¶](#c.METH_CLASS)
- *Part of the*- [Stable ABI](stable.html#stable).- The method will be passed the type object as the first parameter rather than an instance of the type. This is used to create - *class methods*, similar to what is created when using the- `classmethod()`

- 
METH_STATIC[¶](#c.METH_STATIC)
- *Part of the*- [Stable ABI](stable.html#stable).- The method will be passed - `NULL`as the first parameter rather than an instance of the type. This is used to create- *static methods*, similar to what is created when using the- `staticmethod()`

One other constant controls whether a method is loaded in place of another definition with the same method name.

- 
METH_COEXIST[¶](#c.METH_COEXIST)
- *Part of the*- [Stable ABI](stable.html#stable).- The method will be loaded in place of existing definitions. Without - *METH_COEXIST*, the default is to skip repeated definitions. Since slot wrappers are loaded before the method table, the existence of a- *sq_contains*slot, for example, would generate a wrapped method named- `__contains__()`

- 
[PyTypeObject](type.html#c.PyTypeObject)PyCMethod_Type[¶](#c.PyCMethod_Type)
- The type object corresponding to Python C method objects. This is available as - `types.BuiltinMethodType`

- 
int PyCMethod_Check([PyObject](#c.PyObject)*op)[¶](#c.PyCMethod_Check)
- Return true if - *op*is an instance of the- `PyCMethod_Type`

- 
int PyCMethod_CheckExact([PyObject](#c.PyObject)*op)[¶](#c.PyCMethod_CheckExact)
- This is the same as - `PyCMethod_Check()`

- 
[PyObject](#c.PyObject)*PyCMethod_New([PyMethodDef](#c.PyMethodDef)*ml,[PyObject](#c.PyObject)*self,[PyObject](#c.PyObject)*module,[PyTypeObject](type.html#c.PyTypeObject)*cls)[¶](#c.PyCMethod_New)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.9.- Turn - *ml*into a Python- [callable](../glossary.html#term-callable)object. The caller must ensure that- *ml*outlives the callable. Typically,- *ml*is defined as a static variable.- The - *self*parameter will be passed as the- *self*argument to the C function in- `ml->ml_meth`when invoked.- *self*can be- `NULL`.- The - [callable](../glossary.html#term-callable)object’s- `__module__`attribute can be set from the given- *module*argument.- *module*should be a Python string, which will be used as name of the module the function is defined in. If unavailable, it can be set to- `None`- `NULL`.- See also - The - *cls*parameter will be passed as the- *defining_class*argument to the C function. Must be set if- `METH_METHOD`- `ml->ml_flags`.- Added in version 3.9. 

- 
[PyTypeObject](type.html#c.PyTypeObject)PyCFunction_Type[¶](#c.PyCFunction_Type)
- *Part of the*- [Stable ABI](stable.html#stable).- The type object corresponding to Python C function objects. This is available as - `types.BuiltinFunctionType`

- 
int PyCFunction_Check([PyObject](#c.PyObject)*op)[¶](#c.PyCFunction_Check)
- Return true if - *op*is an instance of the- `PyCFunction_Type`

- 
int PyCFunction_CheckExact([PyObject](#c.PyObject)*op)[¶](#c.PyCFunction_CheckExact)
- This is the same as - `PyCFunction_Check()`

- 
[PyObject](#c.PyObject)*PyCFunction_NewEx([PyMethodDef](#c.PyMethodDef)*ml,[PyObject](#c.PyObject)*self,[PyObject](#c.PyObject)*module)[¶](#c.PyCFunction_NewEx)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable).- Equivalent to - `PyCMethod_New(ml, self, module, NULL)`.

- 
[PyObject](#c.PyObject)*PyCFunction_New([PyMethodDef](#c.PyMethodDef)*ml,[PyObject](#c.PyObject)*self)[¶](#c.PyCFunction_New)
- *Return value: New reference.*- *Part of the*- [Stable ABI](stable.html#stable)since version 3.4.- Equivalent to - `PyCMethod_New(ml, self, NULL, NULL)`.

- 
int PyCFunction_GetFlags([PyObject](#c.PyObject)*func)[¶](#c.PyCFunction_GetFlags)
- *Part of the*- [Stable ABI](stable.html#stable).- Get the function’s flags on - *func*as they were passed to- `ml_flags`- If - *func*is not a C function object, this fails with an exception.- *func*must not be- `NULL`.- This function returns the function’s flags on success, and - `-1`with an exception set on failure.

- 
int PyCFunction_GET_FLAGS([PyObject](#c.PyObject)*func)[¶](#c.PyCFunction_GET_FLAGS)
- This is the same as - `PyCFunction_GetFlags()`

- 
[PyCFunction](#c.PyCFunction)PyCFunction_GetFunction([PyObject](#c.PyObject)*func)[¶](#c.PyCFunction_GetFunction)
- *Part of the*- [Stable ABI](stable.html#stable).- Get the function pointer on - *func*as it was passed to- `ml_meth`- If - *func*is not a C function object, this fails with an exception.- *func*must not be- `NULL`.- This function returns the function pointer on success, and - `NULL`with an exception set on failure.

- 
int PyCFunction_GET_FUNCTION([PyObject](#c.PyObject)*func)[¶](#c.PyCFunction_GET_FUNCTION)
- This is the same as - `PyCFunction_GetFunction()`

- 
[PyObject](#c.PyObject)*PyCFunction_GetSelf([PyObject](#c.PyObject)*func)[¶](#c.PyCFunction_GetSelf)
- *Part of the*- [Stable ABI](stable.html#stable).- Get the “self” object on - *func*. This is the object that would be passed to the first argument of a- `PyCFunction`- `PyMethodDef`- `PyModuleDef`- If - *func*is not a C function object, this fails with an exception.- *func*must not be- `NULL`.- This function returns a - [borrowed reference](../glossary.html#term-borrowed-reference)to the “self” object on success, and- `NULL`with an exception set on failure.

- 
[PyObject](#c.PyObject)*PyCFunction_GET_SELF([PyObject](#c.PyObject)*func)[¶](#c.PyCFunction_GET_SELF)
- This is the same as - `PyCFunction_GetSelf()`

## Accessing attributes of extension types[¶](#accessing-attributes-of-extension-types)

- 
type PyMemberDef[¶](#c.PyMemberDef)
- *Part of the*- [Stable ABI](stable.html#stable)(including all members).- Structure which describes an attribute of a type which corresponds to a C struct member. When defining a class, put a NULL-terminated array of these structures in the - `tp_members`- Its fields are, in order: - 
const char *name[¶](#c.PyMemberDef.name)
- Name of the member. A NULL value marks the end of a - `PyMemberDef[]`array.- The string should be static, no copy is made of it. 
 - 
int type[¶](#c.PyMemberDef.type)
- The type of the member in the C struct. See - [Member types](#pymemberdef-types)for the possible values.
 - 
[Py_ssize_t](intro.html#c.Py_ssize_t)offset[¶](#c.PyMemberDef.offset)
- The offset in bytes that the member is located on the type’s object struct. 
 - 
int flags[¶](#c.PyMemberDef.flags)
- Zero or more of the - [Member flags](#pymemberdef-flags), combined using bitwise OR.
 - 
const char *doc[¶](#c.PyMemberDef.doc)
- The docstring, or NULL. The string should be static, no copy is made of it. Typically, it is defined using - `PyDoc_STR`
 - By default (when - `flags`- `0`), members allow both read and write access. Use the- `Py_READONLY`- `Py_T_STRING`- `Py_READONLY`. Only- `Py_T_OBJECT_EX`- `T_OBJECT`- For heap-allocated types (created using - `PyType_FromSpec()`- `PyMemberDef`may contain a definition for the special member- `"__vectorcalloffset__"`, corresponding to- `tp_vectorcall_offset`- `Py_T_PYSSIZET`, and either- `Py_READONLY`or- `Py_READONLY | Py_RELATIVE_OFFSET`. For example:- static PyMemberDef spam_type_members[] = { {"__vectorcalloffset__", Py_T_PYSSIZET, offsetof(Spam_object, vectorcall), Py_READONLY}, {NULL} /* Sentinel */ }; - (You may need to - `#include <stddef.h>`for- `offsetof()`.)- The legacy offsets - `tp_dictoffset`- `tp_weaklistoffset`- `"__dictoffset__"`and- `"__weaklistoffset__"`members, but extensions are strongly encouraged to use- `Py_TPFLAGS_MANAGED_DICT`- `Py_TPFLAGS_MANAGED_WEAKREF`- Changed in version 3.12: - `PyMemberDef`is always available. Previously, it required including- `"structmember.h"`.- Changed in version 3.14: - `Py_RELATIVE_OFFSET`- `"__vectorcalloffset__"`,- `"__dictoffset__"`and- `"__weaklistoffset__"`.
- 
const char *name

- 
[PyObject](#c.PyObject)*PyMember_GetOne(const char *obj_addr, struct[PyMemberDef](#c.PyMemberDef)*m)[¶](#c.PyMember_GetOne)
- *Part of the*- [Stable ABI](stable.html#stable).- Get an attribute belonging to the object at address - *obj_addr*. The attribute is described by- `PyMemberDef`- *m*. Returns- `NULL`on error.- Changed in version 3.12: - `PyMember_GetOne`is always available. Previously, it required including- `"structmember.h"`.

- 
int PyMember_SetOne(char *obj_addr, struct [PyMemberDef](#c.PyMemberDef)*m,[PyObject](#c.PyObject)*o)[¶](#c.PyMember_SetOne)
- *Part of the*- [Stable ABI](stable.html#stable).- Set an attribute belonging to the object at address - *obj_addr*to object- *o*. The attribute to set is described by- `PyMemberDef`- *m*. Returns- `0`if successful and a negative value on failure.- Changed in version 3.12: - `PyMember_SetOne`is always available. Previously, it required including- `"structmember.h"`.

### Member flags[¶](#member-flags)

The following flags can be used with [ PyMemberDef.flags](#c.PyMemberDef.flags):

- 
Py_READONLY[¶](#c.Py_READONLY)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.12.- Not writable. 

- 
Py_AUDIT_READ[¶](#c.Py_AUDIT_READ)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.12.- Emit an - `object.__getattr__`- [audit event](../library/audit_events.html#audit-events)before reading.

- 
Py_RELATIVE_OFFSET[¶](#c.Py_RELATIVE_OFFSET)
- *Part of the*- [Stable ABI](stable.html#stable)since version 3.12.- Indicates that the - `offset`- `PyMemberDef`entry indicates an offset from the subclass-specific data, rather than from- `PyObject`.- Can only be used as part of the - `Py_tp_members`- `slot`- `basicsize`- `tp_members`- `PyMemberDef.offset`- `PyObject`struct.

Changed in version 3.10: The `RESTRICTED`, `READ_RESTRICTED` and
`WRITE_RESTRICTED` macros available with
`#include "structmember.h"` are deprecated.
`READ_RESTRICTED` and `RESTRICTED` are equivalent to
[ Py_AUDIT_READ](#c.Py_AUDIT_READ); 

`WRITE_RESTRICTED` does nothing.Changed in version 3.12: The `READONLY` macro was renamed to [ Py_READONLY](#c.Py_READONLY).
The 

`PY_AUDIT_READ` macro was renamed with the `Py_` prefix.
The new names are now always available.
Previously, these required `#include "structmember.h"`.
The header is still available and it provides the old names.### Member types[¶](#member-types)

[ PyMemberDef.type](#c.PyMemberDef.type) can be one of the following macros corresponding
to various C types.
When the member is accessed in Python, it will be converted to the
equivalent Python type.
When it is set from Python, it will be converted back to the C type.
If that is not possible, an exception such as 

[or](../library/exceptions.html#TypeError)

`TypeError`[is raised.](../library/exceptions.html#ValueError)

`ValueError`Unless marked (D), attributes defined this way cannot be deleted
using e.g. [ del](../reference/simple_stmts.html#del) or 

[.](../library/functions.html#delattr)

`delattr()`| Macro name | C type | Python type | 
|---|---|---|
| 
 | char | |
| 
 | short | |
| 
 | int | |
| 
 | long | |
| 
 | long long | |
| 
 | unsigned char | |
| 
 | unsigned int | |
| 
 | unsigned short | |
| 
 | unsigned long | |
| 
 | unsigned long long | |
| 
 | ||
| 
 | float | |
| 
 | double | |
| 
 | char (written as 0 or 1) | |
| 
 | const char* (*) | 
 | 
| 
 | const char[] (*) | 
 | 
| 
 | char (0-127) | 
 | 
| 
 | 
 | 

(*): Zero-terminated, UTF8-encoded C string. With

`Py_T_STRING`the C representation is a pointer; with`Py_T_STRING_INPLACE`the string is stored directly in the structure.(**): String of length 1. Only ASCII is accepted.

(RO): Implies

[.](#c.Py_READONLY)`Py_READONLY`(D): Can be deleted, in which case the pointer is set to

`NULL`. Reading a`NULL`pointer raises[.](../library/exceptions.html#AttributeError)`AttributeError`

Added in version 3.12: In previous versions, the macros were only available with
`#include "structmember.h"` and were named without the `Py_` prefix
(e.g. as `T_INT`).
The header is still available and contains the old names, along with
the following deprecated types:

- 
T_OBJECT[¶](#c.T_OBJECT)
- Like - `Py_T_OBJECT_EX`, but- `NULL`is converted to- `None`. This results in surprising behavior in Python: deleting the attribute effectively sets it to- `None`.

- 
T_NONE[¶](#c.T_NONE)
- Always - `None`. Must be used with- `Py_READONLY`

### Defining Getters and Setters[¶](#defining-getters-and-setters)

- 
type PyGetSetDef[¶](#c.PyGetSetDef)
- *Part of the*- [Stable ABI](stable.html#stable)(including all members).- Structure to define property-like access for a type. See also description of the - `PyTypeObject.tp_getset`- 
const char *name[¶](#c.PyGetSetDef.name)
- attribute name 
 - 
[setter](#c.setter)set[¶](#c.PyGetSetDef.set)
- Optional C function to set or delete the attribute. If - `NULL`, the attribute is read-only.
 - 
const char *doc[¶](#c.PyGetSetDef.doc)
- optional docstring 
 - 
void *closure[¶](#c.PyGetSetDef.closure)
- Optional user data pointer, providing additional data for getter and setter. 
 
- 
const char *name

- 
typedef [PyObject](#c.PyObject)*(*getter)([PyObject](#c.PyObject)*, void*)[¶](#c.getter)
- *Part of the*- [Stable ABI](stable.html#stable).- The - `get`function takes one- [PyObject](#c.PyObject)* parameter (the instance) and a user data pointer (the associated- `closure`):- It should return a new reference on success or - `NULL`with a set exception on failure.

- 
typedef int (*setter)([PyObject](#c.PyObject)*,[PyObject](#c.PyObject)*, void*)[¶](#c.setter)
- *Part of the*- [Stable ABI](stable.html#stable).- `set`functions take two- [PyObject](#c.PyObject)* parameters (the instance and the value to be set) and a user data pointer (the associated- `closure`):- In case the attribute should be deleted the second parameter is - `NULL`. Should return- `0`on success or- `-1`with a set exception on failure.